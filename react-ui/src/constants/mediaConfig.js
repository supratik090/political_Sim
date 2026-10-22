/**
 * mediaConfig.js
 * 
 * Provides clean, human-readable labels, helper formatters, and turn-based
 * topic rotation for Media Management.
 * Ensures internal keys with underscores (e.g. OPP_POLICE_CUSTODIAL_EXCESSES, NEWS_TV)
 * are NEVER shown to the user in the UI.
 */

import mediaMetadata from './media_metadata.json';

export const CHANNELS = mediaMetadata.channels;
export const GOVERNMENT_TOPICS = mediaMetadata.governmentTopics;
export const OPPOSITION_TOPICS = mediaMetadata.oppositionTopics;
export const NO_SPEND_PENALTY = mediaMetadata.noSpendPenalty;

export const CATEGORY_LABELS = {
  CRIME_SAFETY: 'Crime & Public Safety',
  TARGET_OPPOSITION: 'Targeting Opposition',
  INFRASTRUCTURE: 'Development & Infrastructure',
  INFRASTRUCTURE_CORRUPTION: 'Infrastructure & Scams',
  WELFARE: 'Welfare & Direct Support',
  SOCIAL_STABILITY: 'Social Stability',
  HEALTH_SOCIAL: 'Public Health & Hospitals',
  AGRARIAN: 'Agriculture & Irrigation',
  AGRARIAN_SOCIAL: 'Agrarian Distress',
  CULTURAL_HERITAGE: 'Cultural Heritage',
  ECONOMY: 'Economic Growth & Investment',
  GOVERNANCE_FINANCE: 'State Finances & Debt',
  YOUTH_CRIME: 'Youth & Exam Scams',
  SOCIAL_ECONOMY: 'Price Rise & Living Costs',
  CORRUPTION_TARGET: 'Exposing Government Corruption',
  SOCIAL_JUSTICE: 'Civil Rights & Justice',
  SOCIAL_HOUSING: 'Housing & Displacement'
};

export const CATEGORY_ICONS = {
  CRIME_SAFETY: '🚨',
  TARGET_OPPOSITION: '🎯',
  INFRASTRUCTURE: '🏗️',
  INFRASTRUCTURE_CORRUPTION: '🏚️',
  WELFARE: '🤝',
  SOCIAL_STABILITY: '⚖️',
  HEALTH_SOCIAL: '🏥',
  AGRARIAN: '🌾',
  AGRARIAN_SOCIAL: '🚜',
  CULTURAL_HERITAGE: '🏛️',
  ECONOMY: '📈',
  GOVERNANCE_FINANCE: '💼',
  YOUTH_CRIME: '🎓',
  SOCIAL_ECONOMY: '🛒',
  CORRUPTION_TARGET: '🔍',
  SOCIAL_JUSTICE: '✊',
  SOCIAL_HOUSING: '🏘️'
};

/**
 * Returns a human-friendly category badge label without underscores or technical keys.
 */
export function getCategoryLabel(categoryKey) {
  if (!categoryKey) return 'General Issue';
  return CATEGORY_LABELS[categoryKey] || categoryKey.replace(/_/g, ' ').toLowerCase().replace(/\b\w/g, c => c.toUpperCase());
}

/**
 * Returns clean category icon.
 */
export function getCategoryIcon(categoryKey) {
  return CATEGORY_ICONS[categoryKey] || '📢';
}

/**
 * Returns clean channel display name (never raw key like NEWS_TV).
 */
export function getChannelName(channelKey) {
  const found = CHANNELS.find(c => c.key === channelKey);
  if (found) return found.name;
  if (!channelKey) return '';
  return channelKey.replace(/_/g, ' ').toLowerCase().replace(/\b\w/g, c => c.toUpperCase());
}

/**
 * Returns clean channel short name for compact buttons.
 */
export function getChannelShortName(channelKey) {
  const found = CHANNELS.find(c => c.key === channelKey);
  if (found) return found.shortName || found.name;
  if (!channelKey) return '';
  return channelKey.replace(/_/g, ' ').toLowerCase().replace(/\b\w/g, c => c.toUpperCase());
}

/**
 * Returns channel icon.
 */
export function getChannelIcon(channelKey) {
  const found = CHANNELS.find(c => c.key === channelKey);
  return found ? found.icon : '📡';
}

/**
 * Finds topic definition by key across government and opposition pools.
 */
export function getTopicByKey(topicKey) {
  if (!topicKey) return null;
  return GOVERNMENT_TOPICS.find(t => t.key === topicKey)
      || OPPOSITION_TOPICS.find(t => t.key === topicKey)
      || null;
}

/**
 * Returns clean human-readable title for a topic (never shows OPP_... or GOV_...).
 */
export function getTopicTitle(topicKey) {
  const topic = getTopicByKey(topicKey);
  if (topic) return topic.title;
  if (!topicKey) return '';
  return topicKey.replace(/^(OPP_|GOV_)/, '').replace(/_/g, ' ').toLowerCase().replace(/\b\w/g, c => c.toUpperCase());
}

/**
 * Deterministically samples exactly 4 media topics for the player's role (Government vs Opposition)
 * for the current turn. This guarantees variety each month while remaining consistent across re-renders.
 */
export function getTurnMediaTopics(role, turnNumber = 1, seedString = 'turn_media') {
  const isGovernment = role === 'GOVERNMENT';
  const pool = isGovernment ? GOVERNMENT_TOPICS : OPPOSITION_TOPICS;

  if (pool.length <= 4) return pool;

  // Simple deterministic rotation and hash
  let hash = 0;
  const fullSeed = `${seedString}:${turnNumber}:${role}`;
  for (let i = 0; i < fullSeed.length; i++) {
    hash = ((hash << 5) - hash) + fullSeed.charCodeAt(i);
    hash |= 0;
  }

  const startIdx = Math.abs(hash) % pool.length;
  const selected = [];
  for (let i = 0; i < 4; i++) {
    selected.push(pool[(startIdx + i) % pool.length]);
  }
  return selected;
}
