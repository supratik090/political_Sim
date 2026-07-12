import React, { useState } from 'react';
import { useGameStore } from '../../store/gameStore';
import { getPartyColor, checkDefeatWarnings, renderStatDelta, getFactionDisplayName } from './gameUtils';
import { getPartyThemeByName } from '../../constants/partyThemes';
import { getPostByKey, getPostByName } from './postsConfig';

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

const calculateFactionYield = (f, p, projectDefs) => {
  if (!f.active) return { coins: 0, support: 0, morale: 0, corruption: 0, media: 0 };
  
  let mult = 1.0;
  if (f.loyalty >= 90) mult = 2.0;
  else if (f.loyalty >= 80) mult = 1.5;
  else if (f.loyalty >= 50) mult = 1.0;
  else if (f.loyalty >= 30) mult = 0.5;
  else mult = 0.0;

  const patronageCoins = f.patronage * 2;
  const patronageMorale = f.patronage * 1;
  const patronageCorruption = f.patronage * -1;
  const patronageMedia = f.patronage * 1;

  let postCoins = 0;
  let postMorale = 0;
  let postMedia = 0;

  const posts = Array.isArray(f.post) ? f.post : (f.post && f.post !== 'None' ? [f.post] : []);
  posts.forEach(pKey => {
    const postDef = getPostByKey(pKey) || getPostByName(pKey);
    if (postDef) {
      postCoins += postDef.coinBonus || 0;
      postMorale += postDef.moraleBonus || 0;
      postMedia += postDef.mediaBonus || 0;
    }
  });
  
  let projectCoins = 0;
  let projectMorale = 0;
  let projectMedia = 0;
  let projectCorruption = 0;
  let projectSupport = 0;
  
  const completedProjects = (p.projects || []).filter(proj => proj.progressPercent === 100 && proj.managingFactionKey === f.key);
  completedProjects.forEach(proj => {
    const def = projectDefs[proj.projectKey];
    if (def) {
      projectCoins += def.benefitCoins || 0;
      projectMorale += def.benefitMorale || 0;
      projectMedia += def.benefitMedia || 0;
      projectCorruption += def.benefitCorruption || 0;
      projectSupport += (def.benefitSupport || 0) * 0.01;
    }
  });

  const baseCoins = patronageCoins + postCoins + projectCoins;
  const baseMorale = patronageMorale + postMorale + projectMorale;
  const baseCorruption = patronageCorruption + projectCorruption;
  const baseMedia = patronageMedia + postMedia + projectMedia;
  const baseSupport = f.loyalty >= 50
    ? (f.influence * 0.01) + projectSupport
    : -(f.influence * 0.01) + projectSupport;
 
  return {
    coins: Math.round(baseCoins * mult),
    support: parseFloat((baseSupport * mult).toFixed(1)),
    morale: Math.round(baseMorale * mult),
    corruption: baseCorruption < 0 ? Math.round(baseCorruption * mult) : Math.round(baseCorruption * (2 - mult)),
    media: Math.round(baseMedia * mult)
  };
};

