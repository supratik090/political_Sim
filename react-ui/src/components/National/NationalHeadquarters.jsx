import React, { useState, useEffect, useMemo } from 'react';
import { useGameStore } from '../../store/gameStore';
import { fetchNationalConfigs, startNationalGame } from '../../api/apiClient';
import NationalWarRoomView from './WarRoom/NationalWarRoomView';

import SelectMode, { GAME_MODES } from './selectMode';

// War Room Theme Colors & Utilities
const ALLIANCE_COLORS = {
  NDA: '#f97316',
  INC: '#38bdf8',
  LEFT: '#ef4444',
  INDEPENDENT: '#a855f7',
  OTHERS: '#64748b'
};

export default function NationalHeadquarters() {
  const {
    setScreen,
    activeNationalGame,
    setActiveNationalGame,
    clearActiveNationalGame,
    nationalView,
    setNationalView,
    setActiveNationalTab
  } = useGameStore();

  // Navigation & Flow State: 'HEADQUARTERS', 'CREATE_GAME', or 'WAR_ROOM'
  const view = nationalView || 'HEADQUARTERS';
  const setView = setNationalView;

  // National Configs & Era Selection
  const [configs, setConfigs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [selectedEra, setSelectedEra] = useState(2001);
  const [selectedGameMode, setSelectedGameMode] = useState('PM_POWER');
  const [selectedPartyKey, setSelectedPartyKey] = useState('ydp');

  // Confirmation Modal State
  const [showConfirmModal, setShowConfirmModal] = useState(false);

  // Fetch National Configs on Mount
  useEffect(() => {
    loadConfigs();
  }, []);

  const loadConfigs = async () => {
    setLoading(true);
    try {
      const data = await fetchNationalConfigs();
      if (Array.isArray(data) && data.length > 0) {
        setConfigs(data);
        // Default to 2001 era or first available config
        const found2001 = data.find(c => c.era === 2001) || data[0];
        setSelectedEra(found2001.era);
      }
    } catch (err) {
      console.warn('Could not fetch remote national configs, using local fallback:', err);
    } finally {
      setLoading(false);
    }
  };

  // Currently active Era Config Object
  const currentConfig = useMemo(() => {
    return configs.find(c => c.era === selectedEra) || null;
  }, [configs, selectedEra]);

  // Aggregate Lok Sabha Seat Totals per Party Key from stateSeatData
  const partySeatTotalsMap = useMemo(() => {
    const totals = {};
    if (currentConfig && Array.isArray(currentConfig.stateSeatData)) {
      currentConfig.stateSeatData.forEach(state => {
        if (state.initialSeats) {
          Object.entries(state.initialSeats).forEach(([pKey, seats]) => {
            totals[pKey] = (totals[pKey] || 0) + (seats || 0);
          });
        }
      });
    }
    return totals;
  }, [currentConfig]);

  // Selectable Parties List (YDP sorted FIRST with Recommended Badge)
  const selectableParties = useMemo(() => {
    if (!currentConfig || !Array.isArray(currentConfig.parties)) return [];

    const filtered = currentConfig.parties.filter(p => p.isPlayerSelectable !== false);

    // Ensure YDP is first
    const ydpParty = filtered.find(p => p.partyKey === 'ydp');
    const otherParties = filtered.filter(p => p.partyKey !== 'ydp');

    return ydpParty ? [ydpParty, ...otherParties] : filtered;
  }, [currentConfig]);

  // Active selected party object
  const selectedParty = useMemo(() => {
    return selectableParties.find(p => p.partyKey === selectedPartyKey) || selectableParties[0] || null;
  }, [selectableParties, selectedPartyKey]);

  // Launch Game Handler
  const handleConfirmLaunchGame = async () => {
    if (!selectedParty || !currentConfig) return;

    const seats = partySeatTotalsMap[selectedParty.partyKey] || 0;
    const morale = selectedParty.initialMorale || selectedParty.initialContent || 80;

    const activeModeObj = GAME_MODES.find(m => m.id === selectedGameMode) || GAME_MODES[0];

    // Clear any previous active national game cache so new game starts completely clean
    if (clearActiveNationalGame) {
      clearActiveNationalGame();
    }

    // Base game data for localStorage fallback
    const localGameData = {
      era: currentConfig.era,
      eraTitle: currentConfig.title,
      gameMode: selectedGameMode,
      gameModeTitle: activeModeObj.title,
      gameModeShortTitle: activeModeObj.shortTitle,
      partyKey: selectedParty.partyKey,
      partyName: selectedParty.name,
      partyShortName: selectedParty.shortName,
      partyColor: selectedParty.color || '#7C3AED',
      allianceKey: selectedParty.initialAllianceKey || 'INDEPENDENT',
      seats,
      morale,
      currentSeason: 1,
      season: 1,
      turn: 1,
      alliances: [],
      pendingRequests: [],
      partyStates: (currentConfig.parties || []).map(p => {
        const initAlliance = (p.initialAllianceKey && p.initialAllianceKey !== 'INDEPENDENT' && p.initialAllianceKey !== 'UNALIGNED')
          ? p.initialAllianceKey
          : null;
        return {
          partyKey: p.partyKey,
          partyName: p.name || p.partyName,
          shortName: p.shortName,
          color: p.color,
          ideology: p.ideology,
          seats: partySeatTotalsMap[p.partyKey] || 0,
          morale: p.initialMorale || p.initialContent || 70,
          funds: p.declaredFundsCr || p.fundsCr || p.initialFunds || 10.0,
          workers: p.workers || 50000,
          volunteers: p.volunteers || 15000,
          donors: p.donors || 1000,
          currentAllianceId: initAlliance,
          preSeededAllianceKey: p.initialAllianceKey || 'INDEPENDENT',
          isPlayerParty: p.partyKey === selectedParty.partyKey,
          corruption: 0
        };
      }),
      playerFunds: selectedParty.declaredFundsCr || selectedParty.fundsCr || selectedParty.initialFunds || 15.0,
      playerCorruption: 0,
      corruption: 0,
      createdAt: new Date().toISOString()
    };

    try {
      // Call backend to create the national game in MongoDB
      const userId = useGameStore.getState().user?.id || useGameStore.getState().user?.userId || 'local';
      const apiResult = await startNationalGame({
        userId,
        era: currentConfig.era,
        partyKey: selectedParty.partyKey,
        parties: currentConfig.parties || [],
        stateSeatData: currentConfig.stateSeatData || []
      });

      // Merge backend result with local display fields
      const fullGameData = {
        ...localGameData,
        ...apiResult,
        // Keep display fields even if backend doesn't return them
        eraTitle: localGameData.eraTitle,
        gameMode: localGameData.gameMode,
        gameModeTitle: localGameData.gameModeTitle,
        gameModeShortTitle: localGameData.gameModeShortTitle,
        partyColor: localGameData.partyColor,
      };

      setActiveNationalGame(fullGameData);
    } catch (err) {
      console.warn('Backend startNationalGame failed, using local data:', err);
      // Fallback: use local data so the game still launches
      setActiveNationalGame(localGameData);
    }

    setShowConfirmModal(false);
    setView('WAR_ROOM');
    if (setActiveNationalTab) {
      setActiveNationalTab('intelligence');
    }
  };


  // Render Confirmation Modal
  const renderConfirmModal = () => {
    if (!showConfirmModal || !selectedParty || !currentConfig) return null;

    const seats = partySeatTotalsMap[selectedParty.partyKey] || 0;
    const funds = selectedParty.declaredFundsCr || selectedParty.fundsCr || selectedParty.initialFunds || 15;
    const content = selectedParty.initialContent || 80;
    const allianceColor = ALLIANCE_COLORS[selectedParty.initialAllianceKey] || '#38bdf8';

    return (
      <div style={{
        position: 'fixed',
        top: 0, left: 0, right: 0, bottom: 0,
        backgroundColor: 'rgba(3, 7, 18, 0.85)',
        backdropFilter: 'blur(10px)',
        zIndex: 9999,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '20px'
      }}>
        <div style={{
          backgroundColor: '#0f172a',
          border: '1px solid rgba(56, 189, 248, 0.4)',
          borderRadius: '16px',
          boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.7), 0 0 30px rgba(56, 189, 248, 0.25)',
          maxWidth: '540px',
          width: '100%',
          padding: '28px',
          color: '#f8fafc'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '16px' }}>
            <span style={{ fontSize: '28px' }}>🏛️</span>
            <div>
              <h3 style={{ margin: 0, fontSize: '20px', fontWeight: '800', color: '#38bdf8' }}>
                Confirm Campaign Initialization
              </h3>
              <p style={{ margin: '2px 0 0 0', fontSize: '13px', color: '#94a3b8' }}>
                Review campaign details before launching national command
              </p>
            </div>
          </div>

          {activeNationalGame && (
            <div style={{
              backgroundColor: 'rgba(239, 68, 68, 0.15)',
              border: '1px solid rgba(239, 68, 68, 0.4)',
              borderRadius: '10px',
              padding: '12px 16px',
              marginBottom: '20px',
              fontSize: '13px',
              color: '#fca5a5'
            }}>
              ⚠️ <strong>Active Game Overwrite Warning:</strong> Starting a new game will permanently replace your active campaign (Era {activeNationalGame.era}, {activeNationalGame.partyName}).
            </div>
          )}

          {/* Campaign Summary Card */}
          <div style={{
            backgroundColor: 'rgba(30, 41, 59, 0.8)',
            border: '1px solid rgba(255, 255, 255, 0.1)',
            borderRadius: '12px',
            padding: '20px',
            marginBottom: '24px'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '14px' }}>
              <span style={{ fontSize: '12px', fontWeight: '700', textTransform: 'uppercase', letterSpacing: '0.08em', color: '#94a3b8' }}>
                Selected Era
              </span>
              <span style={{ backgroundColor: '#1e293b', border: '1px solid #334155', color: '#38bdf8', padding: '4px 10px', borderRadius: '6px', fontSize: '12px', fontWeight: '700' }}>
                Era {currentConfig.era} — {currentConfig.title}
              </span>
            </div>

            <div style={{ display: 'flex', alignItems: 'center', gap: '14px', marginBottom: '16px', borderBottom: '1px solid rgba(255,255,255,0.1)', paddingBottom: '14px' }}>
              <div style={{
                width: '40px', height: '40px', borderRadius: '10px',
                backgroundColor: selectedParty.color || '#7C3AED',
                boxShadow: '0 4px 12px rgba(0,0,0,0.4)',
                flexShrink: 0
              }} />
              <div>
                <h4 style={{ margin: 0, fontSize: '17px', fontWeight: '800', color: '#ffffff' }}>
                  {selectedParty.name}
                </h4>
                <div style={{ display: 'flex', gap: '8px', marginTop: '4px', alignItems: 'center' }}>
                  <span style={{ backgroundColor: `${allianceColor}25`, border: `1px solid ${allianceColor}`, color: allianceColor, padding: '2px 8px', borderRadius: '4px', fontSize: '11px', fontWeight: '700' }}>
                    {selectedParty.initialAllianceKey || 'INDEPENDENT'}
                  </span>
                  {selectedParty.partyKey === 'ydp' && (
                    <span style={{ backgroundColor: 'rgba(245, 158, 11, 0.2)', border: '1px solid #f59e0b', color: '#fbbf24', padding: '2px 8px', borderRadius: '4px', fontSize: '11px', fontWeight: '700' }}>
                      ⭐ Recommended
                    </span>
                  )}
                </div>
              </div>
            </div>

            {/* Stats Breakdown */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '10px', textAlign: 'center' }}>
              <div style={{ backgroundColor: '#0f172a', padding: '10px', borderRadius: '8px', border: '1px solid #334155' }}>
                <div style={{ fontSize: '11px', color: '#94a3b8', fontWeight: '600', marginBottom: '4px' }}>LOK SABHA SEATS</div>
                <div style={{ fontSize: '18px', fontWeight: '800', color: '#38bdf8' }}>{seats}</div>
              </div>
              <div style={{ backgroundColor: '#0f172a', padding: '10px', borderRadius: '8px', border: '1px solid #334155' }}>
                <div style={{ fontSize: '11px', color: '#94a3b8', fontWeight: '600', marginBottom: '4px' }}>DECLARED FUNDS</div>
                <div style={{ fontSize: '18px', fontWeight: '800', color: '#fbbf24' }}>₹{funds} Cr</div>
              </div>
              <div style={{ backgroundColor: '#0f172a', padding: '10px', borderRadius: '8px', border: '1px solid #334155' }}>
                <div style={{ fontSize: '11px', color: '#94a3b8', fontWeight: '600', marginBottom: '4px' }}>PARTY MORALE</div>
                <div style={{ fontSize: '18px', fontWeight: '800', color: '#10b981' }}>{content}</div>
              </div>
            </div>
          </div>

          {/* Action Buttons */}
          <div style={{ display: 'flex', gap: '12px' }}>
            <button
              onClick={() => setShowConfirmModal(false)}
              style={{
                flex: 1, padding: '12px', borderRadius: '8px',
                backgroundColor: 'transparent', border: '1px solid #475569',
                color: '#94a3b8', fontWeight: '700', cursor: 'pointer'
              }}
            >
              Cancel
            </button>
            <button
              onClick={handleConfirmLaunchGame}
              style={{
                flex: 1.5, padding: '12px', borderRadius: '8px',
                backgroundColor: '#0284c7', border: '1px solid #38bdf8',
                color: '#ffffff', fontWeight: '800', cursor: 'pointer',
                boxShadow: '0 4px 14px rgba(2, 132, 199, 0.4)'
              }}
            >
              🚀 Confirm & Launch Campaign
            </button>
          </div>
        </div>
      </div>
    );
  };

  if (view === 'WAR_ROOM') {
    return <NationalWarRoomView onReturnToHeadquarters={() => setView('HEADQUARTERS')} />;
  }

  // Main Headquarters Overview Screen
  if (view === 'HEADQUARTERS') {
    return (
      <div style={{
        minHeight: '80vh',
        backgroundColor: '#0b1329',
        borderRadius: '16px',
        border: '1px solid rgba(56, 189, 248, 0.2)',
        padding: 'clamp(14px, 4vw, 30px)',
        color: '#f8fafc',
        boxShadow: '0 20px 40px rgba(0,0,0,0.6)'
      }}>
        {/* Header Title */}
        <div style={{ textAlign: 'center', marginBottom: '30px' }}>
          <div style={{
            display: 'inline-flex', alignItems: 'center', gap: '8px',
            backgroundColor: 'rgba(56, 189, 248, 0.1)',
            border: '1px solid rgba(56, 189, 248, 0.3)',
            color: '#38bdf8', padding: '6px 16px', borderRadius: '9999px',
            fontSize: '11px', fontWeight: '700', letterSpacing: '0.08em',
            textTransform: 'uppercase', marginBottom: '12px'
          }}>
            🏛️ WAR ROOM COMMAND HEADQUARTERS
          </div>
          <h1 style={{ margin: 0, fontSize: 'clamp(22px, 5vw, 32px)', fontWeight: '900', color: '#ffffff', letterSpacing: '-0.02em' }}>
            National Politics Mode
          </h1>
          <p style={{ margin: '8px auto 0 auto', maxWidth: '600px', fontSize: '13px', color: '#94a3b8', lineHeight: 1.5 }}>
            Command 543 Lok Sabha seats across 30 states. Lead your party through national crises, build grand coalitions, and claim the Prime Ministership.
          </p>
        </div>

        {/* Action Cards Container */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))',
          gap: '16px',
          maxWidth: '960px',
          margin: '0 auto'
        }}>
          {/* Card 1: Resume Active Campaign */}
          <div style={{
            backgroundColor: activeNationalGame ? 'rgba(15, 23, 42, 0.9)' : 'rgba(15, 23, 42, 0.5)',
            border: activeNationalGame ? '1.5px solid #38bdf8' : '1px solid #1e293b',
            borderRadius: '16px',
            padding: '28px',
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'space-between',
            boxShadow: activeNationalGame ? '0 10px 30px rgba(56, 189, 248, 0.15)' : 'none',
            position: 'relative',
            overflow: 'hidden'
          }}>
            {activeNationalGame && (
              <div style={{
                position: 'absolute', top: 0, right: 0,
                backgroundColor: '#38bdf8', color: '#0f172a',
                padding: '4px 14px', borderBottomLeftRadius: '10px',
                fontSize: '11px', fontWeight: '800', textTransform: 'uppercase'
              }}>
                Active Campaign
              </div>
            )}

            <div>
              <div style={{ fontSize: '36px', marginBottom: '16px' }}>▶️</div>
              <h3 style={{ margin: '0 0 8px 0', fontSize: '20px', fontWeight: '800', color: '#ffffff' }}>
                Resume Campaign
              </h3>
              <p style={{ margin: 0, fontSize: '14px', color: '#94a3b8', lineHeight: 1.5 }}>
                {activeNationalGame 
                  ? `Continue your ongoing Era ${activeNationalGame.era} campaign as ${activeNationalGame.partyName}.` 
                  : 'No active national campaign found. Start a new campaign below.'}
              </p>

              {activeNationalGame && (
                <div style={{
                  marginTop: '20px',
                  backgroundColor: '#0f172a',
                  border: '1px solid #334155',
                  borderRadius: '10px',
                  padding: '14px'
                }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '10px' }}>
                    <div style={{
                      width: '28px', height: '28px', borderRadius: '6px',
                      backgroundColor: activeNationalGame.partyColor || '#7C3AED',
                      display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '14px'
                    }}>
                      🏛️
                    </div>
                    <div>
                      <div style={{ fontSize: '14px', fontWeight: '800', color: '#ffffff' }}>
                        {activeNationalGame.partyName} ({activeNationalGame.partyShortName})
                      </div>
                      <div style={{ fontSize: '11px', color: '#94a3b8' }}>
                        Era {activeNationalGame.era} • Turn {activeNationalGame.currentSeason || activeNationalGame.season || 1} (Month {activeNationalGame.currentSeason || activeNationalGame.season || 1})
                      </div>
                    </div>
                  </div>
                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '8px', textAlign: 'center', fontSize: '12px' }}>
                    <div>
                      <span style={{ color: '#94a3b8' }}>Seats:</span> <strong style={{ color: '#38bdf8' }}>{activeNationalGame.seats}</strong>
                    </div>
                    <div>
                      <span style={{ color: '#94a3b8' }}>Funds:</span> <strong style={{ color: '#fbbf24' }}>₹{activeNationalGame.playerFunds != null ? activeNationalGame.playerFunds : '—'} Cr</strong>
                    </div>
                    <div>
                      <span style={{ color: '#94a3b8' }}>Morale:</span> <strong style={{ color: '#10b981' }}>{activeNationalGame.morale ?? activeNationalGame.content ?? '—'}</strong>
                    </div>
                  </div>
                </div>
              )}
            </div>

            <div style={{ marginTop: '24px' }}>
              <button
                disabled={!activeNationalGame}
                onClick={() => {
                  setView('WAR_ROOM');
                  if (setActiveNationalTab) {
                    setActiveNationalTab('intelligence');
                  }
                }}
                style={{
                  width: '100%',
                  padding: '14px',
                  borderRadius: '10px',
                  backgroundColor: activeNationalGame ? '#0284c7' : '#1e293b',
                  border: activeNationalGame ? '1px solid #38bdf8' : '1px solid #334155',
                  color: activeNationalGame ? '#ffffff' : '#64748b',
                  fontWeight: '800',
                  fontSize: '14px',
                  cursor: activeNationalGame ? 'pointer' : 'not-allowed',
                  boxShadow: activeNationalGame ? '0 4px 14px rgba(2, 132, 199, 0.4)' : 'none'
                }}
              >
                {activeNationalGame ? '▶ Continue Campaign' : 'No Save Game'}
              </button>
            </div>
          </div>

          {/* Card 2: Create New Campaign */}
          <div style={{
            backgroundColor: 'rgba(15, 23, 42, 0.9)',
            border: '1.5px solid rgba(139, 92, 246, 0.5)',
            borderRadius: '16px',
            padding: '28px',
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'space-between',
            boxShadow: '0 10px 30px rgba(139, 92, 246, 0.15)'
          }}>
            <div>
              <div style={{ fontSize: '36px', marginBottom: '16px' }}>⚡</div>
              <h3 style={{ margin: '0 0 8px 0', fontSize: '20px', fontWeight: '800', color: '#ffffff' }}>
                Select a Major National Party
              </h3>
              <p style={{ margin: 0, fontSize: '14px', color: '#94a3b8', lineHeight: 1.5 }}>
                Select an era (2001–2025) and lead your party to national dominance.
              </p>
            </div>

            <div style={{ marginTop: '24px' }}>
              <button
                onClick={() => setView('CREATE_GAME')}
                style={{
                  width: '100%',
                  padding: '14px',
                  borderRadius: '10px',
                  backgroundColor: '#7c3aed',
                  border: '1px solid #a855f7',
                  color: '#ffffff',
                  fontWeight: '800',
                  fontSize: '14px',
                  cursor: 'pointer',
                  boxShadow: '0 4px 14px rgba(124, 58, 237, 0.4)'
                }}
              >
                ⚡ Start New Campaign
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }

  // View 2: Create New Campaign Setup Flow
  return (
    <div style={{
      minHeight: '80vh',
      backgroundColor: '#0b1329',
      borderRadius: '16px',
      border: '1px solid rgba(56, 189, 248, 0.2)',
      padding: '28px',
      color: '#f8fafc',
      boxShadow: '0 20px 40px rgba(0,0,0,0.6)'
    }}>
      {renderConfirmModal()}

      {/* Top Header Navigation */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '24px', flexWrap: 'wrap', gap: '12px' }}>
        <button
          onClick={() => setView('HEADQUARTERS')}
          style={{
            backgroundColor: 'rgba(30, 41, 59, 0.8)',
            border: '1px solid #475569',
            color: '#94a3b8',
            padding: '8px 16px',
            borderRadius: '8px',
            fontWeight: '700',
            fontSize: '13px',
            cursor: 'pointer'
          }}
        >
          ← Back
        </button>

        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span style={{ backgroundColor: '#1e293b', border: '1px solid #334155', color: '#38bdf8', padding: '4px 12px', borderRadius: '6px', fontSize: '12px', fontWeight: '700' }}>
            Step 1: Era & Party Selection
          </span>
        </div>
      </div>

      {/* SECTION 1: ERA SELECTION */}
      <div style={{ marginBottom: '32px' }}>
        <h3 style={{ margin: '0 0 12px 0', fontSize: '18px', fontWeight: '800', color: '#38bdf8', display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span>📅</span> 1. Select Political Era
        </h3>

        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
          gap: '16px'
        }}>
          {configs.length > 0 ? (
            configs.map(cfg => {
              const isSelected = selectedEra === cfg.era;
              return (
                <div
                  key={cfg.era}
                  onClick={() => setSelectedEra(cfg.era)}
                  style={{
                    backgroundColor: isSelected ? 'rgba(56, 189, 248, 0.12)' : 'rgba(15, 23, 42, 0.7)',
                    border: isSelected ? '2px solid #38bdf8' : '1px solid #1e293b',
                    borderRadius: '12px',
                    padding: '20px',
                    cursor: 'pointer',
                    transition: 'all 0.2s ease',
                    boxShadow: isSelected ? '0 0 20px rgba(56, 189, 248, 0.2)' : 'none'
                  }}
                >
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                    <span style={{ fontSize: '18px', fontWeight: '900', color: isSelected ? '#38bdf8' : '#ffffff' }}>
                      Era {cfg.era}
                    </span>
                    {isSelected && (
                      <span style={{ backgroundColor: '#0284c7', color: '#ffffff', padding: '2px 8px', borderRadius: '4px', fontSize: '11px', fontWeight: '800' }}>
                        Selected
                      </span>
                    )}
                  </div>
                  <h4 style={{ margin: '0 0 6px 0', fontSize: '15px', fontWeight: '700', color: '#f1f5f9' }}>
                    {cfg.title || `Era ${cfg.era}`}
                  </h4>
                  <p style={{ margin: 0, fontSize: '13px', color: '#94a3b8', lineHeight: 1.4 }}>
                    {cfg.description}
                  </p>
                </div>
              );
            })
          ) : (
            /* Fallback single era display if loading/offline */
            <div style={{
              backgroundColor: 'rgba(56, 189, 248, 0.12)',
              border: '2px solid #38bdf8',
              borderRadius: '12px',
              padding: '20px'
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                <span style={{ fontSize: '18px', fontWeight: '900', color: '#38bdf8' }}>Era 2001</span>
                <span style={{ backgroundColor: '#0284c7', color: '#ffffff', padding: '2px 8px', borderRadius: '4px', fontSize: '11px', fontWeight: '800' }}>Default</span>
              </div>
              <h4 style={{ margin: '0 0 6px 0', fontSize: '15px', fontWeight: '700', color: '#f1f5f9' }}>The NDA Experiment</h4>
              <p style={{ margin: 0, fontSize: '13px', color: '#94a3b8', lineHeight: 1.4 }}>
                Vajpayee leads the 24-party NDA coalition through economic reforms and security challenges (2001-2005).
              </p>
            </div>
          )}
        </div>
      </div>

      {/* SECTION 2: GAME MODE OBJECTIVE SELECTION */}
      <SelectMode
        selectedGameMode={selectedGameMode}
        setSelectedGameMode={setSelectedGameMode}
      />

      {/* SECTION 3: PARTY SELECTION TABS */}
      <div style={{ marginBottom: '32px' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '14px' }}>
          <h3 style={{ margin: 0, fontSize: '18px', fontWeight: '800', color: '#38bdf8', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span>🚩</span> 2. Select Your Political Party
          </h3>
          <span style={{ fontSize: '13px', color: '#94a3b8' }}>
            {selectableParties.length} Selectable Parties Available
          </span>
        </div>

        {/* Party Selection Cards/Tabs Grid */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fill, minmax(310px, 1fr))',
          gap: '16px'
        }}>
          {selectableParties.map(party => {
            const isSelected = selectedPartyKey === party.partyKey;
            const isYdp = party.partyKey === 'ydp';
            const seats = partySeatTotalsMap[party.partyKey] || 0;
            const funds = party.declaredFundsCr || party.fundsCr || party.initialFunds || 15;
            const content = party.initialContent || 60;
            const allianceColor = ALLIANCE_COLORS[party.initialAllianceKey] || '#38bdf8';

            return (
              <div
                key={party.partyKey}
                onClick={() => setSelectedPartyKey(party.partyKey)}
                style={{
                  backgroundColor: isSelected ? 'rgba(15, 23, 42, 0.95)' : 'rgba(15, 23, 42, 0.6)',
                  border: isSelected 
                    ? `2px solid ${party.color || '#38bdf8'}` 
                    : isYdp ? '1.5px solid rgba(245, 158, 11, 0.5)' : '1px solid #1e293b',
                  borderRadius: '14px',
                  padding: '20px',
                  cursor: 'pointer',
                  transition: 'all 0.2s cubic-bezier(0.4, 0, 0.2, 1)',
                  boxShadow: isSelected 
                    ? `0 0 25px ${party.color || '#38bdf8'}35` 
                    : isYdp ? '0 0 15px rgba(245, 158, 11, 0.15)' : 'none',
                  position: 'relative'
                }}
              >
                {/* YDP Recommended Badge */}
                {isYdp && (
                  <div style={{
                    position: 'absolute', top: '-10px', right: '14px',
                    backgroundColor: '#f59e0b', color: '#0f172a',
                    padding: '3px 10px', borderRadius: '9999px',
                    fontSize: '10px', fontWeight: '900', textTransform: 'uppercase',
                    boxShadow: '0 4px 10px rgba(245, 158, 11, 0.4)',
                    letterSpacing: '0.04em'
                  }}>
                    ⭐ Recommended Player Party
                  </div>
                )}

                {/* Top Header: Party Color Box, Names & Selection Checkmark */}
                <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', marginBottom: '12px' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                    <div style={{
                      width: '36px', height: '36px', borderRadius: '10px',
                      backgroundColor: party.color || '#7C3AED',
                      boxShadow: '0 4px 10px rgba(0,0,0,0.3)',
                      flexShrink: 0
                    }} />
                    <div>
                      <h4 style={{ margin: 0, fontSize: '16px', fontWeight: '800', color: '#ffffff' }}>
                        {party.name}
                      </h4>
                      <span style={{ fontSize: '12px', color: '#94a3b8', fontWeight: '600' }}>
                        {party.shortName}
                      </span>
                    </div>
                  </div>

                  {isSelected && (
                    <span style={{
                      width: '24px', height: '24px', borderRadius: '50%',
                      backgroundColor: party.color || '#38bdf8',
                      color: '#ffffff', display: 'flex', alignItems: 'center', justifyContent: 'center',
                      fontSize: '12px', fontWeight: '800'
                    }}>
                      ✓
                    </span>
                  )}
                </div>

                {/* Alliance Tag */}
                <div style={{ marginBottom: '14px' }}>
                  <span style={{
                    backgroundColor: `${allianceColor}20`,
                    border: `1px solid ${allianceColor}`,
                    color: allianceColor,
                    padding: '3px 10px',
                    borderRadius: '6px',
                    fontSize: '11px',
                    fontWeight: '700'
                  }}>
                    Alliance: {party.initialAllianceKey || 'INDEPENDENT'}
                  </span>
                </div>

                {/* Stats Breakdown Bar */}
                <div style={{
                  display: 'grid',
                  gridTemplateColumns: 'repeat(3, 1fr)',
                  gap: '8px',
                  backgroundColor: '#090d1a',
                  padding: '10px',
                  borderRadius: '8px',
                  marginBottom: '12px',
                  textAlign: 'center'
                }}>
                  <div>
                    <div style={{ fontSize: '10px', color: '#64748b', fontWeight: '700', textTransform: 'uppercase' }}>SEATS</div>
                    <div style={{ fontSize: '15px', fontWeight: '800', color: '#38bdf8' }}>{seats}</div>
                  </div>
                  <div>
                    <div style={{ fontSize: '10px', color: '#64748b', fontWeight: '700', textTransform: 'uppercase' }}>FUNDS</div>
                    <div style={{ fontSize: '15px', fontWeight: '800', color: '#fbbf24' }}>₹{funds} Cr</div>
                  </div>
                  <div>
                    <div style={{ fontSize: '10px', color: '#64748b', fontWeight: '700', textTransform: 'uppercase' }}>PARTY MORALE</div>
                    <div style={{ fontSize: '15px', fontWeight: '800', color: '#10b981' }}>{content}</div>
                  </div>
                </div>

                {/* Party Description */}
                <p style={{ margin: 0, fontSize: '12px', color: '#94a3b8', lineHeight: 1.4 }}>
                  {party.description}
                </p>
              </div>
            );
          })}
        </div>
      </div>

      {/* SECTION 3: LAUNCH FOOTER */}
      {selectedParty && (
        <div style={{
          position: 'sticky', bottom: '10px',
          backgroundColor: '#0f172a',
          border: '1.5px solid #38bdf8',
          borderRadius: '12px',
          padding: '16px 24px',
          display: 'flex', justifyContent: 'space-between', alignItems: 'center',
          boxShadow: '0 10px 30px rgba(0,0,0,0.8), 0 0 20px rgba(56, 189, 248, 0.3)',
          zIndex: 100, flexWrap: 'wrap', gap: '14px'
        }}>
          <div>
            <div style={{ fontSize: '12px', color: '#94a3b8', fontWeight: '600' }}>Ready to launch national campaign:</div>
            <div style={{ fontSize: '16px', fontWeight: '800', color: '#ffffff' }}>
              Era {selectedEra} • {selectedParty.name} ({partySeatTotalsMap[selectedParty.partyKey] || 0} Lok Sabha Seats)
            </div>
          </div>

          <button
            onClick={() => setShowConfirmModal(true)}
            style={{
              backgroundColor: '#0284c7',
              border: '1px solid #38bdf8',
              color: '#ffffff',
              padding: '12px 28px',
              borderRadius: '8px',
              fontWeight: '900',
              fontSize: '15px',
              cursor: 'pointer',
              boxShadow: '0 4px 16px rgba(2, 132, 199, 0.5)'
            }}
          >
            🚀 Launch Campaign
          </button>
        </div>
      )}
    </div>
  );
}
