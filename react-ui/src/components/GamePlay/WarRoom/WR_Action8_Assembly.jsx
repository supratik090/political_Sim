import React from 'react';
import { useHorizontalScroll } from '../../../hooks/useHorizontalScroll';
import { formatBillName } from '../gameUtils';

/**
 * WR_Action8_Assembly — Assembly Vote / Legislative Agenda
 * Cleaner vote UI with card-section color language.
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
  scenarioBills  = [],
  scenarioEvents = [],
}) {
  const billScrollRef  = useHorizontalScroll();
  const activeBillKey  = turnData?.proposedBillKeyThisTurn;
  const activeEventKey = turnData?.activeEventKey;

  // ── Active Scenario Event ──────────────────────────────────────
  const activeEvent = scenarioEvents.find(e => e.eventKey === activeEventKey);
  if (activeEventKey && activeEvent) {
    return (
      <div style={{ padding: '14px 16px 0' }}>
        <div style={{ fontSize: '15px', fontWeight: 900, letterSpacing: '0.05em', textTransform: 'uppercase', color: '#F59E0B', marginBottom: '14px' }}>
          🌩️ Scenario Event
        </div>

        <div style={{
          background:   'linear-gradient(145deg,#1e1a00,#1a1000)',
          border:       '1px solid rgba(245,158,11,0.25)',
          borderRadius: '14px',
          padding:      '16px',
          marginBottom: '14px',
        }}>
          <div style={{ fontSize: '10px', fontWeight: 800, letterSpacing: '0.08em', textTransform: 'uppercase', color: '#F59E0B', marginBottom: '8px' }}>
            ⚡ ACTIVE EVENT
          </div>
          <div style={{ fontSize: '16px', fontWeight: 900, color: '#ffffff', marginBottom: '8px', lineHeight: 1.3 }}>
            {activeEvent.title || activeEvent.name}
          </div>
          {activeEvent.description && (
            <p style={{ fontSize: '13px', color: '#C9D1D9', lineHeight: 1.6, margin: '0 0 14px 0' }}>{activeEvent.description}</p>
          )}

          <div style={{ fontSize: '10px', fontWeight: 800, letterSpacing: '0.07em', textTransform: 'uppercase', color: '#7D8590', marginBottom: '8px' }}>
            YOUR RESPONSE
          </div>

          {(activeEvent.options || []).map(opt => {
            const optKey     = opt.optionKey || opt.key;
            const isSelected = selectedEventOptionKey === optKey;
            return (
              <button
                key={optKey}
                onClick={() => setSelectedEventOptionKey(optKey)}
                style={{
                  display:     'flex', alignItems: 'center', gap: '10px',
                  width:       '100%', textAlign: 'left',
                  padding:     '11px 12px', borderRadius: '10px', marginBottom: '7px',
                  minHeight:   '48px',
                  background:  isSelected ? 'rgba(108,58,181,0.15)' : 'rgba(255,255,255,0.04)',
                  border:      `1.5px solid ${isSelected ? 'var(--party-primary-color,#7C3AED)' : 'rgba(255,255,255,0.1)'}`,
                  color:       isSelected ? '#ffffff' : '#C9D1D9',
                  fontWeight:  isSelected ? 700 : 400,
                  fontSize:    '13px', cursor: 'pointer',
                  touchAction: 'manipulation', WebkitTapHighlightColor: 'transparent',
                  transition:  'all 0.15s ease',
                  boxShadow:   isSelected ? '0 0 10px rgba(108,58,181,0.3)' : 'none',
                  fontFamily:  'Montserrat,system-ui,sans-serif',
                }}
              >
                <span style={{ flex: 1, lineHeight: 1.4 }}>{opt.text}</span>
                {isSelected && <span style={{ color: '#C084FC', fontSize: '14px', fontWeight: 900 }}>✓</span>}
              </button>
            );
          })}
        </div>
      </div>
    );
  }

  // ── Active Bill Vote ───────────────────────────────────────────
  if (activeBillKey) {
    const activeBill = scenarioBills.find(b => b.billKey === activeBillKey);
    const billName   = formatBillName(activeBillKey, activeBill, scenarioBills);
    const billDesc   = activeBill?.description || 'Review and vote on the proposed legislation.';
    const passEffects= activeBill?.effects?.onPass || activeBill?.passEffects || {};
    const failEffects= activeBill?.effects?.onFail || activeBill?.failEffects || {};

    const currentCoins = activeParty?.stats?.coins ?? activeParty?.coins ?? 0;
    const canAffordWhip = currentCoins >= 25;

    const voteIs = (v) => billVote === v;

    return (
      <div style={{ padding: '14px 16px 0' }}>
        <div style={{ fontSize: '15px', fontWeight: 900, letterSpacing: '0.05em', textTransform: 'uppercase', color: '#60A5FA', marginBottom: '14px' }}>
          🗳️ Assembly Vote
        </div>

        {/* Bill card */}
        <div style={{
          background:   'linear-gradient(145deg,#1E3A5F,#1A2840)',
          border:       '1px solid rgba(37,99,235,0.3)',
          borderRadius: '14px',
          padding:      '16px',
          marginBottom: '14px',
        }}>
          <div style={{ fontSize: '10px', fontWeight: 800, letterSpacing: '0.08em', textTransform: 'uppercase', color: '#60A5FA', marginBottom: '8px' }}>
            📜 BILL UP FOR VOTE
          </div>
          <div style={{ fontSize: '16px', fontWeight: 900, color: '#ffffff', marginBottom: '8px', lineHeight: 1.3 }}>
            {billName}
          </div>
          <p style={{ fontSize: '13px', color: '#C9D1D9', lineHeight: 1.6, margin: '0 0 12px 0' }}>{billDesc}</p>

          {/* Pass / Fail effect chips */}
          {(Object.keys(passEffects).length > 0 || Object.keys(failEffects).length > 0) && (
            <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', marginBottom: '14px' }}>
              {Object.keys(passEffects).length > 0 && (
                <span className="wr-badge wr-badge-teal">
                  ✅ If passes: {Object.entries(passEffects).map(([, v]) => `${v > 0 ? '+' : ''}${v}`).join(', ')}
                </span>
              )}
              {Object.keys(failEffects).length > 0 && (
                <span className="wr-badge wr-badge-red">
                  ❌ If fails: {Object.entries(failEffects).map(([, v]) => `${v > 0 ? '+' : ''}${v}`).join(', ')}
                </span>
              )}
            </div>
          )}

          {/* ── AYE / NAY — large tap targets ── */}
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px', marginBottom: '8px' }}>
            {/* AYE */}
            <button
              onClick={() => setBillVote('YES')}
              style={{
                minHeight:  '54px', fontSize: '15px', fontWeight: 900,
                borderRadius: '12px', cursor: 'pointer',
                touchAction: 'manipulation', WebkitTapHighlightColor: 'transparent',
                transition:  'all 0.15s ease', fontFamily: 'Montserrat,system-ui,sans-serif',
                background:  (voteIs('YES') || voteIs('AYE'))
                  ? 'linear-gradient(135deg,#16A34A,#15803d)'
                  : 'rgba(22,163,74,0.08)',
                color:       (voteIs('YES') || voteIs('AYE')) ? '#ffffff' : '#4ADE80',
                border:      `2px solid ${(voteIs('YES') || voteIs('AYE')) ? '#16A34A' : 'rgba(22,163,74,0.3)'}`,
                boxShadow:   (voteIs('YES') || voteIs('AYE')) ? '0 0 16px rgba(22,163,74,0.45)' : 'none',
              }}
            >
              ✅ AYE
            </button>
            {/* NAY */}
            <button
              onClick={() => setBillVote('NO')}
              style={{
                minHeight:  '54px', fontSize: '15px', fontWeight: 900,
                borderRadius: '12px', cursor: 'pointer',
                touchAction: 'manipulation', WebkitTapHighlightColor: 'transparent',
                transition:  'all 0.15s ease', fontFamily: 'Montserrat,system-ui,sans-serif',
                background:  (voteIs('NO') || voteIs('NAY'))
                  ? 'linear-gradient(135deg,#DC2626,#b91c1c)'
                  : 'rgba(220,38,38,0.08)',
                color:       (voteIs('NO') || voteIs('NAY')) ? '#ffffff' : '#F87171',
                border:      `2px solid ${(voteIs('NO') || voteIs('NAY')) ? '#DC2626' : 'rgba(220,38,38,0.3)'}`,
                boxShadow:   (voteIs('NO') || voteIs('NAY')) ? '0 0 16px rgba(220,38,38,0.4)' : 'none',
              }}
            >
              ❌ NAY
            </button>
          </div>

          {/* Abstain — slim tertiary */}
          <button
            onClick={() => setBillVote('ABSTAIN')}
            style={{
              width:       '100%', minHeight: '40px', marginBottom: '10px',
              background:  voteIs('ABSTAIN') ? 'rgba(255,255,255,0.09)' : 'transparent',
              border:      `1px dashed ${voteIs('ABSTAIN') ? 'rgba(255,255,255,0.35)' : 'rgba(255,255,255,0.18)'}`,
              borderRadius:'10px',
              color:       voteIs('ABSTAIN') ? '#E6EDF3' : '#64748B',
              fontSize:    '12px', fontWeight: 700, cursor: 'pointer',
              touchAction: 'manipulation',
              fontFamily:  'Montserrat,system-ui,sans-serif',
            }}
          >
            ◯ Abstain
          </button>

          {/* Party Whip — secondary toggle */}
          <button
            disabled={!canAffordWhip}
            onClick={() => canAffordWhip && setWhipIssued(!whipIssued)}
            style={{
              width:       '100%', minHeight: '42px',
              background:  whipIssued ? 'rgba(245,158,11,0.13)' : 'rgba(255,255,255,0.04)',
              border:      `1.5px solid ${whipIssued ? '#F59E0B' : 'rgba(255,255,255,0.1)'}`,
              borderRadius:'10px',
              color:       whipIssued ? '#FCD34D' : canAffordWhip ? '#C9D1D9' : '#475569',
              fontSize:    '12px', fontWeight: 700,
              cursor:      canAffordWhip ? 'pointer' : 'not-allowed',
              opacity:     canAffordWhip ? 1 : 0.55,
              transition:  'all 0.15s ease',
              fontFamily:  'Montserrat,system-ui,sans-serif',
              display:     'flex', alignItems: 'center', justifyContent: 'center', gap: '6px',
            }}
          >
            🔔 {whipIssued ? 'Whip Issued' : 'Issue Party Whip'}
            <span style={{
              fontSize:   '10px', fontWeight: 800, padding: '1px 6px', borderRadius: '4px',
              background: whipIssued ? 'rgba(245,158,11,0.2)' : 'rgba(255,255,255,0.07)',
              color:      whipIssued ? '#FCD34D' : '#94A3B8',
            }}>
              25C
            </span>
          </button>

          {!canAffordWhip && (
            <div style={{ fontSize: '11px', color: '#F87171', textAlign: 'center', marginTop: '5px', fontWeight: 700 }}>
              Need 25C — you have {currentCoins}C
            </div>
          )}
        </div>
      </div>
    );
  }

  // ── Propose a Bill ─────────────────────────────────────────────
  const playerRole  = activeParty?.role || 'THIRD_PARTY';
  const isGov       = playerRole === 'GOVERNMENT';
  const unproposed  = (turnData?.bills || []).filter(b => b.status === 'NOT_PROPOSED');
  const available   = unproposed
    .map(state => ({ state, def: scenarioBills.find(b => b.billKey === state.billKey) }))
    .filter(b => b.def)
    .filter(b => isGov ? b.def.proposingRole === 'GOVERNMENT' : b.def.proposingRole === 'OPPOSITION');

  return (
    <div style={{ padding: '14px 16px 0' }}>
      <div style={{ fontSize: '15px', fontWeight: 900, letterSpacing: '0.05em', textTransform: 'uppercase', color: '#7D8590', marginBottom: '14px' }}>
        🏛️ Legislative Agenda
      </div>
      <div style={{ fontSize: '12px', color: '#7D8590', marginBottom: '12px' }}>
        No vote scheduled — propose a bill for next cycle
      </div>

      {available.length === 0 ? (
        <div style={{ textAlign: 'center', padding: '24px 0', color: '#7D8590', fontSize: '13px', fontStyle: 'italic' }}>
          No bills available to propose this turn.
        </div>
      ) : (
        <div ref={billScrollRef} className="wr-hscroll" style={{ paddingBottom: '12px', gap: '10px' }}>
          {available.map(({ def }) => {
            const isSelected = proposedBillKey === def.billKey;
            return (
              <div
                key={def.billKey}
                onClick={() => setProposedBillKey(isSelected ? '' : def.billKey)}
                style={{
                  width:       '170px', flexShrink: 0, padding: '14px',
                  background:  isSelected ? 'rgba(37,99,235,0.12)' : 'rgba(255,255,255,0.04)',
                  border:      `2px solid ${isSelected ? '#2563EB' : 'rgba(255,255,255,0.1)'}`,
                  borderRadius:'12px', cursor: 'pointer',
                  boxShadow:   isSelected ? '0 0 12px rgba(37,99,235,0.3)' : 'none',
                  transition:  'all 0.15s ease',
                  touchAction: 'manipulation', WebkitTapHighlightColor: 'transparent',
                }}
              >
                <div style={{ fontSize: '12px', fontWeight: 900, color: '#ffffff', marginBottom: '6px', lineHeight: 1.3 }}>{def.name}</div>
                {def.description && (
                  <div style={{ fontSize: '11px', color: '#8B949E', lineHeight: 1.5, marginBottom: '8px' }}>
                    {def.description.slice(0, 80)}…
                  </div>
                )}
                <div style={{ fontSize: '10px', fontWeight: 800, color: isSelected ? '#60A5FA' : '#7D8590' }}>
                  {isSelected ? '✓ SELECTED' : '📋 Tap to propose'}
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
