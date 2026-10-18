package com.politicalsim.national;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class NationalStateOperationsTest {

    private NationalGame game;
    private NationalGameService gameService;

    @BeforeEach
    public void setup() {
        gameService = new NationalGameService();
        game = new NationalGame();
        game.setId("test-game-1");
        game.setUserId("user-1");
        game.setPartyKey("ydp");
        game.setPartyName("Youth Development Party");
        game.setPlayerFunds(15.0);
        game.setCurrentSeason(1);

        NationalPartyState playerState = new NationalPartyState();
        playerState.setPartyKey("ydp");
        playerState.setPartyName("Youth Development Party");
        playerState.setFunds(15.0);
        playerState.setWorkers(250000);
        playerState.setVolunteers(120000);
        playerState.setMorale(75);
        playerState.setPlayerParty(true);

        game.getPartyStates().add(playerState);
    }

    @Test
    public void testInitializeStateOperations() {
        gameService.initializeStateOperations(game);

        assertNotNull(game.getStateOperations());
        assertEquals(7, game.getStateOperations().size());

        // Check UP
        NationalStateOperationState up = game.getStateOperations().get("UP");
        assertNotNull(up);
        assertEquals("Uttar Pradesh", up.getStateName());
        assertEquals(80, up.getTotalLokSabhaSeats());
        assertEquals(403, up.getTotalAssemblySeats());
        assertEquals(15, up.getElectionTurn());
        assertEquals("March 2002", up.getElectionMonth());
        assertEquals("NORMAL", up.getElectionPhase());
        assertTrue(up.getVoteSplits().containsKey("BJP"));
        assertTrue(up.getVoteSplits().containsKey("SP"));
        assertTrue(up.getVoteSplits().containsKey("YDP"));
        assertTrue(up.getVoteSplits().containsKey("UNDECIDED"));

        // Check Bihar
        NationalStateOperationState bihar = game.getStateOperations().get("BIHAR");
        assertNotNull(bihar);
        assertEquals("Bihar", bihar.getStateName());
        assertEquals(40, bihar.getTotalLokSabhaSeats());
        assertEquals(243, bihar.getTotalAssemblySeats());
        assertEquals(50, bihar.getElectionTurn());
        assertEquals("February 2005", bihar.getElectionMonth());

        // Check Maharashtra
        NationalStateOperationState mh = game.getStateOperations().get("MAHARASHTRA");
        assertNotNull(mh);
        assertEquals("Maharashtra", mh.getStateName());
        assertEquals(48, mh.getTotalLokSabhaSeats());
        assertEquals(288, mh.getTotalAssemblySeats());
        assertEquals(46, mh.getElectionTurn());
        assertEquals("October 2004", mh.getElectionMonth());

        // Check West Bengal
        NationalStateOperationState wb = game.getStateOperations().get("WEST_BENGAL");
        assertNotNull(wb);
        assertEquals("West Bengal", wb.getStateName());
        assertEquals(42, wb.getTotalLokSabhaSeats());
        assertEquals(294, wb.getTotalAssemblySeats());
        assertEquals(5, wb.getElectionTurn());
        assertEquals("May 2001", wb.getElectionMonth());
        assertTrue(wb.getVoteSplits().containsKey("CPIM"));
        assertTrue(wb.getVoteSplits().containsKey("AITC"));

        // Check Rajasthan
        NationalStateOperationState rj = game.getStateOperations().get("RAJASTHAN");
        assertNotNull(rj);
        assertEquals("Rajasthan", rj.getStateName());
        assertEquals(25, rj.getTotalLokSabhaSeats());
        assertEquals(200, rj.getTotalAssemblySeats());
        assertEquals(36, rj.getElectionTurn());
        assertEquals("December 2003", rj.getElectionMonth());
        assertTrue(rj.getVoteSplits().containsKey("INC"));
        assertTrue(rj.getVoteSplits().containsKey("BJP"));

        // Check Assam
        NationalStateOperationState as = game.getStateOperations().get("ASSAM");
        assertNotNull(as);
        assertEquals("Assam", as.getStateName());
        assertEquals(14, as.getTotalLokSabhaSeats());
        assertEquals(126, as.getTotalAssemblySeats());
        assertEquals(5, as.getElectionTurn());
        assertEquals("May 2001", as.getElectionMonth());
        assertTrue(as.getVoteSplits().containsKey("INC"));
        assertTrue(as.getVoteSplits().containsKey("AGP"));

        // Check Tamil Nadu
        NationalStateOperationState tn = game.getStateOperations().get("TAMIL_NADU");
        assertNotNull(tn);
        assertEquals("Tamil Nadu", tn.getStateName());
        assertEquals(39, tn.getTotalLokSabhaSeats());
        assertEquals(234, tn.getTotalAssemblySeats());
        assertEquals(5, tn.getElectionTurn());
        assertEquals("May 2001", tn.getElectionMonth());
        assertTrue(tn.getVoteSplits().containsKey("AIADMK"));
        assertTrue(tn.getVoteSplits().containsKey("DMK"));
    }

    @Test
    public void testCuratedStateIssuesAndActions() {
        List<NationalStateIssueDefinition> upIssues = NationalStateIssueDefinition.getIssuesForState("UP");
        assertEquals(5, upIssues.size());
        assertTrue(upIssues.stream().anyMatch(i -> i.getId().equals("UP_CASTE_VIOLENCE")));
        assertTrue(upIssues.stream().anyMatch(i -> i.getId().equals("UP_LAW_ORDER")));
        assertTrue(upIssues.stream().anyMatch(i -> i.getId().equals("UP_AGRARIAN_DISTRESS")));
        assertTrue(upIssues.stream().anyMatch(i -> i.getId().equals("UP_MANDAL_POLITICS")));
        assertTrue(upIssues.stream().anyMatch(i -> i.getId().equals("UP_POWER_CRISIS")));

        List<NationalStateIssueDefinition> biharIssues = NationalStateIssueDefinition.getIssuesForState("BIHAR");
        assertEquals(5, biharIssues.size());
        assertTrue(biharIssues.stream().anyMatch(i -> i.getId().equals("BIHAR_JUNGLE_RAJ")));

        List<NationalStateIssueDefinition> mhIssues = NationalStateIssueDefinition.getIssuesForState("MAHARASHTRA");
        assertEquals(5, mhIssues.size());
        assertTrue(mhIssues.stream().anyMatch(i -> i.getId().equals("MH_VIDARBHA_FARMER_CRISIS")));

        List<NationalStateIssueDefinition> wbIssues = NationalStateIssueDefinition.getIssuesForState("WEST_BENGAL");
        assertEquals(5, wbIssues.size());
        assertTrue(wbIssues.stream().anyMatch(i -> i.getId().equals("WB_INDUSTRIAL_STAGNATION")));

        List<NationalStateIssueDefinition> rjIssues = NationalStateIssueDefinition.getIssuesForState("RAJASTHAN");
        assertEquals(5, rjIssues.size());
        assertTrue(rjIssues.stream().anyMatch(i -> i.getId().equals("RJ_DROUGHT_DISTRESS")));

        List<NationalStateIssueDefinition> asIssues = NationalStateIssueDefinition.getIssuesForState("ASSAM");
        assertEquals(5, asIssues.size());
        assertTrue(asIssues.stream().anyMatch(i -> i.getId().equals("AS_BRAHMAPUTRA_FLOODS")));

        List<NationalStateIssueDefinition> tnIssues = NationalStateIssueDefinition.getIssuesForState("TAMIL_NADU");
        assertEquals(5, tnIssues.size());
        assertTrue(tnIssues.stream().anyMatch(i -> i.getId().equals("TN_CAUVERY_WATER_DISPUTE")));

        List<Map<String, Object>> actions = NationalStateIssueDefinition.getTacticalActions();
        assertEquals(10, actions.size());
        assertTrue(actions.stream().anyMatch(a -> "PADAYATRA".equals(a.get("key"))));
        assertTrue(actions.stream().anyMatch(a -> "GHERAO".equals(a.get("key"))));
        assertTrue(actions.stream().anyMatch(a -> "RATH_YATRA".equals(a.get("key"))));
        assertTrue(actions.stream().anyMatch(a -> "JAN_SABHA".equals(a.get("key"))));
        assertTrue(actions.stream().anyMatch(a -> "MEMORANDUM".equals(a.get("key"))));
    }

    @Test
    public void testElectionPhaseProgression() {
        NationalStateOperationState state = new NationalStateOperationState();
        state.setElectionTurn(15);

        // Turn 1 (14 turns left) -> NORMAL
        state.updateElectionPhase(1);
        assertEquals(14, state.getTurnsToElection());
        assertEquals("NORMAL", state.getElectionPhase());

        // Turn 5 (10 turns left) -> PRE_ELECTION
        state.updateElectionPhase(5);
        assertEquals(10, state.getTurnsToElection());
        assertEquals("PRE_ELECTION", state.getElectionPhase());

        // Turn 10 (5 turns left) -> CAMPAIGN
        state.updateElectionPhase(10);
        assertEquals(5, state.getTurnsToElection());
        assertEquals("CAMPAIGN", state.getElectionPhase());

        // Turn 13 (2 turns left) -> FINAL_SPRINT
        state.updateElectionPhase(13);
        assertEquals(2, state.getTurnsToElection());
        assertEquals("FINAL_SPRINT", state.getElectionPhase());

        // Turn 15 (0 turns left) -> ELECTION_DAY
        state.updateElectionPhase(15);
        assertEquals(0, state.getTurnsToElection());
        assertEquals("ELECTION_DAY", state.getElectionPhase());
    }
}
