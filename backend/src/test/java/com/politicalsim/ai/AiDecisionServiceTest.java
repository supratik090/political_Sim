package com.politicalsim.ai;

import static org.junit.jupiter.api.Assertions.assertEquals;

import com.politicalsim.content.CardDefinition;
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
}
