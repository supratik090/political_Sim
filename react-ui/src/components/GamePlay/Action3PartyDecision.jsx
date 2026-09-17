import React, { useState, useEffect, useCallback, useRef } from 'react';
import { getFactionDisplayName } from './gameUtils';
import { getPostByKey, getPostByName, POSTS_CONFIG } from './postsConfig';
import { lockPartyManagement } from '../../api/apiClient';

export default function Action3PartyDecision({
  turnData,
  selectedIssueOptionKey,
  setSelectedIssueOptionKey,
  activeParty,
  selectedEventOptionKey,
  setSelectedEventOptionKey,
  scenarioEvents = [],
  projectDefs = {}
}) {
// A robust key that guarantees isolation across different games AND turns
const gameSessionId = turnData?.gameId || turnData?.scenarioId || 'default_session';
const turnNumber = turnData?.turnNumber || 0;

const storageKey = `political_sim_party_management_${gameSessionId}_turn_${turnNumber}`;

  const dominantFaction = (activeParty?.factions || []).find(f => f.active && f.influence > 50 && f.loyalty > 80);

  // Build factions list dynamically from activeParty or fallback
  const factionsList = (activeParty?.factions || []).map(f => {
    // Loyalty decay is 2% per active faction per turn + jealousy factor
    let decay = 2;
    if (dominantFaction && f.key !== dominantFaction.key) {
      decay += 2;
    }
    const decayedLoyalty = Math.max(0, f.loyalty - decay);
    const delegatedProjects = (activeParty?.projects || []).filter(p => p.progressPercent === 100 && p.managingFactionKey === f.key);
    const projectsMapped = delegatedProjects.map(p => ({
      id: p.id,
      projectKey: p.projectKey,
      type: 'project',
      name: p.name || p.projectKey,
      desc: p.yieldDesc || 'Delegated project.',
      icon: p.icon || '🏗️',
      color: 'linear-gradient(135deg, #115e59 0%, #0d9488 100%)',
      isPermanentlyAssigned: true, // Lock projects from previous turns
      frozenTurnsRemaining: p.frozenTurnsRemaining
    }));

    let accentColor = '#ef4444';
    if (f.key === 'youth') accentColor = '#f97316';
    if (f.key === 'trade') accentColor = '#14b8a6';

    const rawPost = f.post;
    const postArray = Array.isArray(rawPost) ? rawPost : (rawPost && rawPost !== 'None' ? [rawPost] : []);
    const postKeys = postArray.map(p => {
      const def = getPostByName(p);
      return def ? def.key : p;
    });

    return {
      id: f.key,
      name: getFactionDisplayName(activeParty?.name, f.key),
      baseLoyalty: decayedLoyalty,
      loyalty: decayedLoyalty,
      influence: f.influence,
      post: postKeys,
      patronage: 0,
      projects: projectsMapped,
      active: f.active,
      accentColor,
      isPostPermanentlyAssigned: postKeys.length > 0, // Lock posts from previous turns
      frozenTurnsRemaining: f.frozenTurnsRemaining,
      frozenPosts: f.frozenPosts,
      frozenPatronageTurns: f.frozenPatronageTurns
    };
  });



  // ----- Projects: completed + unassigned - defined FIRST so buildDeckFromBackendState can use it -----
  const unassignedProjects = (activeParty?.projects || []).filter(
    p => p.progressPercent === 100 && (p.managingFactionKey === 'None' || !p.managingFactionKey)
  );
  const projectCards = unassignedProjects.map(p => ({
    id: p.id || p.projectKey,
    projectKey: p.projectKey,
    type: 'project',
    name: p.name || p.projectKey,
    desc: p.yieldDesc || 'Completed project.',
    icon: p.icon || '🏗️',
    color: 'linear-gradient(135deg, #115e59 0%, #0d9488 100%)'
  }));


  // ----- Build deck from partyManagementState (from backend MongoDB) -----
  const partyMgmtState = turnData?.partyManagementState;

  const buildDeckFromBackendState = () => {
    const cards = [];
    if (partyMgmtState) {
      // Patronage point cards
      const count = partyMgmtState.unallocatedPatronagePoints || 0;
      for (let i = 0; i < count; i++) {
        cards.push({
          id: `pat-${i}`,
          type: 'patronage',
          name: 'Patronage Point',
          desc: 'Increases loyalty by +5%. Yields: +2 Coins, +1 Morale, -1 Corruption, +1 Media Image.',
          icon: '🛡️',
          color: 'linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%)'
        });
      }
      // AVAILABLE post cards
      const availablePosts = (partyMgmtState.posts || []).filter(p => p.status === 'AVAILABLE');
      availablePosts.forEach((sp, i) => {
        const def = getPostByKey(sp.postKey);
        cards.push({
          id: `post-${sp.postKey}-${i}`,
          postKey: sp.postKey,
          type: 'post',
          name: sp.postName,
          desc: def?.desc || `Assigns a leadership role. Boosts loyalty by +${def?.loyaltyBoost || 10}.`,
          icon: def?.icon || '💼',
          color: def?.color || 'linear-gradient(135deg, #581c87 0%, #a855f7 100%)',
          loyaltyBoost: def?.loyaltyBoost || 10,
          coinBonus: def?.coinBonus || 0,
          moraleBonus: def?.moraleBonus || 0,
          mediaBonus: def?.mediaBonus || 0
        });
      });
    } else {
      // Legacy fallback
      cards.push({ id: 'pat-1', type: 'patronage', name: 'Patronage Point', desc: 'Increases loyalty by +5%.', icon: '🛡️', color: 'linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%)' });
      const assignedPosts = (activeParty?.factions || []).flatMap(f => {
        const rawPost = f.post;
        return Array.isArray(rawPost) ? rawPost : (rawPost && rawPost !== 'None' ? [rawPost] : []);
      });
      if (!assignedPosts.includes('SECRETARY') && !assignedPosts.includes('Secretary')) cards.push({ id: 'post-1', postKey: 'SECRETARY', type: 'post', name: 'Secretary', desc: 'Chief administrator. +15 Loyalty, +6 Morale/turn.', icon: '📋', loyaltyBoost: 15, coinBonus: 0, moraleBonus: 6, mediaBonus: 0, color: 'linear-gradient(135deg, #581c87 0%, #a855f7 100%)' });
      if (!assignedPosts.includes('FUND_MANAGER') && !assignedPosts.includes('Fund Manager')) cards.push({ id: 'post-2', postKey: 'FUND_MANAGER', type: 'post', name: 'Fund Manager', desc: 'Oversees finances. +10 Loyalty, +8 Coins/turn.', icon: '💰', loyaltyBoost: 10, coinBonus: 8, moraleBonus: 0, mediaBonus: 0, color: 'linear-gradient(135deg, #581c87 0%, #a855f7 100%)' });
    }
    // Always add unassigned completed projects (defined above)
    cards.push(...projectCards);
    return cards;
  };

  const initialDeck = buildDeckFromBackendState();




const getInitialFactions = (partyState, factionsList) => {
  // Define base static defaults (used only when backend factions list is empty)
  const defaults = [
    { id: 'loyalist', name: 'Loyalists',    baseLoyalty: 75, loyalty: 75, influence: 45, post: [], patronage: 0, projects: [], active: true, accentColor: '#ef4444' },
    { id: 'youth',   name: 'Youth Wing',   baseLoyalty: 75, loyalty: 75, influence: 35, post: [], patronage: 0, projects: [], active: true, accentColor: '#f97316' },
    { id: 'trade',   name: 'Trade Unions', baseLoyalty: 75, loyalty: 75, influence: 20, post: [], patronage: 0, projects: [], active: true, accentColor: '#14b8a6' }
  ];

  // Base list: prefer live backend factions, fall back to static defaults
  const baseList = (factionsList && factionsList.length > 0) ? factionsList : defaults;

  // If no partyManagementState, return base list as-is
  if (!partyState) return baseList;

  // Enrich each faction with persisted patronage (keyed by faction key) and assigned posts
  return baseList.map(faction => {
    // allocatedPatronagePoints is stored by faction key (e.g. 'veteran', 'youth', 'trade')
    const livePatronage = partyState.allocatedPatronagePoints?.[faction.id] ?? faction.patronage ?? 0;

    // Posts are stored in partyState.posts (ScheduledPost list) with assignedFactionKey
    const assignedPostsForFaction = (partyState.posts || [])
      .filter(p => p.status === 'ASSIGNED' && p.assignedFactionKey === faction.id)
      .map(p => p.postKey);

    const rawPost = faction.post;
    const existingPosts = Array.isArray(rawPost) ? rawPost : (rawPost && rawPost !== 'None' ? [rawPost] : []);
    
    // Normalize to keys
    const normalizedExisting = existingPosts.map(p => {
      const def = getPostByName(p);
      return def ? def.key : p;
    });

    const allPosts = Array.from(new Set([...normalizedExisting, ...assignedPostsForFaction]));

    return {
      ...faction,
      patronage: livePatronage,
      post: allPosts
    };
  });
};


  const initialFactions = getInitialFactions(partyMgmtState, factionsList);

  // Load state from localStorage or fallback to defaults
  const [factions, setFactions] = useState(() => {
    const saved = localStorage.getItem(storageKey);
    if (saved) {
      try {
        const parsed = JSON.parse(saved);
        if (parsed.factions) return parsed.factions;
      } catch (e) {
        console.error("Failed to parse factions state from localStorage", e);
      }
    }
    return initialFactions;
  });

const [deck, setDeck] = useState(() => {
  const saved = localStorage.getItem(storageKey);
  if (saved) {
    try {
      const parsed = JSON.parse(saved);
      if (parsed.deck) return parsed.deck;
    } catch (e) {
      console.error("Failed to parse deck state from localStorage", e);
    }
  }

  // ONLY run this heavy backend-to-deck parser on initial clean turn load!
  return buildDeckFromBackendState();
});

  // Tracks which faction (id) received which post key this turn: { factionId -> postKey }
  const [assignedPostKeys, setAssignedPostKeys] = useState(() => {
    const saved = localStorage.getItem(storageKey);
    if (saved) {
      try { return JSON.parse(saved).assignedPostKeys || {}; } catch (e) { return {}; }
    }
    return {};
  });

  const [history, setHistory] = useState(() => {
    const saved = localStorage.getItem(storageKey);
    if (saved) {
      try {
        const parsed = JSON.parse(saved);
        if (parsed.history) return parsed.history;
      } catch (e) {
        console.error("Failed to parse history state from localStorage", e);
      }
    }
    return [];
  });

  const [factionCrisisChoice, setFactionCrisisChoice] = useState(() => {
    const saved = localStorage.getItem(storageKey);
    if (saved) {
      try {
        const parsed = JSON.parse(saved);
        if (parsed.factionCrisisChoice) return parsed.factionCrisisChoice;
      } catch (e) {
        console.error("Failed to parse factionCrisisChoice state from localStorage", e);
      }
    }
    return null;
  });


  // Lock state: once locked, the allocations are saved to MongoDB and cannot be changed.
  // Persisted in localStorage so the locked state survives page refresh / re-entry.
  const [isLocked, setIsLocked] = useState(() => {
    const saved = localStorage.getItem(storageKey);
    if (saved) {
      try { return JSON.parse(saved).isLocked === true; } catch (e) { return false; }
    }
    return false;
  });
  const [lockError, setLockError] = useState(null);
  const [isLocking, setIsLocking] = useState(false);
  const confirmBtnRef = useRef(null);
  const allCardsAssigned = deck.length === 0 && !isLocked;

  // Auto-scroll to Confirm button when all cards are assigned
  useEffect(() => {
    if (allCardsAssigned) {
      const timer = setTimeout(() => {
        confirmBtnRef.current?.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }, 200);
      return () => clearTimeout(timer);
    }
  }, [allCardsAssigned]);

  const [showCrisisModal, setShowCrisisModal] = useState(false);

  // Save state to localStorage (persists across refresh for the current turn)
  useEffect(() => {
  if (isLocked) {
    localStorage.setItem(storageKey, JSON.stringify({ factions, deck, history, factionCrisisChoice, assignedPostKeys, isLocked }));
    }
  }, [factions, deck, history, factionCrisisChoice, assignedPostKeys, isLocked, storageKey]);


  const handleLock = useCallback(async () => {
    if (isLocked || isLocking) return;
    setIsLocking(true);
    setLockError(null);
    try {
      const partyId = activeParty?.id || turnData?.activeHumanPartyId;
      const gameId = turnData?.gameId;
      if (!partyId || !gameId) throw new Error('Missing game or party ID');

      // Build structured payload
      const patronageUsed = factions.reduce((sum, f) => sum + (f.patronage || 0), 0);
      const postAssignments = assignedPostKeys;
      const factionsPayload = factions.map(f => ({
        key: f.id,
        loyalty: f.loyalty,
        influence: f.influence,
        post: f.post,
        patronage: f.patronage,
        active: f.active
      }));
      // Project assignments: collect from all factions
      const projects = {};
      factions.forEach(f => {
        (f.projects || []).forEach(p => { projects[p.id || p.projectKey] = f.id; });
      });

      await lockPartyManagement(gameId, partyId, { patronageUsed, postAssignments, factions: factionsPayload, projects });
      setIsLocked(true);
      // Mark this action complete
      if (setSelectedIssueOptionKey) setSelectedIssueOptionKey('mock_done');
    } catch (err) {
      console.error('[PartyMgmt] Lock failed:', err);
      setLockError(err.message || 'Failed to lock allocations. Please try again.');
    } finally {
      setIsLocking(false);
    }
  }, [isLocked, isLocking, factions, assignedPostKeys, activeParty, turnData, setSelectedIssueOptionKey]);

  // Automatically open the crisis modal if there's an active crisis and no choice is selected yet
  useEffect(() => {
    if (activeParty?.activeFactionCrisisKey && !factionCrisisChoice) {
      setShowCrisisModal(true);
    }
  }, [activeParty, factionCrisisChoice]);

  // Sync completed projects into the draw deck and unlock if there are unassigned projects
  useEffect(() => {
    const assignedProjectKeys = factions.flatMap(f => (f.projects || []).map(p => p.projectKey));
    const deckProjectKeys = deck.filter(c => c.type === 'project').map(c => c.projectKey);
    const completedProjects = (activeParty?.projects || []).filter(p => p.progressPercent === 100);
    
    const newUnassignedProjects = completedProjects.filter(
      p => !assignedProjectKeys.includes(p.projectKey) && !deckProjectKeys.includes(p.projectKey)
    );

    if (newUnassignedProjects.length > 0) {
      setIsLocked(false);
      
      const newCards = newUnassignedProjects.map(p => ({
        id: p.id || p.projectKey,
        projectKey: p.projectKey,
        type: 'project',
        name: p.name || p.projectKey,
        desc: p.yieldDesc || 'Completed project.',
        icon: p.icon || '🏗️',
        color: 'linear-gradient(135deg, #115e59 0%, #0d9488 100%)'
      }));

      setDeck(prev => [...newCards, ...prev]);
    }
  }, [activeParty?.projects, factions, deck]);

  // Moves page status to ready ONLY after locked is hit (isLocked is true)
  useEffect(() => {
    if (setSelectedIssueOptionKey) {
      if (isLocked) {
        setSelectedIssueOptionKey('mock_done');
      } else {
        setSelectedIssueOptionKey('');
      }
    }
  }, [isLocked, setSelectedIssueOptionKey]);

  const totalCardsCount = initialDeck.length;

  // Push state to undo history
  const pushHistory = (currentDeck, currentFactions) => {
    setHistory(prev => [...prev, { deck: [...currentDeck], factions: JSON.parse(JSON.stringify(currentFactions)) }]);
  };

  // Undo last allocation
  const handleUndo = () => {
    if (history.length === 0) return;
    const lastState = history[history.length - 1];
    setDeck(lastState.deck);
    setFactions(lastState.factions);
    setHistory(prev => prev.slice(0, -1));
  };

  const updateFactionsState = (rawFactions) => {
    const activeFactions = rawFactions.filter(f => f.active);
    const yieldSums = {};
    let totalYieldSum = 0;

    activeFactions.forEach(f => {
      const y = calculateYield(f);
      const sum = Math.max(0, y.coins + y.support * 10 + y.morale + Math.abs(y.corruption) + y.media);
      yieldSums[f.id] = sum;
      totalYieldSum += sum;
    });

    let updatedFactions = rawFactions;
    if (totalYieldSum > 0 && activeFactions.length > 0) {
      let remainingInfluence = 100 - activeFactions.length;
      const quotas = activeFactions.map(f => {
        const exact = (yieldSums[f.id] / totalYieldSum) * remainingInfluence;
        return { id: f.id, exact, int: Math.floor(exact), remainder: exact - Math.floor(exact) };
      });
      let allocated = quotas.reduce((acc, q) => acc + q.int, 0);
      quotas.sort((a, b) => b.remainder - a.remainder);
      for (let i = 0; i < remainingInfluence - allocated; i++) {
        quotas[i].int += 1;
      }
      updatedFactions = rawFactions.map(f => {
        if (!f.active) return f;
        const quota = quotas.find(q => q.id === f.id);
        return { ...f, influence: 1 + quota.int };
      });
    } else if (activeFactions.length > 0) {
      const base = Math.floor(100 / activeFactions.length);
      const rem = 100 % activeFactions.length;
      let i = 0;
      updatedFactions = rawFactions.map(f => {
        if (!f.active) return f;
        const inf = base + (i < rem ? 1 : 0);
        i++;
        return { ...f, influence: inf };
      });
    }

    setFactions(updatedFactions);
  };

  // Reset all allocations
  const handleReset = () => {
    updateFactionsState(initialFactions);
    setDeck(initialDeck);
    setHistory([]);
    setAssignedPostKeys({});
  };

  // Allocate top card to a faction
  const handleAllocate = (factionId) => {
    if (deck.length === 0) return;
    const activeFactions = factions.filter(f => f.active);
    const targetFaction = activeFactions.find(f => f.id === factionId);
    if (!targetFaction) return;

    pushHistory(deck, factions);

    const cardToAllocate = deck[0];
    const newDeck = deck.slice(1);

    const updatedFactions = factions.map(f => {
      if (f.id === factionId) {
        let loyaltyChange = 0;
        let postVal = f.post;
        let patronageVal = f.patronage;
        let projectsVal = [...f.projects];

        if (cardToAllocate.type === 'patronage') {
          patronageVal += 1;
          loyaltyChange = 5;
        } else if (cardToAllocate.type === 'post') {
          const existingPosts = Array.isArray(postVal) ? postVal : (postVal && postVal !== 'None' ? [postVal] : []);
          if (!existingPosts.includes(cardToAllocate.postKey)) {
            postVal = [...existingPosts, cardToAllocate.postKey];
          } else {
            postVal = existingPosts;
          }
          // Use dynamic loyaltyBoost from postsConfig - look up by postKey or name
          const postDef = cardToAllocate.postKey
            ? getPostByKey(cardToAllocate.postKey)
            : getPostByName(cardToAllocate.name);
          loyaltyChange = postDef?.loyaltyBoost ?? 10;
        } else if (cardToAllocate.type === 'project') {
          projectsVal.push(cardToAllocate);
        }

        const newLoyalty = Math.min(100, Math.max(0, f.loyalty + loyaltyChange));
        return {
          ...f,
          patronage: patronageVal,
          post: postVal,
          projects: projectsVal,
          loyalty: newLoyalty
        };
      }
      return f;
    });

    // Track post key assignment for backend submission
    if (cardToAllocate.type === 'post' && cardToAllocate.postKey) {
      setAssignedPostKeys(prev => ({ ...prev, [cardToAllocate.postKey]: factionId }));
    }

    setDeck(newDeck);
    updateFactionsState(updatedFactions);
  };

  // Purge / Dissolve faction
  const handleDissolve = (factionId) => {
    const dissolved = factions.find(f => f.id === factionId);
    if (!dissolved) return;

    if (window.confirm(`Dissolve ${dissolved.name}? All allocated cards will be returned to the Draw Deck stack, and its influence will be distributed to active factions.`)) {
      pushHistory(deck, factions);

      // Gather cards to return
      const cardsToReturn = [];
      for (let i = 0; i < dissolved.patronage; i++) {
        cardsToReturn.push({ id: `pat-refund-${factionId}-${i}-${Date.now()}`, type: 'patronage', name: 'Patronage Point', desc: 'Increases loyalty by +5%. Yields: +2 Coins, +1 Morale, -1 Corruption, +1 Media Image.', icon: '🛡️', color: 'linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%)' });
      }
      if (Array.isArray(dissolved.post)) {
        dissolved.post.forEach(postKey => {
          const postCardDef = initialDeck.find(d => d.postKey === postKey);
          if (postCardDef) {
            cardsToReturn.push({ ...postCardDef, id: `post-refund-${factionId}-${postKey}-${Date.now()}` });
          }
        });
      } else if (dissolved.post && dissolved.post !== 'None') {
        const postCardDef = initialDeck.find(d => d.name === dissolved.post);
        if (postCardDef) {
          cardsToReturn.push({ ...postCardDef, id: `post-refund-${factionId}-${Date.now()}` });
        }
      }
      dissolved.projects.forEach(proj => {
        cardsToReturn.push(proj);
      });

      // Distribute influence
      const activeOthers = factions.filter(f => f.active && f.id !== factionId);
      const baseShare = activeOthers.length > 0 ? Math.floor(dissolved.influence / activeOthers.length) : 0;
      const remShare = activeOthers.length > 0 ? dissolved.influence % activeOthers.length : 0;
      let i = 0;

      const updatedFactions = factions.map(f => {
        if (f.id === factionId) {
          return {
            ...f,
            active: false,
            loyalty: 0,
            influence: 0,
            patronage: 0,
            post: 'None',
            projects: []
          };
        }
        if (f.active) {
          const inf = f.influence + baseShare + (i < remShare ? 1 : 0);
          i++;
          return {
            ...f,
            influence: inf,
            // Drastic shift drops loyalty slightly of other factions (-10 loyalty due to internal disruption)
            loyalty: Math.max(0, f.loyalty - 10)
          };
        }
        return f;
      });

      setDeck(prev => [...cardsToReturn, ...prev]);
      updateFactionsState(updatedFactions);
    }
  };

  // Calculate faction yield multiplier based on loyalty
  const getMultiplierInfo = (loyalty) => {
    if (loyalty >= 90) return { factor: 2.0, badge: '🏆 Synergy (200%)', color: '#22c55e' };
    if (loyalty >= 80) return { factor: 1.5, badge: '⭐ High Trust (150%)', color: '#3b82f6' };
    if (loyalty >= 50) return { factor: 1.0, badge: '✅ Co-op (100%)', color: 'var(--card-text, #64748b)' };
    if (loyalty >= 30) return { factor: 0.5, badge: '⚠️ Friction (50%)', color: '#f59e0b' };
    return { factor: 0.0, badge: '⛔ Stoppage (0%)', color: '#ef4444' };
  };

  // Calculate individual faction yields - uses dynamic config values
  function calculateYield(faction) {
    if (!faction.active) return { coins: 0, support: 0, morale: 0, corruption: 0, media: 0 };
    const mult = getMultiplierInfo(faction.loyalty).factor;

    const patronageCoins = faction.patronage * 2;
    const patronageMorale = faction.patronage * 1;
    const patronageCorruption = faction.patronage * -1;
    const patronageMedia = faction.patronage * 1;

    let postCoins = 0;
    let postMorale = 0;
    let postMedia = 0;

    const posts = Array.isArray(faction.post) ? faction.post : (faction.post && faction.post !== 'None' ? [faction.post] : []);
    posts.forEach(pKey => {
      const postDef = getPostByKey(pKey) || getPostByName(pKey);
      if (postDef) {
        postCoins += postDef.coinBonus || 0;
        postMorale += postDef.moraleBonus || 0;
        postMedia += postDef.mediaBonus || 0;
      }
    });

    let projectCoins = 0;
    let projectMorale = 0;
    let projectMedia = 0;
    let projectCorruption = 0;
    let projectSupport = 0;

    (faction.projects || []).forEach(proj => {
      const pConfig = projectDefs[proj.projectKey];
      if (pConfig) {
        projectCoins += pConfig.benefitCoins || 0;
        projectMorale += pConfig.benefitMorale || 0;
        projectMedia += pConfig.benefitMedia || 0;
        projectCorruption += pConfig.benefitCorruption || 0;
        projectSupport += (pConfig.benefitSupport || 0) * 0.01;
      }
    });

    const baseCoins = patronageCoins + postCoins + projectCoins;
    const baseMorale = patronageMorale + postMorale + projectMorale;
    const baseCorruption = patronageCorruption + projectCorruption;
    const baseMedia = patronageMedia + postMedia + projectMedia;
    const baseSupport = faction.loyalty >= 50
      ? (faction.influence * 0.01) + projectSupport
      : -(faction.influence * 0.01) + projectSupport;

    return {
      coins: Math.round(baseCoins * mult),
      support: parseFloat((baseSupport * mult).toFixed(1)),
      morale: Math.round(baseMorale * mult),
      corruption: baseCorruption < 0 ? Math.round(baseCorruption * mult) : Math.round(baseCorruption * (2 - mult)),
      media: Math.round(baseMedia * mult)
    };
  }


  // Sum combined yields
  const totalYields = factions.reduce((acc, f) => {
    if (!f.active) return acc;
    const y = calculateYield(f);
    return {
      coins: acc.coins + y.coins,
      support: acc.support + y.support,
      morale: acc.morale + y.morale,
      corruption: acc.corruption + y.corruption,
      media: acc.media + y.media
    };
  }, { coins: 0, support: 0, morale: 0, corruption: 0, media: 0 });

  // Check active faction perks matching backend requirements
  let veteranPerkActive = false;
  let youthPerkActive = false;
  let tradePerkActive = false;

  factions.forEach(f => {
    if (!f.active) return;
    if (f.id === 'loyalist' && f.loyalty >= 80 && f.influence >= 50) {
      veteranPerkActive = true;
    } else if (f.id === 'youth' && f.loyalty >= 80 && f.influence >= 40) {
      youthPerkActive = true;
    } else if (f.id === 'trade' && f.loyalty >= 80 && f.influence >= 40) {
      tradePerkActive = true;
    }
  });

  let perkCoins = 0;
  let perkSupport = 0;
  let perkMorale = 0;
  let perkCorruption = 0;
  let perkMedia = 0;

  if (veteranPerkActive) {
    perkCoins += 25;
    perkSupport += 3.0;
  }
  if (youthPerkActive) {
    perkMorale += 5;
    perkSupport += 3.0;
    perkMedia += 5;
  }
  if (tradePerkActive) {
    perkCorruption -= 5;
  }

  // Apply caps to negative yields only! Positive yields are completely uncapped.
  const finalCoins = totalYields.coins + perkCoins;
  const finalSupport = Math.ceil(totalYields.support + perkSupport);
  const finalMedia = totalYields.media + perkMedia;
  
  const rawMorale = totalYields.morale + perkMorale;
  const finalMorale = rawMorale >= 0 ? rawMorale : Math.max(-5, rawMorale);
  
  const rawCorruption = totalYields.corruption + perkCorruption;
  const finalCorruption = rawCorruption <= 0 ? Math.max(-5, rawCorruption) : Math.min(5, rawCorruption);

  const topCard = deck[0];
  const activeFactionsList = factions.filter(f => f.active);
  const remainingCardsCount = deck.length;

  return (
    <div className="action3-warroom-root" style={{
      fontFamily: 'Montserrat, system-ui, -apple-system, sans-serif',
      color: '#E6EDF3'
    }}>
      <style>{`
        @keyframes drawCardAnimation {
          0% { transform: scale(0.95); opacity: 0.8; }
          100% { transform: scale(1); opacity: 1; }
        }
        @keyframes rebelPulse {
          0% { border-color: #ef4444; box-shadow: 0 0 8px rgba(239, 68, 68, 0.4); }
          50% { border-color: #dc2626; box-shadow: 0 0 20px rgba(239, 68, 68, 0.8); }
          100% { border-color: #ef4444; box-shadow: 0 0 8px rgba(239, 68, 68, 0.4); }
        }
        @keyframes perkGold {
          0% { box-shadow: 0 0 6px rgba(234, 179, 8, 0.4); }
          50% { box-shadow: 0 0 16px rgba(234, 179, 8, 0.7); }
          100% { box-shadow: 0 0 6px rgba(234, 179, 8, 0.4); }
        }
        .rebel-border-flash {
          animation: rebelPulse 1.5s infinite ease-in-out !important;
        }
        .gold-perk-glow {
          animation: perkGold 2s infinite ease-in-out !important;
          border: 1.5px solid #eab308 !important;
        }
        @keyframes buttonPulseFlash {
          0% { background: rgba(56, 189, 248, 0.15); box-shadow: 0 0 4px rgba(56, 189, 248, 0.2); }
          50% { background: rgba(56, 189, 248, 0.40); box-shadow: 0 0 14px rgba(56, 189, 248, 0.6); }
          100% { background: rgba(56, 189, 248, 0.15); box-shadow: 0 0 4px rgba(56, 189, 248, 0.2); }
        }
        .pulse-flash-btn {
          animation: buttonPulseFlash 1.5s infinite ease-in-out;
        }
      `}</style>

      {/* Rebellious Faction Crisis Banner */}
      {activeParty?.activeFactionCrisisKey && (
        <div style={{
          background: 'linear-gradient(135deg, #7f1d1d 0%, #b91c1c 100%)',
          border: '1.5px solid #ef4444',
          borderRadius: '12px',
          padding: '14px 18px',
          color: '#ffffff',
          marginBottom: '20px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          boxShadow: '0 4px 15px rgba(239, 68, 68, 0.3)',
          userSelect: 'none'
        }}>
          <div>
            <h4 style={{ margin: 0, fontSize: '15px', fontWeight: 900, display: 'flex', alignItems: 'center', gap: '8px', letterSpacing: '0.04em' }}>
              ⚠️ REBELLIOUS FACTION ULTIMATUM
            </h4>
            <p style={{ margin: '4px 0 0 0', fontSize: '12px', color: 'rgba(255,255,255,0.9)', lineHeight: 1.4 }}>
              The rebellious <b>{activeParty.factions.find(f => f.key === activeParty.activeFactionCrisisKey)?.name || 'Faction'}</b> has issued an ultimatum!
              {factionCrisisChoice ? (
                <span> Selected Resolution: <b style={{ textTransform: 'uppercase', color: '#facc15' }}>Option {factionCrisisChoice}</b></span>
              ) : (
                <span> You must resolve this crisis before completing your turn.</span>
              )}
            </p>
          </div>
          <button
            onClick={() => setShowCrisisModal(true)}
            style={{
              background: '#ffffff',
              border: 'none',
              borderRadius: '8px',
              color: '#b91c1c',
              padding: '8px 14px',
              fontSize: '12px',
              fontWeight: 900,
              cursor: 'pointer',
              touchAction: 'manipulation',
              transition: 'all 0.15s'
            }}
          >
            {factionCrisisChoice ? 'CHANGE CHOICE' : 'RESOLVE CRISIS'}
          </button>
        </div>
      )}

      {/* Faction Crisis Modal Overlay (Dark War Room Backdrop & Touch Friendly) */}
      {showCrisisModal && activeParty?.activeFactionCrisisKey && (
        <div
          style={{
            position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
            zIndex: 99999,
            backgroundColor: 'rgba(0, 0, 0, 0.85)',
            backdropFilter: 'blur(8px)',
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            padding: '16px'
          }}
          onClick={() => setShowCrisisModal(false)}
        >
          <div
            style={{
              background: 'linear-gradient(145deg, #1e293b, #0f172a)',
              borderRadius: '16px',
              maxWidth: '620px',
              width: '100%',
              maxHeight: '85vh',
              overflowY: 'auto',
              boxShadow: '0 25px 50px rgba(0, 0, 0, 0.6)',
              border: '2px solid #ef4444',
              color: '#E6EDF3'
            }}
            onClick={(e) => e.stopPropagation()}
          >
            {/* Header */}
            <div style={{
              background: 'linear-gradient(135deg, #7f1d1d 0%, #991b1b 100%)',
              padding: '16px 20px',
              position: 'relative',
              borderBottom: '1px solid rgba(255,255,255,0.1)'
            }}>
              <h3 style={{ margin: '0 0 4px 0', fontSize: '17px', fontWeight: 900, letterSpacing: '0.04em', color: '#fff', paddingRight: '40px' }}>
                🚨 ULTIMATUM: Rebellious Faction Crisis
              </h3>
              <p style={{ margin: 0, fontSize: '12px', color: 'rgba(255,255,255,0.85)', lineHeight: 1.4 }}>
                The rebellious faction <b>{activeParty.factions.find(f => f.key === activeParty.activeFactionCrisisKey)?.name || 'Faction'}</b> is threatening a party split!
              </p>
              <button
                onClick={() => setShowCrisisModal(false)}
                style={{
                  position: 'absolute', top: '14px', right: '14px',
                  background: 'rgba(255,255,255,0.15)', border: 'none',
                  color: '#ffffff', borderRadius: '50%', width: '32px', height: '32px',
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  cursor: 'pointer', fontSize: '16px', touchAction: 'manipulation'
                }}
                aria-label="Close"
              >
                ✕
              </button>
            </div>

            {/* Options Body */}
            <div style={{ padding: '16px', display: 'flex', flexDirection: 'column', gap: '12px' }}>
              {/* Option A */}
              <div
                onClick={() => { setFactionCrisisChoice('A'); setShowCrisisModal(false); }}
                style={{
                  border: factionCrisisChoice === 'A' ? '2px solid #ef4444' : '1px solid rgba(255,255,255,0.1)',
                  background: factionCrisisChoice === 'A' ? 'rgba(239, 68, 68, 0.12)' : 'rgba(255,255,255,0.03)',
                  borderRadius: '12px', padding: '14px', cursor: 'pointer', touchAction: 'manipulation'
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
                  <strong style={{ fontSize: '14px', color: '#fff', fontWeight: 900 }}>Option A: Make Concessions</strong>
                  <span style={{ fontSize: '9px', fontWeight: 900, background: '#38BDF8', color: '#0f172a', padding: '2px 8px', borderRadius: '4px' }}>CONCEDE</span>
                </div>
                <p style={{ margin: 0, fontSize: '12px', color: '#94a3b8', lineHeight: 1.4 }}>
                  Offer high-level posts and policy promises to buy their loyalty.
                </p>
                <div style={{ marginTop: '8px', fontSize: '11px', fontWeight: 800, color: '#F87171' }}>
                  Cost: -50 Coins, -20 Media Image | Effect: Restores Loyalty to 60%; reduces Influence by 10%.
                </div>
              </div>

              {/* Option B */}
              <div
                onClick={() => { setFactionCrisisChoice('B'); setShowCrisisModal(false); }}
                style={{
                  border: factionCrisisChoice === 'B' ? '2px solid #ef4444' : '1px solid rgba(255,255,255,0.1)',
                  background: factionCrisisChoice === 'B' ? 'rgba(239, 68, 68, 0.12)' : 'rgba(255,255,255,0.03)',
                  borderRadius: '12px', padding: '14px', cursor: 'pointer', touchAction: 'manipulation'
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
                  <strong style={{ fontSize: '14px', color: '#fff', fontWeight: 900 }}>Option B: Purge Rebellious Leaders</strong>
                  <span style={{ fontSize: '9px', fontWeight: 900, background: '#F59E0B', color: '#0f172a', padding: '2px 8px', borderRadius: '4px' }}>PURGE</span>
                </div>
                <p style={{ margin: 0, fontSize: '12px', color: '#94a3b8', lineHeight: 1.4 }}>
                  Exile rebellious dissenters from the party structure.
                </p>
                <div style={{ marginTop: '8px', fontSize: '11px', fontWeight: 800, color: '#F87171' }}>
                  Cost: -20 Party Morale, -5% Voter Support | Effect: Restores Loyalty to 50%; caps Influence at 20%.
                </div>
              </div>

              {/* Option C */}
              <div
                onClick={() => { setFactionCrisisChoice('C'); setShowCrisisModal(false); }}
                style={{
                  border: factionCrisisChoice === 'C' ? '2px solid #ef4444' : '1px solid rgba(255,255,255,0.1)',
                  background: factionCrisisChoice === 'C' ? 'rgba(239, 68, 68, 0.12)' : 'rgba(255,255,255,0.03)',
                  borderRadius: '12px', padding: '14px', cursor: 'pointer', touchAction: 'manipulation'
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
                  <strong style={{ fontSize: '14px', color: '#fff', fontWeight: 900 }}>Option C: Force a Party Split</strong>
                  <span style={{ fontSize: '9px', fontWeight: 900, background: '#EF4444', color: '#ffffff', padding: '2px 8px', borderRadius: '4px' }}>SPLIT</span>
                </div>
                <p style={{ margin: 0, fontSize: '12px', color: '#94a3b8', lineHeight: 1.4 }}>
                  Denounce them publicly. The faction will defect, splitting your voter base.
                </p>
                <div style={{ marginTop: '8px', fontSize: '11px', fontWeight: 800, color: '#F87171' }}>
                  Cost: -15% Voter Support, -30 Party Morale | Effect: Faction permanently defuses and is deleted.
                </div>
              </div>
            </div>

            {/* Footer */}
            <div style={{
              padding: '12px 16px', display: 'flex', justifyContent: 'flex-end',
              borderTop: '1px solid rgba(255,255,255,0.08)', gap: '10px'
            }}>
              <button
                onClick={() => setShowCrisisModal(false)}
                style={{
                  background: 'rgba(255,255,255,0.1)', color: '#ffffff', border: 'none',
                  borderRadius: '8px', padding: '10px 16px', fontSize: '12px', fontWeight: 800,
                  cursor: 'pointer', touchAction: 'manipulation'
                }}
              >
                DISMISS
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Main Grid: Card Draw Stack (Left) + Combined Yield Command HUD (Right) */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
        gap: '16px',
        marginBottom: '20px'
      }}>
        {/* Drawn Card Interface (Playing Cards Deck Stack) */}
        {topCard ? (
          <div style={{
            background: topCard.color || 'linear-gradient(135deg, #1e3a8a, #3b82f6)',
            borderRadius: '14px',
            padding: '18px 20px',
            color: '#ffffff',
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'space-between',
            minHeight: '220px',
            boxShadow: '0 8px 24px rgba(0,0,0,0.4)',
            border: '2px solid rgba(255,255,255,0.2)',
            animation: 'drawCardAnimation 0.2s ease-out'
          }}>
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span style={{
                  fontSize: '10px',
                  fontWeight: 900,
                  background: 'rgba(255,255,255,0.25)',
                  color: '#ffffff',
                  padding: '3px 9px',
                  borderRadius: '6px',
                  textTransform: 'uppercase',
                  letterSpacing: '0.06em'
                }}>
                  {topCard.type}
                </span>
                <span style={{ fontSize: '11px', fontWeight: 800, background: 'rgba(0,0,0,0.25)', padding: '3px 10px', borderRadius: '12px' }}>
                  🃏 {totalCardsCount - remainingCardsCount + 1} of {totalCardsCount} ({remainingCardsCount - 1} left)
                </span>
              </div>
              <h4 style={{ margin: '14px 0 6px 0', fontSize: '19px', fontWeight: 900 }}>
                {topCard.icon} {topCard.name}
              </h4>
              <p style={{ margin: 0, fontSize: '12.5px', color: 'rgba(255,255,255,0.9)', lineHeight: 1.4 }}>
                {topCard.desc}
              </p>
            </div>

            {/* Faction Target Buttons */}
            <div style={{ marginTop: '16px' }}>
              <div style={{ fontSize: '10px', fontWeight: 900, color: 'rgba(255,255,255,0.85)', marginBottom: '8px', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                TAP FACTION TO ASSIGN:
              </div>
              <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
                {activeFactionsList.map(f => (
                  <button
                    key={f.id}
                    type="button"
                    onClick={() => handleAllocate(f.id)}
                    className="pulse-flash-btn"
                    style={{
                      flex: 1,
                      minWidth: '80px',
                      padding: '10px 12px',
                      border: 'none',
                      borderRadius: '8px',
                      color: '#ffffff',
                      fontSize: '12px',
                      fontWeight: 900,
                      cursor: 'pointer',
                      touchAction: 'manipulation',
                      whiteSpace: 'nowrap',
                      textOverflow: 'ellipsis',
                      overflow: 'hidden'
                    }}
                  >
                    {f.name}
                  </button>
                ))}
              </div>
            </div>
          </div>
        ) : (
          <div style={{
            background: 'rgba(34, 197, 94, 0.08)',
            border: '2px solid #22c55e',
            borderRadius: '14px',
            padding: '24px',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            textAlign: 'center',
            minHeight: '220px'
          }}>
            <span style={{ fontSize: '36px', marginBottom: '8px' }}>✅</span>
            <h4 style={{ margin: 0, fontSize: '16px', fontWeight: 900, color: '#4ADE80' }}>
              ALL RESOURCE CARDS ALLOCATED
            </h4>
            <p style={{ margin: '6px 0 0 0', fontSize: '12px', color: '#94a3b8' }}>
              All turn cards have been distributed to factions. You can lock allocations now.
            </p>
          </div>
        )}

        {/* Combined Yield Command HUD */}
        <div style={{
          background: 'linear-gradient(145deg, #1e293b, #0f172a)',
          border: '1.5px solid rgba(255,255,255,0.12)',
          borderRadius: '14px',
          padding: '16px',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'space-between',
          minHeight: '220px'
        }}>
          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
              <h5 style={{ margin: 0, color: '#38BDF8', fontSize: '12px', fontWeight: 900, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                📈 COMBINED TURN YIELDS
              </h5>
              <span style={{ fontSize: '10px', color: '#7D8590', fontWeight: 700 }}>PROJECTED NET</span>
            </div>

            <div style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(2, 1fr)',
              gap: '8px'
            }}>
              <div style={{ background: 'rgba(0,0,0,0.3)', border: '1px solid rgba(255,255,255,0.08)', padding: '8px 10px', borderRadius: '8px' }}>
                <span style={{ fontSize: '10px', color: '#7D8590', display: 'block', textTransform: 'uppercase' }}>Coins</span>
                <strong style={{ fontSize: '15px', color: '#4ADE80' }}>+{finalCoins} 💰</strong>
              </div>
              <div style={{ background: 'rgba(0,0,0,0.3)', border: '1px solid rgba(255,255,255,0.08)', padding: '8px 10px', borderRadius: '8px' }}>
                <span style={{ fontSize: '10px', color: '#7D8590', display: 'block', textTransform: 'uppercase' }}>Support</span>
                <strong style={{ fontSize: '15px', color: '#38BDF8' }}>+{finalSupport}% 📈</strong>
              </div>
              <div style={{ background: 'rgba(0,0,0,0.3)', border: '1px solid rgba(255,255,255,0.08)', padding: '8px 10px', borderRadius: '8px' }}>
                <span style={{ fontSize: '10px', color: '#7D8590', display: 'block', textTransform: 'uppercase' }}>Morale</span>
                <strong style={{ fontSize: '15px', color: finalMorale < 0 ? '#F87171' : '#F43F5E' }}>
                  {finalMorale > 0 ? '+' : ''}{finalMorale} ✊
                </strong>
              </div>
              <div style={{ background: 'rgba(0,0,0,0.3)', border: '1px solid rgba(255,255,255,0.08)', padding: '8px 10px', borderRadius: '8px' }}>
                <span style={{ fontSize: '10px', color: '#7D8590', display: 'block', textTransform: 'uppercase' }}>Corruption</span>
                <strong style={{ fontSize: '15px', color: finalCorruption > 0 ? '#F87171' : '#4ADE80' }}>
                  {finalCorruption > 0 ? '+' : ''}{finalCorruption} ⚖️
                </strong>
              </div>
              <div style={{ background: 'rgba(0,0,0,0.3)', border: '1px solid rgba(255,255,255,0.08)', padding: '8px 10px', borderRadius: '8px', gridColumn: 'span 2' }}>
                <span style={{ fontSize: '10px', color: '#7D8590', display: 'block', textTransform: 'uppercase' }}>Media Image</span>
                <strong style={{ fontSize: '15px', color: '#EC4899' }}>+{finalMedia} 📢</strong>
              </div>
            </div>
          </div>

          {/* Action Buttons (Undo & Lock Allocations) */}
          <div style={{ display: 'flex', marginTop: '14px', gap: '8px', alignItems: 'center' }}>
            <button
              type="button"
              onClick={handleUndo}
              disabled={history.length === 0 || isLocked}
              style={{
                padding: '10px 14px',
                background: 'rgba(255,255,255,0.05)',
                border: '1px solid rgba(255,255,255,0.15)',
                color: (history.length > 0 && !isLocked) ? '#ffffff' : '#64748b',
                borderRadius: '8px',
                fontWeight: 800,
                cursor: (history.length > 0 && !isLocked) ? 'pointer' : 'default',
                fontSize: '12px',
                touchAction: 'manipulation'
              }}
            >
              ↩ UNDO
            </button>

            <button
              ref={confirmBtnRef}
              type="button"
              onClick={handleLock}
              disabled={isLocked || isLocking}
              style={{
                flex: 1,
                padding: '10px 16px',
                background: isLocked
                  ? 'linear-gradient(135deg, #16a34a, #15803d)'
                  : allCardsAssigned
                  ? 'linear-gradient(135deg, #0284c7, #0369a1)'
                  : 'linear-gradient(135deg, #2563eb, #1d4ed8)',
                border: 'none',
                color: '#ffffff',
                fontWeight: 900,
                borderRadius: '8px',
                cursor: isLocked ? 'default' : 'pointer',
                fontSize: '13px',
                touchAction: 'manipulation',
                letterSpacing: '0.04em',
                boxShadow: '0 4px 12px rgba(0,0,0,0.3)',
                opacity: isLocking ? 0.7 : 1
              }}
            >
              {isLocking ? '⏳ SAVING...' : isLocked ? '✅ ALLOCATIONS LOCKED' : '🔒 LOCK ALLOCATIONS'}
            </button>
          </div>
        </div>
      </div>

      {/* FACTION DOSSIER PLAYING CARDS GRID */}
      <div style={{ fontSize: '11px', fontWeight: 800, color: '#7D8590', textTransform: 'uppercase', letterSpacing: '0.06em', marginBottom: '10px' }}>
        FACTION DOSSIER CARDS:
      </div>

      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
        gap: '16px'
      }}>
        {factions.map(f => {
          if (!f.active) {
            return (
              <div
                key={f.id}
                style={{
                  background: 'rgba(15,23,42,0.4)',
                  border: '2px dashed rgba(255,255,255,0.1)',
                  borderRadius: '14px',
                  minHeight: '260px',
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'center',
                  justifyContent: 'center',
                  color: '#64748b'
                }}
              >
                <span style={{ fontSize: '28px', marginBottom: '6px' }}>💀</span>
                <span style={{ fontSize: '12px', fontWeight: 900, textTransform: 'uppercase', letterSpacing: '0.05em' }}>FACTION PURGED</span>
              </div>
            );
          }

          const multInfo = getMultiplierInfo(f.loyalty);
          const y = calculateYield(f);

          const getMoodBadge = (loyalty) => {
            if (loyalty >= 80) return { label: 'Good 😊', color: '#4ADE80', bg: 'rgba(74, 222, 128, 0.1)' };
            if (loyalty >= 50) return { label: 'Co-op 😐', color: '#94A3B8', bg: 'rgba(148, 163, 184, 0.1)' };
            if (loyalty >= 30) return { label: 'Bad 😡', color: '#F59E0B', bg: 'rgba(245, 158, 11, 0.1)' };
            return { label: 'Rebel 💀', color: '#F87171', bg: 'rgba(248, 113, 113, 0.15)' };
          };

          const checkPerkActive = (fid, loyalty, power) => {
            if (fid === 'loyalist' && loyalty >= 80 && power >= 50) return 'Elder Statesmen';
            if (fid === 'youth' && loyalty >= 80 && power >= 40) return 'Campaign Machine';
            if (fid === 'trade' && loyalty >= 80 && power >= 40) return 'Strike Force';
            return null;
          };

          const mood = getMoodBadge(f.loyalty);
          const activePerk = checkPerkActive(f.id, f.loyalty, f.influence);
          const fColor = f.accentColor || '#38BDF8';

          let cardClass = "faction-dossier-card";
          if (f.loyalty < 30) cardClass += " rebel-border-flash";
          else if (activePerk) cardClass += " gold-perk-glow";

          return (
            <div
              key={f.id}
              className={cardClass}
              style={{
                background: 'linear-gradient(145deg, #1e293b, #0f172a)',
                border: activePerk ? '2px solid #eab308' : (f.loyalty < 30 ? '2.5px solid #ef4444' : `2px solid ${fColor}`),
                boxShadow: activePerk ? '0 0 16px rgba(234, 179, 8, 0.3)' : `0 4px 16px ${fColor}25`,
                borderRadius: '14px',
                padding: '16px',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                minHeight: '280px',
                transition: 'all 0.25s ease'
              }}
            >
              <div>
                {/* Header Row */}
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '10px' }}>
                  <div>
                    <h5 style={{ margin: 0, fontSize: '15px', fontWeight: 900, color: '#ffffff' }}>
                      {f.name}
                    </h5>
                    <div style={{ fontSize: '11px', color: '#94A3B8', marginTop: '2px', display: 'flex', alignItems: 'center', gap: '4px' }}>
                      ⚡ Power: <b style={{ color: '#fff' }}>{f.influence}%</b> | ✊ Loyalty: <b style={{ color: mood.color }}>{f.loyalty}%</b>
                    </div>
                  </div>
                  <button
                    type="button"
                    onClick={() => handleDissolve(f.id)}
                    title="Purge / Dissolve Faction"
                    style={{
                      background: 'rgba(239, 68, 68, 0.12)', border: '1px solid rgba(239, 68, 68, 0.3)',
                      color: '#F87171', fontSize: '10px', fontWeight: 800, padding: '3px 8px', borderRadius: '6px',
                      cursor: 'pointer', touchAction: 'manipulation'
                    }}
                  >
                    PURGE 💀
                  </button>
                </div>

                {/* Frozen Indicator */}
                {f.frozenTurnsRemaining > 0 && (
                  <div style={{ fontSize: '11px', color: '#f97316', background: 'rgba(249,115,22,0.1)', border: '1px dashed #f97316', padding: '6px 10px', borderRadius: '6px', fontWeight: 800, marginBottom: '10px' }}>
                    ❄️ FROZEN: Assets locked for {f.frozenTurnsRemaining} turns!
                  </div>
                )}

                {/* Mood & Efficiency Badge */}
                <div style={{
                  background: mood.bg,
                  color: mood.color,
                  border: `1px solid ${mood.color}40`,
                  fontSize: '11px',
                  fontWeight: 800,
                  padding: '5px 10px',
                  borderRadius: '6px',
                  marginBottom: '10px',
                  display: 'flex',
                  justifyContent: 'space-between'
                }}>
                  <span>Mood: {mood.label}</span>
                  <span>Efficiency: {multInfo.factor * 100}%</span>
                </div>

                {/* Perk Badge */}
                {activePerk && (
                  <div style={{ background: '#eab308', color: '#0f172a', fontSize: '10px', fontWeight: 900, padding: '4px 8px', borderRadius: '6px', marginBottom: '10px', textAlign: 'center', textTransform: 'uppercase' }}>
                    🌟 PERK ACTIVE: {activePerk}
                  </div>
                )}

                {/* Allocated Playing Cards Stack */}
                <div style={{
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '6px',
                  minHeight: '90px',
                  background: 'rgba(0,0,0,0.25)',
                  borderRadius: '8px',
                  padding: '8px',
                  border: '1px dashed rgba(255,255,255,0.1)',
                  marginBottom: '12px'
                }}>
                  {(f.patronage === 0 && (!f.post || f.post.length === 0) && f.projects.length === 0) ? (
                    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '70px', color: '#64748b', fontSize: '11px', fontStyle: 'italic' }}>
                      No Resource Cards Assigned
                    </div>
                  ) : (
                    <>
                      {/* Patronage */}
                      {f.patronage > 0 && (
                        <div style={{
                          background: 'linear-gradient(135deg, #1e3a8a, #3b82f6)',
                          padding: '6px 10px', borderRadius: '6px',
                          display: 'flex', justifyContent: 'space-between', alignItems: 'center',
                          fontSize: '11.5px', fontWeight: 800, color: '#ffffff'
                        }}>
                          <span>🛡️ Patronage Points</span>
                          <span style={{ background: 'rgba(255,255,255,0.25)', padding: '1px 6px', borderRadius: '4px', fontSize: '10px' }}>
                            ×{f.patronage}
                          </span>
                        </div>
                      )}

                      {/* Posts */}
                      {Array.isArray(f.post) && f.post.map((postKey, idx) => {
                        const postDef = getPostByKey(postKey) || getPostByName(postKey);
                        if (!postDef) return null;
                        return (
                          <div
                            key={`post-badge-${idx}`}
                            style={{
                              background: 'linear-gradient(135deg, #581c87, #a855f7)',
                              padding: '6px 10px', borderRadius: '6px',
                              fontSize: '11.5px', fontWeight: 800, color: '#ffffff',
                              display: 'flex', justifyContent: 'space-between', alignItems: 'center'
                            }}
                          >
                            <span>💼 {postDef.name}</span>
                            <span style={{ fontSize: '10px', opacity: 0.85 }}>{f.isPostPermanentlyAssigned ? '🔒 Locked' : '📌'}</span>
                          </div>
                        );
                      })}

                      {/* Projects */}
                      {f.projects.map((proj, idx) => (
                        <div
                          key={idx}
                          style={{
                            background: 'linear-gradient(135deg, #115e59, #0d9488)',
                            padding: '6px 10px', borderRadius: '6px',
                            fontSize: '11.5px', fontWeight: 800, color: '#ffffff',
                            display: 'flex', justifyContent: 'space-between', alignItems: 'center'
                          }}
                        >
                          <span>{proj.icon} {proj.name.split(' ')[0]}</span>
                          <span style={{ fontSize: '10px', opacity: 0.85 }}>{proj.isPermanentlyAssigned ? '🔒 Locked' : '📌'}</span>
                        </div>
                      ))}
                    </>
                  )}
                </div>
              </div>

              {/* Faction Yield Footer HUD */}
              <div style={{
                background: 'rgba(0,0,0,0.3)',
                border: '1px solid rgba(255,255,255,0.08)',
                padding: '8px 10px',
                borderRadius: '8px'
              }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', fontWeight: 800 }}>
                  <span style={{ color: '#4ADE80' }}>💰 {y.coins >= 0 ? '+' : ''}{y.coins}</span>
                  <span style={{ color: '#38BDF8' }}>📈 {y.support >= 0 ? '+' : ''}{y.support}%</span>
                  <span style={{ color: '#F43F5E' }}>✊ {y.morale >= 0 ? '+' : ''}{y.morale}</span>
                  <span style={{ color: '#F87171' }}>⚖️ {y.corruption >= 0 ? '+' : ''}{y.corruption}</span>
                  <span style={{ color: '#EC4899' }}>📢 {y.media >= 0 ? '+' : ''}{y.media}</span>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}