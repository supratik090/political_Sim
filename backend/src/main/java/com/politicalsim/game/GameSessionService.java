package com.politicalsim.game;

import com.politicalsim.api.CreateGameRequest;
import com.politicalsim.api.CreatePartySetupRequest;
import com.politicalsim.api.GameSessionSummary;
import com.politicalsim.content.ScenarioDefinition;
import com.politicalsim.content.ScenarioDefinitionRepository;
import com.politicalsim.content.CardDefinition;
import com.politicalsim.content.CardDefinitionRepository;
import com.politicalsim.content.LegislativeBillDefinition;
import com.politicalsim.content.LegislativeBillDefinitionRepository;
import com.politicalsim.party.ControllerType;
import com.politicalsim.party.Ideology;
import com.politicalsim.party.PartyRole;
import com.politicalsim.party.PartyState;
import com.politicalsim.party.PartyStats;
import com.politicalsim.ai.AiProfile;
import com.politicalsim.publicmood.PublicState;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.*;

@Service
public class GameSessionService {
    private static final org.slf4j.Logger log = org.slf4j.LoggerFactory.getLogger(GameSessionService.class);

    private static List<CardDefinition> cachedCards = null;
    private static final Map<String, GameSessionContent> contentCache = new java.util.concurrent.ConcurrentHashMap<>();

    private List<CardDefinition> getCachedCards() {
        if (cachedCards == null) {
            cachedCards = cardRepository.findAll().stream()
                    .filter(CardDefinition::isActive)
                    .toList();
        }
        return cachedCards;
    }

    public static void clearCaches() {
        cachedCards = null;
        contentCache.clear();
        log.info("[METRIC] Static definition caches cleared.");
    }

    @org.springframework.context.event.EventListener(org.springframework.boot.context.event.ApplicationReadyEvent.class)
    public void preloadCaches() {
        log.info("[CACHE] Preloading static caches on startup...");
        long start = System.currentTimeMillis();
        
        // 1. Preload cards
        try {
            getCachedCards();
            log.info("[CACHE] Cards preloaded successfully. Count: {}", cachedCards != null ? cachedCards.size() : 0);
        } catch (Exception e) {
            log.error("[CACHE] Failed to preload cards", e);
        }

        // 2. Preload bills
        try {
            List<String> scenarioKeys = scenarioRepository.findAll().stream()
                    .map(ScenarioDefinition::getScenarioKey)
                    .filter(java.util.Objects::nonNull)
                    .toList();

            for (String key : scenarioKeys) {
                long t = System.currentTimeMillis();
                com.politicalsim.content.DefinitionCache.getBillsForScenario(billRepository, key);
                log.info("[CACHE] Bills for '{}' preloaded in {} ms", key, (System.currentTimeMillis() - t));
            }
            com.politicalsim.content.DefinitionCache.getBillsForScenario(billRepository, "default");
        } catch (Exception e) {
            log.error("[CACHE] Failed to preload bills", e);
        }
        
        log.info("[CACHE] Total preloading finished in {} ms", (System.currentTimeMillis() - start));
    }

    private final GameSessionRepository repository;
    private final ScenarioDefinitionRepository scenarioRepository;
    private final CardDefinitionRepository cardRepository;
    private final GameSessionContentRepository contentRepository;
    private final LegislativeBillDefinitionRepository billRepository;
    private final com.politicalsim.content.FactionDefinitionRepository factionRepository;
    private final String defaultStateName;

    public GameSessionService(
            GameSessionRepository repository,
            ScenarioDefinitionRepository scenarioRepository,
            CardDefinitionRepository cardRepository,
            GameSessionContentRepository contentRepository,
            LegislativeBillDefinitionRepository billRepository,
            com.politicalsim.content.FactionDefinitionRepository factionRepository,
            @Value("${political-sim.default-state-name}") String defaultStateName
    ) {
        this.repository = repository;
        this.scenarioRepository = scenarioRepository;
        this.cardRepository = cardRepository;
        this.contentRepository = contentRepository;
        this.billRepository = billRepository;
        this.factionRepository = factionRepository;
        this.defaultStateName = defaultStateName;
    }

