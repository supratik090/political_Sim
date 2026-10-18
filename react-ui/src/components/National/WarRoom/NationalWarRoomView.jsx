import React, { useState, useEffect, useCallback } from 'react';
import { useGameStore } from '../../../store/gameStore';
import { fetchNationalConfigs, getNationalGame, advanceNationalSeason } from '../../../api/apiClient';

import NationalWR_TabBar from './NationalWR_TabBar';
import NationalWR_Intelligence from './NationalWR_Intelligence';
import NationalWR_Operations from './NationalWR_Operations';
import NationalWR_Hints from './NationalWR_Hints';
import NationalElectionVerdictModal from './NationalElectionVerdictModal';
import NationalTurnDebriefModal from './NationalTurnDebriefModal';

import './national_warroom.css';

export default function NationalWarRoomView({ onReturnToHeadquarters }) {
  const {
    activeNationalGame,
    setActiveNationalGame,
    activeNationalTab,
    setActiveNationalTab
  } = useGameStore();

  const activeTab = activeNationalTab || 'intelligence';
  const setActiveTab = setActiveNationalTab;
  const [configData, setConfigData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [gameState, setGameState] = useState(activeNationalGame);
  const [advancingSeason, setAdvancingSeason] = useState(false);
  const [showVerdictModal, setShowVerdictModal] = useState(Boolean(activeNationalGame?.nationalElectionResult));
  const [turnDebriefData, setTurnDebriefData] = useState(null);
  const [showDebriefModal, setShowDebriefModal] = useState(false);
  const [highlightProjectedSeats, setHighlightProjectedSeats] = useState(false);
  const [completedActions, setCompletedActions] = useState({});
  const [lastSeason, setLastSeason] = useState(gameState?.currentSeason);
  const [operationsSubTab, setOperationsSubTab] = useState('coalition');

  const handleNavigateTab = (tab, subTab) => {
    if (tab) {
      setActiveTab(tab);
    }
    if (subTab) {
      setOperationsSubTab(subTab);
    }
  };

  // Reset completed manual actions when season advances
  useEffect(() => {
    if (gameState?.currentSeason !== undefined && gameState.currentSeason !== lastSeason) {
      setLastSeason(gameState.currentSeason);
      setCompletedActions({});
    }
  }, [gameState?.currentSeason, lastSeason]);

  const markStepComplete = React.useCallback((key, status = true) => {
    setCompletedActions(prev => {
      if (prev[key] === status) return prev;
      return {
        ...prev,
        [key]: status
      };
    });
  }, []);

  // Authoritative 4-step completion checks
  const isCoalitionDone = Boolean(
    completedActions['coalition_hub'] ||
    (gameState?.pendingRequests && gameState.pendingRequests.some(r => r.turn === gameState?.currentSeason || r.status === 'ACCEPTED' || r.status === 'REJECTED'))
  );

  const isFinanceDone = Boolean(
    gameState?.committedFinanceCard ||
    completedActions['finance_ops']
  );

  const isEventsDone = Boolean(
    (gameState?.resolvedEventReactions && Object.keys(gameState.resolvedEventReactions).length > 0) ||
    gameState?.activeThemeAction ||
    completedActions['events_ops']
  );

  const allStatesCompleted = Boolean(
    gameState?.stateOperations &&
    Object.keys(gameState.stateOperations).length > 0 &&
    (() => {
      const eligible = Object.values(gameState.stateOperations).filter(s => s.isEligible !== false && s.isActive !== false);
      return eligible.length === 0 || eligible.every(s => s.doneThisTurn || s.skippedThisTurn);
    })()
  );

  const isStatesDone = Boolean(allStatesCompleted || completedActions['states_ops']);

  const doneCount = [isCoalitionDone, isFinanceDone, isEventsDone, isStatesDone].filter(Boolean).length;
  const isAllFourDone = doneCount === 4;

  useEffect(() => {
    if (gameState?.nationalElectionResult) {
      setShowVerdictModal(true);
    }
  }, [gameState?.nationalElectionResult]);

  const buildTurnDebrief = (prevGame, updatedGame) => {
    if (!prevGame || !updatedGame) return null;

    const completedSeason = prevGame.currentSeason || 1;
    const nextSeason = updatedGame.currentSeason || (completedSeason + 1);

    const playerPartyKey = (updatedGame.partyKey || prevGame.partyKey || 'YDP').toUpperCase();
    const prevParty = (prevGame.partyStates || []).find(p => (p.partyKey || '').toUpperCase() === playerPartyKey);
    const nextParty = (updatedGame.partyStates || []).find(p => (p.partyKey || '').toUpperCase() === playerPartyKey);

    const prevFunds = prevParty?.funds !== undefined ? prevParty.funds : (prevGame.playerFunds || 0);
    const nextFunds = nextParty?.funds !== undefined ? nextParty.funds : (updatedGame.playerFunds || 0);

    const prevMorale = prevParty?.morale !== undefined ? prevParty.morale : 70;
    const nextMorale = nextParty?.morale !== undefined ? nextParty.morale : 70;

    const prevWorkers = prevParty?.workers || 0;
    const nextWorkers = nextParty?.workers || 0;

    const prevVolunteers = prevParty?.volunteers || 0;
    const nextVolunteers = nextParty?.volunteers || 0;

    const prevDonors = prevParty?.donors || 0;
    const nextDonors = nextParty?.donors || 0;

    const prevCorruption = prevParty?.corruption || 0;
    const nextCorruption = nextParty?.corruption || 0;

    const prevProjSeats = (prevGame.nationalProjectedSeats && prevGame.nationalProjectedSeats[playerPartyKey] !== undefined)
      ? prevGame.nationalProjectedSeats[playerPartyKey]
      : (prevParty?.seats || 0);
    const nextProjSeats = (updatedGame.nationalProjectedSeats && updatedGame.nationalProjectedSeats[playerPartyKey] !== undefined)
      ? updatedGame.nationalProjectedSeats[playerPartyKey]
      : (nextParty?.seats || 0);

    // Infrastructure & Buildings
    const newBuildings = [];
    let totalActiveCount = 0;
    let totalNetIncome = 0;

    const prevStates = prevGame.stateOperations || {};
    const nextStates = updatedGame.stateOperations || {};

    Object.keys(nextStates).forEach(sCode => {
      const nState = nextStates[sCode];
      const pState = prevStates[sCode] || {};
      totalNetIncome += nState.netIncomePerTurn || 0;

      // Check state-level buildings
      const nBuildings = nState.buildings || {};
      const pBuildings = pState.buildings || {};
      Object.keys(nBuildings).forEach(bKey => {
        totalActiveCount += nBuildings[bKey] || 0;
        const oldCount = pBuildings[bKey] || 0;
        const newCount = nBuildings[bKey] || 0;
        if (newCount > oldCount) {
          newBuildings.push({
            stateCode: sCode,
            stateName: nState.stateName || sCode,
            buildingName: bKey.replace(/_/g, ' ').toUpperCase(),
            count: newCount - oldCount
          });
        }
      });

      // Check regional wings
      const nRegs = nState.regions || {};
      const pRegs = pState.regions || {};
      Object.keys(nRegs).forEach(rKey => {
        const nr = nRegs[rKey] || {};
        const pr = pRegs[rKey] || {};
        const nWings = nr.wings || {};
        const pWings = pr.wings || {};
        Object.keys(nWings).forEach(wKey => {
          totalActiveCount += nWings[wKey] || 0;
          const oldW = pWings[wKey] || 0;
          const newW = nWings[wKey] || 0;
          if (newW > oldW) {
            newBuildings.push({
              stateCode: sCode,
              stateName: `${nState.stateName || sCode} (${nr.regionName || rKey})`,
              buildingName: wKey.replace(/_/g, ' ').toUpperCase(),
              count: newW - oldW
            });
          }
        });
      });
    });

    // Alliances
    const playerAlliances = updatedGame.alliances || [];
    const playerAlliance = playerAlliances.find(a => (a.leaderPartyKey || '').toUpperCase() === playerPartyKey)
      || playerAlliances.find(a => a.members?.some(m => (m.partyKey || '').toUpperCase() === playerPartyKey));

    const prevAlliance = (prevGame.alliances || []).find(a => a.allianceId === playerAlliance?.allianceId);

    const newJoinedMembers = [];
    if (playerAlliance && playerAlliance.members) {
      const prevMemberKeys = new Set((prevAlliance?.members || []).map(m => (m.partyKey || '').toUpperCase()));
      playerAlliance.members.forEach(m => {
        const mKey = (m.partyKey || '').toUpperCase();
        if (mKey !== playerPartyKey && !prevMemberKeys.has(mKey)) {
          const pState = updatedGame.partyStates?.find(ps => (ps.partyKey || '').toUpperCase() === mKey);
          newJoinedMembers.push({
            partyKey: mKey,
            partyName: pState?.partyName || mKey,
            shortName: pState?.shortName || mKey,
            seats: pState?.seats || 0
          });
        }
      });
    }

    const uniqueAllianceMemberKeys = playerAlliance ? Array.from(new Set([
      playerAlliance.leaderPartyKey,
      ...(playerAlliance.members || []).map(m => m.partyKey)
    ].filter(Boolean))) : [];

    let allianceTotalProjected = 0;
    uniqueAllianceMemberKeys.forEach(mKey => {
      const k = mKey.toUpperCase();
      const p = updatedGame.partyStates?.find(ps => (ps.partyKey || '').toUpperCase() === k);
      const seats = (updatedGame.nationalProjectedSeats && updatedGame.nationalProjectedSeats[k] !== undefined)
        ? updatedGame.nationalProjectedSeats[k]
        : (p?.seats || 0);
      allianceTotalProjected += seats;
    });

    // Newly Unlocked States via Alliance Partner
    const newlyJoinedKeys = new Set(newJoinedMembers.map(m => (m.partyKey || '').toUpperCase()));
    const newlyUnlockedStates = [];

    // State shifts - ONLY include active / eligible states (remove inactive states)!
    const stateShifts = [];
    Object.keys(nextStates).forEach(sCode => {
      const ns = nextStates[sCode];
      const ps = prevStates[sCode];

      // Check if state is active / eligible for player or alliance
      const splits = ns.voteSplits || {};
      const seats = ns.projectedLokSabhaSeats || {};
      const isPlayerDirect = (splits[playerPartyKey] || 0) > 0 || (seats[playerPartyKey] || 0) > 0
        || playerPartyKey === (ns.rulingParty || '').toUpperCase()
        || playerPartyKey === (ns.oppositionParty || '').toUpperCase();

      let unlockedPartner = null;
      let newlyUnlockedPartner = null;
      for (const mKey of uniqueAllianceMemberKeys) {
        const k = (mKey || '').toUpperCase();
        if (k === playerPartyKey) continue;
        const partnerActive = (splits[k] || 0) > 0 || (seats[k] || 0) > 0
          || k === (ns.rulingParty || '').toUpperCase()
          || k === (ns.oppositionParty || '').toUpperCase();
        if (partnerActive) {
          unlockedPartner = k;
          if (newlyJoinedKeys.has(k)) {
            newlyUnlockedPartner = k;
          }
        }
      }

      const isEligible = ns.isEligible !== undefined
        ? Boolean(ns.isEligible)
        : (isPlayerDirect || Boolean(unlockedPartner));

      // If unlocked this turn via newly joined alliance member
      if (!isPlayerDirect && (newlyUnlockedPartner || ns.isNewlyUnlocked)) {
        newlyUnlockedStates.push({
          stateCode: sCode,
          stateName: ns.stateName || sCode,
          unlockedByPartner: newlyUnlockedPartner || ns.unlockedByPartner,
          totalLokSabhaSeats: ns.totalLokSabhaSeats || 0,
          totalAssemblySeats: ns.totalAssemblySeats || 0
        });
      }

      // EXCLUDE inactive states from end of turn modal view!
      if (!isEligible) {
        return;
      }

      const nextSup = ns.supportPercentage || 0;
      const prevSup = ps?.supportPercentage !== undefined ? ps.supportPercentage : nextSup;
      const latestLog = ns.activityLog?.[0]?.detail || null;
      stateShifts.push({
        stateCode: sCode,
        stateName: ns.stateName || sCode,
        support: nextSup,
        deltaSupport: Math.round((nextSup - prevSup) * 10) / 10,
        wasSkipped: ns.skippedThisTurn,
        latestLog
      });
    });

    return {
      completedSeason,
      nextSeason,
      playerPartyName: nextParty?.partyName || playerPartyKey,
      playerStats: {
        funds: { prev: prevFunds, next: nextFunds, delta: Math.round((nextFunds - prevFunds) * 10) / 10 },
        morale: { prev: prevMorale, next: nextMorale, delta: nextMorale - prevMorale },
        workers: { prev: prevWorkers, next: nextWorkers, delta: nextWorkers - prevWorkers },
        volunteers: { prev: prevVolunteers, next: nextVolunteers, delta: nextVolunteers - prevVolunteers },
        donors: { prev: prevDonors, next: nextDonors, delta: nextDonors - prevDonors },
        corruption: { prev: prevCorruption, next: nextCorruption, delta: nextCorruption - prevCorruption },
        projSeats: { prev: prevProjSeats, next: nextProjSeats, delta: nextProjSeats - prevProjSeats }
      },
      alliances: {
        hasPlayerAlliance: Boolean(playerAlliance),
        allianceName: playerAlliance?.allianceName || 'Unaligned',
        allianceColor: playerAlliance?.color || '#38bdf8',
        leaderPartyKey: playerAlliance?.leaderPartyKey || playerPartyKey,
        memberCount: playerAlliance?.members?.length || 1,
        totalProjectedSeats: allianceTotalProjected,
        newJoinedMembers
      },
      buildings: {
        newBuildings,
        totalActiveCount,
        totalNetIncome
      },
      newlyUnlockedStates,
      stateShifts,
      financeReport: updatedGame.lastSeasonFinanceReport,
      eventsReport: updatedGame.activityLog?.find(l => l.season === completedSeason && l.event === 'EVENT_RESOLVED')?.detail || null
    };
  };

  const handleAdvanceSeason = async () => {
    if (!isAllFourDone) {
      alert(`Cannot End Turn: Only ${doneCount}/4 directives completed. You must complete or confirm all 4 stages (Coalition, Finance, Events, and States) before advancing.`);
      return;
    }
    const gameId = gameState?.id || gameState?._id;
    if (!gameId) return;
    setAdvancingSeason(true);
    try {
      const prevSnapshot = JSON.parse(JSON.stringify(gameState));
      const updated = await advanceNationalSeason(gameId);
      if (updated) {
        setCompletedActions({});
        handleGameUpdate(updated);
        // Automatically navigate to Intelligence tab and highlight Lok Sabha projected standings
        setActiveTab('intelligence');
        setHighlightProjectedSeats(true);
        if (!updated.nationalElectionResult) {
          const debrief = buildTurnDebrief(prevSnapshot, updated);
          setTurnDebriefData(debrief);
          setShowDebriefModal(true);
        }
      }
    } catch (err) {
      console.error('Failed to advance national season:', err);
      alert('Could not advance season: ' + (err.message || 'Unknown error'));
    } finally {
      setAdvancingSeason(false);
    }
  };

  useEffect(() => {
    setGameState(activeNationalGame);
  }, [activeNationalGame]);

  // If game state in memory does not have backend id, sync with backend
  useEffect(() => {
    const syncBackendGame = async () => {
      const userId = useGameStore.getState().user?.id || useGameStore.getState().user?.userId || 'local';
      try {
        const remoteGame = await getNationalGame(userId);
        if (remoteGame && (remoteGame.id || remoteGame._id)) {
          const merged = { ...gameState, ...remoteGame };
          setGameState(merged);
          if (setActiveNationalGame) {
            setActiveNationalGame(merged);
          }
        }
      } catch (err) {
        console.warn('Could not sync remote national game:', err);
      }
    };
    if (gameState && !gameState.id && !gameState._id) {
      syncBackendGame();
    }
  }, [gameState?.id]);

  const handleGameUpdate = (updatedGame) => {
    const merged = { ...gameState, ...updatedGame };
    setGameState(merged);
    if (setActiveNationalGame) {
      setActiveNationalGame(merged);
    }
  };

  // Load era config matching active game
  useEffect(() => {
    if (gameState?.era) {
      loadEraConfig(gameState.era);
    }
  }, [gameState?.era]);

  const loadEraConfig = async (era) => {
    setLoading(true);
    try {
      const data = await fetchNationalConfigs();
      if (Array.isArray(data)) {
        const found = data.find(c => c.era === era) || data[0];
        setConfigData(found);
      }
    } catch (err) {
      console.warn('Could not fetch era config for national war room:', err);
    } finally {
      setLoading(false);
    }
  };

  if (!gameState) {
    return (
      <div className="nwr-root" style={{ textAlign: 'center', padding: '60px 20px' }}>
        <h2 style={{ color: '#ef4444' }}>No Active National Campaign</h2>
        <p style={{ color: '#94a3b8' }}>Please initialize a campaign from National Headquarters.</p>
        <button
          onClick={onReturnToHeadquarters}
          style={{
            backgroundColor: '#0284c7', border: 'none', color: '#ffffff',
            padding: '12px 24px', borderRadius: '8px', fontWeight: '800', cursor: 'pointer',
            marginTop: '16px'
          }}
        >
          ← Back
        </button>
      </div>
    );
  }

  return (
    <div className="nwr-root">
      
      {/* Top Command Bar */}
      <div style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        flexWrap: 'wrap',
        gap: '12px',
        marginBottom: '16px',
        paddingBottom: '14px',
        borderBottom: '1px solid rgba(56, 189, 248, 0.2)'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          {onReturnToHeadquarters && (
            <button
              onClick={onReturnToHeadquarters}
              title="Return to Headquarters"
              style={{
                backgroundColor: 'rgba(56, 189, 248, 0.1)',
                border: '1px solid rgba(56, 189, 248, 0.3)',
                color: '#38bdf8',
                padding: '5px 10px',
                borderRadius: '8px',
                fontSize: '11px',
                fontWeight: '800',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '4px',
                transition: 'all 0.2s'
              }}
            >
              ← Back
            </button>
          )}
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <div style={{
              width: '28px', height: '28px', borderRadius: '6px',
              backgroundColor: gameState.partyColor || '#7C3AED',
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              fontSize: '14px', boxShadow: '0 0 10px rgba(124, 58, 237, 0.4)'
            }}>
              🏛️
            </div>
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                <h1 style={{ margin: 0, fontSize: '14px', fontWeight: '900', color: '#ffffff' }}>
                  {gameState.partyName} ({gameState.partyShortName})
                </h1>
                <span className="nwr-badge nwr-badge-cyan">
                  Era {gameState.era}
                </span>
              </div>
              <div style={{ fontSize: '9px', color: '#94a3b8', marginTop: '2px' }}>
                National Command War Room • Alliance: <strong style={{ color: (gameState?.alliances?.find(a => (a.leaderPartyKey || '').toLowerCase() === (gameState?.partyKey || '').toLowerCase()) || (gameState.allianceKey && gameState.allianceKey !== 'INDEPENDENT' && gameState.allianceKey !== 'UNALIGNED')) ? '#38bdf8' : '#a855f7' }}>
                  {gameState?.alliances?.find(a => (a.leaderPartyKey || '').toLowerCase() === (gameState?.partyKey || '').toLowerCase())?.allianceName || ((gameState.allianceKey && gameState.allianceKey !== 'INDEPENDENT' && gameState.allianceKey !== 'UNALIGNED') ? gameState.allianceKey : 'None (Independent / Unaligned)')}
                </strong>
              </div>
            </div>
          </div>
        </div>

        {/* Player Stats & Turn Bar */}
        <div style={{ display: 'flex', gap: '8px', alignItems: 'center', flexWrap: 'wrap' }}>
          {(() => {
            const playerParty = (gameState?.partyStates || []).find(p => 
              (p.partyKey || p.id || '').toLowerCase() === (gameState?.partyKey || '').toLowerCase()
            );
            const displaySeats = playerParty?.seats ?? gameState?.seats ?? 0;
            const displayMorale = playerParty?.morale ?? gameState?.morale ?? gameState?.content ?? 70;
            const displayFunds = playerParty?.funds != null ? Number(playerParty.funds).toFixed(1) : (gameState?.playerFunds != null ? Number(gameState.playerFunds).toFixed(1) : '0.0');
            const displayCorruption = playerParty?.corruption ?? gameState?.playerCorruption ?? 0;
            
            const deltaSeats = playerParty?.deltaSeats || 0;
            const deltaMorale = playerParty?.deltaMorale || 0;
            const deltaFunds = playerParty?.deltaFunds || 0.0;
            const deltaCorruption = playerParty?.deltaCorruption || 0;

            return (
              <>
                <div className="nwr-stat-box" style={{ minWidth: '65px' }}>
                  <div style={{ fontSize: '8px', color: '#94a3b8', fontWeight: '700' }}>🪑 SEATS</div>
                  <div style={{ display: 'flex', alignItems: 'baseline', gap: '3px', justifyContent: 'center' }}>
                    <span style={{ fontSize: '13px', fontWeight: '900', color: '#38bdf8' }}>{displaySeats}</span>
                    {deltaSeats !== 0 && (
                      <span style={{ fontSize: '8.5px', fontWeight: '800', color: deltaSeats > 0 ? '#10b981' : '#ef4444' }}>
                        {deltaSeats > 0 ? `+${deltaSeats}▲` : `${deltaSeats}▼`}
                      </span>
                    )}
                  </div>
                </div>
                <div className="nwr-stat-box" style={{ minWidth: '65px' }}>
                  <div style={{ fontSize: '8px', color: '#94a3b8', fontWeight: '700' }}>❤️ MORALE</div>
                  <div style={{ display: 'flex', alignItems: 'baseline', gap: '3px', justifyContent: 'center' }}>
                    <span style={{ fontSize: '13px', fontWeight: '900', color: '#10b981' }}>{displayMorale}%</span>
                    {deltaMorale !== 0 && (
                      <span style={{ fontSize: '8.5px', fontWeight: '800', color: deltaMorale > 0 ? '#10b981' : '#ef4444' }}>
                        {deltaMorale > 0 ? `+${deltaMorale}%▲` : `${deltaMorale}%▼`}
                      </span>
                    )}
                  </div>
                </div>
                <div className="nwr-stat-box" style={{ minWidth: '75px' }}>
                  <div style={{ fontSize: '8px', color: '#94a3b8', fontWeight: '700' }}>💰 FUNDS</div>
                  <div style={{ display: 'flex', alignItems: 'baseline', gap: '3px', justifyContent: 'center' }}>
                    <span style={{ fontSize: '13px', fontWeight: '900', color: '#f59e0b' }}>
                      ₹{displayFunds}Cr
                    </span>
                    {deltaFunds !== 0 && (
                      <span style={{ fontSize: '8.5px', fontWeight: '800', color: deltaFunds > 0 ? '#10b981' : '#ef4444' }}>
                        {deltaFunds > 0 ? `+₹${deltaFunds.toFixed(1)}▲` : `-₹${Math.abs(deltaFunds).toFixed(1)}▼`}
                      </span>
                    )}
                  </div>
                </div>
                <div className="nwr-stat-box" style={{ minWidth: '65px' }}>
                  <div style={{ fontSize: '8px', color: '#94a3b8', fontWeight: '700' }}>⚖️ CORRUPTION</div>
                  <div style={{ display: 'flex', alignItems: 'baseline', gap: '3px', justifyContent: 'center' }}>
                    <span style={{
                      fontSize: '13px',
                      fontWeight: '900',
                      color: displayCorruption > 40 ? '#ef4444' : displayCorruption > 20 ? '#fbbf24' : '#10b981'
                    }}>
                      {displayCorruption}%
                    </span>
                    {deltaCorruption !== 0 && (
                      <span style={{ fontSize: '8.5px', fontWeight: '800', color: deltaCorruption > 0 ? '#ef4444' : '#10b981' }}>
                        {deltaCorruption > 0 ? `+${deltaCorruption}%⚠️` : `${deltaCorruption}%▼`}
                      </span>
                    )}
                  </div>
                </div>
              </>
            );
          })()}

          <div style={{
            height: '28px',
            width: '1px',
            backgroundColor: 'rgba(56, 189, 248, 0.2)',
            margin: '0 2px'
          }} />

          {/* Turn / Season Box & Flashing End Turn Button */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <div className="nwr-stat-box" style={{ minWidth: '70px', background: 'rgba(56, 189, 248, 0.08)', border: '1px solid rgba(56, 189, 248, 0.35)' }}>
              <div style={{ fontSize: '8px', color: '#38bdf8', fontWeight: '800' }}>🗓️ TURN</div>
              <div style={{ fontSize: '13px', fontWeight: '900', color: '#ffffff' }}>
                Turn {gameState?.currentSeason || 1}
              </div>
            </div>

            <button
              onClick={handleAdvanceSeason}
              disabled={advancingSeason || !isAllFourDone}
              className={isAllFourDone ? 'nwr-end-turn-flashing' : ''}
              style={{
                background: isAllFourDone
                  ? 'linear-gradient(135deg, #f59e0b 0%, #ea580c 50%, #0284c7 100%)'
                  : 'linear-gradient(135deg, #1e293b 0%, #0f172a 100%)',
                border: isAllFourDone
                  ? '2px solid #fbbf24'
                  : '1px solid rgba(255, 255, 255, 0.15)',
                color: isAllFourDone ? '#ffffff' : '#64748b',
                padding: isAllFourDone ? '7px 16px' : '6px 12px',
                borderRadius: '8px',
                fontSize: '11px',
                fontWeight: '900',
                cursor: (!isAllFourDone || advancingSeason) ? 'not-allowed' : 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '6px',
                boxShadow: isAllFourDone
                  ? '0 0 20px rgba(245, 158, 11, 0.6)'
                  : 'none',
                transition: 'all 0.2s',
                opacity: advancingSeason ? 0.7 : (isAllFourDone ? 1 : 0.45)
              }}
              title={isAllFourDone ? 'All 4 operations complete! Click to End Turn & resolve season.' : `Operations in progress (${doneCount}/4 done). Complete Coalition, Finance, Events & States to enable End Turn.`}
            >
              {advancingSeason ? (
                '⏳ Resolving...'
              ) : isAllFourDone ? (
                <>
                  <span>⚡</span>
                  <span>END TURN →</span>
                </>
              ) : (
                <>
                  <span style={{ fontSize: '10px', color: '#94a3b8' }}>🔒 {doneCount}/4</span>
                  <span>End Turn</span>
                </>
              )}
            </button>
          </div>
        </div>
      </div>

      {/* Election Verdict Top Banner (if election concluded) */}
      {gameState?.nationalElectionResult && (
        <div style={{
          marginBottom: '14px',
          padding: '10px 16px',
          borderRadius: '10px',
          backgroundColor: gameState.nationalElectionResult.isPlayerVictory ? 'rgba(16, 185, 129, 0.15)' : 'rgba(239, 68, 68, 0.15)',
          border: gameState.nationalElectionResult.isPlayerVictory ? '1px solid #10b981' : '1px solid #ef4444',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          flexWrap: 'wrap',
          gap: '10px'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span style={{ fontSize: '18px' }}>{gameState.nationalElectionResult.isPlayerVictory ? '🏆' : '🏛️'}</span>
            <div>
              <div style={{ fontSize: '12px', fontWeight: 900, color: gameState.nationalElectionResult.isPlayerVictory ? '#6ee7b7' : '#fca5a5' }}>
                {gameState.nationalElectionResult.headline || 'National Lok Sabha Election Concluded'}
              </div>
              <div style={{ fontSize: '9.5px', color: '#cbd5e1' }}>
                Outcome: {gameState.nationalElectionResult.isPlayerVictory ? 'Absolute Majority Formed (>= 272 Seats)' : 'Defeated (Opposition Mandate)'}
              </div>
            </div>
          </div>

          <button
            onClick={() => setShowVerdictModal(true)}
            style={{
              padding: '6px 14px',
              borderRadius: '6px',
              border: 'none',
              background: gameState.nationalElectionResult.isPlayerVictory ? '#10b981' : '#ef4444',
              color: '#ffffff',
              fontSize: '10px',
              fontWeight: 800,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '4px'
            }}
          >
            📜 View Full Election Verdict
          </button>
        </div>
      )}

      {/* 3 Top Tabs: Intelligence | Operations | Hints */}
      <NationalWR_TabBar
        activeTab={activeTab}
        setActiveTab={setActiveTab}
      />

      {/* Active Tab View */}
      {activeTab === 'intelligence' && (
        <NationalWR_Intelligence
          activeGame={gameState}
          configData={configData}
          onGameUpdate={handleGameUpdate}
          highlightProjected={highlightProjectedSeats}
        />
      )}

      {activeTab === 'operations' && (
        <NationalWR_Operations
          activeGame={gameState}
          configData={configData}
          onGameUpdate={handleGameUpdate}
          onAdvanceSeason={handleAdvanceSeason}
          isAdvancingSeason={advancingSeason}
          completedActions={completedActions}
          markStepComplete={markStepComplete}
          isCoalitionDone={isCoalitionDone}
          isFinanceDone={isFinanceDone}
          isEventsDone={isEventsDone}
          isStatesDone={isStatesDone}
          isAllFourDone={isAllFourDone}
          doneCount={doneCount}
          initialSubTab={operationsSubTab}
          onSubTabChange={setOperationsSubTab}
        />
      )}

      {activeTab === 'hints' && (
        <NationalWR_Hints
          activeGame={gameState}
          configData={configData}
          onNavigateTab={handleNavigateTab}
        />
      )}

      {/* 543 Lok Sabha National Election Verdict Modal */}
      {showVerdictModal && gameState?.nationalElectionResult && (
        <NationalElectionVerdictModal
          electionResult={gameState.nationalElectionResult}
          onClose={() => setShowVerdictModal(false)}
          onReturnToHeadquarters={onReturnToHeadquarters}
        />
      )}

      {/* End of Turn Strategic Debrief Modal */}
      {showDebriefModal && turnDebriefData && (
        <NationalTurnDebriefModal
          isOpen={showDebriefModal}
          debriefData={turnDebriefData}
          onClose={() => {
            setShowDebriefModal(false);
            setActiveTab('intelligence');
            setHighlightProjectedSeats(true);
          }}
        />
      )}

    </div>
  );
}
