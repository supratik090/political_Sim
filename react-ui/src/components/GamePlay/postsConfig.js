/**
 * postsConfig.js
 * ---------------
 * Dynamic registry of political posts in the simulation game.
 * Populated at runtime from the backend REST API definitions.
 */

export let POSTS_CONFIG = [];

export const initializePostDefinitions = (defs) => {
  if (!defs || !Array.isArray(defs)) return;
  POSTS_CONFIG = defs.map(d => ({
    key: d.key,
    name: d.name,
    icon: d.icon || '💼',
    desc: d.description || d.desc || `Assigns a leadership role. Boosts loyalty by +${d.loyaltyBoost || 10}.`,
    loyaltyBoost: d.loyaltyBoost || 10,
    coinBonus: d.coinYieldBonus !== undefined ? d.coinYieldBonus : (d.coinBonus || 0),
    moraleBonus: d.moraleYieldBonus !== undefined ? d.moraleYieldBonus : (d.moraleBonus || 0),
    mediaBonus: d.mediaYieldBonus !== undefined ? d.mediaYieldBonus : (d.mediaBonus || 0),
    color: "linear-gradient(135deg, #581c87 0%, #a855f7 100%)"
  }));
};

/** Look up post definition by key */
export const getPostByKey = (key) => POSTS_CONFIG.find(p => p.key === key) || null;

/** Look up post definition by name (for backwards compatibility) */
export const getPostByName = (name) => POSTS_CONFIG.find(p => p.name === name) || null;
