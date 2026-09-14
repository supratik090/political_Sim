import React from 'react';
import { getPartyColor } from '../gameUtils';

const QUICK_PICKS = [5, 10, 25];

/**
 * WR_Action4_Bid — Competitive Bid
 * Props: { turnData, activeParty, bidAmount, setBidAmount, bidConfirmed, setBidConfirmed }
 */
export default function WR_Action4_Bid({ turnData, activeParty, bidAmount, setBidAmount, bidConfirmed, setBidConfirmed }) {
  const bidMetric = turnData?.biddingMetric || 'COINS';
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

  const lastWonBid = (turnData?.lastRoundWinnerPartyId && turnData?.lastRoundBids?.[turnData.lastRoundWinnerPartyId] != null)
    ? turnData.lastRoundBids[turnData.lastRoundWinnerPartyId]
    : null;
  const safeBidValue = lastWonBid != null ? lastWonBid : 10;

  const quickPickList = [
    { label: `SAFE (${safeBidValue})`, val: safeBidValue },
    ...(safeBidValue !== 15 ? [{ label: '15', val: 15 }] : []),
    ...(safeBidValue !== 25 ? [{ label: '25', val: 25 }] : []),
    { label: 'MAX', val: maxBid }
  ];

  const pct = maxBid > 0 ? Math.round((bidAmount / maxBid) * 100) : 0;
  const isSpecial = turnData?.currentRewardKey?.startsWith('special_');

  // Pressure gauge colour (blue → amber → red)
  const gaugeColor = pct < 33 ? '#3b82f6' : pct < 66 ? '#f59e0b' : '#ef4444';
  const pressureLabel = pct < 33 ? '❄️ Safe Bid' : pct < 66 ? '🔥 Competitive' : '🚨 High Stakes!';

  // SVG semi-circle gauge (180° arc = 251.3 circumference for r=80)
  const CIRC = 251.3;
  const filled = (pct / 100) * CIRC;

  return (
    <div style={{ padding: '14px 16px 0' }}>
      {/* Section header */}
      <div style={{ marginBottom: '14px' }}>
        <div style={{ fontSize: '15px', fontWeight: 900, letterSpacing: '0.05em', textTransform: 'uppercase', color: '#F59E0B' }}>
          💰 Competitive Bid
        </div>
        <div style={{ fontSize: '12px', color: '#7D8590', marginTop: '2px' }}>
          Stake resources to win this cycle's reward (Safe Bid: {safeBidValue} {bidMetric.toUpperCase()})
        </div>
      </div>

      {/* Prize card */}
      {turnData?.currentRewardName && (
        <div style={{
          background: isSpecial ? 'linear-gradient(145deg,rgba(250,204,21,0.1),rgba(234,179,8,0.04))' : 'rgba(255,255,255,0.04)',
          border: `1px solid ${isSpecial ? 'rgba(245,158,11,0.45)' : 'rgba(255,255,255,0.1)'}`,
          borderRadius: '14px',
          padding: '14px',
          marginBottom: '14px',
          position: 'relative',
        }}>
          {isSpecial && (
            <div style={{
              position: 'absolute', top: 0, right: 0,
              background: 'linear-gradient(90deg,#f59e0b,#d97706)',
              color: '#ffffff', fontSize: '10px', fontWeight: 800,
              padding: '3px 10px', borderRadius: '0 14px 0 8px',
              letterSpacing: '0.05em',
            }}>⭐ SPECIAL</div>
          )}
          <div style={{ fontSize: '10px', fontWeight: 800, letterSpacing: '0.08em', textTransform: 'uppercase', color: isSpecial ? '#F59E0B' : '#7D8590', marginBottom: '6px' }}>
            🎯 BIDDING FOR
          </div>
          <div style={{ fontSize: '16px', fontWeight: 900, color: isSpecial ? '#FCD34D' : '#E6EDF3' }}>
            {turnData.currentRewardName}
          </div>
          {turnData.currentRewardDescription && (
            <div style={{ fontSize: '12px', color: '#8B949E', marginTop: '4px', lineHeight: 1.5 }}>
              {turnData.currentRewardDescription}
            </div>
          )}
        </div>
      )}

      {/* Cycle standings leaderboard */}
      <div style={{
        background: 'rgba(255,255,255,0.03)',
        border: '1px solid rgba(255,255,255,0.08)',
        borderRadius: '12px',
        padding: '12px 14px',
        marginBottom: '16px',
      }}>
        <div style={{ fontSize: '11px', fontWeight: 800, letterSpacing: '0.06em', textTransform: 'uppercase', color: '#F59E0B', marginBottom: '10px' }}>
          🏆 5-Turn Cycle Standings
        </div>
        {(turnData?.parties || []).map((p, i) => {
          const wins = turnData?.partyRoundWins?.[p.id] || 0;
          const isMe = p.id === turnData?.activeHumanPartyId;
          return (
            <div key={p.id} style={{
              display: 'flex', alignItems: 'center', justifyContent: 'space-between',
              padding: '5px 0',
              borderBottom: i < (turnData?.parties?.length || 0) - 1 ? '1px solid rgba(255,255,255,0.05)' : 'none',
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <div style={{ width: '8px', height: '8px', borderRadius: '50%', background: getPartyColor(p), flexShrink: 0 }} />
                <span style={{ fontSize: '13px', fontWeight: isMe ? 800 : 400, color: isMe ? '#E6EDF3' : '#8B949E' }}>
                  {p.name} {isMe && <span style={{ color: '#F59E0B', fontSize: '11px' }}>(You)</span>}
                </span>
              </div>
              <span style={{ fontSize: '14px', color: wins > 0 ? '#FCD34D' : '#4B5563' }}>
                {wins > 0 ? '⭐'.repeat(Math.min(wins, 5)) : <span style={{ fontSize: '11px' }}>0 wins</span>}
              </span>
            </div>
          );
        })}
      </div>

      {/* Pressure gauge (SVG semi-circle) */}
      <div style={{ textAlign: 'center', marginBottom: '4px' }}>
        <svg width="170" height="95" viewBox="0 0 170 95" style={{ overflow: 'visible' }}>
          {/* Track arc */}
          <path
            d="M 10 85 A 75 75 0 0 1 160 85"
            fill="none"
            stroke="rgba(255,255,255,0.08)"
            strokeWidth="12"
            strokeLinecap="round"
          />
          {/* Fill arc */}
          <path
            d="M 10 85 A 75 75 0 0 1 160 85"
            fill="none"
            stroke={gaugeColor}
            strokeWidth="12"
            strokeLinecap="round"
            strokeDasharray={`${(pct / 100) * 235} 235`}
            style={{ transition: 'stroke-dasharray 0.3s ease, stroke 0.3s ease' }}
          />
          {/* Center value */}
          <text x="85" y="72" textAnchor="middle" fill="#E6EDF3" fontSize="22" fontWeight="900" fontFamily="Montserrat,sans-serif">
            {bidAmount}
          </text>
          <text x="85" y="88" textAnchor="middle" fill="#7D8590" fontSize="11" fontWeight="700" fontFamily="Montserrat,sans-serif">
            {bidMetric.toUpperCase()}
          </text>
        </svg>
        <div style={{ fontSize: '12px', fontWeight: 800, color: gaugeColor, marginTop: '-4px' }}>
          {pressureLabel}
        </div>
      </div>

      {/* Slider */}
      <input
        type="range"
        min={0}
        max={maxBid}
        value={bidAmount}
        disabled={bidConfirmed}
        onChange={e => setBidAmount(parseInt(e.target.value) || 0)}
        style={{
          width: '100%',
          margin: '10px 0 6px',
          cursor: bidConfirmed ? 'not-allowed' : 'pointer',
          accentColor: gaugeColor,
        }}
      />
      <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', color: '#7D8590', marginBottom: '10px' }}>
        <span>0</span>
        <span style={{ color: '#E6EDF3', fontWeight: 700 }}>Remaining: {maxBid - bidAmount}</span>
        <span>{maxBid}</span>
      </div>

      {/* Quick-pick buttons */}
      <div className="wr-quickpick-row">
        {quickPickList.map(item => {
          const val = item.val;
          const label = item.label;
          const isActive = bidAmount === val;
          return (
            <button
              key={label}
              onClick={() => !bidConfirmed && setBidAmount(Math.min(val, maxBid))}
              disabled={bidConfirmed}
              style={{
                minHeight: '44px',
                background: isActive ? 'rgba(245,158,11,0.25)' : 'rgba(255,255,255,0.06)',
                border: `1.5px solid ${isActive ? '#F59E0B' : 'rgba(255,255,255,0.1)'}`,
                borderRadius: '10px',
                color: isActive ? '#FCD34D' : '#E6EDF3',
                fontSize: '13px', fontWeight: 800,
                cursor: bidConfirmed ? 'not-allowed' : 'pointer',
                touchAction: 'manipulation', WebkitTapHighlightColor: 'transparent',
                transition: 'all 0.15s ease', fontFamily: 'Montserrat,system-ui,sans-serif',
                padding: '0 6px'
              }}
            >
              {label}
            </button>
          );
        })}
      </div>

      {/* Lock Bid CTA */}
      <button
        onClick={() => setBidConfirmed(!bidConfirmed)}
        disabled={bidAmount < 0 || bidAmount > maxBid}
        style={{
          width: '100%', minHeight: '54px', marginTop: '14px', marginBottom: '4px',
          fontSize: '16px', fontWeight: 900, letterSpacing: '0.04em',
          background: bidConfirmed
            ? 'linear-gradient(135deg,#16A34A,#15803d)'
            : 'linear-gradient(135deg,#D97706,#F59E0B)',
          color: '#ffffff', border: 'none', borderRadius: '14px',
          boxShadow: bidConfirmed ? '0 0 18px rgba(22,163,74,0.5)' : '0 0 16px rgba(245,158,11,0.4)',
          cursor: 'pointer', touchAction: 'manipulation', WebkitTapHighlightColor: 'transparent',
          transition: 'all 0.2s ease', fontFamily: 'Montserrat,system-ui,sans-serif',
        }}
      >
        {bidConfirmed ? '✅ BID LOCKED' : '🔒 LOCK BID'}
      </button>

      {bidConfirmed && (
        <div style={{ textAlign: 'center', fontSize: '12px', color: '#4ADE80', fontWeight: 700, marginBottom: '4px' }}>
          Staking {bidAmount} {bidMetric} — tap again to edit
        </div>
      )}
    </div>
  );
}
