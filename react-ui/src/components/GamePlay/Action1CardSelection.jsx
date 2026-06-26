import React from 'react';
import { cardRequiresTarget, formatEffectValue } from './gameUtils';

export default function Action1CardSelection({
  turnData,
  selectedCard,
  setSelectedCard,
  targetPartyId,
  setTargetPartyId,
  cardCategoryFilter,
  setCardCategoryFilter
}) {
  return (
    <div>
      {turnData.turnNumber <= 2 && (
        <p style={{ margin: '0 0 15px 0', fontSize: '13px', color: 'var(--card-text)' }}>
          Draft and execute a political action card. Offensive cards require targeting an opponent.
        </p>
      )}
      {/* Card Category Filter Bar */}
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px', marginBottom: '20px', borderBottom: '1px solid var(--primary-border)', paddingBottom: '12px' }}>
        {[
          { key: 'agitation_movement', label: 'Agitation ✊' },
          { key: 'governance', label: 'Governance 🏛️' },
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
              style={{
                padding: '6px 14px',
                fontSize: '11px',
                background: isActive ? 'var(--button-hover-bg)' : 'var(--primary-dark)',
                color: '#ffffff',
                border: isActive ? '1.5px solid var(--selected-highlight)' : '1.5px solid var(--primary-border)',
                boxShadow: 'none',
                borderRadius: '20px',
                fontWeight: 'bold',
                transition: 'all 0.2s ease',
                transform: 'none',
                cursor: 'pointer'
              }}
            >
              {cat.label}
            </button>
          );
        })}
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '15px', marginBottom: '15px' }}>
        {(() => {
          const filtered = (turnData.availableCards || []).filter(card => {
            if (cardCategoryFilter === 'ALL') return true;
            return card.category?.toLowerCase() === cardCategoryFilter?.toLowerCase();
          });

          if (filtered.length === 0) {
            return (
              <p style={{ color: 'var(--text-secondary)', fontStyle: 'italic', fontSize: '13px', textAlign: 'center', width: '100%', gridColumn: '1 / -1', padding: '20px 0' }}>
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
                style={{
                  border: isCardSelected ? '2px solid var(--selected-highlight)' : '1.5px solid var(--primary-border)',
                  borderRadius: '10px',
                  padding: '12px',
                  background: isCardSelected ? 'rgba(56, 189, 248, 0.2)' : '#334155',
                  cursor: 'pointer',
                  transition: 'all 0.2s ease',
                  boxShadow: isCardSelected ? '0 4px 15px rgba(56, 189, 248, 0.2)' : 'none'
                }}
                onMouseEnter={(e) => {
                  if (!isCardSelected) e.currentTarget.style.background = '#475569';
                }}
                onMouseLeave={(e) => {
                  if (!isCardSelected) e.currentTarget.style.background = '#334155';
                }}
              >
                <div style={{ fontSize: '10px', color: 'var(--text-secondary)', opacity: 0.8, textTransform: 'uppercase', fontWeight: 'bold' }}>{card.category?.replace('_', ' ')}</div>
                <div style={{ fontSize: '14px', fontWeight: 'bold', margin: '4px 0 6px 0', color: 'var(--text-primary)' }}>🃏 {card.name}</div>
                <div style={{ fontSize: '11px', color: 'var(--text-secondary)' }}>Cost: <b style={{ color: 'var(--text-primary)' }}>{card.cost} Coins</b></div>
                {card.visibleEffects && (
                  <div style={{ marginTop: '8px', fontSize: '11px', background: 'rgba(0,0,0,0.2)', padding: '6px', borderRadius: '6px', display: 'flex', flexDirection: 'column', gap: '4px' }}>
                    <div style={{ color: '#22c55e', fontWeight: 'bold' }}>
                      Self: {selfEffects.length > 0 ? selfEffects.map(([key, val]) => formatEffectValue(key, val)).join('   ') : 'None'}
                    </div>
                    <div style={{ color: '#ef4444', fontWeight: 'bold' }}>
                      Opposition: {oppEffects.length > 0 ? oppEffects.map(([key, val]) => formatEffectValue(key, val)).join('   ') : 'None'}
                    </div>
                  </div>
                )}
              </div>
            );
          });
        })()}
      </div>

      {selectedCard && cardRequiresTarget(selectedCard) && (
        <div style={{ marginTop: '15px', padding: '12px', border: '1px dashed var(--primary-border)', borderRadius: '8px', background: 'rgba(99, 102, 241, 0.03)' }}>
          <label htmlFor="card-target-select" style={{ fontSize: '12px', fontWeight: 'bold', display: 'block', marginBottom: '6px', color: 'var(--text-secondary)' }}>
            🎯 Select Opponent Target:
          </label>
          <select 
            id="card-target-select"
            value={targetPartyId}
            onChange={(e) => setTargetPartyId(e.target.value)}
            style={{
              width: '100%',
              padding: '10px',
              borderRadius: '6px',
              border: '1.5px solid var(--primary-border)',
              background: 'var(--primary-dark)',
              color: '#ffffff',
              fontSize: '13px',
              outline: 'none'
            }}
          >
            <option value="">-- Choose Opponent Party --</option>
            {turnData.parties.filter(p => p.id !== turnData.activeHumanPartyId).map(opp => (
              <option key={opp.id} value={opp.id}>{opp.name} ({opp.role})</option>
            ))}
          </select>
        </div>
      )}

      {selectedCard && (
        <div style={{ marginTop: '15px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <span style={{ fontSize: '12px', color: 'var(--text-primary)' }}>
            Selected Move: <b>{selectedCard.name}</b>
          </span>
          <button 
            onClick={() => {
              setSelectedCard(null);
              setTargetPartyId('');
            }}
            style={{ padding: '6px 12px', fontSize: '11px', background: 'transparent', color: '#ef4444', border: '1px solid #ef4444' }}
          >
            Deselect
          </button>
        </div>
      )}
    </div>
  );
}
