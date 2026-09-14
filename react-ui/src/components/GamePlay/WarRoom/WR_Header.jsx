import React from 'react';

/**
 * WR_Header — Campaign War Room top banner
 * Props: { turnData, activeParty, handleSkipTurn, loading, isMyTurn }
 */
export default function WR_Header({ turnData, activeParty, handleSkipTurn, loading, isMyTurn }) {
  const partyColor = getComputedStyle(document.documentElement)
    .getPropertyValue('--party-primary-color').trim() || '#6C3AB5';

  const turnProgress = Math.min(100, Math.round(((turnData?.turnNumber || 1) / 60) * 100));

  return (
    <div style={{
      background: 'linear-gradient(135deg, #1a0533 0%, #0D1117 70%)',
      padding: '12px 16px 10px',
      display: 'flex',
      flexDirection: 'column',
      gap: '8px',
      borderBottom: '1px solid rgba(255,255,255,0.06)',
    }}>
      {/* Row 1: Avatar + Title + Skip */}
      <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
        {/* Party avatar */}
        <div style={{
          width: '42px',
          height: '42px',
          borderRadius: '50%',
          background: 'var(--party-primary-color, #6C3AB5)',
          border: '2.5px solid var(--party-primary-color, #9B5DE5)',
          boxShadow: '0 0 12px var(--party-primary-color, rgba(108,58,181,0.5))',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          flexShrink: 0,
          fontSize: '18px',
          fontWeight: 900,
          color: '#ffffff',
        }}>
          {(activeParty?.name || '?')[0]?.toUpperCase()}
        </div>

        {/* Title block */}
        <div style={{ flex: 1, minWidth: 0 }}>
          <div style={{
            fontSize: '15px',
            fontWeight: 900,
            letterSpacing: '0.07em',
            textTransform: 'uppercase',
            color: '#E6EDF3',
            lineHeight: 1.2,
          }}>
            ⚔️ Campaign War Room
          </div>
          {activeParty?.name && (
            <div style={{ fontSize: '10px', color: '#7D8590', fontWeight: 700, letterSpacing: '0.05em', marginTop: '2px' }}>
              PLAYING AS: <span style={{ color: 'var(--party-primary-color, #9B5DE5)' }}>{activeParty.name.toUpperCase()}</span>
            </div>
          )}
        </div>

        {/* Skip button */}
        <button
          onClick={handleSkipTurn}
          disabled={loading || !isMyTurn}
          className="btn-danger"
          style={{
            cursor: (isMyTurn && !loading) ? 'pointer' : 'not-allowed',
            opacity: (!isMyTurn || loading) ? 0.45 : 1,
            flexShrink: 0,
            fontSize: '12px',
            padding: '8px 14px',
            minHeight: '36px',
          }}
        >
          ⏭️ SKIP
        </button>
      </div>

      {/* Row 2: Month progress bar */}
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '0 2px' }}>
        <span style={{
          fontSize: '10px',
          fontWeight: 800,
          color: '#7D8590',
          whiteSpace: 'nowrap',
          letterSpacing: '0.05em',
        }}>
          MONTH {turnData?.turnNumber || '—'}
        </span>

        <div style={{
          flex: 1,
          height: '4px',
          background: 'rgba(255,255,255,0.08)',
          borderRadius: '2px',
          overflow: 'hidden',
        }}>
          <div style={{
            height: '100%',
            width: `${turnProgress}%`,
            background: 'linear-gradient(90deg, #6C3AB5, #9B5DE5)',
            borderRadius: '2px',
            transition: 'width 0.5s ease',
          }} />
        </div>

        <span style={{
          fontSize: '10px',
          fontWeight: 800,
          color: '#7D8590',
          whiteSpace: 'nowrap',
          letterSpacing: '0.05em',
        }}>
          60
        </span>
      </div>
    </div>
  );
}
