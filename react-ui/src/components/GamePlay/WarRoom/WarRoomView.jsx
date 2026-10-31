import React, { useState, useEffect, useRef, useCallback } from 'react';
import { useGameStore } from '../../../store/gameStore';
import { cardRequiresTarget } from '../gameUtils';

import './warroom.css';

import WR_Header       from './WR_Header';
import WR_TabBar       from './WR_TabBar';
import WR_Action1_Card from './WR_Action1_Card';
import WR_Action2_News from './WR_Action2_News';
import WR_Action3_Governance from './WR_Action3_Governance';
import WR_Action4_Bid  from './WR_Action4_Bid';
import WR_Action5_Reward from './WR_Action5_Reward';
import WR_Action6_PartyBuilding from './WR_Action6_PartyBuilding';
import WR_Action7_Cooperation   from './WR_Action7_Cooperation';
import WR_Action8_Assembly      from './WR_Action8_Assembly';
import WR_Action_Media          from './WR_Action_Media';
import WarRoomSpotlightGuide    from './WarRoomSpotlightGuide';
import { calculateTurnLiveDeltas } from '../../../utils/instantFeedbackEngine';
import { preloadTurnFeedback } from '../../../utils/turnFeedbackCache';

const TAB_POLITICS   = 'politics';
const TAB_GOVERNANCE = 'governance';
const TAB_ECONOMY    = 'economy';

