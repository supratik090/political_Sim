const Map<String, String> ideologies = {
  "Welfare Populist": "WELFARE_POPULIST",
  "Development First": "DEVELOPMENT_FIRST",
  "Regional Pride": "REGIONAL_PRIDE",
  "Anti-Corruption": "ANTI_CORRUPTION",
  "Identity Politics": "IDENTITY_POLITICS",
  "Unity Platform": "UNITY_PLATFORM",
};

const List<String> partySymbols = ["Tiger", "Elephant", "Peacock", "Bull", "Cobra", "Deer"];

const List<String> partyColors = ["#d23f31", "#244f9e", "#1f8f5f", "#c47a1c", "#5a3e8f", "#8c6f39"];

const List<String> aiStyles = [
  "CAUTIOUS_GOVERNOR",
  "AGGRESSIVE_POPULIST",
  "REGIONAL_KINGMAKER",
  "MEDIA_MACHINE",
  "ORGANIZATION_BUILDER",
];

const Map<String, double> aiIntentThresholds = {
  "governmentNoConfidenceSupport": 30.0,
  "governmentNoConfidenceMorale": 35.0,
  "noConfidenceRiskTolerance": 0.55,
  "lowCoins": 65.0,
  "corruptionCrisis": 48.0,
  "mediaCrisis": 34.0,
  "lowMorale": 38.0,
  "electionWindowMonths": 6.0,
  "electionSupportTarget": 42.0,
  "opponentCorruptionAttack": 38.0,
  "scandalAttackPreference": 0.55,
  "lowSupport": 34.0,
  "needMoraleLow": 45.0,
  "needMediaLow": 45.0,
  "needSupportLow": 30.0,
  "needCorruptionHigh": 40.0,
  "needCoinsLow": 100.0,
  "reactionSupportCrisis": 25.0,
};

const Map<String, double> aiScoringWeights = {
  "cardAiPriority": 2.0,
  "cardPublicImpact": 1.5,
  "cardRiskBase": 2.0,
  "selfPublicSupport": 4.0,
  "selfMediaBase": 1.5,
  "selfMorale": 2.0,
  "selfCorruptionPenaltyBase": 2.5,
  "selfCoins": 0.2,
  "opponentPublicSupportDamage": 3.0,
  "opponentMediaDamage": 1.5,
  "opponentCorruptionGainBase": 1.5,
  "intentFit": 8.0,
  "roleCategoryFit": 5.0,
  "opponentScandalWeakness": 8.0,
  "welfareCategoryFit": 4.0,
  "mediaCategoryFit": 4.0,
  "categoryPreference": 5.0,
  "needMoraleBoost": 7.0,
  "needMediaBoost": 7.0,
  "needSupportBoost": 8.0,
  "needCorruptionDefenseBoost": 8.0,
  "needLowCoinFundBoost": 6.0,
  "unaffordableBasePenalty": 30.0,
  "lowCoinCostPenalty": 0.35,
  "reactionIntentBoost": 2.0,
  "reactionCrisisSupportBoost": 2.0,
  "reactionRiskBase": 0.08,
  "reactionRiskToleranceDiscount": 0.06,
  "ideologyStrongFit": 5.0,
  "ideologyWeakFit": -4.0,
  "ideologyCategoryFit": 3.0,
  "electionCategoryBoost": 6.0,
  "electionScandalPenalty": -3.0,
};

