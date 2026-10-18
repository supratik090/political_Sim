import React from 'react';

/**
 * NationalElectionVerdictModal
 * Displays the definitive 543 Lok Sabha Election Verdict
 * Triggered either via a No-Confidence Motion (>272 projected seats) or at Turn 60 Scheduled Election.
 */
export default function NationalElectionVerdictModal({
  electionResult,
  onClose,
  onReturnToHeadquarters
}) {
  if (!electionResult) return null;

  const {
    triggerReason,
    season,
    totalSeats = 543,
    majorityThreshold = 272,
    isPlayerVictory = false,
    winningAllianceKey,
    winningAllianceName = 'Ruling Coalition',
    winningAllianceSeats = 0,
    playerAllianceKey,
    playerAllianceName = 'Player Alliance',
    playerAllianceSeats = 0,
    headline,
    narrative,
    partyBreakdown = [],
    allianceBreakdown = []
  } = electionResult;

  const isNoConfidence = triggerReason === 'NO_CONFIDENCE_MOTION';

  // Sort party breakdown by seats won descending
  const sortedParties = [...partyBreakdown].sort((a, b) => (b.seatsWon || 0) - (a.seatsWon || 0));

  return (
    <div
      style={{
        position: 'fixed',
        inset: 0,
        zIndex: 9999,
        backgroundColor: 'rgba(5, 10, 25, 0.88)',
        backdropFilter: 'blur(10px)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '16px',
        overflowY: 'auto'
      }}
      onClick={onClose}
    >
      <div
        style={{
          width: '100%',
          maxWidth: '860px',
          maxHeight: '92vh',
          backgroundColor: '#0c1530',
          border: isPlayerVictory
            ? '2px solid rgba(16, 185, 129, 0.6)'
            : '2px solid rgba(239, 68, 68, 0.5)',
          borderRadius: '16px',
          boxShadow: isPlayerVictory
            ? '0 0 50px rgba(16, 185, 129, 0.25), 0 25px 60px rgba(0,0,0,0.9)'
            : '0 0 50px rgba(239, 68, 68, 0.2), 0 25px 60px rgba(0,0,0,0.9)',
          display: 'flex',
          flexDirection: 'column',
          overflow: 'hidden',
          animation: 'nwrModalFadeIn 0.3s cubic-bezier(0.16, 1, 0.3, 1)'
        }}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Modal Top Header Banner */}
        <div
          style={{
            padding: '20px 24px',
            background: isPlayerVictory
              ? 'linear-gradient(135deg, rgba(16, 185, 129, 0.22) 0%, rgba(13, 22, 48, 0.95) 100%)'
              : 'linear-gradient(135deg, rgba(239, 68, 68, 0.22) 0%, rgba(13, 22, 48, 0.95) 100%)',
            borderBottom: '1px solid rgba(255, 255, 255, 0.1)',
            position: 'relative'
          }}
        >
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: '16px' }}>
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '6px' }}>
                <span
                  style={{
                    backgroundColor: isPlayerVictory ? '#10b981' : '#ef4444',
                    color: '#ffffff',
                    fontWeight: 900,
                    fontSize: '10px',
                    letterSpacing: '0.08em',
                    padding: '3px 9px',
                    borderRadius: '20px',
                    textTransform: 'uppercase'
                  }}
                >
                  {isPlayerVictory ? '🏆 HISTORIC VICTORY' : '⚠️ OPPOSITION MANDATE'}
                </span>

                <span
                  style={{
                    backgroundColor: 'rgba(255, 255, 255, 0.08)',
                    color: '#94a3b8',
                    fontSize: '9.5px',
                    fontWeight: 700,
                    padding: '3px 8px',
                    borderRadius: '20px'
                  }}
                >
                  {isNoConfidence ? '⚡ Triggered by No-Confidence Motion' : `📅 Season ${season} Scheduled Election`}
                </span>
              </div>

              <h2
                style={{
                  margin: '4px 0 6px 0',
                  fontSize: '20px',
                  fontWeight: 900,
                  color: isPlayerVictory ? '#6ee7b7' : '#fca5a5',
                  letterSpacing: '-0.02em',
                  lineHeight: 1.25
                }}
              >
                {headline || (isPlayerVictory ? 'National Mandate: Alliance Sweeps Lok Sabha' : 'Election Mandate Concluded')}
              </h2>

              <p
                style={{
                  margin: 0,
                  fontSize: '11px',
                  color: '#cbd5e1',
                  lineHeight: 1.45,
                  maxWidth: '720px'
                }}
              >
                {narrative}
              </p>
            </div>

            <button
              onClick={onClose}
              style={{
                background: 'rgba(255,255,255,0.08)',
                border: 'none',
                color: '#94a3b8',
                fontSize: '18px',
                width: '32px',
                height: '32px',
                borderRadius: '8px',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                flexShrink: 0
              }}
              title="Close Verdict"
            >
              ✕
            </button>
          </div>
        </div>

        {/* Scrollable Content Body */}
        <div style={{ padding: '20px 24px', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '20px' }}>
          {/* Key Metric Trophies / Stats Bar */}
          <div
            style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(170px, 1fr))',
              gap: '12px'
            }}
          >
            <div
              style={{
                backgroundColor: 'rgba(15, 23, 42, 0.75)',
                border: '1px solid rgba(255,255,255,0.08)',
                borderRadius: '10px',
                padding: '12px 14px'
              }}
            >
              <div style={{ fontSize: '9px', fontWeight: 700, color: '#94a3b8', textTransform: 'uppercase' }}>
                Total Lok Sabha Seats
              </div>
              <div style={{ fontSize: '22px', fontWeight: 900, color: '#ffffff', marginTop: '4px' }}>
                {totalSeats}
              </div>
              <div style={{ fontSize: '9px', color: '#64748b' }}>
                Majority Mark: <strong style={{ color: '#fbbf24' }}>{majorityThreshold}</strong>
              </div>
            </div>

            <div
              style={{
                backgroundColor: isPlayerVictory ? 'rgba(16, 185, 129, 0.12)' : 'rgba(15, 23, 42, 0.75)',
                border: isPlayerVictory ? '1px solid rgba(16, 185, 129, 0.4)' : '1px solid rgba(255,255,255,0.08)',
                borderRadius: '10px',
                padding: '12px 14px'
              }}
            >
              <div style={{ fontSize: '9px', fontWeight: 700, color: '#94a3b8', textTransform: 'uppercase' }}>
                Your Alliance Tally
              </div>
              <div
                style={{
                  fontSize: '22px',
                  fontWeight: 900,
                  color: isPlayerVictory ? '#34d399' : '#f87171',
                  marginTop: '4px'
                }}
              >
                {playerAllianceSeats}
                <span style={{ fontSize: '11px', fontWeight: 700, marginLeft: '6px', color: '#94a3b8' }}>
                  / {totalSeats}
                </span>
              </div>
              <div style={{ fontSize: '9px', color: playerAllianceSeats >= 272 ? '#10b981' : '#f87171' }}>
                {playerAllianceSeats >= 272 ? '✓ Absolute Majority Formed' : `Deficit: ${272 - playerAllianceSeats} seats to majority`}
              </div>
            </div>

            <div
              style={{
                backgroundColor: 'rgba(15, 23, 42, 0.75)',
                border: '1px solid rgba(255,255,255,0.08)',
                borderRadius: '10px',
                padding: '12px 14px'
              }}
            >
              <div style={{ fontSize: '9px', fontWeight: 700, color: '#94a3b8', textTransform: 'uppercase' }}>
                Winning Coalition
              </div>
              <div style={{ fontSize: '16px', fontWeight: 900, color: '#38bdf8', marginTop: '6px', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                {winningAllianceName}
              </div>
              <div style={{ fontSize: '10px', fontWeight: 800, color: '#e2e8f0', marginTop: '2px' }}>
                {winningAllianceSeats} Seats Won
              </div>
            </div>
          </div>

          {/* Parliamentary Alliance Fronts Summary */}
          {allianceBreakdown && allianceBreakdown.length > 0 && (
            <div
              style={{
                backgroundColor: 'rgba(15, 23, 42, 0.6)',
                border: '1px solid rgba(255,255,255,0.08)',
                borderRadius: '12px',
                padding: '14px 16px'
              }}
            >
              <div style={{ fontSize: '10.5px', fontWeight: 800, color: '#f8fafc', textTransform: 'uppercase', letterSpacing: '0.05em', marginBottom: '12px' }}>
                Coalition Standings vs 272 Majority Benchmark
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                {allianceBreakdown.map(alliance => {
                  const percentage = ((alliance.totalSeats / totalSeats) * 100).toFixed(1);
                  const isWinner = alliance.hasMajority || alliance.allianceId === winningAllianceKey;

                  return (
                    <div key={alliance.allianceId}>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                          <div
                            style={{
                              width: '10px',
                              height: '10px',
                              borderRadius: '3px',
                              backgroundColor: alliance.color || '#38bdf8'
                            }}
                          />
                          <span style={{ fontSize: '11px', fontWeight: 800, color: '#ffffff' }}>
                            {alliance.allianceName}
                          </span>
                          {alliance.isPlayerAlliance && (
                            <span style={{ fontSize: '8px', fontWeight: 900, backgroundColor: '#10b981', color: '#0f172a', padding: '1px 5px', borderRadius: '3px' }}>
                              YOU
                            </span>
                          )}
                          {isWinner && (
                            <span style={{ fontSize: '8px', fontWeight: 900, backgroundColor: '#f59e0b', color: '#0f172a', padding: '1px 5px', borderRadius: '3px' }}>
                              GOVERNMENT
                            </span>
                          )}
                        </div>

                        <div style={{ fontSize: '11.5px', fontWeight: 900, color: '#ffffff' }}>
                          {alliance.totalSeats} <span style={{ fontSize: '9px', fontWeight: 600, color: '#94a3b8' }}>({percentage}%)</span>
                        </div>
                      </div>

                      {/* Progress Bar with 272 Mark Line */}
                      <div style={{ position: 'relative', width: '100%', height: '8px', backgroundColor: 'rgba(255,255,255,0.05)', borderRadius: '4px', overflow: 'hidden' }}>
                        <div
                          style={{
                            width: `${percentage}%`,
                            height: '100%',
                            backgroundColor: alliance.color || '#38bdf8',
                            borderRadius: '4px',
                            transition: 'width 0.6s ease'
                          }}
                        />
                        {/* 272 Mark Indicator at 50.1% */}
                        <div
                          style={{
                            position: 'absolute',
                            left: '50.1%',
                            top: 0,
                            bottom: 0,
                            width: '2px',
                            backgroundColor: '#fbbf24',
                            zIndex: 2
                          }}
                          title="272 Majority Threshold"
                        />
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          )}

          {/* Party-by-Party 543 Lok Sabha Breakdown Table */}
          <div
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.6)',
              border: '1px solid rgba(255,255,255,0.08)',
              borderRadius: '12px',
              padding: '14px 16px',
              overflowX: 'auto'
            }}
          >
            <div style={{ fontSize: '10.5px', fontWeight: 800, color: '#f8fafc', textTransform: 'uppercase', letterSpacing: '0.05em', marginBottom: '10px' }}>
              Final Party Seats Breakdown (543 Lok Sabha Seats)
            </div>

            <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '10px', textAlign: 'left' }}>
              <thead>
                <tr style={{ borderBottom: '1px solid rgba(255,255,255,0.1)', color: '#94a3b8', fontSize: '9px', textTransform: 'uppercase' }}>
                  <th style={{ padding: '8px 6px' }}>Party</th>
                  <th style={{ padding: '8px 6px', textAlign: 'center' }}>Alliance</th>
                  <th style={{ padding: '8px 6px', textAlign: 'right' }}>Seats Won</th>
                  <th style={{ padding: '8px 6px', textAlign: 'right' }}>Swing</th>
                  <th style={{ padding: '8px 6px', textAlign: 'right' }}>Morale</th>
                  <th style={{ padding: '8px 6px', textAlign: 'right' }}>Warchest</th>
                </tr>
              </thead>
              <tbody>
                {sortedParties.map(p => {
                  const delta = p.seatDelta || 0;
                  const isPlayer = p.isPlayerParty;

                  return (
                    <tr
                      key={p.partyKey}
                      style={{
                        borderBottom: '1px solid rgba(255,255,255,0.04)',
                        backgroundColor: isPlayer ? 'rgba(16, 185, 129, 0.08)' : 'transparent'
                      }}
                    >
                      <td style={{ padding: '7px 6px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <div
                          style={{
                            width: '8px',
                            height: '8px',
                            borderRadius: '50%',
                            backgroundColor: p.color || '#94a3b8',
                            flexShrink: 0
                          }}
                        />
                        <span style={{ fontWeight: isPlayer ? 900 : 700, color: '#ffffff' }}>
                          {p.shortName || p.partyName}
                        </span>
                        {isPlayer && (
                          <span style={{ fontSize: '7.5px', fontWeight: 900, backgroundColor: '#10b981', color: '#0f172a', padding: '0 4px', borderRadius: '3px' }}>
                            YOU
                          </span>
                        )}
                      </td>
                      <td style={{ padding: '7px 6px', textAlign: 'center', color: '#cbd5e1' }}>
                        {(() => {
                          const allMatch = allianceBreakdown.find(a => (a.allianceId && a.allianceId.toLowerCase() === (p.allianceId || '').toLowerCase()));
                          return allMatch ? (allMatch.allianceName || p.allianceId) : (p.allianceId || 'UNALIGNED');
                        })()}
                      </td>
                      <td style={{ padding: '7px 6px', textAlign: 'right', fontWeight: 900, fontSize: '12px', color: '#ffffff' }}>
                        {p.seatsWon}
                      </td>
                      <td style={{ padding: '7px 6px', textAlign: 'right', fontWeight: 800 }}>
                        <span
                          style={{
                            color: delta > 0 ? '#34d399' : delta < 0 ? '#f87171' : '#94a3b8'
                          }}
                        >
                          {delta > 0 ? `+${delta}` : delta}
                        </span>
                      </td>
                      <td style={{ padding: '7px 6px', textAlign: 'right', color: '#94a3b8' }}>
                        {p.morale}%
                      </td>
                      <td style={{ padding: '7px 6px', textAlign: 'right', color: '#94a3b8' }}>
                        ₹{p.funds ? p.funds.toFixed(1) : 0} Cr
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>

        {/* Modal Bottom Actions Footer */}
        <div
          style={{
            padding: '14px 24px',
            backgroundColor: 'rgba(11, 19, 41, 0.95)',
            borderTop: '1px solid rgba(255, 255, 255, 0.1)',
            display: 'flex',
            justifyContent: 'flex-end',
            gap: '12px'
          }}
        >
          <button
            onClick={onClose}
            style={{
              padding: '8px 16px',
              borderRadius: '8px',
              border: '1px solid rgba(255, 255, 255, 0.15)',
              backgroundColor: 'rgba(255, 255, 255, 0.05)',
              color: '#cbd5e1',
              fontSize: '11px',
              fontWeight: 700,
              cursor: 'pointer',
              transition: 'all 0.2s'
            }}
          >
            📊 Review War Room & Standings
          </button>

          {onReturnToHeadquarters && (
            <button
              onClick={onReturnToHeadquarters}
              style={{
                padding: '8px 18px',
                borderRadius: '8px',
                border: 'none',
                background: isPlayerVictory
                  ? 'linear-gradient(135deg, #10b981 0%, #059669 100%)'
                  : 'linear-gradient(135deg, #38bdf8 0%, #0284c7 100%)',
                color: '#ffffff',
                fontSize: '11px',
                fontWeight: 900,
                cursor: 'pointer',
                boxShadow: isPlayerVictory ? '0 4px 15px rgba(16, 185, 129, 0.4)' : '0 4px 15px rgba(56, 189, 248, 0.4)',
                transition: 'all 0.2s'
              }}
            >
              🏠 Return to Headquarters
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
