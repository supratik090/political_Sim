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
    "GOVERNMENT": {
        "style": "CAUTIOUS_GOVERNOR",
        "riskTolerance": 0.35,
        "scandalPreference": 0.25,
        "welfarePreference": 0.65,
        "coalitionPreference": 0.45,
        "mediaPreference": 0.55,
        "ideologyStrictness": 0.7,
        "intentThresholds": AI_INTENT_THRESHOLDS,
        "scoringWeights": AI_SCORING_WEIGHTS,
        "categoryPreferences": {"governance": 0.9, "defensive_counter": 0.8, "positive_service": 0.7, "media_narrative": 0.55},
    },
    "OPPOSITION": {
        "style": "AGGRESSIVE_POPULIST",
        "riskTolerance": 0.7,
        "scandalPreference": 0.8,
        "welfarePreference": 0.5,
        "coalitionPreference": 0.4,
        "mediaPreference": 0.65,
        "ideologyStrictness": 0.75,
        "intentThresholds": AI_INTENT_THRESHOLDS,
        "scoringWeights": AI_SCORING_WEIGHTS,
        "categoryPreferences": {"scandal_accusation": 0.95, "agitation_movement": 0.8, "media_narrative": 0.75, "positive_service": 0.5},
    },
    "THIRD_PARTY": {
        "style": "REGIONAL_KINGMAKER",
        "riskTolerance": 0.45,
        "scandalPreference": 0.35,
        "welfarePreference": 0.55,
        "coalitionPreference": 0.8,
        "mediaPreference": 0.45,
        "ideologyStrictness": 0.7,
        "intentThresholds": AI_INTENT_THRESHOLDS,
        "scoringWeights": AI_SCORING_WEIGHTS,
        "categoryPreferences": {"positive_service": 0.75, "organization_resource": 0.7, "ideology_identity": 0.65, "media_narrative": 0.45},
    },
}
AI_PROFILE_PRESETS = {
    "Role Default": None,
    "Cautious Governor": DEFAULT_AI_PROFILES["GOVERNMENT"],
    "Aggressive Populist": DEFAULT_AI_PROFILES["OPPOSITION"],
    "Regional Kingmaker": DEFAULT_AI_PROFILES["THIRD_PARTY"],
    "Media Machine": {
        **DEFAULT_AI_PROFILES["OPPOSITION"],
        "style": "MEDIA_MACHINE",
        "riskTolerance": 0.5,
        "mediaPreference": 0.9,
        "scandalPreference": 0.55,
    },
    "Organization Builder": {
        **DEFAULT_AI_PROFILES["THIRD_PARTY"],
        "style": "ORGANIZATION_BUILDER",
        "riskTolerance": 0.35,
        "coalitionPreference": 0.65,
        "mediaPreference": 0.4,
    },
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
