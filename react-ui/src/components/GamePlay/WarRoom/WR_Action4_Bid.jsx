import React, { useEffect } from 'react';
import { getPartyColor } from '../gameUtils';

/**
 * WR_Action4_Bid — Bid for Rewards
 * Simplified: tap a quick-pick → bid auto-locks. Slider still works for custom.
 * No confirmation step, no secondary navigation button.
 */
export default function WR_Action4_Bid({ turnData, activeParty, bidAmount, setBidAmount, bidConfirmed, setBidConfirmed }) {
  const bidMetric        = turnData?.biddingMetric || 'COINS';
  const activePartyStats = activeParty?.stats || {};

  const metricMap = {
    COINS:          'coins',
    CORRUPTION:     'corruptionScore',
    MORALE:         'partyMorale',
    MEDIA:          'mediaImage',
    PUBLIC_SUPPORT: 'publicSupport',
  };

  let maxBid = activePartyStats[metricMap[bidMetric.toUpperCase()] || 'coins'] || 0;
  if (bidMetric.toUpperCase() === 'CORRUPTION') {
    maxBid = Math.max(0, 95 - (activePartyStats.corruptionScore || 0));
  }

  const lastWonBid  = (turnData?.lastRoundWinnerPartyId && turnData?.lastRoundBids?.[turnData.lastRoundWinnerPartyId] != null)
    ? turnData.lastRoundBids[turnData.lastRoundWinnerPartyId]
    : null;
  const safeBidValue = lastWonBid != null ? lastWonBid : 10;

  // Quick-picks: Safe, two fixed values, MAX
  const quickPickList = [
    { label: `Safe  ${safeBidValue}`, val: safeBidValue },
    ...(safeBidValue !== 15 ? [{ label: '15', val: 15 }] : []),
    ...(safeBidValue !== 25 ? [{ label: '25', val: 25 }] : []),
    { label: 'Max', val: maxBid },
  ];

  const pct           = maxBid > 0 ? Math.round((bidAmount / maxBid) * 100) : 0;
  const isSpecial     = turnData?.currentRewardKey?.startsWith('special_');
  const gaugeColor    = pct < 33 ? '#3b82f6' : pct < 66 ? '#f59e0b' : '#ef4444';
  const pressureLabel = pct < 33 ? '❄️ Safe' : pct < 66 ? '🔥 Competitive' : '🚨 High Stakes';

  /** Tap quick-pick → set amount + auto-lock */
  const handleQuickPick = (val) => {
    if (bidConfirmed) return;               // already locked — ignore
    const clamped = Math.min(val, maxBid);
    setBidAmount(clamped);
    setBidConfirmed(true);                  // instant lock, no confirmation
  };

  /** Slider change → unlock so user can re-pick */
  const handleSlider = (e) => {
    setBidConfirmed(false);
    setBidAmount(parseInt(e.target.value) || 0);
  };

  return (
    <div style={{ padding: '14px 16px 0' }}>

      {/* ── Header ── */}
      <div style={{ marginBottom: '14px' }}>
        <div style={{ fontSize: '15px', fontWeight: 900, letterSpacing: '0.05em', textTransform: 'uppercase', color: '#F59E0B' }}>
          💰 Bid for Rewards
        </div>
        <div style={{ fontSize: '12px', color: '#7D8590', marginTop: '2px' }}>
          Stake {bidMetric.toLowerCase()} to win this cycle's reward
          {safeBidValue > 0 && <span style={{ color: '#4ADE80' }}> · Safe bid: {safeBidValue}</span>}
        </div>
      </div>

      {/* ── Prize card ── */}
      {turnData?.currentRewardName && (
        <div style={{
          background:   isSpecial
            ? 'linear-gradient(145deg,rgba(250,204,21,0.1),rgba(234,179,8,0.04))'
            : 'rgba(255,255,255,0.04)',
          border:       `1px solid ${isSpecial ? 'rgba(245,158,11,0.4)' : 'rgba(255,255,255,0.1)'}`,
          borderRadius: '12px',
          padding:      '12px 14px',
          marginBottom: '12px',
          position:     'relative',
        }}>
          {isSpecial && (
            <div style={{
              position: 'absolute', top: 0, right: 0,
              background: 'linear-gradient(90deg,#f59e0b,#d97706)',
              color: '#ffffff', fontSize: '9px', fontWeight: 800,
              padding: '2px 10px', borderRadius: '0 12px 0 8px', letterSpacing: '0.05em',
            }}>⭐ SPECIAL</div>
          )}
          <div style={{ fontSize: '10px', fontWeight: 800, letterSpacing: '0.07em', textTransform: 'uppercase', color: isSpecial ? '#F59E0B' : '#7D8590', marginBottom: '5px' }}>
            🎯 Bidding for
          </div>
          <div style={{ fontSize: '15px', fontWeight: 900, color: isSpecial ? '#FCD34D' : '#E6EDF3', lineHeight: 1.25 }}>
            {turnData.currentRewardName}
          </div>
          {turnData.currentRewardDescription && (
            <div style={{ fontSize: '12px', color: '#8B949E', marginTop: '4px', lineHeight: 1.5 }}>
              {turnData.currentRewardDescription}
            </div>
          )}
        </div>
      )}

      {/* ── Cycle standings ── */}
      <div style={{
        background:   'rgba(255,255,255,0.03)',
        border:       '1px solid rgba(255,255,255,0.08)',
        borderRadius: '10px',
        padding:      '10px 12px',
        marginBottom: '14px',
      }}>
        <div style={{ fontSize: '10px', fontWeight: 800, letterSpacing: '0.06em', textTransform: 'uppercase', color: '#F59E0B', marginBottom: '8px' }}>
          🏆 5-Turn Cycle Standings
        </div>
        {(turnData?.parties || []).map((p, i) => {
          const wins = turnData?.partyRoundWins?.[p.id] || 0;
          const isMe = p.id === turnData?.activeHumanPartyId;
          return (
            <div key={p.id} style={{
              display: 'flex', alignItems: 'center', justifyContent: 'space-between',
              padding: '4px 0',
              borderBottom: i < (turnData?.parties?.length || 0) - 1 ? '1px solid rgba(255,255,255,0.05)' : 'none',
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <div style={{ width: '7px', height: '7px', borderRadius: '50%', background: getPartyColor(p), flexShrink: 0 }} />
                <span style={{ fontSize: '12px', fontWeight: isMe ? 800 : 400, color: isMe ? '#E6EDF3' : '#8B949E' }}>
                  {p.name} {isMe && <span style={{ color: '#F59E0B', fontSize: '10px' }}>(You)</span>}
                </span>
              </div>
              <span style={{ fontSize: '12px', color: wins > 0 ? '#FCD34D' : '#4B5563' }}>
                {wins > 0 ? '⭐'.repeat(Math.min(wins, 5)) : <span style={{ fontSize: '11px' }}>0 wins</span>}
              </span>
            </div>
          );
        })}
      </div>

      {/* ── Pressure gauge (SVG) ── */}
      <div style={{ textAlign: 'center', marginBottom: '2px' }}>
        <svg width="160" height="88" viewBox="0 0 170 95" style={{ overflow: 'visible' }}>
          <path d="M 10 85 A 75 75 0 0 1 160 85" fill="none" stroke="rgba(255,255,255,0.08)" strokeWidth="11" strokeLinecap="round" />
          <path
            d="M 10 85 A 75 75 0 0 1 160 85"
            fill="none" stroke={gaugeColor} strokeWidth="11" strokeLinecap="round"
            strokeDasharray={`${(pct / 100) * 235} 235`}
            style={{ transition: 'stroke-dasharray 0.3s ease, stroke 0.3s ease' }}
          />
          <text x="85" y="72" textAnchor="middle" fill="#E6EDF3" fontSize="24" fontWeight="900" fontFamily="Montserrat,sans-serif">
            {bidAmount}
          </text>
          <text x="85" y="88" textAnchor="middle" fill="#7D8590" fontSize="10" fontWeight="700" fontFamily="Montserrat,sans-serif">
            {bidMetric.toUpperCase()}
          </text>
        </svg>
        <div style={{ fontSize: '12px', fontWeight: 800, color: gaugeColor, marginTop: '-2px' }}>
          {pressureLabel}
        </div>
      </div>

      {/* ── Slider (unlocks / lets user fine-tune) ── */}
      <input
        type="range"
        min={0}
        max={maxBid}
        value={bidAmount}
        onChange={handleSlider}
        style={{
          width: '100%', margin: '10px 0 6px',
          cursor: 'pointer', accentColor: gaugeColor,
        }}
      />
      <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', color: '#7D8590', marginBottom: '12px' }}>
        <span>0</span>
        <span style={{ color: '#E6EDF3', fontWeight: 700 }}>Remaining: {maxBid - bidAmount}</span>
        <span>{maxBid}</span>
      </div>

      {/* ── Quick-pick row — tap to set & lock instantly ── */}
      <div className="wr-quickpick-row" style={{ marginBottom: '14px' }}>
        {quickPickList.map(item => {
          const isActive = bidAmount === item.val && bidConfirmed;
          return (
            <button
              key={item.label}
              onClick={() => handleQuickPick(item.val)}
              style={{
                minHeight:   '46px',
                background:  isActive ? 'rgba(22,163,74,0.22)' : 'rgba(255,255,255,0.06)',
                border:      `1.5px solid ${isActive ? '#4ADE80' : 'rgba(255,255,255,0.1)'}`,
                borderRadius:'10px',
                color:       isActive ? '#4ADE80' : '#E6EDF3',
                fontSize:    '13px',
                fontWeight:  800,
                cursor:      'pointer',
                touchAction: 'manipulation',
                WebkitTapHighlightColor: 'transparent',
                transition:  'all 0.15s ease',
                fontFamily:  'Montserrat,system-ui,sans-serif',
                padding:     '0 4px',
                boxShadow:   isActive ? '0 0 10px rgba(22,163,74,0.3)' : 'none',
              }}
            >
              {isActive ? '✓ ' : ''}{item.label}
            </button>
          );
        })}
      </div>

      {/* ── Locked state indicator (replaces the old "BID LOCKED" button) ── */}
      {bidConfirmed ? (
        <div style={{
          width:        '100%', minHeight: '50px',
          background:   'linear-gradient(135deg,#16A34A,#15803d)',
          borderRadius: '12px',
          display:      'flex', alignItems: 'center', justifyContent: 'center', gap: '8px',
          boxShadow:    '0 0 16px rgba(22,163,74,0.4)',
          fontSize:     '14px', fontWeight: 900, color: '#ffffff',
          letterSpacing:'0.04em',
          animation:    'wr-fill-in 0.2s ease',
        }}>
          ✅ Bid Locked — {bidAmount} {bidMetric}
        </div>
      ) : (
        /* Muted ghost when slider used but not locked via quick-pick */
        bidAmount > 0 && (
          <button
            onClick={() => setBidConfirmed(true)}
            style={{
              width:        '100%', minHeight: '50px',
              background:   'rgba(245,158,11,0.12)',
              border:       '1.5px solid rgba(245,158,11,0.35)',
              borderRadius: '12px',
              color:        '#FCD34D', fontSize: '13px', fontWeight: 800,
              cursor:       'pointer', touchAction: 'manipulation',
              fontFamily:   'Montserrat,system-ui,sans-serif',
            }}
          >
            Lock {bidAmount} {bidMetric} →
          </button>
        )
      )}

    </div>
  );
}
