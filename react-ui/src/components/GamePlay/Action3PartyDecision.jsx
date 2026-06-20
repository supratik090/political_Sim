import React from 'react';

export default function Action3PartyDecision({
  turnData,
  selectedIssueOptionKey,
  setSelectedIssueOptionKey
}) {
  return (
    <div>
      {turnData.turnNumber <= 2 && (
        <p style={{ margin: '0 0 15px 0', fontSize: '13px', color: 'var(--card-text)' }}>
          Respond to internal party matters and organization reviews.
        </p>
      )}
      {!turnData.currentIssue ? (
        <p style={{ margin: 0, fontSize: '13px', opacity: 0.8 }}>Routine Party Review: No action required.</p>
      ) : (
        <div>
          <h5 style={{ margin: '0 0 4px 0', fontSize: '14px', color: 'var(--primary-dark)' }}>🏛️ {turnData.currentIssue.title}</h5>
          <p style={{ margin: '0 0 10px 0', fontSize: '12px', opacity: 0.8, color: 'var(--card-text)' }}>{turnData.currentIssue.description}</p>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {turnData.currentIssue.options.map(opt => {
              const isSelected = selectedIssueOptionKey === opt.optionKey;
              return (
                <button
                  key={opt.optionKey}
                  onClick={() => setSelectedIssueOptionKey(opt.optionKey)}
                  style={{
                    textAlign: 'left',
                    padding: '12px 18px',
                    borderRadius: '8px',
                    fontSize: '13px',
                    background: 'var(--button-bg)',
                    color: '#ffffff',
                    border: isSelected ? '2.5px solid #22c55e' : '2.5px solid transparent',
                    boxShadow: isSelected ? '0 0 14px rgba(34, 197, 94, 0.6)' : 'none',
                    fontWeight: isSelected ? 'bold' : 'normal',
                    transition: 'all 0.2s ease',
                    cursor: 'pointer',
                    transform: 'none'
                  }}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.background = 'var(--button-hover-bg)';
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.background = 'var(--button-bg)';
                  }}
                >
                  {isSelected ? '✓ ' : ''}{opt.text}
                </button>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
}
