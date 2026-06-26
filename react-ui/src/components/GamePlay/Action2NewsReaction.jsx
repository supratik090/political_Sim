import React from 'react';

export default function Action2NewsReaction({
  turnData,
  selectedNewsReactions,
  setSelectedNewsReactions
}) {
  const newsItems = turnData.currentNews || [];

  return (
    <div style={{
      background: 'var(--card-bg)',
      border: '1.5px solid var(--card-border)',
      boxShadow: '0 10px 30px rgba(0,0,0,0.3)',
      borderRadius: '12px',
      padding: '25px',
      color: 'var(--text-primary)',
      fontFamily: "'Outfit', Georgia, serif"
    }}>
      {/* Newspaper Masthead */}
      <div style={{ textAlign: 'center', marginBottom: '20px' }}>
        <h1 style={{ 
          fontFamily: "'Outfit', Georgia, serif", 
          fontSize: '26px', 
          fontWeight: 900, 
          letterSpacing: '0.05em', 
          margin: '0 0 5px 0',
          textTransform: 'uppercase',
          color: '#fbbf24',
          textShadow: '0 2px 10px rgba(251, 191, 36, 0.2)'
        }}>
          The State Chronicle
        </h1>
        
        {/* Newspaper Meta Bar */}
        <div style={{ 
          borderTop: '1px solid rgba(255, 255, 255, 0.1)', 
          borderBottom: '1px solid rgba(255, 255, 255, 0.1)', 
          padding: '6px 10px', 
          margin: '12px 0 0 0', 
          display: 'flex', 
          justifyContent: 'center', 
          fontSize: '10px', 
          textTransform: 'uppercase', 
          letterSpacing: '0.08em', 
          fontWeight: 'bold',
          color: 'var(--text-secondary)'
        }}>
          <span>📅 {turnData.currentDate}</span>
        </div>
      </div>

      {newsItems.length === 0 ? (
        <div style={{ textAlign: 'center', padding: '20px', fontStyle: 'italic', color: 'var(--text-secondary)' }}>
          No breaking news articles published in this edition.
        </div>
      ) : (
        newsItems.map((news, index) => {
          const newsKey = news.newsKey || news.issueKey;
          const currentReaction = selectedNewsReactions[newsKey];
          const options = news.reactionOptions || news.options || [];
          return (
            <div key={newsKey} style={{ marginBottom: index === newsItems.length - 1 ? 0 : '30px' }}>
               {index > 0 && (
                <div style={{ textAlign: 'center', margin: '20px 0', color: 'var(--primary-border)', letterSpacing: '0.5em', fontSize: '14px' }}>
                  •••
                </div>
              )}
              {/* Headline */}
              <h2 style={{ 
                margin: '0 0 12px 0', 
                fontSize: '20px', 
                fontWeight: 'bold', 
                lineHeight: 1.3, 
                textAlign: 'center',
                color: 'var(--text-primary)',
                fontFamily: "'Outfit', Georgia, serif"
              }}>
                {news.title}
              </h2>
              
              {/* Article Content in Newspaper Column style */}
              <div style={{ 
                fontSize: '13.5px', 
                lineHeight: 1.6, 
                textAlign: 'justify', 
                color: 'var(--text-secondary)',
                marginBottom: '20px',
                textIndent: '20px'
              }}>
                {news.description}
              </div>

              {/* Reaction Options Box (styled as Official Press Release Form) */}
              <div style={{ 
                background: 'var(--primary-dark)', 
                border: '1.5px solid var(--primary-border)',
                borderRadius: '8px', 
                padding: '15px'
              }}>
                <h4 style={{ 
                  margin: '0 0 12px 0', 
                  fontSize: '11px', 
                  textTransform: 'uppercase', 
                  letterSpacing: '0.05em', 
                  color: 'var(--text-secondary)',
                  fontWeight: 900,
                  textAlign: 'center',
                  fontFamily: "'Outfit', sans-serif"
                }}>
                  📢 OFFICIAL PARTY RESPONSE CHANNELS
                </h4>
                
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
                          padding: '10px 14px',
                          borderRadius: '6px',
                          fontSize: '12.5px',
                          background: isSelected ? 'linear-gradient(135deg, #0ea5e9 0%, #6366f1 100%)' : 'var(--card-bg)',
                          color: '#ffffff',
                          border: isSelected ? '1.5px solid var(--selected-highlight)' : '1.5px solid var(--primary-border)',
                          boxShadow: isSelected ? '0 4px 15px rgba(99, 102, 241, 0.3)' : 'none',
                          fontWeight: isSelected ? 'bold' : 'normal',
                          transition: 'all 0.15s ease',
                          cursor: 'pointer',
                          fontFamily: "'Outfit', sans-serif"
                        }}
                        onMouseEnter={(e) => {
                          if (!isSelected) {
                            e.currentTarget.style.background = 'rgba(99, 102, 241, 0.08)';
                            e.currentTarget.style.borderColor = 'var(--selected-highlight)';
                          }
                        }}
                        onMouseLeave={(e) => {
                          if (!isSelected) {
                            e.currentTarget.style.background = 'var(--card-bg)';
                            e.currentTarget.style.borderColor = 'var(--primary-border)';
                          }
                        }}
                      >
                        {isSelected ? '🖋️ [Selected] ' : '○ '}{opt.text}
                      </button>
                    );
                  })}
                </div>
              </div>
            </div>
          );
        })
      )}
    </div>
  );
}
