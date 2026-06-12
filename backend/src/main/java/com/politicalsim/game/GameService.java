package com.politicalsim.game;

import com.politicalsim.api.CreateGameRequest;
import com.politicalsim.api.PartyView;
import com.politicalsim.api.TurnView;
import com.politicalsim.api.TurnAdvanceRequest;
import com.politicalsim.api.HeldRewardView;
import com.politicalsim.api.CampaignProgressResponse;
import com.politicalsim.api.ScenarioProgressView;
import com.politicalsim.ai.AiDecision;
import com.politicalsim.ai.AiDecisionService;
import com.politicalsim.ai.AiProfile;
import com.politicalsim.ai.AiStyle;
import com.politicalsim.content.CardDefinition;
import com.politicalsim.content.CardDefinitionRepository;
import com.politicalsim.content.IssueOptionDefinition;
import com.politicalsim.content.MonthlyIssueDefinition;
import com.politicalsim.content.MonthlyIssueDefinitionRepository;
import com.politicalsim.content.NewsDefinition;
import com.politicalsim.content.NewsDefinitionRepository;
import com.politicalsim.content.NewsReactionDefinition;
import com.politicalsim.content.DefinitionCache;
import com.politicalsim.content.ScenarioDefinition;
import com.politicalsim.content.ScenarioDefinitionRepository;
import com.politicalsim.party.ControllerType;
import com.politicalsim.party.PartyRole;
import com.politicalsim.party.PartyState;
import com.politicalsim.party.PartyStats;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;
import org.springframework.stereotype.Service;

@Service
public class GameService {

    private static final int CYCLE_LENGTH_MONTHS = 60;
    private static final int NO_CONFIDENCE_SUPPORT_THRESHOLD = 30;
    private static final int NO_CONFIDENCE_MORALE_THRESHOLD = 35;

    private final GameSessionService gameSessionService;
    private final RoundResolutionEngine roundResolutionEngine;
    private final CardDefinitionRepository cardRepository;
    private final NewsDefinitionRepository newsRepository;
    private final MonthlyIssueDefinitionRepository issueRepository;
    private final ScenarioDefinitionRepository scenarioRepository;
    private final AiDecisionService aiDecisionService;

    public GameService(
            GameSessionService gameSessionService,
            RoundResolutionEngine roundResolutionEngine,
            CardDefinitionRepository cardRepository,
            NewsDefinitionRepository newsRepository,
            MonthlyIssueDefinitionRepository issueRepository,
            ScenarioDefinitionRepository scenarioRepository,
            AiDecisionService aiDecisionService
    ) {
        this.gameSessionService = gameSessionService;
        this.roundResolutionEngine = roundResolutionEngine;
        this.cardRepository = cardRepository;
        this.newsRepository = newsRepository;
        this.issueRepository = issueRepository;
        this.scenarioRepository = scenarioRepository;
        this.aiDecisionService = aiDecisionService;
    }

