package com.politicalsim.game;

import com.politicalsim.ai.*;
import com.politicalsim.api.CreateGameRequest;
import com.politicalsim.api.PartyView;
import com.politicalsim.api.TurnView;
import com.politicalsim.api.TurnAdvanceRequest;
import com.politicalsim.api.HeldRewardView;
import com.politicalsim.api.CampaignProgressResponse;
import com.politicalsim.api.ScenarioProgressView;
import com.politicalsim.api.GameSessionSummary;
import com.politicalsim.content.*;
import com.politicalsim.party.ControllerType;
import com.politicalsim.party.PartyRole;
import com.politicalsim.party.PartyState;
import com.politicalsim.party.PartyStats;
import com.politicalsim.party.ProjectState;
import com.politicalsim.party.BuildingProject;
import com.politicalsim.party.PartyManagementState;
import com.politicalsim.party.PartyManagementRepository;
import com.politicalsim.party.PostsConfig;
import com.politicalsim.party.ScheduledPost;
import java.time.LocalDate;
import java.util.*;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class GameService {

    private static final Logger log = LoggerFactory.getLogger(GameService.class);

    private static final int CYCLE_LENGTH_MONTHS = 60;
    private static final int NO_CONFIDENCE_SUPPORT_THRESHOLD = 30;
    private static final int NO_CONFIDENCE_MORALE_THRESHOLD = 35;

    private final GameSessionService gameSessionService;
    private final RoundResolutionEngine roundResolutionEngine;
    private final CardDefinitionRepository cardRepository;
    private final NewsDefinitionRepository newsRepository;
    private final ScenarioDefinitionRepository scenarioRepository;
    private final AiDecisionService aiDecisionService;
    private final CooperationResolver cooperationResolver;
    private final com.politicalsim.ai.BrokeFightBackService brokeFightBackService;
    private final LegislativeAiService legislativeAiService;
    private final PartyManagementRepository partyManagementRepository;

    public GameService(
            GameSessionService gameSessionService,
            RoundResolutionEngine roundResolutionEngine,
            CardDefinitionRepository cardRepository,
            NewsDefinitionRepository newsRepository,
            ScenarioDefinitionRepository scenarioRepository,
            AiDecisionService aiDecisionService,
            com.politicalsim.ai.BrokeFightBackService brokeFightBackService
    ) {
        this(gameSessionService, roundResolutionEngine, cardRepository, newsRepository, scenarioRepository, aiDecisionService, brokeFightBackService, new LegislativeAiService(null), null);
    }

    @Autowired
    public GameService(
            GameSessionService gameSessionService,
            RoundResolutionEngine roundResolutionEngine,
            CardDefinitionRepository cardRepository,
            NewsDefinitionRepository newsRepository,
            ScenarioDefinitionRepository scenarioRepository,
            AiDecisionService aiDecisionService,
            com.politicalsim.ai.BrokeFightBackService brokeFightBackService,
            LegislativeAiService legislativeAiService,
            PartyManagementRepository partyManagementRepository
    ) {
        this.gameSessionService = gameSessionService;
        this.roundResolutionEngine = roundResolutionEngine;
        this.cardRepository = cardRepository;
        this.newsRepository = newsRepository;
        this.scenarioRepository = scenarioRepository;
        this.aiDecisionService = aiDecisionService;
        this.brokeFightBackService = brokeFightBackService;
        this.legislativeAiService = legislativeAiService != null ? legislativeAiService : new LegislativeAiService(null);
        this.partyManagementRepository = partyManagementRepository;
        this.cooperationResolver = new CooperationResolver(this);
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

        List<GameSessionRepository.ProgressGameDTO> userGames = new ArrayList<>();
        long start = System.currentTimeMillis();
        if (userId != null && !userId.isBlank() && !"null".equalsIgnoreCase(userId) && !"undefined".equalsIgnoreCase(userId)) {
            userGames = gameSessionService.listProgressGames(userId.trim().toLowerCase());
        }

        long endMethod = System.currentTimeMillis();
        log.info("listGames loaded in ms: {}" ,(endMethod - start));

        List<String> wonScenarioKeys = new ArrayList<>();
        for (GameSessionRepository.ProgressGameDTO g : userGames) {
            String skey = g.scenarioKey();
            if (g.status() == GameStatus.VICTORY) {
                wonScenarioKeys.add(skey);
            } else if (g.status() == GameStatus.GAME_OVER) {
                GameSessionRepository.ProgressPartyDTO gov = g.governmentParty();
                if (gov != null && g.playerPartyIds() != null && g.playerPartyIds().contains(gov.id())) {
                    wonScenarioKeys.add(skey);
                }
            }
        }


        List<ScenarioProgressView> scenarioProgressList = new ArrayList<>();
        for (ScenarioDefinition s : activeScenarios) {
            String key = s.getScenarioKey();
            if (key == null) continue;

            int year= com.politicalsim.util.ScenarioKeyParser.extractYear(s.getScenarioKey());

            boolean prerequisiteWon = year<=2001 ? true : wonScenarioKeys.contains(getPrecedingScenarioKey(s.getScenarioKey()));


            // Check for an active (in-progress) game first
            boolean hasActive = false;
            for (GameSessionRepository.ProgressGameDTO g : userGames) {
                if (key.equals(g.scenarioKey()) && g.status() == GameStatus.ACTIVE) {
                    hasActive = true;
                    break;
                }
            }

            String status;
            if (hasActive) {
                status = "IN_PROGRESS";
            } else if (wonScenarioKeys.contains(key)) {
                status = "WON";
            } else if ( !prerequisiteWon) {

                status = "LOCKED";
            } else {

                status = "AVAILABLE";
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


        return new CampaignProgressResponse(0, scenarioProgressList);
    }

    public GameSession createGame(CreateGameRequest request) {
        long start = System.currentTimeMillis();
        GameSession temp = new GameSession();
        temp.setTurnNumber(1);
        temp.setUsedRewardKeys(new ArrayList<>());
        RewardDefinition firstReward = roundResolutionEngine.selectRandomReward(temp);
        
        long step1 = System.currentTimeMillis();
        GameSession session = gameSessionService.createGame(request, firstReward);
        log.info("[METRIC] gameSessionService.createGame took {} ms", (System.currentTimeMillis() - step1));


        long step3 = System.currentTimeMillis();
        if (request.isRetainInstitutions()) {
            GameSessionRepository.GameSessionDTO preceding = findPrecedingWonSession(request.getUserId(), request.getScenarioKey());
            if (preceding != null) {
                List<String> completedProjectKeys = new ArrayList<>();
                if (preceding.playerPartyIds() != null) {
                    for (String pid : preceding.playerPartyIds()) {
                        PartyState pState = preceding.parties().stream()
                                .filter(p -> p.getId().equals(pid))
                                .findFirst().orElse(null);
                        if (pState != null && pState.getProjects() != null) {
                            for (ProjectState proj : pState.getProjects()) {
                                if (proj.getProgressPercent() >= 100) {
                                    completedProjectKeys.add(proj.getProjectKey());
                                }
                            }
                        }
                    }
                }

                List<String> uniqueCompletedProjectKeys = completedProjectKeys.stream().distinct().toList();
                List<String> projectsToRetain = aiDecisionService.rankAndSelectProjectsToRetain(uniqueCompletedProjectKeys);

                if (!projectsToRetain.isEmpty()) {
                    PartyState playerParty = session.getParties().stream()
                            .filter(p -> p.getId().equals(session.getPlayerPartyId()))
                            .findFirst().orElse(null);
                    if (playerParty != null && playerParty.getProjects() != null) {
                        for (String key : projectsToRetain) {
                            for (ProjectState proj : playerParty.getProjects()) {
                                if (key.equals(proj.getProjectKey())) {
                                    proj.setProgressPercent(100);
                                    if (proj.getCompletionTurn() == 0) {
                                        proj.setCompletionTurn(session.getTurnNumber());
                                    }
                                    proj.setJustCompleted(false);
                                }
                            }
                        }
                        gameSessionService.save(session);
                    }
                }
            }
        }
        log.info("[METRIC] Retain institutions took {} ms", (System.currentTimeMillis() - step3));
        log.info("[METRIC] Total createGame took {} ms", (System.currentTimeMillis() - start));

        // Initialise PartyManagementState for every player party in this game
        initPartyManagementStates(session);

        return session;
    }

    /**
     * Called once when a new game is created. For every player party, generates a
     * PartyManagementState with pre-scheduled posts (shuffled, one per 5 turns) and
     * saves it to MongoDB.
     */
    private void initPartyManagementStates(GameSession session) {
        if (partyManagementRepository == null) return;
        // Delete any stale state for this game (e.g. re-start)
        partyManagementRepository.deleteByGameId(session.getId());
        for (String partyId : session.getPlayerPartyIds()) {
            PartyManagementState pms = new PartyManagementState(session.getId(), partyId);
            pms.setPosts(PostsConfig.buildScheduledPosts());
            partyManagementRepository.save(pms);
        }
    }

    /**
     * Called during turn resolution to:
     * 1. Unlock PENDING posts that have reached their scheduled turn.
     * 2. Apply the player's submitted allocations from the UI:
     *    - patronageUsed: how many patronage cards were placed on factions this turn
     *    - postAssignments: map of { postKey -> factionKey } for posts placed this turn
     * 3. Grant +1 patronage point for the NEXT turn.
     * Saves the updated PartyManagementState to MongoDB.
     */
    public void updatePartyManagementOnTurn(GameSession session, String partyId,
                                             java.util.Map<String, Object> allocations,
                                             int resolvedTurnNumber) {
        if (partyManagementRepository == null) return;

        PartyManagementState pms = partyManagementRepository
                .findByGameIdAndPartyId(session.getId(), partyId)
                .orElse(null);
        if (pms == null) {
            // Auto-create for games that existed before this feature
            pms = new PartyManagementState(session.getId(), partyId);
            pms.setPosts(PostsConfig.buildScheduledPosts());
        }

        // 1. Unlock posts whose scheduled turn has arrived (before applying allocations)
        for (ScheduledPost sp : pms.getPosts()) {
            if (sp.getStatus() == ScheduledPost.Status.PENDING
                    && sp.getAvailableOnTurn() <= resolvedTurnNumber) {
                sp.setStatus(ScheduledPost.Status.AVAILABLE);
            }
        }

        // 2. Apply submitted allocations
        int patronageConsumedThisTurn = 0;
        if (allocations != null && !allocations.isEmpty()) {

            // -- Patronage: how many patronage cards were dragged onto factions this turn
            Object patronageUsedObj = allocations.get("patronageUsed");
            if (patronageUsedObj instanceof Number) {
                patronageConsumedThisTurn = ((Number) patronageUsedObj).intValue();
            }

            // -- Posts: { postKey -> factionKey }
            Object postAssignmentsObj = allocations.get("postAssignments");
            if (postAssignmentsObj instanceof java.util.Map<?, ?> postMap) {
                for (ScheduledPost sp : pms.getPosts()) {
                    Object factionKeyObj = postMap.get(sp.getPostKey());
                    if (factionKeyObj instanceof String factionKey && !factionKey.isBlank()) {
                        sp.setStatus(ScheduledPost.Status.ASSIGNED);
                        sp.setAssignedFactionKey(factionKey);
                        log.info("[PartyMgmt] Post '{}' assigned to faction '{}' for party '{}'",
                                sp.getPostKey(), factionKey, partyId);
                    }
                }
            }

            // -- Factions: sync loyalty, influence, post, patronage into PartyState and PMS map
            @SuppressWarnings("unchecked")
            java.util.List<java.util.Map<String, Object>> factionsData =
                    (java.util.List<java.util.Map<String, Object>>) allocations.get("factions");
            if (factionsData != null && !factionsData.isEmpty()) {
                com.politicalsim.party.PartyState party = session.getParties().stream()
                        .filter(p -> p.getId().equals(partyId)).findFirst().orElse(null);
                java.util.Map<String, Integer> patronageMap = new java.util.HashMap<>();
                if (party != null) {
                    for (java.util.Map<String, Object> fData : factionsData) {
                        String fKey = (String) fData.get("key");
                        if (fKey == null) continue;
                        com.politicalsim.party.FactionState fs = party.getFactions().stream()
                                .filter(f -> f.getKey().equals(fKey)).findFirst().orElse(null);
                        if (fs != null) {
                            if (fData.get("loyalty")   instanceof Number n) fs.setLoyalty(n.intValue());
                            if (fData.get("influence") instanceof Number n) fs.setInfluence(n.intValue());
                            Object postVal = fData.get("post");
                            if (postVal instanceof List<?> list) {
                                fs.setPost(list.stream().map(Object::toString).toList());
                            } else if (postVal instanceof String s) {
                                if ("None".equals(s) || s.isBlank()) {
                                    fs.setPost(new ArrayList<>());
                                } else {
                                    fs.setPost(Arrays.asList(s.split(",\\s*")));
                                }
                            }
                            if (fData.get("active")    instanceof Boolean b) fs.setActive(b);
                            int incomingPatronage = (fData.get("patronage") instanceof Number n) ? n.intValue() : 0;
                            fs.setPatronage(incomingPatronage);
                            patronageMap.put(fKey, incomingPatronage);
                        }
                    }
                }
                // Store patronage keyed by faction key for next-turn rehydration
                pms.setAllocatedPatronagePoints(patronageMap);
            }
        }

        // Deduct what was actually consumed this turn, bounded to 0
        int currentUnallocated = pms.getUnallocatedPatronagePoints();
        int afterDeduction = Math.max(0, currentUnallocated - patronageConsumedThisTurn);
        // Grant +1 for the next turn
        pms.setUnallocatedPatronagePoints(afterDeduction + 1);

        log.info("[PartyMgmt] Party '{}' turn {}: consumed {} patronage, {} remaining + 1 new = {}",
                partyId, resolvedTurnNumber, patronageConsumedThisTurn,
                afterDeduction, pms.getUnallocatedPatronagePoints());

        partyManagementRepository.save(pms);
    }

    /**
     * Convenience method to fetch PartyManagementState for the active human party.
     */
    public PartyManagementState getPartyManagementState(String gameId, String partyId) {
        if (partyManagementRepository == null) return null;
        return partyManagementRepository.findByGameIdAndPartyId(gameId, partyId).orElse(null);
    }

    /**
     * Immediately persists the player's card allocation choices to MongoDB.
     * Called when the player clicks "Lock Allocations" in Action 3.
     * This eliminates the need for localStorage as the source of truth.
     *
     * Returns the updated PartyManagementState so the frontend can refresh.
     */
    public com.politicalsim.party.PartyManagementState lockPartyManagement(
            String gameId, String partyId, com.politicalsim.api.PartyManagementLockRequest req) {

        if (partyManagementRepository == null) {
            throw new IllegalStateException("Party management repository not available.");
        }

        GameSession session = getGame(gameId);
        com.politicalsim.party.PartyManagementState pms = partyManagementRepository
                .findByGameIdAndPartyId(gameId, partyId)
                .orElseGet(() -> {
                    com.politicalsim.party.PartyManagementState newPms =
                            new com.politicalsim.party.PartyManagementState(gameId, partyId);
                    newPms.setPosts(com.politicalsim.party.PostsConfig.buildScheduledPosts());
                    return newPms;
                });

        // Apply post assignments
        if (req.getPostAssignments() != null && !req.getPostAssignments().isEmpty()) {
            for (com.politicalsim.party.ScheduledPost sp : pms.getPosts()) {
                String factionKey = req.getPostAssignments().get(sp.getPostKey());
                if (factionKey != null && !factionKey.isBlank()) {
                    sp.setStatus(com.politicalsim.party.ScheduledPost.Status.ASSIGNED);
                    sp.setAssignedFactionKey(factionKey);
                    log.info("[PartyMgmt Lock] Post '{}' assigned to faction '{}'", sp.getPostKey(), factionKey);
                }
            }
        }

        // Deduct consumed patronage points
        int consumed = req.getPatronageUsed();
        int remaining = Math.max(0, pms.getUnallocatedPatronagePoints() - consumed);
        pms.setUnallocatedPatronagePoints(remaining);
        log.info("[PartyMgmt Lock] Party '{}': {} patronage consumed, {} remaining", partyId, consumed, remaining);

        Map<String,Integer> assignedPointsMap = new HashMap<>();
        // Apply faction state snapshot (loyalty, influence, post, patronage)
        if (req.getFactions() != null && !req.getFactions().isEmpty()) {
            for (java.util.Map<String, Object> fData : req.getFactions()) {
                String fKey = (String) fData.get("key");
                com.politicalsim.party.PartyState party = session.getParties().stream()
                        .filter(p -> p.getId().equals(partyId)).findFirst().orElse(null);
                if (party != null && fKey != null) {
                    com.politicalsim.party.FactionState fs = party.getFactions().stream()
                            .filter(f -> f.getKey().equals(fKey)).findFirst().orElse(null);
                    if (fs != null) {
                        // Apply incoming values from payload FIRST
                        if (fData.get("loyalty")   instanceof Number n) fs.setLoyalty(n.intValue());
                        if (fData.get("influence") instanceof Number n) fs.setInfluence(n.intValue());
                        Object postVal = fData.get("post");
                        if (postVal instanceof List<?> list) {
                            fs.setPost(list.stream().map(Object::toString).toList());
                        } else if (postVal instanceof String s) {
                            if ("None".equals(s) || s.isBlank()) {
                                fs.setPost(new ArrayList<>());
                            } else {
                                fs.setPost(Arrays.asList(s.split(",\\s*")));
                            }
                        }
                        if (fData.get("active")    instanceof Boolean b) fs.setActive(b);
                        // Persist patronage by faction KEY (not name) so frontend can look it up by key
                        int incomingPatronage = (fData.get("patronage") instanceof Number n) ? n.intValue() : 0;
                        fs.setPatronage(incomingPatronage);
                        assignedPointsMap.put(fKey, incomingPatronage);
                        log.info("[PartyMgmt Lock] Faction '{}' patronage={} loyalty={} post={}",
                                fKey, incomingPatronage, fs.getLoyalty(), fs.getPost());
                    }
                }
            }
            pms.setAllocatedPatronagePoints(assignedPointsMap);
        }

        // Apply project assignments
        if (req.getProjects() != null && !req.getProjects().isEmpty()) {
            com.politicalsim.party.PartyState party = session.getParties().stream()
                    .filter(p -> p.getId().equals(partyId)).findFirst().orElse(null);
            if (party != null) {
                for (com.politicalsim.party.ProjectState ps : party.getProjects()) {
                    String assignedFaction = req.getProjects().get(ps.getId());
                    if (assignedFaction == null) {
                        assignedFaction = req.getProjects().get(ps.getProjectKey());
                    }
                    if (assignedFaction != null) {
                        ps.setManagingFactionKey(assignedFaction);
                    }
                }
            }
        }

        gameSessionService.save(session);
        return partyManagementRepository.save(pms);
    }

    private String getPrecedingScenarioKey(String scenarioKey) {
        if (null == scenarioKey ) return null;
        String stateName= com.politicalsim.util.ScenarioKeyParser.extractStateName(scenarioKey);
        int year= com.politicalsim.util.ScenarioKeyParser.extractYear(scenarioKey);
        int lookoutYear= year<=2001 ? 2001 : year-5;
        return stateName+"_"+lookoutYear;
    }

    private GameSessionRepository.GameSessionDTO findPrecedingWonSession(String userId, String scenarioKey) {
        if (userId == null || userId.isBlank() || "null".equalsIgnoreCase(userId) || "undefined".equalsIgnoreCase(userId)) return null;
        String precedingKey = getPrecedingScenarioKey(scenarioKey);
        if (precedingKey == null) return null;

        List<GameSessionRepository.GameSessionDTO> userGames = gameSessionService.listGamesDto(userId.trim().toLowerCase());
        for (GameSessionRepository.GameSessionDTO g : userGames) {
            String skey = g.scenarioKey();
            if (skey == null) continue;
            boolean isMatch = skey.equals(precedingKey) || 
                              ("maharashtra_2001".equals(precedingKey) && "Mh_2001".equals(skey)) ||
                              ("Mh_2001".equals(precedingKey) && "maharashtra_2001".equals(skey));
            if (isMatch) {
                if (g.status() == GameStatus.VICTORY) {
                    return g;
                } else if (g.status() == GameStatus.GAME_OVER) {
                    PartyState gov = g.governmentParty();
                    if (gov != null && g.playerPartyIds() != null && g.playerPartyIds().contains(gov.getId())) {
                        return g;
                    }
                }
            }
        }
        return null;
    }

    public GameSession forfeitGame(String gameId) {
        GameSession session = getGame(gameId);
        session.setStatus(GameStatus.FORFEITED);
        return gameSessionService.save(session);
    }

    public void deleteGame(String gameId) {
        gameSessionService.deleteGame(gameId);
    }

    public GameSession getGame(String gameId) {
        return gameSessionService.getGame(gameId);
    }


    public List<GameSession> listGames(String userId) {
        if (userId == null || userId.isBlank() || "null".equalsIgnoreCase(userId) || "undefined".equalsIgnoreCase(userId)) {
            return new ArrayList<>();
        }
        return gameSessionService.listGames(userId.trim().toLowerCase());
    }

    public List<GameSessionSummary> listGameSummaries() {
        return gameSessionService.listGameSummaries();
    }

    public List<GameSessionSummary> listGameSummaries(String userId) {
        if (userId == null || userId.isBlank() || "null".equalsIgnoreCase(userId) || "undefined".equalsIgnoreCase(userId)) {
            return new ArrayList<>();
        }
        return gameSessionService.listGameSummaries(userId.trim().toLowerCase());
    }
    
    public GameSession getGameByJoinCode(String joinCode) {
        return gameSessionService.getGameByJoinCode(joinCode);
    }
    
    public GameSession joinGame(String userId, String joinCode, String partyId) {
        return gameSessionService.joinGame(userId, joinCode, partyId);
    }
    
    public GameSession startGame(String gameId, String userId) {
        return gameSessionService.startGame(gameId, userId);
    }

    public TurnView getTurnView(String gameId) {
        GameSession session = getGame(gameId);
        ensureSecretMetricInitialized(session);
        if (session.getTripleImpactTurn() <= 0) {
            session.setTripleImpactTurn(5 * ((session.getTurnNumber() - 1) / 5) + new java.util.Random().nextInt(5) + 1);
            gameSessionService.save(session);
        }
        NoConfidenceStatus noConfidence = getNoConfidenceStatus(session);
        List<CardDefinition> availableCards = getAvailableHumanCards(session);
        List<NewsDefinition> currentNews = getCurrentNews(session);
        PartyState activeHumanParty = getActiveHumanParty(session);
        Object currentIssue = null;
        
        List<HeldRewardView> activePlayerHeldRewards = new ArrayList<>();
        if (activeHumanParty != null && session.getPartyHeldRewards() != null) {
            List<HeldReward> held = session.getPartyHeldRewards().get(activeHumanParty.getId());
            if (held != null) {
                activePlayerHeldRewards = held.stream().map(HeldRewardView::from).toList();
            }
        }

        return new TurnView(
                session.getId(),
                session.getScenarioKey(),
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
                activePlayerHeldRewards,
                session.getActiveCrisisKey(),
                session.getActiveCrisisName(),
                session.getActiveCrisisDescription(),
                session.getActiveCrisisTurnsLeft(),
                session.isLastElectionHeld(),
                session.getLastElectionWinner(),
                session.getLastElectionVoteShares(),
                session.getCooperationOffers(),
                session.getActivePacts(),
                session.getTripleImpactTurn() == session.getTurnNumber(),
                session.getLastRoundSecretMetric(),
                session.isMultiplayer(),
                session.getJoinCode(),
                session.getHumanPlayerMap(),
                session.getTurnStartTime(),
                session.getTurnDurationSeconds(),
                session.getBills(),
                session.getBillVotes(),
                session.getProposedBillKeyThisTurn(),
                session.getActiveEventKey(),
                session.getLobbyPledges(),
                session.getLastResolvedBillKey(),
                session.getLastBillYesVotes(),
                session.getLastBillNoVotes(),
                session.getLastBillAbstainVotes(),
                session.getLastBillPartyVotes(),
                getPartyManagementState(session.getId(), activeHumanParty == null ? null : activeHumanParty.getId())
        );
    }

    public TurnView advanceTurn(String gameId, TurnAdvanceRequest request) {
        GameSession session = getGame(gameId);
        if (session.getTripleImpactTurn() <= 0) {
            session.setTripleImpactTurn(5 * ((session.getTurnNumber() - 1) / 5) + new java.util.Random().nextInt(5) + 1);
        }
        if (session.getStatus() != GameStatus.ACTIVE) {
            throw new IllegalArgumentException("The game has already ended (Status: " + session.getStatus() + ").");
        }
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
        int maxAllowedBid = currentMetricValue;
        if ("CORRUPTION".equalsIgnoreCase(activeMetric)) {
            maxAllowedBid = Math.max(0, 95 - activeHumanParty.getStats().getCorruptionScore());
        }
        if (request.getBid() < 0 || request.getBid() > maxAllowedBid) {
            throw new IllegalArgumentException("Bid of " + request.getBid() + " is invalid. Must be between 0 and the maximum allowed for " + activeMetric + " (" + maxAllowedBid + ").");
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
        session.getCurrentRoundSubmissions().removeIf(submission -> submission.getPartyId().equals(activeHumanParty.getId()));
        
        RoundSubmission sub = toSubmission(
                activeHumanParty,
                targetParty,
                selectedCard,
                request.getSelectedNewsReactions(),
                null,
                null
        );
        sub.setBid(request.getBid());
        sub.setProposedBillKey(request.getProposedBillKey());
        sub.setBillVote(request.getBillVote());
        sub.setSelectedEventOptionKey(request.getSelectedEventOptionKey());
        sub.setWhipIssued(request.isWhipIssued());
        sub.setSelectedRewardKey(request.getSelectedRewardKey());
        sub.setAllocations(request.getAllocations());
        sub.setFactionCrisisChoice(request.getFactionCrisisChoice());
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
            RoundSubmission noConfSub = session.getCurrentRoundSubmissions().stream()
                .filter(s -> s.getCardKey() != null && s.getCardKey().contains("no_confidence"))
                .findFirst().orElse(null);
            PartyState motionProposer = null;
            if (noConfSub != null) {
                motionProposer = session.getParties().stream()
                    .filter(p -> p.getId().equals(noConfSub.getPartyId()))
                    .findFirst().orElse(null);
            }
            PartyState govParty = session.getGovernmentParty();
            if (motionProposer != null && govParty != null) {
                if (motionProposer.getStats().getPublicSupport() > govParty.getStats().getPublicSupport()) {
                    noConfidenceSucceeded = true;
                } else {
                    session.getLastRoundCommentary().add("The Opposition's No-Confidence Motion failed to gather enough support. The government survives the vote and continues in office.");
                    session.setLastResults(List.of("No-Confidence Motion failed: Government survives."));
                }
            }
        }

        boolean govDefeated = session.getGovernmentParty() != null && (!session.getGovernmentParty().isActive() || session.getGovernmentParty().getRole() == com.politicalsim.party.PartyRole.DEFEATED);
        boolean electionHeld = (noConfidencePlayed && noConfidenceSucceeded)
                || govDefeated
                || session.getMonthInCycle() >= CYCLE_LENGTH_MONTHS
                || session.getTurnNumber() >= 60;
        if (electionHeld) {
            String reason = "Mandatory 60-month election completed.";
            if (noConfidencePlayed && noConfidenceSucceeded) {
                reason = "No-confidence motion triggered an early election.";
            } else if (govDefeated) {
                reason = "Government collapsed due to critical resource failure, triggering an early election.";
            }
            roundResolutionEngine.conductElection(session, reason, noConfidencePlayed && noConfidenceSucceeded);
            session.setMonthInCycle(1);
        } else {
            session.setMonthInCycle(session.getMonthInCycle() + 1);
        }
        session.setLastRoundSecretMetric(session.getSecretMetric());
        int nextTurn = session.getTurnNumber() + 1;
        ensureSecretMetricInitialized(session);
        if ((nextTurn - 1) % 30 == 0) {
            java.util.Collections.shuffle(session.getSecretMetricSequence());
        }
        session.setSecretMetric(session.getSecretMetricSequence().get((nextTurn - 1) % 30));
        session.setTurnNumber(nextTurn);
        if ((session.getTurnNumber() - 1) % 5 == 0) {
            session.setTripleImpactTurn(session.getTurnNumber() + new java.util.Random().nextInt(5));
        }
        session.setCurrentDate(session.getCurrentDate().plusMonths(1));
        if (session.isMultiplayer()) {
            session.setTurnStartTime(java.time.LocalDateTime.now());
        }

        // Tick Non-Aggression pacts and cooperation offers
        if (session.getActivePacts() != null) {
            session.getActivePacts().forEach(pact -> pact.setTurnsRemaining(pact.getTurnsRemaining() - 1));
            session.getActivePacts().removeIf(pact -> pact.getTurnsRemaining() <= 0);
        }
        if (session.getCooperationOffers() != null) {
            for (CooperationOffer co : session.getCooperationOffers()) {
                if (co.getStatus() == CooperationOffer.OfferStatus.PENDING && co.getTurnCreated() < session.getTurnNumber()) {
                    co.setStatus(CooperationOffer.OfferStatus.EXPIRED);
                }
            }
        }
        session.setActiveHumanPlayerIndex(0);
        session.setCurrentRoundSubmissions(new ArrayList<>());

        Map<String, PartyStats> startStats = new java.util.LinkedHashMap<>();
        for (PartyState party : session.getParties()) {
            PartyStats copied = new PartyStats(
                party.getStats().getCoins(),
                party.getStats().getPartyMorale(),
                party.getStats().getCorruptionScore(),
                party.getStats().getMediaImage(),
                party.getStats().getPublicSupport()
            );
            startStats.put(party.getId(), copied);
        }
        session.setTurnStartStats(startStats);

        // Persist party management state (patronage, posts) for each player party
        int resolvedTurnNumber = session.getTurnNumber(); // turn AFTER increment already applied
        for (String pid : session.getPlayerPartyIds()) {
            RoundSubmission playerSub = session.getLastRoundSubmissions() != null
                    ? session.getLastRoundSubmissions().stream()
                        .filter(s -> s.getPartyId().equals(pid))
                        .findFirst().orElse(null)
                    : null;
            java.util.Map<String, Object> allocs = playerSub != null ? playerSub.getAllocations() : null;
            updatePartyManagementOnTurn(session, pid, allocs, resolvedTurnNumber);
        }

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
        if (!"no_card".equals(card.getCardKey()) && usedCount(session, party, card) >= 3) {
            throw new IllegalArgumentException("Card has no uses remaining in this game: " + cardKey);
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
        return aiDecisionService.chooseOpponent(session, actor, card);
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
            Object issue, Object issueOption) {
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

            // 1. Proactive Faction Bribe (Counter-Attack / Distressed recovery)
            boolean ownFactionUnderAttack = false;
            for (com.politicalsim.party.FactionState ownFs : party.getFactions()) {
                if (ownFs.isActive()) {
                    int frozenPostsCount = ownFs.getFrozenPosts() != null ? ownFs.getFrozenPosts().size() : 0;
                    int frozenPatronage = ownFs.getFrozenPatronageTurns() != null ? ownFs.getFrozenPatronageTurns().size() : 0;
                    if (ownFs.getLoyalty() < 60 || frozenPostsCount > 0 || frozenPatronage > 0) {
                        ownFactionUnderAttack = true;
                        break;
                    }
                }
            }

            double bribeChance = ownFactionUnderAttack ? 0.85 : 0.25;
            if (party.getStats().getCoins() >= 120 && new java.util.Random().nextDouble() < bribeChance) {
                com.politicalsim.party.FactionState bestTargetFs = null;
                PartyState bestTargetParty = null;
                int highestInfluence = -1;

                // Pick the opponent faction with the highest influence to target
                for (PartyState opp : session.getParties()) {
                    if (opp.getId().equals(party.getId()) || opp.getRole() == com.politicalsim.party.PartyRole.DEFEATED || !opp.isActive()) {
                        continue;
                    }
                    for (com.politicalsim.party.FactionState fs : opp.getFactions()) {
                        if (fs.isActive() && fs.getInfluence() > highestInfluence) {
                            highestInfluence = fs.getInfluence();
                            bestTargetFs = fs;
                            bestTargetParty = opp;
                        }
                    }
                }

                if (bestTargetFs != null && bestTargetParty != null) {
                    int bribeCoins = ownFactionUnderAttack 
                            ? Math.min(200, party.getStats().getCoins() - 50)
                            : 80 + new java.util.Random().nextInt(61);

                    // Execute Bribe
                    party.getStats().setCoins(party.getStats().getCoins() - bribeCoins);

                    // Count currently frozen assets of the target faction
                    int targetFrozenCount = 0;
                    if (bestTargetFs.getFrozenPosts() != null) {
                        for (int turns : bestTargetFs.getFrozenPosts().values()) {
                            if (turns > 0) targetFrozenCount++;
                        }
                    }
                    if (bestTargetFs.getFrozenPatronageTurns() != null) {
                        targetFrozenCount += bestTargetFs.getFrozenPatronageTurns().size();
                    }
                    for (ProjectState ps : bestTargetParty.getProjects()) {
                        if (bestTargetFs.getKey().equals(ps.getManagingFactionKey()) && ps.getFrozenTurnsRemaining() > 0) {
                            targetFrozenCount++;
                        }
                    }

                    double baseProb = 0.20;
                    double turnFactor = (double) session.getTurnNumber() / 100.0;
                    if (turnFactor > 0.40) turnFactor = 0.40;
                    double targetPartyCoins = bestTargetParty.getStats().getCoins();
                    double successProb = baseProb + turnFactor + ((double) bribeCoins / (200.0 + (targetPartyCoins * 0.3) + (targetFrozenCount * 30.0)));
                    successProb = Math.max(0.10, Math.min(0.90, successProb));

                    double roll = new java.util.Random().nextDouble();
                    if (roll < successProb) {
                        // Success
                        int loyaltyLoss = 15 + new java.util.Random().nextInt(16);
                        bestTargetFs.setLoyalty(Math.max(0, bestTargetFs.getLoyalty() - loyaltyLoss));

                        int numToFreeze = Math.max(1, bribeCoins / 30);
                        java.util.List<String> postCandidates = new ArrayList<>();
                        if (bestTargetFs.getPost() != null) {
                            for (String pKey : bestTargetFs.getPost()) {
                                if (pKey != null && !pKey.equals("None") && !pKey.isBlank()) {
                                    if (bestTargetFs.getFrozenPosts() == null || !bestTargetFs.getFrozenPosts().containsKey(pKey)) {
                                        postCandidates.add(pKey);
                                    }
                                }
                            }
                        }

                        java.util.List<ProjectState> projectCandidates = new ArrayList<>();
                        for (ProjectState ps : bestTargetParty.getProjects()) {
                            if (ps.getProgressPercent() == 100 && bestTargetFs.getKey().equals(ps.getManagingFactionKey()) && ps.getFrozenTurnsRemaining() <= 0) {
                                projectCandidates.add(ps);
                            }
                        }

                        int currentFrozenPatCount = bestTargetFs.getFrozenPatronageTurns() != null ? bestTargetFs.getFrozenPatronageTurns().size() : 0;
                        int activePatronage = bestTargetFs.getPatronage() - currentFrozenPatCount;

                        java.util.List<String> pool = new ArrayList<>();
                        for (String pc : postCandidates) pool.add("POST:" + pc);
                        for (ProjectState prc : projectCandidates) pool.add("PROJECT:" + prc.getId());
                        for (int i = 0; i < activePatronage; i++) pool.add("PATRONAGE");

                        java.util.Collections.shuffle(pool);
                        java.util.List<String> frozenLabels = new ArrayList<>();

                        for (int i = 0; i < Math.min(numToFreeze, pool.size()); i++) {
                            String act = pool.get(i);
                            if (act.startsWith("POST:")) {
                                String pk = act.substring(5);
                                if (bestTargetFs.getFrozenPosts() == null) bestTargetFs.setFrozenPosts(new java.util.HashMap<>());
                                bestTargetFs.getFrozenPosts().put(pk, 10);
                                frozenLabels.add(pk + " Post");
                            } else if (act.startsWith("PROJECT:")) {
                                String pid = act.substring(8);
                                for (ProjectState ps : bestTargetParty.getProjects()) {
                                    if (ps.getId().equals(pid)) {
                                        ps.setFrozenTurnsRemaining(10);
                                        frozenLabels.add((ps.getName() != null ? ps.getName() : ps.getProjectKey()) + " Project");
                                        break;
                                    }
                                }
                            } else if ("PATRONAGE".equals(act)) {
                                if (bestTargetFs.getFrozenPatronageTurns() == null) bestTargetFs.setFrozenPatronageTurns(new ArrayList<>());
                                bestTargetFs.getFrozenPatronageTurns().add(10);
                                frozenLabels.add("Patronage Point");
                            }
                        }

                        String frozenList = frozenLabels.isEmpty() ? "No active cards found to freeze" : String.join(", ", frozenLabels);
                        String msg = String.format("🚨 AI Sabotage: %s successfully bribed %s's %s faction! Loyalty fell by -%d%%. FROZEN: %s.",
                                party.getName(), bestTargetParty.getName(), bestTargetFs.getName(), loyaltyLoss, frozenList);
                        session.getLastRoundCommentary().add(msg);
                        session.getLastResults().add("🚨 AI " + party.getName() + " successfully bribed opponent faction " + bestTargetFs.getName());
                    } else {
                        // Fail
                        int mediaLoss = Math.max(5, (int) Math.round(party.getStats().getMediaImage() * 0.10));
                        int moraleLoss = Math.max(3, (int) Math.round(party.getStats().getPartyMorale() * 0.05));
                        party.getStats().setMediaImage(Math.max(0, party.getStats().getMediaImage() - mediaLoss));
                        party.getStats().setPartyMorale(Math.max(0, party.getStats().getPartyMorale() - moraleLoss));

                        String msg = String.format("🚨 AI Sabotage Exposed: %s tried to bribe %s's %s but was exposed! %s loses -%d Media Image and -%d Morale.",
                                party.getName(), bestTargetParty.getName(), bestTargetFs.getName(), party.getName(), mediaLoss, moraleLoss);
                        session.getLastRoundCommentary().add(msg);
                        session.getLastResults().add("🚨 AI " + party.getName() + " bribe attempt on " + bestTargetFs.getName() + " exposed!");
                    }
                }
            }

            // 2. Proactive AI Non-Aggression Pact Proposing
            if (party.getStats().getCoins() >= 60 && (party.getStats().getPartyMorale() < 40 || new java.util.Random().nextDouble() < 0.15)) {
                PartyState pactTarget = choosePactTarget(session, party);
                if (pactTarget != null) {
                    CooperationOffer pactOffer = new CooperationOffer();
                    pactOffer.setId(java.util.UUID.randomUUID().toString());
                    pactOffer.setTurnCreated(session.getTurnNumber());
                    pactOffer.setStatus(CooperationOffer.OfferStatus.PENDING);
                    pactOffer.setType(CooperationOffer.OfferType.NON_AGGRESSION);
                    pactOffer.setSenderPartyId(party.getId());
                    pactOffer.setSenderPartyName(party.getName());
                    pactOffer.setRecipientPartyId(pactTarget.getId());
                    pactOffer.setRecipientPartyName(pactTarget.getName());
                    pactOffer.setDurationTurns(10);
                    pactOffer.setSenderPaysPact(true);
                    pactOffer.setPactPaymentResource("COINS");
                    pactOffer.setPactPaymentValue(20);

                    if (session.getCooperationOffers() == null) {
                        session.setCooperationOffers(new java.util.ArrayList<>());
                    }

                    if (pactTarget.getControllerType() == ControllerType.COMPUTER) {
                        boolean accepted = aiDecisionService.evaluateCooperationOffer(session, pactTarget, pactOffer);
                        if (accepted) {
                            cooperationResolver.executeCooperationTrade(session, pactOffer);
                            pactOffer.setStatus(CooperationOffer.OfferStatus.ACCEPTED);
                            session.getLastRoundCommentary().add("🕊️ Pact Accepted: AI " + party.getName() + " entered a Non-Aggression Pact with AI " + pactTarget.getName() + ".");
                        } else {
                            pactOffer.setStatus(CooperationOffer.OfferStatus.REJECTED);
                        }
                    } else {
                        session.getLastRoundCommentary().add("🕊️ Pact Proposed: AI " + party.getName() + " proposed a Non-Aggression Pact to you.");
                    }
                    session.getCooperationOffers().add(pactOffer);
                }
            }

            PartyState opponent = chooseOpponentExcludingPacts(session, party);
            AiDecision decision = aiDecisionService.chooseCard(session, party, opponent, getAvailableCardsForParty(session, party));
            Map<String, String> reactions = new LinkedHashMap<>();
            for (NewsDefinition news : getCurrentNews(session)) {
                NewsReactionDefinition reaction = aiDecisionService.chooseReaction(party, decision.intent(), news.getReactionOptions());
                if (reaction != null) {
                    reactions.put(news.getNewsKey(), reaction.getReactionKey());
                }
            }
            PartyState targetParty = chooseAiTarget(session, party, decision.card());
            RoundSubmission submission = toSubmission(party, targetParty, decision.card(), reactions, null, null);
            submission.setAiIntent(decision.intent().name());

            // AI Legislative Proposing and Lobbying (Danger zone prioritization + Fail limit + 20% coin limit)
            boolean isDangerCoins = party.getStats().getCoins() < 50;
            boolean isDangerMorale = party.getStats().getPartyMorale() < 30;

            List<LegislativeBillDefinition> allBills = com.politicalsim.content.DefinitionCache.getBillsForScenario(aiDecisionService.getBillRepository(), session.getScenarioKey());
            List<LegislativeBillState> currentSessionBills = session.getBills();
            List<String> eligibleBillKeys = currentSessionBills.stream()
                    .filter(b -> "NOT_PROPOSED".equals(b.getStatus()))
                    .map(LegislativeBillState::getBillKey)
                    .toList();

            String myRoleStr = party.getRole() == com.politicalsim.party.PartyRole.GOVERNMENT ? "GOVERNMENT" : "OPPOSITION";
            List<LegislativeBillDefinition> proposePool = allBills.stream()
                    .filter(b -> eligibleBillKeys.contains(b.getBillKey()))
                    .filter(b -> myRoleStr.equalsIgnoreCase(b.getProposingRole()))
                    .filter(b -> session.getBillLobbyFailCounts().getOrDefault(b.getBillKey(), 0) < 3)
                    .toList();

            List<LegislativeBillDefinition> sortedBills = new ArrayList<>(proposePool);
            sortedBills.sort((b1, b2) -> {
                double s1 = scoreBillForPriority(b1, isDangerCoins, isDangerMorale);
                double s2 = scoreBillForPriority(b2, isDangerCoins, isDangerMorale);
                return Double.compare(s2, s1); // descending
            });

            LegislativeBillDefinition bestBill = sortedBills.isEmpty() ? null : sortedBills.get(0);
            String proposedBillKey = (bestBill != null) ? bestBill.getBillKey() : null;

            if (proposedBillKey != null) {
                int totalYesVotes = 0;
                int totalParties = 0;
                List<PartyState> potentialLobbyTargets = new ArrayList<>();
                for (PartyState other : session.getParties()) {
                    if (other.getRole() == com.politicalsim.party.PartyRole.DEFEATED || !other.isActive()) {
                        continue;
                    }
                    totalParties++;
                    if (other.getId().equals(party.getId())) {
                        totalYesVotes++;
                    } else {
                        String vote = legislativeAiService.evaluateAiBillVote(session, other, proposedBillKey);
                        if ("YES".equals(vote)) {
                            totalYesVotes++;
                        } else {
                            potentialLobbyTargets.add(other);
                        }
                    }
                }
                boolean hasMajority = totalYesVotes > (totalParties / 2);
                if (!hasMajority && !potentialLobbyTargets.isEmpty()) {
                    Map<String, Object> passedEffects = bestBill.getEffectsPassed();
                    int coinsEffect = ((Number) passedEffects.getOrDefault("coins", 0)).intValue();
                    int moraleEffect = ((Number) passedEffects.getOrDefault("partyMorale", 0)).intValue();
                    int supportEffect = ((Number) passedEffects.getOrDefault("publicSupport", 0)).intValue();
                    int corruptionEffect = ((Number) passedEffects.getOrDefault("corruptionScore", 0)).intValue();
                    int mediaEffect = ((Number) passedEffects.getOrDefault("mediaImage", 0)).intValue();

                    double billBenefitInCash = (supportEffect * 50.0) + (moraleEffect * 20.0) + (mediaEffect * 20.0) - (corruptionEffect * 20.0) + (coinsEffect * 1.0);
                    int maxLobbyCoins = (int) Math.round(billBenefitInCash * 0.20);
                    if (maxLobbyCoins >= 10 && party.getStats().getCoins() >= maxLobbyCoins) {
                        PartyState lobbyTarget = potentialLobbyTargets.get(new java.util.Random().nextInt(potentialLobbyTargets.size()));
                        
                        CooperationOffer lobbyOffer = new CooperationOffer();
                        lobbyOffer.setId(java.util.UUID.randomUUID().toString());
                        lobbyOffer.setTurnCreated(session.getTurnNumber());
                        lobbyOffer.setStatus(CooperationOffer.OfferStatus.PENDING);
                        lobbyOffer.setType(CooperationOffer.OfferType.LOBBYING);
                        lobbyOffer.setSenderPartyId(party.getId());
                        lobbyOffer.setSenderPartyName(party.getName());
                        lobbyOffer.setRecipientPartyId(lobbyTarget.getId());
                        lobbyOffer.setRecipientPartyName(lobbyTarget.getName());
                        lobbyOffer.setLobbyBillKey(proposedBillKey);
                        lobbyOffer.setOfferedCoins(maxLobbyCoins);

                        if (session.getCooperationOffers() == null) {
                            session.setCooperationOffers(new java.util.ArrayList<>());
                        }

                        if (lobbyTarget.getControllerType() == com.politicalsim.party.ControllerType.COMPUTER) {
                            boolean accepted = aiDecisionService.evaluateCooperationOffer(session, lobbyTarget, lobbyOffer);
                            if (accepted) {
                                cooperationResolver.executeCooperationTrade(session, lobbyOffer);
                                lobbyOffer.setStatus(CooperationOffer.OfferStatus.ACCEPTED);
                                session.getLobbyPledges().add(new com.politicalsim.game.LobbyPledge(
                                    lobbyTarget.getId(),
                                    proposedBillKey
                                ));
                                session.getLastRoundCommentary().add("🤝 Lobbying Success: AI " + party.getName() + " convinced AI " + lobbyTarget.getName() + " to pledge YES on Bill " + proposedBillKey + ".");
                            } else {
                                lobbyOffer.setStatus(CooperationOffer.OfferStatus.REJECTED);
                                session.getBillLobbyFailCounts().put(proposedBillKey, session.getBillLobbyFailCounts().getOrDefault(proposedBillKey, 0) + 1);
                                session.getLastRoundCommentary().add("❌ Lobbying Rejected: AI " + party.getName() + " failed to lobby AI " + lobbyTarget.getName() + " for Bill " + proposedBillKey + ".");
                            }
                        } else {
                            session.getLastRoundCommentary().add("🗳️ Lobbying Proposed: AI " + party.getName() + " proposed to lobby you for Bill " + proposedBillKey + ".");
                        }
                        session.getCooperationOffers().add(lobbyOffer);
                    }
                }
                submission.setProposedBillKey(proposedBillKey);
            }

            // AI Faction Crisis management
            if (party.getActiveFactionCrisisKey() != null && !party.getActiveFactionCrisisKey().isEmpty()) {
                String crisisChoice = aiDecisionService.chooseFactionCrisisChoice(session, party);
                submission.setFactionCrisisChoice(crisisChoice);
            }

            // AI Faction allocations
            com.politicalsim.party.PartyManagementState pms = partyManagementRepository
                    .findByGameIdAndPartyId(session.getId(), party.getId())
                    .orElse(null);
            int availablePatronage = (pms != null) ? pms.getUnallocatedPatronagePoints() : 1;
            List<String> availablePostKeys = new ArrayList<>();
            if (pms != null && pms.getPosts() != null) {
                for (com.politicalsim.party.ScheduledPost sp : pms.getPosts()) {
                    if (sp.getStatus() == com.politicalsim.party.ScheduledPost.Status.AVAILABLE) {
                        availablePostKeys.add(sp.getPostKey());
                    }
                }
            }
            aiDecisionService.makeFactionAllocations(session, party, submission, availablePatronage, availablePostKeys);

            // AI Legislative Vote Selection
            String activeBillKey = session.getProposedBillKeyThisTurn();
            if (activeBillKey != null && !activeBillKey.isEmpty()) {
                String aiVote = legislativeAiService.evaluateAiBillVote(session, party, activeBillKey);
                submission.setBillVote(aiVote);
                
                boolean canAffordWhip = party.getStats().getCoins() >= 25;
                boolean isYesOrNo = "YES".equalsIgnoreCase(aiVote) || "NO".equalsIgnoreCase(aiVote);
                boolean shouldWhip = isYesOrNo && canAffordWhip && (party.getStats().getCorruptionScore() > 30 || party.getStats().getPublicSupport() >= 20);
                submission.setWhipIssued(shouldWhip);
            } else {
                submission.setBillVote("ABSTAIN");
                submission.setWhipIssued(false);
            }

            // AI Bid Selection
            String metric = roundResolutionEngine.getBiddingMetricForTurn(session.getTurnNumber());
            int currentMetricValue = roundResolutionEngine.getStatValue(party, metric);
            int bid = calculateSmartBid(session, party, metric, currentMetricValue);

            // Change 5: Zero-bid on offensive rewards when in self-crisis
            // A party that urgently needs to recover should not burn resources competing
            // for rewards that harm others rather than help itself.
            boolean isInSelfCrisis = party.getStats().getPublicSupport() < 22
                    || party.getStats().getPartyMorale() < 25
                    || party.getStats().getCoins() < 40;
            if (isInSelfCrisis && session.getCurrentRewardKey() != null) {
                boolean isOffensiveReward = com.politicalsim.game.RoundResolutionEngine.REWARD_POOL.stream()
                        .filter(r -> r.key().equals(session.getCurrentRewardKey()))
                        .findFirst()
                        .map(r -> "opponent".equals(r.allowedTargets()))
                        .orElse(false);
                if (isOffensiveReward) {
                    bid = 0;
                }
            }
            submission.setBid(bid);

            // AI Project Funding and Targeting
            // 1. Assign/Modify targets for completed offensive projects
            for (ProjectState project : party.getProjects()) {
                if (project.getProgressPercent() >= 100) {
                    try {
                        BuildingProject projectDef = BuildingProject.valueOf(project.getProjectKey());
                        if (projectDef.isRequiresTarget()) {
                            PartyState target = aiDecisionService.chooseOpponentForProject(session, party, projectDef);
                            if (target != null) {
                                project.setTargetPartyId(target.getId());
                                project.setTargetPartyName(target.getName());
                            }
                        }
                    } catch (Exception e) {}
                }
            }

            // 1b. AI Project Salvage: If in crisis mode and suffering coin crisis (coins <= 80), destroy lowest-utility completed project
            int supportPressureVal = 0;
            for (PartyState other : session.getParties()) {
                if (other.getId().equals(party.getId())) continue;
                if (other.getProjects() == null) continue;
                for (ProjectState otherProj : other.getProjects()) {
                    if (otherProj.getProgressPercent() >= 100 && party.getId().equals(otherProj.getTargetPartyId())) {
                        try {
                            BuildingProject otherProjDef = BuildingProject.valueOf(otherProj.getProjectKey());
                            if (otherProjDef.getBenefitSupport() < 0) {
                                supportPressureVal += Math.abs(otherProjDef.getBenefitSupport());
                            }
                        } catch (Exception e) {}
                    }
                }
            }
            final int supportPressureValFinal = supportPressureVal;
            boolean isCoinCrisisInitial = party.getStats().getCoins() <= 80;
            boolean isSupportCrisisInitial = party.getStats().getPublicSupport() <= 15 || supportPressureValFinal >= 5;
            boolean isMoraleCrisisInitial = party.getStats().getPartyMorale() <= 25;
            boolean isCorruptionCrisisInitial = party.getStats().getCorruptionScore() >= 75;
            boolean isCrisisModeInitial = isCoinCrisisInitial || isSupportCrisisInitial || isMoraleCrisisInitial || isCorruptionCrisisInitial;


            // 2. Compute reserves
            int cardCost = decision.card().getCost();
            int projectedCardCost = cardCost;
            if (session.getActiveCrisisKey() != null) {
                if ("drought_crisis".equals(session.getActiveCrisisKey()) &&
                        ("welfare".equals(decision.card().getCategory()) || "rural".equals(decision.card().getCategory()))) {
                    projectedCardCost += 5;
                } else if ("strike_crisis".equals(session.getActiveCrisisKey())) {
                    projectedCardCost += 2;
                }
            }

            int bidReserveCoins = "COINS".equalsIgnoreCase(metric) ? bid : 0;
            int bidReserveMorale = ("PARTY_MORALE".equalsIgnoreCase(metric) || "MORALE".equalsIgnoreCase(metric)) ? bid : 0;

            // 3. Compute discretionary funds (Safety reserve of 30 coins, 25 morale, 25 media, 15 support)
            boolean isCoinCrisis = party.getStats().getCoins() <= 80;
            boolean isSupportCrisis = party.getStats().getPublicSupport() <= 15 || supportPressureValFinal >= 5;
            boolean isMoraleCrisis = party.getStats().getPartyMorale() <= 25;
            boolean isCorruptionCrisis = party.getStats().getCorruptionScore() >= 75;
            boolean isCrisisMode = isCoinCrisis || isSupportCrisis || isMoraleCrisis || isCorruptionCrisis;

            int maxCoinsSpend = (int) (party.getStats().getCoins() * 0.60);
            int maxMoraleSpend = (int) (party.getStats().getPartyMorale() * 0.50);
            int maxMediaSpend = (int) (party.getStats().getMediaImage() * 0.50);
            int maxSupportSpend = (int) (party.getStats().getPublicSupport() * 0.50);
            int maxCorruptionSpend = (int) ((100 - party.getStats().getCorruptionScore()) * 0.50);

            int discCoins = 0;
            int discMorale = 0;
            int discMedia = 0;
            int discSupport = 0;
            int discCorruption = 0;

            if (!isCoinCrisis) {
                discCoins = party.getStats().getCoins() - projectedCardCost - bidReserveCoins - 30;
                discMorale = party.getStats().getPartyMorale() - bidReserveMorale - (isMoraleCrisis ? 10 : 25);
                discMedia = party.getStats().getMediaImage() - 25;
                discSupport = party.getStats().getPublicSupport() - (isSupportCrisis ? 5 : 15);
                discCorruption = 75 - party.getStats().getCorruptionScore();
            }

            discCoins = Math.max(0, Math.min(discCoins, maxCoinsSpend));
            discMorale = Math.max(0, Math.min(discMorale, maxMoraleSpend));
            discMedia = Math.max(0, Math.min(discMedia, maxMediaSpend));
            discSupport = Math.max(0, Math.min(discSupport, maxSupportSpend));
            discCorruption = Math.max(0, Math.min(discCorruption, maxCorruptionSpend));
            
            // 4. Fund projects with discretionary funds (re-enabled for AI with a 60% coin cap and crisis filtering)
            String projectBasis = "";
            if (isCoinCrisis) {
                projectBasis = "Project strategy: Froze all project funding due to low coin reserves.";
            } else if (discCoins <= 0) {
                projectBasis = "Project strategy: Conserved resources (no discretionary budget left above safety reserves).";
            } else if (isCrisisMode) {
                projectBasis = "Project strategy: Restricted funding to crisis-relief projects due to active warning thresholds.";
            } else {
                projectBasis = "Project strategy: Decided not to fund any projects (could not afford any progress steps or no projects available).";
            }

            if (discCoins > 0 && !isCoinCrisis) {
                List<ProjectScore> scoredProjects = new ArrayList<>();
                for (ProjectState project : party.getProjects()) {
                    if (project.getProgressPercent() < 100) {
                        try {
                            BuildingProject projectDef = BuildingProject.valueOf(project.getProjectKey());
                            
                            // Crisis filtering:
                            if (isSupportCrisis) {
                                boolean helpsSupport = (!projectDef.isRequiresTarget() && projectDef.getBenefitSupport() > 0)
                                        || (projectDef.isRequiresTarget() && projectDef.getBenefitSupport() < 0);
                                if (!helpsSupport) continue;
                            }
                            if (isMoraleCrisis) {
                                boolean helpsMorale = (!projectDef.isRequiresTarget() && projectDef.getBenefitMorale() > 0)
                                        || (projectDef.isRequiresTarget() && projectDef.getBenefitMorale() < 0);
                                if (!helpsMorale) continue;
                            }
                            if (isCorruptionCrisis) {
                                boolean helpsCorruption = (!projectDef.isRequiresTarget() && projectDef.getBenefitCorruption() < 0)
                                        || (projectDef.isRequiresTarget() && projectDef.getBenefitCorruption() > 0);
                                if (!helpsCorruption) continue;
                            }

                            double score = scoreProjectForAi(session, party, decision, projectDef);
                            scoredProjects.add(new ProjectScore(project, projectDef, score));
                        } catch (Exception e) {}
                    }
                }
                
                scoredProjects.sort((a, b) -> Double.compare(b.score(), a.score()));
                
                int projectsFundedThisTurn = 0;
                for (ProjectScore ps : scoredProjects) {
                    if (projectsFundedThisTurn >= 2) break;
                    
                    int remaining = 100 - ps.project().getProgressPercent();
                    if (remaining <= 0) continue;
                    
                    int bestProgress = 0;
                    int bestCoinsCost = 0;
                    int bestMoraleCost = 0;
                    int bestCorruptionCost = 0;
                    int bestMediaCost = 0;
                    int bestSupportCost = 0;
                    
                    int[] steps = {100, 80, 60, 40, 20};
                    for (int step : steps) {
                        if (step <= remaining) {
                            int coinsCost = (int) Math.ceil((double) ps.projectDef().getCostCoins() * step / 100.0);
                            int moraleCost = (int) Math.ceil((double) ps.projectDef().getCostMorale() * step / 100.0);
                            int corruptionCost = (int) Math.ceil((double) ps.projectDef().getCostCorruption() * step / 100.0);
                            int mediaCost = (int) Math.ceil((double) ps.projectDef().getCostMedia() * step / 100.0);
                            int supportCost = (int) Math.ceil((double) ps.projectDef().getCostSupport() * step / 100.0);

                            boolean canAfford = coinsCost <= discCoins;
                            if (ps.projectDef().getCostMorale() > 0 && moraleCost > discMorale) canAfford = false;
                            if (ps.projectDef().getCostCorruption() > 0 && corruptionCost > discCorruption) canAfford = false;
                            if (ps.projectDef().getCostMedia() > 0 && mediaCost > discMedia) canAfford = false;
                            if (ps.projectDef().getCostSupport() > 0 && supportCost > discSupport) canAfford = false;

                            if (canAfford) {
                                bestProgress = step;
                                bestCoinsCost = coinsCost;
                                bestMoraleCost = moraleCost;
                                bestCorruptionCost = corruptionCost;
                                bestMediaCost = mediaCost;
                                bestSupportCost = supportCost;
                                break;
                            }
                        }
                    }
                    
                    if (bestProgress > 0) {
                        party.getStats().setCoins(party.getStats().getCoins() - bestCoinsCost);
                        party.getStats().setPartyMorale(party.getStats().getPartyMorale() - bestMoraleCost);
                        party.getStats().setMediaImage(party.getStats().getMediaImage() - bestMediaCost);
                        party.getStats().setCorruptionScore(Math.min(100, party.getStats().getCorruptionScore() + bestCorruptionCost));
                        if (bestSupportCost > 0) {
                            party.getStats().setPublicSupport(Math.max(0, party.getStats().getPublicSupport() - bestSupportCost));
                            session.getPublicState().setUndecidedSupport(session.getPublicState().getUndecidedSupport() + bestSupportCost);
                        }

                        ps.project().setProgressPercent(ps.project().getProgressPercent() + bestProgress);
                        if (ps.project().getProgressPercent() == 100 && ps.project().getCompletionTurn() == 0) {
                            ps.project().setCompletionTurn(session.getTurnNumber());
                        }
                        
                        // Record AI contribution
                        Map<String, Map<String, Integer>> contribs = session.getProjectContributionsThisTurn();
                        Map<String, Integer> partyContribs = contribs.computeIfAbsent(party.getId(), k -> new java.util.LinkedHashMap<>());
                        partyContribs.put(ps.project().getProjectKey(), partyContribs.getOrDefault(ps.project().getProjectKey(), 0) + bestProgress);
                        
                        discCoins -= bestCoinsCost;
                        discMorale -= bestMoraleCost;
                        discMedia -= bestMediaCost;
                        discSupport -= bestSupportCost;
                        discCorruption -= bestCorruptionCost;
                        
                        String stepMsg = "Funded project '" + ps.projectDef().getName() + "' (Progress: +" + bestProgress + "%)";
                        if (projectsFundedThisTurn == 0) {
                            projectBasis = "Project strategy: " + stepMsg;
                        } else {
                            projectBasis += ", and " + stepMsg;
                        }
                        projectsFundedThisTurn++;

                        if (ps.project().getProgressPercent() >= 100) {
                            boolean hasIncomplete = party.getProjects().stream()
                                .anyMatch(p -> p.getProjectKey().equals(ps.project().getProjectKey()) && p.getProgressPercent() < 100);
                            if (!hasIncomplete) {
                                party.getProjects().add(new ProjectState(ps.project().getProjectKey()));
                            }

                            if (ps.projectDef().isRequiresTarget()) {
                                PartyState target = aiDecisionService.chooseOpponentForProject(session, party, ps.projectDef());
                                if (target != null) {
                                    ps.project().setTargetPartyId(target.getId());
                                    ps.project().setTargetPartyName(target.getName());
                                }
                            }
                        }
                    }
                }
                if (projectsFundedThisTurn > 0) {
                    projectBasis += " to gain passive benefits.";
                }
            }

            // AI Diplomatic Cooperation (Propose Non-Aggression Pact)
            if (session.getTurnNumber() > 2 && session.getTurnNumber() < 55) {
                // If AI is under pressure but not broke, seek a pact
                boolean wantsPact = (party.getStats().getPublicSupport() < 25 || party.getStats().getCoins() < 80) && party.getStats().getCoins() > 20;
                if (wantsPact && new java.util.Random().nextDouble() < 0.25) {
                    PartyState rival = aiDecisionService.chooseOpponent(session, party, null); // Find biggest threat
                    if (rival != null && rival.isActive()) {
                        boolean alreadyHasPact = session.getActivePacts() != null && session.getActivePacts().stream()
                            .anyMatch(p -> (p.getPartyAId().equals(party.getId()) && p.getPartyBId().equals(rival.getId())) ||
                                           (p.getPartyAId().equals(rival.getId()) && p.getPartyBId().equals(party.getId())));
                        if (!alreadyHasPact) {
                            CooperationOffer pactOffer = new CooperationOffer();
                            pactOffer.setId(java.util.UUID.randomUUID().toString());
                            pactOffer.setTurnCreated(session.getTurnNumber());
                            pactOffer.setStatus(CooperationOffer.OfferStatus.PENDING);
                            pactOffer.setType(CooperationOffer.OfferType.NON_AGGRESSION);
                            pactOffer.setSenderPartyId(party.getId());
                            pactOffer.setSenderPartyName(party.getName());
                            pactOffer.setRecipientPartyId(rival.getId());
                            pactOffer.setRecipientPartyName(rival.getName());
                            pactOffer.setDurationTurns(10);
                            
                            // AI offers to pay coins to secure the pact since it feels threatened
                            pactOffer.setSenderPaysPact(true);
                            pactOffer.setPactPaymentResource("COINS");
                            pactOffer.setPactPaymentValue(15);
                            
                            if (session.getCooperationOffers() == null) {
                                session.setCooperationOffers(new java.util.ArrayList<>());
                            }
                            
                            if (rival.getControllerType() == com.politicalsim.party.ControllerType.COMPUTER) {
                                boolean accepted = aiDecisionService.evaluateCooperationOffer(session, rival, pactOffer);
                                if (accepted) {
                                    cooperationResolver.executeCooperationTrade(session, pactOffer);
                                    pactOffer.setStatus(CooperationOffer.OfferStatus.ACCEPTED);
                                } else {
                                    pactOffer.setStatus(CooperationOffer.OfferStatus.REJECTED);
                                }
                            }
                            session.getCooperationOffers().add(pactOffer);
                        }
                    }
                }
            }

            // AI Reward Play Selection
            List<HeldReward> heldRewards = session.getPartyHeldRewards().get(party.getId());
            if (heldRewards != null && !heldRewards.isEmpty()) {
                if (new Random().nextBoolean()) {
                    HeldReward chosenHr = null;
                    PartyState chosenTarget = null;
                    for (HeldReward hr : heldRewards) {
                        if (hr.isRequiresTarget()) {
                            if ("opponent".equals(hr.getAllowedTargets())) {
                                PartyState target = chooseOpponentExcludingPacts(session, party);
                                if (target != null) {
                                    chosenHr = hr;
                                    chosenTarget = target;
                                    break;
                                }
                            } else if ("self".equals(hr.getAllowedTargets())) {
                                chosenHr = hr;
                                chosenTarget = party;
                                break;
                            } else {
                                // "any"
                                PartyState target = chooseOpponentExcludingPacts(session, party);
                                chosenHr = hr;
                                chosenTarget = (target == null || new Random().nextBoolean()) ? party : target;
                                break;
                            }
                        } else {
                            chosenHr = hr;
                            chosenTarget = null;
                            break;
                        }
                    }
                    if (chosenHr != null) {
                        submission.setSelectedRewardKey(chosenHr.getRewardKey());
                        submission.setRewardName(chosenHr.getName());
                        if (chosenTarget != null) {
                            submission.setRewardTargetPartyId(chosenTarget.getId());
                            submission.setRewardTargetPartyName(chosenTarget.getName());
                        }
                    }
                }
            }

            // Construct explanation of AI decision
            boolean hasDefeatHazard = party.getStats().getCoins() <= 20
                    || party.getStats().getPartyMorale() <= 18
                    || party.getStats().getPublicSupport() <= 10
                    || party.getStats().getCorruptionScore() >= 75;

            int cycleTurn = ((session.getTurnNumber() - 1) % 5) + 1;
            int remainingTurns = 5 - cycleTurn;
            int myWins = session.getPartyRoundWins().getOrDefault(party.getId(), 0);
            int leaderWins = 0;
            for (Map.Entry<String, Integer> entry : session.getPartyRoundWins().entrySet()) {
                if (!entry.getKey().equals(party.getId())) {
                    leaderWins = Math.max(leaderWins, entry.getValue());
                }
            }
            int overallMaxWins = Math.max(myWins, leaderWins);

            String intentExplanation = switch (decision.intent()) {
                case FORCE_NO_CONFIDENCE -> "force early elections due to Government vulnerability";
                case RAISE_FUNDS -> "replenish low coin reserves";
                case SURVIVE_SCANDAL -> "reduce high corruption score";
                case DEFEND_IMAGE -> "improve weak media presence";
                case RESTORE_MORALE -> "restore low cadre morale";
                case PREPARE_ELECTION -> "gather voter support before the upcoming election";
                case ATTACK_RIVAL -> "target key rivals and capitalize on their weaknesses";
                case GAIN_SUPPORT -> "increase general voter support";
                default -> "maintain general stability";
            };
            String strategyBasis = party.getName() + " focused on '" + decision.intent().name() + "' (" + intentExplanation + "). "
                + "Decided to play '" + decision.card().getName() + "' (Reserves: " 
                + party.getStats().getCoins() + " Coins, " + party.getStats().getPartyMorale() + " Morale, " 
                + party.getStats().getCorruptionScore() + "% Corruption, " + party.getStats().getMediaImage() + " Media, " 
                + party.getStats().getPublicSupport() + "% Support).";

            // Bid explanation
            String bidReason;
            if (hasDefeatHazard) {
                bidReason = "conserved resources because party is in a defeat hazard zone";
            } else if (overallMaxWins >= 3) {
                bidReason = "placed 0 bid because five-turn cycle reward is already decided";
            } else if (myWins + remainingTurns < leaderWins) {
                bidReason = "placed 0 bid because it is mathematically impossible to win this reward cycle";
            } else {
                RewardDefinition currentReward = null;
                if (session.getCurrentRewardKey() != null) {
                    currentReward = RoundResolutionEngine.REWARD_POOL.stream()
                            .filter(r -> r.key().equals(session.getCurrentRewardKey()))
                            .findFirst()
                            .orElse(null);
                }
                if (currentReward != null) {
                    double rewardUtility = aiDecisionService.evaluateRewardUtility(session, party, currentReward);
                    if (rewardUtility < 0.3) {
                        bidReason = "placed 0 bid because cycle reward utility is low (" + String.format("%.2f", rewardUtility) + ")";
                    } else if (rewardUtility < 0.6) {
                        bidReason = "scaled bid down by 50% to " + bid + " because reward utility is moderate (" + String.format("%.2f", rewardUtility) + ")";
                    } else {
                        bidReason = "bid " + bid + " with high reward utility (" + String.format("%.2f", rewardUtility) + ")";
                    }
                } else {
                    bidReason = "bid " + bid + " (no active cycle reward)";
                }
            }
            String bidBasis = "Bidding strategy on " + metric + ": " + bidReason + ".";

            String explanation = strategyBasis + " " + bidBasis + " " + projectBasis;
            submission.setAiDecisionBasis(explanation);

            // --- CRISIS FIGHT BACK ---
            boolean isCrisisNow = brokeFightBackService.isCrisisActive(party);
            if (isCrisisNow && !party.isBrokeStateActive()) {
                party.setBrokeStateActive(true);
                session.getLastRoundCommentary().add("🚨 " + party.getName() + " has entered a critical resource crisis and is fighting for survival!");
            } else if (!isCrisisNow && party.isBrokeStateActive()) {
                party.setBrokeStateActive(false);
                session.getLastRoundCommentary().add("✅ " + party.getName() + " has successfully recovered from their resource crisis.");
            }

            if (party.isBrokeStateActive()) {
                brokeFightBackService.executeCrisisResponse(session, party, submission);
                submission.setAiDecisionBasis(explanation + " [CRISIS OVERRIDE APPLIED]");
            }

            session.getCurrentRoundSubmissions().add(submission);
            generateAiProactiveOffer(session, party);
        }
    }

    public List<NewsDefinition> getCurrentNews(GameSession session) {
        String monthTag = session.getCurrentDate().getYear() + "-" + String.format("%02d", session.getCurrentDate().getMonthValue());
        return getNewsForScenario(session.getScenarioKey()).stream()
                .filter(NewsDefinition::isActive)
                .filter(news -> news.getMonthTags().contains(monthTag)
                        || news.getMonthTags().contains(session.getCurrentDate().getMonth().name().toLowerCase()))
                .limit(1)
                .toList();
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

    public List<CardDefinition> getAvailableCardsForParty(GameSession session, PartyState party) {
        List<CardDefinition> cards = new java.util.ArrayList<>(
            getCardsForSession(session).stream()
                .filter(CardDefinition::isActive)
                .filter(card -> card.getRoleAllowed().contains(party.getRole().name()))
                .filter(card -> "no_card".equals(card.getCardKey()) || usedCount(session, party, card) < 3)
                .filter(card -> party.getStats().getCoins() >= card.getCost())
                // No-Confidence Motion can only be played by OPPOSITION or THIRD_PARTY, never by GOVERNMENT
                .filter(card -> !(card.getCardKey() != null && card.getCardKey().contains("no_confidence")
                        && party.getRole() == com.politicalsim.party.PartyRole.GOVERNMENT))
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

    private PartyState chooseOpponentExcludingPacts(GameSession session, PartyState actor) {
        return session.getParties().stream()
                .filter(PartyState::isActive)
                .filter(party -> !party.getId().equals(actor.getId()))
                .filter(party -> {
                    if (session.getActivePacts() != null) {
                        for (NonAggressionPact pact : session.getActivePacts()) {
                            if ((pact.getPartyAId().equals(actor.getId()) && pact.getPartyBId().equals(party.getId()))
                                    || (pact.getPartyAId().equals(party.getId()) && pact.getPartyBId().equals(actor.getId()))) {
                                return false;
                            }
                        }
                    }
                    return true;
                })
                .max(Comparator.comparingInt(party -> party.getStats().getPublicSupport()))
                .orElse(null);
    }

    private int calculateSmartBid(GameSession session, PartyState party, String metric, int currentMetricValue) {
        // AI players are allowed to place bids for rewards normally again
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
        if (currentMetricValue <= 0 && !"CORRUPTION".equalsIgnoreCase(metric)) {
            return 0;
        }

        // Defeat condition checks before bidding:
        // Conserve resources if party is in a danger/warning zone on any metrics
        PartyStats stats = party.getStats();
        boolean hasDefeatHazard = stats.getCoins() <= 20
                || stats.getPartyMorale() <= 18
                || stats.getPublicSupport() <= 10
                || stats.getCorruptionScore() >= 75;

        if (hasDefeatHazard) {
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
            int minReserve = Math.max(coinReserve, 20); // Absolute safety reserve of 20 coins
            int usable = Math.max(0, currentMetricValue - minReserve);
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
        } else if ("CORRUPTION".equalsIgnoreCase(metric)) {
            int headroom = Math.max(0, 95 - stats.getCorruptionScore());
            if (headroom > 0) {
                int minBid = Math.max(1, (int) Math.ceil(headroom * 0.05 * bidMultiplier));
                int maxBid = Math.min(20, (int) (headroom * 0.15 * bidMultiplier));
                maxBid = Math.max(minBid, maxBid);
                if (maxBid > minBid) {
                    bid = minBid + new Random().nextInt(maxBid - minBid + 1);
                } else {
                    bid = minBid;
                }
            }
        } else if ("PARTY_MORALE".equalsIgnoreCase(metric) || "MORALE".equalsIgnoreCase(metric)) {
            int minReserve = Math.max(moraleReserve, 18); // Absolute safety reserve of 18 morale
            int usable = Math.max(0, currentMetricValue - minReserve);
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
            int minReserve = Math.max(supportReserve, 10); // Absolute safety reserve of 10 support
            int usable = Math.max(0, currentMetricValue - minReserve);
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
        
        // 4. Enforce strict limits:
        // - Capped at 20% of current metric value (or headroom for corruption)
        int maxAllowedBid = "CORRUPTION".equalsIgnoreCase(metric)
                ? (int) (Math.max(0, 95 - stats.getCorruptionScore()) * 0.20)
                : (int) (currentMetricValue * 0.20);
        bid = Math.min(bid, maxAllowedBid);

        // - "go slow with min Bids at first turns" (First 15 turns)
        if (session.getTurnNumber() <= 15) {
            if ("COINS".equalsIgnoreCase(metric)) {
                bid = Math.min(bid, 4);
            } else if ("PARTY_MORALE".equalsIgnoreCase(metric) || "MORALE".equalsIgnoreCase(metric)) {
                bid = Math.min(bid, 5);
            } else if ("PUBLIC_SUPPORT".equalsIgnoreCase(metric) || "SUPPORT".equalsIgnoreCase(metric)) {
                bid = Math.min(bid, 1);
            } else if ("CORRUPTION".equalsIgnoreCase(metric)) {
                bid = Math.min(bid, 6);
            } else {
                bid = Math.min(bid, 3);
            }
        }

        // Cycle reward utility check:
        // Bid only if AI needs the reward (utility >= 0.3). Moderate need (0.3 <= utility < 0.6) scales bid down by 50%.
        RewardDefinition currentReward = null;
        if (session.getCurrentRewardKey() != null) {
            currentReward = RoundResolutionEngine.REWARD_POOL.stream()
                    .filter(r -> r.key().equals(session.getCurrentRewardKey()))
                    .findFirst()
                    .orElse(null);
        }
        if (currentReward != null) {
            double rewardUtility = aiDecisionService.evaluateRewardUtility(session, party, currentReward);
            if (rewardUtility < 0.3) {
                return 0;
            } else if (rewardUtility < 0.6) {
                bid = (int) Math.ceil(bid * 0.5);
            }
        }
        
        return Math.min(bid, currentMetricValue);
    }

    PartyState findParty(GameSession session, String partyId) {
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

    private String getAlternativeScenarioKey(String scenarioKey) {
        if (scenarioKey == null) return null;
        if ("maharashtra_2001".equals(scenarioKey)) return "Mh_2001";
        if ("Mh_2001".equals(scenarioKey)) return "maharashtra_2001";
        return null;
    }

    private List<CardDefinition> getCardsForScenario(String scenarioKey) {
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

    private List<CardDefinition> getCardsForSession(GameSession session) {
        if (session.getGameCards() != null && !session.getGameCards().isEmpty()) {
            return session.getGameCards();
        }
        return getCardsForScenario(session.getScenarioKey());
    }

    public TurnView fundProject(String gameId, String partyId, String projectIdOrKey, int progress) {
        GameSession session = getGame(gameId);
        if (session.getStatus() != GameStatus.ACTIVE) {
            throw new IllegalArgumentException("The game has already ended (Status: " + session.getStatus() + ").");
        }
        PartyState party = session.getParties().stream()
                .filter(p -> p.getId().equals(partyId))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Party not found: " + partyId));

        ProjectState project = party.getProjects().stream()
                .filter(p -> (p.getId() != null && p.getId().equals(projectIdOrKey)) || p.getProjectKey().equals(projectIdOrKey))
                .filter(p -> p.getProgressPercent() < 100)
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Incomplete project not found: " + projectIdOrKey));

        BuildingProject projectDef = BuildingProject.valueOf(project.getProjectKey());
        int remaining = 100 - project.getProgressPercent();
        int actualProgress = Math.min(progress, remaining);

        if (actualProgress <= 0) {
            throw new IllegalArgumentException("Invalid progress contribution.");
        }

        int coinsCost = (int) Math.ceil((double) projectDef.getCostCoins() * actualProgress / 100.0);
        int moraleCost = (int) Math.ceil((double) projectDef.getCostMorale() * actualProgress / 100.0);
        int corruptionCost = (int) Math.ceil((double) projectDef.getCostCorruption() * actualProgress / 100.0);
        int mediaCost = (int) Math.ceil((double) projectDef.getCostMedia() * actualProgress / 100.0);
        int supportCost = (int) Math.ceil((double) projectDef.getCostSupport() * actualProgress / 100.0);

        if (party.getStats().getCoins() < coinsCost) {
            throw new IllegalArgumentException("Insufficient coins: requires " + coinsCost + " but you have " + party.getStats().getCoins() + ".");
        }
        if (party.getStats().getPartyMorale() < moraleCost) {
            throw new IllegalArgumentException("Insufficient morale: requires " + moraleCost + " but you have " + party.getStats().getPartyMorale() + ".");
        }
        if (party.getStats().getMediaImage() < mediaCost) {
            throw new IllegalArgumentException("Insufficient Media Image: requires " + mediaCost + " but you have " + party.getStats().getMediaImage() + ".");
        }
        if (party.getStats().getPublicSupport() < supportCost) {
            throw new IllegalArgumentException("Insufficient Public Support: requires " + supportCost + " but you have " + party.getStats().getPublicSupport() + ".");
        }

        // Deduct/apply immediately
        party.getStats().setCoins(party.getStats().getCoins() - coinsCost);
        party.getStats().setPartyMorale(party.getStats().getPartyMorale() - moraleCost);
        party.getStats().setMediaImage(party.getStats().getMediaImage() - mediaCost);
        party.getStats().setCorruptionScore(Math.min(100, party.getStats().getCorruptionScore() + corruptionCost));
        if (supportCost > 0) {
            party.getStats().setPublicSupport(Math.max(0, party.getStats().getPublicSupport() - supportCost));
            session.getPublicState().setUndecidedSupport(session.getPublicState().getUndecidedSupport() + supportCost);
        }

        project.setProgressPercent(project.getProgressPercent() + actualProgress);
        if (project.getProgressPercent() == 100 && project.getCompletionTurn() == 0) {
            project.setCompletionTurn(session.getTurnNumber());
        }

        if (project.getProgressPercent() >= 100) {
            boolean hasIncomplete = party.getProjects().stream()
                    .anyMatch(p -> p.getProjectKey().equals(project.getProjectKey()) && p.getProgressPercent() < 100);
            if (!hasIncomplete) {
                party.getProjects().add(new ProjectState(project.getProjectKey()));
            }
        }

        // Record human contribution
        Map<String, Map<String, Integer>> contribs = session.getProjectContributionsThisTurn();
        Map<String, Integer> partyContribs = contribs.computeIfAbsent(partyId, k -> new java.util.LinkedHashMap<>());
        partyContribs.put(project.getProjectKey(), partyContribs.getOrDefault(project.getProjectKey(), 0) + actualProgress);

        gameSessionService.save(session);
        return getTurnView(gameId);
    }

    public TurnView destroyProject(String gameId, String partyId, String projectIdOrKey) {
        GameSession session = getGame(gameId);
        if (session.getStatus() != GameStatus.ACTIVE) {
            throw new IllegalArgumentException("The game has already ended (Status: " + session.getStatus() + ").");
        }
        PartyState party = session.getParties().stream()
                .filter(p -> p.getId().equals(partyId))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Party not found: " + partyId));

        ProjectState project = party.getProjects().stream()
                .filter(p -> (p.getId() != null && p.getId().equals(projectIdOrKey)) || p.getProjectKey().equals(projectIdOrKey))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Project not found: " + projectIdOrKey));

        BuildingProject projectDef = BuildingProject.valueOf(project.getProjectKey());
        int progress = project.getProgressPercent();

        if (progress <= 0) {
            throw new IllegalArgumentException("Cannot destroy project with no progress built.");
        }

        // Calculate refund
        int refundCoins = (int) Math.ceil((double) projectDef.getCostCoins() * progress / 100.0);
        int refundMorale = (int) Math.ceil((double) projectDef.getCostMorale() * progress / 100.0);
        int refundCorruption = (int) Math.ceil((double) projectDef.getCostCorruption() * progress / 100.0);
        int refundMedia = (int) Math.ceil((double) projectDef.getCostMedia() * progress / 100.0);
        int refundSupport = (int) Math.ceil((double) projectDef.getCostSupport() * progress / 100.0);

        // Refund stats
        party.getStats().setCoins(party.getStats().getCoins() + refundCoins);
        party.getStats().setPartyMorale(Math.min(100, party.getStats().getPartyMorale() + refundMorale));
        party.getStats().setMediaImage(Math.min(100, party.getStats().getMediaImage() + refundMedia));
        party.getStats().setCorruptionScore(Math.max(0, party.getStats().getCorruptionScore() - refundCorruption));
        if (refundSupport > 0) {
            party.getStats().setPublicSupport(Math.min(100, party.getStats().getPublicSupport() + refundSupport));
        }

        party.getProjects().remove(project);

        String salvageMsg = party.getName() + " destroyed project '" + projectDef.getName() 
                + "' and recovered spent resources: " + refundCoins + " Coins" 
                + (refundMorale > 0 ? ", " + refundMorale + " Morale" : "") + ".";
        session.getLastRoundCommentary().add("🛠️ " + salvageMsg);

        gameSessionService.save(session);
        return getTurnView(gameId);
    }

    public TurnView setProjectTarget(String gameId, String partyId, String projectIdOrKey, String targetPartyId) {
        GameSession session = getGame(gameId);
        if (session.getStatus() != GameStatus.ACTIVE) {
            throw new IllegalArgumentException("The game has already ended (Status: " + session.getStatus() + ").");
        }
        PartyState party = session.getParties().stream()
                .filter(p -> p.getId().equals(partyId))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Party not found: " + partyId));

        ProjectState project = party.getProjects().stream()
                .filter(p -> (p.getId() != null && p.getId().equals(projectIdOrKey)) || p.getProjectKey().equals(projectIdOrKey))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Project not found: " + projectIdOrKey));

        if (project.getProgressPercent() < 100) {
            throw new IllegalArgumentException("Project must be completed to assign target.");
        }

        BuildingProject projectDef = BuildingProject.valueOf(project.getProjectKey());
        if (!projectDef.isRequiresTarget()) {
            throw new IllegalArgumentException("Project does not require target.");
        }

        PartyState target = session.getParties().stream()
                .filter(p -> p.getId().equals(targetPartyId))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Target party not found: " + targetPartyId));

        if (target.getId().equals(party.getId())) {
            throw new IllegalArgumentException("Cannot target yourself.");
        }

        project.setTargetPartyId(target.getId());
        project.setTargetPartyName(target.getName());

        gameSessionService.save(session);
        return getTurnView(gameId);
    }

    private record ProjectScore(ProjectState project, BuildingProject projectDef, double score) {
    }

    private double scoreProjectForAi(GameSession session, PartyState party, AiDecision decision, BuildingProject projectDef) {
        double score = 0.0;
        int turn = session.getTurnNumber();
        
        // 1. Base Strategy Weight: Passive yields are stronger in the early/mid game.
        // Offensive yields are stronger in the late game to pull down the front runner.
        if (!projectDef.isRequiresTarget()) {
            score += Math.max(0, 60 - turn) * 0.8;
        } else {
            score += turn * 1.0;
        }
        
        // 2. Adjust based on AI Intent / Style
        AiProfile profile = party.getAiProfile() == null ? AiProfile.defaultForRole(party.getRole()) : party.getAiProfile();
        AiStyle style = profile.getStyle();
        
        // If GAIN_SUPPORT or PREPARE_ELECTION, boost projects with support benefits
        if (decision.intent() == AiIntent.GAIN_SUPPORT || decision.intent() == AiIntent.PREPARE_ELECTION) {
            score += projectDef.getBenefitSupport() * 30.0;
        }
        
        // If RESTORE_MORALE, boost morale-generating projects
        if (decision.intent() == AiIntent.RESTORE_MORALE) {
            score += projectDef.getBenefitMorale() * 20.0;
        }
        
        // If RAISE_FUNDS, boost coins-generating projects
        if (decision.intent() == AiIntent.RAISE_FUNDS) {
            score += projectDef.getBenefitCoins() * 10.0;
        }
        
        // Style-specific preferences
        if (style == AiStyle.STRENGTH_BUILDER) {
            // Prefers defensive / economic passive building
            if (!projectDef.isRequiresTarget()) {
                score += 25.0;
            } else {
                score -= 15.0;
            }
        } else if (style == AiStyle.AGGRESSIVE_ATTACKER) {
            // Prefers offensive projects targeting opponents
            if (projectDef.isRequiresTarget()) {
                score += 30.0;
            } else {
                score -= 10.0;
            }
        } else if (style == AiStyle.LATE_STRIKER) {
            if (turn < 40) {
                // Focus on strength first
                if (!projectDef.isRequiresTarget()) score += 20.0;
            } else {
                // Aggressive attacks later
                if (projectDef.isRequiresTarget()) score += 35.0;
            }
        } else if (style == AiStyle.AGGRESSIVE_BIDDER) {
            // Prefers projects that yield coins or morale to fund future bids
            score += projectDef.getBenefitCoins() * 8.0;
            score += projectDef.getBenefitMorale() * 8.0;
        }
        
        // 3. Avoid corruption if party has high aversion or is Anti-Corruption
        if (party.getIdeology() == com.politicalsim.party.Ideology.ANTI_CORRUPTION) {
            score -= projectDef.getCostCorruption() * 2.0;
        }

        // 4. Repeat Penalties: Reduce priority for projects already completed
        long completedCount = 0;
        if (party.getProjects() != null) {
            completedCount = party.getProjects().stream()
                .filter(p -> p.getProjectKey().equals(projectDef.name()) && p.getProgressPercent() >= 100)
                .count();
        }
        if (completedCount > 0) {
            if (!projectDef.isRequiresTarget()) {
                // Unique infrastructure projects should not be spammed
                if (projectDef == BuildingProject.PARTY_HQ || projectDef == BuildingProject.IT_CELL 
                    || projectDef == BuildingProject.CADRE_OFFICE || projectDef == BuildingProject.THINK_TANK 
                    || projectDef == BuildingProject.TRAINING_ACADEMY || projectDef == BuildingProject.YOUTH_WING 
                    || projectDef == BuildingProject.MEDIA_HOUSE) {
                    score -= completedCount * 50.0;
                } else {
                    // Event-type projects can be repeated but with penalty
                    score -= completedCount * 15.0;
                }
            } else {
                // Offensive projects targeting other players
                score -= completedCount * 12.0;
            }
        }

        // 5. Threat Recognition & Support Crisis
        long hostileProjectsTargetingMe = 0;
        for (PartyState other : session.getParties()) {
            if (other.getId().equals(party.getId())) continue;
            if (other.getProjects() == null) continue;
            for (ProjectState otherProj : other.getProjects()) {
                if (otherProj.getProgressPercent() >= 100 && party.getId().equals(otherProj.getTargetPartyId())) {
                    hostileProjectsTargetingMe++;
                }
            }
        }

        int maxOpponentSupport = session.getParties().stream()
            .filter(p -> !p.getId().equals(party.getId()))
            .mapToInt(p -> p.getStats().getPublicSupport())
            .max().orElse(0);
        int supportGap = maxOpponentSupport - party.getStats().getPublicSupport();

        if (hostileProjectsTargetingMe > 0 || supportGap > 15 || party.getStats().getPublicSupport() < 25) {
            // Boost offensive projects to target opponents when under threat
            if (projectDef.isRequiresTarget()) {
                score += 20.0 + (hostileProjectsTargetingMe * 5.0) + (supportGap * 0.5);
            }
            // Boost projects that give support if undecided support is available
            if (projectDef.getBenefitSupport() > 0 && session.getPublicState() != null 
                && session.getPublicState().getUndecidedSupport() > 0) {
                score += projectDef.getBenefitSupport() * 25.0;
            }
        }

        // 6. Grudge System Integration
        Map<String, Map<String, Integer>> grudges = session.getGrudges();
        if (grudges != null && grudges.containsKey(party.getId())) {
            Map<String, Integer> myGrudges = grudges.get(party.getId());
            int maxGrudgeValue = myGrudges.values().stream().mapToInt(Integer::intValue).max().orElse(0);
            if (maxGrudgeValue > 0 && projectDef.isRequiresTarget()) {
                score += maxGrudgeValue * 8.0;
            }
        }

        // 7. Resource Situational Alignment
        PartyStats stats = party.getStats();
        if (stats != null) {
            if (stats.getCoins() < 100) {
                score += projectDef.getBenefitCoins() * 15.0;
                score -= projectDef.getCostCoins() * 0.5;
            }
            if (stats.getPartyMorale() < 40) {
                score += projectDef.getBenefitMorale() * 20.0;
            }
            if (stats.getCorruptionScore() > 50) {
                score -= projectDef.getBenefitCorruption() * 20.0; // benefitCorruption is negative for reduction
            }
            if (stats.getMediaImage() < 40) {
                score += projectDef.getBenefitMedia() * 15.0;
            }
        }
        
        return score;
    }

    public TurnView createCooperationOffer(String gameId, CooperationOffer offer) {
        GameSession session = getGame(gameId);
        if (session.getStatus() != GameStatus.ACTIVE) {
            throw new IllegalArgumentException("The game has already ended.");
        }
        
        offer.setId(java.util.UUID.randomUUID().toString());
        offer.setStatus(CooperationOffer.OfferStatus.PENDING);
        offer.setTurnCreated(session.getTurnNumber());
        
        PartyState sender = findParty(session, offer.getSenderPartyId());
        PartyState recipient = findParty(session, offer.getRecipientPartyId());
        
        // Validate sender has enough assets
        validateOfferSenderAssets(session, sender, offer);
        
        // Log proposal
        String proposalDesc = getOfferDescription(offer);
        session.getLastRoundCommentary().add("🤝 " + sender.getName() + " proposed a deal to " + recipient.getName() + ": " + proposalDesc);
        session.getLastResults().add("🤝 " + sender.getName() + " proposed deal: " + proposalDesc);
        
        if (recipient.getControllerType() == ControllerType.COMPUTER) {
            boolean accepted = aiDecisionService.evaluateCooperationOffer(session, recipient, offer);
            if (accepted) {
                executeCooperationTrade(session, offer);
                offer.setStatus(CooperationOffer.OfferStatus.ACCEPTED);
                session.getLastRoundCommentary().add("✅ " + recipient.getName() + " accepted the deal with " + sender.getName() + ": " + proposalDesc);
                session.getLastResults().add("✅ " + recipient.getName() + " accepted deal from " + sender.getName());
            } else {
                offer.setStatus(CooperationOffer.OfferStatus.REJECTED);
                session.getLastRoundCommentary().add("❌ " + recipient.getName() + " rejected the deal proposed by " + sender.getName() + ".");
                session.getLastResults().add("❌ " + recipient.getName() + " rejected deal from " + sender.getName());
            }
        }
        
        session.getCooperationOffers().add(offer);
        gameSessionService.save(session);
        return getTurnView(gameId);
    }
    
    public TurnView respondToCooperationOffer(String gameId, String offerId, boolean accept) {
        GameSession session = getGame(gameId);
        if (session.getStatus() != GameStatus.ACTIVE) {
            throw new IllegalArgumentException("The game has already ended.");
        }
        
        CooperationOffer offer = session.getCooperationOffers().stream()
            .filter(o -> o.getId().equals(offerId))
            .findFirst()
            .orElseThrow(() -> new IllegalArgumentException("Offer not found: " + offerId));
            
        if (offer.getStatus() != CooperationOffer.OfferStatus.PENDING) {
            throw new IllegalArgumentException("Offer is already resolved.");
        }
        
        PartyState sender = findParty(session, offer.getSenderPartyId());
        PartyState recipient = findParty(session, offer.getRecipientPartyId());
        String proposalDesc = getOfferDescription(offer);
        
        if (accept) {
            // Re-validate assets before executing
            validateOfferSenderAssets(session, sender, offer);
            validateOfferRecipientAssets(session, recipient, offer);
            
            executeCooperationTrade(session, offer);
            offer.setStatus(CooperationOffer.OfferStatus.ACCEPTED);
            session.getLastRoundCommentary().add("✅ " + recipient.getName() + " accepted the deal with " + sender.getName() + ": " + proposalDesc);
            session.getLastResults().add("✅ " + recipient.getName() + " accepted deal from " + sender.getName());
        } else {
            offer.setStatus(CooperationOffer.OfferStatus.REJECTED);
            session.getLastRoundCommentary().add("❌ " + recipient.getName() + " rejected the deal proposed by " + sender.getName() + ".");
            session.getLastResults().add("❌ " + recipient.getName() + " rejected deal from " + sender.getName());
        }
        
        gameSessionService.save(session);
        return getTurnView(gameId);
    }
    
    private void validateOfferSenderAssets(GameSession session, PartyState sender, CooperationOffer offer) {
        cooperationResolver.validateOfferSenderAssets(session, sender, offer);
    }
    
    private void validateOfferRecipientAssets(GameSession session, PartyState recipient, CooperationOffer offer) {
        cooperationResolver.validateOfferRecipientAssets(session, recipient, offer);
    }
    
    private void validatePactPayment(PartyState payer, CooperationOffer offer) {
        cooperationResolver.validatePactPayment(payer, offer);
    }
    
    private String getOfferDescription(CooperationOffer offer) {
        return cooperationResolver.getOfferDescription(offer);
    }
    
    private void executeCooperationTrade(GameSession session, CooperationOffer offer) {
        cooperationResolver.executeCooperationTrade(session, offer);
    }
    
    private void generateAiProactiveOffer(GameSession session, PartyState party) {
        for (PartyState other : session.getParties()) {
            if (!other.isActive() || other.getId().equals(party.getId())) {
                continue;
            }
            
            // Check if other party has low coins
            if (other.getStats().getCoins() < 100) {
                // Check if they have healthy support
                if (other.getStats().getPublicSupport() > 20 && party.getStats().getCoins() >= 150) {
                    CooperationOffer offer = new CooperationOffer();
                    offer.setId(java.util.UUID.randomUUID().toString());
                    offer.setSenderPartyId(party.getId());
                    offer.setSenderPartyName(party.getName());
                    offer.setRecipientPartyId(other.getId());
                    offer.setRecipientPartyName(other.getName());
                    offer.setType(CooperationOffer.OfferType.EXCHANGE);
                    offer.setOfferedCoins(50);
                    offer.setRequestedSupport(3);
                    offer.setStatus(CooperationOffer.OfferStatus.PENDING);
                    offer.setTurnCreated(session.getTurnNumber());
                    
                    String proposalDesc = getOfferDescription(offer);
                    session.getLastRoundCommentary().add("🤝 " + party.getName() + " proposed a trade deal to " + other.getName() + ": " + proposalDesc);
                    session.getLastResults().add("🤝 " + party.getName() + " proposed trade: 50 Coins for 3% Support to " + other.getName());
                    
                    if (other.getControllerType() == ControllerType.COMPUTER) {
                        boolean accepted = aiDecisionService.evaluateCooperationOffer(session, other, offer);
                        if (accepted) {
                            executeCooperationTrade(session, offer);
                            offer.setStatus(CooperationOffer.OfferStatus.ACCEPTED);
                            session.getLastRoundCommentary().add("✅ " + other.getName() + " accepted the deal with " + party.getName() + ": " + proposalDesc);
                            session.getLastResults().add("✅ " + other.getName() + " accepted deal from " + party.getName());
                        } else {
                            offer.setStatus(CooperationOffer.OfferStatus.REJECTED);
                            session.getLastRoundCommentary().add("❌ " + other.getName() + " rejected the deal proposed by " + party.getName() + ".");
                            session.getLastResults().add("❌ " + other.getName() + " rejected deal from " + party.getName());
                        }
                    }
                    
                    session.getCooperationOffers().add(offer);
                    break; // Make at most one proactive offer per turn
                }
                
                // Else check if they have healthy morale
                if (other.getStats().getPartyMorale() > 40 && party.getStats().getCoins() >= 130) {
                    CooperationOffer offer = new CooperationOffer();
                    offer.setId(java.util.UUID.randomUUID().toString());
                    offer.setSenderPartyId(party.getId());
                    offer.setSenderPartyName(party.getName());
                    offer.setRecipientPartyId(other.getId());
                    offer.setRecipientPartyName(other.getName());
                    offer.setType(CooperationOffer.OfferType.EXCHANGE);
                    offer.setOfferedCoins(30);
                    offer.setRequestedMorale(5);
                    offer.setStatus(CooperationOffer.OfferStatus.PENDING);
                    offer.setTurnCreated(session.getTurnNumber());
                    
                    String proposalDesc = getOfferDescription(offer);
                    session.getLastRoundCommentary().add("🤝 " + party.getName() + " proposed a trade deal to " + other.getName() + ": " + proposalDesc);
                    session.getLastResults().add("🤝 " + party.getName() + " proposed trade: 30 Coins for 5 Morale to " + other.getName());
                    
                    if (other.getControllerType() == ControllerType.COMPUTER) {
                        boolean accepted = aiDecisionService.evaluateCooperationOffer(session, other, offer);
                        if (accepted) {
                            executeCooperationTrade(session, offer);
                            offer.setStatus(CooperationOffer.OfferStatus.ACCEPTED);
                            session.getLastRoundCommentary().add("✅ " + other.getName() + " accepted the deal with " + party.getName() + ": " + proposalDesc);
                            session.getLastResults().add("✅ " + other.getName() + " accepted deal from " + party.getName());
                        } else {
                            offer.setStatus(CooperationOffer.OfferStatus.REJECTED);
                            session.getLastRoundCommentary().add("❌ " + other.getName() + " rejected the deal proposed by " + party.getName() + ".");
                            session.getLastResults().add("❌ " + other.getName() + " rejected deal from " + party.getName());
                        }
                    }
                    
                    session.getCooperationOffers().add(offer);
                    break; // Make at most one proactive offer per turn
                }
            }
            
            // Early game Non-aggression check (only if Turn <= 20 and no active pact)
            boolean hasActivePact = false;
            if (session.getActivePacts() != null) {
                for (NonAggressionPact pact : session.getActivePacts()) {
                    if ((pact.getPartyAId().equals(party.getId()) && pact.getPartyBId().equals(other.getId()))
                            || (pact.getPartyAId().equals(other.getId()) && pact.getPartyBId().equals(party.getId()))) {
                        hasActivePact = true;
                        break;
                    }
                }
            }
            
            if (!hasActivePact && session.getTurnNumber() <= 20 && party.getStats().getCoins() >= 80) {
                CooperationOffer offer = new CooperationOffer();
                offer.setId(java.util.UUID.randomUUID().toString());
                offer.setSenderPartyId(party.getId());
                offer.setSenderPartyName(party.getName());
                offer.setRecipientPartyId(other.getId());
                offer.setRecipientPartyName(other.getName());
                offer.setType(CooperationOffer.OfferType.NON_AGGRESSION);
                offer.setDurationTurns(10);
                offer.setSenderPaysPact(true);
                offer.setPactPaymentResource("COINS");
                offer.setPactPaymentValue(5);
                offer.setStatus(CooperationOffer.OfferStatus.PENDING);
                offer.setTurnCreated(session.getTurnNumber());
                
                String proposalDesc = getOfferDescription(offer);
                session.getLastRoundCommentary().add("🤝 " + party.getName() + " proposed a pact to " + other.getName() + ": " + proposalDesc);
                session.getLastResults().add("🤝 " + party.getName() + " proposed pact to " + other.getName());
                
                if (other.getControllerType() == ControllerType.COMPUTER) {
                    boolean accepted = aiDecisionService.evaluateCooperationOffer(session, other, offer);
                    if (accepted) {
                        executeCooperationTrade(session, offer);
                        offer.setStatus(CooperationOffer.OfferStatus.ACCEPTED);
                        session.getLastRoundCommentary().add("✅ " + other.getName() + " accepted the deal with " + party.getName() + ": " + proposalDesc);
                        session.getLastResults().add("✅ " + other.getName() + " accepted deal from " + party.getName());
                    } else {
                        offer.setStatus(CooperationOffer.OfferStatus.REJECTED);
                        session.getLastRoundCommentary().add("❌ " + other.getName() + " rejected the deal proposed by " + party.getName() + ".");
                        session.getLastResults().add("❌ " + other.getName() + " rejected deal from " + party.getName());
                    }
                }
                
                session.getCooperationOffers().add(offer);
                break; // One offer per turn
            }

            // Change 8: Coalition vs dominant human player
            // If a human party leads all AI parties by 10%+ support, AI parties offer each other
            // FREE non-aggression pacts (no payment) beyond the early game window.
            if (!hasActivePact && other.getControllerType() == ControllerType.COMPUTER) {
                PartyState humanLeader = session.getParties().stream()
                        .filter(p -> p.isActive() && p.getControllerType() == ControllerType.HUMAN)
                        .max(java.util.Comparator.comparingInt(p -> p.getStats().getPublicSupport()))
                        .orElse(null);
                boolean humanDominating = humanLeader != null
                        && humanLeader.getStats().getPublicSupport() > party.getStats().getPublicSupport() + 10
                        && humanLeader.getStats().getPublicSupport() > other.getStats().getPublicSupport() + 10;
                if (humanDominating) {
                    CooperationOffer coalitionPact = new CooperationOffer();
                    coalitionPact.setId(java.util.UUID.randomUUID().toString());
                    coalitionPact.setSenderPartyId(party.getId());
                    coalitionPact.setSenderPartyName(party.getName());
                    coalitionPact.setRecipientPartyId(other.getId());
                    coalitionPact.setRecipientPartyName(other.getName());
                    coalitionPact.setType(CooperationOffer.OfferType.NON_AGGRESSION);
                    coalitionPact.setDurationTurns(8);
                    coalitionPact.setSenderPaysPact(false); // Free — both sides benefit
                    coalitionPact.setPactPaymentValue(0);
                    coalitionPact.setStatus(CooperationOffer.OfferStatus.PENDING);
                    coalitionPact.setTurnCreated(session.getTurnNumber());

                    String proposalDesc = getOfferDescription(coalitionPact);
                    session.getLastRoundCommentary().add("🤝 " + party.getName()
                            + " proposed a defensive coalition pact to " + other.getName()
                            + " (" + humanLeader.getName() + " is leading): " + proposalDesc);
                    session.getLastResults().add("🤝 " + party.getName() + " proposed free coalition pact to " + other.getName());

                    boolean accepted = aiDecisionService.evaluateCooperationOffer(session, other, coalitionPact);
                    if (accepted) {
                        executeCooperationTrade(session, coalitionPact);
                        coalitionPact.setStatus(CooperationOffer.OfferStatus.ACCEPTED);
                        session.getLastRoundCommentary().add("✅ " + other.getName()
                                + " accepted the defensive coalition pact with " + party.getName() + ".");
                        session.getLastResults().add("✅ Coalition pact accepted: " + party.getName() + " & " + other.getName());
                    } else {
                        coalitionPact.setStatus(CooperationOffer.OfferStatus.REJECTED);
                        session.getLastRoundCommentary().add("❌ " + other.getName()
                                + " declined the coalition pact from " + party.getName() + ".");
                    }
                    session.getCooperationOffers().add(coalitionPact);
                    break; // One offer per turn
                }
            }
        }
    }

    private record NoConfidenceStatus(boolean available, String reason) {
    }

    private void ensureSecretMetricInitialized(GameSession session) {
        if (session.getSecretMetricSequence() == null || session.getSecretMetricSequence().isEmpty() || session.getSecretMetric() == null) {
            java.util.List<String> list = new java.util.ArrayList<>();
            for (int i = 0; i < 6; i++) {
                list.add("COINS");
                list.add("MORALE");
                list.add("MEDIA_IMAGE");
                list.add("CORRUPTION");
                list.add("PUBLIC_SUPPORT");
            }
            java.util.Collections.shuffle(list);
            session.setSecretMetricSequence(list);
            session.setSecretMetric(list.get(0));
        }
    }

    public TurnView bribeFaction(String gameId, String targetPartyId, String factionKey, int coins) {
        GameSession session = getGame(gameId);
        PartyState sender = getActiveHumanParty(session);
        if (sender == null) {
            throw new IllegalArgumentException("No active human player found.");
        }
        if (sender.getId().equals(targetPartyId)) {
            throw new IllegalArgumentException("Cannot target your own party with a bribe.");
        }
        PartyState targetParty = findParty(session, targetPartyId);
        if (targetParty == null || !targetParty.isActive() || targetParty.getRole() == com.politicalsim.party.PartyRole.DEFEATED) {
            throw new IllegalArgumentException("Target party is not active or defeated.");
        }

        com.politicalsim.party.FactionState fs = targetParty.getFactions().stream()
                .filter(f -> f.getKey().equals(factionKey))
                .findFirst().orElse(null);
        if (fs == null || !fs.isActive()) {
            throw new IllegalArgumentException("Target faction is not active.");
        }

        if (coins <= 0) {
            throw new IllegalArgumentException("Bribe coins must be greater than zero.");
        }

        // Bribe costs coins
        if (sender.getStats().getCoins() < coins) {
            throw new IllegalArgumentException("Insufficient coins. Bribe costs " + coins + " Coins.");
        }

        // Deduct coins
        sender.getStats().setCoins(sender.getStats().getCoins() - coins);

        // 1. Calculate Target Faction Coin Yield
        int patronageCoins = fs.getPatronage() * 2;
        int postCoins = 0;
        if (fs.getPost() != null) {
            for (String pKey : fs.getPost()) {
                PostsConfig.PostDefinition def = PostsConfig.findByKey(pKey);
                if (def == null) def = PostsConfig.findByName(pKey);
                if (def != null) postCoins += def.coinYieldBonus();
            }
        }
        int baseCoins = patronageCoins + postCoins;
        for (ProjectState ps : targetParty.getProjects()) {
            if (ps.getProgressPercent() == 100 && fs.getKey().equals(ps.getManagingFactionKey())) {
                try {
                    BuildingProject bProj = BuildingProject.valueOf(ps.getProjectKey());
                    baseCoins += bProj.getBenefitCoins();
                } catch (Exception e) {
                    // ignore invalid enum
                }
            }
        }

        // 2. Success Probability based on offered coins, target party coins, game turn, and random chance
        double baseProb = 0.20;
        double turnFactor = (double) session.getTurnNumber() / 100.0;
        if (turnFactor > 0.40) {
            turnFactor = 0.40; // cap turn influence at +40%
        }

        // Count currently frozen assets for successive bribe scaling
        int frozenCount = 0;
        if (fs.getFrozenPosts() != null) {
            for (int turns : fs.getFrozenPosts().values()) {
                if (turns > 0) frozenCount++;
            }
        }
        if (fs.getFrozenPatronageTurns() != null) {
            frozenCount += fs.getFrozenPatronageTurns().size();
        }
        if (targetParty.getProjects() != null) {
            for (ProjectState ps : targetParty.getProjects()) {
                if (fs.getKey().equals(ps.getManagingFactionKey()) && ps.getFrozenTurnsRemaining() > 0) {
                    frozenCount++;
                }
            }
        }

        double targetPartyCoins = targetParty.getStats().getCoins();
        // Recalibrated formula: Toned down successive scaling to +30 and adjusted baseline target influence
        double cashFactor = (double) coins / (200.0 + (targetPartyCoins * 0.3) + (frozenCount * 30.0));

        double successProb = baseProb + turnFactor + cashFactor;
        successProb = Math.max(0.10, Math.min(0.90, successProb));

        double roll = new java.util.Random().nextDouble();
        if (roll < successProb) {
            // Success! Loyalty Loss
            int loyaltyLoss = 15 + new java.util.Random().nextInt(16); // 15 to 30 loyalty loss
            fs.setLoyalty(Math.max(0, fs.getLoyalty() - loyaltyLoss));

            // Select specific candidate assets to freeze (1 asset per 30 coins offered)
            int numToFreeze = Math.max(1, coins / 30);
            
            class AssetCandidate {
                String type; // "POST", "PROJECT", "PATRONAGE"
                String identifier; // postKey, projectInstanceId, or empty
                String label; // human-readable label
            }

            java.util.List<AssetCandidate> candidates = new java.util.ArrayList<>();

            // 1. Posts Candidates
            if (fs.getPost() != null) {
                for (String pKey : fs.getPost()) {
                    if (pKey == null || pKey.equals("None") || pKey.isBlank()) continue;
                    if (fs.getFrozenPosts() == null || !fs.getFrozenPosts().containsKey(pKey) || fs.getFrozenPosts().get(pKey) <= 0) {
                        AssetCandidate ac = new AssetCandidate();
                        ac.type = "POST";
                        ac.identifier = pKey;
                        ac.label = pKey + " Post";
                        candidates.add(ac);
                    }
                }
            }

            // 2. Projects Candidates
            if (targetParty.getProjects() != null) {
                for (ProjectState ps : targetParty.getProjects()) {
                    if (ps.getProgressPercent() == 100 && fs.getKey().equals(ps.getManagingFactionKey())) {
                        if (ps.getFrozenTurnsRemaining() <= 0) {
                            AssetCandidate ac = new AssetCandidate();
                            ac.type = "PROJECT";
                            ac.identifier = ps.getId();
                            ac.label = (ps.getName() != null ? ps.getName() : ps.getProjectKey()) + " Project";
                            candidates.add(ac);
                        }
                    }
                }
            }

            // 3. Patronage Candidates (can freeze remaining active patronage)
            int currentlyFrozenPatronage = fs.getFrozenPatronageTurns() != null ? fs.getFrozenPatronageTurns().size() : 0;
            int activePatronageCount = fs.getPatronage() - currentlyFrozenPatronage;
            for (int i = 0; i < activePatronageCount; i++) {
                AssetCandidate ac = new AssetCandidate();
                ac.type = "PATRONAGE";
                ac.label = "Patronage Point";
                candidates.add(ac);
            }

            java.util.Collections.shuffle(candidates);
            java.util.List<String> frozenLabels = new java.util.ArrayList<>();

            for (int i = 0; i < Math.min(numToFreeze, candidates.size()); i++) {
                AssetCandidate selected = candidates.get(i);
                if ("POST".equals(selected.type)) {
                    if (fs.getFrozenPosts() == null) {
                        fs.setFrozenPosts(new java.util.HashMap<>());
                    }
                    fs.getFrozenPosts().put(selected.identifier, 10);
                } else if ("PROJECT".equals(selected.type)) {
                    for (ProjectState ps : targetParty.getProjects()) {
                        if (ps.getId().equals(selected.identifier)) {
                            ps.setFrozenTurnsRemaining(10);
                            break;
                        }
                    }
                } else if ("PATRONAGE".equals(selected.type)) {
                    if (fs.getFrozenPatronageTurns() == null) {
                        fs.setFrozenPatronageTurns(new java.util.ArrayList<>());
                    }
                    fs.getFrozenPatronageTurns().add(10);
                }
                frozenLabels.add(selected.label);
            }

            String frozenListStr = frozenLabels.isEmpty() ? "No active cards/assets found to freeze" : String.join(", ", frozenLabels);
            String msg = String.format("🚨 Sabotage Successful: %s bribed %s's %s faction! Loyalty fell by -%d%% (Current: %d%%). The following specific assets are FROZEN for 10 rounds: %s.",
                    sender.getName(), targetParty.getName(), fs.getName(), loyaltyLoss, fs.getLoyalty(), frozenListStr);
            session.getLastRoundCommentary().add(msg);
            session.getLastResults().add("🚨 " + sender.getName() + " successfully bribed and froze opponent faction " + fs.getName());
        } else {
            // Failed: Refused and Exposed
            int mediaLoss = Math.max(5, (int) Math.round(sender.getStats().getMediaImage() * 0.10));
            int moraleLoss = Math.max(3, (int) Math.round(sender.getStats().getPartyMorale() * 0.05));

            sender.getStats().setMediaImage(Math.max(0, sender.getStats().getMediaImage() - mediaLoss));
            sender.getStats().setPartyMorale(Math.max(0, sender.getStats().getPartyMorale() - moraleLoss));

            String msg = String.format("🚨 Bribe Refused & Exposed: %s attempted to bribe %s's %s but was refused! %s loses -%d Media Image (-10%%) and -%d Party Morale (-5%%).",
                    sender.getName(), targetParty.getName(), fs.getName(), sender.getName(), mediaLoss, moraleLoss);
            session.getLastRoundCommentary().add(msg);
            session.getLastResults().add("🚨 " + sender.getName() + " bribe attempt on " + fs.getName() + " exposed!");
        }

        gameSessionService.save(session);
        return getTurnView(gameId);
    }

    private PartyState choosePactTarget(GameSession session, PartyState party) {
        return session.getParties().stream()
                .filter(p -> !p.getId().equals(party.getId()) && p.isActive() && p.getRole() != com.politicalsim.party.PartyRole.DEFEATED)
                .filter(p -> {
                    if (session.getCooperationOffers() == null) return true;
                    return session.getCooperationOffers().stream()
                            .noneMatch(o -> o.getType() == CooperationOffer.OfferType.NON_AGGRESSION 
                                    && o.getStatus() == CooperationOffer.OfferStatus.ACCEPTED
                                    && ((o.getSenderPartyId().equals(party.getId()) && o.getRecipientPartyId().equals(p.getId()))
                                     || (o.getSenderPartyId().equals(p.getId()) && o.getRecipientPartyId().equals(party.getId()))));
                })
                .findAny()
                .orElse(null);
    }

    private double scoreBillForPriority(com.politicalsim.content.LegislativeBillDefinition bill, boolean isDangerCoins, boolean isDangerMorale) {
        Map<String, Object> passedEffects = bill.getEffectsPassed();
        if (passedEffects == null) return 0.0;
        int coins = ((Number) passedEffects.getOrDefault("coins", 0)).intValue();
        int morale = ((Number) passedEffects.getOrDefault("partyMorale", 0)).intValue();
        int support = ((Number) passedEffects.getOrDefault("publicSupport", 0)).intValue();
        int corruption = ((Number) passedEffects.getOrDefault("corruptionScore", 0)).intValue();
        int media = ((Number) passedEffects.getOrDefault("mediaImage", 0)).intValue();

        if (isDangerCoins) {
            return coins * 50.0 + morale * 1.5 + support * 2.5 + media * 1.5 - corruption * 2.0;
        } else if (isDangerMorale) {
            return morale * 50.0 + coins * 0.1 + support * 2.5 + media * 1.5 - corruption * 2.0;
        } else {
            return support * 2.5 + morale * 1.5 + media * 1.5 - corruption * 2.0 + coins * 0.1;
        }
    }
}
