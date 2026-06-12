import os

API_BASE_URL = os.getenv("POLITICAL_SIM_API_URL", "http://localhost:7810")

IDEOLOGIES = {
    "Welfare Populist": "WELFARE_POPULIST",
    "Development First": "DEVELOPMENT_FIRST",
    "Regional Pride": "REGIONAL_PRIDE",
    "Anti-Corruption": "ANTI_CORRUPTION",
    "Identity Politics": "IDENTITY_POLITICS",
    "Unity Platform": "UNITY_PLATFORM",
}

PARTY_SYMBOLS = ["Tiger", "Elephant", "Peacock", "Bull", "Cobra", "Deer"]
PARTY_COLORS = ["#d23f31", "#244f9e", "#1f8f5f", "#c47a1c", "#5a3e8f", "#8c6f39"]
SYMBOL_ART = {
    "Tiger": "TGR",
    "Elephant": "ELP",
    "Peacock": "PCK",
    "Bull": "BUL",
    "Cobra": "CBR",
    "Deer": "DER",
}
AI_STYLES = [
    "CAUTIOUS_GOVERNOR",
    "AGGRESSIVE_POPULIST",
    "REGIONAL_KINGMAKER",
    "MEDIA_MACHINE",
    "ORGANIZATION_BUILDER",
]
AI_INTENT_THRESHOLDS = {
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
}
AI_SCORING_WEIGHTS = {
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
}
DEFAULT_AI_PROFILES = {
    "STRENGTH_BUILDER": {
        "style": "STRENGTH_BUILDER",
        "riskTolerance": 0.30,
        "scandalPreference": 0.10,
        "welfarePreference": 0.70,
        "coalitionPreference": 0.50,
        "mediaPreference": 0.60,
        "ideologyStrictness": 0.80,
        "intentThresholds": AI_INTENT_THRESHOLDS,
        "scoringWeights": AI_SCORING_WEIGHTS,
        "categoryPreferences": {"governance": 0.8, "positive_service": 0.9, "organization_resource": 0.9, "media_narrative": 0.6},
    },
    "AGGRESSIVE_ATTACKER": {
        "style": "AGGRESSIVE_ATTACKER",
        "riskTolerance": 0.85,
        "scandalPreference": 0.90,
        "welfarePreference": 0.30,
        "coalitionPreference": 0.20,
        "mediaPreference": 0.50,
        "ideologyStrictness": 0.50,
        "intentThresholds": AI_INTENT_THRESHOLDS,
        "scoringWeights": AI_SCORING_WEIGHTS,
        "categoryPreferences": {"scandal_accusation": 0.95, "agitation_movement": 0.9, "media_narrative": 0.7},
    },
    "LATE_STRIKER": {
        "style": "LATE_STRIKER",
        "riskTolerance": 0.50,
        "scandalPreference": 0.60,
        "welfarePreference": 0.50,
        "coalitionPreference": 0.40,
        "mediaPreference": 0.50,
        "ideologyStrictness": 0.60,
        "intentThresholds": AI_INTENT_THRESHOLDS,
        "scoringWeights": AI_SCORING_WEIGHTS,
        "categoryPreferences": {"governance": 0.7, "positive_service": 0.7, "organization_resource": 0.7, "scandal_accusation": 0.8, "agitation_movement": 0.8},
    },
    "AGGRESSIVE_BIDDER": {
        "style": "AGGRESSIVE_BIDDER",
        "riskTolerance": 0.65,
        "scandalPreference": 0.40,
        "welfarePreference": 0.50,
        "coalitionPreference": 0.50,
        "mediaPreference": 0.40,
        "ideologyStrictness": 0.60,
        "intentThresholds": AI_INTENT_THRESHOLDS,
        "scoringWeights": AI_SCORING_WEIGHTS,
        "categoryPreferences": {"organization_resource": 0.9, "positive_service": 0.7},
    },
    "BALANCED_STRATEGIST": {
        "style": "BALANCED_STRATEGIST",
        "riskTolerance": 0.50,
        "scandalPreference": 0.50,
        "welfarePreference": 0.50,
        "coalitionPreference": 0.50,
        "mediaPreference": 0.50,
        "ideologyStrictness": 0.60,
        "intentThresholds": AI_INTENT_THRESHOLDS,
        "scoringWeights": AI_SCORING_WEIGHTS,
        "categoryPreferences": {"governance": 0.6, "positive_service": 0.6, "organization_resource": 0.6, "scandal_accusation": 0.6, "agitation_movement": 0.6},
    },
}
AI_PROFILE_PRESETS = {
    "Strength Builder 🛡️": DEFAULT_AI_PROFILES["STRENGTH_BUILDER"],
    "Aggressive Attacker ⚔️": DEFAULT_AI_PROFILES["AGGRESSIVE_ATTACKER"],
    "Late Striker ⏳": DEFAULT_AI_PROFILES["LATE_STRIKER"],
    "Aggressive Bidder 🪙": DEFAULT_AI_PROFILES["AGGRESSIVE_BIDDER"],
    "Balanced Strategist ⚖️": DEFAULT_AI_PROFILES["BALANCED_STRATEGIST"],
}
CATEGORY_COLORS = {
    "governance": "#4a7c80",
    "positive_service": "#529b71",
    "agitation_movement": "#c67a53",
    "scandal_accusation": "#b5525f",
    "defensive_counter": "#5e72a4",
    "media_narrative": "#baa15e",
    "organization_resource": "#8575a5",
    "ideology_identity": "#90834a",
    "constitutional_power_move": "#575760",
}
POST_IT_COLORS = {
    "governance": "#e2f0d9",            # Soft light green
    "positive_service": "#e8f8f5",      # Soft light mint/teal
    "agitation_movement": "#fff2cc",    # Soft light yellow
    "scandal_accusation": "#fce4d6",    # Soft light peach/coral
    "defensive_counter": "#ebdef0",     # Soft light purple
    "media_narrative": "#fffdf0",       # Very light cream yellow
    "organization_resource": "#d1ecf1", # Soft light blue/cyan
    "ideology_identity": "#fcf3cf",     # Soft light gold/yellow
    "constitutional_power_move": "#e5e7eb", # Soft light grey
    "other": "#fafafa",                 # Soft neutral light grey
}
CATEGORY_LABELS = {
    "governance": "Governance",
    "positive_service": "Positive / Service",
    "agitation_movement": "Agitation / Movement",
    "scandal_accusation": "Scandal / Accusation",
    "defensive_counter": "Defensive / Counter",
    "media_narrative": "Media / Narrative",
    "organization_resource": "Organization / Resource",
    "ideology_identity": "Ideology / Identity",
    "constitutional_power_move": "Constitutional / Power Move",
}
