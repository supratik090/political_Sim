package com.politicalsim.config;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.messaging.simp.config.MessageBrokerRegistry;
import org.springframework.web.socket.config.annotation.EnableWebSocketMessageBroker;
import org.springframework.web.socket.config.annotation.WebSocketMessageBrokerConfigurer;
import org.springframework.web.socket.config.annotation.StompEndpointRegistry;

@Configuration
@EnableWebSocketMessageBroker
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {

    // Same env var as SecurityConfig — comma-separated list of allowed origins
    @Value("${allowed.origins:http://localhost:5173,http://localhost:3000,https://political-sim-mu.vercel.app}")
    private String allowedOriginsRaw;

    @Override
    public void configureMessageBroker(MessageBrokerRegistry config) {
        // Use /topic for broadcasting to clients
        config.enableSimpleBroker("/topic");
        // Use /app for messages bound for @MessageMapping methods
        config.setApplicationDestinationPrefixes("/app");
    }

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        // Split the env var and apply to STOMP/SockJS endpoint
        String[] origins = allowedOriginsRaw.split(",");
        for (int i = 0; i < origins.length; i++) {
            origins[i] = origins[i].trim();
        }
        registry.addEndpoint("/ws-game")
                .setAllowedOriginPatterns(origins)
                .withSockJS();
    }
}
