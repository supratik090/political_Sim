package com.politicalsim.api.v2;

import com.politicalsim.game.GameService;
import com.politicalsim.game.GameSession;
import com.politicalsim.game.RoundResolutionEngine;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;

import java.util.LinkedHashMap;
import java.util.Map;

/**
 * V2 Feedback API Controller.
 * Provides versioned endpoints for locked instant feedback matching backend calculations.
 * Fully backward-compatible with existing /api/games endpoints.
 */
@RestController
@RequestMapping("/api/v2/games/{gameId}/feedback")
public class GameFeedbackV2Controller {

    private final GameService gameService;
    private final RoundResolutionEngine roundResolutionEngine;

    @Autowired
    public GameFeedbackV2Controller(GameService gameService, RoundResolutionEngine roundResolutionEngine) {
        this.gameService = gameService;
        this.roundResolutionEngine = roundResolutionEngine;
    }

    @PostMapping("/news")
    public NewsFeedbackResponse getNewsFeedback(
            @PathVariable String gameId,
            @RequestBody NewsFeedbackRequest request) {
        GameSession session = gameService.getGame(gameId);
        if (session == null) {
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Game session not found: " + gameId);
        }
        if (request.getNewsKey() == null || request.getReactionKey() == null) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "newsKey and reactionKey are required");
        }
        String partyId = request.getPartyId();
        if (partyId == null || partyId.isBlank()) {
            partyId = session.getPlayerPartyId();
        }
        return roundResolutionEngine.evaluateNewsFeedback(session, partyId, request.getNewsKey(), request.getReactionKey());
    }

    @PostMapping("/news/batch")
    public Map<String, NewsFeedbackResponse> getBatchNewsFeedback(
            @PathVariable String gameId,
            @RequestBody BatchNewsFeedbackRequest request) {
        GameSession session = gameService.getGame(gameId);
        if (session == null) {
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Game session not found: " + gameId);
        }
        String partyId = request.getPartyId();
        if (partyId == null || partyId.isBlank()) {
            partyId = session.getPlayerPartyId();
        }

        Map<String, NewsFeedbackResponse> results = new LinkedHashMap<>();
        if (request.getSelectedNewsReactions() != null) {
            for (Map.Entry<String, String> entry : request.getSelectedNewsReactions().entrySet()) {
                NewsFeedbackResponse res = roundResolutionEngine.evaluateNewsFeedback(session, partyId, entry.getKey(), entry.getValue());
                results.put(entry.getKey(), res);
            }
        }
        return results;
    }

    @PostMapping("/card")
    public CardFeedbackResponse getCardFeedback(
            @PathVariable String gameId,
            @RequestBody CardFeedbackRequest request) {
        GameSession session = gameService.getGame(gameId);
        if (session == null) {
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Game session not found: " + gameId);
        }
        if (request.getCardKey() == null || request.getCardKey().isBlank()) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "cardKey is required");
        }
        String partyId = request.getPartyId();
        if (partyId == null || partyId.isBlank()) {
            partyId = session.getPlayerPartyId();
        }
        return roundResolutionEngine.evaluateCardFeedback(session, partyId, request.getCardKey(), request.getTargetPartyId());
    }

    @GetMapping("/turn-cache")
    public TurnFeedbackCacheResponse getTurnFeedbackCache(
            @PathVariable String gameId,
            @RequestParam(required = false) String partyId) {
        GameSession session = gameService.getGame(gameId);
        if (session == null) {
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Game session not found: " + gameId);
        }
        if (partyId == null || partyId.isBlank()) {
            partyId = session.getPlayerPartyId();
        }
        return roundResolutionEngine.evaluateTurnFeedbackCache(session, partyId);
    }
}
