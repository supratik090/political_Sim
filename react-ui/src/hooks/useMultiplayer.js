import { useState, useCallback } from 'react';

// Global toggle to completely disable multiplayer sockets
export const MULTIPLAYER_ENABLED = false;

/**
 * One-shot helper: connects to WS, sends a LOBBY_UPDATED event, then disconnects.
 * Used by JoinGame so the host's lobby refreshes when Player B joins.
 */
export function notifyLobbyJoined(gameId) {
    if (!MULTIPLAYER_ENABLED || !gameId) return;
}

export const useMultiplayer = (gameId, userId, userName, enabled = false) => {
    const [messages] = useState([]);
    const [isConnected] = useState(false);
    const [lobbyUpdateTick] = useState(0);
    const [gameUpdateTick] = useState(0);

    const sendMessage = useCallback(() => {}, []);
    const triggerLobbyUpdate = useCallback(() => {}, []);
    const triggerGameUpdate = useCallback(() => {}, []);

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