const Map<String, Map<String, dynamic>> defaultAiProfiles = {
  "GOVERNMENT": {
    "style": "CAUTIOUS_GOVERNOR",
    "riskTolerance": 0.35,
    "scandalPreference": 0.25,
    "welfarePreference": 0.65,
    "coalitionPreference": 0.45,
    "mediaPreference": 0.55,
    "ideologyStrictness": 0.7,
    "intentThresholds": aiIntentThresholds,
    "scoringWeights": aiScoringWeights,
    "categoryPreferences": {
      "governance": 0.9,
      "defensive_counter": 0.8,
      "positive_service": 0.7,
      "media_narrative": 0.55
    },
  },
  "OPPOSITION": {
    "style": "AGGRESSIVE_POPULIST",
    "riskTolerance": 0.7,
    "scandalPreference": 0.8,
    "welfarePreference": 0.5,
    "coalitionPreference": 0.4,
    "mediaPreference": 0.65,
    "ideologyStrictness": 0.75,
    "intentThresholds": aiIntentThresholds,
    "scoringWeights": aiScoringWeights,
    "categoryPreferences": {
      "scandal_accusation": 0.95,
      "agitation_movement": 0.8,
      "media_narrative": 0.75,
      "positive_service": 0.5
    },
  },
  "THIRD_PARTY": {
    "style": "REGIONAL_KINGMAKER",
    "riskTolerance": 0.45,
    "scandalPreference": 0.35,
    "welfarePreference": 0.55,
    "coalitionPreference": 0.8,
    "mediaPreference": 0.45,
    "ideologyStrictness": 0.7,
    "intentThresholds": aiIntentThresholds,
    "scoringWeights": aiScoringWeights,
    "categoryPreferences": {
      "positive_service": 0.75,
      "organization_resource": 0.7,
      "ideology_identity": 0.65,
      "media_narrative": 0.45
    },
  },
};

const Map<String, dynamic> aiProfilePresets = {
  "Role Default": null,
  "Cautious Governor": {
    "style": "CAUTIOUS_GOVERNOR",
    "riskTolerance": 0.35,
    "scandalPreference": 0.25,
    "welfarePreference": 0.65,
    "coalitionPreference": 0.45,
    "mediaPreference": 0.55,
    "ideologyStrictness": 0.7,
    "intentThresholds": aiIntentThresholds,
    "scoringWeights": aiScoringWeights,
    "categoryPreferences": {
      "governance": 0.9,
      "defensive_counter": 0.8,
      "positive_service": 0.7,
      "media_narrative": 0.55
    },
  },
  "Aggressive Populist": {
    "style": "AGGRESSIVE_POPULIST",
    "riskTolerance": 0.7,
    "scandalPreference": 0.8,
    "welfarePreference": 0.5,
    "coalitionPreference": 0.4,
    "mediaPreference": 0.65,
    "ideologyStrictness": 0.75,
    "intentThresholds": aiIntentThresholds,
    "scoringWeights": aiScoringWeights,
    "categoryPreferences": {
      "scandal_accusation": 0.95,
      "agitation_movement": 0.8,
      "media_narrative": 0.75,
      "positive_service": 0.5
    },
  },
  "Regional Kingmaker": {
    "style": "REGIONAL_KINGMAKER",
    "riskTolerance": 0.45,
    "scandalPreference": 0.35,
    "welfarePreference": 0.55,
    "coalitionPreference": 0.8,
    "mediaPreference": 0.45,
    "ideologyStrictness": 0.7,
    "intentThresholds": aiIntentThresholds,
    "scoringWeights": aiScoringWeights,
    "categoryPreferences": {
      "positive_service": 0.75,
      "organization_resource": 0.7,
      "ideology_identity": 0.65,
      "media_narrative": 0.45
    },
  },
  "Media Machine": {
    "style": "MEDIA_MACHINE",
    "riskTolerance": 0.5,
    "scandalPreference": 0.55,
    "welfarePreference": 0.5,
    "coalitionPreference": 0.4,
    "mediaPreference": 0.9,
    "ideologyStrictness": 0.75,
    "intentThresholds": aiIntentThresholds,
    "scoringWeights": aiScoringWeights,
    "categoryPreferences": {
      "scandal_accusation": 0.95,
      "agitation_movement": 0.8,
      "media_narrative": 0.75,
      "positive_service": 0.5
    },
  },
  "Organization Builder": {
    "style": "ORGANIZATION_BUILDER",
    "riskTolerance": 0.35,
    "scandalPreference": 0.35,
    "welfarePreference": 0.55,
    "coalitionPreference": 0.65,
    "mediaPreference": 0.4,
    "ideologyStrictness": 0.7,
    "intentThresholds": aiIntentThresholds,
    "scoringWeights": aiScoringWeights,
    "categoryPreferences": {
      "positive_service": 0.75,
      "organization_resource": 0.7,
      "ideology_identity": 0.65,
      "media_narrative": 0.45
    },
  },
};
