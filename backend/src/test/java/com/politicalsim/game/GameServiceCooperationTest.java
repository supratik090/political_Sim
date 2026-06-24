package com.politicalsim.game;

import static org.junit.jupiter.api.Assertions.*;

import com.politicalsim.ai.AiDecisionService;
import com.politicalsim.content.ScenarioDefinition;
import com.politicalsim.content.ScenarioDefinitionRepository;
import com.politicalsim.party.ControllerType;
import com.politicalsim.party.Ideology;
import com.politicalsim.party.PartyRole;
import com.politicalsim.party.PartyState;
import com.politicalsim.party.PartyStats;
import com.politicalsim.party.ProjectState;
import com.politicalsim.publicmood.PublicState;
import com.politicalsim.api.CampaignProgressResponse;
import com.politicalsim.api.ScenarioProgressView;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;

class GameServiceCooperationTest {

    private GameSession session;
    private MockGameSessionService sessionService;
    private GameService gameService;
    private AiDecisionService aiDecisionService;
    private RoundResolutionEngine roundEngine;
    private ScenarioDefinitionRepository scenarioRepository;

    private static class MockGameSessionService extends GameSessionService {
        private GameSession currentSession;
        private List<GameSession> sessionList = new ArrayList<>();

        public MockGameSessionService(GameSession session) {
            super(null, null, null, null, null);
            this.currentSession = session;
        }

        public void setSessionList(List<GameSession> list) {
            this.sessionList = list;
        }

        @Override
        public List<GameSession> listGames(String userId) {
            return sessionList;
        }

        @Override
        public GameSession getGame(String gameId) {
            return currentSession;
        }

        @Override
        public GameSession save(GameSession session) {
            this.currentSession = session;
            return session;
        }

        @Override
        public GameSession createGame(com.politicalsim.api.CreateGameRequest request, RewardDefinition firstReward) {
            GameSession s = new GameSession();
            s.setId("mock_created_game");
            s.setUserId(request.getUserId());
            s.setScenarioKey(request.getScenarioKey());
            s.setScenarioName(request.getScenarioKey());
            
            PartyStats stats = new PartyStats(200, 100, 20, 80, 40);
            PartyState player = new PartyState("party_player", request.getPlayerPartyName() != null ? request.getPlayerPartyName() : "Player Party", 
                request.getPlayerRole() != null ? request.getPlayerRole() : PartyRole.GOVERNMENT, 
                ControllerType.HUMAN, "Player 1", request.getIdeology() != null ? request.getIdeology() : Ideology.DEVELOPMENT_FIRST, stats);
            s.setParties(new ArrayList<>(List.of(player)));
            s.setPlayerPartyId("party_player");
            s.setPlayerPartyIds(List.of("party_player"));
            s.setStatus(GameStatus.ACTIVE);
            this.currentSession = s;
            return s;
        }
    }

    @BeforeEach
    void setUp() {
        session = new GameSession();
        session.setId("test_game");
        session.setTurnNumber(10);
        session.setCooperationOffers(new ArrayList<>());
        session.setActivePacts(new ArrayList<>());
        session.setGrudges(new HashMap<>());
        session.setLastRoundCommentary(new ArrayList<>());
        session.setLastResults(new ArrayList<>());

        PublicState publicState = new PublicState();
        publicState.setUndecidedSupport(10);
        session.setPublicState(publicState);

        // Party A (Sender, HUMAN): Coins=200, Morale=100, Corruption=20, Media=80, Support=40
        PartyStats statsA = new PartyStats(200, 100, 20, 80, 40);
        PartyState partyA = new PartyState("party_a", "Party A", PartyRole.GOVERNMENT, ControllerType.HUMAN, "Player 1", Ideology.DEVELOPMENT_FIRST, statsA);

        // Party B (Recipient, COMPUTER): Coins=200, Morale=100, Corruption=20, Media=80, Support=40
        PartyStats statsB = new PartyStats(200, 100, 20, 80, 40);
        PartyState partyB = new PartyState("party_b", "Party B", PartyRole.OPPOSITION, ControllerType.COMPUTER, "AI 1", Ideology.WELFARE_POPULIST, statsB);

        session.setParties(List.of(partyA, partyB));
        session.setGovernmentParty(partyA);
        session.setOppositionParty(partyB);
        session.setPlayerPartyIds(List.of("party_a"));
        session.setStatus(GameStatus.ACTIVE);
        session.setScenarioKey("test_scenario");
        session.setCurrentDate(java.time.LocalDate.now());

        com.politicalsim.content.DefinitionCache.newsCache.put("test_scenario", new ArrayList<>());
        com.politicalsim.content.DefinitionCache.cardsCache.put("test_scenario", new ArrayList<>());
        com.politicalsim.content.DefinitionCache.issuesCache.put("test_scenario", new ArrayList<>());

        roundEngine = new RoundResolutionEngine(null, null, null);
        sessionService = new MockGameSessionService(session);
        aiDecisionService = new AiDecisionService();
        scenarioRepository = Mockito.mock(ScenarioDefinitionRepository.class);
        gameService = new GameService(sessionService, roundEngine, null, null, null, scenarioRepository, aiDecisionService);
    }

