import React, { useState, useEffect, useCallback, useRef } from 'react';
import { getFactionDisplayName } from '../gameUtils';
import { getPostByKey, getPostByName } from '../postsConfig';
import { lockPartyManagement } from '../../../api/apiClient';

/**
 * WR_Action3_Governance — Standalone War Room Governance & Party Management
 */
export default function WR_Action3_Governance({
  turnData,
  selectedIssueOptionKey,
  setSelectedIssueOptionKey,
  activeParty,
  selectedEventOptionKey,
  setSelectedEventOptionKey,
  scenarioEvents = [],
  projectDefs = {}
}) {
  const gameSessionId = turnData?.gameId || turnData?.scenarioId || 'default_session';
  const turnNumber = turnData?.turnNumber || 0;
  const storageKey = `political_sim_party_management_${gameSessionId}_turn_${turnNumber}`;

  const dominantFaction = (activeParty?.factions || []).find(f => f.active && f.influence > 50 && f.loyalty > 80);

  const factionsList = (activeParty?.factions || []).map(f => {
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
      isPermanentlyAssigned: true,
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
      isPostPermanentlyAssigned: postKeys.length > 0,
      frozenTurnsRemaining: f.frozenTurnsRemaining,
      frozenPosts: f.frozenPosts,
      frozenPatronageTurns: f.frozenPatronageTurns
    };
  });

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

  const partyMgmtState = turnData?.partyManagementState;

  const buildDeckFromBackendState = () => {
    const cards = [];
    if (partyMgmtState) {
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
      cards.push({ id: 'pat-1', type: 'patronage', name: 'Patronage Point', desc: 'Increases loyalty by +5%.', icon: '🛡️', color: 'linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%)' });
      const assignedPosts = (activeParty?.factions || []).flatMap(f => {
        const rawPost = f.post;
        return Array.isArray(rawPost) ? rawPost : (rawPost && rawPost !== 'None' ? [rawPost] : []);
      });
      if (!assignedPosts.includes('SECRETARY') && !assignedPosts.includes('Secretary')) cards.push({ id: 'post-1', postKey: 'SECRETARY', type: 'post', name: 'Secretary', desc: 'Chief administrator. +15 Loyalty, +6 Morale/turn.', icon: '📋', loyaltyBoost: 15, coinBonus: 0, moraleBonus: 6, mediaBonus: 0, color: 'linear-gradient(135deg, #581c87 0%, #a855f7 100%)' });
      if (!assignedPosts.includes('FUND_MANAGER') && !assignedPosts.includes('Fund Manager')) cards.push({ id: 'post-2', postKey: 'FUND_MANAGER', type: 'post', name: 'Fund Manager', desc: 'Oversees finances. +10 Loyalty, +8 Coins/turn.', icon: '💰', loyaltyBoost: 10, coinBonus: 8, moraleBonus: 0, mediaBonus: 0, color: 'linear-gradient(135deg, #581c87 0%, #a855f7 100%)' });
    }
    cards.push(...projectCards);
    return cards;
  };

  const initialDeck = buildDeckFromBackendState();

  const getInitialFactions = (partyState, factionsList) => {
    const defaults = [
      { id: 'loyalist', name: 'Loyalists', baseLoyalty: 75, loyalty: 75, influence: 45, post: [], patronage: 0, projects: [], active: true, accentColor: '#ef4444' },
      { id: 'youth', name: 'Youth Wing', baseLoyalty: 75, loyalty: 75, influence: 35, post: [], patronage: 0, projects: [], active: true, accentColor: '#f97316' },
      { id: 'trade', name: 'Trade Unions', baseLoyalty: 75, loyalty: 75, influence: 20, post: [], patronage: 0, projects: [], active: true, accentColor: '#14b8a6' }
    ];

    const baseList = (factionsList && factionsList.length > 0) ? factionsList : defaults;
    if (!partyState) return baseList;

    return baseList.map(faction => {
      const livePatronage = partyState.allocatedPatronagePoints?.[faction.id] ?? faction.patronage ?? 0;
      const assignedPostsForFaction = (partyState.posts || [])
        .filter(p => p.status === 'ASSIGNED' && p.assignedFactionKey === faction.id)
        .map(p => p.postKey);

      const rawPost = faction.post;
      const existingPosts = Array.isArray(rawPost) ? rawPost : (rawPost && rawPost !== 'None' ? [rawPost] : []);
      const normalizedExisting = existingPosts.map(p => {
        const def = getPostByName(p);
        return def ? def.key : p;
      });

      const allPosts = Array.from(new Set([...normalizedExisting, ...assignedPostsForFaction]));

      // Parse projects assigned to this faction from partyState and activeParty
      const partyStateProjects = partyState.projects
        ? Object.entries(partyState.projects)
            .filter(([projKey, fId]) => fId === faction.id)
            .map(([projKey]) => {
              const def = (activeParty?.projects || []).find(p => p.projectKey === projKey || p.id === projKey);
              return {
                id: projKey,
                projectKey: projKey,
                type: 'project',
                name: def?.name || projKey,
                desc: def?.yieldDesc || 'Completed party building.',
                icon: def?.icon || '🏗️',
                color: 'linear-gradient(135deg, #115e59 0%, #0d9488 100%)'
              };
            })
        : [];

      const existingProjects = faction.projects || [];
      const projectMap = new Map();
      [...existingProjects, ...partyStateProjects].forEach(p => {
        if (p) projectMap.set(p.id || p.projectKey, p);
      });

      return {
        ...faction,
        patronage: livePatronage,
        post: allPosts,
        projects: Array.from(projectMap.values())
      };
    });
  };

  const initialFactions = getInitialFactions(partyMgmtState, factionsList);

  const [factions, setFactions] = useState(() => {
    const saved = localStorage.getItem(storageKey);
    if (saved) {
      try {
        const parsed = JSON.parse(saved);
        if (parsed.factions) return parsed.factions;
      } catch (e) {
        console.error("Failed to parse factions state", e);
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
        console.error("Failed to parse deck state", e);
      }
    }
    return buildDeckFromBackendState();
  });

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
        console.error("Failed to parse history state", e);
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
        console.error("Failed to parse factionCrisisChoice", e);
      }
    }
    return null;
  });

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

  useEffect(() => {
    if (allCardsAssigned) {
      const timer = setTimeout(() => {
        confirmBtnRef.current?.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }, 200);
      return () => clearTimeout(timer);
    }
  }, [allCardsAssigned]);

  const [showCrisisModal, setShowCrisisModal] = useState(false);
  const [detailFactionId, setDetailFactionId] = useState(null);

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
      const projects = {};
      factions.forEach(f => {
        (f.projects || []).forEach(p => { projects[p.id || p.projectKey] = f.id; });
      });

      await lockPartyManagement(gameId, partyId, { patronageUsed, postAssignments, factions: factionsPayload, projects });
      setIsLocked(true);
      if (setSelectedIssueOptionKey) setSelectedIssueOptionKey('mock_done');
    } catch (err) {
      console.error('[PartyMgmt] Lock failed:', err);
      setLockError(err.message || 'Failed to lock allocations.');
    } finally {
      setIsLocking(false);
    }
  }, [isLocked, isLocking, factions, assignedPostKeys, activeParty, turnData, setSelectedIssueOptionKey]);

  useEffect(() => {
    if (activeParty?.activeFactionCrisisKey && !factionCrisisChoice) {
      setShowCrisisModal(true);
    }
  }, [activeParty, factionCrisisChoice]);

  const pushHistory = (currentDeck, currentFactions) => {
    setHistory(prev => [...prev, { deck: [...currentDeck], factions: JSON.parse(JSON.stringify(currentFactions)) }]);
  };

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

    if (cardToAllocate.type === 'post' && cardToAllocate.postKey) {
      setAssignedPostKeys(prev => ({ ...prev, [cardToAllocate.postKey]: factionId }));
    }

    setDeck(newDeck);
    setFactions(updatedFactions);
  };

  const topCard = deck[0];
  const totalCards = deck.length + history.length;
  const allocatedCount = history.length;
  const activeFactions = factions.filter(f => f.active);
  const detailFaction = activeFactions.find(f => f.id === detailFactionId);

  /* ── Undo last allocation ── */
  const handleUndo = () => {
    if (history.length === 0) return;
    const last = history[history.length - 1];
    setFactions(last.factions);
    setDeck(last.deck);
    setHistory(prev => prev.slice(0, -1));
    // Also remove last assigned post key if the restored card was a post
    const restoredCard = last.deck[0];
    if (restoredCard?.type === 'post' && restoredCard.postKey) {
      setAssignedPostKeys(prev => {
        const copy = { ...prev };
        delete copy[restoredCard.postKey];
        return copy;
      });
    }
  };

  /* ── Card type accent config ── */
  const getCardTypeConfig = (card) => {
    if (!card) return { accent: '#64748B', badge: 'Resource', badgeBg: 'rgba(100,116,139,0.2)' };
    switch (card.type) {
      case 'patronage':
        return { accent: '#3B82F6', badge: 'Patronage', badgeBg: 'rgba(59,130,246,0.15)' };
      case 'post':
        return { accent: '#A855F7', badge: 'Leadership Post', badgeBg: 'rgba(168,85,247,0.15)' };
      case 'project':
        return { accent: '#14B8A6', badge: 'Project', badgeBg: 'rgba(20,184,166,0.15)' };
      default:
        return { accent: '#64748B', badge: 'Resource', badgeBg: 'rgba(100,116,139,0.2)' };
    }
  };

  const cardConfig = getCardTypeConfig(topCard);

  return (
    <div style={{ padding: '14px 16px' }}>
      {/* Section Header */}
      <div style={{ marginBottom: '14px' }}>
        <div style={{ fontSize: '15px', fontWeight: 900, letterSpacing: '0.05em', textTransform: 'uppercase', color: '#34D399' }}>
          ⚖️ Party Management & Governance
        </div>
        <div style={{ fontSize: '12px', color: '#7D8590', marginTop: '2px' }}>
          Allocate resources, posts & projects to factions · <em>Tap any faction for details</em>
        </div>
      </div>

      {/* ── Faction Status Strip (Clickable Cards) ── */}
      <div style={{
        display: 'flex',
        gap: '6px',
        marginBottom: '14px',
      }}>
        {activeFactions.map(f => {
          const postCount = Array.isArray(f.post) ? f.post.length : (f.post && f.post !== 'None' ? 1 : 0);
          const projectCount = f.projects?.length || 0;
          return (
            <div
              key={f.id}
              onClick={() => setDetailFactionId(f.id)}
              title="Click to view posts, buildings & yield details"
              style={{
                flex: 1,
                background: 'linear-gradient(145deg, rgba(30,41,59,0.7), rgba(15,23,42,0.8))',
                border: `1.5px solid ${detailFactionId === f.id ? '#38BDF8' : `${f.accentColor}40`}`,
                borderRadius: '10px',
                padding: '8px 6px',
                textAlign: 'center',
                cursor: 'pointer',
                touchAction: 'manipulation',
                transition: 'all 0.2s ease',
                boxShadow: detailFactionId === f.id ? '0 0 14px rgba(56, 189, 248, 0.4)' : 'none',
                WebkitTapHighlightColor: 'transparent',
              }}
            >
              <div style={{ fontSize: '11px', fontWeight: 900, color: '#e2e8f0', marginBottom: '2px', lineHeight: 1.2, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '3px' }}>
                <span>{f.name}</span>
                <span style={{ fontSize: '9px', opacity: 0.6 }}>ℹ️</span>
              </div>
              <div style={{
                fontSize: '13px', fontWeight: 900,
                color: f.loyalty >= 70 ? '#4ADE80' : f.loyalty >= 40 ? '#FBBF24' : '#F87171',
                marginBottom: '4px',
              }}>
                {f.loyalty}% <span style={{ fontSize: '8px', color: '#64748B', fontWeight: 700 }}>LOYALTY</span>
              </div>
              {/* Asset counts (Enlarged symbols & numbers) */}
              <div style={{
                display: 'flex',
                justifyContent: 'center',
                gap: '4px',
                marginTop: '4px',
              }}>
                <span
                  title="Patronage Points"
                  style={{
                    fontSize: '11px', fontWeight: 900,
                    background: 'rgba(59,130,246,0.2)', color: '#93C5FD',
                    border: '1px solid rgba(59,130,246,0.4)',
                    padding: '2px 5px', borderRadius: '6px',
                    display: 'inline-flex', alignItems: 'center', gap: '3px',
                  }}
                >
                  <span style={{ fontSize: '13px' }}>🛡️</span> {f.patronage || 0}
                </span>
                <span
                  title="Leadership Posts"
                  style={{
                    fontSize: '11px', fontWeight: 900,
                    background: 'rgba(168,85,247,0.2)', color: '#E9D5FF',
                    border: '1px solid rgba(168,85,247,0.4)',
                    padding: '2px 5px', borderRadius: '6px',
                    display: 'inline-flex', alignItems: 'center', gap: '3px',
                  }}
                >
                  <span style={{ fontSize: '13px' }}>💼</span> {postCount}
                </span>
                <span
                  title="Party Buildings / Projects"
                  style={{
                    fontSize: '11px', fontWeight: 900,
                    background: 'rgba(20,184,166,0.2)', color: '#99F6E4',
                    border: '1px solid rgba(20,184,166,0.4)',
                    padding: '2px 5px', borderRadius: '6px',
                    display: 'inline-flex', alignItems: 'center', gap: '3px',
                  }}
                >
                  <span style={{ fontSize: '13px' }}>🏗️</span> {projectCount}
                </span>
              </div>
            </div>
          );
        })}
      </div>

      {/* ── Progress Bar ── */}
      {totalCards > 0 && (
        <div style={{ marginBottom: '14px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
            <span style={{ fontSize: '10px', fontWeight: 800, color: '#94a3b8', textTransform: 'uppercase', letterSpacing: '0.04em' }}>
              {isLocked ? 'All Allocations Confirmed' : deck.length === 0 ? 'All Cards Allocated' : `Card ${allocatedCount + 1} of ${totalCards}`}
            </span>
            <span style={{ fontSize: '10px', fontWeight: 800, color: isLocked || deck.length === 0 ? '#4ADE80' : '#38BDF8' }}>
              {allocatedCount}/{totalCards}
            </span>
          </div>
          <div style={{
            width: '100%', height: '4px',
            background: 'rgba(255,255,255,0.08)',
            borderRadius: '2px',
            overflow: 'hidden',
          }}>
            <div style={{
              height: '100%',
              width: totalCards > 0 ? `${(allocatedCount / totalCards) * 100}%` : '0%',
              background: isLocked ? '#4ADE80' : 'linear-gradient(90deg, #38BDF8, #818CF8)',
              borderRadius: '2px',
              transition: 'width 0.4s ease',
            }} />
          </div>
        </div>
      )}

      {/* ── Main Card Display ── */}
      {topCard && !isLocked ? (
        <div style={{
          background: 'linear-gradient(160deg, rgba(30,41,59,0.9), rgba(15,23,42,0.95))',
          border: `1.5px solid ${cardConfig.accent}55`,
          borderRadius: '16px',
          overflow: 'hidden',
          boxShadow: `0 8px 32px rgba(0,0,0,0.35), 0 0 20px ${cardConfig.accent}15`,
          marginBottom: '14px',
        }}>
          {/* Card Header Gradient Bar */}
          <div style={{
            height: '4px',
            background: topCard.color || `linear-gradient(90deg, ${cardConfig.accent}, ${cardConfig.accent}80)`,
          }} />

          {/* Card Body */}
          <div style={{ padding: '18px 16px 14px 16px' }}>
            {/* Type Badge */}
            <div style={{
              display: 'inline-block',
              padding: '3px 10px',
              borderRadius: '20px',
              background: cardConfig.badgeBg,
              border: `1px solid ${cardConfig.accent}44`,
              fontSize: '9px',
              fontWeight: 900,
              color: cardConfig.accent,
              textTransform: 'uppercase',
              letterSpacing: '0.06em',
              marginBottom: '10px',
            }}>
              {cardConfig.badge}
            </div>

            {/* Card Icon + Name */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '8px' }}>
              <div style={{
                width: '42px', height: '42px',
                borderRadius: '12px',
                background: topCard.color || 'linear-gradient(135deg, #1e3a8a, #3b82f6)',
                display: 'flex', alignItems: 'center', justifyContent: 'center',
                fontSize: '22px',
                boxShadow: `0 4px 12px ${cardConfig.accent}30`,
                flexShrink: 0,
              }}>
                {topCard.icon}
              </div>
              <div>
                <div style={{ fontSize: '17px', fontWeight: 900, color: '#F1F5F9', lineHeight: 1.2 }}>
                  {topCard.name}
                </div>
                {topCard.type === 'post' && topCard.loyaltyBoost && (
                  <div style={{ fontSize: '10px', fontWeight: 700, color: cardConfig.accent, marginTop: '2px' }}>
                    +{topCard.loyaltyBoost} Loyalty
                    {topCard.coinBonus ? ` · +${topCard.coinBonus} Coins/turn` : ''}
                    {topCard.moraleBonus ? ` · +${topCard.moraleBonus} Morale/turn` : ''}
                  </div>
                )}
              </div>
            </div>

            {/* Card Description */}
            <div style={{
              fontSize: '12px', color: '#94a3b8', lineHeight: 1.5,
              marginBottom: '16px',
              padding: '10px 12px',
              background: 'rgba(0,0,0,0.2)',
              borderRadius: '10px',
              border: '1px solid rgba(255,255,255,0.04)',
            }}>
              {topCard.desc}
            </div>

            {/* ── Divider with label ── */}
            <div style={{
              display: 'flex', alignItems: 'center', gap: '10px',
              marginBottom: '12px',
            }}>
              <div style={{ flex: 1, height: '1px', background: 'rgba(255,255,255,0.08)' }} />
              <span style={{
                fontSize: '9px', fontWeight: 900, color: '#64748B',
                textTransform: 'uppercase', letterSpacing: '0.08em',
                whiteSpace: 'nowrap',
              }}>
                Assign to Faction
              </span>
              <div style={{ flex: 1, height: '1px', background: 'rgba(255,255,255,0.08)' }} />
            </div>

            {/* ── Faction Allocation Buttons ── */}
            <div style={{
              display: 'flex',
              flexDirection: 'column',
              gap: '8px',
            }}>
              {activeFactions.map(f => {
                const isFrozen = f.frozenTurnsRemaining > 0;
                const postList = Array.isArray(f.post) ? f.post : (f.post && f.post !== 'None' ? [f.post] : []);
                const projectCount = f.projects?.length || 0;

                return (
                  <button
                    key={f.id}
                    type="button"
                    onClick={() => !isFrozen && handleAllocate(f.id)}
                    disabled={isFrozen}
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: '12px',
                      width: '100%',
                      padding: '10px 14px',
                      background: isFrozen
                        ? 'rgba(30,41,59,0.4)'
                        : `linear-gradient(135deg, rgba(30,41,59,0.6), rgba(15,23,42,0.7))`,
                      border: `1.5px solid ${isFrozen ? 'rgba(255,255,255,0.06)' : `${f.accentColor}50`}`,
                      borderRadius: '12px',
                      cursor: isFrozen ? 'not-allowed' : 'pointer',
                      touchAction: 'manipulation',
                      opacity: isFrozen ? 0.45 : 1,
                      transition: 'all 0.2s ease',
                      textAlign: 'left',
                      WebkitTapHighlightColor: 'transparent',
                    }}
                  >
                    {/* Faction Avatar */}
                    <div style={{
                      width: '38px', height: '38px',
                      borderRadius: '10px',
                      background: `${f.accentColor}22`,
                      border: `1.5px solid ${f.accentColor}55`,
                      display: 'flex', alignItems: 'center', justifyContent: 'center',
                      fontSize: '16px', fontWeight: 900,
                      color: f.accentColor,
                      flexShrink: 0,
                    }}>
                      {f.name.charAt(0)}
                    </div>

                    {/* Faction Info & Assets Breakdown */}
                    <div style={{ flex: 1, minWidth: 0 }}>
                      <div style={{ fontSize: '13px', fontWeight: 900, color: '#E2E8F0', lineHeight: 1.2 }}>
                        {f.name}
                      </div>
                      <div style={{ fontSize: '11px', fontWeight: 800, color: '#94a3b8', marginTop: '4px', display: 'flex', flexWrap: 'wrap', gap: '10px', alignItems: 'center' }}>
                        <span style={{ display: 'inline-flex', alignItems: 'center', gap: '3px' }}>
                          <span style={{ fontSize: '14px' }}>🛡️</span> Patronage: <strong style={{ fontSize: '13px', color: '#93C5FD' }}>{f.patronage || 0}</strong>
                        </span>
                        <span style={{ display: 'inline-flex', alignItems: 'center', gap: '3px' }}>
                          <span style={{ fontSize: '14px' }}>💼</span> Posts: <strong style={{ fontSize: '12px', color: '#E9D5FF' }}>{postList.length > 0 ? postList.join(', ') : 'None'}</strong>
                        </span>
                        <span style={{ display: 'inline-flex', alignItems: 'center', gap: '3px' }}>
                          <span style={{ fontSize: '14px' }}>🏗️</span> Buildings: <strong style={{ fontSize: '13px', color: '#99F6E4' }}>{projectCount}</strong>
                        </span>
                      </div>
                    </div>

                    {/* Loyalty Badge */}
                    <div style={{
                      padding: '4px 10px',
                      borderRadius: '20px',
                      background: `${f.accentColor}18`,
                      border: `1px solid ${f.accentColor}40`,
                      fontSize: '11px',
                      fontWeight: 900,
                      color: f.accentColor,
                      flexShrink: 0,
                      whiteSpace: 'nowrap',
                    }}>
                      {f.loyalty}%
                    </div>
                  </button>
                );
              })}
            </div>

            {/* ── Undo button ── */}
            {history.length > 0 && (
              <button
                type="button"
                onClick={handleUndo}
                style={{
                  marginTop: '12px',
                  width: '100%',
                  padding: '8px',
                  background: 'transparent',
                  border: '1px solid rgba(255,255,255,0.12)',
                  borderRadius: '8px',
                  color: '#94a3b8',
                  fontSize: '11px',
                  fontWeight: 800,
                  cursor: 'pointer',
                  touchAction: 'manipulation',
                }}
              >
                ↩ Undo Last Allocation
              </button>
            )}
          </div>
        </div>
      ) : (
        /* ── All Allocated / Locked State ── */
        <div style={{
          background: 'linear-gradient(145deg, rgba(30,41,59,0.8), rgba(15,23,42,0.9))',
          border: `1.5px solid ${isLocked ? 'rgba(74,222,128,0.3)' : 'rgba(56,189,248,0.3)'}`,
          borderRadius: '16px',
          padding: '24px 16px',
          textAlign: 'center',
          marginBottom: '14px',
        }}>
          <div style={{ fontSize: '28px', marginBottom: '8px' }}>
            {isLocked ? '✅' : '🎉'}
          </div>
          <div style={{ fontSize: '14px', fontWeight: 900, color: isLocked ? '#4ADE80' : '#38BDF8', marginBottom: '6px' }}>
            {isLocked ? 'Allocations Confirmed & Locked' : 'All Cards Allocated!'}
          </div>
          <div style={{ fontSize: '11px', color: '#64748B' }}>
            {isLocked
              ? 'Your party management decisions have been submitted.'
              : 'Review your allocations below, then confirm to lock.'}
          </div>

          {/* Allocation Summary */}
          {!isLocked && (
            <div style={{ display: 'flex', gap: '8px', marginTop: '14px', justifyContent: 'center', flexWrap: 'wrap' }}>
              {activeFactions.map(f => {
                const postList = Array.isArray(f.post) ? f.post : (f.post && f.post !== 'None' ? [f.post] : []);
                return (
                  <div key={f.id} style={{
                    padding: '8px 12px',
                    background: `${f.accentColor}12`,
                    border: `1px solid ${f.accentColor}30`,
                    borderRadius: '10px',
                    textAlign: 'center',
                    minWidth: '100px',
                  }}>
                    <div style={{ fontSize: '12px', fontWeight: 900, color: f.accentColor }}>{f.name} ({f.loyalty}%)</div>
                    <div style={{ fontSize: '9px', fontWeight: 700, color: '#94a3b8', marginTop: '3px' }}>
                      🛡️ {f.patronage || 0} Pat · 💼 {postList.length} Posts · 🏗️ {f.projects?.length || 0} Builds
                    </div>
                  </div>
                );
              })}
            </div>
          )}

          {/* Undo even when all allocated */}
          {!isLocked && history.length > 0 && (
            <button
              type="button"
              onClick={handleUndo}
              style={{
                marginTop: '12px',
                padding: '6px 16px',
                background: 'transparent',
                border: '1px solid rgba(255,255,255,0.12)',
                borderRadius: '8px',
                color: '#94a3b8',
                fontSize: '11px',
                fontWeight: 800,
                cursor: 'pointer',
                touchAction: 'manipulation',
              }}
            >
              ↩ Undo Last
            </button>
          )}
        </div>
      )}

      {/* ── Lock Error ── */}
      {lockError && (
        <div style={{ color: '#F87171', fontSize: '12px', fontWeight: 700, marginBottom: '10px', textAlign: 'center' }}>
          ⚠️ {lockError}
        </div>
      )}

      {/* ── Confirm & Lock Button ── */}
      {!isLocked && (
        <button
          ref={confirmBtnRef}
          type="button"
          onClick={handleLock}
          disabled={isLocking || deck.length > 0}
          style={{
            width: '100%',
            padding: '14px',
            background: deck.length > 0
              ? 'rgba(100,116,139,0.15)'
              : 'linear-gradient(135deg, #10b981, #059669)',
            color: deck.length > 0 ? '#475569' : '#ffffff',
            border: deck.length > 0 ? '1px solid rgba(255,255,255,0.08)' : 'none',
            borderRadius: '12px',
            fontSize: '13px',
            fontWeight: 900,
            textTransform: 'uppercase',
            letterSpacing: '0.04em',
            cursor: deck.length > 0 ? 'default' : 'pointer',
            touchAction: 'manipulation',
            opacity: isLocking ? 0.6 : 1,
            boxShadow: deck.length === 0 ? '0 4px 16px rgba(16,185,129,0.3)' : 'none',
            transition: 'all 0.3s ease',
          }}
        >
          {isLocking ? '⏳ Locking...' : deck.length > 0 ? `${deck.length} Card${deck.length > 1 ? 's' : ''} Remaining` : 'Confirm & Lock Allocations'}
        </button>
      )}

      {/* ── FACTION DETAILS MODAL ── */}
      {detailFaction && (
        <div
          style={{
            position: 'fixed',
            top: 0, left: 0, right: 0, bottom: 0,
            background: 'rgba(0, 0, 0, 0.8)',
            backdropFilter: 'blur(8px)',
            zIndex: 9999,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            padding: '16px',
            animation: 'wr-slide-in 0.25s ease-out',
          }}
          onClick={() => setDetailFactionId(null)}
        >
          <div
            style={{
              width: '100%',
              maxWidth: '460px',
              maxHeight: '85vh',
              overflowY: 'auto',
              background: 'linear-gradient(160deg, #1e293b 0%, #0f172a 100%)',
              border: `2px solid ${detailFaction.accentColor}`,
              borderRadius: '20px',
              padding: '20px',
              boxShadow: `0 20px 50px rgba(0,0,0,0.7), 0 0 30px ${detailFaction.accentColor}33`,
              position: 'relative',
            }}
            onClick={e => e.stopPropagation()}
          >
            {/* Close Button */}
            <button
              type="button"
              onClick={() => setDetailFactionId(null)}
              style={{
                position: 'absolute',
                top: '16px',
                right: '16px',
                width: '32px',
                height: '32px',
                borderRadius: '50%',
                background: 'rgba(255,255,255,0.1)',
                border: '1px solid rgba(255,255,255,0.2)',
                color: '#ffffff',
                fontSize: '16px',
                fontWeight: 900,
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                touchAction: 'manipulation',
              }}
            >
              ✕
            </button>

            {/* Modal Header */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '16px' }}>
              <div style={{
                width: '46px',
                height: '46px',
                borderRadius: '14px',
                background: `${detailFaction.accentColor}25`,
                border: `2px solid ${detailFaction.accentColor}`,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: '20px',
                fontWeight: 900,
                color: detailFaction.accentColor,
              }}>
                {detailFaction.name.charAt(0)}
              </div>
              <div>
                <div style={{ fontSize: '18px', fontWeight: 900, color: '#ffffff' }}>
                  {detailFaction.name}
                </div>
                <div style={{ fontSize: '11px', color: '#94a3b8', marginTop: '2px' }}>
                  Power Share: <strong>{detailFaction.influence}%</strong> · Loyalty:{' '}
                  <strong style={{
                    color: detailFaction.loyalty >= 70 ? '#4ADE80' : detailFaction.loyalty >= 40 ? '#FBBF24' : '#F87171'
                  }}>
                    {detailFaction.loyalty}%
                  </strong>
                </div>
              </div>
            </div>

            {/* ── SECTION 1: LEADERSHIP POSTS ── */}
            <div style={{ marginBottom: '18px' }}>
              <div style={{
                fontSize: '11px', fontWeight: 900, color: '#A855F7',
                textTransform: 'uppercase', letterSpacing: '0.06em',
                marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '6px'
              }}>
                <span>💼 Leadership Posts</span>
                <span style={{
                  padding: '2px 7px', borderRadius: '10px',
                  background: 'rgba(168,85,247,0.15)', fontSize: '9px'
                }}>
                  {Array.isArray(detailFaction.post) ? detailFaction.post.length : (detailFaction.post && detailFaction.post !== 'None' ? 1 : 0)}
                </span>
              </div>

              {(() => {
                const rawPosts = detailFaction.post;
                const postList = Array.isArray(rawPosts) ? rawPosts : (rawPosts && rawPosts !== 'None' ? [rawPosts] : []);
                if (postList.length === 0) {
                  return (
                    <div style={{ fontSize: '11px', color: '#64748B', fontStyle: 'italic', padding: '8px 12px', background: 'rgba(0,0,0,0.2)', borderRadius: '8px' }}>
                      No leadership posts assigned to this faction.
                    </div>
                  );
                }
                return (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                    {postList.map((pKey, idx) => {
                      const def = getPostByKey(pKey) || getPostByName(pKey);
                      return (
                        <div key={idx} style={{
                          background: 'linear-gradient(135deg, rgba(88,28,135,0.25), rgba(30,41,59,0.5))',
                          border: '1px solid rgba(168,85,247,0.3)',
                          borderRadius: '10px',
                          padding: '10px 12px',
                        }}>
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
                            <span style={{ fontSize: '13px', fontWeight: 900, color: '#E9D5FF' }}>
                              {def?.icon || '💼'} {def?.name || pKey}
                            </span>
                            <span style={{ fontSize: '10px', fontWeight: 800, color: '#A855F7', background: 'rgba(168,85,247,0.2)', padding: '2px 6px', borderRadius: '6px' }}>
                              +{def?.loyaltyBoost || 10} Loyalty
                            </span>
                          </div>
                          <div style={{ fontSize: '11px', color: '#cbd5e1', lineHeight: 1.4, marginBottom: '6px' }}>
                            {def?.desc || 'Assigns a key leadership position in the party.'}
                          </div>
                          {/* Yield Badges */}
                          <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap' }}>
                            {(def?.coinBonus > 0 || !def) && (
                              <span style={{ fontSize: '9px', fontWeight: 800, color: '#FBBF24', background: 'rgba(245,158,11,0.15)', padding: '2px 6px', borderRadius: '4px' }}>
                                🪙 +{def?.coinBonus || 8} Coins/turn
                              </span>
                            )}
                            {(def?.moraleBonus > 0 || !def) && (
                              <span style={{ fontSize: '9px', fontWeight: 800, color: '#38BDF8', background: 'rgba(56,189,248,0.15)', padding: '2px 6px', borderRadius: '4px' }}>
                                 +{def?.moraleBonus || 6} Morale/turn
                              </span>
                            )}
                            {def?.mediaBonus > 0 && (
                              <span style={{ fontSize: '9px', fontWeight: 800, color: '#EC4899', background: 'rgba(236,72,153,0.15)', padding: '2px 6px', borderRadius: '4px' }}>
                                📺 +{def.mediaBonus} Media Image/turn
                              </span>
                            )}
                          </div>
                        </div>
                      );
                    })}
                  </div>
                );
              })()}
            </div>

            {/* ── SECTION 2: PARTY BUILDINGS & PROJECTS ── */}
            <div style={{ marginBottom: '18px' }}>
              <div style={{
                fontSize: '11px', fontWeight: 900, color: '#14B8A6',
                textTransform: 'uppercase', letterSpacing: '0.06em',
                marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '6px'
              }}>
                <span>🏗️ Party Buildings & Projects</span>
                <span style={{
                  padding: '2px 7px', borderRadius: '10px',
                  background: 'rgba(20,184,166,0.15)', fontSize: '9px'
                }}>
                  {detailFaction.projects?.length || 0}
                </span>
              </div>

              {(!detailFaction.projects || detailFaction.projects.length === 0) ? (
                <div style={{ fontSize: '11px', color: '#64748B', fontStyle: 'italic', padding: '8px 12px', background: 'rgba(0,0,0,0.2)', borderRadius: '8px' }}>
                  No party buildings or projects assigned to this faction.
                </div>
              ) : (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  {detailFaction.projects.map((proj, idx) => (
                    <div key={idx} style={{
                      background: 'linear-gradient(135deg, rgba(17,94,89,0.25), rgba(30,41,59,0.5))',
                      border: '1px solid rgba(20,184,166,0.3)',
                      borderRadius: '10px',
                      padding: '10px 12px',
                    }}>
                      <div style={{ fontSize: '13px', fontWeight: 900, color: '#99F6E4', marginBottom: '4px' }}>
                        {proj.icon || '🏗️'} {proj.name}
                      </div>
                      <div style={{ fontSize: '11px', color: '#cbd5e1', lineHeight: 1.4 }}>
                        {proj.desc || proj.yieldDesc || 'Completed party infrastructure.'}
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>

            {/* ── SECTION 3: PATRONAGE POINTS ── */}
            <div style={{ marginBottom: '18px' }}>
              <div style={{
                fontSize: '11px', fontWeight: 900, color: '#3B82F6',
                textTransform: 'uppercase', letterSpacing: '0.06em',
                marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '6px'
              }}>
                <span>🛡️ Patronage Allocation</span>
                <span style={{
                  padding: '2px 7px', borderRadius: '10px',
                  background: 'rgba(59,130,246,0.15)', fontSize: '9px'
                }}>
                  {detailFaction.patronage || 0} Points
                </span>
              </div>

              {detailFaction.patronage > 0 ? (
                <div style={{
                  background: 'linear-gradient(135deg, rgba(30,58,138,0.25), rgba(30,41,59,0.5))',
                  border: '1px solid rgba(59,130,246,0.3)',
                  borderRadius: '10px',
                  padding: '10px 12px',
                }}>
                  <div style={{ fontSize: '12px', fontWeight: 800, color: '#93C5FD', marginBottom: '6px' }}>
                    🛡️ {detailFaction.patronage} Patronage Point{detailFaction.patronage > 1 ? 's' : ''} Allocated
                  </div>
                  <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap' }}>
                    <span style={{ fontSize: '9px', fontWeight: 800, color: '#4ADE80', background: 'rgba(74,222,128,0.15)', padding: '2px 6px', borderRadius: '4px' }}>
                      +{detailFaction.patronage * 5}% Loyalty
                    </span>
                    <span style={{ fontSize: '9px', fontWeight: 800, color: '#FBBF24', background: 'rgba(245,158,11,0.15)', padding: '2px 6px', borderRadius: '4px' }}>
                      🪙 +{detailFaction.patronage * 2} Coins/turn
                    </span>
                    <span style={{ fontSize: '9px', fontWeight: 800, color: '#38BDF8', background: 'rgba(56,189,248,0.15)', padding: '2px 6px', borderRadius: '4px' }}>
                       +{detailFaction.patronage * 1} Morale/turn
                    </span>
                    <span style={{ fontSize: '9px', fontWeight: 800, color: '#A7F3D0', background: 'rgba(167,243,208,0.15)', padding: '2px 6px', borderRadius: '4px' }}>
                      📉 -{detailFaction.patronage * 1} Corruption
                    </span>
                    <span style={{ fontSize: '9px', fontWeight: 800, color: '#EC4899', background: 'rgba(236,72,153,0.15)', padding: '2px 6px', borderRadius: '4px' }}>
                      📺 +{detailFaction.patronage * 1} Media Image
                    </span>
                  </div>
                </div>
              ) : (
                <div style={{ fontSize: '11px', color: '#64748B', fontStyle: 'italic', padding: '8px 12px', background: 'rgba(0,0,0,0.2)', borderRadius: '8px' }}>
                  No patronage points allocated to this faction.
                </div>
              )}
            </div>

            {/* Close Modal Button */}
            <button
              type="button"
              onClick={() => setDetailFactionId(null)}
              style={{
                width: '100%',
                padding: '12px',
                background: 'linear-gradient(135deg, #334155, #1E293B)',
                border: '1px solid rgba(255,255,255,0.15)',
                borderRadius: '10px',
                color: '#ffffff',
                fontSize: '12px',
                fontWeight: 900,
                textTransform: 'uppercase',
                cursor: 'pointer',
                touchAction: 'manipulation',
              }}
            >
              Close Details
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

