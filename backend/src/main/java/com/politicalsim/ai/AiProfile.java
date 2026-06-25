package com.politicalsim.ai;

import com.politicalsim.party.PartyRole;
import java.util.LinkedHashMap;
import java.util.Map;

public class AiProfile {

    private AiStyle style = AiStyle.BALANCED_STRATEGIST;
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
            case GOVERNMENT -> {
                AiProfile p = withCategoryPreferences(
                        new AiProfile(AiStyle.STRENGTH_BUILDER, 0.30, 0.10, 0.70, 0.50, 0.60, 0.80),
                        Map.of("governance", 0.8, "positive_service", 0.9, "organization_resource", 0.9, "media_narrative", 0.6)
                );
                // Change 4: Government-specific thresholds
                p.getIntentThresholds().put("lowMorale", 40.0);          // was 50
                p.getIntentThresholds().put("lowSupport", 30.0);         // unchanged
                p.getIntentThresholds().put("lowCoins", 80.0);           // was 100
                p.getIntentThresholds().put("electionSupportTarget", 45.0); // was 42
                yield p;
            }
            case OPPOSITION -> {
                AiProfile p = withCategoryPreferences(
                        new AiProfile(AiStyle.AGGRESSIVE_ATTACKER, 0.85, 0.90, 0.30, 0.20, 0.50, 0.50),
                        Map.of("scandal_accusation", 0.95, "agitation_movement", 0.9, "media_narrative", 0.7)
                );
                // Change 4: Opposition-specific thresholds
                p.getIntentThresholds().put("lowMorale", 35.0);          // was 50
                p.getIntentThresholds().put("lowSupport", 20.0);         // was 34 — opposition can operate lower
                p.getIntentThresholds().put("lowCoins", 70.0);           // was 100
                p.getIntentThresholds().put("electionSupportTarget", 38.0); // was 42
                yield p;
            }
            case THIRD_PARTY, DEFEATED -> {
                AiProfile p = withCategoryPreferences(
                        new AiProfile(AiStyle.BALANCED_STRATEGIST, 0.50, 0.50, 0.50, 0.50, 0.50, 0.60),
                        Map.of("governance", 0.6, "positive_service", 0.6, "organization_resource", 0.6, "scandal_accusation", 0.6, "agitation_movement", 0.6)
                );
                // Change 4: Third-party-specific thresholds
                p.getIntentThresholds().put("lowMorale", 38.0);          // was 50
                p.getIntentThresholds().put("lowSupport", 28.0);         // was 34
                p.getIntentThresholds().put("lowCoins", 75.0);           // was 100
                p.getIntentThresholds().put("electionSupportTarget", 40.0); // was 42
                yield p;
            }
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
        thresholds.put("lowCoins", 100.0);
        thresholds.put("corruptionCrisis", 50.0);
        thresholds.put("mediaCrisis", 34.0);
        thresholds.put("lowMorale", 50.0);
        thresholds.put("electionWindowMonths", 6.0);
        thresholds.put("electionSupportTarget", 42.0);
        thresholds.put("opponentCorruptionAttack", 38.0);
        thresholds.put("scandalAttackPreference", 0.55);
        thresholds.put("lowSupport", 34.0);
        thresholds.put("needMoraleLow", 50.0);
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
        if (style == null) {
            return AiStyle.BALANCED_STRATEGIST;
        }
        return switch (style) {
            case CAUTIOUS_GOVERNOR, ORGANIZATION_BUILDER -> AiStyle.STRENGTH_BUILDER;
            case AGGRESSIVE_POPULIST -> AiStyle.AGGRESSIVE_ATTACKER;
            case REGIONAL_KINGMAKER -> AiStyle.BALANCED_STRATEGIST;
            case MEDIA_MACHINE -> AiStyle.BALANCED_STRATEGIST;
            default -> style;
        };
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
