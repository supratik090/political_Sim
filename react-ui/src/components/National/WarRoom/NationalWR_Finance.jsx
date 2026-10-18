import React, { useState, useEffect } from 'react';
import {
  fetchNationalFinanceCards,
  playNationalFinanceCard,
  cancelNationalFinanceCard
} from '../../../api/apiClient';

export default function NationalWR_Finance({ activeGame, configData, onGameUpdate, isCompleted = false, onMarkCompleted }) {
  const [allCards, setAllCards] = useState([]);
  const [loading, setLoading] = useState(false);
  const [actionLoading, setActionLoading] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  const gameId = activeGame?.id || activeGame?._id || activeGame?.userId || 'local';

  // Find player's party state
  const playerPartyKey = activeGame?.partyKey;
  const playerState = activeGame?.partyStates?.find(
    p => (p.partyKey || '').toLowerCase() === (playerPartyKey || '').toLowerCase()
  ) || null;

  const currentFunds = playerState?.funds ?? activeGame?.playerFunds ?? 10.0;
  const startingFunds = playerState?.startingFunds ?? currentFunds;
  const workers = playerState?.workers ?? 50000;
  const volunteers = playerState?.volunteers ?? 15000;
  const donors = playerState?.donors ?? 1000;
  const morale = playerState?.morale ?? activeGame?.morale ?? 70;
  const seats = playerState?.seats ?? activeGame?.seats ?? 0;
  const projectedSeats = playerState?.projectedSeats ?? activeGame?.nationalProjectedSeats?.[playerPartyKey?.toUpperCase()] ?? seats;
  const isGainingMomentum = Boolean(playerState?.gainingMomentum ?? (projectedSeats > seats));
  const donationsPerTurn = playerState?.donationsPerTurn ?? Math.max(0.5, Math.round(projectedSeats * (isGainingMomentum ? 0.75 : 0.5) * 10) / 10);

  // Percentage change vs last turn
  const deltaFunds = playerState?.deltaFunds || 0.0;
  const isFirstTurn = (activeGame?.currentSeason || 1) <= 1;
  const lastTurnFunds = isFirstTurn
    ? startingFunds
    : Math.max(0.1, Math.round((currentFunds - deltaFunds) * 10.0) / 10.0);

  const fundDiffPct = lastTurnFunds > 0
    ? (((currentFunds - lastTurnFunds) / lastTurnFunds) * 100).toFixed(1)
    : 0;

  const heat = activeGame?.megaFinanceHeat || 0;
  const committedCardId = activeGame?.committedFinanceCard || null;
  const visibleCardIds = activeGame?.visibleFinanceCardIds || [];

  // Fetch cards config
  useEffect(() => {
    let isMounted = true;
    const loadCards = async () => {
      setLoading(true);
      try {
        const data = await fetchNationalFinanceCards(gameId);
        if (isMounted && Array.isArray(data)) {
          setAllCards(data);
        }
      } catch (err) {
        console.warn('Could not fetch finance cards:', err);
      } finally {
        if (isMounted) setLoading(false);
      }
    };
    loadCards();
    return () => { isMounted = false; };
  }, [gameId]);

  // Handle Play Card
  const handlePlayCard = async (cardId) => {
    setActionLoading(true);
    setError(null);
    setSuccess(null);
    try {
      const updated = await playNationalFinanceCard(gameId, cardId);
      if (updated) {
        onGameUpdate(updated);
        if (onMarkCompleted) onMarkCompleted(true);
        setSuccess('Operation committed for this season! Effects will resolve when season advances.');
      }
    } catch (err) {
      setError(err.message || 'Failed to play finance card.');
    } finally {
      setActionLoading(false);
    }
  };

  // Handle Cancel Selection
  const handleCancelCard = async () => {
    setActionLoading(true);
    setError(null);
    setSuccess(null);
    try {
      const updated = await cancelNationalFinanceCard(gameId);
      if (updated) {
        onGameUpdate(updated);
        if (onMarkCompleted) onMarkCompleted(false);
        setSuccess('Card selection canceled. You can choose another operation.');
      }
    } catch (err) {
      setError(err.message || 'Failed to cancel card.');
    } finally {
      setActionLoading(false);
    }
  };

  // 6 cards visible, 3 hidden
  const visibleCards = visibleCardIds.length > 0
    ? allCards.filter(c => visibleCardIds.includes(c.id))
    : allCards.slice(0, 6);

  // Greed Heat Indicator Configuration
  const getHeatBadge = () => {
    if (heat <= 1) {
      return {
        badgeColor: '#10b981',
        icon: '🟢',
        title: 'Clean Standing (Heat 0-1)',
        subtitle: 'Grassroots connection is healthy. Corporate public scrutiny is minimal.',
        hint: 'You have room to engage private donors or host a summit if treasury demands urgent capital.'
      };
    } else if (heat === 2) {
      return {
        badgeColor: '#fbbf24',
        icon: '🟡',
        title: 'Scrutiny Alert (Heat 2)',
        subtitle: 'Moderate corporate dependency detected. Press scrutiny is rising.',
        hint: '💡 Penalty Active: Extra Corruption +2, Morale Backlash -2. Consider running Grassroots Collection or Campus Elections to cool down scrutiny.'
      };
    } else if (heat === 3) {
      return {
        badgeColor: '#f97316',
        icon: '🟠',
        title: 'High Crony Heat (Heat 3)',
        subtitle: 'Heavy reliance on mega-finance! Investigative reporters are asking questions.',
        hint: '⚠️ Penalty Active: Extra Corruption +5, Morale Backlash -5. Cadre morale is slipping. Run membership drives or campus union polls to restore grassroots trust.'
      };
    } else {
      return {
        badgeColor: '#ef4444',
        icon: '🔴',
        title: 'Critical Greed Level (Heat 4+)',
        subtitle: 'Severe corporate crony backlash! Grassroots cadre feels alienated and betrayed.',
        hint: '🚨 Penalty Active: Extra Corruption +10, Morale Backlash -10. Immediately disconnect from mega-donors and return to grassroots organizing to prevent internal collapse.'
      };
    }
  };

  const heatInfo = getHeatBadge();

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>

      {/* ------------------------------------------------------------------ */}
      {/* 1. FINANCIAL DASHBOARD & CADRE OVERVIEW                             */}
      {/* ------------------------------------------------------------------ */}
      <div style={{
        padding: '14px',
        borderRadius: '12px',
        background: 'linear-gradient(135deg, rgba(15, 23, 42, 0.85), rgba(16, 185, 129, 0.15))',
        borderLeft: '4px solid #10b981',
        boxShadow: '0 4px 16px rgba(0,0,0,0.4)',
        border: '1px solid rgba(16, 185, 129, 0.25)'
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '12px' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <span style={{ fontSize: '18px' }}>💰</span>
              <h2 style={{ margin: 0, color: '#fff', fontSize: '14.5px', fontWeight: '900' }}>
                Party Treasury & Resource Headquarters
              </h2>
              <span className="nwr-badge nwr-badge-green">Season {activeGame?.currentSeason || 1}</span>
            </div>
            <p className="nwr-hide-mobile" style={{ margin: '4px 0 0 0', color: '#94a3b8', fontSize: '9px' }}>
              Manage declared party capital, grassroots workforce, and campaign financing operations.
            </p>
          </div>

          <div style={{ display: 'flex', gap: '10px', alignItems: 'center', flexWrap: 'wrap' }}>
            <div style={{ textAlign: 'right' }}>
              <div style={{ color: '#10b981', fontWeight: '900', fontSize: '15px' }}>
                ₹ {Number(currentFunds).toFixed(1)} Cr
              </div>
              <div style={{ fontSize: '8px', color: Number(fundDiffPct) >= 0 ? '#10b981' : '#ef4444', fontWeight: '800' }}>
                {Number(fundDiffPct) >= 0 ? `▲ +${fundDiffPct}%` : `▼ ${fundDiffPct}%`} vs Last Turn (₹{Number(lastTurnFunds).toFixed(1)} Cr)
              </div>
            </div>
            <div style={{
              padding: '5px 10px',
              backgroundColor: isGainingMomentum ? 'rgba(16, 185, 129, 0.15)' : 'rgba(0,0,0,0.3)',
              borderRadius: '8px',
              border: isGainingMomentum ? '1px solid rgba(16, 185, 129, 0.4)' : '1px solid rgba(255,255,255,0.1)',
              textAlign: 'center'
            }}>
              <div style={{ fontSize: '7.5px', color: isGainingMomentum ? '#34d399' : '#94a3b8', fontWeight: '800', textTransform: 'uppercase', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '4px' }}>
                {isGainingMomentum && <span>🔥</span>} Party Donation
              </div>
              <div style={{ fontSize: '11px', color: isGainingMomentum ? '#10b981' : '#38bdf8', fontWeight: '900' }}>
                +₹{Number(donationsPerTurn).toFixed(1)} Cr / turn
              </div>
              <div style={{ fontSize: '7px', color: '#94a3b8', marginTop: '1px' }}>
                {projectedSeats} proj. seats @ ₹{isGainingMomentum ? '0.75' : '0.50'} Cr {isGainingMomentum ? '(+₹0.25 bonus)' : ''}
              </div>
            </div>
          </div>
        </div>

        {/* Cadre Resources Breakdown */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(62px, 1fr))',
          gap: '6px',
          marginTop: '10px',
          backgroundColor: 'rgba(0,0,0,0.25)',
          padding: '6px 8px',
          borderRadius: '8px'
        }}>
          <div style={{ textAlign: 'center' }}>
            <div style={{ fontSize: '7px', color: '#94a3b8', fontWeight: '800' }}>👷 WORKERS</div>
            <div style={{ fontSize: '11px', fontWeight: '900', color: '#cbd5e1' }}>
              {workers >= 100000 ? `${(workers / 100000).toFixed(1)}L` : workers.toLocaleString()}
            </div>
          </div>
          <div style={{ textAlign: 'center' }}>
            <div style={{ fontSize: '7px', color: '#94a3b8', fontWeight: '800' }}>🤝 VOLUNTEERS</div>
            <div style={{ fontSize: '11px', fontWeight: '900', color: '#38bdf8' }}>
              {volunteers >= 100000 ? `${(volunteers / 100000).toFixed(1)}L` : volunteers.toLocaleString()}
            </div>
          </div>
          <div style={{ textAlign: 'center' }}>
            <div style={{ fontSize: '7px', color: '#94a3b8', fontWeight: '800' }}>💳 DONORS</div>
            <div style={{ fontSize: '11px', fontWeight: '900', color: '#f59e0b' }}>
              {donors >= 1000 ? `${(donors / 1000).toFixed(1)}k` : donors.toLocaleString()}
            </div>
          </div>
          <div style={{ textAlign: 'center' }}>
            <div style={{ fontSize: '7px', color: '#94a3b8', fontWeight: '800' }}>❤️ MORALE</div>
            <div style={{ fontSize: '11px', fontWeight: '900', color: morale > 70 ? '#10b981' : morale > 40 ? '#fbbf24' : '#ef4444' }}>
              {morale}%
            </div>
          </div>
          <div style={{ textAlign: 'center' }}>
            <div style={{ fontSize: '7px', color: '#94a3b8', fontWeight: '800' }}>⚖️ CORRUPTION</div>
            <div style={{ fontSize: '11px', fontWeight: '900', color: corruption > 40 ? '#ef4444' : corruption > 20 ? '#fbbf24' : '#10b981' }}>
              {corruption}%
            </div>
          </div>
        </div>
      </div>

      {/* ------------------------------------------------------------------ */}
      {/* 2. CRONY SCRUTINY HEAT METER & DYNAMIC COOLDOWN HINT               */}
      {/* ------------------------------------------------------------------ */}
      <div style={{
        padding: '10px 14px',
        borderRadius: '10px',
        backgroundColor: '#0f172a',
        border: `1.5px solid ${heatInfo.badgeColor}40`,
        boxShadow: `0 0 15px ${heatInfo.badgeColor}15`,
        display: 'flex',
        flexDirection: 'column',
        gap: '6px'
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span style={{ fontSize: '14px' }}>{heatInfo.icon}</span>
            <strong style={{ color: heatInfo.badgeColor, fontSize: '11px' }}>
              Crony Dependency Meter: {heatInfo.title}
            </strong>
          </div>
          <div style={{ display: 'flex', gap: '4px' }}>
            {[1, 2, 3, 4].map(lvl => (
              <div
                key={lvl}
                style={{
                  width: '18px',
                  height: '8px',
                  borderRadius: '3px',
                  backgroundColor: heat >= lvl
                    ? (lvl >= 4 ? '#ef4444' : lvl === 3 ? '#f97316' : '#fbbf24')
                    : '#1e293b'
                }}
              />
            ))}
          </div>
        </div>
        <p style={{ margin: 0, fontSize: '8.5px', color: '#cbd5e1', lineHeight: 1.4 }}>
          {heatInfo.subtitle}
        </p>
        <div style={{
          backgroundColor: 'rgba(0,0,0,0.3)',
          padding: '5px 8px',
          borderRadius: '6px',
          fontSize: '8px',
          color: heat >= 2 ? heatInfo.badgeColor : '#94a3b8',
          fontWeight: '700'
        }}>
          {heatInfo.hint}
        </div>
      </div>

      {/* ------------------------------------------------------------------ */}
      {/* 3. SEASONAL STATUS & COMMITTED CARD NOTICE                         */}
      {/* ------------------------------------------------------------------ */}
      {committedCardId ? (
        <div style={{
          padding: '12px 14px',
          borderRadius: '10px',
          backgroundColor: 'rgba(16, 185, 129, 0.1)',
          border: '1.5px solid #10b981',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          flexWrap: 'wrap',
          gap: '8px'
        }}>
          <div>
            <div style={{ color: '#10b981', fontWeight: '900', fontSize: '11px', display: 'flex', alignItems: 'center', gap: '6px' }}>
              <span>🔒</span> Finance Operation Committed for Season {activeGame?.currentSeason || 1}
            </div>
            <div style={{ fontSize: '9px', color: '#cbd5e1', marginTop: '3px' }}>
              Operation: <strong>{allCards.find(c => c.id === committedCardId)?.name || committedCardId}</strong>
              {' '}— will resolve and update party stats when advancing to the next season.
            </div>
          </div>
          <button
            disabled={actionLoading}
            onClick={handleCancelCard}
            style={{
              backgroundColor: 'rgba(239, 68, 68, 0.2)',
              border: '1px solid #ef4444',
              color: '#ef4444',
              padding: '5px 10px',
              borderRadius: '6px',
              fontSize: '9px',
              fontWeight: '800',
              cursor: 'pointer'
            }}
          >
            ✕ Change Selection
          </button>
        </div>
      ) : (
        <div style={{
          padding: '10px 14px',
          borderRadius: '10px',
          backgroundColor: 'rgba(56, 189, 248, 0.08)',
          border: '1px dashed rgba(56, 189, 248, 0.4)',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center'
        }}>
          <div>
            <div style={{ color: '#38bdf8', fontWeight: '800', fontSize: '10.5px' }}>
              🟢 1 Finance Operation Available This Season
            </div>
            <div style={{ fontSize: '8.5px', color: '#94a3b8', marginTop: '2px' }}>
              Select any 1 of the 6 available operations below. Exactly 1 card can be played per turn.
            </div>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span style={{ fontSize: '8.5px', color: '#64748b' }}>6 Visible • 3 Hidden</span>
            <button
              onClick={() => onMarkCompleted && onMarkCompleted(!isCompleted)}
              style={{
                padding: '4px 10px',
                borderRadius: '6px',
                border: isCompleted ? '1.5px solid #10b981' : '1px solid #64748b',
                backgroundColor: isCompleted ? 'rgba(16, 185, 129, 0.2)' : 'rgba(30, 41, 59, 0.6)',
                color: isCompleted ? '#34d399' : '#cbd5e1',
                fontSize: '9px',
                fontWeight: '800',
                cursor: 'pointer',
                display: 'inline-flex',
                alignItems: 'center',
                gap: '4px',
                transition: 'all 0.2s ease'
              }}
              title="Confirm treasury strategy (skip card or conclude finance for this turn)"
            >
              {isCompleted ? '✓ Strategy Confirmed' : 'Confirm Strategy'}
            </button>
          </div>
        </div>
      )}

      {/* Notifications */}
      {error && (
        <div style={{ color: '#ef4444', backgroundColor: 'rgba(239,68,68,0.1)', padding: '8px 12px', borderRadius: '6px', fontSize: '9.5px' }}>
          {error}
        </div>
      )}
      {success && (
        <div style={{ color: '#10b981', backgroundColor: 'rgba(16,185,129,0.1)', padding: '8px 12px', borderRadius: '6px', fontSize: '9.5px' }}>
          {success}
        </div>
      )}

      {/* ------------------------------------------------------------------ */}
      {/* 4. THE 6-CARD STRATEGY HAND (3 HIDDEN)                              */}
      {/* ------------------------------------------------------------------ */}
      {loading ? (
        <div style={{ textAlign: 'center', color: '#38bdf8', padding: '30px', fontSize: '11px', fontWeight: '700' }}>
          ⏳ Loading Finance Operations...
        </div>
      ) : (
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
          gap: '12px'
        }}>
          {visibleCards.map(card => {
            const isSelected = committedCardId === card.id;
            const isLocked = committedCardId !== null && !isSelected;

            return (
              <div
                key={card.id}
                style={{
                  backgroundColor: '#0f172a',
                  borderRadius: '10px',
                  border: isSelected
                    ? '2px solid #10b981'
                    : card.megaFinance
                      ? '1px solid rgba(245, 158, 11, 0.3)'
                      : '1px solid rgba(56, 189, 248, 0.25)',
                  boxShadow: isSelected
                    ? '0 0 16px rgba(16, 185, 129, 0.3)'
                    : '0 4px 12px rgba(0,0,0,0.3)',
                  padding: '12px',
                  display: 'flex',
                  flexDirection: 'column',
                  justifyContent: 'space-between',
                  opacity: isLocked ? 0.45 : 1,
                  transition: 'all 0.2s ease'
                }}
              >
                <div>
                  {/* Card Header */}
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '6px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <span style={{ fontSize: '18px' }}>{card.icon}</span>
                      <div>
                        <h4 style={{ margin: 0, color: '#fff', fontSize: '11px', fontWeight: '900' }}>
                          {card.name}
                        </h4>
                        <span style={{
                          fontSize: '7.5px',
                          fontWeight: '800',
                          color: card.megaFinance ? '#fbbf24' : card.grassroots ? '#10b981' : '#38bdf8',
                          textTransform: 'uppercase'
                        }}>
                          {card.category}
                        </span>
                      </div>
                    </div>
                    {isSelected && (
                      <span style={{
                        backgroundColor: '#10b981',
                        color: '#0f172a',
                        fontWeight: '900',
                        fontSize: '7.5px',
                        padding: '2px 6px',
                        borderRadius: '4px'
                      }}>
                        ACTIVE
                      </span>
                    )}
                  </div>

                  <p style={{ margin: '4px 0 8px 0', fontSize: '8.5px', color: '#94a3b8', fontStyle: 'italic', lineHeight: 1.3 }}>
                    "{card.tagline}"
                  </p>

                  <p style={{ margin: '0 0 10px 0', fontSize: '8.5px', color: '#cbd5e1', lineHeight: 1.35 }}>
                    {card.description}
                  </p>

                  {/* Qualitative Gauges (Zero Numbers Visible) */}
                  <div style={{
                    backgroundColor: 'rgba(0,0,0,0.3)',
                    padding: '8px',
                    borderRadius: '6px',
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '4px',
                    marginBottom: '10px'
                  }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '8px' }}>
                      <span style={{ color: '#94a3b8' }}>Treasury Influx:</span>
                      <strong style={{ color: card.treasuryRating.includes('Expense') || card.treasuryRating.includes('Investment') ? '#ef4444' : '#10b981' }}>
                        {card.treasuryRating}
                      </strong>
                    </div>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '8px' }}>
                      <span style={{ color: '#94a3b8' }}>Cadre Growth:</span>
                      <strong style={{ color: card.cadreRating === 'None' ? '#64748b' : '#38bdf8' }}>
                        {card.cadreRating}
                      </strong>
                    </div>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '8px' }}>
                      <span style={{ color: '#94a3b8' }}>Morale Impact:</span>
                      <strong style={{ color: card.moraleRating.includes('Cynicism') || card.moraleRating.includes('Disillusionment') ? '#ef4444' : '#10b981' }}>
                        {card.moraleRating}
                      </strong>
                    </div>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '8px' }}>
                      <span style={{ color: '#94a3b8' }}>Scrutiny Risk:</span>
                      <strong style={{ color: card.scrutinyRating.includes('Extreme') ? '#ef4444' : card.scrutinyRating.includes('Moderate') ? '#fbbf24' : '#10b981' }}>
                        {card.scrutinyRating}
                      </strong>
                    </div>
                  </div>

                  {/* Strategic Caution / Note */}
                  <div style={{
                    fontSize: '7.5px',
                    color: card.megaFinance ? '#fbbf24' : '#94a3b8',
                    backgroundColor: card.megaFinance ? 'rgba(245, 158, 11, 0.08)' : 'rgba(255,255,255,0.02)',
                    borderLeft: `2px solid ${card.megaFinance ? '#fbbf24' : '#38bdf8'}`,
                    padding: '4px 6px',
                    borderRadius: '3px',
                    marginBottom: '10px'
                  }}>
                    💡 {card.strategicNote}
                  </div>
                </div>

                {/* Action Button */}
                <div>
                  {isSelected ? (
                    <button
                      disabled={actionLoading}
                      onClick={handleCancelCard}
                      style={{
                        width: '100%',
                        padding: '6px',
                        backgroundColor: '#10b981',
                        color: '#0f172a',
                        border: 'none',
                        borderRadius: '6px',
                        fontWeight: '900',
                        fontSize: '9.5px',
                        cursor: 'pointer'
                      }}
                    >
                      ✓ Selected for this Season
                    </button>
                  ) : (
                    <button
                      disabled={actionLoading || isLocked}
                      onClick={() => handlePlayCard(card.id)}
                      style={{
                        width: '100%',
                        padding: '6px',
                        backgroundColor: isLocked
                          ? '#1e293b'
                          : card.megaFinance
                            ? '#f59e0b'
                            : '#0284c7',
                        color: isLocked ? '#64748b' : '#ffffff',
                        border: 'none',
                        borderRadius: '6px',
                        fontWeight: '800',
                        fontSize: '9.5px',
                        cursor: isLocked ? 'not-allowed' : 'pointer',
                        transition: 'all 0.2s'
                      }}
                    >
                      {isLocked ? 'Slot Locked' : 'Commit Operation'}
                    </button>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      )}

    </div>
  );
}
