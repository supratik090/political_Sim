package com.politicalsim;

import com.politicalsim.game.GameSession;
import com.politicalsim.game.GameSessionRepository;
import com.politicalsim.party.PartyState;
import com.politicalsim.game.RoundSubmission;
import java.util.List;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class DiagnosticDbTest {

    @Autowired
    private GameSessionRepository repository;

    @Test
    void printLastGameSessionDetails() {
        System.out.println("========== DB DIAGNOSTIC TEST START ==========");
        List<GameSession> sessions = repository.findAllByOrderByCurrentDateDesc();
        if (sessions.isEmpty()) {
            System.out.println("No game sessions found in database!");
            return;
        }

        GameSession session = sessions.get(0);
        System.out.println("Game ID: " + session.getId());
        System.out.println("Scenario: " + session.getScenarioKey());
        System.out.println("Status: " + session.getStatus());
        System.out.println("Turn Number: " + session.getTurnNumber());
        System.out.println("Active Crisis: " + session.getActiveCrisisName() + " (" + session.getActiveCrisisKey() + "), Turns Left: " + session.getActiveCrisisTurnsLeft());

        System.out.println("\n--- Parties Stats ---");
        for (PartyState party : session.getParties()) {
            System.out.println("Party: " + party.getName() + " (" + party.getRole() + ")");
            System.out.println("  Controller: " + party.getControllerType());
            System.out.println("  Active: " + party.isActive());
            System.out.println("  Coins: " + party.getStats().getCoins());
            System.out.println("  Morale: " + party.getStats().getPartyMorale());
            System.out.println("  Corruption: " + party.getStats().getCorruptionScore() + "%");
            System.out.println("  Media Image: " + party.getStats().getMediaImage());
            System.out.println("  Voter Support: " + party.getStats().getPublicSupport() + "%");
            if (session.getLastMetricDeltas() != null && session.getLastMetricDeltas().containsKey(party.getId())) {
                System.out.println("  Last Round Deltas: " + session.getLastMetricDeltas().get(party.getId()));
            }
        }

        System.out.println("\n--- Last Round Submissions ---");
        if (session.getLastRoundSubmissions() != null) {
            for (RoundSubmission sub : session.getLastRoundSubmissions()) {
                System.out.println("Party: " + sub.getPartyName());
                System.out.println("  Played Card: " + sub.getCardName() + " (" + sub.getCardKey() + ")");
                System.out.println("  Bid: " + sub.getBid());
                if (sub.getSelectedRewardKey() != null) {
                    System.out.println("  Played Reward: " + sub.getRewardName() + " (" + sub.getSelectedRewardKey() + ")");
                }
            }
        }

        System.out.println("\n--- Last Round Commentary ---");
        if (session.getLastRoundCommentary() != null) {
            for (String comment : session.getLastRoundCommentary()) {
                System.out.println("  💬 " + comment);
            }
        }

        System.out.println("\n--- Last Round Results Summary ---");
        if (session.getLastResults() != null) {
            for (String result : session.getLastResults()) {
                System.out.println("  - " + result);
            }
        }
        System.out.println("========== DB DIAGNOSTIC TEST END ==========");
    }
}
