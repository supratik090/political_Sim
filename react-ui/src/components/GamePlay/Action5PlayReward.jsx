import React from 'react';

export default function Action5PlayReward({
  turnData,
  selectedRewardKey,
  setSelectedRewardKey,
  rewardTargetPartyId,
  setRewardTargetPartyId,
  rewardConfirmed,
  setRewardConfirmed
}) {
  const hasRewards = turnData.activePlayerHeldRewards && turnData.activePlayerHeldRewards.length > 0;
  const selectedReward = hasRewards ? turnData.activePlayerHeldRewards.find(r => r.rewardKey === selectedRewardKey) : null;
  const rewardRequiresTarget = selectedReward?.requiresTarget;

  return (
    <div>
      {!hasRewards ? (
        <p style={{ margin: 0, fontSize: '13px', opacity: 0.8, color: 'gray', fontStyle: 'italic' }}>
          No inventory rewards held. Win bidding rounds to earn rewards!
        </p>
      ) : (
        <div>
          <label style={{ fontSize: '12px', fontWeight: 'bold', display: 'block', marginBottom: '8px', color: 'var(--primary-dark)' }}>
            🎁 Select a Reward to Play:
          </label>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', marginBottom: '15px' }}>
            <div
              onClick={() => {
                if (rewardConfirmed) return;
                setSelectedRewardKey('');
                setRewardTargetPartyId('');
                setRewardConfirmed(false);
              }}
              style={{
                padding: '10px 12px',
                borderRadius: '8px',
                border: !selectedRewardKey ? '2px solid var(--primary-dark)' : '1px solid var(--primary-border)',
                background: !selectedRewardKey ? 'rgba(101, 148, 177, 0.08)' : '#ffffff',
                cursor: rewardConfirmed ? 'not-allowed' : 'pointer',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                fontSize: '13px',
                fontWeight: 'bold',
                color: '#475569',
                opacity: rewardConfirmed ? 0.6 : 1
              }}
            >
              <span>🚫 Do Not Play Any Reward</span>
              {!selectedRewardKey && <span style={{ color: 'var(--primary-dark)' }}>✓</span>}
            </div>

            {turnData.activePlayerHeldRewards.map(r => {
              const isSelected = selectedRewardKey === r.rewardKey;
              return (
                <div
                  key={r.rewardKey}
                  onClick={() => {
                    if (rewardConfirmed) return;
                    setSelectedRewardKey(r.rewardKey);
                    setRewardTargetPartyId('');
                    setRewardConfirmed(false);
                  }}
                  style={{
                    padding: '10px 12px',
                    borderRadius: '8px',
                    border: isSelected ? '2px solid #1d4ed8' : '1px solid var(--primary-border)',
                    background: isSelected ? '#eff6ff' : '#ffffff',
                    cursor: rewardConfirmed ? 'not-allowed' : 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    transition: 'all 0.15s ease',
                    opacity: rewardConfirmed ? 0.6 : 1
                  }}
                >
                  <div>
                    <strong style={{ display: 'block', fontSize: '13px', color: '#0f172a' }}>🎁 {r.name}</strong>
                    <span style={{ fontSize: '11px', color: '#64748b' }}>Turns left: {r.turnsLeft}</span>
                  </div>
                  {isSelected && <span style={{ color: '#1d4ed8', fontWeight: 'bold', fontSize: '14px' }}>✓</span>}
                </div>
              );
            })}
          </div>

          {selectedRewardKey && selectedReward && (
            <div style={{ padding: '12px', background: 'rgba(0,0,0,0.02)', borderRadius: '8px', marginBottom: '15px' }}>
              <div style={{ fontSize: '12px', color: 'var(--primary-dark)' }}><b>Effect:</b> {selectedReward.description}</div>
              {selectedReward.requiresTarget && (
                <div style={{ marginTop: '12px' }}>
                  <label style={{ fontSize: '12px', fontWeight: 'bold', display: 'block', marginBottom: '8px', color: 'var(--primary-dark)' }}>
                    🎯 Select Target Party:
                  </label>
                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(130px, 1fr))', gap: '8px' }}>
                    {turnData.parties.map(p => {
                      if (selectedReward.allowedTargets === 'opponent' && p.id === turnData.activeHumanPartyId) return null;
                      if (selectedReward.allowedTargets === 'self' && p.id !== turnData.activeHumanPartyId) return null;
                      const isSelected = rewardTargetPartyId === p.id;
                      return (
                        <div
                          key={p.id}
                          onClick={() => {
                            if (rewardConfirmed) return;
                            setRewardTargetPartyId(p.id);
                            setRewardConfirmed(false);
                          }}
                          style={{
                            padding: '10px 12px',
                            borderRadius: '8px',
                            border: isSelected ? `2px solid ${p.color || '#1d4ed8'}` : '1.5px solid var(--primary-border)',
                            background: isSelected ? `${p.color || '#1d4ed8'}14` : '#ffffff',
                            cursor: rewardConfirmed ? 'not-allowed' : 'pointer',
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'space-between',
                            opacity: rewardConfirmed ? 0.6 : 1
                          }}
                        >
                          <div>
                            <strong style={{ display: 'block', fontSize: '13px', color: '#0f172a' }}>{p.symbol || '🏛️'} {p.name}</strong>
                            <span style={{ fontSize: '11px', color: '#64748b' }}>{p.id === turnData.activeHumanPartyId ? '(Self)' : p.role}</span>
                          </div>
                          {isSelected && <span style={{ color: p.color || '#1d4ed8', fontWeight: 'bold', fontSize: '14px' }}>✓</span>}
                        </div>
                      );
                    })}
                  </div>
                </div>
              )}
            </div>
          )}

          <div style={{ marginTop: '15px', textAlign: 'center' }}>
            <button
              onClick={() => setRewardConfirmed(!rewardConfirmed)}
              disabled={selectedRewardKey !== '' && rewardRequiresTarget && !rewardTargetPartyId}
              style={{
                background: rewardConfirmed ? 'var(--selected-highlight)' : 'var(--party-primary-color, var(--primary-dark))',
                borderColor: rewardConfirmed ? 'var(--selected-highlight)' : 'var(--party-primary-color, var(--primary-dark))',
                color: rewardConfirmed ? 'var(--primary-dark)' : '#ffffff',
                fontWeight: 'bold',
                padding: '8px 25px'
              }}
            >
              {rewardConfirmed ? '✅ Reward Locked' : '🔒 Confirm Reward Selection'}
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
