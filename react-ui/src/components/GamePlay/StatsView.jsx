import React from 'react';
import { getPartyColor, checkDefeatWarnings, renderStatDelta } from './gameUtils';
import { getPartyThemeByName } from '../../constants/partyThemes';

const getCleanSymbol = (name, symbol) => {
  const normName = (name || '').toLowerCase().trim();
  if (normName.includes('aiadmk')) return 'Two Leaves';
  if (normName.includes('dmk')) return 'Rising Sun';
  if (normName.includes('jdu') || normName.includes('jd-u')) return 'Arrow';
  if (normName.includes('rjd')) return 'Lantern';
  if (normName.includes('bjp')) return 'Lotus';
  if (normName.includes('inc') || normName.includes('congress') || normName.includes('udf')) return 'Hand';
  if (normName.includes('cpim') || normName.includes('cpi-m') || normName.includes('cpi(m)') || normName.includes('ldf')) return 'Hammer & Sickle';
  if (normName.includes('tmc') || normName.includes('trinamool')) return 'Twin Flowers';
  if (normName.includes('ydp') || normName.includes('youth')) return 'Ashoka Chakra';
  return symbol && symbol !== 'undefined' ? symbol : 'Flag';
};

export default function StatsView({
  turnData,
  commentaryExpanded,
  setCommentaryExpanded,
  commentaryFilter,
  setCommentaryFilter,
  projectDefs = {},
  onOpenResolutionReport
}) {
  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px', gap: '15px', flexWrap: 'wrap' }}>
        <h2 style={{ margin: 0 }}>📊 Campaign Standings (Turn {turnData.turnNumber} - {turnData.stateName})</h2>
        <div style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
          <span style={{ fontSize: '12px', background: 'var(--primary-border)', padding: '5px 12px', borderRadius: '20px', border: '1px solid var(--primary-dark)', color: '#fff', fontWeight: 'bold' }}>
            📆 {turnData.currentDate}
          </span>
          <span style={{ fontSize: '12px', background: turnData.status === 'ACTIVE' ? 'var(--selected-highlight)' : '#d23f31', color: 'var(--primary-dark)', padding: '5px 12px', borderRadius: '20px', fontWeight: 'bold' }}>
            STATUS: {turnData.status}
          </span>
        </div>
      </div>

      {/* Election Results Banner */}
      {turnData.lastElectionHeld && (
        <div style={{
          background: 'linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%)',
          border: '2px solid #3b82f6',
          borderRadius: '16px',
          padding: '25px',
          marginBottom: '25px',
          color: '#ffffff',
          boxShadow: '0 8px 30px rgba(0, 0, 0, 0.3)',
          fontFamily: "'Inter', sans-serif",
          position: 'relative',
          overflow: 'hidden'
        }}>
          {/* Decorative background circle */}
          <div style={{
            position: 'absolute',
            top: '-50px',
            right: '-50px',
            width: '150px',
            height: '150px',
            borderRadius: '50%',
            background: 'rgba(59, 130, 246, 0.1)',
            filter: 'blur(30px)',
            pointerEvents: 'none'
          }} />
          
          <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '15px' }}>
            <span style={{ fontSize: '28px' }}>🗳️</span>
            <div>
              <h3 style={{ margin: 0, fontSize: '18px', fontWeight: 800, letterSpacing: '0.03em', textTransform: 'uppercase', color: '#60a5fa' }}>
                State Election Results
              </h3>
              <p style={{ margin: '2px 0 0 0', fontSize: '12px', opacity: 0.8 }}>
                The voters have spoken. A new government has been formed.
              </p>
            </div>
          </div>
          
          <div style={{ 
            background: 'rgba(255, 255, 255, 0.05)', 
            border: '1px solid rgba(255, 255, 255, 0.1)', 
            borderRadius: '12px', 
            padding: '15px',
            marginBottom: '20px'
          }}>
            <div style={{ fontSize: '14px', lineHeight: 1.5 }}>
              👑 Winner: <strong style={{ color: '#fbbf24', fontSize: '16px' }}>{turnData.lastElectionWinner}</strong>
            </div>
            <div style={{ fontSize: '12px', opacity: 0.9, marginTop: '5px' }}>
              {turnData.lastResults?.[0] || 'Government formation successfully completed.'}
            </div>
          </div>

          <h4 style={{ margin: '0 0 10px 0', fontSize: '12px', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.05em', color: '#94a3b8' }}>
            Final Vote Share
          </h4>
          
          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            {Object.entries(turnData.lastElectionVoteShares || {}).map(([partyName, share]) => {
              const partyObj = turnData.parties?.find(p => p.name === partyName);
              const color = partyObj ? getPartyColor(partyObj) : '#94a3b8';
              return (
                <div key={partyName}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '12px', fontWeight: '600', marginBottom: '4px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                      <span style={{ width: '8px', height: '8px', borderRadius: '50%', backgroundColor: color, display: 'inline-block' }} />
                      <span>{partyName} {partyObj?.playerControlled && '(You)'}</span>
                    </div>
                    <span>{share}%</span>
                  </div>
                  <div style={{ width: '100%', height: '8px', background: 'rgba(255, 255, 255, 0.1)', borderRadius: '4px', overflow: 'hidden' }}>
                    <div style={{ width: `${share}%`, height: '100%', backgroundColor: color, borderRadius: '4px', transition: 'width 0.8s ease-out' }} />
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* Special Event Alert for No-Confidence */}
      {(() => {
        if (turnData.lastElectionHeld) return null; // already shown in the banner
        const hasNoConfidence = turnData.lastResults?.some(r => r.toLowerCase().includes('no-confidence')) ||
                                turnData.lastRoundCommentary?.some(c => c.toLowerCase().includes('no-confidence'));
        if (!hasNoConfidence) return null;
        return (
          <div style={{
            background: 'linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%)',
            border: '2px solid #2563eb',
            borderRadius: '12px',
            padding: '15px',
            marginBottom: '20px',
            color: '#ffffff',
            boxShadow: '0 4px 15px rgba(37, 99, 235, 0.2)'
          }}>
            <h3 style={{ margin: '0 0 5px 0', color: '#ffffff', display: 'flex', alignItems: 'center', gap: '8px', fontSize: '16px' }}>
              ⚡ SPECIAL CONSTITUTIONAL EVENT: No-Confidence Vote
            </h3>
            <p style={{ margin: 0, fontSize: '13px', lineHeight: 1.5 }}>
              The Opposition successfully triggered a No-Confidence Motion, leading to early state elections. Voting results determined the new Government!
            </p>
          </div>
        );
      })()}

      {/* Defeat Warnings Section */}
      {(() => {
        const allWarnings = [];
        turnData.parties.forEach(p => {
          if (!p.playerControlled) return;
          const pWarns = checkDefeatWarnings(p);
          pWarns.forEach(w => allWarnings.push({ partyName: p.name, partyColor: getPartyColor(p), message: w }));
        });

        if (allWarnings.length === 0) return null;

        return (
          <div style={{
            background: 'rgba(210, 63, 49, 0.1)',
            border: '2px solid #d23f31',
            borderRadius: '12px',
            padding: '15px',
            marginBottom: '25px',
            boxShadow: '0 4px 12px rgba(210, 63, 49, 0.05)'
          }}>
            <h3 style={{ margin: '0 0 10px 0', color: '#d23f31', display: 'flex', alignItems: 'center', gap: '8px', fontSize: '16px' }}>
              ⚠️ Defeat Hazard Warnings
            </h3>
            <ul style={{ margin: 0, paddingLeft: '20px', color: '#1e293b', fontSize: '13px', display: 'flex', flexDirection: 'column', gap: '6px' }}>
              {allWarnings.map((warn, i) => (
                <li key={i}>
                  <b style={{ color: warn.partyColor && warn.partyColor !== '#ffffff' && warn.partyColor !== '#fff' ? warn.partyColor : '#1e293b' }}>{warn.partyName}</b>: {warn.message}
                </li>
              ))}
            </ul>
          </div>
        );
      })()}

      {/* Doughnut Chart and Vote Shares */}
      <div style={{ 
        display: 'flex', 
        gap: '30px', 
        marginBottom: '25px', 
        background: '#ffffff', 
        border: '2px solid var(--primary-border)',
        padding: '25px',
        borderRadius: '12px',
        flexWrap: 'wrap',
        alignItems: 'center',
        boxShadow: '0 4px 15px rgba(33,60,81,0.05)'
      }}>
        {/* Left: SVG Doughnut Chart */}
        <div style={{ flex: '1 1 200px', display: 'flex', justifyContent: 'center', alignItems: 'center', position: 'relative' }}>
          {(() => {
            const activeParties = (turnData.parties || []).filter(p => p.role !== 'DEFEATED');
            const partiesSum = activeParties.reduce((sum, p) => sum + (p.stats?.publicSupport || 0), 0);
            const undecidedSupport = Math.max(0, 100 - partiesSum);

            const slices = activeParties.map(p => ({
              name: p.name,
              value: p.stats?.publicSupport || 0,
              color: getPartyColor(p),
              isPlayer: p.playerControlled
            }));

            if (undecidedSupport > 0) {
              slices.push({
                name: 'Undecided Voters',
                value: undecidedSupport,
                color: '#9ca3af', // Gray
                isPlayer: false
              });
            }

            const total = 100;
            const radius = 35;
            const circ = 2 * Math.PI * radius; // ~219.91
            let cumulativePercent = 0;

            return (
              <div style={{ position: 'relative', width: '200px', height: '200px' }}>
                <svg viewBox="0 0 100 100" style={{ width: '100%', height: '100%', transform: 'rotate(-90deg)' }}>
                  {slices.map((slice, idx) => {
                    const pct = (slice.value / total) * 100;
                    const strokeLength = (pct / 100) * circ;
                    const strokeOffset = - (cumulativePercent / 100) * circ;
                    cumulativePercent += pct;
                    return (
                      <circle
                        key={idx}
                        cx="50"
                        cy="50"
                        r={radius}
                        fill="transparent"
                        stroke={slice.color}
                        strokeWidth="14"
                        strokeDasharray={`${strokeLength} ${circ}`}
                        strokeDashoffset={strokeOffset}
                        style={{
                          transition: 'stroke-dashoffset 0.8s ease-in-out, stroke-dasharray 0.8s ease-in-out',
                          cursor: 'pointer'
                        }}
                        title={`${slice.name}: ${slice.value}%`}
                      />
                    );
                  })}
                </svg>
                {/* Center text of the Doughnut Chart */}
                <div style={{
                  position: 'absolute',
                  top: '50%',
                  left: '50%',
                  transform: 'translate(-50%, -50%)',
                  textAlign: 'center',
                  fontFamily: "'Inter', sans-serif"
                }}>
                  <div style={{ fontSize: '11px', fontWeight: 'bold', textTransform: 'uppercase', opacity: 0.6, letterSpacing: '0.05em' }}>
                    Voter Support
                  </div>
                  <div style={{ fontSize: '24px', fontWeight: '900', color: 'var(--primary-dark)' }}>
                    100%
                  </div>
                </div>
              </div>
            );
          })()}
        </div>

        {/* Right: Legend and Vote Shares */}
        <div style={{ flex: '2 1 300px', display: 'flex', flexDirection: 'column', gap: '12px' }}>
          <h3 style={{ margin: '0 0 5px 0', fontSize: '15px', color: 'var(--primary-dark)', fontWeight: 'bold', textTransform: 'uppercase', letterSpacing: '0.03em' }}>
            Current Voter Support share
          </h3>
          {(() => {
            const activeParties = (turnData.parties || []).filter(p => p.role !== 'DEFEATED');
            const partiesSum = activeParties.reduce((sum, p) => sum + (p.stats?.publicSupport || 0), 0);
            const undecidedSupport = Math.max(0, 100 - partiesSum);

            const items = activeParties.map(p => {
              const cleanedSymbol = getCleanSymbol(p.name, p.symbol);
              return {
                name: p.name,
                value: p.stats?.publicSupport || 0,
                color: getPartyColor(p),
                isPlayer: p.playerControlled,
                symbol: cleanedSymbol,
                role: p.role
              };
            });

            if (undecidedSupport > 0) {
              items.push({
                name: 'Undecided Voters',
                value: undecidedSupport,
                color: '#9ca3af', // Gray
                isPlayer: false,
                symbol: 'N/A',
                role: 'UNDECIDED'
              });
            }

            return items.map((item, idx) => (
              <div key={idx} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', fontSize: '13px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <span style={{ width: '12px', height: '12px', borderRadius: '50%', backgroundColor: item.color, border: '1px solid rgba(0,0,0,0.1)', display: 'inline-block' }} />
                  <span style={{ fontWeight: item.isPlayer ? 'bold' : 'normal', color: 'var(--primary-dark)' }}>
                    {item.name} {item.isPlayer && '(You)'} {item.symbol && item.symbol !== 'N/A' && (
                      <span style={{ fontSize: '10px', opacity: 0.6 }}>({item.symbol})</span>
                    )}
                  </span>
                </div>
                <div style={{ fontWeight: 'bold', color: 'var(--primary-dark)' }}>
                  {item.value}%
                </div>
              </div>
            ));
          })()}
        </div>
      </div>

      {/* 3 Party Cards */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '20px', marginBottom: '25px' }}>
        {turnData.parties.map(party => {
          const stats = party.stats || {};
          const isPlayer = party.playerControlled;
          const lastBid = turnData.lastRoundBids?.[party.id];
          const wonBidding = turnData.lastRoundWinnerPartyId === party.id;
          const partyDeltas = turnData.lastMetricDeltas?.[party.id] || {};
          
          const lastSub = (turnData.lastRoundSubmissions || []).find(sub => sub.partyId === party.id);
          const lastPlayedCard = lastSub ? lastSub.cardName : 'None / Pass';
          const isDefeated = party.role === 'DEFEATED';
          
          const theme = getPartyThemeByName(party.name);
          const partyColor = theme.color;
          const WatermarkIcon = theme.WatermarkIcon;

          return (
            <div key={party.id} className="unified-card" style={{
              border: isDefeated 
                ? '2px solid #ef4444' 
                : (isPlayer ? `2.5px solid ${partyColor}` : '1.5px solid var(--primary-border)'),
              position: 'relative',
              padding: '20px',
              display: 'flex',
              flexDirection: 'column',
              justifyContent: 'space-between',
              boxShadow: isDefeated 
                ? '0 4px 12px rgba(239, 68, 68, 0.1)' 
                : (isPlayer ? `0 0 15px rgba(${theme.rgb}, 0.15)` : 'none'),
              background: isDefeated ? '#f8fafc' : '#ffffff',
              opacity: isDefeated ? 0.85 : 1,
              overflow: 'hidden'
            }}>
              {/* Faded top-right watermark icon */}
              <div style={{
                position: 'absolute',
                top: '12px',
                right: '12px',
                opacity: 0.04,
                pointerEvents: 'none',
                zIndex: 0,
                transform: 'rotate(-10deg)'
              }}>
                <WatermarkIcon size={64} />
              </div>

              {/* Bottom-right diagonal triangle ribbon */}
              <div style={{
                position: 'absolute',
                bottom: 0,
                right: 0,
                width: '40px',
                height: '40px',
                background: partyColor,
                clipPath: 'polygon(100% 0, 0 100%, 100% 100%)',
                opacity: 0.85,
                pointerEvents: 'none',
                zIndex: 1
              }} />

              {/* Card content container */}
              <div style={{ position: 'relative', zIndex: 2, display: 'flex', flexDirection: 'column', height: '100%', justifyContent: 'space-between', width: '100%' }}>
                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
                    {isPlayer ? (
                      <span style={{
                        background: 'var(--selected-highlight)',
                        color: 'var(--primary-dark)',
                        fontSize: '9px',
                        fontWeight: 900,
                        padding: '3px 8px',
                        borderRadius: '10px',
                        textTransform: 'uppercase'
                      }}>
                        YOUR PARTY
                      </span>
                    ) : <div />}
                    {isDefeated && (
                      <span style={{
                        background: '#ef4444',
                        color: '#ffffff',
                        fontSize: '9px',
                        fontWeight: 900,
                        padding: '3px 8px',
                        borderRadius: '10px',
                        textTransform: 'uppercase'
                      }}>
                        ❌ DEFEATED
                      </span>
                    )}
                  </div>

                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '5px' }}>
                    <span style={{ width: '12px', height: '12px', borderRadius: '50%', backgroundColor: getPartyColor(party), display: 'inline-block', border: '1px solid rgba(0,0,0,0.1)' }} />
                    <h3 style={{ margin: 0, fontSize: '18px', color: 'var(--primary-dark)' }}>{party.name}</h3>
                  </div>
                  
                  <div style={{ display: 'flex', gap: '6px', marginBottom: '15px' }}>
                    <span style={{ fontSize: '10px', padding: '2px 6px', background: party.role === 'DEFEATED' ? '#ef4444' : 'var(--primary-dark)', borderRadius: '4px', opacity: 0.9, fontWeight: 'bold', color: '#ffffff' }}>
                      {party.role}
                    </span>
                    <span style={{ fontSize: '10px', padding: '2px 6px', background: 'var(--primary-dark)', borderRadius: '4px', opacity: 0.9, fontWeight: 'bold', color: '#ffffff' }}>
                      {party.controllerType === 'HUMAN' ? 'PLAYER' : 'AI'}
                    </span>
                  </div>

                  {/* Stat Metrics Grid */}
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', color: 'var(--card-text)' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '13px', alignItems: 'center' }}>
                      <span>💰 Coins (Reserves)</span>
                      <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                        <span style={{ fontWeight: 'bold', color: stats.coins <= 15 ? '#d23f31' : 'var(--card-text)' }}>
                          {stats.coins} {stats.coins <= 15 && '⚠️'}
                        </span>
                        {renderStatDelta(partyDeltas.coins, false, false)}
                      </span>
                    </div>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '13px', alignItems: 'center' }}>
                      <span>✊ Party Morale</span>
                      <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                        <span style={{ fontWeight: 'bold', color: stats.partyMorale <= 15 ? '#d23f31' : 'var(--card-text)' }}>
                          {stats.partyMorale} {stats.partyMorale <= 15 && '⚠️'}
                        </span>
                        {renderStatDelta(partyDeltas.partyMorale, false, false)}
                      </span>
                    </div>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '13px', alignItems: 'center' }}>
                      <span>⚖️ Corruption Score</span>
                      <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                        <span style={{ fontWeight: 'bold', color: stats.corruptionScore >= 80 ? '#d23f31' : 'var(--card-text)' }}>
                          {stats.corruptionScore}% {stats.corruptionScore >= 80 && '⚠️'}
                        </span>
                        {renderStatDelta(partyDeltas.corruptionScore, true, true)}
                      </span>
                    </div>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '13px', alignItems: 'center' }}>
                      <span>📢 Media Image</span>
                      <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                        <span style={{ fontWeight: 'bold' }}>{stats.mediaImage}</span>
                        {renderStatDelta(partyDeltas.mediaImage, false, false)}
                      </span>
                    </div>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '13px', alignItems: 'center' }}>
                      <span>📈 Voter Support</span>
                      <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                        <span style={{ fontWeight: 'bold', color: stats.publicSupport <= 8 ? '#d23f31' : 'var(--card-text)' }}>
                          {stats.publicSupport}% {stats.publicSupport <= 8 && '⚠️'}
                        </span>
                        {renderStatDelta(partyDeltas.publicSupport, true, false)}
                      </span>
                    </div>
                  </div>
                </div>

                {/* Last Action and Bids */}
                <div style={{ marginTop: '20px', borderTop: '1px solid rgba(101, 148, 177, 0.2)', paddingTop: '15px', color: 'var(--card-text)' }}>
                  <div style={{ fontSize: '12px', marginBottom: '5px' }}>
                    <b>Last Card:</b> <span style={{ opacity: 0.9 }}>{lastPlayedCard}</span>
                  </div>
                  <div style={{ fontSize: '12px' }}>
                    <b>Last Bid:</b> <span style={{ opacity: 0.9 }}>{lastBid !== undefined ? `${lastBid} ${turnData.lastRoundBiddingMetric || ''}` : 'None'}</span>
                    {wonBidding && <span style={{ marginLeft: '5px', color: 'var(--selected-highlight)', fontWeight: 'bold' }}>🏆 Won</span>}
                  </div>
                </div>
              </div>

            </div>
          );
        })}
      </div>

      {/* Campaign info / Bidding metric */}
      <div style={{ 
        marginBottom: '25px', 
        display: 'flex', 
        gap: '20px', 
        background: '#ffffff', 
        border: '2px solid var(--primary-border)',
        padding: '20px',
        borderRadius: '12px',
        flexWrap: 'wrap',
        color: 'var(--primary-dark)'
      }}>
        <div style={{ flex: '1 1 200px' }}>
          <h4 style={{ margin: '0 0 5px 0', textTransform: 'uppercase', fontSize: '10px', opacity: 0.8, letterSpacing: '0.05em', color: 'var(--primary-dark)' }}>Active Cycle Bidding Metric</h4>
          <div style={{ fontSize: '20px', fontWeight: 'bold', color: 'var(--selected-highlight)' }}>
            🎯 {turnData.biddingMetric}
          </div>
          <span style={{ fontSize: '11px', opacity: 0.7, display: 'block', marginBottom: '8px' }}>Submit bids using this metric to win five-turn cycle rewards</span>
          {turnData.turnNumber > 1 && (
            <button 
              onClick={onOpenResolutionReport}
              style={{
                padding: '6px 12px',
                fontSize: '11px',
                fontWeight: 'bold',
                backgroundColor: 'var(--party-primary-color, var(--primary-dark))',
                color: '#ffffff',
                border: 'none',
                borderRadius: '6px',
                cursor: 'pointer',
                display: 'inline-flex',
                alignItems: 'center',
                gap: '4px'
              }}
            >
              📊 View Turn Report
            </button>
          )}
        </div>
        <div className="cycle-reward-pane" style={{ flex: '1 1 200px', borderLeft: '1px solid rgba(0,0,0,0.08)', paddingLeft: '20px' }}>
          <h4 style={{ margin: '0 0 5px 0', textTransform: 'uppercase', fontSize: '10px', opacity: 0.8, letterSpacing: '0.05em', color: 'var(--primary-dark)' }}>Current Cycle Reward</h4>
          <div style={{ fontSize: '16px', fontWeight: 'bold', color: 'var(--primary-dark)' }}>
            🏆 {turnData.currentRewardName || 'None'}
          </div>
          <p style={{ margin: '4px 0 0 0', fontSize: '12px', opacity: 0.9, lineHeight: 1.4 }}>{turnData.currentRewardDescription || 'No reward description'}</p>
        </div>
        {turnData.lastRoundSecretMetric && (
          <div style={{ flex: '1 1 200px', borderLeft: '1px solid rgba(0,0,0,0.08)', paddingLeft: '20px' }}>
            <h4 style={{ margin: '0 0 5px 0', textTransform: 'uppercase', fontSize: '10px', opacity: 0.8, letterSpacing: '0.05em', color: 'var(--primary-dark)' }}>Active Reward</h4>
            <div style={{ fontSize: '18px', fontWeight: 'bold', color: '#16a34a' }}>
              ✨ {turnData.lastRoundSecretMetric === 'COINS' && '💰 Coins'}
              {turnData.lastRoundSecretMetric === 'MORALE' && '✊ Morale'}
              {turnData.lastRoundSecretMetric === 'MEDIA_IMAGE' && '📢 Media'}
              {turnData.lastRoundSecretMetric === 'CORRUPTION' && '⚖️ Corruption'}
              {turnData.lastRoundSecretMetric === 'PUBLIC_SUPPORT' && '📈 Support'}
            </div>
            <span style={{ fontSize: '11px', opacity: 0.7 }}>Matched cards/opposition targets received 3x effects!</span>
          </div>
        )}
      </div>

      {/* TV Breaking News alert for last results */}
      {turnData.lastResults && turnData.lastResults.length > 0 && (
        <div style={{
          background: '#090d16',
          border: '3px solid #ef4444',
          borderRadius: '12px',
          overflow: 'hidden',
          marginBottom: '25px',
          boxShadow: '0 8px 30px rgba(239, 68, 68, 0.15)',
          fontFamily: "system-ui, -apple-system, sans-serif",
          position: 'relative'
        }}>
          {/* Keyframes Style tag */}
          <style>{`
            @keyframes marquee-effect {
              0% { transform: translate3d(0, 0, 0); }
              100% { transform: translate3d(-50%, 0, 0); }
            }
            @keyframes pulse-dot {
              0% { opacity: 0.3; }
              50% { opacity: 1; }
              100% { opacity: 0.3; }
            }
          `}</style>

          {/* TV Breaking News Header Banner */}
          <div style={{
            background: 'linear-gradient(90deg, #ef4444 0%, #b91c1c 50%, #7f1d1d 100%)',
            color: '#ffffff',
            padding: '10px 18px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            fontWeight: '900',
            fontSize: '13px',
            letterSpacing: '0.08em',
            textTransform: 'uppercase',
            borderBottom: '1px solid rgba(255, 255, 255, 0.15)'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <span style={{ 
                width: '10px', 
                height: '10px', 
                borderRadius: '50%', 
                backgroundColor: '#ffffff', 
                display: 'inline-block',
                animation: 'pulse-dot 1.2s infinite'
              }} />
              <span style={{ textShadow: '0 2px 4px rgba(0,0,0,0.5)' }}>📺 BREAKING NEWS</span>
            </div>
            <span style={{ 
              background: '#ffffff', 
              color: '#ef4444', 
              fontSize: '10px', 
              padding: '2px 8px', 
              borderRadius: '4px',
              fontWeight: '900',
              boxShadow: '0 2px 5px rgba(0,0,0,0.2)'
            }}>
              LIVE
            </span>
          </div>

          {/* TV News Body Card grid */}
          <div style={{
            padding: '20px',
            color: '#f8fafc',
            display: 'flex',
            flexDirection: 'column',
            gap: '12px',
            background: 'radial-gradient(circle at center, #1e293b 0%, #0f172a 100%)'
          }}>
            {turnData.lastResults.map((res, i) => (
              <div key={i} style={{
                display: 'flex',
                alignItems: 'center',
                gap: '15px',
                background: 'rgba(15, 23, 42, 0.6)',
                borderLeft: '5px solid #ef4444',
                padding: '14px 18px',
                borderRadius: '0 8px 8px 0',
                boxShadow: '0 4px 10px rgba(0,0,0,0.2)',
                border: '1px solid rgba(255, 255, 255, 0.05)',
                borderLeftWidth: '5px'
              }}>
                <div style={{ 
                  background: '#ef4444', 
                  color: '#ffffff', 
                  fontSize: '9px', 
                  padding: '2px 6px', 
                  borderRadius: '3px', 
                  fontWeight: '900',
                  textTransform: 'uppercase',
                  letterSpacing: '0.05em'
                }}>
                  FLASH
                </div>
                <div style={{ fontSize: '13.5px', lineHeight: 1.5, fontWeight: 600, color: '#f1f5f9' }}>
                  {res}
                </div>
              </div>
            ))}
          </div>

          {/* Scrolling Ticker Footer */}
          <div style={{
            background: '#b91c1c',
            color: '#ffffff',
            padding: '8px 0',
            display: 'flex',
            alignItems: 'center',
            fontSize: '11px',
            overflow: 'hidden',
            whiteSpace: 'nowrap',
            borderTop: '2px solid #ef4444'
          }}>
            <div style={{
              background: '#0f172a',
              padding: '8px 15px',
              fontWeight: '900',
              fontSize: '11px',
              position: 'absolute',
              bottom: 0,
              left: 0,
              zIndex: 10,
              boxShadow: '5px 0 10px rgba(0,0,0,0.3)',
              textTransform: 'uppercase',
              letterSpacing: '0.05em',
              borderRight: '2px solid #ef4444',
              height: '30px',
              display: 'flex',
              alignItems: 'center'
            }}>
              TV FEED
            </div>
            
            <div style={{ 
              display: 'flex', 
              alignItems: 'center',
              width: '200%', 
              overflow: 'hidden'
            }}>
              <div style={{
                display: 'inline-block',
                whiteSpace: 'nowrap',
                animation: 'marquee-effect 35s linear infinite',
                paddingLeft: '110px'
              }}>
                {Array(3).fill(`✦ CAMPAIGN BULLETIN: ${turnData.lastResults.join('   ✦   ')}`).join('   ')}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Commentary Section */}
      <div style={{ 
        border: '1px solid var(--primary-border)', 
        borderRadius: '12px', 
        marginBottom: '25px', 
        background: '#ffffff', 
        color: '#000000', 
        overflow: 'hidden', 
        boxShadow: '0 4px 12px rgba(33,60,81,0.05)' 
      }}>
        {/* Header */}
        <div 
          onClick={() => setCommentaryExpanded(!commentaryExpanded)}
          style={{ 
            display: 'flex', 
            justifyContent: 'space-between', 
            alignItems: 'center', 
            padding: '15px 20px', 
            background: 'rgba(101, 148, 177, 0.05)', 
            borderBottom: commentaryExpanded ? '1px solid var(--primary-border)' : 'none',
            cursor: 'pointer',
            userSelect: 'none'
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span style={{ 
              fontSize: '12px', 
              transition: 'transform 0.2s', 
              transform: commentaryExpanded ? 'rotate(90deg)' : 'rotate(0deg)', 
              display: 'inline-block', 
              color: 'var(--primary-dark)' 
            }}>
              ▶
            </span>
            <h4 style={{ margin: 0, textTransform: 'uppercase', fontSize: '12px', letterSpacing: '0.05em', color: 'var(--primary-dark)', fontWeight: 'bold' }}>
              📢 Political Commentary Feed
            </h4>
          </div>

          {/* Filter Dropdown */}
          <div onClick={(e) => e.stopPropagation()}>
            <label htmlFor="commentary-filter" style={{ marginRight: '8px', fontSize: '11px', fontWeight: 'bold', color: 'var(--primary-dark)' }}>Filter:</label>
            <select 
              id="commentary-filter"
              value={commentaryFilter}
              onChange={(e) => setCommentaryFilter(e.target.value)}
              style={{
                padding: '4px 8px',
                borderRadius: '6px',
                border: '1px solid var(--primary-border)',
                background: '#ffffff',
                color: 'var(--primary-dark)',
                fontSize: '11px',
                fontWeight: 'bold',
                cursor: 'pointer',
                outline: 'none'
              }}
            >
              <option value="ALL">All Parties</option>
              {(turnData.parties || []).map(p => (
                <option key={p.id} value={p.name}>{p.name}</option>
              ))}
            </select>
          </div>
        </div>

        {/* Collapsible Content */}
        {commentaryExpanded && (
          <div style={{ padding: '20px' }}>
            {(!turnData.lastRoundCommentary || turnData.lastRoundCommentary.length === 0) ? (
              <p style={{ margin: 0, fontSize: '13px', opacity: 0.8, color: '#000000' }}>
                No commentary available yet. Submit a turn to generate reports.
              </p>
            ) : (() => {
              const filtered = turnData.lastRoundCommentary.filter(line => {
                if (commentaryFilter === 'ALL') return true;
                return line.toLowerCase().includes(commentaryFilter.toLowerCase());
              });

              if (filtered.length === 0) {
                return (
                  <p style={{ margin: 0, fontSize: '13px', opacity: 0.8, color: '#d23f31', fontWeight: 'bold' }}>
                    No commentary found matching this party.
                  </p>
                );
              }

              return (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', maxHeight: '350px', overflowY: 'auto', paddingRight: '10px' }}>
                  {filtered.map((line, i) => (
                    <div key={i} style={{ fontSize: '13px', borderBottom: '1px solid rgba(101, 148, 177, 0.1)', paddingBottom: '8px', lineHeight: 1.5, color: '#000000' }}>
                      💬 {line}
                    </div>
                  ))}
                </div>
              );
            })()}
          </div>
        )}
      </div>

      {/* Project View Section */}
      <div style={{ 
        border: '1px solid var(--primary-border)', 
        borderRadius: '12px', 
        marginBottom: '25px', 
        background: '#ffffff', 
        color: '#000000', 
        overflow: 'hidden', 
        boxShadow: '0 4px 12px rgba(33,60,81,0.05)' 
      }}>
        {/* Header */}
        <div 
          style={{ 
            display: 'flex', 
            justifyContent: 'space-between', 
            alignItems: 'center', 
            padding: '15px 20px', 
            background: 'rgba(101, 148, 177, 0.05)', 
            borderBottom: '1px solid var(--primary-border)',
            userSelect: 'none'
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span style={{ fontSize: '14px' }}>🏗️</span>
            <h4 style={{ margin: 0, textTransform: 'uppercase', fontSize: '12px', letterSpacing: '0.05em', color: 'var(--primary-dark)', fontWeight: 'bold' }}>
              Completed Projects & Yield View
            </h4>
          </div>
        </div>

        {/* Content */}
        <div style={{ padding: '20px' }}>
          {(() => {
            const activeParties = (turnData.parties || []).filter(p => p.role !== 'DEFEATED');
            return (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
                {activeParties.map(p => {
                  const completedProjects = (p.projects || [])
                    .filter(proj => proj.progressPercent === 100)
                    .sort((a, b) => (a.completionTurn || 0) - (b.completionTurn || 0));
                  
                  // Compute Net Yield
                  let netCoins = 0;
                  let netMorale = 0;
                  let netCorruption = 0;
                  let netMedia = 0;
                  let netSupport = 0;

                  completedProjects.forEach(proj => {
                    const rawKey = proj.projectKey;
                    const def = projectDefs[rawKey];
                    if (def) {
                      netCoins += def.benefitCoins || 0;
                      netMorale += def.benefitMorale || 0;
                      netCorruption += def.benefitCorruption || 0;
                      netMedia += def.benefitMedia || 0;
                      netSupport += def.benefitSupport || 0;
                    }
                  });

                  return (
                    <div key={p.id} style={{ borderBottom: '1px solid rgba(101, 148, 177, 0.1)', paddingBottom: '15px' }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '10px' }}>
                        <span style={{ width: '10px', height: '10px', borderRadius: '50%', backgroundColor: getPartyColor(p) }} />
                        <h5 style={{ margin: 0, fontSize: '14px', color: 'var(--primary-dark)' }}>
                          {p.name} {p.playerControlled && '(You)'}
                        </h5>
                      </div>

                      {completedProjects.length === 0 ? (
                        <div style={{ fontSize: '12px', color: '#64748b', paddingLeft: '18px' }}>
                          No completed projects yet.
                        </div>
                      ) : (
                        <div style={{ paddingLeft: '18px' }}>
                          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px', marginBottom: '10px' }}>
                            {completedProjects.map(proj => {
                              const def = projectDefs[proj.projectKey];
                              const name = def ? def.name : proj.projectKey;
                              return (
                                <span 
                                  key={proj.id} 
                                  style={{ 
                                    fontSize: '11px', 
                                    background: 'rgba(101, 148, 177, 0.1)', 
                                    color: 'var(--primary-dark)', 
                                    padding: '4px 10px', 
                                    borderRadius: '6px',
                                    fontWeight: '600'
                                  }}
                                >
                                  {name} {proj.targetPartyName && `🎯 ${proj.targetPartyName}`}
                                </span>
                              );
                            })}
                          </div>

                          {/* Net Yield Row */}
                          <div style={{ 
                            fontSize: '12px', 
                            background: 'rgba(23, 184, 144, 0.05)', 
                            border: '1px solid rgba(23, 184, 144, 0.15)',
                            padding: '8px 12px', 
                            borderRadius: '8px', 
                            display: 'inline-flex', 
                            gap: '12px',
                            color: '#15803d',
                            fontWeight: '600'
                          }}>
                            <span>Net Yield:</span>
                            {netCoins !== 0 && <span>💰 {netCoins > 0 ? '+' : ''}{netCoins} Coins</span>}
                            {netMorale !== 0 && <span>✊ {netMorale > 0 ? '+' : ''}{netMorale} Morale</span>}
                            {netCorruption !== 0 && <span>⚖️ {netCorruption > 0 ? '+' : ''}{netCorruption} Corruption</span>}
                            {netMedia !== 0 && <span>📢 {netMedia > 0 ? '+' : ''}{netMedia} Media</span>}
                            {netSupport !== 0 && <span>📈 {netSupport > 0 ? '+' : ''}{netSupport}% Support</span>}
                            {netCoins === 0 && netMorale === 0 && netCorruption === 0 && netMedia === 0 && netSupport === 0 && (
                              <span style={{ color: '#64748b' }}>No per-turn yields</span>
                            )}
                          </div>
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>
            );
          })()}
        </div>
      </div>
    </div>
  );
}
