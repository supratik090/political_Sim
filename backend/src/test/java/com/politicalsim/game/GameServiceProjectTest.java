package com.politicalsim.game;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

import com.politicalsim.party.ControllerType;
import com.politicalsim.party.Ideology;
import com.politicalsim.party.PartyRole;
import com.politicalsim.party.PartyState;
import com.politicalsim.party.PartyStats;
import com.politicalsim.party.ProjectState;
import com.politicalsim.publicmood.PublicState;
import java.util.ArrayList;
import java.util.List;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class GameServiceProjectTest {

    private GameSession session;
    private MockGameSessionService sessionService;
    private GameService gameService;

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

        PublicState publicState = new PublicState();
        publicState.setUndecidedSupport(10);
        session.setPublicState(publicState);

        // Stats: Coins=200, Morale=100, Corruption=20, Media=80, Support=50
        PartyStats stats = new PartyStats(200, 100, 20, 80, 50);
        PartyState party = new PartyState("tmc", "TMC", PartyRole.GOVERNMENT, ControllerType.HUMAN, "Player 1", Ideology.DEVELOPMENT_FIRST, stats);
        
        // Add a Mega Rally project with 0% progress
        ProjectState megaRally = new ProjectState("MEGA_RALLY");
        megaRally.setProgressPercent(0);
        
        List<ProjectState> projects = new ArrayList<>();
        projects.add(megaRally);
        party.setProjects(projects);

        session.setParties(List.of(party));
        session.setGovernmentParty(party);
        session.setOppositionParty(party);
        session.setPlayerPartyIds(List.of("tmc"));
        session.setScenarioKey("test_scenario");
        session.setCurrentDate(java.time.LocalDate.now());

        com.politicalsim.content.DefinitionCache.newsCache.put("test_scenario", new ArrayList<>());
        com.politicalsim.content.DefinitionCache.cardsCache.put("test_scenario", new ArrayList<>());
        com.politicalsim.content.DefinitionCache.issuesCache.put("test_scenario", new ArrayList<>());

        RoundResolutionEngine roundEngine = new RoundResolutionEngine(null, null, null);
        sessionService = new MockGameSessionService(session);
        gameService = new GameService(sessionService, roundEngine, null, null, null, null, null);
    }

    @Test
    void testFundProjectMultiResourceDeductionAndNewInstanceOnCompletion() {
        ProjectState megaRally = session.getParties().get(0).getProjects().get(0);

        // Fund 50% of Mega Rally
        // Mega Rally cost: 60 Coins, 10 Media Image, 5% Support.
        // 50% cost: 30 Coins, 5 Media Image, 3% Support (Math.ceil(2.5)).
        gameService.fundProject("test_game", "tmc", megaRally.getId(), 50);

        PartyState party = session.getParties().get(0);
        assertEquals(50, megaRally.getProgressPercent());
        assertEquals(170, party.getStats().getCoins()); // 200 - 30
        assertEquals(75, party.getStats().getMediaImage()); // 80 - 5
        assertEquals(47, party.getStats().getPublicSupport()); // 50 - 3
        assertEquals(13, session.getPublicState().getUndecidedSupport()); // 10 + 3 (support transferred to undecided)

        // Fund the remaining 50% to complete it
        gameService.fundProject("test_game", "tmc", megaRally.getId(), 50);

        assertEquals(100, megaRally.getProgressPercent());
        assertEquals(140, party.getStats().getCoins()); // 170 - 30
        assertEquals(70, party.getStats().getMediaImage()); // 75 - 5
        assertEquals(44, party.getStats().getPublicSupport()); // 47 - 3
        assertEquals(16, session.getPublicState().getUndecidedSupport()); // 13 + 3

        // A new incomplete project instance of MEGA_RALLY should be automatically added
        assertEquals(2, party.getProjects().size());
        
        ProjectState secondInstance = party.getProjects().get(1);
        assertEquals("MEGA_RALLY", secondInstance.getProjectKey());
        assertEquals(0, secondInstance.getProgressPercent());
        assertTrue(secondInstance.getId() != null && !secondInstance.getId().equals(megaRally.getId()));
    }
}
