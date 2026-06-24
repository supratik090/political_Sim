package com.politicalsim.game;

import static org.junit.jupiter.api.Assertions.*;

import com.politicalsim.ai.AiDecisionService;
import com.politicalsim.party.ControllerType;
import com.politicalsim.party.Ideology;
import com.politicalsim.party.PartyRole;
import com.politicalsim.party.PartyState;
import com.politicalsim.party.PartyStats;
import com.politicalsim.publicmood.PublicState;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class GameServiceCooperationTest {

    private GameSession session;
    private MockGameSessionService sessionService;
    private GameService gameService;
    private AiDecisionService aiDecisionService;
    private RoundResolutionEngine roundEngine;

    private static class MockGameSessionService extends GameSessionService {
        private GameSession currentSession;

        public MockGameSessionService(GameSession session) {
            super(null, null, null, null, null);
            this.currentSession = session;
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
        gameService = new GameService(sessionService, roundEngine, null, null, null, null, aiDecisionService);
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
}