    public CampaignProgressResponse getCampaignProgress(String userId) {
        List<ScenarioDefinition> allActive = scenarioRepository.findAll().stream()
                .filter(ScenarioDefinition::isActive)
                .toList();
        List<ScenarioDefinition> activeScenarios = new ArrayList<>();
        java.util.Set<String> seenKeys = new java.util.HashSet<>();
        for (ScenarioDefinition s : allActive) {
            if (s.getScenarioKey() != null && seenKeys.add(s.getScenarioKey())) {
                activeScenarios.add(s);
            }
        }

        List<GameSession> userGames = new ArrayList<>();
        if (userId != null && !userId.isBlank()) {
            userGames = gameSessionService.listGames(userId);
        }

        List<String> wonScenarioKeys = new ArrayList<>();
        for (GameSession g : userGames) {
            String skey = g.getScenarioKey();
            if (g.getStatus() == GameStatus.VICTORY) {
                wonScenarioKeys.add(skey);
            } else if (g.getStatus() == GameStatus.GAME_OVER) {
                PartyState gov = g.getGovernmentParty();
                if (gov != null && g.getPlayerPartyIds() != null && g.getPlayerPartyIds().contains(gov.getId())) {
                    wonScenarioKeys.add(skey);
                }
            }
        }

        boolean wbWon = wonScenarioKeys.contains("west_bengal_2000");
        boolean mhWon = wonScenarioKeys.contains("maharashtra_2001") || wonScenarioKeys.contains("Mh_2001");
        boolean upWon = wonScenarioKeys.contains("uttar_pradesh_2001");
        boolean tnWon = wonScenarioKeys.contains("tamil_nadu_2001");
        boolean rjWon = wonScenarioKeys.contains("rajasthan_2001");

        int currentEra = 2001;
        if (wbWon && mhWon && upWon && tnWon && rjWon) {
            currentEra = 2006;
        }

        List<ScenarioProgressView> scenarioProgressList = new ArrayList<>();
        for (ScenarioDefinition s : activeScenarios) {
            String key = s.getScenarioKey();
            if (key == null) continue;

            boolean is2006 = key.endsWith("_2006");
            boolean is2001 = key.endsWith("_2000") || key.endsWith("_2001");

            if (currentEra == 2006 && !is2006) continue;
            if (currentEra == 2001 && !is2001) continue;

            String status = "AVAILABLE";
            
            boolean hasActive = false;
            for (GameSession g : userGames) {
                if (key.equals(g.getScenarioKey()) && g.getStatus() == GameStatus.ACTIVE) {
                    hasActive = true;
                    break;
                }
            }

            if (hasActive) {
                status = "IN_PROGRESS";
            } else if (wonScenarioKeys.contains(key)) {
                status = "WON";
            } else {
                boolean locked = false;
                if (currentEra == 2006) {
                    if (!"west_bengal_2006".equals(key) && !wonScenarioKeys.contains("west_bengal_2006")) {
                        locked = true;
                    }
                } else {
                    boolean isDefaultUnlocked = "west_bengal_2000".equals(key) || "maharashtra_2001".equals(key) || "Mh_2001".equals(key);
                    if (!isDefaultUnlocked && !wonScenarioKeys.contains("west_bengal_2000")) {
                        locked = true;
                    }
                }
                
                if (locked) {
                    status = "LOCKED";
                }
            }

            scenarioProgressList.add(new ScenarioProgressView(
                key,
                s.getName(),
                s.getStateName(),
                s.getDescription(),
                status,
                s
            ));
        }

        List<String> orderKeys = List.of(
            "west_bengal_2000", "west_bengal_2006",
            "maharashtra_2001", "Mh_2001", "maharashtra_2006",
            "uttar_pradesh_2001", "uttar_pradesh_2006",
            "tamil_nadu_2001", "tamil_nadu_2006",
            "rajasthan_2001", "rajasthan_2006"
        );
        scenarioProgressList.sort((a, b) -> {
            int indexA = orderKeys.indexOf(a.getScenarioKey());
            int indexB = orderKeys.indexOf(b.getScenarioKey());
            if (indexA == -1 && indexB == -1) return a.getScenarioKey().compareTo(b.getScenarioKey());
            if (indexA == -1) return 1;
            if (indexB == -1) return -1;
            return Integer.compare(indexA, indexB);
        });

        return new CampaignProgressResponse(currentEra, scenarioProgressList);
    }

    public GameSession createGame(CreateGameRequest request) {
        GameSession temp = new GameSession();
        temp.setTurnNumber(1);
        temp.setUsedRewardKeys(new ArrayList<>());
        RewardDefinition firstReward = roundResolutionEngine.selectRandomReward(temp);
        return gameSessionService.createGame(request, firstReward);
    }

    public GameSession forfeitGame(String gameId) {
        GameSession session = getGame(gameId);
        session.setStatus(GameStatus.FORFEITED);
        return gameSessionService.save(session);
    }

    public GameSession getGame(String gameId) {
        return gameSessionService.getGame(gameId);
    }

    public List<GameSession> listGames() {
        return gameSessionService.listGames();
    }

    public List<GameSession> listGames(String userId) {
        return gameSessionService.listGames(userId);
    }

