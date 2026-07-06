package com.politicalsim.game;

import static org.junit.jupiter.api.Assertions.assertEquals;

import com.politicalsim.content.CardDefinition;
import com.politicalsim.party.ControllerType;
import com.politicalsim.party.Ideology;
import com.politicalsim.party.PartyRole;
import com.politicalsim.party.PartyState;
import com.politicalsim.party.PartyStats;
import com.politicalsim.publicmood.PublicState;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.Test;

class RoundResolutionEngineTest {

    private final RoundResolutionEngine engine = new RoundResolutionEngine(null, null, null);

    @Test
    void applyRewardEffectDistributesPositiveSupportProportionally() {
        GameSession session = new GameSession();
        PublicState publicState = new PublicState();
        publicState.setUndecidedSupport(10);
        session.setPublicState(publicState);

        PartyState target = party("Tiger Front", PartyRole.GOVERNMENT, new PartyStats(100, 50, 20, 50, 30));
        PartyState other1 = party("Elephant Congress", PartyRole.OPPOSITION, new PartyStats(100, 50, 20, 50, 40));
        PartyState other2 = party("Lotus League", PartyRole.OPPOSITION, new PartyStats(100, 50, 20, 50, 20));

        session.setParties(List.of(target, other1, other2));

        RewardDefinition reward = new RewardDefinition(
                "reward_rally_10_support",
                "Grassroots Rally",
                "Boost public support by 8% of yourself.",
                false,
                "self",
                0, 0, 0, 0, 8
        );

        List<String> commentary = new ArrayList<>();
        engine.applyRewardEffect(session, target, reward, commentary);

        // Deductions calculation:
        // totalOtherSupport = 40 + 20 = 60
        // supportEffect = 8
        // other1 (sorted first since 40 > 20):
        //   deduct = Math.round(40 * 8 / 60.0) = Math.round(5.33) = 5
        //   new support = 40 - 5 = 35
        // other2 (last):
        //   deduct = 8 - 5 = 3
        //   new support = 20 - 3 = 17
        // target:
        //   gains = 5 + 3 = 8
        //   new support = 30 + 8 = 38
        assertEquals(38, target.getStats().getPublicSupport());
        assertEquals(35, other1.getStats().getPublicSupport());
        assertEquals(17, other2.getStats().getPublicSupport());
        assertEquals(10, session.getPublicState().getUndecidedSupport());
    }

    @Test
    void applyRewardEffectHandlesInsufficientSupportOnOtherParties() {
        GameSession session = new GameSession();
        PublicState publicState = new PublicState();
        publicState.setUndecidedSupport(65);
        session.setPublicState(publicState);

        PartyState target = party("Tiger Front", PartyRole.GOVERNMENT, new PartyStats(100, 50, 20, 50, 30));
        PartyState other1 = party("Elephant Congress", PartyRole.OPPOSITION, new PartyStats(100, 50, 20, 50, 3));
        PartyState cervix = party("Lotus League", PartyRole.OPPOSITION, new PartyStats(100, 50, 20, 50, 2));

        session.setParties(List.of(target, other1, cervix));

        RewardDefinition reward = new RewardDefinition(
                "reward_rally_10_support",
                "Grassroots Rally",
                "Boost public support by 8% of yourself.",
                false,
                "self",
                0, 0, 0, 0, 8
        );

        List<String> commentary = new ArrayList<>();
        engine.applyRewardEffect(session, target, reward, commentary);

        // Deductions calculation:
        // totalOtherSupport = 3 + 2 = 5
        // supportEffect = 8
        // other1 (sorted first since 3 > 2):
        //   deduct = Math.round(3 * 8 / 5.0) = Math.round(4.8) = 5
        //   clamped to currentSupport: Math.min(3, 5) = 3
        //   new support = 3 - 3 = 0
        // cervix (last):
        //   deduct = 8 - 3 = 5
        //   clamped to currentSupport: Math.min(2, 5) = 2
        //   new support = 2 - 2 = 0
        // target:
        //   gains = 3 + 2 = 5
        //   new support = 30 + 5 = 35
        assertEquals(35, target.getStats().getPublicSupport());
        assertEquals(0, other1.getStats().getPublicSupport());
        assertEquals(0, cervix.getStats().getPublicSupport());
        assertEquals(65, session.getPublicState().getUndecidedSupport());
    }

