import React, { useState, useCallback, useMemo, useEffect } from 'react';
import { evaluateNewsReaction } from '../../../utils/instantFeedbackEngine';
import { formatEffectValue } from '../gameUtils';
import { fetchBatchNewsFeedback } from '../../../api/apiClient';
import { getCachedBatchNewsFeedback, preloadTurnFeedback } from '../../../utils/turnFeedbackCache';

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
  if (positive && negative)  return 'mixed';
  return 'neutral';
}

// Colour config for each stance tone — unselected state
const TONE_IDLE = {
  positive: { bg: 'rgba(22,163,74,0.07)',  border: 'rgba(22,163,74,0.28)',  icon: '📈' },
  negative: { bg: 'rgba(220,38,38,0.07)',  border: 'rgba(220,38,38,0.28)',  icon: '📉' },
  mixed:    { bg: 'rgba(245,158,11,0.07)', border: 'rgba(245,158,11,0.25)', icon: '⚡' },
  neutral:  { bg: 'rgba(255,255,255,0.04)',border: 'rgba(255,255,255,0.1)', icon: '○'  },
};

/**
 * WR_Action2_News — Breaking News Reaction
 * Auto-locks once every news item has a stance selected (same Option B flow as cards).
 */
export default function WR_Action2_News({ turnData, selectedNewsReactions, setSelectedNewsReactions }) {
  const newsItems   = turnData?.currentNews || [];
  const activeParty = turnData?.parties?.find(p => p.id === turnData.activeHumanPartyId)
    || turnData?.parties?.find(p => p.playerControlled);

  const gameSessionId      = turnData?.gameId || turnData?.id || turnData?.scenarioId || 'default_session';
  const turnNumber         = turnData?.turnNumber || 0;
  const lockStorageKey     = `political_sim_news_locked_${gameSessionId}_turn_${turnNumber}`;
  const feedbackStorageKey = `political_sim_news_feedback_${gameSessionId}_turn_${turnNumber}`;
  const newsStorageKey     = `political_sim_news_reactions_${gameSessionId}_turn_${turnNumber}`;

  // 'idle' | 'calculating' | 'revealed'
  const [feedbackState, setFeedbackState] = useState(() => {
    try { return localStorage.getItem(lockStorageKey) === 'true' ? 'revealed' : 'idle'; } catch (_) { return 'idle'; }
  });

  const [newsFeedbackMap, setNewsFeedbackMap] = useState(() => {
    try {
      const saved = localStorage.getItem(feedbackStorageKey);
      return saved ? JSON.parse(saved) : {};
    } catch (_) { return {}; }
  });

  const isLocked = feedbackState === 'revealed';

  // Restore persisted reactions on mount
  useEffect(() => {
    if (!selectedNewsReactions || Object.keys(selectedNewsReactions).length === 0) {
      try {
        const saved = localStorage.getItem(newsStorageKey);
        if (saved) {
          const parsed = JSON.parse(saved);
          if (parsed && Object.keys(parsed).length > 0) setSelectedNewsReactions(parsed);
        }
      } catch (_) {}
    }
  }, [newsStorageKey, selectedNewsReactions, setSelectedNewsReactions]);

  // Background cache preload
  useEffect(() => {
    const gameId  = turnData?.gameId || turnData?.id;
    const partyId = activeParty?.id;
    if (gameId && partyId) preloadTurnFeedback(gameId, partyId, turnNumber);
  }, [turnData?.gameId, turnData?.id, activeParty?.id, turnNumber]);

  const allNewsAnswered = newsItems.length > 0
    && newsItems.every(n => selectedNewsReactions[n.newsKey || n.issueKey] !== undefined);

  /** Auto-lock — fires once all stances are answered, Option B reveal. */
  const handleAutoLock = useCallback(async (reactionsSnapshot) => {
    if (feedbackState !== 'idle') return;
    setFeedbackState('calculating');

    await new Promise(r => setTimeout(r, 320));

    try {
      const fbMap  = {};
      const gameId  = turnData?.gameId || turnData?.id;
      const partyId = activeParty?.id;

      const cachedBatch = getCachedBatchNewsFeedback(gameId, turnNumber, partyId, reactionsSnapshot);
      if (cachedBatch) {
        Object.assign(fbMap, cachedBatch);
      } else {
        try {
          const res = await fetchBatchNewsFeedback(gameId, {
            partyId,
            selectedNewsReactions: reactionsSnapshot,
          });
          if (res && Object.keys(res).length > 0) {
            Object.entries(res).forEach(([nk, item]) => {
              fbMap[nk] = {
                hasBackfired: item.backfired,
                badgeColor:   item.backfired ? '#F87171' : (item.tripleMultiplier ? '#F59E0B' : '#4ADE80'),
                badgeText:    item.headline || (item.backfired ? '🚨 PRESS BACKLASH' : '✅ PUBLIC RESONANCE'),
                chance:       item.riskChance,
                netEffects:   item.netDeltas || {},
                coinAward:    item.coinAward,
                isBackend:    true,
              };
            });
          }
        } catch (err) {
          console.warn('Backend news feedback fetch failed, using local engine:', err);
          newsItems.forEach(n => {
            const nk = n.newsKey || n.issueKey;
            const chosenOpt = (n.reactionOptions || n.options || [])
              .find(o => (o.reactionKey || o.optionKey) === reactionsSnapshot[nk]);
            fbMap[nk] = evaluateNewsReaction(turnData, turnData?.activeHumanPartyId, n, chosenOpt);
          });
        }
      }

      setNewsFeedbackMap(fbMap);
      setFeedbackState('revealed');

      try {
        localStorage.setItem(lockStorageKey,     'true');
        localStorage.setItem(feedbackStorageKey, JSON.stringify(fbMap));
        localStorage.setItem(newsStorageKey,     JSON.stringify(reactionsSnapshot));
      } catch (_) {}
    } catch (err) {
      console.error('News auto-lock failed:', err);
      setFeedbackState('idle');
    }
  }, [feedbackState, turnData, activeParty, newsItems, turnNumber, lockStorageKey, feedbackStorageKey, newsStorageKey]);

  /** Select a stance for a single news item; auto-lock when all are answered. */
  const handleStanceSelect = useCallback((newsKey, optKey) => {
    if (feedbackState !== 'idle') return;
    setSelectedNewsReactions(prev => {
      const next = { ...prev, [newsKey]: optKey };
      try { localStorage.setItem(newsStorageKey, JSON.stringify(next)); } catch (_) {}

      // Check if this final selection completes all items
      const nowAllDone = newsItems.length > 0
        && newsItems.every(n => next[n.newsKey || n.issueKey] !== undefined);
      if (nowAllDone) {
        // Small timeout so state settles before async lock
        setTimeout(() => handleAutoLock(next), 50);
      }
      return next;
    });
  }, [feedbackState, newsItems, newsStorageKey, setSelectedNewsReactions, handleAutoLock]);

  if (newsItems.length === 0) {
    return (
      <div style={{ padding: '30px 16px', textAlign: 'center', color: '#7D8590', fontSize: '13px', fontStyle: 'italic' }}>
        📰 No breaking news this month.
      </div>
    );
  }

  const isCalculating = feedbackState === 'calculating';

  return (
    <div className="wr-news-section-guide" style={{ padding: '14px 16px 0' }}>

      {/* ── Section header ── */}
      <div style={{ fontSize: '15px', fontWeight: 900, letterSpacing: '0.05em', textTransform: 'uppercase', color: '#F59E0B', marginBottom: '14px' }}>
        📰 Breaking News
      </div>

      {newsItems.map((news, index) => {
        const newsKey        = news.newsKey || news.issueKey;
        const currentReaction = selectedNewsReactions[newsKey];
        const rawOptions     = news.reactionOptions || news.options || [];
        // eslint-disable-next-line react-hooks/rules-of-hooks
        const options = useMemo(
          () => deterministicShuffle(rawOptions, `${turnData?.id || ''}-${turnData?.turnNumber}-${newsKey}`),
          // eslint-disable-next-line react-hooks/exhaustive-deps
          [newsKey, turnData?.turnNumber]
        );

        const feedback = newsFeedbackMap[newsKey];

        return (
          <div key={newsKey}>
            {index > 0 && (
              <div className="wr-divider-gold" style={{ margin: '12px 0 16px' }}>• • •</div>
            )}

            {/* ── News card ── */}
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
              <h3 style={{ margin: '0 0 8px 0', fontSize: '16px', fontWeight: 900, color: '#ffffff', lineHeight: 1.3 }}>
                {news.title}
              </h3>

              {/* Article body */}
              <p style={{ margin: '0 0 14px 0', fontSize: '13px', color: '#C9D1D9', lineHeight: 1.6 }}>
                {news.description}
              </p>

              {/* Stance label */}
              <div style={{
                fontSize: '10px', fontWeight: 800, letterSpacing: '0.07em',
                textTransform: 'uppercase', color: '#7D8590', marginBottom: '8px',
              }}>
                {isLocked ? '🔒 STANCE COMMITTED' : 'YOUR PARTY\'S STANCE'}
              </div>

              {/* Stance options */}
              {options.map(opt => {
                const optKey     = opt.reactionKey || opt.optionKey;
                const isSelected = currentReaction === optKey;
                const tone       = getOptionTone(opt);
                const cfg        = TONE_IDLE[tone] || TONE_IDLE.neutral;

                // Selected: use party primary or green-locked
                const selBg     = isLocked ? 'rgba(16,185,129,0.12)' : 'rgba(108,58,181,0.15)';
                const selBorder = isLocked ? '#10B981' : 'var(--party-primary-color, #7C3AED)';

                return (
                  <button
                    key={optKey}
                    onClick={() => handleStanceSelect(newsKey, optKey)}
                    disabled={isLocked || isCalculating}
                    style={{
                      display:    'flex',
                      alignItems: 'center',
                      gap:        '8px',
                      width:      '100%',
                      textAlign:  'left',
                      padding:    '11px 12px',
                      borderRadius: '10px',
                      marginBottom: '7px',
                      minHeight:  '48px',
                      background: isSelected ? selBg    : cfg.bg,
                      color:      isSelected ? '#ffffff' : '#C9D1D9',
                      border:     `1.5px solid ${isSelected ? selBorder : cfg.border}`,
                      fontWeight: isSelected ? 700 : 400,
                      fontSize:   '13px',
                      cursor:     (isLocked || isCalculating) ? 'default' : 'pointer',
                      opacity:    (isLocked || isCalculating) && !isSelected ? 0.32 : 1,
                      touchAction: 'manipulation',
                      WebkitTapHighlightColor: 'transparent',
                      transition: 'all 0.15s ease',
                      boxShadow:  isSelected
                        ? (isLocked ? '0 0 10px rgba(16,185,129,0.3)' : '0 0 10px rgba(108,58,181,0.3)')
                        : 'none',
                      fontFamily: 'Montserrat,system-ui,sans-serif',
                    }}
                  >
                    <span style={{ fontSize: '14px', flexShrink: 0 }}>{cfg.icon}</span>
                    <span style={{ flex: 1, lineHeight: 1.4 }}>{opt.text}</span>
                    {isSelected && (
                      <span style={{ color: isLocked ? '#10B981' : '#C084FC', fontSize: '14px', fontWeight: 900, flexShrink: 0 }}>
                        {isLocked ? '🔒' : '✓'}
                      </span>
                    )}
                  </button>
                );
              })}
            </div>

            {/* ── Option B: Calculating pulse (shown once last stance selected) ── */}
            {isCalculating && index === newsItems.length - 1 && (
              <div style={{
                margin: '10px 0',
                padding: '11px 14px',
                borderRadius: '12px',
                background: 'rgba(245,158,11,0.07)',
                border: '1.5px solid rgba(245,158,11,0.22)',
                display: 'flex', alignItems: 'center', gap: '10px',
                animation: 'wr-fill-in 0.15s ease',
              }}>
                <span style={{ fontSize: '16px', display: 'inline-block', animation: 'wr-spin 0.7s linear infinite' }}>⚙️</span>
                <span style={{ fontSize: '12px', fontWeight: 800, color: '#FCD34D' }}>
                  Calculating public reaction…
                </span>
              </div>
            )}

            {/* ── Compact result: headline + stat pills, no narrative ── */}
            {isLocked && feedback && (
              <div style={{
                margin:     '8px 0 10px',
                padding:    '12px 14px',
                borderRadius: '12px',
                background: feedback.hasBackfired ? 'rgba(239,68,68,0.10)' : 'rgba(34,197,94,0.08)',
                border:     `1.5px solid ${feedback.badgeColor}`,
                boxShadow:  `0 0 12px ${feedback.badgeColor}25`,
                animation:  'wr-fill-in 0.25s ease',
              }}>
                {/* Headline row */}
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '7px' }}>
                  <span style={{
                    fontSize: '11px', fontWeight: 900,
                    letterSpacing: '0.04em', textTransform: 'uppercase',
                    color: feedback.badgeColor,
                  }}>
                    {feedback.badgeText}
                  </span>
                  {feedback.chance > 0 && (
                    <span style={{ fontSize: '10px', color: '#94A3B8', fontWeight: 600 }}>
                      Risk {feedback.chance}%
                    </span>
                  )}
                </div>

                {/* Compact stat pills */}
                <div style={{ display: 'flex', flexWrap: 'wrap', gap: '5px' }}>
                  {Object.entries(feedback.netEffects || {}).map(([k, v]) => {
                    const val = Number(v);
                    if (val === 0) return null;
                    const isPos = k === 'corruptionScore' ? val < 0 : val > 0;
                    return (
                      <span key={k} style={{
                        fontSize: '11px', fontWeight: 800,
                        padding: '3px 7px', borderRadius: '6px',
                        background: isPos ? 'rgba(34,197,94,0.18)' : 'rgba(239,68,68,0.18)',
                        color:      isPos ? '#4ADE80' : '#F87171',
                        border:     `1px solid ${isPos ? 'rgba(34,197,94,0.35)' : 'rgba(239,68,68,0.35)'}`,
                      }}>
                        {formatEffectValue(k, val)}
                      </span>
                    );
                  })}
                </div>
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
}
