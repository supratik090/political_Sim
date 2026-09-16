/**
 * Hints Engine for Statecraft Political Party Simulator
 * Evaluates current player position & turn data using AI decision-making criteria
 * to generate optimal, actionable hints per turn.
 */

// Format raw bill keys into clean human-readable titles
function formatBillName(billKey, billDef) {
  if (billDef && (billDef.name || billDef.title)) {
    return billDef.name || billDef.title;
  }
  if (!billKey) return 'Legislative Bill';
  
  // Remove bill_ or bill- prefix
  let clean = billKey.replace(/^bill[_-]/i, '');
  // Replace underscores and dashes with spaces
  clean = clean.replace(/[_-]/g, ' ');
  // Capitalize words
  clean = clean.split(' ')
    .map(w => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase())
    .join(' ');
    
  return `${clean} Bill`;
}

// Determine if a card specifically targets an opponent party
function isOpponentTargetCard(cardObj) {
  if (!cardObj) return false;
  if (cardObj.target?.opponentParty) return true;
  const oppEff = cardObj.visibleEffects?.opponentParty || {};
  if (Object.keys(oppEff).length > 0) return true;
  const cat = (cardObj.category || '').toUpperCase();
  if (cat === 'ATTACK' || cat === 'SABOTAGE' || cat === 'SCANDAL') return true;
  return false;
}

// Format card effects into clear human-readable string
function formatCardEffects(cardObj) {
  if (!cardObj) return '';
  const eff = cardObj.effects || cardObj.visibleEffects?.selfParty || {};
  const oppEff = cardObj.visibleEffects?.opponentParty || {};
  const parts = [];

  if (eff.coins > 0) parts.push(`+${eff.coins} Coins 💰`);
  else if (eff.coins < 0) parts.push(`${eff.coins} Coins 💰`);

  if (eff.publicSupport > 0) parts.push(`+${eff.publicSupport}% Support 📈`);
  else if (eff.publicSupport < 0) parts.push(`${eff.publicSupport}% Support 📈`);

  if (eff.partyMorale > 0) parts.push(`+${eff.partyMorale} Morale ✊`);
  else if (eff.partyMorale < 0) parts.push(`${eff.partyMorale} Morale ✊`);

  if (eff.mediaImage > 0) parts.push(`+${eff.mediaImage} Media 📢`);
  else if (eff.mediaImage < 0) parts.push(`${eff.mediaImage} Media 📢`);

  if (eff.corruptionScore < 0) parts.push(`${eff.corruptionScore}% Corruption ⚖️`);
  else if (eff.corruptionScore > 0) parts.push(`+${eff.corruptionScore}% Corruption ⚖️`);

  if (oppEff.publicSupport < 0) parts.push(`Target ${oppEff.publicSupport}% Support`);
  if (oppEff.partyMorale < 0) parts.push(`Target ${oppEff.partyMorale} Morale`);
  if (oppEff.mediaImage < 0) parts.push(`Target ${oppEff.mediaImage} Media`);

  return parts.join(', ');
}

// Determine current strategic intent (matching AiDecisionService.java)
function determineAiIntent(myParty, turnNumber = 1) {
  const coins = myParty.coins ?? 50;
  const morale = myParty.partyMorale ?? 50;
  const support = myParty.publicSupport ?? 25;
  const corruption = myParty.corruptionScore ?? 20;
  const media = myParty.mediaImage ?? 50;
  const turnsRemaining = Math.max(0, 60 - turnNumber);

  if (coins <= 35) return 'RAISE_FUNDS';
  if (support < 20) return 'GAIN_SUPPORT';
  if (morale < 22) return 'RESTORE_MORALE';
  if (corruption > 80) return 'SURVIVE_SCANDAL';
  if (media < 30) return 'DEFEND_IMAGE';
  if (turnsRemaining <= 10 && support < 50) return 'PREPARE_ELECTION';

  if (support < 35) return 'GAIN_SUPPORT';
  if (morale < 45) return 'RESTORE_MORALE';
  return 'CONSOLIDATE_LEAD';
}

