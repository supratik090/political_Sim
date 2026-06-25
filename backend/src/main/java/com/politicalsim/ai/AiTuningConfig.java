package com.politicalsim.ai;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import java.time.Instant;
import java.util.Map;
import java.util.LinkedHashMap;

/**
 * MongoDB document that externalises every tunable AI constant.
 * One document per config version. The one with {@code active = true}
 * (and the highest {@code version}) is used at runtime.
 *
 * Every field has a sensible default so old game sessions or a missing
 * document never cause a NullPointerException.
 */
@Document(collection = "ai_configs")
public class AiTuningConfig {

    @Id
    private String id;

    /** Monotonically increasing version. Newer = higher number. */
    private int version = 1;

    /** Human-readable label for admin UI. */
    private String description = "Default AI config";

    private boolean active = true;

    private Instant createdAt = Instant.now();
    private String approvedBy;

    // ─────────────────────────────────────────────────────────────────────────
    // SECTION 1: Survival override (chooseIntent — top guard)
    // ─────────────────────────────────────────────────────────────────────────
    private SurvivalConfig survival = new SurvivalConfig();

    public static class SurvivalConfig {
        /** Base support% below which GAIN_SUPPORT is forced regardless of style. */
        public int supportCritical = 20;
        /** Base morale below which RESTORE_MORALE is forced. */
        public int moraleCritical  = 22;
        /** Base corruption above which SURVIVE_SCANDAL is forced. */
        public int corruptionCritical = 80;
        /** Base coins below which RAISE_FUNDS is forced. */
        public int coinsCritical = 35;
        /**
         * survivalFactor = survivalFactorBase − riskTolerance × survivalFactorRiskScale.
         * Cautious AI (low risk) → factor > 1 → panics earlier.
         * Bold AI (high risk)   → factor < 1 → holds longer.
         */
        public double survivalFactorBase      = 1.1;
        public double survivalFactorRiskScale = 0.2;
    }

    // ─────────────────────────────────────────────────────────────────────────
    // SECTION 2: Election window (chooseIntent + electionTimingScore)
    // ─────────────────────────────────────────────────────────────────────────
    private ElectionConfig election = new ElectionConfig();

    public static class ElectionConfig {
        /** Turns remaining ≤ this → trigger PREPARE_ELECTION if support below target. */
        public int windowTurns = 6;
        /**
         * "Broad surge" window — all parties push support in this many final turns
         * regardless of whether they've hit electionSupportTarget.
         */
        public int broadSurgeTurns = 10;
        /** Max support% for the broad surge to apply (parties already dominant skip it). */
        public int broadSurgeMaxSupport = 50;
        /** Total turns in one game (used to compute turnsRemaining = totalTurns − turnNumber). */
        public int totalTurns = 60;
    }

    // ─────────────────────────────────────────────────────────────────────────
    // SECTION 3: Role-specific intent thresholds
    // ─────────────────────────────────────────────────────────────────────────
    private RoleThresholds roleThresholds = new RoleThresholds();

    public static class RoleThresholds {
        public RoleThresholdSet government  = new RoleThresholdSet(40, 30, 80, 45, 50, 34);
        public RoleThresholdSet opposition  = new RoleThresholdSet(35, 20, 70, 38, 55, 30);
        public RoleThresholdSet thirdParty  = new RoleThresholdSet(38, 28, 75, 40, 50, 32);

        public static class RoleThresholdSet {
            public double lowMorale;
            public double lowSupport;
            public double lowCoins;
            public double electionSupportTarget;
            public double corruptionCrisis;
            public double mediaCrisis;
            // Misc thresholds also stored in AiProfile.defaultIntentThresholds
            public double governmentNoConfidenceSupport = 30.0;
            public double governmentNoConfidenceMorale  = 35.0;
            public double noConfidenceRiskTolerance     = 0.55;
            public double opponentCorruptionAttack      = 38.0;
            public double scandalAttackPreference       = 0.55;
            public double needMoraleLow                 = 50.0;
            public double needMediaLow                  = 45.0;
            public double needSupportLow                = 30.0;
            public double needCorruptionHigh            = 40.0;
            public double needCoinsLow                  = 100.0;
            public double reactionSupportCrisis         = 25.0;

            public RoleThresholdSet() {}

