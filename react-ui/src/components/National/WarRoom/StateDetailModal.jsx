import React, { useState, useEffect, useMemo } from 'react';
import {
  fetchNationalStateDetail,
  reactNationalStateNews,
  actOnNationalStateIssue,
  allocateNationalStateResources,
  executeNationalStateCampaign,
  fetchStateInfrastructureCatalog,
  buildStateInfrastructure,
  allocateRegionalResources,
  allocateBatchRegionalResources,
  completeNationalState
} from '../../../api/apiClient';

export default function StateDetailModal({ stateSummary, activeGame, onClose, onGameUpdate }) {
  const [subTab, setSubTab] = useState('news'); // 'news' | 'issues' | 'management' | 'polling'
  const [stateDetail, setStateDetail] = useState(null);
  const [loading, setLoading] = useState(true);
  const [actionLoading, setActionLoading] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  // Resource allocation inputs (Top-up transfer from National HQ)
  const [transferFunds, setTransferFunds] = useState(1.0);
  const [transferWorkers, setTransferWorkers] = useState(2000);
  const [transferVolunteers, setTransferVolunteers] = useState(1000);

  // Regional management state
  const [infraCatalog, setInfraCatalog] = useState([]);
  const [buildingModalRegion, setBuildingModalRegion] = useState(null); // regionId or 'STATE'
  const [buildCategoryFilter, setBuildCategoryFilter] = useState('ALL'); // 'ALL' | 'HQ' | 'BUILDING' | 'WING'
  const [regionalAllocDrafts, setRegionalAllocDrafts] = useState({});
  const [selectedRegionId, setSelectedRegionId] = useState(null);
  const [viewAllRegions, setViewAllRegions] = useState(false);

  // Selected issue for issues tab
  const [selectedIssueId, setSelectedIssueId] = useState(null);

  const gameId = activeGame?.id || activeGame?._id || activeGame?.userId || 'local';
  const stateCode = stateSummary?.stateCode;

  const loadDetail = async () => {
    if (!stateCode) return;
    setLoading(true);
    setError(null);
    try {
      const data = await fetchNationalStateDetail(gameId, stateCode);
      if (data) {
        setStateDetail(data);
        if (data.issues && data.issues.length > 0 && !selectedIssueId) {
          setSelectedIssueId(data.state?.activeIssueId || data.issues[0].id);
        }
        if (data.state?.regions) {
          const drafts = {};
          const regKeys = Object.keys(data.state.regions);
          const totalExistingWorkers = Object.values(data.state.regions).reduce((acc, r) => acc + (r.allocatedWorkers || 0), 0);
          const totalExistingVols = Object.values(data.state.regions).reduce((acc, r) => acc + (r.allocatedVolunteers || 0), 0);
          const stWorkers = data.state.stateWorkers || 0;
          const stVols = data.state.stateVolunteers || 0;

          // If no workers or volunteers were allocated yet across regions, default distribute equally
          const shouldDefaultEqualWorkers = totalExistingWorkers === 0 && stWorkers > 0 && regKeys.length > 0;
          const shouldDefaultEqualVols = totalExistingVols === 0 && stVols > 0 && regKeys.length > 0;

          regKeys.forEach((rId) => {
            const rState = data.state.regions[rId];
            const defWorkers = shouldDefaultEqualWorkers ? Math.floor(stWorkers / regKeys.length) : (rState.allocatedWorkers || 0);
            const defVols = shouldDefaultEqualVols ? Math.floor(stVols / regKeys.length) : (rState.allocatedVolunteers || 0);
            drafts[rId] = {
              funds: rState.allocatedFunds !== undefined ? rState.allocatedFunds : 0,
              workers: defWorkers,
              volunteers: defVols
            };
          });
          setRegionalAllocDrafts(drafts);
          if (regKeys.length > 0) {
            setSelectedRegionId(prev => (prev && regKeys.includes(prev)) ? prev : regKeys[0]);
          }
        }
      }

      try {
        const cat = await fetchStateInfrastructureCatalog(gameId);
        if (Array.isArray(cat)) {
          setInfraCatalog(cat);
        }
      } catch (catErr) {
        console.warn('Could not load infrastructure catalog', catErr);
      }
    } catch (err) {
      setError(err.message || 'Failed to load state details.');
    } finally {
      setLoading(false);
    }
  };

  const handleBuildInfra = async (infraKey, regionId) => {
    if (actionLoading) return;
    setActionLoading(true);
    setError(null);
    setSuccess(null);
    try {
      const updated = await buildStateInfrastructure(gameId, stateCode, { infraKey, regionId });
      if (updated) {
        if (onGameUpdate) onGameUpdate(updated);
        setSuccess('Facility/Wing constructed successfully!');
        setBuildingModalRegion(null);
        await loadDetail();
      }
    } catch (err) {
      setError(err.message || 'Failed to construct facility.');
    } finally {
      setActionLoading(false);
    }
  };

  const handleDistributeEvenly = () => {
    if (!stateObj?.regions) return;
    const regKeys = Object.keys(stateObj.regions);
    if (regKeys.length === 0) return;
    const totalWorkers = stateObj.stateWorkers || 0;
    const totalVols = stateObj.stateVolunteers || 0;
    const equalWorkers = Math.floor(totalWorkers / regKeys.length);
    const equalVols = Math.floor(totalVols / regKeys.length);

    const newDrafts = {};
    regKeys.forEach((rId) => {
      newDrafts[rId] = {
        funds: regionalAllocDrafts[rId]?.funds || 0,
        workers: equalWorkers,
        volunteers: equalVols
      };
    });
    setRegionalAllocDrafts(newDrafts);
    setSuccess('Cadres and volunteers distributed equally across all 5 regions! Click "Save & Deploy" to commit.');
  };

  const handleSaveAllRegionalAllocations = async () => {
    if (actionLoading) return;
    setActionLoading(true);
    setError(null);
    setSuccess(null);
    try {
      const updated = await allocateBatchRegionalResources(gameId, stateCode, {
        allocations: regionalAllocDrafts
      });
      if (updated) {
        if (onGameUpdate) onGameUpdate(updated);
        setSuccess('Regional deployments successfully committed across all 5 regions!');
        await loadDetail();
      }
    } catch (err) {
      setError(err.message || 'Failed to deploy regional resources.');
    } finally {
      setActionLoading(false);
    }
  };

  const handleDoneOrSave = async () => {
    if (actionLoading) return;
    setActionLoading(true);
    setError(null);
    try {
      if (regionalAllocDrafts && Object.keys(regionalAllocDrafts).length > 0) {
        await allocateBatchRegionalResources(gameId, stateCode, {
          allocations: regionalAllocDrafts
        });
      }
      const updatedGame = await completeNationalState(gameId, stateCode);
      if (updatedGame && onGameUpdate) {
        onGameUpdate(updatedGame);
      }
      setSuccess('State directives & regional deployments marked as Done!');
      setTimeout(() => {
        onClose();
      }, 300);
    } catch (err) {
      setError(err.message || 'Failed to save state operations.');
      setActionLoading(false);
    }
  };

  const calcMomentum = (w, v, reg) => {
    let m = 0.0;
    m += ((parseInt(w) || 0) / 2000.0) * 0.25;
    m += ((parseInt(v) || 0) / 5000.0) * 0.2;
    if (stateObj?.buildings?.state_party_hq) m += 0.2;
    if (reg?.wings) {
      Object.entries(reg.wings).forEach(([k, count]) => {
        const def = infraCatalog.find(i => i.key === k);
        if (def?.monthlySupportBonus) m += def.monthlySupportBonus * count;
      });
    }
    if (reg?.buildings) {
      Object.entries(reg.buildings).forEach(([k, count]) => {
        const def = infraCatalog.find(i => i.key === k);
        if (def?.monthlySupportBonus) m += def.monthlySupportBonus * count;
      });
    }
    if ((parseInt(w) || 0) <= 0 && (parseInt(v) || 0) <= 0) m -= 0.2;
    return Math.min(2.5, Math.max(-1.0, m));
  };

  const handleAllocateRegion = async (regionId) => {
    if (actionLoading) return;
    const draft = regionalAllocDrafts[regionId] || { funds: 0, workers: 0, volunteers: 0 };
    setActionLoading(true);
    setError(null);
    setSuccess(null);
    try {
      const updated = await allocateRegionalResources(gameId, stateCode, {
        regionId,
        allocatedFunds: parseFloat(draft.funds) || 0,
        allocatedWorkers: parseInt(draft.workers) || 0,
        allocatedVolunteers: parseInt(draft.volunteers) || 0
      });
      if (updated) {
        if (onGameUpdate) onGameUpdate(updated);
        setSuccess(`Resources successfully deployed to ${stateObj?.regions?.[regionId]?.regionName || regionId}!`);
        await loadDetail();
      }
    } catch (err) {
      setError(err.message || 'Failed to deploy resources to region.');
    } finally {
      setActionLoading(false);
    }
  };

  useEffect(() => {
    loadDetail();
  }, [gameId, stateCode]);

  const stateObj = stateDetail?.state || stateSummary;

  // Calculate total monthly cash output from infrastructure & wings
  const monthlyCashOutput = useMemo(() => {
    let cash = 0;
    if (stateObj?.buildings) {
      Object.entries(stateObj.buildings).forEach(([k, count]) => {
        const def = infraCatalog.find(i => i.key === k);
        if (def?.monthlyCashOutput) cash += def.monthlyCashOutput * count;
      });
    }
    if (stateObj?.regions) {
      Object.values(stateObj.regions).forEach(reg => {
        if (reg?.buildings) {
          Object.entries(reg.buildings).forEach(([k, count]) => {
            const def = infraCatalog.find(i => i.key === k);
            if (def?.monthlyCashOutput) cash += def.monthlyCashOutput * count;
          });
        }
        if (reg?.wings) {
          Object.entries(reg.wings).forEach(([k, count]) => {
            const def = infraCatalog.find(i => i.key === k);
            if (def?.monthlyCashOutput) cash += def.monthlyCashOutput * count;
          });
        }
      });
    }
    return Math.round(cash * 100) / 100;
  }, [stateObj, infraCatalog]);

  const netIncomePerTurn = useMemo(() => {
    if (stateDetail?.netIncomePerTurn != null) return stateDetail.netIncomePerTurn;
    if (stateObj?.netIncomePerTurn != null) return stateObj.netIncomePerTurn;
    return Math.round((0.5 + monthlyCashOutput) * 100) / 100;
  }, [stateDetail, stateObj, monthlyCashOutput]);

  // React to news
  const handleReactNews = async (newsKey, optionKey) => {
    if (actionLoading) return;
    if (stateDetail?.resolvedNewsReaction) {
      setError('Reaction has already been committed for this news item and is locked for this turn.');
      return;
    }
    setActionLoading(true);
    setError(null);
    setSuccess(null);
    try {
      const updated = await reactNationalStateNews(gameId, stateCode, { newsKey, optionKey });
      if (updated) {
        if (onGameUpdate) onGameUpdate(updated);
        setSuccess('State reaction published! Decision locked for this turn.');
        await loadDetail();
      }
    } catch (err) {
      setError(err.message || 'Failed to react to state news.');
    } finally {
      setActionLoading(false);
    }
  };

  // Act on state issue
  const handleActOnIssue = async (issueId, actionKey) => {
    if (actionLoading) return;
    if (stateObj?.activeIssueAction) {
      setError('An action has already been deployed for this state and is locked for this turn.');
      return;
    }
    setActionLoading(true);
    setError(null);
    setSuccess(null);
    try {
      const updated = await actOnNationalStateIssue(gameId, stateCode, { issueId, actionKey });
      if (updated) {
        if (onGameUpdate) onGameUpdate(updated);
        setSuccess('Cadre mobilized on state issue! Decision locked for this turn.');
        await loadDetail();
      }
    } catch (err) {
      setError(err.message || 'Failed to execute issue action.');
    } finally {
      setActionLoading(false);
    }
  };

  // Allocate resources from national treasury to state
  const handleAllocate = async () => {
    if (actionLoading) return;
    setActionLoading(true);
    setError(null);
    setSuccess(null);
    try {
      const updated = await allocateNationalStateResources(gameId, stateCode, {
        funds: Number(transferFunds),
        workers: Number(transferWorkers),
        volunteers: Number(transferVolunteers)
      });
      if (updated) {
        if (onGameUpdate) onGameUpdate(updated);
        setSuccess(`Transferred ₹${transferFunds} Cr, ${transferWorkers} workers, and ${transferVolunteers} volunteers to ${stateObj?.stateName}!`);
        await loadDetail();
      }
    } catch (err) {
      setError(err.message || 'Failed to transfer resources.');
    } finally {
      setActionLoading(false);
    }
  };

  // Execute campaign push (Mega Rally, Ad Blitz, Leader Visit, etc.)
  const handleCampaignPush = async (actionType) => {
    if (actionLoading) return;
    setActionLoading(true);
    setError(null);
    setSuccess(null);
    try {
      const updated = await executeNationalStateCampaign(gameId, stateCode, { actionType });
      if (updated) {
        if (onGameUpdate) onGameUpdate(updated);
        setSuccess(`Campaign push '${actionType.replace('_', ' ')}' executed with massive public visibility!`);
        await loadDetail();
      }
    } catch (err) {
      setError(err.message || 'Failed to execute campaign push.');
    } finally {
      setActionLoading(false);
    }
  };

  // Phase badge color
  const getPhaseBadge = (phase) => {
    switch (phase) {
      case 'FINAL_SPRINT':
        return { label: '🔴 FINAL SPRINT', bg: 'rgba(239, 68, 68, 0.2)', border: '#ef4444', color: '#f87171' };
      case 'CAMPAIGN':
        return { label: '🟠 CAMPAIGN MODE', bg: 'rgba(249, 115, 22, 0.2)', border: '#f97316', color: '#fb923c' };
      case 'PRE_ELECTION':
        return { label: '🟡 PRE-ELECTION', bg: 'rgba(234, 179, 8, 0.2)', border: '#eab308', color: '#facc15' };
      case 'ELECTION_DAY':
        return { label: '🗳️ ELECTION DAY', bg: 'rgba(56, 189, 248, 0.2)', border: '#38bdf8', color: '#38bdf8' };
      default:
        return { label: '⚪ REGULAR GOVERNANCE', bg: 'rgba(148, 163, 184, 0.1)', border: '#64748b', color: '#94a3b8' };
    }
  };

  const phaseInfo = getPhaseBadge(stateObj?.electionPhase);
  const playerKey = (activeGame?.partyKey || 'YDP').toUpperCase();

  const issuesList = stateDetail?.issues || [];
  const selectedIssue = issuesList.find(i => i.id === selectedIssueId) || issuesList[0];
  const tacticalActions = stateDetail?.tacticalActions || [];
  const activeNews = stateDetail?.activeNews;
  const isNewsDone = !activeNews || Boolean(stateDetail?.resolvedNewsReaction);
  const isIssueDone = Boolean(stateObj?.activeIssueAction);
  const isAllTasksCompleted = isNewsDone && isIssueDone;

  const isCampaignPhase = stateObj?.electionPhase === 'CAMPAIGN' || stateObj?.electionPhase === 'FINAL_SPRINT';

  return (
    <div style={{
      position: 'fixed',
      top: 0,
      left: 0,
      right: 0,
      bottom: 0,
      backgroundColor: 'rgba(10, 15, 30, 0.92)',
      backdropFilter: 'blur(10px)',
      zIndex: 9999,
      display: 'flex',
      flexDirection: 'column',
      overflow: 'hidden'
    }}>
      {/* ── TOP HEADER ── */}
      <div style={{
        padding: '16px 20px',
        backgroundColor: '#0f172a',
        borderBottom: '1px solid rgba(56, 189, 248, 0.25)',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        flexWrap: 'wrap',
        gap: '12px'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
          <div style={{
            fontSize: '28px',
            width: '46px',
            height: '46px',
            borderRadius: '10px',
            backgroundColor: 'rgba(168, 85, 247, 0.2)',
            border: '1px solid #a855f7',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center'
          }}>
            🏛️
          </div>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <h2 style={{ margin: 0, fontSize: '18px', color: '#ffffff', fontWeight: 900 }}>
                {stateObj?.stateName?.toUpperCase()}
              </h2>
              <span style={{
                fontSize: '9px',
                fontWeight: 900,
                padding: '3px 8px',
                borderRadius: '6px',
                backgroundColor: phaseInfo.bg,
                border: `1px solid ${phaseInfo.border}`,
                color: phaseInfo.color
              }}>
                {phaseInfo.label}
              </span>
            </div>
            <div style={{ fontSize: '10px', color: '#94a3b8', marginTop: '2px', display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
              <span>Ruling: <strong style={{ color: '#f59e0b' }}>{stateObj?.rulingParty}</strong></span>
              <span>•</span>
              <span>{stateObj?.totalAssemblySeats} Assembly / {stateObj?.totalLokSabhaSeats} LS</span>
              <span>•</span>
              <span style={{ color: phaseInfo.color, fontWeight: 700 }}>
                {stateObj?.turnsToElection} Turns Left
              </span>
            </div>
          </div>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap' }}>
          {/* Quick Stats Pill - Hidden on mobile */}
          <div className="nwr-hide-mobile" style={{
            display: 'flex',
            gap: '12px',
            padding: '5px 12px',
            backgroundColor: 'rgba(30, 41, 59, 0.7)',
            borderRadius: '8px',
            border: '1px solid rgba(255,255,255,0.08)',
            fontSize: '10.5px'
          }}>
            <div>
              <span style={{ color: '#94a3b8' }}>State Funds: </span>
              <strong style={{ color: '#34d399' }}>₹{stateObj?.stateFunds?.toFixed(1)} Cr</strong>
            </div>
            <div style={{ borderLeft: '1px solid rgba(255,255,255,0.1)', paddingLeft: '10px' }}>
              <span style={{ color: '#94a3b8' }}>Workers: </span>
              <strong style={{ color: '#38bdf8' }}>{stateObj?.stateWorkers?.toLocaleString()}</strong>
            </div>
            <div style={{ borderLeft: '1px solid rgba(255,255,255,0.1)', paddingLeft: '10px' }}>
              <span style={{ color: '#94a3b8' }}>Momentum: </span>
              <strong style={{ color: '#f59e0b' }}>{stateObj?.momentumMultiplier?.toFixed(1)}x</strong>
            </div>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <div style={{
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              padding: '6px 12px',
              borderRadius: '8px',
              fontSize: '11px',
              fontWeight: 700,
              backgroundColor: isAllTasksCompleted ? 'rgba(16, 185, 129, 0.15)' : 'rgba(245, 158, 11, 0.15)',
              border: `1px solid ${isAllTasksCompleted ? '#10b981' : '#f59e0b'}`,
              color: isAllTasksCompleted ? '#34d399' : '#fbbf24'
            }}>
              <span>{isAllTasksCompleted ? '✅ State Directives Complete' : `⏳ Directives: ${(isNewsDone ? 1 : 0) + (isIssueDone ? 1 : 0)}/2 Taken`}</span>
            </div>

            <button
              onClick={handleDoneOrSave}
              disabled={actionLoading}
              style={{
                backgroundColor: isAllTasksCompleted ? '#10b981' : '#2563eb',
                border: 'none',
                color: '#ffffff',
                borderRadius: '8px',
                padding: '8px 18px',
                fontWeight: 900,
                fontSize: '12px',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '6px',
                boxShadow: isAllTasksCompleted ? '0 0 14px rgba(16, 185, 129, 0.45)' : 'none',
                transition: 'all 0.2s ease'
              }}
            >
              {isAllTasksCompleted ? '✓ Done' : '💾 Save & Exit'}
            </button>

            <button
              onClick={onClose}
              style={{
                backgroundColor: 'rgba(255, 255, 255, 0.06)',
                border: '1px solid rgba(255, 255, 255, 0.15)',
                color: '#cbd5e1',
                borderRadius: '8px',
                padding: '8px 14px',
                fontWeight: 700,
                fontSize: '12px',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '6px'
              }}
            >
              ✕ Close
            </button>
          </div>
        </div>
      </div>

      {/* ── SUB-NAV BAR ── */}
      <div className="nwr-subnav-bar">
        {[
          { key: 'news', label: '📰 Events', count: isNewsDone ? '✓' : '1' },
          { key: 'issues', label: '📋 Issues', count: issuesList.length },
          { key: 'management', label: '🏛️ Regions', count: Object.keys(stateObj?.regions || {}).length ? `${Object.keys(stateObj?.regions || {}).length}` : `₹${stateObj?.stateFunds?.toFixed(0)} Cr` },
          { key: 'polling', label: '📊 Poll', count: `${stateObj?.voteSplits?.[playerKey] || 0}%` }
        ].map(tab => {
          const isActive = subTab === tab.key;
          return (
            <button
              key={tab.key}
              onClick={() => setSubTab(tab.key)}
              className="nwr-subnav-btn"
              style={{
                borderRadius: '8px',
                border: isActive ? '1.5px solid #38bdf8' : '1px solid rgba(255,255,255,0.08)',
                backgroundColor: isActive ? 'rgba(56, 189, 248, 0.16)' : 'rgba(15, 23, 42, 0.5)',
                color: isActive ? '#ffffff' : '#94a3b8',
                fontWeight: isActive ? 800 : 600
              }}
            >
              <span>{tab.label}</span>
              <span style={{
                fontSize: '9px',
                fontWeight: 900,
                padding: '1px 6px',
                borderRadius: '10px',
                backgroundColor: isActive ? '#0284c7' : 'rgba(255,255,255,0.1)',
                color: '#ffffff'
              }}>
                {tab.count}
              </span>
            </button>
          );
        })}
      </div>

      {/* Notifications */}
      {error && (
        <div style={{ margin: '10px 20px 0', padding: '10px 14px', backgroundColor: 'rgba(239, 68, 68, 0.2)', border: '1px solid #ef4444', borderRadius: '8px', color: '#fca5a5', fontSize: '12px' }}>
          ⚠️ {error}
        </div>
      )}
      {success && (
        <div style={{ margin: '10px 20px 0', padding: '10px 14px', backgroundColor: 'rgba(16, 185, 129, 0.2)', border: '1px solid #10b981', borderRadius: '8px', color: '#6ee7b7', fontSize: '12px' }}>
          ✅ {success}
        </div>
      )}

      {/* ── MODAL BODY CONTENT ── */}
      <div className="nwr-modal-body">
        {loading ? (
          <div style={{ textAlign: 'center', padding: '40px', color: '#94a3b8' }}>
            Loading state intelligence...
          </div>
        ) : (
          <>
            {/* ── 1. STATE NEWS TAB ── */}
            {subTab === 'news' && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <h3 style={{ margin: 0, fontSize: '15px', color: '#ffffff' }}>
                    📰 Breaking State Developments — {stateObj?.stateName}
                  </h3>
                  <span style={{ fontSize: '11px', color: '#38bdf8' }}>
                    Month Tag: {activeNews?.monthTags?.[0] || 'Current Month'}
                  </span>
                </div>

                {activeNews ? (
                  <div style={{
                    background: 'linear-gradient(180deg, #1e293b 0%, #0f172a 100%)',
                    borderRadius: '12px',
                    border: '1px solid rgba(56, 189, 248, 0.3)',
                    padding: '20px',
                    boxShadow: '0 8px 24px rgba(0,0,0,0.4)',
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '14px'
                  }}>
                    <div>
                      <div style={{ display: 'flex', gap: '8px', alignItems: 'center', marginBottom: '6px' }}>
                        <span style={{
                          fontSize: '9px',
                          fontWeight: 800,
                          padding: '2px 8px',
                          borderRadius: '4px',
                          backgroundColor: 'rgba(236, 72, 153, 0.2)',
                          color: '#f472b6',
                          border: '1px solid rgba(236, 72, 153, 0.4)'
                        }}>
                          STATE FLASH
                        </span>
                        <span style={{ fontSize: '10px', color: '#94a3b8' }}>
                          Topic: {activeNews.issueTags?.join(', ') || 'Politics'}
                        </span>
                      </div>
                      <h4 style={{ margin: 0, fontSize: '16px', color: '#ffffff', fontWeight: 800 }}>
                        {activeNews.title}
                      </h4>
                      <p style={{ margin: '8px 0 0', fontSize: '12.5px', color: '#cbd5e1', lineHeight: 1.5 }}>
                        {activeNews.description}
                      </p>
                    </div>

                    <h5 style={{ margin: '8px 0 0', fontSize: '12px', color: '#38bdf8', fontWeight: 800 }}>
                      Choose Party Reaction (Affects State Popular Opinion):
                    </h5>

                    {/* Outcome Notification Banner if Reaction Resolved */}
                    {stateDetail?.lastNewsResolution && stateDetail?.lastNewsResolution?.newsKey === activeNews.newsKey && (
                      <div style={{
                        padding: '12px 14px',
                        borderRadius: '8px',
                        backgroundColor: stateDetail.lastNewsResolution.riskTriggered ? 'rgba(239, 68, 68, 0.15)' : 'rgba(16, 185, 129, 0.15)',
                        border: `1.5px solid ${stateDetail.lastNewsResolution.riskTriggered ? '#ef4444' : '#10b981'}`,
                        display: 'flex',
                        flexDirection: 'column',
                        gap: '4px'
                      }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontWeight: 800, fontSize: '12px', color: stateDetail.lastNewsResolution.riskTriggered ? '#f87171' : '#34d399' }}>
                          <span>{stateDetail.lastNewsResolution.riskTriggered ? '💥 BACKLASH MATERIALIZED' : '✅ STANCE RESONATED CLEANLY'}</span>
                          <span style={{ fontSize: '10px', color: '#cbd5e1' }}>
                            (Net Support Impact: <strong>{stateDetail.lastNewsResolution.netSupportDelta >= 0 ? `+${stateDetail.lastNewsResolution.netSupportDelta}` : stateDetail.lastNewsResolution.netSupportDelta}%</strong>)
                          </span>
                        </div>
                        {stateDetail.lastNewsResolution.riskTriggered ? (
                          <div style={{ fontSize: '11px', color: '#fca5a5' }}>
                            ⚠️ {stateDetail.lastNewsResolution.badOutcome} (Base +{stateDetail.lastNewsResolution.baseSupport}% minus penalty {stateDetail.lastNewsResolution.riskSupportPenalty}%)
                          </div>
                        ) : (
                          <div style={{ fontSize: '11px', color: '#a7f3d0' }}>
                            Your party secured popular support across the state electorate!
                          </div>
                        )}
                      </div>
                    )}

                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '12px' }}>
                      {(activeNews.reactionOptions || []).map((opt, idx) => {
                        const optKey = opt.optionKey || opt.reactionKey || `opt_${idx}`;
                        const isSelected = stateDetail?.resolvedNewsReaction === optKey;
                        const eff = opt.effects?.playerParty || opt.effects?.selfParty || {};
                        const support = eff.publicSupport !== undefined ? eff.publicSupport : 0;
                        const morale = eff.partyMorale !== undefined ? eff.partyMorale : 0;
                        const media = eff.mediaImage !== undefined ? eff.mediaImage : 0;

                        return (
                          <div
                            key={optKey}
                            onClick={!isNewsDone ? () => handleReactNews(activeNews.newsKey, optKey) : undefined}
                            style={{
                              backgroundColor: isSelected ? 'rgba(56, 189, 248, 0.15)' : 'rgba(15, 23, 42, 0.7)',
                              border: isSelected ? '2px solid #38bdf8' : '1px solid rgba(255,255,255,0.1)',
                              borderRadius: '10px',
                              padding: '14px',
                              cursor: isNewsDone ? (isSelected ? 'default' : 'not-allowed') : 'pointer',
                              opacity: isNewsDone && !isSelected ? 0.45 : 1,
                              display: 'flex',
                              flexDirection: 'column',
                              justifyContent: 'space-between',
                              gap: '12px',
                              transition: 'all 0.2s',
                              boxShadow: isSelected ? '0 0 12px rgba(56, 189, 248, 0.2)' : 'none'
                            }}
                          >
                            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: '6px' }}>
                                <span style={{
                                  fontSize: '9px',
                                  fontWeight: 800,
                                  color: '#38bdf8',
                                  textTransform: 'uppercase',
                                  letterSpacing: '0.05em',
                                  backgroundColor: 'rgba(56, 189, 248, 0.1)',
                                  padding: '2px 6px',
                                  borderRadius: '4px'
                                }}>
                                  Option {idx + 1}
                                </span>
                                {isSelected && (
                                  <span style={{ fontSize: '8.5px', fontWeight: 900, backgroundColor: '#0284c7', color: '#ffffff', padding: '2px 6px', borderRadius: '4px' }}>
                                    ACTIVE STANCE 🔒
                                  </span>
                                )}
                              </div>

                              <span style={{ fontSize: '12px', fontWeight: 700, color: '#ffffff', lineHeight: 1.4 }}>
                                {opt.text}
                              </span>

                              {/* Baseline Projected Gains */}
                              <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', fontSize: '10px' }}>
                                <span style={{
                                  padding: '2px 6px',
                                  borderRadius: '4px',
                                  backgroundColor: support >= 0 ? 'rgba(16, 185, 129, 0.15)' : 'rgba(239, 68, 68, 0.15)',
                                  color: support >= 0 ? '#34d399' : '#f87171',
                                  fontWeight: 800
                                }}>
                                  📊 Support: {support >= 0 ? `+${support}` : support}%
                                </span>
                                {morale !== 0 && (
                                  <span style={{ padding: '2px 6px', borderRadius: '4px', backgroundColor: 'rgba(251, 191, 36, 0.15)', color: '#fbbf24', fontWeight: 800 }}>
                                    ⚡ Morale: {morale >= 0 ? `+${morale}` : morale}
                                  </span>
                                )}
                                {media !== 0 && (
                                  <span style={{ padding: '2px 6px', borderRadius: '4px', backgroundColor: 'rgba(147, 197, 253, 0.15)', color: '#93c5fd', fontWeight: 800 }}>
                                    📰 Media: {media >= 0 ? `+${media}` : media}
                                  </span>
                                )}
                              </div>
                            </div>

                            <button
                              disabled={actionLoading || isNewsDone}
                              style={{
                                padding: '6px 12px',
                                borderRadius: '6px',
                                border: 'none',
                                cursor: isNewsDone ? (isSelected ? 'default' : 'not-allowed') : 'pointer',
                                fontWeight: 800,
                                fontSize: '11px',
                                backgroundColor: isSelected ? '#0284c7' : isNewsDone ? '#334155' : 'rgba(255,255,255,0.08)',
                                color: isSelected ? '#ffffff' : isNewsDone ? '#64748b' : '#cbd5e1',
                                alignSelf: 'flex-start'
                              }}
                            >
                              {isSelected ? 'Committed 🔒' : isNewsDone ? 'Locked for Turn' : 'Issue Stance'}
                            </button>
                          </div>
                        );
                      })}
                    </div>
                  </div>
                ) : (
                  <div style={{ padding: '30px', textAlign: 'center', backgroundColor: '#1e293b', borderRadius: '10px', color: '#94a3b8' }}>
                    No pending news flash for this state in the current turn.
                  </div>
                )}
              </div>
            )}

            {/* ── 2. REGIONAL ISSUES & TACTICAL ACTIONS ── */}
            {subTab === 'issues' && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
                  <h3 style={{ margin: 0, fontSize: '15px', color: '#ffffff' }}>
                    📋 Curated Historical Issues (2001–2005 Era)
                  </h3>

                  {/* Conviction Streak Indicator */}
                  <div style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '6px',
                    padding: '6px 12px',
                    borderRadius: '8px',
                    backgroundColor: (stateObj?.issueStreak || 0) >= 2 ? 'rgba(245, 158, 11, 0.2)' : 'rgba(255,255,255,0.06)',
                    border: (stateObj?.issueStreak || 0) >= 2 ? '1px solid #f59e0b' : '1px solid rgba(255,255,255,0.15)'
                  }}>
                    <span style={{ fontSize: '14px' }}>⚡</span>
                    <span style={{ fontSize: '11px', fontWeight: 800, color: (stateObj?.issueStreak || 0) >= 2 ? '#fbbf24' : '#ffffff' }}>
                      Conviction Streak: {stateObj?.issueStreak || 0} Turns ({stateObj?.momentumMultiplier?.toFixed(1) || 1.0}x Multiplier)
                    </span>
                  </div>
                </div>

                {/* Issues Row / Selector */}
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '10px' }}>
                  {issuesList.map(issue => {
                    const isSelected = issue.id === selectedIssueId;
                    const isActiveIssue = stateObj?.activeIssueId === issue.id;

                    return (
                      <div
                        key={issue.id}
                        onClick={() => setSelectedIssueId(issue.id)}
                        style={{
                          backgroundColor: isSelected ? 'rgba(56, 189, 248, 0.18)' : 'rgba(15, 23, 42, 0.7)',
                          border: isSelected ? '2px solid #38bdf8' : isActiveIssue ? '1.5px solid #10b981' : '1px solid rgba(255,255,255,0.1)',
                          borderRadius: '10px',
                          padding: '14px',
                          cursor: 'pointer',
                          display: 'flex',
                          flexDirection: 'column',
                          gap: '6px',
                          transition: 'all 0.2s'
                        }}
                      >
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                          <span style={{ fontSize: '20px' }}>{issue.icon}</span>
                          {isActiveIssue && (
                            <span style={{ fontSize: '8px', fontWeight: 900, backgroundColor: '#10b981', color: '#ffffff', padding: '1px 5px', borderRadius: '4px' }}>
                              ACTIVE AGITATION
                            </span>
                          )}
                        </div>
                        <h4 style={{ margin: 0, fontSize: '13px', color: isSelected ? '#38bdf8' : '#ffffff', fontWeight: 800 }}>
                          {issue.title}
                        </h4>
                        <span style={{ fontSize: '9px', color: '#94a3b8', textTransform: 'uppercase' }}>
                          Category: {issue.category}
                        </span>
                      </div>
                    );
                  })}
                </div>

                {/* Selected Issue Detail & 10 Actions */}
                {selectedIssue && (
                  <div style={{
                    backgroundColor: 'rgba(15, 23, 42, 0.85)',
                    border: '1px solid rgba(56, 189, 248, 0.25)',
                    borderRadius: '12px',
                    padding: '18px',
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '14px'
                  }}>
                    <div>
                      <h4 style={{ margin: 0, fontSize: '15px', color: '#38bdf8', fontWeight: 800, display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <span>{selectedIssue.icon}</span> {selectedIssue.title}
                      </h4>
                      <p style={{ margin: '6px 0 0', fontSize: '12px', color: '#cbd5e1', lineHeight: 1.5 }}>
                        {selectedIssue.description}
                      </p>
                    </div>

                    <h5 style={{ margin: '8px 0 0', fontSize: '12px', color: '#fbbf24', fontWeight: 800 }}>
                      Select Tactical Action to Mobilize Cadre on this Issue:
                    </h5>

                    {/* 10 Tactical Actions Grid */}
                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(210px, 1fr))', gap: '10px' }}>
                      {tacticalActions.map(act => {
                        const isIssueLocked = Boolean(stateObj?.activeIssueAction);
                        const isCommitted = stateObj?.activeIssueId === selectedIssue.id && stateObj?.activeIssueAction === act.key;
                        const notEnoughFunds = (stateObj?.stateFunds < act.costCr);

                        return (
                          <div
                            key={act.key}
                            style={{
                              backgroundColor: isCommitted ? 'rgba(16, 185, 129, 0.15)' : 'rgba(30, 41, 59, 0.7)',
                              border: isCommitted ? '2px solid #10b981' : '1px solid rgba(255,255,255,0.1)',
                              borderRadius: '8px',
                              padding: '12px',
                              display: 'flex',
                              flexDirection: 'column',
                              justifyContent: 'space-between',
                              gap: '10px',
                              opacity: isIssueLocked && !isCommitted ? 0.45 : 1
                            }}
                          >
                            <div>
                              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                <span style={{ fontSize: '12.5px', fontWeight: 800, color: isCommitted ? '#34d399' : '#ffffff' }}>
                                  {act.icon} {act.label}
                                </span>
                                {isCommitted && (
                                  <span style={{ fontSize: '8.5px', fontWeight: 900, color: '#10b981' }}>COMMITTED 🔒</span>
                                )}
                              </div>
                              <p style={{ margin: '4px 0', fontSize: '10.5px', color: '#94a3b8', lineHeight: 1.4 }}>
                                {act.description}
                              </p>
                              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '10px', marginTop: '6px' }}>
                                <span style={{ color: '#f59e0b' }}>Cost: ₹{act.costCr} Cr</span>
                                <span style={{ color: '#38bdf8' }}>Base: +{act.baseSupportDelta}%</span>
                              </div>
                            </div>

                            <button
                              disabled={actionLoading || isIssueLocked || notEnoughFunds}
                              onClick={() => !isIssueLocked && handleActOnIssue(selectedIssue.id, act.key)}
                              style={{
                                padding: '6px 10px',
                                borderRadius: '6px',
                                border: 'none',
                                cursor: isIssueLocked ? (isCommitted ? 'default' : 'not-allowed') : notEnoughFunds ? 'not-allowed' : 'pointer',
                                fontWeight: 800,
                                fontSize: '11px',
                                backgroundColor: isCommitted ? '#059669' : isIssueLocked ? '#334155' : notEnoughFunds ? '#475569' : '#0284c7',
                                color: isIssueLocked && !isCommitted ? '#94a3b8' : '#ffffff',
                                width: '100%',
                                transition: 'all 0.2s'
                              }}
                            >
                              {isCommitted ? 'Committed 🔒' : isIssueLocked ? 'Locked for Turn' : notEnoughFunds ? 'Insufficient State Funds' : 'Mobilize'}
                            </button>
                          </div>
                        );
                      })}
                    </div>
                  </div>
                )}
              </div>
            )}

            {/* ── 3. STATE MANAGEMENT & REGIONAL OPERATIONS ── */}
            {subTab === 'management' && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '22px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <h3 style={{ margin: 0, fontSize: '15px', color: '#ffffff', fontWeight: 800 }}>
                    🏛️ State Infrastructure & Regions — {stateObj?.stateName}
                  </h3>
                </div>

                {/* State Balance & Command Overview */}
                <div className="nwr-stat-grid-modal">
                  <div className="nwr-stat-card-modal" style={{ backgroundColor: 'rgba(16, 185, 129, 0.1)', border: '1px solid #10b981' }}>
                    <div style={{ fontSize: '10.5px', color: '#94a3b8', fontWeight: 700 }}>State Treasury Pool</div>
                    <div className="nwr-stat-val-modal" style={{ color: '#34d399' }}>
                      ₹{stateObj?.stateFunds?.toFixed(1)} Cr
                    </div>
                  </div>

                  <div className="nwr-stat-card-modal" style={{ backgroundColor: 'rgba(56, 189, 248, 0.1)', border: '1px solid #38bdf8' }}>
                    <div style={{ fontSize: '10.5px', color: '#94a3b8', fontWeight: 700 }}>Available Cadres</div>
                    <div className="nwr-stat-val-modal" style={{ color: '#38bdf8' }}>
                      {stateObj?.stateWorkers?.toLocaleString()}
                    </div>
                  </div>

                  <div className="nwr-stat-card-modal" style={{ backgroundColor: 'rgba(168, 85, 247, 0.1)', border: '1px solid #a855f7' }}>
                    <div style={{ fontSize: '10.5px', color: '#94a3b8', fontWeight: 700 }}>Volunteers</div>
                    <div className="nwr-stat-val-modal" style={{ color: '#c084fc' }}>
                      {stateObj?.stateVolunteers?.toLocaleString()}
                    </div>
                  </div>

                  <div className="nwr-stat-card-modal" style={{ backgroundColor: 'rgba(245, 158, 11, 0.1)', border: '1px solid #f59e0b' }}>
                    <div style={{ fontSize: '10.5px', color: '#94a3b8', fontWeight: 700 }}>Net Income / Turn</div>
                    <div className="nwr-stat-val-modal" style={{ color: '#fbbf24' }}>
                      +₹{netIncomePerTurn.toFixed(2)} Cr
                    </div>
                  </div>
                </div>

                {/* National Top-up Transfer Bar */}
                <div style={{
                  backgroundColor: 'rgba(15, 23, 42, 0.8)',
                  border: '1px solid rgba(56, 189, 248, 0.25)',
                  borderRadius: '12px',
                  padding: '16px 20px',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '12px'
                }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <div>
                      <span style={{ fontSize: '13px', fontWeight: 800, color: '#ffffff' }}>
                        Top-up Resources from National Headquarters
                      </span>
                      <span style={{ fontSize: '11px', color: '#94a3b8', marginLeft: '10px' }}>
                        (National Reserves: ₹{activeGame?.playerFunds?.toFixed(1) || 0} Cr)
                      </span>
                    </div>
                  </div>

                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '12px' }}>
                    <div>
                      <label style={{ fontSize: '10px', color: '#cbd5e1', fontWeight: 700, display: 'block', marginBottom: '4px' }}>
                        Funds (₹ Cr):
                      </label>
                      <input
                        type="number"
                        min="0"
                        step="0.5"
                        max={activeGame?.playerFunds || 10}
                        value={transferFunds}
                        onChange={(e) => setTransferFunds(e.target.value)}
                        style={{
                          width: '100%',
                          padding: '8px 10px',
                          borderRadius: '6px',
                          border: '1px solid rgba(255,255,255,0.15)',
                          backgroundColor: '#1e293b',
                          color: '#ffffff',
                          fontWeight: 700,
                          fontSize: '12px'
                        }}
                      />
                    </div>

                    <div>
                      <label style={{ fontSize: '10px', color: '#cbd5e1', fontWeight: 700, display: 'block', marginBottom: '4px' }}>
                        Workers:
                      </label>
                      <input
                        type="number"
                        min="0"
                        step="500"
                        value={transferWorkers}
                        onChange={(e) => setTransferWorkers(e.target.value)}
                        style={{
                          width: '100%',
                          padding: '8px 10px',
                          borderRadius: '6px',
                          border: '1px solid rgba(255,255,255,0.15)',
                          backgroundColor: '#1e293b',
                          color: '#ffffff',
                          fontWeight: 700,
                          fontSize: '12px'
                        }}
                      />
                    </div>

                    <div>
                      <label style={{ fontSize: '10px', color: '#cbd5e1', fontWeight: 700, display: 'block', marginBottom: '4px' }}>
                        Volunteers:
                      </label>
                      <input
                        type="number"
                        min="0"
                        step="500"
                        value={transferVolunteers}
                        onChange={(e) => setTransferVolunteers(e.target.value)}
                        style={{
                          width: '100%',
                          padding: '8px 10px',
                          borderRadius: '6px',
                          border: '1px solid rgba(255,255,255,0.15)',
                          backgroundColor: '#1e293b',
                          color: '#ffffff',
                          fontWeight: 700,
                          fontSize: '12px'
                        }}
                      />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'flex-end' }}>
                      <button
                        disabled={actionLoading}
                        onClick={handleAllocate}
                        style={{
                          width: '100%',
                          padding: '9px 16px',
                          borderRadius: '6px',
                          border: 'none',
                          backgroundColor: '#0284c7',
                          color: '#ffffff',
                          fontWeight: 800,
                          fontSize: '12px',
                          cursor: 'pointer'
                        }}
                      >
                        Transfer to State →
                      </button>
                    </div>
                  </div>
                </div>

                {/* ── REGIONAL DIVISIONS ── */}
                {(() => {
                  const totalStateWorkers = stateObj?.stateWorkers || 0;
                  const totalStateVols = stateObj?.stateVolunteers || 0;
                  const totalAllocWorkers = Object.values(regionalAllocDrafts).reduce((sum, d) => sum + (parseInt(d?.workers) || 0), 0);
                  const totalAllocVols = Object.values(regionalAllocDrafts).reduce((sum, d) => sum + (parseInt(d?.volunteers) || 0), 0);
                  const unallocWorkers = totalStateWorkers - totalAllocWorkers;
                  const unallocVols = totalStateVols - totalAllocVols;
                  const hasUnallocated = unallocWorkers > 0 || unallocVols > 0;
                  const isOverAllocated = unallocWorkers < 0 || unallocVols < 0;

                  return (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
                      {/* Top Section Title & State Pool Deployment Bar */}
                      <div style={{
                        backgroundColor: '#0c1322',
                        border: '1.5px solid rgba(56, 189, 248, 0.35)',
                        borderRadius: '14px',
                        padding: '18px 20px',
                        display: 'flex',
                        flexDirection: 'column',
                        gap: '14px',
                        boxShadow: '0 8px 24px rgba(0,0,0,0.4)'
                      }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
                          <div>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                              <h4 style={{ margin: 0, fontSize: '16px', color: '#ffffff', fontWeight: 900 }}>
                                🗺️ Politically Specific Regions ({Object.keys(stateObj?.regions || {}).length || 0}) — Deployment Pool
                              </h4>
                              <span style={{
                                fontSize: '10.5px',
                                fontWeight: 800,
                                padding: '2px 8px',
                                borderRadius: '4px',
                                backgroundColor: isOverAllocated ? 'rgba(239, 68, 68, 0.2)' : hasUnallocated ? 'rgba(245, 158, 11, 0.2)' : 'rgba(16, 185, 129, 0.2)',
                                color: isOverAllocated ? '#fca5a5' : hasUnallocated ? '#fbbf24' : '#6ee7b7',
                                border: isOverAllocated ? '1px solid #ef4444' : hasUnallocated ? '1px solid #f59e0b' : '1px solid #10b981'
                              }}>
                                {isOverAllocated
                                  ? `⚠️ Over-allocated: Exceeds State Pool`
                                  : hasUnallocated
                                    ? `🔔 Unassigned: ${Math.max(0, unallocWorkers).toLocaleString()} Cadres / ${Math.max(0, unallocVols).toLocaleString()} Vols`
                                    : '✅ 100% Deployed Across Regions'}
                              </span>
                            </div>
                          </div>

                          {/* Quick Controls */}
                          <div style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
                            <button
                              onClick={handleDistributeEvenly}
                              style={{
                                padding: '8px 14px',
                                borderRadius: '8px',
                                border: '1px solid rgba(56, 189, 248, 0.4)',
                                backgroundColor: 'rgba(56, 189, 248, 0.12)',
                                color: '#38bdf8',
                                fontSize: '11.5px',
                                fontWeight: 800,
                                cursor: 'pointer'
                              }}
                              title="Evenly distribute total available workers and volunteers across all regions"
                            >
                              ⚡ Distribute Equally
                            </button>

                            <button
                              disabled={actionLoading || isOverAllocated}
                              onClick={handleSaveAllRegionalAllocations}
                              style={{
                                padding: '8px 18px',
                                borderRadius: '8px',
                                border: 'none',
                                backgroundColor: isOverAllocated ? '#475569' : '#0284c7',
                                color: '#ffffff',
                                fontSize: '12px',
                                fontWeight: 800,
                                cursor: isOverAllocated ? 'not-allowed' : 'pointer',
                                boxShadow: isOverAllocated ? 'none' : '0 4px 12px rgba(2, 132, 199, 0.35)'
                              }}
                            >
                              💾 Save & Deploy Allocations
                            </button>
                          </div>
                        </div>

                        {/* Summary Metrics Grid */}
                        <div className="nwr-summary-deploy-bar">
                          {/* Total State Cadres */}
                          <div style={{
                            backgroundColor: '#131e36',
                            border: '1px solid rgba(56, 189, 248, 0.2)',
                            borderRadius: '8px',
                            padding: '8px 12px'
                          }}>
                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                              <span style={{ fontSize: '10px', color: '#94a3b8', fontWeight: 700 }}>👷 Cadres</span>
                              <strong style={{ fontSize: '13px', color: '#38bdf8' }}>{totalStateWorkers.toLocaleString()}</strong>
                            </div>
                            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '9px', marginTop: '4px' }}>
                              <span style={{ color: '#cbd5e1' }}>Deployed: <strong>{totalAllocWorkers.toLocaleString()}</strong></span>
                              <span style={{ color: unallocWorkers > 0 ? '#fbbf24' : unallocWorkers < 0 ? '#f87171' : '#64748b' }}>
                                Reserve: <strong>{unallocWorkers.toLocaleString()}</strong>
                              </span>
                            </div>
                            <div style={{ width: '100%', height: '4px', backgroundColor: 'rgba(255,255,255,0.08)', borderRadius: '2px', marginTop: '4px', overflow: 'hidden' }}>
                              <div style={{
                                width: `${Math.min(100, Math.max(0, totalStateWorkers > 0 ? (totalAllocWorkers / totalStateWorkers) * 100 : 0))}%`,
                                height: '100%',
                                backgroundColor: isOverAllocated ? '#ef4444' : '#38bdf8'
                              }} />
                            </div>
                          </div>

                          {/* Total State Volunteers */}
                          <div style={{
                            backgroundColor: '#131e36',
                            border: '1px solid rgba(192, 132, 252, 0.2)',
                            borderRadius: '8px',
                            padding: '8px 12px'
                          }}>
                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                              <span style={{ fontSize: '10px', color: '#94a3b8', fontWeight: 700 }}>🤝 Volunteers</span>
                              <strong style={{ fontSize: '13px', color: '#c084fc' }}>{totalStateVols.toLocaleString()}</strong>
                            </div>
                            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '9px', marginTop: '4px' }}>
                              <span style={{ color: '#cbd5e1' }}>Deployed: <strong>{totalAllocVols.toLocaleString()}</strong></span>
                              <span style={{ color: unallocVols > 0 ? '#fbbf24' : unallocVols < 0 ? '#f87171' : '#64748b' }}>
                                Reserve: <strong>{unallocVols.toLocaleString()}</strong>
                              </span>
                            </div>
                            <div style={{ width: '100%', height: '4px', backgroundColor: 'rgba(255,255,255,0.08)', borderRadius: '2px', marginTop: '4px', overflow: 'hidden' }}>
                              <div style={{
                                width: `${Math.min(100, Math.max(0, totalStateVols > 0 ? (totalAllocVols / totalStateVols) * 100 : 0))}%`,
                                height: '100%',
                                backgroundColor: isOverAllocated ? '#ef4444' : '#c084fc'
                              }} />
                            </div>
                          </div>

                          {/* State Treasury */}
                          <div style={{
                            backgroundColor: '#131e36',
                            border: '1px solid rgba(245, 158, 11, 0.2)',
                            borderRadius: '8px',
                            padding: '8px 12px',
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'space-between'
                          }}>
                            <span style={{ fontSize: '10px', color: '#94a3b8', fontWeight: 700 }}>💰 Treasury</span>
                            <strong style={{ fontSize: '14px', color: '#fbbf24' }}>₹{stateObj?.stateFunds?.toFixed(1) || 0} Cr</strong>
                          </div>
                        </div>
                      </div>

                      {/* ── REGIONAL NAVIGATION & ALLOCATION CONTROLS ── */}
                      {stateObj?.regions && Object.keys(stateObj.regions).length > 0 ? (() => {
                        const regionEntries = Object.entries(stateObj.regions);
                        const regionKeys = Object.keys(stateObj.regions);
                        const activeRegionId = (selectedRegionId && stateObj.regions[selectedRegionId]) ? selectedRegionId : regionKeys[0];
                        const currentIndex = regionKeys.indexOf(activeRegionId);
                        const prevRegionId = currentIndex > 0 ? regionKeys[currentIndex - 1] : null;
                        const nextRegionId = currentIndex < regionKeys.length - 1 ? regionKeys[currentIndex + 1] : null;

                        const applyPresetPercent = (rId, type, pct) => {
                          const total = type === 'workers' ? totalStateWorkers : totalStateVols;
                          const val = Math.round(total * (pct / 100));
                          setRegionalAllocDrafts(prev => ({
                            ...prev,
                            [rId]: {
                              ...(prev[rId] || {}),
                              [type]: val
                            }
                          }));
                        };

                        const renderRegionCard = (rId, reg, isSingleView = true) => {
                          const draft = regionalAllocDrafts[rId] || { funds: 0, workers: 0, volunteers: 0 };
                          const bldgList = Object.entries(reg.buildings || {}).filter(([_, c]) => c > 0);
                          const wingList = Object.entries(reg.wings || {}).filter(([_, c]) => c > 0);
                          const currentWorkers = parseInt(draft.workers) || 0;
                          const currentVols = parseInt(draft.volunteers) || 0;
                          const projectedMomentum = calcMomentum(currentWorkers, currentVols, reg);

                          return (
                            <div
                              key={rId}
                              style={{
                                backgroundColor: '#131d38',
                                border: isSingleView ? '1.5px solid rgba(56, 189, 248, 0.4)' : '1px solid rgba(56, 189, 248, 0.25)',
                                borderRadius: '12px',
                                padding: '18px',
                                display: 'flex',
                                flexDirection: 'column',
                                gap: '14px',
                                boxShadow: isSingleView ? '0 8px 24px rgba(0,0,0,0.45)' : '0 4px 16px rgba(0,0,0,0.3)',
                                transition: 'all 0.2s ease'
                              }}
                            >
                              {/* Region Header: Name, Seats, Support, Stepper & Build Button */}
                              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
                                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
                                  <span style={{ fontSize: '16px', fontWeight: 900, color: '#ffffff' }}>
                                    {reg.regionName}
                                  </span>
                                  <span style={{
                                    fontSize: '10px',
                                    fontWeight: 800,
                                    padding: '2px 8px',
                                    borderRadius: '4px',
                                    backgroundColor: 'rgba(56, 189, 248, 0.15)',
                                    color: '#38bdf8',
                                    border: '1px solid rgba(56, 189, 248, 0.3)'
                                  }}>
                                    🏛️ {reg.lokSabhaSeats} Lok Sabha Seats
                                  </span>
                                  <span style={{
                                    fontSize: '10px',
                                    fontWeight: 800,
                                    padding: '2px 8px',
                                    borderRadius: '4px',
                                    backgroundColor: 'rgba(168, 85, 247, 0.15)',
                                    color: '#c084fc',
                                    border: '1px solid rgba(168, 85, 247, 0.3)'
                                  }}>
                                    🗳️ {reg.assemblySeats} Assembly Seats
                                  </span>
                                  <span style={{
                                    fontSize: '11px',
                                    fontWeight: 900,
                                    padding: '3px 10px',
                                    borderRadius: '6px',
                                    backgroundColor: reg.supportPercentage >= 30 ? 'rgba(16, 185, 129, 0.2)' : reg.supportPercentage >= 15 ? 'rgba(56, 189, 248, 0.2)' : 'rgba(239, 68, 68, 0.2)',
                                    color: reg.supportPercentage >= 30 ? '#34d399' : reg.supportPercentage >= 15 ? '#38bdf8' : '#f87171',
                                    border: reg.supportPercentage >= 30 ? '1px solid rgba(16, 185, 129, 0.4)' : reg.supportPercentage >= 15 ? '1px solid rgba(56, 189, 248, 0.4)' : '1px solid rgba(239, 68, 68, 0.4)'
                                  }}>
                                    🚩 {playerKey} Support: {(reg.supportPercentage || 0).toFixed(1)}%
                                  </span>
                                </div>

                                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                  {isSingleView && (
                                    <div style={{ display: 'flex', alignItems: 'center', gap: '4px', marginRight: '6px' }}>
                                      <button
                                        disabled={!prevRegionId}
                                        onClick={() => prevRegionId && setSelectedRegionId(prevRegionId)}
                                        style={{
                                          padding: '5px 9px',
                                          borderRadius: '6px',
                                          border: '1px solid rgba(255,255,255,0.15)',
                                          backgroundColor: prevRegionId ? 'rgba(15, 23, 42, 0.8)' : 'rgba(255,255,255,0.05)',
                                          color: prevRegionId ? '#cbd5e1' : '#64748b',
                                          fontSize: '11px',
                                          fontWeight: 800,
                                          cursor: prevRegionId ? 'pointer' : 'not-allowed'
                                        }}
                                        title={prevRegionId ? `Go to ${stateObj.regions[prevRegionId]?.regionName}` : 'First Region'}
                                      >
                                        ◀ Prev
                                      </button>
                                      <span style={{ fontSize: '10px', color: '#94a3b8', fontWeight: 700, padding: '0 4px' }}>
                                        {currentIndex + 1} / {regionKeys.length}
                                      </span>
                                      <button
                                        disabled={!nextRegionId}
                                        onClick={() => nextRegionId && setSelectedRegionId(nextRegionId)}
                                        style={{
                                          padding: '5px 9px',
                                          borderRadius: '6px',
                                          border: '1px solid rgba(255,255,255,0.15)',
                                          backgroundColor: nextRegionId ? 'rgba(15, 23, 42, 0.8)' : 'rgba(255,255,255,0.05)',
                                          color: nextRegionId ? '#cbd5e1' : '#64748b',
                                          fontSize: '11px',
                                          fontWeight: 800,
                                          cursor: nextRegionId ? 'pointer' : 'not-allowed'
                                        }}
                                        title={nextRegionId ? `Go to ${stateObj.regions[nextRegionId]?.regionName}` : 'Last Region'}
                                      >
                                        Next ▶
                                      </button>
                                    </div>
                                  )}

                                  <button
                                    onClick={() => {
                                      setBuildingModalRegion(rId);
                                      setBuildCategoryFilter('ALL');
                                    }}
                                    style={{
                                      padding: '7px 16px',
                                      borderRadius: '7px',
                                      border: '1.5px solid #38bdf8',
                                      backgroundColor: 'rgba(56, 189, 248, 0.15)',
                                      color: '#38bdf8',
                                      fontSize: '11.5px',
                                      fontWeight: 900,
                                      cursor: 'pointer',
                                      display: 'inline-flex',
                                      alignItems: 'center',
                                      gap: '5px',
                                      boxShadow: '0 2px 8px rgba(56, 189, 248, 0.25)'
                                    }}
                                  >
                                    <span>➕ Build Facility / Wing</span>
                                  </button>
                                </div>
                              </div>

                              {/* Regional Party Support Bar */}
                              <div style={{ width: '100%', height: '6px', backgroundColor: 'rgba(255,255,255,0.06)', borderRadius: '3px', overflow: 'hidden' }}>
                                <div
                                  style={{
                                    width: `${Math.min(100, Math.max(0, reg.supportPercentage || 0))}%`,
                                    height: '100%',
                                    backgroundColor: reg.supportPercentage >= 30 ? '#10b981' : reg.supportPercentage >= 15 ? '#0284c7' : '#ef4444',
                                    transition: 'width 0.3s ease'
                                  }}
                                />
                              </div>

                              {/* Description */}
                              <p style={{ margin: 0, fontSize: '11px', color: '#94a3b8', lineHeight: 1.45 }}>
                                {reg.description}
                              </p>

                              {/* Built Assets Chips */}
                              <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap', alignItems: 'center' }}>
                                <span style={{ fontSize: '10.5px', color: '#cbd5e1', fontWeight: 800 }}>Built Assets:</span>
                                {bldgList.length === 0 && wingList.length === 0 && (
                                  <span style={{ fontSize: '10.5px', color: '#64748b', fontStyle: 'italic' }}>
                                    No facilities or frontal wings established yet in {reg.regionName}.
                                  </span>
                                )}
                                {bldgList.map(([k, count]) => {
                                  const def = infraCatalog.find(i => i.key === k);
                                  return (
                                    <span
                                      key={k}
                                      style={{
                                        fontSize: '10px',
                                        fontWeight: 800,
                                        padding: '2px 8px',
                                        borderRadius: '6px',
                                        backgroundColor: 'rgba(56, 189, 248, 0.12)',
                                        color: '#7dd3fc',
                                        border: '1px solid rgba(56, 189, 248, 0.3)'
                                      }}
                                    >
                                      {def?.icon || '🏢'} {def?.name || k} {count > 1 ? `(×${count})` : ''}
                                    </span>
                                  );
                                })}
                                {wingList.map(([k, count]) => {
                                  const def = infraCatalog.find(i => i.key === k);
                                  return (
                                    <span
                                      key={k}
                                      style={{
                                        fontSize: '10px',
                                        fontWeight: 800,
                                        padding: '2px 8px',
                                        borderRadius: '6px',
                                        backgroundColor: 'rgba(236, 72, 153, 0.12)',
                                        color: '#f472b6',
                                        border: '1px solid rgba(236, 72, 153, 0.3)'
                                      }}
                                    >
                                      {def?.icon || '🚩'} {def?.name || k}
                                    </span>
                                  );
                                })}
                                <button
                                  onClick={() => {
                                    setBuildingModalRegion(rId);
                                    setBuildCategoryFilter('ALL');
                                  }}
                                  style={{
                                    fontSize: '9.5px',
                                    fontWeight: 800,
                                    padding: '2px 8px',
                                    borderRadius: '5px',
                                    border: '1px dashed rgba(56, 189, 248, 0.4)',
                                    backgroundColor: 'transparent',
                                    color: '#38bdf8',
                                    cursor: 'pointer'
                                  }}
                                >
                                  + Add Asset
                                </button>
                              </div>

                              {/* Slider Deployment Controls */}
                              <div style={{
                                backgroundColor: 'rgba(15, 23, 42, 0.65)',
                                borderRadius: '10px',
                                padding: '14px 18px',
                                display: 'flex',
                                flexDirection: 'column',
                                gap: '14px',
                                border: '1px solid rgba(255,255,255,0.06)'
                              }}>
                                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                                  <span style={{ fontSize: '11.5px', fontWeight: 900, color: '#e2e8f0' }}>
                                    ⚡ Regional Organizer Deployment
                                  </span>
                                  <span style={{
                                    fontSize: '10.5px',
                                    fontWeight: 800,
                                    color: projectedMomentum >= 0 ? '#34d399' : '#f87171',
                                    backgroundColor: projectedMomentum >= 0 ? 'rgba(16, 185, 129, 0.12)' : 'rgba(239, 68, 68, 0.12)',
                                    padding: '2px 10px',
                                    borderRadius: '5px',
                                    border: projectedMomentum >= 0 ? '1px solid rgba(16, 185, 129, 0.3)' : '1px solid rgba(239, 68, 68, 0.3)'
                                  }}>
                                    📈 Projected Momentum: {projectedMomentum >= 0 ? '+' : ''}{projectedMomentum.toFixed(2)}% / season
                                  </span>
                                </div>

                                {/* Slider 1: Cadre Workers */}
                                <div>
                                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                                    <label style={{ fontSize: '11px', color: '#94a3b8', fontWeight: 700 }}>
                                      👷 Cadre Workers:
                                    </label>
                                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                      {/* Quick Presets */}
                                      <div style={{ display: 'flex', gap: '4px' }}>
                                        {[10, 20, 25, 33, 50].map(pct => (
                                          <button
                                            key={pct}
                                            type="button"
                                            onClick={() => applyPresetPercent(rId, 'workers', pct)}
                                            style={{
                                              padding: '1px 5px',
                                              borderRadius: '3px',
                                              border: '1px solid rgba(56, 189, 248, 0.25)',
                                              backgroundColor: 'rgba(56, 189, 248, 0.08)',
                                              color: '#7dd3fc',
                                              fontSize: '8.5px',
                                              fontWeight: 800,
                                              cursor: 'pointer'
                                            }}
                                          >
                                            {pct}%
                                          </button>
                                        ))}
                                      </div>
                                      <span style={{ fontSize: '13px', fontWeight: 900, color: '#38bdf8' }}>
                                        {currentWorkers.toLocaleString()}
                                      </span>
                                      <span style={{ fontSize: '9.5px', color: '#64748b' }}>
                                        ({totalStateWorkers > 0 ? ((currentWorkers / totalStateWorkers) * 100).toFixed(0) : 0}% of state pool)
                                      </span>
                                    </div>
                                  </div>
                                  <input
                                    type="range"
                                    min="0"
                                    max={totalStateWorkers || 10000}
                                    step="100"
                                    value={currentWorkers}
                                    onChange={(e) => {
                                      const val = parseInt(e.target.value) || 0;
                                      setRegionalAllocDrafts(prev => ({
                                        ...prev,
                                        [rId]: { ...(prev[rId] || {}), workers: val }
                                      }));
                                    }}
                                    style={{
                                      width: '100%',
                                      accentColor: '#38bdf8',
                                      cursor: 'pointer'
                                    }}
                                  />
                                </div>

                                {/* Slider 2: Grassroots Volunteers */}
                                <div>
                                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                                    <label style={{ fontSize: '11px', color: '#94a3b8', fontWeight: 700 }}>
                                      🤝 Grassroots Volunteers:
                                    </label>
                                    <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                      {/* Quick Presets */}
                                      <div style={{ display: 'flex', gap: '4px' }}>
                                        {[10, 20, 25, 33, 50].map(pct => (
                                          <button
                                            key={pct}
                                            type="button"
                                            onClick={() => applyPresetPercent(rId, 'volunteers', pct)}
                                            style={{
                                              padding: '1px 5px',
                                              borderRadius: '3px',
                                              border: '1px solid rgba(192, 132, 252, 0.25)',
                                              backgroundColor: 'rgba(192, 132, 252, 0.08)',
                                              color: '#d8b4fe',
                                              fontSize: '8.5px',
                                              fontWeight: 800,
                                              cursor: 'pointer'
                                            }}
                                          >
                                            {pct}%
                                          </button>
                                        ))}
                                      </div>
                                      <span style={{ fontSize: '13px', fontWeight: 900, color: '#c084fc' }}>
                                        {currentVols.toLocaleString()}
                                      </span>
                                      <span style={{ fontSize: '9.5px', color: '#64748b' }}>
                                        ({totalStateVols > 0 ? ((currentVols / totalStateVols) * 100).toFixed(0) : 0}% of state pool)
                                      </span>
                                    </div>
                                  </div>
                                  <input
                                    type="range"
                                    min="0"
                                    max={totalStateVols || 10000}
                                    step="250"
                                    value={currentVols}
                                    onChange={(e) => {
                                      const val = parseInt(e.target.value) || 0;
                                      setRegionalAllocDrafts(prev => ({
                                        ...prev,
                                        [rId]: { ...(prev[rId] || {}), volunteers: val }
                                      }));
                                    }}
                                    style={{
                                      width: '100%',
                                      accentColor: '#c084fc',
                                      cursor: 'pointer'
                                    }}
                                  />
                                </div>
                              </div>

                              {/* Card Action Bar */}
                              <div style={{ display: 'flex', justifyContent: 'flex-end', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
                                <button
                                  disabled={actionLoading || isOverAllocated}
                                  onClick={handleSaveAllRegionalAllocations}
                                  style={{
                                    padding: '7px 18px',
                                    borderRadius: '7px',
                                    border: 'none',
                                    backgroundColor: isOverAllocated ? '#475569' : '#0284c7',
                                    color: '#ffffff',
                                    fontSize: '11.5px',
                                    fontWeight: 900,
                                    cursor: (actionLoading || isOverAllocated) ? 'not-allowed' : 'pointer',
                                    boxShadow: isOverAllocated ? 'none' : '0 2px 8px rgba(2, 132, 199, 0.35)'
                                  }}
                                >
                                  💾 Save & Deploy All {regionKeys.length} Regions
                                </button>
                              </div>
                            </div>
                          );
                        };

                        return (
                          <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
                            {/* ── TOP REGIONAL SELECTOR BAR & DROPDOWN ── */}
                            <div style={{
                              display: 'flex',
                              alignItems: 'center',
                              justifyContent: 'space-between',
                              flexWrap: 'wrap',
                              gap: '10px',
                              backgroundColor: 'rgba(15, 23, 42, 0.8)',
                              border: '1px solid rgba(56, 189, 248, 0.25)',
                              borderRadius: '10px',
                              padding: '10px 14px'
                            }}>
                              {/* Region Navigation Tabs / Pills */}
                              <div style={{
                                display: 'flex',
                                alignItems: 'center',
                                gap: '8px',
                                flexWrap: 'wrap',
                                flex: 1
                              }}>
                                <span style={{ fontSize: '11px', fontWeight: 900, color: '#38bdf8', textTransform: 'uppercase', letterSpacing: '0.04em', display: 'flex', alignItems: 'center', gap: '4px' }}>
                                  📍 Select Region:
                                </span>
                                {regionEntries.map(([rId, reg]) => {
                                  const isSelected = activeRegionId === rId && !viewAllRegions;
                                  const draft = regionalAllocDrafts[rId] || { workers: 0, volunteers: 0 };
                                  return (
                                    <button
                                      key={rId}
                                      type="button"
                                      onClick={() => {
                                        setSelectedRegionId(rId);
                                        setViewAllRegions(false);
                                      }}
                                      style={{
                                        padding: '6px 12px',
                                        borderRadius: '8px',
                                        border: isSelected ? '1.5px solid #38bdf8' : '1px solid rgba(255,255,255,0.1)',
                                        backgroundColor: isSelected ? 'rgba(56, 189, 248, 0.2)' : 'rgba(30, 41, 59, 0.6)',
                                        color: isSelected ? '#ffffff' : '#cbd5e1',
                                        cursor: 'pointer',
                                        display: 'inline-flex',
                                        alignItems: 'center',
                                        gap: '6px',
                                        transition: 'all 0.15s ease',
                                        boxShadow: isSelected ? '0 2px 10px rgba(56, 189, 248, 0.3)' : 'none'
                                      }}
                                    >
                                      <span style={{ fontSize: '11px', fontWeight: isSelected ? 900 : 700 }}>
                                        {reg.regionName.split('(')[0].trim()}
                                      </span>
                                      <span style={{
                                        fontSize: '8.5px',
                                        fontWeight: 800,
                                        padding: '1px 5px',
                                        borderRadius: '4px',
                                        backgroundColor: reg.supportPercentage >= 30 ? 'rgba(16, 185, 129, 0.25)' : 'rgba(56, 189, 248, 0.25)',
                                        color: reg.supportPercentage >= 30 ? '#34d399' : '#38bdf8'
                                      }}>
                                        {(reg.supportPercentage || 0).toFixed(0)}%
                                      </span>
                                    </button>
                                  );
                                })}
                              </div>

                              {/* Dropdown Selector & View Toggle */}
                              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                <select
                                  value={viewAllRegions ? 'ALL' : activeRegionId}
                                  onChange={(e) => {
                                    if (e.target.value === 'ALL') {
                                      setViewAllRegions(true);
                                    } else {
                                      setViewAllRegions(false);
                                      setSelectedRegionId(e.target.value);
                                    }
                                  }}
                                  style={{
                                    padding: '6px 12px',
                                    borderRadius: '7px',
                                    border: '1px solid rgba(56, 189, 248, 0.4)',
                                    backgroundColor: '#0f172a',
                                    color: '#38bdf8',
                                    fontSize: '11px',
                                    fontWeight: 800,
                                    cursor: 'pointer'
                                  }}
                                >
                                  {regionEntries.map(([rId, reg]) => (
                                    <option key={rId} value={rId}>
                                      {reg.regionName} ({reg.lokSabhaSeats} LS Seats)
                                    </option>
                                  ))}
                                  <option value="ALL">📜 View All Regions (Stacked)</option>
                                </select>

                                <button
                                  type="button"
                                  onClick={() => setViewAllRegions(prev => !prev)}
                                  style={{
                                    padding: '6px 10px',
                                    borderRadius: '7px',
                                    border: '1px solid rgba(255,255,255,0.15)',
                                    backgroundColor: viewAllRegions ? 'rgba(56, 189, 248, 0.15)' : 'rgba(15, 23, 42, 0.6)',
                                    color: viewAllRegions ? '#38bdf8' : '#94a3b8',
                                    fontSize: '10px',
                                    fontWeight: 800,
                                    cursor: 'pointer'
                                  }}
                                  title="Toggle between single focused region and all stacked regions"
                                >
                                  {viewAllRegions ? '📑 Focus Single Region' : '📜 View All'}
                                </button>
                              </div>
                            </div>

                            {/* ── REGIONAL CONTENT DISPLAY ── */}
                            {!viewAllRegions ? (
                              renderRegionCard(activeRegionId, stateObj.regions[activeRegionId], true)
                            ) : (
                              <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
                                {regionEntries.map(([rId, reg]) => renderRegionCard(rId, reg, false))}
                              </div>
                            )}
                          </div>
                        );
                      })() : (
                        <div style={{
                          padding: '30px',
                          textAlign: 'center',
                          backgroundColor: 'rgba(15, 23, 42, 0.6)',
                          borderRadius: '12px',
                          border: '1px dashed rgba(255,255,255,0.15)',
                          color: '#94a3b8',
                          fontSize: '12px'
                        }}>
                          No regional divisions calibrated for this state yet. Operations run on a state-wide consolidated pool.
                        </div>
                      )}
                    </div>
                  );
                })()}

                {/* ── MODAL: CONSTRUCT INFRASTRUCTURE & WINGS ── */}
                {buildingModalRegion && (
                  <div style={{
                    position: 'fixed',
                    top: 0,
                    left: 0,
                    right: 0,
                    bottom: 0,
                    backgroundColor: 'rgba(0, 0, 0, 0.75)',
                    zIndex: 1000,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    padding: '20px'
                  }}>
                    <div style={{
                      backgroundColor: '#0f172a',
                      border: '1.5px solid #38bdf8',
                      borderRadius: '16px',
                      width: '100%',
                      maxWidth: '820px',
                      maxHeight: '85vh',
                      overflowY: 'auto',
                      padding: '24px',
                      boxShadow: '0 20px 50px rgba(0,0,0,0.8)',
                      display: 'flex',
                      flexDirection: 'column',
                      gap: '18px'
                    }}>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <div>
                          <h4 style={{ margin: 0, fontSize: '17px', color: '#ffffff', fontWeight: 900 }}>
                            🛠️ Construct Infrastructure & Mobilize Frontal Wings
                          </h4>
                          <span style={{ fontSize: '11.5px', color: '#38bdf8' }}>
                            {buildCategoryFilter === 'HQ'
                              ? 'State Command HQ (State-Wide Command Centre)'
                              : `Target Region: ${stateObj?.regions?.[buildingModalRegion]?.regionName || buildingModalRegion || 'Regional Hub'}`}
                          </span>
                        </div>
                        <button
                          onClick={() => setBuildingModalRegion(null)}
                          style={{
                            background: 'none',
                            border: 'none',
                            color: '#94a3b8',
                            fontSize: '20px',
                            cursor: 'pointer'
                          }}
                        >
                          ✕
                        </button>
                      </div>

                      {/* Category Filter Pills */}
                      <div style={{ display: 'flex', gap: '8px' }}>
                        {[
                          { key: 'ALL', label: 'All Catalog' },
                          { key: 'HQ', label: '🏛️ HQ' },
                          { key: 'BUILDING', label: '🏢 Offices & Facilities' },
                          { key: 'WING', label: '🚩 Frontal Wings & Forums' }
                        ].map(c => (
                          <button
                            key={c.key}
                            onClick={() => setBuildCategoryFilter(c.key)}
                            style={{
                              padding: '6px 14px',
                              borderRadius: '8px',
                              border: buildCategoryFilter === c.key ? '1px solid #38bdf8' : '1px solid rgba(255,255,255,0.1)',
                              backgroundColor: buildCategoryFilter === c.key ? 'rgba(56, 189, 248, 0.2)' : 'rgba(15, 23, 42, 0.6)',
                              color: buildCategoryFilter === c.key ? '#ffffff' : '#94a3b8',
                              fontSize: '11px',
                              fontWeight: 700,
                              cursor: 'pointer'
                            }}
                          >
                            {c.label}
                          </button>
                        ))}
                      </div>

                      {/* Catalog Grid */}
                      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(340px, 1fr))', gap: '14px' }}>
                        {infraCatalog
                          .filter(item => {
                            const isStateScope = item.scope === 'STATE' || item.key === 'state_party_hq';
                            if (buildCategoryFilter === 'HQ') {
                              return isStateScope;
                            }
                            if (isStateScope) return false;
                            if (buildCategoryFilter !== 'ALL' && item.category !== buildCategoryFilter) return false;
                            return true;
                          })
                          .map(item => {
                            const isStateScope = item.scope === 'STATE' || item.key === 'state_party_hq';
                            const targetState = isStateScope ? stateObj?.buildings : (item.category === 'WING' ? stateObj?.regions?.[buildingModalRegion]?.wings : stateObj?.regions?.[buildingModalRegion]?.buildings);
                            const currentCount = targetState?.[item.key] || 0;
                            const isMax = currentCount >= item.maxAllowedPerScope;
                            const canAfford = (stateObj?.stateFunds || 0) >= item.costFunds;

                            return (
                              <div
                                key={item.key}
                                style={{
                                  backgroundColor: '#1e293b',
                                  border: isMax ? '1px solid rgba(255,255,255,0.06)' : '1px solid rgba(56, 189, 248, 0.2)',
                                  borderRadius: '10px',
                                  padding: '16px',
                                  display: 'flex',
                                  flexDirection: 'column',
                                  justifyContent: 'space-between',
                                  gap: '12px'
                                }}
                              >
                                <div>
                                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '6px' }}>
                                    <span style={{ fontSize: '13.5px', fontWeight: 800, color: '#ffffff' }}>
                                      {item.icon} {item.name}
                                    </span>
                                    <span style={{
                                      fontSize: '9px',
                                      fontWeight: 800,
                                      padding: '2px 6px',
                                      borderRadius: '4px',
                                      backgroundColor: isMax ? 'rgba(239, 68, 68, 0.2)' : 'rgba(16, 185, 129, 0.2)',
                                      color: isMax ? '#fca5a5' : '#6ee7b7'
                                    }}>
                                      {currentCount} / {item.maxAllowedPerScope} Built
                                    </span>
                                  </div>

                                  <p style={{ margin: '0 0 10px', fontSize: '11px', color: '#cbd5e1', lineHeight: 1.4 }}>
                                    {item.description}
                                  </p>

                                  {/* Cost & Monthly Relative Yield Specs */}
                                  <div style={{
                                    backgroundColor: 'rgba(15, 23, 42, 0.6)',
                                    borderRadius: '6px',
                                    padding: '8px 10px',
                                    display: 'flex',
                                    flexDirection: 'column',
                                    gap: '4px',
                                    fontSize: '10px'
                                  }}>
                                    <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                                      <span style={{ color: '#94a3b8' }}>Construction Cost:</span>
                                      <strong style={{ color: '#fbbf24' }}>
                                        ₹{item.costFunds} Cr
                                      </strong>
                                    </div>
                                    <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                                      <span style={{ color: '#94a3b8' }}>Cash Yield / Season:</span>
                                      <strong style={{ color: '#34d399' }}>
                                        +₹{item.monthlyCashOutput} Cr
                                      </strong>
                                    </div>
                                    <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                                      <span style={{ color: '#94a3b8' }}>Growth Yield / Season:</span>
                                      <strong style={{ color: '#7dd3fc' }}>
                                        {item.workersPercentMonthly > 0 ? `+${item.workersPercentMonthly}% cadres ` : ''}
                                        {item.volunteersPercentMonthly > 0 ? `+${item.volunteersPercentMonthly}% vols ` : ''}
                                        {item.donorsPercentMonthly > 0 ? `+${item.donorsPercentMonthly}% donors` : ''}
                                      </strong>
                                    </div>
                                    {item.instantSupportBonus > 0 && (
                                      <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                                        <span style={{ color: '#94a3b8' }}>Instant Stance Gain:</span>
                                        <strong style={{ color: '#38bdf8' }}>
                                          +{item.instantSupportBonus}% (one-time on build)
                                        </strong>
                                      </div>
                                    )}
                                    {item.monthlySupportBonus > 0 && (
                                      <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                                        <span style={{ color: '#94a3b8' }}>Recurring Ground Gain:</span>
                                        <strong style={{ color: '#a78bfa' }}>
                                          +{item.monthlySupportBonus}% (each season)
                                        </strong>
                                      </div>
                                    )}
                                  </div>
                                </div>

                                <button
                                  disabled={actionLoading || isMax || !canAfford}
                                  onClick={() => handleBuildInfra(item.key, isStateScope ? null : buildingModalRegion)}
                                  style={{
                                    padding: '8px 14px',
                                    borderRadius: '6px',
                                    border: 'none',
                                    backgroundColor: isMax ? '#334155' : !canAfford ? '#475569' : '#0284c7',
                                    color: isMax || !canAfford ? '#94a3b8' : '#ffffff',
                                    fontWeight: 800,
                                    fontSize: '11px',
                                    cursor: isMax || !canAfford ? 'not-allowed' : 'pointer',
                                    transition: 'all 0.2s'
                                  }}
                                >
                                  {isMax ? 'Maximum Reached' : !canAfford ? 'Insufficient State Treasury Funds' : 'Build →'}
                                </button>
                              </div>
                            );
                          })}
                      </div>
                    </div>
                  </div>
                )}
              </div>
            )}

            {/* ── 4. POLLING & SEAT PROJECTIONS ── */}
            {subTab === 'polling' && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <h3 style={{ margin: 0, fontSize: '15px', color: '#ffffff' }}>
                    📊 State Vote Splits & Lok Sabha Seat Projections
                  </h3>
                  <span style={{ fontSize: '11px', color: '#38bdf8' }}>
                    Simulated popular opinion
                  </span>
                </div>

                {/* Election Result Banner if election happened */}
                {stateObj?.lastElectionResult && (
                  <div style={{
                    padding: '18px',
                    borderRadius: '12px',
                    backgroundColor: stateObj.lastElectionResult.isPlayerVictory ? 'rgba(16, 185, 129, 0.15)' : 'rgba(239, 68, 68, 0.15)',
                    border: stateObj.lastElectionResult.isPlayerVictory ? '2px solid #10b981' : '2px solid #ef4444'
                  }}>
                    <h4 style={{ margin: 0, fontSize: '16px', color: stateObj.lastElectionResult.isPlayerVictory ? '#34d399' : '#f87171', fontWeight: 900 }}>
                      🗳️ {stateObj.lastElectionResult.headline}
                    </h4>
                    <p style={{ margin: '6px 0 0', fontSize: '12px', color: '#cbd5e1' }}>
                      Assembly Seats Won: {Object.entries(stateObj.lastElectionResult.assemblySeats || {}).map(([p, s]) => `${p}: ${s}`).join(' • ')}
                    </p>
                    <div style={{ marginTop: '8px', fontSize: '11px', color: '#94a3b8' }}>
                      National Morale Impact: <strong style={{ color: stateObj.lastElectionResult.moraleChange >= 0 ? '#34d399' : '#ef4444' }}>
                        {stateObj.lastElectionResult.moraleChange >= 0 ? `+${stateObj.lastElectionResult.moraleChange}` : stateObj.lastElectionResult.moraleChange}
                      </strong>
                    </div>
                  </div>
                )}

                {/* Vote Share Bars */}
                <div style={{
                  backgroundColor: 'rgba(15, 23, 42, 0.8)',
                  border: '1px solid rgba(255,255,255,0.08)',
                  borderRadius: '12px',
                  padding: '20px',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '12px'
                }}>
                  <h4 style={{ margin: 0, fontSize: '13px', color: '#ffffff', fontWeight: 800 }}>
                    Popular Vote Share Breakdown (%):
                  </h4>

                  {Object.entries(stateObj?.voteSplits || {}).map(([party, votePct]) => {
                    const isPlayer = party.toUpperCase() === playerKey;
                    const isUndecided = party.toUpperCase() === 'UNDECIDED';
                    const barColor = isPlayer ? '#7C3AED' : isUndecided ? '#64748b' : '#0284c7';

                    return (
                      <div key={party} style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11.5px' }}>
                          <span style={{ fontWeight: 800, color: isPlayer ? '#c084fc' : isUndecided ? '#94a3b8' : '#ffffff' }}>
                            {party} {isPlayer && '(Your Party)'}
                          </span>
                          <span style={{ fontWeight: 900, color: isPlayer ? '#c084fc' : isUndecided ? '#94a3b8' : '#ffffff' }}>
                            {votePct}%
                          </span>
                        </div>
                        <div style={{ width: '100%', height: '8px', backgroundColor: 'rgba(255,255,255,0.06)', borderRadius: '4px', overflow: 'hidden' }}>
                          <div style={{
                            width: `${Math.min(100, Math.max(0, votePct))}%`,
                            height: '100%',
                            backgroundColor: barColor,
                            transition: 'width 0.4s ease'
                          }} />
                        </div>
                      </div>
                    );
                  })}
                </div>

                {/* Projected Lok Sabha Seats */}
                <div style={{
                  backgroundColor: 'rgba(15, 23, 42, 0.8)',
                  border: '1px solid rgba(56, 189, 248, 0.25)',
                  borderRadius: '12px',
                  padding: '20px',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '12px'
                }}>
                  <h4 style={{ margin: 0, fontSize: '13px', color: '#38bdf8', fontWeight: 800 }}>
                    Projected Lok Sabha Seats (Out of {stateObj?.totalLokSabhaSeats}):
                  </h4>

                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(140px, 1fr))', gap: '10px' }}>
                    {Object.entries(stateObj?.projectedLokSabhaSeats || {}).map(([p, seats]) => (
                      <div key={p} style={{
                        padding: '12px',
                        borderRadius: '8px',
                        backgroundColor: p === playerKey ? 'rgba(124, 58, 237, 0.25)' : 'rgba(30, 41, 59, 0.6)',
                        border: p === playerKey ? '1.5px solid #a855f7' : '1px solid rgba(255,255,255,0.08)',
                        textAlign: 'center'
                      }}>
                        <div style={{ fontSize: '11px', color: '#94a3b8' }}>{p}</div>
                        <div style={{ fontSize: '20px', fontWeight: 900, color: p === playerKey ? '#c084fc' : '#ffffff', marginTop: '2px' }}>
                          {seats}
                        </div>
                        <div style={{ fontSize: '9px', color: '#64748b' }}>Projected MPs</div>
                      </div>
                    ))}
                  </div>
                </div>

                {/* ── State Party Campaign & Intelligence Activity Log ── */}
                <div style={{
                  backgroundColor: 'rgba(15, 23, 42, 0.85)',
                  border: '1px solid rgba(56, 189, 248, 0.2)',
                  borderRadius: '12px',
                  padding: '20px',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '12px'
                }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
                    <div>
                      <h4 style={{ margin: 0, fontSize: '13px', color: '#ffffff', fontWeight: 800, display: 'flex', alignItems: 'center', gap: '6px' }}>
                        <span>📋</span> State Campaign &amp; Party Activity Intelligence Feed
                      </h4>
                      <p style={{ margin: '2px 0 0', fontSize: '10px', color: '#94a3b8' }}>
                        Real-time intelligence on actions taken by your party, BJP, Congress, and regional rivals in {stateObj?.stateName}.
                      </p>
                    </div>
                    <span style={{
                      backgroundColor: 'rgba(56, 189, 248, 0.15)',
                      border: '1px solid rgba(56, 189, 248, 0.3)',
                      color: '#38bdf8',
                      fontSize: '9.5px',
                      fontWeight: 800,
                      padding: '2px 8px',
                      borderRadius: '6px'
                    }}>
                      {(stateObj?.activityLog || []).length} Log Entries
                    </span>
                  </div>

                  {(!stateObj?.activityLog || stateObj.activityLog.length === 0) ? (
                    <div style={{
                      padding: '16px',
                      textAlign: 'center',
                      backgroundColor: 'rgba(255,255,255,0.02)',
                      borderRadius: '8px',
                      color: '#64748b',
                      fontSize: '11px'
                    }}>
                      No campaign activities logged for this state yet. Actions and AI party counter-measures will be logged at the end of each turn.
                    </div>
                  ) : (
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', maxHeight: '220px', overflowY: 'auto', paddingRight: '4px' }}>
                      {stateObj.activityLog.map((entry, idx) => {
                        const isAi = entry.event === 'AI_CAMPAIGN';
                        const isPlayer = entry.event === 'PLAYER_ACTION';
                        const isElection = entry.event === 'ELECTION_RESOLVED';

                        const borderColor = isElection ? '#f59e0b' : isAi ? '#ec4899' : isPlayer ? '#10b981' : '#64748b';
                        const badgeColor = isElection ? '#f59e0b' : isAi ? '#f472b6' : isPlayer ? '#34d399' : '#94a3b8';
                        const badgeBg = isElection ? 'rgba(245, 158, 11, 0.15)' : isAi ? 'rgba(236, 72, 153, 0.15)' : isPlayer ? 'rgba(16, 185, 129, 0.15)' : 'rgba(100, 116, 139, 0.15)';
                        const icon = isElection ? '🗳️' : isAi ? '🤖' : isPlayer ? '🏛️' : '⏭️';

                        return (
                          <div
                            key={idx}
                            style={{
                              display: 'flex',
                              gap: '10px',
                              alignItems: 'flex-start',
                              fontSize: '11px',
                              padding: '8px 12px',
                              backgroundColor: 'rgba(255,255,255,0.03)',
                              borderRadius: '8px',
                              borderLeft: `3px solid ${borderColor}`
                            }}
                          >
                            <span style={{ fontSize: '13px', flexShrink: 0 }}>{icon}</span>
                            <div style={{ flex: 1 }}>
                              <div style={{ display: 'flex', gap: '8px', alignItems: 'center', marginBottom: '2px' }}>
                                <span style={{
                                  backgroundColor: badgeBg,
                                  color: badgeColor,
                                  fontSize: '8.5px',
                                  fontWeight: 800,
                                  padding: '1px 5px',
                                  borderRadius: '3px'
                                }}>
                                  Season {entry.season}
                                </span>
                                <span style={{ fontSize: '9px', color: '#64748b' }}>
                                  {entry.event?.replace('_', ' ')}
                                </span>
                              </div>
                              <span style={{ color: '#e2e8f0', lineHeight: 1.4 }}>
                                {entry.detail}
                              </span>
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  )}
                </div>
              </div>
            )}

            {/* ── 5. CAMPAIGN PUSH SPECIAL ACTIONS (Unlocked in Campaign/Sprint Phase) ── */}
            {isCampaignPhase && (
              <div style={{
                marginTop: '24px',
                background: 'linear-gradient(135deg, rgba(234, 88, 12, 0.15) 0%, rgba(220, 38, 38, 0.15) 100%)',
                border: '1.5px solid #f97316',
                borderRadius: '12px',
                padding: '20px',
                display: 'flex',
                flexDirection: 'column',
                gap: '14px'
              }}>
                <div>
                  <h4 style={{ margin: 0, fontSize: '15px', color: '#fb923c', fontWeight: 900, display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <span>🚀</span> Election Campaign Push (Sprint Actions Unlocked!)
                  </h4>
                  <p style={{ margin: '4px 0 0', fontSize: '11.5px', color: '#fed7aa' }}>
                    Elections are approaching within {stateObj?.turnsToElection} turns! High-impact sprint actions can convert undecided voters.
                  </p>
                </div>

                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '12px' }}>
                  <div style={{ padding: '12px', backgroundColor: 'rgba(15, 23, 42, 0.7)', borderRadius: '8px', border: '1px solid rgba(249, 115, 22, 0.3)', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', gap: '8px' }}>
                    <div>
                      <strong style={{ color: '#ffffff', fontSize: '13px' }}>🎪 Mega Rally</strong>
                      <p style={{ fontSize: '10.5px', color: '#cbd5e1', margin: '4px 0' }}>Massive stadium address. +3.5% support, +5000 volunteers.</p>
                      <span style={{ fontSize: '10px', color: '#f59e0b' }}>Cost: ₹5.0 Cr</span>
                    </div>
                    <button
                      onClick={() => handleCampaignPush('MEGA_RALLY')}
                      disabled={actionLoading || stateObj?.stateFunds < 5.0}
                      style={{ padding: '6px', borderRadius: '6px', border: 'none', backgroundColor: '#ea580c', color: '#fff', fontWeight: 800, fontSize: '11px', cursor: 'pointer' }}
                    >
                      Stage Mega Rally
                    </button>
                  </div>

                  <div style={{ padding: '12px', backgroundColor: 'rgba(15, 23, 42, 0.7)', borderRadius: '8px', border: '1px solid rgba(249, 115, 22, 0.3)', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', gap: '8px' }}>
                    <div>
                      <strong style={{ color: '#ffffff', fontSize: '13px' }}>📺 Media Ad Blitz</strong>
                      <p style={{ fontSize: '10.5px', color: '#cbd5e1', margin: '4px 0' }}>TV and newspaper front-page saturation. +2.2% support.</p>
                      <span style={{ fontSize: '10px', color: '#f59e0b' }}>Cost: ₹3.0 Cr</span>
                    </div>
                    <button
                      onClick={() => handleCampaignPush('AD_BLITZ')}
                      disabled={actionLoading || stateObj?.stateFunds < 3.0}
                      style={{ padding: '6px', borderRadius: '6px', border: 'none', backgroundColor: '#ea580c', color: '#fff', fontWeight: 800, fontSize: '11px', cursor: 'pointer' }}
                    >
                      Launch Ad Blitz
                    </button>
                  </div>

                  <div style={{ padding: '12px', backgroundColor: 'rgba(15, 23, 42, 0.7)', borderRadius: '8px', border: '1px solid rgba(249, 115, 22, 0.3)', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', gap: '8px' }}>
                    <div>
                      <strong style={{ color: '#ffffff', fontSize: '13px' }}>👤 National Leader Visit</strong>
                      <p style={{ fontSize: '10.5px', color: '#cbd5e1', margin: '4px 0' }}>Prime leadership rallies in state. +2.0% support, +5 Morale.</p>
                      <span style={{ fontSize: '10px', color: '#f59e0b' }}>Cost: ₹2.0 Cr</span>
                    </div>
                    <button
                      onClick={() => handleCampaignPush('LEADER_VISIT')}
                      disabled={actionLoading || stateObj?.stateFunds < 2.0}
                      style={{ padding: '6px', borderRadius: '6px', border: 'none', backgroundColor: '#ea580c', color: '#fff', fontWeight: 800, fontSize: '11px', cursor: 'pointer' }}
                    >
                      Host Leader Visit
                    </button>
                  </div>

                  <div style={{ padding: '12px', backgroundColor: 'rgba(15, 23, 42, 0.7)', borderRadius: '8px', border: '1px solid rgba(249, 115, 22, 0.3)', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', gap: '8px' }}>
                    <div>
                      <strong style={{ color: '#ffffff', fontSize: '13px' }}>🚶 Voter Contact Drive</strong>
                      <p style={{ fontSize: '10.5px', color: '#cbd5e1', margin: '4px 0' }}>Door-to-door booth outreach. +1.6% support.</p>
                      <span style={{ fontSize: '10px', color: '#38bdf8' }}>Requires: 100 Workers & 200 Vols</span>
                    </div>
                    <button
                      onClick={() => handleCampaignPush('VOTER_CONTACT')}
                      disabled={actionLoading}
                      style={{ padding: '6px', borderRadius: '6px', border: 'none', backgroundColor: '#0284c7', color: '#fff', fontWeight: 800, fontSize: '11px', cursor: 'pointer' }}
                    >
                      Start Voter Drive
                    </button>
                  </div>
                </div>
              </div>
            )}
          </>
        )}
      </div>

      {/* ── STICKY FOOTER ACTION BAR ── */}
      <div style={{
        backgroundColor: '#0d1527',
        borderTop: '1px solid rgba(56, 189, 248, 0.2)',
        padding: '12px 24px',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        flexWrap: 'wrap',
        gap: '12px',
        zIndex: 10
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '14px', fontSize: '11.5px', flexWrap: 'wrap' }}>
          <span style={{ color: '#94a3b8', fontWeight: 700 }}>Directives Checklist:</span>
          <span style={{
            color: isNewsDone ? '#34d399' : '#f59e0b',
            fontWeight: 700,
            display: 'flex',
            alignItems: 'center',
            gap: '4px'
          }}>
            {isNewsDone ? '✅ News Reaction Committed' : '⚠️ News Reaction Pending'}
          </span>
          <span style={{ color: 'rgba(255,255,255,0.2)' }}>•</span>
          <span style={{
            color: isIssueDone ? '#34d399' : '#f59e0b',
            fontWeight: 700,
            display: 'flex',
            alignItems: 'center',
            gap: '4px'
          }}>
            {isIssueDone ? '✅ Policy Action Deployed' : '⚠️ Tactical Issue Action Pending'}
          </span>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <button
            onClick={onClose}
            style={{
              backgroundColor: 'rgba(255, 255, 255, 0.06)',
              border: '1px solid rgba(255, 255, 255, 0.15)',
              color: '#cbd5e1',
              borderRadius: '8px',
              padding: '8px 16px',
              fontSize: '12px',
              fontWeight: 700,
              cursor: 'pointer'
            }}
          >
            Cancel / Close
          </button>
          <button
            onClick={handleDoneOrSave}
            disabled={actionLoading}
            style={{
              backgroundColor: isAllTasksCompleted ? '#10b981' : '#2563eb',
              border: 'none',
              color: '#ffffff',
              borderRadius: '8px',
              padding: '8px 22px',
              fontSize: '12px',
              fontWeight: 900,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              boxShadow: isAllTasksCompleted ? '0 0 14px rgba(16, 185, 129, 0.45)' : 'none',
              transition: 'all 0.2s ease'
            }}
          >
            {isAllTasksCompleted ? '✓ Done' : '💾 Save & Exit'}
          </button>
        </div>
      </div>
    </div>
  );
}
