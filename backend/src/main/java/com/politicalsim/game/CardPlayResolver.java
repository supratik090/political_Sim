package com.politicalsim.game;

import com.politicalsim.content.CardDefinition;
import com.politicalsim.party.PartyState;
import java.util.List;
import java.util.Map;

public class CardPlayResolver {
    private final RoundResolutionEngine engine;

    public CardPlayResolver(RoundResolutionEngine engine) {
        this.engine = engine;
    }

    public boolean resolveCardPlays(GameSession session, Map<String, Integer> supportPressure, List<String> commentary, List<String> resultLines) {
        return resolveCardPlays(session, supportPressure, null, commentary, resultLines);
    }

    public boolean resolveCardPlays(GameSession session, Map<String, Integer> supportPressure, Map<String, Integer> directSupportChanges, List<String> commentary, List<String> resultLines) {
        boolean noConfidencePlayed = false;
        for (RoundSubmission submission : session.getCurrentRoundSubmissions()) {
            PartyState actor = engine.findParty(session, submission.getPartyId());
            if (actor.getRole() == com.politicalsim.party.PartyRole.DEFEATED) {
                continue;
            }
            PartyState opponent = engine.resolveSubmittedTarget(session, actor, submission);
            CardDefinition card = engine.findCard(session, submission.getCardKey(), actor.getRole());
            if (engine.isNoConfidenceCard(card)) {
                noConfidencePlayed = true;
            }
            engine.incrementCardUsage(session, actor, card);
            engine.applyCard(session, actor, opponent, card, supportPressure, directSupportChanges, commentary);
            engine.scheduleCardDelayedEffects(session, actor, opponent, card, commentary);
            
            String cardEffects = "Effects: self(" + engine.formatEffectsObject(card.getVisibleEffects(), "selfParty") + ")";
            if (opponent != null) {
                cardEffects += ", target " + opponent.getName() + "(" + engine.formatEffectsObject(card.getVisibleEffects(), "opponentParty") + ")";
            }

            if (submission.getAiDecisionBasis() != null && !submission.getAiDecisionBasis().isBlank()) {
                commentary.add("🤖 AI Decision Analysis: " + submission.getAiDecisionBasis());
            }

            if (submission.getAiIntent() == null || submission.getAiIntent().isBlank()) {
                commentary.add(actor.getName() + " played " + card.getName() + engine.targetPhrase(opponent) + ". " + cardEffects);
            } else {
                commentary.add(actor.getName() + " chose " + card.getName() + engine.targetPhrase(opponent)
                        + " with intent " + submission.getAiIntent() + ". " + cardEffects);
            }
            resultLines.add(actor.getName() + " played card: " + card.getName());

            int coinAward = engine.resolveNewsReactions(session, actor, submission.getNewsReactions(), supportPressure, directSupportChanges, commentary);
            commentary.add("💰 News Reward: " + actor.getName() + " gained +" + coinAward + " coins from news handling (Reserves: " + actor.getStats().getCoins() + ").");
        }
        return noConfidencePlayed;
    }
}
