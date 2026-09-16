import React from 'react';
import { cardRequiresTarget, formatEffectValue } from './gameUtils';
import { getSymbolIconComponent } from '../../constants/partyThemes';

export default function Action1CardSelection({
  turnData,
  selectedCard,
  setSelectedCard,
  targetPartyId,
  setTargetPartyId,
  cardCategoryFilter,
  setCardCategoryFilter
}) {
  const activeParty = turnData?.parties?.find(p => p.id === turnData.activeHumanPartyId) || turnData?.parties?.find(p => p.playerControlled);
  const SymbolIcon = getSymbolIconComponent(activeParty?.symbol || 'Flag');

  return (
    <div>
      {turnData.turnNumber <= 2 && (
        <p style={{ margin: '0 0 15px 0', fontSize: '13px', color: 'var(--card-text)' }}>
          Draft and execute a political action card. Offensive cards require targeting an opponent.
        </p>
      )}

      {/* Card Category Filter Bar — 2 lines wrapped layout */}
      <div className="card-filter-bar">
        {[
          { key: 'governance', label: 'Governance 🏙️' },
          { key: 'agitation_movement', label: 'Agitation ✊' },
          { key: 'positive_service', label: 'Welfare 🤝' },
          { key: 'media_narrative', label: 'Media 📢' },
          { key: 'organization_resource', label: 'Organization 🏢' },
          { key: 'ideology_identity', label: 'Ideology ⚡' },
          { key: 'scandal_accusation', label: 'Scandal 🔍' },
          { key: 'defensive_counter', label: 'Defense 🛡️' },
          { key: 'ALL', label: 'All 🃏' }
        ].map(cat => {
          const isActive = cardCategoryFilter === cat.key;
          return (
            <button
              key={cat.key}
              onClick={() => setCardCategoryFilter(cat.key)}
              className="card-filter-pill"
              style={{
                background: isActive ? 'var(--party-primary-color, var(--primary-dark))' : '#ffffff',
                color: isActive ? '#ffffff' : 'var(--party-primary-color, var(--primary-dark))',
                borderColor: isActive ? 'var(--party-primary-color, var(--primary-dark))' : 'rgba(var(--party-primary-color-rgb, 101, 148, 177), 0.4)',
                boxShadow: isActive ? '0 2px 8px rgba(var(--party-primary-color-rgb, 101, 148, 177), 0.25)' : 'none'
              }}
            >
              {cat.label}
            </button>
          );
        })}
      </div>

      {activeParty?.blockCardsTurns > 0 && (
        <div style={{ background: '#fef2f2', border: '1.5px solid #ef4444', color: '#991b1b', padding: '12px 15px', borderRadius: '8px', marginBottom: '15px', fontSize: '13px', fontWeight: 'bold' }}>
          ⚠️ FREEZE IN EFFECT: Card play is blocked for {activeParty.blockCardsTurns} more turns by opponent's special reward. Only "No Card" (Pass Turn) is allowed.
        </div>
      )}

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '15px', marginBottom: '15px' }}>
        {(() => {
          let filtered = (turnData.availableCards || []).filter(card => {
            if (cardCategoryFilter === 'ALL') return true;
            return card.category?.toLowerCase() === cardCategoryFilter?.toLowerCase();
          });

          if (activeParty?.blockCardsTurns > 0) {
            filtered = (turnData.availableCards || []).filter(card => card.cardKey === 'no_card');
          }

          if (filtered.length === 0) {
            return (
              <p style={{ color: 'gray', fontStyle: 'italic', fontSize: '13px', textAlign: 'center', width: '100%', gridColumn: '1 / -1', padding: '20px 0' }}>
                No cards available in this category.
              </p>
            );
          }

          return filtered.map(card => {
            const isCardSelected = selectedCard?.cardKey === card.cardKey;
            const selfEffects = card.visibleEffects?.selfParty ? Object.entries(card.visibleEffects.selfParty) : [];
            const oppEffects = card.visibleEffects?.opponentParty ? Object.entries(card.visibleEffects.opponentParty) : [];

            return (
              <div 
                key={card.cardKey}
                onClick={() => {
                  setSelectedCard(card);
                  setTargetPartyId('');
                }}
                className="themed-action-card"
                style={{
                  border: isCardSelected ? '2.5px solid var(--party-primary-color)' : '1.5px solid rgba(var(--party-primary-color-rgb, 101, 148, 177), 0.15)',
                  borderRadius: '10px',
                  padding: '14px 14px 18px 14px',
                  minHeight: '110px',
                  background: isCardSelected ? 'rgba(var(--party-primary-color-rgb, 101, 148, 177), 0.08)' : '#ffffff',
                  cursor: 'pointer',
                  transition: 'all 0.2s ease',
                  boxShadow: isCardSelected ? '0 8px 16px rgba(var(--party-primary-color-rgb, 101, 148, 177), 0.25)' : '0 2px 4px rgba(0,0,0,0.05)',
                  position: 'relative',
                  overflow: 'hidden',
                  transform: isCardSelected ? 'scale(1.02)' : 'scale(1)'
                }}
              >
                {/* Background Watermark */}
                <div className="themed-card-watermark">
                  <SymbolIcon size={80} color="var(--party-primary-color)" />
                </div>

                {/* Bottom Right Corner Ribbon */}
                <div className="themed-card-ribbon">
                  <SymbolIcon size={12} color="#ffffff" style={{ marginRight: '1px', marginBottom: '1px', filter: 'brightness(0) invert(1)' }} />
                </div>

                <div style={{ position: 'relative', zIndex: 2 }}>
                  <div style={{ fontSize: '12px', color: 'var(--party-primary-color)', textTransform: 'uppercase', fontWeight: '700', letterSpacing: '0.06em' }}>{card.category?.replace('_', ' ')}</div>
                  <div style={{ fontSize: '15px', fontWeight: '800', margin: '6px 0 8px 0', color: 'var(--primary-dark)', lineHeight: 1.3, display: 'flex', alignItems: 'center', gap: '6px' }}>
                    <SymbolIcon size={16} color="var(--party-primary-color)" />
                    <span>{card.name}</span>
                  </div>
                  <div style={{ fontSize: '13px', color: 'var(--card-text)', fontWeight: '600' }}>Cost: <b>{card.cost} Coins</b></div>
                  {card.visibleEffects && (
                    <div style={{ marginTop: '10px', fontSize: '12px', background: 'rgba(0,0,0,0.03)', padding: '8px', borderRadius: '6px', display: 'flex', flexDirection: 'column', gap: '6px', lineHeight: 1.4 }}>
                      <div style={{ color: '#0d9488', fontWeight: 'bold' }}>
                        Self: {selfEffects.length > 0 ? selfEffects.map(([key, val]) => formatEffectValue(key, val)).join('   ') : 'None'}
                      </div>
                      <div style={{ color: '#be123c', fontWeight: 'bold' }}>
                        Opposition: {oppEffects.length > 0 ? oppEffects.map(([key, val]) => formatEffectValue(key, val)).join('   ') : 'None'}
                      </div>
                    </div>
                  )}
                </div>
              </div>
            );
          });
        })()}
      </div>

      {selectedCard && cardRequiresTarget(selectedCard) && (
        <div style={{ marginTop: '15px', padding: '12px', border: '1px dashed var(--primary-border)', borderRadius: '8px', background: 'rgba(101, 148, 177, 0.03)' }}>
          <label style={{ fontSize: '12px', fontWeight: 'bold', display: 'block', marginBottom: '8px', color: 'var(--primary-dark)' }}>
            🎯 Select Opponent Target:
          </label>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(130px, 1fr))', gap: '8px' }}>
            {turnData.parties.filter(p => p.id !== turnData.activeHumanPartyId).map(opp => {
              const isSelected = targetPartyId === opp.id;
              return (
                <div
                  key={opp.id}
                  onClick={() => setTargetPartyId(opp.id)}
                  style={{
                    padding: '10px 12px',
                    borderRadius: '8px',
                    border: isSelected ? `2px solid ${opp.color || 'var(--primary-dark)'}` : '1.5px solid var(--primary-border)',
                    background: isSelected ? `${opp.color || 'var(--primary-dark)'}14` : '#ffffff',
                    cursor: 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    transition: 'all 0.15s ease'
                  }}
                >
                  <div>
                    <strong style={{ display: 'block', fontSize: '13px', color: '#0f172a' }}>{opp.symbol || '🏛️'} {opp.name}</strong>
                    <span style={{ fontSize: '11px', color: '#64748b' }}>{opp.role}</span>
                  </div>
                  {isSelected && <span style={{ color: opp.color || 'var(--primary-dark)', fontWeight: 'bold', fontSize: '14px' }}>✓</span>}
                </div>
              );
            })}
          </div>
        </div>
      )}

      {selectedCard && (
        <div style={{ marginTop: '15px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <span style={{ fontSize: '13px', color: 'var(--primary-dark)', fontWeight: '600' }}>
            Selected Move: <b>{selectedCard.name}</b>
          </span>
          <button 
            onClick={() => {
              setSelectedCard(null);
              setTargetPartyId('');
            }}
            style={{ padding: '8px 14px', fontSize: '13px', background: 'transparent', color: '#d23f31', border: '1.5px solid #d23f31', minHeight: '38px' }}
          >
            Deselect
          </button>
        </div>
      )}
    </div>
  );
}
