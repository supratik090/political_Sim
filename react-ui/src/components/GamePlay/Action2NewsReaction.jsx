import React from 'react';

export default function Action2NewsReaction({
  turnData,
  selectedNewsReactions,
  setSelectedNewsReactions
}) {
  const newsItems = turnData.currentNews || [];

  return (
    <div>
      {turnData.turnNumber <= 2 && (
        <p style={{ margin: '0 0 15px 0', fontSize: '13px', color: 'var(--card-text)' }}>
          React to current monthly news items. Reactions shape public perception.
        </p>
      )}
      {newsItems.length === 0 ? (
        <p style={{ margin: 0, fontSize: '13px', opacity: 0.8 }}>No breaking news this turn.</p>
      ) : (
        newsItems.map(news => {
          const newsKey = news.newsKey || news.issueKey;
          const currentReaction = selectedNewsReactions[newsKey];
          const options = news.reactionOptions || news.options || [];
          return (
            <div key={newsKey} style={{ borderBottom: '1px solid rgba(101,148,177,0.1)', paddingBottom: '15px', marginBottom: '15px' }}>
              <h5 style={{ margin: '0 0 4px 0', fontSize: '14px', color: 'var(--primary-dark)' }}>📰 {news.title}</h5>
              <p style={{ margin: '0 0 10px 0', fontSize: '12px', opacity: 0.8, color: 'var(--card-text)' }}>{news.description}</p>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                {options.map(opt => {
                  const optKey = opt.reactionKey || opt.optionKey;
                  const isSelected = currentReaction === optKey;
                  return (
                    <button
                      key={optKey}
                      onClick={() => setSelectedNewsReactions(prev => ({ ...prev, [newsKey]: optKey }))}
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
          );
        })
      )}
    </div>
  );
}
