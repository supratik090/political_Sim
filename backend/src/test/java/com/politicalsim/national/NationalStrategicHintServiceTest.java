package com.politicalsim.national;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.*;

public class NationalStrategicHintServiceTest {

    private NationalGame game;
    private NationalStrategicHintService hintService;

    @BeforeEach
    public void setup() {
        hintService = new NationalStrategicHintService();
        game = new NationalGame();
        game.setId("hint-test-game");
        game.setUserId("user-123");
        game.setPartyKey("ydp");
        game.setPartyName("Youth Development Party");
        game.setPlayerFunds(20.0);
        game.setCurrentSeason(1);

        NationalPartyState playerState = new NationalPartyState();
        playerState.setPartyKey("ydp");
        playerState.setPartyName("Youth Development Party");
        playerState.setFunds(20.0);
        playerState.setWorkers(100000);
        playerState.setVolunteers(30000);
        playerState.setMorale(70);
        playerState.setCorruption(10);
        playerState.setSeats(26);
        playerState.setPlayerParty(true);
        game.getPartyStates().add(playerState);

        // Add UP as active state
        NationalStateOperationState up = new NationalStateOperationState();
        up.setStateCode("UP");
        up.setStateName("Uttar Pradesh");
        up.setTotalLokSabhaSeats(80);
        up.setTotalAssemblySeats(403);
        up.setTurnsToElection(14);
        up.setElectionPhase("PRE_ELECTION");
        up.setStateFunds(1.0);
        up.setStateWorkers(8000);
        up.setDoneThisTurn(false);
        up.setSkippedThisTurn(false);
        game.getStateOperations().put("UP", up);

        // Add Bihar as active state
        NationalStateOperationState br = new NationalStateOperationState();
        br.setStateCode("BR");
        br.setStateName("Bihar");
        br.setTotalLokSabhaSeats(40);
        br.setTotalAssemblySeats(243);
        br.setTurnsToElection(3);
        br.setElectionPhase("FINAL_SPRINT");
        br.setStateFunds(0.8);
        br.setStateWorkers(5000);
        br.setDoneThisTurn(false);
        br.setSkippedThisTurn(false);
        game.getStateOperations().put("BR", br);
    }

    @Test
    public void testHintsUrgeUnplayedStatesWhenPlayerHasNotPlayedAnyStates() {
        Map<String, Object> hints = hintService.generateStrategicHints(game);
        assertNotNull(hints);

        Map<?, ?> actions = (Map<?, ?>) hints.get("actions");
        assertNotNull(actions);
        Map<?, ?> statesAction = (Map<?, ?>) actions.get("states");
        assertNotNull(statesAction);

        // Player has not played any states
        assertEquals(Boolean.TRUE, statesAction.get("hasNotPlayedAnyStates"));
        assertEquals("PENDING", statesAction.get("status"));

        List<?> warnings = (List<?>) hints.get("urgentWarnings");
        assertNotNull(warnings);
        boolean hasUnplayedWarning = warnings.stream().anyMatch(w -> w.toString().contains("UNPLAYED ELIGIBLE STATES"));
        assertTrue(hasUnplayedWarning, "Urgent warnings must flag unplayed eligible states!");

        // Now simulate player completing action in Bihar
        game.getStateOperations().get("BR").setDoneThisTurn(true);
        Map<String, Object> updatedHints = hintService.generateStrategicHints(game);
        Map<?, ?> updatedStatesAction = (Map<?, ?>) ((Map<?, ?>) updatedHints.get("actions")).get("states");
        assertEquals(Boolean.FALSE, updatedStatesAction.get("hasNotPlayedAnyStates"));
    }

