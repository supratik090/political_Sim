import React, { useState, useEffect } from 'react';

export default function Action3PartyDecision({
  turnData,
  selectedIssueOptionKey,
  setSelectedIssueOptionKey,
  activeParty,
  selectedEventOptionKey,
  setSelectedEventOptionKey,
  scenarioEvents = []
}) {
  // Key for localStorage persistence, unique per session & turn number
  const storageKey = `political_sim_party_management_${turnData.id || 'default'}_${turnData.turnNumber || 0}`;

  // Build factions list dynamically from activeParty or fallback
  const factionsList = (activeParty?.factions || []).map(f => {
    // Loyalty decay is 2% per active faction per turn
    const decayedLoyalty = Math.max(0, f.loyalty - 2);
    const delegatedProjects = (activeParty?.projects || []).filter(p => p.progressPercent === 100 && p.managingFactionKey === f.key);
    const projectsMapped = delegatedProjects.map(p => {
      let name = p.projectKey;
      let icon = '🏗️';
      let desc = 'Delegated project.';
      if (p.projectKey === 'PARTY_HQ') { name = 'Party Headquarters'; icon = '🏢'; desc = 'Yields: +12 Coins, +3 Media Image.'; }
      else if (p.projectKey === 'IT_CELL') { name = 'IT Cell (Digital Bureau)'; icon = '💻'; desc = 'Yields: +2 Media Image.'; }
      else if (p.projectKey === 'CADRE_OFFICE') { name = 'District Cadre Offices'; icon = '🏘️'; desc = 'Yields: +5 Morale.'; }
      else if (p.projectKey === 'THINK_TANK') { name = 'Policy Research Think Tank'; icon = '🧠'; desc = 'Yields: +4 Media Image.'; }
      else if (p.projectKey === 'TRAINING_ACADEMY') { name = 'Grassroots Training Academy'; icon = '🏫'; desc = 'Yields: +3 Morale.'; }
      else if (p.projectKey === 'YOUTH_WING') { name = 'Youth Wing Network'; icon = '✊'; desc = 'Yields: +3 Morale.'; }
      
      return {
        id: p.id,
        projectKey: p.projectKey,
        type: 'project',
        name,
        desc,
        icon,
        color: 'linear-gradient(135deg, #115e59 0%, #0d9488 100%)',
        isPermanentlyAssigned: true // Lock projects from previous turns
      };
    });

    let accentColor = '#ef4444';
    if (f.key === 'youth') accentColor = '#f97316';
    if (f.key === 'trade') accentColor = '#14b8a6';

    return {
      id: f.key,
      name: f.name,
      baseLoyalty: decayedLoyalty,
      loyalty: decayedLoyalty,
      influence: f.influence,
      post: f.post || 'None',
      patronage: 0,
      projects: projectsMapped,
      active: f.active,
      accentColor,
      isPostPermanentlyAssigned: f.post && f.post !== 'None' // Lock posts from previous turns
    };
  });

  const initialFactions = factionsList.length > 0 ? factionsList : [
    { id: 'veteran', name: 'Loyalists', baseLoyalty: 80, loyalty: 80, influence: 45, post: 'None', patronage: 0, projects: [], active: true, accentColor: '#ef4444' },
    { id: 'youth', name: 'Youth Wing', baseLoyalty: 55, loyalty: 55, influence: 35, post: 'None', patronage: 0, projects: [], active: true, accentColor: '#f97316' },
    { id: 'trade', name: 'Trade Unions', baseLoyalty: 65, loyalty: 65, influence: 20, post: 'None', patronage: 0, active: true, projects: [], accentColor: '#14b8a6' }
  ];

  // The resource deck to allocate (exactly 1 Patronage Point card + Completed unassigned projects)
  const unassignedProjects = (activeParty?.projects || []).filter(p => p.progressPercent === 100 && (p.managingFactionKey === 'None' || !p.managingFactionKey));
  const projectCards = unassignedProjects.map(p => {
    let name = p.projectKey;
    let icon = '🏗️';
    let desc = 'Delegated project.';
    if (p.projectKey === 'PARTY_HQ') { name = 'Party Headquarters'; icon = '🏢'; desc = 'Yields: +12 Coins, +3 Media Image.'; }
    else if (p.projectKey === 'IT_CELL') { name = 'IT Cell (Digital Bureau)'; icon = '💻'; desc = 'Yields: +2 Media Image.'; }
    else if (p.projectKey === 'CADRE_OFFICE') { name = 'District Cadre Offices'; icon = '🏘️'; desc = 'Yields: +5 Morale.'; }
    else if (p.projectKey === 'THINK_TANK') { name = 'Policy Research Think Tank'; icon = '🧠'; desc = 'Yields: +4 Media Image.'; }
    else if (p.projectKey === 'TRAINING_ACADEMY') { name = 'Grassroots Training Academy'; icon = '🏫'; desc = 'Yields: +3 Morale.'; }
    else if (p.projectKey === 'YOUTH_WING') { name = 'Youth Wing Network'; icon = '✊'; desc = 'Yields: +3 Morale.'; }
    
    return {
      id: p.id,
      projectKey: p.projectKey,
      type: 'project',
      name,
      desc,
      icon,
      color: 'linear-gradient(135deg, #115e59 0%, #0d9488 100%)'
    };
  });

  const assignedPosts = (activeParty?.factions || []).map(f => f.post).filter(p => p && p !== 'None');
  const initialDeck = [
    { id: 'pat-1', type: 'patronage', name: 'Patronage Point', desc: 'Increases loyalty by +5%. Yields: +2 Coins, +1 Morale, -1 Corruption, +1 Media Image.', icon: '🛡️', color: 'linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%)' }
  ];
  if (!assignedPosts.includes('Secretary Post')) {
    initialDeck.push({ id: 'post-1', type: 'post', name: 'Secretary Post', desc: 'Assigns a leadership role. Boosts loyalty by +15% and increases morale yield.', icon: '💼', color: 'linear-gradient(135deg, #581c87 0%, #a855f7 100%)' });
  }
  if (!assignedPosts.includes('Fund Manager Post')) {
    initialDeck.push({ id: 'post-2', type: 'post', name: 'Fund Manager Post', desc: 'Assigns financial oversight. Boosts loyalty by +15% and increases coin yield.', icon: '💰', color: 'linear-gradient(135deg, #581c87 0%, #a855f7 100%)' });
  }
  initialDeck.push(...projectCards);

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
    return initialDeck;
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

  // Save state to localStorage whenever it updates
  useEffect(() => {
    localStorage.setItem(storageKey, JSON.stringify({ factions, deck, history, factionCrisisChoice }));
  }, [factions, deck, history, factionCrisisChoice, storageKey]);

  const [showCrisisModal, setShowCrisisModal] = useState(false);

  // Automatically open the crisis modal if there's an active crisis and no choice is selected yet
  useEffect(() => {
    if (activeParty?.activeFactionCrisisKey && !factionCrisisChoice) {
      setShowCrisisModal(true);
    }
  }, [activeParty, factionCrisisChoice]);

  // Ensure the section is considered completed so it doesn't block turn submission when deck is empty
  useEffect(() => {
    if (setSelectedIssueOptionKey) {
      if (deck.length === 0) {
        setSelectedIssueOptionKey('mock_done');
      } else {
        setSelectedIssueOptionKey('');
      }
    }
  }, [deck, setSelectedIssueOptionKey]);

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
      const mult = getMultiplierInfo(f.loyalty).factor;
      const patronageCoins = f.patronage * 2;
      const postCoins = f.post === 'Fund Manager Post' ? 8 : 0;
      let baseCoins = patronageCoins + postCoins;

      const patronageMorale = f.patronage * 1;
      const postMorale = f.post === 'Secretary Post' ? 6 : 0;
      
      let projectMorale = 0;
      let projectMedia = 0;
      
      (f.projects || []).forEach(proj => {
        if (proj.projectKey === 'CADRE_OFFICE' || proj.id === 'proj-1') projectMorale += 5;
        else if (proj.projectKey === 'TRAINING_ACADEMY') projectMorale += 3;
        else if (proj.projectKey === 'YOUTH_WING') projectMorale += 3;
        else if (proj.projectKey === 'IT_CELL') projectMedia += 2;
        else if (proj.projectKey === 'THINK_TANK') projectMedia += 4;
        else if (proj.projectKey === 'PARTY_HQ') {
          baseCoins += 12;
          projectMedia += 3;
        }
      });

      const baseMorale = patronageMorale + postMorale + projectMorale;
      const patronageCorruption = f.patronage * -1;
      const postCorruption = f.post !== 'None' ? 2 : 0;
      const baseCorruption = patronageCorruption + postCorruption;
      const patronageMedia = f.patronage * 1;
      const baseMedia = patronageMedia + projectMedia;
      const baseSupport = f.loyalty >= 50 ? (f.influence * 0.01) : -(f.influence * 0.01);

      const coinsYield = Math.round(baseCoins * mult);
      const supportYield = Math.abs(parseFloat((baseSupport * mult).toFixed(1)));
      const moraleYield = Math.round(baseMorale * mult);
      const corruptionYield = Math.round(baseCorruption * (2 - mult));
      const mediaYield = Math.round(baseMedia * mult);

      const sum = coinsYield + supportYield * 10 + moraleYield + Math.abs(corruptionYield) + mediaYield;
      yieldSums[f.id] = sum;
      totalYieldSum += sum;
    });

    let updatedFactions = rawFactions;
    if (totalYieldSum > 0 && activeFactions.length > 0) {
      let remainingInfluence = 100;
      updatedFactions = rawFactions.map((f) => {
        if (!f.active) return f;
        const activeIdx = activeFactions.findIndex(af => af.id === f.id);
        const isLastActive = activeIdx === activeFactions.length - 1;
        
        let newInfluence = 0;
        if (isLastActive) {
          newInfluence = remainingInfluence;
        } else {
          newInfluence = Math.round((yieldSums[f.id] / totalYieldSum) * 100);
          remainingInfluence -= newInfluence;
        }
        return {
          ...f,
          influence: Math.max(1, newInfluence)
        };
      });
    }

    setFactions(updatedFactions);
  };

  // Reset all allocations
  const handleReset = () => {
    updateFactionsState(initialFactions);
    setDeck(initialDeck);
    setHistory([]);
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
          postVal = cardToAllocate.name;
          loyaltyChange = 15;
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
      if (dissolved.post !== 'None') {
        const postCardDef = initialDeck.find(d => d.name === dissolved.post);
        cardsToReturn.push({ ...postCardDef, id: `post-refund-${factionId}-${Date.now()}` });
      }
      dissolved.projects.forEach(proj => {
        cardsToReturn.push(proj);
      });

      // Distribute influence
      const activeOthers = factions.filter(f => f.active && f.id !== factionId);
      const influenceShare = activeOthers.length > 0 ? Math.round(dissolved.influence / activeOthers.length) : 0;

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
          return {
            ...f,
            influence: f.influence + influenceShare,
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

  // Calculate individual faction yields
  const calculateYield = (faction) => {
    if (!faction.active) return { coins: 0, support: 0, morale: 0, corruption: 0, media: 0 };
    const mult = getMultiplierInfo(faction.loyalty).factor;
    
    // Benefits of patronage points: 2 coins, 1 morale, -1 corruption, 1 media, no support
    const patronageCoins = faction.patronage * 2;
    const postCoins = faction.post === 'Fund Manager Post' ? 8 : 0;
    let baseCoins = patronageCoins + postCoins;

    const patronageMorale = faction.patronage * 1;
    const postMorale = faction.post === 'Secretary Post' ? 6 : 0;
    
    // Project yields are calculated here and scaled by faction loyalty
    let projectMorale = 0;
    let projectMedia = 0;
    
    (faction.projects || []).forEach(proj => {
      if (proj.projectKey === 'CADRE_OFFICE' || proj.id === 'proj-1') projectMorale += 5;
      else if (proj.projectKey === 'TRAINING_ACADEMY') projectMorale += 3;
      else if (proj.projectKey === 'YOUTH_WING') projectMorale += 3;
      else if (proj.projectKey === 'IT_CELL') projectMedia += 2;
      else if (proj.projectKey === 'THINK_TANK') projectMedia += 4;
      else if (proj.projectKey === 'PARTY_HQ') {
        baseCoins += 12;
        projectMedia += 3;
      }
    });

    const baseMorale = patronageMorale + postMorale + projectMorale;

    const patronageCorruption = faction.patronage * -1;
    const postCorruption = faction.post !== 'None' ? 2 : 0;
    const baseCorruption = patronageCorruption + postCorruption;

    const patronageMedia = faction.patronage * 1;
    const baseMedia = patronageMedia + projectMedia;

    const baseSupport = faction.loyalty >= 50 ? (faction.influence * 0.01) : -(faction.influence * 0.01);

    return {
      coins: Math.round(baseCoins * mult),
      support: parseFloat((baseSupport * mult).toFixed(1)),
      morale: Math.round(baseMorale * mult),
      corruption: Math.round(baseCorruption * (2 - mult)),
      media: Math.round(baseMedia * mult)
    };
  };

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
  const finalCorruption = totalYields.corruption <= 0 ? totalYields.corruption : Math.min(5, totalYields.corruption);

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
                    { id: 'veteran', name: 'Loyalists (Elder Statesmen)', reqL: 80, reqP: 50, desc: '+25 Coins, +3% Support per turn' },
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

          <div style={{ display: 'flex', marginTop: '14px' }}>
            <button
              onClick={handleUndo}
              disabled={history.length === 0}
              style={{
                width: '100%',
                padding: '8px 12px',
                background: '#ffffff',
                border: '1.5px solid var(--party-primary-color, var(--primary-border))',
                color: history.length > 0 ? 'var(--primary-dark)' : '#94a3b8',
                borderRadius: '6px',
                fontWeight: 'bold',
                cursor: history.length > 0 ? 'pointer' : 'default',
                fontSize: '12px',
                opacity: history.length > 0 ? 1 : 0.6
              }}
            >
              ↩ Undo
            </button>
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
            if (fid === 'veteran' && loyalty >= 80 && power >= 50) return 'Elder Statesmen';
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
                    <div style={{ fontSize: '11px', color: 'var(--card-text)', marginTop: '2px' }}>
                      Power: <b>{f.influence}%</b> | Loyalty: <b style={{ color: mood.color }}>{f.loyalty}%</b>
                    </div>
                  </div>
                </div>

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
                  {f.patronage === 0 && f.post === 'None' && f.projects.length === 0 ? (
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

                      {/* Post */}
                      {f.post !== 'None' && (
                        <div style={{
                          background: 'linear-gradient(135deg, #581c87 0%, #a855f7 100%)',
                          padding: '6px 10px',
                          borderRadius: '4px',
                          fontSize: '11.5px',
                          fontWeight: 'bold',
                          color: '#ffffff',
                          display: 'flex',
                          justifyContent: 'space-between',
                          alignItems: 'center'
                        }}>
                          <span>💼 {f.post}</span>
                          <span style={{ fontSize: '10px', opacity: 0.85 }}>{f.isPostPermanentlyAssigned ? '🔒 Locked' : '📌'}</span>
                        </div>
                      )}

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
                  <span style={{ color: '#15803d' }}>💰 +{y.coins}</span>
                  <span style={{ color: '#1d4ed8' }}>📈 +{y.support}%</span>
                  <span style={{ color: '#a21caf' }}>✊ +{y.morale}</span>
                  <span style={{ color: '#b91c1c' }}>⚖️ +{y.corruption}</span>
                  <span style={{ color: '#ec4899' }}>📢 +{y.media}</span>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
