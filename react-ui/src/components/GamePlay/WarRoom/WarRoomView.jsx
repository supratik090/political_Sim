import React, { useState, useEffect, useRef, useCallback } from 'react';
import { useGameStore } from '../../../store/gameStore';
import { cardRequiresTarget } from '../gameUtils';

import './warroom.css';

import WR_Header       from './WR_Header';
import WR_HexTracker   from './WR_HexTracker';
import WR_TabBar       from './WR_TabBar';
import WR_Action1_Card from './WR_Action1_Card';
import WR_Action2_News from './WR_Action2_News';
import WR_Action3_Governance from './WR_Action3_Governance';
import WR_Action4_Bid  from './WR_Action4_Bid';
import WR_Action5_Reward from './WR_Action5_Reward';
import WR_Action6_PartyBuilding from './WR_Action6_PartyBuilding';
import WR_Action7_Cooperation   from './WR_Action7_Cooperation';
import WR_Action8_Assembly      from './WR_Action8_Assembly';

const TAB_POLITICS   = 'politics';
const TAB_GOVERNANCE = 'governance';
const TAB_ECONOMY    = 'economy';

// Hex navigation — sequential order, tab mapping, and section ID mapping
const HEX_ORDER = ['card', 'news', 'assembly', 'governance', 'cooperation', 'bid', 'reward', 'building'];

const HEX_TAB_MAP = {
  card: 'politics', news: 'politics', assembly: 'politics',
  governance: 'governance', cooperation: 'governance',
  bid: 'economy', reward: 'economy', building: 'economy',
};

const HEX_SECTION_MAP = {
  card: 'wr-section-1', news: 'wr-section-2', assembly: 'wr-section-8',
  governance: 'wr-section-3', cooperation: 'wr-section-7',
  bid: 'wr-section-4', reward: 'wr-section-5', building: 'wr-section-6',
};

const ACCORDION_TO_HEX = {
  1: 'card', 2: 'news', 3: 'governance', 4: 'bid', 5: 'reward',
  6: 'building', 7: 'cooperation', 8: 'assembly',
};

/**
 * WarRoomView — Dark-theme mobile-first Actions UI
 * Accepts the EXACT same props as ActionsView. Zero state lives in GamePlayBoard
 * beyond the toggle `useWarRoom` + useState.
 */
