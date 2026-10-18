package com.politicalsim.national;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.*;

public class NationalPartyDonationTest {

    private NationalGame game;
    private NationalGameService gameService;
    private NationalPartyState bjp;
    private NationalPartyState inc;

    @BeforeEach
    public void setup() {
        gameService = new NationalGameService();
        game = new NationalGame();
        game.setId("donation-test-game");
        game.setCurrentSeason(1);
        game.setPartyKey("BJP");
        game.setPlayerFunds(30.0);

        bjp = new NationalPartyState();
        bjp.setPartyKey("BJP");
        bjp.setPartyName("Bharatiya Janata Party");
        bjp.setFunds(30.0);
        bjp.setSeats(100);
        bjp.setMorale(70);
        bjp.setPlayerParty(true);
        game.getPartyStates().add(bjp);

        inc = new NationalPartyState();
        inc.setPartyKey("INC");
        inc.setPartyName("Indian National Congress");
        inc.setFunds(20.0);
        inc.setSeats(60);
        inc.setMorale(60);
        inc.setPlayerParty(false);
        game.getPartyStates().add(inc);
    }

    @Test
    public void testBaseDonationWithoutMomentum() {
        // BJP has 100 projected seats (same as actual seats 100) and moderate morale (70)
        Map<String, Integer> proj = new HashMap<>();
        proj.put("BJP", 100);
        proj.put("INC", 60);
        game.setNationalProjectedSeats(proj);

        assertFalse(gameService.isPartyGainingMomentum(game, bjp));
        // Base donation = 100 * 0.5 = 50.0 Cr
        double donation = gameService.calculatePartyDonation(game, bjp);
        assertEquals(50.0, donation, 0.01);
    }

    @Test
    public void testMomentumBonusOnProjectedSeatGrowth() {
        // BJP has 120 projected seats (growth over actual 100 seats)
        Map<String, Integer> proj = new HashMap<>();
        proj.put("BJP", 120);
        proj.put("INC", 50);
        game.setNationalProjectedSeats(proj);

        assertTrue(gameService.isPartyGainingMomentum(game, bjp));
        // Donation with momentum bonus = 120 * 0.75 = 90.0 Cr
        double donation = gameService.calculatePartyDonation(game, bjp);
        assertEquals(90.0, donation, 0.01);
    }

    @Test
    public void testMomentumBonusOnMoraleSurge() {
        // INC has 60 projected seats (equal to actual), but morale surges to 80%
        inc.setMorale(80);
        Map<String, Integer> proj = new HashMap<>();
        proj.put("BJP", 100);
        proj.put("INC", 60);
        game.setNationalProjectedSeats(proj);

        assertTrue(gameService.isPartyGainingMomentum(game, inc));
        // Donation = 60 * 0.75 = 45.0 Cr
        double donation = gameService.calculatePartyDonation(game, inc);
        assertEquals(45.0, donation, 0.01);
    }

    @Test
    public void testRecalculateNationalProjectedSeatsSetsPartyFields() {
        Map<String, Integer> proj = new HashMap<>();
        proj.put("BJP", 110);
        proj.put("INC", 60);

        NationalStateOperationState up = new NationalStateOperationState();
        up.setStateCode("UP");
        up.setProjectedLokSabhaSeats(proj);
        Map<String, Integer> base = new HashMap<>();
        base.put("BJP", 100);
        base.put("INC", 60);
        up.setBaselineLokSabhaSeats(base);
        game.getStateOperations().put("UP", up);

        gameService.recalculateNationalProjectedSeats(game);

        assertEquals(110, bjp.getProjectedSeats());
        assertTrue(bjp.isGainingMomentum());
        // 110 * 0.75 = 82.5 Cr
        assertEquals(82.5, bjp.getDonationsPerTurn(), 0.01);
    }
}
