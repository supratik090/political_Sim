package com.politicalsim.api.telemetry;

import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.Map;
import java.util.stream.Collectors;
import org.springframework.beans.factory.annotation.Autowired;

@RestController
public class TelemetryController {

    private final LobbyTelemetryService lobbyTelemetryService;
    private final ChatTelemetryService chatTelemetryService;

    @Autowired
    public TelemetryController(LobbyTelemetryService lobbyTelemetryService,
                               ChatTelemetryService chatTelemetryService) {
        this.lobbyTelemetryService = lobbyTelemetryService;
        this.chatTelemetryService = chatTelemetryService;
    }

    

    /** Lobby creation / player‑join telemetry */
    @GetMapping("/api/telemetry/lobby")
    public Map<String, Object> lobbyStats() {
        return Map.of(
                "totalLobbies", lobbyTelemetryService.countLobbies(),
                "totalJoins", lobbyTelemetryService.countJoins(),
                "recentEvents", lobbyTelemetryService.recentEvents()
        );
    }

    /** Chat persistence health */
    @GetMapping("/api/telemetry/chat")
    public Map<String, Object> chatStats() {
        return Map.of(
                "totalMessagesStored", chatTelemetryService.countMessages(),
                "messagesLast24h", chatTelemetryService.countMessagesLastHours(24)
        );
    }
}
