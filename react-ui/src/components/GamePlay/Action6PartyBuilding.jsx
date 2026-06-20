import React from 'react';
import { PROJECT_DEFS } from './constants';
import { getProgressCost, canAffordCost, getPartyColor } from './gameUtils';

export default function Action6PartyBuilding({
  turnData,
  activeParty,
  projectCategoryFilter,
  setProjectCategoryFilter,
  draftProjectKeys,
  setDraftProjectKeys,
  fundingContributions,
  setFundingContributions,
  partyBuildingConfirmed,
  setPartyBuildingConfirmed,
  handleFundProject,
  handleSetProjectTarget
}) {
  if (!activeParty) return null;

  const activeProjects = activeParty.projects || [];
  const completedProjects = activeProjects.filter(p => p.progressPercent >= 100);
  const selectedProjects = activeProjects.filter(p => p.progressPercent < 100 && (p.progressPercent > 0 || draftProjectKeys.includes(p.id) || draftProjectKeys.includes(p.projectKey)));
  
  const availableProjects = Object.entries(PROJECT_DEFS).map(([key, def]) => {
    const existing = activeProjects.find(p => p.projectKey === key && p.progressPercent < 100);
    const isDraft = existing ? draftProjectKeys.includes(existing.id) || draftProjectKeys.includes(existing.projectKey) : false;
    return {
      key,
      ...def,
      progress: existing ? existing.progressPercent : 0,
      isDraft,
      id: existing ? existing.id : null
    };
  }).filter(p => p.progress === 0 && !p.isDraft);

  const filteredAvail = availableProjects.filter(p => {
    if (projectCategoryFilter === 'BUILD') return !p.offensive;
    return p.offensive;
  });

  return (
    <div>
      {turnData.turnNumber <= 2 && (
        <p style={{ margin: '0 0 15px 0', fontSize: '13px', color: 'var(--card-text)' }}>
          Fund long-term construction projects for passive campaign yields or offensive targets.
        </p>
      )}

      {/* Completed Projects */}
      {completedProjects.length > 0 && (
        <div style={{ marginBottom: '20px' }}>
          <h5 style={{ margin: '0 0 10px 0', fontSize: '13px', color: 'var(--primary-dark)', borderBottom: '1px solid rgba(0,0,0,0.05)', paddingBottom: '4px' }}>Completed Infrastructure</h5>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
            {completedProjects.map((proj, idx) => {
              const pDef = PROJECT_DEFS[proj.projectKey] || {};
              const projId = proj.id || proj.projectKey;
              return (
                <div key={proj.id || `${proj.projectKey}-completed-${idx}`} style={{ border: '1px solid #22c55e', borderRadius: '8px', padding: '12px', background: 'rgba(34,197,94,0.02)' }}>
                  <div style={{ fontWeight: 'bold', fontSize: '13px', color: 'var(--primary-dark)' }}>{pDef.name || proj.projectKey}</div>
                  <div style={{ fontSize: '11px', color: 'var(--card-text)', marginTop: '2px' }}>Yield: {pDef.yield}</div>
                  {pDef.offensive ? (
                    <div style={{ marginTop: '8px' }}>
                      <label htmlFor={`target-${projId}`} style={{ fontSize: '11px', fontWeight: 'bold', display: 'block', marginBottom: '4px' }}>🎯 Target:</label>
                      <select 
                        id={`target-${projId}`}
                        value={proj.targetPartyId || ''} 
                        disabled={partyBuildingConfirmed}
                        onChange={(e) => {
                          handleSetProjectTarget(projId, e.target.value);
                          setPartyBuildingConfirmed(false);
                        }}
                        style={{ padding: '4px 8px', fontSize: '12px', borderRadius: '4px', background: '#fff', color: '#000', border: '1px solid var(--primary-border)' }}
                      >
                        <option value="">-- Select Target Opponent --</option>
                        {turnData.parties.filter(opp => opp.id !== turnData.activeHumanPartyId).map(opp => (
                          <option key={opp.id} value={opp.id}>{opp.name}</option>
                        ))}
                      </select>
                    </div>
                  ) : (
                    <span style={{ fontSize: '10px', color: '#22c55e', fontWeight: 'bold', marginTop: '6px', display: 'inline-block' }}>🛡️ Passive yield active</span>
                  )}
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
              const isDraft = draftProjectKeys.includes(proj.id) || draftProjectKeys.includes(proj.projectKey);
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

              return (
                <div key={proj.id || `${proj.projectKey}-in-progress-${idx}`} style={{ border: '1px solid var(--primary-border)', borderRadius: '8px', padding: '12px', background: '#ffffff' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <div style={{ fontWeight: 'bold', fontSize: '13px', color: 'var(--primary-dark)' }}>{pDef.name || proj.projectKey}</div>
                    {isDraft && (
                      <button 
                        disabled={partyBuildingConfirmed}
                        onClick={() => {
                          setDraftProjectKeys(prev => prev.filter(k => k !== proj.id && k !== proj.projectKey));
                          setPartyBuildingConfirmed(false);
                        }}
                        style={{ background: 'transparent', color: '#d23f31', border: 'none', padding: 0, fontSize: '12px', cursor: 'pointer' }}
                      >
                        ❌ Remove
                      </button>
                    )}
                  </div>
                  <div style={{ fontSize: '11px', color: 'var(--card-text)', marginTop: '2px' }}>Total Cost: {pDef.cost} | Yield: {pDef.yield}</div>
                  
                  <div style={{ marginTop: '8px' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', marginBottom: '4px' }}>
                      <span>Funding: <b>{progress}%</b></span>
                      {chosenContrib > 0 && <span style={{ color: '#22c55e', marginLeft: '6px' }}>+ {chosenContrib}%</span>}
                    </div>
                    <div style={{ width: '100%', height: '8px', background: 'rgba(0,0,0,0.1)', borderRadius: '4px', overflow: 'hidden', display: 'flex' }}>
                      <div style={{ width: `${progress}%`, background: 'var(--primary-dark)' }} />
                      <div style={{ width: `${chosenContrib}%`, background: '#22c55e' }} />
                    </div>
                  </div>

                  <div style={{ marginTop: '12px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                      <label htmlFor={`contrib-${projId}`} style={{ fontSize: '11px', fontWeight: 'bold', color: 'var(--primary-dark)' }}>Add Funding %:</label>
                      <select
                        id={`contrib-${projId}`}
                        value={chosenContrib}
                        disabled={partyBuildingConfirmed}
                        onChange={(e) => {
                          const val = parseInt(e.target.value);
                          setFundingContributions(prev => ({ ...prev, [projId]: val }));
                          setPartyBuildingConfirmed(false);
                        }}
                        style={{ padding: '3px', fontSize: '11px', borderRadius: '4px', background: '#fff', color: '#000', border: '1px solid var(--primary-border)' }}
                      >
                        {presets.map(val => (
                          <option key={val} value={val}>+{val}%</option>
                        ))}
                      </select>
                    </div>

                    <div style={{ fontSize: '11px', color: canAfford ? 'var(--card-text)' : '#d23f31', fontWeight: chosenContrib > 0 ? 'bold' : 'normal' }}>
                      Cost: {costForContrib.coins} Coins
                      {costForContrib.morale > 0 && `, ${costForContrib.morale} Morale`}
                      {costForContrib.corruption > 0 && `, ${costForContrib.corruption} Corruption`}
                      {costForContrib.media > 0 && `, ${costForContrib.media} Media`}
                      {costForContrib.support > 0 && `, ${costForContrib.support}% Support`}
                      {!canAfford && chosenContrib > 0 && " ⚠️ (CANNOT AFFORD)"}
                    </div>
                  </div>

                  {chosenContrib > 0 && canAfford && (
                    <div style={{ marginTop: '12px', textAlign: 'right' }}>
                      <button
                        onClick={() => handleFundProject(projId, chosenContrib)}
                        style={{
                          padding: '6px 15px',
                          fontSize: '11px',
                          background: '#22c55e',
                          color: '#ffffff',
                          border: 'none',
                          fontWeight: 'bold',
                          cursor: 'pointer'
                        }}
                      >
                        🏗️ Confirm Funding
                      </button>
                    </div>
                  )}
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
          <select 
            value={projectCategoryFilter}
            disabled={partyBuildingConfirmed}
            onChange={(e) => setProjectCategoryFilter(e.target.value)}
            style={{ padding: '3px', fontSize: '11px', background: '#fff', color: '#000', border: '1px solid var(--primary-border)' }}
          >
            <option value="BUILD">Build Party</option>
            <option value="OFFENSIVE">Target Opponents</option>
          </select>
        </div>

        {filteredAvail.length === 0 ? (
          <p style={{ margin: 0, fontSize: '11px', color: 'gray', fontStyle: 'italic' }}>No projects available in this category.</p>
        ) : (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '10px' }}>
            {filteredAvail.map(avail => (
              <div key={avail.key} style={{ border: '1px dashed var(--primary-border)', borderRadius: '8px', padding: '10px', background: 'rgba(0,0,0,0.01)', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
                <div>
                  <div style={{ fontWeight: 'bold', fontSize: '12px', color: 'var(--primary-dark)' }}>{avail.name}</div>
                  <div style={{ fontSize: '10px', color: 'gray', marginTop: '2px' }}>Cost: {avail.cost}</div>
                  <div style={{ fontSize: '10px', color: 'var(--card-text)', marginTop: '4px' }}>Yield: {avail.yield}</div>
                </div>
                <button
                  disabled={partyBuildingConfirmed}
                  onClick={() => {
                    setDraftProjectKeys(prev => [...prev, avail.key]);
                    setPartyBuildingConfirmed(false);
                  }}
                  style={{ padding: '4px', fontSize: '10px', marginTop: '8px', width: '100%', cursor: 'pointer' }}
                >
                  Select Project
                </button>
              </div>
            ))}
          </div>
        )}
      </div>

      <div style={{ marginTop: '20px', textAlign: 'center', borderTop: '1px solid rgba(101, 148, 177, 0.2)', paddingTop: '15px' }}>
        <button
          onClick={() => setPartyBuildingConfirmed(!partyBuildingConfirmed)}
          style={{
            background: partyBuildingConfirmed ? 'var(--selected-highlight)' : 'var(--primary-dark)',
            borderColor: partyBuildingConfirmed ? 'var(--selected-highlight)' : 'var(--primary-dark)',
            color: partyBuildingConfirmed ? 'var(--primary-dark)' : '#ffffff',
            fontWeight: 'bold',
            padding: '8px 25px'
          }}
        >
          {partyBuildingConfirmed ? '✅ Projects Choice Locked' : '🔒 Confirm Projects Choice'}
        </button>
      </div>
    </div>
  );
}
