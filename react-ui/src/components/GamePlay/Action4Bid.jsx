import React from 'react';
import { getPartyColor } from './gameUtils';

export default function Action4Bid({
  turnData,
  activeParty,
  bidAmount,
  setBidAmount,
  bidConfirmed,
  setBidConfirmed
}) {
  const bidMetric = turnData.biddingMetric || 'COINS';
  const activePartyStats = activeParty?.stats || {};
  const metricMap = {
    'COINS': 'coins',
    'CORRUPTION': 'corruptionScore',
    'MORALE': 'partyMorale',
    'MEDIA': 'mediaImage',
    'PUBLIC_SUPPORT': 'publicSupport'
  };
  let maxBid = activePartyStats[metricMap[bidMetric.toUpperCase()] || 'coins'] || 0;
  if (bidMetric.toUpperCase() === 'CORRUPTION') {
    maxBid = Math.max(0, 95 - (activePartyStats.corruptionScore || 0));
  }

  return (
    <div>
      {turnData.turnNumber <= 2 && (
        <p style={{ margin: '0 0 15px 0', fontSize: '13px', color: 'var(--card-text)' }}>
          Lock in your bid value to compete with AI controllers for this cycle's reward.
        </p>
      )}

      {/* Present Bidding Scenario Across Parties */}
      {turnData.lastRoundBids && (
        <div style={{ background: 'rgba(var(--party-primary-color-rgb, 101, 148, 177), 0.02)', border: '1.5px solid var(--party-primary-color, var(--primary-border))', padding: '15px', borderRadius: '10px', marginBottom: '20px' }}>
          <h5 style={{ margin: '0 0 10px 0', color: 'var(--primary-dark)', fontSize: '12px', fontWeight: '800', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
            📊 Present Bidding Scenario (Last Round Bids)
          </h5>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {turnData.parties?.map(p => {
              const bid = turnData.lastRoundBids[p.id];
              const isWinner = turnData.lastRoundWinnerPartyId === p.id;
              return (
                <div key={p.id} style={{ display: 'flex', justifyContent: 'space-between', fontSize: '13px', alignItems: 'center', color: 'var(--primary-dark)' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                    <span style={{ width: '8px', height: '8px', borderRadius: '50%', backgroundColor: getPartyColor(p), border: '1px solid rgba(0,0,0,0.1)' }} />
                    <span style={{ fontWeight: p.id === turnData.activeHumanPartyId ? 'bold' : 'normal' }}>
                      {p.name} {p.id === turnData.activeHumanPartyId && '(You)'}
                    </span>
                  </div>
                  <span style={{ fontWeight: 'bold' }}>
                    {bid !== undefined ? `${bid} ${turnData.lastRoundBiddingMetric || ''}` : '0'}
                    {isWinner && <span style={{ marginLeft: '8px', color: '#22c55e', fontSize: '11px', fontWeight: '900' }}>🏆 WINNER</span>}
                  </span>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* Current Cycle Standings */}
      <div style={{ background: 'rgba(var(--party-primary-color-rgb, 101, 148, 177), 0.04)', border: '1.5px dashed var(--party-primary-color, var(--primary-border))', padding: '15px', borderRadius: '10px', marginBottom: '20px' }}>
        <h5 style={{ margin: '0 0 10px 0', color: '#1e3a8a', fontSize: '12px', fontWeight: '800', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
          🏆 Current 5-Turn Cycle Standings
        </h5>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          {turnData.parties?.map(p => {
            const wins = turnData.partyRoundWins?.[p.id] || 0;
            return (
              <div key={p.id} style={{ display: 'flex', justifyContent: 'space-between', fontSize: '13px', alignItems: 'center', color: '#1e3a8a' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                  <span style={{ width: '8px', height: '8px', borderRadius: '50%', backgroundColor: getPartyColor(p), border: '1px solid rgba(0,0,0,0.1)' }} />
                  <span style={{ fontWeight: p.id === turnData.activeHumanPartyId ? 'bold' : 'normal' }}>
                    {p.name} {p.id === turnData.activeHumanPartyId && '(You)'}
                  </span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <span style={{ display: 'flex', gap: '2px' }}>
                    {Array(wins).fill('⭐').join('')}
                    {wins === 0 && <span style={{ fontSize: '11px', opacity: 0.6 }}>0 wins</span>}
                  </span>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {turnData.currentRewardName && (
        <div style={{ background: 'rgba(101,148,177,0.08)', borderLeft: '4px solid var(--selected-highlight)', padding: '10px 15px', borderRadius: '0 8px 8px 0', marginBottom: '15px' }}>
          <div style={{ fontSize: '10px', textTransform: 'uppercase', fontWeight: 'bold', color: 'var(--primary-dark)', opacity: 0.8 }}>Bidding For</div>
          <div style={{ fontSize: '15px', fontWeight: 'bold', color: 'var(--primary-dark)', marginTop: '2px' }}>🎯 {turnData.currentRewardName}</div>
          <div style={{ fontSize: '11px', opacity: 0.8, fontStyle: 'italic', marginTop: '4px' }}>{turnData.currentRewardDescription}</div>
        </div>
      )}
      
      <div style={{ display: 'flex', gap: '15px', marginBottom: '15px' }}>
        <div>
          <div style={{ fontSize: '11px', opacity: 0.8 }}>Bidding Metric</div>
          <div style={{ fontSize: '15px', fontWeight: 'bold', color: 'var(--primary-dark)' }}>⚡ {bidMetric.toUpperCase()}</div>
        </div>
        <div>
          <div style={{ fontSize: '11px', opacity: 0.8 }}>Your Reserves</div>
          <div style={{ fontSize: '15px', fontWeight: 'bold', color: 'var(--primary-dark)' }}>💎 {maxBid}</div>
        </div>
      </div>

      <div style={{ textAlign: 'left', fontSize: '14px', fontWeight: 'bold', marginBottom: '15px', color: 'var(--primary-dark)' }}>
        🗳️ Stake: <span style={{ color: 'var(--selected-highlight)', fontSize: '18px' }}>{bidAmount}</span> / {maxBid} ({bidMetric})
        <span style={{ fontWeight: 'normal', opacity: 0.7, marginLeft: '8px' }}>(Remaining: {maxBid - bidAmount})</span>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '15px', maxWidth: '350px', margin: '0 0 20px 0' }}>
        {/* Option 2: Number Box */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <label htmlFor="custom-bid-input" style={{ fontSize: '12px', fontWeight: 'bold', whiteSpace: 'nowrap', color: 'var(--primary-dark)' }}>Bid Amount:</label>
          <input 
            id="custom-bid-input"
            type="number" 
            min={0} 
            max={maxBid} 
            value={bidAmount}
            disabled={bidConfirmed}
            onChange={(e) => {
              let v = parseInt(e.target.value) || 0;
              if (v < 0) v = 0;
              if (v > maxBid) v = maxBid;
              setBidAmount(v);
            }}
            style={{ flex: 1, padding: '8px', borderRadius: '4px', border: '1px solid var(--primary-border)' }}
          />
        </div>

        {/* Buttons Row */}
        <div style={{ display: 'flex', gap: '10px', marginTop: '5px' }}>
          {/* Option 1: Pass */}
          <button
            disabled={bidConfirmed}
            onClick={() => {
              setBidAmount(0);
            }}
            style={{
              flex: 1,
              minWidth: '150px',
              padding: '10px 15px',
              background: bidAmount === 0 ? 'var(--party-primary-color, var(--primary-dark))' : '#ffffff',
              color: bidAmount === 0 ? '#ffffff' : 'var(--party-primary-color, var(--primary-dark))',
              border: '1.5px solid var(--party-primary-color, var(--party-primary-color))',
              fontWeight: 'bold',
              borderRadius: '6px',
              cursor: 'pointer',
              fontSize: '13px'
            }}
          >
            💤 Pass (Bid 0)
          </button>

          <button
            onClick={() => setBidConfirmed(!bidConfirmed)}
            disabled={bidAmount < 0 || bidAmount > maxBid}
            style={{
              flex: 1,
              minWidth: '150px',
              padding: '10px 15px',
              background: bidConfirmed ? 'var(--selected-highlight)' : 'var(--party-primary-color, var(--primary-dark))',
              borderColor: bidConfirmed ? 'var(--selected-highlight)' : 'var(--party-primary-color, var(--party-primary-color))',
              color: bidConfirmed ? 'var(--primary-dark)' : '#ffffff',
              fontWeight: 'bold',
              borderRadius: '6px',
              cursor: 'pointer',
              fontSize: '13px',
              border: '1.5px solid transparent'
            }}
          >
            {bidConfirmed ? '✅ Bid Locked' : '🔒 Confirm Bid'}
          </button>
        </div>
      </div>
    </div>
  );
}
