import React, { useState, useEffect } from 'react';
import { fetchNationalStates, skipNationalState } from '../../../api/apiClient';
import StateDetailModal from './StateDetailModal';

export default function NationalWR_States({ activeGame, configData, onGameUpdate, isCompleted = false, onMarkCompleted }) {
  const [states, setStates] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedState, setSelectedState] = useState(null);
  const [actionLoading, setActionLoading] = useState(false);

  const gameId = activeGame?.id || activeGame?._id || activeGame?.userId || 'local';
  const playerKey = (activeGame?.partyKey || 'YDP').toUpperCase();

  const loadStates = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await fetchNationalStates(gameId);
      if (Array.isArray(data)) {
        setStates(data);
      }
    } catch (err) {
      setError(err.message || 'Failed to load states.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadStates();
  }, [gameId, activeGame?.currentSeason]);

  const handleSkipState = async (stateCode) => {
    if (actionLoading) return;
    setActionLoading(true);
    try {
      const updated = await skipNationalState(gameId, stateCode);
      if (updated && onGameUpdate) {
        onGameUpdate(updated);
      }
      await loadStates();
    } catch (err) {
      console.warn('Skip state error:', err);
    } finally {
      setActionLoading(false);
    }
  };

  const eligibleStates = states.filter(s => s.isEligible !== false);
  const inactiveStates = states.filter(s => s.isEligible === false);
  const allStatesHandled = eligibleStates.length === 0 || eligibleStates.every(s => s.doneThisTurn || s.skippedThisTurn);

  const onMarkCompletedRef = React.useRef(onMarkCompleted);
  useEffect(() => {
    onMarkCompletedRef.current = onMarkCompleted;
  }, [onMarkCompleted]);

  useEffect(() => {
    if (states.length > 0 && isCompleted !== allStatesHandled) {
      onMarkCompletedRef.current?.(allStatesHandled);
    }
  }, [allStatesHandled, isCompleted, states.length]);

  const getPhaseBadge = (phase) => {
    switch (phase) {
      case 'FINAL_SPRINT':
        return { label: '🔴 Final Sprint', bg: 'rgba(239, 68, 68, 0.2)', border: '#ef4444', color: '#f87171' };
      case 'CAMPAIGN':
        return { label: '🟠 Campaign', bg: 'rgba(249, 115, 22, 0.2)', border: '#f97316', color: '#fb923c' };
      case 'PRE_ELECTION':
        return { label: '🟡 Pre-Election', bg: 'rgba(234, 179, 8, 0.2)', border: '#eab308', color: '#facc15' };
      case 'ELECTION_DAY':
        return { label: '🗳️ Election Day', bg: 'rgba(56, 189, 248, 0.2)', border: '#38bdf8', color: '#38bdf8' };
      default:
        return { label: '⚪ Regular', bg: 'rgba(148, 163, 184, 0.1)', border: '#64748b', color: '#94a3b8' };
    }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>

      {/* Top Banner / Stats Header */}
      <div style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        flexWrap: 'wrap',
        gap: '10px'
      }}>
        <div>
          <h3 style={{ margin: 0, fontSize: '15px', color: '#ffffff', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span>🗺️</span> Regional State Operations & Assembly Elections
          </h3>
          <p className="nwr-hide-mobile" style={{ margin: '4px 0 0', fontSize: '10.5px', color: '#94a3b8' }}>
            Only states where your party or alliance partners have active ground presence are playable. Other states are locked until you form an alliance with local players.
          </p>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <div style={{
            padding: '5px 12px',
            borderRadius: '6px',
            border: allStatesHandled ? '1.5px solid #10b981' : '1px solid #64748b',
            backgroundColor: allStatesHandled ? 'rgba(16, 185, 129, 0.2)' : 'rgba(30, 41, 59, 0.6)',
            color: allStatesHandled ? '#34d399' : '#cbd5e1',
            fontSize: '11px',
            fontWeight: '800',
            display: 'inline-flex',
            alignItems: 'center',
            gap: '6px'
          }}>
            {allStatesHandled
              ? `✅ All Playable States Handled (${eligibleStates.length} Active${inactiveStates.length > 0 ? `, ${inactiveStates.length} Locked Auto-Skipped` : ''})`
              : `⏳ Progress: ${eligibleStates.filter(s => s.doneThisTurn).length}/${eligibleStates.length} Active Done (${inactiveStates.length} Locked Auto-Skipped)`}
          </div>

          <button
            onClick={() => onMarkCompleted && onMarkCompleted(!isCompleted)}
            style={{
              padding: '5px 10px',
              borderRadius: '6px',
              border: isCompleted ? '1.5px solid #10b981' : '1px solid rgba(255,255,255,0.15)',
              backgroundColor: isCompleted ? 'rgba(16, 185, 129, 0.15)' : 'rgba(30, 41, 59, 0.5)',
              color: isCompleted ? '#34d399' : '#94a3b8',
              fontSize: '10px',
              fontWeight: '700',
              cursor: 'pointer'
            }}
          >
            {isCompleted ? '✓ Done' : 'Override Done'}
          </button>
        </div>
      </div>

      {error && (
        <div style={{ padding: '10px 14px', backgroundColor: 'rgba(239, 68, 68, 0.2)', border: '1px solid #ef4444', borderRadius: '8px', color: '#fca5a5', fontSize: '12px' }}>
          ⚠️ {error}
        </div>
      )}

      {/* State Summary Cards List */}
      {loading ? (
        <div style={{ textAlign: 'center', padding: '30px', color: '#94a3b8', fontSize: '12px' }}>
          Loading active states...
        </div>
      ) : states.length === 0 ? (
        <div style={{ padding: '30px', textAlign: 'center', backgroundColor: '#1e293b', borderRadius: '10px', color: '#94a3b8', fontSize: '12px' }}>
          No state operations configured.
        </div>
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
          {states.map(state => {
            const phaseBadge = getPhaseBadge(state.electionPhase);
            const isEligible = state.isEligible !== false;
            const isNewlyUnlocked = state.isNewlyUnlocked === true;
            const unlockedByPartner = state.unlockedByPartner;
            const isSkipped = state.skippedThisTurn;
            const isDone = state.doneThisTurn;

            return (
              <div
                key={state.stateCode}
                style={{
                  background: isEligible
                    ? 'linear-gradient(180deg, #1e293b 0%, #0f172a 100%)'
                    : 'linear-gradient(180deg, #131b2e 0%, #0a0f1d 100%)',
                  borderRadius: '12px',
                  border: !isEligible
                    ? '1px dashed #475569'
                    : isNewlyUnlocked
                    ? '1.5px solid #10b981'
                    : isDone
                    ? '1.5px solid #10b981'
                    : isSkipped
                    ? '1px dashed #64748b'
                    : '1px solid rgba(168, 85, 247, 0.3)',
                  padding: '12px 14px',
                  boxShadow: isNewlyUnlocked
                    ? '0 0 20px rgba(16, 185, 129, 0.35)'
                    : isDone
                    ? '0 0 16px rgba(16, 185, 129, 0.25)'
                    : '0 6px 20px rgba(0,0,0,0.3)',
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  flexWrap: 'wrap',
                  gap: '12px',
                  opacity: !isEligible ? 0.65 : isSkipped ? 0.6 : 1,
                  filter: !isEligible ? 'grayscale(0.4)' : 'none',
                  transition: 'all 0.2s',
                  position: 'relative'
                }}
              >
                {/* Left Info */}
                <div style={{ display: 'flex', alignItems: 'center', gap: '12px', flex: 1, minWidth: 0 }}>
                  <div style={{
                    fontSize: '24px',
                    width: '44px',
                    height: '44px',
                    borderRadius: '10px',
                    backgroundColor: !isEligible
                      ? 'rgba(71, 85, 105, 0.2)'
                      : isDone
                      ? 'rgba(16, 185, 129, 0.15)'
                      : 'rgba(168, 85, 247, 0.15)',
                    border: !isEligible
                      ? '1px solid #475569'
                      : isDone
                      ? '1px solid #10b981'
                      : '1px solid #a855f7',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center'
                  }}>
                    {!isEligible ? '🔒' : isDone ? '✅' : '🏛️'}
                  </div>

                  <div style={{ flex: 1 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
                      <h4 style={{ margin: 0, fontSize: '15px', color: !isEligible ? '#cbd5e1' : '#ffffff', fontWeight: 900 }}>
                        {state.stateName}
                      </h4>

                      {/* Newly Unlocked Highlight Badge */}
                      {isNewlyUnlocked && (
                        <span style={{
                          fontSize: '9.5px',
                          fontWeight: 900,
                          padding: '3px 8px',
                          borderRadius: '6px',
                          backgroundColor: 'rgba(16, 185, 129, 0.25)',
                          border: '1.5px solid #10b981',
                          color: '#34d399',
                          display: 'inline-flex',
                          alignItems: 'center',
                          gap: '4px',
                          animation: 'pulse 2s infinite'
                        }}>
                          ✨ NEWLY UNLOCKED THIS TURN (via {unlockedByPartner || 'Alliance Partner'})
                        </span>
                      )}

                      {/* Unlocked via Partner Badge */}
                      {isEligible && !isNewlyUnlocked && unlockedByPartner && (
                        <span style={{
                          fontSize: '9px',
                          fontWeight: 800,
                          padding: '2px 7px',
                          borderRadius: '4px',
                          backgroundColor: 'rgba(56, 189, 248, 0.15)',
                          border: '1px solid #38bdf8',
                          color: '#38bdf8'
                        }}>
                          🤝 Unlocked via {unlockedByPartner}
                        </span>
                      )}

                      {/* Locked Inactive Badge */}
                      {!isEligible && (
                        <span style={{
                          fontSize: '9px',
                          fontWeight: 900,
                          padding: '2px 7px',
                          borderRadius: '4px',
                          backgroundColor: 'rgba(100, 116, 139, 0.25)',
                          border: '1px solid #64748b',
                          color: '#94a3b8'
                        }}>
                          🔒 INACTIVE / LOCKED
                        </span>
                      )}

                      {isEligible && isDone && (
                        <span style={{
                          fontSize: '9px',
                          fontWeight: 900,
                          padding: '2px 7px',
                          borderRadius: '4px',
                          backgroundColor: 'rgba(16, 185, 129, 0.2)',
                          border: '1px solid #10b981',
                          color: '#34d399'
                        }}>
                          ✓ DONE
                        </span>
                      )}

                      {isEligible && isSkipped && (
                        <span style={{
                          fontSize: '9px',
                          fontWeight: 900,
                          padding: '2px 7px',
                          borderRadius: '4px',
                          backgroundColor: 'rgba(100, 116, 139, 0.2)',
                          border: '1px solid #64748b',
                          color: '#94a3b8'
                        }}>
                          ⏭️ SKIPPED
                        </span>
                      )}

                      <span style={{
                        fontSize: '9px',
                        fontWeight: 900,
                        padding: '2px 6px',
                        borderRadius: '4px',
                        backgroundColor: phaseBadge.bg,
                        border: `1px solid ${phaseBadge.border}`,
                        color: phaseBadge.color
                      }}>
                        {phaseBadge.label} ({state.turnsToElection} turns)
                      </span>
                    </div>

                    {/* Prominent Remark for Inactive States */}
                    {!isEligible && (
                      <div style={{
                        marginTop: '6px',
                        padding: '6px 10px',
                        borderRadius: '6px',
                        backgroundColor: 'rgba(234, 179, 8, 0.1)',
                        border: '1px solid rgba(234, 179, 8, 0.3)',
                        color: '#facc15',
                        fontSize: '11px',
                        fontWeight: 700,
                        display: 'flex',
                        alignItems: 'center',
                        gap: '6px'
                      }}>
                        <span>⚠️</span>
                        <span>
                          Make alliance with state players first
                          {state.unlockingParties && state.unlockingParties.length > 0
                            ? ` (e.g. ${state.unlockingParties.slice(0, 3).join(', ')})`
                            : ''}
                          . Auto-skipped for this turn.
                        </span>
                      </div>
                    )}

                    <div style={{ display: 'flex', gap: '10px', fontSize: '11px', color: '#94a3b8', marginTop: '4px' }}>
                      <span>Ruling: <strong style={{ color: '#f59e0b' }}>{state.rulingParty}</strong></span>
                      <span>•</span>
                      <span>{state.totalLokSabhaSeats} Lok Sabha Seats</span>
                      <span>•</span>
                      <span>{state.totalAssemblySeats} Assembly Seats</span>
                    </div>

                    {/* Stats pills */}
                    <div style={{ display: 'flex', gap: '12px', marginTop: '6px', fontSize: '11px' }}>
                      <div>
                        <span style={{ color: '#94a3b8' }}>Your Party: </span>
                        <strong style={{ color: '#c084fc' }}>{state.playerVoteShare}%</strong>
                      </div>
                      <div>
                        <span style={{ color: '#94a3b8' }}>Alliance Total: </span>
                        <strong style={{ color: '#38bdf8' }}>{state.allianceVoteShare}%</strong>
                      </div>
                      {isEligible && (
                        <div>
                          <span style={{ color: '#94a3b8' }}>Treasury: </span>
                          <strong style={{ color: '#34d399' }}>₹{state.stateFunds?.toFixed(1)} Cr</strong>
                        </div>
                      )}
                    </div>
                  </div>
                </div>

                {/* Right Action Buttons */}
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  {isEligible ? (
                    <>
                      <button
                        onClick={() => setSelectedState(state)}
                        style={{
                          padding: '8px 16px',
                          borderRadius: '8px',
                          border: 'none',
                          backgroundColor: isDone ? '#059669' : '#0284c7',
                          color: '#ffffff',
                          fontWeight: 800,
                          fontSize: '12px',
                          cursor: 'pointer',
                          display: 'flex',
                          alignItems: 'center',
                          gap: '5px',
                          boxShadow: isDone ? '0 2px 10px rgba(16, 185, 129, 0.4)' : '0 2px 10px rgba(2, 132, 199, 0.4)'
                        }}
                      >
                        <span>{isDone ? '✓' : '⚡'}</span> {isDone ? 'Done (Review)' : 'Action'}
                      </button>

                      <button
                        onClick={() => handleSkipState(state.stateCode)}
                        disabled={actionLoading || isSkipped}
                        style={{
                          padding: '8px 12px',
                          borderRadius: '8px',
                          border: '1px solid rgba(255,255,255,0.15)',
                          backgroundColor: isSkipped ? 'rgba(255,255,255,0.05)' : 'rgba(30, 41, 59, 0.6)',
                          color: isSkipped ? '#64748b' : '#cbd5e1',
                          fontWeight: 700,
                          fontSize: '11px',
                          cursor: isSkipped ? 'default' : 'pointer'
                        }}
                      >
                        {isSkipped ? 'Skipped ✓' : '⏭️ Skip'}
                      </button>
                    </>
                  ) : (
                    <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                      <button
                        disabled
                        style={{
                          padding: '8px 14px',
                          borderRadius: '8px',
                          border: '1px dashed #64748b',
                          backgroundColor: 'rgba(51, 65, 85, 0.4)',
                          color: '#94a3b8',
                          fontWeight: 700,
                          fontSize: '11px',
                          cursor: 'not-allowed',
                          display: 'flex',
                          alignItems: 'center',
                          gap: '5px'
                        }}
                      >
                        <span>🔒</span> Locked (Make Alliance)
                      </button>
                      <span style={{
                        padding: '6px 10px',
                        borderRadius: '6px',
                        backgroundColor: 'rgba(100, 116, 139, 0.15)',
                        border: '1px solid rgba(100, 116, 139, 0.3)',
                        color: '#94a3b8',
                        fontSize: '10px',
                        fontWeight: 700
                      }}>
                        ⏭️ Auto-Skipped
                      </span>
                    </div>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* Full-Screen Modal for State Actions */}
      {selectedState && (
        <StateDetailModal
          stateSummary={selectedState}
          activeGame={activeGame}
          onClose={() => {
            setSelectedState(null);
            loadStates();
          }}
          onGameUpdate={(updated) => {
            if (onGameUpdate) onGameUpdate(updated);
            loadStates();
          }}
        />
      )}

    </div>
  );
}