            public RoleThresholdSet(double lowMorale, double lowSupport, double lowCoins,
                                    double electionSupportTarget, double corruptionCrisis,
                                    double mediaCrisis) {
                this.lowMorale             = lowMorale;
                this.lowSupport            = lowSupport;
                this.lowCoins              = lowCoins;
                this.electionSupportTarget = electionSupportTarget;
                this.corruptionCrisis      = corruptionCrisis;
                this.mediaCrisis           = mediaCrisis;
            }
        }
    }

    // ─────────────────────────────────────────────────────────────────────────
    // SECTION 4: Card scoring weights (replaces AiProfile.defaultScoringWeights)
    // ─────────────────────────────────────────────────────────────────────────
    private ScoringWeights scoringWeights = new ScoringWeights();

    public static class ScoringWeights {
        public double cardAiPriority             = 2.0;
        public double cardPublicImpact           = 1.5;
        public double cardRiskBase               = 2.0;
        public double selfPublicSupport          = 4.0;
        public double selfMediaBase              = 1.5;
        public double selfMorale                 = 2.0;
        public double selfCorruptionPenaltyBase  = 2.5;
        public double selfCoins                  = 0.2;
        public double opponentPublicSupportDamage= 3.0;
        public double opponentMediaDamage        = 1.5;
        public double opponentCorruptionGainBase = 1.5;
        public double intentFit                  = 8.0;
        public double roleCategoryFit            = 5.0;
        public double opponentScandalWeakness    = 8.0;
        public double welfareCategoryFit         = 4.0;
        public double mediaCategoryFit           = 4.0;
        public double categoryPreference         = 5.0;
        public double needMoraleBoost            = 7.0;
        public double needMediaBoost             = 7.0;
        public double needSupportBoost           = 8.0;
        public double needCorruptionDefenseBoost = 8.0;
        public double needLowCoinFundBoost       = 6.0;
        public double unaffordableBasePenalty    = 30.0;
        public double lowCoinCostPenalty         = 0.35;
        public double reactionIntentBoost        = 2.0;
        public double reactionCrisisSupportBoost = 2.0;
        public double reactionRiskBase           = 0.08;
        public double reactionRiskToleranceDiscount = 0.06;
        public double ideologyStrongFit          = 5.0;
        public double ideologyWeakFit            = -4.0;
        public double ideologyCategoryFit        = 3.0;
        public double electionCategoryBoost      = 6.0;
        public double electionScandalPenalty     = -3.0;
    }

    // ─────────────────────────────────────────────────────────────────────────
    // SECTION 5: Card diversity penalties
    // ─────────────────────────────────────────────────────────────────────────
    private CardDiversityConfig cardDiversity = new CardDiversityConfig();

    public static class CardDiversityConfig {
        /** Max times any card can be played per game (human + AI). */
        public int maxUsesPerGame = 3;
        /** Score penalty when a card has already been played once this game. */
        public double usedOncePenalty  = -8.0;
        /** Score penalty when a card has been played twice (strong deterrent). */
        public double usedTwicePenalty = -35.0;
        /** Additional penalty when the same card was played last turn (consecutive). */
        public double consecutiveRepeatPenalty = -20.0;
    }

    // ─────────────────────────────────────────────────────────────────────────
    // SECTION 6: Intent-card consistency + attacker health
    // ─────────────────────────────────────────────────────────────────────────
    private AttackConfig attack = new AttackConfig();

    public static class AttackConfig {
        /** Score penalty when a self-recovery intent tries to play an attack card. */
        public double intentMismatchPenalty = -50.0;
        /**
         * Denominator for attackerHealthFactor = min(1, support / denominator).
         * Lower value → factor reaches 1.0 at lower support → attack scoring barely dampened.
         * Higher value → attack bonus scales up only for wealthy, high-support parties.
         */
        public double attackerHealthDenominator = 30.0;
        /** Bonus score when targeting a coin-bankrupt opponent. */
        public double vulnerabilityCoinBonus       = 15.0;
        /** Bonus score when targeting a morale-broken opponent. */
        public double vulnerabilityMoraleBonus     = 15.0;
        /** Bonus score when targeting a corruption-exposed opponent. */
        public double vulnerabilityCorruptionBonus = 15.0;
        /** Bonus score when targeting a near-defeat opponent (support ≤ threshold). */
        public double vulnerabilitySupportBonus    = 10.0;
        /** Target-support threshold below which vulnerabilitySupportBonus applies. */
        public int vulnerabilitySupportThreshold   = 12;
        /** Target-coins threshold below which vulnerabilityCoinBonus applies. */
        public int vulnerabilityCoinThreshold      = 25;
        /** Target-morale threshold below which vulnerabilityMoraleBonus applies. */
        public int vulnerabilityMoraleThreshold    = 20;
        /** Target-corruption threshold above which vulnerabilityCorruptionBonus applies. */
        public int vulnerabilityCorruptionThreshold = 75;
        /** Grudge multiplier: grudge × this × attackerHealthFactor = score added. */
        public double grudgeBoostMultiplier = 3.0;
        /** Penalty applied when card requires a target but no opponent available (NAP). */
        public double noTargetPenalty = -100.0;
    }

