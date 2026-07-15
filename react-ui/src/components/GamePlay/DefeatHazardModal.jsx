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
      background: danger ? 'rgba(220,38,38,0.15)' : 'rgba(255,255,255,0.07)',
      border: `1px solid ${danger ? 'rgba(220,38,38,0.5)' : 'rgba(255,255,255,0.12)'}`,
      borderRadius: '10px',
      padding: '10px 14px',
      minWidth: '80px',
    }}>
      <span style={{ fontSize: '18px', fontWeight: 900, color: danger ? '#f87171' : '#fff' }}>
        {value}{unit}
      </span>
      <span style={{ fontSize: '11px', color: 'rgba(255,255,255,0.6)', marginTop: '3px', fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
        {label}
      </span>
    </div>
  );

  // ── action card helper ─────────────────────────────────────────────────────
  const ActionCard = ({ icon, title, badge, description, bullets, cost, disabled, disabledReason, onClick, ctaLabel, done }) => (
    <div style={{
      background: 'rgba(255,255,255,0.05)',
      border: `1.5px solid ${done ? 'rgba(74,222,128,0.4)' : disabled ? 'rgba(255,255,255,0.08)' : `rgba(${colorRgb}, 0.5)`}`,
      borderRadius: '16px',
      padding: '20px',
      display: 'flex',
      flexDirection: 'column',
      gap: '12px',
      opacity: disabled ? 0.6 : 1,
      transition: 'all 0.2s ease',
      position: 'relative',
      overflow: 'hidden',
    }}>
      {done && (
        <div style={{ position: 'absolute', top: '12px', right: '14px', background: 'rgba(74,222,128,0.2)', border: '1px solid rgba(74,222,128,0.5)', borderRadius: '8px', padding: '3px 10px', fontSize: '11px', fontWeight: 700, color: '#4ade80', letterSpacing: '0.06em' }}>
          ✓ USED
        </div>
      )}
      {badge && !done && (
        <div style={{ position: 'absolute', top: '12px', right: '14px', background: `rgba(${colorRgb},0.25)`, border: `1px solid rgba(${colorRgb},0.5)`, borderRadius: '8px', padding: '3px 10px', fontSize: '11px', fontWeight: 700, color: partyColor, letterSpacing: '0.06em' }}>
          {badge}
        </div>
      )}
      <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
        <span style={{ fontSize: '28px' }}>{icon}</span>
        <div>
          <div style={{ fontSize: '15px', fontWeight: 800, color: '#fff', letterSpacing: '0.02em' }}>{title}</div>
          {cost && <div style={{ fontSize: '12px', color: partyColor, fontWeight: 700, marginTop: '2px' }}>{cost}</div>}
        </div>
      </div>

      <p style={{ margin: 0, fontSize: '13px', color: 'rgba(255,255,255,0.75)', lineHeight: 1.55 }}>{description}</p>

      {bullets && (
        <ul style={{ margin: '0', paddingLeft: '18px', display: 'flex', flexDirection: 'column', gap: '4px' }}>
          {bullets.map((b, i) => (
            <li key={i} style={{ fontSize: '12px', color: 'rgba(255,255,255,0.7)', lineHeight: 1.4 }}>{b}</li>
          ))}
        </ul>
      )}

      {disabledReason && (
        <div style={{ fontSize: '12px', color: '#fb923c', fontWeight: 600, background: 'rgba(251,146,60,0.1)', borderRadius: '8px', padding: '6px 10px', border: '1px solid rgba(251,146,60,0.25)' }}>
          ⚠️ {disabledReason}
        </div>
      )}

      {!done && (
        <button
          disabled={disabled || busy}
          onClick={onClick}
          style={{
            marginTop: '4px',
            padding: '11px 20px',
            borderRadius: '10px',
            border: 'none',
            cursor: disabled || busy ? 'not-allowed' : 'pointer',
            fontWeight: 800,
            fontSize: '13px',
            letterSpacing: '0.05em',
            textTransform: 'uppercase',
            background: disabled ? 'rgba(255,255,255,0.1)' : `rgba(${colorRgb},1)`,
            color: '#fff',
            transition: 'all 0.18s ease',
            boxShadow: disabled ? 'none' : `0 4px 16px rgba(${colorRgb},0.4)`,
          }}
          onMouseEnter={e => { if (!disabled && !busy) e.currentTarget.style.transform = 'translateY(-2px)'; }}
          onMouseLeave={e => { e.currentTarget.style.transform = 'translateY(0)'; }}
        >
          {busy ? '⏳ Processing…' : ctaLabel}
        </button>
      )}
    </div>
  );

  return (
    <div style={{
      position: 'fixed',
      inset: 0,
      backgroundColor: 'rgba(0,0,0,0.88)',
      backdropFilter: 'blur(6px)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      zIndex: 9999,
      padding: '20px',
    }}>
      {/* Animated glow bg */}
      <style>{`
        @keyframes dhPulse {
          0%, 100% { box-shadow: 0 0 60px rgba(${colorRgb},0.25), 0 0 120px rgba(${colorRgb},0.10); }
          50%       { box-shadow: 0 0 80px rgba(${colorRgb},0.40), 0 0 160px rgba(${colorRgb},0.18); }
        }
        @keyframes dhAlarm {
          0%, 100% { opacity: 1; }
          50%       { opacity: 0.65; }
        }
      `}</style>

      <div style={{
        width: '100%',
        maxWidth: '620px',
        maxHeight: '90vh',
        overflowY: 'auto',
        background: 'linear-gradient(160deg, #0d1117 0%, #111827 100%)',
        border: `2px solid rgba(${colorRgb},0.55)`,
        borderRadius: '24px',
        padding: '32px',
        fontFamily: "'Montserrat', sans-serif",
        animation: 'dhPulse 3s ease-in-out infinite',
        scrollbarWidth: 'thin',
        scrollbarColor: `rgba(${colorRgb},0.4) transparent`,
      }}>

        {/* ── Header ── */}
        <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', marginBottom: '24px' }}>
          <div style={{ display: 'flex', gap: '14px', alignItems: 'center' }}>
            <div style={{
              fontSize: '36px',
              animation: 'dhAlarm 1.2s ease-in-out infinite',
              lineHeight: 1,
            }}>🚨</div>
            <div>
              <div style={{ fontSize: '11px', fontWeight: 800, letterSpacing: '0.12em', textTransform: 'uppercase', color: partyColor, marginBottom: '4px' }}>
                DEFEAT HAZARD — EMERGENCY OPTIONS
              </div>
              <h2 style={{ margin: 0, fontSize: '22px', fontWeight: 900, color: '#fff', lineHeight: 1.2 }}>
                {party.name} Is In Crisis
              </h2>
              <p style={{ margin: '6px 0 0 0', fontSize: '12px', color: 'rgba(255,255,255,0.55)', lineHeight: 1.5 }}>
                Your party has breached one or more defeat thresholds. Act now before elimination.
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            style={{
              background: 'rgba(255,255,255,0.07)',
              border: '1px solid rgba(255,255,255,0.14)',
              color: '#fff',
              borderRadius: '50%',
              width: '36px',
              height: '36px',
              cursor: 'pointer',
              fontSize: '16px',
              flexShrink: 0,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              transition: 'background 0.15s',
            }}
            onMouseEnter={e => e.currentTarget.style.background = 'rgba(255,255,255,0.14)'}
            onMouseLeave={e => e.currentTarget.style.background = 'rgba(255,255,255,0.07)'}
          >✕</button>
        </div>

        {/* ── Current Stats ── */}
        <div style={{ marginBottom: '24px' }}>
          <div style={{ fontSize: '11px', fontWeight: 700, letterSpacing: '0.1em', textTransform: 'uppercase', color: 'rgba(255,255,255,0.4)', marginBottom: '10px' }}>
            Current Standing
          </div>
          <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
            <StatPill label="Coins"      value={stats.coins}          danger={stats.coins <= 30} />
            <StatPill label="Morale"     value={stats.partyMorale}    danger={stats.partyMorale <= 20} />
            <StatPill label="Support"    value={stats.publicSupport}  unit="%" danger={stats.publicSupport <= 10} />
            <StatPill label="Corruption" value={stats.corruptionScore} unit="%" danger={stats.corruptionScore >= 75} />
            <StatPill label="Media"      value={stats.mediaImage} />
          </div>
        </div>

        {/* ── Defeat thresholds reference ── */}
        <div style={{
          background: 'rgba(220,38,38,0.08)',
          border: '1px solid rgba(220,38,38,0.3)',
          borderRadius: '12px',
          padding: '12px 16px',
          marginBottom: '24px',
          fontSize: '12px',
          color: '#fca5a5',
          lineHeight: 1.6,
        }}>
          ⚠️ <strong>Defeat thresholds:</strong> Coins ≤ 30 &nbsp;|&nbsp; Morale ≤ 20 &nbsp;|&nbsp; Public Support ≤ 10% &nbsp;|&nbsp; Corruption ≥ 75%
        </div>

        {/* ── Loan active banner ── */}
        {loanTaken && loanTurnsLeft > 0 && (
          <div style={{
            background: 'rgba(251,191,36,0.1)',
            border: '1px solid rgba(251,191,36,0.35)',
            borderRadius: '12px',
            padding: '12px 16px',
            marginBottom: '20px',
            fontSize: '13px',
            color: '#fde68a',
            display: 'flex',
            alignItems: 'center',
            gap: '8px',
          }}>
            💳 Loan active — <strong>20 Coins/turn</strong> auto-deducted for <strong>{loanTurnsLeft}</strong> more turn{loanTurnsLeft !== 1 ? 's' : ''}.
          </div>
        )}

        {/* ── Action Cards ── */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '16px', marginBottom: '24px' }}>

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

        {/* ── Feedback message ── */}
        {msg && (
          <div style={{
            padding: '14px 18px',
            borderRadius: '12px',
            background: msg.startsWith('✅') ? 'rgba(74,222,128,0.1)' : 'rgba(248,113,113,0.1)',
            border: `1px solid ${msg.startsWith('✅') ? 'rgba(74,222,128,0.35)' : 'rgba(248,113,113,0.35)'}`,
            color: msg.startsWith('✅') ? '#86efac' : '#fca5a5',
            fontSize: '13px',
            fontWeight: 600,
            lineHeight: 1.5,
            marginBottom: '16px',
          }}>
            {msg}
          </div>
        )}

        {/* ── Footer ── */}
        <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
          <button
            onClick={onClose}
            style={{
              padding: '11px 28px',
              borderRadius: '10px',
              border: `1.5px solid rgba(${colorRgb},0.5)`,
              background: 'transparent',
              color: partyColor,
              fontWeight: 800,
              fontSize: '13px',
              letterSpacing: '0.05em',
              cursor: 'pointer',
              transition: 'all 0.18s',
            }}
            onMouseEnter={e => { e.currentTarget.style.background = `rgba(${colorRgb},0.12)`; }}
            onMouseLeave={e => { e.currentTarget.style.background = 'transparent'; }}
          >
            Close — I'll Deal with It
          </button>
        </div>
      </div>
    </div>
  );
}
