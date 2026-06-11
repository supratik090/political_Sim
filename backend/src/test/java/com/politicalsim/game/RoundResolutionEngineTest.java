package com.politicalsim.game;

import static org.junit.jupiter.api.Assertions.assertEquals;

import com.politicalsim.party.ControllerType;
import com.politicalsim.party.Ideology;
import com.politicalsim.party.PartyRole;
import com.politicalsim.party.PartyState;
import com.politicalsim.party.PartyStats;
import com.politicalsim.publicmood.PublicState;
import java.util.ArrayList;
import java.util.List;
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
                "reward_rally_8_support",
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
                "reward_rally_8_support",
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
}
