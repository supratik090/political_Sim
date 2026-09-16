import React from 'react';
import { cardRequiresTarget, formatEffectValue } from '../gameUtils';
import { useHorizontalScroll } from '../../../hooks/useHorizontalScroll';

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
  const selfEffects   = card.visibleEffects?.selfParty     ? Object.entries(card.visibleEffects.selfParty)     : [];
  const oppEffects    = card.visibleEffects?.opponentParty ? Object.entries(card.visibleEffects.opponentParty) : [];
  const selfPositive  = selfEffects.some(([, v]) => v > 0);
  const oppNegative   = oppEffects.some(([, v])  => v < 0);
  return { selfPositive, oppNegative, selfEffects, oppEffects };
}

/**
 * WR_Action1_Card — Play Your Card
 * Props: { turnData, selectedCard, setSelectedCard, targetPartyId, setTargetPartyId, cardCategoryFilter, setCardCategoryFilter }
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

  const allCards = turnData?.availableCards || [];
  const filtered = blocked
    ? allCards.filter(c => c.cardKey === 'no_card')
    : cardCategoryFilter === 'ALL'
      ? allCards
      : allCards.filter(c => c.category?.toLowerCase() === cardCategoryFilter?.toLowerCase());

  const cardCarouselRef = useHorizontalScroll();

  return (
    <div style={{ padding: '14px 16px 0' }}>
      {/* Section header */}
      <div style={{ marginBottom: '10px' }}>
        <div style={{ fontSize: '15px', fontWeight: 900, letterSpacing: '0.05em', textTransform: 'uppercase', color: '#F59E0B' }}>
          🃏 Play Your Card
        </div>
        <div style={{ fontSize: '12px', color: '#7D8590', marginTop: '2px' }}>
          Choose your political move for this month
        </div>
      </div>

      {/* Freeze warning */}
      {blocked && (
        <div className="wr-freeze-banner">
          ⚠️ FREEZE IN EFFECT: Card play blocked for {activeParty.blockCardsTurns} more turn(s). Only "Pass Turn" allowed.
        </div>
      )}

      {/* Category filter chips — wrapped 2-line layout */}
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px 10px', marginTop: '12px', marginBottom: '20px', paddingBottom: '4px' }}>
        {CATEGORY_CONFIG.map(cat => {
          const isActive = cardCategoryFilter === cat.key;
          return (
            <button
              key={cat.key}
              onClick={() => setCardCategoryFilter(cat.key)}
              className="wr-chip"
              style={{
                background: isActive ? cat.color : 'rgba(255,255,255,0.05)',
                borderColor: isActive ? cat.color : 'rgba(255,255,255,0.12)',
                color: isActive ? '#ffffff' : '#8B949E',
                boxShadow: isActive ? `0 0 10px ${cat.color}80` : 'none',
                transform: isActive ? 'scale(1.05)' : 'scale(1)',
                fontFamily: 'Montserrat, system-ui, sans-serif',
              }}
            >
              {cat.icon} {cat.label}
            </button>
          );
        })}
      </div>

      {/* Card carousel */}
      {filtered.length === 0 ? (
        <div style={{ textAlign: 'center', padding: '30px 0', color: '#7D8590', fontSize: '13px', fontStyle: 'italic' }}>
          No cards in this category.
        </div>
      ) : (
        <div ref={cardCarouselRef} className="wr-hscroll" style={{ alignItems: 'center', paddingBottom: '12px', paddingTop: '6px', paddingLeft: '2px', paddingRight: '16px', gap: '12px' }}>
          {filtered.map(card => {
            const isSelected = selectedCard?.cardKey === card.cardKey;
            const { selfPositive, oppNegative } = getEffectSummary(card);
            const cardBg = getCategoryBg(card.category);

            return (
              <div
                key={card.cardKey}
                onClick={() => { setSelectedCard(card); setTargetPartyId(''); }}
                className={`wr-play-card ${isSelected ? 'wr-play-card-selected wr-anim-card-glow' : 'wr-play-card-unselected'}`}
                style={{ background: cardBg }}
              >
                {/* Category label */}
                <div style={{ fontSize: '10px', fontWeight: 700, letterSpacing: '0.07em', textTransform: 'uppercase', color: 'rgba(255,255,255,0.65)', marginBottom: '8px' }}>
                  {card.category?.replace(/_/g, ' ')}
                </div>

                {/* Card name */}
                <div style={{ fontSize: '14px', fontWeight: 900, color: '#ffffff', lineHeight: 1.3, flex: 1 }}>
                  {card.name}
                </div>

                {/* Divider */}
                <div style={{ height: '1px', background: 'rgba(255,255,255,0.15)', margin: '8px 0' }} />

                {/* Cost */}
                <div style={{ fontSize: '12px', fontWeight: 700, color: 'rgba(255,255,255,0.8)', marginBottom: '8px' }}>
                  💰 {card.cost} Coins
                </div>

                {/* Effect badges */}
                <div style={{ display: 'flex', flexWrap: 'wrap', gap: '4px' }}>
                  {selfPositive && (
                    <span className="wr-badge wr-badge-green">+Self</span>
                  )}
                  {oppNegative && (
                    <span className="wr-badge wr-badge-red">-Opp</span>
                  )}
                  {!selfPositive && !oppNegative && (
                    <span className="wr-badge wr-badge-amber">Neutral</span>
                  )}
                </div>

                {/* Selected check */}
                {isSelected && (
                  <div style={{
                    position: 'absolute', top: '8px', right: '8px',
                    width: '20px', height: '20px', borderRadius: '50%',
                    background: '#F59E0B', display: 'flex', alignItems: 'center', justifyContent: 'center',
                    fontSize: '12px', fontWeight: 900,
                  }}>
                    ✓
                  </div>
                )}
              </div>
            );
          })}
        </div>
      )}

      {/* Selected card summary */}
      {selectedCard && (
        <div style={{
          margin: '4px 0 12px',
          padding: '10px 14px',
          background: 'rgba(245,158,11,0.08)',
          border: '1px solid rgba(245,158,11,0.25)',
          borderRadius: '10px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          gap: '10px',
        }}>
          <span style={{ fontSize: '13px', color: '#E6EDF3', fontWeight: 700 }}>
            Selected: <span style={{ color: '#F59E0B' }}>{selectedCard.name}</span>
          </span>
          <button
            onClick={() => { setSelectedCard(null); setTargetPartyId(''); }}
            style={{
              background: 'transparent',
              border: '1px solid rgba(220,38,38,0.4)',
              borderRadius: '8px',
              color: '#F87171',
              fontSize: '12px',
              fontWeight: 700,
              padding: '6px 12px',
              cursor: 'pointer',
              minHeight: 'unset',
              fontFamily: 'Montserrat,system-ui,sans-serif',
            }}
          >
            ✕ Clear
          </button>
        </div>
      )}

      {/* Target selector — appears when offensive card selected */}
      {selectedCard && cardRequiresTarget(selectedCard) && (
        <div style={{
          marginBottom: '14px',
          padding: '14px',
          background: 'rgba(255,255,255,0.03)',
          border: '1.5px solid rgba(255,255,255,0.1)',
          borderRadius: '14px',
        }}>
          <div style={{ fontSize: '12px', fontWeight: 800, letterSpacing: '0.06em', textTransform: 'uppercase', color: '#F59E0B', marginBottom: '12px' }}>
            🎯 Select Target
          </div>
          <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
            {opponents.map(opp => {
              const isTargeted = targetPartyId === opp.id;
              const partyInitial = (opp.name || '?')[0]?.toUpperCase();
              return (
                <button
                  key={opp.id}
                  onClick={() => setTargetPartyId(opp.id)}
                  style={{
                    width: '76px',
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    gap: '6px',
                    padding: '10px 6px',
                    background: isTargeted ? 'rgba(245,158,11,0.12)' : 'rgba(255,255,255,0.04)',
                    border: `2px solid ${isTargeted ? '#F59E0B' : 'rgba(255,255,255,0.1)'}`,
                    borderRadius: '12px',
                    boxShadow: isTargeted ? '0 0 12px rgba(245,158,11,0.4)' : 'none',
                    cursor: 'pointer',
                    touchAction: 'manipulation',
                    WebkitTapHighlightColor: 'transparent',
                    transition: 'all 0.15s ease',
                    minHeight: 'unset',
                    fontFamily: 'Montserrat,system-ui,sans-serif',
                  }}
                >
                  <div style={{
                    width: '38px', height: '38px', borderRadius: '50%',
                    background: `var(--party-primary-color, #6C3AB5)`,
                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                    fontSize: '16px', fontWeight: 900, color: '#ffffff',
                    border: isTargeted ? '2px solid #F59E0B' : '2px solid rgba(255,255,255,0.15)',
                  }}>
                    {partyInitial}
                  </div>
                  <span style={{ fontSize: '10px', fontWeight: 700, color: '#C9D1D9', textAlign: 'center', lineHeight: 1.2 }}>
                    {opp.name?.split(' ')[0]}
                  </span>
                  {isTargeted && <span style={{ fontSize: '10px', color: '#F59E0B' }}>✓</span>}
                </button>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
}
