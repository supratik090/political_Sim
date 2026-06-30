import React, { useEffect, useRef } from 'react';
import ActionSection from './ActionSection';
import Action1CardSelection from './Action1CardSelection';
import Action2NewsReaction from './Action2NewsReaction';
import Action3PartyDecision from './Action3PartyDecision';
import Action4Bid from './Action4Bid';
import Action5PlayReward from './Action5PlayReward';
import Action6PartyBuilding from './Action6PartyBuilding';
import Action7Cooperation from './Action7Cooperation';
import { cardRequiresTarget } from './gameUtils';

export default function ActionsView({
  turnData,
  activeParty,
  loading,
  handleAdvanceTurn,
  handleSkipTurn,
  projectDefs,
  
  // Action 1 props
  selectedCard,
  setSelectedCard,
  targetPartyId,
  setTargetPartyId,
  cardCategoryFilter,
  setCardCategoryFilter,

  // Action 2 props
  selectedNewsReactions,
  setSelectedNewsReactions,

  // Action 3 props
  selectedIssueOptionKey,
  setSelectedIssueOptionKey,

  // Action 4 props
  bidAmount,
  setBidAmount,
  bidConfirmed,
  setBidConfirmed,

  // Action 5 props
  selectedRewardKey,
  setSelectedRewardKey,
  rewardTargetPartyId,
  setRewardTargetPartyId,
  rewardConfirmed,
  setRewardConfirmed,

  // Action 6 props
  projectCategoryFilter,
  setProjectCategoryFilter,
  fundingContributions,
  setFundingContributions,
  partyBuildingConfirmed,
  setPartyBuildingConfirmed,
  handleFundProject,
  handleDestroyProject,
  handleSetProjectTarget,
  fundedThisTurn = [],
  setFundedThisTurn,

  // Action 7 props
  handleCooperationUpdate,

  // Accordion props
  activeAccordion,
  setActiveAccordion
}) {
  const isCardCompleted = selectedCard !== null && (!cardRequiresTarget(selectedCard) || targetPartyId !== '');
  
  const newsItems = turnData.currentNews || [];
  const isNewsCompleted = newsItems.length === 0 || newsItems.every(news => selectedNewsReactions[news.newsKey || news.issueKey] !== undefined);
  
  const isIssueCompleted = !turnData.currentIssue || selectedIssueOptionKey !== '';
  const isBidCompleted = bidConfirmed;

  const hasRewards = turnData.activePlayerHeldRewards && turnData.activePlayerHeldRewards.length > 0;
  const selectedReward = hasRewards ? turnData.activePlayerHeldRewards.find(r => r.rewardKey === selectedRewardKey) : null;
  const rewardRequiresTarget = selectedReward?.requiresTarget;
  const isRewardTargetSelected = !rewardRequiresTarget || rewardTargetPartyId !== '';
  const isRewardCompleted = !hasRewards || selectedRewardKey === '' || (rewardConfirmed && isRewardTargetSelected);

  const hasPartyBuildingDrafts = Object.values(fundingContributions).some(v => v > 0);
  const isPartyBuildingCompleted = !hasPartyBuildingDrafts || partyBuildingConfirmed;
  
  const allActionsReady = isCardCompleted && isNewsCompleted && isIssueCompleted && isBidCompleted && isRewardCompleted && isPartyBuildingCompleted;

  const prevCardCompleted = useRef(isCardCompleted);
  useEffect(() => {
    if (!prevCardCompleted.current && isCardCompleted && activeAccordion === 1) {
      setActiveAccordion(2);
    }
    prevCardCompleted.current = isCardCompleted;
  }, [isCardCompleted, activeAccordion, setActiveAccordion]);

  const prevNewsCompleted = useRef(isNewsCompleted);
  useEffect(() => {
    if (!prevNewsCompleted.current && isNewsCompleted && activeAccordion === 2) {
      setActiveAccordion(3);
    }
    prevNewsCompleted.current = isNewsCompleted;
  }, [isNewsCompleted, activeAccordion, setActiveAccordion]);

  const prevIssueCompleted = useRef(isIssueCompleted);
  useEffect(() => {
    if (!prevIssueCompleted.current && isIssueCompleted && activeAccordion === 3) {
      setActiveAccordion(4);
    }
    prevIssueCompleted.current = isIssueCompleted;
  }, [isIssueCompleted, activeAccordion, setActiveAccordion]);

  const prevBidCompleted = useRef(isBidCompleted);
  useEffect(() => {
    if (!prevBidCompleted.current && isBidCompleted && activeAccordion === 4) {
      setActiveAccordion(5);
    }
    prevBidCompleted.current = isBidCompleted;
  }, [isBidCompleted, activeAccordion, setActiveAccordion]);

  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px', flexWrap: 'wrap', gap: '10px' }}>
        <h2 style={{ marginTop: 0, marginBottom: '0' }}>🃏 Card Selection &amp; Campaign Actions</h2>
        <div style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
          <button 
            onClick={handleSkipTurn}
            disabled={loading}
            style={{
              background: 'linear-gradient(135deg, #ef4444 0%, #dc2626 100%)',
              color: '#ffffff',
              fontSize: '11px',
              fontWeight: '900',
              padding: '6px 14px',
              border: 'none',
              borderRadius: '20px',
              cursor: 'pointer',
              textTransform: 'uppercase',
              boxShadow: '0 4px 10px rgba(239, 68, 68, 0.2)',
              transition: 'all 0.2s',
              fontFamily: "system-ui, -apple-system, sans-serif"
            }}
            onMouseEnter={(e) => e.currentTarget.style.transform = 'translateY(-1px)'}
            onMouseLeave={(e) => e.currentTarget.style.transform = 'translateY(0)'}
          >
            ⏭️ Skip Turn
          </button>
          <div style={{ fontSize: '12px', background: 'var(--primary-border)', padding: '5px 12px', borderRadius: '20px', color: '#fff', fontWeight: 'bold' }}>
            Month {turnData.turnNumber} / 60
          </div>
        </div>
      </div>

      {/* 1. Political Card Selection */}
      <ActionSection 
        num={1} 
        title="Political Card Selection" 
        isCompleted={isCardCompleted}
        activeAccordion={activeAccordion}
        setActiveAccordion={setActiveAccordion}
      >
        <Action1CardSelection
          turnData={turnData}
          selectedCard={selectedCard}
          setSelectedCard={setSelectedCard}
          targetPartyId={targetPartyId}
          setTargetPartyId={setTargetPartyId}
          cardCategoryFilter={cardCategoryFilter}
          setCardCategoryFilter={setCardCategoryFilter}
        />
      </ActionSection>

      {/* 2. News Reaction */}
      <ActionSection 
        num={2} 
        title="News Reaction" 
        isCompleted={isNewsCompleted}
        activeAccordion={activeAccordion}
        setActiveAccordion={setActiveAccordion}
      >
        <Action2NewsReaction
          turnData={turnData}
          selectedNewsReactions={selectedNewsReactions}
          setSelectedNewsReactions={setSelectedNewsReactions}
        />
      </ActionSection>

      {/* 3. Party News Reaction */}
      <ActionSection 
        num={3} 
        title="Party News Reaction" 
        isCompleted={isIssueCompleted}
        activeAccordion={activeAccordion}
        setActiveAccordion={setActiveAccordion}
      >
        <Action3PartyDecision
          turnData={turnData}
          selectedIssueOptionKey={selectedIssueOptionKey}
          setSelectedIssueOptionKey={setSelectedIssueOptionKey}
        />
      </ActionSection>

      {/* 4. Bid for Reward */}
      <ActionSection 
        num={4} 
        title="Bid for Reward" 
        isCompleted={isBidCompleted}
        activeAccordion={activeAccordion}
        setActiveAccordion={setActiveAccordion}
      >
        <Action4Bid
          turnData={turnData}
          activeParty={activeParty}
          bidAmount={bidAmount}
          setBidAmount={setBidAmount}
          bidConfirmed={bidConfirmed}
          setBidConfirmed={setBidConfirmed}
        />
      </ActionSection>

      {/* 5. Play Reward */}
      <ActionSection 
        num={5} 
        title="Play Reward" 
        isCompleted={isRewardCompleted} 
        isOptional={true}
        activeAccordion={activeAccordion}
        setActiveAccordion={setActiveAccordion}
      >
        <Action5PlayReward
          turnData={turnData}
          selectedRewardKey={selectedRewardKey}
          setSelectedRewardKey={setSelectedRewardKey}
          rewardTargetPartyId={rewardTargetPartyId}
          setRewardTargetPartyId={setRewardTargetPartyId}
          rewardConfirmed={rewardConfirmed}
          setRewardConfirmed={setRewardConfirmed}
        />
      </ActionSection>

      {/* 6. Party Building activity */}
      <ActionSection 
        num={6} 
        title="Party Building activity" 
        isCompleted={isPartyBuildingCompleted} 
        isOptional={true}
        activeAccordion={activeAccordion}
        setActiveAccordion={setActiveAccordion}
      >
        <Action6PartyBuilding
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
          setFundedThisTurn={setFundedThisTurn}
        />
      </ActionSection>

      {/* 7. Diplomatic Cooperation */}
      <ActionSection 
        num={7} 
        title="Diplomatic Cooperation" 
        isCompleted={true} 
        isOptional={true}
        activeAccordion={activeAccordion}
        setActiveAccordion={setActiveAccordion}
      >
        <Action7Cooperation
          turnData={turnData}
          projectDefs={projectDefs}
          onActionComplete={handleCooperationUpdate}
        />
      </ActionSection>

      {/* Submit Section */}
      <div style={{ marginTop: '30px', borderTop: '2px solid var(--primary-border)', paddingTop: '20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '15px' }}>
        <div>
          {!allActionsReady ? (
            <span style={{ color: '#d23f31', fontWeight: 'bold', fontSize: '13px' }}>
              ⏳ Please complete all required actions (Political Card, News Reaction, Party Decision, Bid).
            </span>
          ) : (
            <span style={{ color: '#22c55e', fontWeight: 'bold', fontSize: '13px' }}>
              🎉 All required decisions locked! Ready to proceed.
            </span>
          )}
        </div>
        <button 
          onClick={handleAdvanceTurn}
          disabled={!allActionsReady || loading}
          style={{
            backgroundColor: allActionsReady ? '#22c55e' : 'gray',
            borderColor: allActionsReady ? '#22c55e' : 'gray',
            color: '#ffffff',
            padding: '12px 30px',
            fontSize: '15px',
            fontWeight: 'bold',
            cursor: allActionsReady ? 'pointer' : 'not-allowed',
            border: 'none',
            borderRadius: '8px'
          }}
        >
          {loading ? 'Advancing Turn...' : 'End Turn (Submit Decisions) ➔'}
        </button>
      </div>
    </div>
  );
}
