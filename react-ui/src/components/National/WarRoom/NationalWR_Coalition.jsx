import React, { useState } from 'react';
import {
  createNationalAlliance,
  invitePartyToAlliance,
  respondToCoalitionRequest,
  removePartyFromAlliance,
  dissolveNationalAlliance,
  leaveNationalAlliance,
  reallocateAllianceResources,
  processNationalAiRequests
} from '../../../api/apiClient';

export default function NationalWR_Coalition({ activeGame, configData, onGameUpdate, isCompleted = false, onMarkCompleted }) {
  const [activeModal, setActiveModal] = useState(null); // null | 'create' | 'invite' | 'remove' | 'reallocate'
  const [selectedPartyKey, setSelectedPartyKey] = useState('');
  const [showInviteSection, setShowInviteSection] = useState(false);
  
  // Forms
  const [createForm, setCreateForm] = useState({ allianceName: '', color: '#38bdf8' });
  const [inviteForm, setInviteForm] = useState({ joiningBonus: 0, cabinetMinistersPromised: 0, stateMinistersPromised: 0 });
  const [reallocateForm, setReallocateForm] = useState([]);
  
  // Status
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  // 3-Second Flashing Response State
  const [flashBanner, setFlashBanner] = useState(null); // { message, type: 'success' | 'counter' | 'error', title }
  const [isFlashing, setIsFlashing] = useState(false);

  const triggerFlash = (message, type = 'info', title = null, extra = null) => {
    setFlashBanner({ message, type, title, ...(extra || {}) });
    setIsFlashing(true);
    // Flash for 3 seconds
    setTimeout(() => {
      setIsFlashing(false);
    }, 3000);
  };

  const playerAlliance = activeGame?.alliances?.find(a => a.leaderPartyKey === activeGame?.partyKey) || null;
  const partyStates = activeGame?.partyStates || [];
  const incomingRequests = (activeGame?.pendingRequests || []).filter(r => r.direction === 'INCOMING' && r.status === 'PENDING');
  const playerPartyState = partyStates.find(p => p.partyKey === activeGame?.partyKey || p.isPlayerParty);
  const playerPartyFunds = Number(playerPartyState?.funds ?? activeGame?.playerFunds ?? 0);
  const playerPartySeats = Number(playerPartyState?.seats ?? 0);
  const playerProjectedSeats = Number(playerPartyState?.projectedSeats ?? activeGame?.nationalProjectedSeats?.[activeGame?.partyKey?.toUpperCase()] ?? playerPartySeats);
  const isGainingMomentum = Boolean(playerPartyState?.gainingMomentum || (playerProjectedSeats > playerPartySeats));
  const playerDonationsPerTurn = Number(playerPartyState?.donationsPerTurn ?? Math.max(0.5, playerProjectedSeats * (isGainingMomentum ? 0.75 : 0.5)));

  // Helper to check if a party is genuinely unaligned based on last turn data (activeGame)
  const isPartyUnaligned = (p) => {
    const pKey = (p.partyKey || p.id || '').toLowerCase();
    const playerKey = (activeGame?.partyKey || '').toLowerCase();
    
    // 1. Cannot be player's party
    if (p.isPlayerParty || pKey === playerKey) return false;

    // 2. Cannot be active member or leader of any active alliance in last turn data
    const activeAlliances = activeGame?.alliances || [];
    for (const a of activeAlliances) {
      if ((a.leaderPartyKey || '').toLowerCase() === pKey) return false;
      if (a.members && a.members.some(m => (m.partyKey || '').toLowerCase() === pKey && !m.contract?.isBroken)) {
        return false;
      }
    }

    // 3. Load party's current alliance strictly from last turn data (partyStates)
    if (p.currentAllianceId !== undefined) {
      if (p.currentAllianceId === null) return true; // Explicitly unaligned / no alliance in current turn!
      const curr = String(p.currentAllianceId).toUpperCase();
      return curr === 'UNALIGNED' || curr === 'INDEPENDENT' || curr === 'NONE' || curr === '';
    }

    // 4. Initial turn fallback only if currentAllianceId was never set on the turn object
    const fallbackAlliance = p.preSeededAllianceKey || p.initialAllianceKey;
    if (!fallbackAlliance) return true;
    const upper = String(fallbackAlliance).toUpperCase();
    return upper === 'UNALIGNED' || upper === 'INDEPENDENT';
  };

  const rawParties = (partyStates && partyStates.length > 0)
    ? partyStates
    : (configData?.parties || []);

  const availableParties = rawParties.filter(isPartyUnaligned);

  const gameId = activeGame?.id || activeGame?._id || activeGame?.userId || 'local';

  const getPartyDetails = (partyKey) => {
    const pKey = (partyKey || '').toLowerCase();
    const pState = partyStates.find(p => (p.partyKey || p.id || '').toLowerCase() === pKey);
    const pConfig = configData?.parties?.find(p => (p.partyKey || p.id || '').toLowerCase() === pKey);
    return {
      name: pConfig?.name || pState?.partyName || pState?.partyKey || partyKey,
      shortName: pConfig?.shortName || pState?.shortName || (partyKey || '').toUpperCase(),
      color: pConfig?.color || pState?.color || '#94a3b8',
      seats: pState?.seats !== undefined ? pState.seats : (pConfig?.initialSeats || 0),
      morale: pState?.morale !== undefined ? pState.morale : (pConfig?.initialMorale || pConfig?.initialContent || 50),
      funds: pState?.funds !== undefined ? pState.funds : (pConfig?.declaredFundsCr || pConfig?.fundsCr || pConfig?.initialFunds || 10.0),
      workers: pState?.workers !== undefined ? pState.workers : (pConfig?.workers || 0),
      volunteers: pState?.volunteers !== undefined ? pState.volunteers : (pConfig?.volunteers || 0),
      donors: pState?.donors !== undefined ? pState.donors : (pConfig?.donors || 0),
      currentAlliance: pState?.currentAllianceId || null
    };
  };

  const handleAction = async (actionFn, successMsg = null, successTitle = null, ...args) => {
    setLoading(true);
    setError(null);
    setSuccess(null);
    try {
      const result = await actionFn(...args);
      // Close modal immediately so the response is clearly visible
      setActiveModal(null);

      if (result) {
        const gameToUpdate = result.game || (result.id ? result : null);
        if (gameToUpdate) {
          onGameUpdate(gameToUpdate);
        }
        if (onMarkCompleted) {
          onMarkCompleted(true);
        }

        // If result is a NationalCoalitionActionResponse (invitation response with boolean success)
        if (typeof result.success === 'boolean') {
          const respMsg = result.responseMessage || (result.success ? 'Coalition invitation accepted!' : 'Coalition invitation was declined.');
          if (result.success === false) {
            setError(respMsg);
            const isCounter = respMsg.includes('open to joining') || result.responseCode === 'COUNTER_PROPOSAL';
            triggerFlash(
              respMsg,
              isCounter ? 'counter' : 'error',
              isCounter ? 'COUNTER-PROPOSAL RECEIVED' : 'INVITATION DECLINED',
              isCounter ? {
                counterProposal: result.counterProposal,
                targetPartyKey: selectedPartyKey
              } : null
            );
          } else {
            setSuccess(respMsg);
            triggerFlash(respMsg, 'success', 'INVITATION ACCEPTED');
          }
        } else {
          // Result is a NationalGame object returned from alliance create/remove/dissolve/reallocate/respond
          const finalMsg = successMsg || 'Alliance action completed successfully!';
          const finalTitle = successTitle || 'ALLIANCE UPDATED';
          setSuccess(finalMsg);
          triggerFlash(finalMsg, 'success', finalTitle);
        }
      }
    } catch (err) {
      setActiveModal(null);
      setError(err.message || 'An error occurred.');
      triggerFlash(err.message || 'An error occurred.', 'error', 'ACTION FAILED');
    } finally {
      setLoading(false);
    }
  };

  const handleCreateAlliance = () => {
    if (!createForm.allianceName) return setError('Alliance name required');
    handleAction(
      createNationalAlliance,
      `Alliance "${createForm.allianceName}" formed successfully!`,
      'ALLIANCE CREATED',
      gameId,
      createForm
    );
  };

  const handleInviteParty = () => {
    if (!selectedPartyKey) return setError('Select a party to invite');
    handleAction(
      invitePartyToAlliance,
      null,
      null,
      gameId,
      { targetPartyKey: selectedPartyKey, ...inviteForm }
    );
  };

  const handleRemoveParty = () => {
    if (!selectedPartyKey) return setError('Select a party to remove');
    handleAction(
      removePartyFromAlliance,
      `Party ${selectedPartyKey.toUpperCase()} removed from alliance.`,
      'PARTY REMOVED',
      gameId,
      { targetPartyKey: selectedPartyKey }
    );
  };

  const handleDissolveAlliance = () => {
    if (window.confirm("Are you sure you want to dissolve the alliance? This will incur morale penalties.")) {
      handleAction(
        dissolveNationalAlliance,
        'Alliance dissolved successfully.',
        'ALLIANCE DISSOLVED',
        gameId
      );
    }
  };
  
  const handleLeaveAlliance = () => {
    if (window.confirm("Are you sure you want to leave your current alliance?")) {
      handleAction(
        leaveNationalAlliance,
        'Successfully left the alliance.',
        'LEFT ALLIANCE',
        gameId
      );
    }
  };

  const handleReallocate = () => {
    handleAction(
      reallocateAllianceResources,
      'Alliance resources successfully reallocated.',
      'RESOURCES REALLOCATED',
      gameId,
      { allocations: reallocateForm }
    );
  };

  const handleRespondRequest = (requestId, accepted) => {
    handleAction(
      respondToCoalitionRequest,
      accepted ? 'Coalition request accepted.' : 'Coalition request rejected.',
      accepted ? 'REQUEST ACCEPTED' : 'REQUEST DECLINED',
      gameId,
      { requestId, accept: accepted }
    );
  };

  const openInviteModal = (partyKey) => {
    setSelectedPartyKey(partyKey);
    setInviteForm({ joiningBonus: 0, cabinetMinistersPromised: 0, stateMinistersPromised: 0 });
    setActiveModal('invite');
  };

  const openReallocateModal = () => {
    if (!playerAlliance) return;
    const initialAllocations = playerAlliance.members.map(m => ({
      partyKey: m.partyKey,
      cabinetMinistersPromised: m.contract.cabinetMinistersPromised,
      stateMinistersPromised: m.contract.stateMinistersPromised
    }));
    setReallocateForm(initialAllocations);
    setActiveModal('reallocate');
  };

  // Helper for alliance stats: deduplicate constituent party keys so leader is not counted twice
  const uniqueMemberKeys = playerAlliance ? Array.from(new Set([
    playerAlliance.leaderPartyKey,
    ...(playerAlliance.members || []).map(m => m.partyKey)
  ].filter(Boolean))) : [];

  const totalAllianceSeats = uniqueMemberKeys.reduce((sum, pk) => {
    const p = partyStates.find(ps => (ps.partyKey || ps.id || '').toLowerCase() === pk.toLowerCase());
    return sum + (p?.seats || 0);
  }, 0);

  const totalCabinet = playerAlliance ? playerAlliance.members.reduce((s, m) => s + (m.contract?.cabinetMinistersPromised || 0), 0) : 0;
  const totalState = playerAlliance ? playerAlliance.members.reduce((s, m) => s + (m.contract?.stateMinistersPromised || 0), 0) : 0;
  
  const modalStyle = {
    position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
    backgroundColor: 'rgba(15, 23, 42, 0.9)', display: 'flex', justifyContent: 'center', alignItems: 'center', zIndex: 1000
  };
  const modalContentStyle = {
    backgroundColor: '#131d38', padding: '16px', borderRadius: '12px', border: '1px solid #38bdf8', minWidth: '320px', maxWidth: '90vw',
    boxShadow: '0 8px 32px rgba(0, 0, 0, 0.6)'
  };
  const inputStyle = {
    width: '100%', padding: '6px 8px', marginBottom: '8px', borderRadius: '6px', fontSize: '10px',
    border: '1px solid #334155', backgroundColor: '#0f172a', color: '#fff'
  };
  const labelStyle = { display: 'block', marginBottom: '3px', color: '#94a3b8', fontSize: '8.5px', fontWeight: 'bold' };
  
  const renderLoading = () => loading && (
    <div style={{ textAlign: 'center', color: '#38bdf8', fontWeight: 'bold', margin: '8px 0', fontSize: '10px' }}>⏳ Processing...</div>
  );
  
  const renderMessages = () => (
    <>
      {error && <div style={{ color: '#ef4444', backgroundColor: 'rgba(239,68,68,0.1)', padding: '7px 10px', borderRadius: '6px', marginBottom: '12px', fontSize: '9.5px' }}>{error}</div>}
      {success && <div style={{ color: '#10b981', backgroundColor: 'rgba(16,185,129,0.1)', padding: '7px 10px', borderRadius: '6px', marginBottom: '12px', fontSize: '9.5px' }}>{success}</div>}
    </>
  );

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
      
      {/* 2-Second Flashing Response Notification Banner */}
      {flashBanner && (
        <div
          style={{
            padding: '14px 18px',
            borderRadius: '10px',
            background: flashBanner.type === 'counter'
              ? 'linear-gradient(135deg, rgba(30, 41, 59, 0.98), rgba(15, 23, 42, 0.98))'
              : flashBanner.type === 'success'
              ? 'linear-gradient(135deg, rgba(6, 78, 59, 0.98), rgba(15, 23, 42, 0.98))'
              : 'linear-gradient(135deg, rgba(127, 29, 29, 0.98), rgba(15, 23, 42, 0.98))',
            border: flashBanner.type === 'counter'
              ? '2px solid #f59e0b'
              : flashBanner.type === 'success'
              ? '2px solid #10b981'
              : '2px solid #ef4444',
            boxShadow: isFlashing
              ? (flashBanner.type === 'counter'
                  ? '0 0 28px rgba(245, 158, 11, 0.95), inset 0 0 14px rgba(245, 158, 11, 0.4)'
                  : flashBanner.type === 'success'
                  ? '0 0 28px rgba(16, 185, 129, 0.95), inset 0 0 14px rgba(16, 185, 129, 0.4)'
                  : '0 0 28px rgba(239, 68, 68, 0.95), inset 0 0 14px rgba(239, 68, 68, 0.4)')
              : '0 4px 16px rgba(0,0,0,0.4)',
            transform: isFlashing ? 'scale(1.02)' : 'scale(1)',
            transition: 'all 0.3s ease-in-out',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            gap: '12px',
            zIndex: 100
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
            <span style={{ fontSize: '26px' }}>
              {flashBanner.type === 'counter' ? '🤝' : flashBanner.type === 'success' ? '✅' : '⛔'}
            </span>
            <div>
              <div style={{
                fontSize: '10.5px',
                fontWeight: 900,
                textTransform: 'uppercase',
                letterSpacing: '0.06em',
                color: flashBanner.type === 'counter' ? '#f59e0b' : flashBanner.type === 'success' ? '#10b981' : '#ef4444',
                marginBottom: '2px'
              }}>
                {flashBanner.title || (flashBanner.type === 'counter' ? 'COUNTER-PROPOSAL RECEIVED' : flashBanner.type === 'success' ? 'ACTION SUCCESSFUL' : 'INVITATION DECLINED')}
              </div>
              <div style={{ fontSize: '12.5px', fontWeight: 800, color: '#ffffff', lineHeight: 1.4 }}>
                {flashBanner.message}
              </div>

              {flashBanner.type === 'counter' && flashBanner.counterProposal && flashBanner.targetPartyKey && (
                <div style={{ marginTop: '8px', display: 'flex', gap: '8px' }}>
                  <button
                    onClick={() => {
                      const cp = flashBanner.counterProposal;
                      const pKey = flashBanner.targetPartyKey;
                      if (pKey && cp) {
                        handleAction(
                          invitePartyToAlliance,
                          null,
                          null,
                          gameId,
                          {
                            targetPartyKey: pKey,
                            joiningBonus: cp.joiningBonus || 0,
                            cabinetMinistersPromised: cp.cabinetMinistersPromised || 0,
                            stateMinistersPromised: cp.stateMinistersPromised || 0
                          }
                        );
                      }
                    }}
                    style={{
                      padding: '6px 14px',
                      borderRadius: '6px',
                      border: 'none',
                      backgroundColor: '#f59e0b',
                      color: '#0f172a',
                      fontSize: '11px',
                      fontWeight: 900,
                      cursor: 'pointer',
                      display: 'inline-flex',
                      alignItems: 'center',
                      gap: '5px',
                      boxShadow: '0 2px 8px rgba(245, 158, 11, 0.4)'
                    }}
                  >
                    <span>🤝</span> Accept Counter-Terms & Seal Deal (₹{Number(flashBanner.counterProposal.joiningBonus).toFixed(1)} Cr, {flashBanner.counterProposal.cabinetMinistersPromised} Cab, {flashBanner.counterProposal.stateMinistersPromised} State)
                  </button>
                </div>
              )}
            </div>
          </div>
          <button
            onClick={() => setFlashBanner(null)}
            style={{
              background: 'transparent',
              border: 'none',
              color: '#94a3b8',
              fontSize: '18px',
              cursor: 'pointer',
              padding: '4px',
              lineHeight: 1
            }}
            title="Dismiss"
          >
            ✕
          </button>
        </div>
      )}

      {/* Section 1 - Banner */}
      {playerAlliance ? (
        <div style={{
          padding: '14px', borderRadius: '12px', background: 'linear-gradient(135deg, rgba(15, 23, 42, 0.8), rgba(19, 29, 56, 0.9))',
          borderLeft: `4px solid ${playerAlliance.color || '#38bdf8'}`, boxShadow: '0 4px 12px rgba(0,0,0,0.3)'
        }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '10px' }}>
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <h2 style={{ margin: '0 0 3px 0', color: '#fff', fontSize: '15px', fontWeight: '900' }}>
                  {playerAlliance.allianceName || playerAlliance.name}
                </h2>
                <span className="nwr-badge nwr-badge-green">Active Front Leader</span>
              </div>
              <div style={{ display: 'flex', gap: '12px', color: '#cbd5e1', fontSize: '9.5px', marginTop: '3px' }}>
                <span>🪑 Total Seats: <strong style={{ color: '#38bdf8' }}>{totalAllianceSeats}</strong></span>
                <span>📅 Formed: Season {playerAlliance.formedAtSeason || playerAlliance.establishedSeason || 1}</span>
                <span>👥 Members: <strong style={{ color: '#10b981' }}>{uniqueMemberKeys.length}</strong></span>
              </div>
            </div>
            <div style={{ textAlign: 'right', display: 'flex', flexDirection: 'column', alignItems: 'flex-end', gap: '6px' }}>
              <div>
                <div style={{ color: '#10b981', fontWeight: '900', fontSize: '14px' }}>
                  ₹ {playerPartyFunds.toFixed(1)} Cr Party Funds
                </div>
                <div style={{ color: isGainingMomentum ? '#34d399' : '#fbbf24', fontSize: '8.5px', fontWeight: '700' }}>
                  {isGainingMomentum ? '🔥 ' : ''}Party Donations: ₹ {playerDonationsPerTurn.toFixed(1)} Cr / turn ({playerProjectedSeats} proj. seats @ ₹{isGainingMomentum ? '0.75' : '0.50'} Cr)
                </div>
              </div>
              <button
                onClick={() => onMarkCompleted && onMarkCompleted(!isCompleted)}
                style={{
                  padding: '5px 12px',
                  borderRadius: '6px',
                  border: isCompleted ? '1.5px solid #10b981' : '1px solid #64748b',
                  backgroundColor: isCompleted ? 'rgba(16, 185, 129, 0.2)' : 'rgba(30, 41, 59, 0.7)',
                  color: isCompleted ? '#34d399' : '#cbd5e1',
                  fontSize: '9px',
                  fontWeight: '800',
                  cursor: 'pointer',
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '5px',
                  transition: 'all 0.2s ease'
                }}
                title="Mark coalition step completed for this season"
              >
                {isCompleted ? '✓ Strategy Confirmed' : 'Confirm Front Strategy'}
              </button>
            </div>
          </div>
          
          <div style={{ marginTop: '14px', display: 'flex', gap: '20px', flexWrap: 'wrap' }}>
            <div style={{ flex: 1, minWidth: '150px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '8.5px', marginBottom: '3px' }}>
                <span style={{ color: '#94a3b8' }}>Cabinet Ministers Promised</span>
                <span style={{ color: (playerAlliance.totalCabinetPromised || totalCabinet) > 20 ? '#ef4444' : '#fff', fontWeight: '800' }}>
                  {playerAlliance.totalCabinetPromised || totalCabinet} / 20
                </span>
              </div>
              <div style={{ height: '6px', background: '#1e293b', borderRadius: '3px', overflow: 'hidden' }}>
                <div style={{ height: '100%', width: `${Math.min(100, (((playerAlliance.totalCabinetPromised || totalCabinet)/20)*100))}%`, background: (playerAlliance.totalCabinetPromised || totalCabinet) > 20 ? '#ef4444' : '#38bdf8' }} />
              </div>
            </div>
            <div style={{ flex: 1, minWidth: '150px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '8.5px', marginBottom: '3px' }}>
                <span style={{ color: '#94a3b8' }}>State Ministers Promised</span>
                <span style={{ color: (playerAlliance.totalStatePromised || totalState) > 50 ? '#ef4444' : '#fff', fontWeight: '800' }}>
                  {playerAlliance.totalStatePromised || totalState} / 50
                </span>
              </div>
              <div style={{ height: '6px', background: '#1e293b', borderRadius: '3px', overflow: 'hidden' }}>
                <div style={{ height: '100%', width: `${Math.min(100, (((playerAlliance.totalStatePromised || totalState)/50)*100))}%`, background: (playerAlliance.totalStatePromised || totalState) > 50 ? '#ef4444' : '#fbbf24' }} />
              </div>
            </div>
          </div>
        </div>
      ) : (
        <div style={{
          padding: '14px', borderRadius: '12px', background: 'linear-gradient(135deg, rgba(15, 23, 42, 0.8), rgba(19, 29, 56, 0.9))',
          borderLeft: '4px solid #a855f7', boxShadow: '0 4px 12px rgba(0,0,0,0.3)'
        }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '4px' }}>
                <span style={{ fontSize: '14px' }}>🏛️</span>
                <h2 style={{ margin: 0, color: '#fff', fontSize: '12.5px', fontWeight: '800' }}>
                  Status: Independent / Unaligned ({activeGame?.partyName || (activeGame?.partyKey || '').toUpperCase()})
                </h2>
                <span className="nwr-badge nwr-badge-cyan">Open for Coalition</span>
              </div>
              <p style={{ margin: 0, color: '#94a3b8', fontSize: '9px', lineHeight: 1.4 }}>
                Your party is not aligned with any coalition bloc. You are completely open to create a new national alliance and invite unaligned regional parties to join your front.
              </p>
            </div>
            <div style={{ textAlign: 'right', display: 'flex', flexDirection: 'column', alignItems: 'flex-end', gap: '6px' }}>
              <div>
                <div style={{ color: '#10b981', fontWeight: '900', fontSize: '14px' }}>
                  ₹ {Number(((activeGame?.partyStates?.find(p => (p.partyKey || '').toLowerCase() === (activeGame?.partyKey || '').toLowerCase())?.funds) ?? (activeGame?.playerFunds || 15.0))).toFixed(1)} Cr
                </div>
                <div style={{ color: '#94a3b8', fontSize: '8px', fontWeight: '700' }}>Declared Party Funds</div>
              </div>
              <button
                onClick={() => onMarkCompleted && onMarkCompleted(!isCompleted)}
                style={{
                  padding: '5px 12px',
                  borderRadius: '6px',
                  border: isCompleted ? '1.5px solid #10b981' : '1px solid #64748b',
                  backgroundColor: isCompleted ? 'rgba(16, 185, 129, 0.2)' : 'rgba(30, 41, 59, 0.7)',
                  color: isCompleted ? '#34d399' : '#cbd5e1',
                  fontSize: '9px',
                  fontWeight: '800',
                  cursor: 'pointer',
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '5px',
                  transition: 'all 0.2s ease'
                }}
                title="Mark coalition step completed for this season"
              >
                {isCompleted ? '✓ Strategy Confirmed' : 'Confirm Front Strategy'}
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Section 2 - Action Buttons */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '10px' }}>
        <button className="nwr-card" disabled={!!playerAlliance} onClick={() => setActiveModal('create')}
          style={{ opacity: playerAlliance ? 0.5 : 1, cursor: playerAlliance ? 'not-allowed' : 'pointer', textAlign: 'center', padding: '10px' }}>
          <div style={{ fontSize: '16px', marginBottom: '4px' }}>🏛️</div>
          <div style={{ fontWeight: 'bold', color: '#fff', fontSize: '10px' }}>Create Alliance</div>
        </button>
        
        <button
          className="nwr-card"
          onClick={() => {
            if (!playerAlliance) {
              setError('Please create your alliance first before inviting coalition partners.');
              return;
            }
            setShowInviteSection(prev => !prev);
          }}
          style={{
            opacity: !playerAlliance ? 0.6 : 1,
            cursor: 'pointer',
            textAlign: 'center',
            padding: '10px',
            border: showInviteSection ? '1.5px solid #38bdf8' : (!playerAlliance ? '1px solid rgba(255,255,255,0.08)' : '1px solid var(--nwr-border)'),
            background: showInviteSection ? 'rgba(56, 189, 248, 0.15)' : 'var(--nwr-surface)',
            boxShadow: showInviteSection ? '0 0 12px rgba(56, 189, 248, 0.3)' : 'none',
            transition: 'all 0.2s ease-in-out'
          }}
        >
          <div style={{ fontSize: '16px', marginBottom: '4px' }}>✉️</div>
          <div style={{ fontWeight: 'bold', color: showInviteSection ? '#38bdf8' : '#fff', fontSize: '10px' }}>
            Invite for coalition
          </div>
        </button>
        
        <button className="nwr-card" disabled={!playerAlliance || playerAlliance.members.length === 0} onClick={() => setActiveModal('remove')}
          style={{ opacity: (!playerAlliance || playerAlliance.members.length === 0) ? 0.5 : 1, cursor: (!playerAlliance || playerAlliance.members.length === 0) ? 'not-allowed' : 'pointer', textAlign: 'center', padding: '10px' }}>
          <div style={{ fontSize: '16px', marginBottom: '4px' }}>❌</div>
          <div style={{ fontWeight: 'bold', color: '#fff', fontSize: '10px' }}>Remove Party</div>
        </button>
        
        <button className="nwr-card" disabled={!playerAlliance} onClick={handleDissolveAlliance}
          style={{ opacity: !playerAlliance ? 0.5 : 1, cursor: !playerAlliance ? 'not-allowed' : 'pointer', textAlign: 'center', padding: '10px', border: '1px solid rgba(239,68,68,0.3)' }}>
          <div style={{ fontSize: '16px', marginBottom: '4px' }}>💥</div>
          <div style={{ fontWeight: 'bold', color: '#ef4444', fontSize: '10px' }}>Dissolve Alliance</div>
        </button>

        <button className="nwr-card" disabled={!!playerAlliance} onClick={handleLeaveAlliance}
          style={{ opacity: !!playerAlliance ? 0.5 : 1, cursor: !playerAlliance ? 'not-allowed' : 'pointer', textAlign: 'center', padding: '10px' }}>
          <div style={{ fontSize: '16px', marginBottom: '4px' }}>🚪</div>
          <div style={{ fontWeight: 'bold', color: '#fff', fontSize: '10px' }}>Leave Alliance</div>
        </button>

        <button className="nwr-card" disabled={!playerAlliance || playerAlliance.members.length < 1} onClick={openReallocateModal}
          style={{ opacity: (!playerAlliance || playerAlliance.members.length < 1) ? 0.5 : 1, cursor: (!playerAlliance || playerAlliance.members.length < 1) ? 'not-allowed' : 'pointer', textAlign: 'center', padding: '10px' }}>
          <div style={{ fontSize: '16px', marginBottom: '4px' }}>🔄</div>
          <div style={{ fontWeight: 'bold', color: '#fff', fontSize: '10px' }}>Reallocate Resources</div>
        </button>
      </div>

      {renderLoading()}
      {renderMessages()}

      {/* Section 3 - Current Members */}
      {playerAlliance && playerAlliance.members.length > 0 && (
        <div className="nwr-card" style={{ padding: '14px' }}>
          <h3 className="nwr-section-title">Current Alliance Members</h3>
          <div style={{ overflowX: 'auto' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '10px' }}>
              <thead>
                <tr style={{ borderBottom: '1px solid #334155', color: '#94a3b8' }}>
                  <th style={{ padding: '8px' }}>Party</th>
                  <th style={{ padding: '8px' }}>Seats</th>
                  <th style={{ padding: '8px' }}>Morale</th>
                  <th style={{ padding: '8px' }}>Joining Bonus</th>
                  <th style={{ padding: '8px' }}>Cabinet</th>
                  <th style={{ padding: '8px' }}>State</th>
                  <th style={{ padding: '8px' }}>Status</th>
                  <th style={{ padding: '8px' }}>Action</th>
                </tr>
              </thead>
              <tbody>
                {playerAlliance.members.map(member => {
                  const details = getPartyDetails(member.partyKey);
                  return (
                    <tr key={member.partyKey} style={{ borderBottom: '1px solid #1e293b' }}>
                      <td style={{ padding: '8px', fontWeight: 'bold', color: details.color }}>{details.name}</td>
                      <td style={{ padding: '8px' }}>{details.seats}</td>
                      <td style={{ padding: '8px', color: details.morale > 70 ? '#10b981' : details.morale > 40 ? '#fbbf24' : '#ef4444' }}>{details.morale}%</td>
                      <td style={{ padding: '8px' }}>₹{Number(member.contract?.joiningBonus || 0).toFixed(1)} Cr</td>
                      <td style={{ padding: '8px' }}>{member.contract?.cabinetMinistersPromised || 0}</td>
                      <td style={{ padding: '8px' }}>{member.contract?.stateMinistersPromised || 0}</td>
                      <td style={{ padding: '8px' }}>
                        {member.contract?.isBroken ? <span style={{ color: '#ef4444', fontWeight: 'bold' }}>⚠️ BREACHED</span> : <span style={{ color: '#10b981' }}>Active</span>}
                      </td>
                      <td style={{ padding: '8px' }}>
                        {member.partyKey.toLowerCase() === playerAlliance.leaderPartyKey.toLowerCase() ? (
                          <span style={{ fontSize: '8px', fontWeight: '800', color: '#38bdf8', backgroundColor: 'rgba(56, 189, 248, 0.15)', padding: '2px 6px', borderRadius: '4px' }}>
                            LEADER
                          </span>
                        ) : (
                          <button onClick={() => { setSelectedPartyKey(member.partyKey); setActiveModal('remove'); }}
                            style={{ background: 'transparent', border: '1px solid #ef4444', color: '#ef4444', padding: '3px 6px', borderRadius: '4px', cursor: 'pointer', fontSize: '9px' }}>
                            ❌
                          </button>
                        )}
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Section 4 - Pending Requests */}
      {incomingRequests.length > 0 && (
        <div className="nwr-card" style={{ padding: '14px', border: '1px solid #fbbf24' }}>
          <h3 className="nwr-section-title" style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            📋 Incoming Coalition Requests
            <span style={{ background: '#ef4444', color: '#fff', fontSize: '8.5px', padding: '1px 6px', borderRadius: '8px' }}>{incomingRequests.length}</span>
          </h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
            {incomingRequests.map(req => {
              const details = getPartyDetails(req.fromPartyKey);
              return (
                <div key={req.requestId || req.id} style={{ background: 'rgba(15,23,42,0.5)', padding: '10px', borderRadius: '8px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <div>
                    <strong style={{ color: details.color, fontSize: '11px' }}>{details.name}</strong> requests to join!
                    <div style={{ fontSize: '9.5px', color: '#cbd5e1', marginTop: '4px', display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
                      <span>Joining Bonus: ₹{Number(req.requestedJoiningBonus || req.terms?.joiningBonus || 0).toFixed(1)} Cr</span>
                      <span>Cabinet: {req.requestedCabinetMinisters || req.terms?.cabinetMinistersPromised || 0} posts</span>
                      <span>State: {req.requestedStateMinisters || req.terms?.stateMinistersPromised || 0} posts</span>
                    </div>
                  </div>
                  <div style={{ display: 'flex', gap: '8px' }}>
                    <button onClick={() => handleRespondRequest(req.requestId || req.id, true)} style={{ background: '#10b981', color: '#fff', border: 'none', padding: '6px 12px', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold', fontSize: '9.5px' }}>✅ Accept</button>
                    <button onClick={() => handleRespondRequest(req.requestId || req.id, false)} style={{ background: '#ef4444', color: '#fff', border: 'none', padding: '6px 12px', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold', fontSize: '9.5px' }}>❌ Reject</button>
                  </div>
                </div>
              )
            })}
          </div>
        </div>
      )}

      {/* Section 5 - Available Parties (Visible only when Invite for coalition is clicked) */}
      {showInviteSection && (
        <div className="nwr-card" style={{ padding: '14px', border: '1.5px solid rgba(56, 189, 248, 0.4)', boxShadow: '0 8px 24px rgba(0, 0, 0, 0.4)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px', flexWrap: 'wrap', gap: '8px' }}>
            <div>
              <h3 className="nwr-section-title" style={{ margin: 0 }}>🏛️ Invite for coalition</h3>
              <p style={{ margin: '3px 0 0 0', fontSize: '8.5px', color: '#94a3b8' }}>
                Select an unaligned party below to offer a joining bonus and ministerial portfolios.
              </p>
            </div>
            <button
              onClick={() => setShowInviteSection(false)}
              style={{
                background: 'rgba(255, 255, 255, 0.08)',
                border: '1px solid rgba(255, 255, 255, 0.15)',
                color: '#cbd5e1',
                padding: '4px 10px',
                borderRadius: '6px',
                fontSize: '9px',
                fontWeight: '700',
                cursor: 'pointer'
              }}
            >
              ✕ Close
            </button>
          </div>
          {availableParties.length === 0 ? (
            <p style={{ color: '#94a3b8', fontSize: '9.5px' }}>No unaligned parties available.</p>
          ) : (
            <div className="nwr-grid-4">
            {availableParties.map(party => {
              const details = getPartyDetails(party.partyKey);
              return (
                <div key={party.partyKey} style={{ background: '#0f172a', padding: '10px', borderRadius: '8px', border: `1px solid ${details.color}40`, display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
                  <div>
                    <h4 style={{ margin: '0 0 5px 0', color: details.color, fontSize: '10.5px' }}>{details.name}</h4>
                    <div style={{
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'space-between',
                      backgroundColor: 'rgba(0, 0, 0, 0.3)',
                      padding: '3px 6px',
                      borderRadius: '4px',
                      marginBottom: '7px',
                      fontSize: '8px'
                    }}>
                      <span style={{ color: '#94a3b8', fontWeight: '700' }}>Alliance:</span>
                      <span style={{ color: '#a855f7', fontWeight: '800' }}>Unaligned</span>
                    </div>
                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '3px', textAlign: 'center', marginBottom: '6px' }}>
                      <div className="nwr-stat-box" style={{ padding: '3px 2px' }}>
                        <div style={{ fontSize: '6px', color: '#94a3b8', fontWeight: '800' }}>🪑 SEATS</div>
                        <div style={{ fontSize: '9.5px', fontWeight: '900', color: '#38bdf8' }}>{details.seats}</div>
                      </div>
                      <div className="nwr-stat-box" style={{ padding: '3px 2px' }}>
                        <div style={{ fontSize: '6px', color: '#94a3b8', fontWeight: '800' }}>❤️ MOR</div>
                        <div style={{ fontSize: '9.5px', fontWeight: '900', color: details.morale > 70 ? '#10b981' : details.morale > 40 ? '#fbbf24' : '#ef4444' }}>{details.morale}%</div>
                      </div>
                      <div className="nwr-stat-box" style={{ padding: '3px 2px' }}>
                        <div style={{ fontSize: '6px', color: '#94a3b8', fontWeight: '800' }}>💰 FND</div>
                        <div style={{ fontSize: '9px', fontWeight: '900', color: '#f59e0b' }}>₹{Number(details.funds || 0).toFixed(1)}Cr</div>
                      </div>
                      <div className="nwr-stat-box" style={{ padding: '3px 2px' }}>
                        <div style={{ fontSize: '6px', color: '#94a3b8', fontWeight: '800' }}>⚖️ CRP</div>
                        <div style={{ fontSize: '9px', fontWeight: '900', color: (details.corruption || 0) > 40 ? '#ef4444' : (details.corruption || 0) > 20 ? '#fbbf24' : '#10b981' }}>{details.corruption || 0}%</div>
                      </div>
                    </div>
                    {/* Cadre Base: 👷 WRK | 🤝 VOL | 💳 DON */}
                    <div style={{
                      display: 'grid',
                      gridTemplateColumns: 'repeat(3, 1fr)',
                      gap: '3px',
                      backgroundColor: 'rgba(0, 0, 0, 0.25)',
                      padding: '4px 3px',
                      borderRadius: '4px',
                      marginBottom: '7px',
                      textAlign: 'center'
                    }}>
                      <div>
                        <div style={{ fontSize: '6px', color: '#94a3b8', fontWeight: '800' }}>👷 WRK</div>
                        <div style={{ fontSize: '8px', fontWeight: '800', color: '#cbd5e1' }}>
                          {details.workers >= 100000 ? `${(details.workers / 100000).toFixed(1)}L` : (details.workers || 0).toLocaleString()}
                        </div>
                      </div>
                      <div>
                        <div style={{ fontSize: '6px', color: '#94a3b8', fontWeight: '800' }}>🤝 VOL</div>
                        <div style={{ fontSize: '8px', fontWeight: '800', color: '#cbd5e1' }}>
                          {details.volunteers >= 100000 ? `${(details.volunteers / 100000).toFixed(1)}L` : (details.volunteers || 0).toLocaleString()}
                        </div>
                      </div>
                      <div>
                        <div style={{ fontSize: '6px', color: '#94a3b8', fontWeight: '800' }}>💳 DON</div>
                        <div style={{ fontSize: '8px', fontWeight: '800', color: '#cbd5e1' }}>
                          {details.donors >= 1000 ? `${(details.donors / 1000).toFixed(1)}k` : (details.donors || 0).toLocaleString()}
                        </div>
                      </div>
                    </div>
                  </div>
                  <button 
                    disabled={!playerAlliance}
                    onClick={() => openInviteModal(party.partyKey)}
                    style={{ width: '100%', padding: '5px 8px', background: playerAlliance ? '#38bdf8' : '#334155', color: '#fff', border: 'none', borderRadius: '6px', cursor: playerAlliance ? 'pointer' : 'not-allowed', fontWeight: 'bold', fontSize: '9.5px', marginTop: '6px' }}
                  >
                    Invite
                  </button>
                </div>
              );
            })}
          </div>
        )}
      </div>
      )}

      {/* MODALS */}
      
      {/* Create Alliance Modal */}
      {activeModal === 'create' && (
        <div style={modalStyle}>
          <div style={modalContentStyle}>
            <h3 style={{ margin: '0 0 12px 0', color: '#fff', fontSize: '12px' }}>Create New Alliance</h3>
            <label style={labelStyle}>Alliance Name</label>
            <input type="text" value={createForm.allianceName} onChange={e => setCreateForm({...createForm, allianceName: e.target.value})} style={inputStyle} placeholder="e.g. National Democratic Alliance" />
            <label style={labelStyle}>Theme Color</label>
            <input type="color" value={createForm.color} onChange={e => setCreateForm({...createForm, color: e.target.value})} style={{...inputStyle, padding: '2px', height: '30px'}} />
            <div style={{ display: 'flex', gap: '8px', marginTop: '16px' }}>
              <button onClick={handleCreateAlliance} style={{ flex: 1, padding: '7px', background: '#38bdf8', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold', fontSize: '10px' }}>Create</button>
              <button onClick={() => setActiveModal(null)} style={{ flex: 1, padding: '7px', background: '#334155', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold', fontSize: '10px' }}>Cancel</button>
            </div>
          </div>
        </div>
      )}

      {/* Invite Party Modal */}
      {activeModal === 'invite' && selectedPartyKey && (
        <div style={modalStyle}>
          <div style={modalContentStyle}>
            {(() => {
              const details = getPartyDetails(selectedPartyKey);
              let accMsg = '';
              let accColor = '';
              if (details.morale < 35) { accMsg = "🟢 HIGH acceptance likelihood — party is struggling"; accColor = "#10b981"; }
              else if (details.morale < 50) { accMsg = "🟡 MODERATE likelihood — open to offers with good terms"; accColor = "#fbbf24"; }
              else if (details.morale < 80) { accMsg = "🔴 LOW likelihood — will need strong terms to sway them"; accColor = "#ef4444"; }
              else { accMsg = "⛔ Will almost certainly REFUSE — high morale & confident independence"; accColor = "#ef4444"; }

              const currentFunds = playerPartyFunds;
              const remainingFunds = currentFunds - inviteForm.joiningBonus;
              const maxCabinet = Math.max(0, 20 - (playerAlliance?.totalCabinetPromised ?? totalCabinet));
              const maxState = Math.max(0, 50 - (playerAlliance?.totalStatePromised ?? totalState));

              // Compute bonus as % of target's funds for the live AI hint
              const targetFunds = Math.max(1, details.funds || 1);
              const bonusPct = ((inviteForm.joiningBonus / targetFunds) * 100).toFixed(0);
              const bonusPctColor = bonusPct >= 40 ? '#10b981' : bonusPct >= 20 ? '#fbbf24' : '#94a3b8';

              return (
                <>
                  <h3 style={{ margin: '0 0 6px 0', color: details.color, fontSize: '12px' }}>Invite {details.name}</h3>
                  <div style={{ fontSize: '9px', color: '#cbd5e1', marginBottom: '4px', display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
                    <span>🪑 Seats: <strong style={{ color: '#fff' }}>{details.seats}</strong></span>
                    <span>⚡ Morale: <strong style={{ color: details.morale > 70 ? '#10b981' : details.morale > 40 ? '#fbbf24' : '#ef4444' }}>{details.morale}%</strong></span>
                    <span>💰 Funds: <strong style={{ color: '#f59e0b' }}>₹{Number(details.funds || 0).toFixed(1)} Cr</strong></span>
                  </div>
                  <div style={{ fontSize: '8px', color: '#94a3b8', marginBottom: '8px', display: 'flex', gap: '8px', backgroundColor: 'rgba(0,0,0,0.2)', padding: '3px 6px', borderRadius: '4px' }}>
                    <span>Workers: <strong style={{ color: '#cbd5e1' }}>{details.workers >= 100000 ? `${(details.workers / 100000).toFixed(1)}L` : (details.workers || 0).toLocaleString()}</strong></span>
                    <span>Volunteers: <strong style={{ color: '#cbd5e1' }}>{details.volunteers >= 100000 ? `${(details.volunteers / 100000).toFixed(1)}L` : (details.volunteers || 0).toLocaleString()}</strong></span>
                    <span>Donors: <strong style={{ color: '#cbd5e1' }}>{details.donors >= 1000 ? `${(details.donors / 1000).toFixed(1)}k` : (details.donors || 0).toLocaleString()}</strong></span>
                  </div>

                  <div style={{ padding: '6px', background: 'rgba(0,0,0,0.2)', borderRadius: '6px', marginBottom: '10px', color: accColor, fontSize: '9.5px', fontWeight: 'bold' }}>
                    {accMsg}
                  </div>

                  <label style={labelStyle}>Joining Bonus (₹ Cr)</label>
                  <input type="number" step="0.1" min="0" value={inviteForm.joiningBonus} onChange={e => setInviteForm({...inviteForm, joiningBonus: parseFloat(e.target.value) || 0})} style={inputStyle} />
                  {/* Live % hint — AI scores bonus relative to target's funds */}
                  <div style={{ fontSize: '8.5px', color: bonusPctColor, marginBottom: '8px', marginTop: '-4px' }}>
                    💡 That's <strong>{bonusPct}%</strong> of their ₹{Number(targetFunds).toFixed(1)} Cr treasury
                    {bonusPct >= 40 ? ' — very attractive to them' : bonusPct >= 20 ? ' — a meaningful offer' : bonusPct > 0 ? ' — consider increasing for better odds' : ''}
                  </div>

                  <div style={{ display: 'flex', gap: '10px' }}>
                    <div style={{ flex: 1 }}>
                      <label style={labelStyle}>Cabinet Ministers (Max: {maxCabinet})</label>
                      <input type="number" min="0" max={maxCabinet} value={inviteForm.cabinetMinistersPromised} onChange={e => setInviteForm({...inviteForm, cabinetMinistersPromised: parseInt(e.target.value) || 0})} style={inputStyle} />
                    </div>
                    <div style={{ flex: 1 }}>
                      <label style={labelStyle}>State Ministers (Max: {maxState})</label>
                      <input type="number" min="0" max={maxState} value={inviteForm.stateMinistersPromised} onChange={e => setInviteForm({...inviteForm, stateMinistersPromised: parseInt(e.target.value) || 0})} style={inputStyle} />
                    </div>
                  </div>

                  <div style={{ margin: '10px 0', fontSize: '9.5px', color: remainingFunds < 0 ? '#ef4444' : '#10b981' }}>
                    Party treasury after bonus: ₹{Number(remainingFunds).toFixed(1)} Cr (Current: ₹{Number(currentFunds).toFixed(1)} Cr)
                  </div>

                  <div style={{ display: 'flex', gap: '8px' }}>
                    <button onClick={handleInviteParty} style={{ flex: 1, padding: '7px', background: '#38bdf8', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold', fontSize: '10px' }}>Send Invitation</button>
                    <button onClick={() => setActiveModal(null)} style={{ flex: 1, padding: '7px', background: '#334155', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold', fontSize: '10px' }}>Cancel</button>
                  </div>
                </>
              );
            })()}
          </div>
        </div>

      )}

      {/* Remove Party Modal */}
      {activeModal === 'remove' && (
        <div style={modalStyle}>
          <div style={modalContentStyle}>
            <h3 style={{ margin: '0 0 10px 0', color: '#ef4444', fontSize: '12px' }}>Remove Party from Alliance</h3>
            <p style={{ color: '#cbd5e1', fontSize: '9.5px', marginBottom: '10px' }}>
              Warning: Removing a party breaks their contract. -25 morale for them, -5 for you.
            </p>
            <label style={labelStyle}>Select Party to Remove</label>
            <select value={selectedPartyKey} onChange={e => setSelectedPartyKey(e.target.value)} style={{...inputStyle, height: '32px'}}>
              <option value="">-- Select --</option>
              {playerAlliance?.members.map(m => (
                <option key={m.partyKey} value={m.partyKey}>{getPartyDetails(m.partyKey).name}</option>
              ))}
            </select>
            <div style={{ display: 'flex', gap: '8px', marginTop: '16px' }}>
              <button onClick={handleRemoveParty} style={{ flex: 1, padding: '7px', background: '#ef4444', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold', fontSize: '10px' }}>Confirm Removal</button>
              <button onClick={() => setActiveModal(null)} style={{ flex: 1, padding: '7px', background: '#334155', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold', fontSize: '10px' }}>Cancel</button>
            </div>
          </div>
        </div>
      )}

      {/* Reallocate Resources Modal */}
      {activeModal === 'reallocate' && (
        <div style={modalStyle}>
          <div style={{...modalContentStyle, minWidth: '340px'}}>
            <h3 style={{ margin: '0 0 10px 0', color: '#fff', fontSize: '12px' }}>Reallocate Resources</h3>
            <div style={{ maxHeight: '300px', overflowY: 'auto' }}>
              {reallocateForm.map((alloc, idx) => {
                const details = getPartyDetails(alloc.partyKey);
                return (
                  <div key={alloc.partyKey} style={{ background: '#0f172a', padding: '10px', borderRadius: '6px', marginBottom: '8px' }}>
                    <div style={{ fontWeight: 'bold', color: details.color, marginBottom: '6px', fontSize: '10px' }}>{details.name}</div>
                    <div style={{ display: 'flex', gap: '8px' }}>
                      <div style={{ flex: 1 }}>
                        <label style={labelStyle}>Cabinet Ministers</label>
                        <input type="number" min="0" value={alloc.cabinetMinistersPromised} onChange={e => {
                          const newForm = [...reallocateForm];
                          newForm[idx].cabinetMinistersPromised = parseInt(e.target.value) || 0;
                          setReallocateForm(newForm);
                        }} style={inputStyle} />
                      </div>
                      <div style={{ flex: 1 }}>
                        <label style={labelStyle}>State Ministers</label>
                        <input type="number" min="0" value={alloc.stateMinistersPromised} onChange={e => {
                          const newForm = [...reallocateForm];
                          newForm[idx].stateMinistersPromised = parseInt(e.target.value) || 0;
                          setReallocateForm(newForm);
                        }} style={inputStyle} />
                      </div>
                    </div>
                  </div>
                )
              })}

            </div>
            
            {(() => {
              const currentTotalCab = reallocateForm.reduce((s, a) => s + a.cabinetMinistersPromised, 0);
              const currentTotalState = reallocateForm.reduce((s, a) => s + a.stateMinistersPromised, 0);
              return (
                <div style={{ display: 'flex', gap: '16px', margin: '10px 0', padding: '8px', background: 'rgba(0,0,0,0.2)', borderRadius: '6px', fontSize: '9px' }}>
                  <div style={{ color: currentTotalCab > 20 ? '#ef4444' : '#fff' }}>Total Cabinet: {currentTotalCab} / 20</div>
                  <div style={{ color: currentTotalState > 50 ? '#ef4444' : '#fff' }}>Total State: {currentTotalState} / 50</div>
                </div>
              );
            })()}

            <div style={{ display: 'flex', gap: '8px' }}>
              <button onClick={handleReallocate} style={{ flex: 1, padding: '7px', background: '#38bdf8', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold', fontSize: '10px' }}>Save Allocations</button>
              <button onClick={() => setActiveModal(null)} style={{ flex: 1, padding: '7px', background: '#334155', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold', fontSize: '10px' }}>Cancel</button>
            </div>
          </div>
        </div>
      )}

    </div>
  );
}
