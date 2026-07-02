package com.politicalsim.api.telemetry;

import org.springframework.stereotype.Service;
import java.time.Instant;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Map;

@Service
public class LobbyTelemetryService {
    private int totalLobbies = 0;
    private int totalJoins = 0;
    private final Deque<Map<String, Object>> recentEvents = new ArrayDeque<>();
    private static final int MAX_EVENTS = 100;

    public void recordEvent(String gameId, String eventType, String detail) {
        if ("LOBBY_CREATED".equals(eventType)) {
            totalLobbies++;
        } else if ("PLAYER_JOINED".equals(eventType)) {
            totalJoins++;
        }
        recentEvents.addLast(Map.of(
                "timestamp", Instant.now().toString(),
                "gameId", gameId,
                "event", eventType,
                "detail", detail
        ));
        if (recentEvents.size() > MAX_EVENTS) {
            recentEvents.removeFirst();
        }
    }

    public int countLobbies() { return totalLobbies; }
    public int countJoins() { return totalJoins; }
    public Deque<Map<String, Object>> recentEvents() { return recentEvents; }
}
