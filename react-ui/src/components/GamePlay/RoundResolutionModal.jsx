import React from 'react';

export default function RoundResolutionModal({
  isOpen,
  onClose,
  turnData,
  activeParty,
  partyColor = '#6594b1',
  projectDefs = {}
}) {
  if (!isOpen || !turnData) return null;

  const lastTurnNum = turnData.turnNumber - 1;
  if (lastTurnNum <= 0) return null; // No previous turn on turn 1

  // Extract deltas for active human party
  const partyDeltas = turnData.lastMetricDeltas?.[activeParty.id] || {};
  
  // Format resource deltas
  const statsList = [
    { key: 'coins', label: 'Coins', icon: '💰', val: partyDeltas.coins || 0, suffix: '' },
    { key: 'partyMorale', label: 'Morale', icon: '✊', val: partyDeltas.partyMorale || 0, suffix: '' },
    { key: 'publicSupport', label: 'Support', icon: '📈', val: partyDeltas.publicSupport || 0, suffix: '%' },
    { key: 'corruptionScore', label: 'Corruption', icon: '⚖️', val: partyDeltas.corruptionScore || 0, suffix: '', invertColor: true },
    { key: 'mediaImage', label: 'Media', icon: '📢', val: partyDeltas.mediaImage || 0, suffix: '' }
  ];

  // Calculate completed projects & yields
  const completedProjectsLastTurn = (activeParty.projects || []).filter(p => p.progressPercent === 100 && p.completionTurn === lastTurnNum);
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

  return (
    <div style={{
      position: 'fixed',
      top: 0,
      left: 0,
      right: 0,
      bottom: 0,
      backgroundColor: 'rgba(9, 13, 22, 0.85)',
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      zIndex: 9999,
      padding: '15px',
      backdropFilter: 'blur(8px)',
      fontFamily: "'Inter', system-ui, sans-serif"
    }}>
      <div style={{
        backgroundColor: '#ffffff',
        width: '100%',
        maxWidth: '520px',
        borderRadius: '20px',
        overflow: 'hidden',
        boxShadow: '0 15px 40px rgba(0, 0, 0, 0.4)',
        border: `3px solid ${partyColor}`,
        animation: 'modalSlideIn 0.3s ease-out'
      }}>
        {/* Style block for animations */}
        <style dangerouslySetInnerHTML={{__html: `
          @keyframes modalSlideIn {
            from { transform: translateY(30px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
          }
        `}} />

        {/* Modal Header */}
        <div style={{
          backgroundColor: partyColor,
          padding: '20px',
          color: '#ffffff',
          textAlign: 'center',
          position: 'relative'
        }}>
          <h2 style={{ margin: 0, fontSize: '18px', fontWeight: '800', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
            Round Resolution Report
          </h2>
          <div style={{ fontSize: '14px', fontWeight: 'bold', marginTop: '4px', opacity: 0.9 }}>
            Turn {lastTurnNum}
          </div>
          <button 
            onClick={onClose}
            style={{
              position: 'absolute',
              top: '15px',
              right: '15px',
              background: 'rgba(255, 255, 255, 0.2)',
              border: 'none',
              color: '#ffffff',
              borderRadius: '50%',
              width: '28px',
              height: '28px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              cursor: 'pointer',
              fontWeight: 'bold',
              fontSize: '14px'
            }}
          >
            ✕
          </button>
        </div>

        {/* Modal Body */}
        <div style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '20px' }}>
          
          {/* Resource Changes Grid */}
          <div>
            <h4 style={{ margin: '0 0 12px 0', fontSize: '12px', textTransform: 'uppercase', letterSpacing: '0.05em', color: '#64748b', fontWeight: 'bold' }}>
              Resource Changes Last Turn
            </h4>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: '8px' }}>
              {statsList.map(stat => {
                const isPositive = stat.val > 0;
                const isZero = stat.val === 0;
                
                // Determine coloring based on invertColor flag (e.g. corruption increase is bad, decrease is good)
                let colorClass = '#64748b'; // default gray
                if (!isZero) {
                  if (stat.invertColor) {
                    colorClass = isPositive ? '#ef4444' : '#22c55e'; // positive corruption = red, negative = green
                  } else {
                    colorClass = isPositive ? '#22c55e' : '#ef4444'; // positive support/morale/coins = green, negative = red
                  }
                }

                const displayVal = isZero ? '0' : (isPositive ? `+${stat.val}` : `${stat.val}`);

                return (
                  <div key={stat.key} style={{
                    background: '#f8fafc',
                    border: '1px solid #e2e8f0',
                    borderRadius: '12px',
                    padding: '12px 4px',
                    textAlign: 'center',
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    gap: '4px'
                  }}>
                    <span style={{ fontSize: '20px' }}>{stat.icon}</span>
                    <span style={{ fontSize: '10px', color: '#64748b', fontWeight: '600', textTransform: 'uppercase' }}>
                      {stat.label}
                    </span>
                    <span style={{ 
                      fontSize: '13px', 
                      fontWeight: 'bold', 
                      color: colorClass 
                    }}>
                      {displayVal}{stat.suffix}
                    </span>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Last Turn Legislative Bill Vote Results */}
          {(() => {
            const lastResolvedBillKey = turnData.lastResolvedBillKey;
            const lastResolvedBill = turnData.bills?.find(b => b.billKey === lastResolvedBillKey);
            const voteHappenedLastRound = lastResolvedBill && lastResolvedBill.turnResolved === lastTurnNum;
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

            const total = yes + no + abstain;
            const yesPercent = total > 0 ? (yes / total) * 100 : 0;
            const noPercent = total > 0 ? (no / total) * 100 : 0;
            const abstainPercent = total > 0 ? (abstain / total) * 100 : 0;

            return (
              <div style={{
                background: '#f8fafc',
                border: '1px solid #e2e8f0',
                borderRadius: '12px',
                padding: '15px'
              }}>
                <h4 style={{ margin: '0 0 10px 0', fontSize: '12px', textTransform: 'uppercase', letterSpacing: '0.05em', color: '#64748b', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '6px' }}>
                  🗳️ Legislative Vote: {lastResolvedBillKey}
                </h4>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                  <div style={{
                    background: passed ? 'rgba(34, 197, 94, 0.08)' : 'rgba(239, 68, 68, 0.08)',
                    border: `1px solid ${passed ? '#22c55e' : '#ef4444'}`,
                    borderRadius: '8px',
                    padding: '8px 12px',
                    fontWeight: 'bold',
                    fontSize: '13px',
                    color: passed ? '#15803d' : '#b91c1c'
                  }}>
                    {passed ? '✅ PASSED' : '❌ DEFEATED'}
                    {!passed && (
                      <div style={{ fontSize: '11px', color: '#7f1d1d', fontWeight: 500, marginTop: '2px' }}>
                        Reason: {defeatReason}
                      </div>
                    )}
                  </div>

                  {/* Chart Bar */}
                  <div style={{ display: 'flex', height: '18px', borderRadius: '4px', overflow: 'hidden', background: '#f3f4f6', marginBottom: '4px', border: '1px solid #e5e7eb' }}>
                    {yes > 0 && (
                      <div style={{ width: `${yes}%`, background: '#22c55e', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontSize: '9px', fontWeight: 'bold' }}>
                        YES {yes.toFixed(1)}%
                      </div>
                    )}
                    {no > 0 && (
                      <div style={{ width: `${no}%`, background: '#ef4444', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontSize: '9px', fontWeight: 'bold' }}>
                        NO {no.toFixed(1)}%
                      </div>
                    )}
                    {abstain > 0 && (
                      <div style={{ width: `${abstain}%`, background: '#9ca3af', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontSize: '9px', fontWeight: 'bold' }}>
                        ABS {abstain.toFixed(1)}%
                      </div>
                    )}
                  </div>

                  <div style={{ fontSize: '11px', color: '#475569' }}>
                    <strong>Breakdown:</strong> {Object.entries(turnData.lastBillPartyVotes || {}).map(([partyName, voteText]) => `${partyName}: ${voteText}`).join(', ')}
                  </div>
                </div>
              </div>
            );
          })()}

          {/* Project Yields at Bottom */}
          <div style={{
            background: 'rgba(101, 148, 177, 0.05)',
            border: '1px solid rgba(101, 148, 177, 0.15)',
            borderRadius: '12px',
            padding: '15px'
          }}>
            <h4 style={{ margin: '0 0 10px 0', fontSize: '12px', textTransform: 'uppercase', letterSpacing: '0.05em', color: '#64748b', fontWeight: 'bold' }}>
              🏗️ Projects Completed Last Turn
            </h4>
            {completedProjectsLastTurn.length === 0 ? (
              <div style={{ fontSize: '12px', color: '#64748b', fontStyle: 'italic' }}>
                No projects completed last turn.
              </div>
            ) : (
              <div>
                <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px', marginBottom: '12px' }}>
                  {completedProjectsLastTurn.map(proj => {
                    const def = projectDefs[proj.projectKey];
                    const name = def ? def.name : proj.projectKey;
                    return (
                      <span key={proj.id} style={{
                        fontSize: '10px',
                        background: 'rgba(101, 148, 177, 0.15)',
                        color: 'var(--primary-dark)',
                        padding: '3px 8px',
                        borderRadius: '4px',
                        fontWeight: 'bold'
                      }}>
                        {name}
                      </span>
                    );
                  })}
                </div>

                <div style={{ 
                  fontSize: '12px', 
                  display: 'flex', 
                  flexWrap: 'wrap',
                  gap: '10px',
                  color: '#15803d',
                  fontWeight: 'bold',
                  background: 'rgba(34, 197, 94, 0.05)',
                  padding: '8px 10px',
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

          {/* Action Close Button */}
          <button 
            onClick={onClose}
            style={{
              backgroundColor: partyColor,
              color: '#ffffff',
              border: 'none',
              padding: '12px',
              borderRadius: '10px',
              fontWeight: 'bold',
              fontSize: '14px',
              cursor: 'pointer',
              boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
              textAlign: 'center'
            }}
          >
            Review Board &amp; Plan Turn
          </button>

        </div>
      </div>
    </div>
  );
}
