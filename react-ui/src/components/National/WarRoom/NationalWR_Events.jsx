import React, { useState, useEffect } from 'react';
import {
  fetchNationalEvents,
  respondToNationalEvent,
  fetchNationalThemes,
  chooseNationalThemeAction,
  setNationalTargetParty,
  allocateNationalMediaSocial,
  cancelNationalMediaSocial
} from '../../../api/apiClient';

export default function NationalWR_Events({ activeGame, configData, onGameUpdate, isCompleted = false, onMarkCompleted }) {
  const gameId = activeGame?.id || activeGame?._id || activeGame?.userId || 'local';

  const [events, setEvents] = useState([]);
  const [themesData, setThemesData] = useState({ themes: [] });
  const [selectedThemeKey, setSelectedThemeKey] = useState(null);

  const getInitialTargetParty = () => {
    if (activeGame?.targetPartyKey) return activeGame.targetPartyKey;
    if (typeof window !== 'undefined') {
      const stored = localStorage.getItem(`national_target_party_${gameId}`) || localStorage.getItem('national_target_party_last');
      if (stored) return stored;
    }
    return '';
  };

  const [selectedTargetParty, setSelectedTargetParty] = useState(getInitialTargetParty);
  const [mediaAllocations, setMediaAllocations] = useState({
    social_ads: 0,
    influencer_collabs: 0,
    podcasts: 0,
    whatsapp_networks: 0
  });
  const [mediaCommitted, setMediaCommitted] = useState(false);
  const [loading, setLoading] = useState(false);
  const [actionLoading, setActionLoading] = useState(false);
  const [mediaLoading, setMediaLoading] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  // Find player's party and alliance state
  const playerPartyKey = activeGame?.partyKey;
  const playerState = activeGame?.partyStates?.find(
    p => (p.partyKey || '').toLowerCase() === (playerPartyKey || '').toLowerCase()
  ) || null;

  const playerFunds = playerState?.funds ?? activeGame?.playerFunds ?? 15.0;

  const playerAlliance = (activeGame?.alliances || []).find(a =>
    (a.leaderPartyKey || '').toLowerCase() === (playerPartyKey || '').toLowerCase() ||
    (a.members || []).some(m => (m.partyKey || '').toLowerCase() === (playerPartyKey || '').toLowerCase())
  );

  const rulingAllianceKey = activeGame?.rulingAllianceKey || 'NDA';
  const isRuling = playerAlliance 
    ? (playerAlliance.allianceId || '').toLowerCase() === rulingAllianceKey.toLowerCase() || (playerAlliance.allianceName || '').includes(rulingAllianceKey)
    : (playerState?.currentAllianceId || '').toLowerCase() === rulingAllianceKey.toLowerCase();

  const isPlayerInPower = themesData?.isPlayerInPower !== undefined ? themesData.isPlayerInPower : isRuling;

  const currentThemeKey = activeGame?.activeThemeKey || null;
  const currentThemeAction = activeGame?.activeThemeAction || null;
  const streak = activeGame?.themePersistenceStreak || 0;

  // Filter available rival parties (exclude player party and alliance allies)
  const playerAllianceMemberKeys = new Set(
    (playerAlliance?.members || []).map(m => (m.partyKey || '').toUpperCase())
  );
  if (playerPartyKey) playerAllianceMemberKeys.add(playerPartyKey.toUpperCase());

  const rivalParties = (activeGame?.partyStates || []).filter(p => {
    const pk = (p.partyKey || p.id || '').toUpperCase();
    return !playerAllianceMemberKeys.has(pk);
  });

  // Load Events & Themes from API
  const loadData = async () => {
    setLoading(true);
    try {
      const [evts, thms] = await Promise.all([
        fetchNationalEvents(gameId),
        fetchNationalThemes(gameId)
      ]);
      if (Array.isArray(evts)) setEvents(evts);
      if (thms && thms.themes) {
        setThemesData(thms);
        if (!selectedThemeKey && thms.themes.length > 0) {
          setSelectedThemeKey(thms.activeThemeKey || thms.themes[0].themeKey || thms.themes[0].id);
        }
        if (thms.targetPartyKey) {
          setSelectedTargetParty(thms.targetPartyKey);
          if (typeof window !== 'undefined') {
            try {
              localStorage.setItem(`national_target_party_${gameId}`, thms.targetPartyKey);
              localStorage.setItem('national_target_party_last', thms.targetPartyKey);
            } catch (_) {}
          }
        }
        if (thms.mediaSocialSpend) {
          setMediaAllocations(prev => ({
            social_ads: thms.mediaSocialSpend.social_ads ?? prev.social_ads ?? 0,
            influencer_collabs: thms.mediaSocialSpend.influencer_collabs ?? prev.influencer_collabs ?? 0,
            podcasts: thms.mediaSocialSpend.podcasts ?? prev.podcasts ?? 0,
            whatsapp_networks: thms.mediaSocialSpend.whatsapp_networks ?? prev.whatsapp_networks ?? 0
          }));
        }
        if (thms.mediaSocialCommitted !== undefined) {
          setMediaCommitted(thms.mediaSocialCommitted);
        }
      }
    } catch (err) {
      console.warn('Could not load events/themes:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData();
  }, [gameId, activeGame?.currentSeason]);

  // Sync state from activeGame prop
  useEffect(() => {
    if (activeGame?.targetPartyKey) {
      setSelectedTargetParty(activeGame.targetPartyKey);
      if (typeof window !== 'undefined') {
        try {
          localStorage.setItem(`national_target_party_${gameId}`, activeGame.targetPartyKey);
          localStorage.setItem('national_target_party_last', activeGame.targetPartyKey);
        } catch (_) {}
      }
    }
    if (activeGame?.mediaSocialSpend) {
      setMediaAllocations(prev => ({
        social_ads: activeGame.mediaSocialSpend.social_ads ?? prev.social_ads ?? 0,
        influencer_collabs: activeGame.mediaSocialSpend.influencer_collabs ?? prev.influencer_collabs ?? 0,
        podcasts: activeGame.mediaSocialSpend.podcasts ?? prev.podcasts ?? 0,
        whatsapp_networks: activeGame.mediaSocialSpend.whatsapp_networks ?? prev.whatsapp_networks ?? 0
      }));
    }
    if (activeGame?.mediaSocialCommitted !== undefined) {
      setMediaCommitted(activeGame.mediaSocialCommitted);
    }
  }, [activeGame, gameId]);

  // Remember last choice and make it chosen by default
  useEffect(() => {
    if (rivalParties.length > 0) {
      const stored = typeof window !== 'undefined'
        ? (localStorage.getItem(`national_target_party_${gameId}`) || localStorage.getItem('national_target_party_last'))
        : null;

      // 1. If activeGame has a valid target party, keep it
      if (activeGame?.targetPartyKey && rivalParties.some(p => (p.partyKey || p.id || '').toUpperCase() === activeGame.targetPartyKey.toUpperCase())) {
        if ((selectedTargetParty || '').toUpperCase() !== activeGame.targetPartyKey.toUpperCase()) {
          setSelectedTargetParty(activeGame.targetPartyKey);
        }
        return;
      }

      // 2. If currently selected target party is already a valid rival party, keep it
      if (selectedTargetParty && rivalParties.some(p => (p.partyKey || p.id || '').toUpperCase() === selectedTargetParty.toUpperCase())) {
        return;
      }

      // 3. If a remembered choice is in localStorage and matches a valid rival, pick it by default
      if (stored && rivalParties.some(p => (p.partyKey || p.id || '').toUpperCase() === stored.toUpperCase())) {
        const matched = rivalParties.find(p => (p.partyKey || p.id || '').toUpperCase() === stored.toUpperCase());
        const validKey = matched.partyKey || matched.id;
        setSelectedTargetParty(validKey);
        handleSelectTargetParty(validKey);
        return;
      }

      // 4. Default to top rival party by Lok Sabha seats
      const sorted = [...rivalParties].sort((a, b) => (b.seats || 0) - (a.seats || 0));
      const defaultKey = sorted[0].partyKey || sorted[0].id;
      setSelectedTargetParty(defaultKey);
      handleSelectTargetParty(defaultKey);
    }
  }, [rivalParties, activeGame?.targetPartyKey, gameId]);

  // Handle Event Response
  const handleSelectOption = async (eventId, optionId) => {
    if (!optionId || actionLoading) return;
    const existingOpt = (activeGame?.resolvedEventReactions || {})[eventId];
    if (existingOpt) {
      setError('Event decision has already been committed and is locked for this season.');
      return;
    }
    setActionLoading(true);
    setError(null);
    setSuccess(null);
    try {
      const updated = await respondToNationalEvent(gameId, { eventId, optionId });
      if (updated) {
        onGameUpdate(updated);
        if (onMarkCompleted) onMarkCompleted(true);
        setSuccess('Response registered! Decision locked for this season.');
        loadData();
      }
    } catch (err) {
      setError(err.message || 'Failed to register event response.');
    } finally {
      setActionLoading(false);
    }
  };

  // Handle Target Party Selection
  const handleSelectTargetParty = async (partyKey) => {
    if (currentThemeAction) {
      setError('Cannot change target party after a campaign theme mobilization has been committed for this season.');
      return;
    }
    setSelectedTargetParty(partyKey);
    if (typeof window !== 'undefined') {
      try {
        localStorage.setItem(`national_target_party_${gameId}`, partyKey);
        localStorage.setItem('national_target_party_last', partyKey);
      } catch (_) {}
    }
    try {
      const updated = await setNationalTargetParty(gameId, partyKey);
      if (updated) {
        onGameUpdate(updated);
      }
    } catch (err) {
      console.warn('Failed to persist target party selection:', err);
    }
  };

  // Handle Theme Action Selection
  const handleSelectThemeAction = async (themeKey, actionKey) => {
    if (actionLoading) return;
    if (currentThemeAction) {
      setError('Campaign theme mobilization is already committed and is locked for this season.');
      return;
    }
    setActionLoading(true);
    setError(null);
    setSuccess(null);
    try {
      const updated = await chooseNationalThemeAction(gameId, {
        themeKey,
        actionKey,
        targetPartyKey: selectedTargetParty
      });
      if (updated) {
        onGameUpdate(updated);
        if (onMarkCompleted) onMarkCompleted(true);
        setSuccess(`Mobilization declared on this theme against ${(selectedTargetParty || 'rivals').toUpperCase()} for the season. Decision locked.`);
        loadData();
      }
    } catch (err) {
      setError(err.message || 'Failed to set theme action.');
    } finally {
      setActionLoading(false);
    }
  };

  // Handle Media Social Slider Change
  const handleMediaSliderChange = (channelKey, val) => {
    if (mediaCommitted) return;
    const num = Math.max(0, Math.min(5.0, parseFloat(val) || 0));
    setMediaAllocations(prev => ({
      ...prev,
      [channelKey]: Math.round(num * 10) / 10
    }));
  };

  // Handle Commit Media Social Campaign
  const handleCommitMediaSocial = async () => {
    if (mediaLoading) return;
    setMediaLoading(true);
    setError(null);
    setSuccess(null);
    try {
      const updated = await allocateNationalMediaSocial(gameId, mediaAllocations, true);
      if (updated) {
        onGameUpdate(updated);
        setMediaCommitted(true);
        setSuccess('Digital Media & Social Campaign budget committed! Workers and momentum will be resolved upon season completion.');
        loadData();
      }
    } catch (err) {
      setError(err.message || 'Failed to commit social media allocations.');
    } finally {
      setMediaLoading(false);
    }
  };

  // Handle Cancel / Reset Media Social Campaign
  const handleCancelMediaSocial = async () => {
    if (mediaLoading) return;
    setMediaLoading(true);
    setError(null);
    setSuccess(null);
    try {
      const updated = await cancelNationalMediaSocial(gameId);
      if (updated) {
        onGameUpdate(updated);
        setMediaCommitted(false);
        setMediaAllocations({ social_ads: 0, influencer_collabs: 0, podcasts: 0, whatsapp_networks: 0 });
        setSuccess('Media allocations have been reset.');
        loadData();
      }
    } catch (err) {
      setError(err.message || 'Failed to reset media allocations.');
    } finally {
      setMediaLoading(false);
    }
  };

  // Media Live Calculations
  const totalMediaSpend = Math.round((
    (mediaAllocations.social_ads || 0) +
    (mediaAllocations.influencer_collabs || 0) +
    (mediaAllocations.podcasts || 0) +
    (mediaAllocations.whatsapp_networks || 0)
  ) * 10) / 10;

  let effectiveMediaSpend = 0.0;
  let hasDiminishingChannel = false;
  let maxChannelSpend = 0.0;
  let topChannelName = 'Social Ads';

  Object.entries(mediaAllocations).forEach(([chKey, val]) => {
    const sp = val || 0;
    if (sp > maxChannelSpend) {
      maxChannelSpend = sp;
      topChannelName = chKey.replace('_', ' ').toUpperCase();
    }
    if (sp <= 3.0) {
      effectiveMediaSpend += sp;
    } else {
      hasDiminishingChannel = true;
      effectiveMediaSpend += 3.0 + Math.pow(sp - 3.0, 0.6);
    }
  });
  effectiveMediaSpend = Math.round(effectiveMediaSpend * 10) / 10;

  const isExcessiveSpend = totalMediaSpend > 6.0;
  const isOverBudget = totalMediaSpend > playerFunds;

  // Real-time Viral Odds calculation
  let viralOdds = 0.18;
  if (maxChannelSpend >= 2.5) viralOdds += 0.07;
  if (events.length > 0 && events.every(e => (activeGame?.resolvedEventReactions || {})[e.id])) viralOdds += 0.10;
  if (currentThemeAction) viralOdds += 0.10;
  viralOdds = Math.min(0.45, Math.round(viralOdds * 100) / 100);

  const estimatedCadres = Math.round(effectiveMediaSpend * 4000);
  const estimatedVolunteers = Math.round(effectiveMediaSpend * 2200);
  const estimatedMorale = Math.min(8, Math.round(effectiveMediaSpend * 1.5));

  const selectedTheme = (themesData.themes || []).find(
    t => (t.themeKey || t.id) === selectedThemeKey
  ) || (themesData.themes || [])[0] || null;

  const targetedPartyObj = rivalParties.find(
    rp => (rp.partyKey || rp.id || '').toUpperCase() === (selectedTargetParty || '').toUpperCase()
  ) || null;

  const previousMediaReport = activeGame?.mediaSocialReport || themesData?.mediaSocialReport || null;
  const previousTargetReport = activeGame?.themeTargetReport || themesData?.themeTargetReport || null;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>



      {/* Notifications */}
      {error && (
        <div style={{ padding: '10px 14px', backgroundColor: 'rgba(239, 68, 68, 0.2)', border: '1px solid #ef4444', borderRadius: '8px', color: '#fca5a5', fontSize: '12px' }}>
          ⚠️ {error}
        </div>
      )}
      {success && (
        <div style={{ padding: '10px 14px', backgroundColor: 'rgba(16, 185, 129, 0.2)', border: '1px solid #10b981', borderRadius: '8px', color: '#6ee7b7', fontSize: '12px' }}>
          ✅ {success}
        </div>
      )}

      {/* ------------------------------------------------------------------ */}
      {/* 2. SECTION: NATIONAL EVENTS & CRISES                               */}
      {/* ------------------------------------------------------------------ */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
          <h3 style={{ margin: 0, fontSize: '16px', color: '#ffffff', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span>📰</span> Current Season Crises & National Events
          </h3>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <span style={{ fontSize: '11px', color: '#ec4899', fontWeight: 700 }}>
              {events.length} Active Event{events.length === 1 ? '' : 's'}
            </span>
            <button
              onClick={() => onMarkCompleted && onMarkCompleted(!isCompleted)}
              style={{
                padding: '4px 10px',
                borderRadius: '6px',
                border: isCompleted ? '1.5px solid #10b981' : '1px solid #64748b',
                backgroundColor: isCompleted ? 'rgba(16, 185, 129, 0.2)' : 'rgba(30, 41, 59, 0.6)',
                color: isCompleted ? '#34d399' : '#cbd5e1',
                fontSize: '9px',
                fontWeight: '800',
                cursor: 'pointer',
                display: 'inline-flex',
                alignItems: 'center',
                gap: '4px',
                transition: 'all 0.2s ease'
              }}
              title="Confirm that issues and events have been addressed for this season"
            >
              {isCompleted ? '✓ Issues & Events Reviewed' : 'Confirm Events Reviewed'}
            </button>
          </div>
        </div>

        {loading ? (
          <div style={{ textAlign: 'center', padding: '24px', color: '#94a3b8', fontSize: '12px' }}>
            Loading national developments...
          </div>
        ) : events.length === 0 ? (
          <div style={{ padding: '20px', textAlign: 'center', backgroundColor: '#1e293b', borderRadius: '10px', color: '#94a3b8', fontSize: '12px' }}>
            No major crises reported for this season.
          </div>
        ) : (
          events.map(evt => {
            const resolvedOptId = evt.selectedOptionId || (activeGame?.resolvedEventReactions || {})[evt.id] || null;
            const options = evt.options || [];

            return (
              <div 
                key={evt.id}
                style={{
                  background: 'linear-gradient(180deg, #1e293b 0%, #0f172a 100%)',
                  border: '1px solid rgba(236, 72, 153, 0.3)',
                  borderRadius: '12px',
                  padding: '18px',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '14px',
                  boxShadow: '0 8px 24px rgba(0,0,0,0.35)'
                }}
              >
                {/* Event Header */}
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '8px' }}>
                  <div style={{ display: 'flex', gap: '12px', alignItems: 'center' }}>
                    <span style={{ fontSize: '28px' }}>{evt.icon || '📢'}</span>
                    <div>
                      <div style={{ display: 'flex', gap: '6px', alignItems: 'center' }}>
                        <span style={{
                          fontSize: '9px',
                          fontWeight: 800,
                          padding: '2px 6px',
                          borderRadius: '4px',
                          backgroundColor: 'rgba(236, 72, 153, 0.2)',
                          color: '#f472b6',
                          border: '1px solid rgba(236, 72, 153, 0.4)'
                        }}>
                          {evt.type || 'POLITICAL_DEVELOPMENT'}
                        </span>
                        <span style={{ fontSize: '10px', color: '#94a3b8' }}>
                          Season {activeGame?.currentSeason || 1}
                        </span>
                      </div>
                      <h4 style={{ margin: '4px 0 0 0', fontSize: '16px', color: '#ffffff', fontWeight: 800 }}>
                        {evt.title}
                      </h4>
                    </div>
                  </div>

                  {resolvedOptId ? (
                    <span style={{
                      fontSize: '11px',
                      fontWeight: 800,
                      color: '#10b981',
                      backgroundColor: 'rgba(16, 185, 129, 0.15)',
                      padding: '4px 10px',
                      borderRadius: '6px',
                      border: '1px solid #10b981'
                    }}>
                      ✓ Response Committed
                    </span>
                  ) : (
                    <span style={{
                      fontSize: '11px',
                      fontWeight: 800,
                      color: '#f59e0b',
                      backgroundColor: 'rgba(245, 158, 11, 0.15)',
                      padding: '4px 10px',
                      borderRadius: '6px',
                      border: '1px solid #f59e0b'
                    }}>
                      ⏳ Response Awaited
                    </span>
                  )}
                </div>

                {/* Narrative / Contextual summary */}
                <p style={{ margin: 0, fontSize: '12px', color: '#cbd5e1', lineHeight: 1.5 }}>
                  {evt.narrative || evt.summary}
                </p>

                {/* 4 Reaction Options Grid */}
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))', gap: '10px' }}>
                  {options.map(opt => {
                    const optId = opt.optionId || opt.id;
                    const isSelected = Boolean(resolvedOptId && optId && resolvedOptId === optId);
                    const isLocked = Boolean(resolvedOptId);

                    return (
                      <div
                        key={optId || opt.label}
                        onClick={!isLocked ? () => handleSelectOption(evt.id, optId) : undefined}
                        style={{
                          backgroundColor: isSelected ? 'rgba(56, 189, 248, 0.18)' : 'rgba(15, 23, 42, 0.7)',
                          border: isSelected ? '2px solid #38bdf8' : '1px solid rgba(255,255,255,0.1)',
                          borderRadius: '8px',
                          padding: '14px',
                          cursor: isLocked ? (isSelected ? 'default' : 'not-allowed') : 'pointer',
                          opacity: isLocked && !isSelected ? 0.45 : 1,
                          display: 'flex',
                          flexDirection: 'column',
                          justifyContent: 'space-between',
                          gap: '10px',
                          transition: 'all 0.2s ease',
                          boxShadow: isSelected ? '0 0 16px rgba(56, 189, 248, 0.35)' : 'none'
                        }}
                      >
                        <div>
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '6px', gap: '6px' }}>
                            <span style={{ fontSize: '12.5px', fontWeight: 800, color: isSelected ? '#38bdf8' : '#ffffff', lineHeight: 1.3 }}>
                              {opt.label}
                            </span>
                            {isSelected && (
                              <span style={{
                                fontSize: '9px',
                                color: '#ffffff',
                                backgroundColor: '#0284c7',
                                padding: '2px 6px',
                                borderRadius: '4px',
                                fontWeight: 900,
                                whiteSpace: 'nowrap'
                              }}>
                                COMMITTED 🔒
                              </span>
                            )}
                          </div>
                          <p style={{ margin: 0, fontSize: '11px', color: '#94a3b8', lineHeight: 1.45 }}>
                            {opt.description}
                          </p>
                        </div>

                        <button
                          type="button"
                          disabled={actionLoading || isLocked}
                          style={{
                            padding: '6px 12px',
                            borderRadius: '6px',
                            border: 'none',
                            cursor: isLocked ? (isSelected ? 'default' : 'not-allowed') : 'pointer',
                            fontWeight: 800,
                            fontSize: '11px',
                            backgroundColor: isSelected ? '#0284c7' : isLocked ? '#334155' : 'rgba(255,255,255,0.08)',
                            color: isSelected ? '#ffffff' : isLocked ? '#64748b' : '#cbd5e1',
                            transition: 'all 0.2s ease',
                            alignSelf: 'flex-start'
                          }}
                        >
                          {isSelected ? 'Committed 🔒' : isLocked ? 'Locked for Season' : 'Select'}
                        </button>
                      </div>
                    );
                  })}
                </div>
              </div>
            );
          })
        )}
      </div>

      {/* ------------------------------------------------------------------ */}
      {/* 3. SECTION: CAMPAIGN THEMES & AGITATION ENGINE                     */}
      {/* ------------------------------------------------------------------ */}
      <div style={{
        background: 'linear-gradient(180deg, #1e293b 0%, #0f172a 100%)',
        border: '1px solid rgba(56, 189, 248, 0.3)',
        borderRadius: '12px',
        padding: '20px',
        display: 'flex',
        flexDirection: 'column',
        gap: '16px',
        boxShadow: '0 8px 24px rgba(0,0,0,0.35)'
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
          <div>
            <h3 style={{ margin: 0, fontSize: '16px', color: '#ffffff', display: 'flex', alignItems: 'center', gap: '8px' }}>
              <span>{isPlayerInPower ? '🏛️' : '🔥'}</span> {isPlayerInPower ? 'Governance Blitz & Development Showcase' : 'Campaign Themes & Agitation Tactics'}
            </h3>
            <span style={{ fontSize: '11px', color: isPlayerInPower ? '#67e8f9' : '#fca5a5' }}>
              {isPlayerInPower 
                ? 'Ruling Coalition: Direct development delivery, mega-infrastructures, and DBT disbursals to consolidate federal dominance.'
                : 'Opposition Front: Spearhead mass agitations, strikes, and expose regime corruption to erode ruling alliance stability.'}
            </span>
          </div>

          {/* Clean Streak Badge */}
          <div 
            title="Persisting on the same campaign theme builds compounding momentum. You can switch anytime without penalties."
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              backgroundColor: streak >= 3 ? 'rgba(245, 158, 11, 0.2)' : 'rgba(255,255,255,0.06)',
              border: streak >= 3 ? '1px solid #f59e0b' : '1px solid rgba(255,255,255,0.15)',
              padding: '6px 12px',
              borderRadius: '8px',
              cursor: 'help'
            }}
          >
            <span style={{ fontSize: '14px' }}>⚡</span>
            <div style={{ fontSize: '11.5px', fontWeight: 800, color: streak >= 3 ? '#fbbf24' : '#ffffff' }}>
              Conviction Streak: {streak} Turn{streak === 1 ? '' : 's'}
              {streak >= 5 ? ' (Breakthrough)' : streak >= 3 ? ' (Compounding)' : ''}
            </div>
            <span style={{ fontSize: '10px', color: '#94a3b8' }}>ℹ️</span>
          </div>
        </div>

        {/* Previous Turn Theme Target Attack Report if available */}
        {previousTargetReport && (
          <div style={{
            backgroundColor: 'rgba(239, 68, 68, 0.12)',
            border: '1px solid rgba(239, 68, 68, 0.3)',
            borderRadius: '8px',
            padding: '10px 14px',
            fontSize: '11px',
            color: '#fca5a5',
            display: 'flex',
            alignItems: 'center',
            gap: '8px'
          }}>
            <span style={{ fontSize: '14px' }}>💥</span>
            <span><strong>Previous Offensive Impact:</strong> {previousTargetReport}</span>
          </div>
        )}

        {/* TARGET RIVAL PARTY SELECTOR (Section Level) - Dropdown with Memory */}
        <div style={{
          backgroundColor: 'rgba(15, 23, 42, 0.75)',
          border: '1px solid rgba(244, 63, 94, 0.35)',
          borderRadius: '10px',
          padding: '14px 16px',
          display: 'flex',
          flexDirection: 'column',
          gap: '12px'
        }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <span style={{ fontSize: '16px' }}>🎯</span>
              <label htmlFor="target-party-select" style={{ fontSize: '13px', fontWeight: 800, color: '#f43f5e', cursor: 'pointer' }}>
                Primary Target Rival Party for Campaign Offensive
              </label>
            </div>
            <span style={{ fontSize: '10.5px', color: '#94a3b8' }}>
              Offensives inflict morale decay, cadre desertions, and vote split erosion on the selected rival.
            </span>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '14px', flexWrap: 'wrap' }}>
            <div style={{ flex: '1 1 320px' }}>
              <select
                id="target-party-select"
                value={selectedTargetParty ? selectedTargetParty.toUpperCase() : ''}
                disabled={Boolean(currentThemeAction)}
                onChange={(e) => handleSelectTargetParty(e.target.value)}
                style={{
                  width: '100%',
                  padding: '10px 14px',
                  borderRadius: '8px',
                  backgroundColor: 'rgba(30, 41, 59, 0.95)',
                  border: '1.5px solid #f43f5e',
                  color: '#ffffff',
                  fontSize: '13px',
                  fontWeight: 700,
                  cursor: currentThemeAction ? 'not-allowed' : 'pointer',
                  outline: 'none',
                  boxShadow: '0 0 10px rgba(244, 63, 94, 0.25)',
                  opacity: currentThemeAction ? 0.6 : 1
                }}
              >
                {rivalParties.map(rp => {
                  const rKey = (rp.partyKey || rp.id || '').toUpperCase();
                  return (
                    <option key={rKey} value={rKey} style={{ backgroundColor: '#0f172a', color: '#ffffff' }}>
                      🎯 {rp.partyName || rKey} ({rKey}) — {rp.seats || 0} Seats | {rp.morale || 50}% Morale
                    </option>
                  );
                })}
              </select>
            </div>

            {/* Targeted Party Summary Card */}
            {targetedPartyObj && (
              <div style={{
                flex: '1 1 240px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                backgroundColor: 'rgba(244, 63, 94, 0.12)',
                border: '1px solid rgba(244, 63, 94, 0.3)',
                borderRadius: '8px',
                padding: '8px 14px',
                gap: '10px'
              }}>
                <div>
                  <div style={{ fontSize: '11.5px', fontWeight: 800, color: '#fda4af' }}>
                    Active Target: {targetedPartyObj.partyName || targetedPartyObj.partyKey} ({targetedPartyObj.partyKey})
                  </div>
                  <div style={{ fontSize: '10px', color: '#cbd5e1', marginTop: '2px' }}>
                    Projected Seats: <strong style={{ color: '#ffffff' }}>{targetedPartyObj.seats || 0}</strong> | Morale: <strong style={{ color: '#ffffff' }}>{targetedPartyObj.morale || 50}%</strong>
                  </div>
                </div>
                <span style={{
                  fontSize: '9px',
                  fontWeight: 900,
                  padding: '3px 8px',
                  borderRadius: '4px',
                  backgroundColor: '#f43f5e',
                  color: '#ffffff',
                  whiteSpace: 'nowrap'
                }}>
                  {currentThemeAction ? 'LOCKED 🔒' : 'SELECTED 🎯'}
                </span>
              </div>
            )}
          </div>
        </div>

        {/* Theme Selectors */}
        <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
          {(themesData.themes || []).map(theme => {
            const isSelected = selectedThemeKey === (theme.themeKey || theme.id);
            const isCurrentActive = currentThemeKey === (theme.themeKey || theme.id);

            return (
              <button
                key={theme.themeKey || theme.id}
                onClick={() => setSelectedThemeKey(theme.themeKey || theme.id)}
                style={{
                  flex: '1 1 200px',
                  padding: '12px 14px',
                  borderRadius: '10px',
                  backgroundColor: isSelected ? 'rgba(56, 189, 248, 0.2)' : 'rgba(15, 23, 42, 0.6)',
                  border: isSelected ? '2px solid #38bdf8' : isCurrentActive ? '1px solid #10b981' : '1px solid rgba(255,255,255,0.1)',
                  color: '#ffffff',
                  cursor: 'pointer',
                  textAlign: 'left',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '10px',
                  transition: 'all 0.2s ease'
                }}
              >
                <span style={{ fontSize: '24px' }}>{theme.icon || '🔥'}</span>
                <div>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                    <span style={{ fontSize: '13px', fontWeight: 800 }}>{theme.title}</span>
                    {isCurrentActive && (
                      <span style={{ fontSize: '8.5px', padding: '1px 5px', borderRadius: '4px', backgroundColor: '#10b981', color: '#fff', fontWeight: 900 }}>
                        ACTIVE ✓
                      </span>
                    )}
                  </div>
                  <div style={{ fontSize: '10px', color: '#94a3b8' }}>
                    {theme.themeType === 'GOVERNANCE' ? '🏛️ Governance Deck' : '🔥 Agitation Deck'}
                  </div>
                </div>
              </button>
            );
          })}
        </div>

        {/* Selected Theme Details & Tactical Actions */}
        {selectedTheme && (
          <div style={{
            backgroundColor: 'rgba(15, 23, 42, 0.8)',
            border: '1px solid rgba(255,255,255,0.08)',
            borderRadius: '10px',
            padding: '16px',
            display: 'flex',
            flexDirection: 'column',
            gap: '14px'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
              <div>
                <h4 style={{ margin: 0, fontSize: '14px', color: '#38bdf8', fontWeight: 800 }}>
                  {selectedTheme.icon} {selectedTheme.title}
                </h4>
                <p style={{ margin: '4px 0 0 0', fontSize: '11px', color: '#cbd5e1' }}>
                  {selectedTheme.description}
                </p>
              </div>
              <span style={{
                fontSize: '10px',
                padding: '3px 8px',
                borderRadius: '6px',
                backgroundColor: selectedTheme.themeType === 'GOVERNANCE' ? 'rgba(6, 182, 212, 0.2)' : 'rgba(239, 68, 68, 0.2)',
                color: selectedTheme.themeType === 'GOVERNANCE' ? '#67e8f9' : '#fca5a5',
                border: `1px solid ${selectedTheme.themeType === 'GOVERNANCE' ? '#06b6d4' : '#ef4444'}`,
                fontWeight: 700
              }}>
                {selectedTheme.themeType === 'GOVERNANCE' ? 'GOVERNANCE BLITZ' : 'AGITATION CAMPAIGN'}
              </span>
            </div>

            {/* Tactical Actions Grid */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '10px' }}>
              {selectedTheme.actionEffects && Object.entries(selectedTheme.actionEffects).map(([actKey, actData]) => {
                const isCommitted = currentThemeKey === (selectedTheme.themeKey || selectedTheme.id) && currentThemeAction === actKey;
                const isThemeLocked = Boolean(currentThemeAction);

                return (
                  <div
                    key={actKey}
                    style={{
                      backgroundColor: isCommitted ? 'rgba(16, 185, 129, 0.15)' : 'rgba(30, 41, 59, 0.6)',
                      border: isCommitted ? '2px solid #10b981' : '1px solid rgba(255,255,255,0.1)',
                      borderRadius: '8px',
                      padding: '12px',
                      display: 'flex',
                      flexDirection: 'column',
                      justifyContent: 'space-between',
                      gap: '10px',
                      opacity: isThemeLocked && !isCommitted ? 0.45 : 1
                    }}
                  >
                    <div>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <span style={{ fontSize: '12px', fontWeight: 800, color: isCommitted ? '#34d399' : '#ffffff' }}>
                          {actData.label || actKey}
                        </span>
                        {isCommitted && (
                          <span style={{ fontSize: '9px', fontWeight: 900, color: '#10b981' }}>COMMITTED 🔒</span>
                        )}
                      </div>
                      <p style={{ margin: '4px 0 0 0', fontSize: '10.5px', color: '#94a3b8', lineHeight: 1.4 }}>
                        {actData.description || 'Mobilize party apparatus for this operation.'}
                      </p>
                    </div>

                    <button
                      onClick={() => !isThemeLocked && handleSelectThemeAction(selectedTheme.themeKey || selectedTheme.id, actKey)}
                      disabled={actionLoading || isThemeLocked}
                      style={{
                        padding: '7px 12px',
                        borderRadius: '6px',
                        border: 'none',
                        cursor: isThemeLocked ? (isCommitted ? 'default' : 'not-allowed') : 'pointer',
                        fontWeight: 800,
                        fontSize: '11px',
                        backgroundColor: isCommitted ? '#059669' : isThemeLocked ? '#334155' : '#0284c7',
                        color: isThemeLocked && !isCommitted ? '#94a3b8' : '#ffffff',
                        transition: 'all 0.2s ease',
                        width: '100%'
                      }}
                    >
                      {isCommitted ? 'Committed 🔒' : isThemeLocked ? 'Locked for Season' : `Mobilize against ${(selectedTargetParty || 'Rival').toUpperCase()}`}
                    </button>
                  </div>
                );
              })}
            </div>
          </div>
        )}
      </div>

      {/* ------------------------------------------------------------------ */}
      {/* 4. SECTION: DIGITAL MEDIA & SOCIAL CAMPAIGN BLITZ                   */}
      {/* ------------------------------------------------------------------ */}
      <div style={{
        background: 'linear-gradient(180deg, #1e293b 0%, #0f172a 100%)',
        border: '1px solid rgba(168, 85, 247, 0.35)',
        borderRadius: '12px',
        padding: '20px',
        display: 'flex',
        flexDirection: 'column',
        gap: '18px',
        boxShadow: '0 8px 24px rgba(0,0,0,0.35)'
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '10px' }}>
          <div>
            <h3 style={{ margin: 0, fontSize: '16px', color: '#ffffff', display: 'flex', alignItems: 'center', gap: '8px' }}>
              <span>📱</span> Digital Media & Social Campaign Blitz
            </h3>
            <p style={{ margin: '4px 0 0 0', fontSize: '11px', color: '#cbd5e1' }}>
              Allocate treasury funds to digital channels, podcasts, and influencer networks. Drives cadre recruitment and potential viral breakthroughs.
            </p>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span style={{
              fontSize: '11px',
              padding: '4px 10px',
              borderRadius: '6px',
              backgroundColor: 'rgba(168, 85, 247, 0.15)',
              border: '1px solid #a855f7',
              color: '#c084fc',
              fontWeight: 800
            }}>
              Treasury Reserves: ₹{playerFunds.toFixed(1)} Cr
            </span>
            {mediaCommitted && (
              <span style={{
                fontSize: '11px',
                padding: '4px 10px',
                borderRadius: '6px',
                backgroundColor: 'rgba(16, 185, 129, 0.2)',
                border: '1px solid #10b981',
                color: '#34d399',
                fontWeight: 900
              }}>
                COMMITTED FOR SEASON 🔒
              </span>
            )}
          </div>
        </div>

        {/* Previous Season Media Debrief Banner if available */}
        {previousMediaReport && previousMediaReport.summary && (
          <div style={{
            backgroundColor: previousMediaReport.viralTriggered ? 'rgba(245, 158, 11, 0.15)' : 'rgba(30, 41, 59, 0.7)',
            border: previousMediaReport.viralTriggered ? '1px solid #f59e0b' : '1px solid rgba(255,255,255,0.1)',
            borderRadius: '10px',
            padding: '12px 16px',
            display: 'flex',
            flexDirection: 'column',
            gap: '6px'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <span style={{ fontSize: '12px', fontWeight: 900, color: previousMediaReport.viralTriggered ? '#fbbf24' : '#38bdf8' }}>
                {previousMediaReport.viralTriggered ? `🔥 VIRAL BREAKTHROUGH ON ${previousMediaReport.viralChannel || 'MEDIA'}!` : '📡 Previous Season Media Debrief'}
              </span>
              <div style={{ display: 'flex', gap: '6px' }}>
                <span style={{ fontSize: '9px', padding: '2px 6px', borderRadius: '4px', backgroundColor: 'rgba(16, 185, 129, 0.2)', color: '#34d399', fontWeight: 800 }}>
                  +{previousMediaReport.workersRecruited || 0} Cadres
                </span>
                <span style={{ fontSize: '9px', padding: '2px 6px', borderRadius: '4px', backgroundColor: 'rgba(56, 189, 248, 0.2)', color: '#38bdf8', fontWeight: 800 }}>
                  +{previousMediaReport.volunteersGained || 0} Volunteers
                </span>
                <span style={{ fontSize: '9px', padding: '2px 6px', borderRadius: '4px', backgroundColor: 'rgba(236, 72, 153, 0.2)', color: '#f472b6', fontWeight: 800 }}>
                  +{previousMediaReport.moraleBonus || 0}% Morale
                </span>
              </div>
            </div>
            <div style={{ fontSize: '11px', color: '#e2e8f0', lineHeight: 1.4 }}>
              {previousMediaReport.summary}
            </div>
          </div>
        )}

        {/* 4 Media Channels Sliders Grid */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '14px' }}>
          {[
            {
              key: 'social_ads',
              name: 'Social Ad Blitz (FB & Instagram)',
              icon: '📱',
              desc: 'Micro-targeted targeted campaign ads across Facebook and Instagram feeds.',
              color: '#3b82f6'
            },
            {
              key: 'influencer_collabs',
              name: 'Influencer & YouTuber Collabs',
              icon: '🎙️',
              desc: 'Sponsored content and regional creator videos. Highest viral ceiling.',
              color: '#ec4899'
            },
            {
              key: 'podcasts',
              name: 'Long-Form Podcasts & Video Shows',
              icon: '🎧',
              desc: 'In-depth policy discussions building intellectual narrative dominance.',
              color: '#a855f7'
            },
            {
              key: 'whatsapp_networks',
              name: 'Grassroots WhatsApp & Messaging',
              icon: '💬',
              desc: 'Hyper-local constituency broadcast groups for cadre activation.',
              color: '#10b981'
            }
          ].map(ch => {
            const val = mediaAllocations[ch.key] || 0;
            const isDiminishing = val > 3.0;

            return (
              <div
                key={ch.key}
                style={{
                  backgroundColor: 'rgba(15, 23, 42, 0.75)',
                  border: isDiminishing ? '1px solid #f59e0b' : '1px solid rgba(255,255,255,0.08)',
                  borderRadius: '10px',
                  padding: '14px',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '10px'
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <span style={{ fontSize: '18px' }}>{ch.icon}</span>
                    <span style={{ fontSize: '12px', fontWeight: 800, color: '#ffffff' }}>{ch.name}</span>
                  </div>
                  <span style={{
                    fontSize: '13px',
                    fontWeight: 900,
                    color: ch.color,
                    backgroundColor: 'rgba(0,0,0,0.3)',
                    padding: '2px 8px',
                    borderRadius: '6px'
                  }}>
                    ₹{val.toFixed(1)} Cr
                  </span>
                </div>

                <p className="nwr-hide-mobile" style={{ margin: 0, fontSize: '10.5px', color: '#94a3b8', lineHeight: 1.4 }}>
                  {ch.desc}
                </p>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                  <input
                    type="range"
                    min="0"
                    max="5.0"
                    step="0.25"
                    value={val}
                    disabled={mediaCommitted}
                    onChange={(e) => handleMediaSliderChange(ch.key, e.target.value)}
                    style={{
                      width: '100%',
                      cursor: mediaCommitted ? 'not-allowed' : 'pointer',
                      accentColor: ch.color
                    }}
                  />
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '9px', color: '#64748b' }}>
                    <span>₹0.0 Cr</span>
                    <span style={{ color: isDiminishing ? '#f59e0b' : '#64748b' }}>
                      {isDiminishing ? '⚠️ Saturation (Diminishing)' : 'Sweet Spot: ≤ ₹3.0 Cr'}
                    </span>
                    <span>₹5.0 Cr</span>
                  </div>
                </div>
              </div>
            );
          })}
        </div>

        {/* Live Projections & Evaluation Panel */}
        <div style={{
          backgroundColor: 'rgba(15, 23, 42, 0.9)',
          border: '1px solid rgba(56, 189, 248, 0.25)',
          borderRadius: '10px',
          padding: '16px',
          display: 'flex',
          flexDirection: 'column',
          gap: '12px'
        }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
            <span style={{ fontSize: '12px', fontWeight: 800, color: '#38bdf8' }}>
              📊 Campaign Efficiency & Live Projection
            </span>
            <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
              <span style={{ fontSize: '11px', color: '#cbd5e1' }}>
                Total Allocated: <strong style={{ color: isOverBudget ? '#ef4444' : '#ffffff' }}>₹{totalMediaSpend.toFixed(1)} Cr</strong>
              </span>
              <span style={{ fontSize: '11px', color: '#94a3b8' }}>
                (Effective Impact: <strong style={{ color: '#38bdf8' }}>₹{effectiveMediaSpend.toFixed(1)} Cr</strong>)
              </span>
            </div>
          </div>

          {/* Metric Badges Grid */}
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(140px, 1fr))', gap: '10px' }}>
            <div style={{ backgroundColor: 'rgba(30, 41, 59, 0.7)', padding: '10px', borderRadius: '8px', textAlign: 'center' }}>
              <div style={{ fontSize: '10px', color: '#94a3b8' }}>Estimated Cadres</div>
              <div style={{ fontSize: '15px', fontWeight: 900, color: '#34d399' }}>
                +{estimatedCadres.toLocaleString()}
              </div>
            </div>
            <div style={{ backgroundColor: 'rgba(30, 41, 59, 0.7)', padding: '10px', borderRadius: '8px', textAlign: 'center' }}>
              <div style={{ fontSize: '10px', color: '#94a3b8' }}>Estimated Volunteers</div>
              <div style={{ fontSize: '15px', fontWeight: 900, color: '#38bdf8' }}>
                +{estimatedVolunteers.toLocaleString()}
              </div>
            </div>
            <div style={{ backgroundColor: 'rgba(30, 41, 59, 0.7)', padding: '10px', borderRadius: '8px', textAlign: 'center' }}>
              <div style={{ fontSize: '10px', color: '#94a3b8' }}>Cadre Morale</div>
              <div style={{ fontSize: '15px', fontWeight: 900, color: '#ec4899' }}>
                +{estimatedMorale}%
              </div>
            </div>
            <div style={{ backgroundColor: 'rgba(30, 41, 59, 0.7)', padding: '10px', borderRadius: '8px', textAlign: 'center' }}>
              <div style={{ fontSize: '10px', color: '#94a3b8' }}>Viral Breakthrough Chance</div>
              <div style={{ fontSize: '15px', fontWeight: 900, color: viralOdds >= 0.35 ? '#fbbf24' : '#cbd5e1' }}>
                {Math.round(viralOdds * 100)}%
              </div>
            </div>
          </div>

          {/* Viral Multiplier Factors */}
          <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', alignItems: 'center', fontSize: '10px' }}>
            <span style={{ color: '#94a3b8' }}>Viral Synergies:</span>
            <span style={{ padding: '2px 6px', borderRadius: '4px', backgroundColor: maxChannelSpend >= 2.5 ? 'rgba(16, 185, 129, 0.2)' : 'rgba(255,255,255,0.06)', color: maxChannelSpend >= 2.5 ? '#34d399' : '#64748b' }}>
              {maxChannelSpend >= 2.5 ? '✓' : '○'} High Channel Depth (+7%)
            </span>
            <span style={{ padding: '2px 6px', borderRadius: '4px', backgroundColor: events.length > 0 && events.every(e => (activeGame?.resolvedEventReactions || {})[e.id]) ? 'rgba(16, 185, 129, 0.2)' : 'rgba(255,255,255,0.06)', color: events.length > 0 && events.every(e => (activeGame?.resolvedEventReactions || {})[e.id]) ? '#34d399' : '#64748b' }}>
              {events.length > 0 && events.every(e => (activeGame?.resolvedEventReactions || {})[e.id]) ? '✓' : '○'} Active Crises Responded (+10%)
            </span>
            <span style={{ padding: '2px 6px', borderRadius: '4px', backgroundColor: currentThemeAction ? 'rgba(16, 185, 129, 0.2)' : 'rgba(255,255,255,0.06)', color: currentThemeAction ? '#34d399' : '#64748b' }}>
              {currentThemeAction ? '✓' : '○'} Campaign Theme Mobilized (+10%)
            </span>
          </div>

          {/* Warning Banners */}
          {hasDiminishingChannel && (
            <div style={{ backgroundColor: 'rgba(245, 158, 11, 0.15)', border: '1px solid #f59e0b', borderRadius: '6px', padding: '8px 12px', fontSize: '10.5px', color: '#fbbf24' }}>
              ⚠️ <strong>Diminishing Returns:</strong> Spend exceeding ₹3.0 Cr on any single channel experiences reduced conversion due to ad fatigue and audience saturation.
            </div>
          )}

          {isExcessiveSpend && (
            <div style={{ backgroundColor: 'rgba(239, 68, 68, 0.2)', border: '1px solid #ef4444', borderRadius: '6px', padding: '8px 12px', fontSize: '10.5px', color: '#fca5a5' }}>
              🚨 <strong>Excessive Spend Warning:</strong> Allocating over ₹6.0 Cr total triggers investigative media scrutiny and +1 Scrutiny Heat!
            </div>
          )}

          {isOverBudget && (
            <div style={{ backgroundColor: 'rgba(239, 68, 68, 0.25)', border: '1px solid #ef4444', borderRadius: '6px', padding: '8px 12px', fontSize: '10.5px', color: '#fca5a5' }}>
              ❌ <strong>Insufficient Funds:</strong> Total allocation (₹{totalMediaSpend.toFixed(1)} Cr) exceeds current treasury reserves (₹{playerFunds.toFixed(1)} Cr). Please lower your sliders.
            </div>
          )}

          {/* Action Commit / Cancel Buttons */}
          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '6px' }}>
            {mediaCommitted ? (
              <button
                type="button"
                onClick={handleCancelMediaSocial}
                disabled={mediaLoading}
                style={{
                  padding: '8px 16px',
                  borderRadius: '6px',
                  border: '1px solid #ef4444',
                  backgroundColor: 'rgba(239, 68, 68, 0.15)',
                  color: '#fca5a5',
                  fontSize: '11px',
                  fontWeight: 800,
                  cursor: 'pointer'
                }}
              >
                {mediaLoading ? 'Resetting...' : 'Modify / Reset Media Allocation'}
              </button>
            ) : (
              <button
                type="button"
                onClick={handleCommitMediaSocial}
                disabled={mediaLoading || totalMediaSpend === 0 || isOverBudget}
                style={{
                  padding: '9px 20px',
                  borderRadius: '6px',
                  border: 'none',
                  backgroundColor: totalMediaSpend === 0 || isOverBudget ? '#334155' : '#a855f7',
                  color: totalMediaSpend === 0 || isOverBudget ? '#94a3b8' : '#ffffff',
                  fontSize: '12px',
                  fontWeight: 900,
                  cursor: totalMediaSpend === 0 || isOverBudget ? 'not-allowed' : 'pointer',
                  boxShadow: totalMediaSpend > 0 && !isOverBudget ? '0 0 16px rgba(168, 85, 247, 0.4)' : 'none',
                  transition: 'all 0.2s'
                }}
              >
                {mediaLoading ? 'Committing...' : `Commit Social Blitz (₹${totalMediaSpend.toFixed(1)} Cr) 🔒`}
              </button>
            )}
          </div>
        </div>
      </div>

    </div>
  );
}
