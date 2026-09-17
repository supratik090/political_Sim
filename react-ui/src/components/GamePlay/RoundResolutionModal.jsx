import React, { useState, useEffect, useRef } from 'react';

// Rolling number animation component
function RollingNumber({ value, prefix = '', suffix = '' }) {
  const [current, setCurrent] = useState(0);

  useEffect(() => {
    let start = 0;
    const end = value;
    if (start === end) {
      setCurrent(end);
      return;
    }
    const duration = 1000; // 1s animation
    const range = end - start;
    let currentTimer = start;
    const increment = end > start ? 1 : -1;
    const stepTime = Math.abs(Math.floor(duration / range));
    
    if (!isFinite(stepTime) || stepTime < 10) {
      setCurrent(end);
      return;
    }

    const timer = setInterval(() => {
      currentTimer += increment;
      setCurrent(currentTimer);
      if (currentTimer === end) {
        clearInterval(timer);
      }
    }, stepTime);

    return () => clearInterval(timer);
  }, [value]);

  const isPositive = value > 0;
  const isZero = value === 0;
  const displayVal = isZero ? '0' : (isPositive ? `+${current}` : `${current}`);

  return <span>{prefix}{displayVal}{suffix}</span>;
}

// Particle generator canvas
function ConfettiCanvas({ mode }) {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let animationFrameId;
    
    canvas.width = canvas.parentElement.clientWidth || 500;
    canvas.height = canvas.parentElement.clientHeight || 550;

    const particles = [];
    const particleCount = mode === 'JACKPOT' ? 80 : 50;

    class Particle {
      constructor() {
        this.x = Math.random() * canvas.width;
        if (mode === 'JACKPOT') {
          this.y = Math.random() * -50;
          this.vy = Math.random() * 4 + 2;
          this.vx = Math.random() * 2 - 1;
          this.color = Math.random() > 0.5 ? '#fbbf24' : '#10b981';
          this.size = Math.random() * 6 + 4;
          this.type = Math.random() > 0.7 ? 'coin' : 'circle';
        } else {
          this.y = canvas.height + Math.random() * 50;
          this.vy = -(Math.random() * 3 + 1);
          this.vx = Math.random() * 3 - 1.5;
          this.color = Math.random() > 0.5 ? '#ef4444' : '#f97316';
          this.size = Math.random() * 4 + 2;
          this.type = 'spark';
        }
      }

      update() {
        this.x += this.vx;
        this.y += this.vy;
        
        if (mode === 'JACKPOT') {
          if (this.y > canvas.height) {
            this.y = -20;
            this.x = Math.random() * canvas.width;
          }
        } else {
          if (this.y < -20) {
            this.y = canvas.height + 20;
            this.x = Math.random() * canvas.width;
          }
        }
      }

      draw() {
        ctx.beginPath();
        if (this.type === 'coin') {
          ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
          ctx.fillStyle = '#f59e0b';
          ctx.fill();
          ctx.lineWidth = 1;
          ctx.strokeStyle = '#d97706';
          ctx.stroke();
        } else {
          ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
          ctx.fillStyle = this.color;
          ctx.fill();
        }
      }
    }

    for (let i = 0; i < particleCount; i++) {
      particles.push(new Particle());
    }

    const render = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      particles.forEach(p => {
        p.update();
        p.draw();
      });
      animationFrameId = requestAnimationFrame(render);
    };

    render();

    return () => {
      cancelAnimationFrame(animationFrameId);
    };
  }, [mode]);

  return (
    <canvas 
      ref={canvasRef} 
      style={{
        position: 'absolute',
        top: 0,
        left: 0,
        width: '100%',
        height: '100%',
        pointerEvents: 'none',
        zIndex: 5
      }} 
    />
  );
}