    @Test
    public void testHintsGuideMoraleRecoveryWhenMoraleCollapses() {
        // Drop player morale to critical levels
        game.findPartyState("ydp").setMorale(35);

        Map<String, Object> hints = hintService.generateStrategicHints(game);
        assertNotNull(hints);

        Map<?, ?> summary = (Map<?, ?>) hints.get("summary");
        assertNotNull(summary);
        Map<?, ?> moraleStatus = (Map<?, ?>) summary.get("moraleStatus");
        assertNotNull(moraleStatus);

        assertEquals(35, moraleStatus.get("morale"));
        assertEquals("CRITICAL", moraleStatus.get("trend"));
        assertTrue(moraleStatus.get("advice").toString().contains("turnout"));

        List<?> warnings = (List<?>) hints.get("urgentWarnings");
        boolean hasMoraleWarning = warnings.stream().anyMatch(w -> w.toString().contains("CRITICAL CADRE MORALE"));
        assertTrue(hasMoraleWarning, "Urgent warnings must alert player on critical morale collapse!");
    }

    @Test
    public void testStateLevelResourceTransfersAndInfrastructureRecommendations() {
        Map<String, Object> hints = hintService.generateStrategicHints(game);
        assertNotNull(hints);

        @SuppressWarnings("unchecked")
        List<Map<String, Object>> ranked = (List<Map<String, Object>>) hints.get("rankedStates");
        assertNotNull(ranked);
        assertFalse(ranked.isEmpty());

        // Bihar is in FINAL_SPRINT (3 turns), so should have high urgency score
        Map<String, Object> bihar = ranked.stream().filter(s -> "BR".equals(s.get("stateCode"))).findFirst().orElse(null);
        assertNotNull(bihar);
        assertEquals("FINAL SPRINT ⚡", bihar.get("urgencyBadge"));
        assertTrue(((Number) bihar.get("recTransferFunds")).doubleValue() > 0.0);
        assertTrue(((Number) bihar.get("recTransferWorkers")).intValue() > 0);

        // Check recommended infra
        Map<?, ?> recInfra = (Map<?, ?>) bihar.get("recInfra");
        assertNotNull(recInfra);
        assertEquals("state_party_hq", recInfra.get("key"));
    }

    @Test
    public void testTargetPartyAndMediaSocialGuidance() {
        // Add a rival party
        NationalPartyState bjp = new NationalPartyState();
        bjp.setPartyKey("bjp");
        bjp.setPartyName("Bharatiya Janata Party");
        bjp.setSeats(182);
        bjp.setMorale(75);
        game.getPartyStates().add(bjp);

        Map<String, Object> hints = hintService.generateStrategicHints(game);
        assertNotNull(hints);

        Map<?, ?> actions = (Map<?, ?>) hints.get("actions");
        Map<?, ?> eventsAction = (Map<?, ?>) actions.get("events");
        assertNotNull(eventsAction);

        // Check target party tip recommends targeting BJP (top rival)
        String targetTip = (String) eventsAction.get("targetPartyTip");
        assertNotNull(targetTip);
        assertTrue(targetTip.contains("BJP") || targetTip.contains("Bharatiya Janata Party"),
            "Target party tip should advise attacking main rival BJP");

        // Check media social tip
        String mediaTip = (String) eventsAction.get("mediaSocialTip");
        assertNotNull(mediaTip);
        assertTrue(mediaTip.contains("Influencers") || mediaTip.contains("WhatsApp"),
            "Media tip should advise on digital channels");

        // Now set target party explicitly
        game.setTargetPartyKey("bjp");
        game.setMediaSocialCommitted(true);
        Map<String, Double> spend = new HashMap<>();
        spend.put("social_ads", 2.0);
        spend.put("podcasts", 1.5);
        game.setMediaSocialSpend(spend);

        Map<String, Object> updatedHints = hintService.generateStrategicHints(game);
        Map<?, ?> updatedEventsAction = (Map<?, ?>) ((Map<?, ?>) updatedHints.get("actions")).get("events");

        String updatedTargetTip = (String) updatedEventsAction.get("targetPartyTip");
        assertTrue(updatedTargetTip.contains("BJP"), "Should reflect selected target party");

        String updatedMediaTip = (String) updatedEventsAction.get("mediaSocialTip");
        assertTrue(updatedMediaTip.contains("committed"), "Should confirm media campaign is committed");
    }
}
