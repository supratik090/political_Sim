import React, { useState } from 'react';
import { useGameStore } from '../../store/gameStore';
import { getGameByJoinCode, joinGameLobby } from '../../api/apiClient';

export default function JoinGame() {
    const { user, setScreen, setActiveGame } = useGameStore();
    const [joinCode, setJoinCode] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const [lobbyData, setLobbyData] = useState(null);
    const [selectedPartyId, setSelectedPartyId] = useState('');

    const handleFindLobby = async () => {
        if (!joinCode.trim()) {
            setError('Please enter a valid join code');
            return;
        }

        setLoading(true);
        setError('');
        try {
            const data = await getGameByJoinCode(joinCode);
            setLobbyData(data);
        } catch (err) {
            console.error(err);
            setError(err.message || 'Failed to find lobby. Make sure the code is correct.');
        } finally {
            setLoading(false);
        }
    };

    const handleJoin = async () => {
        if (!selectedPartyId) {
            setError('Please select a party');
            return;
        }
        
        setLoading(true);
        setError('');
        try {
            const data = await joinGameLobby(user.id || user.email, joinCode, selectedPartyId);
            setActiveGame(data.id);
            setScreen('LOBBY');
        } catch (err) {
            console.error(err);
            setError(err.message || 'Failed to join lobby.');
        } finally {
            setLoading(false);
        }
    };

    if (lobbyData) {
        return (
            <div className="unified-card">
                <h2 style={{ marginTop: 0 }}>Join Campaign: {lobbyData.scenarioName || lobbyData.scenarioKey}</h2>
                {error && <p style={{ color: 'red' }}>{error}</p>}
                
                <div style={{ marginTop: '20px' }}>
                    <p style={{ fontWeight: 'bold' }}>Select Your Party</p>
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                        {lobbyData.parties.map(p => {
                            const isClaimed = lobbyData.humanPlayerMap && lobbyData.humanPlayerMap[p.id];
                            return (
                                <div key={p.id} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '10px', border: '1px solid var(--primary-border)', borderRadius: '8px', opacity: isClaimed ? 0.6 : 1 }}>
                                    <div>
                                        <span style={{ fontWeight: 'bold' }}>{p.name}</span>
                                        {isClaimed && <span style={{ fontSize: '12px', color: 'red', marginLeft: '10px' }}>Already Claimed</span>}
                                    </div>
                                    <button 
                                        onClick={() => setSelectedPartyId(p.id)}
                                        disabled={isClaimed}
                                        style={{ backgroundColor: selectedPartyId === p.id ? 'var(--selected-highlight)' : '' }}
                                    >
                                        {selectedPartyId === p.id ? 'Selected' : 'Select'}
                                    </button>
                                </div>
                            );
                        })}
                    </div>
                </div>

                <div style={{ marginTop: '20px', display: 'flex', gap: '10px' }}>
                    <button onClick={handleJoin} disabled={loading || !selectedPartyId}>
                        {loading ? 'Joining...' : 'Confirm & Join'}
                    </button>
                    <button onClick={() => setLobbyData(null)} style={{ backgroundColor: 'transparent', color: 'var(--primary-dark)', border: '1px solid var(--primary-border)' }}>
                        Back
                    </button>
                </div>
            </div>
        );
    }

    return (
        <div className="unified-card">
            <h2 style={{ marginTop: 0 }}>Join Multiplayer Campaign</h2>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            
            <div style={{ marginTop: '20px', display: 'flex', flexDirection: 'column', gap: '15px', maxWidth: '300px' }}>
                <label style={{ fontWeight: 'bold' }}>Enter 6-Character Join Code</label>
                <input 
                    type="text" 
                    value={joinCode}
                    onChange={(e) => setJoinCode(e.target.value.toUpperCase())}
                    placeholder="e.g. A1B2C3"
                    maxLength={6}
                    style={{ padding: '10px', fontSize: '18px', textAlign: 'center', textTransform: 'uppercase', letterSpacing: '4px' }}
                />
                <button onClick={handleFindLobby} disabled={loading || joinCode.length !== 6}>
                    {loading ? 'Searching...' : 'Find Lobby'}
                </button>
                <button onClick={() => setScreen('HOME')} style={{ backgroundColor: 'transparent', color: 'var(--primary-dark)', border: '1px solid var(--primary-border)' }}>
                    Cancel
                </button>
            </div>
        </div>
    );
}
