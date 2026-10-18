import React, { useState } from 'react';
import { generateStrategicHints } from './hintEngine';

export default function NationalWR_Hints({ activeGame, configData, onNavigateTab }) {
  const hintsData = generateStrategicHints(activeGame, configData);

  // Selected state tab in the state tactical dossier
  const defaultState = hintsData?.stateGuide?.topPriorityState?.stateCode || 'UP';
  const [selectedStateCode, setSelectedStateCode] = useState(defaultState);

  if (!hintsData) {
    return (
      <div style={{ padding: '24px', textAlign: 'center', color: '#94a3b8' }}>
        No game session loaded for strategy advice.
      </div>
    );
  }

  const { executiveSummary, coalitionGuide, financeGuide, eventsGuide, stateGuide } = hintsData;
  const activeState = stateGuide.allStates.find(s => s.stateCode === selectedStateCode) || stateGuide.topPriorityState || stateGuide.allStates[0];

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>

      {/* ------------------------------------------------------------------ */}
      {/* 1. TOP STRATEGIC EXECUTIVE BRIEFING                                */}
      {/* ------------------------------------------------------------------ */}
      <div style={{
        background: 'linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.9) 100%)',
        border: '1.5px solid rgba(56, 189, 248, 0.3)',
        borderRadius: '14px',
        padding: '16px 20px',
        boxShadow: '0 8px 24px rgba(0, 0, 0, 0.4)',
        display: 'flex',
        flexDirection: 'column',
        gap: '12px'
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '10px' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <span style={{ fontSize: '20px' }}>💡</span>
              <h2 style={{ margin: 0, fontSize: '16px', fontWeight: '900', color: '#ffffff' }}>
                AI War Room Strategy Advisory & Hint Engine
              </h2>
              <span className="nwr-badge nwr-badge-cyan" style={{ fontSize: '8px' }}>
                {executiveSummary.phaseTitle}
              </span>
              {hintsData.source === 'BACKEND_AI_ENGINE' && (
                <span className="nwr-badge nwr-badge-emerald" style={{ fontSize: '7.5px' }}>
                  LIVE SERVER ENGINE
                </span>
              )}
            </div>
            <p style={{ margin: '4px 0 0 0', fontSize: '10px', color: '#94a3b8' }}>
              Turn {executiveSummary.currentSeason} • Live tactical analysis of your national alliance, treasury chest, and state battlegrounds.
            </p>
          </div>

          <div style={{ display: 'flex', gap: '10px', alignItems: 'center', flexWrap: 'wrap' }}>
            {hintsData.moraleStatus && (
              <div style={{
                backgroundColor: 'rgba(0, 0, 0, 0.4)',
                border: `1px solid ${hintsData.moraleStatus.badgeColor || '#ec4899'}55`,
                borderRadius: '8px',
                padding: '6px 12px',
                textAlign: 'right'
              }}>
                <div style={{ fontSize: '7.5px', color: '#94a3b8', fontWeight: '800', textTransform: 'uppercase' }}>
                  CADRE MORALE
                </div>
                <div style={{ fontSize: '13px', fontWeight: '900', color: hintsData.moraleStatus.badgeColor || '#ec4899' }}>
                  {hintsData.moraleStatus.morale}% • {hintsData.moraleStatus.trend}
                </div>
              </div>
            )}

            <div style={{
              backgroundColor: 'rgba(0, 0, 0, 0.4)',
              border: '1px solid rgba(56, 189, 248, 0.25)',
              borderRadius: '8px',
              padding: '6px 12px',
              textAlign: 'right'
            }}>
              <div style={{ fontSize: '7.5px', color: '#94a3b8', fontWeight: '800', textTransform: 'uppercase' }}>
                LOK SABHA MAJORITY
              </div>
              <div style={{ fontSize: '13px', fontWeight: '900', color: executiveSummary.hasMajority ? '#10b981' : '#38bdf8' }}>
                {executiveSummary.totalAllianceSeats} / 272 Seats
              </div>
            </div>

            <div style={{
              backgroundColor: 'rgba(0, 0, 0, 0.4)',
              border: '1px solid rgba(245, 158, 11, 0.25)',
              borderRadius: '8px',
              padding: '6px 12px',
              textAlign: 'right'
            }}>
              <div style={{ fontSize: '7.5px', color: '#94a3b8', fontWeight: '800', textTransform: 'uppercase' }}>
                MAJORITY GAP
              </div>
              <div style={{ fontSize: '13px', fontWeight: '900', color: executiveSummary.hasMajority ? '#10b981' : '#fbbf24' }}>
                {executiveSummary.hasMajority ? 'SECURED 🏆' : `${executiveSummary.majorityGap} Needed`}
              </div>
            </div>
          </div>
        </div>

        {/* Priority Commander's Order Banner */}
        <div style={{
          backgroundColor: executiveSummary.hasMajority ? 'rgba(16, 185, 129, 0.12)' : 'rgba(56, 189, 248, 0.08)',
          borderLeft: `4px solid ${executiveSummary.hasMajority ? '#10b981' : '#38bdf8'}`,
          borderRadius: '8px',
          padding: '10px 14px',
          display: 'flex',
          alignItems: 'center',
          gap: '10px'
        }}>
          <span style={{ fontSize: '18px' }}>🎯</span>
          <div>
            <div style={{ fontSize: '8px', fontWeight: '900', color: executiveSummary.hasMajority ? '#34d399' : '#38bdf8', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
              TURN {executiveSummary.currentSeason} COMMAND OBJECTIVE
            </div>
            <div style={{ fontSize: '11.5px', fontWeight: '700', color: '#ffffff', marginTop: '2px', lineHeight: 1.4 }}>
              {executiveSummary.topObjective}
            </div>
          </div>
        </div>

        {/* Morale Specific Guidance Bar if Low/Critical */}
        {hintsData.moraleStatus && (hintsData.moraleStatus.trend === 'CRITICAL' || hintsData.moraleStatus.trend === 'LOW') && (
          <div style={{
            backgroundColor: 'rgba(239, 68, 68, 0.1)',
            borderLeft: `4px solid ${hintsData.moraleStatus.badgeColor}`,
            borderRadius: '6px',
            padding: '8px 12px',
            fontSize: '10px',
            color: '#fecaca',
            lineHeight: 1.4
          }}>
            🚩 <strong style={{ color: hintsData.moraleStatus.badgeColor }}>Cadre Morale Advisory:</strong> {hintsData.moraleStatus.advice}
          </div>
        )}
      </div>

      {/* ------------------------------------------------------------------ */}
      {/* 2. FOUR STRATEGIC DIRECTIVE ADVISORY CARDS                          */}
      {/* ------------------------------------------------------------------ */}
      <div>
        <div style={{ fontSize: '9px', fontWeight: '800', textTransform: 'uppercase', letterSpacing: '0.08em', color: '#94a3b8', marginBottom: '8px' }}>
          ⚔️ 4 Turn Directives — Specific Action Guidance
        </div>

        <div className="nwr-grid-2" style={{ gap: '12px' }}>

          {/* CARD 1: COALITION FRONT */}
          <div className="nwr-card" style={{ borderLeft: '4px solid #a855f7', padding: '14px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', gap: '10px' }}>
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                <span style={{ fontSize: '12px', fontWeight: '900', color: '#c084fc', display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <span>🤝</span> ACTION 1: COALITION FRONT
                </span>
                <span className="nwr-badge" style={{ backgroundColor: coalitionGuide.hasAlliance ? 'rgba(16, 185, 129, 0.15)' : 'rgba(239, 68, 68, 0.15)', color: coalitionGuide.hasAlliance ? '#34d399' : '#f87171', border: `1px solid ${coalitionGuide.hasAlliance ? '#10b981' : '#ef4444'}` }}>
                  {coalitionGuide.statusBadge}
                </span>
              </div>

              <div style={{ fontSize: '11px', fontWeight: '800', color: '#ffffff', lineHeight: 1.4, marginBottom: '6px' }}>
                {coalitionGuide.recommendation}
              </div>

              <div style={{ backgroundColor: 'rgba(0, 0, 0, 0.3)', borderRadius: '6px', padding: '8px 10px', fontSize: '9.5px', color: '#cbd5e1', lineHeight: 1.4, border: '1px solid rgba(168, 85, 247, 0.2)' }}>
                💡 <strong style={{ color: '#c084fc' }}>Tactical Contract Advice:</strong> {coalitionGuide.actionTip}
              </div>
            </div>

            <button
              onClick={() => onNavigateTab && onNavigateTab('operations', 'coalition')}
              style={{
                padding: '6px 12px',
                borderRadius: '6px',
                border: '1px solid #a855f7',
                backgroundColor: 'rgba(168, 85, 247, 0.15)',
                color: '#c084fc',
                fontSize: '10px',
                fontWeight: '800',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                gap: '6px',
                transition: 'all 0.2s'
              }}
            >
              <span>Go to Coalition Hub</span>
              <span>→</span>
            </button>
          </div>

          {/* CARD 2: FINANCE & TREASURY */}
          <div className="nwr-card" style={{ borderLeft: '4px solid #f59e0b', padding: '14px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', gap: '10px' }}>
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                <span style={{ fontSize: '12px', fontWeight: '900', color: '#fbbf24', display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <span>💰</span> ACTION 2: FINANCE & TREASURY
                </span>
                <span className="nwr-badge" style={{ backgroundColor: financeGuide.isComplete ? 'rgba(16, 185, 129, 0.15)' : 'rgba(245, 158, 11, 0.15)', color: financeGuide.isComplete ? '#34d399' : '#fbbf24', border: `1px solid ${financeGuide.isComplete ? '#10b981' : '#f59e0b'}` }}>
                  {financeGuide.statusBadge}
                </span>
              </div>

              <div style={{ fontSize: '11px', fontWeight: '800', color: '#ffffff', lineHeight: 1.4, marginBottom: '6px' }}>
                {financeGuide.recommendation}
              </div>

              <div style={{ backgroundColor: 'rgba(0, 0, 0, 0.3)', borderRadius: '6px', padding: '8px 10px', fontSize: '9.5px', color: '#cbd5e1', lineHeight: 1.4, border: '1px solid rgba(245, 158, 11, 0.2)' }}>
                💡 <strong style={{ color: '#fbbf24' }}>Recommended Card Choice:</strong> {financeGuide.cardHint}
              </div>
            </div>

            <button
              onClick={() => onNavigateTab && onNavigateTab('operations', 'finance')}
              style={{
                padding: '6px 12px',
                borderRadius: '6px',
                border: '1px solid #f59e0b',
                backgroundColor: 'rgba(245, 158, 11, 0.15)',
                color: '#fbbf24',
                fontSize: '10px',
                fontWeight: '800',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                gap: '6px',
                transition: 'all 0.2s'
              }}
            >
              <span>Go to Treasury War Room</span>
              <span>→</span>
            </button>
          </div>

          {/* CARD 3: NATIONAL EVENTS & ISSUES */}
          <div className="nwr-card" style={{ borderLeft: '4px solid #38bdf8', padding: '14px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', gap: '10px' }}>
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                <span style={{ fontSize: '12px', fontWeight: '900', color: '#38bdf8', display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <span>📰</span> ACTION 3: EVENTS & CRISES
                </span>
                <span className="nwr-badge" style={{ backgroundColor: eventsGuide.isComplete ? 'rgba(16, 185, 129, 0.15)' : 'rgba(56, 189, 248, 0.15)', color: eventsGuide.isComplete ? '#34d399' : '#38bdf8', border: `1px solid ${eventsGuide.isComplete ? '#10b981' : '#38bdf8'}` }}>
                  {eventsGuide.statusBadge}
                </span>
              </div>

              <div style={{ fontSize: '11px', fontWeight: '800', color: '#ffffff', lineHeight: 1.4, marginBottom: '6px' }}>
                {eventsGuide.recommendation}
              </div>

              <div style={{ backgroundColor: 'rgba(0, 0, 0, 0.3)', borderRadius: '6px', padding: '8px 10px', fontSize: '9.5px', color: '#cbd5e1', lineHeight: 1.4, border: '1px solid rgba(56, 189, 248, 0.2)', display: 'flex', flexDirection: 'column', gap: '6px' }}>
                <div>💡 <strong style={{ color: '#38bdf8' }}>Stance Recommendation:</strong> {eventsGuide.actionTip}</div>
                {eventsGuide.targetPartyTip && (
                  <div>🎯 <strong style={{ color: '#f43f5e' }}>Rival Target Advisory:</strong> {eventsGuide.targetPartyTip}</div>
                )}
                {eventsGuide.mediaSocialTip && (
                  <div>📱 <strong style={{ color: '#c084fc' }}>Media & Social Blitz:</strong> {eventsGuide.mediaSocialTip}</div>
                )}
              </div>
            </div>

            <button
              onClick={() => onNavigateTab && onNavigateTab('operations', 'events')}
              style={{
                padding: '6px 12px',
                borderRadius: '6px',
                border: '1px solid #38bdf8',
                backgroundColor: 'rgba(56, 189, 248, 0.15)',
                color: '#38bdf8',
                fontSize: '10px',
                fontWeight: '800',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                gap: '6px',
                transition: 'all 0.2s'
              }}
            >
              <span>Review Events & Themes</span>
              <span>→</span>
            </button>
          </div>

          {/* CARD 4: STATE OPERATIONS */}
          <div className="nwr-card" style={{ borderLeft: '4px solid #10b981', padding: '14px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', gap: '10px' }}>
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                <span style={{ fontSize: '12px', fontWeight: '900', color: '#34d399', display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <span>🗺️</span> ACTION 4: STATE GROUND WARS
                </span>
                <span className="nwr-badge" style={{ backgroundColor: stateGuide.isComplete ? 'rgba(16, 185, 129, 0.15)' : 'rgba(52, 211, 153, 0.15)', color: stateGuide.isComplete ? '#34d399' : '#a7f3d0', border: `1px solid ${stateGuide.isComplete ? '#10b981' : '#34d399'}` }}>
                  {stateGuide.statusBadge}
                </span>
              </div>

              <div style={{ fontSize: '11px', fontWeight: '800', color: '#ffffff', lineHeight: 1.4, marginBottom: '6px' }}>
                Top Priority: <strong style={{ color: '#38bdf8' }}>{stateGuide.topPriorityState?.stateName} ({stateGuide.topPriorityState?.totalLokSabhaSeats} Seats)</strong> — {stateGuide.topPriorityState?.urgencyBadge}
              </div>

              <div style={{ backgroundColor: 'rgba(0, 0, 0, 0.3)', borderRadius: '6px', padding: '8px 10px', fontSize: '9.5px', color: '#cbd5e1', lineHeight: 1.4, border: '1px solid rgba(16, 185, 129, 0.2)' }}>
                💡 <strong style={{ color: '#34d399' }}>Immediate Ground Action:</strong> Transfer ₹{stateGuide.topPriorityState?.recTransferFunds} Cr & build {stateGuide.topPriorityState?.recInfra?.name} to secure vote momentum.
              </div>
            </div>

            <button
              onClick={() => onNavigateTab && onNavigateTab('operations', 'states')}
              style={{
                padding: '6px 12px',
                borderRadius: '6px',
                border: '1px solid #10b981',
                backgroundColor: 'rgba(16, 185, 129, 0.15)',
                color: '#34d399',
                fontSize: '10px',
                fontWeight: '800',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                gap: '6px',
                transition: 'all 0.2s'
              }}
            >
              <span>Go to State Operations</span>
              <span>→</span>
            </button>
          </div>

        </div>
      </div>

      {/* ------------------------------------------------------------------ */}
      {/* 3. STATE-BY-STATE TACTICAL DOSSIER                                 */}
      {/* ------------------------------------------------------------------ */}
      <div className="nwr-card" style={{ padding: '16px', border: '1px solid rgba(168, 85, 247, 0.3)' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px', flexWrap: 'wrap', gap: '8px' }}>
          <div>
            <div className="nwr-card-title" style={{ color: '#c084fc', fontSize: '12.5px' }}>
              📍 BATTLEGROUND DOSSIER: STATE-LEVEL SPECIFIC GUIDANCE
            </div>
            <p style={{ margin: '3px 0 0 0', fontSize: '9px', color: '#94a3b8' }}>
              Select a state to inspect customized recommendations for resource transfers, infrastructure building, and issue stances.
            </p>
          </div>

          {/* State Selector Tabs */}
          <div style={{ display: 'flex', gap: '4px', flexWrap: 'wrap' }}>
            {stateGuide.allStates.map(st => {
              const isSelected = st.stateCode === activeState?.stateCode;
              return (
                <button
                  key={st.stateCode}
                  onClick={() => setSelectedStateCode(st.stateCode)}
                  style={{
                    padding: '4px 9px',
                    borderRadius: '6px',
                    border: isSelected ? '1.5px solid #c084fc' : '1px solid rgba(255, 255, 255, 0.1)',
                    backgroundColor: isSelected ? 'rgba(168, 85, 247, 0.3)' : 'rgba(255, 255, 255, 0.03)',
                    color: isSelected ? '#ffffff' : '#94a3b8',
                    fontSize: '9px',
                    fontWeight: 800,
                    cursor: 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '4px',
                    transition: 'all 0.2s'
                  }}
                >
                  <span>{st.stateName}</span>
                  <span style={{ fontSize: '7.5px', color: st.urgencyColor }}>
                    ({st.totalLokSabhaSeats})
                  </span>
                </button>
              );
            })}
          </div>
        </div>

        {/* Selected State Detailed Guidance Sheet */}
        {activeState && (
          <div style={{
            backgroundColor: 'rgba(10, 15, 29, 0.85)',
            border: '1px solid rgba(168, 85, 247, 0.25)',
            borderRadius: '10px',
            padding: '16px',
            display: 'flex',
            flexDirection: 'column',
            gap: '14px'
          }}>
            {/* Top State Banner */}
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px', borderBottom: '1px solid rgba(255, 255, 255, 0.08)', paddingBottom: '10px' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span style={{ fontSize: '20px' }}>🏛️</span>
                <div>
                  <div style={{ fontSize: '14px', fontWeight: '900', color: '#ffffff' }}>
                    {activeState.stateName} ({activeState.totalLokSabhaSeats} Lok Sabha Seats • {activeState.totalAssemblySeats} Assembly Seats)
                  </div>
                  <div style={{ fontSize: '8.5px', color: '#94a3b8', marginTop: '1px' }}>
                    Current State Treasury: <strong style={{ color: '#10b981' }}>₹{activeState.stateFunds.toFixed(1)} Cr</strong> • Workers: <strong style={{ color: '#38bdf8' }}>{activeState.stateWorkers.toLocaleString()}</strong>
                  </div>
                </div>
              </div>

              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                {activeState.turnStatus === 'DONE' && (
                  <span className="nwr-badge nwr-badge-emerald" style={{ fontSize: '9px', fontWeight: '900' }}>
                    ACTION TAKEN ✓
                  </span>
                )}
                {activeState.turnStatus === 'PENDING' && (
                  <span className="nwr-badge nwr-badge-rose" style={{ fontSize: '9px', fontWeight: '900' }}>
                    ⚠️ PENDING ACTION
                  </span>
                )}
                {activeState.turnStatus === 'SKIPPED' && (
                  <span className="nwr-badge" style={{ backgroundColor: 'rgba(148, 163, 184, 0.2)', color: '#94a3b8', fontSize: '9px', fontWeight: '900' }}>
                    SKIPPED THIS TURN
                  </span>
                )}
                <span className="nwr-badge" style={{ backgroundColor: `${activeState.urgencyColor}25`, color: activeState.urgencyColor, border: `1px solid ${activeState.urgencyColor}`, fontSize: '9px', fontWeight: '900' }}>
                  {activeState.urgencyBadge}
                </span>
                <span style={{ fontSize: '10px', color: '#94a3b8' }}>
                  {activeState.turnsToElection > 0 ? `${activeState.turnsToElection} Turns to Assembly Election` : 'Election Turn Active'}
                </span>
              </div>
            </div>

            {/* 3 Pillar Guidance Grid */}
            <div className="nwr-grid-3" style={{ gap: '10px' }}>

              {/* PILLAR 1: RECOMMENDED RESOURCE TRANSFER */}
              <div style={{
                backgroundColor: 'rgba(15, 23, 42, 0.7)',
                border: '1px solid rgba(56, 189, 248, 0.25)',
                borderRadius: '8px',
                padding: '12px',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                gap: '8px'
              }}>
                <div>
                  <div style={{ fontSize: '8px', fontWeight: '800', color: '#38bdf8', textTransform: 'uppercase', letterSpacing: '0.06em', marginBottom: '4px' }}>
                    💰 1. HQ RESOURCE ALLOCATION
                  </div>
                  <div style={{ fontSize: '12px', fontWeight: '900', color: '#ffffff' }}>
                    {activeState.recTransferFunds > 0 ? `Transfer ₹${activeState.recTransferFunds.toFixed(1)} Cr` : 'No Funds Transfer Required'}
                  </div>
                  <div style={{ fontSize: '9px', color: '#94a3b8', marginTop: '3px' }}>
                    {activeState.recTransferWorkers > 0 ? `Mobilize ${activeState.recTransferWorkers.toLocaleString()} National Workers` : 'State worker pool is stable.'}
                  </div>
                </div>
                <div style={{ fontSize: '8px', color: '#64748b', fontStyle: 'italic', borderTop: '1px solid rgba(255,255,255,0.05)', paddingTop: '6px' }}>
                  Safely keeps national HQ treasury above ₹15 Cr reserve buffer.
                </div>
              </div>

              {/* PILLAR 2: RECOMMENDED INFRASTRUCTURE */}
              <div style={{
                backgroundColor: 'rgba(15, 23, 42, 0.7)',
                border: '1px solid rgba(245, 158, 11, 0.25)',
                borderRadius: '8px',
                padding: '12px',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                gap: '8px'
              }}>
                <div>
                  <div style={{ fontSize: '8px', fontWeight: '800', color: '#fbbf24', textTransform: 'uppercase', letterSpacing: '0.06em', marginBottom: '4px' }}>
                    🏢 2. INFRASTRUCTURE PRIORITY
                  </div>
                  <div style={{ fontSize: '12px', fontWeight: '900', color: '#ffffff' }}>
                    {activeState.recInfra?.name || 'State Party Headquarters'}
                  </div>
                  <div style={{ fontSize: '9px', color: '#cbd5e1', marginTop: '3px' }}>
                    Cost: <strong style={{ color: '#fbbf24' }}>{activeState.recInfra?.cost}</strong> • Yield: <strong style={{ color: '#10b981' }}>{activeState.recInfra?.yield}</strong>
                  </div>
                </div>
                <div style={{ fontSize: '8px', color: '#94a3b8', lineHeight: 1.3, borderTop: '1px solid rgba(255,255,255,0.05)', paddingTop: '6px' }}>
                  {activeState.recInfra?.rationale}
                </div>
              </div>

              {/* PILLAR 3: RECOMMENDED ISSUE ACTION */}
              <div style={{
                backgroundColor: 'rgba(15, 23, 42, 0.7)',
                border: '1px solid rgba(16, 185, 129, 0.25)',
                borderRadius: '8px',
                padding: '12px',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                gap: '8px'
              }}>
                <div>
                  <div style={{ fontSize: '8px', fontWeight: '800', color: '#34d399', textTransform: 'uppercase', letterSpacing: '0.06em', marginBottom: '4px' }}>
                    📢 3. TACTICAL ISSUE ACTION
                  </div>
                  <div style={{ fontSize: '12px', fontWeight: '900', color: '#ffffff' }}>
                    {activeState.recTacticalAction?.label}
                  </div>
                  <div style={{ fontSize: '9px', color: '#cbd5e1', marginTop: '3px' }}>
                    Expected Impact: <strong style={{ color: '#34d399' }}>{activeState.recTacticalAction?.effect}</strong>
                  </div>
                </div>
                <div style={{ fontSize: '8px', color: '#94a3b8', lineHeight: 1.3, borderTop: '1px solid rgba(255,255,255,0.05)', paddingTop: '6px' }}>
                  {activeState.recTacticalAction?.rationale}
                </div>
              </div>

            </div>

            {/* State Political Stance Spotlight */}
            <div style={{
              backgroundColor: 'rgba(30, 41, 59, 0.6)',
              border: '1px dashed rgba(168, 85, 247, 0.3)',
              borderRadius: '8px',
              padding: '10px 14px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              flexWrap: 'wrap',
              gap: '10px'
            }}>
              <div>
                <span style={{ fontSize: '8.5px', fontWeight: '800', color: '#c084fc', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                  ⚡ REGIONAL POLITICAL NARRATIVE STANCE:
                </span>
                <p style={{ margin: '3px 0 0', fontSize: '10.5px', color: '#ffffff', fontWeight: 600, lineHeight: 1.4 }}>
                  {activeState.issueSpotlight}
                </p>
              </div>

              <button
                onClick={() => onNavigateTab && onNavigateTab('operations', 'states')}
                style={{
                  padding: '5px 12px',
                  borderRadius: '6px',
                  border: '1px solid #10b981',
                  backgroundColor: 'rgba(16, 185, 129, 0.2)',
                  color: '#34d399',
                  fontSize: '9.5px',
                  fontWeight: 800,
                  cursor: 'pointer',
                  flexShrink: 0
                }}
              >
                Open State Ground War →
              </button>
            </div>
          </div>
        )}
      </div>

      {/* ------------------------------------------------------------------ */}
      {/* 4. DYNAMIC TURN COMMAND WARNINGS (UNPLAYED STATES, MORALE, HEAT)   */}
      {/* ------------------------------------------------------------------ */}
      {hintsData.urgentWarnings && hintsData.urgentWarnings.length > 0 && (
        <div style={{
          backgroundColor: 'rgba(239, 68, 68, 0.12)',
          border: '1.5px solid #ef4444',
          borderRadius: '12px',
          padding: '12px 16px',
          boxShadow: '0 4px 16px rgba(239, 68, 68, 0.25)',
          display: 'flex',
          flexDirection: 'column',
          gap: '8px'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span style={{ fontSize: '16px' }}>🚨</span>
            <span style={{ fontSize: '11px', fontWeight: '900', color: '#f87171', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
              Urgent Turn Command Directives — Action Required
            </span>
            <span className="nwr-badge nwr-badge-rose" style={{ fontSize: '8px' }}>
              {hintsData.urgentWarnings.length} PENDING ALERTS
            </span>
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
            {hintsData.urgentWarnings.map((warn, idx) => (
              <div key={idx} style={{
                fontSize: '11px',
                color: '#fecaca',
                display: 'flex',
                alignItems: 'flex-start',
                gap: '6px',
                lineHeight: 1.4
              }}>
                <span style={{ color: '#ef4444', fontWeight: '900' }}>•</span>
                <span>{warn}</span>
              </div>
            ))}
          </div>
        </div>
      )}

    </div>
  );
}
