import React, { useState, useEffect, useMemo } from 'react';
import { useGameStore } from '../../store/gameStore';
import { listGames, fetchScenarioProgress, createGame, deleteGame } from '../../api/apiClient';
import { getPartyThemeByName } from '../../constants/partyThemes';

export default function DashboardHome() {
  const { user, setScreen, setActiveGame, currentScreen } = useGameStore();
  const [view, setView] = useState('TABLE'); // TABLE, CREATE, LOAD
  const [games, setGames] = useState([]);
  const [scenarios, setScenarios] = useState([]);
  const [allScenarios, setAllScenarios] = useState([]);
  const [selectedYear, setSelectedYear] = useState(2001);
  const [selectedStateName, setSelectedStateName] = useState(null);
  const [geoData, setGeoData] = useState(null);
  const [mapLoading, setMapLoading] = useState(true);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Selected scenario config state
  const [selectedScenarioIndex, setSelectedScenarioIndex] = useState(0);
  const [partyConfigs, setPartyConfigs] = useState([]);
  const [retainInstitutions, setRetainInstitutions] = useState(false);

  useEffect(() => {
    if (currentScreen === 'HOME') {
      loadDashboardData();
    }
  }, [user, currentScreen]);

  useEffect(() => {
    fetch('/india_states.geojson')
      .then(res => {
        if (!res.ok) throw new Error('Failed to load map data');
        return res.json();
      })
      .then(data => {
        setGeoData(data);
        setMapLoading(false);
      })
      .catch(err => {
        console.error(err);
        setMapLoading(false);
      });
  }, []);

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

      const allScenariosData = (progressData?.scenarios || [])
        .map(s => {
          const def = s.scenarioDefinition || {};
          return {
            ...def,
            id: def.id || s.scenarioKey,
            scenarioKey: s.scenarioKey,
            name: s.name || def.name,
            description: s.description || def.description,
            stateName: s.stateName || def.stateName,
            status: s.status,
            startYear: def.startDate ? parseInt(def.startDate.split('-')[0]) : 2001
          };
        });
      setAllScenarios(allScenariosData);
      setScenarios(allScenariosData.filter(s => s.status !== 'LOCKED'));
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
        retainInstitutions: retainInstitutions,
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

  const handleDeleteGame = async (gameId) => {
    const confirmed = window.confirm("Are you sure you want to delete this campaign? This action cannot be undone.");
    if (!confirmed) return;
    setLoading(true);
    try {
      await deleteGame(gameId);
      alert('Campaign deleted successfully.');
      await loadDashboardData();
    } catch (err) {
      console.error(err);
      alert('Failed to delete campaign: ' + err.message);
    } finally {
      setLoading(false);
    }
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

        {currentScenario?.scenarioKey?.endsWith('_2006') && (
          <div style={{ margin: '20px 0', display: 'flex', alignItems: 'center', gap: '10px', justifyContent: 'center' }}>
            <input 
              type="checkbox" 
              id="retainInstitutions"
              checked={retainInstitutions} 
              onChange={(e) => setRetainInstitutions(e.target.checked)} 
              style={{ width: 'auto', margin: 0 }}
            />
            <label htmlFor="retainInstitutions" style={{ fontWeight: 'bold', cursor: 'pointer', color: 'var(--primary-dark)' }}>
              Carry forward completed public institutions from previous campaign
            </label>
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

  const renderLoad = () => {
    const activeGames = games.filter(game => game.status === 'ACTIVE');
    return (
      <div className="unified-card">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h2 style={{ marginTop: 0 }}>Load Saved Campaign</h2>
          <button onClick={() => setView('TABLE')} style={{ backgroundColor: 'transparent', color: 'var(--primary-dark)', border: '1px solid var(--primary-border)' }}>Back</button>
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '15px', marginTop: '20px' }}>
          {activeGames.length === 0 && <p>No active saved games found.</p>}
          {activeGames.map(game => (
            <div key={game.id} style={{ border: '1px solid var(--primary-border)', padding: '15px', borderRadius: '8px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div>
                <h4 style={{ margin: '0 0 5px 0' }}>{game.scenarioName || game.scenarioKey}</h4>
                <span style={{ fontSize: '12px', color: 'var(--text-secondary)' }}>Status: {game.status} | Started: {formatDate(game.createdAt)}</span>
              </div>
              <div style={{ display: 'flex', gap: '10px' }}>
                <button onClick={() => handleLoadGame(game.id)}>Load Game</button>
                <button 
                  onClick={() => handleDeleteGame(game.id)} 
                  style={{ backgroundColor: '#D9534F', color: '#ffffff', border: 'none' }}
                >
                  🗑️ Delete
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    );
  };

  const getWinnerColorForScenario = (scenarioKey) => {
    const scenarioGames = games.filter(g => g.scenarioKey === scenarioKey);
    if (scenarioGames.length === 0) return null;

    const completedGames = scenarioGames.filter(g => g.status === 'VICTORY' || g.status === 'DEFEAT' || g.status === 'GAME_OVER');
    if (completedGames.length === 0) return null;

    completedGames.sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt));
    const latestGame = completedGames[0];

    let winnerName = null;
    if (latestGame.status === 'VICTORY') {
      const playerParty = latestGame.parties?.find(p => p.id === latestGame.playerPartyId);
      winnerName = playerParty ? playerParty.name : latestGame.lastElectionWinner;
    } else {
      winnerName = latestGame.lastElectionWinner;
    }

    if (winnerName) {
      const party = latestGame.parties?.find(p => p.name === winnerName);
      if (party && party.color) return party.color;
      return getPartyThemeByName(winnerName).color;
    }

    return null;
  };

  const projection = useMemo(() => {
    if (!geoData) return null;
    let minLng = 180, maxLng = -180, minLat = 90, maxLat = -90;
    geoData.features.forEach(feature => {
      if (feature.geometry) {
        const type = feature.geometry.type;
        const processCoord = (c) => {
          const lng = c[0];
          const lat = c[1];
          if (lng < minLng) minLng = lng;
          if (lng > maxLng) maxLng = lng;
          if (lat < minLat) minLat = lat;
          if (lat > maxLat) maxLat = lat;
        };
        if (type === 'Polygon') {
          feature.geometry.coordinates[0].forEach(processCoord);
        } else if (type === 'MultiPolygon') {
          feature.geometry.coordinates.forEach(poly => {
            poly[0].forEach(processCoord);
          });
        }
      }
    });

    const width = 500;
    const height = 550;
    const pad = 15;
    const innerW = width - 2 * pad;
    const innerH = height - 2 * pad;

    const lngDelta = maxLng - minLng;
    const latDelta = maxLat - minLat;
    const latToLngRatio = Math.cos(((minLat + maxLat) / 2) * Math.PI / 180);
    const scaleX = innerW / lngDelta;
    const scaleY = innerH / (latDelta / latToLngRatio);
    const scale = Math.min(scaleX, scaleY);

    const offsetX = pad + (innerW - lngDelta * scale) / 2;
    const offsetY = pad + (innerH - (latDelta / latToLngRatio) * scale) / 2;

    const project = ([lng, lat]) => {
      const x = offsetX + (lng - minLng) * scale;
      const y = height - (offsetY + (lat - minLat) * latToLngRatio * scale);
      return [x, y];
    };

    return { project, width, height };
  }, [geoData]);

  const getPathData = (geometry) => {
    if (!projection) return '';
    const { project } = projection;
    if (geometry.type === 'Polygon') {
      const points = geometry.coordinates[0].map(project).map(p => p.join(',')).join(' L ');
      return `M ${points} Z`;
    } else if (geometry.type === 'MultiPolygon') {
      return geometry.coordinates.map(poly => {
        const points = poly[0].map(project).map(p => p.join(',')).join(' L ');
        return `M ${points} Z`;
      }).join(' ');
    }
    return '';
  };

  const renderMapCard = () => {
    if (mapLoading) {
      return (
        <div className="unified-card" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '400px' }}>
          <span style={{ fontSize: '15px', color: 'var(--text-secondary)' }}>⌛ Loading India map boundaries...</span>
        </div>
      );
    }

    if (!geoData) {
      return (
        <div className="unified-card" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: '400px' }}>
          <span style={{ fontSize: '15px', color: 'red' }}>⚠️ Failed to load map data.</span>
        </div>
      );
    }

    return (
      <div className="unified-card" style={{ display: 'flex', flexDirection: 'column' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '15px', borderBottom: '1px solid var(--primary-border)', paddingBottom: '10px' }}>
          <h3 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--primary-dark)' }}>
            🗺️ India Campaign Map
          </h3>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span style={{ fontSize: '11px', fontWeight: '800', color: 'var(--text-secondary)' }}>ERA:</span>
            <select 
              value={selectedYear} 
              onChange={(e) => {
                setSelectedYear(parseInt(e.target.value));
                setSelectedStateName(null);
              }}
              style={{ width: 'auto', padding: '6px 12px', fontSize: '13px', borderRadius: '6px', fontWeight: 'bold' }}
            >
              <option value={2001}>2001 Era</option>
              <option value={2006}>2006 Era</option>
            </select>
          </div>
        </div>

        <div style={{ display: 'flex', justifyContent: 'center', position: 'relative', overflow: 'hidden', padding: '10px', backgroundColor: '#f8fafc', borderRadius: '8px', border: '1px solid var(--primary-border)' }}>
          <svg 
            width="100%" 
            height={projection?.height || 550} 
            viewBox={`0 0 ${projection?.width || 500} ${projection?.height || 550}`}
            style={{ maxWidth: '500px' }}
          >
            {geoData.features.map((feature, idx) => {
              const stateName = feature.properties.ST_NM;
              const scenario = allScenarios.find(s => 
                s.stateName?.toLowerCase() === stateName?.toLowerCase() && 
                s.startYear === selectedYear
              );
              
              let fillColor = '#f1f5f9';
              let strokeColor = '#94a3b8';
              let strokeWidth = '0.5px';
              let cursor = 'default';
              let winningColor = null;

              if (scenario) {
                if (scenario.status === 'LOCKED') {
                  fillColor = '#cbd5e1';
                } else if (scenario.status === 'AVAILABLE' || scenario.status === 'IN_PROGRESS') {
                  fillColor = '#22c55e';
                  cursor = 'pointer';
                } else if (scenario.status === 'WON') {
                  winningColor = getWinnerColorForScenario(scenario.scenarioKey);
                  fillColor = winningColor || '#3b82f6';
                  cursor = 'pointer';
                }
              }

              const isSelected = selectedStateName?.toLowerCase() === stateName?.toLowerCase();

              return (
                <path 
                  key={idx}
                  d={getPathData(feature.geometry)}
                  fill={fillColor}
                  stroke={isSelected ? '#0f172a' : strokeColor}
                  strokeWidth={isSelected ? '2px' : strokeWidth}
                  cursor={cursor}
                  onClick={() => {
                    if (scenario) {
                      setSelectedStateName(stateName);
                    }
                  }}
                  onMouseEnter={(e) => {
                    if (scenario) {
                      e.target.style.fillOpacity = '0.85';
                      if (!isSelected) {
                        e.target.style.stroke = '#213C51';
                        e.target.style.strokeWidth = '1px';
                      }
                    }
                  }}
                  onMouseLeave={(e) => {
                    e.target.style.fillOpacity = '1.0';
                    if (!isSelected) {
                      e.target.style.stroke = strokeColor;
                      e.target.style.strokeWidth = strokeWidth;
                    }
                  }}
                  style={{
                    transition: 'all 0.2s ease',
                  }}
                />
              );
            })}
          </svg>
        </div>

        {/* Legend */}
        <div style={{ display: 'flex', gap: '15px', justifyContent: 'center', marginTop: '15px', flexWrap: 'wrap', fontSize: '11px', fontWeight: 'bold', color: 'var(--primary-dark)' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
            <span style={{ width: '12px', height: '12px', backgroundColor: '#22c55e', borderRadius: '3px', border: '1px solid #94a3b8' }} />
            <span>Available / Active</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
            <span style={{ width: '12px', height: '12px', backgroundColor: '#3b82f6', borderRadius: '3px', border: '1px solid #94a3b8' }} />
            <span>Won (Party color)</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
            <span style={{ width: '12px', height: '12px', backgroundColor: '#cbd5e1', borderRadius: '3px', border: '1px solid #94a3b8' }} />
            <span>Locked</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
            <span style={{ width: '12px', height: '12px', backgroundColor: '#f1f5f9', borderRadius: '3px', border: '1px solid #94a3b8' }} />
            <span>No Campaign</span>
          </div>
        </div>

        {/* Details Panel */}
        {selectedStateName && (() => {
          const scenario = allScenarios.find(s => 
            s.stateName?.toLowerCase() === selectedStateName?.toLowerCase() && 
            s.startYear === selectedYear
          );
          if (!scenario) return null;

          const activeGame = games.find(g => g.scenarioKey === scenario.scenarioKey && g.status === 'ACTIVE');

          return (
            <div style={{
              marginTop: '20px',
              padding: '15px',
              borderRadius: '8px',
              border: '1.5px solid var(--primary-border)',
              backgroundColor: 'rgba(176, 203, 224, 0.1)',
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '8px' }}>
                <div>
                  <h4 style={{ margin: 0, color: 'var(--primary-dark)', fontSize: '16px', fontWeight: 900 }}>{scenario.stateName}</h4>
                  <span style={{ fontSize: '12px', color: 'var(--text-secondary)', fontWeight: 'bold' }}>{scenario.name}</span>
                </div>
                <span style={{
                  fontSize: '11px',
                  fontWeight: 'bold',
                  padding: '4px 8px',
                  borderRadius: '12px',
                  textTransform: 'uppercase',
                  backgroundColor: scenario.status === 'WON' ? '#dbeafe' : scenario.status === 'LOCKED' ? '#f1f5f9' : '#dcfce7',
                  color: scenario.status === 'WON' ? '#1e40af' : scenario.status === 'LOCKED' ? '#64748b' : '#15803d',
                  border: `1px solid ${scenario.status === 'WON' ? '#bfdbfe' : scenario.status === 'LOCKED' ? '#e2e8f0' : '#bbf7d0'}`
                }}>
                  {scenario.status === 'IN_PROGRESS' ? 'In Progress' : scenario.status}
                </span>
              </div>
              <p style={{ fontSize: '13px', margin: '0 0 15px 0', color: 'var(--text-secondary)', lineHeight: 1.4 }}>
                {scenario.description}
              </p>

              {scenario.status === 'WON' && (() => {
                const sGames = games.filter(g => g.scenarioKey === scenario.scenarioKey);
                const completed = sGames.filter(g => g.status === 'VICTORY' || g.status === 'DEFEAT' || g.status === 'GAME_OVER');
                completed.sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt));
                const latestCompleted = completed[0];
                
                let winnerText = 'N/A';
                let winnerColor = '#3b82f6';
                if (latestCompleted) {
                  if (latestCompleted.status === 'VICTORY') {
                    const playerParty = latestCompleted.parties?.find(p => p.id === latestCompleted.playerPartyId);
                    winnerText = playerParty ? `${playerParty.name} (You)` : latestCompleted.lastElectionWinner;
                  } else {
                    winnerText = latestCompleted.lastElectionWinner || 'Opposing Coalition';
                  }
                  winnerColor = getWinnerColorForScenario(scenario.scenarioKey) || '#3b82f6';
                }

                return (
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '15px', fontSize: '12px', fontWeight: 'bold', color: 'var(--primary-dark)' }}>
                    <span>🏆 Campaign Winner:</span>
                    <span style={{ display: 'inline-flex', alignItems: 'center', gap: '5px', color: winnerColor }}>
                      <span style={{ width: '8px', height: '8px', borderRadius: '50%', backgroundColor: winnerColor }} />
                      {winnerText}
                    </span>
                  </div>
                );
              })()}

              <div style={{ display: 'flex', gap: '10px' }}>
                {scenario.status !== 'LOCKED' && (
                  <button 
                    onClick={() => {
                      const idx = scenarios.findIndex(s => s.scenarioKey === scenario.scenarioKey);
                      if (idx !== -1) {
                        setSelectedScenarioIndex(idx);
                        setView('CREATE');
                      }
                    }}
                    style={{ fontSize: '12px', padding: '8px 15px' }}
                  >
                    {scenario.status === 'WON' ? '🔄 Replay Campaign' : '🎮 Start Campaign'}
                  </button>
                )}

                {activeGame && (
                  <button 
                    onClick={() => handleLoadGame(activeGame.id)}
                    style={{ fontSize: '12px', padding: '8px 15px', backgroundColor: 'var(--selected-highlight)', borderColor: 'var(--selected-highlight)' }}
                  >
                    📂 Resume Active Session
                  </button>
                )}
              </div>
            </div>
          );
        })()}
      </div>
    );
  };

  const renderDashboardGrid = () => (
    <div className="dashboard-grid" style={{
      display: 'grid',
      gridTemplateColumns: '1.2fr 1fr',
      gap: '24px',
      alignItems: 'start',
      marginTop: '10px'
    }}>
      {/* Map Column */}
      {renderMapCard()}

      {/* Campaigns list Column */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
        {renderTable()}
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

      {view === 'TABLE' && renderDashboardGrid()}
      {view === 'CREATE' && renderCreate()}
      {view === 'LOAD' && renderLoad()}
    </div>
  );
}
