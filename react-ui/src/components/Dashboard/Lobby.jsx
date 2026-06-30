import React, { useEffect, useState } from 'react';
import { useGameStore } from '../../store/gameStore';
import { getGame, startGame } from '../../api/apiClient';
import { useMultiplayer } from '../../hooks/useMultiplayer';

export default function Lobby() {
    const { user, activeGameId, setScreen } = useGameStore();
    const [gameData, setGameData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');
    const { isConnected, lobbyUpdateTick } = useMultiplayer(activeGameId, user?.id || user?.email, user?.name);

    const loadGame = async () => {
        try {
            const data = await getGame(activeGameId);
            setGameData(data);
            if (data.status === 'ACTIVE') {
                setScreen('GAME'); // Game started!
            }
        } catch (err) {
            console.error(err);
            setError('Failed to load lobby data');
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        loadGame();
    }, [activeGameId, lobbyUpdateTick]); // Reload when tick changes

    const handleStartGame = async () => {
        setLoading(true);
        try {
            await startGame(activeGameId, user.id || user.email);
            // This could trigger a LOBBY update so others start too
        } catch (err) {
            console.error(err);
            setError(err.message || 'Failed to start game');
            setLoading(false);
        }
    };

    if (loading && !gameData) {
        return <div className="unified-card">Loading lobby...</div>;
    }

    if (!gameData) {
        return <div className="unified-card">Lobby not found.</div>;
    }

    const isCreator = (user.id || user.email) === gameData.userId;
    const humanPlayers = Object.entries(gameData.humanPlayerMap || {}).map(([partyId, pUserId]) => {
        const party = gameData.parties.find(p => p.id === partyId);
        return {
            partyName: party?.name || 'Unknown Party',
            userId: pUserId
        };
    });

    return (
        <div className="unified-card" style={{ maxWidth: '600px', margin: '40px auto' }}>
            <h2 style={{ marginTop: 0, textAlign: 'center' }}>Multiplayer Lobby</h2>
            
            <div style={{ textAlign: 'center', marginBottom: '30px' }}>
                <span style={{ fontSize: '14px', color: 'var(--text-secondary)' }}>Share this code with your friends:</span>
                <h1 style={{ margin: '10px 0', fontSize: '48px', letterSpacing: '8px', color: 'var(--primary-dark)' }}>
                    {gameData.joinCode}
                </h1>
                <p style={{ fontWeight: 'bold' }}>Scenario: {gameData.scenarioName || gameData.scenarioKey}</p>
            </div>

            {error && <p style={{ color: 'red', textAlign: 'center' }}>{error}</p>}

            <div style={{ marginBottom: '30px' }}>
                <h3 style={{ borderBottom: '1px solid var(--primary-border)', paddingBottom: '10px' }}>
                    Players Joined ({humanPlayers.length} / {gameData.parties.length})
                </h3>
                
                {gameData.parties.map(p => {
                    const isClaimed = gameData.humanPlayerMap && gameData.humanPlayerMap[p.id];
                    const claimerId = gameData.humanPlayerMap?.[p.id];
                    const isMe = claimerId === (user.id || user.email);
                    
                    return (
                        <div key={p.id} style={{ display: 'flex', justifyContent: 'space-between', padding: '15px', borderBottom: '1px solid var(--primary-border)', backgroundColor: isMe ? 'rgba(59, 130, 246, 0.1)' : 'transparent' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                                <div style={{ width: '15px', height: '15px', backgroundColor: p.color || 'gray', borderRadius: '50%' }} />
                                <span style={{ fontWeight: 'bold', fontSize: '16px' }}>{p.name}</span>
                            </div>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                                {isClaimed ? (
                                    <span style={{ color: 'var(--accent-teal)', fontWeight: 'bold' }}>
                                        {isMe ? '👤 You (Ready)' : `👤 Player (${claimerId})`}
                                    </span>
                                ) : (
                                    <span style={{ color: 'var(--text-secondary)', fontStyle: 'italic' }}>
                                        🤖 AI (Waiting...)
                                    </span>
                                )}
                            </div>
                        </div>
                    );
                })}
            </div>

            <div style={{ display: 'flex', justifyContent: 'center', gap: '15px' }}>
                {isCreator ? (
                    <button onClick={handleStartGame} disabled={loading} style={{ padding: '15px 40px', fontSize: '18px' }}>
                        Start Game
                    </button>
                ) : (
                    <div style={{ padding: '15px', backgroundColor: 'rgba(0,0,0,0.05)', borderRadius: '8px', fontStyle: 'italic' }}>
                        Waiting for Host to start the game...
                    </div>
                )}
                
                <button onClick={() => setScreen('HOME')} style={{ backgroundColor: 'transparent', color: 'var(--primary-dark)', border: '1px solid var(--primary-border)' }}>
                    Leave Lobby
                </button>
            </div>
            
            <div style={{ textAlign: 'center', marginTop: '20px', fontSize: '12px', color: 'var(--text-secondary)' }}>
                Status: {isConnected ? '🟢 Connected to Server' : '🔴 Connecting...'}
            </div>
        </div>
    );
}
