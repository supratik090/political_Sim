package com.politicalsim.ai;

import com.politicalsim.party.PartyRole;
import java.util.LinkedHashMap;
import java.util.Map;

public class AiProfile {

    private AiStyle style = AiStyle.ORGANIZATION_BUILDER;
    private double riskTolerance = 0.45;
    private double scandalPreference = 0.45;
    private double welfarePreference = 0.45;
    private double coalitionPreference = 0.35;
    private double mediaPreference = 0.45;
    private double ideologyStrictness = 0.65;
    private Map<String, Double> intentThresholds = defaultIntentThresholds();
    private Map<String, Double> scoringWeights = defaultScoringWeights();
    private Map<String, Double> categoryPreferences = new LinkedHashMap<>();

    public AiProfile() {
    }

    public AiProfile(AiStyle style, double riskTolerance, double scandalPreference, double welfarePreference,
            double coalitionPreference, double mediaPreference, double ideologyStrictness) {
        this.style = style;
        this.riskTolerance = riskTolerance;
        this.scandalPreference = scandalPreference;
        this.welfarePreference = welfarePreference;
        this.coalitionPreference = coalitionPreference;
        this.mediaPreference = mediaPreference;
        this.ideologyStrictness = ideologyStrictness;
    }

    public static AiProfile defaultForRole(PartyRole role) {
        return switch (role) {
            case GOVERNMENT -> withCategoryPreferences(
                    new AiProfile(AiStyle.CAUTIOUS_GOVERNOR, 0.35, 0.25, 0.65, 0.45, 0.55, 0.7),
                    Map.of("governance", 0.9, "defensive_counter", 0.8, "positive_service", 0.7, "media_narrative", 0.55)
            );
            case OPPOSITION -> withCategoryPreferences(
                    new AiProfile(AiStyle.AGGRESSIVE_POPULIST, 0.7, 0.8, 0.5, 0.4, 0.65, 0.75),
                    Map.of("scandal_accusation", 0.95, "agitation_movement", 0.8, "media_narrative", 0.75, "positive_service", 0.5)
            );
            case THIRD_PARTY -> withCategoryPreferences(
                    new AiProfile(AiStyle.REGIONAL_KINGMAKER, 0.45, 0.35, 0.55, 0.8, 0.45, 0.7),
                    Map.of("positive_service", 0.75, "organization_resource", 0.7, "ideology_identity", 0.65, "media_narrative", 0.45)
            );
        };
    }

    private static AiProfile withCategoryPreferences(AiProfile profile, Map<String, Double> preferences) {
        profile.setCategoryPreferences(new LinkedHashMap<>(preferences));
        return profile;
    }

    public static Map<String, Double> defaultIntentThresholds() {
        Map<String, Double> thresholds = new LinkedHashMap<>();
        thresholds.put("governmentNoConfidenceSupport", 30.0);
        thresholds.put("governmentNoConfidenceMorale", 35.0);
        thresholds.put("noConfidenceRiskTolerance", 0.55);
        thresholds.put("lowCoins", 65.0);
        thresholds.put("corruptionCrisis", 48.0);
        thresholds.put("mediaCrisis", 34.0);
        thresholds.put("lowMorale", 38.0);
        thresholds.put("electionWindowMonths", 6.0);
        thresholds.put("electionSupportTarget", 42.0);
        thresholds.put("opponentCorruptionAttack", 38.0);
        thresholds.put("scandalAttackPreference", 0.55);
        thresholds.put("lowSupport", 34.0);
        thresholds.put("needMoraleLow", 45.0);
        thresholds.put("needMediaLow", 45.0);
        thresholds.put("needSupportLow", 30.0);
        thresholds.put("needCorruptionHigh", 40.0);
        thresholds.put("needCoinsLow", 100.0);
        thresholds.put("reactionSupportCrisis", 25.0);
        return thresholds;
    }

    public static Map<String, Double> defaultScoringWeights() {
        Map<String, Double> weights = new LinkedHashMap<>();
        weights.put("cardAiPriority", 2.0);
        weights.put("cardPublicImpact", 1.5);
        weights.put("cardRiskBase", 2.0);
        weights.put("selfPublicSupport", 4.0);
        weights.put("selfMediaBase", 1.5);
        weights.put("selfMorale", 2.0);
        weights.put("selfCorruptionPenaltyBase", 2.5);
        weights.put("selfCoins", 0.2);
        weights.put("opponentPublicSupportDamage", 3.0);
        weights.put("opponentMediaDamage", 1.5);
        weights.put("opponentCorruptionGainBase", 1.5);
        weights.put("intentFit", 8.0);
        weights.put("roleCategoryFit", 5.0);
        weights.put("opponentScandalWeakness", 8.0);
        weights.put("welfareCategoryFit", 4.0);
        weights.put("mediaCategoryFit", 4.0);
        weights.put("categoryPreference", 5.0);
        weights.put("needMoraleBoost", 7.0);
        weights.put("needMediaBoost", 7.0);
        weights.put("needSupportBoost", 8.0);
        weights.put("needCorruptionDefenseBoost", 8.0);
        weights.put("needLowCoinFundBoost", 6.0);
        weights.put("unaffordableBasePenalty", 30.0);
        weights.put("lowCoinCostPenalty", 0.35);
        weights.put("reactionIntentBoost", 2.0);
        weights.put("reactionCrisisSupportBoost", 2.0);
        weights.put("reactionRiskBase", 0.08);
        weights.put("reactionRiskToleranceDiscount", 0.06);
        weights.put("ideologyStrongFit", 5.0);
        weights.put("ideologyWeakFit", -4.0);
        weights.put("ideologyCategoryFit", 3.0);
        weights.put("electionCategoryBoost", 6.0);
        weights.put("electionScandalPenalty", -3.0);
        return weights;
    }

    public AiStyle getStyle() {
        return style;
    }

    public void setStyle(AiStyle style) {
        this.style = style;
    }

    public double getRiskTolerance() {
        return riskTolerance;
    }

    public void setRiskTolerance(double riskTolerance) {
        this.riskTolerance = riskTolerance;
    }

    public double getScandalPreference() {
        return scandalPreference;
    }

    public void setScandalPreference(double scandalPreference) {
        this.scandalPreference = scandalPreference;
    }

    public double getWelfarePreference() {
        return welfarePreference;
    }

    public void setWelfarePreference(double welfarePreference) {
        this.welfarePreference = welfarePreference;
    }

    public double getCoalitionPreference() {
        return coalitionPreference;
    }

    public void setCoalitionPreference(double coalitionPreference) {
        this.coalitionPreference = coalitionPreference;
    }

    public double getMediaPreference() {
        return mediaPreference;
    }

    public void setMediaPreference(double mediaPreference) {
        this.mediaPreference = mediaPreference;
    }

    public double getIdeologyStrictness() {
        return ideologyStrictness;
    }

    public void setIdeologyStrictness(double ideologyStrictness) {
        this.ideologyStrictness = ideologyStrictness;
    }

    public Map<String, Double> getIntentThresholds() {
        return intentThresholds;
    }

    public void setIntentThresholds(Map<String, Double> intentThresholds) {
        this.intentThresholds = intentThresholds;
    }

    public Map<String, Double> getScoringWeights() {
        return scoringWeights;
    }

    public void setScoringWeights(Map<String, Double> scoringWeights) {
        this.scoringWeights = scoringWeights;
    }

    public Map<String, Double> getCategoryPreferences() {
        return categoryPreferences;
    }

    public void setCategoryPreferences(Map<String, Double> categoryPreferences) {
        this.categoryPreferences = categoryPreferences;
    }
}
