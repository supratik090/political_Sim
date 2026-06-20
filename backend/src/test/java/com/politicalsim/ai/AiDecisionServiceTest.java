package com.politicalsim.ai;

import static org.junit.jupiter.api.Assertions.assertEquals;

import com.politicalsim.content.CardDefinition;
import com.politicalsim.game.RewardDefinition;
import com.politicalsim.game.GameSession;
import com.politicalsim.party.ControllerType;
import com.politicalsim.party.Ideology;
import com.politicalsim.party.PartyRole;
import com.politicalsim.party.PartyState;
import com.politicalsim.party.PartyStats;
import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.Test;

class AiDecisionServiceTest {

    private final AiDecisionService service = new AiDecisionService();

    @Test
    void oppositionTargetsWeakGovernmentForNoConfidence() {
        GameSession session = new GameSession();
        session.setMonthInCycle(20);
        PartyState government = party("Tiger Front", PartyRole.GOVERNMENT, new PartyStats(150, 28, 45, 35, 26));
        PartyState opposition = party("Elephant Congress", PartyRole.OPPOSITION, new PartyStats(120, 55, 12, 50, 34));
        session.setGovernmentParty(government);

        AiIntent intent = service.chooseIntent(session, opposition, government);

        assertEquals(AiIntent.FORCE_NO_CONFIDENCE, intent);
    }

