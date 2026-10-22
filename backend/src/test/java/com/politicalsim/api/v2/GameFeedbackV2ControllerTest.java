package com.politicalsim.api.v2;

import com.politicalsim.content.CardDefinition;
import com.politicalsim.content.NewsDefinition;
import com.politicalsim.content.NewsReactionDefinition;
import com.politicalsim.game.GameSession;
import com.politicalsim.game.RoundResolutionEngine;
import com.politicalsim.party.PartyRole;
import com.politicalsim.party.PartyState;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

public class GameFeedbackV2ControllerTest {

    private RoundResolutionEngine engine;
    private GameSession session;
    private PartyState party;

    @BeforeEach
    public void setup() {
        engine = new RoundResolutionEngine(null, null, null);

        session = new GameSession();
        session.setId("test_game_123");
        session.setTurnNumber(1);

        party = new PartyState();
        party.setId("party_a");
        party.setName("Party A");
        party.setRole(PartyRole.GOVERNMENT);
        session.setParties(List.of(party));
        session.setPlayerPartyId("party_a");
    }

    @Test
    public void testNewsFeedbackResolution() {
        NewsDefinition news = new NewsDefinition();
        news.setNewsKey("economic_crisis");
        news.setTitle("Economic Slump");

        NewsReactionDefinition reaction = new NewsReactionDefinition();
        reaction.setReactionKey("relief_package");
        reaction.setText("Announce immediate stimulus");
        reaction.setWeight(3);
        reaction.setEffects(Map.of("playerParty", Map.of("coins", 5, "publicSupport", 2)));
        reaction.setRisk(Map.of("chance", 0)); // deterministic no backfire
        news.setReactionOptions(List.of(reaction));

        session.setGameIssues(List.of(news));

        NewsFeedbackResponse response = engine.evaluateNewsFeedback(session, "party_a", "economic_crisis", "relief_package");
        assertNotNull(response);
        assertEquals("economic_crisis", response.getNewsKey());
        assertEquals("relief_package", response.getReactionKey());
        assertFalse(response.isBackfired());
        assertEquals("🎉 PUBLIC RESONANCE", response.getHeadline());
        assertNotNull(response.getNetDeltas());
        assertTrue(response.getNetDeltas().get("publicSupport") >= 2);
    }

    @Test
    public void testCardFeedbackResolution() {
        CardDefinition card = new CardDefinition();
        card.setCardKey("rally_workers");
        card.setName("Workers Rally");
        card.setCost(5);
        card.setActive(true);
        card.setRoleAllowed(List.of("GOVERNMENT", "ALL"));
        card.setVisibleEffects(Map.of("selfParty", Map.of("partyMorale", 4, "publicSupport", 3)));
        card.setRiskRoll(Map.of("chance", 0));
        session.setGameCards(List.of(card));

        CardFeedbackResponse response = engine.evaluateCardFeedback(session, "party_a", "rally_workers", null);
        assertNotNull(response);
        assertEquals("rally_workers", response.getCardKey());
        assertEquals(5, response.getCost());
        assertFalse(response.isBackfired());
        assertEquals("⚡ TACTICAL HIT", response.getHeadline());
        assertEquals(4, response.getSelfDeltas().get("partyMorale"));
        assertEquals(3, response.getSelfDeltas().get("publicSupport"));
    }

    @Test
    public void testTurnFeedbackCacheResolution() {
        NewsDefinition news = new NewsDefinition();
        news.setNewsKey("economic_crisis");
        news.setTitle("Economic Slump");
        NewsReactionDefinition reaction = new NewsReactionDefinition();
        reaction.setReactionKey("relief_package");
        reaction.setText("Announce immediate stimulus");
        reaction.setWeight(3);
        reaction.setEffects(Map.of("playerParty", Map.of("coins", 5, "publicSupport", 2)));
        reaction.setRisk(Map.of("chance", 0));
        news.setReactionOptions(List.of(reaction));
        session.setGameIssues(List.of(news));

        CardDefinition card = new CardDefinition();
        card.setCardKey("rally_workers");
        card.setName("Workers Rally");
        card.setCost(5);
        card.setActive(true);
        card.setRoleAllowed(List.of("GOVERNMENT", "ALL"));
        card.setVisibleEffects(Map.of("selfParty", Map.of("partyMorale", 4, "publicSupport", 3)));
        card.setRiskRoll(Map.of("chance", 0));
        session.setGameCards(List.of(card));

        TurnFeedbackCacheResponse cache = engine.evaluateTurnFeedbackCache(session, "party_a");
        assertNotNull(cache);
        assertEquals(1, cache.getTurnNumber());
        assertEquals("party_a", cache.getPartyId());
        assertTrue(cache.getNews().containsKey("economic_crisis:relief_package"));
        assertTrue(cache.getCards().containsKey("rally_workers:none"));
    }
}
