import React, { useState, useCallback, useEffect } from 'react';
import { cardRequiresTarget, formatEffectValue } from '../gameUtils';
import { evaluateCardPlay } from '../../../utils/instantFeedbackEngine';
import { useHorizontalScroll } from '../../../hooks/useHorizontalScroll';
import { fetchCardFeedback } from '../../../api/apiClient';
import { getCachedCardFeedback, preloadTurnFeedback } from '../../../utils/turnFeedbackCache';

const CATEGORY_CONFIG = [
  { key: 'governance',            label: 'Governance', icon: '🏙️', color: '#7C3AED', bg: 'linear-gradient(145deg,#3b1d8e,#5b21b6)' },
  { key: 'agitation_movement',    label: 'Agitation',  icon: '✊',  color: '#DC2626', bg: 'linear-gradient(145deg,#7f1d1d,#b91c1c)' },
  { key: 'positive_service',      label: 'Welfare',    icon: '🤝',  color: '#059669', bg: 'linear-gradient(145deg,#064e3b,#059669)' },
  { key: 'media_narrative',       label: 'Media',      icon: '📢',  color: '#2563EB', bg: 'linear-gradient(145deg,#1e3a8a,#2563eb)' },
  { key: 'organization_resource', label: 'Org',        icon: '🏢',  color: '#0891B2', bg: 'linear-gradient(145deg,#164e63,#0891b2)' },
  { key: 'ideology_identity',     label: 'Ideology',   icon: '⚡',  color: '#D97706', bg: 'linear-gradient(145deg,#78350f,#d97706)' },
  { key: 'scandal_accusation',    label: 'Scandal',    icon: '🔍',  color: '#EA580C', bg: 'linear-gradient(145deg,#7c2d12,#ea580c)' },
  { key: 'defensive_counter',     label: 'Defense',    icon: '🛡️',  color: '#4B5563', bg: 'linear-gradient(145deg,#1f2937,#374151)' },
  { key: 'ALL',                   label: 'All',        icon: '🃏',  color: '#E6EDF3', bg: 'linear-gradient(145deg,#1a3448,#2d4a62)' },
];

function getCategoryBg(categoryKey) {
  const found = CATEGORY_CONFIG.find(c => c.key === categoryKey?.toLowerCase());
  return found ? found.bg : 'linear-gradient(145deg,#1a3448,#2d4a62)';
}

function getEffectSummary(card) {
  const selfEffects  = card.visibleEffects?.selfParty     ? Object.entries(card.visibleEffects.selfParty)     : [];
  const oppEffects   = card.visibleEffects?.opponentParty ? Object.entries(card.visibleEffects.opponentParty) : [];
  const selfPositive = selfEffects.some(([, v]) => v > 0);
  const oppNegative  = oppEffects.some(([, v])  => v < 0);
  return { selfPositive, oppNegative };
}

function getCardIcon(selfPositive, oppNegative) {
  if (selfPositive && oppNegative) return '⚔️';
  if (selfPositive) return '🛡️';
  if (oppNegative)  return '💥';
  return '⚡';
}

/**
 * WR_Action1_Card — Frictionless card play.
 * Flow: tap card → (if target needed: tap party) → auto-lock → reveal result → auto-scroll.
 * No manual Lock button. No noisy helper text.
 */