    public TurnView getTurnView(String gameId) {
        GameSession session = getGame(gameId);
        NoConfidenceStatus noConfidence = getNoConfidenceStatus(session);
        List<CardDefinition> availableCards = getAvailableHumanCards(session);
        List<NewsDefinition> currentNews = getCurrentNews(session);
        PartyState activeHumanParty = getActiveHumanParty(session);
        MonthlyIssueDefinition currentIssue = activeHumanParty == null ? null : getCurrentIssue(session, activeHumanParty);
        
        List<HeldRewardView> activePlayerHeldRewards = new ArrayList<>();
        if (activeHumanParty != null && session.getPartyHeldRewards() != null) {
            List<HeldReward> held = session.getPartyHeldRewards().get(activeHumanParty.getId());
            if (held != null) {
                activePlayerHeldRewards = held.stream().map(HeldRewardView::from).toList();
            }
        }

        return new TurnView(
                session.getId(),
                session.getStateName(),
                session.getTurnNumber(),
                session.getMonthInCycle(),
                CYCLE_LENGTH_MONTHS - session.getMonthInCycle() + 1,
                session.getCurrentDate(),
                session.getStatus(),
                session.getParties().stream()
                        .map(party -> PartyView.from(party, session.getPlayerPartyIds()))
                        .toList(),
                activeHumanParty == null ? null : activeHumanParty.getId(),
                activeHumanParty == null ? null : activeHumanParty.getName(),
                session.getActiveHumanPlayerIndex(),
                PartyView.from(session.getGovernmentParty(), session.getPlayerPartyIds()),
                PartyView.from(session.getOppositionParty(), session.getPlayerPartyIds()),
                availableCards,
                currentNews,
                currentIssue,
                session.getPublicState(),
                noConfidence.available(),
                noConfidence.reason(),
                session.getCardUsageByParty(),
                session.getCurrentRoundSubmissions(),
                session.getLastRoundSubmissions(),
                session.getLastMetricDeltas(),
                session.getLastRoundCommentary(),
                session.getDelayedEffects(),
                session.getPendingResults(),
                session.getLastResults(),
                session.getCurrentRewardName(),
                session.getCurrentRewardDescription(),
                session.getPartyRoundWins(),
                session.getLastRoundBids(),
                session.getLastRoundBiddingMetric(),
                session.getLastRoundWinnerPartyId(),
                roundResolutionEngine.getBiddingMetricForTurn(session.getTurnNumber()),
                activePlayerHeldRewards
        );
    }

