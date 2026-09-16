import React from 'react';
import { useHorizontalScroll } from '../../../hooks/useHorizontalScroll';

/**
 * WR_Action8_Assembly — Assembly Vote / Legislative Agenda
 * Props: { turnData, activeParty, billVote, setBillVote, whipIssued, setWhipIssued,
 *           proposedBillKey, setProposedBillKey, selectedEventOptionKey, setSelectedEventOptionKey,
 *           scenarioBills, scenarioEvents }
 */
export default function WR_Action8_Assembly({
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
  scenarioEvents = [],
}) {
  const billScrollRef = useHorizontalScroll();
  const activeBillKey  = turnData?.proposedBillKeyThisTurn;
  const activeEventKey = turnData?.activeEventKey;

  // ── Active Event ──
  const activeEvent = scenarioEvents.find(e => e.eventKey === activeEventKey);
  if (activeEventKey && activeEvent) {
    return (
      <div style={{ padding: '14px 16px 0' }}>
        <div style={{ marginBottom: '14px' }}>
          <div style={{ fontSize: '15px', fontWeight: 900, letterSpacing: '0.05em', textTransform: 'uppercase', color: '#F59E0B' }}>
            🌩️ Scenario Event
          </div>
          <div style={{ fontSize: '12px', color: '#7D8590', marginTop: '2px' }}>React to the active event</div>
        </div>

        <div style={{
          background: 'linear-gradient(145deg,#1e1a00,#1a1000)',
          border: '1px solid rgba(245,158,11,0.25)',
          borderRadius: '14px',
          padding: '16px',
          marginBottom: '14px',
        }}>
          <div style={{ fontSize: '10px', fontWeight: 800, letterSpacing: '0.08em', textTransform: 'uppercase', color: '#F59E0B', marginBottom: '8px' }}>
            ⚡ ACTIVE EVENT
          </div>
          <div style={{ fontSize: '17px', fontWeight: 900, color: '#ffffff', marginBottom: '8px' }}>{activeEvent.title || activeEvent.name}</div>
          {activeEvent.description && (
            <p style={{ fontSize: '13px', color: '#C9D1D9', lineHeight: 1.6, margin: '0 0 14px 0' }}>{activeEvent.description}</p>
          )}

          <div style={{ fontSize: '11px', fontWeight: 800, letterSpacing: '0.07em', textTransform: 'uppercase', color: '#7D8590', marginBottom: '8px' }}>
            YOUR RESPONSE
          </div>
          {(activeEvent.options || []).map(opt => {
            const optKey = opt.optionKey || opt.key;
            const isSelected = selectedEventOptionKey === optKey;
            return (
              <button key={optKey} onClick={() => setSelectedEventOptionKey(optKey)} style={{
                display: 'flex', alignItems: 'flex-start', gap: '10px', width: '100%', textAlign: 'left',
                padding: '13px 14px', borderRadius: '10px', marginBottom: '8px', minHeight: '52px',
                background: isSelected ? 'rgba(245,158,11,0.12)' : 'rgba(255,255,255,0.04)',
                border: `1.5px solid ${isSelected ? '#F59E0B' : 'rgba(255,255,255,0.1)'}`,
                color: isSelected ? '#FCD34D' : '#C9D1D9', fontWeight: isSelected ? 700 : 400,
                fontSize: '14px', cursor: 'pointer', touchAction: 'manipulation',
                WebkitTapHighlightColor: 'transparent', transition: 'all 0.15s ease',
                fontFamily: 'Montserrat,system-ui,sans-serif',
              }}>
                <span style={{ flex: 1, lineHeight: 1.4 }}>{opt.text}</span>
                {isSelected && <span style={{ color: '#F59E0B', fontSize: '16px', fontWeight: 900 }}>✓</span>}
              </button>
            );
          })}
        </div>
      </div>
    );
  }

  // ── Active Bill Vote ──
  if (activeBillKey) {
    const activeBill = scenarioBills.find(b => b.billKey === activeBillKey);
    const billName   = activeBill?.name || activeBillKey;
    const billDesc   = activeBill?.description || 'Review and vote on the proposed legislation.';

    const passEffects = activeBill?.effects?.onPass || activeBill?.passEffects || {};
    const failEffects = activeBill?.effects?.onFail || activeBill?.failEffects || {};

    return (
      <div style={{ padding: '14px 16px 0' }}>
        <div style={{ marginBottom: '14px' }}>
          <div style={{ fontSize: '15px', fontWeight: 900, letterSpacing: '0.05em', textTransform: 'uppercase', color: '#60A5FA' }}>
            🗳️ Assembly Vote
          </div>
          <div style={{ fontSize: '12px', color: '#7D8590', marginTop: '2px' }}>Cast your party's vote on the active bill</div>
        </div>

        {/* Bill card */}
        <div style={{
          background: 'linear-gradient(145deg,#1E3A5F,#1A2840)',
          border: '1px solid rgba(37,99,235,0.35)',
          borderRadius: '14px', padding: '16px', marginBottom: '16px',
        }}>
          <div style={{ fontSize: '10px', fontWeight: 800, letterSpacing: '0.08em', textTransform: 'uppercase', color: '#60A5FA', marginBottom: '8px' }}>
            📜 BILL UP FOR VOTE
          </div>
          <div style={{ fontSize: '17px', fontWeight: 900, color: '#ffffff', marginBottom: '8px' }}>{billName}</div>
          <p style={{ fontSize: '13px', color: '#C9D1D9', lineHeight: 1.6, margin: '0 0 14px 0' }}>{billDesc}</p>

          {/* If-passed / if-failed chips */}
          {(Object.keys(passEffects).length > 0 || Object.keys(failEffects).length > 0) && (
            <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', marginBottom: '14px' }}>
              {Object.keys(passEffects).length > 0 && (
                <span className="wr-badge wr-badge-teal">✅ If passed: {Object.entries(passEffects).map(([k,v]) => `${v>0?'+':''}${v}`).join(', ')}</span>
              )}
              {Object.keys(failEffects).length > 0 && (
                <span className="wr-badge wr-badge-red">❌ If failed: {Object.entries(failEffects).map(([k,v]) => `${v>0?'+':''}${v}`).join(', ')}</span>
              )}
            </div>
          )}

          {/* AYE / NAY */}
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px', marginBottom: '10px' }}>
            <button onClick={() => setBillVote('AYE')} style={{
              minHeight: '56px', fontSize: '16px', fontWeight: 900,
              background: billVote === 'AYE' ? '#16A34A' : 'rgba(22,163,74,0.10)',
              color: billVote === 'AYE' ? '#ffffff' : '#4ADE80',
              border: `2px solid ${billVote === 'AYE' ? '#16A34A' : 'rgba(22,163,74,0.3)'}`,
              borderRadius: '12px', cursor: 'pointer', touchAction: 'manipulation',
              boxShadow: billVote === 'AYE' ? '0 0 18px rgba(22,163,74,0.5)' : 'none',
              transition: 'all 0.15s ease', fontFamily: 'Montserrat,system-ui,sans-serif',
            }}>
              ✅ AYE
            </button>
            <button onClick={() => setBillVote('NAY')} style={{
              minHeight: '56px', fontSize: '16px', fontWeight: 900,
              background: billVote === 'NAY' ? '#DC2626' : 'rgba(220,38,38,0.10)',
              color: billVote === 'NAY' ? '#ffffff' : '#F87171',
              border: `2px solid ${billVote === 'NAY' ? '#DC2626' : 'rgba(220,38,38,0.3)'}`,
              borderRadius: '12px', cursor: 'pointer', touchAction: 'manipulation',
              boxShadow: billVote === 'NAY' ? '0 0 18px rgba(220,38,38,0.45)' : 'none',
              transition: 'all 0.15s ease', fontFamily: 'Montserrat,system-ui,sans-serif',
            }}>
              ❌ NAY
            </button>
          </div>

          {/* Abstain */}
          <button onClick={() => setBillVote('ABSTAIN')} style={{
            width: '100%', minHeight: '44px', marginBottom: '10px',
            background: billVote === 'ABSTAIN' ? 'rgba(255,255,255,0.10)' : 'transparent',
            border: '1px dashed rgba(255,255,255,0.2)', borderRadius: '10px',
            color: billVote === 'ABSTAIN' ? '#E6EDF3' : '#7D8590',
            fontSize: '13px', fontWeight: 700, cursor: 'pointer', touchAction: 'manipulation',
            fontFamily: 'Montserrat,system-ui,sans-serif',
          }}>
            ◯ Abstain
          </button>

          {/* Party Whip toggle */}
          {(() => {
            const currentCoins = activeParty?.stats?.coins ?? activeParty?.coins ?? 0;
            const canAffordWhip = currentCoins >= 25;
            return (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                <button
                  disabled={!canAffordWhip}
                  onClick={() => canAffordWhip && setWhipIssued(!whipIssued)}
                  style={{
                    width: '100%', minHeight: '46px',
                    background: whipIssued ? 'rgba(245,158,11,0.15)' : 'rgba(255,255,255,0.04)',
                    border: `1.5px solid ${whipIssued ? '#F59E0B' : 'rgba(255,255,255,0.1)'}`,
                    borderRadius: '10px', color: whipIssued ? '#FCD34D' : canAffordWhip ? '#E6EDF3' : '#64748b',
                    fontSize: '13px', fontWeight: 700, cursor: canAffordWhip ? 'pointer' : 'not-allowed',
                    opacity: canAffordWhip ? 1 : 0.6,
                    transition: 'all 0.15s ease', fontFamily: 'Montserrat,system-ui,sans-serif',
                  }}
                >
                  🔔 {whipIssued ? 'Party Whip ISSUED (Cost: 25 Coins)' : 'Issue Party Whip (Cost: 25 Coins)'}
                </button>
                {!canAffordWhip && (
                  <span style={{ fontSize: '11px', color: '#ef4444', textAlign: 'center', fontWeight: 'bold' }}>
                    ⚠️ Insufficient Coins (25 required, current: {currentCoins})
                  </span>
                )}
              </div>
            );
          })()}
        </div>
      </div>
    );
  }

  // ── Propose a Bill ──
  const playerRole = activeParty?.role || 'THIRD_PARTY';
  const isGov = playerRole === 'GOVERNMENT';
  const unproposed = (turnData?.bills || []).filter(b => b.status === 'NOT_PROPOSED');
  const available = unproposed
    .map(state => ({ state, def: scenarioBills.find(b => b.billKey === state.billKey) }))
    .filter(b => b.def)
    .filter(b => isGov ? b.def.proposingRole === 'GOVERNMENT' : b.def.proposingRole === 'OPPOSITION');

  return (
    <div style={{ padding: '14px 16px 0' }}>
      <div style={{ marginBottom: '14px' }}>
        <div style={{ fontSize: '15px', fontWeight: 900, letterSpacing: '0.05em', textTransform: 'uppercase', color: '#7D8590' }}>
          🏛️ Legislative Agenda
        </div>
        <div style={{ fontSize: '12px', color: '#7D8590', marginTop: '2px' }}>
          No vote scheduled — you may propose a bill for next cycle
        </div>
      </div>

      {available.length === 0 ? (
        <div style={{ textAlign: 'center', padding: '24px 0', color: '#7D8590', fontSize: '13px', fontStyle: 'italic' }}>
          No bills available to propose this turn.
        </div>
      ) : (
        <div ref={billScrollRef} className="wr-hscroll" style={{ paddingBottom: '12px', gap: '12px' }}>
          {available.map(({ state, def }) => {
            const isSelected = proposedBillKey === def.billKey;
            return (
              <div
                key={def.billKey}
                onClick={() => setProposedBillKey(isSelected ? '' : def.billKey)}
                style={{
                  width: '180px', flexShrink: 0, padding: '14px',
                  background: isSelected ? 'rgba(37,99,235,0.12)' : 'rgba(255,255,255,0.04)',
                  border: `2px solid ${isSelected ? '#2563EB' : 'rgba(255,255,255,0.1)'}`,
                  borderRadius: '14px', cursor: 'pointer',
                  boxShadow: isSelected ? '0 0 14px rgba(37,99,235,0.35)' : 'none',
                  transition: 'all 0.15s ease',
                  touchAction: 'manipulation', WebkitTapHighlightColor: 'transparent',
                }}
              >
                <div style={{ fontSize: '13px', fontWeight: 900, color: '#ffffff', marginBottom: '6px', lineHeight: 1.3 }}>{def.name}</div>
                {def.description && (
                  <div style={{ fontSize: '11px', color: '#8B949E', lineHeight: 1.5, marginBottom: '8px' }}>{def.description.slice(0, 80)}…</div>
                )}
                <div style={{ fontSize: '11px', fontWeight: 800, color: isSelected ? '#60A5FA' : '#7D8590' }}>
                  {isSelected ? '✓ SELECTED TO PROPOSE' : '📋 Tap to propose'}
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
