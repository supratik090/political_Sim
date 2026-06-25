package com.politicalsim.game;

import com.politicalsim.content.CardDefinition;
import com.politicalsim.content.CardDefinitionRepository;
import com.politicalsim.content.IssueOptionDefinition;
import com.politicalsim.content.MonthlyIssueDefinition;
import com.politicalsim.content.MonthlyIssueDefinitionRepository;
import com.politicalsim.content.NewsDefinition;
import com.politicalsim.content.NewsDefinitionRepository;
import com.politicalsim.content.NewsReactionDefinition;
import com.politicalsim.content.DefinitionCache;
import com.politicalsim.party.PartyRole;
import com.politicalsim.party.PartyState;
import com.politicalsim.party.PartyStats;
import com.politicalsim.party.ProjectState;
import com.politicalsim.party.BuildingProject;
import com.politicalsim.publicmood.PublicState;

import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.UUID;

@Service
public class RoundResolutionEngine {

    public static final List<RewardDefinition> REWARD_POOL = new java.util.concurrent.CopyOnWriteArrayList<>();

    static {
        loadRewardsFromClasspath();
    }

    private static void loadRewardsFromClasspath() {
        try {
            com.fasterxml.jackson.databind.ObjectMapper mapper = new com.fasterxml.jackson.databind.ObjectMapper();
            java.io.InputStream stream = RoundResolutionEngine.class.getResourceAsStream("/config/rewards.json");
            if (stream != null) {
                List<RewardDefinition> raw = mapper.readValue(stream, new com.fasterxml.jackson.core.type.TypeReference<List<RewardDefinition>>() {});
                REWARD_POOL.addAll(raw);
            } else {
                System.err.println("⚠️ rewards.json not found on classpath!");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.err.println("❌ Failed to parse rewards.json: " + e.getMessage());
        }
    }

    private final CardDefinitionRepository cardRepository;
    private final NewsDefinitionRepository newsRepository;
    private final MonthlyIssueDefinitionRepository issueRepository;

    private final CardPlayResolver cardPlayResolver;
    private final BiddingResolver biddingResolver;
    private final ProjectResolver projectResolver;
    private final ElectionResolver electionResolver;

    public RoundResolutionEngine(
            CardDefinitionRepository cardRepository,
            NewsDefinitionRepository newsRepository,
            MonthlyIssueDefinitionRepository issueRepository
    ) {
        this.cardRepository = cardRepository;
        this.newsRepository = newsRepository;
        this.issueRepository = issueRepository;
        this.cardPlayResolver = new CardPlayResolver(this);
        this.biddingResolver = new BiddingResolver(this);
        this.projectResolver = new ProjectResolver(this);
        this.electionResolver = new ElectionResolver(this);
    }

    public boolean resolveRound(GameSession session) {
        session.setLastElectionHeld(false);
        session.setLastElectionWinner(null);
        session.setLastElectionVoteShares(new java.util.LinkedHashMap<>());

        Map<String, PartyStats> beforeStats = new LinkedHashMap<>();
        Map<String, PartyStats> defeatedStartingStats = new LinkedHashMap<>();
        for (PartyState party : session.getParties()) {
            PartyStats start = session.getTurnStartStats().get(party.getId());
            if (start != null) {
                beforeStats.put(party.getId(), copyStats(start));
            } else {
                beforeStats.put(party.getId(), copyStats(party.getStats()));
            }
            if (party.getRole() == com.politicalsim.party.PartyRole.DEFEATED) {
                defeatedStartingStats.put(party.getId(), copyStats(party.getStats()));
            }
        }

        List<String> commentary = new ArrayList<>();
        List<String> resultLines = new ArrayList<>();

        // Trigger crisis from monthly news
        List<NewsDefinition> currentNewsList = getCurrentNews(session);
        if (currentNewsList != null && !currentNewsList.isEmpty()) {
            NewsDefinition news = currentNewsList.get(0);
            if (news.getCrisisTriggerKey() != null && !news.getCrisisTriggerKey().isBlank()) {
                if (session.getActiveCrisisKey() == null) {
                    session.setActiveCrisisKey(news.getCrisisTriggerKey());
                    session.setActiveCrisisName(news.getTitle());
                    session.setActiveCrisisDescription(news.getDescription());
                    session.setActiveCrisisTurnsLeft(news.getCrisisDuration() <= 0 ? 2 : news.getCrisisDuration());
                    commentary.add("🚨 STATE CRISIS TRIGGERED: " + news.getTitle() + " has thrown the state into a crisis! Active for " + session.getActiveCrisisTurnsLeft() + " turns.");
                }
            }
        }

        Map<String, Integer> supportPressure = initialSupportPressure(session);
        resolveDueDelayedEffects(session, supportPressure, commentary);
        
        // Log bids first (do NOT deduct yet)
        String biddingMetric = getBiddingMetricForTurn(session.getTurnNumber());
        for (RoundSubmission submission : session.getCurrentRoundSubmissions()) {
            PartyState actor = findParty(session, submission.getPartyId());
            if (actor.getRole() == com.politicalsim.party.PartyRole.DEFEATED) {
                continue;
            }
            int bid = submission.getBid();
            commentary.add("Bidding: " + actor.getName() + " bid " + bid + " " + biddingMetric + ".");
        }

        // Apply played rewards
        for (RoundSubmission submission : session.getCurrentRoundSubmissions()) {
            if (submission.getSelectedRewardKey() != null && !submission.getSelectedRewardKey().isBlank()) {
                PartyState actor = findParty(session, submission.getPartyId());
                if (actor.getRole() == com.politicalsim.party.PartyRole.DEFEATED) {
                    continue;
                }
                RewardDefinition rewardDef = REWARD_POOL.stream()
                        .filter(r -> r.key().equals(submission.getSelectedRewardKey()))
                        .findFirst().orElse(null);
                if (rewardDef != null) {
                    // Remove from inventory
                    List<HeldReward> held = session.getPartyHeldRewards().get(actor.getId());
                    if (held != null) {
                        held.removeIf(hr -> hr.getRewardKey().equals(submission.getSelectedRewardKey()));
                    }

                    // Apply reward effects to target
                    PartyState rTarget = actor;
                    if (rewardDef.requiresTarget() && submission.getRewardTargetPartyId() != null) {
                        rTarget = findParty(session, submission.getRewardTargetPartyId());
                    }
                    if (rTarget != actor && (rewardDef.coinsEffect() < 0 || rewardDef.moraleEffect() < 0 || rewardDef.corruptionEffect() > 0 || rewardDef.mediaEffect() < 0 || rewardDef.publicSupportEffect() < 0)) {
                        checkAndProcessPactViolation(session, actor, rTarget, "reward '" + rewardDef.name() + "'", commentary);
                    }
                    applyRewardEffect(session, rTarget, rewardDef, commentary);
                    String rewardEffects = formatRewardEffects(rewardDef);
                    commentary.add("🏆 Reward played: " + actor.getName() + " played reward '" + rewardDef.name() + "' on target " + rTarget.getName() + ". Effects: " + rewardEffects);
                    resultLines.add(actor.getName() + " played reward: " + rewardDef.name() + (rewardDef.requiresTarget() ? " on " + rTarget.getName() : ""));
                }
            }
        }

        boolean noConfidencePlayed = cardPlayResolver.resolveCardPlays(session, supportPressure, commentary, resultLines);
        biddingResolver.resolveBidding(session, biddingMetric, commentary);



        resolveActiveCrisis(session, supportPressure, commentary);
        projectResolver.resolveBuildingProjects(session, supportPressure, commentary);
        resolvePublicSupport(session, supportPressure, commentary);
        applyMonthlyStatDrift(session, commentary);
        applyHiddenMetricRules(session, commentary);

        // Restore stats for already defeated parties, and enforce support = 0
        for (PartyState party : session.getParties()) {
            if (party.getRole() == com.politicalsim.party.PartyRole.DEFEATED) {
                PartyStats startStats = defeatedStartingStats.get(party.getId());
                if (startStats != null) {
                    party.getStats().setCoins(startStats.getCoins());
                    party.getStats().setPartyMorale(startStats.getPartyMorale());
                    party.getStats().setCorruptionScore(startStats.getCorruptionScore());
                    party.getStats().setMediaImage(startStats.getMediaImage());
                }
                party.getStats().setPublicSupport(0);
            }
        }

        // Emergency Campaign Subsidy (Skip defeated parties)
        for (PartyState party : session.getParties()) {
            if (party.getRole() == com.politicalsim.party.PartyRole.DEFEATED || !party.isActive()) {
                continue;
            }
            if (party.getStats().getCoins() < 10) {
                party.getStats().setCoins(party.getStats().getCoins() + 15);
                commentary.add("Subsidy: " + party.getName() + " received an emergency campaign subsidy (+15 coins) because their reserves fell below 10.");
            }
        }

        // Clamp stats and compute deltas
        Map<String, Map<String, Integer>> deltas = new LinkedHashMap<>();
        for (PartyState party : session.getParties()) {
            clampStats(party.getStats());
            Map<String, Integer> partyDeltas = delta(beforeStats.get(party.getId()), party.getStats());
            deltas.put(party.getId(), partyDeltas);
        }

        // Check for party elimination (both Human and AI)
        for (PartyState party : session.getParties()) {
            if (!party.isActive() || party.getRole() == com.politicalsim.party.PartyRole.DEFEATED) {
                continue;
            }
            PartyStats stats = party.getStats();
            if (stats.getCoins() <= 0 || stats.getPartyMorale() < 10 || stats.getCorruptionScore() > 95 || stats.getPublicSupport() < 5) {
                party.setRole(com.politicalsim.party.PartyRole.DEFEATED);
                party.setActive(false);
                int supportToMove = stats.getPublicSupport();
                stats.setPublicSupport(0);
                session.getPublicState().setUndecidedSupport(session.getPublicState().getUndecidedSupport() + supportToMove);

                if (session.getPlayerPartyIds().contains(party.getId())) {
                    session.setStatus(GameStatus.DEFEAT);
                    commentary.add("❌ DEFEAT: Your party " + party.getName() + " has been politically eliminated due to critical resource failure (Coins: " + stats.getCoins() + ", Morale: " + stats.getPartyMorale() + ", Corruption: " + stats.getCorruptionScore() + ", Support: " + stats.getPublicSupport() + "%).");
                    resultLines.add("Defeat: Your party was eliminated.");
                } else {
                    commentary.add("💀 ELIMINATED: AI Party " + party.getName() + " has been politically eliminated and is no longer active in this campaign.");
                    resultLines.add("Eliminated: AI Party " + party.getName() + " was eliminated.");
                }
            }
        }

        // Check if only the human player is left active (all other 2 parties are defeated)
        if (session.getStatus() == GameStatus.ACTIVE) {
            int activePartiesCount = 0;
            PartyState activeHumanParty = null;
            for (PartyState party : session.getParties()) {
                if (party.isActive() && party.getRole() != com.politicalsim.party.PartyRole.DEFEATED) {
                    activePartiesCount++;
                    if (session.getPlayerPartyIds().contains(party.getId())) {
                        activeHumanParty = party;
                    }
                }
            }
            if (activePartiesCount == 1 && activeHumanParty != null) {
                session.setStatus(GameStatus.VICTORY);
                commentary.add("🏆 VICTORY: All opponent parties have been defeated! Your party " + activeHumanParty.getName() + " wins the campaign by political survival.");
                resultLines.add("Victory: All opponent parties defeated.");
            }
        }

        normalizePublicSupport(session);

        projectResolver.logProjectFundingActivity(session, commentary, resultLines);

        // 2. Log Coin Movement from round events
        commentary.add("💰 Turn Coin Movements:");
        for (PartyState party : session.getParties()) {
            if (party.getRole() == com.politicalsim.party.PartyRole.DEFEATED) {
                commentary.add("  - " + party.getName() + " is defeated (Coins: 0).");
                continue;
            }
            if (!party.isActive()) {
                continue;
            }
            int oldCoins = beforeStats.get(party.getId()).getCoins();
            int newCoins = party.getStats().getCoins();
            int diff = newCoins - oldCoins;
            if (diff > 0) {
                commentary.add("  - " + party.getName() + " had a net change of +" + diff + " coins this round (Current: " + newCoins + ").");
            } else if (diff < 0) {
                commentary.add("  - " + party.getName() + " had a net change of -" + Math.abs(diff) + " coins this round (Current: " + newCoins + ").");
            } else {
                commentary.add("  - " + party.getName() + " had no net coin change this round (Current: " + newCoins + ").");
            }
        }

        // 3. Log Held Rewards
        commentary.add("🎒 Current Held Rewards:");
        for (PartyState party : session.getParties()) {
            if (party.getRole() == com.politicalsim.party.PartyRole.DEFEATED || !party.isActive()) {
                continue;
            }
            List<HeldReward> held = session.getPartyHeldRewards().get(party.getId());
            if (held != null && !held.isEmpty()) {
                List<String> names = held.stream().map(HeldReward::getName).toList();
                String msg = party.getName() + " is holding reward: " + String.join(", ", names);
                commentary.add("  - " + msg);
                resultLines.add(msg);
            } else {
                commentary.add("  - " + party.getName() + " is holding reward: None");
            }
        }

        // 4. Log Next Round Strategic Outlook for AI players
        commentary.add("🔮 Next Round Strategic Outlook:");
        for (PartyState party : session.getParties()) {
            if (party.getRole() == com.politicalsim.party.PartyRole.DEFEATED || !party.isActive()) {
                continue;
            }
            if (party.getControllerType() != com.politicalsim.party.ControllerType.COMPUTER) {
                continue;
            }
            PartyStats stats = party.getStats();
            List<String> needs = new ArrayList<>();
            if (stats.getCoins() < 100) {
                needs.add("Coins (current: " + stats.getCoins() + " < 100)");
            }
            if (stats.getPartyMorale() < 50) {
                needs.add("Morale (current: " + stats.getPartyMorale() + " < 50)");
            }
            if (stats.getCorruptionScore() >= 50) {
                needs.add("Corruption Reduction (current: " + stats.getCorruptionScore() + "% >= 50%)");
            }
            if (stats.getMediaImage() < 50) {
                needs.add("Media Image (current: " + stats.getMediaImage() + " < 50)");
            }
            if (stats.getPublicSupport() < 25) {
                needs.add("Voter Support (current: " + stats.getPublicSupport() + "% < 25%)");
            }
            
            String priorities;
            if (!needs.isEmpty()) {
                priorities = "needs to focus on restoring " + String.join(", ", needs);
            } else {
                priorities = "focus on offensive campaign maneuvers / consolidating lead";
            }
            commentary.add("  - " + party.getName() + " next round priorities: " + priorities + ".");
        }

        session.setLastRoundSubmissions(new ArrayList<>(session.getCurrentRoundSubmissions()));
        session.setLastMetricDeltas(deltas);
        session.setLastRoundCommentary(commentary);
        session.setLastResults(resultLines);
        return noConfidencePlayed;
    }

    public String getBiddingMetricForTurn(int turnNumber) {
        int cycleTurn = ((turnNumber - 1) % 5) + 1;
        return switch (cycleTurn) {
            case 1 -> "COINS";
            case 2 -> "CORRUPTION";
            case 3 -> "MORALE";
            case 4 -> "MEDIA";
            case 5 -> "PUBLIC_SUPPORT";
            default -> "COINS";
        };
    }

    public int getStatValue(PartyState party, String metric) {
        return switch (metric.toUpperCase()) {
            case "COINS" -> party.getStats().getCoins();
            case "CORRUPTION" -> party.getStats().getCorruptionScore();
            case "MORALE" -> party.getStats().getPartyMorale();
            case "MEDIA" -> party.getStats().getMediaImage();
            case "PUBLIC_SUPPORT" -> party.getStats().getPublicSupport();
            default -> 0;
        };
    }

    public void deductStatValue(PartyState party, String metric, int value) {
        switch (metric.toUpperCase()) {
            case "COINS" -> party.getStats().setCoins(Math.max(0, party.getStats().getCoins() - value));
            case "CORRUPTION" -> party.getStats().setCorruptionScore(clamp(party.getStats().getCorruptionScore() + value));
            case "MORALE" -> party.getStats().setPartyMorale(Math.max(0, party.getStats().getPartyMorale() - value));
            case "MEDIA" -> party.getStats().setMediaImage(Math.max(0, party.getStats().getMediaImage() - value));
            case "PUBLIC_SUPPORT" -> party.getStats().setPublicSupport(Math.max(0, party.getStats().getPublicSupport() - value));
        }
    }

    public RewardDefinition selectRandomReward(GameSession session) {
        List<String> used = session.getUsedRewardKeys();
        if (used == null) {
            used = new ArrayList<>();
        }
        if (used.size() >= REWARD_POOL.size() || (session.getTurnNumber() > 60 && (session.getTurnNumber() - 1) % 60 == 0)) {
            used.clear();
        }
        List<RewardDefinition> available = new ArrayList<>();
        for (RewardDefinition reward : REWARD_POOL) {
            if (!used.contains(reward.key())) {
                available.add(reward);
            }
        }
        if (available.isEmpty()) {
            available = REWARD_POOL;
        }
        RewardDefinition chosen = available.get(new Random().nextInt(available.size()));
        used.add(chosen.key());
        session.setUsedRewardKeys(used);
        return chosen;
    }

    RewardDefinition getReward(String key) {
        return REWARD_POOL.stream()
            .filter(r -> r.key().equals(key))
            .findFirst().orElse(null);
    }

    void applyRewardEffect(GameSession session, PartyState target, RewardDefinition reward, List<String> commentary) {
        PartyStats stats = target.getStats();
        stats.setCoins(stats.getCoins() + reward.coinsEffect());
        stats.setPartyMorale(stats.getPartyMorale() + reward.moraleEffect());
        stats.setCorruptionScore(stats.getCorruptionScore() + reward.corruptionEffect());
        stats.setMediaImage(stats.getMediaImage() + reward.mediaEffect());
        
        int supportEffect = reward.publicSupportEffect();
        int actualSupportChange = 0;
        if (supportEffect != 0) {
            if (supportEffect > 0) {
                // Proportional deduction from others
                int totalOtherSupport = 0;
                for (PartyState p : session.getParties()) {
                    if (!p.getId().equals(target.getId())) {
                        totalOtherSupport += p.getStats().getPublicSupport();
                    }
                }
                
                if (totalOtherSupport > 0) {
                    int distributedDeduction = 0;
                    List<PartyState> otherParties = new ArrayList<>();
                    for (PartyState p : session.getParties()) {
                        if (!p.getId().equals(target.getId())) {
                            otherParties.add(p);
                        }
                    }
                    
                    // Sort other parties by support descending to handle rounding correctly
                    otherParties.sort(Comparator.comparingInt((PartyState p) -> p.getStats().getPublicSupport()).reversed());
                    
                    for (int i = 0; i < otherParties.size(); i++) {
                        PartyState p = otherParties.get(i);
                        int currentSupport = p.getStats().getPublicSupport();
                        int deduct;
                        if (i == otherParties.size() - 1) {
                            deduct = supportEffect - distributedDeduction;
                        } else {
                            deduct = (int) Math.round((double) currentSupport * supportEffect / totalOtherSupport);
                        }
                        deduct = Math.min(currentSupport, Math.max(0, deduct));
                        p.getStats().setPublicSupport(currentSupport - deduct);
                        distributedDeduction += deduct;
                    }
                    stats.setPublicSupport(stats.getPublicSupport() + distributedDeduction);
                    actualSupportChange = distributedDeduction;
                } else {
                    stats.setPublicSupport(stats.getPublicSupport() + supportEffect);
                    actualSupportChange = supportEffect;
                }
            } else {
                // Negative support effect, subtract from target directly
                int originalSupport = stats.getPublicSupport();
                stats.setPublicSupport(Math.max(0, originalSupport + supportEffect));
                actualSupportChange = stats.getPublicSupport() - originalSupport;
            }
        }
        
        List<String> changes = new ArrayList<>();
        if (reward.coinsEffect() != 0) changes.add("coins " + signed(reward.coinsEffect()));
        if (reward.moraleEffect() != 0) changes.add("morale " + signed(reward.moraleEffect()));
        if (reward.corruptionEffect() != 0) changes.add("corruption " + signed(reward.corruptionEffect()));
        if (reward.mediaEffect() != 0) changes.add("media " + signed(reward.mediaEffect()));
        if (actualSupportChange != 0) changes.add("public support " + signed(actualSupportChange));
        
        commentary.add("Reward effect: " + target.getName() + " stats adjusted: " + String.join(", ", changes) + ".");
    }

    void applyCard(GameSession session, PartyState actor, PartyState opponent, CardDefinition card,
                   Map<String, Integer> supportPressure, List<String> commentary) {
        int cost = card.getCost();
        if (session.getActiveCrisisKey() != null) {
            if ("drought_crisis".equals(session.getActiveCrisisKey())) {
                if ("positive_service".equals(card.getCategory()) || card.getCardKey().contains("farmer") || card.getCardKey().contains("rural") || card.getCardKey().contains("welfare")) {
                    cost += 5;
                    commentary.add("Crisis Surcharge: " + actor.getName() + " paid +5 coins to play welfare card during Drought.");
                }
            } else if ("industrial_strike".equals(session.getActiveCrisisKey())) {
                cost += 2;
                commentary.add("Crisis Surcharge: " + actor.getName() + " paid +2 coins to play card during strike.");
            }
        }
        actor.getStats().setCoins(Math.max(0, actor.getStats().getCoins() - cost));

        // Mitigation of crisis duration via card plays
        if (session.getActiveCrisisKey() != null) {
            if ("drought_crisis".equals(session.getActiveCrisisKey()) && "positive_service".equals(card.getCategory())) {
                session.setActiveCrisisTurnsLeft(Math.max(1, session.getActiveCrisisTurnsLeft() - 1));
                commentary.add(actor.getName() + " played a Welfare card, helping mitigate the Drought crisis (Shortened duration by 1 turn).");
            } else if ("industrial_strike".equals(session.getActiveCrisisKey()) && "governance".equals(card.getCategory())) {
                session.setActiveCrisisTurnsLeft(Math.max(1, session.getActiveCrisisTurnsLeft() - 1));
                commentary.add(actor.getName() + " played a Governance card, helping negotiate the strike resolution (Shortened duration by 1 turn).");
            } else if ("scam_panic".equals(session.getActiveCrisisKey()) && ("defensive_counter".equals(card.getCategory()) || card.getCardKey().contains("reform"))) {
                session.setActiveCrisisTurnsLeft(Math.max(1, session.getActiveCrisisTurnsLeft() - 1));
                commentary.add(actor.getName() + " addressed transparency, calming public panic around the scam (Shortened duration by 1 turn).");
            }
        }

        Map<String, Object> selfEffects = new LinkedHashMap<>(partyEffect(card.getVisibleEffects(), "selfParty"));
        if (selfEffects.containsKey("coins")) {
            int effectCoins = intValue(selfEffects.get("coins"));
            if (effectCoins < 0) {
                // The cost was already deducted, so we offset the negative coins effect to prevent double-deduction
                int extraLoss = effectCoins + cost;
                if (extraLoss > 0) {
                    extraLoss = 0; // Don't let it become positive
                }
                selfEffects.put("coins", extraLoss);
            }
        }

        applyEffects(session, actor, selfEffects, supportPressure);
        if (opponent != null) {
            Map<String, Object> oppEffects = partyEffect(card.getVisibleEffects(), "opponentParty");
            if (oppEffects != null && !oppEffects.isEmpty()) {
                int c = intValue(oppEffects.get("coins"));
                int m = intValue(oppEffects.get("partyMorale"));
                int s = intValue(oppEffects.get("publicSupport"));
                int med = intValue(oppEffects.get("mediaImage"));
                int corr = intValue(oppEffects.get("corruptionScore"));
                if (c < 0 || m < 0 || s < 0 || med < 0 || corr > 0) {
                    checkAndProcessPactViolation(session, actor, opponent, "card '" + card.getName() + "'", commentary);
                }
            }
            applyEffects(session, opponent, oppEffects, supportPressure);
            
            // Record grudge: opponent holds a grudge against actor
            Map<String, Map<String, Integer>> grudges = session.getGrudges();
            Map<String, Integer> opponentGrudges = grudges.computeIfAbsent(opponent.getId(), k -> new LinkedHashMap<>());
            opponentGrudges.put(actor.getId(), opponentGrudges.getOrDefault(actor.getId(), 0) + 1);
        }
        applyRiskRoll(session, actor, opponent, card, supportPressure, commentary);
    }

    @SuppressWarnings("unchecked")
    private Map<String, Object> partyEffect(Map<String, Object> effects, String key) {
        if (effects == null) {
            return Map.of();
        }
        Object value = effects.get(key);
        if (value == null && "playerParty".equals(key)) {
            value = effects.get("selfParty");
        } else if (value == null && "selfParty".equals(key)) {
            value = effects.get("playerParty");
        }
        if (value instanceof Map<?, ?> map) {
            return (Map<String, Object>) map;
        }
        return Map.of();
    }

    int resolveNewsReactions(GameSession session, PartyState actor, Map<String, String> selectedReactions,
                             Map<String, Integer> supportPressure, List<String> commentary) {
        int coinAward = 0;
        List<NewsDefinition> newsItems = getCurrentNews(session);
        for (Map.Entry<String, String> entry : selectedReactions.entrySet()) {
            NewsReactionDefinition reaction = findReaction(newsItems, entry.getKey(), entry.getValue());
            NewsDefinition news = findNews(newsItems, entry.getKey());
            if (reaction == null) {
                coinAward += 1;
                continue;
            }
            applyEffects(session, actor, partyEffect(reaction.getEffects(), "playerParty"), supportPressure);
            applyReactionRisk(session, actor, reaction, supportPressure, commentary);

            // Adjust active crisis duration based on Government reactions
            if (session.getActiveCrisisKey() != null && news != null && news.getCrisisTriggerKey() != null) {
                PartyState gov = session.getGovernmentParty();
                if (gov != null && actor.getId().equals(gov.getId())) {
                    String reactionKey = reaction.getReactionKey();
                    if (reactionKey != null) {
                        if (reactionKey.contains("no_comment")) {
                            session.setActiveCrisisTurnsLeft(session.getActiveCrisisTurnsLeft() + 1);
                            commentary.add("Negligence Surcharge: Government chose 'No Comment', extending the crisis by +1 turn!");
                        } else if (reactionKey.contains("relief") || reactionKey.contains("suspend") || reactionKey.contains("disbursement") || reactionKey.contains("reform")) {
                            session.setActiveCrisisTurnsLeft(Math.max(1, session.getActiveCrisisTurnsLeft() - 1));
                            commentary.add("Proactive Mitigation: Government responded with immediate policy action, shortening the crisis by -1 turn!");
                        }
                    }
                }
            }

            if (news != null) {
                scheduleNewsDelayedEffects(session, actor, news, reaction, commentary);
                Map<String, Object> selfEff = partyEffect(reaction.getEffects(), "playerParty");
                commentary.add("💬 News Handling: " + actor.getName() + " responded to news '" + news.getTitle() + "' by choosing option '" + reaction.getText() + "'. Effects: " + formatEffectsMap(selfEff));
            }
            coinAward += Math.max(0, Math.min(10, 2 + reaction.getWeight()));
        }
        coinAward = Math.max(0, Math.min(10, coinAward));
        actor.getStats().setCoins(actor.getStats().getCoins() + coinAward);
        return coinAward;
    }

    private NewsReactionDefinition findReaction(List<NewsDefinition> newsItems, String newsKey, String reactionKey) {
        return newsItems.stream()
                .filter(news -> news.getNewsKey().equals(newsKey))
                .flatMap(news -> news.getReactionOptions().stream())
                .filter(reaction -> reaction.getReactionKey().equals(reactionKey))
                .findFirst()
                .orElse(null);
    }

    private NewsDefinition findNews(List<NewsDefinition> newsItems, String newsKey) {
        return newsItems.stream()
                .filter(news -> news.getNewsKey().equals(newsKey))
                .findFirst()
                .orElse(null);
    }

    void resolveIssueChoice(GameSession session, PartyState actor, RoundSubmission submission,
                            Map<String, Integer> supportPressure, List<String> commentary) {
        if (submission.getIssueKey() == null || submission.getIssueOptionKey() == null) {
            return;
        }
        MonthlyIssueDefinition issue = getIssueByKey(session, actor, submission.getIssueKey());
        if (issue == null) {
            return;
        }
        IssueOptionDefinition option = findIssueOption(issue, submission.getIssueOptionKey());
        if (option == null) {
            return;
        }
        applyEffects(session, actor, partyEffect(option.getEffects(), "selfParty"), supportPressure);
        applyIssueRisk(session, actor, option, supportPressure, commentary);
        commentary.add("💬 Issue Handling: " + actor.getName() + " resolved monthly issue '" + issue.getTitle() + "' by choosing: '" + option.getText() + "'. Effects: " + formatEffectsObject(option.getEffects(), "selfParty"));
        scheduleIssueDelayedEffects(session, actor, issue, option, commentary);
    }

    private void applyIssueRisk(GameSession session, PartyState actor, IssueOptionDefinition option,
                                Map<String, Integer> supportPressure, List<String> commentary) {
        int chance = intValue(option.getRisk().get("chance"));
        if (chance <= 0 || !riskHit(session, "issue:" + actor.getId() + ":" + option.getOptionKey(), chance)) {
            return;
        }
        applyEffects(session, actor, riskEffect(option.getRisk(), "selfParty"), supportPressure);
        Object badOutcome = option.getRisk().get("badOutcome");
        commentary.add("Surprise: " + actor.getName() + "'s issue response backfired"
                + (badOutcome == null ? "." : ": " + badOutcome + "."));
    }

    private void resolveDueDelayedEffects(GameSession session, Map<String, Integer> supportPressure, List<String> commentary) {
        if (session.getDelayedEffects() == null || session.getDelayedEffects().isEmpty()) {
            return;
        }

        List<DelayedEffect> remaining = new ArrayList<>();
        for (DelayedEffect delayedEffect : session.getDelayedEffects()) {
            if (isLegacyAutoCardDelayedEffect(session, delayedEffect)) {
                commentary.add("Legacy delayed card result cleared: " + delayedEffect.getSourceName()
                        + " for " + delayedEffect.getTargetPartyName() + ".");
                continue;
            }
            if (delayedEffect.getDueTurnNumber() > session.getTurnNumber()) {
                remaining.add(delayedEffect);
                continue;
            }
            PartyState target = findParty(session, delayedEffect.getTargetPartyId());
            if (delayedEffect.getChance() < 100
                    && !riskHit(session, "delayed:" + delayedEffect.getId(), delayedEffect.getChance())) {
                commentary.add("Delayed result did not materialize: " + delayedEffect.getSourceName() + " for " + target.getName() + ".");
                continue;
            }
            applyEffects(session, target, delayedEffect.getEffects(), supportPressure);
            commentary.add("⏰ Delayed result: " + (delayedEffect.getCommentary() == null
                    ? delayedEffect.getSourceName() + " affected " + target.getName()
                    : delayedEffect.getCommentary()) + " Effects: " + formatEffectsMap(delayedEffect.getEffects()));
        }
        session.setDelayedEffects(remaining);
    }

    private boolean isLegacyAutoCardDelayedEffect(GameSession session, DelayedEffect delayedEffect) {
        if (!"card".equals(delayedEffect.getSourceType())) {
            return false;
        }
        return getCardsForSession(session).stream()
                .filter(card -> card.getCardKey().equals(delayedEffect.getSourceKey()))
                .noneMatch(card -> {
                    Object scheduled = card.getVisibleEffects().get("scheduled");
                    return scheduled instanceof List<?> list && !list.isEmpty();
                });
    }

    void scheduleCardDelayedEffects(GameSession session, PartyState actor, PartyState opponent,
                                    CardDefinition card, List<String> commentary) {
        Object scheduled = card.getVisibleEffects().get("scheduled");
        if (scheduled instanceof List<?> list && !list.isEmpty()) {
            for (Object item : list) {
                if (item instanceof Map<?, ?> scheduledMap) {
                    schedulePartyEffectsFromMap(session, actor, opponent, "card", card.getCardKey(), card.getName(),
                            scheduledMap, commentary);
                }
            }
            return;
        }
    }

    private void scheduleIssueDelayedEffects(GameSession session, PartyState actor, MonthlyIssueDefinition issue,
                                             IssueOptionDefinition option, List<String> commentary) {
        if (option.getDelayedEffects() == null) {
            return;
        }
        for (Map<String, Object> delayedEffect : option.getDelayedEffects()) {
            scheduleDelayedEffect(session, actor, "issue", issue.getIssueKey(), issue.getTitle(),
                    partyEffectFromEffectsObject(delayedEffect.get("effects"), "selfParty"),
                    intValue(delayedEffect.get("minTurns")),
                    intValue(delayedEffect.get("maxTurns")),
                    intValueOrDefault(delayedEffect.get("chance"), 100),
                    stringValue(delayedEffect.get("commentary"), issue.getTitle() + " has delayed consequences."),
                    commentary);
        }
    }

    private void scheduleNewsDelayedEffects(GameSession session, PartyState actor, NewsDefinition news,
                                            NewsReactionDefinition reaction, List<String> commentary) {
        Object delayed = reaction.getHiddenEffects().get("delayedEffects");
        if (!(delayed instanceof List<?> list)) {
            return;
        }
        for (Object item : list) {
            if (item instanceof Map<?, ?> delayedMap) {
                scheduleDelayedEffect(session, actor, "news", news.getNewsKey(), news.getTitle(),
                        partyEffectFromEffectsObject(delayedMap.get("effects"), "playerParty"),
                        intValue(delayedMap.get("minTurns")),
                        intValue(delayedMap.get("maxTurns")),
                        intValueOrDefault(delayedMap.get("chance"), 100),
                        stringValue(delayedMap.get("commentary"), news.getTitle() + " has delayed public reaction."),
                        commentary);
            }
        }
    }

    private void schedulePartyEffectsFromMap(GameSession session, PartyState actor, PartyState opponent,
                                             String sourceType, String sourceKey, String sourceName, Map<?, ?> delayedMap, List<String> commentary) {
        Object timingObject = delayedMap.get("timing");
        Map<?, ?> timing = timingObject instanceof Map<?, ?> map ? map : Map.of();
        int minTurns = intValue(timing.get("minTurns"));
        int maxTurns = intValue(timing.get("maxTurns"));
        int chance = intValueOrDefault(delayedMap.get("chance"), 100);
        Object effects = delayedMap.get("effects");
        scheduleDelayedEffect(session, actor, sourceType, sourceKey, sourceName,
                partyEffectFromEffectsObject(effects, "selfParty"), minTurns, maxTurns, chance,
                sourceName + " has delayed impact for " + actor.getName(), commentary);
        if (opponent != null) {
            scheduleDelayedEffect(session, opponent, sourceType, sourceKey, sourceName,
                    partyEffectFromEffectsObject(effects, "opponentParty"), minTurns, maxTurns, chance,
                    sourceName + " has delayed impact on " + opponent.getName(), commentary);
        }
    }

    private void scheduleDelayedEffect(GameSession session, PartyState target, String sourceType, String sourceKey,
                                       String sourceName, Map<String, Object> effects, int minTurns, int maxTurns, int chance,
                                       String delayedCommentary, List<String> commentary) {
        if (effects == null || effects.isEmpty()) {
            return;
        }
        int dueInTurns = deterministicDelay(session, sourceType + ":" + sourceKey + ":" + target.getId(), minTurns, maxTurns);
        DelayedEffect delayedEffect = new DelayedEffect();
        delayedEffect.setId(UUID.randomUUID().toString());
        delayedEffect.setDueTurnNumber(session.getTurnNumber() + dueInTurns);
        delayedEffect.setSourceType(sourceType);
        delayedEffect.setSourceKey(sourceKey);
        delayedEffect.setSourceName(sourceName);
        delayedEffect.setTargetPartyId(target.getId());
        delayedEffect.setTargetPartyName(target.getName());
        delayedEffect.setChance(chance <= 0 ? 100 : Math.min(100, chance));
        delayedEffect.setEffects(new LinkedHashMap<>(effects));
        delayedEffect.setCommentary(delayedCommentary);
        if (session.getDelayedEffects() == null) {
            session.setDelayedEffects(new ArrayList<>());
        }
        session.getDelayedEffects().add(delayedEffect);
        commentary.add("Delayed effect scheduled: " + sourceName + " may affect " + target.getName()
                + " in " + dueInTurns + " turn(s).");
    }

    private int deterministicDelay(GameSession session, String key, int minTurns, int maxTurns) {
        int min = Math.max(1, minTurns <= 0 ? 1 : minTurns);
        int max = Math.max(min, maxTurns <= 0 ? min : maxTurns);
        int spread = max - min + 1;
        return min + new Random((session.getId() + ":" + session.getTurnNumber() + ":" + key).hashCode()).nextInt(spread);
    }

    private void applyEffects(GameSession session, PartyState party, Map<String, Object> effects, Map<String, Integer> supportPressure) {
        applyPartyEffectsWithoutSupport(session, party.getStats(), effects);
        supportPressure.computeIfPresent(party.getId(), (id, value) -> value + intValue(effects.get("publicSupport")));
    }

    private void applyPartyEffectsWithoutSupport(GameSession session, PartyStats stats, Map<String, Object> effects) {
        stats.setCoins(stats.getCoins() + intValue(effects.get("coins")));
        stats.setPartyMorale(stats.getPartyMorale() + intValue(effects.get("partyMorale")));
        
        int corruptionVal = intValue(effects.get("corruptionScore"));
        int mediaVal = intValue(effects.get("mediaImage"));
        
        if (session != null && "scam_panic".equals(session.getActiveCrisisKey())) {
            if (corruptionVal > 0) {
                corruptionVal *= 2;
            }
            if (mediaVal < 0) {
                mediaVal *= 2;
            }
        }
        
        stats.setCorruptionScore(stats.getCorruptionScore() + corruptionVal);
        stats.setMediaImage(stats.getMediaImage() + mediaVal);
    }

    private void applyRiskRoll(GameSession session, PartyState actor, PartyState opponent, CardDefinition card,
                               Map<String, Integer> supportPressure, List<String> commentary) {
        int chance = intValue(card.getRiskRoll().get("chance"));
        if (chance <= 0 || !riskHit(session, "card:" + actor.getId() + ":" + card.getCardKey(), chance)) {
            return;
        }
        applyEffects(session, actor, riskEffect(card.getRiskRoll(), "selfParty"), supportPressure);
        if (opponent != null) {
            applyEffects(session, opponent, riskEffect(card.getRiskRoll(), "opponentParty"), supportPressure);
        }
        Object badOutcome = card.getRiskRoll().get("badOutcome");
        commentary.add("Surprise: " + actor.getName() + "'s " + card.getName() + " had a backlash"
                + (badOutcome == null ? "." : ": " + badOutcome + "."));
    }

    private void applyReactionRisk(GameSession session, PartyState actor, NewsReactionDefinition reaction,
                                   Map<String, Integer> supportPressure, List<String> commentary) {
        int chance = intValue(reaction.getRisk().get("chance"));
        if (chance <= 0 || !riskHit(session, "news:" + actor.getId() + ":" + reaction.getReactionKey(), chance)) {
            return;
        }
        applyEffects(session, actor, riskEffect(reaction.getRisk(), "playerParty"), supportPressure);
        Object badOutcome = reaction.getRisk().get("badOutcome");
        commentary.add("Surprise: " + actor.getName() + "'s news response backfired"
                + (badOutcome == null ? "." : ": " + badOutcome + "."));
    }

    private boolean riskHit(GameSession session, String key, int chance) {
        long seed = (session.getId() + ":" + session.getTurnNumber() + ":" + key).hashCode();
        return new Random(seed).nextInt(100) < chance;
    }

    @SuppressWarnings("unchecked")
    private Map<String, Object> riskEffect(Map<String, Object> risk, String key) {
        Object effects = risk.get("effects");
        if (effects instanceof Map<?, ?> map) {
            return partyEffect((Map<String, Object>) map, key);
        }
        return Map.of();
    }

    @SuppressWarnings("unchecked")
    private Map<String, Object> partyEffectFromEffectsObject(Object effects, String key) {
        if (effects instanceof Map<?, ?> map) {
            Object partyEffects = map.get(key);
            if (partyEffects == null && "playerParty".equals(key)) {
                partyEffects = map.get("selfParty");
            } else if (partyEffects == null && "selfParty".equals(key)) {
                partyEffects = map.get("playerParty");
            }
            if (partyEffects instanceof Map<?, ?> partyMap) {
                return (Map<String, Object>) partyMap;
            }
        }
        return Map.of();
    }

    private Map<String, Integer> initialSupportPressure(GameSession session) {
        Map<String, Integer> supportPressure = new LinkedHashMap<>();
        for (PartyState party : session.getParties()) {
            supportPressure.put(party.getId(), 0);
        }
        return supportPressure;
    }

    private void resolvePublicSupport(GameSession session, Map<String, Integer> supportPressure, List<String> commentary) {
        // Apply ongoing support drag from corruption: more corruption leads to negative support pressure
        for (PartyState party : session.getParties()) {
            int corruption = party.getStats().getCorruptionScore();
            if (corruption > 30) {
                int drag = -((corruption - 10) / 20); // -1 for >30, -2 for >50, -3 for >70, -4 for >90
                if (drag < 0) {
                    supportPressure.put(party.getId(), supportPressure.getOrDefault(party.getId(), 0) + drag);
                    commentary.add("Corruption Drag: " + party.getName() + " suffered support pressure of " + drag + " due to corruption (Score: " + corruption + ").");
                }
            }
        }

        normalizePublicSupport(session);
        int floatingVoters = session.getPublicState().getUndecidedSupport();

        for (PartyState party : session.getParties()) {
            int pressure = supportPressure.getOrDefault(party.getId(), 0);
            if (pressure >= 0) {
                continue;
            }
            int release = Math.min(party.getStats().getPublicSupport(), dampenSupportMove(Math.abs(pressure)));
            if (release > 0) {
                party.getStats().setPublicSupport(party.getStats().getPublicSupport() - release);
                floatingVoters += release;
                commentary.add(party.getName() + " lost " + release + "% support after public pressure.");
            }
        }

        List<PartyState> gainers = session.getParties().stream()
                .filter(party -> supportPressure.getOrDefault(party.getId(), 0) > 0)
                .sorted(Comparator.comparingInt((PartyState party) -> supportPressure.getOrDefault(party.getId(), 0)).reversed())
                .toList();
        for (PartyState party : gainers) {
            int pressure = supportPressure.getOrDefault(party.getId(), 0);
            if (floatingVoters <= 0) {
                continue;
            }
            int gain = Math.min(floatingVoters, dampenSupportGain(pressure));
            if (gain > 0) {
                party.getStats().setPublicSupport(party.getStats().getPublicSupport() + gain);
                floatingVoters -= gain;
                commentary.add(party.getName() + " gained " + gain + "% support from shifting voters.");
            }
        }

        session.getPublicState().setUndecidedSupport(floatingVoters);
        normalizePublicSupport(session);
        updatePublicMood(session, supportPressure);
    }

    private int dampenSupportMove(int pressure) {
        if (pressure <= 0) {
            return 0;
        }
        return Math.min(6, Math.max(1, (pressure + 1) / 2));
    }

    private int dampenSupportGain(int pressure) {
        if (pressure <= 0) {
            return 0;
        }
        return Math.min(5, Math.max(1, (pressure + 1) / 2));
    }

    private void applyMonthlyStatDrift(GameSession session, List<String> commentary) {
        for (PartyState party : session.getParties()) {
            PartyStats stats = party.getStats();
            int moraleDrift = reputationDrift(stats.getPartyMorale(), 90, 75, 25, 5, 3, 2);
            int mediaDrift = reputationDrift(stats.getMediaImage(), 90, 75, 25, 6, 3, 1);
            if (stats.getCorruptionScore() >= 70) {
                mediaDrift -= 2;
            }
            if (party.getRole() == PartyRole.GOVERNMENT && stats.getPublicSupport() < 35) {
                moraleDrift -= 1;
            }
            if (moraleDrift == 0 && mediaDrift == 0) {
                continue;
            }
            stats.setPartyMorale(stats.getPartyMorale() + moraleDrift);
            stats.setMediaImage(stats.getMediaImage() + mediaDrift);
            commentary.add(party.getName() + " faced monthly reputation drift: morale "
                    + signed(moraleDrift) + ", media " + signed(mediaDrift) + ".");
        }
    }

    private void applyHiddenMetricRules(GameSession session, List<String> commentary) {
        if (session.getFiredHiddenRuleKeysByParty() == null) {
            session.setFiredHiddenRuleKeysByParty(new LinkedHashMap<>());
        }

        for (PartyState party : session.getParties()) {
            List<String> firedRules = session.getFiredHiddenRuleKeysByParty()
                    .computeIfAbsent(party.getId(), id -> new ArrayList<>());
            for (HiddenMetricRule rule : hiddenMetricRules()) {
                if (firedRules.contains(rule.key()) || !hiddenRuleMatches(rule.key(), party.getStats())) {
                    continue;
                }
                applyHiddenRuleEffect(party.getStats(), rule);
                firedRules.add(rule.key());
                
                List<String> ruleEffects = new ArrayList<>();
                if (rule.coins() != 0) ruleEffects.add("💰 " + (rule.coins() > 0 ? "+" : "") + rule.coins() + " Coins");
                if (rule.partyMorale() != 0) ruleEffects.add("✊ " + (rule.partyMorale() > 0 ? "+" : "") + rule.partyMorale() + " Morale");
                if (rule.corruptionScore() != 0) ruleEffects.add("⚖️ " + (rule.corruptionScore() > 0 ? "+" : "") + rule.corruptionScore() + "% Corruption");
                if (rule.mediaImage() != 0) ruleEffects.add("📢 " + (rule.mediaImage() > 0 ? "+" : "") + rule.mediaImage() + " Media Image");
                if (rule.publicSupport() != 0) ruleEffects.add("📈 " + (rule.publicSupport() > 0 ? "+" : "") + rule.publicSupport() + "% Support");
                String effectsStr = ruleEffects.isEmpty() ? "" : " (Effects: " + String.join(", ", ruleEffects) + ")";
                
                commentary.add("Political consequence: " + party.getName() + " - " + rule.commentary() + effectsStr);
            }
        }
    }

    private boolean hiddenRuleMatches(String key, PartyStats stats) {
        return switch (key) {
            case "coins_under_30_worker_anxiety" -> stats.getCoins() < 30;
            case "coins_under_15_campaign_paralysis" -> stats.getCoins() < 15;
            case "morale_under_50_fundraiser_exit" -> stats.getPartyMorale() < 50;
            case "morale_under_25_cadre_collapse" -> stats.getPartyMorale() < 25;
            case "media_under_30_message_doubt" -> stats.getMediaImage() < 30;
            case "media_under_15_reputation_crisis" -> stats.getMediaImage() < 15;
            case "corruption_over_60_trust_drag" -> stats.getCorruptionScore() > 60;
            case "corruption_over_80_patronage_panic" -> stats.getCorruptionScore() > 80;
            case "support_under_25_electability_fear" -> stats.getPublicSupport() < 25;
            case "support_under_15_survival_panic" -> stats.getPublicSupport() < 15;
            case "coins_over_220_money_machine" -> stats.getCoins() > 220;
            case "media_over_80_favorable_cycle" -> stats.getMediaImage() > 80;
            case "morale_over_85_worker_surge" -> stats.getPartyMorale() > 85;
            case "corruption_under_15_clean_premium" -> stats.getCorruptionScore() < 15;
            case "support_over_45_donor_confidence" -> stats.getPublicSupport() > 45;
            case "support_over_55_winner_effect" -> stats.getPublicSupport() > 55;
            case "low_cash_low_morale_desertion" -> stats.getCoins() < 60 && stats.getPartyMorale() < 45;
            case "bad_media_high_corruption_scandal_loop" -> stats.getMediaImage() < 40 && stats.getCorruptionScore() > 50;
            case "low_morale_high_corruption_leakage" -> stats.getPartyMorale() < 40 && stats.getCorruptionScore() > 55;
            case "low_cash_bad_media_public_doubt" -> stats.getCoins() < 40 && stats.getMediaImage() < 35;
            
            // 10 new realistic rules
            case "low_cash_desperation_corruption" -> stats.getCoins() < 25;
            case "low_morale_corruption_leakage" -> stats.getPartyMorale() < 30;
            case "high_corruption_voter_backlash" -> stats.getCorruptionScore() > 50;
            case "low_morale_voter_apathy" -> stats.getPartyMorale() < 35;
            case "low_media_support_bleed" -> stats.getMediaImage() < 35;
            case "high_cash_patronage_inflation" -> stats.getCoins() > 150;
            case "high_corruption_media_boycott" -> stats.getCorruptionScore() > 75;
            case "low_cash_organizer_desertion" -> stats.getCoins() < 15;
            case "low_media_internal_infighting" -> stats.getMediaImage() < 25;
            case "high_morale_volunteer_surge" -> stats.getPartyMorale() > 80;
            default -> false;
        };
    }

    private List<HiddenMetricRule> hiddenMetricRules() {
        return List.of(
                new HiddenMetricRule("coins_under_30_worker_anxiety", 0, -8, 0, -1, 0,
                        "cash falls below 30 coins, so workers start doubting campaign strength."),
                new HiddenMetricRule("coins_under_15_campaign_paralysis", 0, -5, 0, -4, -2,
                        "cash falls below 15 coins, creating campaign paralysis and public doubt."),
                new HiddenMetricRule("morale_under_50_fundraiser_exit", -20, 0, 0, 0, 0,
                        "morale drops below 50, and donors hold back 20 coins as people leave the party network."),
                new HiddenMetricRule("morale_under_25_cadre_collapse", -10, 0, 0, -5, -2,
                        "cadre morale collapses, weakening both field work and public confidence."),
                new HiddenMetricRule("media_under_30_message_doubt", 0, -3, 0, 0, -4,
                        "media image falls below 30, so voters begin doubting the party message."),
                new HiddenMetricRule("media_under_15_reputation_crisis", -10, 0, 0, 0, -5,
                        "media image falls below 15, causing a full reputation crisis."),
                new HiddenMetricRule("corruption_over_60_trust_drag", 0, 0, 0, -5, -3,
                        "corruption crosses 60, dragging down trust and media coverage."),
                new HiddenMetricRule("corruption_over_80_patronage_panic", -10, -6, 0, 0, -5,
                        "corruption crosses 80, triggering patronage panic and voter anger."),
                new HiddenMetricRule("support_under_25_electability_fear", -8, -5, 0, 0, 0,
                        "support falls below 25%, so donors and workers question electability."),
                new HiddenMetricRule("support_under_10_survival_panic", -10, -8, 0, -5, 0,
                        "support falls below 15%, creating survival panic inside the organization."),
                new HiddenMetricRule("coins_over_220_money_machine", 0, 2, 4, 2, 0,
                        "huge reserves create confidence, but voters notice a money-machine image."),
                new HiddenMetricRule("media_over_80_favorable_cycle", 10, 2, 0, 0, 3,
                        "media image rises above 80, creating a favorable attention cycle."),
                new HiddenMetricRule("morale_over_85_worker_surge", 20, 0, 0, 0, 2,
                        "morale rises above 85, and energized workers bring funds and voters."),
                new HiddenMetricRule("corruption_under_15_clean_premium", -5, 1, 0, 3, 2,
                        "corruption falls below 15, earning a clean-image premium at some operating cost."),
                new HiddenMetricRule("support_over_45_donor_confidence", 15, 5, 0, 0, 0,
                        "support crosses 45%, so donors and workers sense possible victory."),
                new HiddenMetricRule("support_over_55_winner_effect", 20, 0, 2, 4, 0,
                        "support crosses 55%, creating a winner effect but attracting opportunists."),
                new HiddenMetricRule("low_cash_low_morale_desertion", -8, -4, 0, -2, -3,
                        "low cash and low morale combine into local desertions."),
                new HiddenMetricRule("bad_media_high_corruption_scandal_loop", 0, -4, 0, -3, -4,
                        "bad media and high corruption feed a scandal loop."),
                new HiddenMetricRule("low_morale_high_corruption_leakage", -12, -3, 0, -3, 0,
                        "low morale and high corruption encourage internal leaks."),
                new HiddenMetricRule("low_cash_bad_media_public_doubt", 0, -3, 0, 0, -3,
                        "low cash and poor media coverage make the party look unviable."),
                new HiddenMetricRule("low_cash_desperation_corruption", 0, -6, 6, 0, 0,
                        "cash falls below 25 coins, causing financial desperation: party morale drops and corruption increases as campaign shortcuts are taken."),
                new HiddenMetricRule("low_morale_corruption_leakage", 0, 0, 8, 0, 0,
                        "morale falls below 30, leading to a rise in corruption as unmotivated party workers seek self-enrichment."),
                new HiddenMetricRule("high_corruption_voter_backlash", 0, 0, 0, -3, -4,
                        "rising corruption (above 50) triggers public backlash: media image and public support fall."),
                new HiddenMetricRule("low_morale_voter_apathy", 0, -4, 0, -2, -4,
                        "morale falls below 35, causing campaign apathy which drags down media presence and voter support."),
                new HiddenMetricRule("low_media_support_bleed", 0, 0, 0, 0, -5,
                        "low media image (below 35) scares away undecided voters, bleeding public support."),
                new HiddenMetricRule("high_cash_patronage_inflation", 0, 0, 5, 0, 0,
                        "cash exceeds 150 coins, drawing internal patronage demands and increasing corruption risk."),
                new HiddenMetricRule("high_corruption_media_boycott", 0, 0, 0, -10, -6,
                        "corruption exceeds 75, triggering a media boycott that severely damages the party image and public support."),
                new HiddenMetricRule("low_cash_organizer_desertion", 0, -12, 0, 0, -5,
                        "cash drops below 15 coins, causing campaign organizers to desert, hurting grassroots morale and voter support."),
                new HiddenMetricRule("low_media_internal_infighting", 0, -10, 0, 0, 0,
                        "media image drops below 25, causing negative publicity which triggers internal finger-pointing and demoralization."),
                new HiddenMetricRule("high_morale_volunteer_surge", 15, 0, 0, 0, 4,
                        "morale rises above 80, triggering a surge in volunteers who boost campaigns and bring in donations.")
        );
    }

    private void applyHiddenRuleEffect(PartyStats stats, HiddenMetricRule rule) {
        stats.setCoins(stats.getCoins() + rule.coins());
        stats.setPartyMorale(stats.getPartyMorale() + rule.partyMorale());
        stats.setCorruptionScore(stats.getCorruptionScore() + rule.corruptionScore());
        stats.setMediaImage(stats.getMediaImage() + rule.mediaImage());
        stats.setPublicSupport(stats.getPublicSupport() + rule.publicSupport());
    }

    private int reputationDrift(int value, int hardCeiling, int softCeiling, int lowFloor,
                                 int hardDrop, int softDrop, int lowRecovery) {
        if (value >= hardCeiling) {
            return -hardDrop;
        }
        if (value >= softCeiling) {
            return -softDrop;
        }
        if (value <= lowFloor) {
            return lowRecovery;
        }
        return 0;
    }

    private void updatePublicMood(GameSession session, Map<String, Integer> supportPressure) {
        int netPressure = supportPressure.values().stream().mapToInt(Integer::intValue).sum();
        int absolutePressure = supportPressure.values().stream().mapToInt(Math::abs).sum();
        PartyState government = session.getGovernmentParty();
        PublicState publicState = session.getPublicState();
        if (government != null && government.getStats().getCorruptionScore() >= 70
                && government.getStats().getMediaImage() <= 35) {
            publicState.setMood("Angry");
            publicState.setMemoryHint("Voters are connecting corruption allegations with poor government credibility.");
        } else if (absolutePressure >= 8) {
            publicState.setMood("Volatile");
            publicState.setMemoryHint("Voters noticed a sharp political swing this month. Repeated pressure may move committed voters.");
        } else if (netPressure > 2) {
            publicState.setMood("Hopeful");
            publicState.setMemoryHint("Some voters are warming to campaign promises, but undecided voters still need consistency.");
        } else if (netPressure < -2) {
            publicState.setMood("Angry");
            publicState.setMemoryHint("Negative campaigning and governance failures are pushing voters away from parties.");
        } else {
            publicState.setMood("Watchful");
            publicState.setMemoryHint("The public is watching for repeated behavior, not one-off claims.");
        }
        publicState.setMainIssues(List.of("Governance delivery", "Corruption credibility", "Campaign consistency"));
    }

    public void conductElection(GameSession session, String reason, boolean isNoConfidenceElection) {
        electionResolver.conductElection(session, reason, isNoConfidenceElection);
    }

    private Map<String, Map<String, Integer>> initialCardUsage(List<PartyState> parties) {
        Map<String, Map<String, Integer>> usage = new LinkedHashMap<>();
        for (PartyState party : parties) {
            usage.put(party.getId(), new LinkedHashMap<>());
        }
        return usage;
    }

    public void normalizePublicSupport(GameSession session) {
        int turn = session.getTurnNumber();
        int minUndecided = 0;
        if (turn < 45) {
            minUndecided = 10;
        }
        int maxPartyTotal = 100 - minUndecided;

        int total = session.getParties().stream()
                .filter(PartyState::isActive)
                .mapToInt(party -> party.getStats().getPublicSupport())
                .sum();
        if (total <= maxPartyTotal) {
            session.getPublicState().setUndecidedSupport(100 - total);
            for (PartyState party : session.getParties()) {
                if (!party.isActive()) {
                    party.getStats().setPublicSupport(0);
                }
            }
            return;
        }

        int normalizedTotal = 0;
        for (PartyState party : session.getParties()) {
            if (!party.isActive()) {
                party.getStats().setPublicSupport(0);
                continue;
            }
            int normalized = Math.max(0, party.getStats().getPublicSupport() * maxPartyTotal / total);
            party.getStats().setPublicSupport(normalized);
            normalizedTotal += normalized;
        }

        int remainder = maxPartyTotal - normalizedTotal;
        for (PartyState party : session.getParties()) {
            if (!party.isActive()) {
                continue;
            }
            if (remainder <= 0) {
                break;
            }
            party.getStats().setPublicSupport(party.getStats().getPublicSupport() + 1);
            remainder--;
        }
        session.getPublicState().setUndecidedSupport(100 - maxPartyTotal);
    }

    private void clampStats(PartyStats stats) {
        stats.setCoins(Math.max(0, stats.getCoins()));
        stats.setPartyMorale(clamp(stats.getPartyMorale()));
        stats.setCorruptionScore(clamp(stats.getCorruptionScore()));
        stats.setMediaImage(clamp(stats.getMediaImage()));
        stats.setPublicSupport(clamp(stats.getPublicSupport()));
    }

    int clamp(int value) {
        return Math.max(0, Math.min(100, value));
    }

    private PartyStats copyStats(PartyStats stats) {
        return new PartyStats(stats.getCoins(), stats.getPartyMorale(), stats.getCorruptionScore(),
                stats.getMediaImage(), stats.getPublicSupport());
    }

    private Map<String, Integer> delta(PartyStats before, PartyStats after) {
        Map<String, Integer> deltas = new LinkedHashMap<>();
        deltas.put("coins", after.getCoins() - before.getCoins());
        deltas.put("partyMorale", after.getPartyMorale() - before.getPartyMorale());
        deltas.put("corruptionScore", after.getCorruptionScore() - before.getCorruptionScore());
        deltas.put("mediaImage", after.getMediaImage() - before.getMediaImage());
        deltas.put("publicSupport", after.getPublicSupport() - before.getPublicSupport());
        return deltas;
    }

    private void significantMovement(PartyState party, Map<String, Integer> deltas, List<String> commentary) {
        deltas.forEach((metric, value) -> {
            if (Math.abs(value) >= 3) {
                commentary.add(party.getName() + " saw a significant " + metric + " movement: " + signed(value) + ".");
            }
        });
    }

    private String signed(int value) {
        return value > 0 ? "+" + value : String.valueOf(value);
    }

    String targetPhrase(PartyState target) {
        return target == null ? "" : " targeting " + target.getName();
    }

    boolean isNoConfidenceCard(CardDefinition card) {
        return card.getCardKey() != null && card.getCardKey().contains("no_confidence");
    }

    PartyState findParty(GameSession session, String partyId) {
        return session.getParties().stream()
                .filter(party -> party.getId().equals(partyId))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Party not found: " + partyId));
    }

    PartyState resolveSubmittedTarget(GameSession session, PartyState actor, RoundSubmission submission) {
        if (submission.getTargetPartyId() == null || submission.getTargetPartyId().isBlank()) {
            return null;
        }
        return findParty(session, submission.getTargetPartyId());
    }

    CardDefinition findCard(GameSession session, String cardKey, PartyRole role) {
        if ("no_card".equals(cardKey)) {
            CardDefinition noCard = new CardDefinition();
            noCard.setCardKey("no_card");
            noCard.setName("No Card (Pass Turn)");
            noCard.setCategory("governance");
            noCard.setCost(0);
            noCard.setMaxUsesPerCycle(9999);
            noCard.setActive(true);
            noCard.setRoleAllowed(List.of(role.name()));
            noCard.setTarget(new LinkedHashMap<>());
            noCard.setVisibleEffects(new LinkedHashMap<>());
            noCard.setHiddenEffects(new LinkedHashMap<>());
            noCard.setRiskRoll(new LinkedHashMap<>());
            noCard.setIdeologyTags(new LinkedHashMap<>());
            noCard.setTiming(new LinkedHashMap<>());
            noCard.setWeights(new LinkedHashMap<>());
            return noCard;
        }
        return getCardsForSession(session).stream()
                .filter(CardDefinition::isActive)
                .filter(card -> card.getCardKey().equals(cardKey))
                .filter(card -> card.getRoleAllowed().contains(role.name()))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Card not available for party role: " + cardKey));
    }

    private List<NewsDefinition> getCurrentNews(GameSession session) {
        String monthTag = session.getCurrentDate().getYear() + "-" + String.format("%02d", session.getCurrentDate().getMonthValue());
        return getNewsForScenario(session.getScenarioKey()).stream()
                .filter(NewsDefinition::isActive)
                .filter(news -> news.getMonthTags().contains(monthTag)
                        || news.getMonthTags().contains(session.getCurrentDate().getMonth().name().toLowerCase()))
                .limit(1)
                .toList();
    }

    private MonthlyIssueDefinition getIssueByKey(GameSession session, PartyState party, String issueKey) {
        return getIssuesForSession(session).stream()
                .filter(MonthlyIssueDefinition::isActive)
                .filter(issue -> issue.getRoleAllowed().contains(party.getRole().name()))
                .filter(issue -> issue.getIssueKey().equals(issueKey))
                .findFirst()
                .orElseGet(() -> fallbackIssue(party));
    }

    private IssueOptionDefinition findIssueOption(MonthlyIssueDefinition issue, String optionKey) {
        return issue.getOptions().stream()
                .filter(option -> option.getOptionKey().equals(optionKey))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Issue option not available: " + optionKey));
    }

    private MonthlyIssueDefinition fallbackIssue(PartyState party) {
        MonthlyIssueDefinition issue = new MonthlyIssueDefinition();
        issue.setScenarioKey("fallback");
        issue.setIssueKey("routine_role_review_" + party.getRole().name().toLowerCase());
        issue.setRoleAllowed(List.of(party.getRole().name()));
        issue.setCategory(party.getRole() == PartyRole.GOVERNMENT ? "governance_review" : "party_review");
        issue.setTitle(party.getRole() == PartyRole.GOVERNMENT ? "Routine Governance Review" : "Routine Party Review");
        issue.setDescription("No special monthly issue is configured for this role yet. Handle routine political maintenance.");
        IssueOptionDefinition option = new IssueOptionDefinition();
        option.setOptionKey("routine_maintenance");
        option.setText("Handle routine maintenance without major public drama.");
        option.setEffects(Map.of("selfParty", Map.of(
                "coins", -2,
                "partyMorale", 1,
                "corruptionScore", 0,
                "mediaImage", 0,
                "publicSupport", 0
        )));
        option.setRisk(Map.of());
        issue.setOptions(List.of(option));
        return issue;
    }

    private int usedCount(GameSession session, PartyState party, CardDefinition card) {
        if (session.getCardUsageByParty() == null) {
            session.setCardUsageByParty(initialCardUsage(session.getParties()));
        }
        return session.getCardUsageByParty()
                .computeIfAbsent(party.getId(), id -> new LinkedHashMap<>())
                .getOrDefault(card.getCardKey(), 0);
    }

    void incrementCardUsage(GameSession session, PartyState party, CardDefinition card) {
        if (session.getCardUsageByParty() == null) {
            session.setCardUsageByParty(initialCardUsage(session.getParties()));
        }
        Map<String, Integer> partyUsage = session.getCardUsageByParty()
                .computeIfAbsent(party.getId(), id -> new LinkedHashMap<>());
        partyUsage.put(card.getCardKey(), partyUsage.getOrDefault(card.getCardKey(), 0) + 1);
    }

    private record HiddenMetricRule(
            String key,
            int coins,
            int partyMorale,
            int corruptionScore,
            int mediaImage,
            int publicSupport,
            String commentary
    ) {
    }

    private int intValue(Object value) {
        if (value == null) return 0;
        if (value instanceof Number number) {
            return number.intValue();
        }
        try {
            return Integer.parseInt(value.toString());
        } catch (NumberFormatException e) {
            try {
                return (int) Double.parseDouble(value.toString());
            } catch (NumberFormatException ex) {
                return 0;
            }
        }
    }

    private int intValueOrDefault(Object value, int defaultValue) {
        if (value == null) return defaultValue;
        if (value instanceof Number number) {
            return number.intValue();
        }
        try {
            return Integer.parseInt(value.toString());
        } catch (NumberFormatException e) {
            try {
                return (int) Double.parseDouble(value.toString());
            } catch (NumberFormatException ex) {
                return defaultValue;
            }
        }
    }

    private String stringValue(Object value, String defaultValue) {
        if (value == null) return defaultValue;
        return value.toString();
    }

    private String getAlternativeScenarioKey(String scenarioKey) {
        if (scenarioKey == null) return null;
        if ("maharashtra_2001".equals(scenarioKey)) return "Mh_2001";
        if ("Mh_2001".equals(scenarioKey)) return "maharashtra_2001";
        return null;
    }

    private List<CardDefinition> getCardsForScenario(String scenarioKey) {
        if (cardRepository == null) {
            return List.of();
        }
        return DefinitionCache.cardsCache.computeIfAbsent(scenarioKey, key -> {
            List<CardDefinition> cards = cardRepository.findByScenarioKeyOrderByCategoryAscNameAsc(key);
            if (cards.isEmpty()) {
                String altKey = getAlternativeScenarioKey(key);
                if (altKey != null) {
                    cards = cardRepository.findByScenarioKeyOrderByCategoryAscNameAsc(altKey);
                }
            }
            if (cards.isEmpty()) {
                cards = cardRepository.findByScenarioKeyOrderByCategoryAscNameAsc("west_bengal_2000");
            }
            return cards;
        });
    }

    private List<NewsDefinition> getNewsForScenario(String scenarioKey) {
        if (newsRepository == null) {
            return List.of();
        }
        return DefinitionCache.newsCache.computeIfAbsent(scenarioKey, key -> {
            List<NewsDefinition> news = newsRepository.findByScenarioKeyOrderByTypeAscTitleAsc(key);
            if (news.isEmpty()) {
                String altKey = getAlternativeScenarioKey(key);
                if (altKey != null) {
                    news = newsRepository.findByScenarioKeyOrderByTypeAscTitleAsc(altKey);
                }
            }
            return news;
        });
    }

    private List<MonthlyIssueDefinition> getIssuesForScenario(String scenarioKey) {
        if (issueRepository == null) {
            return List.of();
        }
        return DefinitionCache.issuesCache.computeIfAbsent(scenarioKey, key -> {
            List<MonthlyIssueDefinition> issues = issueRepository.findByScenarioKeyOrderByCategoryAscTitleAsc(key);
            if (issues.isEmpty()) {
                String altKey = getAlternativeScenarioKey(key);
                if (altKey != null) {
                    issues = issueRepository.findByScenarioKeyOrderByCategoryAscTitleAsc(altKey);
                }
            }
            if (issues.isEmpty()) {
                issues = issueRepository.findByScenarioKeyOrderByCategoryAscTitleAsc("west_bengal_2000");
            }
            return issues;
        });
    }

    private List<CardDefinition> getCardsForSession(GameSession session) {
        if (session.getGameCards() != null && !session.getGameCards().isEmpty()) {
            return session.getGameCards();
        }
        return getCardsForScenario(session.getScenarioKey());
    }

    private List<MonthlyIssueDefinition> getIssuesForSession(GameSession session) {
        if (session.getGameIssues() != null && !session.getGameIssues().isEmpty()) {
            return session.getGameIssues();
        }
        return getIssuesForScenario(session.getScenarioKey());
    }

    private void resolveActiveCrisis(GameSession session, Map<String, Integer> supportPressure, List<String> commentary) {
        if (session.getActiveCrisisKey() == null) {
            return;
        }

        String key = session.getActiveCrisisKey();
        commentary.add("⚡ Ongoing Crisis Impact: " + session.getActiveCrisisName() + " (Turns remaining: " + session.getActiveCrisisTurnsLeft() + ")");

        if ("drought_crisis".equals(key)) {
            PartyState gov = session.getGovernmentParty();
            if (gov != null) {
                supportPressure.put(gov.getId(), supportPressure.getOrDefault(gov.getId(), 0) - 2);
                gov.getStats().setPartyMorale(Math.max(0, gov.getStats().getPartyMorale() - 3));
                commentary.add("Drought Distress: Government (" + gov.getName() + ") suffered -2 support pressure and -3 Morale due to public rural anger.");
            }
        } else if ("industrial_strike".equals(key)) {
            for (PartyState party : session.getParties()) {
                if (party.isActive()) {
                    party.getStats().setCoins(Math.max(0, party.getStats().getCoins() - 3));
                }
            }
            commentary.add("Labor Strike: All active parties lost 3 coins due to halted business activity.");
            
            PartyState gov = session.getGovernmentParty();
            PartyState opp = session.getOppositionParty();
            if (gov != null) supportPressure.put(gov.getId(), supportPressure.getOrDefault(gov.getId(), 0) - 1);
            if (opp != null) supportPressure.put(opp.getId(), supportPressure.getOrDefault(opp.getId(), 0) - 1);
            commentary.add("Strike Volatility: Governance failure pushes support from major parties into the Undecided pool.");
        } else if ("scam_panic".equals(key)) {
            PartyState gov = session.getGovernmentParty();
            if (gov != null && gov.getStats().getCorruptionScore() > 40) {
                supportPressure.put(gov.getId(), supportPressure.getOrDefault(gov.getId(), 0) - 2);
                gov.getStats().setMediaImage(Math.max(0, gov.getStats().getMediaImage() - 4));
                commentary.add("Scam Backlash: Government (" + gov.getName() + ") has high corruption (>40) and suffered -2 support pressure and -4 Media Image.");
            }
            for (PartyState party : session.getParties()) {
                if (party.isActive() && party.getStats().getCorruptionScore() > 50) {
                    party.getStats().setPartyMorale(Math.max(0, party.getStats().getPartyMorale() - 3));
                    commentary.add("Scam Panic: " + party.getName() + " has high corruption, causing internal panic and -3 Morale.");
                }
            }
        }

        session.setActiveCrisisTurnsLeft(session.getActiveCrisisTurnsLeft() - 1);
        if (session.getActiveCrisisTurnsLeft() <= 0) {
            commentary.add("🎉 Crisis Resolved: " + session.getActiveCrisisName() + " has ended. Normal campaigning resumes.");
            session.setActiveCrisisKey(null);
            session.setActiveCrisisName(null);
            session.setActiveCrisisDescription(null);
            session.setActiveCrisisTurnsLeft(0);
        }
    }

    private void resolveBuildingProjects(GameSession session, Map<String, Integer> supportPressure, List<String> commentary) {
        for (PartyState party : session.getParties()) {
            if (!party.isActive()) {
                continue;
            }
            if (party.getProjects() == null) {
                continue;
            }
            for (ProjectState project : party.getProjects()) {
                if (project.getProgressPercent() < 100) {
                    continue;
                }

                BuildingProject def = BuildingProject.valueOf(project.getProjectKey());
                boolean logCommentary = project.isJustCompleted();
                if (logCommentary) {
                    commentary.add("🏗️ " + party.getName() + " completed project '" + def.getName() + "'!");
                }

                if (def.isRequiresTarget()) {
                    if (project.getTargetPartyId() == null || project.getTargetPartyId().isBlank()) {
                        if (logCommentary) {
                            commentary.add("  ⚠️ Warning: No target assigned to '" + def.getName() + "'. No effect this turn.");
                        }
                        project.setJustCompleted(false);
                        continue;
                    }
                    PartyState target = session.getParties().stream()
                            .filter(p -> p.getId().equals(project.getTargetPartyId()))
                            .findFirst().orElse(null);
                    if (target == null || !target.isActive()) {
                        if (logCommentary) {
                            commentary.add("  ⚠️ Warning: Targeted party is no longer active. Assign a new target.");
                        }
                        project.setJustCompleted(false);
                        continue;
                    }

                    // Check if project is hostile and violates a non-aggression pact
                    boolean projectHostile = def.getBenefitCoins() < 0 
                                          || def.getBenefitMorale() < 0 
                                          || def.getBenefitMedia() < 0 
                                          || def.getBenefitCorruption() > 0 
                                          || def.getBenefitSupport() < 0;
                    if (projectHostile) {
                        checkAndProcessPactViolation(session, party, target, "hostile project '" + def.getName() + "'", commentary);
                    }

                    // Record grudge: target holds a grudge against project owner
                    Map<String, Map<String, Integer>> grudges = session.getGrudges();
                    Map<String, Integer> targetGrudges = grudges.computeIfAbsent(target.getId(), k -> new LinkedHashMap<>());
                    targetGrudges.put(party.getId(), targetGrudges.getOrDefault(party.getId(), 0) + 1);

                    if (def.getBenefitCoins() != 0) {
                        int coinDrain = Math.min(target.getStats().getCoins(), Math.abs(def.getBenefitCoins()));
                        if (coinDrain > 0) {
                            target.getStats().setCoins(target.getStats().getCoins() - coinDrain);
                            if (logCommentary) {
                                commentary.add("  💥 Drained " + target.getName() + "'s Coins by -" + coinDrain + ".");
                            }
                        }
                    }
                    if (def.getBenefitMorale() != 0) {
                        target.getStats().setPartyMorale(Math.max(0, target.getStats().getPartyMorale() + def.getBenefitMorale()));
                        if (logCommentary) {
                            commentary.add("  💥 Drained " + target.getName() + "'s Morale by " + Math.abs(def.getBenefitMorale()) + ".");
                        }
                    }
                    if (def.getBenefitMedia() != 0) {
                        target.getStats().setMediaImage(Math.max(0, target.getStats().getMediaImage() + def.getBenefitMedia()));
                        if (logCommentary) {
                            commentary.add("  💥 Drained " + target.getName() + "'s Media Image by " + Math.abs(def.getBenefitMedia()) + ".");
                        }
                    }
                    if (def.getBenefitCorruption() != 0) {
                        target.getStats().setCorruptionScore(Math.min(100, target.getStats().getCorruptionScore() + def.getBenefitCorruption()));
                        if (logCommentary) {
                            commentary.add("  💥 Exposed " + target.getName() + ", raising their Corruption by +" + def.getBenefitCorruption() + ".");
                        }
                    }
                    if (def.getBenefitSupport() != 0) {
                        int supportDrain = Math.min(target.getStats().getPublicSupport(), Math.abs(def.getBenefitSupport()));
                        if (supportDrain > 0) {
                            target.getStats().setPublicSupport(target.getStats().getPublicSupport() - supportDrain);
                            session.getPublicState().setUndecidedSupport(session.getPublicState().getUndecidedSupport() + supportDrain);
                            if (logCommentary) {
                                commentary.add("  💥 Drained " + target.getName() + "'s Public Support by -" + supportDrain + "%.");
                            }
                        }
                    }
                } else {
                    if (def.getBenefitCoins() != 0) {
                        party.getStats().setCoins(party.getStats().getCoins() + def.getBenefitCoins());
                        if (logCommentary) {
                            commentary.add("  💰 Received +" + def.getBenefitCoins() + " Coins.");
                        }
                    }
                    if (def.getBenefitMorale() != 0) {
                        party.getStats().setPartyMorale(Math.min(100, party.getStats().getPartyMorale() + def.getBenefitMorale()));
                        if (logCommentary) {
                            commentary.add("  ⚡ Received +" + def.getBenefitMorale() + " Morale.");
                        }
                    }
                    if (def.getBenefitMedia() != 0) {
                        party.getStats().setMediaImage(Math.min(100, party.getStats().getMediaImage() + def.getBenefitMedia()));
                        if (logCommentary) {
                            commentary.add("  📢 Received +" + def.getBenefitMedia() + " Media Image.");
                        }
                    }
                    if (def.getBenefitCorruption() != 0) {
                        party.getStats().setCorruptionScore(Math.max(0, party.getStats().getCorruptionScore() + def.getBenefitCorruption()));
                        if (logCommentary) {
                            commentary.add("  🛡️ Reduced Corruption by " + Math.abs(def.getBenefitCorruption()) + ".");
                        }
                    }
                    if (def.getBenefitSupport() != 0) {
                        int undecided = session.getPublicState().getUndecidedSupport();
                        int supportGain = Math.min(undecided, def.getBenefitSupport());
                        if (supportGain > 0) {
                            party.getStats().setPublicSupport(party.getStats().getPublicSupport() + supportGain);
                            session.getPublicState().setUndecidedSupport(undecided - supportGain);
                            if (logCommentary) {
                                commentary.add("  📈 Gained +" + supportGain + "% Public Support from Undecided voters.");
                            }
                        } else {
                            if (logCommentary) {
                                commentary.add("  📈 No Undecided voters available to gain support.");
                            }
                        }
                    }
                }
                project.setJustCompleted(false);
            }
        }
    }

    private String formatEffectsMap(Map<String, Object> effects) {
        if (effects == null || effects.isEmpty()) return "None";
        List<String> parts = new ArrayList<>();
        int coins = intValue(effects.get("coins"));
        if (coins != 0) parts.add("💰 " + (coins > 0 ? "+" : "") + coins + " Coins");
        int morale = intValue(effects.get("partyMorale"));
        if (morale != 0) parts.add("✊ " + (morale > 0 ? "+" : "") + morale + " Morale");
        int corruption = intValue(effects.get("corruptionScore"));
        if (corruption != 0) parts.add("⚖️ " + (corruption > 0 ? "+" : "") + corruption + "% Corruption");
        int media = intValue(effects.get("mediaImage"));
        if (media != 0) parts.add("📢 " + (media > 0 ? "+" : "") + media + " Media Image");
        int support = intValue(effects.get("publicSupport"));
        if (support != 0) parts.add("📈 " + (support > 0 ? "+" : "") + support + "% Support");
        
        if (parts.isEmpty()) return "None";
        return String.join(", ", parts);
    }

    String formatEffectsObject(Map<String, Object> outerEffects, String key) {
        Map<String, Object> subEffects = partyEffect(outerEffects, key);
        return formatEffectsMap(subEffects);
    }

    private String formatRewardEffects(RewardDefinition reward) {
        List<String> parts = new ArrayList<>();
        if (reward.coinsEffect() != 0) parts.add("💰 " + (reward.coinsEffect() > 0 ? "+" : "") + reward.coinsEffect() + " Coins");
        if (reward.moraleEffect() != 0) parts.add("✊ " + (reward.moraleEffect() > 0 ? "+" : "") + reward.moraleEffect() + " Morale");
        if (reward.corruptionEffect() != 0) parts.add("⚖️ " + (reward.corruptionEffect() > 0 ? "+" : "") + reward.corruptionEffect() + "% Corruption");
        if (reward.mediaEffect() != 0) parts.add("📢 " + (reward.mediaEffect() > 0 ? "+" : "") + reward.mediaEffect() + " Media Image");
        if (reward.publicSupportEffect() != 0) parts.add("📈 " + (reward.publicSupportEffect() > 0 ? "+" : "") + reward.publicSupportEffect() + "% Support");
        if (parts.isEmpty()) return "None";
        return String.join(", ", parts);
    }

    void checkAndProcessPactViolation(GameSession session, PartyState actor, PartyState target, String sourceName, List<String> commentary) {
        if (target == null || session.getActivePacts() == null) {
            return;
        }
        NonAggressionPact violatedPact = null;
        for (NonAggressionPact pact : session.getActivePacts()) {
            if ((pact.getPartyAId().equals(actor.getId()) && pact.getPartyBId().equals(target.getId()))
                    || (pact.getPartyAId().equals(target.getId()) && pact.getPartyBId().equals(actor.getId()))) {
                violatedPact = pact;
                break;
            }
        }
        if (violatedPact != null) {
            session.getActivePacts().remove(violatedPact);
            actor.getStats().setPartyMorale(Math.max(0, actor.getStats().getPartyMorale() - 15));
            String msg = "🚨 Treaty Violation! " + actor.getName() + " broke their Non-Aggression Pact with " + target.getName() 
                    + " via " + sourceName + "! They suffer a backlash of -15 Party Morale for their betrayal.";
            commentary.add(msg);
            session.getLastResults().add("🚨 Pact Violation: " + actor.getName() + " attacked " + target.getName());
        }
    }
}