    private PartyState party(String name, PartyRole role, PartyStats stats) {
        return new PartyState(
                "party-" + name.replace(" ", "-").toLowerCase(),
                name,
                role,
                ControllerType.COMPUTER,
                null,
                "#000000",
                "Tiger",
                Ideology.ANTI_CORRUPTION,
                null,
                stats
        );
    }

    @Test
    void resolveRoundLogsHeldRewardsProjectFundingAndCoinMovements() {
        GameSession session = new GameSession();
        session.setTurnNumber(1);
        session.setCurrentDate(java.time.LocalDate.now());
        session.setScenarioKey("test");
        PublicState publicState = new PublicState();
        session.setPublicState(publicState);
        
        PartyState partyA = party("Party A", PartyRole.GOVERNMENT, new PartyStats(100, 50, 0, 50, 40));
        PartyState partyB = party("Party B", PartyRole.OPPOSITION, new PartyStats(80, 50, 0, 50, 40));
        session.setParties(List.of(partyA, partyB));
        session.setGovernmentParty(partyA);
        
        // Setup a card in the session cards
        CardDefinition card = new CardDefinition();
        card.setCardKey("test_card");
        card.setName("Transparency Campaign");
        card.setRoleAllowed(List.of("GOVERNMENT"));
        card.setCost(30); // costs 30 coins
        card.setVisibleEffects(Map.of(
            "selfParty", Map.of(
                "coins", 0
            )
        ));
        card.setWeights(Map.of("riskWeight", 0.0, "basePlayWeight", 1.0, "aiPriorityWeight", 1.0, "publicImpactWeight", 1.0));
        session.setGameCards(List.of(card));

        // Add a submission for Party A playing this card
        RoundSubmission sub = new RoundSubmission();
        sub.setPartyId(partyA.getId());
        sub.setPartyName(partyA.getName());
        sub.setCardKey("test_card");
        sub.setCardName("Transparency Campaign");
        session.getCurrentRoundSubmissions().add(sub);
        
        // 1. Setup held reward
        HeldReward hr = new HeldReward("reward_donation_100_coins", "Private Donation", "Gift 40 coins", 15, false, "self");
        session.getPartyHeldRewards().computeIfAbsent(partyA.getId(), k -> new ArrayList<>()).add(hr);
        
        // 2. Setup project contribution
        // Project contributions: Party B contributed 20% to Party Headquarters
        session.getProjectContributionsThisTurn().computeIfAbsent(partyB.getId(), k -> new java.util.LinkedHashMap<>()).put("PARTY_HQ", 20);
        
        // Resolve the round
        engine.resolveRound(session);
        
        List<String> commentary = session.getLastRoundCommentary();
        List<String> results = session.getLastResults();
        
        // Assert project funding is logged
        org.junit.jupiter.api.Assertions.assertTrue(commentary.stream().anyMatch(c -> c.contains("funded project 'Party Headquarters'")));
        org.junit.jupiter.api.Assertions.assertTrue(results.stream().anyMatch(r -> r.contains("funded project 'Party Headquarters'")));
        
        // Assert coin movement is logged (Party A had a net change of -30 coins)
        org.junit.jupiter.api.Assertions.assertTrue(commentary.stream().anyMatch(c -> c.contains("Party A had a net change of -30 coins")));
        
        // Assert held rewards are logged
        org.junit.jupiter.api.Assertions.assertTrue(commentary.stream().anyMatch(c -> c.contains("Party A is holding reward: Private Donation")));
        org.junit.jupiter.api.Assertions.assertTrue(results.stream().anyMatch(r -> r.contains("Party A is holding reward: Private Donation")));
    }