    private void populateSessionContent(GameSession session) {
        if (session != null) {
            GameSessionContent content = contentCache.computeIfAbsent(session.getId(), id -> 
                contentRepository.findById(id).orElse(null)
            );
            if (content != null) {
                session.setGameCards(content.getGameCards());
                session.setGameIssues(new ArrayList<>());
            }
        }
    }

    private void initializeLegislativeBills(GameSession session) {
        List<LegislativeBillDefinition> allBills = com.politicalsim.content.DefinitionCache.getBillsForScenario(billRepository, session.getScenarioKey());
        allBills = allBills.stream().filter(LegislativeBillDefinition::isActive).toList();

        List<LegislativeBillDefinition> govtPool = allBills.stream()
                .filter(b -> "GOVERNMENT".equalsIgnoreCase(b.getProposingRole()))
                .collect(java.util.stream.Collectors.toList());
        List<LegislativeBillDefinition> oppPool = allBills.stream()
                .filter(b -> "OPPOSITION".equalsIgnoreCase(b.getProposingRole()))
                .collect(java.util.stream.Collectors.toList());

        java.util.Collections.shuffle(govtPool);
        java.util.Collections.shuffle(oppPool);

        List<LegislativeBillDefinition> chosenGovt = govtPool.subList(0, Math.min(10, govtPool.size()));
        List<LegislativeBillDefinition> chosenOpp = oppPool.subList(0, Math.min(10, oppPool.size()));

        List<LegislativeBillState> states = new java.util.ArrayList<>();
        for (LegislativeBillDefinition b : chosenGovt) {
            states.add(new LegislativeBillState(b.getBillKey()));
        }
        for (LegislativeBillDefinition b : chosenOpp) {
            states.add(new LegislativeBillState(b.getBillKey()));
        }
        session.setBills(states);
    }

