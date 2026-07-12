import React, { useState, useEffect, useCallback } from 'react';
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

  // Build factions list dynamically from activeParty or fallback
  const factionsList = (activeParty?.factions || []).map(f => {
    // Loyalty decay is 2% per active faction per turn
    const decayedLoyalty = Math.max(0, f.loyalty - 2);
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
    return getInitialFactions(partyMgmtState, factionsList);
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

  // 1. Lock the turn immediately when the component mounts
  useEffect(() => {
    setIsLocked(false);
  }, []); // Empty array ensures this only runs once on mount

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

  // Apply caps to negative yields only! Positive yields are completely uncapped.
  const finalCoins = totalYields.coins;
  const finalSupport = Math.ceil(totalYields.support);
  const finalMedia = totalYields.media;
  // Morale negative yields capped to -5
  const finalMorale = totalYields.morale >= 0 ? totalYields.morale : Math.max(-5, totalYields.morale);
  // Corruption negative yields (which is positive corruption addition) capped to +5
  const finalCorruption = totalYields.corruption <= 0 ? Math.max(-5, totalYields.corruption) : Math.min(5, totalYields.corruption);

  const topCard = deck[0];
  const activeFactionsList = factions.filter(f => f.active);
  const remainingCardsCount = deck.length;

  return (
    <div style={{
      fontFamily: 'system-ui, -apple-system, sans-serif'
    }}>
      <style>{`
        @keyframes drawCardAnimation {
          0% { transform: scale(0.95); opacity: 0.8; }
          100% { transform: scale(1); opacity: 1; }
        }
        @keyframes rebelPulse {
          0% { border-color: #ef4444; box-shadow: 0 0 4px rgba(239, 68, 68, 0.4); }
          50% { border-color: #dc2626; box-shadow: 0 0 16px rgba(239, 68, 68, 0.7); }
          100% { border-color: #ef4444; box-shadow: 0 0 4px rgba(239, 68, 68, 0.4); }
        }
        @keyframes perkGold {
          0% { box-shadow: 0 0 4px rgba(234, 179, 8, 0.3); }
          50% { box-shadow: 0 0 14px rgba(234, 179, 8, 0.6); }
          100% { box-shadow: 0 0 4px rgba(234, 179, 8, 0.3); }
        }
        .rebel-border-flash {
          animation: rebelPulse 1.5s infinite ease-in-out !important;
        }
        .gold-perk-glow {
          animation: perkGold 2s infinite ease-in-out !important;
          border: 1.5px solid #eab308 !important;
        }
        @keyframes buttonPulseFlash {
          0% { background: rgba(255, 255, 255, 0.15); box-shadow: 0 0 2px rgba(255, 255, 255, 0.2); }
          50% { background: rgba(255, 255, 255, 0.45); box-shadow: 0 0 12px rgba(255, 255, 255, 0.7); }
          100% { background: rgba(255, 255, 255, 0.15); box-shadow: 0 0 2px rgba(255, 255, 255, 0.2); }
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
          borderRadius: '10px',
          padding: '14px 20px',
          color: '#ffffff',
          marginBottom: '20px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          boxShadow: '0 4px 15px rgba(239, 68, 68, 0.2)',
          userSelect: 'none'
        }}>
          <div>
            <h4 style={{ margin: 0, fontSize: '15px', fontWeight: '800', display: 'flex', alignItems: 'center', gap: '8px' }}>
              ⚠️ REBELLIOUS FACTION ULTIMATUM
            </h4>
            <p style={{ margin: '4px 0 0 0', fontSize: '12px', color: 'rgba(255,255,255,0.9)' }}>
              The rebellious <b>{activeParty.factions.find(f => f.key === activeParty.activeFactionCrisisKey)?.name || 'Faction'}</b> has issued an ultimatum!
              {factionCrisisChoice ? (
                <span> Selected Resolution: <b style={{ textTransform: 'uppercase', color: '#facc15' }}>Option {factionCrisisChoice}</b></span>
              ) : (
                <span> You must resolve this crisis before taking this turn.</span>
              )}
            </p>
          </div>
          <button
            onClick={() => setShowCrisisModal(true)}
            style={{
              background: '#ffffff',
              border: 'none',
              borderRadius: '6px',
              color: '#b91c1c',
              padding: '6px 14px',
              fontSize: '12px',
              fontWeight: 'bold',
              cursor: 'pointer',
              transition: 'all 0.15s'
            }}
          >
            {factionCrisisChoice ? 'Change Choice' : 'Resolve Ultimatum'}
          </button>
        </div>
      )}

      {/* Faction Crisis Modal Overlay */}
      {showCrisisModal && activeParty?.activeFactionCrisisKey && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          background: 'rgba(15, 23, 42, 0.85)',
          backdropFilter: 'blur(8px)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 99999,
          padding: '20px'
        }}>
          <div style={{
            background: '#ffffff',
            maxWidth: '650px',
            width: '100%',
            borderRadius: '16px',
            boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.5)',
            border: '2px solid #ef4444',
            overflow: 'hidden',
            fontFamily: "'Inter', sans-serif"
          }}>
            {/* Modal Header */}
            <div style={{
              background: 'linear-gradient(135deg, #7f1d1d 0%, #b91c1c 100%)',
              padding: '20px 24px',
              color: '#ffffff',
              position: 'relative'
            }}>
              <h3 style={{ margin: 0, fontSize: '18px', fontWeight: '800', letterSpacing: '0.02em' }}>
                🚨 ULTIMATUM: Rebellious Faction Crisis
              </h3>
              <p style={{ margin: '6px 0 0 0', fontSize: '13px', color: 'rgba(255,255,255,0.85)' }}>
                The rebellious faction <b>{activeParty.factions.find(f => f.key === activeParty.activeFactionCrisisKey)?.name || 'Faction'}</b> is threatening a party split! You must select a resolution.
              </p>
            </div>

            {/* Options list */}
            <div style={{ padding: '24px', display: 'flex', flexDirection: 'column', gap: '16px' }}>

              {/* Option A */}
              <div
                onClick={() => {
                  setFactionCrisisChoice('A');
                  setShowCrisisModal(false);
                }}
                style={{
                  border: factionCrisisChoice === 'A' ? '2.5px solid #ef4444' : '1.5px solid var(--primary-border)',
                  background: factionCrisisChoice === 'A' ? 'rgba(239, 68, 68, 0.03)' : '#ffffff',
                  borderRadius: '10px',
                  padding: '16px',
                  cursor: 'pointer',
                  transition: 'all 0.15s'
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                  <strong style={{ fontSize: '14px', color: 'var(--primary-dark)' }}>Option A: Make Concessions</strong>
                  <span style={{ fontSize: '10px', fontWeight: 'bold', background: '#e2e8f0', padding: '2px 8px', borderRadius: '4px' }}>CONCEDE</span>
                </div>
                <p style={{ margin: 0, fontSize: '12px', color: 'var(--card-text)', lineHeight: '1.4' }}>
                  Offer high-level posts and policy promises to buy their loyalty.
                </p>
                <div style={{ marginTop: '8px', fontSize: '11px', fontWeight: 'bold', color: '#b91c1c' }}>
                  Cost: -50 Coins, -20 Media Image | Effect: Restores Loyalty to 60%; reduces their Influence share by 10%.
                </div>
              </div>

              {/* Option B */}
              <div
                onClick={() => {
                  setFactionCrisisChoice('B');
                  setShowCrisisModal(false);
                }}
                style={{
                  border: factionCrisisChoice === 'B' ? '2.5px solid #ef4444' : '1.5px solid var(--primary-border)',
                  background: factionCrisisChoice === 'B' ? 'rgba(239, 68, 68, 0.03)' : '#ffffff',
                  borderRadius: '10px',
                  padding: '16px',
                  cursor: 'pointer',
                  transition: 'all 0.15s'
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                  <strong style={{ fontSize: '14px', color: 'var(--primary-dark)' }}>Option B: Purge rebellious leaders</strong>
                  <span style={{ fontSize: '10px', fontWeight: 'bold', background: '#e2e8f0', padding: '2px 8px', borderRadius: '4px' }}>PURGE</span>
                </div>
                <p style={{ margin: 0, fontSize: '12px', color: 'var(--card-text)', lineHeight: '1.4' }}>
                  Exile rebellious dissenters from the party structure.
                </p>
                <div style={{ marginTop: '8px', fontSize: '11px', fontWeight: 'bold', color: '#b91c1c' }}>
                  Cost: -20 Party Morale, -5% Voter Support | Effect: Restores Loyalty to 50%; permanently caps their Influence share at 20%.
                </div>
              </div>

              {/* Option C */}
              <div
                onClick={() => {
                  setFactionCrisisChoice('C');
                  setShowCrisisModal(false);
                }}
                style={{
                  border: factionCrisisChoice === 'C' ? '2.5px solid #ef4444' : '1.5px solid var(--primary-border)',
                  background: factionCrisisChoice === 'C' ? 'rgba(239, 68, 68, 0.03)' : '#ffffff',
                  borderRadius: '10px',
                  padding: '16px',
                  cursor: 'pointer',
                  transition: 'all 0.15s'
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                  <strong style={{ fontSize: '14px', color: 'var(--primary-dark)' }}>Option C: Force a Party Split</strong>
                  <span style={{ fontSize: '10px', fontWeight: 'bold', background: '#ef4444', color: '#ffffff', padding: '2px 8px', borderRadius: '4px' }}>SPLIT</span>
                </div>
                <p style={{ margin: 0, fontSize: '12px', color: 'var(--card-text)', lineHeight: '1.4' }}>
                  Denounce them publicly. The faction will defect, splitting your voter base.
                </p>
                <div style={{ marginTop: '8px', fontSize: '11px', fontWeight: 'bold', color: '#b91c1c' }}>
                  Cost: -15% Voter Support, -30 Party Morale | Effect: Faction permanently defuses and is deleted. (Support dropping to 0% triggers defeat!).
                </div>
              </div>

            </div>

            {/* Modal Footer */}
            <div style={{
              background: '#f8fafc',
              padding: '16px 24px',
              display: 'flex',
              justifyContent: 'flex-end',
              borderTop: '1px solid var(--primary-border)'
            }}>
              {factionCrisisChoice && (
                <button
                  onClick={() => setShowCrisisModal(false)}
                  style={{
                    background: '#1e293b',
                    color: '#ffffff',
                    border: 'none',
                    borderRadius: '6px',
                    padding: '8px 18px',
                    fontSize: '12px',
                    fontWeight: 'bold',
                    cursor: 'pointer'
                  }}
                >
                  Close &amp; Keep Choice
                </button>
              )}
            </div>
          </div>
        </div>
      )}

      {/* Top Header & Summary */}
      <div style={{ marginBottom: '20px' }}>
        <p style={{ margin: '0 0 15px 0', fontSize: '13px', color: 'var(--card-text)' }}>
          Allocate resource cards one-by-one from the pile to factions. Keep faction loyalty high to maximize yields.
        </p>
      </div>

      {/* Main Workspace (Card on Left, Yield Stats on Right) */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
        gap: '20px',
        marginBottom: '25px'
      }}>
        {/* Drawn Card Interface */}
        {topCard ? (
          <div style={{
            background: topCard.color,
            borderRadius: '10px',
            padding: '16px 20px',
            color: '#ffffff',
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'space-between',
            minHeight: '200px',
            boxShadow: '0 4px 15px rgba(0,0,0,0.15)',
            border: '1.5px solid rgba(255,255,255,0.12)',
            animation: 'drawCardAnimation 0.2s ease-out'
          }}>
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span style={{
                  fontSize: '9px',
                  fontWeight: '900',
                  background: 'rgba(255,255,255,0.22)',
                  color: '#ffffff',
                  padding: '2px 8px',
                  borderRadius: '4px',
                  textTransform: 'uppercase',
                  letterSpacing: '0.05em'
                }}>
                  {topCard.type}
                </span>
                <span style={{ fontSize: '11px', fontWeight: 'bold', background: 'rgba(0,0,0,0.15)', padding: '2px 8px', borderRadius: '12px' }}>
                  🃏 {totalCardsCount - remainingCardsCount + 1} of {totalCardsCount} ({remainingCardsCount - 1} left)
                </span>
              </div>
              <h4 style={{ margin: '12px 0 6px 0', fontSize: '18px', fontWeight: '800' }}>
                {topCard.icon} {topCard.name}
              </h4>
              <p style={{ margin: 0, fontSize: '12px', color: 'rgba(255,255,255,0.85)', lineHeight: '1.4' }}>
                {topCard.desc}
              </p>
            </div>

            {/* Allocation Options */}
            <div style={{ marginTop: '16px' }}>
              <div style={{ fontSize: '10px', fontWeight: '900', color: 'rgba(255,255,255,0.9)', marginBottom: '8px', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                Assign Faction:
              </div>
              <div style={{ display: 'flex', gap: '8px' }}>
                {activeFactionsList.map(f => (
                  <button
                    key={f.id}
                    onClick={() => handleAllocate(f.id)}
                    className="pulse-flash-btn"
                    style={{
                      flex: 1,
                      padding: '8px 10px',
                      border: 'none',
                      borderRadius: '6px',
                      color: '#ffffff',
                      fontSize: '11.5px',
                      fontWeight: '800',
                      cursor: 'pointer',
                      transition: 'background 0.15s ease, transform 0.15s ease',
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
            background: 'rgba(34, 197, 94, 0.04)',
            border: '2.5px solid #22c55e',
            borderRadius: '10px',
            padding: '24px',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            textAlign: 'center',
            minHeight: '200px'
          }}>
            <span style={{ fontSize: '32px', marginBottom: '8px' }}>✅</span>
            <h4 style={{ margin: 0, fontSize: '15px', fontWeight: '800', color: '#166534' }}>
              All Resource Cards Allocated
            </h4>
            <p style={{ margin: '4px 0 0 0', fontSize: '12px', color: 'var(--card-text)' }}>
              Factions allocations are completed. You can safely lock in your turn.
            </p>
          </div>
        )}

        {/* Combined Yield Summary Box */}
        <div style={{
          background: 'rgba(var(--party-primary-color-rgb, 101, 148, 177), 0.03)',
          border: '1.5px solid var(--party-primary-color, var(--primary-border))',
          borderRadius: '10px',
          padding: '16px',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'space-between',
          minHeight: '200px'
        }}>
          <div>
            <h5 style={{ margin: '0 0 12px 0', color: 'var(--primary-dark)', fontSize: '12px', fontWeight: '800', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
              📈 Combined Turn Yields
            </h5>
            <div style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(2, 1fr)',
              gap: '10px'
            }}>
              <div style={{ background: '#ffffff', border: '1px solid var(--primary-border)', padding: '8px 12px', borderRadius: '6px' }}>
                <span style={{ fontSize: '11px', color: 'var(--card-text)', display: 'block' }}>Party Coins</span>
                <strong style={{ fontSize: '15px', color: '#15803d' }}>+{finalCoins} 💰</strong>
              </div>
              <div style={{ background: '#ffffff', border: '1px solid var(--primary-border)', padding: '8px 12px', borderRadius: '6px' }}>
                <span style={{ fontSize: '11px', color: 'var(--card-text)', display: 'block' }}>Voter Support</span>
                <strong style={{ fontSize: '15px', color: '#1d4ed8' }}>+{finalSupport}% 📈</strong>
              </div>
              <div style={{ background: '#ffffff', border: '1px solid var(--primary-border)', padding: '8px 12px', borderRadius: '6px' }}>
                <span style={{ fontSize: '11px', color: 'var(--card-text)', display: 'block' }}>Morale</span>
                <strong style={{ fontSize: '15px', color: finalMorale < 0 ? '#b91c1c' : '#a21caf' }}>
                  {finalMorale > 0 ? '+' : ''}{finalMorale} ✊
                </strong>
                {totalYields.morale < -5 && <span style={{ fontSize: '9px', color: '#b91c1c', display: 'block' }}>(Capped)</span>}
              </div>
              <div style={{ background: '#ffffff', border: '1px solid var(--primary-border)', padding: '8px 12px', borderRadius: '6px' }}>
                <span style={{ fontSize: '11px', color: 'var(--card-text)', display: 'block' }}>Corruption</span>
                <strong style={{ fontSize: '15px', color: finalCorruption > 0 ? '#b91c1c' : '#15803d' }}>
                  {finalCorruption > 0 ? '+' : ''}{finalCorruption} ⚖️
                </strong>
                {totalYields.corruption > 5 && <span style={{ fontSize: '9px', color: '#b91c1c', display: 'block' }}>(Capped)</span>}
              </div>
              <div style={{ background: '#ffffff', border: '1px solid var(--primary-border)', padding: '8px 12px', borderRadius: '6px', gridColumn: 'span 2' }}>
                <span style={{ fontSize: '11px', color: 'var(--card-text)', display: 'block' }}>Media Image</span>
                <strong style={{ fontSize: '15px', color: '#ec4899' }}>+{finalMedia} 📢</strong>
              </div>
            </div>

            <div style={{ marginTop: '15px', borderTop: '1px dashed var(--primary-border)', paddingTop: '15px' }}>
              <h5 style={{ margin: '0 0 10px 0', color: 'var(--primary-dark)', fontSize: '12px', fontWeight: '800', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                ⚡ Faction Power Perks
              </h5>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                {(() => {
                  const getPerkStatus = (fid, reqL, reqP) => {
                    const f = factions.find(fac => fac.id === fid);
                    if (!f || !f.active) return { active: false, loyalty: 0, power: 0 };
                    return { active: f.loyalty >= reqL && f.influence >= reqP, loyalty: f.loyalty, power: f.influence };
                  };

                  const perks = [
                    { id: 'loyalist', name: 'Loyalists (Elder Statesmen)', reqL: 80, reqP: 50, desc: '+25 Coins, +3% Support per turn' },
                    { id: 'youth', name: 'Youth Wing (Campaign Machine)', reqL: 80, reqP: 40, desc: '+5 Morale, +3% Support, +5 Media per turn' },
                    { id: 'trade', name: 'Trade Unions (Strike Force)', reqL: 80, reqP: 40, desc: '-5 Corruption; -3% Support & -3 Morale to opponents' }
                  ];

                  return perks.map(p => {
                    const stat = getPerkStatus(p.id, p.reqL, p.reqP);
                    return (
                      <div key={p.id} style={{
                        padding: '8px 10px',
                        background: stat.active ? 'rgba(234, 179, 8, 0.08)' : '#ffffff',
                        border: stat.active ? '1.5px solid #eab308' : '1px solid var(--primary-border)',
                        borderRadius: '6px',
                        fontSize: '11px',
                        transition: 'all 0.2s',
                        boxShadow: stat.active ? '0 0 8px rgba(234, 179, 8, 0.15)' : 'none'
                      }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
                          <strong style={{ color: stat.active ? '#a16207' : 'var(--primary-dark)', fontSize: '11.5px' }}>{p.name}</strong>
                          <span style={{
                            fontSize: '9px',
                            fontWeight: 'bold',
                            padding: '2px 6px',
                            borderRadius: '4px',
                            background: stat.active ? '#eab308' : '#e2e8f0',
                            color: stat.active ? '#ffffff' : '#475569'
                          }}>
                            {stat.active ? 'ACTIVE ⚡' : `Requires L:${p.reqL} P:${p.reqP}`}
                          </span>
                        </div>
                        <div style={{ color: 'var(--card-text)', fontSize: '10px', lineHeight: '1.3' }}>{p.desc}</div>
                        <div style={{ fontSize: '9px', color: '#94a3b8', marginTop: '3px' }}>
                          Current: Loyalty {stat.loyalty}% | Power {stat.power}%
                        </div>
                      </div>
                    );
                  });
                })()}
              </div>
            </div>
          </div>

          <div style={{ display: 'flex', marginTop: '14px', flexDirection: 'column', gap: '8px' }}>
            {/* Error message */}
            {lockError && (
              <div style={{ color: '#f87171', fontSize: '12px', padding: '6px 10px', background: '#450a0a', borderRadius: '6px', border: '1px solid #ef4444' }}>
                ⚠️ {lockError}
              </div>
            )}

            <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
              <button
                onClick={handleUndo}
                disabled={history.length === 0 || isLocked}
                style={{
                  flex: '0 0 auto',
                  padding: '10px 15px',
                  background: '#ffffff',
                  border: '1.5px solid var(--party-primary-color, var(--primary-border))',
                  color: (history.length > 0 && !isLocked) ? 'var(--primary-dark)' : '#94a3b8',
                  borderRadius: '6px',
                  fontWeight: 'bold',
                  cursor: (history.length > 0 && !isLocked) ? 'pointer' : 'default',
                  fontSize: '13px',
                  opacity: (history.length > 0 && !isLocked) ? 1 : 0.4
                }}
              >
                ↩ Undo
              </button>

              {/* Lock Allocations button */}
              <button
                onClick={handleLock}
                disabled={isLocked || isLocking}
                style={{
                  flex: '1 1 0%',
                  minWidth: '150px',
                  padding: '10px 15px',
                  background: isLocked
                    ? 'var(--selected-highlight, #22c55e)'
                    : 'var(--party-primary-color, var(--primary-dark))',
                  borderWidth: '1.5px',
                  borderStyle: 'solid',
                  borderColor: isLocked
                    ? 'var(--selected-highlight, #22c55e)'
                    : 'var(--party-primary-color, var(--primary-dark))',
                  color: isLocked ? 'var(--primary-dark, #1e3a5f)' : '#ffffff',
                  fontWeight: 'bold',
                  borderRadius: '6px',
                  cursor: isLocked ? 'default' : 'pointer',
                  fontSize: '13px',
                  opacity: isLocking ? 0.7 : 1,
                  transition: 'all 0.2s',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  gap: '6px'
                }}
              >
                {isLocking ? '⏳ Saving...' : isLocked ? '✅ Allocations Locked' : '🔒 Confirm'}
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Factions Deck columns */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
        gap: '20px'
      }}>
        {factions.map(f => {
          if (!f.active) {
            return (
              <div
                key={f.id}
                style={{
                  background: 'rgba(0,0,0,0.02)',
                  border: '2px dashed var(--primary-border)',
                  borderRadius: '10px',
                  minHeight: '280px',
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'center',
                  justifyContent: 'center',
                  color: 'gray'
                }}
              >
                <span style={{ fontSize: '24px', marginBottom: '6px' }}>❌</span>
                <span style={{ fontSize: '13px', fontWeight: 'bold', textTransform: 'uppercase', letterSpacing: '0.05em' }}>Faction Purged</span>
              </div>
            );
          }

          const multInfo = getMultiplierInfo(f.loyalty);
          const y = calculateYield(f);

          const getMoodBadge = (loyalty) => {
            if (loyalty >= 80) return { label: 'Good 😊', color: '#22c55e', bg: 'rgba(34, 197, 94, 0.06)', shadow: '0 0 8px rgba(34, 197, 94, 0.12)' };
            if (loyalty >= 50) return { label: 'Neutral 😐', color: '#64748b', bg: 'rgba(100, 116, 139, 0.06)', shadow: 'none' };
            if (loyalty >= 30) return { label: 'Bad 😡', color: '#f97316', bg: 'rgba(249, 115, 22, 0.06)', shadow: '0 0 8px rgba(249, 115, 22, 0.12)' };
            return { label: 'Rebel 💀', color: '#ef4444', bg: 'rgba(239, 68, 68, 0.06)', shadow: '0 0 12px rgba(239, 68, 68, 0.25)' };
          };

          const checkPerkActive = (fid, loyalty, power) => {
            if (fid === 'loyalist' && loyalty >= 80 && power >= 50) return 'Elder Statesmen';
            if (fid === 'youth' && loyalty >= 80 && power >= 40) return 'Campaign Machine';
            if (fid === 'trade' && loyalty >= 80 && power >= 40) return 'Strike Force';
            return null;
          };

          const mood = getMoodBadge(f.loyalty);
          const activePerk = checkPerkActive(f.id, f.loyalty, f.influence);

          let cardClass = "themed-action-card";
          if (f.loyalty < 30) cardClass += " rebel-border-flash";
          else if (activePerk) cardClass += " gold-perk-glow";

          return (
            <div
              key={f.id}
              className={cardClass}
              style={{
                border: activePerk ? '2px solid #eab308' : (f.loyalty < 30 ? '2.5px solid #ef4444' : `2px solid ${mood.color}`),
                boxShadow: activePerk ? '0 0 12px rgba(234, 179, 8, 0.3)' : mood.shadow,
                borderRadius: '10px',
                padding: '16px',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                minHeight: '280px',
                background: 'rgba(255,255,255,0.2)',
                transition: 'all 0.25s ease'
              }}
            >
              <div>
                {/* Column Header */}
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '10px' }}>
                  <div>
                    <h5 style={{ margin: 0, fontSize: '14px', fontWeight: 'bold', color: 'var(--primary-dark)' }}>
                       {f.name}
                    </h5>
                    <div style={{ fontSize: '11px', color: 'var(--card-text)', marginTop: '2px', display: 'flex', alignItems: 'center', gap: '3px', flexWrap: 'wrap' }}>
                      ⚡ <b>{f.influence}%</b> | ✊ <b style={{ color: mood.color }}>{f.loyalty}%</b>
                      {(() => {
                        const diff = f.loyalty - f.baseLoyalty;
                        if (diff > 0) return <span style={{ color: '#22c55e', fontSize: '10px', fontWeight: 'bold', marginLeft: '3px' }}>▲ +{diff}%</span>;
                        if (diff < 0) return <span style={{ color: '#ef4444', fontSize: '10px', fontWeight: 'bold', marginLeft: '3px' }}>▼ {diff}%</span>;
                        return null;
                      })()}
                    </div>
                  </div>
                </div>

                {f.frozenTurnsRemaining > 0 && (() => {
                  const frozenPostsCount = f.frozenPosts ? Object.values(f.frozenPosts).filter(t => t > 0).length : 0;
                  const frozenPatronageCount = f.frozenPatronageTurns ? f.frozenPatronageTurns.filter(t => t > 0).length : 0;
                  const frozenProjectsCount = (f.projects || []).filter(p => p.frozenTurnsRemaining > 0).length;
                  const totalFrozenAssets = frozenPostsCount + frozenPatronageCount + frozenProjectsCount;

                  return (
                    <div style={{
                      fontSize: '11px',
                      color: '#c2410c',
                      backgroundColor: '#fff7ed',
                      border: '1.5px dashed #ffedd5',
                      padding: '6px 10px',
                      borderRadius: '6px',
                      fontWeight: '800',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '4px',
                      marginBottom: '10px'
                    }}>
                      ❄️ FROZEN: {totalFrozenAssets} card/asset{totalFrozenAssets !== 1 ? 's' : ''} locked for {f.frozenTurnsRemaining} turn{f.frozenTurnsRemaining !== 1 ? 's' : ''}!
                    </div>
                  );
                })()}

                {/* Mood Badge */}
                <div style={{
                  background: mood.bg,
                  color: mood.color,
                  border: `1.5px solid ${mood.color}25`,
                  fontSize: '11px',
                  fontWeight: 'bold',
                  padding: '4px 8px',
                  borderRadius: '4px',
                  marginBottom: '10px',
                  textAlign: 'center'
                }}>
                  Mood: {mood.label} | Efficiency: {multInfo.factor * 100}%
                </div>

                {/* Perk Badge */}
                {activePerk && (
                  <div style={{
                    background: '#eab308',
                    color: '#ffffff',
                    fontSize: '10px',
                    fontWeight: '900',
                    padding: '4px 8px',
                    borderRadius: '4px',
                    marginBottom: '10px',
                    textAlign: 'center',
                    textTransform: 'uppercase',
                    letterSpacing: '0.05em'
                  }}>
                    🌟 Perk Active: {activePerk}
                  </div>
                )}

                {/* Stack Pile */}
                <div style={{
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '8px',
                  minHeight: '100px',
                  background: 'rgba(0,0,0,0.02)',
                  borderRadius: '6px',
                  padding: '8px',
                  border: '1px dashed var(--primary-border)',
                  marginBottom: '14px'
                }}>
                  {(f.patronage === 0 && (!f.post || f.post.length === 0) && f.projects.length === 0) ? (
                    <div style={{
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      height: '84px',
                      color: 'gray',
                      fontSize: '11px',
                      fontStyle: 'italic'
                    }}>
                      No Cards Assigned
                    </div>
                  ) : (
                    <>
                      {/* Patronage */}
                      {f.patronage > 0 && (
                        <div style={{
                          background: 'linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%)',
                          padding: '6px 10px',
                          borderRadius: '4px',
                          display: 'flex',
                          justifyContent: 'space-between',
                          alignItems: 'center',
                          fontSize: '11.5px',
                          fontWeight: 'bold',
                          color: '#ffffff'
                        }}>
                          <span>🛡️ Patronage Points</span>
                          <span style={{ background: 'rgba(255,255,255,0.25)', padding: '1px 5px', borderRadius: '3px', fontSize: '10px' }}>
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
                              background: 'linear-gradient(135deg, #581c87 0%, #a855f7 100%)',
                              padding: '6px 10px',
                              borderRadius: '4px',
                              fontSize: '11.5px',
                              fontWeight: 'bold',
                              color: '#ffffff',
                              display: 'flex',
                              justifyContent: 'space-between',
                              alignItems: 'center'
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
                            background: 'linear-gradient(135deg, #115e59 0%, #0d9488 100%)',
                            padding: '6px 10px',
                            borderRadius: '4px',
                            fontSize: '11.5px',
                            fontWeight: 'bold',
                            color: '#ffffff',
                            display: 'flex',
                            justifyContent: 'space-between',
                            alignItems: 'center'
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

              {/* Faction Yield Footer */}
              <div style={{
                background: 'rgba(0,0,0,0.01)',
                border: '1px solid var(--primary-border)',
                padding: '8px 12px',
                borderRadius: '6px'
              }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', fontWeight: 'bold' }}>
                  <span style={{ color: '#15803d' }}>💰 {y.coins >= 0 ? '+' : ''}{y.coins}</span>
                  <span style={{ color: '#1d4ed8' }}>📈 {y.support >= 0 ? '+' : ''}{y.support}%</span>
                  <span style={{ color: '#a21caf' }}>✊ {y.morale >= 0 ? '+' : ''}{y.morale}</span>
                  <span style={{ color: '#b91c1c' }}>⚖️ {y.corruption >= 0 ? '+' : ''}{y.corruption}</span>
                  <span style={{ color: '#ec4899' }}>📢 {y.media >= 0 ? '+' : ''}{y.media}</span>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}