import React, { useMemo } from 'react';

function deterministicShuffle(array, seedString) {
  if (!array || array.length === 0) return [];
  let hash = 0;
  for (let i = 0; i < seedString.length; i++) {
    hash = seedString.charCodeAt(i) + ((hash << 5) - hash);
  }
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const val = Math.abs(Math.sin(hash + i) * 10000);
    const j = Math.floor((val - Math.floor(val)) * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

function getOptionTone(opt) {
  const effects = opt.effects?.playerParty || opt.effects || {};
  let positive = false; let negative = false;
  Object.entries(effects).forEach(([key, val]) => {
    const n = Number(val) || 0;
    if (key === 'corruptionScore') { if (n > 0) negative = true; if (n < 0) positive = true; }
    else { if (n > 0) positive = true; if (n < 0) negative = true; }
  });
  if (positive && !negative) return 'positive';
  if (negative && !positive) return 'negative';
  if (positive && negative) return 'mixed';
  return 'neutral';
}

function toneConfig(tone, isSelected) {
  if (isSelected) return {
    bg: 'var(--party-primary-color, #6C3AB5)',
    border: 'var(--party-primary-color, #9B5DE5)',
    color: '#ffffff',
    icon: '🖋️',
  };
  if (tone === 'positive') return { bg: 'rgba(22,163,74,0.07)', border: 'rgba(22,163,74,0.35)', color: '#C9D1D9', icon: '📈' };
  if (tone === 'negative') return { bg: 'rgba(220,38,38,0.07)', border: 'rgba(220,38,38,0.35)', color: '#C9D1D9', icon: '📉' };
  if (tone === 'mixed')    return { bg: 'rgba(245,158,11,0.07)', border: 'rgba(245,158,11,0.3)', color: '#C9D1D9', icon: '⚡' };
  return { bg: 'rgba(255,255,255,0.04)', border: 'rgba(255,255,255,0.1)', color: '#C9D1D9', icon: '○' };
}

/**
 * WR_Action2_News — Breaking News Reaction
 * Props: { turnData, selectedNewsReactions, setSelectedNewsReactions }
 */
export default function WR_Action2_News({ turnData, selectedNewsReactions, setSelectedNewsReactions }) {
  const newsItems = turnData?.currentNews || [];

  if (newsItems.length === 0) {
    return (
      <div style={{ padding: '30px 16px', textAlign: 'center', color: '#7D8590', fontSize: '13px', fontStyle: 'italic' }}>
        📰 No breaking news this month.
      </div>
    );
  }

  return (
    <div style={{ padding: '14px 16px 0' }}>
      {/* Section header */}
      <div style={{ marginBottom: '14px' }}>
        <div style={{ fontSize: '15px', fontWeight: 900, letterSpacing: '0.05em', textTransform: 'uppercase', color: '#F59E0B' }}>
          📰 Breaking News
        </div>
        <div style={{ fontSize: '12px', color: '#7D8590', marginTop: '2px' }}>
          Issue your party's official response
        </div>
      </div>

      {newsItems.map((news, index) => {
        const newsKey = news.newsKey || news.issueKey;
        const currentReaction = selectedNewsReactions[newsKey];
        const rawOptions = news.reactionOptions || news.options || [];
        // eslint-disable-next-line react-hooks/rules-of-hooks
        const options = useMemo(
          () => deterministicShuffle(rawOptions, `${turnData?.id || ''}-${turnData?.turnNumber}-${newsKey}`),
          // eslint-disable-next-line react-hooks/exhaustive-deps
          [newsKey, turnData?.turnNumber]
        );

        return (
          <div key={newsKey}>
            {/* Separator between multiple news items */}
            {index > 0 && (
              <div className="wr-divider-gold" style={{ margin: '12px 0 16px' }}>• • •</div>
            )}

            {/* Dark news card */}
            <div className="wr-news-card">
              {/* Masthead */}
              <div style={{
                fontSize: '10px', fontWeight: 800, letterSpacing: '0.1em',
                textTransform: 'uppercase', color: '#F59E0B', marginBottom: '10px',
                display: 'flex', justifyContent: 'space-between',
              }}>
                <span>📰 BREAKING NEWS</span>
                <span style={{ color: '#7D8590' }}>{turnData?.currentDate}</span>
              </div>

              {/* Headline */}
              <h3 style={{
                margin: '0 0 10px 0', fontSize: '18px', fontWeight: 900,
                color: '#ffffff', lineHeight: 1.3,
              }}>
                {news.title}
              </h3>

              {/* Article body */}
              <p style={{ margin: '0 0 16px 0', fontSize: '13px', color: '#C9D1D9', lineHeight: 1.65 }}>
                {news.description}
              </p>

              {/* Stance label */}
              <div style={{
                fontSize: '11px', fontWeight: 800, letterSpacing: '0.07em',
                textTransform: 'uppercase', color: '#7D8590', marginBottom: '10px',
              }}>
                YOUR PARTY'S STANCE
              </div>

              {/* Response buttons */}
              {options.map(opt => {
                const optKey = opt.reactionKey || opt.optionKey;
                const isSelected = currentReaction === optKey;
                const tone = getOptionTone(opt);
                const cfg = toneConfig(tone, isSelected);

                return (
                  <button
                    key={optKey}
                    onClick={() => setSelectedNewsReactions(prev => ({ ...prev, [newsKey]: optKey }))}
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: '8px',
                      width: '100%',
                      textAlign: 'left',
                      padding: '13px 14px',
                      borderRadius: '10px',
                      marginBottom: '8px',
                      minHeight: '52px',
                      background: cfg.bg,
                      color: cfg.color,
                      border: `1.5px solid ${cfg.border}`,
                      fontWeight: isSelected ? 700 : 400,
                      fontSize: '14px',
                      cursor: 'pointer',
                      touchAction: 'manipulation',
                      WebkitTapHighlightColor: 'transparent',
                      transition: 'all 0.15s ease',
                      animation: isSelected ? 'wr-fill-in 0.18s ease' : 'none',
                      fontFamily: 'Montserrat,system-ui,sans-serif',
                      boxShadow: isSelected ? '0 0 14px var(--wr-glow-purple, rgba(108,58,181,0.4))' : 'none',
                    }}
                  >
                    <span style={{ fontSize: '16px', flexShrink: 0 }}>{cfg.icon}</span>
                    <span style={{ flex: 1, lineHeight: 1.4 }}>{opt.text}</span>
                    {isSelected && (
                      <span style={{ color: '#4ADE80', fontSize: '16px', fontWeight: 900, flexShrink: 0 }}>✓</span>
                    )}
                  </button>
                );
              })}
            </div>
          </div>
        );
      })}
    </div>
  );
}