export default function RoundResolutionModal({
  isOpen,
  onClose,
  turnData,
  activeParty,
  partyColor = '#6594b1',
  projectDefs = {}
}) {
  if (!isOpen || !turnData || !activeParty) return null;

  const lastTurnNum = turnData.turnNumber - 1;
  if (lastTurnNum <= 0) return null;

  const partyDeltas = turnData.lastMetricDeltas?.[activeParty.id] || {};
  
  const statsList = [
    { key: 'coins', label: 'Coins', icon: '💰', val: partyDeltas.coins || 0, suffix: '' },
    { key: 'partyMorale', label: 'Morale', icon: '✊', val: partyDeltas.partyMorale || 0, suffix: '' },
    { key: 'publicSupport', label: 'Support', icon: '📈', val: partyDeltas.publicSupport || 0, suffix: '%' },
    { key: 'corruptionScore', label: 'Corruption', icon: '⚖️', val: partyDeltas.corruptionScore || 0, suffix: '', invertColor: true },
    { key: 'mediaImage', label: 'Media', icon: '📢', val: partyDeltas.mediaImage || 0, suffix: '' }
  ];

  const completedProjectsLastTurn = (activeParty.projects || []).filter(p => p.progressPercent === 100 && p.completionTurn === lastTurnNum);
  const hasCompletedProject = completedProjectsLastTurn.length > 0;
  const allCompletedProjects = (activeParty.projects || []).filter(p => p.progressPercent === 100);
  
  let netCoins = 0;
  let netMorale = 0;
  let netCorruption = 0;
  let netMedia = 0;
  let netSupport = 0;

  allCompletedProjects.forEach(proj => {
    const def = projectDefs[proj.projectKey];
    if (def) {
      netCoins += def.benefitCoins || 0;
      netMorale += def.benefitMorale || 0;
      netCorruption += def.benefitCorruption || 0;
      netMedia += def.benefitMedia || 0;
      netSupport += def.benefitSupport || 0;
    }
  });

  const hasYields = netCoins !== 0 || netMorale !== 0 || netCorruption !== 0 || netMedia !== 0 || netSupport !== 0;

  // Legislative Vote Info
  const lastResolvedBillKey = turnData.lastResolvedBillKey;
  const lastResolvedBill = turnData.bills?.find(b => b.billKey === lastResolvedBillKey);
  const voteHappenedLastRound = lastResolvedBill && lastResolvedBill.turnResolved === lastTurnNum;

  // Classify Success (Jackpot) and Failure (Bust)
  const isPlayerBillPassed = voteHappenedLastRound && lastResolvedBill.proposedByPartyId === activeParty.id && lastResolvedBill.status === 'PASSED';
  const isPlayerBillFailed = voteHappenedLastRound && lastResolvedBill.proposedByPartyId === activeParty.id && lastResolvedBill.status === 'FAILED';
  const playerBid = turnData.lastRoundBids?.[activeParty.id] || 0;
  const wonBiddingWithBid = (turnData.lastRoundWinnerPartyId === activeParty.id) && (playerBid > 0);
  const hasLootDropped = turnData.lastRoundDroppedReward && turnData.lastRoundDroppedReward.partyId === activeParty.id;

  const isMajorMoraleLoss = (partyDeltas.partyMorale || 0) <= -15;
  const isMajorSupportLoss = (partyDeltas.publicSupport || 0) <= -8;
  // Coin loss is normal unless it triggers defeat warning safety threshold (Coins < 10)
  const isDefeatWarning = activeParty.hasDefeatHazard || (activeParty.stats?.coins < 10) || (activeParty.stats?.partyMorale < 10) || (activeParty.stats?.publicSupport < 5) || (activeParty.stats?.corruptionScore > 95);
  const isBribeScandal = turnData.lastResults?.some(r => r.includes("Bribe Scandal Exposed"));

  const isBust = isPlayerBillFailed || isMajorMoraleLoss || isMajorSupportLoss || isDefeatWarning || isBribeScandal;
  const isSuccess = !isBust && (isPlayerBillPassed || wonBiddingWithBid || hasLootDropped);

  // Set colors and titles based on outcome mode
  let headerColor = partyColor;
  let modalBorder = `2px solid ${partyColor}`;
  let modeName = 'DEFAULT';
  let headerTitle = 'Round Resolution Report';

  if (isBust) {
    headerColor = '#be123c';
    modalBorder = '2px solid #f43f5e';
    modeName = 'BUST';
    headerTitle = '⚠️ Turn Resolution Alert';
  } else if (isSuccess) {
    headerColor = '#047857';
    modalBorder = '2px solid #10b981';
    modeName = 'SUCCESS';
    if (wonBiddingWithBid) {
      headerTitle = '🏆 Winning Bid';
    } else if (isPlayerBillPassed) {
      headerTitle = '📜 Legislative Bill Passed';
    } else if (hasLootDropped) {
      headerTitle = '🎁 Special Reward Claimed';
    } else {
      headerTitle = '✨ Round Success';
    }
  }

  return (
    <div
      className="modal-overlay"
      style={{
        fontFamily: "'Inter', system-ui, sans-serif",
        zIndex: 9999,
        backgroundColor: 'rgba(9, 13, 22, 0.85)',
        backdropFilter: 'blur(8px)',
      }}
    >
      {/* Style block for animations */}
      <style dangerouslySetInnerHTML={{__html: `
        @keyframes modalSlideIn {
          from { transform: translateY(30px); opacity: 0; }
          to { transform: translateY(0); opacity: 1; }
        }
        @keyframes modalShake {
          0%, 100% { transform: translateX(0); }
          20%, 60% { transform: translateX(-8px); }
          40%, 80% { transform: translateX(8px); }
        }
      `}} />

      <div
        className="modal-card"
        style={{
          backgroundColor: '#ffffff',
          maxWidth: '520px',
          boxShadow: modeName === 'SUCCESS'
            ? '0 15px 35px rgba(16, 185, 129, 0.2)'
            : (modeName === 'BUST' ? '0 15px 35px rgba(239, 68, 68, 0.2)' : '0 15px 40px rgba(0, 0, 0, 0.4)'),
          border: modalBorder,
          animation: modeName === 'BUST' ? 'modalShake 0.4s ease-out' : 'modalSlideIn 0.3s ease-out'
        }}
      >
        {/* Sticky Modal Header */}
        <div
          className="modal-header"
          style={{
            backgroundColor: headerColor,
            padding: '16px 20px',
            color: '#ffffff',
            textAlign: 'center',
          }}
        >
          <h2 style={{ margin: 0, fontSize: '17px', fontWeight: '800', textTransform: 'uppercase', letterSpacing: '0.04em' }}>
            {headerTitle}
          </h2>
          <div style={{ fontSize: '12px', fontWeight: 'bold', marginTop: '3px', opacity: 0.9 }}>
            Turn {lastTurnNum}
          </div>
          <button
            className="modal-close-btn"
            onClick={onClose}
            style={{
              position: 'absolute',
              top: '12px',
              right: '12px',
              background: 'rgba(255, 255, 255, 0.2)',
              border: 'none',
              color: '#ffffff',
              borderRadius: '50%',
              width: '34px',
              height: '34px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              cursor: 'pointer',
              fontWeight: 'bold',
              fontSize: '16px',
              flexShrink: 0,
              zIndex: 11
            }}
            aria-label="Close"
          >
            ✕
          </button>
        </div>

        {/* Scrollable Modal Body */}
        <div className="modal-body" style={{ padding: '16px', display: 'flex', flexDirection: 'column', gap: '14px' }}>

          {/* Resource Changes Grid */}
          <div>
            <h4 style={{ margin: '0 0 10px 0', fontSize: '11px', textTransform: 'uppercase', letterSpacing: '0.05em', color: '#64748b', fontWeight: 'bold' }}>
              Resource Changes Last Turn
            </h4>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: '6px' }}>
              {statsList.map(stat => {
                const isPositive = stat.val > 0;
                const isZero = stat.val === 0;

                let colorClass = '#64748b';
                if (!isZero) {
                  if (stat.invertColor) {
                    colorClass = isPositive ? '#ef4444' : '#22c55e';
                  } else {
                    colorClass = isPositive ? '#22c55e' : '#ef4444';
                  }
                }

                return (
                  <div key={stat.key} style={{
                    background: '#f8fafc',
                    border: '1px solid #e2e8f0',
                    borderRadius: '10px',
                    padding: '8px 3px',
                    textAlign: 'center',
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    gap: '3px'
                  }}>
                    <span style={{ fontSize: '17px' }}>{stat.icon}</span>
                    <span style={{ fontSize: '9px', color: '#64748b', fontWeight: '600', textTransform: 'uppercase' }}>
                      {stat.label}
                    </span>
                    <span style={{
                      fontSize: '12px',
                      fontWeight: 'bold',
                      color: colorClass
                    }}>
                      <RollingNumber value={stat.val} suffix={stat.suffix} />
                    </span>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Operations, Sabotage & Diplomacy Log */}
          {(() => {
            const opsLines = [];
            if (turnData.lastRoundCommentary) {
              turnData.lastRoundCommentary.forEach(line => {
                if (
                  line.includes('Sabotage') ||
                  line.includes('bribed') ||
                  line.includes('Bribe Scandal') ||
                  line.includes('Exposed') ||
                  line.includes('Diplomatic') ||
                  line.includes('Pact') ||
                  line.includes('FROZEN') ||
                  line.includes('Reward played') ||
                  line.includes('ABSTAINED')
                ) {
                  opsLines.push(line);
                }
              });
            }
            if (turnData.lastResults) {
              turnData.lastResults.forEach(line => {
                if (
                  (line.includes('bribed') || line.includes('Exposed') || line.includes('Sabotage') || line.includes('Pact')) &&
                  !opsLines.some(existing => existing.includes(line))
                ) {
                  opsLines.push(line);
                }
              });
            }

            if (opsLines.length === 0) return null;

            return (
              <div style={{
                background: '#f8fafc',
                border: '2px solid #64748b',
                borderRadius: '12px',
                padding: '12px',
                boxShadow: '0 4px 12px rgba(0,0,0,0.05)'
              }}>
                <h4 style={{ margin: '0 0 8px 0', fontSize: '11px', textTransform: 'uppercase', letterSpacing: '0.05em', color: '#334155', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '6px' }}>
                  🚨 Operations, Sabotage &amp; Diplomacy Log
                </h4>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', maxHeight: '150px', overflowY: 'auto', paddingRight: '4px' }}>
                  {opsLines.map((line, idx) => {
                    const isFailure = line.includes('Exposed') || line.includes('FAILED') || line.includes('Scandal');
                    const isSabotage = line.includes('Sabotage') || line.includes('bribed') || line.includes('FROZEN');
                    const isDiplomacy = line.includes('Diplomatic') || line.includes('Pact');

                    let bg = '#eff6ff';
                    let border = '#bfdbfe';
                    let color = '#1e40af';

                    if (isFailure) {
                      bg = '#fef2f2'; border = '#fca5a5'; color = '#991b1b';
                    } else if (isSabotage) {
                      bg = '#fff7ed'; border = '#fdba74'; color = '#9a3412';
                    } else if (isDiplomacy) {
                      bg = '#f0fdf4'; border = '#86efac'; color = '#166534';
                    }

                    return (
                      <div key={idx} style={{
                        background: bg,
                        border: `1px solid ${border}`,
                        color: color,
                        borderRadius: '8px',
                        padding: '6px 10px',
                        fontSize: '11px',
                        fontWeight: '600',
                        lineHeight: 1.4
                      }}>
                        {line}
                      </div>
                    );
                  })}
                </div>
              </div>
            );
          })()}

          {/* Last Turn Legislative Bill Vote Results */}
          {(() => {
            if (!voteHappenedLastRound) return null;

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
              <div style={{
                background: '#f8fafc',
                border: passed ? '2px solid #34d399' : '2px solid #ef4444',
                borderRadius: '12px',
                padding: '12px',
                boxShadow: passed ? '0 0 10px rgba(52, 211, 153, 0.15)' : '0 0 10px rgba(239, 68, 68, 0.15)'
              }}>
                <h4 style={{ margin: '0 0 8px 0', fontSize: '11px', textTransform: 'uppercase', letterSpacing: '0.05em', color: '#64748b', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '6px' }}>
                  🗳️ Legislative Vote: {lastResolvedBillKey}
                </h4>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  <div style={{
                    background: passed ? 'rgba(34, 197, 94, 0.08)' : 'rgba(239, 68, 68, 0.08)',
                    border: `1px solid ${passed ? '#22c55e' : '#ef4444'}`,
                    borderRadius: '8px',
                    padding: '7px 10px',
                    fontWeight: 'bold',
                    fontSize: '12px',
                    color: passed ? '#15803d' : '#b91c1c'
                  }}>
                    {passed ? '✅ PASSED' : '❌ DEFEATED'}
                    {!passed && (
                      <div style={{ fontSize: '10px', color: '#7f1d1d', fontWeight: 500, marginTop: '2px' }}>
                        Reason: {defeatReason}
                      </div>
                    )}
                  </div>

                  {/* Parliament semi-circle seating chart */}
                  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', margin: '6px 0' }}>
                    <svg width="200" height="100" viewBox="0 0 240 120" style={{ overflow: 'visible', maxWidth: '100%' }}>
                      <style dangerouslySetInnerHTML={{__html: `
                        @keyframes seatPop {
                          0% { transform: scale(0); opacity: 0; }
                          70% { transform: scale(1.3); opacity: 0.8; }
                          100% { transform: scale(1); opacity: 1; }
                        }
                      `}} />
                      {(() => {
                        const totalSeats = 100;
                        const yesCount = Math.min(totalSeats, Math.round(yes));
                        const abstainCount = Math.min(totalSeats - yesCount, Math.round(abstain));
                        const noCount = Math.max(0, totalSeats - yesCount - abstainCount);

                        const seats = [];
                        const arcs = [
                          { r: 35, count: 12 },
                          { r: 55, count: 20 },
                          { r: 75, count: 28 },
                          { r: 95, count: 40 }
                        ];

                        arcs.forEach(arc => {
                          for (let i = 0; i < arc.count; i++) {
                            const angle = Math.PI - (i * Math.PI / (arc.count - 1));
                            seats.push({
                              x: 120 + arc.r * Math.cos(angle),
                              y: 110 - arc.r * Math.sin(angle)
                            });
                          }
                        });

                        seats.sort((a, b) => a.x - b.x);

                        return seats.map((s, index) => {
                          let color = '#ef4444';
                          if (index < yesCount) {
                            color = '#22c55e';
                          } else if (index < yesCount + abstainCount) {
                            color = '#9ca3af';
                          }

                          return (
                            <circle
                              key={index}
                              cx={s.x}
                              cy={s.y}
                              r="4.5"
                              fill={color}
                              style={{
                                transformOrigin: `${s.x}px ${s.y}px`,
                                animation: 'seatPop 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) both',
                                animationDelay: `${index * 0.01}s`
                              }}
                            />
                          );
                        });
                      })()}
                    </svg>
                    <div style={{ display: 'flex', gap: '12px', fontSize: '10px', marginTop: '4px', fontWeight: 'bold' }}>
                      <span style={{ color: '#22c55e' }}>● YES: {yes.toFixed(1)}%</span>
                      <span style={{ color: '#ef4444' }}>● NO: {no.toFixed(1)}%</span>
                      {abstain > 0 && <span style={{ color: '#9ca3af' }}>● ABS: {abstain.toFixed(1)}%</span>}
                    </div>
                  </div>

                  <div style={{ fontSize: '10px', color: '#475569' }}>
                    <strong>Breakdown:</strong> {Object.entries(turnData.lastBillPartyVotes || {}).map(([pName, voteText]) => `${pName}: ${voteText}`).join(', ')}
                  </div>
                </div>
              </div>
            );
          })()}

          {/* Project Yields at Bottom */}
          <div style={{
            background: hasCompletedProject ? 'rgba(52, 211, 153, 0.05)' : 'rgba(101, 148, 177, 0.05)',
            border: hasCompletedProject ? '2px solid #34d399' : '1px solid rgba(101, 148, 177, 0.15)',
            borderRadius: '12px',
            padding: '12px'
          }}>
            <h4 style={{ margin: '0 0 8px 0', fontSize: '11px', textTransform: 'uppercase', letterSpacing: '0.05em', color: '#64748b', fontWeight: 'bold' }}>
              🏗️ Projects Completed Last Turn
            </h4>
            {completedProjectsLastTurn.length === 0 ? (
              <div style={{ fontSize: '11px', color: '#64748b', fontStyle: 'italic' }}>
                No projects completed last turn.
              </div>
            ) : (
              <div>
                <div style={{ display: 'flex', flexWrap: 'wrap', gap: '5px', marginBottom: '10px' }}>
                  {completedProjectsLastTurn.map(proj => {
                    const def = projectDefs[proj.projectKey];
                    const name = def ? def.name : proj.projectKey;
                    return (
                      <span key={proj.id} style={{
                        fontSize: '10px',
                        background: 'rgba(52, 211, 153, 0.15)',
                        color: '#047857',
                        padding: '2px 7px',
                        borderRadius: '4px',
                        fontWeight: 'bold',
                      }}>
                        {name}
                      </span>
                    );
                  })}
                </div>

                <div style={{
                   fontSize: '11px',
                   display: 'flex',
                   flexWrap: 'wrap',
                   gap: '8px',
                   color: '#15803d',
                   fontWeight: 'bold',
                   background: 'rgba(34, 197, 94, 0.05)',
                   padding: '7px 9px',
                   borderRadius: '6px'
                }}>
                  <span style={{ color: '#15803d' }}>Total Yield:</span>
                  {netCoins !== 0 && <span>💰 {netCoins > 0 ? '+' : ''}{netCoins}</span>}
                  {netMorale !== 0 && <span>✊ {netMorale > 0 ? '+' : ''}{netMorale}</span>}
                  {netSupport !== 0 && <span>📈 {netSupport > 0 ? '+' : ''}{netSupport}%</span>}
                  {netCorruption !== 0 && <span>⚖️ {netCorruption > 0 ? '+' : ''}{netCorruption}</span>}
                  {netMedia !== 0 && <span>📢 {netMedia > 0 ? '+' : ''}{netMedia}</span>}
                  {!hasYields && <span style={{ color: '#64748b' }}>No active yields</span>}
                </div>
              </div>
            )}
          </div>

        </div>

        {/* Sticky Footer */}
        <div className="modal-footer" style={{ padding: '12px 16px', borderTop: '1px solid #e2e8f0', background: '#fff' }}>
          <button
            onClick={onClose}
            style={{
              width: '100%',
              backgroundColor: headerColor,
              color: '#ffffff',
              border: 'none',
              padding: '12px',
              borderRadius: '10px',
              fontWeight: 'bold',
              fontSize: '14px',
              cursor: 'pointer',
              boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
              textAlign: 'center',
            }}
          >
            Review Board &amp; Plan Turn
          </button>
        </div>

      </div>
    </div>
  );
}
