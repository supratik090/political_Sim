import React, { useState, useEffect } from 'react';
import { useGameStore } from '../../store/gameStore';
import { fetchTurnView, advanceTurn, fundProject, setProjectTarget } from '../../api/apiClient';
import { getPartyColor, cardRequiresTarget } from './gameUtils';
import StatsView from './StatsView';
import ActionsView from './ActionsView';

export default function GamePlayBoard() {
  const [activeView, setActiveView] = useState('INFO');
  const { activeGameId, turnData, setTurnData } = useGameStore();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [commentaryExpanded, setCommentaryExpanded] = useState(false);
  const [commentaryFilter, setCommentaryFilter] = useState('ALL');

  // Real 6 actions states
  const [selectedCard, setSelectedCard] = useState(null);
  const [targetPartyId, setTargetPartyId] = useState('');
  const [selectedNewsReactions, setSelectedNewsReactions] = useState({});
  const [selectedIssueOptionKey, setSelectedIssueOptionKey] = useState('');
  const [bidAmount, setBidAmount] = useState(0);
  const [bidConfirmed, setBidConfirmed] = useState(false);
  const [selectedRewardKey, setSelectedRewardKey] = useState('');
  const [rewardTargetPartyId, setRewardTargetPartyId] = useState('');
  const [activeAccordion, setActiveAccordion] = useState(1); // 1-6
  const [rewardConfirmed, setRewardConfirmed] = useState(false);
  const [partyBuildingConfirmed, setPartyBuildingConfirmed] = useState(false);
  const [cardCategoryFilter, setCardCategoryFilter] = useState('agitation_movement');

  // Project building draft states
  const [projectCategoryFilter, setProjectCategoryFilter] = useState('BUILD');
  const [draftProjectKeys, setDraftProjectKeys] = useState([]);
  const [fundingContributions, setFundingContributions] = useState({});

  const activeParty = turnData?.parties?.find(p => p.id === turnData.activeHumanPartyId) || turnData?.parties?.find(p => p.playerControlled);
  const playerPartyName = turnData?.activeHumanPartyName || activeParty?.name;
  const playerPartyColor = getPartyColor(activeParty);

  const resetLocalStates = () => {
    setSelectedCard(null);
    setTargetPartyId('');
    setSelectedNewsReactions({});
    setSelectedIssueOptionKey('');
    setBidAmount(0);
    setBidConfirmed(false);
    setSelectedRewardKey('');
    setRewardTargetPartyId('');
    setFundingContributions({});
    setDraftProjectKeys([]);
    setRewardConfirmed(false);
    setPartyBuildingConfirmed(false);
    setCardCategoryFilter('agitation_movement');
  };

  const loadTurnData = async (isNewTurn = false) => {
    if (!activeGameId) return;
    setLoading(true);
    setError('');
    try {
      const data = await fetchTurnView(activeGameId);
      setTurnData(data);
      if (isNewTurn) {
        resetLocalStates();
        setActiveAccordion(1);
      }
    } catch (err) {
      console.error(err);
      setError('Failed to fetch campaign stats.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadTurnData(true);
  }, [activeGameId]);

  const handleAdvanceTurn = async () => {
    setLoading(true);
    setError('');
    try {
      const payload = {
        selectedCardKey: selectedCard?.cardKey,
        targetPartyId: selectedCard && cardRequiresTarget(selectedCard) ? targetPartyId : null,
        selectedNewsReactions: selectedNewsReactions,
        selectedIssueOptionKey: turnData.currentIssue ? selectedIssueOptionKey : 'routine_maintenance',
        bid: bidAmount,
        selectedRewardKey: selectedRewardKey || null,
        rewardTargetPartyId: selectedRewardKey && rewardTargetPartyId ? rewardTargetPartyId : null
      };

      const result = await advanceTurn(activeGameId, payload);
      setTurnData(result);
      resetLocalStates();
      setActiveView('INFO');
      setActiveAccordion(1);
    } catch (err) {
      console.error(err);
      setError(err.message || 'Failed to advance turn.');
    } finally {
      setLoading(false);
    }
  };

  const handleSkipTurn = async () => {
    if (!window.confirm("Are you sure you want to skip this turn? Your party will pass its card play, place a 0 bid, and submit routine/default responses to news and issues.")) {
      return;
    }
    
    setLoading(true);
    setError('');
    try {
      const defaultReactions = {};
      (turnData.currentNews || []).forEach(news => {
        const newsKey = news.newsKey || news.issueKey;
        const firstOpt = news.reactionOptions?.[0] || news.options?.[0];
        if (firstOpt) {
          defaultReactions[newsKey] = firstOpt.reactionKey || firstOpt.optionKey;
        }
      });

      let defaultIssueOpt = 'routine_maintenance';
      if (turnData.currentIssue) {
        const firstOpt = turnData.currentIssue.reactionOptions?.[0] || turnData.currentIssue.options?.[0];
        if (firstOpt) {
          defaultIssueOpt = firstOpt.reactionKey || firstOpt.optionKey;
        }
      }

      const payload = {
        selectedCardKey: 'no_card',
        targetPartyId: null,
        selectedNewsReactions: defaultReactions,
        selectedIssueOptionKey: defaultIssueOpt,
        bid: 0,
        selectedRewardKey: null,
        rewardTargetPartyId: null
      };

      const result = await advanceTurn(activeGameId, payload);
      setTurnData(result);
      resetLocalStates();
      setActiveView('INFO');
      setActiveAccordion(1);
    } catch (err) {
      console.error(err);
      setError(err.message || 'Failed to skip turn.');
    } finally {
      setLoading(false);
    }
  };

  const handleFundProject = async (projectKey, progress) => {
    setLoading(true);
    setError('');
    try {
      const data = await fundProject(activeGameId, activeParty.id, projectKey, progress);
      setTurnData(data);
      setFundingContributions(prev => {
        const next = { ...prev };
        delete next[projectKey];
        return next;
      });
    } catch (err) {
      console.error(err);
      setError(err.message || 'Failed to fund project.');
    } finally {
      setLoading(false);
    }
  };

  const handleSetProjectTarget = async (projectKey, targetId) => {
    setLoading(true);
    setError('');
    try {
      const data = await setProjectTarget(activeGameId, activeParty.id, projectKey, targetId);
      setTurnData(data);
    } catch (err) {
      console.error(err);
      setError(err.message || 'Failed to set project target.');
    } finally {
      setLoading(false);
    }
  };

  // Map: winning a 2001-era scenario key → which 2006 campaign it unlocks
  const NEXT_CAMPAIGN_MAP = {
    'west_bengal_2000':    { key: 'west_bengal_2006',    name: 'West Bengal 2006' },
    'maharashtra_2001':    { key: 'maharashtra_2006',    name: 'Maharashtra 2006' },
    'uttar_pradesh_2001':  { key: 'uttar_pradesh_2006',  name: 'Uttar Pradesh 2006' },
    'tamil_nadu_2001':     { key: 'tamil_nadu_2006',     name: 'Tamil Nadu 2006' },
    'rajasthan_2001':      { key: 'rajasthan_2006',      name: 'Rajasthan 2006' },
    'bihar_2001':          { key: 'bihar_2006',          name: 'Bihar 2006' },
    'goa_2001':            { key: 'goa_2006',            name: 'Goa 2006' },
    'delhi_2001':          { key: 'delhi_2006',          name: 'Delhi 2006' },
    'andhra_pradesh_2001': { key: 'andhra_pradesh_2006', name: 'Andhra Pradesh 2006' },
    'kerala_2001':         { key: 'kerala_2006',         name: 'Kerala 2006' },
  };

  if (turnData && (turnData.status === 'VICTORY' || turnData.status === 'DEFEAT' || turnData.status === 'GAME_OVER' || turnData.status === 'FORFEITED')) {
    const isVictory = turnData.status === 'VICTORY';
    const bgGradient = isVictory 
      ? 'linear-gradient(135deg, #15803d 0%, #166534 100%)' 
      : 'linear-gradient(135deg, #991b1b 0%, #7f1d1d 100%)';
    const emoji = isVictory ? '🏆' : '💀';
    const titleText = isVictory ? 'CAMPAIGN VICTORY!' : 'CAMPAIGN FAILED';

    // Check if this victory unlocks a 2006 campaign
    const unlockedNext = isVictory ? NEXT_CAMPAIGN_MAP[turnData.scenarioKey] : null;

    return (
      <div style={{
        minHeight: '80vh',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '40px 20px',
        color: '#ffffff',
        background: bgGradient,
        borderRadius: '24px',
        border: '4px solid #ffffff',
        boxShadow: '0 20px 50px rgba(0,0,0,0.3)',
        textAlign: 'center',
        fontFamily: "'Montserrat', sans-serif"
      }}>
        <span style={{ fontSize: '96px', marginBottom: '20px', display: 'block', filter: 'drop-shadow(0 10px 15px rgba(0,0,0,0.3))' }}>
          {emoji}
        </span>
        <h1 style={{ fontSize: '48px', fontWeight: 900, margin: '0 0 10px 0', letterSpacing: '0.05em', textShadow: '0 4px 10px rgba(0,0,0,0.4)' }}>
          {titleText}
        </h1>
        <p style={{ fontSize: '18px', opacity: 0.9, maxWidth: '600px', margin: '0 auto 30px auto', lineHeight: 1.6 }}>
          {turnData.lastResults?.[0] || 'The campaign has concluded.'}
        </p>

        {/* Next Campaign Unlocked Banner — shown only on victory of a 2001-era scenario */}
        {unlockedNext && (
          <div style={{
            background: 'rgba(255,255,255,0.15)',
            border: '2px solid rgba(255,255,255,0.6)',
            borderRadius: '16px',
            padding: '18px 30px',
            marginBottom: '28px',
            maxWidth: '500px',
            width: '100%',
            backdropFilter: 'blur(8px)',
            animation: 'pulse 2s ease-in-out infinite',
          }}>
            <div style={{ fontSize: '28px', marginBottom: '6px' }}>🎊</div>
            <div style={{ fontSize: '16px', fontWeight: 900, letterSpacing: '0.05em', textTransform: 'uppercase', marginBottom: '4px' }}>
              Next Campaign Unlocked!
            </div>
            <div style={{ fontSize: '14px', opacity: 0.95, fontWeight: 600 }}>
              <span style={{ fontWeight: 900, fontSize: '16px' }}>{unlockedNext.name}</span> is now available on the Dashboard.
            </div>
          </div>
        )}

        {/* Voting Results Board */}
        <div className="unified-card" style={{
          width: '100%',
          maxWidth: '500px',
          background: 'rgba(255, 255, 255, 0.95)',
          color: '#213C51',
          padding: '25px',
          borderRadius: '16px',
          border: 'none',
          boxShadow: '0 10px 30px rgba(0,0,0,0.2)',
          marginBottom: '35px',
          textAlign: 'left'
        }}>
          <h3 style={{ margin: '0 0 15px 0', textAlign: 'center', fontWeight: 800, textTransform: 'uppercase', fontSize: '15px', letterSpacing: '0.05em', borderBottom: '2px solid rgba(33,60,81,0.1)', paddingBottom: '10px' }}>
            🗳️ Final Election Results
          </h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
            {turnData.parties?.map(party => {
              const support = party.stats?.publicSupport || 0;
              return (
                <div key={party.id}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '14px', fontWeight: 'bold', marginBottom: '6px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <span style={{ width: '12px', height: '12px', borderRadius: '50%', backgroundColor: getPartyColor(party), display: 'inline-block', border: '1px solid rgba(0,0,0,0.2)' }} />
                      <span>{party.name} {party.playerControlled && '(You)'}</span>
                    </div>
                    <span>{support}%</span>
                  </div>
                  {/* Progress Bar */}
                  <div style={{ width: '100%', height: '12px', background: 'rgba(33,60,81,0.1)', borderRadius: '6px', overflow: 'hidden' }}>
                    <div style={{ width: `${support}%`, height: '100%', backgroundColor: getPartyColor(party), borderRadius: '6px' }} />
                  </div>
                </div>
              );
            })}
            {/* Undecided */}
            {turnData.publicState && (
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '14px', fontWeight: 'bold', marginBottom: '6px', opacity: 0.8 }}>
                  <span>Undecided Voters</span>
                  <span>{turnData.publicState.undecidedSupport}%</span>
                </div>
                <div style={{ width: '100%', height: '12px', background: 'rgba(33,60,81,0.1)', borderRadius: '6px', overflow: 'hidden' }}>
                  <div style={{ width: `${turnData.publicState.undecidedSupport}%`, height: '100%', backgroundColor: '#94a3b8', borderRadius: '6px' }} />
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Action Button */}
        <button 
          onClick={() => {
            const { setScreen, setActiveGame } = useGameStore.getState();
            setScreen('HOME');
            setActiveGame(null);
          }}
          style={{
            background: '#ffffff',
            color: isVictory ? '#166534' : '#7f1d1d',
            fontSize: '16px',
            fontWeight: '900',
            padding: '16px 40px',
            border: 'none',
            borderRadius: '12px',
            boxShadow: '0 8px 25px rgba(0,0,0,0.2)',
            cursor: 'pointer',
            transition: 'all 0.2s ease'
          }}
          onMouseEnter={(e) => {
            e.currentTarget.style.transform = 'translateY(-3px)';
            e.currentTarget.style.boxShadow = '0 12px 30px rgba(0,0,0,0.3)';
          }}
          onMouseLeave={(e) => {
            e.currentTarget.style.transform = 'translateY(0)';
            e.currentTarget.style.boxShadow = '0 8px 25px rgba(0,0,0,0.2)';
          }}
        >
          ➔ Return to Dashboard
        </button>
      </div>
    );
  }

  return (
    <div className="game-board-container">
      {/* Title Banner */}
      <div className="game-title-banner">
        <span style={{ fontSize: '12px', textTransform: 'uppercase', fontWeight: 800, letterSpacing: '0.15em', display: 'block', marginBottom: '5px', opacity: 0.9 }} className="banner-subtitle">
          GRAND CAMPAIGN BOARD
        </span>
        <h1 className="game-title-h1">
          Indian Politics Simulation
        </h1>
        <p className="game-title-p">
          Command campaign strategies, form coalitions, and win state elections.
        </p>
        {playerPartyName && (
          <div style={{ 
            marginTop: '15px', 
            display: 'inline-flex', 
            alignItems: 'center', 
            gap: '8px',
            background: 'var(--primary-dark)',
            padding: '8px 16px',
            borderRadius: '20px',
            border: '1px solid rgba(255, 255, 255, 0.2)',
            boxShadow: '0 4px 10px rgba(0,0,0,0.1)'
          }}>
            <span style={{ 
              width: '10px', 
              height: '10px', 
              borderRadius: '50%', 
              backgroundColor: playerPartyColor, 
              display: 'inline-block' 
            }} />
            <span style={{ fontSize: '12px', fontWeight: '800', letterSpacing: '0.05em', color: '#ffffff' }}>
              PLAYING AS: <span style={{ color: playerPartyColor, fontWeight: '900' }}>{playerPartyName.toUpperCase()}</span>
            </span>
          </div>
        )}
      </div>

      {/* View Toggle Bar */}
      <div className="view-toggle-bar">
        <button 
          className={`view-toggle-button ${activeView === 'INFO' ? 'selected' : ''}`}
          onClick={() => setActiveView('INFO')}
        >
          📊 Stats &amp; Commentary
        </button>
        <button 
          className={`view-toggle-button ${activeView === 'ACTION' ? 'selected' : ''}`}
          onClick={() => setActiveView('ACTION')}
        >
          🃏 Actions &amp; Cards
        </button>
      </div>

      {/* View Content */}
      <div className="unified-card game-content-card" style={{ minHeight: '400px' }}>
        {loading && <div style={{ textAlign: 'center', padding: '50px 0' }}>⌛ Loading Campaign State...</div>}
        {error && <div style={{ color: '#d23f31', textAlign: 'center', padding: '50px 0' }}>⚠️ {error}</div>}
        
        {!turnData && !loading && !error && (
          <div style={{ textAlign: 'center', padding: '50px 0' }}>
            No campaign data loaded. Please return to the Dashboard to load or start a campaign.
          </div>
        )}

        {activeView === 'INFO' && turnData && (
          <StatsView
            turnData={turnData}
            commentaryExpanded={commentaryExpanded}
            setCommentaryExpanded={setCommentaryExpanded}
            commentaryFilter={commentaryFilter}
            setCommentaryFilter={setCommentaryFilter}
          />
        )}

        {activeView === 'ACTION' && turnData && (
          <ActionsView
            turnData={turnData}
            activeParty={activeParty}
            loading={loading}
            handleAdvanceTurn={handleAdvanceTurn}
            handleSkipTurn={handleSkipTurn}
            
            // Action 1 props
            selectedCard={selectedCard}
            setSelectedCard={setSelectedCard}
            targetPartyId={targetPartyId}
            setTargetPartyId={setTargetPartyId}
            cardCategoryFilter={cardCategoryFilter}
            setCardCategoryFilter={setCardCategoryFilter}

            // Action 2 props
            selectedNewsReactions={selectedNewsReactions}
            setSelectedNewsReactions={setSelectedNewsReactions}

            // Action 3 props
            selectedIssueOptionKey={selectedIssueOptionKey}
            setSelectedIssueOptionKey={setSelectedIssueOptionKey}

            // Action 4 props
            bidAmount={bidAmount}
            setBidAmount={setBidAmount}
            bidConfirmed={bidConfirmed}
            setBidConfirmed={setBidConfirmed}

            // Action 5 props
            selectedRewardKey={selectedRewardKey}
            setSelectedRewardKey={setSelectedRewardKey}
            rewardTargetPartyId={rewardTargetPartyId}
            setRewardTargetPartyId={setRewardTargetPartyId}
            rewardConfirmed={rewardConfirmed}
            setRewardConfirmed={setRewardConfirmed}

            // Action 6 props
            projectCategoryFilter={projectCategoryFilter}
            setProjectCategoryFilter={setProjectCategoryFilter}
            draftProjectKeys={draftProjectKeys}
            setDraftProjectKeys={setDraftProjectKeys}
            fundingContributions={fundingContributions}
            setFundingContributions={setFundingContributions}
            partyBuildingConfirmed={partyBuildingConfirmed}
            setPartyBuildingConfirmed={setPartyBuildingConfirmed}
            handleFundProject={handleFundProject}
            handleSetProjectTarget={handleSetProjectTarget}

            // Action 7 props
            handleCooperationUpdate={setTurnData}

            // Accordion state
            activeAccordion={activeAccordion}
            setActiveAccordion={setActiveAccordion}
          />
        )}
      </div>

      {/* Floating Center-Right Navigation Arrow */}
      {activeView === 'INFO' && turnData && (
        <div 
          onClick={() => setActiveView('ACTION')}
          className="floating-nav-arrow"
          title="Proceed to Actions & Cards"
        >
          <span style={{ fontSize: '28px', fontWeight: 'bold' }}>➔</span>
        </div>
      )}
    </div>
  );
}