export default function WR_Action1_Card({
  turnData,
  selectedCard,
  setSelectedCard,
  targetPartyId,
  setTargetPartyId,
  cardCategoryFilter,
  setCardCategoryFilter,
}) {
  const activeParty = turnData?.parties?.find(p => p.id === turnData.activeHumanPartyId)
    || turnData?.parties?.find(p => p.playerControlled);
  const opponents   = (turnData?.parties || []).filter(p => p.id !== turnData?.activeHumanPartyId);
  const blocked     = activeParty?.blockCardsTurns > 0;

  const gameSessionId     = turnData?.gameId || turnData?.id || turnData?.scenarioId || 'default_session';
  const turnNumber        = turnData?.turnNumber || 0;
  const lockStorageKey    = `political_sim_card_locked_${gameSessionId}_turn_${turnNumber}`;
  const feedbackStorageKey= `political_sim_card_feedback_${gameSessionId}_turn_${turnNumber}`;
  const cardStorageKey    = `political_sim_card_selected_${gameSessionId}_turn_${turnNumber}`;
  const targetStorageKey  = `political_sim_card_target_${gameSessionId}_turn_${turnNumber}`;

  // 'idle' | 'calculating' | 'revealed'
  const [feedbackState, setFeedbackState] = useState(() => {
    try { return localStorage.getItem(lockStorageKey) === 'true' ? 'revealed' : 'idle'; } catch (_) { return 'idle'; }
  });

  const [cardFeedbackData, setCardFeedbackData] = useState(() => {
    try {
      const saved = localStorage.getItem(feedbackStorageKey);
      return saved ? JSON.parse(saved) : null;
    } catch (_) { return null; }
  });

  const isLocked = feedbackState === 'revealed';

  // Restore persisted card selection on mount
  useEffect(() => {
    if (!selectedCard) {
      try {
        const savedCard = localStorage.getItem(cardStorageKey);
        if (savedCard) {
          const parsed = JSON.parse(savedCard);
          if (parsed?.cardKey) setSelectedCard(parsed);
        }
      } catch (_) {}
    }
  }, [cardStorageKey, selectedCard, setSelectedCard]);

  useEffect(() => {
    if (!targetPartyId) {
      try {
        const savedTarget = localStorage.getItem(targetStorageKey);
        if (savedTarget) setTargetPartyId(savedTarget);
      } catch (_) {}
    }
  }, [targetStorageKey, targetPartyId, setTargetPartyId]);

  // Preload turn feedback cache in background
  useEffect(() => {
    const gameId  = turnData?.gameId || turnData?.id;
    const partyId = activeParty?.id;
    if (gameId && partyId) preloadTurnFeedback(gameId, partyId, turnNumber);
  }, [turnData?.gameId, turnData?.id, activeParty?.id, turnNumber]);

  /**
   * Core lock handler — called automatically once card (+ target if needed) is chosen.
   * Option B: 320ms calculating phase → then reveal.
   */
  const handleAutoLock = useCallback(async (card, target) => {
    if (feedbackState !== 'idle') return;
    setFeedbackState('calculating');

    // Option B dramatic pause — feels intentional, not laggy
    await new Promise(r => setTimeout(r, 320));

    try {
      const gameId  = turnData?.gameId || turnData?.id;
      const partyId = activeParty?.id;

      let fb = getCachedCardFeedback(gameId, turnNumber, partyId, card.cardKey, target || null);

      if (!fb) {
        try {
          const res = await fetchCardFeedback(gameId, {
            partyId,
            cardKey:       card.cardKey,
            targetPartyId: target || null,
          });
          if (res) {
            fb = {
              hasBackfired: res.backfired,
              badgeColor:   res.backfired ? '#F87171' : (res.tripleMultiplier ? '#F59E0B' : '#4ADE80'),
              badgeText:    res.headline || (res.backfired ? '🚨 BACKFIRE' : res.tripleMultiplier ? '🔥 CRITICAL HIT' : '✅ MOVE PLAYED'),
              summary:      res.narrative,
              cost:         res.cost,
              selfEffects:  res.selfDeltas    || {},
              oppEffects:   res.opponentDeltas || {},
              isBackend:    true,
            };
          }
        } catch (err) {
          console.warn('Backend card feedback fetch failed, using local engine:', err);
          const targetParty = opponents.find(p => p.id === target);
          fb = evaluateCardPlay(turnData, activeParty?.id, card, targetParty);
        }
      }

      setCardFeedbackData(fb);
      setFeedbackState('revealed');

      try {
        localStorage.setItem(lockStorageKey,     'true');
        if (fb)   localStorage.setItem(feedbackStorageKey, JSON.stringify(fb));
        if (card) localStorage.setItem(cardStorageKey,     JSON.stringify(card));
        localStorage.setItem(targetStorageKey, target || '');
      } catch (_) {}
    } catch (err) {
      console.error('Auto-lock failed:', err);
      setFeedbackState('idle');
    }
  }, [feedbackState, turnData, activeParty, opponents, turnNumber, lockStorageKey, feedbackStorageKey, cardStorageKey, targetStorageKey]);

  /** Tap a card — auto-lock immediately if no target needed, else show target picker. */
  const handleCardSelect = useCallback((card) => {
    if (feedbackState !== 'idle') return;
    setSelectedCard(card);
    setTargetPartyId('');
    try {
      localStorage.setItem(cardStorageKey,   JSON.stringify(card));
      localStorage.setItem(targetStorageKey, '');
    } catch (_) {}

    if (!cardRequiresTarget(card)) {
      handleAutoLock(card, null);
    }
    // If target required, wait — user will tap a party next
  }, [feedbackState, setSelectedCard, setTargetPartyId, cardStorageKey, targetStorageKey, handleAutoLock]);

  /** Tap a party avatar — auto-lock immediately. */
  const handleTargetSelect = useCallback((targetId) => {
    if (feedbackState !== 'idle' || !selectedCard) return;
    setTargetPartyId(targetId);
    try { localStorage.setItem(targetStorageKey, targetId); } catch (_) {}
    handleAutoLock(selectedCard, targetId);
  }, [feedbackState, selectedCard, setTargetPartyId, targetStorageKey, handleAutoLock]);

  const allCards = turnData?.availableCards || [];
  const filtered = blocked
    ? allCards.filter(c => c.cardKey === 'no_card')
    : cardCategoryFilter === 'ALL'
      ? allCards
      : allCards.filter(c => c.category?.toLowerCase() === cardCategoryFilter?.toLowerCase());

  const cardCarouselRef  = useHorizontalScroll();
  const needsTarget      = selectedCard && cardRequiresTarget(selectedCard);
  const isCalculating    = feedbackState === 'calculating';

  return (
    <div style={{ padding: '14px 16px 0' }}>

      {/* ── Section header ── */}
      <div style={{ fontSize: '15px', fontWeight: 900, letterSpacing: '0.05em', textTransform: 'uppercase', color: '#FF9933', marginBottom: '12px', display: 'flex', alignItems: 'center', gap: '6px' }}>
        ⭐ PLAY YOUR CARD
      </div>

      {/* ── Freeze warning ── */}
      {blocked && (
        <div className="wr-freeze-banner">
          ⚠️ FREEZE: Card play blocked for {activeParty.blockCardsTurns} more turn(s).
        </div>
      )}

      {/* ── Category filter chips — wrapped grid, no horizontal scroll ── */}
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px 7px', marginBottom: '14px' }}>
        {CATEGORY_CONFIG.map(cat => {
          const isActive = cardCategoryFilter === cat.key;
          return (
            <button
              key={cat.key}
              onClick={() => setCardCategoryFilter(cat.key)}
              className="wr-chip"
              style={{
                padding:     '4px 10px',
                minHeight:   '28px',
                fontSize:    '11px',
                background:  isActive ? cat.color : 'rgba(255,255,255,0.08)',
                borderColor: isActive ? cat.color : 'rgba(255,255,255,0.18)',
                color:       isActive ? '#ffffff' : '#CBD5E1',
                boxShadow:   isActive ? `0 0 8px ${cat.color}60` : 'none',
                transform:   isActive ? 'scale(1.03)' : 'scale(1)',
                fontFamily:  'Montserrat, system-ui, sans-serif',
              }}
            >
              {cat.icon} {cat.label}
            </button>
          );
        })}
      </div>

      {/* ── Prompt nudge — only when nothing is selected yet ── */}
      {!selectedCard && !isLocked && !isCalculating && (
        <div style={{
          textAlign:     'center',
          padding:       '6px 0 10px',
          color:         '#FF9933',
          fontSize:      '12px',
          fontWeight:    700,
          letterSpacing: '0.04em',
          opacity:       0.9,
        }}>
          👆 Tap a card to play it
        </div>
      )}

      {/* ── Card carousel ── */}
      {filtered.length === 0 ? (
        <div style={{ textAlign: 'center', padding: '30px 0', color: '#7D8590', fontSize: '13px', fontStyle: 'italic' }}>
          No cards in this category.
        </div>
      ) : (
        <div
          ref={cardCarouselRef}
          className="wr-hscroll wr-card-carousel-guide"
          style={{ paddingBottom: '12px', paddingTop: '4px', paddingLeft: '2px', paddingRight: '16px', gap: '10px', alignItems: 'center' }}
        >
          {filtered.map(card => {
            const isSelected = selectedCard?.cardKey === card.cardKey;
            const { selfPositive, oppNegative } = getEffectSummary(card);

            return (
              <div
                key={card.cardKey}
                onClick={() => handleCardSelect(card)}
                className={`wr-card-v2 ${isSelected ? 'wr-card-v2-selected wr-anim-card-glow' : 'wr-card-v2-idle'}`}
                style={{
                  background: getCategoryBg(card.category),
                  cursor:     (isLocked || isCalculating) ? 'default' : 'pointer',
                  opacity:    isLocked && !isSelected ? 0.32 : isCalculating && !isSelected ? 0.38 : 1,
                  filter:     isLocked && !isSelected ? 'grayscale(0.55)' : 'none',
                }}
              >
                {/* Category label */}
                <div style={{ fontSize: '9px', fontWeight: 700, letterSpacing: '0.07em', textTransform: 'uppercase', color: 'rgba(255,255,255,0.55)', marginBottom: '5px', lineHeight: 1.2 }}>
                  {card.category?.replace(/_/g, ' ')}
                </div>

                {/* Card name */}
                <div style={{ fontSize: '13px', fontWeight: 900, color: '#ffffff', lineHeight: 1.25, flex: 1 }}>
                  {card.name}
                </div>

                {/* Bottom row: cost pill + effect icon */}
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '8px' }}>
                  <span style={{
                    fontSize:   '10px', fontWeight: 800,
                    color:      'rgba(255,255,255,0.8)',
                    background: 'rgba(0,0,0,0.25)',
                    padding:    '2px 6px', borderRadius: '4px',
                  }}>
                    💰 {card.cost}C
                  </span>
                  <span style={{ fontSize: '14px', lineHeight: 1 }}>
                    {getCardIcon(selfPositive, oppNegative)}
                  </span>
                </div>

                {/* Selected / locked badge */}
                {isSelected && (
                  <div style={{
                    position: 'absolute', top: '5px', right: '5px',
                    width: '17px', height: '17px', borderRadius: '50%',
                    background: isLocked ? '#10B981' : '#F59E0B',
                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                    fontSize: '9px', fontWeight: 900,
                  }}>
                    {isLocked ? '🔒' : '✓'}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      )}

      {/* ── Inline target picker — slides in when an offensive card is tapped ── */}
      {needsTarget && feedbackState === 'idle' && (
        <div style={{
          margin:     '8px 0 12px',
          padding:    '12px 14px',
          background: 'rgba(245,158,11,0.06)',
          border:     '1.5px solid rgba(245,158,11,0.22)',
          borderRadius: '12px',
          animation:  'wr-fill-in 0.2s ease',
        }}>
          <div style={{ fontSize: '11px', fontWeight: 800, letterSpacing: '0.06em', textTransform: 'uppercase', color: '#F59E0B', marginBottom: '10px' }}>
            🎯 Target party
          </div>
          <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
            {opponents.map(opp => {
              const initial = (opp.name || '?')[0]?.toUpperCase();
              return (
                <button
                  key={opp.id}
                  onClick={() => handleTargetSelect(opp.id)}
                  style={{
                    width:       '64px',
                    display:     'flex', flexDirection: 'column', alignItems: 'center', gap: '5px',
                    padding:     '8px 4px',
                    background:  'rgba(255,255,255,0.04)',
                    border:      '2px solid rgba(255,255,255,0.1)',
                    borderRadius:'10px',
                    cursor:      'pointer',
                    touchAction: 'manipulation',
                    WebkitTapHighlightColor: 'transparent',
                    transition:  'all 0.15s ease',
                    fontFamily:  'Montserrat,system-ui,sans-serif',
                  }}
                >
                  <div style={{
                    width: '32px', height: '32px', borderRadius: '50%',
                    background: 'var(--party-primary-color, #6C3AB5)',
                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                    fontSize: '13px', fontWeight: 900, color: '#ffffff',
                  }}>
                    {initial}
                  </div>
                  <span style={{ fontSize: '10px', fontWeight: 700, color: '#C9D1D9', textAlign: 'center', lineHeight: 1.2 }}>
                    {opp.name?.split(' ')[0]}
                  </span>
                </button>
              );
            })}
          </div>
        </div>
      )}

      {/* ── Option B: Calculating pulse ── */}
      {isCalculating && (
        <div style={{
          margin:     '10px 0',
          padding:    '11px 14px',
          borderRadius: '12px',
          background: 'rgba(245,158,11,0.07)',
          border:     '1.5px solid rgba(245,158,11,0.22)',
          display:    'flex', alignItems: 'center', gap: '10px',
          animation:  'wr-fill-in 0.15s ease',
        }}>
          <span style={{ fontSize: '16px', display: 'inline-block', animation: 'wr-spin 0.7s linear infinite' }}>⚙️</span>
          <span style={{ fontSize: '12px', fontWeight: 800, color: '#FCD34D', letterSpacing: '0.03em' }}>
            Calculating impact…
          </span>
        </div>
      )}

      {/* ── Result panel — 1-line headline + compact stat pills, no narrative ── */}
      {feedbackState === 'revealed' && cardFeedbackData && (
        <div style={{
          margin:     '10px 0',
          padding:    '12px 14px',
          borderRadius: '12px',
          background: cardFeedbackData.hasBackfired ? 'rgba(239,68,68,0.10)' : 'rgba(34,197,94,0.08)',
          border:     `1.5px solid ${cardFeedbackData.badgeColor}`,
          boxShadow:  `0 0 12px ${cardFeedbackData.badgeColor}25`,
          animation:  'wr-fill-in 0.25s ease',
        }}>
          {/* Headline row */}
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px' }}>
            <span style={{
              fontSize:      '11px', fontWeight: 900,
              letterSpacing: '0.04em', textTransform: 'uppercase',
              color:         cardFeedbackData.badgeColor,
            }}>
              {cardFeedbackData.badgeText}
            </span>
            {cardFeedbackData.cost > 0 && (
              <span style={{ fontSize: '11px', fontWeight: 800, color: '#FCD34D' }}>
                −{cardFeedbackData.cost}C
              </span>
            )}
          </div>

          {/* Compact stat pills */}
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '5px' }}>
            {Object.entries(cardFeedbackData.selfEffects || {}).map(([k, v]) => {
              const val = Number(v);
              if (val === 0) return null;
              const isPos = k === 'corruptionScore' ? val < 0 : val > 0;
              return (
                <span key={`self-${k}`} style={{
                  fontSize:   '11px', fontWeight: 800,
                  padding:    '3px 7px', borderRadius: '6px',
                  background: isPos ? 'rgba(34,197,94,0.18)' : 'rgba(239,68,68,0.18)',
                  color:      isPos ? '#4ADE80' : '#F87171',
                  border:     `1px solid ${isPos ? 'rgba(34,197,94,0.35)' : 'rgba(239,68,68,0.35)'}`,
                }}>
                  You: {formatEffectValue(k, val)}
                </span>
              );
            })}
            {targetPartyId && Object.entries(cardFeedbackData.oppEffects || {}).map(([k, v]) => {
              const val = Number(v);
              if (val === 0) return null;
              const oppName = opponents.find(p => p.id === targetPartyId)?.name?.split(' ')[0] || 'Opp';
              return (
                <span key={`opp-${k}`} style={{
                  fontSize: '11px', fontWeight: 800,
                  padding:  '3px 7px', borderRadius: '6px',
                  background: 'rgba(239,68,68,0.18)', color: '#F87171',
                  border:   '1px solid rgba(239,68,68,0.35)',
                }}>
                  {oppName}: {formatEffectValue(k, val)}
                </span>
              );
            })}
          </div>
        </div>
      )}

    </div>
  );
}
