import React from 'react';

/**
 * NationalTurnDebriefModal
 * Displays an end-of-turn debrief pop-up summarizing:
 * - Changes in Player Party stats (Funds, Morale, Workers, Volunteers, Donors, Corruption, Projected Seats)
 * - Infrastructure yields & newly constructed buildings across states
 * - Coalition & Alliance movements (new alliances, newly joined parties, seat counts)
 * - State Campaign operations & AI party maneuvers
 * - Scheduled State Elections outcomes & Finance resolution
 */
export default function NationalTurnDebriefModal({
  isOpen,
  debriefData,
  onClose
}) {
  if (!isOpen || !debriefData) return null;

  const {
    completedSeason = 1,
    nextSeason = 2,
    playerPartyName = 'Your Party',
    playerStats = {},
    alliances = {},
    buildings = {},
    newlyUnlockedStates = [],
    stateShifts = [],
    financeReport = null,
    eventsReport = null
  } = debriefData;

  const formatDelta = (val, isCurrency = false, isPercent = false) => {
    if (val === undefined || val === null || val === 0) {
      return <span style={{ color: '#94a3b8' }}>— No change</span>;
    }
    const isPositive = val > 0;
    const sign = isPositive ? '+' : '';
    const formatted = isCurrency
      ? `${sign}₹${val.toFixed(1)} Cr`
      : isPercent
      ? `${sign}${val.toFixed(1)}%`
      : `${sign}${val.toLocaleString()}`;
    return (
      <span style={{ color: isPositive ? '#34d399' : '#f87171', fontWeight: 800 }}>
        {formatted} {isPositive ? '▲' : '▼'}
      </span>
    );
  };

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
          maxWidth: '900px',
          maxHeight: '92vh',
          backgroundColor: '#0c1530',
          border: '2px solid rgba(56, 189, 248, 0.4)',
          borderRadius: '16px',
          boxShadow: '0 0 50px rgba(56, 189, 248, 0.2), 0 25px 60px rgba(0,0,0,0.9)',
          display: 'flex',
          flexDirection: 'column',
          overflow: 'hidden',
          animation: 'nwrModalFadeIn 0.3s cubic-bezier(0.16, 1, 0.3, 1)'
        }}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div
          style={{
            padding: '20px 24px',
            background: 'linear-gradient(135deg, rgba(2, 132, 199, 0.25) 0%, rgba(15, 23, 42, 0.95) 100%)',
            borderBottom: '1px solid rgba(255, 255, 255, 0.1)',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            flexWrap: 'wrap',
            gap: '12px'
          }}
        >
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '4px' }}>
              <span
                style={{
                  backgroundColor: '#0284c7',
                  color: '#ffffff',
                  fontWeight: 900,
                  fontSize: '10px',
                  letterSpacing: '0.08em',
                  padding: '3px 9px',
                  borderRadius: '20px',
                  textTransform: 'uppercase'
                }}
              >
                🏁 SEASON CONCLUDED
              </span>
              <span style={{ fontSize: '12px', color: '#94a3b8' }}>
                Turn {completedSeason} Debrief ➔ Entering Turn {nextSeason}
              </span>
            </div>
            <h2 style={{ margin: 0, fontSize: '20px', fontWeight: 900, color: '#ffffff', letterSpacing: '-0.02em' }}>
              Strategic Round Overview: {playerPartyName}
            </h2>
          </div>

          <button
            onClick={onClose}
            style={{
              backgroundColor: 'rgba(255, 255, 255, 0.08)',
              border: '1px solid rgba(255, 255, 255, 0.15)',
              color: '#94a3b8',
              width: '32px',
              height: '32px',
              borderRadius: '8px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontSize: '16px',
              cursor: 'pointer',
              transition: 'all 0.2s'
            }}
            title="Dismiss"
          >
            ✕
          </button>
        </div>

        {/* Scrollable Content Body */}
        <div style={{ padding: '20px 24px', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '20px' }}>

          {/* 1. Core Party Stats Shift Cards */}
          <div>
            <div style={{ fontSize: '11px', fontWeight: 900, color: '#38bdf8', textTransform: 'uppercase', letterSpacing: '0.05em', marginBottom: '10px' }}>
              📊 Party Stats & Electoral Trajectory Shifts
            </div>

            <div style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(130px, 1fr))',
              gap: '10px'
            }}>
              {/* Treasury */}
              <div style={statCardStyle}>
                <div style={statLabelStyle}>💰 Treasury</div>
                <div style={statValueStyle}>
                  ₹{(playerStats.funds?.next || 0).toFixed(1)} Cr
                </div>
                <div style={statDeltaStyle}>
                  {formatDelta(playerStats.funds?.delta, true)}
                </div>
              </div>

              {/* Projected Lok Sabha Seats */}
              <div style={{ ...statCardStyle, border: '1px solid rgba(168, 85, 247, 0.4)' }}>
                <div style={{ ...statLabelStyle, color: '#c084fc' }}>🏛️ Projected Seats</div>
                <div style={{ ...statValueStyle, color: '#c084fc' }}>
                  {playerStats.projSeats?.next || 0} / 543
                </div>
                <div style={statDeltaStyle}>
                  {formatDelta(playerStats.projSeats?.delta)}
                </div>
              </div>

              {/* Morale */}
              <div style={statCardStyle}>
                <div style={statLabelStyle}>⚡ Morale</div>
                <div style={statValueStyle}>
                  {playerStats.morale?.next || 0}%
                </div>
                <div style={statDeltaStyle}>
                  {formatDelta(playerStats.morale?.delta, false, true)}
                </div>
              </div>

              {/* Cadre Workers */}
              <div style={statCardStyle}>
                <div style={statLabelStyle}>🚩 Cadre Workers</div>
                <div style={statValueStyle}>
                  {(playerStats.workers?.next || 0).toLocaleString()}
                </div>
                <div style={statDeltaStyle}>
                  {formatDelta(playerStats.workers?.delta)}
                </div>
              </div>

              {/* Volunteers */}
              <div style={statCardStyle}>
                <div style={statLabelStyle}>🤝 Volunteers</div>
                <div style={statValueStyle}>
                  {(playerStats.volunteers?.next || 0).toLocaleString()}
                </div>
                <div style={statDeltaStyle}>
                  {formatDelta(playerStats.volunteers?.delta)}
                </div>
              </div>

              {/* Donors */}
              <div style={statCardStyle}>
                <div style={statLabelStyle}>👥 Donors</div>
                <div style={statValueStyle}>
                  {(playerStats.donors?.next || 0).toLocaleString()}
                </div>
                <div style={statDeltaStyle}>
                  {formatDelta(playerStats.donors?.delta)}
                </div>
              </div>

              {/* Corruption */}
              <div style={statCardStyle}>
                <div style={statLabelStyle}>⚠️ Corruption</div>
                <div style={{ ...statValueStyle, color: (playerStats.corruption?.next || 0) > 30 ? '#f87171' : '#e2e8f0' }}>
                  {playerStats.corruption?.next || 0}%
                </div>
                <div style={statDeltaStyle}>
                  {playerStats.corruption?.delta !== 0 ? (
                    <span style={{ color: (playerStats.corruption?.delta || 0) > 0 ? '#f87171' : '#34d399', fontWeight: 800 }}>
                      {(playerStats.corruption?.delta || 0) > 0 ? `+${playerStats.corruption?.delta}% ⚠️` : `${playerStats.corruption?.delta}% ▼`}
                    </span>
                  ) : (
                    <span style={{ color: '#94a3b8' }}>— Stable</span>
                  )}
                </div>
              </div>
            </div>
          </div>

          {/* 2. Infrastructure & Building Developments */}
          <div style={{
            background: 'rgba(15, 23, 42, 0.7)',
            border: '1px solid rgba(56, 189, 248, 0.2)',
            borderRadius: '12px',
            padding: '14px 16px'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '10px' }}>
              <div style={{ fontSize: '11px', fontWeight: 900, color: '#38bdf8', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                🏗️ Infrastructure & Party Machinery
              </div>
              {buildings.totalNetIncome > 0 && (
                <span className="nwr-badge nwr-badge-emerald" style={{ fontSize: '9px' }}>
                  +₹{buildings.totalNetIncome.toFixed(1)} Cr Passive Revenue Collected
                </span>
              )}
            </div>

            {buildings.newBuildings && buildings.newBuildings.length > 0 ? (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                {buildings.newBuildings.map((b, idx) => (
                  <div key={idx} style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    padding: '8px 12px',
                    background: 'rgba(56, 189, 248, 0.08)',
                    border: '1px solid rgba(56, 189, 248, 0.25)',
                    borderRadius: '8px'
                  }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <span style={{ fontSize: '16px' }}>🏛️</span>
                      <div>
                        <div style={{ fontWeight: 800, color: '#ffffff', fontSize: '11px' }}>
                          {b.buildingName} in {b.stateName}
                        </div>
                        <div style={{ fontSize: '9px', color: '#94a3b8' }}>
                          Constructed / Upgraded ({b.count} Active Unit{b.count > 1 ? 's' : ''})
                        </div>
                      </div>
                    </div>
                    <span style={{ fontSize: '9px', fontWeight: 800, color: '#34d399', backgroundColor: 'rgba(52, 211, 153, 0.15)', padding: '2px 8px', borderRadius: '4px' }}>
                      NEW FACILITY READY
                    </span>
                  </div>
                ))}
              </div>
            ) : (
              <div style={{ fontSize: '10.5px', color: '#94a3b8' }}>
                {buildings.totalActiveCount > 0 ? (
                  <>Existing state machinery active ({buildings.totalActiveCount} structures across party hubs). All facilities yielded scheduled treasury funds and recruitment bonuses.</>
                ) : (
                  <>No infrastructure built yet. You can construct State Party HQs, Media Cells, Legal Cells, and Trade Unions under the States operations tab.</>
                )}
              </div>
            )}
          </div>

          {/* 3. Coalition & Alliances Section */}
          <div style={{
            background: 'rgba(15, 23, 42, 0.7)',
            border: '1px solid rgba(168, 85, 247, 0.25)',
            borderRadius: '12px',
            padding: '14px 16px'
          }}>
            <div style={{ fontSize: '11px', fontWeight: 900, color: '#c084fc', textTransform: 'uppercase', letterSpacing: '0.05em', marginBottom: '10px' }}>
              🤝 Coalition Front & Alliance Movements
            </div>

            {alliances.hasPlayerAlliance ? (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                <div style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  padding: '10px 14px',
                  background: 'linear-gradient(135deg, rgba(168, 85, 247, 0.12) 0%, rgba(30, 41, 59, 0.8) 100%)',
                  border: '1px solid rgba(168, 85, 247, 0.35)',
                  borderRadius: '10px'
                }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                    <div style={{
                      width: '10px',
                      height: '10px',
                      borderRadius: '50%',
                      backgroundColor: alliances.allianceColor || '#c084fc'
                    }} />
                    <div>
                      <div style={{ fontWeight: 900, color: '#ffffff', fontSize: '12px' }}>
                        {alliances.allianceName}
                      </div>
                      <div style={{ fontSize: '9.5px', color: '#94a3b8' }}>
                        Led by {alliances.leaderPartyKey} • {alliances.memberCount} coalition partner{alliances.memberCount > 1 ? 's' : ''}
                      </div>
                    </div>
                  </div>

                  <div style={{ textAlign: 'right' }}>
                    <div style={{ fontSize: '13px', fontWeight: 900, color: alliances.totalProjectedSeats >= 272 ? '#34d399' : '#38bdf8' }}>
                      {alliances.totalProjectedSeats} / 272 Seats
                    </div>
                    <div style={{ fontSize: '8.5px', fontWeight: 800, color: alliances.totalProjectedSeats >= 272 ? '#34d399' : '#94a3b8' }}>
                      {alliances.totalProjectedSeats >= 272 ? '👑 MAJORITY ATTAINED' : `${272 - alliances.totalProjectedSeats} seats to majority`}
                    </div>
                  </div>
                </div>

                {/* Newly joined members this turn */}
                {alliances.newJoinedMembers && alliances.newJoinedMembers.length > 0 && (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                    <div style={{ fontSize: '10px', fontWeight: 800, color: '#cbd5e1' }}>Newly Recruited Coalition Partners:</div>
                    {alliances.newJoinedMembers.map((m, idx) => (
                      <div key={idx} style={{
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'space-between',
                        padding: '6px 12px',
                        background: 'rgba(52, 211, 153, 0.08)',
                        border: '1px solid rgba(52, 211, 153, 0.3)',
                        borderRadius: '6px',
                        fontSize: '10.5px'
                      }}>
                        <span style={{ fontWeight: 800, color: '#ffffff' }}>
                          {m.shortName || m.partyKey} ({m.partyName})
                        </span>
                        <span style={{ color: '#34d399', fontWeight: 900 }}>
                          +{m.seats || 0} Seats Added
                        </span>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            ) : (
              <div style={{ fontSize: '10.5px', color: '#94a3b8' }}>
                Your party remains unaligned. You can establish a new coalition front and recruit regional allies under the Coalition tab to cross the 272-seat threshold.
              </div>
            )}
          </div>

          {/* 3b. Newly Unlocked Regional Theatres via Alliance */}
          {newlyUnlockedStates && newlyUnlockedStates.length > 0 && (
            <div style={{
              background: 'linear-gradient(135deg, rgba(16, 185, 129, 0.15) 0%, rgba(15, 23, 42, 0.85) 100%)',
              border: '1.5px solid #10b981',
              borderRadius: '12px',
              padding: '14px 16px',
              boxShadow: '0 0 25px rgba(16, 185, 129, 0.25)'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '10px' }}>
                <div style={{ fontSize: '11px', fontWeight: 900, color: '#34d399', textTransform: 'uppercase', letterSpacing: '0.05em', display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <span>✨</span> NEW REGIONAL THEATRES UNLOCKED VIA ALLIANCE
                </div>
                <span style={{
                  fontSize: '9px',
                  fontWeight: 900,
                  padding: '2px 8px',
                  borderRadius: '4px',
                  backgroundColor: 'rgba(16, 185, 129, 0.25)',
                  color: '#34d399',
                  border: '1px solid #10b981'
                }}>
                  {newlyUnlockedStates.length} New State{newlyUnlockedStates.length > 1 ? 's' : ''} Ready
                </span>
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                {newlyUnlockedStates.map((st, idx) => (
                  <div key={idx} style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    padding: '8px 12px',
                    backgroundColor: 'rgba(16, 185, 129, 0.1)',
                    border: '1px solid rgba(16, 185, 129, 0.3)',
                    borderRadius: '8px'
                  }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                      <span style={{ fontSize: '18px' }}>🗺️</span>
                      <div>
                        <div style={{ fontWeight: 900, color: '#ffffff', fontSize: '12px' }}>
                          {st.stateName}
                        </div>
                        <div style={{ fontSize: '9.5px', color: '#94a3b8' }}>
                          Unlocked via coalition partner <strong style={{ color: '#38bdf8' }}>{st.unlockedByPartner}</strong> • {st.totalLokSabhaSeats} Lok Sabha Seats ({st.totalAssemblySeats} Assembly Seats)
                        </div>
                      </div>
                    </div>
                    <span style={{
                      fontSize: '9px',
                      fontWeight: 800,
                      color: '#34d399',
                      backgroundColor: 'rgba(52, 211, 153, 0.2)',
                      padding: '3px 8px',
                      borderRadius: '4px',
                      border: '1px solid rgba(52, 211, 153, 0.4)'
                    }}>
                      ⚡ BATTLEGROUND UNLOCKED
                    </span>
                  </div>
                ))}
              </div>
              <p style={{ margin: '8px 0 0', fontSize: '10px', color: '#94a3b8' }}>
                You can now allocate state funds, construct regional infrastructure, and execute campaign pushes in these newly accessible states next turn!
              </p>
            </div>
          )}

          {/* 4. State Battlegrounds & Operational Momentum */}
          {stateShifts && stateShifts.length > 0 && (
            <div style={{
              background: 'rgba(15, 23, 42, 0.7)',
              border: '1px solid rgba(56, 189, 248, 0.2)',
              borderRadius: '12px',
              padding: '14px 16px'
            }}>
              <div style={{ fontSize: '11px', fontWeight: 900, color: '#38bdf8', textTransform: 'uppercase', letterSpacing: '0.05em', marginBottom: '10px' }}>
                🗺️ Playable State Field Reports & AI Activity
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                {stateShifts.map((s, idx) => (
                  <div key={idx} style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    flexWrap: 'wrap',
                    gap: '8px',
                    padding: '8px 12px',
                    background: 'rgba(30, 41, 59, 0.6)',
                    border: '1px solid rgba(255, 255, 255, 0.06)',
                    borderRadius: '8px'
                  }}>
                    <div>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                        <span style={{ fontWeight: 900, color: '#ffffff', fontSize: '11px' }}>{s.stateName}</span>
                        <span style={{
                          fontSize: '8px',
                          fontWeight: 800,
                          padding: '1px 5px',
                          borderRadius: '4px',
                          backgroundColor: s.wasSkipped ? 'rgba(100, 116, 139, 0.2)' : 'rgba(52, 211, 153, 0.2)',
                          color: s.wasSkipped ? '#94a3b8' : '#34d399'
                        }}>
                          {s.wasSkipped ? 'SKIPPED' : 'ACTIVE CAMPAIGN'}
                        </span>
                      </div>
                      <div style={{ fontSize: '9px', color: '#94a3b8', marginTop: '2px' }}>
                        {s.latestLog || (s.wasSkipped ? 'Passive infrastructure and cadre yields collected.' : 'Ground cadres deployed across operational regions.')}
                      </div>
                    </div>

                    <div style={{ textAlign: 'right' }}>
                      <div style={{ fontSize: '11px', fontWeight: 900, color: '#ffffff' }}>
                        {s.support?.toFixed(1)}% Support
                      </div>
                      <div style={{ fontSize: '9px' }}>
                        {formatDelta(s.deltaSupport, false, true)}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* 5. Directives & Operations Resolution */}
          {(financeReport || eventsReport) && (
            <div style={{
              background: 'rgba(15, 23, 42, 0.7)',
              border: '1px solid rgba(245, 158, 11, 0.25)',
              borderRadius: '12px',
              padding: '14px 16px'
            }}>
              <div style={{ fontSize: '11px', fontWeight: 900, color: '#f59e0b', textTransform: 'uppercase', letterSpacing: '0.05em', marginBottom: '8px' }}>
                📜 National Directives & Finance Impact
              </div>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', fontSize: '10px', color: '#cbd5e1' }}>
                {financeReport && (
                  <div style={{ display: 'flex', alignItems: 'flex-start', gap: '6px' }}>
                    <span>💳</span>
                    <span>{financeReport}</span>
                  </div>
                )}
                {eventsReport && (
                  <div style={{ display: 'flex', alignItems: 'flex-start', gap: '6px' }}>
                    <span>📢</span>
                    <span>{eventsReport}</span>
                  </div>
                )}
              </div>
            </div>
          )}

        </div>

        {/* Footer Dismiss / Continue Button */}
        <div
          style={{
            padding: '16px 24px',
            backgroundColor: '#091024',
            borderTop: '1px solid rgba(255, 255, 255, 0.1)',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            flexWrap: 'wrap',
            gap: '12px'
          }}
        >
          <div style={{ fontSize: '10px', color: '#94a3b8' }}>
            All statistics updated. Ready for Turn {nextSeason} command operations.
          </div>

          <button
            onClick={onClose}
            style={{
              background: 'linear-gradient(135deg, #0284c7 0%, #0369a1 100%)',
              border: '1px solid #38bdf8',
              color: '#ffffff',
              padding: '10px 24px',
              borderRadius: '10px',
              fontSize: '12px',
              fontWeight: 900,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              boxShadow: '0 0 20px rgba(2, 132, 199, 0.4)',
              transition: 'all 0.2s'
            }}
          >
            <span>START TURN {nextSeason} DIRECTIVES</span>
            <span>→</span>
          </button>
        </div>
      </div>
    </div>
  );
}

const statCardStyle = {
  background: 'rgba(30, 41, 59, 0.5)',
  border: '1px solid rgba(255, 255, 255, 0.08)',
  borderRadius: '10px',
  padding: '10px 12px',
  display: 'flex',
  flexDirection: 'column',
  gap: '3px'
};

const statLabelStyle = {
  fontSize: '9px',
  fontWeight: 800,
  color: '#94a3b8',
  textTransform: 'uppercase',
  letterSpacing: '0.04em'
};

const statValueStyle = {
  fontSize: '13px',
  fontWeight: 900,
  color: '#ffffff'
};

const statDeltaStyle = {
  fontSize: '9.5px',
  marginTop: '2px'
};
