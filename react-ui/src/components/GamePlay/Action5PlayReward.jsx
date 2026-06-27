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
          <label htmlFor="reward-select" style={{ fontSize: '12px', fontWeight: 'bold', display: 'block', marginBottom: '6px', color: 'var(--primary-dark)' }}>
            🎁 Select a Reward to Play:
          </label>
          <select
            id="reward-select"
            value={selectedRewardKey}
            disabled={rewardConfirmed}
            onChange={(e) => {
              setSelectedRewardKey(e.target.value);
              setRewardTargetPartyId('');
              setRewardConfirmed(false);
            }}
            style={{
              width: '100%',
              padding: '8px',
              borderRadius: '6px',
              border: '1px solid var(--primary-border)',
              background: '#ffffff',
              color: 'var(--primary-dark)',
              fontSize: '13px',
              marginBottom: '15px'
            }}
          >
            <option value="">-- Do Not Play Any Reward --</option>
            {turnData.activePlayerHeldRewards.map(r => (
              <option key={r.rewardKey} value={r.rewardKey}>🎁 {r.name} (Turns left: {r.turnsLeft})</option>
            ))}
          </select>

          {selectedRewardKey && selectedReward && (
            <div style={{ padding: '12px', background: 'rgba(0,0,0,0.02)', borderRadius: '8px', marginBottom: '15px' }}>
              <div style={{ fontSize: '12px', color: 'var(--primary-dark)' }}><b>Effect:</b> {selectedReward.description}</div>
              {selectedReward.requiresTarget && (
                <div style={{ marginTop: '12px' }}>
                  <label htmlFor="reward-target-select" style={{ fontSize: '12px', fontWeight: 'bold', display: 'block', marginBottom: '6px', color: 'var(--primary-dark)' }}>
                    🎯 Select Target Party:
                  </label>
                  <select
                    id="reward-target-select"
                    value={rewardTargetPartyId}
                    disabled={rewardConfirmed}
                    onChange={(e) => {
                      setRewardTargetPartyId(e.target.value);
                      setRewardConfirmed(false);
                    }}
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
                    <option value="">-- Choose Target Party --</option>
                    {turnData.parties.map(p => {
                      if (selectedReward.allowedTargets === 'opponent' && p.id === turnData.activeHumanPartyId) return null;
                      if (selectedReward.allowedTargets === 'self' && p.id !== turnData.activeHumanPartyId) return null;
                      return (
                        <option key={p.id} value={p.id}>{p.name} {p.id === turnData.activeHumanPartyId ? '(Self)' : `(${p.role})`}</option>
                      );
                    })}
                  </select>
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