    @Test
    void cautiousGovernmentPrefersDefensiveCounterWhenCorruptionIsHigh() {
        GameSession session = new GameSession();
        session.setMonthInCycle(12);
        PartyState government = party("Tiger Front", PartyRole.GOVERNMENT, new PartyStats(180, 60, 58, 42, 36));
        PartyState opposition = party("Elephant Congress", PartyRole.OPPOSITION, new PartyStats(120, 55, 15, 50, 34));
        session.setGovernmentParty(government);

        AiDecision decision = service.chooseCard(session, government, opposition, List.of(
                card("gov_big_rally", "media_narrative", PartyRole.GOVERNMENT, 10, 1, 2, 0, -1),
                card("gov_counter_scandal", "defensive_counter", PartyRole.GOVERNMENT, 8, 0, 3, -6, 0)
        ));

        assertEquals(AiIntent.SURVIVE_SCANDAL, decision.intent());
        assertEquals("gov_counter_scandal", decision.card().getCardKey());
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
                AiProfile.defaultForRole(role),
                stats
        );
    }

    private CardDefinition card(String key, String category, PartyRole role, int cost, int support, int media,
            int corruption, int morale) {
        CardDefinition card = new CardDefinition();
        card.setScenarioKey("test");
        card.setCardKey(key);
        card.setName(key);
        card.setCategory(category);
        card.setRoleAllowed(List.of(role.name()));
        card.setCost(cost);
        card.setVisibleEffects(Map.of(
                "selfParty", Map.of(
                        "coins", -cost,
                        "publicSupport", support,
                        "mediaImage", media,
                        "corruptionScore", corruption,
                        "partyMorale", morale
                )
        ));
        card.setWeights(Map.of(
                "basePlayWeight", 1.0,
                "aiPriorityWeight", 1.0,
                "publicImpactWeight", 1.0,
                "riskWeight", 0.3
        ));
        return card;
    }

    @Test
    void rewardUtilityVariesBasedOnNeeds() {
        GameSession session = new GameSession();
        PartyState party = party("Elephant Congress", PartyRole.OPPOSITION, new PartyStats(35, 20, 20, 50, 20)); // low coins, low morale
        RewardDefinition coinsReward = new RewardDefinition("reward_donation", "Coins Boost", "Gift coins", false, "self", 40, 0, 0, 0, 0);
        RewardDefinition moraleReward = new RewardDefinition("reward_morale", "Morale Boost", "Gift morale", false, "self", 0, 35, 0, 0, 0);
        RewardDefinition supportReward = new RewardDefinition("reward_support", "Support Boost", "Gift support", false, "self", 0, 0, 0, 0, 8);
        
        double coinsUtility = service.evaluateRewardUtility(session, party, coinsReward);
        double moraleUtility = service.evaluateRewardUtility(session, party, moraleReward);
        double supportUtility = service.evaluateRewardUtility(session, party, supportReward);
        
        org.junit.jupiter.api.Assertions.assertTrue(coinsUtility >= 0.8);
        org.junit.jupiter.api.Assertions.assertTrue(moraleUtility >= 0.8);
        org.junit.jupiter.api.Assertions.assertTrue(supportUtility >= 0.9);
    }

    @Test
    void chooseOpponentConsidersGrudgesAndWeaknesses() {
        GameSession session = new GameSession();
        PartyState actor = party("Party A", PartyRole.OPPOSITION, new PartyStats(100, 50, 0, 50, 20));
        PartyState opp1 = party("Party B", PartyRole.GOVERNMENT, new PartyStats(100, 50, 0, 50, 40)); // Leader: 40% support
        PartyState opp2 = party("Party C", PartyRole.THIRD_PARTY, new PartyStats(20, 50, 0, 50, 10)); // Low support, low coins
        
        session.setParties(List.of(actor, opp1, opp2));
        
        // Without grudges or specific cards, it should choose leader opp1 (40% support vs 10% support)
        PartyState targetNoCard = service.chooseOpponent(session, actor, null);
        assertEquals(opp1.getId(), targetNoCard.getId());
        
        // With a coins damage card, opp2 should be targeted because they have low coins (20)
        CardDefinition coinsDrainingCard = card("coins_drain", "scandal", PartyRole.OPPOSITION, 10, 0, 0, 0, 0);
        coinsDrainingCard.setVisibleEffects(Map.of(
            "opponentParty", Map.of(
                "coins", -20
            )
        ));
        PartyState targetWithDrainingCard = service.chooseOpponent(session, actor, coinsDrainingCard);
        assertEquals(opp2.getId(), targetWithDrainingCard.getId());
        
        // Add a grudge against the leader (opp1). Grudge level 8 means score gets +80.0 boost
        session.getGrudges().computeIfAbsent(actor.getId(), k -> new java.util.LinkedHashMap<>()).put(opp1.getId(), 8);
        
        PartyState targetWithGrudge = service.chooseOpponent(session, actor, coinsDrainingCard);
        assertEquals(opp1.getId(), targetWithGrudge.getId());
    }

    @Test
    void aiChoosesNoCardWhenCoinsAreTooLow() {
        GameSession session = new GameSession();
        session.setMonthInCycle(12);
        
        // Government party has 15 coins left (which is dangerously low)
        PartyState government = party("Tiger Front", PartyRole.GOVERNMENT, new PartyStats(15, 60, 10, 50, 36));
        PartyState opposition = party("Elephant Congress", PartyRole.OPPOSITION, new PartyStats(120, 55, 15, 50, 34));
        session.setGovernmentParty(government);

        // We offer a card that costs 10 coins, and the "no_card" (Pass Turn) which costs 0
        CardDefinition rally = card("gov_big_rally", "media_narrative", PartyRole.GOVERNMENT, 10, 1, 2, 0, 0);
        CardDefinition noCard = card("no_card", "governance", PartyRole.GOVERNMENT, 0, 0, 0, 0, 0);

        AiDecision decision = service.chooseCard(session, government, opposition, List.of(rally, noCard));

        // The AI should avoid the 10-cost card because it would leave them with only 5 coins (< 10 critical threshold)
        // and instead choose "no_card" (Pass Turn).
        assertEquals("no_card", decision.card().getCardKey());
    }

    @Test
    void aiAvoidsMoraleDepletingCardsWhenMoraleIsLow() {
        GameSession session = new GameSession();
        session.setMonthInCycle(12);
        
        // Government party has 20 morale (low)
        PartyState government = party("Tiger Front", PartyRole.GOVERNMENT, new PartyStats(100, 20, 10, 50, 36));
        PartyState opposition = party("Elephant Congress", PartyRole.OPPOSITION, new PartyStats(120, 55, 15, 50, 34));
        session.setGovernmentParty(government);

        // We offer a card that costs 0 coins but deducts 9 morale, and a standard card that does not deduct morale
        CardDefinition sacrificeMinister = card("gov_sacrifice_minister", "defensive_counter", PartyRole.GOVERNMENT, 0, 0, 1, -1, -9);
        CardDefinition normalCard = card("gov_normal_card", "governance", PartyRole.GOVERNMENT, 0, 0, 0, 0, 0);

        AiDecision decision = service.chooseCard(session, government, opposition, List.of(sacrificeMinister, normalCard));

        // The AI should avoid the morale-depleting card since remaining morale would be 11 (< 12 critical threshold)
        assertEquals("gov_normal_card", decision.card().getCardKey());
    }

    @Test
    void aiPlaysWelfareOrOrganizationCardToIncreaseCoinsInCrisis() {
        GameSession session = new GameSession();
        session.setMonthInCycle(12);
        
        // Government has 22 coins (low coins crisis)
        PartyState government = party("Tiger Front", PartyRole.GOVERNMENT, new PartyStats(22, 60, 10, 50, 36));
        PartyState opposition = party("Elephant Congress", PartyRole.OPPOSITION, new PartyStats(120, 55, 15, 50, 34));
        session.setGovernmentParty(government);

        // We offer:
        // 1. A welfare card that costs 6 coins but yields +20 coins (net change = +14 coins)
        CardDefinition welfareCard = card("gov_welfare_campaign", "positive_service", PartyRole.GOVERNMENT, 6, 1, 1, 0, 0);
        welfareCard.setVisibleEffects(Map.of(
            "selfParty", Map.of(
                "coins", 20
            )
        ));

        // 2. A pass card which costs 0 coins and gives 0 coins (net change = 0 coins)
        CardDefinition noCard = card("no_card", "governance", PartyRole.GOVERNMENT, 0, 0, 0, 0, 0);

        AiDecision decision = service.chooseCard(session, government, opposition, List.of(welfareCard, noCard));

        // AI should select the welfare campaign since it yields net coins in a coin crisis, bypassing safety penalties.
        assertEquals("gov_welfare_campaign", decision.card().getCardKey());
    }

    @Test
    void aiPlaysMoraleRestoringCardInMoraleCrisis() {
        GameSession session = new GameSession();
        session.setMonthInCycle(12);
        
        // Government has 20 morale (morale crisis)
        PartyState government = party("Tiger Front", PartyRole.GOVERNMENT, new PartyStats(100, 20, 10, 50, 36));
        PartyState opposition = party("Elephant Congress", PartyRole.OPPOSITION, new PartyStats(120, 55, 15, 50, 34));
        session.setGovernmentParty(government);

        // We offer a card that costs 0 but restores +10 morale, and a pass card (no morale boost)
        CardDefinition moraleRestore = card("gov_morale_rally", "positive_service", PartyRole.GOVERNMENT, 0, 0, 0, 0, 10);
        CardDefinition noCard = card("no_card", "governance", PartyRole.GOVERNMENT, 0, 0, 0, 0, 0);

        AiDecision decision = service.chooseCard(session, government, opposition, List.of(moraleRestore, noCard));

        // AI should select the morale restore card in morale crisis
        assertEquals("gov_morale_rally", decision.card().getCardKey());
    }
}