const ACCORDION_TO_TAB = {
  1: TAB_POLITICS,
  2: TAB_POLITICS,
  8: TAB_POLITICS,
  3: TAB_GOVERNANCE,
  7: TAB_GOVERNANCE,
  4: TAB_ECONOMY,
  5: TAB_ECONOMY,
  6: TAB_ECONOMY,
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
  selectedMediaTopicKey,
  setSelectedMediaTopicKey,
  selectedMediaChannels,
  setSelectedMediaChannels,
}) {
  const [activeTab, setActiveTab] = useState(TAB_POLITICS);
  const [runGuide, setRunGuide] = useState(false);
  const [tourKey, setTourKey] = useState(0);
  const nudgeTimerRef = useRef(null);

  // Auto-play Spotlight Guide on first load
  useEffect(() => {
    try {
      const seen = localStorage.getItem('hasSeenWarRoomGuide_v1');
      if (!seen && turnData && !loading) {
        const timer = setTimeout(() => {
          setRunGuide(true);
        }, 800);
        return () => clearTimeout(timer);
      }
    } catch (e) {
      // Ignore localStorage restrictions
    }
  }, [turnData, loading]);

  // Preload turn feedback cache for 0ms instant feedback
  useEffect(() => {
    const gameId = turnData?.gameId || turnData?.id || turnData?.scenarioId;
    const partyId = activeParty?.id;
    const turnNumber = turnData?.turnNumber || 0;
    if (gameId && partyId) {
      preloadTurnFeedback(gameId, partyId, turnNumber);
    }
  }, [turnData?.gameId, turnData?.id, turnData?.scenarioId, turnData?.turnNumber, activeParty?.id]);

  const handleOpenGuide = useCallback(() => {
    setActiveTab(TAB_POLITICS);
    setRunGuide(false);
    setTourKey(prev => prev + 1);
    setTimeout(() => {
      setRunGuide(true);
    }, 150);
  }, []);

  // ── Multiplayer identity ──
  const { user } = useGameStore();
  const humanPlayerMap = turnData?.humanPlayerMap || {};
  const isMultiplayer  = turnData?.isMultiplayer;
  const loggedInUserId = (user?.id || user?.email)?.toLowerCase();
  const myParty = isMultiplayer
    ? turnData?.parties?.find(p => humanPlayerMap[p.id]?.toLowerCase() === loggedInUserId)
    : activeParty;
  const isMyTurn = !isMultiplayer || (myParty?.id === turnData?.activeHumanPartyId);

  const gameSessionId = turnData?.gameId || turnData?.id || turnData?.scenarioId || 'default_session';
  const turnNumber = turnData?.turnNumber || 0;
  const cardLockStorageKey = `political_sim_card_locked_${gameSessionId}_turn_${turnNumber}`;
  const isCardLocked = typeof window !== 'undefined' && localStorage.getItem(cardLockStorageKey) === 'true';

  // Restore persisted card and target if not yet in state
  useEffect(() => {
    const cardStorageKey = `political_sim_card_selected_${gameSessionId}_turn_${turnNumber}`;
    const targetStorageKey = `political_sim_card_target_${gameSessionId}_turn_${turnNumber}`;
    if (!selectedCard) {
      try {
        const saved = localStorage.getItem(cardStorageKey);
        if (saved) {
          const parsed = JSON.parse(saved);
          if (parsed && parsed.cardKey) {
            setSelectedCard(parsed);
          }
        }
      } catch (_) {}
    }
    if (!targetPartyId) {
      try {
        const savedTarget = localStorage.getItem(targetStorageKey);
        if (savedTarget) {
          setTargetPartyId(savedTarget);
        }
      } catch (_) {}
    }
  }, [gameSessionId, turnNumber, selectedCard, targetPartyId, setSelectedCard, setTargetPartyId]);

  // ── Completion checks (guarded against undefined/null props) ──
  const isCardCompleted = isCardLocked || (selectedCard !== null && selectedCard !== undefined && (!cardRequiresTarget(selectedCard) || targetPartyId !== ''));
  const newsItems       = turnData?.currentNews || [];
  const safeNewsReactions = selectedNewsReactions || {};
  const newsLockStorageKey = `political_sim_news_locked_${gameSessionId}_turn_${turnNumber}`;
  const isNewsLocked = typeof window !== 'undefined' && localStorage.getItem(newsLockStorageKey) === 'true';
  const isNewsCompleted = isNewsLocked || newsItems.length === 0 || newsItems.every(n => n && (safeNewsReactions[n.newsKey || n.issueKey] !== undefined));
  const isEventCompleted = !turnData?.activeEventKey || (selectedEventOptionKey !== '' && selectedEventOptionKey !== null && selectedEventOptionKey !== undefined);
  const isLegislativeCompleted = (!turnData?.proposedBillKeyThisTurn || (billVote !== '' && billVote !== null && billVote !== undefined)) && isEventCompleted;

  // Governance completion checks
  const hasFactionCrisis = !!activeParty?.activeFactionCrisisKey;
  const isCrisisResolved = !hasFactionCrisis || (selectedIssueOptionKey === 'crisis_resolved' || selectedIssueOptionKey === 'mock_done');
  const partyMgmtStorageKey = `political_sim_party_management_${gameSessionId}_turn_${turnNumber}`;
  const isPartyMgmtLocked = activeParty?.partyManagementLocked ||
    turnData?.partyManagementState?.locked ||
    (typeof window !== 'undefined' && JSON.parse(localStorage.getItem(partyMgmtStorageKey) || '{}')?.isLocked === true) ||
    selectedIssueOptionKey === 'mock_done';
  const isSection3Completed = isCrisisResolved && isPartyMgmtLocked;

  const mediaLockStorageKey = `political_sim_media_locked_${gameSessionId}_turn_${turnNumber}`;
  const mediaSelectionStorageKey = `political_sim_media_selection_${gameSessionId}_turn_${turnNumber}`;
  const isMediaLocked = typeof window !== 'undefined' && localStorage.getItem(mediaLockStorageKey) === 'true';
  const isMediaSelected = typeof window !== 'undefined' && !!localStorage.getItem(mediaSelectionStorageKey);
  const isMediaCompleted = isMediaLocked || isMediaSelected || (selectedMediaTopicKey !== '' && selectedMediaTopicKey !== null && selectedMediaTopicKey !== undefined);

  const coopStorageKey = `political_sim_coop_done_${gameSessionId}_turn_${turnNumber}`;
  const [coopDone, setCoopDone] = useState(() => {
    try {
      return localStorage.getItem(coopStorageKey) === 'true';
    } catch (_) {
      return false;
    }
  });

  useEffect(() => {
    try {
      setCoopDone(localStorage.getItem(coopStorageKey) === 'true');
    } catch (_) {}
  }, [coopStorageKey]);

  const isCoopCompleted = coopDone || (typeof window !== 'undefined' && localStorage.getItem(coopStorageKey) === 'true');

  const governanceDone = isSection3Completed && isMediaCompleted && isCoopCompleted;
  const governancePending = !governanceDone;

  // Economy completion checks
  const isBidCompleted  = bidConfirmed;
  const hasRewards      = turnData?.activePlayerHeldRewards && turnData.activePlayerHeldRewards.length > 0;
  const selectedReward  = hasRewards ? (turnData?.activePlayerHeldRewards || []).find(r => r && r.rewardKey === selectedRewardKey) : null;
  const isRewardCompleted = !hasRewards || selectedRewardKey === '' || (rewardConfirmed && (!selectedReward?.requiresTarget || rewardTargetPartyId !== ''));
  const hasPartyBuildingDrafts   = Object.values(fundingContributions || {}).some(v => v > 0);
  const isPartyBuildingCompleted = !hasPartyBuildingDrafts || partyBuildingConfirmed;

  // Tab-level completion for WR_TabBar
  const politicsDone    = isCardCompleted && isNewsCompleted && isLegislativeCompleted;
  const economyDone     = isBidCompleted && isRewardCompleted && isPartyBuildingCompleted;
  const politicsPending   = !politicsDone;
  const economyPending    = !economyDone;

  const allActionsReady = politicsDone && governanceDone && economyDone;

  const isCurrentTabReady =
    (activeTab === TAB_POLITICS && politicsDone) ||
    (activeTab === TAB_GOVERNANCE && governanceDone) ||
    (activeTab === TAB_ECONOMY && economyDone);

  const isNextButtonActive = isCurrentTabReady || allActionsReady;

  // Determine the primary pending action and which tab/section it belongs to
  // Order: Card → News → Assembly → Governance (Party/Crisis → Media → Diplomacy) → Economy (Bid → Rewards → Party Building)
  let pendingAction = null;
  if (!isCardCompleted) {
    if (!selectedCard && !isCardLocked) {
      pendingAction = { message: 'Select your monthly Campaign Card', tab: TAB_POLITICS, section: 'wr-section-1' };
    } else {
      pendingAction = { message: 'Select an opponent target for your card', tab: TAB_POLITICS, section: 'wr-section-1' };
    }
  } else if (!isNewsCompleted) {
    pendingAction = { message: 'Respond to Breaking News', tab: TAB_POLITICS, section: 'wr-section-2' };
  } else if (!isLegislativeCompleted) {
    if (turnData?.activeEventKey && !isEventCompleted) {
      pendingAction = { message: 'Respond to Active Scenario Event', tab: TAB_POLITICS, section: 'wr-section-8' };
    } else {
      pendingAction = { message: 'Cast your Assembly Vote', tab: TAB_POLITICS, section: 'wr-section-8' };
    }
  } else if (!isSection3Completed) {
    pendingAction = {
      message: hasFactionCrisis ? 'Resolve internal Faction Crisis' : 'Confirm & Lock Party Allocations',
      tab: TAB_GOVERNANCE,
      section: 'wr-section-3'
    };
  } else if (!isMediaCompleted) {
    pendingAction = { message: 'Set Media & Narrative strategy', tab: TAB_GOVERNANCE, section: 'wr-section-media' };
  } else if (!isCoopCompleted) {
    pendingAction = { message: 'Review Diplomatic Cooperation', tab: TAB_GOVERNANCE, section: 'wr-section-7' };
  } else if (!isBidCompleted) {
    pendingAction = { message: 'Set and lock your Monthly Bid', tab: TAB_ECONOMY, section: 'wr-section-4' };
  } else if (!isRewardCompleted) {
    pendingAction = { message: 'Confirm your reward deployment target', tab: TAB_ECONOMY, section: 'wr-section-5' };
  } else if (!isPartyBuildingCompleted) {
    pendingAction = { message: 'Confirm your party building contributions', tab: TAB_ECONOMY, section: 'wr-section-6' };
  }

  // ── Nudge timer helpers ──
  const clearNudgeTimer = useCallback(() => {
    if (nudgeTimerRef.current) {
      clearTimeout(nudgeTimerRef.current);
      nudgeTimerRef.current = null;
    }
  }, []);

  const handleUserActivity = useCallback(() => {
    clearNudgeTimer();
  }, [clearNudgeTimer]);

  // Sync tab & scroll to section when navigated from Hint
  useEffect(() => {
    if (!activeAccordion) return;

    clearNudgeTimer();

    const targetTab = ACCORDION_TO_TAB[activeAccordion] || TAB_POLITICS;
    setActiveTab(targetTab);

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

  const liveDeltas = calculateTurnLiveDeltas(
    turnData,
    activeParty?.id,
    selectedCard,
    targetPartyId,
    selectedNewsReactions,
    bidAmount
  );

  return (
    <div className="wr-root" style={{ display: 'flex', flexDirection: 'column', minHeight: '100%' }}>
      {/* ── TOP CHROME ── */}
      <WR_Header
        turnData={turnData}
        activeParty={activeParty}
        handleSkipTurn={handleSkipTurn}
        loading={loading}
        isMyTurn={isMyTurn}
        onOpenGuide={handleOpenGuide}
        liveDeltas={liveDeltas}
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

            {/* Action 9 — Media & Narrative Management */}
            <div id="wr-section-media" style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.08)', borderRadius: '16px', padding: '16px 12px', marginBottom: '24px', boxShadow: '0 4px 16px rgba(0,0,0,0.2)' }}>
              <WR_Action_Media
                turnData={turnData}
                activeParty={activeParty}
                selectedMediaTopicKey={selectedMediaTopicKey}
                setSelectedMediaTopicKey={setSelectedMediaTopicKey}
                selectedMediaChannels={selectedMediaChannels}
                setSelectedMediaChannels={setSelectedMediaChannels}
              />
            </div>

            {/* Action 7 — Cooperation (optional) */}
            <div id="wr-section-7" style={{ background: 'rgba(255,255,255,0.03)', border: '1px solid rgba(255,255,255,0.08)', borderRadius: '16px', padding: '16px 12px', marginBottom: '24px', boxShadow: '0 4px 16px rgba(0,0,0,0.2)' }}>
              <WR_Action7_Cooperation
                turnData={turnData}
                projectDefs={projectDefs}
                onActionComplete={(data) => {
                  setCoopDone(true);
                  try {
                    localStorage.setItem(coopStorageKey, 'true');
                  } catch (_) {}
                  if (typeof handleCooperationUpdate === 'function') {
                    handleCooperationUpdate(data);
                  }
                }}
                coopDone={isCoopCompleted}
                onToggleCoopDone={(val) => {
                  setCoopDone(val);
                  try {
                    localStorage.setItem(coopStorageKey, val ? 'true' : 'false');
                  } catch (_) {}
                }}
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

            {/* Action 5 — Rewards (only shown when player has won a bid and holds rewards) */}
            {hasRewards && (
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
            )}

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

        {/* ── SINGLE NEXT / END TURN BUTTON ── */}
        <div className="wr-end-turn-footer wr-end-turn-guide">
          <button
            onClick={() => {
              if (allActionsReady && isMyTurn && !loading) {
                handleAdvanceTurn();
              } else if (activeTab === TAB_POLITICS && politicsDone) {
                setActiveTab(TAB_GOVERNANCE);
              } else if (activeTab === TAB_GOVERNANCE && governanceDone) {
                setActiveTab(TAB_ECONOMY);
              } else if (pendingAction) {
                setActiveTab(pendingAction.tab);
              }
            }}
            disabled={loading}
            style={{
              width:        '100%',
              minHeight:    '54px',
              fontSize:     '15px',
              fontWeight:   900,
              letterSpacing:'0.04em',
              borderRadius: '16px',
              border:       isNextButtonActive && isMyTurn ? 'none' : '1.5px solid rgba(255,255,255,0.16)',
              cursor:       loading ? 'wait' : 'pointer',
              touchAction:  'manipulation',
              WebkitTapHighlightColor: 'transparent',
              fontFamily:   'Montserrat,system-ui,sans-serif',
              transition:   'all 0.3s ease',
              background: isNextButtonActive && isMyTurn
                ? 'linear-gradient(135deg, #16A34A 0%, #15803d 100%)'
                : 'rgba(255,255,255,0.08)',
              color:     isNextButtonActive && isMyTurn ? '#ffffff' : '#CBD5E1',
              boxShadow: isNextButtonActive && isMyTurn ? '0 0 24px rgba(22,163,74,0.5)' : 'none',
              animation: isNextButtonActive && isMyTurn ? 'wr-pulse-green 2s ease-in-out infinite' : 'none',
            }}
          >
            {loading
              ? '⏳ Submitting…'
              : allActionsReady
                ? '⚔️  End Turn →'
                : activeTab === TAB_POLITICS && politicsDone
                  ? 'Next: Governance →'
                  : activeTab === TAB_GOVERNANCE && governanceDone
                    ? 'Next: Economy →'
                    : 'Next →'}
          </button>
        </div>
      </div>

      {/* ── INTERACTIVE SPOTLIGHT GUIDE ── */}
      <WarRoomSpotlightGuide
        key={tourKey}
        run={runGuide}
        setRun={setRunGuide}
        activeTab={activeTab}
        setActiveTab={setActiveTab}
      />
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