    @Test
    void resolveRoundLogsAiDecisionBasisAndNextRoundStrategicOutlook() {
        GameSession session = new GameSession();
        session.setTurnNumber(1);
        session.setCurrentDate(java.time.LocalDate.now());
        session.setScenarioKey("test");
        PublicState publicState = new PublicState();
        session.setPublicState(publicState);
        
        // Party A is COMPUTER, so it gets next turn priorities logged
        PartyStats stats = new PartyStats(60, 40, 0, 50, 20); // low coins, low morale, low support
        PartyState partyA = party("Party A", PartyRole.GOVERNMENT, stats);
        partyA.setControllerType(ControllerType.COMPUTER);
        session.setParties(List.of(partyA));
        session.setGovernmentParty(partyA);
        
        CardDefinition card = new CardDefinition();
        card.setCardKey("no_card");
        card.setName("No Card");
        card.setRoleAllowed(List.of("GOVERNMENT"));
        card.setWeights(Map.of("riskWeight", 0.0, "basePlayWeight", 1.0, "aiPriorityWeight", 1.0, "publicImpactWeight", 1.0));
        session.setGameCards(List.of(card));

        RoundSubmission sub = new RoundSubmission();
        sub.setPartyId(partyA.getId());
        sub.setPartyName(partyA.getName());
        sub.setCardKey("no_card");
        sub.setCardName("No Card");
        sub.setAiDecisionBasis("Party A decided to conserve energy.");
        session.getCurrentRoundSubmissions().add(sub);
        
        engine.resolveRound(session);
        
        List<String> commentary = session.getLastRoundCommentary();
        
        // Assert AI decision basis is logged
        org.junit.jupiter.api.Assertions.assertTrue(commentary.stream().anyMatch(c -> c.contains("🤖 AI Decision Analysis: Party A decided to conserve energy.")));
        
        // Assert Next Round Outlook is logged with low coins, morale, support needs
        org.junit.jupiter.api.Assertions.assertTrue(commentary.stream().anyMatch(c -> c.contains("🔮 Next Round Strategic Outlook:")));
        org.junit.jupiter.api.Assertions.assertTrue(commentary.stream().anyMatch(c -> c.contains("Party A next round priorities: needs to focus on restoring Coins") 
                && c.contains("Morale") && c.contains("Voter Support")));
    }

    @Test
    void testResolveRoundTriggersVictoryWhenAllOpponentsDefeated() {
        GameSession session = new GameSession();
        session.setTurnNumber(1);
        session.setCurrentDate(java.time.LocalDate.now());
        session.setScenarioKey("test");
        session.setStatus(GameStatus.ACTIVE);
        PublicState publicState = new PublicState();
        session.setPublicState(publicState);

        PartyState humanParty = party("Human Party", PartyRole.GOVERNMENT, new PartyStats(100, 50, 0, 50, 60));
        humanParty.setControllerType(ControllerType.HUMAN);
        
        PartyState ai1 = party("AI 1", PartyRole.DEFEATED, new PartyStats(0, 0, 0, 0, 0));
        ai1.setActive(false);
        
        PartyState ai2 = party("AI 2", PartyRole.DEFEATED, new PartyStats(0, 0, 0, 0, 0));
        ai2.setActive(false);

        session.setParties(List.of(humanParty, ai1, ai2));
        session.setPlayerPartyIds(List.of(humanParty.getId()));

        engine.resolveRound(session);

        assertEquals(GameStatus.VICTORY, session.getStatus());
        org.junit.jupiter.api.Assertions.assertTrue(session.getLastRoundCommentary().stream().anyMatch(c -> c.contains("🏆 VICTORY: All opponent parties have been defeated!")));
    }

    @Test
    void testConductElectionEndsGameOnOrAfterTurn60() {
        GameSession session = new GameSession();
        session.setTurnNumber(60);
        session.setCurrentDate(java.time.LocalDate.now());
        session.setScenarioKey("test");
        session.setStatus(GameStatus.ACTIVE);
        PublicState publicState = new PublicState();
        publicState.setUndecidedSupport(10);
        session.setPublicState(publicState);

        PartyState humanParty = party("Human Party", PartyRole.OPPOSITION, new PartyStats(100, 50, 0, 50, 50));
        humanParty.setControllerType(ControllerType.HUMAN);
        
        PartyState aiParty = party("AI Party", PartyRole.GOVERNMENT, new PartyStats(100, 50, 0, 50, 40));
        aiParty.setControllerType(ControllerType.COMPUTER);

        session.setParties(List.of(humanParty, aiParty));
        session.setPlayerPartyIds(List.of(humanParty.getId()));

        engine.conductElection(session, "Mandatory 60-month election completed.", false);

        // Human has 50% vs AI 40%, so Human should win
        assertEquals(GameStatus.VICTORY, session.getStatus());
        assertEquals("Human Party", session.getLastElectionWinner());
        org.junit.jupiter.api.Assertions.assertTrue(session.isLastElectionHeld());
        assertEquals(56, session.getLastElectionVoteShares().get("Human Party"));
        assertEquals(44, session.getLastElectionVoteShares().get("AI Party"));
        assertEquals(0, session.getLastElectionVoteShares().get("Undecided Voters"));
    }
}
