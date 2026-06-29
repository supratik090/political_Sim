package com.politicalsim.api;

import com.politicalsim.game.GameNotFoundException;
import com.politicalsim.game.GameService;
import com.politicalsim.game.GameSession;
import jakarta.validation.Valid;
import java.util.List;
import java.util.Map;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/games")
public class GameController {

    private final GameService gameService;

    public GameController(GameService gameService) {
        this.gameService = gameService;
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public GameSession createGame(@Valid @RequestBody CreateGameRequest request) {
        return gameService.createGame(request);
    }

    @GetMapping("/{gameId}")
    public GameSession getGame(@PathVariable String gameId) {
        return gameService.getGame(gameId);
    }

    @GetMapping
    public List<GameSession> listGames(@org.springframework.web.bind.annotation.RequestParam(required = false) String userId) {
        if (userId != null && !userId.isBlank()) {
            return gameService.listGames(userId);
        }
        return gameService.listGames();
    }

    @GetMapping("/{gameId}/turn-view")
    public TurnView getTurnView(@PathVariable String gameId) {
        return gameService.getTurnView(gameId);
    }

    @PostMapping("/{gameId}/turn/advance")
    public TurnView advanceTurn(@PathVariable String gameId, @RequestBody TurnAdvanceRequest request) {
        return gameService.advanceTurn(gameId, request);
    }

    @PostMapping("/{gameId}/forfeit")
    public GameSession forfeitGame(@PathVariable String gameId) {
        return gameService.forfeitGame(gameId);
    }

    @DeleteMapping("/{gameId}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void deleteGame(@PathVariable String gameId) {
        gameService.deleteGame(gameId);
    }

    @PostMapping("/{gameId}/parties/{partyId}/projects/fund")
    public TurnView fundProject(
            @PathVariable String gameId,
            @PathVariable String partyId,
            @RequestParam String projectKey,
            @RequestParam int progress) {
        return gameService.fundProject(gameId, partyId, projectKey, progress);
    }

    @PostMapping("/{gameId}/parties/{partyId}/projects/destroy")
    public TurnView destroyProject(
            @PathVariable String gameId,
            @PathVariable String partyId,
            @RequestParam String projectKey) {
        return gameService.destroyProject(gameId, partyId, projectKey);
    }

    @PostMapping("/{gameId}/parties/{partyId}/projects/{projectKey}/target")
    public TurnView setProjectTarget(
            @PathVariable String gameId,
            @PathVariable String partyId,
            @PathVariable String projectKey,
            @RequestParam String targetPartyId) {
        return gameService.setProjectTarget(gameId, partyId, projectKey, targetPartyId);
    }

    @PostMapping("/{gameId}/cooperation/offer")
    public TurnView createCooperationOffer(
            @PathVariable String gameId,
            @RequestBody com.politicalsim.game.CooperationOffer offer) {
        return gameService.createCooperationOffer(gameId, offer);
    }

    @PostMapping("/{gameId}/cooperation/respond")
    public TurnView respondToCooperationOffer(
            @PathVariable String gameId,
            @RequestParam String offerId,
            @RequestParam boolean accept) {
        return gameService.respondToCooperationOffer(gameId, offerId, accept);
    }

    @GetMapping("/building-projects/definitions")
    public Map<com.politicalsim.party.BuildingProject, com.politicalsim.party.BuildingProject.ProjectConfig> getBuildingProjectDefinitions() {
        return com.politicalsim.party.BuildingProject.getConfigs();
    }

    @ExceptionHandler(GameNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public Map<String, String> handleGameNotFound(GameNotFoundException exception) {
        return Map.of("error", exception.getMessage());
    }

    @ExceptionHandler(IllegalArgumentException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public Map<String, String> handleBadRequest(IllegalArgumentException exception) {
        return Map.of("error", exception.getMessage());
    }
}
