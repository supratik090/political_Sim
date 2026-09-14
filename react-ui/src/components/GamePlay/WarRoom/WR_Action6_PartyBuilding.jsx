import React, { useState } from 'react';
import { getProgressCost, canAffordCost } from '../gameUtils';

const CATEGORY_CONFIG = [
  { key: 'BUILD',     label: 'Build Party',      icon: '🛡️', color: '#0891B2', bg: 'linear-gradient(145deg,#164e63,#0891b2)' },
  { key: 'OFFENSIVE', label: 'Target Opponents', icon: '💥', color: '#DC2626', bg: 'linear-gradient(145deg,#7f1d1d,#b91c1c)' },
];

function getCategoryGrad(isOffensive) {
  return isOffensive
    ? 'linear-gradient(145deg,#7f1d1d,#b91c1c)'
    : 'linear-gradient(145deg,#164e63,#0891b2)';
}

/**
 * WR_Action6_PartyBuilding — fully native War Room card UI
 * Shows available projects as portrait cards (same style as WR_Action1_Card)
 * Shows completed + in-progress projects as readable dark tiles above.
 */
export default function WR_Action6_PartyBuilding({
  turnData,
  activeParty,
  projectDefs: PROJECT_DEFS = {},
  projectCategoryFilter,
  setProjectCategoryFilter,
  fundingContributions,
  setFundingContributions,
  partyBuildingConfirmed,
  setPartyBuildingConfirmed,
  handleFundProject,
  handleDestroyProject,
  handleSetProjectTarget,
  fundedThisTurn = [],
}) {
  const [destroyConfirm, setDestroyConfirm] = useState(null);

  if (!activeParty) return null;

  const activeProjects   = activeParty.projects || [];
  const completedProjects = activeProjects.filter(p => p.progressPercent >= 100)
    .sort((a, b) => (a.completionTurn || 0) - (b.completionTurn || 0));
  const inProgressProjects = activeProjects.filter(p => p.progressPercent > 0 && p.progressPercent < 100);
  const capReached = fundedThisTurn.length >= 3;

  const availableProjects = Object.entries(PROJECT_DEFS).map(([key, def]) => {
    const existing = activeProjects.find(p => p.projectKey === key && p.progressPercent < 100);
    const buildsThisCycle = activeParty.projectBuildsThisCycle || {};
    const limit = (def.costCoins || 0) > 100 ? 1 : 2;
    const builds = buildsThisCycle[key] || 0;
    const remaining = Math.max(0, limit - builds);
    return { key, ...def, progress: existing ? existing.progressPercent : 0, id: existing ? existing.id : null, remainingBuilds: remaining };
  }).filter(p => p.progress === 0 && !fundedThisTurn.includes(p.key) && p.remainingBuilds > 0);

  const filteredAvail = availableProjects.filter(p =>
    projectCategoryFilter === 'BUILD' ? !p.offensive : p.offensive
  );

  /* ── Label & info helpers ── */
  const PRESETS = [20, 40, 60, 80, 100];
  const opponents = (turnData?.parties || []).filter(p => p.id !== turnData?.activeHumanPartyId);

  return (
    <div style={{ padding: '14px 16px 0' }}>
      {/* Section header */}
      <div style={{ marginBottom: '12px' }}>
        <div style={{ fontSize: '15px', fontWeight: 900, letterSpacing: '0.05em', textTransform: 'uppercase', color: '#F59E0B' }}>
          🏗️ Party Building
        </div>
        <div style={{ fontSize: '12px', color: '#7D8590', marginTop: '2px' }}>
          Fund long-term projects for passive yields
        </div>
        <span style={{ display: 'inline-block', marginTop: '6px', fontSize: '10px', fontWeight: 700, color: '#7D8590', background: 'rgba(255,255,255,0.06)', padding: '2px 8px', borderRadius: '20px', letterSpacing: '0.04em' }}>
          OPTIONAL
        </span>
      </div>

      {/* Cycle info bar */}
      <div style={{
        display: 'flex', justifyContent: 'space-between', alignItems: 'center',
        background: 'rgba(37,99,235,0.08)', border: '1px solid rgba(37,99,235,0.2)',
        padding: '8px 12px', borderRadius: '10px', marginBottom: '14px',
        fontSize: '12px', color: '#60A5FA', fontWeight: 700,
      }}>
        <span>📅 Cycle: <strong>20 turns</strong></span>
        <span>🔄 Refresh in: <strong style={{ color: '#FCD34D' }}>{activeParty.turnsUntilProjectLimitRefresh} turns</strong></span>
      </div>

      {/* Daily cap warning */}
      {capReached && (
        <div className="wr-freeze-banner" style={{ marginBottom: '14px' }}>
          ⚠️ Daily funding limit reached — max 3 projects per turn.
        </div>
      )}

      {/* ── COMPLETED PROJECTS ── */}
      {completedProjects.length > 0 && (
        <div style={{ marginBottom: '16px' }}>
          <div style={{ fontSize: '11px', fontWeight: 800, letterSpacing: '0.07em', textTransform: 'uppercase', color: '#4ADE80', marginBottom: '10px' }}>
            ✅ Completed Infrastructure
          </div>
          {completedProjects.map((proj, idx) => {
            const pDef = PROJECT_DEFS[proj.projectKey] || {};
            const projId = proj.id || proj.projectKey;
            const needsTarget = pDef.offensive && (!proj.targetPartyId || proj.targetPartyId === '');

            return (
              <div key={`${projId}-${idx}`} style={{
                background: needsTarget
                  ? 'linear-gradient(145deg,rgba(220,38,38,0.12),rgba(127,29,29,0.08))'
                  : 'linear-gradient(145deg,rgba(22,163,74,0.12),rgba(6,78,59,0.08))',
                border: `1.5px solid ${needsTarget ? 'rgba(220,38,38,0.45)' : 'rgba(22,163,74,0.35)'}`,
                borderRadius: '12px',
                padding: '12px 14px',
                marginBottom: '10px',
                animation: needsTarget ? 'wr-pending-pulse 1.4s ease-in-out infinite' : 'none',
              }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: '8px' }}>
                  <div>
                    <div style={{ fontSize: '14px', fontWeight: 900, color: needsTarget ? '#F87171' : '#4ADE80', marginBottom: '4px' }}>
                      {pDef.name || proj.projectKey}
                    </div>
                    <div style={{ fontSize: '11px', color: '#D1D5DB', lineHeight: 1.5 }}>
                      {pDef.yield || 'Passive yield active'}
                    </div>
                  </div>
                  {needsTarget && (
                    <span className="wr-badge wr-badge-red" style={{ animation: 'wr-pending-pulse 1.2s ease-in-out infinite', flexShrink: 0 }}>
                      ⚠️ ASSIGN TARGET
                    </span>
                  )}
                  {!needsTarget && !pDef.offensive && (
                    <span className="wr-badge wr-badge-green" style={{ flexShrink: 0 }}>🛡️ Active</span>
                  )}
                </div>

                {/* Target selector for offensive completed projects */}
                {pDef.offensive && (
                  <div style={{ marginTop: '10px' }}>
                    <div style={{ fontSize: '11px', fontWeight: 800, color: '#F59E0B', marginBottom: '8px', letterSpacing: '0.05em', textTransform: 'uppercase' }}>
                      🎯 Select Target
                    </div>
                    <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
                      {opponents.map(opp => {
                        const isSelected = proj.targetPartyId === opp.id;
                        return (
                          <button key={opp.id} onClick={() => handleSetProjectTarget(projId, opp.id)} disabled={partyBuildingConfirmed} style={{
                            display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '4px',
                            padding: '8px 10px', width: '66px',
                            background: isSelected ? 'rgba(245,158,11,0.15)' : 'rgba(255,255,255,0.05)',
                            border: `1.5px solid ${isSelected ? '#F59E0B' : 'rgba(255,255,255,0.12)'}`,
                            borderRadius: '10px', cursor: partyBuildingConfirmed ? 'not-allowed' : 'pointer',
                            touchAction: 'manipulation', WebkitTapHighlightColor: 'transparent',
                            transition: 'all 0.15s ease', minHeight: 'unset', fontFamily: 'Montserrat,sans-serif',
                          }}>
                            <div style={{ width: '30px', height: '30px', borderRadius: '50%', background: 'var(--party-primary-color,#6C3AB5)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '13px', fontWeight: 900, color: '#fff' }}>
                              {(opp.name || '?')[0]?.toUpperCase()}
                            </div>
                            <span style={{ fontSize: '10px', color: '#C9D1D9', textAlign: 'center', lineHeight: 1.2, fontWeight: 700 }}>
                              {opp.name?.split(' ')[0]}
                            </span>
                          </button>
                        );
                      })}
                    </div>
                  </div>
                )}

                {/* Destroy button */}
                <button onClick={() => setDestroyConfirm({ projectKey: projId, refundCoins: pDef.costCoins || 0, name: pDef.name || proj.projectKey })}
                  disabled={partyBuildingConfirmed}
                  style={{
                    marginTop: '10px', padding: '6px 12px', fontSize: '11px', fontWeight: 800,
                    background: 'rgba(220,38,38,0.15)', color: '#F87171',
                    border: '1px solid rgba(220,38,38,0.35)', borderRadius: '8px',
                    cursor: partyBuildingConfirmed ? 'not-allowed' : 'pointer',
                    touchAction: 'manipulation', fontFamily: 'Montserrat,sans-serif', minHeight: 'unset',
                  }}>
                  🗑️ Destroy & Refund ({pDef.costCoins || 0} 💰)
                </button>
              </div>
            );
          })}
        </div>
      )}

      {/* ── IN-PROGRESS PROJECTS ── */}
      {inProgressProjects.length > 0 && (
        <div style={{ marginBottom: '16px' }}>
          <div style={{ fontSize: '11px', fontWeight: 800, letterSpacing: '0.07em', textTransform: 'uppercase', color: '#60A5FA', marginBottom: '10px' }}>
            🔨 Under Construction
          </div>
          {inProgressProjects.map((proj, idx) => {
            const pDef = PROJECT_DEFS[proj.projectKey] || {};
            const projId = proj.id || proj.projectKey;
            const progress = proj.progressPercent || 0;
            const remaining = 100 - progress;
            const presets = [0];
            for (const val of [20, 40, 60, 80, 100]) { if (val <= remaining) presets.push(val); }
            if (remaining > 0 && !presets.includes(remaining)) presets.push(remaining);
            presets.sort((a, b) => a - b);
            const chosenContrib = fundingContributions[proj.id] || fundingContributions[proj.projectKey] || 0;
            const costForContrib = getProgressCost(pDef, chosenContrib);
            const canAfford = canAffordCost(costForContrib, activeParty.stats);
            const isAlreadyFunded = fundedThisTurn.includes(proj.id) || fundedThisTurn.includes(proj.projectKey);

            return (
              <div key={`${projId}-ip-${idx}`} style={{
                background: 'linear-gradient(145deg,rgba(30,58,138,0.25),rgba(23,37,84,0.15))',
                border: '1.5px dashed rgba(96,165,250,0.45)',
                borderRadius: '12px', padding: '12px 14px', marginBottom: '10px',
              }}>
                <div style={{ fontWeight: 900, fontSize: '14px', color: '#93C5FD', marginBottom: '4px' }}>
                  📐 {pDef.name || proj.projectKey}
                  <span style={{ fontSize: '10px', fontWeight: 700, color: '#60A5FA', marginLeft: '8px', letterSpacing: '0.05em' }}>UNDER CONSTRUCTION</span>
                </div>
                <div style={{ fontSize: '11px', color: '#D1D5DB', marginBottom: '10px' }}>Cost: {pDef.cost}</div>

                {/* Progress bar */}
                <div style={{ marginBottom: '10px' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', fontWeight: 700, marginBottom: '4px', color: '#C9D1D9' }}>
                    <span>Progress: {progress}%</span>
                    {chosenContrib > 0 && <span style={{ color: '#4ADE80' }}>+ {chosenContrib}%</span>}
                  </div>
                  <div style={{ height: '8px', background: 'rgba(255,255,255,0.08)', borderRadius: '4px', overflow: 'hidden', display: 'flex' }}>
                    <div style={{ width: `${progress}%`, background: '#3B82F6', transition: 'width 0.3s ease' }} />
                    <div style={{ width: `${chosenContrib}%`, background: '#22C55E', transition: 'width 0.3s ease' }} />
                  </div>
                </div>

                {isAlreadyFunded ? (
                  <div style={{ padding: '8px 12px', background: 'rgba(34,197,94,0.12)', border: '1px solid rgba(34,197,94,0.3)', borderRadius: '8px', fontSize: '12px', fontWeight: 700, color: '#4ADE80', textAlign: 'center' }}>
                    ✅ Funding submitted this turn
                  </div>
                ) : (
                  <div>
                    {/* Funding % selector */}
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
                      <span style={{ fontSize: '11px', fontWeight: 700, color: '#93C5FD' }}>Add Funding %:</span>
                      <select value={chosenContrib} disabled={partyBuildingConfirmed}
                        onChange={e => { setFundingContributions(prev => ({ ...prev, [projId]: parseInt(e.target.value) })); setPartyBuildingConfirmed(false); }}
                        style={{ padding: '4px 8px', fontSize: '12px', borderRadius: '6px', background: 'rgba(255,255,255,0.08)', color: '#E6EDF3', border: '1px solid rgba(255,255,255,0.18)', minHeight: 'unset' }}>
                        {presets.map(val => <option key={val} value={val}>+{val}%</option>)}
                      </select>
                      {chosenContrib > 0 && (
                        <span style={{ fontSize: '11px', color: canAfford ? '#D1D5DB' : '#F87171', fontWeight: 700 }}>
                          {costForContrib.coins} 💰{costForContrib.morale > 0 ? `, ${costForContrib.morale} Morale` : ''}{!canAfford ? ' ⚠️' : ''}
                        </span>
                      )}
                    </div>
                    <div style={{ display: 'flex', gap: '8px' }}>
                      {chosenContrib > 0 && canAfford && (
                        <button onClick={() => handleFundProject(projId, chosenContrib)} disabled={partyBuildingConfirmed || capReached}
                          style={{ padding: '6px 14px', fontSize: '12px', fontWeight: 800, background: (partyBuildingConfirmed || capReached) ? 'rgba(255,255,255,0.08)' : '#22C55E', color: '#ffffff', border: 'none', borderRadius: '8px', cursor: (partyBuildingConfirmed || capReached) ? 'not-allowed' : 'pointer', minHeight: 'unset', fontFamily: 'Montserrat,sans-serif' }}>
                          🏗️ Confirm Funding
                        </button>
                      )}
                      {progress > 0 && (
                        <button onClick={() => setDestroyConfirm({ projectKey: projId, refundCoins: Math.ceil((pDef.costCoins || 0) * progress / 100), name: pDef.name || proj.projectKey })}
                          disabled={partyBuildingConfirmed}
                          style={{ padding: '6px 12px', fontSize: '11px', fontWeight: 800, background: 'rgba(220,38,38,0.15)', color: '#F87171', border: '1px solid rgba(220,38,38,0.35)', borderRadius: '8px', cursor: partyBuildingConfirmed ? 'not-allowed' : 'pointer', minHeight: 'unset', fontFamily: 'Montserrat,sans-serif' }}>
                          🗑️ Scrap ({Math.ceil((pDef.costCoins || 0) * progress / 100)} 💰)
                        </button>
                      )}
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      )}

      {/* ── AVAILABLE PROJECTS — Category filter chips ── */}
      <div style={{ fontSize: '11px', fontWeight: 800, letterSpacing: '0.07em', textTransform: 'uppercase', color: '#7D8590', marginBottom: '10px' }}>
        🧱 Build Infrastructure
      </div>

      {/* Category filter chips */}
      <div className="wr-hscroll" style={{ marginBottom: '14px', paddingBottom: '4px' }}>
        {CATEGORY_CONFIG.map(cat => {
          const isActive = projectCategoryFilter === cat.key;
          return (
            <button key={cat.key} onClick={() => !partyBuildingConfirmed && setProjectCategoryFilter(cat.key)}
              disabled={partyBuildingConfirmed}
              className="wr-chip"
              style={{
                background: isActive ? cat.color : 'rgba(255,255,255,0.05)',
                borderColor: isActive ? cat.color : 'rgba(255,255,255,0.12)',
                color: isActive ? '#ffffff' : '#8B949E',
                boxShadow: isActive ? `0 0 10px ${cat.color}80` : 'none',
                transform: isActive ? 'scale(1.05)' : 'scale(1)',
                fontFamily: 'Montserrat,system-ui,sans-serif',
              }}>
              {cat.icon} {cat.label}
            </button>
          );
        })}
      </div>

      {/* Available project CARDS — portrait style matching Action 1 */}
      {filteredAvail.length === 0 ? (
        <div style={{ textAlign: 'center', padding: '24px 0', color: '#7D8590', fontSize: '13px', fontStyle: 'italic' }}>
          No projects available in this category.
        </div>
      ) : (
        <div className="wr-hscroll" style={{ paddingBottom: '14px', paddingTop: '6px', paddingLeft: '2px', paddingRight: '16px', gap: '12px', alignItems: 'flex-start' }}>
          {filteredAvail.map(avail => {
            const chosenContrib = fundingContributions[avail.key] || 0;
            const costForContrib = getProgressCost(avail, chosenContrib);
            const canAfford = canAffordCost(costForContrib, activeParty.stats);
            const isSelected = chosenContrib > 0;
            const cardBg = getCategoryGrad(avail.offensive);

            return (
              <div key={avail.key} style={{
                width: '155px',
                flexShrink: 0,
                borderRadius: '14px',
                background: cardBg,
                border: `2px solid ${isSelected ? '#F59E0B' : 'rgba(255,255,255,0.10)'}`,
                boxShadow: isSelected
                  ? '0 0 20px rgba(245,158,11,0.5), 0 8px 30px rgba(0,0,0,0.5)'
                  : '0 4px 16px rgba(0,0,0,0.4)',
                transform: isSelected ? 'scale(1.04) translateY(-4px)' : 'scale(1)',
                transition: 'all 0.2s ease',
                display: 'flex', flexDirection: 'column',
                padding: '12px 11px 11px',
                overflow: 'hidden', position: 'relative',
                cursor: partyBuildingConfirmed ? 'not-allowed' : 'default',
                scrollSnapAlign: 'center',
              }}>
                {/* Remaining builds badge */}
                {avail.remainingBuilds === 2 && (
                  <div style={{
                    position: 'absolute', top: '8px', right: '8px',
                    width: '18px', height: '18px', borderRadius: '50%',
                    background: 'rgba(255,255,255,0.25)',
                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                    fontSize: '10px', fontWeight: 900, color: '#ffffff',
                    border: '1px solid rgba(255,255,255,0.4)',
                  }}>2</div>
                )}

                {/* Project name */}
                <div style={{ fontSize: '13px', fontWeight: 900, color: '#ffffff', lineHeight: 1.3, flex: 1, marginBottom: '6px', paddingRight: '20px' }}>
                  {avail.name}
                </div>

                {/* Cost */}
                <div style={{ fontSize: '11px', fontWeight: 700, color: 'rgba(255,255,255,0.75)', marginBottom: '4px' }}>
                  {avail.cost}
                </div>

                {/* Yield */}
                <div style={{ fontSize: '10px', color: 'rgba(255,255,255,0.6)', marginBottom: '10px', lineHeight: 1.4 }}>
                  {avail.yield}
                </div>

                {/* Divider */}
                <div style={{ height: '1px', background: 'rgba(255,255,255,0.15)', marginBottom: '8px' }} />

                {/* Funding % selector */}
                <div style={{ fontSize: '10px', fontWeight: 700, color: 'rgba(255,255,255,0.7)', marginBottom: '4px', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                  Fund %
                </div>
                <select
                  value={chosenContrib}
                  disabled={partyBuildingConfirmed || capReached}
                  onChange={e => { setFundingContributions(prev => ({ ...prev, [avail.key]: parseInt(e.target.value) })); setPartyBuildingConfirmed(false); }}
                  style={{
                    width: '100%', padding: '5px 6px', fontSize: '12px', fontWeight: 800,
                    borderRadius: '6px',
                    background: 'rgba(0,0,0,0.35)',
                    color: '#E6EDF3',
                    border: `1.5px solid ${isSelected ? '#F59E0B' : 'rgba(255,255,255,0.2)'}`,
                    marginBottom: '8px', minHeight: 'unset',
                    fontFamily: 'Montserrat,sans-serif',
                    cursor: (partyBuildingConfirmed || capReached) ? 'not-allowed' : 'pointer',
                  }}
                >
                  <option value={0}>-- Select --</option>
                  {PRESETS.map(val => <option key={val} value={val}>{val}%</option>)}
                </select>

                {/* Cost display */}
                {chosenContrib > 0 && (
                  <div style={{ fontSize: '10px', fontWeight: 700, color: canAfford ? 'rgba(255,255,255,0.8)' : '#F87171', marginBottom: '8px' }}>
                    Cost: {costForContrib.coins} 💰
                    {costForContrib.morale > 0 && `, ${costForContrib.morale} Morale`}
                    {!canAfford && ' ⚠️'}
                  </div>
                )}

                {/* Confirm funding button */}
                <button
                  disabled={partyBuildingConfirmed || capReached || chosenContrib === 0 || !canAfford}
                  onClick={() => handleFundProject(avail.key, chosenContrib)}
                  style={{
                    width: '100%', padding: '7px 6px', fontSize: '11px', fontWeight: 900,
                    background: (partyBuildingConfirmed || capReached || chosenContrib === 0 || !canAfford)
                      ? 'rgba(255,255,255,0.12)'
                      : '#22C55E',
                    color: '#ffffff', border: 'none', borderRadius: '8px', cursor:
                      (partyBuildingConfirmed || capReached || chosenContrib === 0 || !canAfford)
                        ? 'not-allowed' : 'pointer',
                    minHeight: 'unset', fontFamily: 'Montserrat,sans-serif',
                    transition: 'background 0.15s ease',
                  }}
                >
                  🏗️ Fund
                </button>
              </div>
            );
          })}
        </div>
      )}

      {/* Confirm projects lock */}
      <div style={{ paddingTop: '14px', borderTop: '1px solid rgba(255,255,255,0.06)', marginBottom: '4px' }}>
        <button onClick={() => setPartyBuildingConfirmed(!partyBuildingConfirmed)}
          style={{
            width: '100%', minHeight: '50px', fontSize: '14px', fontWeight: 900,
            background: partyBuildingConfirmed ? 'linear-gradient(135deg,#16A34A,#15803d)' : 'rgba(255,255,255,0.06)',
            color: partyBuildingConfirmed ? '#ffffff' : '#8B949E',
            border: partyBuildingConfirmed ? 'none' : '1px solid rgba(255,255,255,0.12)',
            borderRadius: '12px', cursor: 'pointer',
            boxShadow: partyBuildingConfirmed ? '0 0 16px rgba(22,163,74,0.4)' : 'none',
            transition: 'all 0.2s ease', touchAction: 'manipulation',
            fontFamily: 'Montserrat,system-ui,sans-serif',
          }}>
          {partyBuildingConfirmed ? '✅ Projects Locked' : '🔒 Confirm Projects Choice'}
        </button>
      </div>

      {/* Destroy confirm modal */}
      {destroyConfirm && (
        <div style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, background: 'rgba(0,0,0,0.75)', zIndex: 2000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px' }}>
          <div style={{ background: '#1C2128', border: '1px solid rgba(255,255,255,0.15)', borderRadius: '16px', padding: '24px', maxWidth: '340px', width: '100%', textAlign: 'center' }}>
            <div style={{ fontSize: '28px', marginBottom: '12px' }}>🗑️</div>
            <div style={{ fontSize: '17px', fontWeight: 900, color: '#F87171', marginBottom: '8px' }}>Destroy Project?</div>
            <p style={{ fontSize: '13px', color: '#C9D1D9', lineHeight: 1.6, marginBottom: '20px' }}>
              Destroy <strong style={{ color: '#E6EDF3' }}>{destroyConfirm.name}</strong>?<br />
              You'll receive a refund of <strong style={{ color: '#FCD34D' }}>{destroyConfirm.refundCoins} Coins</strong>.
            </p>
            <div style={{ display: 'flex', gap: '10px' }}>
              <button onClick={() => { handleDestroyProject(destroyConfirm.projectKey); setDestroyConfirm(null); }}
                style={{ flex: 1, padding: '12px', fontWeight: 900, fontSize: '14px', background: '#DC2626', color: '#fff', border: 'none', borderRadius: '10px', cursor: 'pointer', fontFamily: 'Montserrat,sans-serif' }}>
                Yes, Destroy
              </button>
              <button onClick={() => setDestroyConfirm(null)}
                style={{ flex: 1, padding: '12px', fontWeight: 700, fontSize: '14px', background: 'rgba(255,255,255,0.06)', color: '#E6EDF3', border: '1px solid rgba(255,255,255,0.15)', borderRadius: '10px', cursor: 'pointer', fontFamily: 'Montserrat,sans-serif' }}>
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
