import React from 'react';

const HEXES = [
  { key: 'card',        icon: '🃏', label: 'Card',   tab: 'politics' },
  { key: 'news',        icon: '📰', label: 'News',   tab: 'politics' },
  { key: 'assembly',    icon: '🏛️', label: 'Vote',   tab: 'politics' },
  { key: 'governance',  icon: '⚖️', label: 'Govt',   tab: 'governance' },
  { key: 'cooperation', icon: '🤝', label: 'Coop',   tab: 'governance' },
  { key: 'bid',         icon: '💰', label: 'Bid',    tab: 'economy' },
  { key: 'reward',      icon: '🎁', label: 'Reward', tab: 'economy' },
];

/**
 * WR_HexTracker — High contrast, crystal-clear 7 hexagonal action progress indicators
 * Props: { doneMap: { card, news, assembly, governance, cooperation, bid, reward }, doneCount, onHexClick(tabId) }
 */
export default function WR_HexTracker({ doneMap = {}, doneCount = 0, onHexClick }) {
  return (
    <div style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      padding: '14px 14px',
      background: 'linear-gradient(180deg, #1E293B 0%, #151D2A 100%)',
      borderRadius: '14px',
      border: '1px solid rgba(255,255,255,0.15)',
      marginBottom: '14px',
      boxShadow: '0 4px 14px rgba(0,0,0,0.25)',
      gap: '4px',
    }}>
      {HEXES.map((hex, i) => {
        const done = !!doneMap[hex.key];
        return (
          <React.Fragment key={hex.key}>
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '4px' }}>
              <button
                onClick={() => onHexClick(hex.tab)}
                title={hex.label}
                style={{
                  width: '40px',
                  height: '44px',
                  clipPath: 'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  cursor: 'pointer',
                  background: done
                    ? 'linear-gradient(145deg, #F59E0B, #D97706)'
                    : 'linear-gradient(145deg, #334155, #1E293B)',
                  border: 'none',
                  boxShadow: done
                    ? '0 0 14px rgba(245, 158, 11, 0.75)'
                    : '0 2px 8px rgba(0, 0, 0, 0.4)',
                  animation: done ? 'wr-gold-fill 0.3s ease' : 'none',
                  transition: 'all 0.2s ease',
                  touchAction: 'manipulation',
                  WebkitTapHighlightColor: 'transparent',
                  padding: 0,
                  borderRadius: 0,
                  minHeight: 'unset',
                  minWidth: 'unset',
                  fontSize: '17px',
                  lineHeight: 1,
                  filter: done ? 'drop-shadow(0 2px 4px rgba(0,0,0,0.3))' : 'none'
                }}
              >
                {hex.icon}
              </button>
              <span style={{
                fontSize: '9px',
                fontWeight: 800,
                color: done ? '#FDE68A' : '#94A3B8',
                letterSpacing: '0.02em',
                textTransform: 'uppercase',
                lineHeight: 1
              }}>
                {hex.label}
              </span>
            </div>

            {/* Connector line between hexes */}
            {i < HEXES.length - 1 && (
              <div style={{
                flex: 1,
                height: done ? '3px' : '2px',
                background: done ? '#F59E0B' : 'rgba(255, 255, 255, 0.2)',
                borderRadius: '1px',
                minWidth: '3px',
                maxWidth: '12px',
                marginBottom: '14px',
                boxShadow: done ? '0 0 6px rgba(245, 158, 11, 0.6)' : 'none',
                transition: 'all 0.3s ease',
              }} />
            )}
          </React.Fragment>
        );
      })}

      {/* Done count badge */}
      <div style={{
        marginLeft: '6px',
        marginBottom: '14px',
        padding: '3px 8px',
        borderRadius: '12px',
        background: doneCount === 7 ? 'rgba(74, 222, 128, 0.2)' : 'rgba(255,255,255,0.1)',
        border: `1.5px solid ${doneCount === 7 ? '#4ADE80' : 'rgba(255,255,255,0.25)'}`,
        fontSize: '11px',
        fontWeight: 900,
        color: doneCount === 7 ? '#4ADE80' : '#FDE68A',
        whiteSpace: 'nowrap',
        flexShrink: 0,
        boxShadow: doneCount === 7 ? '0 0 10px rgba(74,222,128,0.4)' : 'none'
      }}>
        {doneCount}/7
      </div>
    </div>
  );
}
