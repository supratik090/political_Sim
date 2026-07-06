package com.politicalsim.game;

import com.politicalsim.ai.AiDecision;
import com.politicalsim.ai.AiDecisionService;
import com.politicalsim.api.TurnAdvanceRequest;
import com.politicalsim.content.CardDefinition;
import com.politicalsim.content.NewsDefinition;
import com.politicalsim.content.NewsReactionDefinition;
import com.politicalsim.party.PartyState;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

@Service
public class TurnTimerService {

    private static final Logger log = LoggerFactory.getLogger(TurnTimerService.class);

    private final GameSessionRepository repository;
    private final GameService gameService;
    private final AiDecisionService aiDecisionService;
    private final RoundResolutionEngine roundResolutionEngine;
    private final SimpMessagingTemplate messagingTemplate;

    public TurnTimerService(GameSessionRepository repository, GameService gameService,
                            AiDecisionService aiDecisionService, RoundResolutionEngine roundResolutionEngine,
                            SimpMessagingTemplate messagingTemplate) {
        this.repository = repository;
        this.gameService = gameService;
        this.aiDecisionService = aiDecisionService;
        this.roundResolutionEngine = roundResolutionEngine;
        this.messagingTemplate = messagingTemplate;
    }

    @Scheduled(fixedRate = 10000)
    public void checkTurnTimeouts() {
        List<GameSession> activeMultiplayerGames = repository.findByStatus(GameStatus.ACTIVE).stream()
                .filter(GameSession::isMultiplayer)
                .toList();

        LocalDateTime now = LocalDateTime.now();

        for (GameSession session : activeMultiplayerGames) {
            LocalDateTime turnStart = session.getTurnStartTime();
            Integer duration = session.getTurnDurationSeconds();
            
            if (turnStart != null && duration != null) {
                if (now.isAfter(turnStart.plusSeconds(duration))) {
                    handleTimeout(session);
                }
            }
        }
    }

    private void handleTimeout(GameSession session) {
        // Find the active human party
        if (session.getPlayerPartyIds().isEmpty()) {
            return;
        }
        
        int activeIndex = Math.min(session.getActiveHumanPlayerIndex(), session.getPlayerPartyIds().size() - 1);
        String activePartyId = session.getPlayerPartyIds().get(activeIndex);
        
        PartyState party = session.getParties().stream()
                .filter(p -> p.getId().equals(activePartyId))
                .findFirst()
                .orElse(null);

        if (party == null) return;

        log.info("Turn timed out for game {} player {}. Auto-generating move.", session.getId(), party.getName());

        TurnAdvanceRequest request = generateAutoMove(session, party);
        
        try {
            gameService.advanceTurn(session.getId(), request);
            messagingTemplate.convertAndSend("/topic/game/" + session.getId(), "TURN_ADVANCED");
        } catch (Exception e) {
            log.error("Failed to auto-advance turn for game " + session.getId(), e);
        }
    }

    private TurnAdvanceRequest generateAutoMove(GameSession session, PartyState party) {
        TurnAdvanceRequest request = new TurnAdvanceRequest();
        
        // 1. Choose Card
        PartyState opponent = aiDecisionService.chooseOpponent(session, party, null);
        List<CardDefinition> availableCards = gameService.getAvailableCardsForParty(session, party);
        AiDecision decision = aiDecisionService.chooseCard(session, party, opponent, availableCards);
        
        request.setSelectedCardKey(decision.card().getCardKey());
        
        if (decision.card().getTarget() != null && decision.card().getTarget().containsKey("opponentParty")) {
            PartyState target = aiDecisionService.chooseOpponent(session, party, decision.card());
            if (target != null) {
                request.setTargetPartyId(target.getId());
            }
        }
        
        // 2. Choose News Reactions
        List<NewsDefinition> currentNews = gameService.getCurrentNews(session);
        Map<String, String> reactions = new LinkedHashMap<>();
        for (NewsDefinition news : currentNews) {
            NewsReactionDefinition reaction = aiDecisionService.chooseReaction(party, decision.intent(), news.getReactionOptions());
            if (reaction != null) {
                reactions.put(news.getNewsKey(), reaction.getReactionKey());
            }
        }
        request.setSelectedNewsReactions(reactions);

        // 3. Choose Issue Option
        request.setSelectedIssueOptionKey("dummy_option");

        // 4. Bid
        String metric = roundResolutionEngine.getBiddingMetricForTurn(session.getTurnNumber());
        int bid = 0; // fallback safe bid for timeout
        request.setBid(bid);
        
        return request;
    }
}
