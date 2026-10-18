import React from 'react';

export const GAME_MODES = [
  {
    id: 'PM_POWER',
    title: '👑 PM & National Power',
    shortTitle: 'PM National Power',
    color: '#38bdf8',
    description: 'Objective: Claim national executive authority by securing 272+ Lok Sabha majority seats. Lead central government and pass national legislation.'
  },
  {
    id: 'ALLIANCE_COALITION',
    title: '🤝 Form and Manage Alliances',
    shortTitle: 'Form & Manage Alliances',
    color: '#f59e0b',
    description: 'Objective: Master coalition diplomacy. Negotiate seat-sharing pacts with key regional partners in Uttar Pradesh, Bihar, Tamil Nadu, and Maharashtra.'
  },
  {
    id: 'STATE_BASE_BUILDING',
    title: '🗺️ Develop States to Build Base',
    shortTitle: 'Develop States Base',
    color: '#10b981',
    description: 'Objective: Expand grassroots party footprint state-by-state. Build cadre organizations across 30 states to establish Lok Sabha strongholds.'
  }
];

export default function SelectMode({ selectedGameMode, setSelectedGameMode }) {
  return (
    <div style={{ marginBottom: '32px' }}>
      <h3 style={{ margin: '0 0 12px 0', fontSize: '18px', fontWeight: '800', color: '#f59e0b', display: 'flex', alignItems: 'center', gap: '8px' }}>
        <span>🎯</span> 2. Select Strategic Game Mode Objective
      </h3>

      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))',
        gap: '16px'
      }}>
        {GAME_MODES.map(mode => {
          const isSelected = selectedGameMode === mode.id;
          return (
            <div
              key={mode.id}
              onClick={() => setSelectedGameMode(mode.id)}
              style={{
                backgroundColor: isSelected ? 'rgba(245, 158, 11, 0.12)' : 'rgba(15, 23, 42, 0.7)',
                border: isSelected ? `2px solid ${mode.color}` : '1px solid #1e293b',
                borderRadius: '12px',
                padding: '20px',
                cursor: 'pointer',
                transition: 'all 0.2s ease',
                boxShadow: isSelected ? `0 0 20px ${mode.color}35` : 'none'
              }}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                <span style={{ fontSize: '16px', fontWeight: '900', color: isSelected ? mode.color : '#ffffff' }}>
                  {mode.title}
                </span>
                {isSelected && (
                  <span style={{ backgroundColor: mode.color, color: '#0f172a', padding: '2px 8px', borderRadius: '4px', fontSize: '11px', fontWeight: '900' }}>
                    Selected
                  </span>
                )}
              </div>
              <p style={{ margin: 0, fontSize: '13px', color: '#94a3b8', lineHeight: 1.4 }}>
                {mode.description}
              </p>
            </div>
          );
        })}
      </div>
    </div>
  );
}
