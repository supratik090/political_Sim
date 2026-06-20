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
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px', marginBottom: '20px', borderBottom: '1px solid rgba(101, 148, 177, 0.2)', paddingBottom: '12px' }}>
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
                background: isActive ? 'var(--primary-dark)' : '#ffffff',
                color: isActive ? '#ffffff' : 'var(--primary-dark)',
                border: isActive ? '2px solid var(--primary-dark)' : '1px solid var(--primary-border)',
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
                style={{
                  border: isCardSelected ? '2px solid #a855f7' : '1.5px solid var(--primary-border)',
                  borderRadius: '10px',
                  padding: '12px',
                  background: isCardSelected ? '#e9d5ff' : '#f5f3ff',
                  cursor: 'pointer',
                  transition: 'all 0.2s ease',
                  boxShadow: isCardSelected ? '0 4px 12px rgba(168, 85, 247, 0.2)' : 'none'
                }}
                onMouseEnter={(e) => {
                  if (!isCardSelected) e.currentTarget.style.background = '#ede9fe';
                }}
                onMouseLeave={(e) => {
                  if (!isCardSelected) e.currentTarget.style.background = '#f5f3ff';
                }}
              >
                <div style={{ fontSize: '10px', color: 'var(--primary-dark)', opacity: 0.7, textTransform: 'uppercase', fontWeight: 'bold' }}>{card.category?.replace('_', ' ')}</div>
                <div style={{ fontSize: '14px', fontWeight: 'bold', margin: '4px 0 6px 0', color: 'var(--primary-dark)' }}>🃏 {card.name}</div>
                <div style={{ fontSize: '11px', color: 'var(--card-text)' }}>Cost: <b>{card.cost} Coins</b></div>
                {card.visibleEffects && (
                  <div style={{ marginTop: '8px', fontSize: '11px', background: 'rgba(0,0,0,0.03)', padding: '6px', borderRadius: '6px', display: 'flex', flexDirection: 'column', gap: '4px' }}>
                    <div style={{ color: '#0d9488', fontWeight: 'bold' }}>
                      Self: {selfEffects.length > 0 ? selfEffects.map(([key, val]) => formatEffectValue(key, val)).join('   ') : 'None'}
                    </div>
                    <div style={{ color: '#be123c', fontWeight: 'bold' }}>
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
        <div style={{ marginTop: '15px', padding: '12px', border: '1px dashed var(--primary-border)', borderRadius: '8px', background: 'rgba(101, 148, 177, 0.03)' }}>
          <label htmlFor="card-target-select" style={{ fontSize: '12px', fontWeight: 'bold', display: 'block', marginBottom: '6px', color: 'var(--primary-dark)' }}>
            🎯 Select Opponent Target:
          </label>
          <select 
            id="card-target-select"
            value={targetPartyId}
            onChange={(e) => setTargetPartyId(e.target.value)}
            style={{
              width: '100%',
              padding: '8px',
              borderRadius: '6px',
              border: '1px solid var(--primary-border)',
              background: '#ffffff',
              color: 'var(--primary-dark)',
              fontSize: '13px'
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
          <span style={{ fontSize: '12px', color: 'var(--primary-dark)' }}>
            Selected Move: <b>{selectedCard.name}</b>
          </span>
          <button 
            onClick={() => {
              setSelectedCard(null);
              setTargetPartyId('');
            }}
            style={{ padding: '6px 12px', fontSize: '11px', background: 'transparent', color: '#d23f31', border: '1px solid #d23f31' }}
          >
            Deselect
          </button>
        </div>
      )}
    </div>
  );
}