export function generateTurnHints(turnData, localDecisions = {}, scenarioBills = [], scenarioEvents = []) {
  if (!turnData) {
    return [
      {
        id: 'no-data',
        category: 'GENERAL',
        urgency: 'RECOMMENDED',
        priorityScore: 50,
        title: 'Waiting for Turn Data',
        description: 'Start or join a campaign turn to receive tailored strategic guidance.',
        targetTab: 'INFO',
        actionLabel: 'View Campaign',
        badgeText: 'Info',
        badgeBg: '#3b82f6'
      }
    ];
  }

  const hints = [];
  const myParty = turnData.myParty || turnData.parties?.[0] || {};
  const parties = turnData.parties || [];
  const coins = myParty.coins ?? 50;
  const partyMorale = myParty.partyMorale ?? 50;
  const corruptionScore = myParty.corruptionScore ?? 20;
  const publicSupport = myParty.publicSupport ?? 25;
  const playerRole = myParty.role || 'THIRD_PARTY';
  const rawCards = myParty.availableCards || turnData.availableCards || [];
  const projects = myParty.projects || turnData.projects || [];
  const turnNumber = turnData.turnNumber || 1;

  const aiIntent = determineAiIntent(myParty, turnNumber);

  // Filter out dummy/pass turn cards ("no_card" / "No Card (Pass Turn)")
  const availableCards = rawCards.filter(c => {
    if (!c) return false;
    const key = (c.cardKey || c.id || '').toLowerCase();
    const name = (typeof c === 'string' ? c : (c.title || c.name || '')).toLowerCase();
    return key !== 'no_card' && !name.includes('no card') && !name.includes('pass turn');
  });

  // Find leading opponent
  const opponentParties = parties.filter(p => p.id !== myParty.id && p.name !== myParty.name);
  const leadingOpponent = opponentParties.length > 0 
    ? [...opponentParties].sort((a, b) => (b.publicSupport || 0) - (a.publicSupport || 0))[0] 
    : null;

  // 1. FINANCIAL EMERGENCY (Coins < 20)
  if (coins < 20) {
    hints.push({
      id: 'low-coins',
      category: 'RESOURCES',
      urgency: 'CRITICAL',
      priorityScore: 100,
      title: `Treasury Reserve Low (${coins} Coins)`,
      description: `You are critically low on treasury funds. Take a Governance Loan in War Room, play a fundraising card, or build income structures like IT Cell / Media House.`,
      targetTab: 'ACTIONS',
      actionLabel: 'Manage Treasury',
      badgeText: 'Financial Risk',
      badgeBg: '#be123c'
    });
  } else if (coins < 40) {
    hints.push({
      id: 'moderate-coins',
      category: 'RESOURCES',
      urgency: 'RECOMMENDED',
      priorityScore: 55,
      title: `Cash Flow Optimization (${coins} Coins)`,
      description: `Consider building an 'IT Cell' or 'Media House' to maintain a healthy passive coin stream each turn.`,
      targetTab: 'BUILDINGS',
      actionLabel: 'View Buildings',
      badgeText: 'Economy',
      badgeBg: '#059669'
    });
  }

  // 2. MORALE CRISIS (Party Morale < 35)
  if (partyMorale < 35) {
    hints.push({
      id: 'morale-crisis',
      category: 'RESOURCES',
      urgency: 'CRITICAL',
      priorityScore: 95,
      title: `Party Morale Emergency (${partyMorale}%)`,
      description: `Party morale is at a dangerous low! Build a 'Youth Wing', host a 'Mega Rally', or pick morale-boosting news options to avoid cadre revolt.`,
      targetTab: 'BUILDINGS',
      actionLabel: 'Boost Morale',
      badgeText: 'Morale Alert',
      badgeBg: '#dc2626'
    });
  }

  // 3. HIGH CORRUPTION DANGER (Corruption > 60)
  if (corruptionScore > 60) {
    hints.push({
      id: 'high-corruption',
      category: 'RESOURCES',
      urgency: 'HIGH',
      priorityScore: 90,
      title: `High Corruption Level (${corruptionScore}%)`,
      description: `High corruption exposes your party to scandals. Vote AYE on anti-corruption bills in Assembly or fund clean governance initiatives.`,
      targetTab: 'ASSEMBLY',
      actionLabel: 'Clean Governance',
      badgeText: 'Scandal Risk',
      badgeBg: '#d97706'
    });
  }

  // 4. ASSEMBLY & LEGISLATIVE VOTING NUDGES (AI Recommendation Engine)
  const activeBillKey = turnData.proposedBillKeyThisTurn;
  let activeBillDef = null;

  if (activeBillKey) {
    // Lookup in all bill repositories
    if (scenarioBills && scenarioBills.length > 0) {
      activeBillDef = scenarioBills.find(b => b.billKey === activeBillKey || b.id === activeBillKey);
    }
    if (!activeBillDef && turnData.bills) {
      activeBillDef = turnData.bills.find(b => b.billKey === activeBillKey || b.id === activeBillKey);
    }
    if (!activeBillDef && turnData.allBills) {
      activeBillDef = turnData.allBills.find(b => b.billKey === activeBillKey || b.id === activeBillKey);
    }
    if (!activeBillDef && turnData.proposedBillDef) {
      activeBillDef = turnData.proposedBillDef;
    }
  }

  if (activeBillKey || activeBillDef) {
    const formattedBillName = formatBillName(activeBillKey, activeBillDef);
    const passedEffects = activeBillDef?.effectsPassed || activeBillDef?.passedEffects || activeBillDef?.effects || {};
    
    // Check if player party is the proposer
    const isProposer = activeBillDef?.proposedByPartyId === myParty.id || 
                       (activeBillDef?.proposingRole === playerRole);
    
    const scaleFactor = isProposer ? 1.0 : 0.5;

    const supportVal = Math.round((passedEffects.publicSupport || 0) * scaleFactor);
    const moraleVal = Math.round((passedEffects.partyMorale || 0) * scaleFactor) + (isProposer ? (activeBillDef?.pointsPassed || 0) : 0);
    const mediaVal = Math.round((passedEffects.mediaImage || 0) * scaleFactor);
    const corruptionVal = Math.round((passedEffects.corruptionScore || 0) * scaleFactor);
    const coinsVal = Math.round((passedEffects.coins || 0) * scaleFactor);

    // AI Bill Utility Formula matching AiDecisionService.java scoreBillForAi
    const billScore = (supportVal * 2.5) + (moraleVal * 1.5) + (mediaVal * 1.5) - (corruptionVal * 2.0) + (coinsVal * 0.1);

    // Format benefit / harm list for detailed explanation
    const positiveParts = [];
    const negativeParts = [];

    if (supportVal > 0) positiveParts.push(`+${supportVal}% Support`);
    else if (supportVal < 0) negativeParts.push(`${supportVal}% Support`);

    if (moraleVal > 0) positiveParts.push(`+${moraleVal} Morale`);
    else if (moraleVal < 0) negativeParts.push(`${moraleVal} Morale`);

    if (coinsVal > 0) positiveParts.push(`+${coinsVal} Coins`);
    else if (coinsVal < 0) negativeParts.push(`${coinsVal} Coins`);

    if (mediaVal > 0) positiveParts.push(`+${mediaVal} Media Image`);
    else if (mediaVal < 0) negativeParts.push(`${mediaVal} Media Image`);

    if (corruptionVal < 0) positiveParts.push(`${corruptionVal}% Corruption`);
    else if (corruptionVal > 0) negativeParts.push(`+${corruptionVal}% Corruption`);

    const positiveStr = positiveParts.join(', ');
    const negativeStr = negativeParts.join(', ');

    if (billScore > 0) {
      hints.push({
        id: 'assembly-vote-aye',
        category: 'ASSEMBLY',
        urgency: 'HIGH',
        priorityScore: 88,
        title: `Assembly Vote: Vote AYE (YES) on '${formattedBillName}'`,
        description: `AI Analysis recommends AYE (YES). Passing this legislation yields net positive gains (${positiveStr || 'National Benefit'})${isProposer ? ' (100% Proposer Benefit)' : ' (50% Voter Share)'}.`,
        targetTab: 'ASSEMBLY',
        actionLabel: 'Vote AYE',
        badgeText: 'Optimal Vote',
        badgeBg: '#16a34a'
      });
    } else {
      const reasonText = negativeStr 
        ? `It inflicts penalties: ${negativeStr}` 
        : `It fails to provide net benefits for your party's agenda`;
      hints.push({
        id: 'assembly-vote-nay',
        category: 'ASSEMBLY',
        urgency: 'HIGH',
        priorityScore: 88,
        title: `Assembly Vote: Vote NO (NAY) on '${formattedBillName}'`,
        description: `AI Analysis recommends NAY (NO) on '${formattedBillName}'. ${reasonText}. Issue a Party Whip and vote NAY to block it!`,
        targetTab: 'ASSEMBLY',
        actionLabel: 'Vote NAY',
        badgeText: 'Block Bill',
        badgeBg: '#be123c'
      });
    }
  } else {
    // Nudge to propose a bill if role allows
    const unproposedBills = (scenarioBills || turnData.bills || []).filter(b => {
      if (playerRole === 'GOVERNMENT') return b.proposingRole === 'GOVERNMENT' || b.roleAllowed === 'GOVERNMENT';
      return b.proposingRole === 'OPPOSITION' || b.roleAllowed === 'OPPOSITION';
    });
    if (unproposedBills.length > 0) {
      const topBill = unproposedBills[0];
      const topBillName = formatBillName(topBill.billKey, topBill);
      hints.push({
        id: 'propose-bill',
        category: 'ASSEMBLY',
        urgency: 'MEDIUM',
        priorityScore: 68,
        title: `Propose Bill: '${topBillName}'`,
        description: `As ${playerRole}, you have unproposed bills. Table '${topBillName}' to set the legislative agenda in the Assembly.`,
        targetTab: 'ASSEMBLY',
        actionLabel: 'Go to Assembly',
        badgeText: 'Legislative Nudge',
        badgeBg: '#2563eb'
      });
    }
  }

  // 5. NEWS REACTION GUIDANCE (AI Decision Optimization)
  const currentNews = turnData.currentNews || turnData.events || [];
  if (currentNews.length > 0) {
    const newsItem = currentNews[0];
    const rawOptions = newsItem.reactionOptions || newsItem.options || [];
    if (rawOptions.length > 0) {
      let bestOption = null;
      let bestScore = -9999;

      rawOptions.forEach(opt => {
        const rawEffects = opt.effects || {};
        const eff = rawEffects.playerParty || rawEffects;
        let score = (eff.publicSupport || 0) * 3 + (eff.partyMorale || 0) * 2 + (eff.coins || 0) - (eff.corruptionScore || 0) * 2;

        if (aiIntent === 'GAIN_SUPPORT' && eff.publicSupport > 0) score += 25;
        if (aiIntent === 'RESTORE_MORALE' && eff.partyMorale > 0) score += 25;
        if (aiIntent === 'RAISE_FUNDS' && eff.coins > 0) score += 25;
        if (aiIntent === 'SURVIVE_SCANDAL' && eff.corruptionScore < 0) score += 25;

        if (score > bestScore) {
          bestScore = score;
          bestOption = opt;
        }
      });

      if (bestOption) {
        const optionText = bestOption.text || bestOption.label || bestOption.title || bestOption.reactionKey || bestOption.optionKey || 'the recommended response';
        hints.push({
          id: 'news-reaction',
          category: 'NEWS',
          urgency: 'HIGH',
          priorityScore: 80,
          title: `News Strategy: '${newsItem.title || 'State Chronicle Event'}'`,
          description: `AI Analysis recommends choice: "${optionText}" for optimal stat growth.`,
          targetTab: 'ACTIONS',
          actionLabel: 'React to News',
          badgeText: 'AI News Pick',
          badgeBg: '#ea580c'
        });
      }
    }
  }

  // 6. ACTION CARD PLAY RECOMMENDATIONS (Accurate Per-Card Intent Scoring)
  if (availableCards.length > 0 && !(myParty.blockCardsTurns > 0)) {
    const scoredCards = availableCards.map(card => {
      if (!card) return null;
      const cardObj = typeof card === 'string' ? { title: card, name: card } : card;
      const eff = cardObj.effects || cardObj.visibleEffects?.selfParty || {};
      const isTargeting = isOpponentTargetCard(cardObj);

      let score = (eff.publicSupport || 0) * 3 + (eff.partyMorale || 0) * 2 + (eff.coins || 0) - (eff.corruptionScore || 0) * 2;

      if (aiIntent === 'RAISE_FUNDS' && (eff.coins > 0)) score += 35;
      if (aiIntent === 'GAIN_SUPPORT' && (eff.publicSupport > 0)) score += 35;
      if (aiIntent === 'RESTORE_MORALE' && (eff.partyMorale > 0)) score += 35;
      if (aiIntent === 'SURVIVE_SCANDAL' && (eff.corruptionScore < 0)) score += 35;

      if (isTargeting && leadingOpponent) {
        score += 15;
      }

      return { cardObj, score, isTargeting, effectSummary: formatCardEffects(cardObj) };
    }).filter(Boolean);

    scoredCards.sort((a, b) => b.score - a.score);

    // Top self-benefit card
    const topSelfCard = scoredCards.find(c => !c.isTargeting);
    // Top offensive / attack card
    const topAttackCard = scoredCards.find(c => c.isTargeting);

    if (topSelfCard) {
      const cardTitle = topSelfCard.cardObj.title || topSelfCard.cardObj.name || 'Campaign Strategy Card';
      const categoryName = (topSelfCard.cardObj.category || 'Strategy').replace(/_/g, ' ');
      hints.push({
        id: `card-recommendation-${topSelfCard.cardObj.id || 'self'}`,
        category: 'CARDS',
        urgency: 'HIGH',
        priorityScore: 84,
        title: `Optimal Strategy: Play '${cardTitle}'`,
        description: topSelfCard.effectSummary 
          ? `AI Strategy Engine recommends playing '${cardTitle}' (${categoryName}). Benefits: ${topSelfCard.effectSummary}.`
          : `AI Strategy Engine recommends playing '${cardTitle}' to boost active campaign priorities (${aiIntent.replace(/_/g, ' ')}).`,
        targetTab: 'CARDS',
        actionLabel: `Play ${cardTitle}`,
        badgeText: 'Optimal Card',
        badgeBg: '#7c3aed'
      });
    }

    if (topAttackCard && leadingOpponent) {
      const cardTitle = topAttackCard.cardObj.title || topAttackCard.cardObj.name || 'Tactical Offensive Card';
      hints.push({
        id: `card-attack-${topAttackCard.cardObj.id || 'attack'}`,
        category: 'CARDS',
        urgency: 'HIGH',
        priorityScore: 81,
        title: `Offensive Strategy: Play '${cardTitle}'`,
        description: `AI Strategy Engine recommends playing '${cardTitle}' targeting opponent ${leadingOpponent.name} to disrupt their campaign lead (${topAttackCard.effectSummary || 'Inflicts relative penalties'}).`,
        targetTab: 'CARDS',
        actionLabel: `Target ${leadingOpponent.name}`,
        badgeText: 'Attack Card',
        badgeBg: '#dc2626'
      });
    }
  }

  // 7. INFRASTRUCTURE & BUILDINGS NUDGE
  const completedProjectKeys = projects.filter(p => p.progressPercent === 100).map(p => p.projectKey);
  if (!completedProjectKeys.includes('PARTY_HQ')) {
    hints.push({
      id: 'build-hq',
      category: 'BUILDINGS',
      urgency: 'MEDIUM',
      priorityScore: 65,
      title: `Foundation: Build Party HQ`,
      description: `Constructing a Party HQ unlocks passive coin & morale generation every round.`,
      targetTab: 'BUILDINGS',
      actionLabel: 'Build HQ',
      badgeText: 'Infrastructure',
      badgeBg: '#4f46e5'
    });
  } else if (leadingOpponent && (leadingOpponent.publicSupport || 0) > publicSupport) {
    hints.push({
      id: 'sabotage-opponent',
      category: 'BUILDINGS',
      urgency: 'MEDIUM',
      priorityScore: 62,
      title: `Target Leading Opponent (${leadingOpponent.name})`,
      description: `${leadingOpponent.name} is leading with ${leadingOpponent.publicSupport}% support. Build 'Dissent Newspaper' or 'Campaign Sabotage' to disrupt them.`,
      targetTab: 'BUILDINGS',
      actionLabel: 'View Offensive Projects',
      badgeText: 'Offensive Tactic',
      badgeBg: '#b91c1c'
    });
  }

  // 8. WINNING POSITION CONSOLIDATION
  if (publicSupport > 35 && (!leadingOpponent || publicSupport >= (leadingOpponent.publicSupport || 0))) {
    hints.push({
      id: 'consolidate-lead',
      category: 'GENERAL',
      urgency: 'RECOMMENDED',
      priorityScore: 50,
      title: `Consolidate Campaign Lead (${publicSupport}% Support)`,
      description: `You are in pole position! Build Think Tanks, maintain high media image, and avoid scandalous news choices to secure victory.`,
      targetTab: 'STATS',
      actionLabel: 'View Campaign Stats',
      badgeText: 'Leader Strategy',
      badgeBg: '#d97706'
    });
  }

  // Fallback hint to ensure at least 3 hints if needed
  if (hints.length < 3) {
    hints.push({
      id: 'general-rally',
      category: 'GENERAL',
      urgency: 'RECOMMENDED',
      priorityScore: 40,
      title: `Citizen Outreach & Morale`,
      description: `Engage with constituencies, issue party whips in Assembly, and keep cadre morale above 50% to maintain steady progress.`,
      targetTab: 'WAR_ROOM',
      actionLabel: 'Open War Room',
      badgeText: 'Campaign Tip',
      badgeBg: '#0891b2'
    });
  }

  // Sort by priorityScore descending and return up to 8 hints
  const sortedHints = hints.sort((a, b) => b.priorityScore - a.priorityScore);
  const maxHints = Math.min(Math.max(sortedHints.length, 3), 8);
  return sortedHints.slice(0, maxHints);
}
