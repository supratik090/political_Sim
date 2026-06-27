import React from 'react';

export default function Action2NewsReaction({
  turnData,
  selectedNewsReactions,
  setSelectedNewsReactions
}) {
  const newsItems = turnData.currentNews || [];

  return (
    <div style={{
      background: '#fdfbf7',
      border: '1px solid #dcd7ca',
      boxShadow: 'inset 0 0 30px rgba(0,0,0,0.02), 0 10px 25px rgba(0,0,0,0.05)',
      borderRadius: '12px',
      padding: '25px',
      color: '#1c1917',
      fontFamily: "Georgia, 'Times New Roman', serif"
    }}>
      {/* Newspaper Masthead */}
      <div style={{ textAlign: 'center', marginBottom: '20px' }}>
        <h1 style={{ 
          fontFamily: "'Playfair Display', Georgia, serif", 
          fontSize: '24px', 
          fontWeight: 900, 
          letterSpacing: '0.05em', 
          margin: '0 0 5px 0',
          textTransform: 'uppercase',
          color: '#1c1917'
        }}>
          The State Chronicle
        </h1>
        
        {/* Newspaper Meta Bar */}
        <div style={{ 
          borderTop: '1px solid #d6d3d1', 
          borderBottom: '1px solid #d6d3d1', 
          padding: '6px 10px', 
          margin: '12px 0 0 0', 
          display: 'flex', 
          justifyContent: 'center', 
          fontSize: '10px', 
          textTransform: 'uppercase', 
          letterSpacing: '0.08em', 
          fontWeight: 'bold',
          color: '#57534e'
        }}>
          <span>📅 {turnData.currentDate}</span>
        </div>
      </div>

      {newsItems.length === 0 ? (
        <div style={{ textAlign: 'center', padding: '20px', fontStyle: 'italic', color: '#78716c' }}>
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
                <div style={{ textAlign: 'center', margin: '20px 0', color: '#a8a29e', letterSpacing: '0.5em', fontSize: '14px' }}>
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
                color: '#0c0a09',
                fontFamily: "Georgia, serif"
              }}>
                {news.title}
              </h2>
              
              {/* Article Content in Newspaper Column style */}
              <div style={{ 
                fontSize: '13.5px', 
                lineHeight: 1.6, 
                textAlign: 'justify', 
                color: '#292524',
                marginBottom: '20px',
                textIndent: '20px',
                columnCount: news.description.length > 200 ? 1 : 1,
                columnGap: '20px'
              }}>
                {news.description}
              </div>

              {/* Reaction Options Box (styled as Official Press Release Form) */}
              <div style={{ 
                background: '#f5f5f4', 
                borderRadius: '8px', 
                padding: '15px'
              }}>
                <h4 style={{ 
                  margin: '0 0 12px 0', 
                  fontSize: '11px', 
                  textTransform: 'uppercase', 
                  letterSpacing: '0.05em', 
                  color: '#57534e',
                  fontWeight: 900,
                  textAlign: 'center',
                  fontFamily: 'sans-serif'
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
                          fontSize: '12px',
                          background: isSelected ? 'var(--party-primary-color)' : '#ffffff',
                          color: isSelected ? '#ffffff' : '#1c1917',
                          border: isSelected ? '1px solid var(--party-primary-color)' : '1px solid #d6d3d1',
                          boxShadow: isSelected ? '0 4px 10px rgba(var(--party-primary-color-rgb), 0.2)' : 'none',
                          fontWeight: isSelected ? 'bold' : 'normal',
                          transition: 'all 0.15s ease',
                          cursor: 'pointer',
                          fontFamily: "system-ui, -apple-system, sans-serif"
                        }}
                        onMouseEnter={(e) => {
                          if (!isSelected) {
                            e.currentTarget.style.background = '#fafaf9';
                            e.currentTarget.style.borderColor = '#a8a29e';
                          }
                        }}
                        onMouseLeave={(e) => {
                          if (!isSelected) {
                            e.currentTarget.style.background = '#ffffff';
                            e.currentTarget.style.borderColor = '#d6d3d1';
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