    public TurnView advanceTurn(String gameId, TurnAdvanceRequest request) {
        GameSession session = getGame(gameId);
        if (request.getSelectedCardKey() == null || request.getSelectedCardKey().isBlank()) {
            throw new IllegalArgumentException("A card must be selected before advancing turn.");
        }
        if (!getCurrentNews(session).isEmpty()
                && (request.getSelectedNewsReactions() == null || request.getSelectedNewsReactions().isEmpty())) {
            throw new IllegalArgumentException("News reactions must be selected before advancing turn.");
        }
        if (request.getSelectedIssueOptionKey() == null || request.getSelectedIssueOptionKey().isBlank()) {
            throw new IllegalArgumentException("A monthly issue response must be selected before advancing turn.");
        }

        PartyState activeHumanParty = getActiveHumanParty(session);
        if (activeHumanParty == null) {
            throw new IllegalArgumentException("No active human player found.");
        }

        // Validate bid
        String activeMetric = roundResolutionEngine.getBiddingMetricForTurn(session.getTurnNumber());
        int currentMetricValue = roundResolutionEngine.getStatValue(activeHumanParty, activeMetric);
        if (request.getBid() < 0 || request.getBid() > currentMetricValue) {
            throw new IllegalArgumentException("Bid of " + request.getBid() + " is invalid. Must be between 0 and your current " + activeMetric + " (" + currentMetricValue + ").");
        }

        // Validate optional reward play
        if (request.getSelectedRewardKey() != null && !request.getSelectedRewardKey().isBlank()) {
            List<HeldReward> heldList = session.getPartyHeldRewards().get(activeHumanParty.getId());
            boolean holds = false;
            if (heldList != null) {
                for (HeldReward hr : heldList) {
                    if (hr.getRewardKey().equals(request.getSelectedRewardKey())) {
                        holds = true;
                        break;
                    }
                }
            }
            if (!holds) {
                throw new IllegalArgumentException("You do not possess the reward: " + request.getSelectedRewardKey());
            }

            RewardDefinition rewardDef = RoundResolutionEngine.REWARD_POOL.stream()
                .filter(r -> r.key().equals(request.getSelectedRewardKey()))
                .findFirst().orElse(null);
            if (rewardDef != null && rewardDef.requiresTarget()) {
                if (request.getRewardTargetPartyId() == null || request.getRewardTargetPartyId().isBlank()) {
                    throw new IllegalArgumentException("Target party is required for playing reward: " + rewardDef.name());
                }
                PartyState target = findParty(session, request.getRewardTargetPartyId());
                if ("opponent".equals(rewardDef.allowedTargets()) && target.getId().equals(activeHumanParty.getId())) {
                    throw new IllegalArgumentException("Cannot target yourself with this reward.");
                }
                if ("self".equals(rewardDef.allowedTargets()) && !target.getId().equals(activeHumanParty.getId())) {
                    throw new IllegalArgumentException("Must target yourself with this reward.");
                }
            }
        }

        CardDefinition selectedCard = findAvailableCard(session, request.getSelectedCardKey(), activeHumanParty);
        PartyState targetParty = resolveTargetParty(session, activeHumanParty, selectedCard, request.getTargetPartyId());
        MonthlyIssueDefinition selectedIssue = getCurrentIssue(session, activeHumanParty);
        IssueOptionDefinition selectedIssueOption = findIssueOption(selectedIssue, request.getSelectedIssueOptionKey());
        session.getCurrentRoundSubmissions().removeIf(submission -> submission.getPartyId().equals(activeHumanParty.getId()));
        
        RoundSubmission sub = toSubmission(
                activeHumanParty,
                targetParty,
                selectedCard,
                request.getSelectedNewsReactions(),
                selectedIssue,
                selectedIssueOption
        );
        sub.setBid(request.getBid());
        sub.setSelectedRewardKey(request.getSelectedRewardKey());
        if (request.getSelectedRewardKey() != null && !request.getSelectedRewardKey().isBlank()) {
            sub.setRewardTargetPartyId(request.getRewardTargetPartyId());
            if (request.getRewardTargetPartyId() != null) {
                PartyState rTarget = findParty(session, request.getRewardTargetPartyId());
                sub.setRewardTargetPartyName(rTarget.getName());
            }
            RewardDefinition rDef = RoundResolutionEngine.REWARD_POOL.stream()
                .filter(r -> r.key().equals(request.getSelectedRewardKey()))
                .findFirst().orElse(null);
            if (rDef != null) {
                sub.setRewardName(rDef.name());
            }
        }
        session.getCurrentRoundSubmissions().add(sub);

        if (session.getCurrentRoundSubmissions().size() < session.getPlayerPartyIds().size()) {
            session.setActiveHumanPlayerIndex(session.getActiveHumanPlayerIndex() + 1);
            gameSessionService.save(session);
            return getTurnView(gameId);
        }

        addComputerSubmissions(session);
        boolean noConfidencePlayed = roundResolutionEngine.resolveRound(session);
        boolean noConfidenceSucceeded = false;
        if (noConfidencePlayed) {
            PartyState humanParty = session.getParties().stream()
                .filter(p -> p.getControllerType() == com.politicalsim.party.ControllerType.HUMAN)
                .findFirst().orElse(null);
            PartyState govParty = session.getGovernmentParty();
            if (humanParty != null && govParty != null && humanParty.getStats().getPublicSupport() > govParty.getStats().getPublicSupport()) {
                noConfidenceSucceeded = true;
            } else {
                session.getLastRoundCommentary().add("The Opposition's No-Confidence Motion failed to gather enough support. The government survives the vote and continues in office.");
                session.setLastResults(List.of("No-Confidence Motion failed: Government survives."));
            }
        }

        boolean electionHeld = (noConfidencePlayed && noConfidenceSucceeded) || session.getMonthInCycle() >= CYCLE_LENGTH_MONTHS;
        if (electionHeld) {
            roundResolutionEngine.conductElection(session, noConfidencePlayed ? "No-confidence motion triggered an early election." : "Mandatory 60-month election completed.", noConfidencePlayed);
            session.setMonthInCycle(1);
        } else {
            session.setMonthInCycle(session.getMonthInCycle() + 1);
        }
        session.setTurnNumber(session.getTurnNumber() + 1);
        session.setCurrentDate(session.getCurrentDate().plusMonths(1));
        session.setActiveHumanPlayerIndex(0);
        session.setCurrentRoundSubmissions(new ArrayList<>());
        gameSessionService.save(session);
        return getTurnView(gameId);
    }