    @Test
    void testCreateExchangeOfferAcceptedByAI() {
        CooperationOffer offer = new CooperationOffer();
        offer.setSenderPartyId("party_a");
        offer.setSenderPartyName("Party A");
        offer.setRecipientPartyId("party_b");
        offer.setRecipientPartyName("Party B");
        offer.setType(CooperationOffer.OfferType.EXCHANGE);
        
        // Offer: 110 Coins
        // Request: 5 Morale (utility value 100). Utility received = 110. Utility given = 100.
        // Recipient has 200 Morale, so subtracting 5 leaves 95 (>18 safety limit).
        // Recipient has 200 Coins, so adding 110 leaves them (>20 safety limit).
        // Evaluates to accepted.
        offer.setOfferedCoins(110);
        offer.setRequestedMorale(5);

        gameService.createCooperationOffer("test_game", offer);

        // Verify status and execution
        assertEquals(CooperationOffer.OfferStatus.ACCEPTED, offer.getStatus());
        
        // Party A (Sender): Coins: 200 - 110 = 90, Morale: 100 + 5 = 105
        assertEquals(90, session.getParties().get(0).getStats().getCoins());
        assertEquals(105, session.getParties().get(0).getStats().getPartyMorale());

        // Party B (Recipient): Coins: 200 + 110 = 310, Morale: 100 - 5 = 95
        assertEquals(310, session.getParties().get(1).getStats().getCoins());
        assertEquals(95, session.getParties().get(1).getStats().getPartyMorale());
    }

    @Test
    void testCreateExchangeOfferRejectedByAISafetyLimits() {
        CooperationOffer offer = new CooperationOffer();
        offer.setSenderPartyId("party_a");
        offer.setSenderPartyName("Party A");
        offer.setRecipientPartyId("party_b");
        offer.setRecipientPartyName("Party B");
        offer.setType(CooperationOffer.OfferType.EXCHANGE);
        
        // Request 90 Morale (recipient is left with 10 Morale, which is < 18 safety limit)
        // Offer 50 Coins (sender has enough)
        offer.setOfferedCoins(50);
        offer.setRequestedMorale(90);

        gameService.createCooperationOffer("test_game", offer);

        // Verify status: Rejected because of safety limits
        assertEquals(CooperationOffer.OfferStatus.REJECTED, offer.getStatus());
        
        // No stats should change
        assertEquals(200, session.getParties().get(0).getStats().getCoins());
        assertEquals(100, session.getParties().get(1).getStats().getPartyMorale());
    }

    @Test
    void testCreateNonAggressionPactWithPayment() {
        CooperationOffer offer = new CooperationOffer();
        offer.setSenderPartyId("party_a");
        offer.setSenderPartyName("Party A");
        offer.setRecipientPartyId("party_b");
        offer.setRecipientPartyName("Party B");
        offer.setType(CooperationOffer.OfferType.NON_AGGRESSION);
        offer.setDurationTurns(10);
        offer.setSenderPaysPact(true);
        offer.setPactPaymentResource("COINS");
        offer.setPactPaymentValue(50);

        gameService.createCooperationOffer("test_game", offer);

        // Verify status: Accepted (Sender pays, AI receives positive safety + coins)
        assertEquals(CooperationOffer.OfferStatus.ACCEPTED, offer.getStatus());

        // Verify payment execution
        assertEquals(150, session.getParties().get(0).getStats().getCoins());
        assertEquals(250, session.getParties().get(1).getStats().getCoins());

        // Verify pact exists in active pacts
        assertEquals(1, session.getActivePacts().size());
        NonAggressionPact pact = session.getActivePacts().get(0);
        assertEquals("party_a", pact.getPartyAId());
        assertEquals("party_b", pact.getPartyBId());
        assertEquals(10, pact.getTurnsRemaining());
    }

