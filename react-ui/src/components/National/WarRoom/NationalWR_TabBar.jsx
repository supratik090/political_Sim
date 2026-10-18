import React from 'react';

const TABS = [
  {
    id: 'intelligence',
    label: 'Intelligence',
    icon: '🏛️',
    color: '#38bdf8',
    activeBg: 'linear-gradient(135deg, rgba(15, 118, 110, 0.4), rgba(56, 189, 248, 0.25))',
    activeBorder: '#38bdf8',
    glow: 'rgba(56, 189, 248, 0.4)'
  },
  {
    id: 'operations',
    label: 'Operations',
    icon: '⚡',
    color: '#fbbf24',
    activeBg: 'linear-gradient(135deg, rgba(217, 119, 6, 0.4), rgba(245, 158, 11, 0.25))',
    activeBorder: '#f59e0b',
    glow: 'rgba(245, 158, 11, 0.4)'
  },
  {
    id: 'hints',
    label: 'Hints',
    icon: '💡',
    badge: 4,
    badgeBg: '#ef4444',
    color: '#f87171',
    activeBg: 'linear-gradient(135deg, rgba(185, 28, 28, 0.4), rgba(239, 68, 68, 0.25))',
    activeBorder: '#ef4444',
    glow: 'rgba(239, 68, 68, 0.4)'
  }
];

export default function NationalWR_TabBar({ activeTab, setActiveTab }) {
  return (
    <div style={{
      display: 'flex',
      gap: '8px',
      marginBottom: '16px',
      background: 'rgba(15, 23, 42, 0.8)',
      padding: '6px',
      borderRadius: '12px',
      border: '1px solid rgba(56, 189, 248, 0.2)',
      boxShadow: '0 8px 24px rgba(0, 0, 0, 0.4)'
    }}>
      {TABS.map(tab => {
        const isActive = activeTab === tab.id;

        return (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            style={{
              flex: 1,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: '6px',
              padding: '9px 12px',
              borderRadius: '8px',
              border: isActive ? `1.5px solid ${tab.activeBorder}` : '1px solid rgba(255, 255, 255, 0.08)',
              background: isActive ? tab.activeBg : 'rgba(255, 255, 255, 0.03)',
              color: isActive ? '#ffffff' : '#94a3b8',
              fontWeight: isActive ? 800 : 600,
              fontSize: '11px',
              letterSpacing: '0.03em',
              cursor: 'pointer',
              transition: 'all 0.2s ease-in-out',
              boxShadow: isActive ? `0 0 20px ${tab.glow}` : 'none',
              transform: isActive ? 'translateY(-1px)' : 'none',
              position: 'relative'
            }}
          >
            <span style={{ fontSize: '13px' }}>{tab.icon}</span>
            <span>{tab.label}</span>

            {tab.badge !== undefined && (
              <span style={{
                backgroundColor: tab.badgeBg,
                color: '#ffffff',
                fontSize: '8px',
                fontWeight: 900,
                width: '15px',
                height: '15px',
                borderRadius: '9999px',
                display: 'inline-flex',
                alignItems: 'center',
                justifyContent: 'center',
                boxShadow: `0 0 8px ${tab.badgeBg}`
              }}>
                {tab.badge}
              </span>
            )}
          </button>
        );
      })}
    </div>
  );
}
