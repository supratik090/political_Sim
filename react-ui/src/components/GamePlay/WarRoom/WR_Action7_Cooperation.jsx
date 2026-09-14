import React, { useState } from 'react';
// Wrap existing cooperation component — all logic stays there
import Action7Cooperation from '../Action7Cooperation';

/**
 * WR_Action7_Cooperation — Diplomatic Cooperation (optional)
 * Shows as a collapsible "bonus action" panel with teal dashed border.
 */
export default function WR_Action7_Cooperation({ turnData, projectDefs, onActionComplete }) {
  const [expanded, setExpanded] = useState(false);

  return (
    <div style={{ padding: '0 16px 14px' }}>
      <div className="wr-coop-panel">
        {/* Header row */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div>
            <span style={{ fontSize: '13px', fontWeight: 800, letterSpacing: '0.05em', textTransform: 'uppercase', color: '#34D399' }}>
              🤝 Diplomatic Cooperation
            </span>
            <span style={{
              marginLeft: '8px', fontSize: '10px', fontWeight: 700,
              color: '#7D8590', background: 'rgba(255,255,255,0.06)',
              padding: '2px 7px', borderRadius: '20px',
              verticalAlign: 'middle', letterSpacing: '0.04em',
            }}>
              OPTIONAL
            </span>
          </div>
          <button
            onClick={() => setExpanded(e => !e)}
            style={{
              background: 'transparent', border: 'none',
              color: '#34D399', fontSize: '18px', cursor: 'pointer',
              padding: '4px 8px', minHeight: 'unset',
              touchAction: 'manipulation', WebkitTapHighlightColor: 'transparent',
              fontFamily: 'Montserrat,system-ui,sans-serif',
              transition: 'transform 0.2s ease',
              transform: expanded ? 'rotate(180deg)' : 'rotate(0deg)',
            }}
          >
            ▼
          </button>
        </div>

        {!expanded && (
          <div style={{ fontSize: '12px', color: '#7D8590', marginTop: '6px' }}>
            Tap to manage alliances & diplomatic cables with other parties.
          </div>
        )}

        {/* Existing component rendered when expanded */}
        {expanded && (
          <div style={{
            marginTop: '14px',
            padding: '14px',
            background: 'rgba(255,255,255,0.03)',
            border: '1px solid rgba(255,255,255,0.08)',
            borderRadius: '12px',
            animation: 'wr-slide-in 0.2s ease',
          }}>
            <Action7Cooperation
              turnData={turnData}
              projectDefs={projectDefs}
              onActionComplete={onActionComplete}
            />
          </div>
        )}
      </div>
    </div>
  );
}
