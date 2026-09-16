import React from 'react';

const TABS = [
  {
    id: 'politics',
    label: 'Politics',
    icon: '🗳️',
    gradFrom: '#6C3AB5',
    gradTo:   '#9B5DE5',
    glowColor: 'rgba(108,58,181,0.5)',
  },
  {
    id: 'governance',
    label: 'Governance',
    icon: '🏛️',
    gradFrom: '#0F766E',
    gradTo:   '#10B981',
    glowColor: 'rgba(16,185,129,0.45)',
  },
  {
    id: 'economy',
    label: 'Economy',
    icon: '💰',
    gradFrom: '#D97706',
    gradTo:   '#F59E0B',
    glowColor: 'rgba(245,158,11,0.45)',
  },
];

/**
 * WR_TabBar — three gradient tabs (Politics / Governance / Economy)
 * Props: {
 *   activeTab, setActiveTab,
 *   politicsDone, politicsPending,
 *   governanceDone, governancePending,
 *   economyDone, economyPending,
 * }
 */
export default function WR_TabBar({
  activeTab,
  setActiveTab,
  politicsDone,
  politicsPending,
  governanceDone,
  governancePending,
  economyDone,
  economyPending,
}) {
  const statusMap = {
    politics:   { done: politicsDone,   pending: politicsPending },
    governance: { done: governanceDone, pending: governancePending },
    economy:    { done: economyDone,    pending: economyPending },
  };

  return (
    <div style={{
      display: 'flex',
      background: '#0D1117',
      borderRadius: '14px',
      overflow: 'hidden',
      border: '1px solid rgba(255,255,255,0.15)',
      marginBottom: '20px',
      boxShadow: '0 4px 14px rgba(0,0,0,0.25)',
    }}>
      {TABS.map((tab, idx) => {
        const isActive = activeTab === tab.id;
        const { done: isDone, pending: isPending } = statusMap[tab.id];

        const statusIndicator = isDone ? '✓' : isPending ? '!' : '—';
        const statusColor = isDone ? '#4ADE80' : isPending ? '#FCD34D' : 'rgba(255,255,255,0.3)';

        return (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            style={{
              flex: 1,
              minHeight: '64px',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
              gap: '4px',
              position: 'relative',
              padding: '10px 4px 14px',
              border: 'none',
              borderRadius: 0,
              cursor: 'pointer',
              touchAction: 'manipulation',
              WebkitTapHighlightColor: 'transparent',
              transition: 'all 0.2s ease',
              // Active vs inactive — pending inactive tabs get a subtle flash
              background: isActive
                ? `linear-gradient(135deg, ${tab.gradFrom}, ${tab.gradTo})`
                : (!isDone && isPending)
                  ? 'rgba(245,158,11,0.07)'
                  : 'rgba(255,255,255,0.03)',
              borderBottom: isActive ? '3px solid #ffffff' : '3px solid transparent',
              boxShadow: isActive
                ? `0 4px 20px ${tab.glowColor}`
                : (!isDone && isPending)
                  ? 'inset 0 0 0 1.5px rgba(245,158,11,0.35)'
                  : 'none',
              transform: isActive ? 'translateY(-1px)' : 'none',
              animation: (!isActive && isPending && !isDone)
                ? 'wr-tab-pending-flash 1.8s ease-in-out infinite'
                : 'none',
              // override global button defaults
              minWidth: 'unset',
              fontSize: '11px',
              fontWeight: isActive ? 800 : 600,
              letterSpacing: '0.04em',
              textTransform: 'uppercase',
              color: isActive ? '#ffffff' : (!isDone && isPending) ? '#FCD34D' : 'rgba(255,255,255,0.45)',
            }}
          >
            {/* Large icon */}
            <span style={{ fontSize: '22px', lineHeight: 1 }}>{tab.icon}</span>

            {/* Label */}
            <span style={{ fontSize: '11px', letterSpacing: '0.04em' }}>{tab.label}</span>

            {/* Completion badge — bottom right */}
            <span style={{
              position: 'absolute',
              bottom: '6px',
              right: '8px',
              fontSize: '11px',
              fontWeight: 900,
              color: statusColor,
              lineHeight: 1,
            }}>
              {statusIndicator}
            </span>

            {/* Divider between tabs (not after last) */}
            {idx < TABS.length - 1 && (
              <div style={{
                position: 'absolute',
                right: 0,
                top: '12px',
                bottom: '12px',
                width: '1px',
                background: 'rgba(255,255,255,0.07)',
              }} />
            )}
          </button>
        );
      })}
    </div>
  );
}
