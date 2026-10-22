import React, { useState, useCallback, useMemo, useEffect, useRef } from 'react';
import {
  CHANNELS,
  NO_SPEND_PENALTY,
  getCategoryLabel,
  getCategoryIcon,
  getChannelShortName,
  getTopicByKey,
  getTurnMediaTopics
} from '../../../constants/mediaConfig';
import { javaHashCode, javaRandomNextInt } from '../../../utils/instantFeedbackEngine';

/**
 * WR_Action_Media — Media & Narrative Management (Governance Tab)
 * Simplified flow: pick topic → pick channel(s) → auto-lock.
 * No Lock button. No stat rows on topic cards. No tagline. Default = nothing selected.
 */
export default function WR_Action_Media({
  turnData,
  activeParty,
  selectedMediaTopicKey: externalTopicKey,
  setSelectedMediaTopicKey: externalSetTopicKey,
  selectedMediaChannels: externalChannels,
  setSelectedMediaChannels: externalSetChannels
}) {
  const currentParty = activeParty
    || turnData?.parties?.find(p => p.id === turnData?.activeHumanPartyId)
    || turnData?.parties?.find(p => p.playerControlled);

  const role           = currentParty?.role || (currentParty?.isGovernment ? 'GOVERNMENT' : 'OPPOSITION');
  const turnNumber     = turnData?.turnNumber || 1;
  const gameSessionId  = turnData?.gameId || turnData?.id || turnData?.scenarioId || 'default_session';
  const availableFunds = currentParty?.stats?.coins ?? currentParty?.coins ?? currentParty?.funds ?? 0;
  const currentMediaImage = currentParty?.stats?.mediaImage ?? 50;

  const lockStorageKey      = `political_sim_media_locked_${gameSessionId}_turn_${turnNumber}`;
  const feedbackStorageKey  = `political_sim_media_feedback_${gameSessionId}_turn_${turnNumber}`;
  const selectionStorageKey = `political_sim_media_selection_${gameSessionId}_turn_${turnNumber}`;

  // 4 deterministic topics for this turn
  const availableTopics = useMemo(() => {
    return getTurnMediaTopics(role, turnNumber, gameSessionId);
  }, [role, turnNumber, gameSessionId]);

  // Internal state — DEFAULT = nothing selected
  const [internalTopicKey, setInternalTopicKey] = useState(() => {
    try {
      const saved = localStorage.getItem(selectionStorageKey);
      if (saved) {
        const parsed = JSON.parse(saved);
        if (parsed.topicKey) return parsed.topicKey;
      }
    } catch (_) {}
    return ''; // ← no default
  });

  const [internalChannels, setInternalChannels] = useState(() => {
    try {
      const saved = localStorage.getItem(selectionStorageKey);
      if (saved) {
        const parsed = JSON.parse(saved);
        if (Array.isArray(parsed.channels)) return parsed.channels;
      }
    } catch (_) {}
    return []; // ← no default channel
  });

  const [isNoSpend, setIsNoSpend] = useState(() => {
    try {
      const saved = localStorage.getItem(selectionStorageKey);
      if (saved) return Boolean(JSON.parse(saved).isNoSpend);
    } catch (_) {}
    return false;
  });

  const selectedTopicKey  = externalTopicKey  !== undefined ? externalTopicKey  : internalTopicKey;
  const setSelectedTopicKey = externalSetTopicKey || setInternalTopicKey;
  const selectedChannels  = externalChannels  !== undefined ? externalChannels  : internalChannels;
  const setSelectedChannels = externalSetChannels || setInternalChannels;

  // 'idle' | 'calculating' | 'revealed'
  const [feedbackState, setFeedbackState] = useState(() => {
    try { return localStorage.getItem(lockStorageKey) === 'true' ? 'revealed' : 'idle'; } catch (_) { return 'idle'; }
  });

  const [feedback, setFeedback] = useState(() => {
    try {
      const saved = localStorage.getItem(feedbackStorageKey);
      return saved ? JSON.parse(saved) : null;
    } catch (_) { return null; }
  });

  const isLocked     = feedbackState === 'revealed';
  const isCalculating= feedbackState === 'calculating';

  const currentTopic = useMemo(() => {
    return getTopicByKey(selectedTopicKey) || null;
  }, [selectedTopicKey]);

  const totalCost = useMemo(() => {
    if (isNoSpend) return 0;
    return selectedChannels.reduce((sum, chKey) => {
      const ch = CHANNELS.find(c => c.key === chKey);
      return sum + (ch ? ch.costCoins : 0);
    }, 0);
  }, [selectedChannels, isNoSpend]);

  const hasEnoughCoins = availableFunds >= totalCost;

  // Channel toggling (max 2)
  const handleToggleChannel = useCallback((chKey) => {
    if (isLocked || isCalculating) return;
    setIsNoSpend(false);
    setSelectedChannels(prev => {
      const current = Array.isArray(prev) ? prev : [];
      if (current.includes(chKey)) return current.filter(k => k !== chKey);
      if (current.length >= 2)    return [current[1], chKey];
      return [...current, chKey];
    });
  }, [isLocked, isCalculating, setSelectedChannels]);

  const handleToggleNoSpend = useCallback(() => {
    if (isLocked || isCalculating) return;
    setIsNoSpend(prev => {
      const next = !prev;
      setSelectedChannels(next ? [] : []);
      return next;
    });
  }, [isLocked, isCalculating, setSelectedChannels]);

  /** Auto-lock: fires once topic selected + (channel or noSpend decided) */
  const handleAutoLock = useCallback(async (topicKey, channels, noSpend) => {
    if (feedbackState !== 'idle') return;
    const topic = getTopicByKey(topicKey);
    if (!topic) return;
    if (!noSpend && channels.length === 0) return;
    if (!noSpend && !hasEnoughCoins) return;

    setFeedbackState('calculating');
    await new Promise(r => setTimeout(r, 320));

    try {
      let fb = null;

      if (noSpend || channels.length === 0) {
        fb = {
          hasBackfired:    true,
          badgeColor:      '#F87171',
          badgeText:       '⚠️ MEDIA SILENCE',
          headline:        NO_SPEND_PENALTY.headline,
          costCoins:       0,
          supportDelta:    NO_SPEND_PENALTY.supportDelta,
          mediaImageDelta: NO_SPEND_PENALTY.mediaImageDelta,
          pressureDelta:   NO_SPEND_PENALTY.pressureDelta,
        };
      } else {
        const seedStr = `${gameSessionId}:${turnNumber}:media:${currentParty?.id || 'party'}:${topic.key}`;
        const seed    = javaHashCode(seedStr);
        const roll    = javaRandomNextInt(seed, 100);

        let affinitySum = 0; let mediaBonusSum = 0;
        channels.forEach(chKey => {
          const ch = CHANNELS.find(c => c.key === chKey);
          affinitySum  += topic.channelAffinity?.[chKey] || 1.0;
          mediaBonusSum += (ch?.mediaImageBonus || 3);
        });
        const avgAffinity = Math.max(0.7, affinitySum / channels.length);
        const cost = channels.reduce((s, k) => {
          const ch = CHANNELS.find(c => c.key === k);
          return s + (ch ? ch.costCoins : 0);
        }, 0);

        if (roll < topic.riskChance) {
          fb = {
            hasBackfired:    true,
            badgeColor:      '#F87171',
            badgeText:       '🚨 NARRATIVE COLLAPSE',
            headline:        topic.backfireHeadline,
            costCoins:       cost,
            supportDelta:    topic.backfireEffects?.support || -1.5,
            mediaImageDelta: topic.backfireEffects?.mediaImage || -5,
            pressureDelta:   topic.backfireEffects?.pressure || 2,
          };
        } else {
          fb = {
            hasBackfired:    false,
            badgeColor:      '#4ADE80',
            badgeText:       '✅ ON AIR',
            headline:        topic.successHeadline,
            costCoins:       cost,
            supportDelta:    +(topic.baseSupport * avgAffinity).toFixed(1),
            mediaImageDelta: +(topic.baseMediaImage + mediaBonusSum),
            pressureDelta:   +(topic.basePressure * avgAffinity).toFixed(1),
          };
        }
      }

      setFeedback(fb);
      setFeedbackState('revealed');

      try {
        localStorage.setItem(lockStorageKey, 'true');
        if (fb) localStorage.setItem(feedbackStorageKey, JSON.stringify(fb));
        localStorage.setItem(selectionStorageKey, JSON.stringify({ topicKey, channels, isNoSpend: noSpend }));
      } catch (_) {}
    } catch (err) {
      console.error('Media auto-lock failed:', err);
      setFeedbackState('idle');
    }
  }, [feedbackState, hasEnoughCoins, gameSessionId, turnNumber, currentParty, lockStorageKey, feedbackStorageKey, selectionStorageKey]);

  const prevTurnRef = useRef(turnNumber);
  const prevSessionRef = useRef(gameSessionId);

  // Sync state when turn changes or session changes
  useEffect(() => {
    const isNewTurn = prevTurnRef.current !== turnNumber || prevSessionRef.current !== gameSessionId;
    if (isNewTurn) {
      prevTurnRef.current = turnNumber;
      prevSessionRef.current = gameSessionId;

      const savedLock = localStorage.getItem(lockStorageKey);
      const savedFeedback = localStorage.getItem(feedbackStorageKey);
      const savedSelection = localStorage.getItem(selectionStorageKey);

      if (savedLock === 'true' && savedFeedback) {
        try {
          setFeedback(JSON.parse(savedFeedback));
          setFeedbackState('revealed');
          if (savedSelection) {
            const parsed = JSON.parse(savedSelection);
            if (parsed.topicKey) setSelectedTopicKey(parsed.topicKey);
            if (Array.isArray(parsed.channels)) setSelectedChannels(parsed.channels);
            setIsNoSpend(Boolean(parsed.isNoSpend));
          }
          return;
        } catch (_) {}
      }

      setFeedbackState('idle');
      setFeedback(null);
      setSelectedTopicKey('');
      setSelectedChannels([]);
      setIsNoSpend(false);
    }
  }, [turnNumber, gameSessionId, lockStorageKey, feedbackStorageKey, selectionStorageKey, setSelectedTopicKey, setSelectedChannels]);

  /** Select topic — if channels already set, auto-lock */
  const handleTopicSelect = useCallback((topicKey) => {
    if (isLocked || isCalculating) return;
    setSelectedTopicKey(topicKey);
    const channels = selectedChannels;
    const noSpend  = isNoSpend;
    if (noSpend || channels.length > 0) {
      setTimeout(() => handleAutoLock(topicKey, channels, noSpend), 50);
    }
  }, [isLocked, isCalculating, setSelectedTopicKey, selectedChannels, isNoSpend, handleAutoLock]);

  /** Toggle channel — if topic already set, auto-lock when 2 channels chosen or allow broadcast */
  const handleChannelToggleAndLock = useCallback((chKey) => {
    if (isLocked || isCalculating) return;
    setIsNoSpend(false);
    setSelectedChannels(prev => {
      const current = Array.isArray(prev) ? prev : [];
      let next;
      if (current.includes(chKey)) {
        next = current.filter(k => k !== chKey);
      } else if (current.length >= 2) {
        next = [current[1], chKey];
      } else {
        next = [...current, chKey];
      }
      if (next.length > 0 && selectedTopicKey) {
        setTimeout(() => handleAutoLock(selectedTopicKey, next, false), 50);
      }
      return next;
    });
  }, [isLocked, isCalculating, setSelectedChannels, selectedTopicKey, handleAutoLock]);

  /** No Spend toggle — auto-lock immediately if topic is set */
  const handleNoSpendAndLock = useCallback(() => {
    if (isLocked || isCalculating) return;
    const next = !isNoSpend;
    setIsNoSpend(next);
    setSelectedChannels([]);
    if (next && selectedTopicKey) {
      setTimeout(() => handleAutoLock(selectedTopicKey, [], true), 50);
    }
  }, [isLocked, isCalculating, isNoSpend, setSelectedChannels, selectedTopicKey, handleAutoLock]);

  const canAffordChannel = (chKey) => {
    const ch  = CHANNELS.find(c => c.key === chKey);
    const cost= ch ? ch.costCoins : 0;
    if (selectedChannels.includes(chKey)) return true;
    const currentCost = selectedChannels.reduce((s, k) => {
      const c2 = CHANNELS.find(c => c.key === k); return s + (c2 ? c2.costCoins : 0);
    }, 0);
    return availableFunds >= currentCost + cost;
  };

  const topicSelected = Boolean(selectedTopicKey);
  const channelReady  = isNoSpend || selectedChannels.length > 0;

  return (
    <div style={{ padding: '14px 16px 0' }}>

      {/* ── Header ── */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '14px' }}>
        <div>
          <div style={{ fontSize: '15px', fontWeight: 900, letterSpacing: '0.05em', textTransform: 'uppercase', color: '#60A5FA' }}>
            📡 Media & Narrative
          </div>
          <div style={{ fontSize: '11px', fontWeight: 800, color: '#FCD34D', marginTop: '2px' }}>
            🪙 Available: <strong>{availableFunds} Coins</strong>
          </div>
        </div>
        <div style={{
          background: 'rgba(96,165,250,0.1)', border: '1px solid rgba(96,165,250,0.25)',
          borderRadius: '10px', padding: '4px 10px', textAlign: 'right',
        }}>
          <div style={{ fontSize: '9px', color: '#94A3B8', fontWeight: 700, textTransform: 'uppercase' }}>Media</div>
          <div style={{ fontSize: '12px', fontWeight: 900, color: currentMediaImage >= 50 ? '#60A5FA' : '#F87171' }}>
            📢 {currentMediaImage}/100
          </div>
        </div>
      </div>

      {/* ── Step 1: Topic ── */}
      <div style={{ marginBottom: '14px' }}>
        <div style={{ fontSize: '11px', fontWeight: 800, color: '#94A3B8', letterSpacing: '0.06em', textTransform: 'uppercase', marginBottom: '8px' }}>
          1. Choose Narrative Topic
        </div>

        {!topicSelected && !isLocked && !isCalculating && (
          <div style={{ textAlign: 'center', fontSize: '12px', fontWeight: 700, color: '#60A5FA', opacity: 0.8, marginBottom: '8px' }}>
            👆 Tap a topic to run
          </div>
        )}

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '8px' }}>
          {availableTopics.map(topic => {
            const isSelected = selectedTopicKey === topic.key;
            const categoryLabel = getCategoryLabel(topic.category);
            const categoryIcon  = getCategoryIcon(topic.category);
            const isHighRisk    = topic.riskChance > 20;

            return (
              <div
                key={topic.key}
                onClick={() => handleTopicSelect(topic.key)}
                style={{
                  background:   isSelected
                    ? 'linear-gradient(145deg,rgba(37,99,235,0.22),rgba(30,58,138,0.32))'
                    : 'rgba(255,255,255,0.03)',
                  border:       `1.5px solid ${isSelected ? '#60A5FA' : 'rgba(255,255,255,0.08)'}`,
                  borderRadius: '10px',
                  padding:      '10px 10px',
                  cursor:       (isLocked || isCalculating) ? 'default' : 'pointer',
                  transition:   'all 0.15s ease',
                  boxShadow:    isSelected ? '0 0 12px rgba(96,165,250,0.22)' : 'none',
                  opacity:      (isLocked || isCalculating) && !isSelected ? 0.35 : 1,
                  touchAction:  'manipulation',
                  WebkitTapHighlightColor: 'transparent',
                }}
              >
                {/* Category chip + risk */}
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '5px' }}>
                  <span style={{
                    fontSize: '9px', fontWeight: 800, textTransform: 'uppercase',
                    color: '#93C5FD', background: 'rgba(59,130,246,0.15)',
                    padding: '2px 6px', borderRadius: '4px',
                  }}>
                    {categoryIcon} {categoryLabel}
                  </span>
                  <span style={{ fontSize: '9px', color: isHighRisk ? '#FCA5A5' : '#86EFAC', fontWeight: 700 }}>
                    {topic.riskChance}% risk
                  </span>
                </div>

                {/* Title only — no tagline, no stat row */}
                <div style={{
                  fontSize:   '12px',
                  fontWeight: 800,
                  color:      isSelected ? '#ffffff' : '#E2E8F0',
                  lineHeight: 1.3,
                }}>
                  {topic.title}
                </div>

                {/* Selected check */}
                {isSelected && (
                  <div style={{ marginTop: '6px', fontSize: '10px', fontWeight: 800, color: isLocked ? '#10B981' : '#60A5FA' }}>
                    {isLocked ? '🔒 Locked' : '✓ Selected'}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>

      {/* ── Step 2: Channels — appears after topic selected ── */}
      {(topicSelected || isLocked) && (
        <div style={{ marginBottom: '14px', animation: 'wr-fill-in 0.2s ease' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
            <div style={{ fontSize: '11px', fontWeight: 800, color: '#94A3B8', letterSpacing: '0.06em', textTransform: 'uppercase' }}>
              2. Deploy Channels {!isLocked && <span style={{ fontWeight: 400 }}>(pick up to 2)</span>}
            </div>
            {totalCost > 0 && (
              <span style={{ fontSize: '11px', fontWeight: 800, color: hasEnoughCoins ? '#FCD34D' : '#F87171' }}>
                {totalCost}C / {availableFunds}C
              </span>
            )}
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '7px', marginBottom: '7px' }}>
            {CHANNELS.map(ch => {
              const isSelected   = !isNoSpend && selectedChannels.includes(ch.key);
              const topicAff     = currentTopic?.channelAffinity?.[ch.key] || 1.0;
              const isHighAff    = topicAff >= 1.3;
              const affordable   = canAffordChannel(ch.key);

              return (
                <button
                  key={ch.key}
                  type="button"
                  disabled={isLocked || isCalculating || (!isSelected && !affordable)}
                  onClick={() => handleChannelToggleAndLock(ch.key)}
                  style={{
                    background:   isSelected
                      ? 'rgba(59,130,246,0.2)'
                      : 'rgba(255,255,255,0.03)',
                    border:       `1.5px solid ${isSelected ? '#3B82F6' : 'rgba(255,255,255,0.08)'}`,
                    borderRadius: '10px',
                    padding:      '9px 10px',
                    textAlign:    'left',
                    cursor:       (isLocked || isCalculating || (!isSelected && !affordable)) ? 'default' : 'pointer',
                    display:      'flex', justifyContent: 'space-between', alignItems: 'center',
                    transition:   'all 0.15s ease',
                    opacity:      (isLocked || isCalculating) && !isSelected ? 0.32
                      : (!affordable && !isSelected) ? 0.4 : 1,
                    touchAction:  'manipulation',
                    fontFamily:   'Montserrat,system-ui,sans-serif',
                  }}
                >
                  <div>
                    <div style={{ fontSize: '12px', fontWeight: 800, color: isSelected ? '#ffffff' : '#CBD5E1', display: 'flex', alignItems: 'center', gap: '5px' }}>
                      <span>{ch.icon}</span>
                      <span>{getChannelShortName(ch.key)}</span>
                    </div>
                    {isHighAff && (
                      <div style={{ fontSize: '9px', color: '#86EFAC', marginTop: '2px', fontWeight: 700 }}>
                        🔥 {topicAff}x match
                      </div>
                    )}
                  </div>
                  <div style={{
                    fontSize: '11px', fontWeight: 800,
                    color:    isSelected ? '#FCD34D' : '#94A3B8',
                    background: 'rgba(0,0,0,0.25)',
                    padding:  '2px 6px', borderRadius: '5px',
                  }}>
                    {ch.costCoins}C
                  </div>
                </button>
              );
            })}
          </div>

          {/* No Spend option */}
          <div
            onClick={handleNoSpendAndLock}
            style={{
              background:   isNoSpend ? 'rgba(239,68,68,0.1)' : 'rgba(255,255,255,0.02)',
              border:       `1px solid ${isNoSpend ? 'rgba(239,68,68,0.35)' : 'rgba(255,255,255,0.06)'}`,
              borderRadius: '8px', padding: '7px 10px',
              display:      'flex', alignItems: 'center', justifyContent: 'space-between',
              cursor:       (isLocked || isCalculating) ? 'default' : 'pointer',
              touchAction:  'manipulation',
            }}
          >
            <span style={{ fontSize: '11px', fontWeight: 700, color: isNoSpend ? '#FCA5A5' : '#64748B' }}>
              {isNoSpend ? '🛑' : '○'} No Media Spend
            </span>
            <span style={{ fontSize: '10px', color: '#F87171', fontWeight: 700 }}>−2% Support</span>
          </div>

          {/* Insufficient funds warning */}
          {!isNoSpend && !hasEnoughCoins && selectedChannels.length > 0 && !isLocked && (
            <div style={{ fontSize: '11px', color: '#F87171', fontWeight: 700, marginTop: '6px', textAlign: 'center' }}>
              ⚠️ Not enough coins — reduce channels or choose No Media Spend
            </div>
          )}
        </div>
      )}

      {/* ── Option B: Calculating ── */}
      {isCalculating && (
        <div style={{
          margin: '10px 0', padding: '11px 14px', borderRadius: '12px',
          background: 'rgba(96,165,250,0.07)', border: '1.5px solid rgba(96,165,250,0.22)',
          display: 'flex', alignItems: 'center', gap: '10px',
          animation: 'wr-fill-in 0.15s ease',
        }}>
          <span style={{ fontSize: '16px', display: 'inline-block', animation: 'wr-spin 0.7s linear infinite' }}>⚙️</span>
          <span style={{ fontSize: '12px', fontWeight: 800, color: '#93C5FD' }}>Broadcasting campaign…</span>
        </div>
      )}

      {/* ── Compact result: headline + 3 pills ── */}
      {isLocked && feedback && (
        <div style={{
          margin: '10px 0', padding: '12px 14px', borderRadius: '12px',
          background: feedback.hasBackfired ? 'rgba(239,68,68,0.10)' : 'rgba(34,197,94,0.08)',
          border: `1.5px solid ${feedback.badgeColor}`,
          boxShadow: `0 0 12px ${feedback.badgeColor}25`,
          animation: 'wr-fill-in 0.25s ease',
        }}>
          {/* Headline row */}
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '7px' }}>
            <span style={{ fontSize: '11px', fontWeight: 900, letterSpacing: '0.04em', textTransform: 'uppercase', color: feedback.badgeColor }}>
              {feedback.badgeText}
            </span>
            {feedback.costCoins > 0 && (
              <span style={{ fontSize: '11px', fontWeight: 800, color: '#FCD34D' }}>−{feedback.costCoins}C</span>
            )}
          </div>

          {/* Stat pills */}
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '5px' }}>
            <span style={{
              fontSize: '11px', fontWeight: 800, padding: '3px 7px', borderRadius: '6px',
              background: feedback.supportDelta >= 0 ? 'rgba(34,197,94,0.18)' : 'rgba(239,68,68,0.18)',
              color:      feedback.supportDelta >= 0 ? '#4ADE80' : '#F87171',
              border:     `1px solid ${feedback.supportDelta >= 0 ? 'rgba(34,197,94,0.35)' : 'rgba(239,68,68,0.35)'}`,
            }}>
              {feedback.supportDelta >= 0 ? `+${feedback.supportDelta}` : feedback.supportDelta}% Support
            </span>
            <span style={{
              fontSize: '11px', fontWeight: 800, padding: '3px 7px', borderRadius: '6px',
              background: feedback.mediaImageDelta >= 0 ? 'rgba(96,165,250,0.18)' : 'rgba(239,68,68,0.18)',
              color:      feedback.mediaImageDelta >= 0 ? '#60A5FA' : '#F87171',
              border:     `1px solid ${feedback.mediaImageDelta >= 0 ? 'rgba(96,165,250,0.35)' : 'rgba(239,68,68,0.35)'}`,
            }}>
              {feedback.mediaImageDelta >= 0 ? `+${feedback.mediaImageDelta}` : feedback.mediaImageDelta} Media
            </span>
            <span style={{
              fontSize: '11px', fontWeight: 800, padding: '3px 7px', borderRadius: '6px',
              background: feedback.pressureDelta >= 0 ? 'rgba(245,158,11,0.18)' : 'rgba(239,68,68,0.18)',
              color:      feedback.pressureDelta >= 0 ? '#FCD34D' : '#F87171',
              border:     `1px solid ${feedback.pressureDelta >= 0 ? 'rgba(245,158,11,0.35)' : 'rgba(239,68,68,0.35)'}`,
            }}>
              {feedback.pressureDelta >= 0 ? `+${feedback.pressureDelta}` : feedback.pressureDelta} Pressure
            </span>
          </div>

        </div>
      )}
    </div>
  );
}
