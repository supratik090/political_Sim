import React, { useEffect, useRef } from 'react';
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

  // Action 8 / Assembly props
  billVote,
  setBillVote,
  whipIssued,
  setWhipIssued,
  proposedBillKey,
  setProposedBillKey,
  selectedEventOptionKey,
  setSelectedEventOptionKey,
  scenarioBills,
  scenarioEvents,

  // Accordion props
  activeAccordion,
  setActiveAccordion
}) {
  const { user } = useGameStore();
  const humanPlayerMap = turnData?.humanPlayerMap || {};
  const isMultiplayer = turnData?.isMultiplayer;
  // Find which party belongs to the logged-in user in multiplayer
  const loggedInUserId = (user?.id || user?.email)?.toLowerCase();
  const myParty = isMultiplayer
    ? turnData?.parties?.find(p => humanPlayerMap[p.id]?.toLowerCase() === loggedInUserId)
    : activeParty;
  
  const isMyTurn = !isMultiplayer || (myParty?.id === turnData?.activeHumanPartyId);

  const isCardCompleted = selectedCard !== null && (!cardRequiresTarget(selectedCard) || targetPartyId !== '');
  
  const newsItems = turnData.currentNews || [];
  const isNewsCompleted = newsItems.length === 0 || newsItems.every(news => selectedNewsReactions[news.newsKey || news.issueKey] !== undefined);
  
  const isSection3Completed = turnData.activeEventKey
    ? (selectedEventOptionKey !== '' && selectedEventOptionKey !== null && selectedEventOptionKey !== undefined)
    : (selectedIssueOptionKey === 'mock_done');
  const isBidCompleted = bidConfirmed;

  const hasRewards = turnData.activePlayerHeldRewards && turnData.activePlayerHeldRewards.length > 0;
  const selectedReward = hasRewards ? turnData.activePlayerHeldRewards.find(r => r.rewardKey === selectedRewardKey) : null;
  const rewardRequiresTarget = selectedReward?.requiresTarget;
  const isRewardTargetSelected = !rewardRequiresTarget || rewardTargetPartyId !== '';
  const isRewardCompleted = !hasRewards || selectedRewardKey === '' || (rewardConfirmed && isRewardTargetSelected);

  const hasPartyBuildingDrafts = Object.values(fundingContributions).some(v => v > 0);
  const isPartyBuildingCompleted = !hasPartyBuildingDrafts || partyBuildingConfirmed;
  const isLegislativeCompleted = !turnData.proposedBillKeyThisTurn || (billVote !== '' && billVote !== null && billVote !== undefined);
  
  const allActionsReady = isCardCompleted && isNewsCompleted && isSection3Completed && isBidCompleted && isRewardCompleted && isPartyBuildingCompleted && isLegislativeCompleted;

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



  const isSection4Completed = isBidCompleted && isRewardCompleted;
  const prevSection4Completed = useRef(isSection4Completed);
  useEffect(() => {
    if (!prevSection4Completed.current && isSection4Completed && activeAccordion === 4) {
      setActiveAccordion(5);
    }
    prevSection4Completed.current = isSection4Completed;
  }, [isSection4Completed, activeAccordion, setActiveAccordion]);

  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px', flexWrap: 'wrap', gap: '10px' }}>
        <h2 style={{ marginTop: 0, marginBottom: '0' }}>🃏 Card Selection &amp; Campaign Actions</h2>
        <div style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
          <button
            onClick={handleSkipTurn}
            disabled={loading || !isMyTurn}
            style={{
              background: 'linear-gradient(135deg, #ef4444 0%, #dc2626 100%)',
              color: '#ffffff',
              fontSize: '11px',
              fontWeight: '900',
              padding: '6px 14px',
              border: 'none',
              borderRadius: '20px',
              cursor: isMyTurn ? 'pointer' : 'not-allowed',
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

      {/* Multiplayer wait banner when it’s not this player’s turn */}
      {!isMyTurn && (
        <div style={{
          background: 'linear-gradient(135deg, var(--primary-dark) 0%, #1a2f3e 100%)',
          border: '2px solid var(--primary-border)',
          borderRadius: '14px',
          padding: '30px',
          textAlign: 'center',
          color: '#ffffff',
          marginBottom: '20px',
          boxShadow: '0 8px 25px rgba(33,60,81,0.2)'
        }}>
          <div style={{ fontSize: '36px', marginBottom: '12px' }}>⏳</div>
          <h3 style={{ margin: '0 0 8px 0', fontSize: '18px', fontWeight: 900 }}>Waiting for Opponent</h3>
          <p style={{ margin: 0, opacity: 0.75, fontSize: '14px' }}>
            It is <strong>{turnData.activeHumanPartyName || 'the other player'}’s</strong> turn to play.
            <br />Actions will be available once they submit their decisions.
          </p>
        </div>
      )}

      {/* Show action sections only when it’s this player’s turn */}
      {isMyTurn && (
        <>
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

      {/* 3. Party Management */}
      <ActionSection
        num={3}
        title="Party Management"
        isCompleted={isSection3Completed}
        activeAccordion={activeAccordion}
        setActiveAccordion={setActiveAccordion}
      >
        <Action3PartyDecision
          turnData={turnData}
          selectedIssueOptionKey={selectedIssueOptionKey}
          setSelectedIssueOptionKey={setSelectedIssueOptionKey}
          activeParty={activeParty}
          selectedEventOptionKey={selectedEventOptionKey}
          setSelectedEventOptionKey={setSelectedEventOptionKey}
          scenarioEvents={scenarioEvents}
          projectDefs={projectDefs}
        />
      </ActionSection>

      {/* 4. Bid & Play Rewards */}
      <ActionSection
        num={4}
        title="Bid & Play Rewards"
        isCompleted={isSection4Completed}
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

        <div style={{ marginTop: '20px', borderTop: '1px dashed var(--primary-border)', paddingTop: '20px' }}>
          <Action5PlayReward
            turnData={turnData}
            selectedRewardKey={selectedRewardKey}
            setSelectedRewardKey={setSelectedRewardKey}
            rewardTargetPartyId={rewardTargetPartyId}
            setRewardTargetPartyId={setRewardTargetPartyId}
            rewardConfirmed={rewardConfirmed}
            setRewardConfirmed={setRewardConfirmed}
          />
        </div>
      </ActionSection>

      {/* 5. Party Building activity */}
      <ActionSection
        num={5}
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

      {/* 6. Diplomatic Cooperation */}
      <ActionSection
        num={6}
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

      {/* 7. Legislative Assembly & State Affairs */}
      <ActionSection
        num={7}
        title={turnData.proposedBillKeyThisTurn ? "🗳️ Legislative Assembly Vote" : "🏛️ Legislative Agenda"}
        isCompleted={isLegislativeCompleted}
        isOptional={!turnData.proposedBillKeyThisTurn}
        activeAccordion={activeAccordion}
        setActiveAccordion={setActiveAccordion}
      >
        <Action8Assembly
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
      </ActionSection>

      {/* Submit Section */}
      <div style={{ marginTop: '30px', borderTop: '2px solid var(--primary-border)', paddingTop: '20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '15px' }}>
        <div>
          {!allActionsReady ? (
            <span style={{ color: '#d23f31', fontWeight: 'bold', fontSize: '13px' }}>
              ⏳ Please complete all required actions (Political Card, News Reaction, Event Decision, Bid).
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
      </>
      )}
    </div>
  );
}
