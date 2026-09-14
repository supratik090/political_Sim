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
 * WR_HexTracker — 7 hexagonal action progress indicators
 * Props: { doneMap: { card, news, assembly, governance, cooperation, bid, reward }, onHexClick(tabId) }
 */
export default function WR_HexTracker({ doneMap = {}, doneCount = 0, onHexClick }) {
  return (
    <div style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      padding: '10px 16px 8px',
      background: '#0D1117',
      borderBottom: '1px solid rgba(255,255,255,0.06)',
      gap: '4px',
    }}>
      {HEXES.map((hex, i) => {
        const done = !!doneMap[hex.key];
        return (
          <React.Fragment key={hex.key}>
            <button
              onClick={() => onHexClick(hex.tab)}
              title={hex.label}
              style={{
                width: '38px',
                height: '44px',
                clipPath: 'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                cursor: 'pointer',
                background: done
                  ? 'linear-gradient(145deg, #D97706, #F59E0B)'
                  : 'rgba(255,255,255,0.06)',
                border: 'none',
                boxShadow: done ? '0 0 10px rgba(245,158,11,0.45)' : 'none',
                animation: done ? 'wr-gold-fill 0.3s ease' : 'wr-pending-pulse 1.6s ease-in-out infinite',
                transition: 'all 0.2s ease',
                touchAction: 'manipulation',
                WebkitTapHighlightColor: 'transparent',
                padding: 0,
                borderRadius: 0,
                minHeight: 'unset',
                overflow: 'visible',
                // override global button styles
                minWidth: 'unset',
                fontSize: '15px',
                lineHeight: 1,
              }}
            >
              {hex.icon}
            </button>

            {/* Connector line between hexes */}
            {i < HEXES.length - 1 && (
              <div style={{
                flex: 1,
                height: '2px',
                background: done ? 'rgba(245,158,11,0.4)' : 'rgba(255,255,255,0.07)',
                borderRadius: '1px',
                minWidth: '4px',
                maxWidth: '16px',
                transition: 'background 0.3s ease',
              }} />
            )}
          </React.Fragment>
        );
      })}

      {/* Done count badge */}
      <div style={{
        marginLeft: '6px',
        fontSize: '11px',
        fontWeight: 800,
        color: doneCount === 7 ? '#4ADE80' : '#7D8590',
        whiteSpace: 'nowrap',
        flexShrink: 0,
      }}>
        {doneCount}/7
      </div>
    </div>
  );
}
