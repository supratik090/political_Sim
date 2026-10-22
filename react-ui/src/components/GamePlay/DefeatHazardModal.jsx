import React, { useState } from 'react';

/**
 * DefeatHazardModal
 * Shown when the player's party has `hasDefeatHazard === true`.
 * Uses the party's primary color for branding. Lets the player:
 *   • Take a one-time emergency loan of 150 Coins (repaid 20/turn × 10 turns)
 *   • Buy a Recovery Pack: +20 Morale, −20 Corruption, +5 Support, +20 Media (costs 80 Coins)
 */
export default function DefeatHazardModal({
  isOpen,
  onClose,
  party,
  partyColor = '#E15554',
  onTakeLoan,
  onBuyRecoveryPack,
}) {
  const [busy, setBusy] = useState(false);
  const [msg, setMsg] = useState('');

  if (!isOpen || !party) return null;

  const stats = party.stats || {};
  const loanTaken = party.loanTaken || false;
  const loanTurnsLeft = party.loanRepaymentTurnsLeft || 0;
  const hasDefeatHazard = party.hasDefeatHazard;
  const canBuyPack = hasDefeatHazard && stats.coins >= 80;

  // ── derive a dark variant of the party color for backgrounds ──────────────
  const hexToRgbArr = (hex) => {
    let c = (hex || '#6594b1').replace('#', '');
    if (c.length === 3) c = c.split('').map(x => x + x).join('');
    return [
      parseInt(c.substring(0, 2), 16),
      parseInt(c.substring(2, 4), 16),
      parseInt(c.substring(4, 6), 16),
    ];
  };
  const [r, g, b] = hexToRgbArr(partyColor);
  const colorRgb = `${r}, ${g}, ${b}`;

  const handleLoan = async () => {
    setBusy(true);
    setMsg('');
    try {
      await onTakeLoan();
      setMsg('✅ Emergency loan of 150 Coins secured! Repayment: 20 Coins/turn × 10 turns.');
    } catch (e) {
      setMsg(`❌ ${e.message}`);
    } finally {
      setBusy(false);
    }
  };

  const handlePack = async () => {
    setBusy(true);
    setMsg('');
    try {
      await onBuyRecoveryPack();
      setMsg('✅ Recovery Pack applied! +20 Morale · −20 Corruption · +5 Support · +20 Media');
    } catch (e) {
      setMsg(`❌ ${e.message}`);
    } finally {
      setBusy(false);
    }
  };

  // ── stat pill helper ───────────────────────────────────────────────────────
  const StatPill = ({ label, value, unit = '', danger }) => (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      background: danger ? 'rgba(220,38,38,0.2)' : 'rgba(255,255,255,0.06)',
      border: `1.5px solid ${danger ? 'rgba(239,68,68,0.7)' : 'rgba(255,255,255,0.1)'}`,
      borderRadius: '8px',
      padding: '7px 4px',
      minWidth: 0,
      textAlign: 'center',
      boxShadow: danger ? '0 0 10px rgba(239,68,68,0.25)' : 'none',
      boxSizing: 'border-box',
    }}>
      <span style={{
        fontSize: '15px',
        fontWeight: 900,
        color: danger ? '#f87171' : '#fff',
        lineHeight: 1.1,
      }}>
        {value}{unit}
      </span>
      <span style={{
        fontSize: '9.5px',
        color: danger ? '#fca5a5' : 'rgba(255,255,255,0.6)',
        marginTop: '3px',
        fontWeight: 700,
        textTransform: 'uppercase',
        letterSpacing: '0.04em',
        lineHeight: 1.1,
      }}>
        {label}
      </span>
    </div>
  );

  // ── action card helper ─────────────────────────────────────────────────────
  const ActionCard = ({
    icon,
    title,
    badge,
    description,
    bullets,
    cost,
    disabled,
    disabledReason,
    onClick,
    ctaLabel,
    done,
  }) => (
    <div
      className="dh-action-card"
      style={{
        background: 'rgba(255,255,255,0.04)',
        border: `1.5px solid ${
          done
            ? 'rgba(74,222,128,0.45)'
            : disabled
            ? 'rgba(255,255,255,0.08)'
            : `rgba(${colorRgb}, 0.5)`
        }`,
        borderRadius: '14px',
        padding: '14px',
        display: 'flex',
        flexDirection: 'column',
        gap: '10px',
        opacity: disabled ? 0.65 : 1,
        transition: 'all 0.2s ease',
        boxSizing: 'border-box',
      }}
    >
      {/* Header row with Icon, Title/Cost on left, and Badge on right without overlap */}
      <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', gap: '8px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flex: 1, minWidth: 0 }}>
          <span style={{ fontSize: '24px', flexShrink: 0, lineHeight: 1 }}>{icon}</span>
          <div style={{ minWidth: 0 }}>
            <div style={{ fontSize: '14px', fontWeight: 800, color: '#fff', letterSpacing: '0.01em', lineHeight: 1.25, wordBreak: 'break-word' }}>
              {title}
            </div>
            {cost && (
              <div style={{ fontSize: '11px', color: partyColor, fontWeight: 700, marginTop: '2px', lineHeight: 1.3 }}>
                {cost}
              </div>
            )}
          </div>
        </div>

        {done && (
          <div style={{
            flexShrink: 0,
            background: 'rgba(74,222,128,0.18)',
            border: '1px solid rgba(74,222,128,0.45)',
            borderRadius: '6px',
            padding: '2px 8px',
            fontSize: '10px',
            fontWeight: 800,
            color: '#4ade80',
            letterSpacing: '0.05em',
            whiteSpace: 'nowrap',
          }}>
            ✓ USED
          </div>
        )}
        {badge && !done && (
          <div style={{
            flexShrink: 0,
            background: `rgba(${colorRgb},0.25)`,
            border: `1px solid rgba(${colorRgb},0.5)`,
            borderRadius: '6px',
            padding: '2px 8px',
            fontSize: '10px',
            fontWeight: 800,
            color: partyColor,
            letterSpacing: '0.05em',
            whiteSpace: 'nowrap',
          }}>
            {badge}
          </div>
        )}
      </div>

      <p style={{ margin: 0, fontSize: '12px', color: 'rgba(255,255,255,0.72)', lineHeight: 1.45 }}>
        {description}
      </p>

      {bullets && (
        <ul style={{ margin: 0, paddingLeft: '16px', display: 'flex', flexDirection: 'column', gap: '3px' }}>
          {bullets.map((b, i) => (
            <li key={i} style={{ fontSize: '11.5px', color: 'rgba(255,255,255,0.68)', lineHeight: 1.35 }}>
              {b}
            </li>
          ))}
        </ul>
      )}

      {disabledReason && (
        <div style={{
          fontSize: '11px',
          color: '#fb923c',
          fontWeight: 600,
          background: 'rgba(251,146,60,0.1)',
          borderRadius: '8px',
          padding: '6px 10px',
          border: '1px solid rgba(251,146,60,0.25)',
          lineHeight: 1.35,
        }}>
          ⚠️ {disabledReason}
        </div>
      )}

      {!done && (
        <button
          disabled={disabled || busy}
          onClick={onClick}
          style={{
            marginTop: '2px',
            padding: '10px 16px',
            minHeight: '40px',
            borderRadius: '10px',
            border: 'none',
            cursor: disabled || busy ? 'not-allowed' : 'pointer',
            fontWeight: 800,
            fontSize: '12px',
            letterSpacing: '0.04em',
            textTransform: 'uppercase',
            background: disabled ? 'rgba(255,255,255,0.1)' : `rgba(${colorRgb},1)`,
            color: '#fff',
            transition: 'all 0.18s ease',
            boxShadow: disabled ? 'none' : `0 3px 12px rgba(${colorRgb},0.35)`,
            width: '100%',
          }}
          onMouseEnter={e => { if (!disabled && !busy) e.currentTarget.style.transform = 'translateY(-1px)'; }}
          onMouseLeave={e => { e.currentTarget.style.transform = 'translateY(0)'; }}
        >
          {busy ? '⏳ Processing…' : ctaLabel}
        </button>
      )}
    </div>
  );

  return (
    <div
      className="modal-overlay"
      style={{
        zIndex: 9999,
        backgroundColor: 'rgba(0,0,0,0.88)',
        backdropFilter: 'blur(6px)',
      }}
    >
      {/* Animated glow bg & mobile styles */}
      <style>{`
        @keyframes dhPulse {
          0%, 100% { box-shadow: 0 0 40px rgba(${colorRgb},0.25), 0 0 90px rgba(${colorRgb},0.10); }
          50%       { box-shadow: 0 0 65px rgba(${colorRgb},0.40), 0 0 130px rgba(${colorRgb},0.18); }
        }
        @keyframes dhAlarm {
          0%, 100% { opacity: 1; transform: scale(1); }
          50%       { opacity: 0.7; transform: scale(1.08); }
        }
        .dh-modal-card {
          max-width: 560px;
          width: 100%;
          max-height: calc(100dvh - 24px);
          display: flex;
          flex-direction: column;
          background: linear-gradient(160deg, #0d1117 0%, #111827 100%);
          border: 1.5px solid rgba(${colorRgb},0.55);
          border-radius: 18px;
          overflow: hidden;
          box-sizing: border-box;
          font-family: 'Montserrat', system-ui, sans-serif;
          animation: dhPulse 3s ease-in-out infinite;
        }
        .dh-modal-header {
          flex-shrink: 0;
          padding: 16px 20px 14px 20px;
          border-bottom: 1px solid rgba(255,255,255,0.08);
          background: rgba(13, 17, 23, 0.96);
          display: flex;
          align-items: flex-start;
          justify-content: space-between;
          gap: 12px;
          box-sizing: border-box;
        }
        .dh-modal-body {
          flex: 1 1 auto;
          overflow-y: auto;
          -webkit-overflow-scrolling: touch;
          overscroll-behavior: contain;
          padding: 16px 20px;
          display: flex;
          flex-direction: column;
          gap: 14px;
          box-sizing: border-box;
          scrollbar-width: thin;
          scrollbar-color: rgba(${colorRgb},0.5) rgba(255,255,255,0.04);
        }
        .dh-modal-body::-webkit-scrollbar {
          width: 6px;
        }
        .dh-modal-body::-webkit-scrollbar-track {
          background: rgba(255,255,255,0.04);
        }
        .dh-modal-body::-webkit-scrollbar-thumb {
          background: rgba(${colorRgb},0.5);
          border-radius: 4px;
        }
        .dh-modal-footer {
          flex-shrink: 0;
          padding: 12px 20px;
          border-top: 1px solid rgba(255,255,255,0.08);
          background: rgba(13, 17, 23, 0.96);
          display: flex;
          justify-content: flex-end;
          box-sizing: border-box;
        }
        .dh-stats-grid {
          display: grid;
          grid-template-columns: repeat(5, 1fr);
          gap: 8px;
        }
        @media (max-width: 600px) {
          .dh-modal-card {
            max-height: calc(100dvh - 12px);
            border-radius: 16px;
          }
          .dh-modal-header {
            padding: 12px 14px 10px 14px;
          }
          .dh-modal-body {
            padding: 12px 14px;
            gap: 12px;
          }
          .dh-modal-footer {
            padding: 10px 14px;
          }
          .dh-stats-grid {
            gap: 5px;
          }
          .dh-header-title {
            font-size: 16px !important;
          }
          .dh-alarm-icon {
            font-size: 24px !important;
          }
          .dh-action-card {
            padding: 12px !important;
          }
        }
        @media (max-width: 380px) {
          .dh-stats-grid {
            gap: 4px;
          }
          .dh-header-title {
            font-size: 15px !important;
          }
        }
      `}</style>

      <div className="modal-card dh-modal-card">

        {/* ── Sticky Header ── */}
        <div className="dh-modal-header">
          <div style={{ display: 'flex', gap: '10px', alignItems: 'flex-start', flex: 1, minWidth: 0 }}>
            <div
              className="dh-alarm-icon"
              style={{
                fontSize: '28px',
                animation: 'dhAlarm 1.2s ease-in-out infinite',
                lineHeight: 1,
                flexShrink: 0,
                marginTop: '2px',
              }}
            >
              🚨
            </div>
            <div style={{ minWidth: 0 }}>
              <div style={{
                fontSize: '10px',
                fontWeight: 800,
                letterSpacing: '0.08em',
                textTransform: 'uppercase',
                color: partyColor,
                marginBottom: '2px',
              }}>
                DEFEAT HAZARD — EMERGENCY OPTIONS
              </div>
              <h2
                className="dh-header-title"
                style={{
                  margin: 0,
                  fontSize: '18px',
                  fontWeight: 900,
                  color: '#fff',
                  lineHeight: 1.2,
                  wordBreak: 'break-word',
                }}
              >
                {party.name} Is In Crisis
              </h2>
              <p style={{
                margin: '3px 0 0 0',
                fontSize: '11px',
                color: 'rgba(255,255,255,0.6)',
                lineHeight: 1.4,
              }}>
                Your party has breached one or more defeat thresholds. Act now before elimination.
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            aria-label="Close"
            style={{
              background: 'rgba(255,255,255,0.08)',
              border: '1px solid rgba(255,255,255,0.15)',
              color: '#fff',
              borderRadius: '50%',
              width: '32px',
              height: '32px',
              cursor: 'pointer',
              fontSize: '14px',
              flexShrink: 0,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              transition: 'background 0.15s',
            }}
            onMouseEnter={e => e.currentTarget.style.background = 'rgba(255,255,255,0.18)'}
            onMouseLeave={e => e.currentTarget.style.background = 'rgba(255,255,255,0.08)'}
          >
            ✕
          </button>
        </div>

        {/* ── Scrollable Body ── */}
        <div className="dh-modal-body">

          {/* Current Stats */}
          <div>
            <div style={{
              fontSize: '10px',
              fontWeight: 700,
              letterSpacing: '0.08em',
              textTransform: 'uppercase',
              color: 'rgba(255,255,255,0.45)',
              marginBottom: '6px',
            }}>
              Current Standing
            </div>
            <div className="dh-stats-grid">
              <StatPill label="Coins"      value={stats.coins}          danger={stats.coins <= 30} />
              <StatPill label="Morale"     value={stats.partyMorale}    danger={stats.partyMorale <= 20} />
              <StatPill label="Support"    value={stats.publicSupport}  unit="%" danger={stats.publicSupport <= 10} />
              <StatPill label="Corrupt"    value={stats.corruptionScore} unit="%" danger={stats.corruptionScore >= 75} />
              <StatPill label="Media"      value={stats.mediaImage} />
            </div>
          </div>

          {/* Defeat thresholds reference */}
          <div style={{
            background: 'rgba(220,38,38,0.08)',
            border: '1px solid rgba(220,38,38,0.28)',
            borderRadius: '10px',
            padding: '8px 12px',
            fontSize: '11px',
            color: '#fca5a5',
            lineHeight: 1.45,
          }}>
            ⚠️ <strong>Defeat thresholds:</strong> Coins ≤ 30 · Morale ≤ 20 · Public Support ≤ 10% · Corruption ≥ 75%
          </div>

          {/* Loan active banner */}
          {loanTaken && loanTurnsLeft > 0 && (
            <div style={{
              background: 'rgba(251,191,36,0.1)',
              border: '1px solid rgba(251,191,36,0.35)',
              borderRadius: '10px',
              padding: '10px 12px',
              fontSize: '12px',
              color: '#fde68a',
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              lineHeight: 1.4,
            }}>
              💳 Loan active — <strong>20 Coins/turn</strong> auto-deducted for <strong>{loanTurnsLeft}</strong> more turn{loanTurnsLeft !== 1 ? 's' : ''}.
            </div>
          )}

          {/* Action Cards */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            <ActionCard
              icon="💰"
              title="Emergency Campaign Loan"
              badge="ONCE PER GAME"
              description="Secure an emergency government loan of 150 Coins immediately. Repayments of 20 Coins are auto-deducted each turn for 10 turns."
              bullets={[
                'Instant: +150 Coins credited now',
                'Auto-repayment: −20 Coins × 10 turns',
                'Available only once per campaign',
                'Can only be taken while in Defeat Hazard',
              ]}
              cost="Cost: 0 upfront · Repay 200 Coins over 10 turns"
              done={loanTaken}
              disabled={loanTaken || !hasDefeatHazard}
              disabledReason={
                !hasDefeatHazard ? 'Only available during a Defeat Hazard phase.' :
                loanTaken ? 'Loan already taken this campaign.' : null
              }
              onClick={handleLoan}
              ctaLabel="📥 Take Emergency Loan"
            />

            <ActionCard
              icon="🏥"
              title="Recovery Pack"
              description="Deploy a comprehensive recovery package to stabilise your party's core metrics instantly. Funded from your current Coins (use the loan first if needed)."
              bullets={[
                '+20 Party Morale',
                '−20 Corruption Score',
                '+5 Public Support',
                '+20 Media Image',
              ]}
              cost="Cost: 80 Coins"
              disabled={!canBuyPack}
              disabledReason={
                !hasDefeatHazard ? 'Only available during a Defeat Hazard phase.' :
                stats.coins < 80 ? `Insufficient Coins — need 80, have ${stats.coins}. Take the loan first!` : null
              }
              onClick={handlePack}
              ctaLabel="🚑 Buy Recovery Pack (80 Coins)"
            />
          </div>

          {/* Feedback message */}
          {msg && (
            <div style={{
              padding: '10px 14px',
              borderRadius: '10px',
              background: msg.startsWith('✅') ? 'rgba(74,222,128,0.12)' : 'rgba(248,113,113,0.12)',
              border: `1px solid ${msg.startsWith('✅') ? 'rgba(74,222,128,0.35)' : 'rgba(248,113,113,0.35)'}`,
              color: msg.startsWith('✅') ? '#86efac' : '#fca5a5',
              fontSize: '12px',
              fontWeight: 600,
              lineHeight: 1.45,
            }}>
              {msg}
            </div>
          )}
        </div>

        {/* ── Sticky Footer ── */}
        <div className="dh-modal-footer">
          <button
            onClick={onClose}
            style={{
              padding: '9px 20px',
              minHeight: '38px',
              borderRadius: '9px',
              border: `1.5px solid rgba(${colorRgb},0.5)`,
              background: 'transparent',
              color: partyColor,
              fontWeight: 800,
              fontSize: '12px',
              letterSpacing: '0.04em',
              cursor: 'pointer',
              transition: 'all 0.18s',
              width: '100%',
              maxWidth: '240px',
            }}
            onMouseEnter={e => { e.currentTarget.style.background = `rgba(${colorRgb},0.15)`; }}
            onMouseLeave={e => { e.currentTarget.style.background = 'transparent'; }}
          >
            Close — I'll Deal with It
          </button>
        </div>

      </div>
    </div>
  );
}
