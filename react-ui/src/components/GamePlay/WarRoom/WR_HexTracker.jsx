import React from 'react';

const HEXES = [
  { key: 'card',        icon: '🃏', label: 'Card',   tab: 'politics' },
  { key: 'news',        icon: '📰', label: 'News',   tab: 'politics' },
  { key: 'assembly',    icon: '🏛️', label: 'Vote',   tab: 'politics' },
  { key: 'governance',  icon: '⚖️', label: 'Govt',   tab: 'governance' },
  { key: 'cooperation', icon: '🤝', label: 'Coop',   tab: 'governance' },
  { key: 'bid',         icon: '💰', label: 'Bid',    tab: 'economy' },
  { key: 'reward',      icon: '🎁', label: 'Reward', tab: 'economy' },
  { key: 'building',    icon: '🏗️', label: 'Build',  tab: 'economy' },
];

/**
 * WR_HexTracker — 8 hexagonal action progress indicators with Active / Done / Pending states
 *
 * Visual states:
 *   Active  → Cyan pulsing glow, brighter interior, blue dot badge
 *   Done    → Gold gradient fill, green ✓ checkmark badge
 *   Pending → Dark slate, dimmed opacity
 *
 * Props: { doneMap, activeHex, onHexClick(hexKey) }
 */
export default function WR_HexTracker({ doneMap = {}, activeHex = 'card', onHexClick }) {
  const hexDoneCount = HEXES.filter(h => !!doneMap[h.key]).length;
  const totalHexes = HEXES.length;

  return (
    <div style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      padding: '12px 10px',
      background: 'linear-gradient(180deg, #1E293B 0%, #151D2A 100%)',
      borderRadius: '14px',
      border: '1px solid rgba(255,255,255,0.15)',
      marginBottom: '14px',
      boxShadow: '0 4px 14px rgba(0,0,0,0.25)',
      gap: '2px',
    }}>
      {HEXES.map((hex, i) => {
        const done = !!doneMap[hex.key];
        const active = activeHex === hex.key;
        const pending = !done && !active;

        /* ── Hex button visual properties ── */
        let hexBg, hexAnimation, hexFilter, hexOpacity;

        if (done) {
          hexBg = 'linear-gradient(145deg, #F59E0B, #D97706)';
          hexAnimation = 'wr-gold-fill 0.3s ease';
          hexFilter = 'drop-shadow(0 0 8px rgba(245, 158, 11, 0.7))';
          hexOpacity = 1;
        } else if (active) {
          hexBg = 'linear-gradient(145deg, #475569, #334155)';
          hexAnimation = 'wr-hex-active-pulse 1.5s ease-in-out infinite';
          hexFilter = 'drop-shadow(0 0 6px rgba(56, 189, 248, 0.65))';
          hexOpacity = 1;
        } else {
          // pending
          hexBg = 'linear-gradient(145deg, #334155, #1E293B)';
          hexAnimation = 'none';
          hexFilter = 'none';
          hexOpacity = 0.4;
        }

        const labelColor = done ? '#FDE68A' : active ? '#38BDF8' : '#64748B';
        const labelWeight = active ? 900 : 800;

        /* ── Connector line visual ── */
        const connectorGold = done;
        const connectorCyan = active;

        return (
          <React.Fragment key={hex.key}>
            <div style={{
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              gap: '3px',
              position: 'relative',
            }}>
              {/* Hex button */}
              <button
                onClick={() => onHexClick(hex.key)}
                title={`${hex.label}${done ? ' ✓ Done' : active ? ' ● Active' : ' – Pending'}`}
                style={{
                  width: '36px',
                  height: '40px',
                  clipPath: 'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  cursor: 'pointer',
                  background: hexBg,
                  border: 'none',
                  animation: hexAnimation,
                  filter: hexFilter,
                  opacity: hexOpacity,
                  transition: 'opacity 0.3s ease, background 0.3s ease',
                  touchAction: 'manipulation',
                  WebkitTapHighlightColor: 'transparent',
                  padding: 0,
                  borderRadius: 0,
                  minHeight: 'unset',
                  minWidth: 'unset',
                  fontSize: '15px',
                  lineHeight: 1,
                }}
              >
                {hex.icon}
              </button>

              {/* Done checkmark badge (green circle with ✓) */}
              {done && (
                <div style={{
                  position: 'absolute',
                  top: '-3px',
                  right: '-4px',
                  width: '15px',
                  height: '15px',
                  borderRadius: '50%',
                  background: '#16A34A',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontSize: '8px',
                  fontWeight: 900,
                  color: '#ffffff',
                  border: '2px solid #151D2A',
                  zIndex: 2,
                  boxShadow: '0 0 6px rgba(22, 163, 74, 0.5)',
                }}>
                  ✓
                </div>
              )}

              {/* Active indicator dot (pulsing cyan dot) */}
              {active && !done && (
                <div style={{
                  position: 'absolute',
                  top: '-2px',
                  right: '-3px',
                  width: '10px',
                  height: '10px',
                  borderRadius: '50%',
                  background: '#38BDF8',
                  border: '2px solid #151D2A',
                  zIndex: 2,
                  animation: 'wr-pending-pulse 1.2s ease-in-out infinite',
                  boxShadow: '0 0 8px rgba(56, 189, 248, 0.6)',
                }} />
              )}

              {/* Label */}
              <span style={{
                fontSize: '8px',
                fontWeight: labelWeight,
                color: labelColor,
                letterSpacing: '0.02em',
                textTransform: 'uppercase',
                lineHeight: 1,
                transition: 'color 0.3s ease',
              }}>
                {hex.label}
              </span>
            </div>

            {/* Connector line between hexes */}
            {i < HEXES.length - 1 && (
              <div style={{
                flex: 1,
                height: connectorGold ? '3px' : connectorCyan ? '2px' : '2px',
                background: connectorGold
                  ? '#F59E0B'
                  : connectorCyan
                    ? '#38BDF8'
                    : 'rgba(255, 255, 255, 0.1)',
                borderRadius: '1px',
                minWidth: '2px',
                maxWidth: '10px',
                marginBottom: '13px',
                boxShadow: connectorGold
                  ? '0 0 6px rgba(245, 158, 11, 0.6)'
                  : connectorCyan
                    ? '0 0 4px rgba(56, 189, 248, 0.4)'
                    : 'none',
                transition: 'all 0.3s ease',
              }} />
            )}
          </React.Fragment>
        );
      })}

      {/* Done count badge */}
      <div style={{
        marginLeft: '4px',
        marginBottom: '13px',
        padding: '3px 6px',
        borderRadius: '12px',
        background: hexDoneCount === totalHexes
          ? 'rgba(74, 222, 128, 0.2)'
          : 'rgba(255,255,255,0.1)',
        border: `1.5px solid ${hexDoneCount === totalHexes ? '#4ADE80' : 'rgba(255,255,255,0.25)'}`,
        fontSize: '10px',
        fontWeight: 900,
        color: hexDoneCount === totalHexes ? '#4ADE80' : '#FDE68A',
        whiteSpace: 'nowrap',
        flexShrink: 0,
        boxShadow: hexDoneCount === totalHexes ? '0 0 10px rgba(74,222,128,0.4)' : 'none',
      }}>
        {hexDoneCount}/{totalHexes}
      </div>
    </div>
  );
}
