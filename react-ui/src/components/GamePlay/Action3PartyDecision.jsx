import React from 'react';

export default function Action3PartyDecision({
  turnData,
  selectedIssueOptionKey,
  setSelectedIssueOptionKey
}) {
  return (
    <div style={{ fontFamily: "system-ui, -apple-system, sans-serif" }}>
      <style>{`
        @keyframes pulse-live-dot {
          0% { opacity: 0.3; transform: scale(0.9); }
          50% { opacity: 1; transform: scale(1.1); }
          100% { opacity: 0.3; transform: scale(0.9); }
        }
        @keyframes scanline-flicker {
          0% { opacity: 0.98; }
          50% { opacity: 1; }
          100% { opacity: 0.98; }
        }
      `}</style>

      {turnData.turnNumber <= 2 && (
        <p style={{ margin: '0 0 15px 0', fontSize: '12px', color: '#64748b', fontStyle: 'italic' }}>
          Directive: Review internal party developments and issue executive policy responses.
        </p>
      )}

      {!turnData.currentIssue ? (
        /* Retro TV Standby screen for no active issues */
        <div style={{
          position: 'relative',
          borderRadius: '12px',
          overflow: 'hidden',
          border: '3px solid #475569',
          boxShadow: '0 4px 20px rgba(0, 0, 0, 0.15)',
          background: '#0f172a'
        }}>
          {/* Color Bars Container */}
          <div style={{ display: 'flex', width: '100%', height: '120px' }}>
            <div style={{ flex: 1, backgroundColor: '#e2e8f0' }} />
            <div style={{ flex: 1, backgroundColor: '#eab308' }} />
            <div style={{ flex: 1, backgroundColor: '#06b6d4' }} />
            <div style={{ flex: 1, backgroundColor: '#10b981' }} />
            <div style={{ flex: 1, backgroundColor: '#ec4899' }} />
            <div style={{ flex: 1, backgroundColor: '#ef4444' }} />
            <div style={{ flex: 1, backgroundColor: '#3b82f6' }} />
          </div>
          {/* Glassmorphic Overlay */}
          <div style={{
            position: 'absolute',
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            background: 'rgba(15, 23, 42, 0.85)',
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',
            alignItems: 'center',
            padding: '20px',
            textAlign: 'center'
          }}>
            <div style={{
              background: '#1e293b',
              border: '1px solid rgba(255, 255, 255, 0.15)',
              borderRadius: '6px',
              padding: '6px 14px',
              fontSize: '11px',
              fontWeight: '900',
              color: '#94a3b8',
              letterSpacing: '0.15em',
              textTransform: 'uppercase',
              marginBottom: '6px',
              boxShadow: '0 2px 8px rgba(0,0,0,0.3)'
            }}>
              📡 STANDBY
            </div>
            <div style={{ fontSize: '13px', fontWeight: 'bold', color: '#f1f5f9' }}>
              No Active Broadcasting Needed
            </div>
            <div style={{ fontSize: '11px', color: '#94a3b8', marginTop: '2px' }}>
              Routine communications operating on nominal channels.
            </div>
          </div>
        </div>
      ) : (
        /* High-tech TV Breaking News style container */
        <div style={{
          background: 'radial-gradient(circle at center, #1e1b4b 0%, #09090b 100%)',
          border: '3px solid var(--party-primary-color)',
          borderRadius: '12px',
          padding: '20px',
          color: '#f4f4f5',
          boxShadow: '0 10px 30px rgba(var(--party-primary-color-rgb), 0.15)',
          position: 'relative',
          overflow: 'hidden',
          animation: 'scanline-flicker 0.15s infinite'
        }}>
          {/* Subtle Scanline Overlay */}
          <div style={{
            position: 'absolute',
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            backgroundImage: 'linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.15) 50%)',
            backgroundSize: '100% 4px',
            pointerEvents: 'none',
            zIndex: 1
          }} />

          {/* TV Header Bar */}
          <div style={{
            background: 'var(--party-primary-color)',
            color: '#ffffff',
            padding: '6px 14px',
            borderRadius: '6px',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            marginBottom: '15px',
            fontSize: '11px',
            fontWeight: '900',
            letterSpacing: '0.08em',
            textTransform: 'uppercase',
            position: 'relative',
            zIndex: 2
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <span style={{ 
                width: '8px', 
                height: '8px', 
                borderRadius: '50%', 
                backgroundColor: '#ffffff', 
                display: 'inline-block',
                animation: 'pulse-live-dot 1.2s infinite'
              }} />
              <span>📺 INTERNAL REPORT</span>
            </div>
            <span style={{ 
              background: '#ffffff', 
              color: 'var(--party-primary-color)', 
              fontSize: '9px', 
              padding: '1px 6px', 
              borderRadius: '3px',
              fontWeight: '900'
            }}>
              LIVE FEED
            </span>
          </div>

          {/* Headline Display */}
          <div style={{ position: 'relative', zIndex: 2 }}>
            <h3 style={{
              margin: '0 0 12px 0',
              fontSize: '18px',
              fontWeight: '800',
              lineHeight: 1.4,
              color: '#fef08a', // bright yellow
              textShadow: '0 2px 4px rgba(0,0,0,0.5)',
              fontFamily: "Impact, system-ui, sans-serif"
            }}>
              🚨 URGENT: {turnData.currentIssue.title.toUpperCase()}
            </h3>

            {/* Anchored Transcript Box */}
            <div style={{
              background: 'rgba(9, 9, 11, 0.6)',
              borderLeft: '4px solid #3b82f6',
              padding: '12px 16px',
              borderRadius: '0 6px 6px 0',
              fontSize: '13px',
              lineHeight: 1.6,
              color: '#e4e4e7',
              marginBottom: '20px',
              boxShadow: 'inset 0 2px 4px rgba(0,0,0,0.5)'
            }}>
              <strong style={{ color: '#60a5fa', textTransform: 'uppercase', fontSize: '11px', display: 'block', marginBottom: '4px' }}>
                🎙️ BRIEFING DESK:
              </strong>
              {turnData.currentIssue.description}
            </div>

            {/* Resolution Selector Title */}
            <h4 style={{
              margin: '0 0 8px 0',
              fontSize: '10px',
              textTransform: 'uppercase',
              letterSpacing: '0.06em',
              color: '#a1a1aa',
              fontWeight: 800
            }}>
              📡 SELECT EXECUTIVE ACTION:
            </h4>

            {/* Options list */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              {turnData.currentIssue.options.map((opt, i) => {
                const isSelected = selectedIssueOptionKey === opt.optionKey;
                return (
                  <button
                    key={opt.optionKey}
                    onClick={() => setSelectedIssueOptionKey(opt.optionKey)}
                    style={{
                      textAlign: 'left',
                      padding: '12px 16px',
                      borderRadius: '8px',
                      fontSize: '12.5px',
                      lineHeight: '1.4',
                      background: isSelected 
                        ? 'var(--party-primary-color)' 
                        : 'linear-gradient(180deg, #1f2937 0%, #111827 100%)',
                      color: '#ffffff',
                      border: isSelected ? '1px solid var(--party-primary-color)' : '1px solid rgba(255, 255, 255, 0.12)',
                      boxShadow: isSelected ? '0 4px 15px rgba(var(--party-primary-color-rgb), 0.3)' : 'none',
                      fontWeight: isSelected ? '700' : 'normal',
                      transition: 'all 0.15s ease',
                      cursor: 'pointer',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '10px'
                    }}
                    onMouseEnter={(e) => {
                      if (!isSelected) {
                        e.currentTarget.style.background = 'linear-gradient(180deg, #374151 0%, #1f2937 100%)';
                        e.currentTarget.style.borderColor = 'rgba(255, 255, 255, 0.3)';
                      }
                    }}
                    onMouseLeave={(e) => {
                      if (!isSelected) {
                        e.currentTarget.style.background = 'linear-gradient(180deg, #1f2937 0%, #111827 100%)';
                        e.currentTarget.style.borderColor = 'rgba(255, 255, 255, 0.12)';
                      }
                    }}
                  >
                    <span style={{ 
                      display: 'inline-flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      width: '20px',
                      height: '20px',
                      borderRadius: '50%',
                      background: isSelected ? '#ffffff' : 'rgba(255,255,255,0.1)',
                      color: isSelected ? 'var(--party-primary-color)' : '#ffffff',
                      fontSize: '10px',
                      fontWeight: '900'
                    }}>
                      {isSelected ? '✓' : i + 1}
                    </span>
                    <span style={{ flex: 1 }}>{opt.text}</span>
                  </button>
                );
              })}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
