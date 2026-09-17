import React, { useState } from 'react';
import { getProgressCost, canAffordCost, getPartyColor } from './gameUtils';
import { getSymbolIconComponent } from '../../constants/partyThemes';

export default function Action6PartyBuilding({
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
  fundedThisTurn = []
}) {
  const [destroyingProject, setDestroyingProject] = useState(null); // { projectKey, refundCoins, name, isInProgress }

  if (!activeParty) return null;

  const activeProjects = activeParty.projects || [];
  const completedProjects = activeProjects
    .filter(p => p.progressPercent >= 100)
    .sort((a, b) => (a.completionTurn || 0) - (b.completionTurn || 0));
  
  const selectedProjects = activeProjects.filter(p => 
    p.progressPercent < 100 && 
    p.progressPercent > 0
  );
  
  const capReached = fundedThisTurn.length >= 3;
  
  const availableProjects = Object.entries(PROJECT_DEFS).map(([key, def]) => {
    const existing = activeProjects.find(p => p.projectKey === key && p.progressPercent < 100);
    const buildsThisCycle = activeParty.projectBuildsThisCycle || {};
    const limit = (def.costCoins || 0) > 100 ? 1 : 2;
    const builds = buildsThisCycle[key] || 0;
    const remaining = Math.max(0, limit - builds);
    return {
      key,
      ...def,
      progress: existing ? existing.progressPercent : 0,
      id: existing ? existing.id : null,
      remainingBuilds: remaining
    };
  }).filter(p => p.progress === 0 && !fundedThisTurn.includes(p.key) && p.remainingBuilds > 0);

  const filteredAvail = availableProjects.filter(p => {
    if (projectCategoryFilter === 'BUILD') return !p.offensive;
    return p.offensive;
  });

  const SymbolIcon = getSymbolIconComponent(activeParty.symbol || 'Flag');

  return (
    <div>
      <style>{`
        @keyframes borderFlashRed {
          0% { border-color: #ef4444; box-shadow: 0 0 4px rgba(239, 68, 68, 0.3); }
          50% { border-color: #f43f5e; box-shadow: 0 0 12px rgba(244, 63, 94, 0.6); }
          100% { border-color: #ef4444; box-shadow: 0 0 4px rgba(239, 68, 68, 0.3); }
        }
        @keyframes textBlink {
          0% { opacity: 0.45; }
          50% { opacity: 1; }
          100% { opacity: 0.45; }
        }
      `}</style>

      <div style={{ 
        display: 'flex', 
        justifyContent: 'space-between', 
        alignItems: 'center', 
        background: 'rgba(59, 130, 246, 0.04)', 
        border: '1.5px solid rgba(59, 130, 246, 0.15)',
        padding: '8px 12px', 
        borderRadius: '8px', 
        fontSize: '12px', 
        color: '#1e40af', 
        marginBottom: '15px',
        fontWeight: '500'
      }}>
        <span>📅 Project Limit Cycle: <b>20 turns</b></span>
        <span>🔄 Limits refresh in: <b style={{ color: '#b45309' }}>{activeParty.turnsUntilProjectLimitRefresh} turns</b></span>
      </div>

      {turnData.turnNumber <= 2 && (
        <p style={{ margin: '0 0 15px 0', fontSize: '13px', color: 'var(--card-text)' }}>
          Fund long-term construction projects for passive campaign yields or offensive targets.
        </p>
      )}

      {capReached && (
        <div style={{ padding: '8px 12px', background: '#fef3c7', border: '1px solid #f59e0b', borderRadius: '8px', color: '#b45309', fontSize: '12px', fontWeight: 'bold', marginBottom: '15px' }}>
          ⚠️ Daily funding limit reached: You can contribute to at most 3 projects in a single turn.
        </div>
      )}

      {/* Completed Projects */}
      {completedProjects.length > 0 && (
        <div style={{ marginBottom: '20px' }}>
          <h5 style={{ margin: '0 0 10px 0', fontSize: '13px', color: 'var(--primary-dark)', borderBottom: '1px solid rgba(0,0,0,0.05)', paddingBottom: '4px' }}>Completed Infrastructure</h5>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '12px' }}>
            {completedProjects.map((proj, idx) => {
              const pDef = PROJECT_DEFS[proj.projectKey] || {};
              const projId = proj.id || proj.projectKey;
              const needsTargetWarning = pDef.offensive && (!proj.targetPartyId || proj.targetPartyId === '');

              return (
                <div 
                  key={proj.id || `${proj.projectKey}-completed-${idx}`} 
                  className="themed-action-card"
                  style={{ 
                    border: needsTargetWarning ? '2.5px solid #ef4444' : '2.5px solid #22c55e', 
                    borderRadius: '8px', 
                    padding: '12px', 
                    background: needsTargetWarning ? 'rgba(239, 68, 68, 0.04)' : 'rgba(34,197,94,0.04)',
                    position: 'relative',
                    overflow: 'hidden',
                    animation: needsTargetWarning ? 'borderFlashRed 1.5s infinite ease-in-out' : 'none'
                  }}
                >
                  {/* Faint Background Watermark */}
                  <div className="themed-card-watermark">
                    <SymbolIcon size={64} color={needsTargetWarning ? "#ef4444" : "#22c55e"} />
                  </div>

                  {/* Bottom Right Corner Ribbon */}
                  <div className="themed-card-ribbon" style={{ background: needsTargetWarning ? "#ef4444" : "#22c55e" }}>
                    <SymbolIcon size={10} color="#ffffff" style={{ marginRight: '1px', marginBottom: '1px', filter: 'brightness(0) invert(1)' }} />
                  </div>

                  <div style={{ position: 'relative', zIndex: 2 }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <div style={{ fontWeight: 'bold', fontSize: '13px', color: needsTargetWarning ? '#991b1b' : '#1b5e20' }}>{pDef.name || proj.projectKey}</div>
                      {needsTargetWarning && (
                        <span style={{ 
                          fontSize: '9px', 
                          background: '#ef4444', 
                          color: '#ffffff', 
                          padding: '2px 6px', 
                          borderRadius: '4px', 
                          fontWeight: '900', 
                          whiteSpace: 'nowrap',
                          animation: 'textBlink 1.2s infinite ease-in-out',
                          boxShadow: '0 2px 5px rgba(239,68,68,0.2)'
                        }}>
                          ⚠️ ASSIGN TARGET!
                        </span>
                      )}
                    </div>

                    {pDef.offensive ? (
                      <div style={{ marginTop: '8px' }}>
                        <label style={{ fontSize: '11px', fontWeight: 'bold', display: 'block', marginBottom: '4px', color: '#0f172a' }}>🎯 Target Opponent:</label>
                        <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap' }}>
                          {turnData.parties.filter(opp => opp.id !== turnData.activeHumanPartyId).map(opp => {
                            const isSelected = proj.targetPartyId === opp.id;
                            return (
                              <button
                                key={opp.id}
                                type="button"
                                disabled={partyBuildingConfirmed}
                                onClick={() => {
                                  handleSetProjectTarget(projId, opp.id);
                                  setPartyBuildingConfirmed(false);
                                }}
                                style={{
                                  padding: '4px 8px',
                                  fontSize: '11.5px',
                                  fontWeight: 'bold',
                                  borderRadius: '6px',
                                  border: isSelected ? `2px solid ${opp.color || '#1d4ed8'}` : needsTargetWarning ? '1.5px solid #ef4444' : '1px solid var(--primary-border)',
                                  background: isSelected ? `${opp.color || '#1d4ed8'}18` : '#ffffff',
                                  color: isSelected ? opp.color || '#1d4ed8' : '#334155',
                                  cursor: partyBuildingConfirmed ? 'not-allowed' : 'pointer'
                                }}
                              >
                                {opp.symbol || '🏛️'} {opp.name} {isSelected ? '✓' : ''}
                              </button>
                            );
                          })}
                        </div>
                      </div>
                    ) : (
                      <span style={{ fontSize: '10px', color: '#22c55e', fontWeight: 'bold', marginTop: '6px', display: 'inline-block' }}>🛡️ Passive yield active</span>
                    )}
                    <div style={{ marginTop: '10px', borderTop: '1px solid rgba(34,197,94,0.15)', paddingTop: '6px' }}>
                      <button
                        disabled={partyBuildingConfirmed}
                        onClick={() => {
                          const refundCoins = pDef.costCoins || 0;
                          setDestroyingProject({
                            projectKey: projId,
                            refundCoins,
                            name: pDef.name || proj.projectKey,
                            isInProgress: false
                          });
                        }}
                        style={{
                          padding: '4px 8px',
                          fontSize: '11px',
                          background: '#ef4444',
                          color: '#ffffff',
                          border: 'none',
                          fontWeight: 'bold',
                          cursor: partyBuildingConfirmed ? 'not-allowed' : 'pointer',
                          borderRadius: '4px',
                          boxShadow: '0 2px 4px rgba(239, 68, 68, 0.2)'
                        }}
                      >
                        🗑️ Destroy &amp; Refund ({pDef.costCoins || 0} 💰)
                      </button>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* Selected Projects */}
      {selectedProjects.length > 0 && (
        <div style={{ marginBottom: '20px' }}>
          <h5 style={{ margin: '0 0 10px 0', fontSize: '13px', color: 'var(--primary-dark)', borderBottom: '1px solid rgba(0,0,0,0.05)', paddingBottom: '4px' }}>Projects in Progress</h5>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
            {selectedProjects.map((proj, idx) => {
              const pDef = PROJECT_DEFS[proj.projectKey] || {};
              const projId = proj.id || proj.projectKey;
              const progress = proj.progressPercent || 0;
              const remaining = 100 - progress;

              const presets = [0];
              for (const val of [20, 40, 60, 80, 100]) {
                if (val <= remaining) presets.push(val);
              }
              if (remaining > 0 && !presets.includes(remaining)) presets.push(remaining);
              presets.sort((a, b) => a - b);

              const chosenContrib = fundingContributions[proj.id] || fundingContributions[proj.projectKey] || 0;
              const costForContrib = getProgressCost(pDef, chosenContrib);
              const canAfford = canAffordCost(costForContrib, activeParty.stats);

                const blueprintBg = 'linear-gradient(135deg, #1e3a8a 0%, #172554 100%)';
                const blueprintGrid = 'repeating-linear-gradient(0deg, rgba(255,255,255,0.07), rgba(255,255,255,0.07) 1px, transparent 1px, transparent 12px), repeating-linear-gradient(90deg, rgba(255,255,255,0.07), rgba(255,255,255,0.07) 1px, transparent 1px, transparent 12px)';

                return (
                  <div 
                    key={proj.id || `${proj.projectKey}-in-progress-${idx}`} 
                    className="themed-action-card"
                    style={{ 
                      border: '2px dashed #60a5fa', 
                      borderRadius: '12px', 
                      padding: '15px', 
                      backgroundImage: `${blueprintGrid}, ${blueprintBg}`,
                      position: 'relative',
                      overflow: 'hidden',
                      color: '#ffffff',
                      boxShadow: '0 6px 20px rgba(30, 58, 138, 0.2)'
                    }}
                  >
                    {/* Faint Background Watermark */}
                    <div className="themed-card-watermark">
                      <SymbolIcon size={64} color="rgba(96, 165, 250, 0.15)" />
                    </div>

                    {/* Bottom Right Corner Ribbon */}
                    <div className="themed-card-ribbon" style={{ background: '#3b82f6' }}>
                      <SymbolIcon size={10} color="#ffffff" style={{ marginRight: '1px', marginBottom: '1px', filter: 'brightness(0) invert(1)' }} />
                    </div>

                    <div style={{ position: 'relative', zIndex: 2 }}>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <div style={{ fontWeight: '900', fontSize: '14px', color: '#93c5fd', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                          📐 {pDef.name || proj.projectKey} [UNDER CONSTRUCTION]
                        </div>
                      </div>
                      <div style={{ fontSize: '11px', color: '#cbd5e1', marginTop: '4px' }}>
                        Total Cost: {pDef.cost}
                      </div>
                      
                      <div style={{ marginTop: '12px' }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', marginBottom: '4px', fontWeight: 'bold' }}>
                          <span>Funding Progress: {progress}%</span>
                          {chosenContrib > 0 && <span style={{ color: '#4ade80' }}>+ {chosenContrib}%</span>}
                        </div>
                        <div style={{ width: '100%', height: '8px', background: 'rgba(0,0,0,0.3)', borderRadius: '4px', overflow: 'hidden', display: 'flex', border: '1px solid rgba(255,255,255,0.1)' }}>
                          <div style={{ width: `${progress}%`, background: '#3b82f6' }} />
                          <div style={{ width: `${chosenContrib}%`, background: '#22c55e' }} />
                        </div>
                      </div>

                      {(() => {
                        const isAlreadyFunded = fundedThisTurn.includes(proj.id) || fundedThisTurn.includes(proj.projectKey);
                        if (isAlreadyFunded) {
                          return (
                            <div style={{
                              marginTop: '12px',
                              background: 'rgba(34, 197, 94, 0.15)',
                              border: '1.5px solid #22c55e',
                              color: '#4ade80',
                              padding: '8px 12px',
                              borderRadius: '6px',
                              fontSize: '12px',
                              fontWeight: 'bold',
                              textAlign: 'center'
                            }}>
                              ✅ Construction Funding Submitted (Locked This Turn)
                            </div>
                          );
                        }

                        return (
                          <>
                            <div style={{ marginTop: '12px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
                              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                                <label style={{ fontSize: '11px', fontWeight: 'bold', color: '#93c5fd' }}>Funding %:</label>
                                <div style={{ display: 'flex', gap: '4px' }}>
                                  {presets.map(val => (
                                    <button
                                      key={val}
                                      type="button"
                                      disabled={partyBuildingConfirmed}
                                      onClick={() => {
                                        setFundingContributions(prev => ({ ...prev, [projId]: val }));
                                        setPartyBuildingConfirmed(false);
                                      }}
                                      style={{
                                        padding: '3px 6px',
                                        fontSize: '11px',
                                        fontWeight: 'bold',
                                        borderRadius: '4px',
                                        border: chosenContrib === val ? '1.5px solid #38bdf8' : '1px solid #475569',
                                        background: chosenContrib === val ? '#0284c7' : '#1e293b',
                                        color: '#ffffff',
                                        cursor: partyBuildingConfirmed ? 'not-allowed' : 'pointer'
                                      }}
                                    >
                                      +{val}%
                                    </button>
                                  ))}
                                </div>
                              </div>

                              <div style={{ fontSize: '11px', color: canAfford ? '#cbd5e1' : '#f87171', fontWeight: chosenContrib > 0 ? 'bold' : 'normal' }}>
                                Cost: {costForContrib.coins} Coins
                                {costForContrib.morale > 0 && `, ${costForContrib.morale} Morale`}
                                {costForContrib.corruption > 0 && `, ${costForContrib.corruption} Corruption`}
                                {costForContrib.media > 0 && `, ${costForContrib.media} Media`}
                                {costForContrib.support > 0 && `, ${costForContrib.support}% Support`}
                                {!canAfford && chosenContrib > 0 && " ⚠️ (CANNOT AFFORD)"}
                              </div>
                            </div>

                            <div style={{ marginTop: '12px', display: 'flex', flexWrap: 'wrap', gap: '10px', alignItems: 'center' }}>
                              {chosenContrib > 0 && canAfford && (
                                <button
                                  disabled={partyBuildingConfirmed || capReached}
                                  onClick={() => handleFundProject(projId, chosenContrib)}
                                  style={{
                                    padding: '6px 15px',
                                    fontSize: '11px',
                                    background: capReached ? 'gray' : '#22c55e',
                                    color: '#ffffff',
                                    border: 'none',
                                    fontWeight: 'bold',
                                    cursor: capReached ? 'not-allowed' : 'pointer',
                                    borderRadius: '4px',
                                    boxShadow: '0 4px 10px rgba(34,197,94,0.3)'
                                  }}
                                >
                                  🏗️ Confirm Funding
                                </button>
                              )}

                              {progress > 0 && (
                                <button
                                  disabled={partyBuildingConfirmed}
                                  onClick={() => {
                                    const refundCoins = Math.ceil((pDef.costCoins || 0) * progress / 100.0);
                                    setDestroyingProject({
                                      projectKey: projId,
                                      refundCoins,
                                      name: pDef.name || proj.projectKey,
                                      isInProgress: true
                                    });
                                  }}
                                  style={{
                                    padding: '6px 15px',
                                    fontSize: '11px',
                                    background: '#ef4444',
                                    color: '#ffffff',
                                    border: 'none',
                                    fontWeight: 'bold',
                                    cursor: 'pointer',
                                    borderRadius: '4px',
                                    boxShadow: '0 2px 4px rgba(239, 68, 68, 0.2)'
                                  }}
                                >
                                  🗑️ Scrap &amp; Refund ({Math.ceil((pDef.costCoins || 0) * progress / 100.0)} 💰)
                                </button>
                              )}
                            </div>
                          </>
                        );
                      })()}
                    </div>
                  </div>
                );
            })}
          </div>
        </div>
      )}

      {/* Available Projects */}
      <div>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px', borderBottom: '1px solid rgba(0,0,0,0.05)', paddingBottom: '4px' }}>
          <h5 style={{ margin: 0, fontSize: '13px', color: 'var(--primary-dark)' }}>Build Infrastructure</h5>
          <div style={{ display: 'flex', gap: '6px' }}>
            {[
              { key: 'BUILD', label: 'Build Party 🛡️' },
              { key: 'OFFENSIVE', label: 'Target Opponents 💥' }
            ].map(tab => {
              const isActive = projectCategoryFilter === tab.key;
              return (
                <button
                  key={tab.key}
                  disabled={partyBuildingConfirmed}
                  onClick={() => setProjectCategoryFilter(tab.key)}
                  style={{
                    padding: '4px 12px',
                    fontSize: '11px',
                    background: isActive ? 'var(--party-primary-color, var(--primary-dark))' : '#ffffff',
                    color: isActive ? '#ffffff' : 'var(--party-primary-color, var(--primary-dark))',
                    border: isActive ? '1.5px solid var(--party-primary-color, var(--primary-dark))' : '1px solid rgba(var(--party-primary-color-rgb, 101, 148, 177), 0.3)',
                    borderRadius: '20px',
                    fontWeight: 'bold',
                    cursor: partyBuildingConfirmed ? 'not-allowed' : 'pointer',
                    transition: 'all 0.2s ease',
                    opacity: partyBuildingConfirmed ? 0.6 : 1
                  }}
                >
                  {tab.label}
                </button>
              );
            })}
          </div>
        </div>

        {filteredAvail.length === 0 ? (
          <p style={{ margin: 0, fontSize: '11px', color: 'gray', fontStyle: 'italic' }}>No projects available in this category.</p>
        ) : (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '10px' }}>
            {filteredAvail.map(avail => {
              const presets = [20, 40, 60, 80, 100];
              const chosenContrib = fundingContributions[avail.key] || 0;
              const costForContrib = getProgressCost(avail, chosenContrib);
              const canAfford = canAffordCost(costForContrib, activeParty.stats);

              return (
                <div 
                  key={avail.key} 
                  className="themed-action-card"
                  style={{ 
                    border: '2.5px dashed #94a3b8', 
                    borderRadius: '8px', 
                    padding: '10px', 
                    background: 'rgba(148, 163, 184, 0.04)', 
                    display: 'flex', 
                    flexDirection: 'column', 
                    justifyContent: 'space-between',
                    position: 'relative',
                    overflow: 'hidden'
                  }}
                >
                  {avail.remainingBuilds === 2 && (
                    <div style={{
                      position: 'absolute',
                      top: '8px',
                      right: '8px',
                      background: 'var(--party-primary-color, #3b82f6)',
                      color: '#ffffff',
                      borderRadius: '50%',
                      width: '20px',
                      height: '20px',
                      fontSize: '11px',
                      fontWeight: 'bold',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      boxShadow: '0 2px 4px rgba(0,0,0,0.15)',
                      zIndex: 10
                    }} title="2 builds available in this cycle">
                      2
                    </div>
                  )}

                  {/* Faint Background Watermark */}
                  <div className="themed-card-watermark">
                    <SymbolIcon size={64} color="#cbd5e1" />
                  </div>

                  {/* Bottom Right Corner Ribbon */}
                  <div className="themed-card-ribbon">
                    <SymbolIcon size={10} color="#ffffff" style={{ marginRight: '1px', marginBottom: '1px', filter: 'brightness(0) invert(1)' }} />
                  </div>

                  <div style={{ position: 'relative', zIndex: 2, display: 'flex', flexDirection: 'column', height: '100%', justifyContent: 'space-between' }}>
                    <div>
                      <div style={{ fontWeight: 'bold', fontSize: '12px', color: '#475569' }}>{avail.name}</div>
                      <div style={{ fontSize: '10px', color: 'gray', marginTop: '2px' }}>Total Cost: {avail.cost}</div>
                      <div style={{ fontSize: '10px', color: 'var(--card-text)', marginTop: '4px' }}>Yield: {avail.yield}</div>
                      
                      <div style={{ marginTop: '12px' }}>
                        <label style={{ fontSize: '11px', fontWeight: 'bold', display: 'block', marginBottom: '4px', color: 'var(--primary-dark)' }}>Start Funding %:</label>
                        <div style={{ display: 'flex', gap: '4px', marginTop: '4px' }}>
                          {presets.map(val => (
                            <button
                              key={val}
                              type="button"
                              disabled={partyBuildingConfirmed}
                              onClick={() => {
                                setFundingContributions(prev => ({ ...prev, [avail.key]: val }));
                                setPartyBuildingConfirmed(false);
                              }}
                              style={{
                                flex: 1,
                                padding: '4px 0',
                                fontSize: '11px',
                                fontWeight: 'bold',
                                borderRadius: '4px',
                                border: chosenContrib === val ? '1.5px solid var(--primary-dark)' : '1px solid var(--primary-border)',
                                background: chosenContrib === val ? 'var(--primary-dark)' : '#ffffff',
                                color: chosenContrib === val ? '#ffffff' : '#334155',
                                cursor: partyBuildingConfirmed ? 'not-allowed' : 'pointer'
                              }}
                            >
                              +{val}%
                            </button>
                          ))}
                        </div>
                      </div>

                      {chosenContrib > 0 && (
                        <div style={{ fontSize: '10px', marginTop: '6px', color: canAfford ? 'var(--card-text)' : '#d23f31', fontWeight: 'bold' }}>
                          Cost: {costForContrib.coins} Coins
                          {costForContrib.morale > 0 && `, ${costForContrib.morale} Morale`}
                          {costForContrib.corruption > 0 && `, ${costForContrib.corruption} Corruption`}
                          {costForContrib.media > 0 && `, ${costForContrib.media} Media`}
                          {costForContrib.support > 0 && `, ${costForContrib.support}% Support`}
                          {!canAfford && " ⚠️ (CANNOT AFFORD)"}
                        </div>
                      )}
                    </div>
                    
                    <button
                      disabled={partyBuildingConfirmed || capReached || chosenContrib === 0 || !canAfford}
                      onClick={() => handleFundProject(avail.key, chosenContrib)}
                      style={{ 
                        padding: '6px 12px', 
                        fontSize: '11px', 
                        marginTop: '12px', 
                        alignSelf: 'flex-start',
                        cursor: (partyBuildingConfirmed || capReached || chosenContrib === 0 || !canAfford) ? 'not-allowed' : 'pointer',
                        background: (partyBuildingConfirmed || capReached || chosenContrib === 0 || !canAfford) ? 'gray' : 'var(--party-primary-color)',
                        borderColor: (partyBuildingConfirmed || capReached || chosenContrib === 0 || !canAfford) ? 'gray' : 'var(--party-primary-color)',
                        color: '#ffffff',
                        fontWeight: 'bold',
                        borderRadius: '4px'
                      }}
                    >
                      🏗️ Confirm Funding
                    </button>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>

      <div style={{ marginTop: '20px', textAlign: 'center', borderTop: '1px solid rgba(101, 148, 177, 0.2)', paddingTop: '15px' }}>
        <button
          onClick={() => setPartyBuildingConfirmed(!partyBuildingConfirmed)}
          className={(fundedThisTurn.length > 0 && !partyBuildingConfirmed) ? 'btn-pulse-highlight' : ''}
          style={{
            background: partyBuildingConfirmed
              ? 'var(--selected-highlight, #22c55e)'
              : (fundedThisTurn.length > 0)
              ? '#0ea5e9'
              : 'var(--party-primary-color, var(--primary-dark))',
            borderColor: partyBuildingConfirmed
              ? 'var(--selected-highlight, #22c55e)'
              : (fundedThisTurn.length > 0)
              ? '#38bdf8'
              : 'var(--party-primary-color, var(--primary-dark))',
            color: partyBuildingConfirmed ? 'var(--primary-dark)' : '#ffffff',
            fontWeight: 'bold',
            padding: '10px 25px',
            borderRadius: '8px',
            fontSize: '14px',
            cursor: 'pointer'
          }}
        >
          {partyBuildingConfirmed ? '✅ Projects Choice Locked' : '🔒 Confirm Projects Choice'}
        </button>
      </div>

      {/* Custom Confirmation Modal for Destroying/Scrapping Project */}
      {destroyingProject && (
        <div
          className="modal-overlay"
          style={{ zIndex: 2000, backgroundColor: 'rgba(0,0,0,0.6)' }}
        >
          <div className="modal-card" style={{ background: 'var(--primary-dark)', border: '2px solid var(--primary-border)', maxWidth: '380px' }}>
            <div className="modal-header" style={{ padding: '20px 20px 0 20px', textAlign: 'center', position: 'relative' }}>
              <h2 style={{ margin: '0 0 12px 0', color: 'var(--party-primary-color, #ef4444)', fontSize: '18px', fontWeight: 800 }}>
                {destroyingProject.isInProgress ? '🗑️ Scrap Project?' : '🗑️ Destroy Project?'}
              </h2>
              <button
                className="modal-close-btn"
                onClick={() => setDestroyingProject(null)}
                style={{ position: 'absolute', top: '12px', right: '12px', background: 'rgba(255,255,255,0.15)', border: 'none', color: '#fff', borderRadius: '50%', width: '32px', height: '32px', fontSize: '15px', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center' }}
                aria-label="Close"
              >✕</button>
            </div>
            <div className="modal-body" style={{ padding: '0 20px 20px 20px', textAlign: 'center' }}>
              <p style={{ fontSize: '13px', color: 'var(--card-text, #ffffff)', marginBottom: '20px', lineHeight: 1.5, opacity: 0.95 }}>
                Are you sure you want to {destroyingProject.isInProgress ? 'scrap' : 'destroy'} project <b>{destroyingProject.name}</b>?
                You will receive a refund of <b>{destroyingProject.refundCoins} Coins</b>.
              </p>
              <div style={{ display: 'flex', gap: '12px', justifyContent: 'center' }}>
                <button
                  onClick={() => { handleDestroyProject(destroyingProject.projectKey); setDestroyingProject(null); }}
                  style={{ flex: 1, padding: '11px', fontSize: '13px', fontWeight: 'bold', backgroundColor: '#D9534F', color: '#fff', border: 'none', borderRadius: '8px', cursor: 'pointer' }}
                >
                  Yes, Confirm
                </button>
                <button
                  onClick={() => setDestroyingProject(null)}
                  style={{ flex: 1, padding: '11px', fontSize: '13px', fontWeight: 'bold', backgroundColor: 'transparent', color: 'var(--card-text, #fff)', border: '1px solid var(--primary-border)', borderRadius: '8px', cursor: 'pointer' }}
                >
                  Cancel
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
