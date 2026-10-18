/**
 * hintEngine.js
 * Dynamic AI Tactical & Strategy Advisor Engine for National Political War Room.
 * Evaluates live game state, election schedules, treasury reserves,
 * alliance status, and state-level battlegrounds to generate actionable recommendations.
 */

export function generateStrategicHints(activeGame, configData) {
  if (!activeGame) return null;

  // 1. Authoritative Backend Dynamic AI Strategy Engine Integration
  if (activeGame.strategicHints && activeGame.strategicHints.summary) {
    const backendHints = activeGame.strategicHints;
    const summary = backendHints.summary || {};
    const actions = backendHints.actions || {};
    const rankedStates = backendHints.rankedStates || [];
    const urgentWarnings = backendHints.urgentWarnings || [];

    const coalitionAction = actions.coalition || {};
    const financeAction = actions.finance || {};
    const eventsAction = actions.events || {};
    const statesAction = actions.states || {};

    return {
      source: 'BACKEND_AI_ENGINE',
      urgentWarnings,
      moraleStatus: summary.moraleStatus || null,
      treasuryStatus: summary.treasuryStatus || null,
      actions,
      rankedStates,
      executiveSummary: {
        currentSeason: summary.currentSeason || activeGame.currentSeason || 1,
        strategicPhase: summary.strategicPhase || 'FOUNDATION',
        phaseTitle: summary.phaseTitle || 'Phase 1: Grassroots Foundation',
        topObjective: summary.topObjective || '',
        totalAllianceSeats: summary.totalAllianceSeats || 0,
        majorityGap: summary.majorityGap !== undefined ? summary.majorityGap : 272,
        hasMajority: Boolean(summary.hasMajority),
        doneCount: summary.doneCount || 0,
        isAllFourDone: Boolean(summary.isAllFourDone)
      },
      coalitionGuide: {
        isComplete: Boolean(coalitionAction.isDone),
        statusBadge: coalitionAction.badge || (coalitionAction.isDone ? 'COMPLETED ✓' : 'PENDING ⚠️'),
        badgeColor: coalitionAction.badgeColor || '#38bdf8',
        hasAlliance: coalitionAction.badge !== 'NO FRONT FORMED ⚠️',
        cabinetLeft: coalitionAction.cabinetLeft ?? 20,
        stateLeft: coalitionAction.stateLeft ?? 50,
        topRecruitTarget: coalitionAction.targetParty || null,
        recommendation: coalitionAction.recommendation || '',
        actionTip: coalitionAction.actionTip || ''
      },
      financeGuide: {
        isComplete: Boolean(financeAction.isDone),
        statusBadge: financeAction.badge || (financeAction.isDone ? 'COMMITTED ✓' : 'ACTION PENDING ⏳'),
        badgeColor: financeAction.badgeColor || '#fbbf24',
        posture: financeAction.posture || 'BALANCED',
        recommendation: financeAction.recommendation || '',
        cardHint: financeAction.actionTip || ''
      },
      eventsGuide: {
        isComplete: Boolean(eventsAction.isDone),
        statusBadge: eventsAction.badge || (eventsAction.isDone ? 'RESOLVED ✓' : 'PENDING ⏳'),
        badgeColor: eventsAction.badgeColor || '#38bdf8',
        pendingCount: eventsAction.pendingCount || 0,
        recommendation: eventsAction.recommendation || '',
        actionTip: eventsAction.actionTip || '',
        targetPartyTip: eventsAction.targetPartyTip || '',
        mediaSocialTip: eventsAction.mediaSocialTip || ''
      },
      stateGuide: {
        isComplete: Boolean(statesAction.isDone),
        statusBadge: statesAction.badge || (statesAction.isDone ? 'ALL STATES DONE ✓' : 'OPERATIONS PENDING ⏳'),
        badgeColor: statesAction.badgeColor || '#10b981',
        hasNotPlayedAnyStates: Boolean(statesAction.hasNotPlayedAnyStates),
        recommendation: statesAction.recommendation || '',
        actionTip: statesAction.actionTip || '',
        topPriorityState: rankedStates[0] || null,
        allStates: rankedStates
      }
    };
  }

  // 2. Client-side Fallback if backend hints are initializing
  const currentSeason = activeGame.currentSeason || 1;
  const era = activeGame.era || 2001;
  const playerPartyKey = (activeGame.partyKey || 'ydp').toLowerCase();
  const playerPartyKeyUpper = playerPartyKey.toUpperCase();

  const partyStates = activeGame.partyStates || [];
  const playerState = partyStates.find(
    p => (p.partyKey || p.id || '').toLowerCase() === playerPartyKey
  ) || null;

  const currentFunds = playerState?.funds ?? activeGame.playerFunds ?? 15.0;
  const currentMorale = playerState?.morale ?? activeGame.morale ?? 70;
  const currentCorruption = playerState?.corruption ?? activeGame.playerCorruption ?? 0;
  const currentWorkers = playerState?.workers ?? 50000;
  const currentVolunteers = playerState?.volunteers ?? 15000;
  const currentDonors = playerState?.donors ?? 1000;
  const initialSeats = playerState?.seats ?? activeGame.seats ?? 0;
  const projSeats = activeGame.nationalProjectedSeats?.[playerPartyKeyUpper] ?? initialSeats;

  // ── 1. ALLIANCE & MAJORITY EVALUATION ──────────────────────────────────────
  const alliances = activeGame.alliances || [];
  const playerAlliance = alliances.find(a =>
    (a.leaderPartyKey || '').toLowerCase() === playerPartyKey ||
    (a.members && a.members.some(m => (m.partyKey || '').toLowerCase() === playerPartyKey))
  ) || null;

  const isAllianceLeader = playerAlliance && (playerAlliance.leaderPartyKey || '').toLowerCase() === playerPartyKey;
  
  // Calculate total alliance seats (projected or actual)
  let totalAllianceSeats = projSeats;
  if (playerAlliance && playerAlliance.members) {
    const memberKeys = Array.from(new Set([
      playerAlliance.leaderPartyKey,
      ...playerAlliance.members.map(m => m.partyKey)
    ].filter(Boolean)));

    totalAllianceSeats = memberKeys.reduce((sum, pk) => {
      const pkUpper = pk.toUpperCase();
      if (activeGame.nationalProjectedSeats?.[pkUpper] !== undefined) {
        return sum + activeGame.nationalProjectedSeats[pkUpper];
      }
      const p = partyStates.find(ps => (ps.partyKey || ps.id || '').toLowerCase() === pk.toLowerCase());
      return sum + (p?.seats || 0);
    }, 0);
  }

  const majorityGap = Math.max(0, 272 - totalAllianceSeats);
  const hasMajority = totalAllianceSeats >= 272;

  // ── 2. EXECUTIVE SUMMARY & STRATEGIC PRIORITY ──────────────────────────────
  let strategicPhase = 'FOUNDATION';
  let phaseTitle = 'Phase 1: Grassroots Foundation';
  if (currentSeason > 40 || majorityGap <= 30) {
    strategicPhase = 'ENDGAME';
    phaseTitle = 'Phase 3: Endgame & 272 Threshold';
  } else if (currentSeason > 15) {
    strategicPhase = 'EXPANSION';
    phaseTitle = 'Phase 2: Regional Expansion';
  }

  let topObjective = '';
  if (hasMajority) {
    topObjective = 'Majority Secured! You have crossed 272 projected seats. Maintain coalition morale and consider calling a No-Confidence Motion to trigger early victory.';
  } else if (!playerAlliance) {
    topObjective = `Form a coalition front immediately. Without alliance partners, you cannot bridge the ${majorityGap} seat gap to the 272 majority threshold.`;
  } else if (majorityGap > 100) {
    topObjective = `Expand alliance front into key battlegrounds. Recruit high-seat regional parties in UP, Bihar, and Maharashtra to close the ${majorityGap}-seat deficit.`;
  } else {
    topObjective = `Final sprint to power: Only ${majorityGap} more seats required to reach 272. Target upcoming state assembly polls to swing critical battleground seats.`;
  }

  // ── 3. ACTION 1: COALITION FRONT STRATEGY ──────────────────────────────────
  const cabinetUsed = playerAlliance?.totalCabinetPromised || 0;
  const stateUsed = playerAlliance?.totalStatePromised || 0;
  const cabinetLeft = Math.max(0, 20 - cabinetUsed);
  const stateLeft = Math.max(0, 50 - stateUsed);

  // Find promising unaligned parties to invite
  const unalignedParties = partyStates.filter(p => {
    const pk = (p.partyKey || p.id || '').toLowerCase();
    if (pk === playerPartyKey) return false;
    if (playerAlliance?.members?.some(m => (m.partyKey || '').toLowerCase() === pk)) return false;
    // Exclude major rival alliance leaders (BJP, INC)
    if (pk === 'bjp' || pk === 'inc') return false;
    return true;
  });

  // Sort by projected seats descending, then low morale (desperate parties are cheaper to recruit)
  unalignedParties.sort((a, b) => {
    const aSeats = activeGame.nationalProjectedSeats?.[(a.partyKey || '').toUpperCase()] ?? a.seats ?? 0;
    const bSeats = activeGame.nationalProjectedSeats?.[(b.partyKey || '').toUpperCase()] ?? b.seats ?? 0;
    if (bSeats !== aSeats) return bSeats - aSeats;
    return (a.morale || 70) - (b.morale || 70);
  });

  const topRecruitTarget = unalignedParties[0] || null;
  const targetProjSeats = topRecruitTarget
    ? (activeGame.nationalProjectedSeats?.[(topRecruitTarget.partyKey || '').toUpperCase()] ?? topRecruitTarget.seats ?? 0)
    : 0;

  let coalitionRecommendation = '';
  let coalitionActionTip = '';

  if (!playerAlliance) {
    coalitionRecommendation = `Create a new Coalition Front (e.g. "National Progressive Front") and invite ${topRecruitTarget?.partyName || 'regional allies'} (+${targetProjSeats} seats).`;
    coalitionActionTip = `Offer 2 Cabinet Ministers, 4 State Ministers, and ₹${Math.min(3.0, (currentFunds * 0.15)).toFixed(1)} Cr joining bonus.`;
  } else if (isAllianceLeader) {
    if (majorityGap <= 0) {
      coalitionRecommendation = 'Your Coalition Front controls 272+ projected seats. Review member contracts to ensure zero breaches, then click "Confirm Front Strategy".';
      coalitionActionTip = 'All portfolios are secured. Save capital for state election ground campaigns.';
    } else if (cabinetLeft >= 2 && topRecruitTarget) {
      coalitionRecommendation = `Invite ${topRecruitTarget.partyName || topRecruitTarget.partyKey.toUpperCase()} (${targetProjSeats} Projected Seats). You have ${cabinetLeft} Cabinet & ${stateLeft} State ministerial slots remaining.`;
      const offerBonus = currentFunds > 30 ? '₹2.5 Cr' : '₹1.0 Cr';
      coalitionActionTip = `Recommended Contract: 2 Cabinet Ministers, 3 State Ministers, ${offerBonus} joining bonus.`;
    } else {
      coalitionRecommendation = 'Cabinet minister quota is nearly exhausted. Maintain existing partner contracts and click "Confirm Front Strategy" to lock in current alliance bonuses.';
      coalitionActionTip = 'Do not promise beyond 20 Cabinet slots or coalition partners will breach with severe morale backlash.';
    }
  } else {
    coalitionRecommendation = `You are a member party of ${playerAlliance.allianceName}. Fulfill alliance agreements and coordinate with the leadership front.`;
    coalitionActionTip = 'Confirm front strategy to receive recurring federal aid and shared rally momentum.';
  }

  // ── 4. ACTION 2: FINANCE & TREASURY STRATEGY ───────────────────────────────
  const greedHeat = activeGame.megaFinanceHeat || 0;
  let financePosture = 'BALANCED';
  let financeRecommendation = '';
  let financeCardHint = '';

  if (greedHeat >= 3 || currentCorruption > 35) {
    financePosture = 'COOL_DOWN';
    financeRecommendation = 'High Corruption / Media Scrutiny Alert! Cadres are restless and journalists are probing corporate ties.';
    financeCardHint = 'Select "Grassroots Micro-Donation Drive" or "Campus Union Collection". Avoid Mega-Corporate Cards to lower scrutiny heat and restore party morale.';
  } else if (currentFunds < 22.0) {
    financePosture = 'CAPITAL_INFLOW';
    financeRecommendation = `Treasury is running low (₹${currentFunds.toFixed(1)} Cr). You need funds to finance state operations and infrastructure building.`;
    financeCardHint = 'Select a high-yield financing operation such as "Corporate Dinner" or "Diaspora Fundraiser" to inject ₹12-18 Cr into party reserves.';
  } else if (currentMorale < 55) {
    financePosture = 'CADRE_MORALE';
    financeRecommendation = `Cadre morale has dropped to ${currentMorale}%. Low morale penalizes voting swings across all state battlegrounds.`;
    financeCardHint = 'Select worker-centric funding cards that offer morale bonuses and volunteer surges over raw cash.';
  } else {
    financePosture = 'BALANCED';
    financeRecommendation = `Treasury is stable at ₹${currentFunds.toFixed(1)} Cr with low corruption (${currentCorruption}%).`;
    financeCardHint = 'Choose balanced strategy cards like "Party Subscription Drive" or "SME Chamber Summit" to steadily grow cadres and funds simultaneously.';
  }

  // ── 5. ACTION 3: NATIONAL EVENTS & ISSUES STRATEGY ─────────────────────────
  const activeEventIds = activeGame.currentSeasonEventIds || [];
  const resolvedEventCount = Object.keys(activeGame.resolvedEventReactions || {}).length;
  const pendingEventsCount = Math.max(0, activeEventIds.length - resolvedEventCount);

  let eventsRecommendation = '';
  let eventsActionTip = '';

  if (pendingEventsCount > 0) {
    eventsRecommendation = `${pendingEventsCount} National Event Reaction${pendingEventsCount > 1 ? 's are' : ' is'} awaiting your response.`;
    eventsActionTip = 'Choose options that maximize Public Support and Cadre Morale while keeping Corruption Risk under 20%. Reject bribe or kickback options.';
  } else if (activeGame.activeThemeKey) {
    eventsRecommendation = `Active National Narrative: "${activeGame.activeThemeKey.replace(/_/g, ' ')}".`;
    eventsActionTip = 'Trigger the Theme Action to maintain narrative momentum streak (+15% national rally swing bonus).';
  } else {
    eventsRecommendation = 'No urgent national crises this turn. National public opinion is calm.';
    eventsActionTip = 'Use this window of stability to push grassroots volunteer drives and consolidate state positions.';
  }

  // ── 6. ACTION 4: STATE-LEVEL BATTLEGROUND STRATEGY ────────────────────────
  const stateOps = activeGame.stateOperations || {};
  const stateList = Object.values(stateOps);

  // Score each state for urgency
  const rankedStates = stateList.map(st => {
    const turns = st.turnsToElection !== undefined ? st.turnsToElection : 99;
    const seats = st.totalLokSabhaSeats || 20;
    const funds = st.stateFunds || 0;
    const workers = st.stateWorkers || 0;

    let urgencyScore = 0;
    let urgencyBadge = 'NORMAL';
    let urgencyColor = '#94a3b8';

    if (turns <= 3) {
      urgencyScore += 100;
      urgencyBadge = 'FINAL SPRINT ⚡';
      urgencyColor = '#ef4444';
    } else if (turns <= 6) {
      urgencyScore += 60;
      urgencyBadge = 'CAMPAIGN ⚔️';
      urgencyColor = '#f59e0b';
    } else if (turns <= 12) {
      urgencyScore += 30;
      urgencyBadge = 'PRE-ELECTION 🗓️';
      urgencyColor = '#38bdf8';
    }

    // Weight by Lok Sabha seats
    urgencyScore += seats * 0.8;

    // Deficit penalties (states that urgently need resources)
    if (funds < 1.5) urgencyScore += 15;
    if (workers < 10000) urgencyScore += 10;

    // Dynamic resource transfer calculations
    const safeHqReserve = 15.0; // Keep at least 15 Cr at HQ
    const availableHqFunds = Math.max(0, currentFunds - safeHqReserve);
    
    let recTransferFunds = 0.0;
    if (funds < 1.5) {
      recTransferFunds = Math.min(3.5, Math.max(1.5, availableHqFunds * 0.3));
    } else if (funds < 3.0 && turns <= 6) {
      recTransferFunds = Math.min(2.0, availableHqFunds * 0.2);
    } else {
      recTransferFunds = 0.0;
    }
    recTransferFunds = Math.round(recTransferFunds * 10) / 10;

    let recTransferWorkers = 0;
    if (workers < 10000) {
      recTransferWorkers = Math.min(15000, Math.floor(currentWorkers * 0.2));
    } else if (workers < 20000 && turns <= 6) {
      recTransferWorkers = Math.min(8000, Math.floor(currentWorkers * 0.1));
    }

    // Specific Infrastructure Recommendation
    const hasHq = Boolean(st.buildings?.['state_party_hq']);
    let recInfra = null;

    if (!hasHq) {
      recInfra = {
        key: 'state_party_hq',
        name: 'State Party Headquarters',
        cost: '₹1.0 Cr',
        yield: '+₹0.15 Cr/mo cash, +1.0% instant support, +0.2% monthly support',
        rationale: 'Foundation nerve centre required to coordinate statewide district units and generate recurring cash.'
      };
    } else {
      // Suggest based on state characteristics
      const code = (st.stateCode || '').toUpperCase();
      if (code === 'UP' || code === 'BIHAR' || code === 'RAJASTHAN') {
        recInfra = {
          key: 'farmers_rural_wing',
          name: "Farmers' and Rural Affairs Wing",
          cost: '₹0.25 Cr',
          yield: '+0.7% instant support, +2.2% monthly volunteers, +0.25% support/turn',
          rationale: 'Rural and agricultural demographics dominate this state. Mobilizes massive farm worker cadres.'
        };
      } else if (code === 'MAHARASHTRA' || code === 'TAMIL_NADU' || code === 'WEST_BENGAL') {
        recInfra = {
          key: 'regional_divisional_office',
          name: 'Regional / Divisional Office',
          cost: '₹0.5 Cr',
          yield: '+0.8% instant support, +₹0.08 Cr/mo cash, +1.5% volunteers',
          rationale: 'Coordinates regional cluster districts and expands vernacular media war-room coverage.'
        };
      } else {
        recInfra = {
          key: 'youth_wing',
          name: 'Youth Wing',
          cost: '₹0.2 Cr',
          yield: '+0.5% instant support, +1.8% volunteers, +0.2% support/turn',
          rationale: 'High-energy youth cadres mobilize polling booth volunteers across local constituencies.'
        };
      }
    }

    // Recommended Issue Stance / Tactical Action
    let recTacticalAction = null;
    if (turns <= 3) {
      recTacticalAction = {
        key: 'RALLY',
        label: 'Mass Public Rally (₹1.0 Cr)',
        effect: '+1.0% immediate vote support',
        rationale: 'Election is imminent. Stage massive public demonstrations in the state capital to flip swing voters.'
      };
    } else if (funds < 1.0) {
      recTacticalAction = {
        key: 'DHARNA',
        label: 'Indefinite Collectorate Dharna (₹0.3 Cr)',
        effect: '+0.9% vote support, highly cost-effective',
        rationale: 'Low cost mobilization on administrative corruption that resonates with local voters without exhausting treasury.'
      };
    } else {
      recTacticalAction = {
        key: 'AGITATION',
        label: 'Street Agitation & Blockade (₹0.5 Cr)',
        effect: '+1.4% vote support (Top ROI)',
        rationale: 'Draws aggressive local press coverage and galvanizes grassroots youth cadres.'
      };
    }

    // State Historical Stance Spotlight
    const code = (st.stateCode || '').toUpperCase();
    let issueSpotlight = '';
    if (code === 'UP') {
      issueSpotlight = 'Focus on Sugarcane Farmer Arrears and Youth Public Exam Recruitment. Balance rural farm backward class consolidation.';
    } else if (code === 'BIHAR') {
      issueSpotlight = 'Prioritize North Bihar Flood Protection Infrastructure and Backward Caste Social Justice against governance decay.';
    } else if (code === 'MAHARASHTRA') {
      issueSpotlight = 'Champion Vidarbha Cotton Farmer Subsidies and Mumbai Slum Tenant Rehabilitation rights against crony power deals.';
    } else if (code === 'WEST_BENGAL') {
      issueSpotlight = 'Mobilize on Farmland Anti-Acquisition and Industrial Job Revitalization in closed factory belts.';
    } else if (code === 'RAJASTHAN') {
      issueSpotlight = 'Advocate for Eastern Rajasthan Canal Project (ERCP) water allocations and student depression safeguards in Kota.';
    } else if (code === 'ASSAM') {
      issueSpotlight = 'Support Clause 6 Constitutional Protections for indigenous identity and permanent Brahmaputra river embankment modernization.';
    } else if (code === 'TAMIL_NADU') {
      issueSpotlight = 'Champion Cauvery River Water Rights, Dravidian Federal Autonomy, and rural medical student exam protections.';
    } else {
      issueSpotlight = 'Champion local infrastructure grievances, fair agricultural procurement prices, and youth job creation.';
    }

    return {
      stateCode: st.stateCode,
      stateName: st.stateName || st.stateCode,
      totalLokSabhaSeats: seats,
      totalAssemblySeats: st.totalAssemblySeats || 200,
      turnsToElection: turns,
      electionPhase: st.electionPhase || 'NORMAL',
      stateFunds: funds,
      stateWorkers: workers,
      stateVolunteers: st.stateVolunteers || 0,
      urgencyScore,
      urgencyBadge,
      urgencyColor,
      isDoneThisTurn: Boolean(st.doneThisTurn || st.skippedThisTurn),
      recTransferFunds,
      recTransferWorkers,
      recInfra,
      recTacticalAction,
      issueSpotlight
    };
  });

  rankedStates.sort((a, b) => b.urgencyScore - a.urgencyScore);

  return {
    executiveSummary: {
      playerPartyKey,
      playerPartyName: playerState?.partyName || playerPartyKeyUpper,
      currentSeason,
      era,
      strategicPhase,
      phaseTitle,
      topObjective,
      totalAllianceSeats,
      majorityGap,
      hasMajority,
      currentFunds,
      currentMorale,
      currentCorruption,
      currentWorkers,
      currentVolunteers,
      currentDonors
    },
    coalitionGuide: {
      isComplete: Boolean(activeGame.pendingRequests?.some(r => r.turn === currentSeason) || playerAlliance),
      statusBadge: playerAlliance ? 'ALLIANCE FORMED' : 'UNALIGNED ⚠️',
      hasAlliance: Boolean(playerAlliance),
      allianceName: playerAlliance?.allianceName || 'Unaligned Independent',
      isAllianceLeader,
      cabinetLeft,
      stateLeft,
      topRecruitTarget: topRecruitTarget ? {
        partyKey: topRecruitTarget.partyKey,
        name: topRecruitTarget.partyName,
        projSeats: targetProjSeats
      } : null,
      recommendation: coalitionRecommendation,
      actionTip: coalitionActionTip
    },
    financeGuide: {
      isComplete: Boolean(activeGame.committedFinanceCard),
      statusBadge: activeGame.committedFinanceCard ? 'COMMITTED ✓' : 'ACTION PENDING ⏳',
      greedHeat,
      posture: financePosture,
      recommendation: financeRecommendation,
      cardHint: financeCardHint
    },
    eventsGuide: {
      isComplete: Boolean(
        (activeGame.resolvedEventReactions && Object.keys(activeGame.resolvedEventReactions).length > 0) ||
        activeGame.activeThemeAction
      ),
      statusBadge: (activeGame.resolvedEventReactions && Object.keys(activeGame.resolvedEventReactions).length > 0) ? 'RESOLVED ✓' : 'PENDING ⏳',
      pendingCount: pendingEventsCount,
      recommendation: eventsRecommendation,
      actionTip: eventsActionTip
    },
    stateGuide: {
      isComplete: Boolean(stateList.length > 0 && stateList.every(s => s.doneThisTurn || s.skippedThisTurn)),
      statusBadge: stateList.every(s => s.doneThisTurn || s.skippedThisTurn) ? 'ALL STATES DONE ✓' : 'OPERATIONS PENDING ⏳',
      topPriorityState: rankedStates[0] || null,
      allStates: rankedStates
    }
  };
}
