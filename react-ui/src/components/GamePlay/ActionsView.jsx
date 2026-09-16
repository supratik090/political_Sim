import React, { useState, useEffect, useRef } from 'react';
import { useGameStore } from '../../store/gameStore';
import ActionSection from './ActionSection';
import Action1CardSelection from './Action1CardSelection';
import Action2NewsReaction from './Action2NewsReaction';
import Action3PartyDecision from './Action3PartyDecision';
import Action4Bid from './Action4Bid';
import Action5PlayReward from './Action5PlayReward';
import Action6PartyBuilding from './Action6PartyBuilding';
import Action7Cooperation from './Action7Cooperation';
import Action8Assembly from './Action8Assembly';
import { cardRequiresTarget } from './gameUtils';

const TAB_POLITICS   = 'politics';
const TAB_GOVERNANCE = 'governance';
const TAB_ECONOMY    = 'economy';

export default function ActionsView({
  turnData, activeParty, loading, handleAdvanceTurn, handleSkipTurn, projectDefs,
  selectedCard, setSelectedCard, targetPartyId, setTargetPartyId,
  cardCategoryFilter, setCardCategoryFilter,
  selectedNewsReactions, setSelectedNewsReactions,
  selectedIssueOptionKey, setSelectedIssueOptionKey,
  bidAmount, setBidAmount, bidConfirmed, setBidConfirmed,
  selectedRewardKey, setSelectedRewardKey, rewardTargetPartyId, setRewardTargetPartyId,
  rewardConfirmed, setRewardConfirmed,
  projectCategoryFilter, setProjectCategoryFilter,
  fundingContributions, setFundingContributions,
  partyBuildingConfirmed, setPartyBuildingConfirmed,
  handleFundProject, handleDestroyProject, handleSetProjectTarget,
  fundedThisTurn = [], setFundedThisTurn,
  handleCooperationUpdate,
  billVote, setBillVote, whipIssued, setWhipIssued,
  proposedBillKey, setProposedBillKey,
  selectedEventOptionKey, setSelectedEventOptionKey,
  scenarioBills, scenarioEvents,
  activeAccordion, setActiveAccordion,
}) {
  const [activeTab, setActiveTab] = useState(TAB_POLITICS);
  const [polAcc, setPolAcc] = useState(1);
  const [govAcc, setGovAcc] = useState(31);
  const [ecoAcc, setEcoAcc] = useState(41);

  const { user } = useGameStore();
  const humanPlayerMap = turnData?.humanPlayerMap || {};
  const isMultiplayer  = turnData?.isMultiplayer;
  const loggedInUserId = (user?.id || user?.email)?.toLowerCase();
  const myParty = isMultiplayer
    ? turnData?.parties?.find(p => humanPlayerMap[p.id]?.toLowerCase() === loggedInUserId)
    : activeParty;
  const isMyTurn = !isMultiplayer || (myParty?.id === turnData?.activeHumanPartyId);

  const isCardCompleted = selectedCard !== null && (!cardRequiresTarget(selectedCard) || targetPartyId !== '');
  const newsItems       = turnData.currentNews || [];
  const isNewsCompleted = newsItems.length === 0 || newsItems.every(n => selectedNewsReactions[n.newsKey || n.issueKey] !== undefined);
  const isSection3Completed = turnData.activeEventKey
    ? (selectedEventOptionKey !== '' && selectedEventOptionKey !== null && selectedEventOptionKey !== undefined)
    : (selectedIssueOptionKey === 'mock_done');
  const isBidCompleted  = bidConfirmed;
  const hasRewards      = turnData.activePlayerHeldRewards && turnData.activePlayerHeldRewards.length > 0;
  const selectedReward  = hasRewards ? turnData.activePlayerHeldRewards.find(r => r.rewardKey === selectedRewardKey) : null;
  const isRewardCompleted = !hasRewards || selectedRewardKey === '' || (rewardConfirmed && (!selectedReward?.requiresTarget || rewardTargetPartyId !== ''));
  const hasPartyBuildingDrafts   = Object.values(fundingContributions).some(v => v > 0);
  const isPartyBuildingCompleted = !hasPartyBuildingDrafts || partyBuildingConfirmed;
  const isLegislativeCompleted   = !turnData.proposedBillKeyThisTurn || (billVote !== '' && billVote !== null && billVote !== undefined);
  const allActionsReady = isCardCompleted && isNewsCompleted && isSection3Completed && isBidCompleted && isRewardCompleted && isPartyBuildingCompleted && isLegislativeCompleted;

  const politicsDone    = isCardCompleted && isNewsCompleted && isLegislativeCompleted;
  const governanceDone  = isSection3Completed;
  const economyDone     = isBidCompleted && isRewardCompleted && isPartyBuildingCompleted;
  const politicsPending   = !isCardCompleted || !isNewsCompleted || (!!turnData.proposedBillKeyThisTurn && !isLegislativeCompleted);
  const governancePending = !isSection3Completed;
  const economyPending    = !isBidCompleted;
  const doneCount = [isCardCompleted, isNewsCompleted, isSection3Completed, isBidCompleted, isRewardCompleted, isPartyBuildingCompleted, isLegislativeCompleted].filter(Boolean).length;

  const prevCard = useRef(isCardCompleted);
  useEffect(() => { if (!prevCard.current && isCardCompleted && polAcc === 1) setPolAcc(2); prevCard.current = isCardCompleted; }, [isCardCompleted, polAcc]);
  const prevNews = useRef(isNewsCompleted);
  useEffect(() => { if (!prevNews.current && isNewsCompleted && polAcc === 2 && turnData.proposedBillKeyThisTurn) setPolAcc(3); prevNews.current = isNewsCompleted; }, [isNewsCompleted, polAcc]);
  const prevBid = useRef(isBidCompleted);
  useEffect(() => { if (!prevBid.current && isBidCompleted && ecoAcc === 41 && hasRewards) setEcoAcc(42); prevBid.current = isBidCompleted; }, [isBidCompleted, ecoAcc, hasRewards]);

  const prevPolDone = useRef(politicsDone);
  useEffect(() => {
    if (!prevPolDone.current && politicsDone && activeTab === TAB_POLITICS) {
      if (!governanceDone) setActiveTab(TAB_GOVERNANCE); else if (!economyDone) setActiveTab(TAB_ECONOMY);
    }
    prevPolDone.current = politicsDone;
  }, [politicsDone]);
  const prevGovDone = useRef(governanceDone);
  useEffect(() => {
    if (!prevGovDone.current && governanceDone && activeTab === TAB_GOVERNANCE && !economyDone) setActiveTab(TAB_ECONOMY);
    prevGovDone.current = governanceDone;
  }, [governanceDone]);

  useEffect(() => {
    if (!activeAccordion) return;
    if (activeAccordion === 1 || activeAccordion === 2 || activeAccordion === 8 || activeAccordion === 3) {
      setActiveTab(TAB_POLITICS);
      if (activeAccordion === 8) setPolAcc(3);
      else setPolAcc(activeAccordion);
    } else if (activeAccordion === 7 || activeAccordion === 31 || activeAccordion === 32) {
      setActiveTab(TAB_GOVERNANCE);
      if (activeAccordion === 7) setGovAcc(32);
      else setGovAcc(activeAccordion);
    } else if (activeAccordion === 4 || activeAccordion === 5 || activeAccordion === 6 || activeAccordion === 41 || activeAccordion === 42 || activeAccordion === 43) {
      setActiveTab(TAB_ECONOMY);
      if (activeAccordion === 4) setEcoAcc(41);
      else if (activeAccordion === 5) setEcoAcc(42);
      else if (activeAccordion === 6) setEcoAcc(43);
      else setEcoAcc(activeAccordion);
    }
  }, [activeAccordion]);

  function TabBtn({ id, icon, label, isDone, hasPending }) {
    const isActive = activeTab === id;
    const dot = isDone ? '#16A34A' : hasPending ? '#f59e0b' : '#94a3b8';
    return (
      <button onClick={() => setActiveTab(id)} style={{
        flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '4px',
        padding: '10px 6px 12px', minHeight: '60px', position: 'relative',
        background: isActive ? 'var(--party-primary-color, var(--primary-dark))' : 'transparent',
        color: isActive ? '#ffffff' : 'var(--primary-dark)',
        border: 'none', borderRadius: 0,
        borderBottom: isActive ? '3px solid var(--selected-highlight)' : '3px solid transparent',
        fontWeight: isActive ? 800 : 600, fontSize: '11px', letterSpacing: '0.03em',
        textTransform: 'uppercase', cursor: 'pointer', transition: 'all 0.18s ease',
        boxShadow: 'none', WebkitTapHighlightColor: 'transparent', touchAction: 'manipulation',
      }}>
        <span style={{ position: 'absolute', top: '7px', right: '7px', width: '8px', height: '8px', borderRadius: '50%', background: dot, boxShadow: isDone ? `0 0 5px ${dot}` : 'none' }} />
        <span style={{ fontSize: '20px', lineHeight: 1 }}>{icon}</span>
        <span>{label}</span>
      </button>
    );
  }

  function SummaryChip({ label, value, done }) {
    return (
      <div style={{
        display: 'inline-flex', alignItems: 'center', gap: '4px', flexShrink: 0,
        background: done ? 'rgba(22,163,74,0.10)' : 'rgba(245,158,11,0.10)',
        border: `1px solid ${done ? 'rgba(22,163,74,0.3)' : 'rgba(245,158,11,0.3)'}`,
        borderRadius: '20px', padding: '4px 10px', fontSize: '11px', fontWeight: 700,
        color: done ? '#16A34A' : '#92400e', whiteSpace: 'nowrap',
      }}>
        {done ? '✅' : '⚠️'} {label}: <span style={{ fontWeight: 400, marginLeft: 2 }}>{value}</span>
      </div>
    );
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 0 }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '16px', flexWrap: 'wrap', gap: '10px' }}>
        <h2 style={{ margin: 0, fontSize: '17px', fontWeight: 900, color: 'var(--primary-dark)' }}>🃏 Campaign Actions</h2>
        <div style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
          <div style={{ fontSize: '13px', background: 'var(--primary-dark)', padding: '5px 14px', borderRadius: '20px', color: '#fff', fontWeight: 700 }}>
            📅 Month {turnData.turnNumber} / 60
          </div>
        </div>
      </div>

      {!isMyTurn && (
        <div style={{ background: 'linear-gradient(135deg, var(--primary-dark) 0%, #1a2f3e 100%)', border: '2px solid var(--primary-border)', borderRadius: '14px', padding: '30px', textAlign: 'center', color: '#ffffff', marginBottom: '20px', boxShadow: '0 8px 25px rgba(33,60,81,0.2)' }}>
          <div style={{ fontSize: '36px', marginBottom: '12px' }}>⏳</div>
          <h3 style={{ margin: '0 0 8px 0', fontSize: '18px', fontWeight: 900 }}>Waiting for Opponent</h3>
          <p style={{ margin: 0, opacity: 0.75, fontSize: '14px' }}>
            It is <strong>{turnData.activeHumanPartyName || 'the other player'}'s</strong> turn to play.<br />
            Actions will be available once they submit their decisions.
          </p>
        </div>
      )}

      {isMyTurn && (<>
        <div style={{ display: 'flex', background: 'rgba(var(--party-primary-color-rgb,26,52,72),0.05)', borderRadius: '12px 12px 0 0', border: '1.5px solid var(--card-border)', borderBottom: 'none', overflow: 'hidden' }}>
          <TabBtn id={TAB_POLITICS}   icon="🗳️" label="Politics"   isDone={politicsDone}   hasPending={politicsPending}   />
          <div style={{ width: '1px', background: 'var(--card-border)', flexShrink: 0 }} />
          <TabBtn id={TAB_GOVERNANCE} icon="🏛️" label="Governance" isDone={governanceDone} hasPending={governancePending} />
          <div style={{ width: '1px', background: 'var(--card-border)', flexShrink: 0 }} />
          <TabBtn id={TAB_ECONOMY}    icon="💰" label="Economy"    isDone={economyDone}    hasPending={economyPending}    />
        </div>

        <div style={{ background: 'rgba(26,52,72,0.03)', border: '1.5px solid var(--card-border)', borderTop: 'none', borderBottom: 'none', padding: '7px 12px', display: 'flex', gap: '7px', overflowX: 'auto', scrollbarWidth: 'none', flexWrap: 'nowrap' }}>
          {activeTab !== TAB_POLITICS && (<>
            <SummaryChip label="Card" value={selectedCard ? selectedCard.name : 'Not chosen'} done={isCardCompleted} />
            <SummaryChip label="News" value={isNewsCompleted ? `${newsItems.length} done` : `${newsItems.length - Object.keys(selectedNewsReactions).length} left`} done={isNewsCompleted} />
          </>)}
          {activeTab !== TAB_GOVERNANCE && (
            <SummaryChip label="Govt" value={isSection3Completed ? 'Done' : 'Pending'} done={isSection3Completed} />
          )}
          {activeTab !== TAB_ECONOMY && (<>
            <SummaryChip label="Bid" value={isBidCompleted ? `${bidAmount} staked` : 'Not locked'} done={isBidCompleted} />
            {hasRewards && <SummaryChip label="Reward" value={isRewardCompleted ? 'Set' : 'Pending'} done={isRewardCompleted} />}
          </>)}
        </div>

        <div style={{ border: '1.5px solid var(--card-border)', borderTop: 'none', borderRadius: '0 0 12px 12px', background: '#ffffff', minHeight: '300px', padding: '16px 12px 4px 12px' }}>
          {activeTab === TAB_POLITICS && (
            <div>
              <ActionSection num={1} title="Political Card" isCompleted={isCardCompleted} activeAccordion={polAcc} setActiveAccordion={setPolAcc}>
                <Action1CardSelection turnData={turnData} selectedCard={selectedCard} setSelectedCard={setSelectedCard} targetPartyId={targetPartyId} setTargetPartyId={setTargetPartyId} cardCategoryFilter={cardCategoryFilter} setCardCategoryFilter={setCardCategoryFilter} />
              </ActionSection>
              <ActionSection num={2} title="News Reaction" isCompleted={isNewsCompleted} activeAccordion={polAcc} setActiveAccordion={setPolAcc}>
                <Action2NewsReaction turnData={turnData} selectedNewsReactions={selectedNewsReactions} setSelectedNewsReactions={setSelectedNewsReactions} />
              </ActionSection>
              <ActionSection num={3} title={turnData.proposedBillKeyThisTurn ? '🗳️ Assembly Vote' : '🏛️ Legislative Agenda'} isCompleted={isLegislativeCompleted} isOptional={!turnData.proposedBillKeyThisTurn} activeAccordion={polAcc} setActiveAccordion={setPolAcc}>
                <Action8Assembly turnData={turnData} activeParty={activeParty} billVote={billVote} setBillVote={setBillVote} whipIssued={whipIssued} setWhipIssued={setWhipIssued} proposedBillKey={proposedBillKey} setProposedBillKey={setProposedBillKey} selectedEventOptionKey={selectedEventOptionKey} setSelectedEventOptionKey={setSelectedEventOptionKey} scenarioBills={scenarioBills} scenarioEvents={scenarioEvents} />
              </ActionSection>
            </div>
          )}

          {activeTab === TAB_GOVERNANCE && (
            <div>
              <ActionSection num={31} title="Party Management" isCompleted={isSection3Completed} activeAccordion={govAcc} setActiveAccordion={setGovAcc}>
                <Action3PartyDecision turnData={turnData} selectedIssueOptionKey={selectedIssueOptionKey} setSelectedIssueOptionKey={setSelectedIssueOptionKey} activeParty={activeParty} selectedEventOptionKey={selectedEventOptionKey} setSelectedEventOptionKey={setSelectedEventOptionKey} scenarioEvents={scenarioEvents} projectDefs={projectDefs} />
              </ActionSection>
              <ActionSection num={32} title="Diplomatic Cooperation" isCompleted={true} isOptional={true} activeAccordion={govAcc} setActiveAccordion={setGovAcc}>
                <Action7Cooperation turnData={turnData} projectDefs={projectDefs} onActionComplete={handleCooperationUpdate} />
              </ActionSection>
            </div>
          )}

          {activeTab === TAB_ECONOMY && (
            <div>
              <ActionSection num={41} title="Competitive Bid" isCompleted={isBidCompleted} activeAccordion={ecoAcc} setActiveAccordion={setEcoAcc}>
                <Action4Bid turnData={turnData} activeParty={activeParty} bidAmount={bidAmount} setBidAmount={setBidAmount} bidConfirmed={bidConfirmed} setBidConfirmed={setBidConfirmed} />
              </ActionSection>
              <ActionSection num={42} title="Play Rewards" isCompleted={isRewardCompleted} isOptional={!hasRewards} activeAccordion={ecoAcc} setActiveAccordion={setEcoAcc}>
                <Action5PlayReward turnData={turnData} selectedRewardKey={selectedRewardKey} setSelectedRewardKey={setSelectedRewardKey} rewardTargetPartyId={rewardTargetPartyId} setRewardTargetPartyId={setRewardTargetPartyId} rewardConfirmed={rewardConfirmed} setRewardConfirmed={setRewardConfirmed} />
              </ActionSection>
              <ActionSection num={43} title="Party Building" isCompleted={isPartyBuildingCompleted} isOptional={true} activeAccordion={ecoAcc} setActiveAccordion={setEcoAcc}>
                <Action6PartyBuilding turnData={turnData} activeParty={activeParty} projectDefs={projectDefs} projectCategoryFilter={projectCategoryFilter} setProjectCategoryFilter={setProjectCategoryFilter} fundingContributions={fundingContributions} setFundingContributions={setFundingContributions} partyBuildingConfirmed={partyBuildingConfirmed} setPartyBuildingConfirmed={setPartyBuildingConfirmed} handleFundProject={handleFundProject} handleDestroyProject={handleDestroyProject} handleSetProjectTarget={handleSetProjectTarget} fundedThisTurn={fundedThisTurn} setFundedThisTurn={setFundedThisTurn} />
              </ActionSection>
            </div>
          )}
        </div>

        <div style={{ marginTop: '14px', background: 'rgba(26,52,72,0.04)', border: '1.5px solid var(--card-border)', borderRadius: '12px', padding: '14px 16px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '7px' }}>
            <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-secondary)', textTransform: 'uppercase', letterSpacing: '0.04em' }}>Turn Progress</span>
            <span style={{ fontSize: '12px', fontWeight: 700, color: allActionsReady ? '#16A34A' : 'var(--text-secondary)' }}>{doneCount} / 7 done</span>
          </div>
          <div style={{ width: '100%', height: '6px', background: 'rgba(26,52,72,0.12)', borderRadius: '3px', overflow: 'hidden', marginBottom: '12px' }}>
            <div style={{ height: '100%', width: `${(doneCount / 7) * 100}%`, background: allActionsReady ? '#16A34A' : 'var(--party-primary-color, var(--primary-dark))', borderRadius: '3px', transition: 'width 0.4s ease' }} />
          </div>
          <div style={{ marginBottom: '10px', fontSize: '14px', fontWeight: 700, color: allActionsReady ? '#16A34A' : '#d23f31' }}>
            {allActionsReady ? '🎉 All decisions locked — ready to submit!' : '⏳ Complete required actions in all tabs.'}
          </div>
          <button onClick={handleAdvanceTurn} disabled={!allActionsReady || loading} className="btn-primary-cta"
            style={{ backgroundColor: allActionsReady ? '#16A34A' : '#3A5469', color: '#ffffff', cursor: allActionsReady ? 'pointer' : 'not-allowed', border: 'none' }}>
            {loading ? '⏳ Advancing Turn...' : 'End Turn — Submit Decisions ➔'}
          </button>
        </div>
      </>)}
    </div>
  );
}
