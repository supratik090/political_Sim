import React, { useState, useEffect } from 'react';
import { useGameStore } from '../../store/gameStore';
import { listGames, fetchScenarioProgress, createGame } from '../../api/apiClient';

export default function DashboardHome() {
  const { user, setScreen, setActiveGame, currentScreen } = useGameStore();
  const [view, setView] = useState('TABLE'); // TABLE, CREATE, LOAD
  const [games, setGames] = useState([]);
  const [scenarios, setScenarios] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Selected scenario config state
  const [selectedScenarioIndex, setSelectedScenarioIndex] = useState(0);
  const [partyConfigs, setPartyConfigs] = useState([]);

  useEffect(() => {
    if (currentScreen === 'HOME') {
      loadDashboardData();
    }
  }, [user, currentScreen]);

  useEffect(() => {
    // When scenario changes, populate default parties
    if (scenarios.length > 0) {
      const scenario = scenarios[selectedScenarioIndex];
      if (scenario && scenario.politicalParties) {
        setPartyConfigs(scenario.politicalParties.map(p => {
          const defaultColor = p.startingRole === 'GOVERNMENT' ? '#E15554' : p.startingRole === 'OPPOSITION' ? '#3F88C5' : '#17B890';
          const defaultSymbol = p.startingRole === 'GOVERNMENT' ? 'Tiger' : p.startingRole === 'OPPOSITION' ? 'Elephant' : 'Peacock';
          return {
            partyKey: p.partyKey,
            name: p.name,
            controllerType: p.defaultControllerType,
            ideology: p.ideology,
            aiProfile: p.aiProfile ? p.aiProfile.style : '',
            role: p.startingRole,
            color: p.color || defaultColor,
            symbol: p.symbol || defaultSymbol,
            startingStats: p.startingStats
          };
        }));
      }
    }
  }, [selectedScenarioIndex, scenarios]);

  const loadDashboardData = async () => {
    setLoading(true);
    try {
      const [gamesData, progressData] = await Promise.all([
        listGames(user?.id || user?.email),
        fetchScenarioProgress(user?.id || user?.email)
      ]);
      setGames(gamesData);

      // Only show unlocked scenarios
      const unlockedScenarios = (progressData?.scenarios || [])
        .filter(s => s.status !== 'LOCKED')
        .map(s => {
          const def = s.scenarioDefinition || {};
          return {
            ...def,
            id: def.id || s.scenarioKey,
            scenarioKey: s.scenarioKey,
            name: s.name || def.name,
            description: s.description || def.description,
            stateName: s.stateName || def.stateName,
            status: s.status
          };
        });
      setScenarios(unlockedScenarios);
    } catch (err) {
      console.error(err);
      setError('Failed to fetch dashboard data from server.');
    } finally {
      setLoading(false);
    }
  };

  const handleStartNewGame = async () => {
    const scenario = scenarios[selectedScenarioIndex];
    if (!scenario) return;

    setLoading(true);
    try {
      const payload = {
        userId: user.id || user.email,
        scenarioKey: scenario.scenarioKey,
        partySetups: partyConfigs.map(config => ({
          partyKey: config.partyKey,
          partyName: config.name,
          role: config.role,
          controllerType: config.controllerType,
          color: config.color,
          symbol: config.symbol,
          ideology: config.ideology,
          aiProfile: config.controllerType === 'COMPUTER' ? { style: config.aiProfile || 'BALANCED_STRATEGIST' } : null,
          startingStats: config.startingStats
        }))
      };
      
      const gameData = await createGame(payload);
      setActiveGame(gameData.id);
      setScreen('GAME');
    } catch (err) {
      console.error(err);
      alert('Failed to create game. Check console for details.');
    } finally {
      setLoading(false);
    }
  };

  const handleLoadGame = (gameId) => {
    setActiveGame(gameId);
    setScreen('GAME');
  };

  const formatDate = (dateStr) => {
    if (!dateStr) return 'N/A';
    const d = new Date(dateStr);
    return isNaN(d.getTime()) ? 'N/A' : d.toLocaleDateString();
  };

  const updatePartyConfig = (index, field, value) => {
    const newConfigs = [...partyConfigs];
    newConfigs[index] = { ...newConfigs[index], [field]: value };
    setPartyConfigs(newConfigs);
  };

  const renderTable = () => (
    <div className="unified-card">
      <h2 style={{ marginTop: 0 }}>📊 Campaigns Status</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <table style={{ width: '100%', textAlign: 'left', borderCollapse: 'collapse', marginTop: '10px' }}>
        <thead>
          <tr style={{ borderBottom: '2px solid var(--primary-border)' }}>
            <th style={{ padding: '10px' }}>State Campaign</th>
            <th style={{ padding: '10px' }}>Status</th>
            <th style={{ padding: '10px' }}>Started At</th>
          </tr>
        </thead>
        <tbody>
          {games.length === 0 && !loading && (
            <tr><td colSpan="3" style={{ padding: '10px' }}>No campaigns found.</td></tr>
          )}
          {games.map(game => (
            <tr key={game.id} style={{ borderBottom: '1px solid rgba(101, 148, 177, 0.3)' }}>
              <td style={{ padding: '10px', fontWeight: 'bold' }}>{game.scenarioName || game.scenarioKey}</td>
              <td style={{ padding: '10px', color: game.status === 'COMPLETED' ? 'gray' : 'var(--selected-highlight)' }}>
                {game.status}
              </td>
              <td style={{ padding: '10px' }}>{formatDate(game.createdAt)}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <div style={{ display: 'flex', gap: '15px', marginTop: '30px', justifyContent: 'center' }}>
        <button onClick={() => setView('CREATE')} disabled={loading}>🎮 Create Campaign</button>
        <button onClick={() => setView('LOAD')} disabled={loading}>📂 Load Saved Campaign</button>
      </div>
    </div>
  );

  const renderCreate = () => {
    if (scenarios.length === 0) return <div className="unified-card">Loading scenarios...</div>;

    const currentScenario = scenarios[selectedScenarioIndex];

    return (
      <div className="unified-card">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h2 style={{ marginTop: 0 }}>Create New Campaign</h2>
          <button onClick={() => setView('TABLE')} style={{ backgroundColor: 'transparent', color: 'var(--primary-dark)', border: '1px solid var(--primary-border)' }}>Back</button>
        </div>

        <div style={{ marginBottom: '20px' }}>
          <label style={{ fontWeight: 'bold', display: 'block', marginBottom: '5px' }}>Select Scenario</label>
          <select 
            value={selectedScenarioIndex} 
            onChange={(e) => setSelectedScenarioIndex(parseInt(e.target.value))}
          >
            {scenarios.map((s, idx) => (
              <option key={s.id} value={idx}>{s.name} - "{s.description?.slice(0, 30)}..."</option>
            ))}
          </select>
        </div>

        {partyConfigs.length === 3 && (
          <div className="create-party-grid">
            {['Government', 'Opposition', 'Third Party'].map((role, idx) => (
              <div key={idx} style={{ border: '1px solid var(--primary-border)', padding: '15px', borderRadius: '8px' }}>
                <h4>Party {idx + 1} ({role})</h4>
                <input 
                  type="text" 
                  value={partyConfigs[idx].name} 
                  onChange={(e) => updatePartyConfig(idx, 'name', e.target.value)}
                  style={{ marginBottom: '10px' }} 
                />
                <select 
                  value={partyConfigs[idx].controllerType}
                  onChange={(e) => updatePartyConfig(idx, 'controllerType', e.target.value)}
                  style={{ marginBottom: '10px' }}
                >
                  <option value="HUMAN">Human Controller</option>
                  <option value="COMPUTER">AI</option>
                </select>
                {partyConfigs[idx].controllerType === 'COMPUTER' && (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                    <label style={{ fontSize: '11px', fontWeight: '800', opacity: 0.8, textTransform: 'uppercase' }}>AI Style Profile</label>
                    <select 
                      value={partyConfigs[idx].aiProfile || 'BALANCED_STRATEGIST'}
                      onChange={(e) => updatePartyConfig(idx, 'aiProfile', e.target.value)}
                    >
                      <option value="BALANCED_STRATEGIST">Balanced Strategist</option>
                      <option value="STRENGTH_BUILDER">Strength Builder</option>
                      <option value="AGGRESSIVE_ATTACKER">Aggressive Attacker</option>
                      <option value="LATE_STRIKER">Late Striker</option>
                      <option value="AGGRESSIVE_BIDDER">Aggressive Bidder</option>
                    </select>
                  </div>
                )}
              </div>
            ))}
          </div>
        )}

        <div style={{ marginTop: '30px', textAlign: 'center' }}>
          <button onClick={handleStartNewGame} disabled={loading} style={{ padding: '15px 40px', fontSize: '18px' }}>
            {loading ? 'Starting...' : 'Start Game'}
          </button>
        </div>
      </div>
    );
  };

  const renderLoad = () => (
    <div className="unified-card">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h2 style={{ marginTop: 0 }}>Load Saved Campaign</h2>
        <button onClick={() => setView('TABLE')} style={{ backgroundColor: 'transparent', color: 'var(--primary-dark)', border: '1px solid var(--primary-border)' }}>Back</button>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '15px', marginTop: '20px' }}>
        {games.length === 0 && <p>No saved games found.</p>}
        {games.map(game => (
          <div key={game.id} style={{ border: '1px solid var(--primary-border)', padding: '15px', borderRadius: '8px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div>
              <h4 style={{ margin: '0 0 5px 0' }}>{game.scenarioName || game.scenarioKey}</h4>
              <span style={{ fontSize: '12px', color: 'var(--text-secondary)' }}>Status: {game.status} | Started: {formatDate(game.createdAt)}</span>
            </div>
            <button onClick={() => handleLoadGame(game.id)}>Load Game</button>
          </div>
        ))}
      </div>
    </div>
  );

  return (
    <div>
      <div style={{
        background: 'var(--primary-border)',
        padding: '30px',
        borderRadius: '16px',
        border: '2px solid var(--primary-dark)',
        marginBottom: '25px',
        textAlign: 'center',
        color: '#ffffff',
        boxShadow: '0 10px 30px rgba(33,60,81,0.1)'
      }}>
        <h1 style={{ fontSize: '36px', fontWeight: 900, margin: 0, letterSpacing: '-0.02em', color: '#ffffff' }}>
          Dashboard
        </h1>
        <p style={{ fontSize: '15px', marginTop: '8px', opacity: 0.95, color: '#ffffff' }}>
          Select a campaign to manage or start a new political journey.
        </p>
      </div>

      {view === 'TABLE' && renderTable()}
      {view === 'CREATE' && renderCreate()}
      {view === 'LOAD' && renderLoad()}
    </div>
  );
}
