import React, { useState, useMemo, useRef, useEffect } from 'react';
import { callNoConfidenceVote } from '../../../api/apiClient';

// Alliance Colors & Branding
const ALLIANCE_COLORS = {
  NDA: '#f97316',
  INC: '#38bdf8',
  LEFT: '#ef4444',
  UNALIGNED: '#a855f7',
  INDEPENDENT: '#a855f7',
  OTHERS: '#64748b'
};

const TOTAL_LOK_SABHA_SEATS = 543;

/**
 * Interactive SVG Donut Chart for 543 Lok Sabha Seats
 * Displays seat numbers and percentages directly on donut slices & callouts
 */
function AllianceDonutChart({ categories: propCategories, allianceSeats }) {
  const totalSeats = TOTAL_LOK_SABHA_SEATS;
  const cx = 160;
  const cy = 160;
  const radius = 95;
  const strokeWidth = 36;
  const circumference = 2 * Math.PI * radius; // ~596.9px

  // Keys to display on Donut
  const categories = propCategories && propCategories.length > 0 ? propCategories : [
    { key: 'NDA', label: 'NDA', color: '#f97316' },
    { key: 'INC', label: 'INC', color: '#38bdf8' },
    { key: 'LEFT', label: 'LEFT', color: '#ef4444' },
    { key: 'UNALIGNED', label: 'UNALIGNED', color: '#a855f7' }
  ];

  // Calculate slice math
  const slices = useMemo(() => {
    let accumulatedFraction = 0;
    let currentAngle = -Math.PI / 2; // Start at top (12 o'clock)

    return categories.map(cat => {
      const seats = cat.seats !== undefined ? cat.seats : (allianceSeats?.[cat.key] || 0);
      const fraction = seats / totalSeats;
      const dasharray = `${(fraction * circumference).toFixed(2)} ${circumference.toFixed(2)}`;
      const dashoffset = (-accumulatedFraction * circumference).toFixed(2);

      const angleDelta = fraction * 2 * Math.PI;
      const midAngle = currentAngle + angleDelta / 2;

      accumulatedFraction += fraction;
      currentAngle += angleDelta;

      // Label callout positioning radius (outside donut center)
      const labelRadius = 95;
      const lx = Math.round(cx + labelRadius * Math.cos(midAngle));
      const ly = Math.round(cy + labelRadius * Math.sin(midAngle));

      return {
        ...cat,
        seats,
        percentage: (fraction * 100).toFixed(1),
        dasharray,
        dashoffset,
        lx,
        ly,
        midAngle
      };
    });
  }, [categories, allianceSeats]);

  return (
    <div style={{ position: 'relative', width: '250px', height: '250px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
      <svg width="250" height="250" viewBox="0 0 320 320">
        {/* Outer subtle glow circle */}
        <circle cx={cx} cy={cy} r={radius + strokeWidth / 2 + 4} fill="none" stroke="rgba(255, 255, 255, 0.05)" strokeWidth="1" />

        {/* Donut Background Ring */}
        <circle
          cx={cx}
          cy={cy}
          r={radius}
          fill="none"
          stroke="#131d38"
          strokeWidth={strokeWidth}
        />

        {/* Donut Alliance Slices */}
        {slices.map(slice => (
          <circle
            key={slice.key}
            cx={cx}
            cy={cy}
            r={radius}
            fill="none"
            stroke={slice.color}
            strokeWidth={strokeWidth}
            strokeDasharray={slice.dasharray}
            strokeDashoffset={slice.dashoffset}
            transform={`rotate(-90 ${cx} ${cy})`}
            style={{
              transition: 'all 0.5s ease-in-out',
              cursor: 'pointer'
            }}
          />
        ))}

        {/* Seat Number Callout Labels on Segments */}
        {slices.map(slice => {
          if (slice.seats === 0) return null;
          return (
            <g key={`label-${slice.key}`} transform={`translate(${slice.lx}, ${slice.ly})`}>
              <rect
                x="-18"
                y="-9"
                width="36"
                height="18"
                rx="5"
                fill="#0f172a"
                stroke={slice.color}
                strokeWidth="1.2"
              />
              <text
                x="0"
                y="3.5"
                textAnchor="middle"
                fill="#ffffff"
                fontSize="9.5"
                fontWeight="900"
                fontFamily="system-ui, sans-serif"
              >
                {slice.seats}
              </text>
            </g>
          );
        })}
      </svg>

      {/* Donut Center Overlay */}
      <div style={{
        position: 'absolute',
        textAlign: 'center',
        pointerEvents: 'none',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        width: '95px',
        height: '95px',
        borderRadius: '9999px',
        backgroundColor: '#0b1329',
        border: '1px solid rgba(56, 189, 248, 0.2)',
        boxShadow: 'inset 0 0 20px rgba(0,0,0,0.8)'
      }}>
        <div style={{ fontSize: '22px', fontWeight: '900', color: '#ffffff', lineHeight: 1 }}>
          543
        </div>
        <div style={{ fontSize: '7.5px', fontWeight: '800', color: '#94a3b8', textTransform: 'uppercase', letterSpacing: '0.08em', marginTop: '2px' }}>
          LOK SABHA SEATS
        </div>
        <div style={{ fontSize: '8px', color: '#fbbf24', fontWeight: '800', marginTop: '2px' }}>
          Majority: 272
        </div>
      </div>
    </div>
  );
}

export default function NationalWR_Intelligence({ activeGame, configData, onGameUpdate, highlightProjected = false }) {
  const totalLokSabhaSeats = configData?.totalSeats || TOTAL_LOK_SABHA_SEATS;

  const standingsRef = useRef(null);
  const [expandedAlliances, setExpandedAlliances] = useState({});
  const [seatMode, setSeatMode] = useState(highlightProjected ? 'projected' : 'actual'); // 'actual' | 'projected'
  const [showNoConfidenceConfirm, setShowNoConfidenceConfirm] = useState(false);
  const [isCallingNoConfidence, setIsCallingNoConfidence] = useState(false);
  const [noConfidenceError, setNoConfidenceError] = useState(null);

  useEffect(() => {
    if (highlightProjected) {
      setSeatMode('projected');
      const timer = setTimeout(() => {
        standingsRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }, 150);
      return () => clearTimeout(timer);
    }
  }, [highlightProjected, activeGame?.currentSeason]);

  const toggleAllianceExpansion = (key) => {
    setExpandedAlliances(prev => ({
      ...prev,
      [key]: !prev[key]
    }));
  };

  const playerPartyKey = (activeGame?.partyKey || 'ydp').toLowerCase();

  // Compute Player Alliance Total Projected Lok Sabha Seats (Threshold: > 272)
  const playerAllianceProjectedSeats = useMemo(() => {
    const playerAlliances = activeGame?.alliances || [];
    const playerAllianceObj = playerAlliances.find(a =>
      (a.leaderPartyKey || '').toLowerCase() === playerPartyKey ||
      (a.members && a.members.some(m => (m.partyKey || '').toLowerCase() === playerPartyKey))
    );
    const memberKeys = new Set();
    memberKeys.add(playerPartyKey.toUpperCase());
    if (playerAllianceObj?.members) {
      playerAllianceObj.members.forEach(m => {
        if (m.partyKey) memberKeys.add(m.partyKey.toUpperCase());
      });
    }

    const proj = activeGame?.nationalProjectedSeats || {};
    let total = 0;
    memberKeys.forEach(pk => {
      const pState = activeGame?.partyStates?.find(p => (p.partyKey || '').toUpperCase() === pk);
      const seats = proj[pk] !== undefined ? proj[pk] : (pState?.seats || 0);
      total += seats;
    });
    return total;
  }, [activeGame, playerPartyKey]);

  const handleExecuteNoConfidence = async () => {
    const gameId = activeGame?.id || activeGame?._id;
    if (!gameId) return;
    setIsCallingNoConfidence(true);
    setNoConfidenceError(null);
    try {
      const updated = await callNoConfidenceVote(gameId);
      if (updated) {
        if (onGameUpdate) onGameUpdate(updated);
        setShowNoConfidenceConfirm(false);
      }
    } catch (err) {
      console.error('Failed to call no-confidence vote:', err);
      setNoConfidenceError(err.message || 'Failed to move No-Confidence Motion.');
    } finally {
      setIsCallingNoConfidence(false);
    }
  };

  // Group Parties by Alliance Key for Widgets (dynamic based on live alliances + partyStates)
  const { allianceGroupMap, allianceSeats, dynamicCategories, playerAllianceKey, orderedGroupKeys } = useMemo(() => {
    const groups = {};
    const seatsMap = {};

    const playerAlliances = activeGame?.alliances || [];
    const playerAllianceObj = playerAlliances.find(a => (a.leaderPartyKey || '').toLowerCase() === playerPartyKey);

    let activePlayerAllianceKey = null;

    // 1. If player has formed an alliance, add it as the primary group
    if (playerAllianceObj) {
      activePlayerAllianceKey = playerAllianceObj.allianceId || 'PLAYER_FRONT';
      groups[activePlayerAllianceKey] = {
        key: activePlayerAllianceKey,
        shortCode: playerAllianceObj.allianceName || 'ALLIANCE',
        name: playerAllianceObj.allianceName || 'Your Alliance',
        color: playerAllianceObj.color || '#38bdf8',
        badgeText: 'Your Coalition Front',
        isPlayerGroup: true,
        parties: []
      };
    }

    // 2. Base Pre-seeded alliance groups
    groups['NDA'] = { key: 'NDA', shortCode: 'NDA', name: 'National Democratic Alliance (NDA)', color: '#f97316', badgeText: 'Ruling Coalition', parties: [] };
    groups['INC'] = { key: 'INC', shortCode: 'INC', name: 'Congress & Allies (INC)', color: '#38bdf8', badgeText: 'Main Opposition', parties: [] };
    groups['LEFT'] = { key: 'LEFT', shortCode: 'LEFT', name: 'Left Front (LEFT)', color: '#ef4444', badgeText: 'Left Coalition', parties: [] };
    groups['UNALIGNED'] = { key: 'UNALIGNED', shortCode: 'UNALIGNED', name: 'Unaligned Regional & Independent Parties', color: '#a855f7', badgeText: 'Non-Coalition Regional', parties: [] };

    // Register all active game alliances
    playerAlliances.forEach(a => {
      const aId = a.allianceId;
      if (aId && !groups[aId]) {
        groups[aId] = {
          key: aId,
          shortCode: a.allianceName || 'ALLIANCE',
          name: a.allianceName || 'Coalition Front',
          color: a.color || '#38bdf8',
          badgeText: (a.leaderPartyKey || '').toLowerCase() === playerPartyKey ? 'Your Coalition Front' : 'Coalition Front',
          isPlayerGroup: (a.leaderPartyKey || '').toLowerCase() === playerPartyKey,
          parties: []
        };
      }
    });

    // 3. Collect parties from activeGame.partyStates or configData.parties
    const partyStateList = (activeGame?.partyStates && activeGame.partyStates.length > 0)
      ? activeGame.partyStates
      : (configData?.parties || []);

    partyStateList.forEach(p => {
      const pKey = (p.partyKey || p.id || '').toLowerCase();
      const pConfig = configData?.parties?.find(cp => (cp.partyKey || cp.id || '').toLowerCase() === pKey);

      const pKeyUpper = (p.partyKey || p.id || pKey).toUpperCase();
      const projSeats = activeGame?.nationalProjectedSeats?.[pKeyUpper] !== undefined
        ? activeGame.nationalProjectedSeats[pKeyUpper]
        : (p.seats !== undefined ? p.seats : (pConfig?.initialSeats || 0));

      const partyObj = {
        partyKey: p.partyKey || p.id || pKey,
        name: p.partyName || pConfig?.name || p.name || pKey.toUpperCase(),
        shortName: p.shortName || pConfig?.shortName || pKey.toUpperCase(),
        color: p.color || pConfig?.color || '#94a3b8',
        description: p.description || pConfig?.description || '',
        initialSeats: p.seats !== undefined ? p.seats : (pConfig?.initialSeats || p.initialSeats || 0),
        projSeats,
        initialMorale: p.morale !== undefined ? p.morale : (p.initialMorale || p.initialContent || 70),
        funds: p.funds !== undefined ? p.funds : (pConfig?.declaredFundsCr || pConfig?.fundsCr || pConfig?.initialFunds || 10.0),
        workers: p.workers !== undefined ? p.workers : (pConfig?.workers || 50000),
        volunteers: p.volunteers !== undefined ? p.volunteers : (pConfig?.volunteers || 15000),
        donors: p.donors !== undefined ? p.donors : (pConfig?.donors || 1000),
        currentAllianceId: p.currentAllianceId,
        corruption: p.corruption !== undefined ? p.corruption : 0,
        // Turn-by-turn deltas
        deltaSeats: p.deltaSeats || 0,
        deltaMorale: p.deltaMorale || 0,
        deltaFunds: p.deltaFunds || 0.0,
        deltaCorruption: p.deltaCorruption || 0,
        deltaWorkers: p.deltaWorkers || 0,
        deltaVolunteers: p.deltaVolunteers || 0,
        deltaDonors: p.deltaDonors || 0
      };

      // Check if this party belongs to the player's alliance
      const isMemberOfPlayerAlliance = playerAllianceObj && (
        pKey === playerPartyKey ||
        (p.currentAllianceId && p.currentAllianceId === playerAllianceObj.allianceId) ||
        (playerAllianceObj.members && playerAllianceObj.members.some(m => (m.partyKey || '').toLowerCase() === pKey))
      );

      if (isMemberOfPlayerAlliance && activePlayerAllianceKey) {
        groups[activePlayerAllianceKey].parties.push(partyObj);
      } else {
        // Load alliance directly from the last turn data (p.currentAllianceId)
        let allianceTarget;
        if (p.currentAllianceId !== undefined) {
          allianceTarget = p.currentAllianceId || 'UNALIGNED';
        } else {
          // Fallback only if currentAllianceId was not initialized in legacy state
          allianceTarget = p.preSeededAllianceKey || 'UNALIGNED';
        }

        if (allianceTarget === 'INDEPENDENT' || allianceTarget === 'NONE' || !groups[allianceTarget]) {
          allianceTarget = 'UNALIGNED';
        }
        groups[allianceTarget].parties.push(partyObj);
      }
    });

    // 4. Calculate totalSeats for each group (actual or projected)
    Object.values(groups).forEach(g => {
      g.parties.sort((a, b) => (b.initialSeats || 0) - (a.initialSeats || 0));
      g.totalSeats = g.parties.reduce((sum, p) => {
        const pKeyUpper = (p.partyKey || p.key || '').toUpperCase();
        const pSeats = (seatMode === 'projected' && activeGame?.nationalProjectedSeats?.[pKeyUpper] !== undefined)
          ? activeGame.nationalProjectedSeats[pKeyUpper]
          : (p.initialSeats || 0);
        return sum + pSeats;
      }, 0);
      seatsMap[g.key] = g.totalSeats;
    });

    // 5. Build dynamic donut categories & ordered keys
    const dynamicCats = [];
    const orderedKeys = [];

    if (activePlayerAllianceKey && groups[activePlayerAllianceKey]) {
      dynamicCats.push({
        key: activePlayerAllianceKey,
        label: groups[activePlayerAllianceKey].name.slice(0, 16),
        name: groups[activePlayerAllianceKey].name,
        color: groups[activePlayerAllianceKey].color,
        seats: groups[activePlayerAllianceKey].totalSeats,
        isPlayer: true
      });
      orderedKeys.push(activePlayerAllianceKey);
    }

    ['NDA', 'INC', 'LEFT', 'UNALIGNED'].forEach(k => {
      if (groups[k]) {
        dynamicCats.push({
          key: k,
          label: k === 'UNALIGNED' ? 'INDEPENDENT' : k,
          name: groups[k].name,
          color: groups[k].color,
          seats: groups[k].totalSeats,
          isPlayer: false
        });
        orderedKeys.push(k);
      }
    });

    return {
      allianceGroupMap: groups,
      allianceSeats: seatsMap,
      dynamicCategories: dynamicCats,
      playerAllianceKey: activePlayerAllianceKey,
      orderedGroupKeys: orderedKeys
    };
  }, [configData, activeGame, playerPartyKey, seatMode]);

  const [electoralFilter, setElectoralFilter] = useState('ALL'); // 'ALL' | 'BATTLEGROUND' | 'GAINING' | 'LOSING'
  const [showStateBreakdown, setShowStateBreakdown] = useState(false);
  const [activeStateTab, setActiveStateTab] = useState('UP');

  // Compute National Projected Seats & Real-time Voter Swings from State Operations
  const electoralProjections = useMemo(() => {
    const partyList = activeGame?.partyStates || [];
    const stateOps = activeGame?.stateOperations || {};
    const nationalProjSeats = activeGame?.nationalProjectedSeats || {};

    const norm = (k) => (k || '').toUpperCase().replace(/[^A-Z0-9]/g, '');

    const states = Object.values(stateOps);

    const partyRows = partyList.map(party => {
      const pKey = party.partyKey;
      const pKeyUpper = (pKey || '').toUpperCase();
      const pKeyNorm = norm(pKey);
      const shortName = party.shortName || pKeyUpper;
      const shortNorm = norm(shortName);

      const baseSeats = party.seats ?? 0;
      let projSeats = nationalProjSeats[pKeyUpper];

      const stateDetails = [];
      let totalStateSeatDelta = 0;
      let totalWeightedVoteSwing = 0;
      let totalStateWeight = 0;

      states.forEach(s => {
        const sSeats = s.totalLokSabhaSeats || 1;
        const vKey = Object.keys(s.voteSplits || {}).find(k =>
          k.toUpperCase() === pKeyUpper ||
          norm(k) === pKeyNorm ||
          norm(k) === shortNorm
        );

        if (vKey) {
          const currentVote = (s.voteSplits?.[vKey] != null) ? s.voteSplits[vKey] : 0.0;
          const baseVote = (s.baselineVoteSplits?.[vKey] != null)
            ? s.baselineVoteSplits[vKey]
            : currentVote;
          const voteSwing = currentVote - baseVote;

          const curProjSeat = (s.projectedLokSabhaSeats?.[vKey] != null)
            ? s.projectedLokSabhaSeats[vKey]
            : 0;
          const baseProjSeat = (s.baselineLokSabhaSeats?.[vKey] != null)
            ? s.baselineLokSabhaSeats[vKey]
            : curProjSeat;
          const seatShiftInState = curProjSeat - baseProjSeat;

          totalStateSeatDelta += seatShiftInState;
          totalWeightedVoteSwing += voteSwing * sSeats;
          totalStateWeight += sSeats;

          stateDetails.push({
            stateCode: s.stateCode,
            stateName: s.stateName,
            totalLokSabhaSeats: sSeats,
            currentVote: Math.round(currentVote * 10) / 10,
            baseVote: Math.round(baseVote * 10) / 10,
            voteSwing: Math.round(voteSwing * 10) / 10,
            currentSeats: curProjSeat,
            baseSeats: baseProjSeat,
            seatShift: seatShiftInState
          });
        }
      });

      if (projSeats === undefined) {
        projSeats = Math.max(0, baseSeats + totalStateSeatDelta);
      }

      const netSeatShift = projSeats - baseSeats;
      const netVoteSwing = totalStateWeight > 0
        ? Math.round((totalWeightedVoteSwing / totalStateWeight) * 10) / 10
        : 0.0;

      // Resolve friendly alliance name and styling
      const allianceMatch = (activeGame?.alliances || []).find(a => 
        (a.allianceId && a.allianceId.toLowerCase() === (party.currentAllianceId || '').toLowerCase()) ||
        (a.allianceName && a.allianceName.toLowerCase() === (party.currentAllianceId || '').toLowerCase())
      );

      const allianceDisplayName = allianceMatch
        ? (allianceMatch.allianceName || party.currentAllianceId)
        : (party.currentAllianceId === 'NDA' ? 'NDA' :
           party.currentAllianceId === 'INC' ? 'INC' :
           party.currentAllianceId === 'LEFT' ? 'LEFT' :
           (!party.currentAllianceId || party.currentAllianceId === 'UNALIGNED' || party.currentAllianceId === 'INDEPENDENT') ? 'UNALIGNED' :
           party.currentAllianceId);

      const allianceColor = allianceMatch ? (allianceMatch.color || '#c084fc') :
        party.currentAllianceId === 'NDA' ? '#f97316' :
        party.currentAllianceId === 'INC' ? '#38bdf8' :
        party.currentAllianceId === 'LEFT' ? '#ef4444' :
        '#94a3b8';

      return {
        partyKey: pKey,
        partyName: party.partyName || shortName,
        shortName,
        color: party.color || '#94a3b8',
        currentAllianceId: party.currentAllianceId || 'UNALIGNED',
        allianceDisplayName,
        allianceColor,
        isPlayerParty: Boolean(party.isPlayerParty),
        baseSeats,
        projSeats,
        netSeatShift,
        netVoteSwing,
        contestingBattlegrounds: stateDetails.length > 0,
        stateDetails
      };
    });

    partyRows.sort((a, b) => {
      if (a.isPlayerParty) return -1;
      if (b.isPlayerParty) return 1;
      return (b.projSeats || 0) - (a.projSeats || 0);
    });

    const blocTotals = {
      NDA: 0,
      INC: 0,
      PLAYER: 0,
      OTHERS: 0
    };

    partyRows.forEach(p => {
      const seats = p.projSeats || 0;
      if (p.isPlayerParty || (playerAllianceKey && p.currentAllianceId === playerAllianceKey)) {
        blocTotals.PLAYER += seats;
      } else if (p.currentAllianceId === 'NDA') {
        blocTotals.NDA += seats;
      } else if (p.currentAllianceId === 'INC') {
        blocTotals.INC += seats;
      } else {
        blocTotals.OTHERS += seats;
      }
    });

    return {
      partyRows,
      states,
      blocTotals
    };
  }, [activeGame?.partyStates, activeGame?.stateOperations, activeGame?.nationalProjectedSeats, playerAllianceKey]);

  const filteredPartyRows = useMemo(() => {
    let rows = electoralProjections.partyRows;
    if (electoralFilter === 'BATTLEGROUND') {
      rows = rows.filter(p => p.contestingBattlegrounds);
    } else if (electoralFilter === 'GAINING') {
      rows = rows.filter(p => p.netVoteSwing > 0 || p.netSeatShift > 0);
    } else if (electoralFilter === 'LOSING') {
      rows = rows.filter(p => p.netVoteSwing < 0 || p.netSeatShift < 0);
    }
    return rows;
  }, [electoralProjections.partyRows, electoralFilter]);

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
      
      {/* Header Banner */}
      <div style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        flexWrap: 'wrap',
        gap: '12px',
        backgroundColor: 'rgba(19, 29, 56, 0.8)',
        border: '1px solid rgba(56, 189, 248, 0.2)',
        borderRadius: '14px',
        padding: '16px 24px'
      }}>
        <div>
          <h2 style={{ margin: 0, fontSize: '20px', fontWeight: '900', color: '#ffffff' }}>
            📊 National Campaign Standings
          </h2>
          <p style={{ margin: '4px 0 0 0', fontSize: '13px', color: '#94a3b8' }}>
            Era {activeGame?.era || 2001} • Turn {activeGame?.currentSeason || activeGame?.turn || 1} (Month {activeGame?.currentSeason || activeGame?.turn || 1})
          </p>
        </div>

        <div style={{ display: 'flex', gap: '10px', alignItems: 'center', flexWrap: 'wrap' }}>
          {activeGame?.gameModeShortTitle && (
            <span style={{
              backgroundColor: 'rgba(245, 158, 11, 0.15)',
              border: '1px solid #f59e0b',
              color: '#fbbf24',
              padding: '6px 14px',
              borderRadius: '8px',
              fontSize: '12px',
              fontWeight: '800'
            }}>
              🎯 Objective: {activeGame.gameModeShortTitle}
            </span>
          )}
          <span style={{
            backgroundColor: '#1e293b',
            border: '1px solid #334155',
            color: '#38bdf8',
            padding: '4px 10px',
            borderRadius: '6px',
            fontSize: '8.5px',
            fontWeight: '700'
          }}>
            📅 {activeGame?.era || 2001}-01-01
          </span>
          <span className="nwr-badge nwr-badge-green">
            ● STATUS: ACTIVE
          </span>
        </div>
      </div>

      {/* WIDGET 1: Alliance Donut Chart & Seat Standings */}
      <div
        ref={standingsRef}
        id="alliance-lok-sabha-standings"
        className={`nwr-card ${highlightProjected ? 'nwr-standings-highlighted' : ''}`}
        style={{
          border: seatMode === 'projected' ? '1.5px solid rgba(168, 85, 247, 0.45)' : '1.5px solid rgba(56, 189, 248, 0.3)',
          transition: 'all 0.3s ease'
        }}
      >
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '14px', flexWrap: 'wrap', gap: '8px' }}>
          <div>
            <div className="nwr-card-title">
              🏛️ ALLIANCE LOK SABHA STANDINGS (543 SEATS TOTAL)
            </div>
            <p style={{ margin: '3px 0 0 0', fontSize: '9px', color: '#94a3b8' }}>
              Seat breakdown displayed directly on the Parliamentary Donut Chart.
            </p>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <div style={{
              display: 'flex',
              backgroundColor: '#0f172a',
              borderRadius: '8px',
              padding: '2px',
              border: seatMode === 'projected' ? '1px solid rgba(168, 85, 247, 0.5)' : '1px solid rgba(255,255,255,0.1)'
            }}>
              <button
                onClick={() => setSeatMode('actual')}
                style={{
                  padding: '4px 10px',
                  borderRadius: '6px',
                  border: 'none',
                  backgroundColor: seatMode === 'actual' ? 'rgba(56, 189, 248, 0.25)' : 'transparent',
                  color: seatMode === 'actual' ? '#38bdf8' : '#94a3b8',
                  fontSize: '9.5px',
                  fontWeight: 800,
                  cursor: 'pointer',
                  transition: 'all 0.2s'
                }}
              >
                Current Seats
              </button>
              <button
                onClick={() => setSeatMode('projected')}
                style={{
                  padding: '4px 10px',
                  borderRadius: '6px',
                  border: seatMode === 'projected' ? '1px solid #c084fc' : 'none',
                  backgroundColor: seatMode === 'projected' ? 'rgba(168, 85, 247, 0.35)' : 'transparent',
                  color: seatMode === 'projected' ? '#ffffff' : '#94a3b8',
                  fontSize: '9.5px',
                  fontWeight: 900,
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '5px',
                  boxShadow: seatMode === 'projected' ? '0 0 14px rgba(168, 85, 247, 0.6)' : 'none',
                  transition: 'all 0.2s'
                }}
              >
                <span>🔮</span>
                <span>Projected Seats</span>
                {seatMode === 'projected' && (
                  <span style={{
                    width: '6px',
                    height: '6px',
                    borderRadius: '50%',
                    backgroundColor: '#34d399',
                    display: 'inline-block',
                    boxShadow: '0 0 6px #34d399'
                  }} />
                )}
              </button>
            </div>
            <span className="nwr-badge nwr-badge-gold">
              Majority: 272
            </span>
            {playerAllianceProjectedSeats > 272 && !activeGame?.nationalElectionResult && (
              <button
                onClick={() => setShowNoConfidenceConfirm(true)}
                style={{
                  padding: '5px 12px',
                  borderRadius: '8px',
                  border: '1.5px solid #fbbf24',
                  background: 'linear-gradient(135deg, rgba(245, 158, 11, 0.35) 0%, rgba(220, 38, 38, 0.45) 100%)',
                  color: '#fef08a',
                  fontSize: '9.5px',
                  fontWeight: 900,
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '6px',
                  boxShadow: '0 0 16px rgba(245, 158, 11, 0.5)',
                  letterSpacing: '0.04em',
                  transition: 'all 0.2s'
                }}
                title="Your alliance commands > 272 projected Lok Sabha seats! Move a No-Confidence Motion to trigger an immediate national election."
              >
                <span>⚡</span> CHALLENGE NO-CONFIDENCE VOTE ({playerAllianceProjectedSeats} SEATS)
              </button>
            )}
          </div>
        </div>

        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))',
          gap: '16px',
          alignItems: 'center'
        }}>
          {/* Donut Chart with Data Badges on Segments */}
          <div style={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            backgroundColor: 'rgba(15, 23, 42, 0.6)',
            padding: '14px',
            borderRadius: '12px',
            border: '1px solid rgba(255,255,255,0.05)'
          }}>
            <AllianceDonutChart categories={dynamicCategories} allianceSeats={allianceSeats} />
          </div>

          {/* Alliance & Unaligned Parties Seat Numbers Breakdown */}
          <div>
            <div style={{ fontSize: '8.5px', fontWeight: '700', textTransform: 'uppercase', letterSpacing: '0.08em', color: '#94a3b8', marginBottom: '10px' }}>
              Parliamentary Coalitions & Regional Parties (Seat Numbers)
            </div>

            {dynamicCategories.map(group => {
              const seats = group.seats || 0;
              const isPlayerGroup = group.isPlayer || group.key === playerAllianceKey;

              return (
                <div
                  key={group.key}
                  className={`nwr-alliance-item ${isPlayerGroup ? 'is-player' : ''}`}
                  style={{ marginBottom: '7px', padding: '8px 10px' }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <div style={{
                      width: '10px',
                      height: '10px',
                      borderRadius: '3px',
                      backgroundColor: group.color,
                      boxShadow: `0 0 6px ${group.color}`,
                      flexShrink: 0
                    }} />
                    <div style={{ fontSize: '11px', fontWeight: '900', color: '#ffffff', letterSpacing: '0.03em' }}>
                      {group.name || group.label}
                    </div>
                  </div>

                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexShrink: 0 }}>
                    {isPlayerGroup && (
                      <span style={{
                        backgroundColor: '#10b981',
                        color: '#0f172a',
                        padding: '1.5px 5px',
                        borderRadius: '3px',
                        fontSize: '7.5px',
                        fontWeight: '900'
                      }}>
                        YOU
                      </span>
                    )}
                    <div style={{ textAlign: 'right' }}>
                      <span style={{ fontSize: '14px', fontWeight: '900', color: '#ffffff', lineHeight: 1 }}>
                        {seats}
                      </span>
                      <span style={{ fontSize: '8px', fontWeight: '800', color: group.color, marginLeft: '3px' }}>
                        SEATS
                      </span>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>

      {/* WIDGET 2: KEY ALLIANCES & CONSTITUENT PARTIES OVERVIEW (Interactive Expandable Alliance Boxes) */}
      <div className="nwr-card">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px', flexWrap: 'wrap', gap: '8px' }}>
          <div>
            <div className="nwr-card-title">
              👑 KEY ALLIANCES & CONSTITUENT PARTIES OVERVIEW
            </div>
            <p style={{ margin: '3px 0 0 0', fontSize: '9px', color: '#94a3b8' }}>
              Click any alliance box to expand and inspect each party's alliance membership, seat count, funds, and morale level.
            </p>
          </div>
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
          {orderedGroupKeys.map(key => {
            const group = allianceGroupMap[key];
            if (!group || !group.parties || group.parties.length === 0) return null;

            const isExpanded = !!expandedAlliances[key];
            const isPlayerGroup = group.isPlayerGroup || key === playerAllianceKey;

            return (
              <div
                key={key}
                style={{
                  backgroundColor: 'rgba(19, 29, 56, 0.9)',
                  border: isPlayerGroup ? `1.5px solid ${group.color}` : '1px solid rgba(255, 255, 255, 0.1)',
                  borderRadius: '10px',
                  overflow: 'hidden',
                  transition: 'all 0.2s ease-in-out',
                  boxShadow: isPlayerGroup ? `0 0 15px ${group.color}25` : 'none'
                }}
              >
                {/* Alliance Header Box (Clickable to Expand/Collapse) */}
                <div
                  onClick={() => toggleAllianceExpansion(key)}
                  style={{
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center',
                    padding: '12px 14px',
                    backgroundColor: 'rgba(30, 41, 59, 0.8)',
                    cursor: 'pointer',
                    userSelect: 'none',
                    borderBottom: isExpanded ? '1px solid rgba(255, 255, 255, 0.08)' : 'none'
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                    <div style={{
                      width: '13px',
                      height: '13px',
                      borderRadius: '4px',
                      backgroundColor: group.color,
                      boxShadow: `0 0 8px ${group.color}`
                    }} />
                    <div>
                      <div style={{ fontSize: '12px', fontWeight: '800', color: '#ffffff', display: 'flex', alignItems: 'center', gap: '8px' }}>
                        {group.name}
                        {isPlayerGroup && (
                          <span style={{ backgroundColor: '#10b981', color: '#0f172a', fontSize: '7.5px', padding: '1.5px 6px', borderRadius: '3px', fontWeight: '900', textTransform: 'uppercase' }}>
                            YOUR ALLIANCE
                          </span>
                        )}
                      </div>
                      <div style={{ fontSize: '8.5px', color: '#94a3b8', marginTop: '1px' }}>
                        {group.parties.length} Constituent Parties • Seat Share: <strong style={{ color: '#38bdf8' }}>{(((group.totalSeats || 0) / (totalLokSabhaSeats || 543)) * 100).toFixed(1)}%</strong>
                      </div>
                    </div>
                  </div>

                  <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                    <div style={{ textAlign: 'right' }}>
                      <span style={{ fontSize: '15px', fontWeight: '900', color: '#ffffff' }}>
                        {group.totalSeats}
                      </span>
                      <span style={{ fontSize: '8.5px', fontWeight: '800', color: group.color, marginLeft: '3px' }}>
                        SEATS
                      </span>
                    </div>

                    <div style={{
                      width: '24px', height: '24px', borderRadius: '6px',
                      backgroundColor: 'rgba(255, 255, 255, 0.05)',
                      border: '1px solid rgba(255, 255, 255, 0.1)',
                      display: 'flex', alignItems: 'center', justifyContent: 'center',
                      color: group.color, fontWeight: '800', fontSize: '10px'
                    }}>
                      {isExpanded ? '▲' : '▼'}
                    </div>
                  </div>
                </div>

                {/* Expanded Party Grid */}
                {isExpanded && (
                  <div style={{ padding: '14px', backgroundColor: 'rgba(15, 23, 42, 0.5)' }}>
                    <div className="nwr-grid-4">
                      {group.parties.map(p => {
                        const isPlayerParty = (p.partyKey || '').toLowerCase() === playerPartyKey;

                        return (
                          <div
                            key={p.partyKey}
                            style={{
                              backgroundColor: isPlayerParty ? 'rgba(16, 185, 129, 0.12)' : '#1c294d',
                              border: isPlayerParty ? '1.5px solid #10b981' : '1px solid rgba(255, 255, 255, 0.08)',
                              borderRadius: '10px',
                              padding: '10px',
                              boxShadow: isPlayerParty ? '0 0 15px rgba(16, 185, 129, 0.25)' : 'none',
                              position: 'relative',
                              display: 'flex',
                              flexDirection: 'column',
                              justifyContent: 'space-between'
                            }}
                          >
                            {isPlayerParty && (
                              <span style={{
                                position: 'absolute', top: '-8px', right: '8px',
                                backgroundColor: '#10b981', color: '#0f172a',
                                padding: '1.5px 6px', borderRadius: '3px',
                                fontSize: '7.5px', fontWeight: '900', textTransform: 'uppercase'
                              }}>
                                {isPlayerGroup ? '⭐ YOUR ALLIANCE LEADER' : '⭐ YOUR PARTY (UNALIGNED)'}
                              </span>
                            )}

                            <div>
                              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '6px' }}>
                                <div style={{
                                  width: '9px', height: '9px', borderRadius: '2px',
                                  backgroundColor: p.color || group.color,
                                  boxShadow: `0 0 5px ${p.color || group.color}`
                                }} />
                                <div style={{ fontSize: '10.5px', fontWeight: '800', color: '#ffffff' }}>
                                  {p.name} ({p.shortName})
                                </div>
                              </div>

                              <div style={{ fontSize: '8.5px', color: '#94a3b8', marginBottom: '8px', minHeight: '22px', lineHeight: 1.3 }}>
                                {p.description || 'Regional political party.'}
                              </div>

                              {/* Dedicated Alliance Information Box */}
                              <div style={{
                                display: 'flex',
                                alignItems: 'center',
                                justifyContent: 'space-between',
                                backgroundColor: 'rgba(0, 0, 0, 0.35)',
                                padding: '4px 8px',
                                borderRadius: '6px',
                                marginBottom: '8px',
                                border: `1px solid ${group.color}35`
                              }}>
                                <span style={{ fontSize: '7.5px', color: '#94a3b8', fontWeight: '700', textTransform: 'uppercase', letterSpacing: '0.04em' }}>Alliance:</span>
                                <span style={{
                                  fontSize: '8.5px',
                                  color: group.color || '#38bdf8',
                                  fontWeight: '900',
                                  display: 'flex',
                                  alignItems: 'center',
                                  gap: '4px'
                                }}>
                                  <span style={{
                                    width: '5px',
                                    height: '5px',
                                    borderRadius: '50%',
                                    backgroundColor: group.color || '#38bdf8',
                                    display: 'inline-block',
                                    boxShadow: `0 0 4px ${group.color}`
                                  }} />
                                  {isPlayerGroup
                                    ? (isPlayerParty ? `${group.shortCode || group.key} (Leader)` : `${group.shortCode || group.key} (Member)`)
                                    : (group.key === 'UNALIGNED' ? 'Unaligned' : (group.shortCode || group.key))}
                                </span>
                              </div>
                            </div>

                            {/* Stats Breakdown: 🪑 SEATS | ❤️ MOR | 💰 FND | ⚖️ CRP */}
                            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '4px', textAlign: 'center' }}>
                              <div className="nwr-stat-box" style={{ padding: '4px 2px' }}>
                                <div style={{ fontSize: '6.5px', color: '#94a3b8', fontWeight: '800' }}>🪑 SEATS</div>
                                <div style={{ fontSize: '10px', fontWeight: '900', color: '#38bdf8' }}>
                                  {seatMode === 'projected' ? (p.projSeats !== undefined ? p.projSeats : (p.initialSeats || 0)) : (p.initialSeats || 0)}
                                </div>
                                {seatMode === 'projected' ? (
                                  ((p.projSeats !== undefined ? p.projSeats : (p.initialSeats || 0)) - (p.initialSeats || 0)) !== 0 && (
                                    <div style={{ fontSize: '7.5px', fontWeight: '800', color: ((p.projSeats !== undefined ? p.projSeats : (p.initialSeats || 0)) - (p.initialSeats || 0)) > 0 ? '#10b981' : '#ef4444' }}>
                                      {((p.projSeats !== undefined ? p.projSeats : (p.initialSeats || 0)) - (p.initialSeats || 0)) > 0
                                        ? `+${(p.projSeats !== undefined ? p.projSeats : (p.initialSeats || 0)) - (p.initialSeats || 0)}▲`
                                        : `${(p.projSeats !== undefined ? p.projSeats : (p.initialSeats || 0)) - (p.initialSeats || 0)}▼`}
                                    </div>
                                  )
                                ) : (
                                  p.deltaSeats !== 0 && (
                                    <div style={{ fontSize: '7.5px', fontWeight: '800', color: p.deltaSeats > 0 ? '#10b981' : '#ef4444' }}>
                                      {p.deltaSeats > 0 ? `+${p.deltaSeats}▲` : `${p.deltaSeats}▼`}
                                    </div>
                                  )
                                )}
                              </div>
                              <div className="nwr-stat-box" style={{ padding: '4px 2px' }}>
                                <div style={{ fontSize: '6.5px', color: '#94a3b8', fontWeight: '800' }}>❤️ MOR</div>
                                <div style={{ fontSize: '10px', fontWeight: '900', color: '#10b981' }}>{p.initialMorale || p.initialContent || 70}%</div>
                                {p.deltaMorale !== 0 && (
                                  <div style={{ fontSize: '7.5px', fontWeight: '800', color: p.deltaMorale > 0 ? '#10b981' : '#ef4444' }}>
                                    {p.deltaMorale > 0 ? `+${p.deltaMorale}%▲` : `${p.deltaMorale}%▼`}
                                  </div>
                                )}
                              </div>
                              <div className="nwr-stat-box" style={{ padding: '4px 2px' }}>
                                <div style={{ fontSize: '6.5px', color: '#94a3b8', fontWeight: '800' }}>💰 FND</div>
                                <div style={{ fontSize: '9px', fontWeight: '900', color: '#f59e0b' }}>
                                  ₹{Number(p.funds || 0).toFixed(1)}Cr
                                </div>
                                {p.deltaFunds !== 0 && (
                                  <div style={{ fontSize: '7.5px', fontWeight: '800', color: p.deltaFunds > 0 ? '#10b981' : '#ef4444' }}>
                                    {p.deltaFunds > 0 ? `+₹${p.deltaFunds.toFixed(1)}▲` : `-₹${Math.abs(p.deltaFunds).toFixed(1)}▼`}
                                  </div>
                                )}
                              </div>
                              <div className="nwr-stat-box" style={{ padding: '4px 2px' }}>
                                <div style={{ fontSize: '6.5px', color: '#94a3b8', fontWeight: '800' }}>⚖️ CRP</div>
                                <div style={{ fontSize: '10px', fontWeight: '900', color: (p.corruption || 0) > 40 ? '#ef4444' : (p.corruption || 0) > 20 ? '#fbbf24' : '#10b981' }}>
                                  {p.corruption || 0}%
                                </div>
                                {p.deltaCorruption !== 0 && (
                                  <div style={{ fontSize: '7.5px', fontWeight: '800', color: p.deltaCorruption > 0 ? '#ef4444' : '#10b981' }}>
                                    {p.deltaCorruption > 0 ? `+${p.deltaCorruption}%⚠️` : `${p.deltaCorruption}%▼`}
                                  </div>
                                )}
                              </div>
                            </div>

                            {/* Grassroots & Cadre Mobilization Stats: 👷 WRK | 🤝 VOL | 💳 DON */}
                            <div style={{
                              display: 'grid',
                              gridTemplateColumns: 'repeat(3, 1fr)',
                              gap: '4px',
                              marginTop: '6px',
                              backgroundColor: 'rgba(15, 23, 42, 0.65)',
                              padding: '4px 6px',
                              borderRadius: '6px',
                              border: '1px solid rgba(255, 255, 255, 0.06)',
                              textAlign: 'center'
                            }}>
                              <div>
                                <div style={{ fontSize: '6.5px', color: '#94a3b8', fontWeight: '800', textTransform: 'uppercase' }}>👷 WRK</div>
                                <div style={{ fontSize: '8.5px', fontWeight: '800', color: '#cbd5e1' }}>
                                  {p.workers >= 100000 ? `${(p.workers / 100000).toFixed(1)}L` : (p.workers || 0).toLocaleString()}
                                </div>
                                {p.deltaWorkers !== 0 && (
                                  <div style={{ fontSize: '7px', fontWeight: '800', color: p.deltaWorkers > 0 ? '#10b981' : '#ef4444' }}>
                                    {p.deltaWorkers > 0 ? `+${p.deltaWorkers >= 100000 ? (p.deltaWorkers / 100000).toFixed(1) + 'L' : p.deltaWorkers.toLocaleString()}▲` : `${p.deltaWorkers <= -100000 ? (p.deltaWorkers / 100000).toFixed(1) + 'L' : p.deltaWorkers.toLocaleString()}▼`}
                                  </div>
                                )}
                              </div>
                              <div>
                                <div style={{ fontSize: '6.5px', color: '#94a3b8', fontWeight: '800', textTransform: 'uppercase' }}>🤝 VOL</div>
                                <div style={{ fontSize: '8.5px', fontWeight: '800', color: '#cbd5e1' }}>
                                  {p.volunteers >= 100000 ? `${(p.volunteers / 100000).toFixed(1)}L` : (p.volunteers || 0).toLocaleString()}
                                </div>
                                {p.deltaVolunteers !== 0 && (
                                  <div style={{ fontSize: '7px', fontWeight: '800', color: p.deltaVolunteers > 0 ? '#10b981' : '#ef4444' }}>
                                    {p.deltaVolunteers > 0 ? `+${p.deltaVolunteers >= 100000 ? (p.deltaVolunteers / 100000).toFixed(1) + 'L' : p.deltaVolunteers.toLocaleString()}▲` : `${p.deltaVolunteers <= -100000 ? (p.deltaVolunteers / 100000).toFixed(1) + 'L' : p.deltaVolunteers.toLocaleString()}▼`}
                                  </div>
                                )}
                              </div>
                              <div>
                                <div style={{ fontSize: '6.5px', color: '#94a3b8', fontWeight: '800', textTransform: 'uppercase' }}>💳 DON</div>
                                <div style={{ fontSize: '8.5px', fontWeight: '800', color: '#cbd5e1' }}>
                                  {p.donors >= 1000 ? `${(p.donors / 1000).toFixed(1)}k` : (p.donors || 0).toLocaleString()}
                                </div>
                                {p.deltaDonors !== 0 && (
                                  <div style={{ fontSize: '7px', fontWeight: '800', color: p.deltaDonors > 0 ? '#10b981' : '#ef4444' }}>
                                    {p.deltaDonors > 0 ? `+${p.deltaDonors >= 1000 ? (p.deltaDonors / 1000).toFixed(1) + 'k' : p.deltaDonors.toLocaleString()}▲` : `${p.deltaDonors <= -1000 ? (p.deltaDonors / 1000).toFixed(1) + 'k' : p.deltaDonors.toLocaleString()}▼`}
                                  </div>
                                )}
                              </div>
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>

      {/* WIDGET 3: YOUR ALLIANCE — FUND & CONTRACT STATUS */}
      {(() => {
        // Find player's alliance from live game state (alliances array on activeGame)
        const playerAlliances = activeGame?.alliances || [];
        const playerAllianceObj = playerAlliances.find(a => (a.leaderPartyKey || '').toLowerCase() === (activeGame?.partyKey || '').toLowerCase());
        if (!playerAllianceObj) return null;

        const members = playerAllianceObj.members || [];
        const partyStatesList = activeGame?.partyStates || [];

        // Deduplicate member party keys so leader party is never double counted
        const uniqueMemberKeys = Array.from(new Set([
          playerAllianceObj.leaderPartyKey,
          ...members.map(m => m.partyKey)
        ].filter(Boolean)));

        const totalAllianceSeats = uniqueMemberKeys.reduce((sum, pk) => {
          const pkUpper = pk.toUpperCase();
          if (seatMode === 'projected' && activeGame?.nationalProjectedSeats?.[pkUpper] !== undefined) {
            return sum + activeGame.nationalProjectedSeats[pkUpper];
          }
          const p = partyStatesList.find(ps => (ps.partyKey || ps.id || '').toLowerCase() === pk.toLowerCase());
          return sum + (p?.seats || 0);
        }, 0);

        const partnerMembers = members.filter(m => (m.partyKey || '').toLowerCase() !== (playerAllianceObj.leaderPartyKey || '').toLowerCase());
        const totalPartiesCount = uniqueMemberKeys.length;

        const cabinetUsed = playerAllianceObj.totalCabinetPromised || 0;
        const stateUsed = playerAllianceObj.totalStatePromised || 0;
        const cabinetPct = Math.min(100, (cabinetUsed / 20) * 100);
        const statePct = Math.min(100, (stateUsed / 50) * 100);
        const activityLog = playerAllianceObj.activityLog || [];

        return (
          <div className="nwr-card" style={{ border: '1.5px solid rgba(16, 185, 129, 0.3)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '14px', flexWrap: 'wrap', gap: '8px' }}>
              <div>
                <div className="nwr-card-title" style={{ color: '#10b981' }}>
                  🤝 YOUR ALLIANCE — COALITION &amp; PORTFOLIO STATUS
                </div>
                <p style={{ margin: '3px 0 0 0', fontSize: '9px', color: '#94a3b8' }}>
                  {playerAllianceObj.allianceName} • Season {activeGame?.currentSeason || 1}
                </p>
              </div>
              <span style={{
                backgroundColor: 'rgba(16, 185, 129, 0.15)',
                border: '1px solid #10b981',
                color: '#10b981',
                padding: '4px 10px',
                borderRadius: '6px',
                fontSize: '8.5px',
                fontWeight: '800'
              }}>
                {totalPartiesCount} Parties ({partnerMembers.length} Coalition Partner{partnerMembers.length !== 1 ? 's' : ''})
              </span>
            </div>

            {/* Coalition Overview Row */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(110px, 1fr))', gap: '8px', marginBottom: '14px' }}>
              {[
                { label: seatMode === 'projected' ? 'ALLIANCE SEATS (PROJ)' : 'ALLIANCE SEATS', value: `${totalAllianceSeats} / 543`, color: '#38bdf8' },
                { label: 'MAJORITY STATUS', value: totalAllianceSeats >= 272 ? 'Majority Secured' : `${272 - totalAllianceSeats} Needed`, color: totalAllianceSeats >= 272 ? '#10b981' : '#fbbf24' },
                { label: 'CABINET COMMITTED', value: `${cabinetUsed} / 20`, color: '#fbbf24' },
                { label: 'STATE MIN. COMMITTED', value: `${stateUsed} / 50`, color: '#a78bfa' },
              ].map(stat => (
                <div key={stat.label} className="nwr-stat-box" style={{ padding: '10px' }}>
                  <div style={{ fontSize: '6.5px', color: '#94a3b8', fontWeight: '700', marginBottom: '2px' }}>{stat.label}</div>
                  <div style={{ fontSize: '11px', fontWeight: '900', color: stat.color }}>{stat.value}</div>
                </div>
              ))}
            </div>

            {/* Minister Commitment Progress Bars */}
            <div style={{ marginBottom: '14px' }}>
              <div style={{ fontSize: '8.5px', fontWeight: '700', textTransform: 'uppercase', letterSpacing: '0.08em', color: '#94a3b8', marginBottom: '8px' }}>
                MINISTER COMMITMENTS
              </div>
              {[
                { label: 'Cabinet Ministers', used: cabinetUsed, max: 20, pct: cabinetPct, color: '#fbbf24' },
                { label: 'State Ministers', used: stateUsed, max: 50, pct: statePct, color: '#38bdf8' },
              ].map(bar => (
                <div key={bar.label} style={{ marginBottom: '7px' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '3px' }}>
                    <span style={{ fontSize: '8.5px', color: '#e2e8f0', fontWeight: '600' }}>{bar.label}</span>
                    <span style={{ fontSize: '8.5px', fontWeight: '800', color: bar.pct > 90 ? '#ef4444' : bar.color }}>
                      {bar.used} / {bar.max}
                    </span>
                  </div>
                  <div style={{ height: '5px', backgroundColor: 'rgba(255,255,255,0.08)', borderRadius: '2.5px', overflow: 'hidden' }}>
                    <div style={{
                      width: `${bar.pct}%`,
                      height: '100%',
                      backgroundColor: bar.pct > 90 ? '#ef4444' : bar.color,
                      borderRadius: '2.5px',
                      transition: 'width 0.4s ease',
                      boxShadow: `0 0 6px ${bar.color}`
                    }} />
                  </div>
                </div>
              ))}
            </div>

            {/* Member Contract Health */}
            <div style={{ marginBottom: '14px' }}>
              <div style={{ fontSize: '8.5px', fontWeight: '700', textTransform: 'uppercase', letterSpacing: '0.08em', color: '#94a3b8', marginBottom: '8px' }}>
                MEMBER CONTRACT HEALTH
              </div>
              {partnerMembers.length > 0 ? (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                  {partnerMembers.map(member => {
                    const isBroken = member.contract?.isBroken;
                    const morale = member.morale || 70;
                    const moraleColor = morale >= 70 ? '#10b981' : morale >= 40 ? '#fbbf24' : '#ef4444';
                    return (
                      <div key={member.partyKey} style={{
                        display: 'flex',
                        justifyContent: 'space-between',
                        alignItems: 'center',
                        backgroundColor: isBroken ? 'rgba(239, 68, 68, 0.08)' : 'rgba(255,255,255,0.03)',
                        border: isBroken ? '1px solid rgba(239, 68, 68, 0.3)' : '1px solid rgba(255,255,255,0.06)',
                        borderRadius: '6px',
                        padding: '7px 10px',
                        flexWrap: 'wrap',
                        gap: '6px'
                      }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                          <span style={{ fontSize: '9.5px', fontWeight: '800', color: '#ffffff' }}>
                            {member.partyKey.toUpperCase()}
                          </span>
                          {isBroken ? (
                            <span style={{ backgroundColor: '#ef4444', color: '#fff', fontSize: '7.5px', padding: '1.5px 5px', borderRadius: '3px', fontWeight: '900' }}>
                              ⚠️ BREACHED
                            </span>
                          ) : (
                            <span style={{ backgroundColor: 'rgba(16,185,129,0.2)', color: '#10b981', fontSize: '7.5px', padding: '1.5px 5px', borderRadius: '3px', fontWeight: '700' }}>
                              ✅ ACTIVE
                            </span>
                          )}
                        </div>
                        <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap' }}>
                          <span style={{ fontSize: '8px', color: '#94a3b8' }}>
                            Recurring: <strong style={{ color: '#fbbf24' }}>₹{Number(member.contract?.recurringPerSeason || 0).toFixed(1)} Cr/season</strong>
                          </span>
                          <span style={{ fontSize: '8px', color: '#94a3b8' }}>
                            Cab: <strong style={{ color: '#38bdf8' }}>{member.contract?.cabinetMinistersPromised || 0}</strong>
                          </span>
                          <span style={{ fontSize: '8px', color: '#94a3b8' }}>
                            State: <strong style={{ color: '#a855f7' }}>{member.contract?.stateMinistersPromised || 0}</strong>
                          </span>
                          <span style={{ fontSize: '8px', color: '#94a3b8' }}>
                            Morale: <strong style={{ color: moraleColor }}>{morale}</strong>
                          </span>
                        </div>
                      </div>
                    );
                  })}
                </div>
              ) : (
                <div style={{ fontSize: '9px', color: '#94a3b8', fontStyle: 'italic', padding: '6px 0' }}>
                  No regional coalition partners recruited yet. Go to Operations ➔ Coalition to invite regional parties.
                </div>
              )}
            </div>

            {/* Activity Log */}
            {activityLog.length > 0 && (
              <div>
                <div style={{ fontSize: '8.5px', fontWeight: '700', textTransform: 'uppercase', letterSpacing: '0.08em', color: '#94a3b8', marginBottom: '8px' }}>
                  📋 ALLIANCE ACTIVITY LOG
                </div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', maxHeight: '160px', overflowY: 'auto' }}>
                  {activityLog.slice(0, 15).map((entry, idx) => (
                    <div key={idx} style={{
                      display: 'flex',
                      gap: '8px',
                      alignItems: 'flex-start',
                      fontSize: '8.5px',
                      padding: '4px 8px',
                      backgroundColor: 'rgba(255,255,255,0.02)',
                      borderRadius: '4px',
                      borderLeft: `2.5px solid ${
                        entry.event === 'PARTY_JOINED' ? '#10b981' :
                        entry.event === 'PARTY_REMOVED' || entry.event === 'ALLIANCE_DISSOLVED' ? '#ef4444' :
                        entry.event === 'CONTRACT_BREACH' ? '#f97316' :
                        entry.event === 'ALLIANCE_FORMED' ? '#fbbf24' :
                        '#38bdf8'
                      }`
                    }}>
                      <span style={{ color: '#64748b', flexShrink: 0, fontWeight: '700' }}>S{entry.season}</span>
                      <span style={{ color: '#cbd5e1', lineHeight: 1.4 }}>{entry.detail}</span>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        );
      })()}

      {/* ================================================================== */}
      {/* PROJECTED LOK SABHA SEATS & ELECTORAL TRAJECTORY (IF ELECTIONS HELD NOW) */}
      {/* ================================================================== */}
      <div className="nwr-card" style={{ padding: '18px', display: 'flex', flexDirection: 'column', gap: '16px' }}>
        {/* Card Header */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '12px' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <span style={{ fontSize: '20px' }}>🗳️</span>
              <h2 style={{ margin: 0, fontSize: '14px', fontWeight: '900', color: '#ffffff', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                Projected Lok Sabha Seats & Electoral Trajectory
              </h2>
              <span className="nwr-badge nwr-badge-cyan" style={{ fontSize: '8px' }}>
                IF ELECTIONS HELD NOW
              </span>
            </div>
            <div style={{ fontSize: '9.5px', color: '#94a3b8', marginTop: '3px' }}>
              Real-time national seat projections and voter swings based on focus battleground states and national baseline. Shows which parties are gaining and losing ground turn-by-turn.
            </div>
          </div>

          {/* Quick Stats Badges */}
          <div style={{ display: 'flex', gap: '6px', alignItems: 'center' }}>
            <span className="nwr-badge" style={{ backgroundColor: 'rgba(56, 189, 248, 0.1)', color: '#38bdf8', border: '1px solid rgba(56, 189, 248, 0.3)', fontSize: '9px', fontWeight: '800' }}>
              543 TOTAL SEATS
            </span>
            <span className="nwr-badge" style={{ backgroundColor: 'rgba(251, 191, 36, 0.1)', color: '#fbbf24', border: '1px solid rgba(251, 191, 36, 0.3)', fontSize: '9px', fontWeight: '800' }}>
              272 TO MAJORITY
            </span>
          </div>
        </div>

        {/* Lok Sabha Majority Threshold Progress Bar */}
        <div style={{
          backgroundColor: '#0d1527',
          padding: '12px 14px',
          borderRadius: '10px',
          border: '1px solid rgba(56, 189, 248, 0.2)'
        }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px', flexWrap: 'wrap', gap: '6px' }}>
            <div style={{ fontSize: '9px', fontWeight: '800', color: '#94a3b8', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
              🏛️ LOK SABHA MAJORITY BARRIER (TARGET: 272 OF 543 SEATS)
            </div>
            <div style={{ display: 'flex', gap: '12px', fontSize: '9px', fontWeight: '800', flexWrap: 'wrap' }}>
              <span style={{ color: '#f97316' }}>NDA: {electoralProjections.blocTotals.NDA}</span>
              <span style={{ color: '#38bdf8' }}>INC & Allies: {electoralProjections.blocTotals.INC}</span>
              {electoralProjections.blocTotals.PLAYER > 0 && (
                <span style={{ color: '#c084fc' }}>Your Alliance: {electoralProjections.blocTotals.PLAYER}</span>
              )}
              <span style={{ color: '#64748b' }}>Others: {electoralProjections.blocTotals.OTHERS}</span>
            </div>
          </div>

          {/* Progress Stack */}
          <div style={{
            position: 'relative',
            height: '14px',
            borderRadius: '7px',
            backgroundColor: '#1e293b',
            overflow: 'hidden',
            display: 'flex'
          }}>
            <div
              style={{
                width: `${(electoralProjections.blocTotals.NDA / 543) * 100}%`,
                backgroundColor: '#f97316',
                transition: 'width 0.4s ease'
              }}
              title={`NDA: ${electoralProjections.blocTotals.NDA} seats`}
            />
            <div
              style={{
                width: `${(electoralProjections.blocTotals.INC / 543) * 100}%`,
                backgroundColor: '#38bdf8',
                transition: 'width 0.4s ease'
              }}
              title={`INC: ${electoralProjections.blocTotals.INC} seats`}
            />
            {electoralProjections.blocTotals.PLAYER > 0 && (
              <div
                style={{
                  width: `${(electoralProjections.blocTotals.PLAYER / 543) * 100}%`,
                  backgroundColor: '#a855f7',
                  transition: 'width 0.4s ease'
                }}
                title={`Your Alliance: ${electoralProjections.blocTotals.PLAYER} seats`}
              />
            )}
            <div
              style={{
                flex: 1,
                backgroundColor: '#334155'
              }}
              title={`Others / Unaligned: ${electoralProjections.blocTotals.OTHERS} seats`}
            />

            {/* 272 Majority Indicator Marker */}
            <div style={{
              position: 'absolute',
              left: `${(272 / 543) * 100}%`,
              top: 0,
              bottom: 0,
              width: '2px',
              backgroundColor: '#fbbf24',
              boxShadow: '0 0 6px #fbbf24',
              zIndex: 2
            }} title="272 Majority Threshold" />
          </div>

          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '4px', fontSize: '8px', color: '#64748b' }}>
            <span>0</span>
            <span style={{ color: '#fbbf24', fontWeight: '800' }}>▲ 272 Majority Threshold</span>
            <span>543</span>
          </div>
        </div>

        {/* Filter Controls & State Breakdown Toggle */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
          <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap' }}>
            {[
              { id: 'ALL', label: 'All Parties' },
              { id: 'BATTLEGROUND', label: '⚔️ Battleground Active' },
              { id: 'GAINING', label: '▲ Gaining Ground' },
              { id: 'LOSING', label: '▼ Losing Ground' }
            ].map(f => (
              <button
                key={f.id}
                onClick={() => setElectoralFilter(f.id)}
                style={{
                  padding: '4px 8px',
                  borderRadius: '6px',
                  fontSize: '9px',
                  fontWeight: '700',
                  border: electoralFilter === f.id ? '1px solid #38bdf8' : '1px solid rgba(255,255,255,0.1)',
                  backgroundColor: electoralFilter === f.id ? 'rgba(56, 189, 248, 0.2)' : 'rgba(255,255,255,0.03)',
                  color: electoralFilter === f.id ? '#ffffff' : '#94a3b8',
                  cursor: 'pointer'
                }}
              >
                {f.label}
              </button>
            ))}
          </div>

          <button
            onClick={() => setShowStateBreakdown(prev => !prev)}
            style={{
              padding: '5px 12px',
              borderRadius: '6px',
              fontSize: '9px',
              fontWeight: '800',
              border: '1px solid rgba(168, 85, 247, 0.4)',
              backgroundColor: showStateBreakdown ? 'rgba(168, 85, 247, 0.25)' : 'rgba(168, 85, 247, 0.1)',
              color: '#c084fc',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '4px'
            }}
          >
            🗺️ {showStateBreakdown ? 'Hide State Details ▲' : 'View State Details ▼'}
          </button>
        </div>

        {/* State Breakdown Expandable View */}
        {showStateBreakdown && (
          <div style={{
            backgroundColor: '#0a0f1d',
            padding: '12px 14px',
            borderRadius: '8px',
            border: '1px solid rgba(168, 85, 247, 0.3)',
            display: 'flex',
            flexDirection: 'column',
            gap: '12px'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
              <div style={{ fontSize: '9.5px', fontWeight: '800', color: '#c084fc', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                📍 Focus State Projections & Electoral Swings
              </div>
              <div style={{ display: 'flex', gap: '4px', flexWrap: 'wrap' }}>
                {((electoralProjections.states && electoralProjections.states.length > 0)
                  ? electoralProjections.states.map(s => s.stateCode)
                  : ['UP', 'BIHAR', 'MAHARASHTRA', 'WEST_BENGAL', 'RAJASTHAN', 'ASSAM', 'TAMIL_NADU']
                ).map(sCode => {
                  const sObj = electoralProjections.states.find(s => s.stateCode === sCode);
                  const isAct = activeStateTab === sCode;
                  return (
                    <button
                      key={sCode}
                      onClick={() => setActiveStateTab(sCode)}
                      style={{
                        padding: '3px 8px',
                        borderRadius: '4px',
                        fontSize: '8.5px',
                        fontWeight: '800',
                        border: isAct ? '1px solid #c084fc' : '1px solid rgba(255,255,255,0.1)',
                        backgroundColor: isAct ? 'rgba(168, 85, 247, 0.3)' : 'transparent',
                        color: isAct ? '#ffffff' : '#94a3b8',
                        cursor: 'pointer'
                      }}
                    >
                      {sObj?.stateName || sCode} ({sObj?.totalLokSabhaSeats || ''} Seats)
                    </button>
                  );
                })}
              </div>
            </div>

            {/* Selected State Details Grid */}
            {(() => {
              const curState = electoralProjections.states.find(s => s.stateCode === activeStateTab);
              if (!curState) return <div style={{ fontSize: '9px', color: '#94a3b8' }}>State operations data loading...</div>;

              const stateSplits = curState.voteSplits || {};
              const baseSplits = curState.baselineVoteSplits || {};
              const projSeats = curState.projectedLokSabhaSeats || {};
              const baseSeats = curState.baselineLokSabhaSeats || {};

              const partyEntries = Object.keys(stateSplits)
                .filter(k => k !== 'UNDECIDED')
                .map(pKey => {
                  const vote = stateSplits[pKey] || 0.0;
                  const baseV = baseSplits[pKey] != null ? baseSplits[pKey] : vote;
                  const swing = vote - baseV;
                  const pSeat = projSeats[pKey] || 0;
                  const bSeat = baseSeats[pKey] != null ? baseSeats[pKey] : pSeat;
                  const sDelta = pSeat - bSeat;

                  const matchedParty = electoralProjections.partyRows.find(p =>
                    p.partyKey.toUpperCase() === pKey.toUpperCase() ||
                    p.shortName.toUpperCase() === pKey.toUpperCase()
                  );

                  return {
                    pKey,
                    color: matchedParty?.color || '#94a3b8',
                    partyName: matchedParty?.partyName || pKey,
                    vote: Math.round(vote * 10) / 10,
                    baseV: Math.round(baseV * 10) / 10,
                    swing: Math.round(swing * 10) / 10,
                    pSeat,
                    bSeat,
                    sDelta
                  };
                })
                .sort((a, b) => b.pSeat - a.pSeat);

              return (
                <div style={{
                  display: 'grid',
                  gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))',
                  gap: '8px'
                }}>
                  {partyEntries.map(entry => (
                    <div
                      key={entry.pKey}
                      style={{
                        backgroundColor: '#131d38',
                        padding: '8px 10px',
                        borderRadius: '6px',
                        borderLeft: `3px solid ${entry.color}`,
                        display: 'flex',
                        flexDirection: 'column',
                        gap: '4px'
                      }}
                    >
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <span style={{ fontSize: '10px', fontWeight: '900', color: '#ffffff' }}>
                          {entry.pKey}
                        </span>
                        <span style={{
                          fontSize: '9px',
                          fontWeight: '900',
                          color: entry.swing > 0 ? '#34d399' : entry.swing < 0 ? '#f87171' : '#94a3b8'
                        }}>
                          {entry.swing > 0 ? `+${entry.swing.toFixed(1)}% ▲` : entry.swing < 0 ? `${entry.swing.toFixed(1)}% ▼` : `0.0% —`}
                        </span>
                      </div>

                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '8.5px', color: '#94a3b8' }}>
                        <span>Vote Share:</span>
                        <span style={{ color: '#ffffff', fontWeight: '800' }}>{entry.vote}%</span>
                      </div>

                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '8.5px', color: '#94a3b8' }}>
                        <span>Projected Lok Sabha:</span>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                          <span style={{ color: '#38bdf8', fontWeight: '900' }}>{entry.pSeat} Seats</span>
                          {entry.sDelta !== 0 && (
                            <span style={{
                              fontSize: '8px',
                              fontWeight: '900',
                              color: entry.sDelta > 0 ? '#34d399' : '#f87171'
                            }}>
                              ({entry.sDelta > 0 ? `+${entry.sDelta}` : entry.sDelta})
                            </span>
                          )}
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              );
            })()}
          </div>
        )}

        {/* National Table */}
        <div style={{ overflowX: 'auto' }}>
          <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '9.5px', textAlign: 'left' }}>
            <thead>
              <tr style={{ borderBottom: '1px solid rgba(56, 189, 248, 0.2)', color: '#94a3b8', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                <th style={{ padding: '8px 6px' }}>Party / Front</th>
                <th style={{ padding: '8px 6px', textAlign: 'center' }}>Alliance</th>
                <th style={{ padding: '8px 6px', textAlign: 'right' }}>Baseline Seats</th>
                <th style={{ padding: '8px 6px', textAlign: 'right' }}>Projected Seats Now</th>
                <th style={{ padding: '8px 6px', textAlign: 'center' }}>Seat Shift</th>
                <th style={{ padding: '8px 6px', textAlign: 'center' }}>Vote Swing (+ / -)</th>
                <th style={{ padding: '8px 6px', textAlign: 'center' }}>Electoral Status</th>
              </tr>
            </thead>
            <tbody>
              {filteredPartyRows.map((party) => (
                <tr
                  key={party.partyKey}
                  style={{
                    borderBottom: '1px solid rgba(255, 255, 255, 0.04)',
                    backgroundColor: party.isPlayerParty ? 'rgba(124, 58, 237, 0.08)' : 'transparent',
                    transition: 'background-color 0.15s ease'
                  }}
                >
                  {/* Party Name */}
                  <td style={{ padding: '8px 6px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <div style={{ width: '8px', height: '8px', borderRadius: '50%', backgroundColor: party.color, flexShrink: 0 }} />
                      <div>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                          <span style={{ fontWeight: '900', color: '#ffffff' }}>{party.shortName}</span>
                          {party.isPlayerParty && (
                            <span className="nwr-badge nwr-badge-purple" style={{ fontSize: '7.5px', padding: '1px 4px' }}>
                              YOU
                            </span>
                          )}
                        </div>
                        <div style={{ fontSize: '8px', color: '#64748b' }}>
                          {party.partyName}
                        </div>
                      </div>
                    </div>
                  </td>

                  {/* Alliance */}
                  <td style={{ padding: '8px 6px', textAlign: 'center' }}>
                    <span className="nwr-badge" style={{
                      backgroundColor: party.allianceColor ? `${party.allianceColor}25` : 'rgba(100, 116, 139, 0.15)',
                      border: party.allianceColor ? `1px solid ${party.allianceColor}55` : '1px solid rgba(100, 116, 139, 0.3)',
                      color: party.allianceColor || '#94a3b8',
                      fontSize: '8px',
                      fontWeight: '800'
                    }}>
                      {party.allianceDisplayName}
                    </span>
                  </td>

                  {/* Baseline Seats */}
                  <td style={{ padding: '8px 6px', textAlign: 'right', color: '#94a3b8', fontWeight: '700' }}>
                    {party.baseSeats}
                  </td>

                  {/* Projected Seats Now */}
                  <td style={{ padding: '8px 6px', textAlign: 'right', fontWeight: '900', color: party.isPlayerParty ? '#c084fc' : '#ffffff', fontSize: '11px' }}>
                    {party.projSeats}
                  </td>

                  {/* Seat Shift */}
                  <td style={{ padding: '8px 6px', textAlign: 'center' }}>
                    {party.netSeatShift > 0 ? (
                      <span style={{ color: '#34d399', fontWeight: '900' }}>
                        +{party.netSeatShift} ▲
                      </span>
                    ) : party.netSeatShift < 0 ? (
                      <span style={{ color: '#f87171', fontWeight: '900' }}>
                        {party.netSeatShift} ▼
                      </span>
                    ) : (
                      <span style={{ color: '#64748b' }}>—</span>
                    )}
                  </td>

                  {/* Vote Swing */}
                  <td style={{ padding: '8px 6px', textAlign: 'center' }}>
                    {party.netVoteSwing > 0 ? (
                      <span style={{
                        backgroundColor: 'rgba(52, 211, 153, 0.12)',
                        color: '#34d399',
                        padding: '2px 6px',
                        borderRadius: '4px',
                        fontWeight: '900',
                        fontSize: '8.5px'
                      }}>
                        +{party.netVoteSwing.toFixed(1)}% ▲ GAINING
                      </span>
                    ) : party.netVoteSwing < 0 ? (
                      <span style={{
                        backgroundColor: 'rgba(248, 113, 113, 0.12)',
                        color: '#f87171',
                        padding: '2px 6px',
                        borderRadius: '4px',
                        fontWeight: '900',
                        fontSize: '8.5px'
                      }}>
                        {party.netVoteSwing.toFixed(1)}% ▼ LOSING
                      </span>
                    ) : (
                      <span style={{ color: '#64748b', fontSize: '8.5px' }}>
                        0.0% — Stable
                      </span>
                    )}
                  </td>

                  {/* Status Badge */}
                  <td style={{ padding: '8px 6px', textAlign: 'center' }}>
                    {party.projSeats >= 272 ? (
                      <span className="nwr-badge nwr-badge-emerald" style={{ fontSize: '7.5px' }}>
                        👑 MAJORITY
                      </span>
                    ) : party.projSeats >= 150 ? (
                      <span className="nwr-badge nwr-badge-cyan" style={{ fontSize: '7.5px' }}>
                        🏛️ MAIN CONTENDER
                      </span>
                    ) : party.netVoteSwing > 0 ? (
                      <span className="nwr-badge nwr-badge-emerald" style={{ fontSize: '7.5px' }}>
                        🚀 SURGING
                      </span>
                    ) : party.netVoteSwing < 0 ? (
                      <span className="nwr-badge" style={{ backgroundColor: 'rgba(239, 68, 68, 0.15)', color: '#ef4444', fontSize: '7.5px' }}>
                        ⚠️ UNDER PRESSURE
                      </span>
                    ) : (
                      <span style={{ color: '#64748b', fontSize: '8px' }}>
                        STATUS QUO
                      </span>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Confirmation Modal for No-Confidence Motion */}
      {showNoConfidenceConfirm && (
        <div
          style={{
            position: 'fixed',
            inset: 0,
            zIndex: 10000,
            backgroundColor: 'rgba(5, 10, 25, 0.85)',
            backdropFilter: 'blur(8px)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            padding: '16px'
          }}
          onClick={() => !isCallingNoConfidence && setShowNoConfidenceConfirm(false)}
        >
          <div
            style={{
              width: '100%',
              maxWidth: '560px',
              backgroundColor: '#0c1530',
              border: '2px solid #f59e0b',
              borderRadius: '16px',
              boxShadow: '0 0 40px rgba(245, 158, 11, 0.3), 0 20px 50px rgba(0,0,0,0.9)',
              padding: '24px',
              display: 'flex',
              flexDirection: 'column',
              gap: '16px'
            }}
            onClick={(e) => e.stopPropagation()}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
              <span style={{ fontSize: '24px' }}>⚡</span>
              <div>
                <h3 style={{ margin: 0, fontSize: '16px', fontWeight: 900, color: '#fef08a' }}>
                  TABLE NO-CONFIDENCE MOTION IN LOK SABHA
                </h3>
                <span style={{ fontSize: '9px', fontWeight: 700, color: '#94a3b8', textTransform: 'uppercase' }}>
                  Dissolve Parliament & Trigger Immediate General Election
                </span>
              </div>
            </div>

            <div
              style={{
                backgroundColor: 'rgba(245, 158, 11, 0.1)',
                border: '1px solid rgba(245, 158, 11, 0.3)',
                borderRadius: '10px',
                padding: '12px 14px',
                fontSize: '11px',
                color: '#e2e8f0',
                lineHeight: 1.5
              }}
            >
              Your alliance commands <strong style={{ color: '#fbbf24', fontSize: '13px' }}>{playerAllianceProjectedSeats} Projected Seats</strong>, surpassing the <strong style={{ color: '#fbbf24' }}>272</strong> absolute majority mark!
              <br /><br />
              Moving a No-Confidence Motion will immediately collapse the current Lok Sabha and trigger a <strong>Full National Election</strong> across all 543 constituencies.
              Final results will be calculated using all parties' campaign chests, volunteer cadres, morale, and regional support.
            </div>

            {noConfidenceError && (
              <div
                style={{
                  backgroundColor: 'rgba(239, 68, 68, 0.15)',
                  border: '1px solid #ef4444',
                  borderRadius: '8px',
                  padding: '10px',
                  color: '#fca5a5',
                  fontSize: '10px',
                  fontWeight: 700
                }}
              >
                ⚠️ {noConfidenceError}
              </div>
            )}

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '4px' }}>
              <button
                disabled={isCallingNoConfidence}
                onClick={() => setShowNoConfidenceConfirm(false)}
                style={{
                  padding: '8px 16px',
                  borderRadius: '8px',
                  border: '1px solid rgba(255,255,255,0.15)',
                  backgroundColor: 'rgba(255,255,255,0.05)',
                  color: '#cbd5e1',
                  fontSize: '11px',
                  fontWeight: 700,
                  cursor: isCallingNoConfidence ? 'not-allowed' : 'pointer'
                }}
              >
                Withdraw Motion
              </button>

              <button
                disabled={isCallingNoConfidence}
                onClick={handleExecuteNoConfidence}
                style={{
                  padding: '8px 18px',
                  borderRadius: '8px',
                  border: 'none',
                  background: 'linear-gradient(135deg, #f59e0b 0%, #dc2626 100%)',
                  color: '#ffffff',
                  fontSize: '11px',
                  fontWeight: 900,
                  cursor: isCallingNoConfidence ? 'not-allowed' : 'pointer',
                  boxShadow: '0 4px 15px rgba(245, 158, 11, 0.4)',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '6px'
                }}
              >
                {isCallingNoConfidence ? (
                  <>
                    <span style={{ animation: 'spin 1s linear infinite' }}>⏳</span>
                    Dissolving Parliament...
                  </>
                ) : (
                  <>
                    <span>🔥</span> Move No-Confidence & Call Election
                  </>
                )}
              </button>
            </div>
          </div>
        </div>
      )}

    </div>
  );
}
