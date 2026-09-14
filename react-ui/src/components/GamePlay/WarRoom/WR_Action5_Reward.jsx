import React from 'react';

/**
 * WR_Action5_Reward — Play Rewards inventory
 * Props: { turnData, selectedRewardKey, setSelectedRewardKey,
 *           rewardTargetPartyId, setRewardTargetPartyId, rewardConfirmed, setRewardConfirmed }
 */
export default function WR_Action5_Reward({
  turnData,
  selectedRewardKey,
  setSelectedRewardKey,
  rewardTargetPartyId,
  setRewardTargetPartyId,
  rewardConfirmed,
  setRewardConfirmed,
}) {
  const hasRewards = turnData?.activePlayerHeldRewards?.length > 0;
  const selectedReward = hasRewards
    ? turnData.activePlayerHeldRewards.find(r => r.rewardKey === selectedRewardKey)
    : null;
  const requiresTarget = selectedReward?.requiresTarget;

  const opponents = (turnData?.parties || []).filter(p => p.id !== turnData?.activeHumanPartyId);

  if (!hasRewards) {
    return (
      <div style={{ padding: '14px 16px 0' }}>
        <div style={{ marginBottom: '14px' }}>
          <div style={{ fontSize: '15px', fontWeight: 900, letterSpacing: '0.05em', textTransform: 'uppercase', color: '#F59E0B' }}>
            🎁 Play Rewards
          </div>
        </div>
        <div style={{
          padding: '30px 20px', textAlign: 'center',
          background: 'rgba(255,255,255,0.03)',
          border: '1px dashed rgba(255,255,255,0.1)',
          borderRadius: '14px',
        }}>
          <div style={{ fontSize: '32px', marginBottom: '10px' }}>🎁</div>
          <div style={{ fontSize: '14px', color: '#7D8590', fontStyle: 'italic' }}>
            No rewards in inventory.
          </div>
          <div style={{ fontSize: '12px', color: '#4B5563', marginTop: '6px' }}>
            Win bidding rounds to earn special rewards!
          </div>
        </div>
      </div>
    );
  }

  return (
    <div style={{ padding: '14px 16px 0' }}>
      {/* Section header */}
      <div style={{ marginBottom: '14px' }}>
        <div style={{ fontSize: '15px', fontWeight: 900, letterSpacing: '0.05em', textTransform: 'uppercase', color: '#F59E0B' }}>
          🎁 Play Rewards
        </div>
        <div style={{ fontSize: '12px', color: '#7D8590', marginTop: '2px' }}>
          Choose a reward to activate this turn
        </div>
      </div>

      {/* Reward cards */}
      {turnData.activePlayerHeldRewards.map(r => {
        const isSelected = selectedRewardKey === r.rewardKey;
        const isSpecial = r.rewardKey?.startsWith('special_');

        return (
          <div
            key={r.rewardKey}
            onClick={() => {
              if (rewardConfirmed) return;
              setSelectedRewardKey(isSelected ? '' : r.rewardKey);
              setRewardTargetPartyId('');
              setRewardConfirmed(false);
            }}
            className={`wr-reward-card ${isSelected ? 'wr-reward-card-selected' : 'wr-reward-card-inactive'}`}
          >
            {/* Icon */}
            <div style={{
              width: '46px', height: '46px', borderRadius: '12px', flexShrink: 0,
              background: isSpecial
                ? 'linear-gradient(135deg,#F59E0B,#D97706)'
                : 'rgba(255,255,255,0.08)',
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              fontSize: '22px',
              border: isSpecial ? 'none' : '1px solid rgba(255,255,255,0.1)',
            }}>
              {isSpecial ? '⭐' : '🎁'}
            </div>

            {/* Info */}
            <div style={{ flex: 1, minWidth: 0 }}>
              <div style={{ fontSize: '14px', fontWeight: 800, color: '#E6EDF3', marginBottom: '3px' }}>
                {r.name}
                {isSpecial && (
                  <span className="wr-badge wr-badge-special" style={{ marginLeft: '6px', verticalAlign: 'middle' }}>SPECIAL</span>
                )}
              </div>
              {r.description && (
                <div style={{ fontSize: '12px', color: '#8B949E', lineHeight: 1.45 }}>{r.description}</div>
              )}
              <div style={{ fontSize: '11px', color: '#FCD34D', marginTop: '4px', fontWeight: 700 }}>
                ⏳ {r.turnsLeft} turn{r.turnsLeft !== 1 ? 's' : ''} remaining
              </div>
            </div>

            {/* Selected check */}
            {isSelected && (
              <span style={{ color: '#F59E0B', fontSize: '20px', fontWeight: 900, flexShrink: 0 }}>✓</span>
            )}
          </div>
        );
      })}

      {/* Target selector (if selected reward requires a target) */}
      {selectedRewardKey && requiresTarget && !rewardConfirmed && (
        <div style={{
          marginBottom: '14px', padding: '14px',
          background: 'rgba(255,255,255,0.03)',
          border: '1.5px solid rgba(255,255,255,0.1)',
          borderRadius: '14px',
        }}>
          <div style={{ fontSize: '12px', fontWeight: 800, letterSpacing: '0.06em', textTransform: 'uppercase', color: '#F59E0B', marginBottom: '10px' }}>
            🎯 Select Target
          </div>
          <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
            {(turnData?.parties || []).map(p => {
              if (selectedReward?.allowedTargets === 'opponent' && p.id === turnData?.activeHumanPartyId) return null;
              if (selectedReward?.allowedTargets === 'self'     && p.id !== turnData?.activeHumanPartyId) return null;
              const isTargeted = rewardTargetPartyId === p.id;
              const isSelf = p.id === turnData?.activeHumanPartyId;
              return (
                <button
                  key={p.id}
                  onClick={() => setRewardTargetPartyId(p.id)}
                  style={{
                    width: '76px', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '6px',
                    padding: '10px 6px',
                    background: isTargeted ? 'rgba(245,158,11,0.12)' : 'rgba(255,255,255,0.04)',
                    border: `2px solid ${isTargeted ? '#F59E0B' : 'rgba(255,255,255,0.1)'}`,
                    borderRadius: '12px',
                    boxShadow: isTargeted ? '0 0 12px rgba(245,158,11,0.4)' : 'none',
                    cursor: 'pointer', touchAction: 'manipulation', WebkitTapHighlightColor: 'transparent',
                    transition: 'all 0.15s ease', minHeight: 'unset',
                    fontFamily: 'Montserrat,system-ui,sans-serif',
                  }}
                >
                  <div style={{
                    width: '36px', height: '36px', borderRadius: '50%',
                    background: 'var(--party-primary-color,#6C3AB5)',
                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                    fontSize: '15px', fontWeight: 900, color: '#ffffff',
                    border: isTargeted ? '2px solid #F59E0B' : '2px solid rgba(255,255,255,0.15)',
                  }}>
                    {(p.name || '?')[0]?.toUpperCase()}
                  </div>
                  <span style={{ fontSize: '10px', fontWeight: 700, color: '#C9D1D9', textAlign: 'center', lineHeight: 1.2 }}>
                    {p.name?.split(' ')[0]}{isSelf ? ' (Self)' : ''}
                  </span>
                  {isTargeted && <span style={{ fontSize: '10px', color: '#F59E0B' }}>✓</span>}
                </button>
              );
            })}
          </div>
        </div>
      )}

      {/* Skip option */}
      <button
        onClick={() => { setSelectedRewardKey(''); setRewardConfirmed(false); }}
        disabled={rewardConfirmed}
        style={{
          width: '100%', padding: '12px', marginBottom: '12px',
          background: (!selectedRewardKey && !rewardConfirmed) ? 'rgba(255,255,255,0.06)' : 'transparent',
          border: '1px dashed rgba(255,255,255,0.18)',
          borderRadius: '10px', color: '#7D8590',
          fontSize: '13px', fontWeight: 700, cursor: 'pointer',
          touchAction: 'manipulation', WebkitTapHighlightColor: 'transparent',
          fontFamily: 'Montserrat,system-ui,sans-serif',
          transition: 'all 0.15s ease',
        }}
      >
        ◯ Skip — Don't use any reward this turn
      </button>

      {/* Confirm button */}
      <button
        onClick={() => setRewardConfirmed(!rewardConfirmed)}
        disabled={selectedRewardKey !== '' && requiresTarget && !rewardTargetPartyId}
        style={{
          width: '100%', minHeight: '52px', marginBottom: '4px',
          fontSize: '15px', fontWeight: 900, letterSpacing: '0.04em',
          background: rewardConfirmed
            ? 'linear-gradient(135deg,#16A34A,#15803d)'
            : 'linear-gradient(135deg,#D97706,#F59E0B)',
          color: '#ffffff', border: 'none', borderRadius: '14px',
          boxShadow: rewardConfirmed ? '0 0 16px rgba(22,163,74,0.45)' : '0 0 14px rgba(245,158,11,0.35)',
          cursor: 'pointer', touchAction: 'manipulation', WebkitTapHighlightColor: 'transparent',
          transition: 'all 0.2s ease', fontFamily: 'Montserrat,system-ui,sans-serif',
        }}
      >
        {rewardConfirmed ? '✅ REWARD LOCKED' : '🔒 CONFIRM REWARD'}
      </button>
    </div>
  );
}
