/**
 * instantFeedbackEngine.js
 * 
 * Provides real-time tactical feedback for player choices (Cards & News reactions).
 * Uses deterministic pseudo-random evaluation matching backend RoundResolutionEngine
 * to predict if an action resonates with voters or backfires due to risk roll.
 */

export function javaHashCode(str) {
  let hash = 0;
  if (!str || str.length === 0) return 0;
  for (let i = 0; i < str.length; i++) {
    hash = ((hash << 5) - hash) + str.charCodeAt(i);
    hash |= 0; // Convert to 32bit integer
  }
  return hash;
}

export function javaRandomNextInt(seedInt, bound) {
  let seed = (BigInt(seedInt) ^ 0x5DEECE66Dn) & ((1n << 48n) - 1n);
  seed = (seed * 0x5DEECE66Dn + 0xBn) & ((1n << 48n) - 1n);
  const raw = Number(seed >> 17n);
  return Math.abs(raw % bound);
}

/**
 * Check if a risk roll hits (matching backend riskHit).
 */
export function isRiskHit(sessionId, turnNumber, riskKey, chance) {
  if (!chance || chance <= 0) return false;
  const hashString = `${sessionId || 'session'}:${turnNumber || 1}:${riskKey}`;
  const seed = javaHashCode(hashString);
  const roll = javaRandomNextInt(seed, 100);
  return roll < chance;
}

/**
 * Evaluates the real-time public and media response to a chosen news reaction.
 */
export function evaluateNewsReaction(turnData, partyId, newsItem, reactionOption) {
  if (!reactionOption) return null;

  const sessionId = turnData?.gameId || turnData?.id || turnData?.scenarioId || 'session';
  const turnNumber = turnData?.turnNumber || 1;
  const reactionKey = reactionOption.reactionKey || reactionOption.optionKey || 'reaction';

  const risk = reactionOption.risk || {};
  const chance = Number(risk.chance) || 0;
  const riskKey = `news:${partyId}:${reactionKey}`;
  const hasBackfired = chance > 0 && isRiskHit(sessionId, turnNumber, riskKey, chance);

  const baseEffects = reactionOption.effects?.playerParty || reactionOption.effects?.selfParty || reactionOption.effects || {};
  const riskEffects = risk.effects?.playerParty || risk.effects?.selfParty || risk.effects || {};

  // Compute net effects
  const netEffects = { ...baseEffects };
  if (hasBackfired) {
    Object.entries(riskEffects).forEach(([k, v]) => {
      netEffects[k] = (netEffects[k] || 0) + (Number(v) || 0);
    });
  }

  let status = 'RESONATED';
  let badgeText = '🎉 PUBLIC RESONANCE';
  let badgeColor = '#4ADE80';
  let summary = 'Your statement resonated with voters! Public mood is shifting in your favor.';

  if (hasBackfired) {
    status = 'BACKFIRED';
    badgeText = '🚨 PRESS BACKLASH — BACKFIRED!';
    badgeColor = '#EF4444';
    summary = risk.badOutcome || 'Voters perceived this statement as cynical politics.';
  } else {
    // Check if neutral or minor
    const totalPositive = Object.values(baseEffects).filter(v => Number(v) > 0).length;
    const totalNegative = Object.values(baseEffects).filter(v => Number(v) < 0).length;
    if (totalPositive === 0 && totalNegative === 0) {
      status = 'NEUTRAL';
      badgeText = '🛡️ STABLE POSITION';
      badgeColor = '#38BDF8';
      summary = 'Diplomatic posture held steady without raising public controversy.';
    }
  }

  return {
    status,
    badgeText,
    badgeColor,
    summary,
    hasBackfired,
    chance,
    baseEffects,
    netEffects,
  };
}

/**
 * Evaluates the real-time ground impact of playing a campaign card.
 */
export function evaluateCardPlay(turnData, partyId, card, targetParty) {
  if (!card) return null;

  const sessionId = turnData?.gameId || turnData?.id || turnData?.scenarioId || 'session';
  const turnNumber = turnData?.turnNumber || 1;
  const cardKey = card.cardKey || card.id || 'card';

  const riskRoll = card.riskRoll || card.risk_roll || {};
  const chance = Number(riskRoll.chance) || 0;
  const riskKey = `card:${partyId}:${cardKey}`;
  const hasBackfired = chance > 0 && isRiskHit(sessionId, turnNumber, riskKey, chance);

  const selfEffects = card.visibleEffects?.selfParty || {};
  const oppEffects = card.visibleEffects?.opponentParty || {};
  const cost = Number(card.cost) || 0;

  let status = 'SUCCESS';
  let badgeText = '⚡ OPERATION DEPLOYED';
  let badgeColor = '#38BDF8';
  let summary = `Campaign teams activated across the state. Ground presence solidified.`;

  if (hasBackfired) {
    status = 'BACKFIRED';
    badgeText = '⚠️ CARD PLAY BACKFIRED!';
    badgeColor = '#EF4444';
    summary = riskRoll.badOutcome || riskRoll.bad_outcome || 'The offensive move was exposed as politically motivated.';
  } else if (targetParty) {
    status = 'SUCCESS';
    badgeText = `🎯 ATTACK ON ${targetParty.name?.toUpperCase()}`;
    badgeColor = '#F59E0B';
    summary = `Direct hit against ${targetParty.name}. Rival cadres are on the defensive!`;
  }

  return {
    status,
    badgeText,
    badgeColor,
    summary,
    cost,
    hasBackfired,
    chance,
    selfEffects,
    oppEffects,
    targetPartyName: targetParty?.name,
  };
}

/**
 * Calculates live estimated net delta for the player's party based on current turn choices.
 */
export function calculateTurnLiveDeltas(turnData, partyId, selectedCard, targetPartyId, selectedNewsReactions, bidAmount) {
  let coins = -(Number(bidAmount) || 0);
  let morale = 0;
  let support = 0;
  let media = 0;
  let corruption = 0;

  if (selectedCard) {
    coins -= (Number(selectedCard.cost) || 0);
    const self = selectedCard.visibleEffects?.selfParty || {};
    morale += (Number(self.partyMorale) || 0);
    support += (Number(self.publicSupport) || 0);
    media += (Number(self.mediaImage) || 0);
    corruption += (Number(self.corruptionScore) || 0);
  }

  const newsItems = turnData?.currentNews || [];
  newsItems.forEach(news => {
    const newsKey = news.newsKey || news.issueKey;
    const choiceKey = selectedNewsReactions?.[newsKey];
    if (choiceKey) {
      const opts = news.reactionOptions || news.options || [];
      const opt = opts.find(o => (o.reactionKey || o.optionKey) === choiceKey);
      if (opt) {
        const feedback = evaluateNewsReaction(turnData, partyId, news, opt);
        if (feedback?.netEffects) {
          morale += (Number(feedback.netEffects.partyMorale) || 0);
          support += (Number(feedback.netEffects.publicSupport) || 0);
          media += (Number(feedback.netEffects.mediaImage) || 0);
          corruption += (Number(feedback.netEffects.corruptionScore) || 0);
        }
      }
    }
  });

  return { coins, morale, support, media, corruption };
}