    private PartyState getActiveHumanParty(GameSession session) {
        if (session.getPlayerPartyIds().isEmpty()) {
            return null;
        }
        int activeIndex = Math.min(session.getActiveHumanPlayerIndex(), session.getPlayerPartyIds().size() - 1);
        String activePartyId = session.getPlayerPartyIds().get(activeIndex);
        return session.getParties().stream()
                .filter(party -> party.getId().equals(activePartyId))
                .findFirst()
                .orElse(null);
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
        return getCardsForSession(session).stream()
                .filter(CardDefinition::isActive)
                .filter(card -> card.getCardKey().equals(cardKey))
                .filter(card -> card.getRoleAllowed().contains(role.name()))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Card not available for party role: " + cardKey));
    }

    private CardDefinition findAvailableCard(GameSession session, String cardKey, PartyState party) {
        CardDefinition card = findCard(session, cardKey, party.getRole());
        if (usedCount(session, party, card) >= card.getMaxUsesPerCycle()) {
            throw new IllegalArgumentException("Card has no uses remaining this election cycle: " + cardKey);
        }
        return card;
    }

    private PartyState resolveTargetParty(GameSession session, PartyState actor, CardDefinition card, String targetPartyId) {
        if (!requiresTarget(card)) {
            return null;
        }
        if (targetPartyId == null || targetPartyId.isBlank()) {
            throw new IllegalArgumentException("A target party must be selected for this card.");
        }
        PartyState target = findParty(session, targetPartyId);
        if (target.getId().equals(actor.getId())) {
            throw new IllegalArgumentException("A card target must be another party.");
        }
        return target;
    }

    private PartyState chooseAiTarget(GameSession session, PartyState actor, CardDefinition card) {
        if (!requiresTarget(card)) {
            return null;
        }
        return chooseOpponent(session, actor);
    }

    private boolean requiresTarget(CardDefinition card) {
        Object declaredTarget = card.getTarget().get("opponentParty");
        return Boolean.TRUE.equals(declaredTarget) || !partyEffect(card.getVisibleEffects(), "opponentParty").isEmpty();
    }

    @SuppressWarnings("unchecked")
    private Map<String, Object> partyEffect(Map<String, Object> effects, String key) {
        Object value = effects.get(key);
        if (value instanceof Map<?, ?> map) {
            return (Map<String, Object>) map;
        }
        return Map.of();
    }

    private RoundSubmission toSubmission(PartyState party, PartyState targetParty, CardDefinition card, Map<String, String> newsReactions,
            MonthlyIssueDefinition issue, IssueOptionDefinition issueOption) {
        RoundSubmission submission = new RoundSubmission();
        submission.setPartyId(party.getId());
        submission.setPartyName(party.getName());
        if (targetParty != null) {
            submission.setTargetPartyId(targetParty.getId());
            submission.setTargetPartyName(targetParty.getName());
        }
        submission.setCardKey(card.getCardKey());
        submission.setCardName(card.getName());
        submission.setNewsReactions(new LinkedHashMap<>(newsReactions));
        if (issue != null && issueOption != null) {
            submission.setIssueKey(issue.getIssueKey());
            submission.setIssueTitle(issue.getTitle());
            submission.setIssueOptionKey(issueOption.getOptionKey());
            submission.setIssueOptionText(issueOption.getText());
        }
        return submission;
    }

