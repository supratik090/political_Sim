import React from 'react';

/**
 * WR_Header — Campaign War Room top banner
 * Props: { turnData, activeParty, handleSkipTurn, loading, isMyTurn }
 */
export default function WR_Header({ turnData, activeParty, handleSkipTurn, loading, isMyTurn, onOpenGuide, liveDeltas }) {
  const partyColor = getComputedStyle(document.documentElement)
    .getPropertyValue('--party-primary-color').trim() || '#6C3AB5';

  const turnProgress = Math.min(100, Math.round(((turnData?.turnNumber || 1) / 60) * 100));

  return (
    <div className="wr-header-guide" style={{
      background: 'linear-gradient(135deg, #2D1558 0%, #151D2A 100%)',
      padding: '14px 16px',
      display: 'flex',
      flexDirection: 'column',
      gap: '10px',
      borderRadius: '14px',
      border: '1px solid rgba(255,255,255,0.15)',
      marginBottom: '14px',
      boxShadow: '0 4px 14px rgba(0,0,0,0.25)'
    }}>
      {/* Row 1: Avatar + Title + Guide Button */}
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

        {/* 🎯 Quick Guide button */}
        {onOpenGuide && (
          <button
            onClick={onOpenGuide}
            className="wr-guide-btn"
            title="How to Play Spotlight Guide"
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '6px',
              background: 'linear-gradient(135deg, rgba(245,158,11,0.2) 0%, rgba(217,119,6,0.3) 100%)',
              border: '1.5px solid #F59E0B',
              borderRadius: '20px',
              padding: '6px 12px',
              color: '#FCD34D',
              fontSize: '12px',
              fontWeight: 800,
              cursor: 'pointer',
              boxShadow: '0 0 12px rgba(245,158,11,0.25)',
              transition: 'all 0.2s ease',
              whiteSpace: 'nowrap',
              fontFamily: 'Montserrat, system-ui, sans-serif',
              flexShrink: 0,
            }}
            onMouseEnter={e => {
              e.currentTarget.style.background = 'linear-gradient(135deg, rgba(245,158,11,0.35) 0%, rgba(217,119,6,0.45) 100%)';
              e.currentTarget.style.boxShadow = '0 0 16px rgba(245,158,11,0.5)';
            }}
            onMouseLeave={e => {
              e.currentTarget.style.background = 'linear-gradient(135deg, rgba(245,158,11,0.2) 0%, rgba(217,119,6,0.3) 100%)';
              e.currentTarget.style.boxShadow = '0 0 12px rgba(245,158,11,0.25)';
            }}
          >
            <span style={{ fontSize: '14px' }}>🎯</span> Guide
          </button>
        )}
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

      {/* Row 3: Live Projected Shifts HUD */}
      {liveDeltas && (liveDeltas.coins !== 0 || liveDeltas.morale !== 0 || liveDeltas.support !== 0 || liveDeltas.media !== 0 || liveDeltas.corruption !== 0) && (
        <div style={{
          display: 'flex',
          alignItems: 'center',
          flexWrap: 'wrap',
          gap: '6px 12px',
          background: 'rgba(0,0,0,0.35)',
          border: '1px solid rgba(255,255,255,0.1)',
          borderRadius: '8px',
          padding: '6px 10px',
          marginTop: '2px',
          animation: 'wr-fill-in 0.2s ease',
        }}>
          <span style={{ fontSize: '10px', fontWeight: 900, color: '#F59E0B', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
            ⚡ Live Projected Shift:
          </span>
          {liveDeltas.coins !== 0 && (
            <span style={{ fontSize: '11px', fontWeight: 800, color: liveDeltas.coins > 0 ? '#4ADE80' : '#FCD34D' }}>
              💰 {liveDeltas.coins > 0 ? `+₹${liveDeltas.coins}L` : `-₹${Math.abs(liveDeltas.coins)}L`}
            </span>
          )}
          {liveDeltas.morale !== 0 && (
            <span style={{ fontSize: '11px', fontWeight: 800, color: liveDeltas.morale > 0 ? '#4ADE80' : '#F87171' }}>
              ✊ {liveDeltas.morale > 0 ? `+${liveDeltas.morale}` : liveDeltas.morale}
            </span>
          )}
          {liveDeltas.media !== 0 && (
            <span style={{ fontSize: '11px', fontWeight: 800, color: liveDeltas.media > 0 ? '#4ADE80' : '#F87171' }}>
              📢 {liveDeltas.media > 0 ? `+${liveDeltas.media}` : liveDeltas.media}
            </span>
          )}
          {liveDeltas.support !== 0 && (
            <span style={{ fontSize: '11px', fontWeight: 800, color: liveDeltas.support > 0 ? '#4ADE80' : '#F87171' }}>
              📈 {liveDeltas.support > 0 ? `+${liveDeltas.support}%` : `${liveDeltas.support}%`}
            </span>
          )}
          {liveDeltas.corruption !== 0 && (
            <span style={{ fontSize: '11px', fontWeight: 800, color: liveDeltas.corruption < 0 ? '#4ADE80' : '#F87171' }}>
              ⚖️ {liveDeltas.corruption > 0 ? `+${liveDeltas.corruption}%` : `${liveDeltas.corruption}%`}
            </span>
          )}
        </div>
      )}
    </div>
  );
}