    @Test
    void testInsufficientAssetsThrowsException() {
        CooperationOffer offer = new CooperationOffer();
        offer.setSenderPartyId("party_a");
        offer.setSenderPartyName("Party A");
        offer.setRecipientPartyId("party_b");
        offer.setRecipientPartyName("Party B");
        offer.setType(CooperationOffer.OfferType.EXCHANGE);
        
        // Sender has 200 Coins, tries to offer 300
        offer.setOfferedCoins(300);

        assertThrows(IllegalArgumentException.class, () -> {
            gameService.createCooperationOffer("test_game", offer);
        });
    }

    @Test
    void testPactBetrayalDeductsMoraleAndClearsPact() throws Exception {
        PartyState partyA = session.getParties().get(0);
        PartyState partyB = session.getParties().get(1);

        // Create an active pact in session
        NonAggressionPact pact = new NonAggressionPact("pact_1", "party_a", "Party A", "party_b", "Party B", 10);
        session.getActivePacts().add(pact);

        List<String> commentary = new ArrayList<>();
        
        // Invoke checkAndProcessPactViolation via reflection
        java.lang.reflect.Method method = RoundResolutionEngine.class.getDeclaredMethod(
            "checkAndProcessPactViolation", 
            GameSession.class, 
            PartyState.class, 
            PartyState.class, 
            String.class, 
            List.class
        );
        method.setAccessible(true);
        method.invoke(roundEngine, session, partyA, partyB, "card 'Scandal Campaign'", commentary);

        // Morale check: Party A had 100, should be deducted by exactly 15 -> 85
        assertEquals(85, partyA.getStats().getPartyMorale());

        // Active pacts should now be empty (broken)
        assertTrue(session.getActivePacts().isEmpty());

        // Commentary should log the betrayal
        assertTrue(commentary.stream().anyMatch(c -> c.contains("broke their Non-Aggression Pact")));
        assertTrue(session.getLastResults().stream().anyMatch(r -> r.contains("Pact Violation: Party A attacked Party B")));
    }

    @Test
    void testRewardHostilePlayBetrayalDeductsMoraleAndClearsPact() {
        PartyState partyA = session.getParties().get(0);
        PartyState partyB = session.getParties().get(1);

        // Setup active pact
        NonAggressionPact pact = new NonAggressionPact("pact_1", "party_a", "Party A", "party_b", "Party B", 10);
        session.getActivePacts().add(pact);

        // Hostile reward
        RewardDefinition hostileReward = new RewardDefinition(
            "reward_sabotage_20_morale",
            "Morale Sabotage",
            "Deduct 20 morale from an opponent party.",
            true,
            "opponent",
            0,
            -20,
            0,
            0,
            0
        );

        List<String> commentary = new ArrayList<>();
        RoundResolutionEngine.REWARD_POOL.add(hostileReward);

        // Build submission
        RoundSubmission sub = new RoundSubmission();
        sub.setPartyId("party_a");
        sub.setSelectedRewardKey("reward_sabotage_20_morale");
        sub.setRewardTargetPartyId("party_b");
        session.setCurrentRoundSubmissions(List.of(sub));

        // Execute reward play resolution using roundEngine
        if (hostileReward.requiresTarget() && sub.getRewardTargetPartyId() != null) {
            PartyState rTarget = roundEngine.findParty(session, sub.getRewardTargetPartyId());
            if (rTarget != partyA && (hostileReward.coinsEffect() < 0 || hostileReward.moraleEffect() < 0 || hostileReward.corruptionEffect() > 0 || hostileReward.mediaEffect() < 0 || hostileReward.publicSupportEffect() < 0)) {
                roundEngine.checkAndProcessPactViolation(session, partyA, rTarget, "reward '" + hostileReward.name() + "'", commentary);
            }
            roundEngine.applyRewardEffect(session, rTarget, hostileReward, commentary);
        }

        // Verify morale: Party A suffers pact violation backlash (-15 morale -> 85)
        assertEquals(85, partyA.getStats().getPartyMorale());
        // Verify target: Party B suffers reward morale penalty (-20 morale -> 80)
        assertEquals(80, partyB.getStats().getPartyMorale());
        // Verify pact is broken
        assertTrue(session.getActivePacts().isEmpty());
        // Clean up REWARD_POOL
        RoundResolutionEngine.REWARD_POOL.remove(hostileReward);
    }

