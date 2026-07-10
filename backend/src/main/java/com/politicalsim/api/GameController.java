package com.politicalsim.api;

import com.politicalsim.game.GameNotFoundException;
import com.politicalsim.game.GameService;
import com.politicalsim.game.GameSession;
import jakarta.validation.Valid;

import java.util.Collections;
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
import org.springframework.beans.factory.annotation.Autowired;
import com.politicalsim.api.telemetry.LobbyTelemetryService;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/games")
public class GameController {

    private final GameService gameService;
    private final LobbyTelemetryService lobbyTelemetryService;

    @Autowired
    private com.politicalsim.content.LegislativeBillDefinitionRepository billRepository;

    @Autowired
    public GameController(GameService gameService, LobbyTelemetryService lobbyTelemetryService) {
        this.gameService = gameService;
        this.lobbyTelemetryService = lobbyTelemetryService;
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public GameSession createGame(@Valid @RequestBody CreateGameRequest request) {
        GameSession session = gameService.createGame(request);
        // Record lobby creation telemetry
//        lobbyTelemetryService.recordEvent(session.getId(), "LOBBY_CREATED", session.getJoinCode());
        return session;
    }

    @GetMapping("/{gameId}")
    public GameSession getGame(@PathVariable String gameId) {
        return gameService.getGame(gameId);
    }

    @GetMapping("/join-code/{joinCode}")
    public GameSession getGameByJoinCode(@PathVariable String joinCode) {
        return gameService.getGameByJoinCode(joinCode);
    }

    @PostMapping("/join")
    public GameSession joinGame(@RequestParam String userId, @RequestParam String joinCode, @RequestParam String partyId) {
        GameSession session = gameService.joinGame(userId, joinCode, partyId);
        // Record player join telemetry
//        lobbyTelemetryService.recordEvent(session.getId(), "PLAYER_JOINED", userId);
        return session;
    }

    @PostMapping("/{gameId}/start")
    public GameSession startGame(@PathVariable String gameId, @RequestParam(required = false) String userId) {
        return gameService.startGame(gameId, userId);
    }

    @GetMapping("/bills/scenario/{scenarioKey}")
    public List<com.politicalsim.content.LegislativeBillDefinition> getBillsByScenario(@PathVariable String scenarioKey) {
        List<com.politicalsim.content.LegislativeBillDefinition> list = billRepository.findByScenarioKey(scenarioKey);
        if (list.isEmpty()) {
            list = billRepository.findByScenarioKey("default");
        }
        return list;
    }



    @GetMapping
    public List<GameSession> listGames(@org.springframework.web.bind.annotation.RequestParam(required = false) String userId) {
        if (userId != null && !userId.isBlank() && !"null".equalsIgnoreCase(userId) && !"undefined".equalsIgnoreCase(userId)) {
            return gameService.listGames(userId.trim().toLowerCase());
        }
        return Collections.emptyList();
    }

    @GetMapping("/summaries")
    public List<GameSessionSummary> listGameSummaries(@RequestParam(required = false) String userId) {
        if (userId != null && !userId.isBlank() && !"null".equalsIgnoreCase(userId) && !"undefined".equalsIgnoreCase(userId)) {
            return gameService.listGameSummaries(userId.trim().toLowerCase());
        }
        return gameService.listGameSummaries();
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

    @PostMapping("/{gameId}/bribe")
    public TurnView bribeFaction(
            @PathVariable String gameId,
            @RequestParam String targetPartyId,
            @RequestParam String factionKey,
            @RequestParam int coins) {
        return gameService.bribeFaction(gameId, targetPartyId, factionKey, coins);
    }

    @GetMapping("/building-projects/definitions")
    public Map<com.politicalsim.party.BuildingProject, com.politicalsim.party.BuildingProject.ProjectConfig> getBuildingProjectDefinitions() {
        return com.politicalsim.party.BuildingProject.getConfigs();
    }
 
    @GetMapping("/posts/definitions")
    public List<com.politicalsim.party.PostsConfig.PostDefinition> getPostDefinitions() {
        return com.politicalsim.party.PostsConfig.ALL_POSTS;
    }

    /**
     * Immediately persists party management card allocations to MongoDB.
     * Called when the player clicks "Lock Allocations" in Action 3.
     * This replaces the localStorage-based submission approach with a direct API save.
     */
    @PostMapping("/{gameId}/party-management/lock")
    public com.politicalsim.party.PartyManagementState lockPartyManagement(
            @PathVariable String gameId,
            @RequestParam String partyId,
            @RequestBody PartyManagementLockRequest request) {
        return gameService.lockPartyManagement(gameId, partyId, request);
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
