import React from 'react';

function deterministicShuffle(array, seedString) {
  if (!array || array.length === 0) return [];
  let hash = 0;
  for (let i = 0; i < seedString.length; i++) {
    hash = seedString.charCodeAt(i) + ((hash << 5) - hash);
  }
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const val = Math.abs(Math.sin(hash + i) * 10000);
    const j = Math.floor((val - Math.floor(val)) * (i + 1));
    const temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }
  return arr;
}

export default function Action3PartyDecision({
  turnData,
  selectedIssueOptionKey,
  setSelectedIssueOptionKey,
  activeParty,
  selectedEventOptionKey,
  setSelectedEventOptionKey,
  scenarioEvents = []
}) {
  const activeEventKey = turnData.activeEventKey;
  const activeEvent = scenarioEvents.find(e => e.eventKey === activeEventKey);

  const rawOptions = turnData.currentIssue?.options || [];
  const issueKey = turnData.currentIssue?.issueKey || '';
  const options = React.useMemo(() => {
    return deterministicShuffle(rawOptions, `${turnData.id || ''}-${turnData.turnNumber}-${issueKey}`);
  }, [rawOptions, turnData.id, turnData.turnNumber, issueKey]);

  const formatEffects = (effects) => {
    if (!effects || Object.keys(effects).length === 0) return 'None';
    const parts = [];
    if (effects.coins) parts.push(`💰 ${effects.coins > 0 ? '+' : ''}${effects.coins} Coins`);
    if (effects.partyMorale) parts.push(`✊ ${effects.partyMorale > 0 ? '+' : ''}${effects.partyMorale} Morale`);
    if (effects.corruptionScore) parts.push(`⚖️ ${effects.corruptionScore > 0 ? '+' : ''}${effects.corruptionScore} Corruption`);
    if (effects.mediaImage) parts.push(`📢 ${effects.mediaImage > 0 ? '+' : ''}${effects.mediaImage} Media`);
    if (effects.publicSupport) parts.push(`📈 ${effects.publicSupport > 0 ? '+' : ''}${effects.publicSupport}% Support`);
    return parts.join(', ');
  };

  return (
    <div style={{ fontFamily: "system-ui, -apple-system, sans-serif" }}>
      <style>{`
        @keyframes pulse-live-dot {
          0% { opacity: 0.3; transform: scale(0.9); }
          50% { opacity: 1; transform: scale(1.1); }
          100% { opacity: 0.3; transform: scale(0.9); }
        }
        @keyframes scanline-flicker {
          0% { opacity: 0.98; }
          50% { opacity: 1; }
          100% { opacity: 0.98; }
        }
      `}</style>

      {/* CASE A: Active Event Card Decision */}
      {activeEventKey ? (
        <div style={{
          border: '2px solid #3b82f6',
          borderRadius: '12px',
          padding: '20px',
          background: 'rgba(59, 130, 246, 0.03)',
          boxShadow: '0 4px 15px rgba(0,0,0,0.02)'
        }}>
          <div style={{
            background: '#3b82f6',
            color: '#ffffff',
            padding: '6px 14px',
            borderRadius: '6px',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            marginBottom: '15px',
            fontSize: '11px',
            fontWeight: '900',
            letterSpacing: '0.08em',
            textTransform: 'uppercase'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <span style={{ 
                width: '8px', 
                height: '8px', 
                borderRadius: '50%', 
                backgroundColor: '#ffffff', 
                display: 'inline-block',
                animation: 'pulse-live-dot 1.2s infinite'
              }} />
              <span>📢 STATE AFFAIRS EVENT</span>
            </div>
            <span style={{ 
              background: '#ffffff', 
              color: '#3b82f6', 
              fontSize: '9px', 
              padding: '1px 6px', 
              borderRadius: '3px',
              fontWeight: '900'
            }}>
              IMMEDIATE
            </span>
          </div>

          <h3 style={{
            margin: '0 0 12px 0',
            fontSize: '18px',
            fontWeight: '800',
            lineHeight: 1.4,
            color: '#1d4ed8',
            fontFamily: "Impact, system-ui, sans-serif"
          }}>
            {activeEvent ? activeEvent.name.toUpperCase() : activeEventKey.toUpperCase()}
          </h3>

          <div style={{
            background: 'rgba(59, 130, 246, 0.05)',
            borderLeft: '4px solid #3b82f6',
            padding: '12px 16px',
            borderRadius: '0 6px 6px 0',
            fontSize: '13px',
            lineHeight: 1.6,
            color: '#374151',
            marginBottom: '20px'
          }}>
            {activeEvent ? activeEvent.description : 'A special event requires your intervention.'}
          </div>

          <label style={{ fontSize: '11px', fontWeight: 'bold', display: 'block', marginBottom: '8px', color: '#4b5563', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
            Select Your Party's Response: <span style={{ color: '#ef4444' }}>*</span>
          </label>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            {activeEvent?.options?.map(opt => {
              const hasCoinsCost = opt.cost?.coins > 0;
              const hasMoraleCost = opt.cost?.partyMorale > 0;
              const canAffordCoins = !hasCoinsCost || (activeParty?.stats?.coins || 0) >= opt.cost.coins;
              const canAffordMorale = !hasMoraleCost || (activeParty?.stats?.partyMorale || 0) >= opt.cost.partyMorale;
              const isAffordable = canAffordCoins && canAffordMorale;
              const isSelected = selectedEventOptionKey === opt.optionKey;

              const costLabels = [];
              if (hasCoinsCost) costLabels.push(`${opt.cost.coins} Coins`);
              if (hasMoraleCost) costLabels.push(`${opt.cost.partyMorale} Morale`);
              const costText = costLabels.length > 0 ? `Cost: ${costLabels.join(', ')}` : 'Cost: None';

              return (
                <div
                  key={opt.optionKey}
                  onClick={() => {
                    setSelectedEventOptionKey(opt.optionKey);
                  }}
                  style={{
                    border: `2px solid ${isSelected ? '#3b82f6' : '#e5e7eb'}`,
                    background: isSelected ? '#eff6ff' : '#fff',
                    borderRadius: '8px',
                    padding: '12px 15px',
                    cursor: 'pointer',
                    transition: 'all 0.15s ease',
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '6px'
                  }}
                >
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <span style={{ fontSize: '13px', fontWeight: 'bold', color: isSelected ? '#1e40af' : '#374151' }}>
                      {opt.text}
                    </span>
                    <span style={{
                      fontSize: '11px',
                      fontWeight: 'bold',
                      color: isAffordable ? '#6b7280' : '#ef4444',
                      background: isAffordable ? 'rgba(0,0,0,0.04)' : 'rgba(239, 68, 68, 0.08)',
                      padding: '2px 6px',
                      borderRadius: '4px'
                    }}>
                      {costText}
                    </span>
                  </div>
                  <div style={{ fontSize: '11px', color: '#166534', fontWeight: 'bold' }}>
                    ⚡ Effects: {formatEffects(opt.effects)}
                  </div>
                  {!isAffordable && (
                    <div style={{ fontSize: '10px', color: '#ef4444', fontWeight: 'bold', marginTop: '2px' }}>
                      ⚠️ Note: This option exceeds your current resources and may floor your stats at 0.
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>
      ) : turnData.currentIssue ? (
        /* CASE B: High-tech TV Breaking News style container for Party Decision */
        <div style={{
          background: 'radial-gradient(circle at center, #1e1b4b 0%, #09090b 100%)',
          border: '3px solid var(--party-primary-color)',
          borderRadius: '12px',
          padding: '20px',
          color: '#f4f4f5',
          boxShadow: '0 10px 30px rgba(var(--party-primary-color-rgb), 0.15)',
          position: 'relative',
          overflow: 'hidden',
          animation: 'scanline-flicker 0.15s infinite'
        }}>
          {/* Subtle Scanline Overlay */}
          <div style={{
            position: 'absolute',
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            backgroundImage: 'linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.15) 50%)',
            backgroundSize: '100% 4px',
            pointerEvents: 'none',
            zIndex: 1
          }} />

          {/* TV Header Bar */}
          <div style={{
            background: 'var(--party-primary-color)',
            color: '#ffffff',
            padding: '6px 14px',
            borderRadius: '6px',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            marginBottom: '15px',
            fontSize: '11px',
            fontWeight: '900',
            letterSpacing: '0.08em',
            textTransform: 'uppercase',
            position: 'relative',
            zIndex: 2
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <span style={{ 
                width: '8px', 
                height: '8px', 
                borderRadius: '50%', 
                backgroundColor: '#ffffff', 
                display: 'inline-block',
                animation: 'pulse-live-dot 1.2s infinite'
              }} />
              <span>📺 INTERNAL REPORT</span>
            </div>
            <span style={{ 
              background: '#ffffff', 
              color: 'var(--party-primary-color)', 
              fontSize: '9px', 
              padding: '1px 6px', 
              borderRadius: '3px',
              fontWeight: '900'
            }}>
              LIVE FEED
            </span>
          </div>

          {/* Headline Display */}
          <div style={{ position: 'relative', zIndex: 2 }}>
            <h3 style={{
              margin: '0 0 12px 0',
              fontSize: '18px',
              fontWeight: '800',
              lineHeight: 1.4,
              color: '#fef08a', // bright yellow
              textShadow: '0 2px 4px rgba(0,0,0,0.5)',
              fontFamily: "Impact, system-ui, sans-serif"
            }}>
              🚨 URGENT: {turnData.currentIssue.title.toUpperCase()}
            </h3>

            {/* Anchored Transcript Box */}
            <div style={{
              background: 'rgba(9, 9, 11, 0.6)',
              borderLeft: '4px solid #3b82f6',
              padding: '12px 16px',
              borderRadius: '0 6px 6px 0',
              fontSize: '13px',
              lineHeight: 1.6,
              color: '#e4e4e7',
              marginBottom: '20px',
              boxShadow: 'inset 0 2px 4px rgba(0,0,0,0.5)'
            }}>
              <strong style={{ color: '#60a5fa', textTransform: 'uppercase', fontSize: '11px', display: 'block', marginBottom: '4px' }}>
                🎙️ BRIEFING DESK:
              </strong>
              {turnData.currentIssue.description}
            </div>

            {/* Resolution Selector Title */}
            <h4 style={{
              margin: '0 0 8px 0',
              fontSize: '10px',
              textTransform: 'uppercase',
              letterSpacing: '0.06em',
              color: '#a1a1aa',
              fontWeight: 800
            }}>
              📡 SELECT EXECUTIVE ACTION:
            </h4>

            {/* Options list */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              {options.map((opt, i) => {
                const isSelected = selectedIssueOptionKey === opt.optionKey;
                return (
                  <button
                    key={opt.optionKey}
                    onClick={() => setSelectedIssueOptionKey(opt.optionKey)}
                    style={{
                      textAlign: 'left',
                      padding: '12px 16px',
                      borderRadius: '8px',
                      fontSize: '12.5px',
                      lineHeight: '1.4',
                      background: isSelected 
                        ? 'var(--party-primary-color)' 
                        : 'linear-gradient(180deg, #1f2937 0%, #111827 100%)',
                      color: '#ffffff',
                      borderWidth: '1px',
                      borderStyle: 'solid',
                      borderColor: isSelected ? 'var(--party-primary-color)' : 'rgba(255, 255, 255, 0.12)',
                      boxShadow: isSelected ? '0 4px 15px rgba(var(--party-primary-color-rgb), 0.3)' : 'none',
                      fontWeight: isSelected ? '700' : 'normal',
                      transition: 'all 0.15s ease',
                      cursor: 'pointer',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '10px'
                    }}
                    onMouseEnter={(e) => {
                      if (!isSelected) {
                        e.currentTarget.style.background = 'linear-gradient(180deg, #374151 0%, #1f2937 100%)';
                        e.currentTarget.style.borderColor = 'rgba(255, 255, 255, 0.3)';
                      }
                    }}
                    onMouseLeave={(e) => {
                      if (!isSelected) {
                        e.currentTarget.style.background = 'linear-gradient(180deg, #1f2937 0%, #111827 100%)';
                        e.currentTarget.style.borderColor = 'rgba(255, 255, 255, 0.12)';
                      }
                    }}
                  >
                    <span style={{ 
                      display: 'inline-flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      width: '20px',
                      height: '20px',
                      borderRadius: '50%',
                      background: isSelected ? '#ffffff' : 'rgba(255,255,255,0.1)',
                      color: isSelected ? 'var(--party-primary-color)' : '#ffffff',
                      fontSize: '10px',
                      fontWeight: '900'
                    }}>
                      {isSelected ? '✓' : i + 1}
                    </span>
                    <span style={{ flex: 1 }}>{opt.text}</span>
                  </button>
                );
              })}
            </div>
          </div>
        </div>
      ) : (
        /* CASE C: Retro TV Standby screen for no active events or issues */
        <div style={{
          position: 'relative',
          borderRadius: '12px',
          overflow: 'hidden',
          border: '3px solid #475569',
          boxShadow: '0 4px 20px rgba(0, 0, 0, 0.15)',
          background: '#0f172a'
        }}>
          {/* Color Bars Container */}
          <div style={{ display: 'flex', width: '100%', height: '120px' }}>
            <div style={{ flex: 1, backgroundColor: '#e2e8f0' }} />
            <div style={{ flex: 1, backgroundColor: '#eab308' }} />
            <div style={{ flex: 1, backgroundColor: '#06b6d4' }} />
            <div style={{ flex: 1, backgroundColor: '#10b981' }} />
            <div style={{ flex: 1, backgroundColor: '#ec4899' }} />
            <div style={{ flex: 1, backgroundColor: '#ef4444' }} />
            <div style={{ flex: 1, backgroundColor: '#3b82f6' }} />
          </div>
          {/* Glassmorphic Overlay */}
          <div style={{
            position: 'absolute',
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            background: 'rgba(15, 23, 42, 0.85)',
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',
            alignItems: 'center',
            padding: '20px',
            textAlign: 'center'
          }}>
            <div style={{
              background: '#1e293b',
              border: '1px solid rgba(255, 255, 255, 0.15)',
              borderRadius: '6px',
              padding: '6px 14px',
              fontSize: '11px',
              fontWeight: '900',
              color: '#94a3b8',
              letterSpacing: '0.15em',
              textTransform: 'uppercase',
              marginBottom: '6px',
              boxShadow: '0 2px 8px rgba(0,0,0,0.3)'
            }}>
              📡 STANDBY
            </div>
            <div style={{ fontSize: '13px', fontWeight: 'bold', color: '#f1f5f9' }}>
              No Active Event or Decision
            </div>
            <div style={{ fontSize: '11px', color: '#94a3b8', marginTop: '2px' }}>
              Nominal status. Enjoy this turn of stable state affairs!
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