    @Test
    void testAiTargetingExcludesPactPartners() {
        PartyState partyA = session.getParties().get(0); // HUMAN
        PartyState partyB = session.getParties().get(1); // COMPUTER

        // Add third party C to ensure a target exists when B is in a pact with A
        PartyStats statsC = new PartyStats(200, 100, 20, 80, 50);
        PartyState partyC = new PartyState("party_c", "Party C", PartyRole.THIRD_PARTY, ControllerType.COMPUTER, "AI 2", Ideology.WELFARE_POPULIST, statsC);
        
        List<PartyState> parties = new ArrayList<>(session.getParties());
        parties.add(partyC);
        session.setParties(parties);

        // Scenario 1: No active pact. Party B targeting should select party C because support is higher (50 vs 40).
        PartyState targetWithoutPact = aiDecisionService.chooseOpponent(session, partyB, null);
        assertNotNull(targetWithoutPact);
        assertEquals("party_c", targetWithoutPact.getId());
        
        // Scenario 2: Active pact between B (AI) and C (leading opponent).
        NonAggressionPact pact = new NonAggressionPact("pact_1", "party_b", "Party B", "party_c", "Party C", 10);
        session.getActivePacts().add(pact);

        // B should exclude C and choose A instead
        PartyState targetWithPact = aiDecisionService.chooseOpponent(session, partyB, null);
        assertNotNull(targetWithPact);
        assertEquals("party_a", targetWithPact.getId());
    }

    @Test
    void testCycleRewardAllocationMatchesCurrentReward() {
        PartyState partyA = session.getParties().get(0);
        PartyState partyB = session.getParties().get(1);

        // Turn 5 triggers cycle-complete check (cycleTurn = 5)
        session.setTurnNumber(5);
        session.setCurrentRewardKey("reward_grant_50_coins");

        // Set round wins: Party A has 2 wins, Party B has 1 win
        session.getPartyRoundWins().put("party_a", 2);
        session.getPartyRoundWins().put("party_b", 1);

        // Add the reward definition to REWARD_POOL so getReward can find it
        RewardDefinition activeReward = new RewardDefinition(
            "reward_grant_50_coins",
            "Federal Funding Grant",
            "Gift 50 coins to a selected party.",
            true,
            "any",
            50,
            0,
            0,
            0,
            0
        );
        RoundResolutionEngine.REWARD_POOL.add(activeReward);

        List<String> commentary = new ArrayList<>();
        // Run bidding resolver (which handles cycle complete on turn 5)
        BiddingResolver biddingResolver = new BiddingResolver(roundEngine);
        biddingResolver.resolveBidding(session, "COINS", commentary);

        // Verify that the cycle winner is Party A
        List<HeldReward> heldRewards = session.getPartyHeldRewards().get("party_a");
        assertNotNull(heldRewards);
        assertEquals(1, heldRewards.size());
        
        // Verify that the allocated reward matches the current active reward "reward_grant_50_coins"
        HeldReward awarded = heldRewards.get(0);
        assertEquals("reward_grant_50_coins", awarded.getRewardKey());
        assertEquals("Federal Funding Grant", awarded.getName());

        // Verify that round wins were reset to 0
        assertEquals(0, session.getPartyRoundWins().get("party_a"));
        assertEquals(0, session.getPartyRoundWins().get("party_b"));

        // Clean up REWARD_POOL
        RoundResolutionEngine.REWARD_POOL.remove(activeReward);
    }

    @Test
    void testWestBengal2006UnlockedWhen2000Won() {
        ScenarioDefinition sd1 = new ScenarioDefinition();
        sd1.setScenarioKey("west_bengal_2000");
        sd1.setName("West Bengal 2000");
        sd1.setActive(true);

        ScenarioDefinition sd2 = new ScenarioDefinition();
        sd2.setScenarioKey("west_bengal_2006");
        sd2.setName("West Bengal 2006");
        sd2.setActive(true);

        Mockito.when(scenarioRepository.findAll()).thenReturn(List.of(sd1, sd2));

        // 1. With no won games, 2006 scenario should not be visible/present
        sessionService.setSessionList(new ArrayList<>());
        CampaignProgressResponse resp = gameService.getCampaignProgress("user123");
        boolean has2006 = resp.getScenarios().stream().anyMatch(s -> "west_bengal_2006".equals(s.getScenarioKey()));
        assertFalse(has2006);

        // 2. Once west_bengal_2000 is won, west_bengal_2006 should be AVAILABLE
        GameSession wonGame = new GameSession();
        wonGame.setScenarioKey("west_bengal_2000");
        wonGame.setStatus(GameStatus.VICTORY);
        sessionService.setSessionList(List.of(wonGame));

        CampaignProgressResponse resp2 = gameService.getCampaignProgress("user123");
        ScenarioProgressView view2006 = resp2.getScenarios().stream()
                .filter(s -> "west_bengal_2006".equals(s.getScenarioKey()))
                .findFirst().orElse(null);
        assertNotNull(view2006);
        assertEquals("AVAILABLE", view2006.getStatus());
    }

