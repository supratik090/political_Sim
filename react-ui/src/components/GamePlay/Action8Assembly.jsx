import React from 'react';

export default function Action8Assembly({
  turnData,
  activeParty,
  billVote,
  setBillVote,
  whipIssued,
  setWhipIssued,
  proposedBillKey,
  setProposedBillKey,
  selectedEventOptionKey,
  setSelectedEventOptionKey,
  scenarioBills = [],
  scenarioEvents = []
}) {
  const activeBillKey = turnData.proposedBillKeyThisTurn;
  const activeEventKey = turnData.activeEventKey;

  // 1. Find active bill details
  const activeBill = scenarioBills.find(b => b.billKey === activeBillKey);
  const activeBillName = activeBill ? activeBill.name : activeBillKey;
  const activeBillDescription = activeBill ? activeBill.description : 'Details of the active bill.';

  // 2. Find active event details
  const activeEvent = scenarioEvents.find(e => e.eventKey === activeEventKey);

  // 3. Find unproposed bills the player can propose
  // Show all NOT_PROPOSED bills, but label/filter them nicely.
  // The player's role is activeParty?.role (GOVERNMENT or OPPOSITION)
  const playerRole = activeParty?.role || 'THIRD_PARTY';
  const unproposedStates = (turnData.bills || []).filter(b => b.status === 'NOT_PROPOSED');
  
  const availableBillsToPropose = unproposedStates.map(state => {
    const def = scenarioBills.find(b => b.billKey === state.billKey);
    return {
      state,
      def
    };
  }).filter(b => b.def);

  // Government gets GOVERNMENT bills; Opposition and Third Parties get OPPOSITION bills
  const isGovernment = playerRole === 'GOVERNMENT';
  const myRoleBills = availableBillsToPropose.filter(b => {
    if (isGovernment) {
      return b.def.proposingRole === 'GOVERNMENT';
    } else {
      return b.def.proposingRole === 'OPPOSITION';
    }
  });

  const formatEffects = (effects) => {
    if (!effects || Object.keys(effects).length === 0) return 'None';
    const parts = [];
    if (effects.coins) parts.push(`💰 ${effects.coins > 0 ? '+' : ''}${effects.coins} Coins`);
    if (effects.partyMorale) parts.push(`✊ ${effects.partyMorale > 0 ? '+' : ''}${effects.partyMorale} Morale`);
    if (effects.corruptionScore) parts.push(`⚖️ ${effects.corruptionScore > 0 ? '+' : ''}${effects.corruptionScore} Corruption`);
    if (effects.mediaImage) parts.push(`📢 ${effects.mediaImage > 0 ? '+' : ''}${effects.mediaImage} Media`);
    if (effects.publicSupport) parts.push(`📈 ${effects.publicSupport > 0 ? '+' : ''}${effects.publicSupport}% Support`);
    return parts.join(', ');
  };

  const getPassCostAndBenefit = (effects) => {
    if (!effects || Object.keys(effects).length === 0) return { cost: 'None', benefit: 'None' };
    const costs = [];
    const benefits = [];
    Object.entries(effects).forEach(([key, val]) => {
      const isNegative = val < 0;
      const emoji = key === 'coins' ? '💰' : (key === 'partyMorale' ? '✊' : (key === 'corruptionScore' ? '⚖️' : (key === 'mediaImage' ? '📢' : (key === 'publicSupport' ? '📈' : ''))));
      const absVal = Math.abs(val);
      
      // For corruptionScore, negative is good (benefit), positive is bad (cost)
      if (key === 'corruptionScore') {
        if (val > 0) {
          costs.push(`${emoji} +${val} Corruption`);
        } else {
          benefits.push(`${emoji} -${absVal} Corruption`);
        }
      } else {
        if (isNegative) {
          costs.push(`${emoji} ${absVal} ${key === 'publicSupport' ? '% Support' : key.replace('party', '')}`);
        } else {
          benefits.push(`${emoji} +${val} ${key === 'publicSupport' ? '% Support' : key.replace('party', '')}`);
        }
      }
    });

    return {
      cost: costs.length > 0 ? costs.join(', ') : 'None',
      benefit: benefits.length > 0 ? benefits.join(', ') : 'None'
    };
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '25px' }}>
      
      {/* SECTION A: Active Legislative Bill Voting */}
      {activeBillKey && (
        <div style={{
          border: '2px solid var(--primary-border)',
          borderRadius: '12px',
          padding: '20px',
          background: 'rgba(var(--party-primary-color-rgb, 101, 148, 177), 0.03)',
          boxShadow: '0 4px 15px rgba(0,0,0,0.02)'
        }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px', borderBottom: '1px solid var(--primary-border)', paddingBottom: '8px' }}>
            <h4 style={{ margin: 0, fontSize: '15px', color: 'var(--primary-dark)', fontWeight: 800 }}>
              🗳️ Assembly Vote: {activeBillName}
            </h4>
            <span style={{ fontSize: '11px', background: 'var(--primary-dark)', color: '#fff', padding: '2px 8px', borderRadius: '10px', fontWeight: 'bold' }}>
              PROPOSED BY: {activeBill?.proposingRole || 'CABINET'}
            </span>
          </div>

          <p style={{ margin: '0 0 16px 0', fontSize: '13px', color: '#4b5563', lineHeight: 1.5 }}>
            {activeBillDescription}
          </p>

          {/* Effects Panel */}
          {activeBill && (
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '15px', background: '#fff', padding: '12px', borderRadius: '8px', border: '1px solid var(--primary-border)', marginBottom: '20px', fontSize: '12px' }}>
              <div>
                <strong style={{ color: '#166534', display: 'block', marginBottom: '4px' }}>✅ If Passed:</strong>
                <span style={{ color: '#374151' }}>{formatEffects(activeBill.effectsPassed)}</span>
                <span style={{ display: 'block', color: '#15803d', fontWeight: 'bold', marginTop: '2px' }}>
                  +{activeBill.pointsPassed} Morale (Proposer)
                </span>
              </div>
              <div>
                <strong style={{ color: '#9f1239', display: 'block', marginBottom: '4px' }}>❌ If Failed:</strong>
                <span style={{ color: '#374151' }}>{formatEffects(activeBill.effectsFailed)}</span>
                <span style={{ display: 'block', color: '#b91c1c', fontWeight: 'bold', marginTop: '2px' }}>
                  {activeBill.pointsFailed} Morale (Proposer)
                </span>
              </div>
            </div>
          )}

          {/* Vote Choices */}
          <div style={{ marginBottom: '20px' }}>
            <label style={{ fontSize: '11px', fontWeight: 'bold', display: 'block', marginBottom: '8px', color: '#4b5563', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
              Cast Your Party's Vote:
            </label>
            <div style={{ display: 'flex', gap: '10px' }}>
              <button
                type="button"
                onClick={() => {
                  setBillVote('YES');
                }}
                style={{
                  flex: 1,
                  padding: '12px',
                  borderRadius: '8px',
                  border: `2px solid ${billVote === 'YES' ? '#22c55e' : '#e5e7eb'}`,
                  background: billVote === 'YES' ? '#e8f5e9' : '#fff',
                  color: billVote === 'YES' ? '#1b5e20' : '#4b5563',
                  fontWeight: 'bold',
                  cursor: 'pointer',
                  fontSize: '13px',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  gap: '6px',
                  transition: 'all 0.15s ease'
                }}
              >
                👍 VOTE YES
              </button>
              <button
                type="button"
                onClick={() => {
                  setBillVote('NO');
                }}
                style={{
                  flex: 1,
                  padding: '12px',
                  borderRadius: '8px',
                  border: `2px solid ${billVote === 'NO' ? '#ef4444' : '#e5e7eb'}`,
                  background: billVote === 'NO' ? '#ffebee' : '#fff',
                  color: billVote === 'NO' ? '#c62828' : '#4b5563',
                  fontWeight: 'bold',
                  cursor: 'pointer',
                  fontSize: '13px',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  gap: '6px',
                  transition: 'all 0.15s ease'
                }}
              >
                👎 VOTE NO
              </button>
              <button
                type="button"
                onClick={() => {
                  setBillVote('ABSTAIN');
                  setWhipIssued(false); // Can't issue a whip on abstain
                }}
                style={{
                  flex: 1,
                  padding: '12px',
                  borderRadius: '8px',
                  border: `2px solid ${billVote === 'ABSTAIN' ? '#9ca3af' : '#e5e7eb'}`,
                  background: billVote === 'ABSTAIN' ? '#f3f4f6' : '#fff',
                  color: billVote === 'ABSTAIN' ? '#374151' : '#4b5563',
                  fontWeight: 'bold',
                  cursor: 'pointer',
                  fontSize: '13px',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  gap: '6px',
                  transition: 'all 0.15s ease'
                }}
              >
                ⚪ ABSTAIN
              </button>
            </div>
          </div>

          {/* Whip Mechanic Toggle */}
          {billVote !== 'ABSTAIN' && (
            <div style={{
              background: '#fff',
              border: '1px solid var(--primary-border)',
              borderRadius: '8px',
              padding: '12px 15px',
              display: 'flex',
              flexDirection: 'column',
              gap: '6px'
            }}>
              <label style={{ display: 'flex', alignItems: 'center', gap: '8px', cursor: 'pointer', fontSize: '13px', fontWeight: 'bold', color: 'var(--primary-dark)' }}>
                <input
                  type="checkbox"
                  checked={whipIssued}
                  disabled={(activeParty?.stats?.coins || 0) < 25}
                  onChange={(e) => setWhipIssued(e.target.checked)}
                  style={{ width: '16px', height: '16px' }}
                />
                📣 Issue Legislative Whip (Cost: 25 Coins)
              </label>
              <span style={{ fontSize: '11px', color: '#6b7280', paddingLeft: '24px', lineHeight: 1.4 }}>
                Enforces absolute voting discipline. All {activeParty?.stats?.publicSupport}% of your support share will vote <strong>{billVote}</strong>. If whip is not issued, voters split based on party corruption ({activeParty?.stats?.corruptionScore}%) and media image ({activeParty?.stats?.mediaImage}%), risking rebel votes!
              </span>
              {(activeParty?.stats?.coins || 0) < 25 && (
                <span style={{ fontSize: '11px', color: '#ef4444', fontWeight: 'bold', paddingLeft: '24px', marginTop: '4px' }}>
                  ⚠️ Cannot issue whip: Insufficient coins (Current: {activeParty?.stats?.coins || 0} / 25 required).
                </span>
              )}
            </div>
          )}
        </div>
      )}

      {/* SECTION B: Active Event Card Decision */}
      {activeEventKey && (
        <div style={{
          border: '2px solid #3b82f6',
          borderRadius: '12px',
          padding: '20px',
          background: 'rgba(59, 130, 246, 0.03)',
          boxShadow: '0 4px 15px rgba(0,0,0,0.02)'
        }}>
          <h4 style={{ margin: '0 0 8px 0', fontSize: '15px', color: '#1d4ed8', fontWeight: 800, display: 'flex', alignItems: 'center', gap: '6px' }}>
            📢 Special Event: {activeEvent ? activeEvent.name : activeEventKey}
          </h4>
          <p style={{ margin: '0 0 18px 0', fontSize: '13px', color: '#4b5563', lineHeight: 1.5 }}>
            {activeEvent ? activeEvent.description : 'A special event requires your intervention.'}
          </p>

          <label style={{ fontSize: '11px', fontWeight: 'bold', display: 'block', marginBottom: '8px', color: '#4b5563', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
            Select Your Party's Response: <span style={{ color: '#ef4444' }}>*</span>
          </label>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            {activeEvent?.options?.map(opt => {
              const hasCoinsCost = opt.cost?.coins > 0;
              const hasMoraleCost = opt.cost?.partyMorale > 0;
              const canAffordCoins = !hasCoinsCost || (activeParty?.stats?.coins || 0) >= opt.cost.coins;
              const canAffordMorale = !hasMoraleCost || (activeParty?.stats?.partyMorale || 0) >= opt.cost.partyMorale;
              const isAffordable = canAffordCoins && canAffordMorale;
              const isSelected = selectedEventOptionKey === opt.optionKey;

              const costLabels = [];
              if (hasCoinsCost) costLabels.push(`${opt.cost.coins} Coins`);
              if (hasMoraleCost) costLabels.push(`${opt.cost.partyMorale} Morale`);
              const costText = costLabels.length > 0 ? `Cost: ${costLabels.join(', ')}` : 'Cost: None';

              return (
                <div
                  key={opt.optionKey}
                  onClick={() => {
                    setSelectedEventOptionKey(opt.optionKey);
                  }}
                  style={{
                    border: `2px solid ${isSelected ? '#3b82f6' : '#e5e7eb'}`,
                    background: isSelected ? '#eff6ff' : '#fff',
                    borderRadius: '8px',
                    padding: '12px 15px',
                    cursor: 'pointer',
                    transition: 'all 0.15s ease',
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '6px'
                  }}
                >
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <span style={{ fontSize: '13px', fontWeight: 'bold', color: isSelected ? '#1e40af' : '#374151' }}>
                      {opt.text}
                    </span>
                    <span style={{
                      fontSize: '11px',
                      fontWeight: 'bold',
                      color: isAffordable ? '#6b7280' : '#ef4444',
                      background: isAffordable ? 'rgba(0,0,0,0.04)' : 'rgba(239, 68, 68, 0.08)',
                      padding: '2px 6px',
                      borderRadius: '4px'
                    }}>
                      {costText}
                    </span>
                  </div>
                  <div style={{ fontSize: '11px', color: '#166534', fontWeight: 'bold' }}>
                    ⚡ Effects: {formatEffects(opt.effects)}
                  </div>
                  {!isAffordable && (
                    <div style={{ fontSize: '10px', color: '#ef4444', fontWeight: 'bold', marginTop: '2px' }}>
                      ⚠️ Note: This option exceeds your current resources and may floor your stats at 0.
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* SECTION C: Propose a Bill for the Next Round */}
      <div style={{
        border: '1px solid var(--primary-border)',
        borderRadius: '12px',
        padding: '20px',
        background: '#ffffff'
      }}>
        <h4 style={{ margin: '0 0 6px 0', fontSize: '14px', color: 'var(--primary-dark)', fontWeight: 800 }}>
          🏛️ Propose Bill for Next Round
        </h4>
        <p style={{ margin: '0 0 15px 0', fontSize: '12px', color: '#6b7280', lineHeight: 1.4 }}>
          Set the assembly agenda! If your proposed bill is selected, it will be voted on in the next round. Government has higher agenda priority.
        </p>

        <label style={{ fontSize: '11px', fontWeight: 'bold', display: 'block', marginBottom: '12px', color: '#4b5563', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
          Select a Bill to Propose (Optional):
        </label>

        {(() => {
          const displayedBills = myRoleBills;

          if (displayedBills.length === 0) {
            return (
              <p style={{ color: 'gray', fontStyle: 'italic', fontSize: '12px', margin: 0 }}>
                No unproposed bills available for your role at this time.
              </p>
            );
          }

          return (
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '15px' }}>
              {displayedBills.map(({ def }) => {
                const isSelected = proposedBillKey === def.billKey;
                const { cost: passCost, benefit: passBenefit } = getPassCostAndBenefit(def.effectsPassed);

                return (
                  <div
                    key={def.billKey}
                    onClick={() => {
                      setProposedBillKey(isSelected ? '' : def.billKey);
                    }}
                    style={{
                      border: isSelected ? '2.5px solid var(--party-primary-color, var(--primary-dark))' : '1.5px solid rgba(var(--party-primary-color-rgb, 101, 148, 177), 0.15)',
                      borderRadius: '10px',
                      padding: '14px',
                      background: isSelected ? 'rgba(var(--party-primary-color-rgb, 101, 148, 177), 0.08)' : '#ffffff',
                      cursor: 'pointer',
                      transition: 'all 0.2s ease',
                      boxShadow: isSelected ? '0 4px 12px rgba(var(--party-primary-color-rgb, 101, 148, 177), 0.12)' : 'none',
                      position: 'relative',
                      overflow: 'hidden',
                      display: 'flex',
                      flexDirection: 'column',
                      justifyContent: 'space-between',
                      gap: '12px'
                    }}
                    onMouseEnter={(e) => {
                      if (!isSelected) e.currentTarget.style.background = 'rgba(var(--party-primary-color-rgb, 101, 148, 177), 0.02)';
                    }}
                    onMouseLeave={(e) => {
                      if (!isSelected) e.currentTarget.style.background = '#ffffff';
                    }}
                  >
                    <div>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                        <span style={{ fontSize: '9px', background: 'var(--primary-dark)', color: '#fff', padding: '1px 5px', borderRadius: '3px', fontWeight: 'bold', textTransform: 'uppercase' }}>
                          {def.proposingRole}
                        </span>
                        {isSelected && (
                          <span style={{ fontSize: '11px', color: '#166534', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '3px' }}>
                            🎯 SELECTED
                          </span>
                        )}
                      </div>
                      <h5 style={{ margin: '0 0 6px 0', fontSize: '13px', fontWeight: 'bold', color: 'var(--primary-dark)' }}>
                        📋 {def.name}
                      </h5>
                      <p style={{ margin: 0, fontSize: '11px', color: '#6b7280', lineHeight: 1.4 }}>
                        {def.description}
                      </p>
                    </div>

                    <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', fontSize: '11px', borderTop: '1px dashed var(--primary-border)', paddingTop: '8px' }}>
                      {passCost !== 'None' && (
                        <div style={{ color: '#be123c', fontWeight: 'bold' }}>
                          💸 Pass Cost: {passCost}
                        </div>
                      )}
                      <div style={{ color: '#166534', fontWeight: 'bold' }}>
                        🎁 Pass Benefit: {passBenefit} (+{def.pointsPassed} Morale)
                      </div>
                      <div style={{ color: '#6b7280', fontWeight: 'bold' }}>
                        ❌ If Defeated: {formatEffects(def.effectsFailed)} ({def.pointsFailed} Morale)
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          );
        })()}
      </div>

    </div>
  );
}
