package com.politicalsim.game;

import com.politicalsim.content.CardDefinition;
import com.politicalsim.content.CardDefinitionRepository;
import com.politicalsim.content.IssueOptionDefinition;
import com.politicalsim.content.MonthlyIssueDefinition;
import com.politicalsim.content.MonthlyIssueDefinitionRepository;
import com.politicalsim.content.NewsDefinition;
import com.politicalsim.content.NewsDefinitionRepository;
import com.politicalsim.content.NewsReactionDefinition;
import com.politicalsim.party.PartyRole;
import com.politicalsim.party.PartyState;
import com.politicalsim.party.PartyStats;
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

    public static final List<RewardDefinition> REWARD_POOL = List.of(
        new RewardDefinition("reward_grant_50_coins", "Federal Funding Grant", "Gift 50 coins to a selected party.", true, "any", 50, 0, 0, 0, 0),
        new RewardDefinition("reward_sabotage_20_morale", "Morale Sabotage", "Deduct 20 morale from an opponent party.", true, "opponent", 0, -20, 0, 0, 0),
        new RewardDefinition("reward_leak_25_corruption", "Corruption Exposure", "Increase corruption score by 25 on an opponent party.", true, "opponent", 0, 0, 25, 0, 0),
        new RewardDefinition("reward_smear_5_support", "Smear Campaign", "Decrease public support by 5% of an opponent party.", true, "opponent", 0, 0, 0, 0, -5),
        new RewardDefinition("reward_donation_40_coins", "Private Donation", "Gift 40 coins to yourself.", false, "self", 40, 0, 0, 0, 0),
        new RewardDefinition("reward_cadre_15_morale", "Cadre Boost", "Increase morale by 15 of yourself.", false, "self", 0, 15, 0, 0, 0),
        new RewardDefinition("reward_spotlight_20_media", "Media Spotlight", "Boost media image by 20 of a selected party.", true, "any", 0, 0, 0, 20, 0),
        new RewardDefinition("reward_reform_15_corruption", "Internal Reform", "Decrease corruption score by 15 of yourself.", false, "self", 0, 0, -15, 0, 0),
        new RewardDefinition("reward_rally_8_support", "Grassroots Rally", "Boost public support by 8% of yourself.", false, "self", 0, 0, 0, 0, 8),
        new RewardDefinition("reward_morale_tax", "Morale Tradeoff", "Deduct 15 morale from yourself to gain 30 coins.", false, "self", 30, -15, 0, 0, 0),
        new RewardDefinition("reward_tax_audit", "Tax Audit Trigger", "Increase corruption by 20 and deduct 15 coins from an opponent party.", true, "opponent", -15, 0, 20, 0, 0),
        new RewardDefinition("reward_assassination", "Character Assassination", "Deduct 25 media image and 15 morale from an opponent party.", true, "opponent", 0, -15, 0, -25, 0),
        new RewardDefinition("reward_alliance", "Local Coalition Boost", "Boost public support by 6% and media image by 10 of yourself.", false, "self", 0, 0, 0, 10, 6),
        new RewardDefinition("reward_bribe_scandal", "Bribe Scandal Setup", "Increase corruption by 30 and deduct 10 morale from an opponent party.", true, "opponent", 0, -10, 30, 0, 0),
        new RewardDefinition("reward_charity_event", "Charity Gala", "Deduct 20 coins from yourself but boost media image by 25.", false, "self", -20, 0, 0, 25, 0),
        new RewardDefinition("reward_ideological_purge", "Ideological Purge", "Boost morale by 25 add 5% public support from yourself.", false, "self", 0, 25, 0, 0, 5),
        new RewardDefinition("reward_foreign_aid", "Foreign Aid Link", "Gift 60 coins to yourself, but increase corruption by 10.", false, "self", 60, 0, 10, 0, 0),
        new RewardDefinition("reward_press_boycott", "Press Boycott", "Deduct 30 media image from an opponent party.", true, "opponent", 0, 0, 0, -30, 0),
        new RewardDefinition("reward_voter_suppression", "Voter Suppression Probe", "Deduct 8% public support from an opponent party.", true, "opponent", 0, 0, 0, 0, -8),
        new RewardDefinition("reward_audit_cleanse", "Audit Cleanse", "Decrease corruption score by 25 of yourself.", false, "self", 0, 0, -25, 0, 0)
    );

    private final CardDefinitionRepository cardRepository;
    private final NewsDefinitionRepository newsRepository;
    private final MonthlyIssueDefinitionRepository issueRepository;

    public RoundResolutionEngine(
            CardDefinitionRepository cardRepository,
            NewsDefinitionRepository newsRepository,
            MonthlyIssueDefinitionRepository issueRepository
    ) {
        this.cardRepository = cardRepository;
        this.newsRepository = newsRepository;
        this.issueRepository = issueRepository;
    }

    public boolean resolveRound(GameSession session) {
        Map<String, PartyStats> beforeStats = new LinkedHashMap<>();
        for (PartyState party : session.getParties()) {
            beforeStats.put(party.getId(), copyStats(party.getStats()));
        }

        List<String> commentary = new ArrayList<>();
        List<String> resultLines = new ArrayList<>();
        Map<String, Integer> supportPressure = initialSupportPressure(session);
        resolveDueDelayedEffects(session, supportPressure, commentary);
        
        // Deduct bids first
        String biddingMetric = getBiddingMetricForTurn(session.getTurnNumber());
        for (RoundSubmission submission : session.getCurrentRoundSubmissions()) {
            PartyState actor = findParty(session, submission.getPartyId());
            int bid = submission.getBid();
            deductStatValue(actor, biddingMetric, bid);
            commentary.add("Bidding: " + actor.getName() + " bid " + bid + " " + biddingMetric + ".");
        }

        // Apply played rewards
        for (RoundSubmission submission : session.getCurrentRoundSubmissions()) {
            if (submission.getSelectedRewardKey() != null && !submission.getSelectedRewardKey().isBlank()) {
                PartyState actor = findParty(session, submission.getPartyId());
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
                    applyRewardEffect(session, rTarget, rewardDef, commentary);
                    commentary.add("Reward played: " + actor.getName() + " played reward '" + rewardDef.name() + "' on target " + rTarget.getName() + ".");
                    resultLines.add(actor.getName() + " played reward: " + rewardDef.name() + (rewardDef.requiresTarget() ? " on " + rTarget.getName() : ""));
                }
            }
        }

        boolean noConfidencePlayed = false;
        for (RoundSubmission submission : session.getCurrentRoundSubmissions()) {
            PartyState actor = findParty(session, submission.getPartyId());
            PartyState opponent = resolveSubmittedTarget(session, actor, submission);
            CardDefinition card = findCard(session, submission.getCardKey(), actor.getRole());
            if (isNoConfidenceCard(card)) {
                noConfidencePlayed = true;
            }
            incrementCardUsage(session, actor, card);
            applyCard(session, actor, opponent, card, supportPressure, commentary);
            scheduleCardDelayedEffects(session, actor, opponent, card, commentary);
            if (submission.getAiIntent() == null || submission.getAiIntent().isBlank()) {
                commentary.add(actor.getName() + " played " + card.getName() + targetPhrase(opponent) + ".");
            } else {
                commentary.add(actor.getName() + " chose " + card.getName() + targetPhrase(opponent)
                        + " with intent " + submission.getAiIntent() + ".");
            }
            resultLines.add(actor.getName() + " played card: " + card.getName());
            int coinAward = resolveNewsReactions(session, actor, submission.getNewsReactions(), supportPressure, commentary);
            commentary.add(actor.getName() + " gained " + coinAward + " coins from news handling.");
            resolveIssueChoice(session, actor, submission, supportPressure, commentary);
        }

        // Bidding Winner determination
        int highestBid = -1;
        List<RoundSubmission> winners = new ArrayList<>();
        for (RoundSubmission sub : session.getCurrentRoundSubmissions()) {
            if (sub.getBid() > highestBid) {
                highestBid = sub.getBid();
                winners.clear();
                winners.add(sub);
            } else if (sub.getBid() == highestBid) {
                winners.add(sub);
            }
        }

        RoundSubmission roundWinnerSub = null;
        if (winners.size() == 1) {
            roundWinnerSub = winners.get(0);
        } else if (winners.size() > 1) {
            int highestSupport = -1;
            List<RoundSubmission> supportWinners = new ArrayList<>();
            for (RoundSubmission sub : winners) {
                PartyState party = findParty(session, sub.getPartyId());
                int support = party.getStats().getPublicSupport();
                if (support > highestSupport) {
                    highestSupport = support;
                    supportWinners.clear();
                    supportWinners.add(sub);
                } else if (support == highestSupport) {
                    supportWinners.add(sub);
                }
            }
            if (supportWinners.size() == 1) {
                roundWinnerSub = supportWinners.get(0);
            } else {
                for (PartyRole role : List.of(PartyRole.GOVERNMENT, PartyRole.OPPOSITION, PartyRole.THIRD_PARTY)) {
                    for (RoundSubmission sub : supportWinners) {
                        PartyState party = findParty(session, sub.getPartyId());
                        if (party.getRole() == role) {
                            roundWinnerSub = sub;
                            break;
                        }
                    }
                    if (roundWinnerSub != null) break;
                }
            }
        }

        String winnerPartyId = null;
        if (roundWinnerSub != null) {
            winnerPartyId = roundWinnerSub.getPartyId();
            PartyState winnerParty = findParty(session, winnerPartyId);
            int currentWins = session.getPartyRoundWins().getOrDefault(winnerPartyId, 0);
            session.getPartyRoundWins().put(winnerPartyId, currentWins + 1);
            commentary.add("Bidding Winner: " + winnerParty.getName() + " wins the bidding round with a bid of " + highestBid + " " + biddingMetric + "!");
        } else {
            commentary.add("Bidding Winner: No winner for this round.");
        }

        Map<String, Integer> roundBids = new LinkedHashMap<>();
        for (RoundSubmission sub : session.getCurrentRoundSubmissions()) {
            roundBids.put(sub.getPartyId(), sub.getBid());
        }
        session.setLastRoundBids(roundBids);
        session.setLastRoundBiddingMetric(biddingMetric);
        session.setLastRoundWinnerPartyId(winnerPartyId);

        // Update held rewards expiration countdown
        for (Map.Entry<String, List<HeldReward>> entry : session.getPartyHeldRewards().entrySet()) {
            List<HeldReward> list = entry.getValue();
            if (list != null) {
                List<HeldReward> kept = new ArrayList<>();
                for (HeldReward hr : list) {
                    hr.setTurnsLeft(hr.getTurnsLeft() - 1);
                    if (hr.getTurnsLeft() > 0) {
                        kept.add(hr);
                    } else {
                        commentary.add("Expired: " + hr.getName() + " in " + findParty(session, entry.getKey()).getName() + "'s inventory has expired.");
                    }
                }
                entry.setValue(kept);
            }
        }

        // Cycle complete check at turn 5
        int cycleTurn = ((session.getTurnNumber() - 1) % 5) + 1;
        if (cycleTurn == 5) {
            int maxWins = -1;
            List<String> cycleWinners = new ArrayList<>();
            for (Map.Entry<String, Integer> entry : session.getPartyRoundWins().entrySet()) {
                if (entry.getValue() > maxWins) {
                    maxWins = entry.getValue();
                    cycleWinners.clear();
                    cycleWinners.add(entry.getKey());
                } else if (entry.getValue() == maxWins) {
                    cycleWinners.add(entry.getKey());
                }
            }

            String cycleWinnerPartyId = null;
            if (cycleWinners.size() == 1) {
                cycleWinnerPartyId = cycleWinners.get(0);
            } else if (cycleWinners.size() > 1) {
                int highestSupport = -1;
                for (String partyId : cycleWinners) {
                    PartyState party = findParty(session, partyId);
                    if (party.getStats().getPublicSupport() > highestSupport) {
                        highestSupport = party.getStats().getPublicSupport();
                        cycleWinnerPartyId = partyId;
                    }
                }
            }

            if (cycleWinnerPartyId != null) {
                PartyState winnerParty = findParty(session, cycleWinnerPartyId);
                RewardDefinition reward = REWARD_POOL.stream()
                        .filter(r -> r.key().equals(session.getCurrentRewardKey()))
                        .findFirst().orElse(null);
                if (reward != null) {
                    List<HeldReward> held = session.getPartyHeldRewards().computeIfAbsent(cycleWinnerPartyId, k -> new ArrayList<>());
                    HeldReward newHeld = new HeldReward(reward.key(), reward.name(), reward.description(), 5, reward.requiresTarget(), reward.allowedTargets());
                    held.add(newHeld);
                    commentary.add("🏆 CYCLE REWARD AWARDED: " + winnerParty.getName() + " wins the 5-turn cycle reward: " + reward.name() + " (" + reward.description() + ")!");
                }
            } else {
                commentary.add("🏆 CYCLE REWARD: No winner could be determined for this cycle.");
            }

            // Select next reward
            RewardDefinition nextReward = selectRandomReward(session);
            session.setCurrentRewardKey(nextReward.key());
            session.setCurrentRewardName(nextReward.name());
            session.setCurrentRewardDescription(nextReward.description());

            // Reset round wins
            for (String partyId : session.getPartyRoundWins().keySet()) {
                session.getPartyRoundWins().put(partyId, 0);
            }
        }

        resolvePublicSupport(session, supportPressure, commentary);
        applyMonthlyStatDrift(session, commentary);
        applyHiddenMetricRules(session, commentary);

        for (PartyState party : session.getParties()) {
            if (party.getStats().getCoins() < 10) {
                party.getStats().setCoins(party.getStats().getCoins() + 15);
                commentary.add("Subsidy: " + party.getName() + " received an emergency campaign subsidy (+15 coins) because their reserves fell below 10.");
            }
        }

        Map<String, Map<String, Integer>> deltas = new LinkedHashMap<>();
        for (PartyState party : session.getParties()) {
            clampStats(party.getStats());
            Map<String, Integer> partyDeltas = delta(beforeStats.get(party.getId()), party.getStats());
            deltas.put(party.getId(), partyDeltas);
            significantMovement(party, partyDeltas, commentary);
        }
        normalizePublicSupport(session);

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

    private void applyCard(GameSession session, PartyState actor, PartyState opponent, CardDefinition card,
                           Map<String, Integer> supportPressure, List<String> commentary) {
        actor.getStats().setCoins(actor.getStats().getCoins() - card.getCost());
        applyEffects(actor, partyEffect(card.getVisibleEffects(), "selfParty"), supportPressure);
        if (opponent != null) {
            applyEffects(opponent, partyEffect(card.getVisibleEffects(), "opponentParty"), supportPressure);
        }
        applyRiskRoll(session, actor, opponent, card, supportPressure, commentary);
    }

    @SuppressWarnings("unchecked")
    private Map<String, Object> partyEffect(Map<String, Object> effects, String key) {
        Object value = effects.get(key);
        if (value instanceof Map<?, ?> map) {
            return (Map<String, Object>) map;
        }
        return Map.of();
    }

    private int resolveNewsReactions(GameSession session, PartyState actor, Map<String, String> selectedReactions,
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
            applyEffects(actor, partyEffect(reaction.getEffects(), "playerParty"), supportPressure);
            applyReactionRisk(session, actor, reaction, supportPressure, commentary);
            if (news != null) {
                scheduleNewsDelayedEffects(session, actor, news, reaction, commentary);
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

    private void resolveIssueChoice(GameSession session, PartyState actor, RoundSubmission submission,
                                    Map<String, Integer> supportPressure, List<String> commentary) {
        if (submission.getIssueKey() == null || submission.getIssueOptionKey() == null) {
            return;
        }
        MonthlyIssueDefinition issue = getIssueByKey(session, actor, submission.getIssueKey());
        IssueOptionDefinition option = findIssueOption(issue, submission.getIssueOptionKey());
        applyEffects(actor, partyEffect(option.getEffects(), "selfParty"), supportPressure);
        applyIssueRisk(session, actor, option, supportPressure, commentary);
        commentary.add(actor.getName() + " handled issue '" + issue.getTitle() + "' by choosing: " + option.getText());
        scheduleIssueDelayedEffects(session, actor, issue, option, commentary);
    }

    private void applyIssueRisk(GameSession session, PartyState actor, IssueOptionDefinition option,
                                Map<String, Integer> supportPressure, List<String> commentary) {
        int chance = intValue(option.getRisk().get("chance"));
        if (chance <= 0 || !riskHit(session, "issue:" + actor.getId() + ":" + option.getOptionKey(), chance)) {
            return;
        }
        applyEffects(actor, riskEffect(option.getRisk(), "selfParty"), supportPressure);
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
            applyEffects(target, delayedEffect.getEffects(), supportPressure);
            commentary.add("Delayed result: " + (delayedEffect.getCommentary() == null
                    ? delayedEffect.getSourceName() + " affected " + target.getName()
                    : delayedEffect.getCommentary()));
        }
        session.setDelayedEffects(remaining);
    }

    private boolean isLegacyAutoCardDelayedEffect(GameSession session, DelayedEffect delayedEffect) {
        if (!"card".equals(delayedEffect.getSourceType())) {
            return false;
        }
        return getCardsForScenario(session.getScenarioKey()).stream()
                .filter(card -> card.getCardKey().equals(delayedEffect.getSourceKey()))
                .noneMatch(card -> {
                    Object scheduled = card.getVisibleEffects().get("scheduled");
                    return scheduled instanceof List<?> list && !list.isEmpty();
                });
    }

    private void scheduleCardDelayedEffects(GameSession session, PartyState actor, PartyState opponent,
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

    private void applyEffects(PartyState party, Map<String, Object> effects, Map<String, Integer> supportPressure) {
        applyPartyEffectsWithoutSupport(party.getStats(), effects);
        supportPressure.computeIfPresent(party.getId(), (id, value) -> value + intValue(effects.get("publicSupport")));
    }

    private void applyPartyEffectsWithoutSupport(PartyStats stats, Map<String, Object> effects) {
        stats.setCoins(stats.getCoins() + intValue(effects.get("coins")));
        stats.setPartyMorale(stats.getPartyMorale() + intValue(effects.get("partyMorale")));
        stats.setCorruptionScore(stats.getCorruptionScore() + intValue(effects.get("corruptionScore")));
        stats.setMediaImage(stats.getMediaImage() + intValue(effects.get("mediaImage")));
    }

    private void applyRiskRoll(GameSession session, PartyState actor, PartyState opponent, CardDefinition card,
                               Map<String, Integer> supportPressure, List<String> commentary) {
        int chance = intValue(card.getRiskRoll().get("chance"));
        if (chance <= 0 || !riskHit(session, "card:" + actor.getId() + ":" + card.getCardKey(), chance)) {
            return;
        }
        applyEffects(actor, riskEffect(card.getRiskRoll(), "selfParty"), supportPressure);
        if (opponent != null) {
            applyEffects(opponent, riskEffect(card.getRiskRoll(), "opponentParty"), supportPressure);
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
        applyEffects(actor, riskEffect(reaction.getRisk(), "playerParty"), supportPressure);
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
                commentary.add("Political consequence: " + party.getName() + " - " + rule.commentary());
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
                new HiddenMetricRule("support_under_15_survival_panic", -15, -8, 0, -5, 0,
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

    public void conductElection(GameSession session, String reason) {
        List<PartyState> ranking = new ArrayList<>(session.getParties());
        ranking.sort(Comparator.comparingInt((PartyState party) -> party.getStats().getPublicSupport()).reversed());

        PartyState winner = ranking.get(0);
        PartyState runnerUp = ranking.size() > 1 ? ranking.get(1) : winner;
        for (PartyState party : ranking) {
            if (party.getId().equals(winner.getId())) {
                party.setRole(PartyRole.GOVERNMENT);
                party.getStats().setCoins(100);
                party.getStats().setPartyMorale(clamp(party.getStats().getPartyMorale() + 5));
            } else if (party.getId().equals(runnerUp.getId())) {
                party.setRole(PartyRole.OPPOSITION);
                party.getStats().setCoins(75);
            } else {
                party.setRole(PartyRole.THIRD_PARTY);
                party.getStats().setCoins(75);
            }
        }

        session.setGovernmentParty(winner);
        session.setOppositionParty(runnerUp);
        session.setCardUsageByParty(initialCardUsage(session.getParties()));
        session.getLastRoundCommentary().add(reason + " " + winner.getName() + " forms the government with "
                + winner.getStats().getPublicSupport() + "% support.");
        session.setLastResults(List.of("Election result: " + winner.getName() + " forms the government."));
        session.setStatus(GameStatus.GAME_OVER);
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

        int total = session.getParties().stream().mapToInt(party -> party.getStats().getPublicSupport()).sum();
        if (total <= maxPartyTotal) {
            session.getPublicState().setUndecidedSupport(100 - total);
            return;
        }

        int normalizedTotal = 0;
        for (PartyState party : session.getParties()) {
            int normalized = Math.max(0, party.getStats().getPublicSupport() * maxPartyTotal / total);
            party.getStats().setPublicSupport(normalized);
            normalizedTotal += normalized;
        }

        int remainder = maxPartyTotal - normalizedTotal;
        for (PartyState party : session.getParties()) {
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

    private int clamp(int value) {
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

    private String targetPhrase(PartyState target) {
        return target == null ? "" : " targeting " + target.getName();
    }

    private boolean isNoConfidenceCard(CardDefinition card) {
        return card.getCardKey() != null && card.getCardKey().contains("no_confidence");
    }

    private PartyState findParty(GameSession session, String partyId) {
        return session.getParties().stream()
                .filter(party -> party.getId().equals(partyId))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Party not found: " + partyId));
    }

    private PartyState resolveSubmittedTarget(GameSession session, PartyState actor, RoundSubmission submission) {
        if (submission.getTargetPartyId() == null || submission.getTargetPartyId().isBlank()) {
            return null;
        }
        return findParty(session, submission.getTargetPartyId());
    }

    private CardDefinition findCard(GameSession session, String cardKey, PartyRole role) {
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
        return getCardsForScenario(session.getScenarioKey()).stream()
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
        return getIssuesForScenario(session.getScenarioKey()).stream()
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

    private void incrementCardUsage(GameSession session, PartyState party, CardDefinition card) {
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

    private List<CardDefinition> getCardsForScenario(String scenarioKey) {
        List<CardDefinition> cards = cardRepository.findByScenarioKeyOrderByCategoryAscNameAsc(scenarioKey);
        if (cards.isEmpty()) {
            cards = cardRepository.findByScenarioKeyOrderByCategoryAscNameAsc("west_bengal_2000");
        }
        return cards;
    }

    private List<NewsDefinition> getNewsForScenario(String scenarioKey) {
        List<NewsDefinition> news = newsRepository.findByScenarioKeyOrderByTypeAscTitleAsc(scenarioKey);
        if (news.isEmpty()) {
            news = newsRepository.findByScenarioKeyOrderByTypeAscTitleAsc("west_bengal_2000");
        }
        return news;
    }

    private List<MonthlyIssueDefinition> getIssuesForScenario(String scenarioKey) {
        List<MonthlyIssueDefinition> issues = issueRepository.findByScenarioKeyOrderByCategoryAscTitleAsc(scenarioKey);
        if (issues.isEmpty()) {
            issues = issueRepository.findByScenarioKeyOrderByCategoryAscTitleAsc("west_bengal_2000");
        }
        return issues;
    }
}

