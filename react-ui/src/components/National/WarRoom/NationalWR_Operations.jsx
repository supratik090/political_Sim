import React, { useState, useEffect, useMemo, useCallback } from 'react';
import NationalWR_Coalition from './NationalWR_Coalition';
import NationalWR_Finance from './NationalWR_Finance';
import NationalWR_Events from './NationalWR_Events';
import NationalWR_States from './NationalWR_States';
import { generateStrategicHints } from './hintEngine';

// Hexagonal Actions configuration - Coalition, Finance, Events, and States
const HEX_ACTIONS = [
  { key: 'coalition_hub', icon: '🤝', label: 'Coalition', tab: 'coalition', title: 'Coalition & Front Politics' },
  { key: 'finance_ops', icon: '💰', label: 'Finance', tab: 'finance', title: 'Party Treasury & Strategy Cards' },
  { key: 'events_ops', icon: '📰', label: 'Events & Issues', tab: 'events', title: 'National Crises & Campaign Themes' },
  { key: 'states_ops', icon: '🗺️', label: 'States', tab: 'states', title: 'Regional Operations & Assembly Elections' }
];

export default function NationalWR_Operations({
  activeGame,
  configData,
  onGameUpdate,
  onAdvanceSeason,
  isAdvancingSeason = false,
  completedActions: parentCompletedActions,
  markStepComplete: parentMarkStepComplete,
  isCoalitionDone: parentIsCoalitionDone,
  isFinanceDone: parentIsFinanceDone,
  isEventsDone: parentIsEventsDone,
  isStatesDone: parentIsStatesDone,
  isAllFourDone: parentIsAllFourDone,
  doneCount: parentDoneCount,
  initialSubTab = 'coalition',
  onSubTabChange
}) {
  // Current active sub-tab: 'coalition' | 'finance' | 'events' | 'states'
  const [activeSubTab, setActiveSubTab] = useState(initialSubTab || 'coalition');
  const [activeHexKey, setActiveHexKey] = useState(
    HEX_ACTIONS.find(h => h.tab === (initialSubTab || 'coalition'))?.key || 'coalition_hub'
  );

  // Sync when initialSubTab changes from parent
  useEffect(() => {
    if (initialSubTab) {
      setActiveSubTab(initialSubTab);
      const found = HEX_ACTIONS.find(h => h.tab === initialSubTab);
      if (found) setActiveHexKey(found.key);
    }
  }, [initialSubTab]);

  // Compute live strategic hints
  const hintData = useMemo(() => generateStrategicHints(activeGame, configData), [activeGame, configData]);

  // Track completed actions for hex tracker completion state (fallback)
  const [localCompletedActions, setLocalCompletedActions] = useState({});
  const [lastSeason, setLastSeason] = useState(activeGame?.currentSeason);
  const [showStrategicAdvice, setShowStrategicAdvice] = useState(false);

  // Reset manual completion overrides when season advances
  useEffect(() => {
    if (activeGame?.currentSeason !== undefined && activeGame.currentSeason !== lastSeason) {
      setLastSeason(activeGame.currentSeason);
      setLocalCompletedActions({});
    }
  }, [activeGame?.currentSeason, lastSeason]);

  const markStepComplete = useCallback((key, status = true) => {
    if (parentMarkStepComplete) {
      parentMarkStepComplete(key, status);
    }
    setLocalCompletedActions(prev => {
      if (prev[key] === status) return prev;
      return {
        ...prev,
        [key]: status
      };
    });
  }, [parentMarkStepComplete]);

  const handleMarkCoalitionCompleted = useCallback((status = true) => markStepComplete('coalition_hub', status), [markStepComplete]);
  const handleMarkFinanceCompleted = useCallback((status = true) => markStepComplete('finance_ops', status), [markStepComplete]);
  const handleMarkEventsCompleted = useCallback((status = true) => markStepComplete('events_ops', status), [markStepComplete]);
  const handleMarkStatesCompleted = useCallback((status = true) => markStepComplete('states_ops', status), [markStepComplete]);

  const effectiveCompletedActions = parentCompletedActions || localCompletedActions;

  // Derive completion states for each action hex
  const isFinanceDone = parentIsFinanceDone !== undefined ? parentIsFinanceDone : Boolean(
    activeGame?.committedFinanceCard || effectiveCompletedActions['finance_ops']
  );
  const isEventsDone = parentIsEventsDone !== undefined ? parentIsEventsDone : Boolean(
    (activeGame?.resolvedEventReactions && Object.keys(activeGame.resolvedEventReactions).length > 0) ||
    activeGame?.activeThemeAction ||
    effectiveCompletedActions['events_ops']
  );
  const isCoalitionDone = parentIsCoalitionDone !== undefined ? parentIsCoalitionDone : Boolean(
    effectiveCompletedActions['coalition_hub'] ||
    (activeGame?.pendingRequests && activeGame.pendingRequests.some(r => r.turn === activeGame?.currentSeason || r.status === 'ACCEPTED' || r.status === 'REJECTED'))
  );
  const allStatesCompleted = React.useMemo(() => {
    if (activeGame?.stateOperations && Object.keys(activeGame.stateOperations).length > 0) {
      const eligible = Object.values(activeGame.stateOperations).filter(s => s.isEligible !== false && s.isActive !== false);
      return eligible.length === 0 || eligible.every(s => s.doneThisTurn || s.skippedThisTurn);
    }
    return false;
  }, [activeGame?.stateOperations]);

  const isStatesDone = parentIsStatesDone !== undefined ? parentIsStatesDone : Boolean(
    allStatesCompleted || effectiveCompletedActions['states_ops']
  );

  const doneCount = parentDoneCount !== undefined ? parentDoneCount : [isCoalitionDone, isFinanceDone, isEventsDone, isStatesDone].filter(Boolean).length;
  const isAllFourDone = parentIsAllFourDone !== undefined ? parentIsAllFourDone : (doneCount === 4);

  const getIsHexDone = (hexKey) => {
    if (hexKey === 'coalition_hub') return isCoalitionDone;
    if (hexKey === 'finance_ops') return isFinanceDone;
    if (hexKey === 'events_ops') return isEventsDone;
    if (hexKey === 'states_ops') return isStatesDone;
    return !!effectiveCompletedActions[hexKey];
  };

  // Handle Hex Click: switch to that hex's tab and set active hex
  const handleHexClick = (hex) => {
    setActiveHexKey(hex.key);
    setActiveSubTab(hex.tab);
    if (onSubTabChange) onSubTabChange(hex.tab);
  };

  // Handle Sub-Tab Click: set tab and default hex for that tab
  const handleTabClick = (tabKey) => {
    setActiveSubTab(tabKey);
    const firstHexOfTab = HEX_ACTIONS.find(h => h.tab === tabKey);
    if (firstHexOfTab) {
      setActiveHexKey(firstHexOfTab.key);
    }
    if (onSubTabChange) onSubTabChange(tabKey);
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>

      {/* ------------------------------------------------------------------ */}
      {/* HEXAGONAL PROGRESS TRACKER                                         */}
      {/* ------------------------------------------------------------------ */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '10px 8px',
        background: 'linear-gradient(180deg, #1E293B 0%, #151D2A 100%)',
        borderRadius: '12px',
        border: '1px solid rgba(56, 189, 248, 0.3)',
        boxShadow: '0 8px 24px rgba(0,0,0,0.4)',
        gap: '8px',
        flexWrap: 'wrap'
      }}>
        {HEX_ACTIONS.map((hex) => {
          const isDone = getIsHexDone(hex.key);
          const isActive = activeHexKey === hex.key;

          let hexBg = 'linear-gradient(145deg, #334155, #1E293B)';
          let hexFilter = 'none';
          let hexOpacity = 0.55;

          if (isDone) {
            hexBg = isActive
              ? 'linear-gradient(145deg, #34D399, #059669)'
              : 'linear-gradient(145deg, #10B981, #059669)';
            hexFilter = isActive
              ? 'drop-shadow(0 0 12px rgba(52, 211, 153, 0.95))'
              : 'drop-shadow(0 0 8px rgba(16, 185, 129, 0.75))';
            hexOpacity = 1;
          } else if (isActive) {
            hexBg = 'linear-gradient(145deg, #0284C7, #38BDF8)';
            hexFilter = 'drop-shadow(0 0 10px rgba(56, 189, 248, 0.8))';
            hexOpacity = 1;
          }

          const labelColor = isDone
            ? (isActive ? '#6EE7B7' : '#34D399')
            : (isActive ? '#38BDF8' : '#64748B');

          return (
            <div
              key={hex.key}
              onClick={() => handleHexClick(hex)}
              style={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                gap: '3px',
                cursor: 'pointer',
                padding: '2px 8px'
              }}
              title={`${hex.title} (${hex.tab.toUpperCase()})${isDone ? ' - Completed ✓' : ''}`}
            >
              {/* Clip-Path Hexagon Button */}
              <div style={{
                width: '38px',
                height: '42px',
                clipPath: 'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                background: hexBg,
                filter: hexFilter,
                opacity: hexOpacity,
                transition: 'all 0.3s ease',
                position: 'relative'
              }}>
                <span style={{ fontSize: '14px', userSelect: 'none' }}>{hex.icon}</span>

                {/* Done badge indicator */}
                {isDone && (
                  <span style={{
                    position: 'absolute',
                    top: '2px',
                    right: '3px',
                    fontSize: '9px',
                    color: '#ffffff',
                    fontWeight: 900,
                    textShadow: '0 0 4px rgba(0,0,0,0.8)'
                  }}>✓</span>
                )}
              </div>

              {/* Hex Label & Tab Category */}
              <div style={{ textAlign: 'center' }}>
                <div style={{
                  fontSize: '8px',
                  fontWeight: (isActive || isDone) ? '900' : '700',
                  color: labelColor,
                  lineHeight: 1.1,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  gap: '2px'
                }}>
                  {hex.label}
                  {isDone && <span style={{ color: '#10B981', fontSize: '7.5px' }}>✓</span>}
                </div>
                <div style={{
                  fontSize: '6.5px',
                  color: isDone ? '#34D399' : '#94a3b8',
                  textTransform: 'uppercase',
                  letterSpacing: '0.04em',
                  marginTop: '1px',
                  fontWeight: isDone ? '800' : 'normal'
                }}>
                  {isDone ? 'DONE' : hex.tab}
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {/* ------------------------------------------------------------------ */}
      {/* ACTION CATEGORY SUB-TABS: Coalition | Finance | Events | States    */}
      {/* ------------------------------------------------------------------ */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        gap: '8px',
        backgroundColor: '#131d38',
        padding: '4px',
        borderRadius: '10px',
        border: '1px solid rgba(56, 189, 248, 0.2)'
      }}>
        {[
          { key: 'coalition', label: '🤝 Coalition', color: '#f59e0b', hexKey: 'coalition_hub' },
          { key: 'finance', label: '💰 Finance', color: '#10b981', hexKey: 'finance_ops' },
          { key: 'events', label: '📰 Events & Issues', color: '#ec4899', hexKey: 'events_ops' },
          { key: 'states', label: '🗺️ States', color: '#a855f7', hexKey: 'states_ops' }
        ].map(tab => {
          const isActive = activeSubTab === tab.key;
          const isTabDone = tab.hexKey ? getIsHexDone(tab.hexKey) : false;
          return (
            <button
              key={tab.key}
              onClick={() => handleTabClick(tab.key)}
              style={{
                flex: 1,
                padding: '7px 10px',
                borderRadius: '6px',
                border: isActive
                  ? `1.5px solid ${tab.color}`
                  : isTabDone
                  ? '1px solid rgba(16, 185, 129, 0.4)'
                  : '1px solid transparent',
                backgroundColor: isActive
                  ? 'rgba(56, 189, 248, 0.12)'
                  : isTabDone
                  ? 'rgba(16, 185, 129, 0.08)'
                  : 'transparent',
                color: isActive ? '#ffffff' : isTabDone ? '#34d399' : '#94a3b8',
                fontWeight: isActive ? '900' : '700',
                fontSize: '9.5px',
                cursor: 'pointer',
                transition: 'all 0.2s ease',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                gap: '4px'
              }}
            >
              <span>{tab.label}</span>
              {isTabDone && (
                <span style={{
                  backgroundColor: '#10B981',
                  color: '#ffffff',
                  borderRadius: '50%',
                  width: '12px',
                  height: '12px',
                  display: 'inline-flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontSize: '7.5px',
                  fontWeight: 900
                }}>✓</span>
              )}
            </button>
          );
        })}
      </div>

      {/* ------------------------------------------------------------------ */}
      {/* SEASONAL TURN DIRECTIVES STATUS & NEXT TURN CALLOUT                 */}
      {/* ------------------------------------------------------------------ */}
      {onAdvanceSeason && (
        <div style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          flexWrap: 'wrap',
          gap: '12px',
          padding: '10px 14px',
          background: (isCoalitionDone && isFinanceDone && isEventsDone && isStatesDone)
            ? 'linear-gradient(135deg, rgba(16, 185, 129, 0.15) 0%, rgba(5, 150, 105, 0.25) 100%)'
            : 'linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(15, 23, 42, 0.9) 100%)',
          border: (isCoalitionDone && isFinanceDone && isEventsDone && isStatesDone)
            ? '1px solid rgba(52, 211, 153, 0.5)'
            : '1px solid rgba(56, 189, 248, 0.25)',
          borderRadius: '10px',
          boxShadow: (isCoalitionDone && isFinanceDone && isEventsDone && isStatesDone)
            ? '0 0 16px rgba(16, 185, 129, 0.2)'
            : '0 4px 12px rgba(0, 0, 0, 0.25)'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <div style={{ fontSize: '18px', lineHeight: 1 }}>
              {(isCoalitionDone && isFinanceDone && isEventsDone && isStatesDone) ? '🏁' : '📋'}
            </div>
            <div>
              <div style={{
                fontSize: '11px',
                fontWeight: '900',
                color: (isCoalitionDone && isFinanceDone && isEventsDone && isStatesDone) ? '#34d399' : '#e2e8f0',
                display: 'flex',
                alignItems: 'center',
                gap: '6px'
              }}>
                <span>Turn {activeGame?.currentSeason || 1} Operations Status:</span>
                <span style={{
                  color: (isCoalitionDone && isFinanceDone && isEventsDone && isStatesDone) ? '#10b981' : '#38bdf8',
                  fontWeight: '900'
                }}>
                  {[isCoalitionDone, isFinanceDone, isEventsDone, isStatesDone].filter(Boolean).length} / 4 Directives Complete
                </span>
                {(isCoalitionDone && isFinanceDone && isEventsDone && isStatesDone) && (
                  <span className="nwr-badge nwr-badge-emerald" style={{ fontSize: '8px', padding: '2px 6px' }}>
                    ALL TASKS DONE
                  </span>
                )}
              </div>
              <div style={{ fontSize: '9px', color: '#94a3b8', marginTop: '2px' }}>
                {(isCoalitionDone && isFinanceDone && isEventsDone && isStatesDone)
                  ? 'All 4 directives (Coalition, Finance, Events & States) resolved. Ready to end turn below.'
                  : 'Complete directives across Coalition, Finance, Events & States, then end the turn below.'}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* ------------------------------------------------------------------ */}
      {/* CONTEXTUAL STRATEGIC ADVISORY CALLOUT                               */}
      {/* ------------------------------------------------------------------ */}
      {/* ------------------------------------------------------------------ */}
      {/* CONTEXTUAL STRATEGIC ADVISORY CALLOUT (ON-DEMAND / COLLAPSIBLE)     */}
      {/* ------------------------------------------------------------------ */}
      {hintData?.actions?.[activeSubTab] && (() => {
        const currentAction = hintData.actions[activeSubTab];
        return (
          <div style={{
            background: 'linear-gradient(135deg, rgba(30, 41, 59, 0.75) 0%, rgba(15, 23, 42, 0.9) 100%)',
            border: '1px solid rgba(56, 189, 248, 0.2)',
            borderRadius: '10px',
            padding: showStrategicAdvice ? '12px 16px' : '7px 12px',
            boxShadow: '0 4px 16px rgba(0,0,0,0.25)',
            borderLeft: `4px solid ${currentAction.badgeColor || '#38bdf8'}`,
            transition: 'all 0.2s ease-in-out'
          }}>
            {/* Header / Toggle Row */}
            <div style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              gap: '12px'
            }}>
              <div
                onClick={() => setShowStrategicAdvice(prev => !prev)}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '8px',
                  cursor: 'pointer',
                  userSelect: 'none',
                  flex: 1
                }}
              >
                <span
                  title={showStrategicAdvice ? 'Click to hide advice' : 'Click to ask for advice'}
                  style={{
                    display: 'inline-flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    width: '22px',
                    height: '22px',
                    borderRadius: '50%',
                    backgroundColor: showStrategicAdvice ? 'rgba(56, 189, 248, 0.25)' : 'rgba(56, 189, 248, 0.12)',
                    border: `1.5px solid ${showStrategicAdvice ? '#38bdf8' : 'rgba(56, 189, 248, 0.4)'}`,
                    color: '#38bdf8',
                    fontSize: '11px',
                    fontWeight: '900',
                    lineHeight: 1,
                    transition: 'all 0.15s ease'
                  }}
                >
                  ℹ
                </span>
                <span style={{ fontSize: '10.5px', fontWeight: 900, color: '#38bdf8', letterSpacing: '0.04em', textTransform: 'uppercase' }}>
                  Strategic Advisor: {currentAction.title}
                </span>
                <span style={{
                  fontSize: '8.5px',
                  fontWeight: 800,
                  padding: '1px 6px',
                  borderRadius: '4px',
                  backgroundColor: `${currentAction.badgeColor || '#38bdf8'}22`,
                  color: currentAction.badgeColor || '#38bdf8',
                  border: `1px solid ${currentAction.badgeColor || '#38bdf8'}55`
                }}>
                  {currentAction.badge}
                </span>
              </div>

              {/* Ask for advice / Hide toggle button */}
              <button
                type="button"
                onClick={() => setShowStrategicAdvice(prev => !prev)}
                style={{
                  padding: '4px 10px',
                  borderRadius: '6px',
                  border: showStrategicAdvice ? '1px solid rgba(148, 163, 184, 0.35)' : '1px solid rgba(56, 189, 248, 0.4)',
                  backgroundColor: showStrategicAdvice ? 'rgba(30, 41, 59, 0.6)' : 'rgba(56, 189, 248, 0.15)',
                  color: showStrategicAdvice ? '#94a3b8' : '#38bdf8',
                  fontSize: '9.5px',
                  fontWeight: '800',
                  cursor: 'pointer',
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '5px',
                  transition: 'all 0.15s ease'
                }}
              >
                <span>{showStrategicAdvice ? 'Hide Advice ▲' : '💡 Ask for Advice ▼'}</span>
              </button>
            </div>

            {/* Expandable Advice Content */}
            {showStrategicAdvice && (
              <div style={{
                marginTop: '10px',
                paddingTop: '10px',
                borderTop: '1px solid rgba(255, 255, 255, 0.08)',
                display: 'flex',
                flexDirection: 'column',
                gap: '6px'
              }}>
                <div style={{ fontSize: '11.5px', color: '#f1f5f9', lineHeight: 1.45, fontWeight: '500' }}>
                  {currentAction.recommendation}
                </div>
                {currentAction.actionTip && (
                  <div style={{
                    fontSize: '10.5px',
                    color: '#93c5fd',
                    display: 'flex',
                    alignItems: 'flex-start',
                    gap: '5px',
                    fontWeight: '600',
                    backgroundColor: 'rgba(0, 0, 0, 0.25)',
                    padding: '6px 10px',
                    borderRadius: '6px',
                    border: '1px solid rgba(56, 189, 248, 0.15)'
                  }}>
                    <span style={{ color: '#38bdf8' }}>🎯 Tactical Directive:</span>
                    <span>{currentAction.actionTip}</span>
                  </div>
                )}
              </div>
            )}
          </div>
        );
      })()}

      {/* ------------------------------------------------------------------ */}
      {/* TAB CONTENT: COALITION                                             */}
      {/* ------------------------------------------------------------------ */}
      {activeSubTab === 'coalition' && (
        <NationalWR_Coalition
          activeGame={activeGame}
          configData={configData}
          onGameUpdate={onGameUpdate}
          isCompleted={isCoalitionDone}
          onMarkCompleted={handleMarkCoalitionCompleted}
        />
      )}

      {/* ------------------------------------------------------------------ */}
      {/* TAB CONTENT: FINANCE (FINANCE DASHBOARD & 6-CARD HAND)             */}
      {/* ------------------------------------------------------------------ */}
      {activeSubTab === 'finance' && (
        <NationalWR_Finance
          activeGame={activeGame}
          configData={configData}
          onGameUpdate={onGameUpdate}
          isCompleted={isFinanceDone}
          onMarkCompleted={handleMarkFinanceCompleted}
        />
      )}

      {/* ------------------------------------------------------------------ */}
      {/* TAB CONTENT: EVENTS & ISSUES                                       */}
      {/* ------------------------------------------------------------------ */}
      {activeSubTab === 'events' && (
        <NationalWR_Events
          activeGame={activeGame}
          configData={configData}
          onGameUpdate={onGameUpdate}
          isCompleted={isEventsDone}
          onMarkCompleted={handleMarkEventsCompleted}
        />
      )}

      {/* ------------------------------------------------------------------ */}
      {/* TAB CONTENT: STATES (REGIONAL STATE OPERATIONS & ELECTIONS)        */}
      {/* ------------------------------------------------------------------ */}
      {activeSubTab === 'states' && (
        <NationalWR_States
          activeGame={activeGame}
          configData={configData}
          onGameUpdate={onGameUpdate}
          isCompleted={isStatesDone}
          onMarkCompleted={handleMarkStatesCompleted}
        />
      )}

      {/* ------------------------------------------------------------------ */}
      {/* BOTTOM FLASHING END TURN BANNER                                    */}
      {/* ------------------------------------------------------------------ */}
      {(() => {
        const isAllFourDone = isCoalitionDone && isFinanceDone && isEventsDone && isStatesDone;
        const doneCount = [isCoalitionDone, isFinanceDone, isEventsDone, isStatesDone].filter(Boolean).length;

        return (
          <div style={{
            marginTop: '12px',
            padding: '16px 20px',
            borderRadius: '12px',
            background: isAllFourDone
              ? 'linear-gradient(135deg, rgba(245, 158, 11, 0.15) 0%, rgba(2, 132, 199, 0.25) 100%)'
              : 'linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(15, 23, 42, 0.9) 100%)',
            border: isAllFourDone
              ? '2px solid #fbbf24'
              : '1px solid rgba(56, 189, 248, 0.25)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            flexWrap: 'wrap',
            gap: '14px',
            boxShadow: isAllFourDone
              ? '0 0 24px rgba(245, 158, 11, 0.35)'
              : '0 4px 16px rgba(0,0,0,0.3)'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
              <div style={{ fontSize: '26px' }}>
                {isAllFourDone ? '⚡' : '📋'}
              </div>
              <div>
                <div style={{
                  fontSize: '13px',
                  fontWeight: 900,
                  color: isAllFourDone ? '#fbbf24' : '#e2e8f0',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '8px'
                }}>
                  <span>Turn {activeGame?.currentSeason || 1} Command Cycle:</span>
                  <span style={{ color: isAllFourDone ? '#34d399' : '#38bdf8' }}>
                    {doneCount} / 4 Operations Ready
                  </span>
                  {isAllFourDone && (
                    <span className="nwr-badge nwr-badge-gold" style={{ fontSize: '8px' }}>
                      ALL 4 ACTIONS COMPLETE
                    </span>
                  )}
                </div>
                <div style={{ fontSize: '10px', color: '#94a3b8', marginTop: '3px' }}>
                  {isAllFourDone
                    ? 'All 4 strategic operations committed. Ending turn will evaluate state battles, execute AI party maneuvers, recalculate national projected seats, and resolve scheduled elections.'
                    : `Complete or skip remaining directives (Coalition: ${isCoalitionDone ? '✓' : 'Pending'}, Finance: ${isFinanceDone ? '✓' : 'Pending'}, Events: ${isEventsDone ? '✓' : 'Pending'}, States: ${isStatesDone ? '✓' : 'Pending'}).`}
                </div>
              </div>
            </div>

            <button
              onClick={onAdvanceSeason}
              disabled={isAdvancingSeason || !isAllFourDone}
              className={isAllFourDone ? 'nwr-end-turn-flashing' : ''}
              style={{
                background: isAllFourDone
                  ? 'linear-gradient(135deg, #f59e0b 0%, #ea580c 50%, #0284c7 100%)'
                  : 'linear-gradient(135deg, #1e293b 0%, #0f172a 100%)',
                border: isAllFourDone ? '2px solid #fde047' : '1px solid rgba(255,255,255,0.15)',
                color: isAllFourDone ? '#ffffff' : '#64748b',
                padding: isAllFourDone ? '10px 24px' : '8px 16px',
                borderRadius: '10px',
                fontSize: '12px',
                fontWeight: 900,
                cursor: (!isAllFourDone || isAdvancingSeason) ? 'not-allowed' : 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                boxShadow: isAllFourDone ? '0 0 20px rgba(245, 158, 11, 0.7)' : 'none',
                transition: 'all 0.2s',
                opacity: isAdvancingSeason ? 0.7 : (isAllFourDone ? 1 : 0.45)
              }}
              title={isAllFourDone ? 'All 4 directives complete! Click to end turn.' : `Complete all 4 operations (${doneCount}/4 done) to enable End Turn.`}
            >
              {isAdvancingSeason ? (
                '⏳ Resolving Turn...'
              ) : isAllFourDone ? (
                <>
                  <span>⚡</span>
                  <span>END TURN & RESOLVE SEASON →</span>
                </>
              ) : (
                <>
                  <span>🔒 Complete All Directives ({doneCount}/4 Ready)</span>
                </>
              )}
            </button>
          </div>
        );
      })()}

    </div>
  );
}