    private void addComputerSubmissions(GameSession session) {
        for (PartyState party : session.getParties()) {
            if (party.getControllerType() != ControllerType.COMPUTER) {
                continue;
            }
            if (!party.isActive()) {
                continue;
            }
            if (session.getCurrentRoundSubmissions().stream().anyMatch(s -> s.getPartyId().equals(party.getId()))) {
                continue;
            }
            PartyState opponent = chooseOpponent(session, party);
            AiDecision decision = aiDecisionService.chooseCard(session, party, opponent, getAvailableCardsForParty(session, party));
            Map<String, String> reactions = new LinkedHashMap<>();
            for (NewsDefinition news : getCurrentNews(session)) {
                NewsReactionDefinition reaction = aiDecisionService.chooseReaction(party, decision.intent(), news.getReactionOptions());
                if (reaction != null) {
                    reactions.put(news.getNewsKey(), reaction.getReactionKey());
                }
            }
            MonthlyIssueDefinition issue = getCurrentIssue(session, party);
            IssueOptionDefinition issueOption = chooseComputerIssueOption(party, issue);
            PartyState targetParty = chooseAiTarget(session, party, decision.card());
            RoundSubmission submission = toSubmission(party, targetParty, decision.card(), reactions, issue, issueOption);
            submission.setAiIntent(decision.intent().name());

            // AI Bid Selection
            String metric = roundResolutionEngine.getBiddingMetricForTurn(session.getTurnNumber());
            int currentMetricValue = roundResolutionEngine.getStatValue(party, metric);
            int bid = calculateSmartBid(session, party, metric, currentMetricValue);
            submission.setBid(bid);

            // AI Reward Play Selection
            List<HeldReward> heldRewards = session.getPartyHeldRewards().get(party.getId());
            if (heldRewards != null && !heldRewards.isEmpty()) {
                if (new Random().nextBoolean()) {
                    HeldReward hr = heldRewards.get(0);
                    submission.setSelectedRewardKey(hr.getRewardKey());
                    submission.setRewardName(hr.getName());
                    if (hr.isRequiresTarget()) {
                        PartyState rTarget = null;
                        if ("opponent".equals(hr.getAllowedTargets())) {
                            rTarget = opponent;
                        } else if ("self".equals(hr.getAllowedTargets())) {
                            rTarget = party;
                        } else {
                            rTarget = new Random().nextBoolean() ? party : opponent;
                        }
                        if (rTarget != null) {
                            submission.setRewardTargetPartyId(rTarget.getId());
                            submission.setRewardTargetPartyName(rTarget.getName());
                        }
                    }
                }
            }

            session.getCurrentRoundSubmissions().add(submission);
        }
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

    private MonthlyIssueDefinition getCurrentIssue(GameSession session, PartyState party) {
        List<MonthlyIssueDefinition> issues = getIssuesForSession(session).stream()
                .filter(MonthlyIssueDefinition::isActive)
                .filter(issue -> issue.getRoleAllowed().contains(party.getRole().name()))
                .sorted(Comparator.comparing(MonthlyIssueDefinition::getIssueKey))
                .toList();
        if (issues.isEmpty()) {
            return fallbackIssue(party);
        }
        int partyOffset = Math.floorMod(party.getId().hashCode(), issues.size());
        int index = Math.floorMod(session.getTurnNumber() - 1 + partyOffset, issues.size());
        return issues.get(index);
    }

    private IssueOptionDefinition findIssueOption(MonthlyIssueDefinition issue, String optionKey) {
        return issue.getOptions().stream()
                .filter(option -> option.getOptionKey().equals(optionKey))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Issue option not available: " + optionKey));
    }

    private IssueOptionDefinition chooseComputerIssueOption(PartyState party, MonthlyIssueDefinition issue) {
        return issue.getOptions().stream()
                .max((left, right) -> Double.compare(scoreIssueOption(party, left), scoreIssueOption(party, right)))
                .orElseThrow(() -> new IllegalArgumentException("Issue has no options: " + issue.getIssueKey()));
    }

    private double scoreIssueOption(PartyState party, IssueOptionDefinition option) {
        Map<String, Object> effects = partyEffect(option.getEffects(), "selfParty");
        double score = 0;
        score += intValue(effects.get("coins")) * 0.25;
        score += intValue(effects.get("partyMorale")) * 2.0;
        score += intValue(effects.get("mediaImage")) * 2.0;
        score += intValue(effects.get("publicSupport")) * 4.0;
        score -= intValue(effects.get("corruptionScore")) * 3.0;
        if (party.getStats().getCoins() < 80) {
            score += Math.max(0, intValue(effects.get("coins"))) * 0.4;
        }
        if (party.getStats().getCorruptionScore() > 40) {
            score -= Math.max(0, intValue(effects.get("corruptionScore"))) * 2.0;
        }
        score -= intValue(option.getRisk().get("chance")) * 0.05;
        return score;
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

    private NoConfidenceStatus getNoConfidenceStatus(GameSession session) {
        boolean playerIsOpposition = session.getPlayerPartyIds().contains(session.getOppositionParty().getId());
        if (!playerIsOpposition) {
            return new NoConfidenceStatus(false, "Only a human-controlled opposition can call no-confidence.");
        }

        PartyStats stats = session.getGovernmentParty().getStats();
        if (stats.getPublicSupport() >= NO_CONFIDENCE_SUPPORT_THRESHOLD) {
            return new NoConfidenceStatus(false, "Government public support is at or above 30%.");
        }
        if (stats.getPartyMorale() >= NO_CONFIDENCE_MORALE_THRESHOLD) {
            return new NoConfidenceStatus(false, "Government party morale is not low enough.");
        }
        return new NoConfidenceStatus(true, "Government is vulnerable.");
    }

    private List<CardDefinition> getAvailableHumanCards(GameSession session) {
        PartyState activeHumanParty = getActiveHumanParty(session);
        if (activeHumanParty == null) {
            return List.of();
        }
        return getAvailableCardsForParty(session, activeHumanParty);
    }

    private List<CardDefinition> getAvailableCardsForParty(GameSession session, PartyState party) {
        List<CardDefinition> cards = new java.util.ArrayList<>(
            getCardsForSession(session).stream()
                .filter(CardDefinition::isActive)
                .filter(card -> card.getRoleAllowed().contains(party.getRole().name()))
                .filter(card -> usedCount(session, party, card) < card.getMaxUsesPerCycle())
                .filter(card -> party.getStats().getCoins() >= card.getCost())
                .toList()
        );
        
        CardDefinition noCard = new CardDefinition();
        noCard.setCardKey("no_card");
        noCard.setName("No Card (Pass Turn)");
        noCard.setCategory("governance");
        noCard.setCost(0);
        noCard.setMaxUsesPerCycle(9999);
        noCard.setActive(true);
        noCard.setRoleAllowed(List.of(party.getRole().name()));
        noCard.setTarget(new LinkedHashMap<>());
        noCard.setVisibleEffects(new LinkedHashMap<>());
        noCard.setHiddenEffects(new LinkedHashMap<>());
        noCard.setRiskRoll(new LinkedHashMap<>());
        noCard.setIdeologyTags(new LinkedHashMap<>());
        noCard.setTiming(new LinkedHashMap<>());
        noCard.setWeights(new LinkedHashMap<>());
        cards.add(0, noCard);
        
        return cards;
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

    private PartyState chooseOpponent(GameSession session, PartyState actor) {
        return session.getParties().stream()
                .filter(PartyState::isActive)
                .filter(party -> !party.getId().equals(actor.getId()))
                .max(Comparator.comparingInt(party -> party.getStats().getPublicSupport()))
                .orElse(null);
    }

    private int calculateSmartBid(GameSession session, PartyState party, String metric, int currentMetricValue) {
        int cycleTurn = ((session.getTurnNumber() - 1) % 5) + 1; // 1 to 5
        int remainingTurns = 5 - cycleTurn;
        int myWins = session.getPartyRoundWins().getOrDefault(party.getId(), 0);
        
        int leaderWins = 0;
        for (Map.Entry<String, Integer> entry : session.getPartyRoundWins().entrySet()) {
            if (!entry.getKey().equals(party.getId())) {
                leaderWins = Math.max(leaderWins, entry.getValue());
            }
        }
        
        int overallMaxWins = Math.max(myWins, leaderWins);
        
        // 1. If any party has already won 3 rounds, cycle is decided. Bid 0.
        if (overallMaxWins >= 3) {
            return 0;
        }
        
        // 2. If we cannot win or tie, save resources. Bid 0.
        if (myWins + remainingTurns < leaderWins) {
            return 0;
        }
        
        // 3. Resource-safe bid calculation
        if (currentMetricValue <= 0) {
            return 0;
        }
        
        AiStyle style = party.getAiProfile() != null ? party.getAiProfile().getStyle() : AiStyle.BALANCED_STRATEGIST;
        int coinReserve = 30;
        int moraleReserve = 20;
        int supportReserve = 15;
        double bidMultiplier = 1.0;
        int maxCoinBidLimit = 15;
        int maxMoraleBidLimit = 20;
        int maxSupportBidLimit = 3;

        if (style == AiStyle.STRENGTH_BUILDER) {
            coinReserve = 40;
            moraleReserve = 30;
            bidMultiplier = 0.6;
        } else if (style == AiStyle.LATE_STRIKER) {
            if (session.getTurnNumber() < 40) {
                coinReserve = 35;
                moraleReserve = 25;
                bidMultiplier = 0.5;
            } else {
                coinReserve = 15;
                moraleReserve = 10;
                bidMultiplier = 1.5;
                maxCoinBidLimit = 22;
                maxMoraleBidLimit = 28;
                maxSupportBidLimit = 4;
            }
        } else if (style == AiStyle.AGGRESSIVE_BIDDER) {
            coinReserve = 15;
            moraleReserve = 10;
            bidMultiplier = 1.6;
            maxCoinBidLimit = 25;
            maxMoraleBidLimit = 35;
            maxSupportBidLimit = 6;
        }

        int bid = 0;
        if ("COINS".equalsIgnoreCase(metric)) {
            int usable = Math.max(0, currentMetricValue - coinReserve);
            if (usable > 0) {
                int minBid = Math.max(1, (int) Math.ceil(usable * 0.05 * bidMultiplier));
                int maxBid = Math.min(maxCoinBidLimit, (int) (usable * 0.20 * bidMultiplier));
                maxBid = Math.max(minBid, maxBid);
                if (maxBid > minBid) {
                    bid = minBid + new Random().nextInt(maxBid - minBid + 1);
                } else {
                    bid = minBid;
                }
            }
        } else if ("PARTY_MORALE".equalsIgnoreCase(metric) || "MORALE".equalsIgnoreCase(metric)) {
            int usable = Math.max(0, currentMetricValue - moraleReserve);
            if (usable > 0) {
                int minBid = Math.max(1, (int) Math.ceil(usable * 0.05 * bidMultiplier));
                int maxBid = Math.min(maxMoraleBidLimit, (int) (usable * 0.25 * bidMultiplier));
                maxBid = Math.max(minBid, maxBid);
                if (maxBid > minBid) {
                    bid = minBid + new Random().nextInt(maxBid - minBid + 1);
                } else {
                    bid = minBid;
                }
            }
        } else if ("PUBLIC_SUPPORT".equalsIgnoreCase(metric) || "SUPPORT".equalsIgnoreCase(metric)) {
            int usable = Math.max(0, currentMetricValue - supportReserve);
            if (usable > 0) {
                int maxPossibleBid = Math.min(maxSupportBidLimit, usable);
                if (maxPossibleBid > 0) {
                    bid = 1 + new Random().nextInt(maxPossibleBid);
                }
            }
        } else {
            int minBid = (int) Math.ceil(currentMetricValue * 0.02 * bidMultiplier);
            int maxBid = (int) (currentMetricValue * 0.10 * bidMultiplier);
            maxBid = Math.max(minBid, maxBid);
            if (maxBid > minBid) {
                bid = minBid + new Random().nextInt(maxBid - minBid + 1);
            } else {
                bid = minBid;
            }
        }
        
        return Math.min(bid, currentMetricValue);
    }

    private PartyState findParty(GameSession session, String partyId) {
        return session.getParties().stream()
                .filter(party -> party.getId().equals(partyId))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Party not found: " + partyId));
    }

    private Map<String, Map<String, Integer>> initialCardUsage(List<PartyState> parties) {
        Map<String, Map<String, Integer>> usage = new LinkedHashMap<>();
        for (PartyState party : parties) {
            usage.put(party.getId(), new LinkedHashMap<>());
        }
        return usage;
    }

    private int intValue(Object value) {
        if (value instanceof Number number) {
            return number.intValue();
        }
        return 0;
    }

    private List<CardDefinition> getCardsForScenario(String scenarioKey) {
        return DefinitionCache.cardsCache.computeIfAbsent(scenarioKey, key -> {
            List<CardDefinition> cards = cardRepository.findByScenarioKeyOrderByCategoryAscNameAsc(key);
            if (cards.isEmpty()) {
                cards = cardRepository.findByScenarioKeyOrderByCategoryAscNameAsc("west_bengal_2000");
            }
            return cards;
        });
    }

    private List<NewsDefinition> getNewsForScenario(String scenarioKey) {
        return DefinitionCache.newsCache.computeIfAbsent(scenarioKey, key -> {
            List<NewsDefinition> news = newsRepository.findByScenarioKeyOrderByTypeAscTitleAsc(key);
            if (news.isEmpty()) {
                news = newsRepository.findByScenarioKeyOrderByTypeAscTitleAsc("west_bengal_2000");
            }
            return news;
        });
    }

    private List<MonthlyIssueDefinition> getIssuesForScenario(String scenarioKey) {
        return DefinitionCache.issuesCache.computeIfAbsent(scenarioKey, key -> {
            List<MonthlyIssueDefinition> issues = issueRepository.findByScenarioKeyOrderByCategoryAscTitleAsc(key);
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

    private record NoConfidenceStatus(boolean available, String reason) {
    }
}
