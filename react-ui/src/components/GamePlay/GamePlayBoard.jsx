import React, { useState, useEffect, useRef } from 'react';
import { useGameStore } from '../../store/gameStore';
import { fetchTurnView, advanceTurn, fundProject, destroyProject, setProjectTarget, fetchBuildingProjects, fetchPostDefinitions, takeLoan, buyRecoveryPack } from '../../api/apiClient';
import { getPartyColor, cardRequiresTarget } from './gameUtils';
import StatsView from './StatsView';
import ActionsView from './ActionsView';
import { getPartyThemeByName } from '../../constants/partyThemes';
import { PROJECT_DEFS } from './constants';
import RoundResolutionModal from './RoundResolutionModal';
import SkipTurnConfirmationModal from './SkipTurnConfirmationModal';
import DefeatHazardModal from './DefeatHazardModal';
import GameTutorial from './GameTutorial';
import { useMultiplayer } from '../../hooks/useMultiplayer';
import ChatDrawer from '../../components/Chat/ChatDrawer';
import { initializePostDefinitions } from './postsConfig';

const PROJECT_EMOJIS = {
  PARTY_HQ: '🏢',
  IT_CELL: '💻',
  CADRE_OFFICE: '🏘️',
  THINK_TANK: '🧠',
  TRAINING_ACADEMY: '🏫',
  YOUTH_WING: '✊',
  MEGA_RALLY: '📢',
  PRIME_LEADER_VISIT: '⭐',
  FOUNDATION_DAY: '🎉',
  PARTY_CONGRESS: '🤝',
  DISSENT_NEWSPAPER: '📰',
  MEDIA_HOUSE: '📺',
  PARTY_DISSENT: '📣',
  CORRUPTION_EXPOSE: '🔍',
  CAMPAIGN_SABOTAGE: '💣',
  AUDIT_HARASSMENT: '💼',
  MEDIA_SMEAR: '📻',
  WHISTLEBLOWER_FORUM: '🔍',
  CITIZEN_OUTREACH: '🤝',
  PROTEST_STRIKE: '✊',
  LEAK_INTERNAL_MEMO: '📄'
};

function formatProjectDefinitions(backendDefs) {
  const getCostString = (proj) => {
    const parts = [];
    if (proj.costCoins) parts.push(`💰 ${proj.costCoins}`);
    if (proj.costMorale) parts.push(`✊ ${proj.costMorale}`);
    if (proj.costCorruption) parts.push(`⚖️ ${proj.costCorruption}`);
    if (proj.costMedia) parts.push(`📢 ${proj.costMedia}`);
    if (proj.costSupport) parts.push(`📈 ${proj.costSupport}%`);
    return parts.length > 0 ? parts.join(', ') : 'Free';
  };

  const getYieldString = (proj) => {
    const parts = [];
    const prefix = proj.requiresTarget ? '💥 ' : '';
    if (proj.benefitCoins) parts.push(`💰 ${proj.benefitCoins > 0 ? '+' : ''}${proj.benefitCoins}`);
    if (proj.benefitMorale) parts.push(`✊ ${proj.benefitMorale > 0 ? '+' : ''}${proj.benefitMorale}`);
    if (proj.benefitCorruption) parts.push(`⚖️ ${proj.benefitCorruption > 0 ? '+' : ''}${proj.benefitCorruption}`);
    if (proj.benefitMedia) parts.push(`📢 ${proj.benefitMedia > 0 ? '+' : ''}${proj.benefitMedia}`);
    if (proj.benefitSupport) parts.push(`📈 ${proj.benefitSupport > 0 ? '+' : ''}${proj.benefitSupport}%`);
    const suffix = proj.requiresTarget ? ' to Target per turn' : ' per turn';
    return prefix + (parts.length > 0 ? parts.join(', ') : 'None') + suffix;
  };

  const newDefs = {};
  Object.entries(backendDefs).forEach(([key, proj]) => {
    newDefs[key] = {
      name: `${PROJECT_EMOJIS[key] || '🏗️'} ${proj.name}`,
      cost: getCostString(proj),
      costCoins: proj.costCoins || 0,
      costMorale: proj.costMorale || 0,
      costCorruption: proj.costCorruption || 0,
      costMedia: proj.costMedia || 0,
      costSupport: proj.costSupport || 0,
      yield: getYieldString(proj),
      offensive: proj.requiresTarget || false,
      benefitCoins: proj.benefitCoins || 0,
      benefitMorale: proj.benefitMorale || 0,
      benefitCorruption: proj.benefitCorruption || 0,
      benefitMedia: proj.benefitMedia || 0,
      benefitSupport: proj.benefitSupport || 0
    };
  });
  return newDefs;
}

