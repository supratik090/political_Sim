package com.politicalsim.national;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.*;

public class NationalStateEligibilityTest {

    private NationalGame game;

    @BeforeEach
    public void setup() {
        game = new NationalGame();
        game.setId("test-game");
        game.setCurrentSeason(3);
        game.setPartyKey("BJP");

        NationalPartyState bjp = new NationalPartyState();
        bjp.setPartyKey("BJP");
        bjp.setPartyName("Bharatiya Janata Party");
        bjp.setPlayerParty(true);
        game.getPartyStates().add(bjp);

        NationalPartyState dmk = new NationalPartyState();
        dmk.setPartyKey("DMK");
        dmk.setPartyName("Dravida Munnetra Kazhagam");
        game.getPartyStates().add(dmk);
    }

    @Test
    public void testDirectPlayerStateIsEligible() {
        // UP where BJP is ruling party and has vote split
        NationalStateOperationState up = new NationalStateOperationState();
        up.setStateCode("UP");
        up.setStateName("Uttar Pradesh");
        up.setRulingParty("BJP");
        Map<String, Double> votes = new HashMap<>();
        votes.put("BJP", 34.0);
        votes.put("SP", 30.0);
        up.setVoteSplits(votes);

        Map<String, Object> eval = NationalGameService.evaluateStateEligibility(game, up);
        assertEquals(Boolean.TRUE, eval.get("isEligible"));
        assertEquals(Boolean.TRUE, eval.get("isPlayerActive"));
        assertEquals(Boolean.FALSE, eval.get("isNewlyUnlocked"));
        assertNull(eval.get("unlockedByPartner"));
    }

    @Test
    public void testInactiveStateIsLockedUntilAllianceFormed() {
        // Tamil Nadu where BJP has 0% vote and is not ruling/opposition
        NationalStateOperationState tn = new NationalStateOperationState();
        tn.setStateCode("TAMIL_NADU");
        tn.setStateName("Tamil Nadu");
        tn.setRulingParty("AIADMK");
        tn.setOppositionParty("DMK");
        Map<String, Double> votes = new HashMap<>();
        votes.put("AIADMK", 40.0);
        votes.put("DMK", 36.0);
        votes.put("INC", 5.0);
        votes.put("BJP", 0.0);
        tn.setVoteSplits(votes);

        // Before alliance: state is locked
        Map<String, Object> evalBefore = NationalGameService.evaluateStateEligibility(game, tn);
        assertEquals(Boolean.FALSE, evalBefore.get("isEligible"));
        assertEquals(Boolean.FALSE, evalBefore.get("isPlayerActive"));
        assertEquals(Boolean.FALSE, evalBefore.get("isNewlyUnlocked"));
        assertNull(evalBefore.get("unlockedByPartner"));

        List<?> unlockingParties = (List<?>) evalBefore.get("unlockingParties");
        assertNotNull(unlockingParties);
        assertTrue(unlockingParties.contains("DMK"));
        assertTrue(unlockingParties.contains("AIADMK"));

        // Now form an alliance with DMK in the current season (season 3)
        NationalAlliance alliance = new NationalAlliance();
        alliance.setAllianceId("test-nda");
        alliance.setLeaderPartyKey("BJP");
        NationalAllianceMember bjpMember = new NationalAllianceMember();
        bjpMember.setPartyKey("BJP");
        bjpMember.setJoinedAtSeason(1);

        NationalAllianceMember dmkMember = new NationalAllianceMember();
        dmkMember.setPartyKey("DMK");
        dmkMember.setJoinedAtSeason(3); // Joined this turn!

        alliance.setMembers(new ArrayList<>(Arrays.asList(bjpMember, dmkMember)));
        game.getAlliances().add(alliance);

        // After alliance: state is newly unlocked via DMK!
        Map<String, Object> evalAfter = NationalGameService.evaluateStateEligibility(game, tn);
        assertEquals(Boolean.TRUE, evalAfter.get("isEligible"));
        assertEquals(Boolean.FALSE, evalAfter.get("isPlayerActive"));
        assertEquals(Boolean.TRUE, evalAfter.get("isNewlyUnlocked"));
        assertEquals("DMK", evalAfter.get("unlockedByPartner"));
    }
}