    // ─────────────────────────────────────────────────────────────────────────
    // SECTION 7: Style-specific card scoring multipliers
    // ─────────────────────────────────────────────────────────────────────────
    private StyleMultipliers styleMultipliers = new StyleMultipliers();

    public static class StyleMultipliers {
        // STRENGTH_BUILDER
        public double sbSelfSupportMult   = 1.3;
        public double sbSelfMediaMult     = 1.5;
        public double sbSelfMoraleMult    = 1.5;
        public double sbSelfCoinsMult     = 1.5;
        public double sbSelfCorruptMult   = 1.8;
        public double sbOppSupportMult    = 0.5;
        public double sbOppMediaMult      = 0.5;
        public double sbOppCorruptMult    = 0.5;
        public double sbScandalPenalty    = -15.0;

        // AGGRESSIVE_ATTACKER
        public double aaOppSupportMult    = 2.0;
        public double aaOppMediaMult      = 2.0;
        public double aaOppCorruptMult    = 2.0;
        public double aaSelfSupportMult   = 0.7;
        public double aaSelfCoinsMult     = 0.5;
        public double aaScandalBonus      = 15.0;

        // LATE_STRIKER (early phase: turn < lateStrikerTurn)
        public int    lateStrikerTurn         = 40;
        public double lsEarlySelfSupportMult  = 1.3;
        public double lsEarlySelfMoraleMult   = 1.4;
        public double lsEarlySelfCoinsMult    = 1.4;
        public double lsEarlyOppSupportMult   = 0.3;
        public double lsEarlyScandalPenalty   = -12.0;
        // Late phase (turn >= lateStrikerTurn)
        public double lsLateOppSupportMult    = 2.5;
        public double lsLateOppMediaMult      = 2.0;
        public double lsLateScandalBonus      = 18.0;

        // AGGRESSIVE_BIDDER
        public double abSelfCoinsMult         = 2.0;
        public double abSelfMoraleMult        = 1.8;
        public double abOrgResourceBonus      = 12.0;
    }

    // ─────────────────────────────────────────────────────────────────────────
    // SECTION 8: Dynamic safety thresholds (in-scoreCard coin/morale/support/corruption)
    // ─────────────────────────────────────────────────────────────────────────
    private SafetyThresholds safetyThresholds = new SafetyThresholds();

    public static class SafetyThresholds {
        // Coin safety
        public int coinCrisisThreshold   = 100;  // Below this → encourage coin generators
        public int coinCritical          = 25;    // Below this → massive penalty
        public int coinHighRisk          = 50;
        public int coinMediumRisk        = 75;
        public int coinLowRisk           = 100;
        public double coinCriticalPenalty     = 80.0;
        public double coinCriticalPerUnit     = 3.0;
        public double coinHighRiskPenalty     = 40.0;
        public double coinMediumRiskPenalty   = 20.0;
        public double coinLowRiskPenalty      = 5.0;
        public double coinCrisisBonus         = 2.5; // Multiplier for coin-gen cards when coins < crisisThreshold

        // Morale safety
        public int moraleCrisisThreshold = 50;
        public int moraleCritical        = 15;
        public int moraleHighRisk        = 25;
        public int moraleMediumRisk      = 35;
        public int moraleLowRisk         = 50;
        public double moraleCriticalPenalty   = 100.0;
        public double moraleCriticalPerUnit   = 4.0;
        public double moraleHighRiskPenalty   = 50.0;
        public double moraleMediumRiskPenalty = 25.0;
        public double moraleLowRiskPenalty    = 10.0;
        public double moraleCrisisBonus       = 3.0; // Multiplier for morale-restore cards in crisis

        // Support safety
        public int supportCrisisThreshold = 25;
        public int supportCritical        = 6;   // < 5 is defeat
        public int supportHighRisk        = 10;
        public int supportMediumRisk      = 15;
        public int supportLowRisk         = 20;
        public double supportCriticalPenalty   = 100.0;
        public double supportCriticalPerUnit   = 5.0;
        public double supportHighRiskPenalty   = 50.0;
        public double supportMediumRiskPenalty = 25.0;
        public double supportLowRiskPenalty    = 10.0;
        public double supportCrisisBonus       = 4.0; // Multiplier for support-boost cards in crisis

