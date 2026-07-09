/**
 * postsConfig.js
 * ---------------
 * Central registry of all 15 political posts in the game.
 * This mirrors PostsConfig.java on the backend.
 * Each post defines its unique key, display name, icon, description, loyalty boost,
 * and the resource yields it adds to the faction holding it per turn.
 */

export const POSTS_CONFIG = [
  {
    key: "SECRETARY",
    name: "Secretary",
    icon: "📋",
    desc: "Party's chief administrator. Boosts loyalty and morale coordination.",
    loyaltyBoost: 15,
    coinBonus: 0,
    moraleBonus: 6,
    mediaBonus: 0,
    color: "linear-gradient(135deg, #581c87 0%, #a855f7 100%)"
  },
  {
    key: "PRESS_SECRETARY",
    name: "Press Secretary",
    icon: "📰",
    desc: "Manages party communications and media. Improves media image.",
    loyaltyBoost: 8,
    coinBonus: 0,
    moraleBonus: 0,
    mediaBonus: 4,
    color: "linear-gradient(135deg, #581c87 0%, #a855f7 100%)"
  },
  {
    key: "FUND_MANAGER",
    name: "Fund Manager",
    icon: "💰",
    desc: "Oversees party finances. Significantly boosts coin income.",
    loyaltyBoost: 10,
    coinBonus: 8,
    moraleBonus: 0,
    mediaBonus: 0,
    color: "linear-gradient(135deg, #581c87 0%, #a855f7 100%)"
  },
  {
    key: "DISTRICT_HEAD",
    name: "District Head",
    icon: "🏘️",
    desc: "Leads party operations in a district. Provides grassroots morale.",
    loyaltyBoost: 5,
    coinBonus: 0,
    moraleBonus: 3,
    mediaBonus: 0,
    color: "linear-gradient(135deg, #581c87 0%, #a855f7 100%)"
  },
  {
    key: "CAMPAIGN_MANAGER",
    name: "Campaign Manager",
    icon: "📣",
    desc: "Strategizes election campaigns. Boosts support and morale.",
    loyaltyBoost: 10,
    coinBonus: 0,
    moraleBonus: 4,
    mediaBonus: 2,
    color: "linear-gradient(135deg, #581c87 0%, #a855f7 100%)"
  },
  {
    key: "LEADER_IN_HOUSE",
    name: "Leader in House",
    icon: "🏛️",
    desc: "Represents party in legislative house. Improves public support.",
    loyaltyBoost: 8,
    coinBonus: 2,
    moraleBonus: 2,
    mediaBonus: 0,
    color: "linear-gradient(135deg, #581c87 0%, #a855f7 100%)"
  },
  {
    key: "CHIEF_WHIP",
    name: "Chief Whip",
    icon: "⚖️",
    desc: "Enforces party discipline. Stabilises loyalty across factions.",
    loyaltyBoost: 7,
    coinBonus: 0,
    moraleBonus: 3,
    mediaBonus: 0,
    color: "linear-gradient(135deg, #581c87 0%, #a855f7 100%)"
  },
  {
    key: "YOUTH_WING_PRES",
    name: "Youth Wing President",
    icon: "✊",
    desc: "Leads the youth wing. Energises younger members, boosts morale.",
    loyaltyBoost: 6,
    coinBonus: 0,
    moraleBonus: 4,
    mediaBonus: 1,
    color: "linear-gradient(135deg, #581c87 0%, #a855f7 100%)"
  },
  {
    key: "TRADE_UNION_LIAISON",
    name: "Trade Union Liaison",
    icon: "🤝",
    desc: "Bridges party and unions. Improves coin yields from labour sectors.",
    loyaltyBoost: 6,
    coinBonus: 3,
    moraleBonus: 2,
    mediaBonus: 0,
    color: "linear-gradient(135deg, #581c87 0%, #a855f7 100%)"
  },
  {
    key: "POLICY_DIRECTOR",
    name: "Policy Director",
    icon: "🧠",
    desc: "Shapes party policy agenda. Increases media image significantly.",
    loyaltyBoost: 9,
    coinBonus: 0,
    moraleBonus: 0,
    mediaBonus: 5,
    color: "linear-gradient(135deg, #581c87 0%, #a855f7 100%)"
  },
  {
    key: "STATE_COORDINATOR",
    name: "State Coordinator",
    icon: "🗺️",
    desc: "Manages party operations across the state. Improves coins and morale.",
    loyaltyBoost: 11,
    coinBonus: 4,
    moraleBonus: 3,
    mediaBonus: 0,
    color: "linear-gradient(135deg, #581c87 0%, #a855f7 100%)"
  },
  {
    key: "DIGITAL_MEDIA_HEAD",
    name: "Digital Media Head",
    icon: "💻",
    desc: "Runs party's digital/social media. Provides strong media boost.",
    loyaltyBoost: 7,
    coinBonus: 0,
    moraleBonus: 0,
    mediaBonus: 6,
    color: "linear-gradient(135deg, #581c87 0%, #a855f7 100%)"
  },
  {
    key: "ELECTION_STRATEGIST",
    name: "Election Strategist",
    icon: "🗳️",
    desc: "Plans electoral strategy. Major morale and media improvements.",
    loyaltyBoost: 12,
    coinBonus: 0,
    moraleBonus: 4,
    mediaBonus: 4,
    color: "linear-gradient(135deg, #581c87 0%, #a855f7 100%)"
  },
  {
    key: "SPOKESPERSON",
    name: "Spokesperson",
    icon: "🎤",
    desc: "Official voice of the party. Boosts media image.",
    loyaltyBoost: 5,
    coinBonus: 0,
    moraleBonus: 0,
    mediaBonus: 3,
    color: "linear-gradient(135deg, #581c87 0%, #a855f7 100%)"
  },
  {
    key: "TREASURER",
    name: "Treasurer",
    icon: "🏦",
    desc: "Controls party treasury. Large coin income boost.",
    loyaltyBoost: 14,
    coinBonus: 10,
    moraleBonus: 0,
    mediaBonus: 0,
    color: "linear-gradient(135deg, #581c87 0%, #a855f7 100%)"
  }
];

/** Look up post definition by key */
export const getPostByKey = (key) => POSTS_CONFIG.find(p => p.key === key) || null;

/** Look up post definition by name (for backwards compatibility) */
export const getPostByName = (name) => POSTS_CONFIG.find(p => p.name === name) || null;
