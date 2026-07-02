import { useEffect, useState, useRef, useCallback } from 'react';
import { Client } from '@stomp/stompjs';
import SockJS from 'sockjs-client';

const WEBSOCKET_URL = import.meta.env.VITE_API_BASE_URL?.replace('/api', '/ws-game') || 'http://localhost:7810/ws-game';

/**
 * One-shot helper: connects to WS, sends a LOBBY_UPDATED event, then disconnects.
 * Used by JoinGame so the host's lobby refreshes when Player B joins.
 */
export function notifyLobbyJoined(gameId) {
    const client = new Client({
        webSocketFactory: () => { const sock = new SockJS(WEBSOCKET_URL); sock.withCredentials = true; return sock; },
        reconnectDelay: 0,
    });
    client.onConnect = () => {
        client.publish({
            destination: `/app/lobby/${gameId}/update`,
            body: 'PLAYER_JOINED',
        });
        setTimeout(() => client.deactivate(), 500);
    };
    client.activate();
}



export const useMultiplayer = (gameId, userId, userName) => {
    const [messages, setMessages] = useState([]);
    const [isConnected, setIsConnected] = useState(false);
    const clientRef = useRef(null);
    const [lobbyUpdateTick, setLobbyUpdateTick] = useState(0);
    const [gameUpdateTick, setGameUpdateTick] = useState(0);

    useEffect(() => {
        if (!gameId) return;

        const client = new Client({
            webSocketFactory: () => { const sock = new SockJS(WEBSOCKET_URL); sock.withCredentials = true; return sock; },
            reconnectDelay: 5000,
            heartbeatIncoming: 4000,
            heartbeatOutgoing: 4000,
        });

        client.onConnect = () => {
            setIsConnected(true);

            // Subscribe to chat
            client.subscribe(`/topic/chat/${gameId}`, (message) => {
                if (message.body) {
                    const parsedMessage = JSON.parse(message.body);
                    setMessages((prev) => [...prev, parsedMessage]);
                }
            });

            // Subscribe to lobby updates
            client.subscribe(`/topic/lobby/${gameId}`, (message) => {
                setLobbyUpdateTick((prev) => prev + 1);
            });

            // Subscribe to game updates
            client.subscribe(`/topic/game/${gameId}`, (message) => {
                setGameUpdateTick((prev) => prev + 1);
            });
        };

        client.onStompError = (frame) => {
            console.error('Broker reported error: ' + frame.headers['message']);
            console.error('Additional details: ' + frame.body);
        };

        client.activate();
        clientRef.current = client;

        return () => {
            client.deactivate();
            setIsConnected(false);
        };
    }, [gameId]);

    const sendMessage = useCallback((text) => {
        if (clientRef.current && clientRef.current.connected) {
            clientRef.current.publish({
                destination: `/app/chat/${gameId}`,
                body: JSON.stringify({
                    senderId: userId,
                    senderName: userName || userId,
                    text: text
                }),
            });
        }
    }, [gameId, userId, userName]);

    const triggerLobbyUpdate = useCallback(() => {
        if (clientRef.current && clientRef.current.connected) {
            clientRef.current.publish({
                destination: `/app/lobby/${gameId}/update`,
                body: "LOBBY_UPDATED",
            });
        }
    }, [gameId]);

    const triggerGameUpdate = useCallback(() => {
        if (clientRef.current && clientRef.current.connected) {
            clientRef.current.publish({
                destination: `/app/game/${gameId}/update`,
                body: "GAME_UPDATED",
            });
        }
    }, [gameId]);

    return {
        isConnected,
        messages,
        sendMessage,
        triggerLobbyUpdate,
        triggerGameUpdate,
        lobbyUpdateTick,
        gameUpdateTick
    };
};