        // Corruption safety
        public int corruptionCrisisThreshold = 60; // Above this → encourage corruption reducers
        public int corruptionCritical        = 90; // Above this → massive penalty
        public int corruptionHighRisk        = 80;
        public int corruptionMediumRisk      = 70;
        public double corruptionCriticalPenalty = 100.0;
        public double corruptionCriticalPerUnit = 5.0;
        public double corruptionHighRiskPenalty = 50.0;
        public double corruptionMediumRiskPenalty = 25.0;
        public double corruptionCrisisBonus     = 4.0; // Multiplier for corruption-reduce cards
    }

    // ─────────────────────────────────────────────────────────────────────────
    // SECTION 9: Intent effects fit multipliers
    // ─────────────────────────────────────────────────────────────────────────
    private IntentFitConfig intentFit = new IntentFitConfig();

    public static class IntentFitConfig {
        public double raiseFundsPosMultiplier  = 0.3;
        public double raiseFundsNegMultiplier  = 0.25;
        public double restoreMoralePosMultiplier = 0.4;
        public double restoreMoraleNegMultiplier = 0.3;
        public double gainSupportPosMultiplier   = 0.5;
        public double gainSupportNegMultiplier   = 0.4;
        public double defendImagePosMultiplier   = 0.4;
        public double defendImageNegMultiplier   = 0.3;
        public double surviveScandPosMultiplier  = 0.5;
        public double surviveScandNegMultiplier  = 0.4;
        // ATTACK_RIVAL offensive sub-weights
        public double attackSupportDmgMult  = 0.4;
        public double attackMediaDmgMult    = 0.2;
        public double attackMoraleDmgMult   = 0.2;
        public double attackCoinsDmgMult    = 0.2;
        public double attackCorruptGainMult = 0.2;
    }

    // ─────────────────────────────────────────────────────────────────────────
    // SECTION 10: Bidding crisis config
    // ─────────────────────────────────────────────────────────────────────────
    private BiddingConfig bidding = new BiddingConfig();

    public static class BiddingConfig {
        /** Support threshold below which a party won't bid on offensive rewards. */
        public int crisisSupportThreshold = 22;
        /** Morale threshold below which a party won't bid on offensive rewards. */
        public int crisisMoraleThreshold  = 25;
        /** Coins threshold below which a party won't bid on offensive rewards. */
        public int crisisCoinsThreshold   = 40;
    }

    // ─────────────────────────────────────────────────────────────────────────
    // SECTION 11: Coalition / NAP config
    // ─────────────────────────────────────────────────────────────────────────
    private CoalitionConfig coalition = new CoalitionConfig();

    public static class CoalitionConfig {
        /** Human support lead (%) above each AI party that triggers free coalition pact. */
        public int humanDominanceThreshold = 10;
        /** Duration of the free defensive NAP in turns. */
        public int freeNapDurationTurns = 8;
        /** Early-game NAP offers only happen at or before this turn. */
        public int earlyGameNapTurnLimit = 20;
        /** Minimum coins required to offer an early-game NAP. */
        public int earlyGameNapCoinMin = 80;
        /** Cost in coins that the sender pays for an early-game NAP. */
        public int earlyGameNapCost = 5;
        /** Proactive exchange offer: min coins for the sender to offer 50 coins to another. */
        public int exchangeCoinsForSupportSenderMin = 150;
        /** Proactive exchange offer: min coins for the sender to offer 30 coins for morale. */
        public int exchangeCoinsForMoraleSenderMin  = 130;
        /** Target's support threshold below which the coins-for-support exchange is triggered. */
        public int exchangeTargetCoinLow = 100;
        /** Offered coins in the coins-for-support exchange. */
        public int exchangeOfferedCoinsForSupport = 50;
        /** Requested support in the coins-for-support exchange. */
        public int exchangeRequestedSupport = 3;
        /** Offered coins in the coins-for-morale exchange. */
        public int exchangeOfferedCoinsForMorale = 30;
        /** Requested morale in the coins-for-morale exchange. */
        public int exchangeRequestedMorale = 5;
    }

    // ─────────────────────────────────────────────────────────────────────────
    // SECTION 12: Role defaults (style, riskTolerance, etc.)
    // ─────────────────────────────────────────────────────────────────────────
    private RoleDefaults roleDefaults = new RoleDefaults();

