/**
 * turnFeedbackCache.js
 * 
 * Client-side Lazy Cache for V2 Turn Feedback.
 * Pre-populates all news reaction and card selection feedback when a turn loads.
 * Provides 0ms instant feedback lookup when player clicks "Lock In",
 * falling back to on-demand REST call only if cache entry is not found.
 */

import { fetchTurnFeedbackCache } from '../api/apiClient';

const memoryCache = new Map();
const inFlightPromises = new Map();

function makeKey(gameId, turnNumber, partyId) {
  return `${gameId || 'game'}_${turnNumber || 0}_${partyId || 'default'}`;
}

export function formatCardFeedback(res) {
  if (!res) return null;
  return {
    hasBackfired: Boolean(res.backfired),
    badgeColor: res.backfired ? '#F87171' : (res.tripleMultiplier ? '#F59E0B' : '#4ADE80'),
    badgeText: res.headline || (res.backfired ? '🚨 TACTICAL BACKLASH' : '⚡ TACTICAL HIT'),
    summary: res.narrative,
    cost: res.cost,
    selfEffects: res.selfDeltas || {},
    oppEffects: res.opponentDeltas || {},
    tripleReason: res.tripleReason,
    isBackend: true
  };
}

export function formatNewsFeedback(item) {
  if (!item) return null;
  return {
    hasBackfired: Boolean(item.backfired),
    badgeColor: item.backfired ? '#F87171' : (item.tripleMultiplier ? '#F59E0B' : '#4ADE80'),
    badgeText: item.headline || (item.backfired ? '🚨 PRESS BACKLASH' : '🎉 PUBLIC RESONANCE'),
    summary: item.narrative,
    chance: item.riskChance,
    netEffects: item.netDeltas || {},
    coinAward: item.coinAward,
    isBackend: true
  };
}

/**
 * Lazy preloader: fetch turn feedback cache in background if not already cached.
 */
export async function preloadTurnFeedback(gameId, partyId, turnNumber) {
  if (!gameId) return null;
  const key = makeKey(gameId, turnNumber, partyId);

  // Check in-memory
  if (memoryCache.has(key)) {
    return memoryCache.get(key);
  }

  // Check sessionStorage
  try {
    const raw = sessionStorage.getItem(`wr_feedback_cache_${key}`);
    if (raw) {
      const parsed = JSON.parse(raw);
      memoryCache.set(key, parsed);
      return parsed;
    }
  } catch (_) {}

  // Deduplicate in-flight requests
  if (inFlightPromises.has(key)) {
    return inFlightPromises.get(key);
  }

  const promise = (async () => {
    try {
      const data = await fetchTurnFeedbackCache(gameId, partyId);
      if (data) {
        memoryCache.set(key, data);
        try {
          sessionStorage.setItem(`wr_feedback_cache_${key}`, JSON.stringify(data));
        } catch (_) {}
      }
      return data;
    } catch (err) {
      console.warn('Lazy turn feedback preload failed (will fallback to on-demand):', err);
      return null;
    } finally {
      inFlightPromises.delete(key);
    }
  })();

  inFlightPromises.set(key, promise);
  return promise;
}

/**
 * Synchronous / instant lookup for Card feedback in cache.
 * Returns formatted feedback object or null if cache miss.
 */
export function getCachedCardFeedback(gameId, turnNumber, partyId, cardKey, targetPartyId) {
  if (!gameId || !cardKey) return null;
  const key = makeKey(gameId, turnNumber, partyId);
  let data = memoryCache.get(key);

  if (!data) {
    try {
      const raw = sessionStorage.getItem(`wr_feedback_cache_${key}`);
      if (raw) {
        data = JSON.parse(raw);
        memoryCache.set(key, data);
      }
    } catch (_) {}
  }

  if (!data || !data.cards) return null;

  const targetKey = targetPartyId ? `${cardKey}:${targetPartyId}` : null;
  let rawFb = targetKey ? data.cards[targetKey] : null;

  if (!rawFb) {
    rawFb = data.cards[`${cardKey}:none`] || data.cards[`${cardKey}:`] || data.cards[cardKey];
  }

  return rawFb ? formatCardFeedback(rawFb) : null;
}

/**
 * Synchronous / instant lookup for News reaction feedback in cache.
 * Returns formatted feedback object or null if cache miss.
 */
export function getCachedNewsFeedback(gameId, turnNumber, partyId, newsKey, reactionKey) {
  if (!gameId || !newsKey || !reactionKey) return null;
  const key = makeKey(gameId, turnNumber, partyId);
  let data = memoryCache.get(key);

  if (!data) {
    try {
      const raw = sessionStorage.getItem(`wr_feedback_cache_${key}`);
      if (raw) {
        data = JSON.parse(raw);
        memoryCache.set(key, data);
      }
    } catch (_) {}
  }

  if (!data || !data.news) return null;

  const rawFb = data.news[`${newsKey}:${reactionKey}`];
  return rawFb ? formatNewsFeedback(rawFb) : null;
}

/**
 * Synchronous / instant lookup for all chosen news reactions.
 * Returns map of { [newsKey]: formattedFeedback } only if ALL selected reactions are in cache.
 */
export function getCachedBatchNewsFeedback(gameId, turnNumber, partyId, selectedNewsReactions) {
  if (!selectedNewsReactions || Object.keys(selectedNewsReactions).length === 0) return null;
  const results = {};

  for (const [newsKey, reactionKey] of Object.entries(selectedNewsReactions)) {
    const fb = getCachedNewsFeedback(gameId, turnNumber, partyId, newsKey, reactionKey);
    if (!fb) {
      // Partial cache miss: fallback needed
      return null;
    }
    results[newsKey] = fb;
  }

  return results;
}
