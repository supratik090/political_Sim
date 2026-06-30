package com.politicalsim.api;

import org.springframework.messaging.handler.annotation.DestinationVariable;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.stereotype.Controller;

@Controller
public class MultiplayerController {

    @MessageMapping("/chat/{gameId}")
    @SendTo("/topic/chat/{gameId}")
    public ChatMessage sendMessage(@DestinationVariable String gameId, ChatMessage message) {
        if (message.getTimestamp() == null) {
            message.setTimestamp(java.time.Instant.now().toString());
        }
        return message;
    }

    @MessageMapping("/lobby/{gameId}/update")
    @SendTo("/topic/lobby/{gameId}")
    public String triggerLobbyUpdate(@DestinationVariable String gameId, String updateMessage) {
        // Simple broadcast to tell clients in lobby to refresh
        return updateMessage;
    }

    @MessageMapping("/game/{gameId}/update")
    @SendTo("/topic/game/{gameId}")
    public String triggerGameUpdate(@DestinationVariable String gameId, String updateMessage) {
        // Broadcast game state changes
        return updateMessage;
    }
}