    @Test
    void testRetainInstitutionsFeature() {
        GameSession preceding = new GameSession();
        preceding.setScenarioKey("west_bengal_2000");
        preceding.setStatus(GameStatus.VICTORY);
        preceding.setPlayerPartyId("party_player");
        preceding.setPlayerPartyIds(List.of("party_player"));

        PartyState prevPlayerParty = new PartyState();
        prevPlayerParty.setId("party_player");

        // Complete PARTY_HQ and CADRE_OFFICE
        ProjectState p1 = new ProjectState("PARTY_HQ");
        p1.setProgressPercent(100);
        ProjectState p2 = new ProjectState("CADRE_OFFICE");
        p2.setProgressPercent(100);
        ProjectState p3 = new ProjectState("IT_CELL");
        p3.setProgressPercent(50); // not completed

        prevPlayerParty.setProjects(List.of(p1, p2, p3));
        preceding.setParties(List.of(prevPlayerParty));

        sessionService.setSessionList(List.of(preceding));

        com.politicalsim.api.CreateGameRequest request = new com.politicalsim.api.CreateGameRequest();
        request.setScenarioKey("west_bengal_2006");
        request.setUserId("user123");
        request.setRetainInstitutions(true);
        request.setPlayerPartyName("My Party");
        request.setPlayerRole(PartyRole.GOVERNMENT);

        GameSession newSession = gameService.createGame(request);

        PartyState newPlayerParty = newSession.getParties().stream()
                .filter(p -> p.getId().equals(newSession.getPlayerPartyId()))
                .findFirst().orElse(null);

        assertNotNull(newPlayerParty);

        // Verify that PARTY_HQ and CADRE_OFFICE are carried over at 100% progress
        ProjectState newHq = newPlayerParty.getProjects().stream()
                .filter(p -> "PARTY_HQ".equals(p.getProjectKey()))
                .findFirst().orElse(null);
        assertNotNull(newHq);
        assertEquals(100, newHq.getProgressPercent());

        ProjectState newCadre = newPlayerParty.getProjects().stream()
                .filter(p -> "CADRE_OFFICE".equals(p.getProjectKey()))
                .findFirst().orElse(null);
        assertNotNull(newCadre);
        assertEquals(100, newCadre.getProgressPercent());

        // IT_CELL was not completed, so it should be at 0 in the new session
        ProjectState newIt = newPlayerParty.getProjects().stream()
                .filter(p -> "IT_CELL".equals(p.getProjectKey()))
                .findFirst().orElse(null);
        assertNotNull(newIt);
        assertEquals(0, newIt.getProgressPercent());
    }

    @Test
    void testProjectYieldCommentarySummary() {
        // Party A (from setUp) gets a completed PARTY_HQ
        PartyState partyA = session.getParties().get(0);
        ProjectState hq = partyA.getProjects().stream()
                .filter(p -> "PARTY_HQ".equals(p.getProjectKey()))
                .findFirst().orElse(null);
        assertNotNull(hq);
        hq.setProgressPercent(100);
        hq.setJustCompleted(false);

        // Set initial stats
        partyA.getStats().setCoins(100);
        partyA.getStats().setMediaImage(50);
        partyA.getStats().setPublicSupport(30);

        List<String> commentary = new ArrayList<>();
        ProjectResolver projectResolver = new ProjectResolver(roundEngine);
        projectResolver.resolveBuildingProjects(session, new HashMap<>(), commentary);

        // Verify stats updated (PARTY_HQ yields: benefitCoins: 12, benefitMedia: 3, benefitSupport: 1)
        assertEquals(112, partyA.getStats().getCoins());
        assertEquals(53, partyA.getStats().getMediaImage());
        assertEquals(31, partyA.getStats().getPublicSupport());

        // Verify commentary has yields summary block
        boolean hasYieldHeader = commentary.stream().anyMatch(c -> c.contains("Passive yields from completed projects this turn:"));
        assertTrue(hasYieldHeader);

        boolean hasPartyYield = commentary.stream().anyMatch(c -> c.contains("Party A: +12 Coins, +3 Media Image, +1% Support"));
        assertTrue(hasPartyYield);
    }

    @Test
    void testScenarioNameFormattingFallback() {
        GameSession s = new GameSession();
        s.setScenarioKey("west_bengal_2000");
        assertEquals("West Bengal 2000", s.getScenarioName());

        s.setScenarioName("Custom Bengal Name");
        assertEquals("Custom Bengal Name", s.getScenarioName());
    }
}