export default function WarRoomView({
  turnData,
  activeParty,
  loading = false,
  handleAdvanceTurn,
  handleSkipTurn,
  projectDefs = {},
  selectedCard = null,
  setSelectedCard = () => {},
  targetPartyId = '',
  setTargetPartyId = () => {},
  cardCategoryFilter = 'agitation_movement',
  setCardCategoryFilter = () => {},
  selectedNewsReactions = {},
  setSelectedNewsReactions = () => {},
  selectedIssueOptionKey = '',
  setSelectedIssueOptionKey = () => {},
  bidAmount = 0,
  setBidAmount = () => {},
  bidConfirmed = false,
  setBidConfirmed = () => {},
  selectedRewardKey = '',
  setSelectedRewardKey = () => {},
  rewardTargetPartyId = '',
  setRewardTargetPartyId = () => {},
  rewardConfirmed = false,
  setRewardConfirmed = () => {},
  projectCategoryFilter = 'BUILD',
  setProjectCategoryFilter = () => {},
  fundingContributions = {},
  setFundingContributions = () => {},
  partyBuildingConfirmed = false,
  setPartyBuildingConfirmed = () => {},
  handleFundProject = () => {},
  handleDestroyProject = () => {},
  handleSetProjectTarget = () => {},
  fundedThisTurn = [],
  setFundedThisTurn = () => {},
  handleCooperationUpdate = () => {},
  billVote = '',
  setBillVote = () => {},
  whipIssued = false,
  setWhipIssued = () => {},
  proposedBillKey = '',
  setProposedBillKey = () => {},
  selectedEventOptionKey = '',
  setSelectedEventOptionKey = () => {},
  scenarioBills = [],
  scenarioEvents = [],
  activeAccordion = 1,
  setActiveAccordion = () => {},
}) {
  const [activeTab, setActiveTab] = useState(TAB_POLITICS);
  const [activeHex, setActiveHex] = useState('card');
  const nudgeTimerRef = useRef(null);
  const activeHexRef = useRef('card');

  // ── Multiplayer identity ──
  const { user } = useGameStore();
  const humanPlayerMap = turnData?.humanPlayerMap || {};
  const isMultiplayer  = turnData?.isMultiplayer;
  const loggedInUserId = (user?.id || user?.email)?.toLowerCase();
  const myParty = isMultiplayer
    ? turnData?.parties?.find(p => humanPlayerMap[p.id]?.toLowerCase() === loggedInUserId)
    : activeParty;
  const isMyTurn = !isMultiplayer || (myParty?.id === turnData?.activeHumanPartyId);

  // ── Completion checks (guarded against undefined/null props) ──
  const isCardCompleted = selectedCard !== null && selectedCard !== undefined && (!cardRequiresTarget(selectedCard) || targetPartyId !== '');
  const newsItems       = turnData?.currentNews || [];
  const safeNewsReactions = selectedNewsReactions || {};
  const isNewsCompleted = newsItems.length === 0 || newsItems.every(n => n && (safeNewsReactions[n.newsKey || n.issueKey] !== undefined));
  const isSection3Completed = turnData?.activeEventKey
    ? (selectedEventOptionKey !== '' && selectedEventOptionKey !== null && selectedEventOptionKey !== undefined)
    : (selectedIssueOptionKey === 'mock_done');
  const isBidCompleted  = bidConfirmed;
  const hasRewards      = turnData?.activePlayerHeldRewards && turnData.activePlayerHeldRewards.length > 0;
  const selectedReward  = hasRewards ? (turnData?.activePlayerHeldRewards || []).find(r => r && r.rewardKey === selectedRewardKey) : null;
  const isRewardCompleted = !hasRewards || selectedRewardKey === '' || (rewardConfirmed && (!selectedReward?.requiresTarget || rewardTargetPartyId !== ''));
  const hasPartyBuildingDrafts   = Object.values(fundingContributions || {}).some(v => v > 0);
  const isPartyBuildingCompleted = !hasPartyBuildingDrafts || partyBuildingConfirmed;
  const isLegislativeCompleted   = !turnData?.proposedBillKeyThisTurn || (billVote !== '' && billVote !== null && billVote !== undefined);

  const allActionsReady = isCardCompleted && isNewsCompleted && isSection3Completed && isBidCompleted && isRewardCompleted && isPartyBuildingCompleted && isLegislativeCompleted;

  // Tab-level completion for WR_TabBar
  const politicsDone    = isCardCompleted && isNewsCompleted && isLegislativeCompleted;
  const governanceDone  = isSection3Completed;
  const economyDone     = isBidCompleted && isRewardCompleted && isPartyBuildingCompleted;
  const politicsPending   = !isCardCompleted || !isNewsCompleted || (!!turnData?.proposedBillKeyThisTurn && !isLegislativeCompleted);
  const governancePending = !isSection3Completed;
  const economyPending    = !isBidCompleted;

  // Hex map — 8 hexes
  const doneMap = {
    card:        isCardCompleted,
    news:        isNewsCompleted,
    assembly:    isLegislativeCompleted,
    governance:  isSection3Completed,
    cooperation: true,              // optional — always mark done
    bid:         isBidCompleted,
    reward:      isRewardCompleted,
    building:    isPartyBuildingCompleted,
  };

  const doneCount = Object.values(doneMap).filter(Boolean).length;

  // ── Keep activeHex ref in sync ──
  useEffect(() => { activeHexRef.current = activeHex; }, [activeHex]);

  // ── Nudge timer helpers ──
  const clearNudgeTimer = useCallback(() => {
    if (nudgeTimerRef.current) {
      clearTimeout(nudgeTimerRef.current);
      nudgeTimerRef.current = null;
    }
  }, []);

  const navigateToHex = useCallback((hexKey) => {
    clearNudgeTimer();
    setActiveHex(hexKey);
    const targetTab = HEX_TAB_MAP[hexKey];
    setActiveTab(targetTab);
    // Scroll to the section after the tab switch renders
    setTimeout(() => {
      const el = document.getElementById(HEX_SECTION_MAP[hexKey]);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
        // Brief highlight flash on the target section
        el.style.transition = 'box-shadow 0.3s ease, border-color 0.3s ease';
        el.style.borderColor = '#38bdf8';
        el.style.boxShadow = '0 0 20px rgba(56, 189, 248, 0.35)';
        setTimeout(() => {
          el.style.borderColor = 'rgba(255,255,255,0.08)';
          el.style.boxShadow = '0 4px 16px rgba(0,0,0,0.2)';
        }, 1500);
      }
    }, 250);
  }, [clearNudgeTimer]);

  const startNudgeTimer = useCallback(() => {
    clearNudgeTimer();
    nudgeTimerRef.current = setTimeout(() => {
      const currentIdx = HEX_ORDER.indexOf(activeHexRef.current);
      if (currentIdx < HEX_ORDER.length - 1) {
        navigateToHex(HEX_ORDER[currentIdx + 1]);
      }
    }, 2000);
  }, [clearNudgeTimer, navigateToHex]);

  // ── Auto-nudge: when active hex is done, start 2s timer to advance ──
  const isActiveHexDone = !!doneMap[activeHex];

  useEffect(() => {
    clearNudgeTimer();
    if (isActiveHexDone) {
      startNudgeTimer();
    }
    return () => clearNudgeTimer();
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [activeHex, isActiveHexDone]);

  // ── Reset nudge timer on any user activity (click, touch, scroll) ──
  const handleUserActivity = useCallback(() => {
    if (nudgeTimerRef.current) {
      startNudgeTimer(); // clears and restarts the 2s timer
    }
  }, [startNudgeTimer]);

  // ── Hex click handler ──
  const handleHexClick = useCallback((hexKey) => {
    navigateToHex(hexKey);
  }, [navigateToHex]);

  // Sync tab, activeHex & scroll to section when navigated from Hint
  useEffect(() => {
    if (!activeAccordion) return;

    clearNudgeTimer();

    let targetTab = TAB_POLITICS;
    if (activeAccordion === 1 || activeAccordion === 2 || activeAccordion === 8) {
      targetTab = TAB_POLITICS;
    } else if (activeAccordion === 3 || activeAccordion === 7) {
      targetTab = TAB_GOVERNANCE;
    } else if (activeAccordion === 4 || activeAccordion === 5 || activeAccordion === 6) {
      targetTab = TAB_ECONOMY;
    }

    setActiveTab(targetTab);

    // Also sync the active hex
    const hexKey = ACCORDION_TO_HEX[activeAccordion];
    if (hexKey) setActiveHex(hexKey);

    const timer = setTimeout(() => {
      const el = document.getElementById(`wr-section-${activeAccordion}`);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        el.style.transition = 'box-shadow 0.3s ease, border-color 0.3s ease';
        const origBorder = el.style.borderColor;
        const origShadow = el.style.boxShadow;
        el.style.borderColor = '#38bdf8';
        el.style.boxShadow = '0 0 24px rgba(56, 189, 248, 0.5)';
        setTimeout(() => {
          el.style.borderColor = origBorder || 'rgba(255,255,255,0.08)';
          el.style.boxShadow = origShadow || '0 4px 16px rgba(0,0,0,0.2)';
        }, 1800);
      }
    }, 150);

    return () => clearTimeout(timer);
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [activeAccordion]);

  if (!turnData) {
    return (
      <div className="wr-root">
        <div className="wr-waiting">
          <div style={{ fontSize: '32px', marginBottom: '12px' }}>⏳</div>
          <div style={{ color: '#7D8590', fontSize: '14px' }}>Loading campaign data…</div>
        </div>
      </div>
    );
  }

  // Multiplayer waiting state
  if (isMultiplayer && !isMyTurn) {
    return (
      <div className="wr-root">
        <WR_Header turnData={turnData} activeParty={activeParty} handleSkipTurn={handleSkipTurn} loading={loading} isMyTurn={false} />
        <div className="wr-waiting">
          <div style={{ fontSize: '40px', marginBottom: '14px' }}>⚔️</div>
          <div style={{ fontSize: '18px', fontWeight: 900, color: '#E6EDF3', marginBottom: '8px' }}>
            Waiting for Opponents
          </div>
          <div style={{ fontSize: '13px', color: '#7D8590' }}>
            Other players are making their moves…
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="wr-root" style={{ display: 'flex', flexDirection: 'column', minHeight: '100%' }}>
      {/* ── TOP CHROME ── */}
      <WR_Header
        turnData={turnData}
        activeParty={activeParty}
        handleSkipTurn={handleSkipTurn}
        loading={loading}
        isMyTurn={isMyTurn}
      />

      <WR_HexTracker
        doneMap={doneMap}
        activeHex={activeHex}
        onHexClick={handleHexClick}
      />

      <WR_TabBar
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        politicsDone={politicsDone}
        politicsPending={politicsPending}
        governanceDone={governanceDone}
        governancePending={governancePending}
        economyDone={economyDone}
        economyPending={economyPending}
      />

      {/* ── TAB CONTENT ── */}
      <div
        className="wr-tab-content"
        key={activeTab}
        style={{ flex: 1, overflowY: 'auto', paddingBottom: '30px' }}
        onMouseDown={handleUserActivity}
        onTouchStart={handleUserActivity}
        onScroll={handleUserActivity}
      >
        {/* ──────────── POLITICS TAB ──────────── */}
        {activeTab === TAB_POLITICS && (
          <>
            {/* Action 1 — Card */}
            <div id="wr-section-1" style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.08)', borderRadius: '16px', padding: '16px 12px', marginBottom: '24px', boxShadow: '0 4px 16px rgba(0,0,0,0.2)' }}>
              <WR_Action1_Card
                turnData={turnData}
                selectedCard={selectedCard}
                setSelectedCard={setSelectedCard}
                targetPartyId={targetPartyId}
                setTargetPartyId={setTargetPartyId}
                cardCategoryFilter={cardCategoryFilter}
                setCardCategoryFilter={setCardCategoryFilter}
              />
            </div>

            {/* Action 2 — News */}
            <div id="wr-section-2" style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.08)', borderRadius: '16px', padding: '16px 12px', marginBottom: '24px', boxShadow: '0 4px 16px rgba(0,0,0,0.2)' }}>
              <WR_Action2_News
                turnData={turnData}
                selectedNewsReactions={selectedNewsReactions}
                setSelectedNewsReactions={setSelectedNewsReactions}
              />
            </div>

            {/* Action 8 — Assembly Vote (Politics tab) */}
            <div id="wr-section-8" style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.08)', borderRadius: '16px', padding: '16px 12px', marginBottom: '24px', boxShadow: '0 4px 16px rgba(0,0,0,0.2)' }}>
              <WR_Action8_Assembly
                turnData={turnData}
                activeParty={activeParty}
                billVote={billVote}
                setBillVote={setBillVote}
                whipIssued={whipIssued}
                setWhipIssued={setWhipIssued}
                proposedBillKey={proposedBillKey}
                setProposedBillKey={setProposedBillKey}
                selectedEventOptionKey={selectedEventOptionKey}
                setSelectedEventOptionKey={setSelectedEventOptionKey}
                scenarioBills={scenarioBills}
                scenarioEvents={scenarioEvents}
              />
            </div>
          </>
        )}

        {/* ──────────── GOVERNANCE TAB ──────────── */}
        {activeTab === TAB_GOVERNANCE && (
          <>
            {/* Action 3/4 — Party Management */}
            <div id="wr-section-3" style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.08)', borderRadius: '16px', padding: '16px 12px', marginBottom: '24px', boxShadow: '0 4px 16px rgba(0,0,0,0.2)' }}>
              <WR_Action3_Governance
                turnData={turnData}
                selectedIssueOptionKey={selectedIssueOptionKey}
                setSelectedIssueOptionKey={setSelectedIssueOptionKey}
                activeParty={activeParty}
                selectedEventOptionKey={selectedEventOptionKey}
                setSelectedEventOptionKey={setSelectedEventOptionKey}
                scenarioEvents={scenarioEvents}
                projectDefs={projectDefs}
              />
            </div>

            {/* Action 7 — Cooperation (optional) */}
            <div id="wr-section-7" style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.08)', borderRadius: '16px', padding: '16px 12px', marginBottom: '24px', boxShadow: '0 4px 16px rgba(0,0,0,0.2)' }}>
              <WR_Action7_Cooperation
                turnData={turnData}
                projectDefs={projectDefs}
                onActionComplete={handleCooperationUpdate}
              />
            </div>
          </>
        )}

        {/* ──────────── ECONOMY TAB ──────────── */}
        {activeTab === TAB_ECONOMY && (
          <>
            {/* Action 4 — Competitive Bid */}
            <div id="wr-section-4" style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.08)', borderRadius: '16px', padding: '16px 12px', marginBottom: '24px', boxShadow: '0 4px 16px rgba(0,0,0,0.2)' }}>
              <WR_Action4_Bid
                turnData={turnData}
                activeParty={activeParty}
                bidAmount={bidAmount}
                setBidAmount={setBidAmount}
                bidConfirmed={bidConfirmed}
                setBidConfirmed={setBidConfirmed}
              />
            </div>

            {/* Action 5 — Rewards */}
            <div id="wr-section-5" style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.08)', borderRadius: '16px', padding: '16px 12px', marginBottom: '24px', boxShadow: '0 4px 16px rgba(0,0,0,0.2)' }}>
              <WR_Action5_Reward
                turnData={turnData}
                selectedRewardKey={selectedRewardKey}
                setSelectedRewardKey={setSelectedRewardKey}
                rewardTargetPartyId={rewardTargetPartyId}
                setRewardTargetPartyId={setRewardTargetPartyId}
                rewardConfirmed={rewardConfirmed}
                setRewardConfirmed={setRewardConfirmed}
              />
            </div>

            {/* Action 6 — Party Building (optional) */}
            <div id="wr-section-6" style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.08)', borderRadius: '16px', padding: '16px 12px', marginBottom: '24px', boxShadow: '0 4px 16px rgba(0,0,0,0.2)' }}>
              <WR_Action6_PartyBuilding
                turnData={turnData}
                activeParty={activeParty}
                projectDefs={projectDefs}
                projectCategoryFilter={projectCategoryFilter}
                setProjectCategoryFilter={setProjectCategoryFilter}
                fundingContributions={fundingContributions}
                setFundingContributions={setFundingContributions}
                partyBuildingConfirmed={partyBuildingConfirmed}
                setPartyBuildingConfirmed={setPartyBuildingConfirmed}
                handleFundProject={handleFundProject}
                handleDestroyProject={handleDestroyProject}
                handleSetProjectTarget={handleSetProjectTarget}
                fundedThisTurn={fundedThisTurn}
              />
            </div>
          </>
        )}

        {/* ── END TURN FOOTER (AT BOTTOM OF OPTIONS) ── */}
        <div className="wr-end-turn-footer">
          {/* Status caption */}
          <div style={{
            textAlign: 'center',
            marginBottom: '10px',
            fontSize: '13px',
            fontWeight: 700,
            color: allActionsReady ? '#4ADE80' : '#7D8590',
            transition: 'color 0.3s ease',
          }}>
            {allActionsReady
              ? '🎉 All decisions locked — ready to submit!'
              : `${doneCount} of 8 actions complete`}
          </div>

          {/* End Turn button */}
          <button
            onClick={handleAdvanceTurn}
            disabled={!allActionsReady || loading || !isMyTurn}
            style={{
              width: '100%',
              minHeight: '56px',
              fontSize: '17px',
              fontWeight: 900,
              letterSpacing: '0.04em',
              borderRadius: '16px',
              border: 'none',
              background: allActionsReady && isMyTurn
                ? 'linear-gradient(135deg,#16A34A 0%,#15803d 100%)'
                : 'rgba(255,255,255,0.06)',
              color: allActionsReady && isMyTurn ? '#ffffff' : '#4B5563',
              boxShadow: allActionsReady && isMyTurn ? '0 0 24px rgba(22,163,74,0.5)' : 'none',
              animation: allActionsReady && isMyTurn ? 'wr-pulse-green 2s ease-in-out infinite' : 'none',
              cursor: allActionsReady && isMyTurn && !loading ? 'pointer' : 'not-allowed',
              transition: 'background 0.3s ease, color 0.3s ease, box-shadow 0.3s ease',
              touchAction: 'manipulation',
              WebkitTapHighlightColor: 'transparent',
              fontFamily: 'Montserrat,system-ui,sans-serif',
            }}
          >
            {loading ? '⏳ Submitting…' : '⚔️  END TURN — SUBMIT DECISIONS  →'}
          </button>

          {/* Multiplayer waiting hint */}
          {isMultiplayer && isMyTurn && !allActionsReady && (
            <div style={{ textAlign: 'center', marginTop: '8px', fontSize: '11px', color: '#4B5563' }}>
              Complete all required actions to submit your turn
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export class WarRoomErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error("WarRoomView render error:", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div style={{
          padding: '24px',
          margin: '16px',
          background: 'rgba(239, 68, 68, 0.1)',
          border: '1px solid #ef4444',
          borderRadius: '12px',
          color: '#f8fafc',
          textAlign: 'center',
        }}>
          <h3 style={{ color: '#f87171', margin: '0 0 8px 0' }}>⚠️ War Room Display Error</h3>
          <p style={{ fontSize: '13px', color: '#94a3b8', margin: '0 0 16px 0' }}>
            {this.state.error?.message || 'An unexpected error occurred while rendering the War Room.'}
          </p>
          <button
            type="button"
            onClick={() => this.setState({ hasError: false, error: null })}
            style={{
              padding: '8px 16px',
              background: '#ef4444',
              border: 'none',
              borderRadius: '8px',
              color: '#ffffff',
              fontWeight: 'bold',
              cursor: 'pointer',
            }}
          >
            🔄 Reload War Room
          </button>
        </div>
      );
    }
    return this.props.children;
  }
}