function hexToRgbStr(hex) {
  let c = hex.replace('#', '');
  if (c.length === 3) {
    c = c.split('').map(x => x + x).join('');
  }
  const r = parseInt(c.substring(0, 2), 16);
  const g = parseInt(c.substring(2, 4), 16);
  const b = parseInt(c.substring(4, 6), 16);
  return isNaN(r) || isNaN(g) || isNaN(b) ? '101, 148, 177' : `${r}, ${g}, ${b}`;
}

export default function GamePlayBoard() {
  const [activeView, setActiveView] = useState('INFO');
  const { user, activeGameId, turnData, setTurnData, setTimeLeft } = useGameStore();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [projectDefs, setProjectDefs] = useState(PROJECT_DEFS);
  
  // Multiplayer
  const { isConnected, messages, sendMessage, gameUpdateTick, triggerGameUpdate } = useMultiplayer(activeGameId, user?.id || user?.email, user?.name);
  const [showChat, setShowChat] = useState(false);
  const [chatInput, setChatInput] = useState('');
  const [unreadCount, setUnreadCount] = useState(0);
  const [newMsgPulse, setNewMsgPulse] = useState(false);
  const prevMsgCountRef = useRef(0);

  useEffect(() => {
    fetchBuildingProjects()
      .then(data => {
        const formatted = formatProjectDefinitions(data);
        setProjectDefs(formatted);
      })
      .catch(err => console.error("Failed to load building projects from backend, using fallbacks:", err));

    fetchPostDefinitions()
      .then(data => {
        initializePostDefinitions(data);
      })
      .catch(err => console.error("Failed to load post definitions from backend:", err));
  }, []);

  const [scenarioBills, setScenarioBills] = useState([]);
  const [scenarioEvents, setScenarioEvents] = useState([]);

  useEffect(() => {
    if (turnData?.scenarioKey) {
      import('../../api/apiClient').then(client => {
        if (client.fetchBillsForGameplay) {
          client.fetchBillsForGameplay(turnData.scenarioKey)
            .then(data => setScenarioBills(data || []))
            .catch(err => console.error("Failed to load scenario bills:", err));
        }
        if (client.fetchEventsForGameplay) {
          client.fetchEventsForGameplay(turnData.scenarioKey)
            .then(data => setScenarioEvents(data || []))
            .catch(err => console.error("Failed to load scenario events:", err));
        }
      });
    }
  }, [turnData?.scenarioKey]);

  useEffect(() => {
    if (turnData?.gameId && turnData?.parties) {
      const historyKey = `faction_loyalty_history_${turnData.gameId}`;
      let historyData = {};
      try {
        historyData = JSON.parse(localStorage.getItem(historyKey) || '{}');
      } catch (e) {}

      const turnNum = turnData.turnNumber;
      historyData[turnNum] = historyData[turnNum] || {};

      turnData.parties.forEach(party => {
        if (party.factions) {
          party.factions.forEach(f => {
            historyData[turnNum][f.key] = f.loyalty;
          });
        }
      });

      localStorage.setItem(historyKey, JSON.stringify(historyData));
    }
  }, [turnData]);

  const [commentaryExpanded, setCommentaryExpanded] = useState(false);
  const [commentaryFilter, setCommentaryFilter] = useState('ALL');
  const [showDroppedRewardModal, setShowDroppedRewardModal] = useState(false);
  const [showProjectRefreshModal, setShowProjectRefreshModal] = useState(false);

  useEffect(() => {
    if (turnData?.lastRoundDroppedReward) {
      setShowDroppedRewardModal(true);
    }
    if (turnData?.lastRoundProjectLimitsRefreshed) {
      setShowProjectRefreshModal(true);
    }
  }, [turnData]);



  // Real 6 actions states
  const [selectedCard, setSelectedCard] = useState(null);
  const [targetPartyId, setTargetPartyId] = useState('');
  const [selectedNewsReactions, setSelectedNewsReactions] = useState({});
  const [selectedIssueOptionKey, setSelectedIssueOptionKey] = useState('');
  const [bidAmount, setBidAmount] = useState(0);
  const [bidConfirmed, setBidConfirmed] = useState(false);
  const [selectedRewardKey, setSelectedRewardKey] = useState('');
  const [rewardTargetPartyId, setRewardTargetPartyId] = useState('');
  const [billVote, setBillVote] = useState('');
  const [whipIssued, setWhipIssued] = useState(false);
  const [proposedBillKey, setProposedBillKey] = useState('');
  const [selectedEventOptionKey, setSelectedEventOptionKey] = useState('');
  const [activeAccordion, setActiveAccordion] = useState(1); // 1-8
  const [rewardConfirmed, setRewardConfirmed] = useState(false);
  const [partyBuildingConfirmed, setPartyBuildingConfirmed] = useState(false);
  const [cardCategoryFilter, setCardCategoryFilter] = useState('agitation_movement');
  const [showResolutionReport, setShowResolutionReport] = useState(false);
  const [showSkipModal, setShowSkipModal] = useState(false);
  const [showDefeatHazardModal, setShowDefeatHazardModal] = useState(false);

  // Project building draft states
  const [projectCategoryFilter, setProjectCategoryFilter] = useState('BUILD');
  const [draftProjectKeys, setDraftProjectKeys] = useState([]);
  const [fundingContributions, setFundingContributions] = useState({});
  const [fundedThisTurn, setFundedThisTurn] = useState([]);

  const myPartyId = turnData?.isMultiplayer && turnData?.humanPlayerMap && user
    ? Object.keys(turnData.humanPlayerMap).find(k => turnData.humanPlayerMap[k]?.toLowerCase() === (user.id || user.email)?.toLowerCase())
    : (turnData?.activeHumanPartyId || turnData?.parties?.find(p => p.playerControlled)?.id);
  
  const myParty = turnData?.parties?.find(p => p.id === myPartyId);
  const activeParty = myParty || turnData?.parties?.find(p => p.playerControlled);
  const playerPartyName = myParty?.name || turnData?.activeHumanPartyName || activeParty?.name;
  
  const partyTheme = getPartyThemeByName(playerPartyName || '');
  const isDefaultFallback = partyTheme.symbolName === 'Flag';
  const customColor = activeParty?.color;
  const hasCustomColor = customColor && customColor !== '#ffffff' && customColor !== '#fff' && customColor !== '';
  const playerPartyColor = (isDefaultFallback && hasCustomColor) ? customColor : partyTheme.color;
  const playerPartyColorRgb = (isDefaultFallback && hasCustomColor) ? hexToRgbStr(customColor) : partyTheme.rgb;
  const SymbolIcon = partyTheme.SymbolIcon;

  // Auto-open the Defeat Hazard Modal when the player's party enters crisis
  const prevHasDefeatHazardRef = useRef(false);
  useEffect(() => {
    const myP = turnData?.parties?.find(p => p.id === myPartyId);
    const nowInHazard = !!(myP?.hasDefeatHazard);
    if (nowInHazard && !prevHasDefeatHazardRef.current) {
      setShowDefeatHazardModal(true);
    }
    prevHasDefeatHazardRef.current = nowInHazard;
  }, [turnData, myPartyId]);

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
    setFundedThisTurn([]);
    setRewardConfirmed(false);
    setPartyBuildingConfirmed(false);
    setCardCategoryFilter('governance');
    setBillVote('');
    setWhipIssued(false);
    setProposedBillKey('');
    setSelectedEventOptionKey('');
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

  // Track unread chat messages when chat is closed
  useEffect(() => {
    if (messages.length > prevMsgCountRef.current) {
      if (!showChat) {
        setUnreadCount(prev => prev + (messages.length - prevMsgCountRef.current));
        setNewMsgPulse(true);
        setTimeout(() => setNewMsgPulse(false), 1200);
      }
      prevMsgCountRef.current = messages.length;
    }
  }, [messages.length, showChat]);

  useEffect(() => {
    loadTurnData(true);
  }, [activeGameId]);

  useEffect(() => {
    if (gameUpdateTick > 0) {
      loadTurnData(false);
    }
  }, [gameUpdateTick]);

  useEffect(() => {
    if (turnData?.turnStartTime && turnData?.turnDurationSeconds) {
      const interval = setInterval(() => {
        const start = new Date(turnData.turnStartTime).getTime();
        const duration = turnData.turnDurationSeconds * 1000;
        const now = Date.now();
      const remaining = Math.max(0, Math.floor((start + duration - now) / 1000));
      setTimeLeft(remaining);
    }, 1000);
    return () => clearInterval(interval);
  } else {
    setTimeLeft(null);
  }
}, [turnData]);

const prevTurnNumberRef = useRef(turnData?.turnNumber);
useEffect(() => {
  if (turnData && prevTurnNumberRef.current !== undefined) {
    if (turnData.turnNumber > prevTurnNumberRef.current) {
      // Turn was advanced (e.g. by time running out or other players submitting)
      setShowResolutionReport(true);
      setActiveView('INFO');
      setActiveAccordion(1);
    }
  }
  prevTurnNumberRef.current = turnData?.turnNumber;
}, [turnData]);

  const handleAdvanceTurn = async () => {
    setLoading(true);
    setError('');
    try {
      const storageKey = `political_sim_party_management_${activeGameId}_${turnData.turnNumber || 0}`;
      const saved = localStorage.getItem(storageKey);
      let factionAllocs = {};
      let factionCrisisChoice = null;
      if (saved) {
        try {
          const parsed = JSON.parse(saved);
          factionCrisisChoice = parsed.factionCrisisChoice || null;
          const savedFactions = parsed.factions || [];

          // Count patronage points used (patronage field delta from base 0)
          const patronageUsed = savedFactions.reduce((sum, f) => sum + (f.patronage || 0), 0);

          // Build postAssignments: { postKey -> factionId } for all posts that were assigned this turn
          const postAssignments = parsed.assignedPostKeys || {};

          factionAllocs = {
            patronageUsed,
            postAssignments,
            factions: savedFactions.map(f => ({
              key: f.id,
              loyalty: f.loyalty,
              influence: f.influence,
              post: f.post,
              patronage: f.patronage,
              active: f.active
            })),
            projects: savedFactions.reduce((acc, f) => {
              const map = {};
              (f.projects || []).forEach(p => {
                map[p.projectKey || p.id] = f.id;
              });
              return { ...acc, ...map };
            }, {})
          };
        } catch (e) {
          console.error("Failed to parse allocations from localStorage", e);
        }
      }

      const payload = {
        selectedCardKey: selectedCard?.cardKey,
        targetPartyId: selectedCard && cardRequiresTarget(selectedCard) ? targetPartyId : null,
        selectedNewsReactions: selectedNewsReactions,
        selectedIssueOptionKey: turnData.currentIssue ? selectedIssueOptionKey : 'routine_maintenance',
        bid: bidAmount,
        selectedRewardKey: selectedRewardKey || null,
        rewardTargetPartyId: selectedRewardKey && rewardTargetPartyId ? rewardTargetPartyId : null,
        proposedBillKey: proposedBillKey || null,
        billVote: turnData.proposedBillKeyThisTurn ? billVote : null,
        selectedEventOptionKey: turnData.activeEventKey ? selectedEventOptionKey : null,
        whipIssued: turnData.proposedBillKeyThisTurn ? whipIssued : false,
        allocations: factionAllocs,
        factionCrisisChoice: factionCrisisChoice
      };

      const result = await advanceTurn(activeGameId, payload);
      setTurnData(result);
      if (turnData.isMultiplayer) triggerGameUpdate();
      resetLocalStates();
      setShowResolutionReport(true);
      setActiveView('INFO');
      setActiveAccordion(1);
    } catch (err) {
      console.error(err);
      setError(err.message || 'Failed to advance turn.');
    } finally {
      setLoading(false);
    }
  };

  const handleSkipTurn = () => {
    setShowSkipModal(true);
  };

  const executeSkipTurn = async () => {
    setShowSkipModal(false);
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

      // Default event option for skipping
      let defaultEventOption = null;
      if (turnData.activeEventKey) {
        const activeEvDef = scenarioEvents.find(e => e.eventKey === turnData.activeEventKey);
        if (activeEvDef && activeEvDef.options && activeEvDef.options.length > 0) {
          defaultEventOption = activeEvDef.options[activeEvDef.options.length - 1].optionKey;
        }
      }

      const payload = {
        selectedCardKey: 'no_card',
        targetPartyId: null,
        selectedNewsReactions: defaultReactions,
        selectedIssueOptionKey: defaultIssueOpt,
        bid: 0,
        selectedRewardKey: null,
        rewardTargetPartyId: null,
        proposedBillKey: null,
        billVote: turnData.proposedBillKeyThisTurn ? 'ABSTAIN' : null,
        selectedEventOptionKey: defaultEventOption,
        whipIssued: false
      };

      const result = await advanceTurn(activeGameId, payload);
      setTurnData(result);
      if (turnData.isMultiplayer) triggerGameUpdate();
      resetLocalStates();
      setShowResolutionReport(true);
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
    setError('');
    try {
      const data = await fundProject(activeGameId, activeParty.id, projectKey, progress);
      setTurnData(data);
      setFundingContributions(prev => {
        const next = { ...prev };
        delete next[projectKey];
        return next;
      });
      setDraftProjectKeys(prev => prev.filter(k => k !== projectKey));
      setFundedThisTurn(prev => [...prev, projectKey]);
    } catch (err) {
      console.error(err);
      setError(err.message || 'Failed to fund project.');
    }
  };

  const handleDestroyProject = async (projectKey) => {
    setError('');
    try {
      const data = await destroyProject(activeGameId, activeParty.id, projectKey);
      setTurnData(data);
      setFundingContributions(prev => {
        const next = { ...prev };
        delete next[projectKey];
        return next;
      });
      setDraftProjectKeys(prev => prev.filter(k => k !== projectKey));
    } catch (err) {
      console.error(err);
      setError(err.message || 'Failed to destroy project.');
    }
  };

  const handleSetProjectTarget = async (projectKey, targetId) => {
    setError('');
    try {
      const data = await setProjectTarget(activeGameId, activeParty.id, projectKey, targetId);
      setTurnData(data);
    } catch (err) {
      console.error(err);
      setError(err.message || 'Failed to set project target.');
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
                      <span>{party.name} {party.id === turnData.activeHumanPartyId && '(You)'}</span>
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
    <div className="game-board-container" style={{
      '--party-primary-color': playerPartyColor,
      '--party-primary-color-rgb': playerPartyColorRgb
    }}>
      <style>{`
        @keyframes chatVibrate {
          0%   { transform: translateX(0); }
          15%  { transform: translateX(-6px); }
          30%  { transform: translateX(6px); }
          45%  { transform: translateX(-5px); }
          60%  { transform: translateX(5px); }
          75%  { transform: translateX(-3px); }
          90%  { transform: translateX(3px); }
          100% { transform: translateX(0); }
        }
        @keyframes chatBounce {
          0%, 100% { transform: translateY(0) scale(1); }
          50% { transform: translateY(-10px) scale(1.1); }
        }
        .chat-btn-new-msg {
          animation: chatBounce 0.5s ease 2;
        }
      `}</style>
      <GameTutorial />
      {/* Title Banner */}
      <div className="game-title-banner" style={{ padding: '24px 20px', background: 'var(--party-primary-color)' }}>
        <h1 className="game-title-h1" style={{ margin: 0, textTransform: 'uppercase', letterSpacing: '0.08em' }}>
          GRAND CAMPAIGN BOARD
        </h1>
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
        {turnData?.isMultiplayer && turnData?.joinCode && (
          <div style={{ 
            marginTop: '15px', 
            marginLeft: '15px',
            display: 'inline-flex', 
            alignItems: 'center', 
            background: 'var(--primary-dark)',
            padding: '8px 16px',
            borderRadius: '20px',
            border: '1px solid rgba(255, 255, 255, 0.2)',
            boxShadow: '0 4px 10px rgba(0,0,0,0.1)'
          }}>
            <span style={{ fontSize: '12px', fontWeight: '800', letterSpacing: '0.05em', color: '#ffffff' }}>
              JOIN CODE: <span style={{ color: 'var(--accent-teal)', fontWeight: '900', letterSpacing: '2px', marginLeft: '4px' }}>{turnData.joinCode}</span>
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
          📊 Party info
        </button>
        <button
          className={`view-toggle-button ${activeView === 'ACTION' ? 'selected' : ''}`}
          onClick={() => setActiveView('ACTION')}
        >
          🃏 Actions &amp; Cards
        </button>
        {myParty?.hasDefeatHazard && (
          <button
            className="view-toggle-button"
            onClick={() => setShowDefeatHazardModal(true)}
            style={{ 
              background: 'rgba(220, 38, 38, 0.1)', 
              color: '#f87171', 
              border: '1px solid rgba(220, 38, 38, 0.4)',
              marginLeft: 'auto' 
            }}
          >
            🚨 CRISIS: SOS
          </button>
        )}
      </div>

      {/* View Content inside Curved Layout Wrapper */}
      <div className="game-layout-wrapper">
        {/* Left themed sidebar */}
        <div className="themed-left-sidebar">
          <div className="themed-symbol-badge">
            <SymbolIcon size={32} color={playerPartyColor} />
          </div>
        </div>

        {/* Right Content */}
        <div className="themed-right-content">
          {loading && !turnData && <div style={{ textAlign: 'center', padding: '50px 0' }}>⌛ Loading Campaign State...</div>}
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
              projectDefs={projectDefs}
              onOpenResolutionReport={() => setShowResolutionReport(true)}
              scenarioBills={scenarioBills}
            />
          )}

          {activeView === 'ACTION' && turnData && (
            <ActionsView
              turnData={turnData}
              activeParty={activeParty}
              loading={loading}
              handleAdvanceTurn={handleAdvanceTurn}
              handleSkipTurn={handleSkipTurn}
              projectDefs={projectDefs}
              
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
              handleDestroyProject={handleDestroyProject}
              handleSetProjectTarget={handleSetProjectTarget}
              fundedThisTurn={fundedThisTurn}
              setFundedThisTurn={setFundedThisTurn}

              // Action 7 props
              handleCooperationUpdate={setTurnData}

              // Action 8 / Assembly props
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

              // Accordion state
              activeAccordion={activeAccordion}
              setActiveAccordion={setActiveAccordion}
            />
          )}

        </div>
      </div>

      {/* Floating Chat Toggle Button (bottom-right) – multiplayer only */}
      {turnData?.isMultiplayer && (
        <div style={{ position: 'fixed', bottom: '24px', right: '24px', zIndex: 1100, display: 'inline-block' }}>
          <div style={{ position: 'relative', display: 'inline-block' }}>
          <button
            onClick={() => { setShowChat(!showChat); if (!showChat) setUnreadCount(0); }}
            title="Toggle Chat"
            className={newMsgPulse ? 'chat-btn-new-msg' : ''}
            style={{
              width: '54px',
              height: '54px',
              borderRadius: '50%',
              backgroundColor: playerPartyColor,
              border: `3px solid #ffffff`,
              color: '#ffffff',
              fontSize: '22px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              cursor: 'pointer',
              boxShadow: `0 6px 20px rgba(0,0,0,0.35)`,
              transition: 'transform 0.2s ease, box-shadow 0.2s ease',
              padding: 0,
            }}
            onMouseEnter={e => { e.currentTarget.style.transform = 'scale(1.12)'; e.currentTarget.style.boxShadow = '0 10px 28px rgba(0,0,0,0.45)'; }}
            onMouseLeave={e => { e.currentTarget.style.transform = 'scale(1)'; e.currentTarget.style.boxShadow = '0 6px 20px rgba(0,0,0,0.35)'; }}
          >
            {showChat ? '✕' : '💬'}
          </button>
          {/* Unread badge */}
          {!showChat && unreadCount > 0 && (
            <span style={{
              position: 'absolute',
              top: '-4px',
              right: '-4px',
              background: '#ef4444',
              color: '#fff',
              fontSize: '11px',
              fontWeight: 900,
              borderRadius: '999px',
              minWidth: '20px',
              height: '20px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              padding: '0 4px',
              border: '2px solid #fff',
              pointerEvents: 'none',
              animation: 'chatVibrate 0.5s ease'
            }}>
              {unreadCount > 9 ? '9+' : unreadCount}
            </span>
          )}
          </div>
        </div>
      )}

      {/* Chat Drawer Panel */}
      {turnData?.isMultiplayer && (
        <ChatDrawer
          isOpen={showChat}
          onClose={() => setShowChat(false)}
          messages={messages}
          sendMessage={sendMessage}
          chatInput={chatInput}
          setChatInput={setChatInput}
          user={user}
          partyColor={playerPartyColor}
        />
      )}


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

      {/* Defeat Hazard Emergency Modal */}
      <DefeatHazardModal
        isOpen={showDefeatHazardModal}
        onClose={() => setShowDefeatHazardModal(false)}
        party={myParty}
        partyColor={playerPartyColor}
        onTakeLoan={async () => {
          const data = await takeLoan(activeGameId, myPartyId);
          setTurnData(data);
        }}
        onBuyRecoveryPack={async () => {
          const data = await buyRecoveryPack(activeGameId, myPartyId);
          setTurnData(data);
        }}
      />

      {/* Round Resolution Summary Modal */}
      <RoundResolutionModal
        isOpen={showResolutionReport}
        onClose={() => setShowResolutionReport(false)}
        turnData={turnData}
        activeParty={activeParty}
        partyColor={playerPartyColor}
        projectDefs={projectDefs}
      />

      {/* Skip Turn Confirmation Modal */}
      <SkipTurnConfirmationModal
        isOpen={showSkipModal}
        onConfirm={executeSkipTurn}
        onCancel={() => setShowSkipModal(false)}
        partyColor={playerPartyColor}
      />

      {showDroppedRewardModal && turnData?.lastRoundDroppedReward && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          width: '100%',
          height: '100%',
          backgroundColor: 'rgba(15, 23, 42, 0.85)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 10005,
          backdropFilter: 'blur(8px)',
        }}>
          <div style={{
            background: 'linear-gradient(135deg, #1e1b4b 0%, #311042 100%)',
            border: '2px solid #eab308',
            borderRadius: '24px',
            padding: '40px',
            maxWidth: '550px',
            width: '90%',
            textAlign: 'center',
            boxShadow: '0 25px 50px -12px rgba(234, 179, 8, 0.3)',
            color: '#ffffff',
            position: 'relative',
            overflow: 'hidden'
          }}>
            <div style={{
              position: 'absolute',
              top: '-50%',
              left: '-50%',
              width: '200%',
              height: '200%',
              background: 'radial-gradient(circle, rgba(234, 179, 8, 0.1) 0%, transparent 60%)',
              pointerEvents: 'none'
            }} />

            <span style={{ fontSize: '72px', display: 'block', marginBottom: '15px', filter: 'drop-shadow(0 10px 15px rgba(234, 179, 8, 0.4))' }}>
              🎁
            </span>
            
            <h2 style={{
              fontSize: '28px',
              fontWeight: 900,
              margin: '0 0 10px 0',
              letterSpacing: '0.05em',
              textTransform: 'uppercase',
              color: '#fef08a',
              textShadow: '0 2px 8px rgba(0,0,0,0.5)'
            }}>
              10-Round Reward Drop!
            </h2>
            
            <p style={{ fontSize: '15px', opacity: 0.9, lineHeight: 1.6, margin: '0 auto 25px auto', maxWidth: '400px' }}>
              Every 10 rounds, one randomly selected party receives a free random reward.
            </p>

            <div style={{
              background: 'rgba(255, 255, 255, 0.05)',
              border: '1.5px solid rgba(234, 179, 8, 0.3)',
              borderRadius: '16px',
              padding: '20px',
              marginBottom: '30px',
              backdropFilter: 'blur(4px)'
            }}>
              <div style={{ fontSize: '13px', opacity: 0.7, textTransform: 'uppercase', letterSpacing: '0.05em' }}>Recipient Party</div>
              <div style={{ fontSize: '20px', fontWeight: 'bold', color: '#ffffff', margin: '4px 0 12px 0', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px' }}>
                <span style={{
                  width: '10px',
                  height: '10px',
                  borderRadius: '50%',
                  backgroundColor: getPartyColor(turnData.parties?.find(p => p.id === turnData.lastRoundDroppedReward.partyId) || {}),
                  border: '1px solid rgba(255,255,255,0.2)'
                }} />
                {turnData.lastRoundDroppedReward.partyName}
              </div>
              
              <div style={{ width: '100%', height: '1px', background: 'rgba(234, 179, 8, 0.2)', margin: '12px 0' }} />

              <div style={{ fontSize: '13px', opacity: 0.7, textTransform: 'uppercase', letterSpacing: '0.05em' }}>Reward Unlocked</div>
              <div style={{ fontSize: '18px', fontWeight: 800, color: '#facc15', margin: '4px 0' }}>
                ⭐ {turnData.lastRoundDroppedReward.rewardName}
              </div>
              <div style={{ fontSize: '12px', opacity: 0.9, fontStyle: 'italic' }}>
                {turnData.lastRoundDroppedReward.rewardDescription}
              </div>
            </div>

            <button
              onClick={() => setShowDroppedRewardModal(false)}
              style={{
                background: 'linear-gradient(90deg, #f59e0b, #d97706)',
                color: '#ffffff',
                fontSize: '14px',
                fontWeight: 'bold',
                padding: '12px 35px',
                border: 'none',
                borderRadius: '10px',
                cursor: 'pointer',
                boxShadow: '0 4px 15px rgba(217, 119, 6, 0.4)',
                transition: 'all 0.2s ease',
                textTransform: 'uppercase',
                letterSpacing: '0.05em'
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.transform = 'translateY(-2px)';
                e.currentTarget.style.boxShadow = '0 6px 20px rgba(217, 119, 6, 0.5)';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.transform = 'translateY(0)';
                e.currentTarget.style.boxShadow = '0 4px 15px rgba(217, 119, 6, 0.4)';
              }}
            >
              Acknowledge
            </button>
          </div>
        </div>
      )}

      {showProjectRefreshModal && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          width: '100%',
          height: '100%',
          backgroundColor: 'rgba(15, 23, 42, 0.85)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 10005,
          backdropFilter: 'blur(8px)',
        }}>
          <div style={{
            background: 'linear-gradient(135deg, #0f172a 0%, #1e293b 100%)',
            border: '2px solid #3b82f6',
            borderRadius: '24px',
            padding: '40px',
            maxWidth: '550px',
            width: '90%',
            textAlign: 'center',
            boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.5), 0 0 40px rgba(59, 130, 246, 0.25)',
            color: '#ffffff',
            position: 'relative',
            overflow: 'hidden'
          }}>
            <div style={{ position: 'absolute', top: 0, left: 0, right: 0, height: '4px', background: 'linear-gradient(90deg, #3b82f6, #60a5fa)' }} />
            
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '15px' }}>
              <div style={{
                width: '70px',
                height: '70px',
                borderRadius: '50%',
                background: 'rgba(59, 130, 246, 0.1)',
                border: '2px solid #3b82f6',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: '32px',
                boxShadow: '0 0 20px rgba(59, 130, 246, 0.2)',
                animation: 'pulse 2s infinite'
              }}>
                🔄
              </div>
              
              <h2 style={{ fontSize: '24px', fontWeight: 900, margin: 0, background: 'linear-gradient(90deg, #60a5fa, #93c5fd)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>
                PROJECT BUILD LIMITS RESET
              </h2>
              
              <p style={{ fontSize: '14px', lineHeight: '1.6', opacity: 0.9, margin: '10px 0 20px 0' }}>
                All party project build quotas have been refreshed! You can now start new construction projects. 
                <br /><br />
                Remember:
                <br />
                • Cost &gt; 100 💰: <b>1 build per 20 turns</b>
                <br />
                • Cost &lt; 100 💰: <b>2 builds per 20 turns</b>
              </p>

              <button
                onClick={() => setShowProjectRefreshModal(false)}
                style={{
                  background: 'linear-gradient(90deg, #3b82f6, #2563eb)',
                  color: '#ffffff',
                  fontSize: '14px',
                  fontWeight: 'bold',
                  padding: '12px 35px',
                  border: 'none',
                  borderRadius: '10px',
                  cursor: 'pointer',
                  boxShadow: '0 4px 15px rgba(37, 99, 235, 0.4)',
                  transition: 'all 0.2s ease',
                  textTransform: 'uppercase',
                  letterSpacing: '0.05em'
                }}
                onMouseEnter={(e) => {
                  e.currentTarget.style.transform = 'translateY(-2px)';
                  e.currentTarget.style.boxShadow = '0 6px 20px rgba(37, 99, 235, 0.5)';
                }}
                onMouseLeave={(e) => {
                  e.currentTarget.style.transform = 'translateY(0)';
                  e.currentTarget.style.boxShadow = '0 4px 15px rgba(37, 99, 235, 0.4)';
                }}
              >
                Let's Build
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