    public GameSession createGame(CreateGameRequest request, RewardDefinition firstReward) {
        String key = request.getScenarioKey() == null ? "west_bengal_2000" : request.getScenarioKey();
        String userId = request.getUserId();
        if (userId == null || userId.isBlank() || "null".equalsIgnoreCase(userId) || "undefined".equalsIgnoreCase(userId)) {
            userId = null;
        } else {
            userId = userId.trim().toLowerCase();
        }
        List<GameSession> active;
        if (userId != null) {
            active = repository.findByScenarioKeyAndStatusAndUserId(key, GameStatus.ACTIVE, userId);
        } else {
            active = repository.findByScenarioKeyAndStatus(key, GameStatus.ACTIVE);
        }
        if (!active.isEmpty()) {
            throw new IllegalArgumentException("An active game already exists for scenario: " + key + ". Please end or forfeit that game first.");
        }

        ScenarioDefinition scenario = request.getScenarioKey() == null ? null
                : scenarioRepository.findByScenarioKey(request.getScenarioKey()).stream().findFirst().orElse(null);
        List<PartyState> parties = buildParties(request);
        PartyState governmentParty = findPartyByRole(parties, PartyRole.GOVERNMENT);
        PartyState oppositionParty = findPartyByRole(parties, PartyRole.OPPOSITION);
        List<String> playerPartyIds = parties.stream()
                .filter(party -> party.getControllerType() == ControllerType.HUMAN)
                .map(PartyState::getId)
                .toList();

        GameSession session = new GameSession();
        session.setUserId(userId);
        String finalKey = blankToDefault(request.getScenarioKey(), "west_bengal_2001");
        session.setScenarioKey(finalKey);
        session.setScenarioName(scenario != null ? scenario.getName() : finalKey);
        session.setStateName(blankToDefault(request.getStateName(), scenario == null ? defaultStateName : scenario.getStateName()));
        session.setTurnNumber(1);
        session.setMonthInCycle(1);
        session.setTripleImpactTurn(new java.util.Random().nextInt(5) + 1);
        initializeSecretMetricSequence(session);
        LocalDate scenarioStartDate = scenario == null ? LocalDate.of(2021, 1, 1) : scenario.getStartDate();
        session.setCurrentDate(request.getStartDate() == null ? scenarioStartDate : request.getStartDate());
        session.setPlayerPartyId(playerPartyIds.get(0));
        session.setPlayerPartyIds(playerPartyIds);
        session.setActiveHumanPlayerIndex(0);
        
        session.setMultiplayer(request.isMultiplayer());
        if (request.isMultiplayer()) {
            session.setJoinCode(UUID.randomUUID().toString().substring(0, 6).toUpperCase());
            session.setTurnDurationSeconds(request.getTurnDurationSeconds() != null ? request.getTurnDurationSeconds() : 180);
            session.setStatus(GameStatus.LOBBY);
            if (userId != null) {
                session.getHumanPlayerMap().put(playerPartyIds.get(0), userId);
            }
        } else {
            session.setStatus(GameStatus.ACTIVE);
        }
        session.setParties(parties);
        List<com.politicalsim.content.FactionDefinition> factionDefs = com.politicalsim.content.DefinitionCache.getFactionsForScenario(factionRepository, finalKey);
        if (factionDefs == null || factionDefs.isEmpty()) {
            factionDefs = new ArrayList<>();
            com.politicalsim.content.FactionDefinition fd1 = new com.politicalsim.content.FactionDefinition();
            fd1.setFactionKey("loyalist");
            fd1.setName("Loyalists");
            fd1.setStartingLoyalty(75);
            fd1.setStartingInfluence(45);
            factionDefs.add(fd1);

            com.politicalsim.content.FactionDefinition fd2 = new com.politicalsim.content.FactionDefinition();
            fd2.setFactionKey("youth");
            fd2.setName("Youth Wing");
            fd2.setStartingLoyalty(75);
            fd2.setStartingInfluence(35);
            factionDefs.add(fd2);

            com.politicalsim.content.FactionDefinition fd3 = new com.politicalsim.content.FactionDefinition();
            fd3.setFactionKey("trade");
            fd3.setName("Trade Unions");
            fd3.setStartingLoyalty(75);
            fd3.setStartingInfluence(20);
            factionDefs.add(fd3);
        }
        for (PartyState p : parties) {
            p.setAssemblySeatShare(p.getStats().getPublicSupport());
            List<com.politicalsim.party.FactionState> fStates = new ArrayList<>();
            for (com.politicalsim.content.FactionDefinition fd : factionDefs) {
                fStates.add(new com.politicalsim.party.FactionState(
                    fd.getFactionKey(),
                    fd.getName(),
                    fd.getStartingLoyalty(),
                    fd.getStartingInfluence()
                ));
            }
            p.setFactions(fStates);
        }
        session.setGovernmentParty(governmentParty);
        session.setOppositionParty(oppositionParty);
        session.setCardUsageByParty(initialCardUsage(parties));
        session.setPublicState(scenario != null && scenario.getPublicState() != null ? scenario.getPublicState() : new PublicState(
                25,
                "Watchful",
                List.of("Jobs", "Price Rise", "Governance"),
                "A new political cycle has started. Voters are waiting for early signals."
        ));
        session.setLastResults(List.of("New government formed by " + governmentParty.getName() + "."));
        session.setPendingResults(List.of());

        Map<String, PartyStats> startStats = new java.util.LinkedHashMap<>();
        for (PartyState party : parties) {
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
        
        // Initialize Reward States
        session.setUsedRewardKeys(new ArrayList<>());
        session.setCurrentRewardKey(firstReward.key());
        session.setCurrentRewardName(firstReward.name());
        session.setCurrentRewardDescription(firstReward.description());

        Map<String, Integer> wins = new LinkedHashMap<>();
        Map<String, List<HeldReward>> held = new LinkedHashMap<>();
        for (PartyState party : parties) {
            wins.put(party.getId(), 0);
            held.put(party.getId(), new ArrayList<>());
        }
        session.setPartyRoundWins(wins);
        session.setPartyHeldRewards(held);

        // Initialize Game Cards and Issues (up to 60 chosen randomly across all scenarios)
        long t1 = System.currentTimeMillis();
        List<CardDefinition> allCards = getCachedCards();
        log.info("[METRIC] getCachedCards() took {} ms (count={})", (System.currentTimeMillis() - t1), allCards.size());
        
        List<CardDefinition> selectedCards = new ArrayList<>(allCards);
        if (selectedCards.size() > 60) {
            java.util.Collections.shuffle(selectedCards);
            selectedCards = selectedCards.subList(0, 60);
        }
        session.setGameCards(selectedCards);

        session.setGameIssues(new ArrayList<>());

        initializeLegislativeBills(session);

        normalizePublicSupport(session);

        GameSession saved = repository.save(session);
        GameSessionContent content = new GameSessionContent(saved.getId(), selectedCards, new ArrayList<>());
        contentRepository.save(content);
        contentCache.put(saved.getId(), content);

        saved.setGameCards(selectedCards);
        saved.setGameIssues(new ArrayList<>());
        return saved;
    }

    public GameSession getGame(String gameId) {
        GameSession session = repository.findById(gameId).orElseThrow(() -> new GameNotFoundException(gameId));
        populateSessionContent(session);
        syncRoleReferences(session);
        return session;
    }

    public List<GameSession> listGames() {
        return repository.findAllByOrderByCurrentDateDesc();
    }

    public List<GameSessionRepository.GameSessionDTO> listGamesDto(String userId) {
        if (userId != null && !userId.isBlank() && !"null".equalsIgnoreCase(userId) && !"undefined".equalsIgnoreCase(userId)) {
            return repository.findAllByUserIdOrderByCurrentDateDesc(userId.trim().toLowerCase(), GameSessionRepository.GameSessionDTO.class);
        }
        return Collections.emptyList();
    }

    public List<GameSessionRepository.ProgressGameDTO> listProgressGames(String userId) {
        if (userId != null && !userId.isBlank() && !"null".equalsIgnoreCase(userId) && !"undefined".equalsIgnoreCase(userId)) {
            return repository.findProgressGamesByUserId(userId.trim().toLowerCase());
        }
        return Collections.emptyList();
    }
    public List<GameSession> listGames(String userId) {
        if (userId != null && !userId.isBlank() && !"null".equalsIgnoreCase(userId) && !"undefined".equalsIgnoreCase(userId)) {
            return repository.findAllByUserIdOrderByCurrentDateDesc(userId.trim().toLowerCase(), GameSession.class);
        }
        return Collections.emptyList();
    }


    public List<GameSessionSummary> listGameSummaries() {
        return repository.findAllSummaries().stream()
                .map(GameSessionSummary::from)
                .toList();
    }

    public List<GameSessionSummary> listGameSummaries(String userId) {
        if (userId != null && !userId.isBlank() && !"null".equalsIgnoreCase(userId) && !"undefined".equalsIgnoreCase(userId)) {
            return repository.findSummariesByUserId(userId.trim().toLowerCase()).stream()
                    .map(GameSessionSummary::from)
                    .toList();
        }
        return repository.findAllSummaries().stream()
                .map(GameSessionSummary::from)
                .toList();
    }

    public GameSession save(GameSession session) {
        return repository.save(session);
    }

    public void deleteGame(String gameId) {
        if (!repository.existsById(gameId)) {
            throw new GameNotFoundException(gameId);
        }
        repository.deleteById(gameId);
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

    public GameSession getGameByJoinCode(String joinCode) {
        GameSession session = repository.findByJoinCode(joinCode.toUpperCase()).stream()
                .filter(s -> s.getStatus() == GameStatus.LOBBY || s.getStatus() == GameStatus.ACTIVE)
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Invalid join code or game is not active/lobby"));
        populateSessionContent(session);
        return session;
    }

    public GameSession joinGame(String userId, String joinCode, String partyId) {
        if (userId == null || userId.isBlank()) {
            throw new IllegalArgumentException("User ID is required to join a game");
        }
        String cleanUserId = userId.trim().toLowerCase();
        
        GameSession session = repository.findByJoinCode(joinCode.toUpperCase()).stream()
                .filter(s -> s.getStatus() == GameStatus.LOBBY || s.getStatus() == GameStatus.ACTIVE)
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Invalid join code or game is not active/lobby"));
        populateSessionContent(session);
        
        if (session.getHumanPlayerMap().containsValue(cleanUserId)) {
            return session;
        }
        
        PartyState party = session.getParties().stream()
                .filter(p -> p.getId().equals(partyId))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Invalid party ID"));
                
        if (session.getHumanPlayerMap().containsKey(partyId)) {
            throw new IllegalArgumentException("Party already claimed by another player");
        }
        
        session.getHumanPlayerMap().put(partyId, cleanUserId);
        party.setControllerType(ControllerType.HUMAN);
        
        if (!session.getPlayerPartyIds().contains(partyId)) {
            session.getPlayerPartyIds().add(partyId);
        }
        
        return repository.save(session);
    }
    
    public GameSession startGame(String gameId, String userId) {
        GameSession session = getGame(gameId);
        if (session.getStatus() != GameStatus.LOBBY) {
            throw new IllegalArgumentException("Game is not in lobby");
        }
        
        if (userId != null && !userId.equals(session.getUserId())) {
            throw new IllegalArgumentException("Only the creator can start the game");
        }
        
        session.setStatus(GameStatus.ACTIVE);
        session.setTurnStartTime(java.time.LocalDateTime.now());
        return repository.save(session);
    }

    private List<PartyState> buildParties(CreateGameRequest request) {
        if (request.getPartySetups() == null || request.getPartySetups().isEmpty()) {
            return buildLegacyParties(request);
        }

        if (request.getPartySetups().size() != 3) {
            throw new IllegalArgumentException("Game must have exactly 3 parties.");
        }

        long humanCount = request.getPartySetups().stream()
                .filter(setup -> setup.getControllerType() == ControllerType.HUMAN)
                .count();
        long computerCount = request.getPartySetups().stream()
                .filter(setup -> setup.getControllerType() == ControllerType.COMPUTER)
                .count();
        if (!((humanCount == 1 && computerCount == 2) || (humanCount == 2 && computerCount == 1))) {
            throw new IllegalArgumentException("Game must be either 1 human + 2 computer or 2 human + 1 computer.");
        }

        if (request.getPartySetups().stream().filter(setup -> setup.getRole() == PartyRole.GOVERNMENT).count() != 1) {
            throw new IllegalArgumentException("Exactly one party must start as GOVERNMENT.");
        }
        if (request.getPartySetups().stream().filter(setup -> setup.getRole() == PartyRole.OPPOSITION).count() != 1) {
            throw new IllegalArgumentException("Exactly one party must start as OPPOSITION.");
        }
        if (request.getPartySetups().stream().filter(setup -> setup.getRole() == PartyRole.THIRD_PARTY).count() != 1) {
            throw new IllegalArgumentException("Exactly one party must start as THIRD_PARTY.");
        }

        List<PartyState> parties = new ArrayList<>();
        for (CreatePartySetupRequest setup : request.getPartySetups()) {
            parties.add(newParty(
                    "party-" + UUID.randomUUID(),
                    setup.getPartyName(),
                    setup.getRole(),
                    setup.getControllerType(),
                    setup.getHumanPlayerLabel(),
                    setup.getColor(),
                    setup.getSymbol(),
                    setup.getIdeology(),
                    setup.getAiProfile() == null ? AiProfile.defaultForRole(setup.getRole()) : setup.getAiProfile(),
                    setup.getStartingStats() == null ? defaultStatsForRole(setup.getRole()) : setup.getStartingStats()
            ));
        }
        return parties;
    }

    private List<PartyState> buildLegacyParties(CreateGameRequest request) {
        PartyRole playerRole = request.getPlayerRole();
        String playerPartyId = "party-" + UUID.randomUUID();
        String rivalPartyId = "party-" + UUID.randomUUID();
        String thirdPartyId = "party-" + UUID.randomUUID();

        PartyState governmentParty;
        PartyState oppositionParty;
        if (playerRole == PartyRole.GOVERNMENT) {
            governmentParty = newParty(playerPartyId, request.getPlayerPartyName(), PartyRole.GOVERNMENT,
                    ControllerType.HUMAN, "Player 1", "#d23f31", "Tiger", request.getIdeology(),
                    AiProfile.defaultForRole(PartyRole.GOVERNMENT), new PartyStats(260, 72, 24, 62, 43));
            oppositionParty = newParty(rivalPartyId, "Tiger Front", PartyRole.OPPOSITION,
                    ControllerType.COMPUTER, null, "#244f9e", "Elephant", Ideology.ANTI_CORRUPTION,
                    AiProfile.defaultForRole(PartyRole.OPPOSITION), new PartyStats(150, 58, 18, 48, 32));
        } else {
            governmentParty = newParty(rivalPartyId, "Tiger Front", PartyRole.GOVERNMENT,
                    ControllerType.COMPUTER, null, "#d23f31", "Tiger", Ideology.DEVELOPMENT_FIRST,
                    AiProfile.defaultForRole(PartyRole.GOVERNMENT), new PartyStats(260, 72, 24, 62, 43));
            oppositionParty = newParty(playerPartyId, request.getPlayerPartyName(), PartyRole.OPPOSITION,
                    ControllerType.HUMAN, "Player 1", "#244f9e", "Elephant", request.getIdeology(),
                    AiProfile.defaultForRole(PartyRole.OPPOSITION), new PartyStats(150, 58, 18, 48, 32));
        }

        PartyState thirdParty = newParty(thirdPartyId, "Peacock Party", PartyRole.THIRD_PARTY,
                ControllerType.COMPUTER, null, "#1f8f5f", "Peacock", Ideology.REGIONAL_PRIDE,
                AiProfile.defaultForRole(PartyRole.THIRD_PARTY), new PartyStats(120, 52, 16, 42, 15));
        return List.of(governmentParty, oppositionParty, thirdParty);
    }

    private PartyState findPartyByRole(List<PartyState> parties, PartyRole role) {
        return parties.stream()
                .filter(party -> party.getRole() == role)
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Missing party with role " + role));
    }

    private void syncRoleReferences(GameSession session) {
        session.getParties().stream()
                .filter(party -> party.getRole() == PartyRole.GOVERNMENT)
                .findFirst()
                .ifPresent(session::setGovernmentParty);
        session.getParties().stream()
                .filter(party -> party.getRole() == PartyRole.OPPOSITION)
                .findFirst()
                .ifPresent(session::setOppositionParty);
    }

    private PartyStats defaultStatsForRole(PartyRole role) {
        return switch (role) {
            case GOVERNMENT -> new PartyStats(260, 72, 24, 62, 43);
            case OPPOSITION -> new PartyStats(150, 58, 18, 48, 32);
            case THIRD_PARTY, DEFEATED -> new PartyStats(120, 52, 16, 42, 15);
        };
    }

    private PartyState newParty(String id, String name, PartyRole role, ControllerType controllerType,
                                String humanPlayerLabel, String color, String symbol, Ideology ideology, AiProfile aiProfile, PartyStats stats) {
        return new PartyState(id, name, role, controllerType, humanPlayerLabel, color, symbol, ideology, aiProfile, stats);
    }

    private Map<String, Map<String, Integer>> initialCardUsage(List<PartyState> parties) {
        Map<String, Map<String, Integer>> usage = new LinkedHashMap<>();
        for (PartyState party : parties) {
            usage.put(party.getId(), new LinkedHashMap<>());
        }
        return usage;
    }

    private String blankToDefault(String value, String defaultValue) {
        return value == null || value.isBlank() ? defaultValue : value;
    }

    private void initializeSecretMetricSequence(GameSession session) {
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