    public static class RoleDefaults {
        public RoleDefault government = new RoleDefault(
            "STRENGTH_BUILDER", 0.30, 0.10, 0.70, 0.50, 0.60, 0.80,
            Map.of("governance", 0.8, "positive_service", 0.9, "organization_resource", 0.9, "media_narrative", 0.6)
        );
        public RoleDefault opposition = new RoleDefault(
            "AGGRESSIVE_ATTACKER", 0.85, 0.90, 0.30, 0.20, 0.50, 0.50,
            Map.of("scandal_accusation", 0.95, "agitation_movement", 0.9, "media_narrative", 0.7)
        );
        public RoleDefault thirdParty = new RoleDefault(
            "BALANCED_STRATEGIST", 0.50, 0.50, 0.50, 0.50, 0.50, 0.60,
            Map.of("governance", 0.6, "positive_service", 0.6, "organization_resource", 0.6,
                   "scandal_accusation", 0.6, "agitation_movement", 0.6)
        );

        public static class RoleDefault {
            public String style;
            public double riskTolerance;
            public double scandalPreference;
            public double welfarePreference;
            public double coalitionPreference;
            public double mediaPreference;
            public double ideologyStrictness;
            public Map<String, Double> categoryPreferences;

            public RoleDefault() {}

            public RoleDefault(String style, double riskTolerance, double scandalPreference,
                               double welfarePreference, double coalitionPreference,
                               double mediaPreference, double ideologyStrictness,
                               Map<String, Double> categoryPreferences) {
                this.style               = style;
                this.riskTolerance       = riskTolerance;
                this.scandalPreference   = scandalPreference;
                this.welfarePreference   = welfarePreference;
                this.coalitionPreference = coalitionPreference;
                this.mediaPreference     = mediaPreference;
                this.ideologyStrictness  = ideologyStrictness;
                this.categoryPreferences = new LinkedHashMap<>(categoryPreferences);
            }
        }
    }

    // ─────────────────────────────────────────────────────────────────────────
    // Getters & Setters
    // ─────────────────────────────────────────────────────────────────────────

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public int getVersion() { return version; }
    public void setVersion(int version) { this.version = version; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    public boolean isActive() { return active; }
    public void setActive(boolean active) { this.active = active; }

    public Instant getCreatedAt() { return createdAt; }
    public void setCreatedAt(Instant createdAt) { this.createdAt = createdAt; }

    public String getApprovedBy() { return approvedBy; }
    public void setApprovedBy(String approvedBy) { this.approvedBy = approvedBy; }

    public SurvivalConfig getSurvival() { return survival; }
    public void setSurvival(SurvivalConfig survival) { this.survival = survival; }

    public ElectionConfig getElection() { return election; }
    public void setElection(ElectionConfig election) { this.election = election; }

    public RoleThresholds getRoleThresholds() { return roleThresholds; }
    public void setRoleThresholds(RoleThresholds roleThresholds) { this.roleThresholds = roleThresholds; }

    public ScoringWeights getScoringWeights() { return scoringWeights; }
    public void setScoringWeights(ScoringWeights scoringWeights) { this.scoringWeights = scoringWeights; }

    public CardDiversityConfig getCardDiversity() { return cardDiversity; }
    public void setCardDiversity(CardDiversityConfig cardDiversity) { this.cardDiversity = cardDiversity; }

    public AttackConfig getAttack() { return attack; }
    public void setAttack(AttackConfig attack) { this.attack = attack; }

    public StyleMultipliers getStyleMultipliers() { return styleMultipliers; }
    public void setStyleMultipliers(StyleMultipliers styleMultipliers) { this.styleMultipliers = styleMultipliers; }

    public SafetyThresholds getSafetyThresholds() { return safetyThresholds; }
    public void setSafetyThresholds(SafetyThresholds safetyThresholds) { this.safetyThresholds = safetyThresholds; }

    public IntentFitConfig getIntentFit() { return intentFit; }
    public void setIntentFit(IntentFitConfig intentFit) { this.intentFit = intentFit; }

    public BiddingConfig getBidding() { return bidding; }
    public void setBidding(BiddingConfig bidding) { this.bidding = bidding; }

    public CoalitionConfig getCoalition() { return coalition; }
    public void setCoalition(CoalitionConfig coalition) { this.coalition = coalition; }

    public RoleDefaults getRoleDefaults() { return roleDefaults; }
    public void setRoleDefaults(RoleDefaults roleDefaults) { this.roleDefaults = roleDefaults; }
}