export default function StatsView({
  turnData,
  commentaryExpanded,
  setCommentaryExpanded,
  commentaryFilter,
  setCommentaryFilter,
  projectDefs = {},
  onOpenResolutionReport,
  scenarioBills = []
}) {
  const [isPartyInfoCollapsed, setIsPartyInfoCollapsed] = useState(true);
  const [expandedFactions, setExpandedFactions] = useState({});

  const toggleFactionExpand = (fKey) => {
    setExpandedFactions(prev => ({
      ...prev,
      [fKey]: !prev[fKey]
    }));
  };
  // In multiplayer: the current user's party is identified by activeHumanPartyId.
  // humanPlayerMap: { partyId -> userId } — contains ALL human players.Factions (Loyalty / Power)
  // We use activeHumanPartyId to show "You", and show "Player" for other human parties.
  const { user } = useGameStore();
  const humanPlayerMap = turnData.humanPlayerMap || {};

  const getMyPartyId = () => {
    if (turnData?.isMultiplayer && humanPlayerMap) {
      const loggedInUserId = (user?.id || user?.email)?.toLowerCase();
      const foundEntry = Object.entries(humanPlayerMap).find(
        ([partyId, userId]) => userId?.toLowerCase() === loggedInUserId
      );
      if (foundEntry) return foundEntry[0];
    }
    return turnData.activeHumanPartyId || turnData.parties?.find(p => p.playerControlled)?.id;
  };

  const myPartyId = getMyPartyId();

  const getPartyLabel = (party) => {
    if (party.id === myPartyId) return '(You)';
    if (humanPlayerMap[party.id]) return '(Player)';
    return '';
  };

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
                      <span>{partyName} {partyObj && partyObj.id === myPartyId && '(You)'}</span>
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
        const noConfidenceSucceeded = turnData.lastResults?.some(r => 
          r.startsWith('No-Confidence Successful') || r.startsWith('No-Confidence Lost')
        );
        const noConfidenceFailed = turnData.lastResults?.some(r => 
          r.startsWith('No-Confidence Motion failed')
        );

        if (!noConfidenceSucceeded && !noConfidenceFailed) return null;

        return (
          <div style={{
            background: noConfidenceSucceeded 
              ? 'linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%)' 
              : 'linear-gradient(135deg, #78350f 0%, #b45309 100%)',
            border: `2px solid ${noConfidenceSucceeded ? '#2563eb' : '#d97706'}`,
            borderRadius: '12px',
            padding: '15px',
            marginBottom: '20px',
            color: '#ffffff',
            boxShadow: `0 4px 15px ${noConfidenceSucceeded ? 'rgba(37, 99, 235, 0.2)' : 'rgba(217, 119, 6, 0.2)'}`
          }}>
            <h3 style={{ margin: '0 0 5px 0', color: '#ffffff', display: 'flex', alignItems: 'center', gap: '8px', fontSize: '16px' }}>
              ⚡ SPECIAL CONSTITUTIONAL EVENT: No-Confidence Vote
            </h3>
            <p style={{ margin: 0, fontSize: '13px', lineHeight: 1.5 }}>
              {noConfidenceSucceeded 
                ? 'The Opposition successfully triggered a No-Confidence Motion, leading to early state elections. Voting results determined the new Government!'
                : 'The Opposition triggered a No-Confidence Motion, but the Government survived the vote. No early elections were held.'}
            </p>
          </div>
        );
      })()}

      {/* Defeat Warnings Section */}
      {(() => {
        const allWarnings = [];
        turnData.parties.forEach(p => {
          if (p.id !== myPartyId) return; // only warn for current player's party
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

      {/* Last Turn Legislative Bill Vote Results */}
      {(() => {
        const lastTurnNum = turnData.turnNumber - 1;
        const lastResolvedBill = turnData.bills?.find(b => b.billKey === turnData.lastResolvedBillKey);
        const voteHappenedLastRound = lastResolvedBill && lastResolvedBill.turnResolved === lastTurnNum;
        if (!voteHappenedLastRound) return null;

        return (
          <div style={{
            border: '1px solid var(--primary-border)',
            borderRadius: '12px',
            padding: '20px',
            background: '#ffffff',
            marginBottom: '25px',
            boxShadow: '0 4px 12px rgba(33,60,81,0.05)'
          }}>
            <h4 style={{ margin: '0 0 6px 0', fontSize: '13px', color: 'var(--primary-dark)', fontWeight: 800, textTransform: 'uppercase', letterSpacing: '0.05em', display: 'flex', alignItems: 'center', gap: '6px' }}>
              🗳️ Last Turn Legislative Vote Tally
            </h4>
            <p style={{ margin: '0 0 15px 0', fontSize: '12px', color: '#6b7280', lineHeight: 1.4 }}>
              Vote results for bill: <strong>{scenarioBills?.find(b => b.billKey === turnData.lastResolvedBillKey)?.name || turnData.lastResolvedBillKey}</strong>.
            </p>

            {(() => {
              const yes = turnData.lastBillYesVotes || 0;
              const no = turnData.lastBillNoVotes || 0;
              const abstain = turnData.lastBillAbstainVotes || 0;
              const passed = yes > no && yes >= 30.0;
              
              let defeatReason = '';
              if (!passed) {
                if (yes > no && yes < 30.0) {
                  defeatReason = 'Quorum not present (minimum 30% YES votes required).';
                } else {
                  defeatReason = 'NO votes were greater than or equal to YES votes.';
                }
              }

              return (
                <div>
                  <div style={{
                    background: passed ? 'rgba(34, 197, 94, 0.08)' : 'rgba(239, 68, 68, 0.08)',
                    border: `1px solid ${passed ? '#22c55e' : '#ef4444'}`,
                    borderRadius: '8px',
                    padding: '10px 12px',
                    marginBottom: '15px',
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '2px'
                  }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '6px', fontWeight: 'bold', fontSize: '13px', color: passed ? '#15803d' : '#b91c1c' }}>
                      {passed ? '✅ PASSED' : '❌ DEFEATED'}
                    </div>
                    {!passed && (
                      <div style={{ fontSize: '11px', color: '#7f1d1d', fontWeight: 500 }}>
                        Reason: {defeatReason}
                      </div>
                    )}
                  </div>

                  {/* Chart Bar */}
                  <div style={{ display: 'flex', height: '24px', borderRadius: '6px', overflow: 'hidden', background: '#f3f4f6', marginBottom: '15px', border: '1px solid #e5e7eb' }}>
                    {yes > 0 && (
                      <div style={{ width: `${yes}%`, background: '#22c55e', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontSize: '10px', fontWeight: 'bold' }} title={`YES: ${yes.toFixed(1)}%`}>
                        YES {yes.toFixed(1)}%
                      </div>
                    )}
                    {no > 0 && (
                      <div style={{ width: `${no}%`, background: '#ef4444', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontSize: '10px', fontWeight: 'bold' }} title={`NO: ${no.toFixed(1)}%`}>
                        NO {no.toFixed(1)}%
                      </div>
                    )}
                    {abstain > 0 && (
                      <div style={{ width: `${abstain}%`, background: '#9ca3af', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontSize: '10px', fontWeight: 'bold' }} title={`ABSTAIN: ${abstain.toFixed(1)}%`}>
                        ABS {abstain.toFixed(1)}%
                      </div>
                    )}
                  </div>

                  {/* Vote Breakdown by Party */}
                  <div style={{ fontSize: '12px' }}>
                    <div style={{ fontWeight: 'bold', marginBottom: '8px', color: '#374151' }}>Party Vote Breakdown:</div>
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                      {Object.entries(turnData.lastBillPartyVotes || {}).map(([partyName, voteText]) => {
                        let color = '#374151';
                        let bg = '#f3f4f6';
                        if (voteText.startsWith('YES')) {
                          color = '#166534';
                          bg = '#dcfce7';
                        } else if (voteText.startsWith('NO')) {
                          color = '#991b1b';
                          bg = '#fee2e2';
                        } else if (voteText === 'ABSTAIN') {
                          color = '#374151';
                          bg = '#e5e7eb';
                        }
                        return (
                          <div key={partyName} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '6px 10px', borderRadius: '6px', background: '#fafafa', border: '1px solid #f0f0f0' }}>
                            <span style={{ fontWeight: 500, color: '#374151' }}>{partyName}</span>
                            <span style={{
                              fontSize: '11px',
                              fontWeight: 'bold',
                              padding: '2px 8px',
                              borderRadius: '4px',
                              color: color,
                              backgroundColor: bg
                            }}>{voteText}</span>
                          </div>
                        );
                      })}
                    </div>
                  </div>
                </div>
              );
            })()}
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
              isPlayer: p.id === myPartyId
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
                isPlayer: p.id === myPartyId,
                isOtherHuman: !!(humanPlayerMap[p.id]) && p.id !== myPartyId,
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
                    {item.name}
                    {item.isPlayer && <span style={{ marginLeft: '4px', fontSize: '10px', background: 'var(--selected-highlight)', color: '#fff', padding: '1px 5px', borderRadius: '6px', fontWeight: 700 }}> You</span>}
                    {item.isOtherHuman && <span style={{ marginLeft: '4px', fontSize: '10px', background: 'var(--primary-dark)', color: '#fff', padding: '1px 5px', borderRadius: '6px', fontWeight: 700 }}>Player</span>}

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
          const isPlayer = party.id === myPartyId;
          const isOtherHuman = !!(humanPlayerMap[party.id]) && !isPlayer;
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
                    ) : isOtherHuman ? (
                      <span style={{
                        background: 'var(--primary-dark)',
                        color: '#ffffff',
                        fontSize: '9px',
                        fontWeight: 900,
                        padding: '3px 8px',
                        borderRadius: '10px',
                        textTransform: 'uppercase'
                      }}>
                        👤 PLAYER
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

                  {/* Factions Loyalty & Power */}
                  {party.factions && party.factions.length > 0 && (
                    <div style={{ marginTop: '15px', paddingTop: '12px', borderTop: '1px dashed rgba(101, 148, 177, 0.2)' }}>
                      <span style={{ fontSize: '11px', fontWeight: '800', textTransform: 'uppercase', color: 'var(--primary-dark)', display: 'block', marginBottom: '8px', letterSpacing: '0.05em' }}>
                        ⚡ Factions (Loyalty / Power)
                      </span>
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                        {party.factions.map(f => {
                          let label = getFactionDisplayName(party.name, f.key);

                          if (!f.active) {
                            return (
                              <div key={f.key} style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11.5px', color: '#94a3b8', fontStyle: 'italic' }}>
                                <span>{label}</span>
                                <span>Purged</span>
                              </div>
                            );
                          }

                          return (
                            <div key={f.key} style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11.5px', alignItems: 'center' }}>
                              <span style={{ fontWeight: '500', color: 'var(--card-text)', display: 'inline-flex', alignItems: 'center' }}>
                                {label}
                                {f.frozenTurnsRemaining > 0 && <span style={{ color: '#ea580c', fontSize: '9px', fontWeight: 'bold', marginLeft: '6px', backgroundColor: '#fff7ed', border: '1px solid #ffedd5', padding: '1px 4px', borderRadius: '3px' }}>❄️ FROZEN ({f.frozenTurnsRemaining}t)</span>}
                              </span>
                              <span style={{ fontSize: '11px', display: 'inline-flex', alignItems: 'center', gap: '3px' }}>
                                ✊ <strong style={{ color: f.loyalty >= 80 ? '#16a34a' : (f.loyalty >= 50 ? '#ca8a04' : '#dc2626') }}>{f.loyalty}%</strong>
                                {(() => {
                                  const historyKey = `faction_loyalty_history_${turnData?.gameId || 'default'}`;
                                  let prevLoyalty = null;
                                  try {
                                    const historyData = JSON.parse(localStorage.getItem(historyKey) || '{}');
                                    prevLoyalty = historyData[turnData.turnNumber - 1]?.[f.key];
                                  } catch (e) {}
                                  if (prevLoyalty !== null && prevLoyalty !== undefined) {
                                    const diff = f.loyalty - prevLoyalty;
                                    if (diff > 0) return <span style={{ color: '#22c55e', fontSize: '9px', fontWeight: 'bold', marginLeft: '1px' }}>▲</span>;
                                    if (diff < 0) return <span style={{ color: '#ef4444', fontSize: '9px', fontWeight: 'bold', marginLeft: '1px' }}>▼</span>;
                                  }
                                  return null;
                                })()}
                                <span style={{ color: '#cbd5e1', margin: '0 2px' }}>|</span>
                                ⚡ <strong style={{ color: 'var(--primary-dark)' }}>{f.influence}%</strong>
                              </span>
                            </div>
                          );
                        })}
                      </div>
                    </div>
                  )}
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

      {/* Legislative Assembly Status Card */}
      <div style={{
        border: '1px solid var(--primary-border)',
        borderRadius: '12px',
        marginBottom: '25px',
        background: '#ffffff',
        overflow: 'hidden',
        boxShadow: '0 4px 12px rgba(33,60,81,0.05)'
      }}>
        {/* Card Header */}
        <div style={{
          background: 'rgba(var(--party-primary-color-rgb, 101, 148, 177), 0.05)',
          padding: '15px 20px',
          borderBottom: '1px solid var(--primary-border)',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center'
        }}>
          <h3 style={{ margin: 0, fontSize: '14px', fontWeight: '800', color: 'var(--primary-dark)', textTransform: 'uppercase', letterSpacing: '0.05em', display: 'flex', alignItems: 'center', gap: '8px' }}>
            🏛️ Legislative Assembly Agenda
          </h3>
          <span style={{ fontSize: '11px', fontWeight: 'bold', color: 'var(--primary-dark)', background: 'rgba(var(--party-primary-color-rgb, 101, 148, 177), 0.15)', padding: '2px 8px', borderRadius: '10px' }}>
            Active Bills
          </span>
        </div>

        {/* Card Body */}
        <div style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '15px' }}>
          
          {/* Active Bill Status */}
          {turnData.proposedBillKeyThisTurn ? (() => {
            const activeBillDef = scenarioBills.find(b => b.billKey === turnData.proposedBillKeyThisTurn);
            const billName = activeBillDef ? activeBillDef.name : turnData.proposedBillKeyThisTurn;
            const proposerParty = turnData.parties?.find(p => p.id === (turnData.bills?.find(b => b.billKey === turnData.proposedBillKeyThisTurn)?.proposedByPartyId));
            return (
              <div style={{
                background: 'rgba(var(--party-primary-color-rgb, 101, 148, 177), 0.03)',
                border: '1px solid var(--primary-border)',
                borderRadius: '8px',
                padding: '12px 15px'
              }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                  <span style={{ fontSize: '11px', background: '#3b82f6', color: '#fff', padding: '2px 6px', borderRadius: '4px', fontWeight: 'bold' }}>
                    🗳️ ACTIVE VOTE THIS MONTH
                  </span>
                  {proposerParty && (
                    <span style={{ fontSize: '11px', color: '#4b5563', fontWeight: 'bold' }}>
                      Proposed by: {proposerParty.name}
                    </span>
                  )}
                </div>
                <h4 style={{ margin: '0 0 4px 0', fontSize: '13px', fontWeight: 'bold', color: 'var(--primary-dark)' }}>
                  {billName}
                </h4>
                <p style={{ margin: 0, fontSize: '12px', color: '#6b7280', lineHeight: 1.4 }}>
                  {activeBillDef?.description || 'This bill is currently tabled and being voted on.'}
                </p>
              </div>
            );
          })() : (
            <div style={{
              background: '#f8fafc',
              border: '1px dashed #cbd5e1',
              borderRadius: '8px',
              padding: '15px',
              textAlign: 'center',
              color: '#64748b',
              fontSize: '12px',
              fontStyle: 'italic'
            }}>
              No active bill is up for vote this month. {turnData.activeEventKey ? 'A state affair event is currently active.' : ''}
            </div>
          )}

          {/* Legislative History / Bill Tracker */}
          <div>
            <h4 style={{ margin: '0 0 10px 0', fontSize: '12px', color: '#4b5563', fontWeight: 'bold', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
              📜 Bill Tracker History
            </h4>
            
            {(!turnData.bills || turnData.bills.length === 0) ? (
              <p style={{ margin: 0, fontSize: '12px', color: '#94a3b8', fontStyle: 'italic' }}>
                No bills in the agenda pool.
              </p>
            ) : (() => {
              // Group bills
              const passedBills = turnData.bills.filter(b => b.status === 'PASSED');
              const failedBills = turnData.bills.filter(b => b.status === 'FAILED');
              const pendingBills = turnData.bills.filter(b => b.status === 'PENDING_VOTE');
              const notProposedBills = turnData.bills.filter(b => b.status === 'NOT_PROPOSED');

              return (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                  {/* Lists of passed & failed */}
                  {passedBills.length === 0 && failedBills.length === 0 && pendingBills.length === 0 && (
                    <p style={{ margin: 0, fontSize: '12px', color: '#64748b', fontStyle: 'italic' }}>
                      No bills have been voted on or tabled yet. Propose bills in the Legislative tab.
                    </p>
                  )}

                  {pendingBills.map(b => {
                    const def = scenarioBills.find(x => x.billKey === b.billKey);
                    const proposerParty = turnData.parties?.find(p => p.id === b.proposedByPartyId);
                    const proposerName = proposerParty ? proposerParty.name : 'Government';
                    return (
                      <div key={b.billKey} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 12px', border: '1px solid #cbd5e1', borderRadius: '6px', fontSize: '12px', background: '#fff' }}>
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '2px' }}>
                          <span style={{ fontWeight: '600' }}>📋 {def?.name || b.billKey}</span>
                          <span style={{ fontSize: '11px', color: '#64748b' }}>Proposed by: <strong>{proposerName}</strong></span>
                        </div>
                        <span style={{ background: '#3b82f6', color: '#fff', fontSize: '10px', padding: '2px 6px', borderRadius: '4px', fontWeight: 'bold' }}>PENDING VOTE (Turn {b.turnProposed})</span>
                      </div>
                    );
                  })}

                  {passedBills.map(b => {
                    const def = scenarioBills.find(x => x.billKey === b.billKey);
                    const proposerParty = turnData.parties?.find(p => p.id === b.proposedByPartyId);
                    const proposerName = proposerParty ? proposerParty.name : 'Government';
                    return (
                      <div key={b.billKey} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 12px', border: '1px solid #bbf7d0', borderRadius: '6px', fontSize: '12px', background: '#f0fdf4' }}>
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '2px' }}>
                          <span style={{ fontWeight: '600', color: '#166534' }}>✅ {def?.name || b.billKey}</span>
                          <span style={{ fontSize: '11px', color: '#166534', opacity: 0.8 }}>Proposed by: <strong>{proposerName}</strong></span>
                        </div>
                        <span style={{ background: '#22c55e', color: '#fff', fontSize: '10px', padding: '2px 6px', borderRadius: '4px', fontWeight: 'bold' }}>PASSED (Turn {b.turnResolved})</span>
                      </div>
                    );
                  })}

                  {failedBills.map(b => {
                    const def = scenarioBills.find(x => x.billKey === b.billKey);
                    const proposerParty = turnData.parties?.find(p => p.id === b.proposedByPartyId);
                    const proposerName = proposerParty ? proposerParty.name : 'Government';
                    return (
                      <div key={b.billKey} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '8px 12px', border: '1px solid #fecaca', borderRadius: '6px', fontSize: '12px', background: '#fef2f2' }}>
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '2px' }}>
                          <span style={{ fontWeight: '600', color: '#9f1239' }}>❌ {def?.name || b.billKey}</span>
                          <span style={{ fontSize: '11px', color: '#9f1239', opacity: 0.8 }}>Proposed by: <strong>{proposerName}</strong></span>
                        </div>
                        <span style={{ background: '#ef4444', color: '#fff', fontSize: '10px', padding: '2px 6px', borderRadius: '4px', fontWeight: 'bold' }}>FAILED (Turn {b.turnResolved})</span>
                      </div>
                    );
                  })}

                  {/* Summary counts */}
                  <div style={{ display: 'flex', gap: '15px', fontSize: '11px', color: '#64748b', fontWeight: 'bold', borderTop: '1px dashed var(--primary-border)', paddingTop: '8px', marginTop: '4px' }}>
                    <span>Total Pool: {turnData.bills.length}</span>
                    <span style={{ color: '#166534' }}>Passed: {passedBills.length}</span>
                    <span style={{ color: '#9f1239' }}>Defeated: {failedBills.length}</span>
                    <span>Remaining Agenda: {notProposedBills.length}</span>
                  </div>
                </div>
              );
            })()}
          </div>

        </div>
      </div>

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
          onClick={() => setIsPartyInfoCollapsed(!isPartyInfoCollapsed)}
          style={{ 
            display: 'flex', 
            justifyContent: 'space-between', 
            alignItems: 'center', 
            padding: '15px 20px', 
            background: 'rgba(101, 148, 177, 0.05)', 
            borderBottom: isPartyInfoCollapsed ? 'none' : '1px solid var(--primary-border)',
            userSelect: 'none',
            cursor: 'pointer'
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span style={{ fontSize: '14px' }}>🛡️</span>
            <h4 style={{ margin: 0, textTransform: 'uppercase', fontSize: '12px', letterSpacing: '0.05em', color: 'var(--primary-dark)', fontWeight: 'bold' }}>
              Inner Party Factions
            </h4>
          </div>
          <span style={{ fontSize: '12.5px', fontWeight: 'bold', color: 'var(--primary-dark)', opacity: 0.8 }}>
            {isPartyInfoCollapsed ? '▼ Expand' : '▲ Collapse'}
          </span>
        </div>

        {/* Content */}
        {!isPartyInfoCollapsed && (
          <div style={{ padding: '20px' }}>
          {(() => {
            const activeParties = (turnData.parties || []).filter(p => p.role !== 'DEFEATED');
            return (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '25px' }}>
                {activeParties.map(p => {
                  const completedProjects = (p.projects || [])
                    .filter(proj => proj.progressPercent === 100)
                    .sort((a, b) => (a.completionTurn || 0) - (b.completionTurn || 0));

                  const activeFactions = (p.factions || []).filter(f => f.active);
                  const factionYields = activeFactions.map(f => {
                    const y = calculateFactionYield(f, p, projectDefs);
                    const completedProjectsForFaction = (p.projects || []).filter(proj => proj.progressPercent === 100 && proj.managingFactionKey === f.key);
                    return { faction: f, yields: y, projects: completedProjectsForFaction };
                  });

                  let netCoins = 0;
                  let rawSupport = 0;
                  let netMorale = 0;
                  let netCorruption = 0;
                  let netMedia = 0;

                  factionYields.forEach(fy => {
                    netCoins += fy.yields.coins;
                    rawSupport += fy.yields.support;
                    netMorale += fy.yields.morale;
                    netCorruption += fy.yields.corruption;
                    netMedia += fy.yields.media;
                  });

                  const netSupport = Math.ceil(rawSupport);
                  const finalMorale = netMorale >= 0 ? netMorale : Math.max(-5, netMorale);
                  const finalCorruption = netCorruption <= 0 ? Math.max(-5, netCorruption) : Math.min(5, netCorruption);

                  return (
                    <div key={p.id} style={{ borderBottom: '1px solid rgba(101, 148, 177, 0.15)', paddingBottom: '20px' }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '12px' }}>
                        <span style={{ width: '10px', height: '10px', borderRadius: '50%', backgroundColor: getPartyColor(p) }} />
                        <h5 style={{ margin: 0, fontSize: '15px', color: 'var(--primary-dark)', fontWeight: 'bold' }}>
                          {p.name} {p.id === myPartyId && '(You)'}
                        </h5>
                      </div>

                      {/* Party Factions Details Grid */}
                      <div style={{ paddingLeft: '18px', display: 'flex', flexDirection: 'column', gap: '12px', marginBottom: '15px' }}>
                        {factionYields.map(fy => {
                          const { faction: f, yields: y, projects } = fy;
                          const getMoodText = (loy) => {
                            if (loy >= 80) return 'Good 😊';
                            if (loy >= 50) return 'Neutral 😐';
                            if (loy >= 30) return 'Bad 😡';
                            return 'Rebel 💀';
                          };
                          const getMoodColor = (loy) => {
                            if (loy >= 80) return '#22c55e';
                            if (loy >= 50) return '#64748b';
                            if (loy >= 30) return '#f97316';
                            return '#ef4444';
                          };
                          
                          return (
                            <div key={f.key || f.id} style={{
                              background: '#ffffff',
                              border: `1.5px solid ${getMoodColor(f.loyalty)}`,
                              borderRadius: '8px',
                              padding: '12px 16px',
                              boxShadow: '0 2px 5px rgba(0,0,0,0.02)'
                            }}>
                              {/* Header row: Faction Name, Power, Loyalty */}
                              <div 
                                onClick={() => toggleFactionExpand(`${p.id}_${f.key || f.id}`)}
                                style={{ 
                                  display: 'flex', 
                                  justifyContent: 'space-between', 
                                  alignItems: 'center', 
                                  marginBottom: expandedFactions[`${p.id}_${f.key || f.id}`] ? '8px' : '0', 
                                  borderBottom: expandedFactions[`${p.id}_${f.key || f.id}`] ? '1px solid var(--primary-border)' : 'none', 
                                  paddingBottom: expandedFactions[`${p.id}_${f.key || f.id}`] ? '6px' : '0',
                                  cursor: 'pointer',
                                  userSelect: 'none'
                                }}
                              >
                                <span style={{ fontSize: '13px', fontWeight: 'bold', color: 'var(--primary-dark)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                                  <span>{expandedFactions[`${p.id}_${f.key || f.id}`] ? '▼' : '►'}</span>
                                  <span>{getFactionDisplayName(p.name, f.key)}</span>
                                </span>
                                <span style={{ fontSize: '11px', color: 'var(--card-text)', display: 'inline-flex', alignItems: 'center', gap: '3px' }}>
                                  ⚡ <b>{f.influence}%</b> | ✊ <b style={{ color: getMoodColor(f.loyalty) }}>{f.loyalty}% ({getMoodText(f.loyalty)})</b>
                                  {(() => {
                                    const historyKey = `faction_loyalty_history_${turnData?.gameId || 'default'}`;
                                    let prevLoyalty = null;
                                    try {
                                      const historyData = JSON.parse(localStorage.getItem(historyKey) || '{}');
                                      prevLoyalty = historyData[turnData.turnNumber - 1]?.[f.key];
                                    } catch (e) {}
                                    if (prevLoyalty !== null && prevLoyalty !== undefined) {
                                      const diff = f.loyalty - prevLoyalty;
                                      if (diff > 0) return <span style={{ color: '#22c55e', fontSize: '9px', fontWeight: 'bold', marginLeft: '1px' }}>▲</span>;
                                      if (diff < 0) return <span style={{ color: '#ef4444', fontSize: '9px', fontWeight: 'bold', marginLeft: '1px' }}>▼</span>;
                                    }
                                    return null;
                                  })()}
                                </span>
                              </div>

                              {/* Collapsible details content */}
                              {expandedFactions[`${p.id}_${f.key || f.id}`] && (() => {
                                const frozenPostsCount = f.frozenPosts ? Object.values(f.frozenPosts).filter(t => t > 0).length : 0;
                                const frozenPatronageCount = f.frozenPatronageTurns ? f.frozenPatronageTurns.filter(t => t > 0).length : 0;
                                const frozenProjectsCount = projects.filter(proj => proj.frozenTurnsRemaining > 0).length;
                                const totalFrozenAssets = frozenPostsCount + frozenPatronageCount + frozenProjectsCount;

                                return (
                                  <div style={{ marginTop: '10px', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                                    {f.frozenTurnsRemaining > 0 && (
                                      <div style={{
                                        fontSize: '11px',
                                        color: '#c2410c',
                                        backgroundColor: '#fff7ed',
                                        border: '1.5px dashed #ffedd5',
                                        padding: '6px 10px',
                                        borderRadius: '6px',
                                        fontWeight: '800',
                                        display: 'flex',
                                        alignItems: 'center',
                                        gap: '4px',
                                        marginBottom: '4px'
                                      }}>
                                        ❄️ SABOTAGE ALERT: Faction is frozen! {totalFrozenAssets} card/asset{totalFrozenAssets !== 1 ? 's' : ''} disabled for {f.frozenTurnsRemaining} turn{f.frozenTurnsRemaining !== 1 ? 's' : ''}.
                                      </div>
                                    )}
                                    {/* Allocation details */}
                                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '8px', fontSize: '11px', color: '#475569', marginBottom: '8px' }}>
                                    <div>
                                      💼 <b>Posts:</b> {(() => {
                                        const posts = Array.isArray(f.post) ? f.post : (f.post && f.post !== 'None' ? [f.post] : []);
                                        if (posts.length === 0) return 'None';
                                        return posts.map(pKey => {
                                          const def = getPostByKey(pKey) || getPostByName(pKey);
                                          return def ? def.name : pKey;
                                        }).join(', ');
                                      })()}
                                    </div>
                                    <div>
                                      🛡️ <b>Patronage:</b> {f.patronage > 0 ? `${f.patronage} Point${f.patronage > 1 ? 's' : ''}` : 'None'}
                                    </div>
                                    <div>
                                      🏗️ <b>Projects:</b> {projects.length === 0 ? 'None' : projects.map(proj => {
                                        const def = projectDefs[proj.projectKey];
                                        return def ? def.name : proj.projectKey;
                                      }).join(', ')}
                                    </div>
                                  </div>

                                  {/* Faction Yields row */}
                                  <div style={{ display: 'flex', gap: '15px', fontSize: '11px', fontWeight: 'bold', borderTop: '1px dotted var(--primary-border)', paddingTop: '6px' }}>
                                    <span style={{ color: '#15803d' }}>Coins: {y.coins >= 0 ? '+' : ''}{y.coins} 💰</span>
                                    <span style={{ color: '#1d4ed8' }}>Support: {y.support >= 0 ? '+' : ''}{y.support}% 📈</span>
                                    <span style={{ color: '#a21caf' }}>Morale: {y.morale >= 0 ? '+' : ''}{y.morale} ✊</span>
                                    <span style={{ color: y.corruption > 0 ? '#b91c1c' : '#15803d' }}>Corruption: {y.corruption >= 0 ? '+' : ''}{y.corruption} ⚖️</span>
                                    <span style={{ color: '#ec4899' }}>Media: {y.media >= 0 ? '+' : ''}{y.media} 📢</span>
                                  </div>
                                </div>
                              );
                            })()}
                            </div>
                          );
                        })}
                      </div>

                      {/* Net Yield Row */}
                      <div style={{ paddingLeft: '18px' }}>
                        <div style={{ 
                          fontSize: '12px', 
                          background: 'rgba(22, 163, 74, 0.05)', 
                          border: '1.5px solid rgba(22, 163, 74, 0.25)',
                          padding: '10px 16px', 
                          borderRadius: '8px', 
                          display: 'inline-flex', 
                          flexWrap: 'wrap',
                          gap: '14px',
                          color: '#166534',
                          fontWeight: 'bold'
                        }}>
                          <span>Combined Yield Sum:</span>
                          <span>💰 {netCoins >= 0 ? '+' : ''}{netCoins} Coins</span>
                          <span>📈 {netSupport >= 0 ? '+' : ''}{netSupport}% Support</span>
                          <span>✊ {finalMorale >= 0 ? '+' : ''}{finalMorale} Morale</span>
                          <span>⚖️ {finalCorruption >= 0 ? '+' : ''}{finalCorruption} Corruption</span>
                          <span>📢 {netMedia >= 0 ? '+' : ''}{netMedia} Media</span>
                        </div>
                      </div>
                    </div>
                  );
                })}
              </div>
            );
          })()}
        </div>
      )}
      </div>
    </div>
  );
}
