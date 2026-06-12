package com.politicalsim.ai;

import com.politicalsim.content.CardDefinition;
import com.politicalsim.content.NewsReactionDefinition;
import com.politicalsim.game.GameSession;
import com.politicalsim.party.Ideology;
import com.politicalsim.party.PartyRole;
import com.politicalsim.party.PartyState;
import com.politicalsim.party.PartyStats;
import java.util.List;
import java.util.Map;
import org.springframework.stereotype.Service;

@Service
public class AiDecisionService {

    public AiDecision chooseCard(GameSession session, PartyState party, PartyState opponent, List<CardDefinition> cards) {
        AiIntent intent = chooseIntent(session, party, opponent);
        CardDefinition card = cards.stream()
                .filter(CardDefinition::isActive)
                .filter(candidate -> candidate.getRoleAllowed().contains(party.getRole().name()))
                .max((left, right) -> Double.compare(
                        scoreCard(session, party, opponent, left, intent),
                        scoreCard(session, party, opponent, right, intent)
                ))
                .orElseThrow(() -> new IllegalArgumentException("No cards found for role " + party.getRole()));
        return new AiDecision(intent, card);
    }

    public NewsReactionDefinition chooseReaction(PartyState party, AiIntent intent, List<NewsReactionDefinition> reactions) {
        return reactions.stream()
                .filter(reaction -> reaction.getRoleAllowed().contains(party.getRole().name()))
                .max((left, right) -> Double.compare(
                        scoreReaction(party, left, intent),
                        scoreReaction(party, right, intent)
                ))
                .orElse(null);
    }

    public AiIntent chooseIntent(GameSession session, PartyState party, PartyState opponent) {
        PartyStats stats = party.getStats();
        AiProfile profile = profileFor(party);
        int monthsLeft = Math.max(0, 60 - session.getMonthInCycle() + 1);

        if (party.getRole() != PartyRole.GOVERNMENT
                && session.getGovernmentParty().getStats().getPublicSupport() < threshold(profile, "governmentNoConfidenceSupport")
                && session.getGovernmentParty().getStats().getPartyMorale() < threshold(profile, "governmentNoConfidenceMorale")
                && profile.getRiskTolerance() >= threshold(profile, "noConfidenceRiskTolerance")) {
            return AiIntent.FORCE_NO_CONFIDENCE;
        }
        if (stats.getCoins() < threshold(profile, "lowCoins")) {
            return AiIntent.RAISE_FUNDS;
        }
        if (stats.getCorruptionScore() > threshold(profile, "corruptionCrisis")
                || stats.getMediaImage() < threshold(profile, "mediaCrisis")) {
            return stats.getCorruptionScore() > threshold(profile, "corruptionCrisis")
                    ? AiIntent.SURVIVE_SCANDAL : AiIntent.DEFEND_IMAGE;
        }
        if (stats.getPartyMorale() < threshold(profile, "lowMorale")) {
            return AiIntent.RESTORE_MORALE;
        }
        if (monthsLeft <= threshold(profile, "electionWindowMonths")
                && stats.getPublicSupport() < threshold(profile, "electionSupportTarget")) {
            return AiIntent.PREPARE_ELECTION;
        }
        if (opponent.getStats().getCorruptionScore() > threshold(profile, "opponentCorruptionAttack")
                && profile.getScandalPreference() >= threshold(profile, "scandalAttackPreference")) {
            return AiIntent.ATTACK_RIVAL;
        }
        if (stats.getPublicSupport() < threshold(profile, "lowSupport")) {
            return AiIntent.GAIN_SUPPORT;
        }

        return switch (profile.getStyle()) {
            case STRENGTH_BUILDER -> AiIntent.RESTORE_MORALE;
            case AGGRESSIVE_ATTACKER -> AiIntent.ATTACK_RIVAL;
            case LATE_STRIKER -> (session.getTurnNumber() >= 40) ? AiIntent.ATTACK_RIVAL : AiIntent.GAIN_SUPPORT;
            case AGGRESSIVE_BIDDER -> AiIntent.RAISE_FUNDS;
            case BALANCED_STRATEGIST -> stats.getPublicSupport() < 30 ? AiIntent.GAIN_SUPPORT : AiIntent.RESTORE_MORALE;
            default -> AiIntent.RESTORE_MORALE;
        };
    }

    private double scoreCard(GameSession session, PartyState party, PartyState opponent, CardDefinition card, AiIntent intent) {
        PartyStats stats = party.getStats();
        AiProfile profile = profileFor(party);
        Map<String, Object> selfEffects = partyEffect(card.getVisibleEffects(), "selfParty");
        Map<String, Object> opponentEffects = partyEffect(card.getVisibleEffects(), "opponentParty");

        double score = doubleValue(card.getWeights().get("basePlayWeight"));
        score += doubleValue(card.getWeights().get("aiPriorityWeight")) * weight(profile, "cardAiPriority");
        score += doubleValue(card.getWeights().get("publicImpactWeight")) * weight(profile, "cardPublicImpact");
        score -= doubleValue(card.getWeights().get("riskWeight")) * (weight(profile, "cardRiskBase") - profile.getRiskTolerance());

        double selfSupportVal = intValue(selfEffects.get("publicSupport")) * weight(profile, "selfPublicSupport");
        double selfMediaVal = intValue(selfEffects.get("mediaImage")) * (weight(profile, "selfMediaBase") + profile.getMediaPreference());
        double selfMoraleVal = intValue(selfEffects.get("partyMorale")) * weight(profile, "selfMorale");
        double selfCorruptionVal = intValue(selfEffects.get("corruptionScore")) * (weight(profile, "selfCorruptionPenaltyBase") + profile.getIdeologyStrictness());
        double selfCoinsVal = intValue(selfEffects.get("coins")) * weight(profile, "selfCoins");

        double oppSupportVal = intValue(opponentEffects.get("publicSupport")) * weight(profile, "opponentPublicSupportDamage");
        double oppMediaVal = intValue(opponentEffects.get("mediaImage")) * weight(profile, "opponentMediaDamage");
        double oppCorruptionVal = intValue(opponentEffects.get("corruptionScore")) * (weight(profile, "opponentCorruptionGainBase") + profile.getScandalPreference());

        // Strategy-based adjustments
        if (profile.getStyle() == AiStyle.STRENGTH_BUILDER) {
            selfSupportVal *= 1.3;
            selfMediaVal *= 1.5;
            selfMoraleVal *= 1.5;
            selfCoinsVal *= 1.5;
            selfCorruptionVal *= 1.8; // High aversion to corruption
            oppSupportVal *= 0.5;
            oppMediaVal *= 0.5;
            oppCorruptionVal *= 0.5;
            if (oneOf(card.getCategory(), "scandal", "scandal_accusation", "agitation", "agitation_movement")) {
                score -= 15.0;
            }
        } else if (profile.getStyle() == AiStyle.AGGRESSIVE_ATTACKER) {
            oppSupportVal *= 2.0;
            oppMediaVal *= 2.0;
            oppCorruptionVal *= 2.0;
            selfSupportVal *= 0.7;
            selfCoinsVal *= 0.5;
            if (oneOf(card.getCategory(), "scandal", "scandal_accusation", "agitation", "agitation_movement")) {
                score += 15.0;
            }
        } else if (profile.getStyle() == AiStyle.LATE_STRIKER) {
            int turn = session.getTurnNumber();
            if (turn < 40) {
                selfSupportVal *= 1.3;
                selfMoraleVal *= 1.4;
                selfCoinsVal *= 1.4;
                oppSupportVal *= 0.3;
                if (oneOf(card.getCategory(), "scandal", "scandal_accusation", "agitation", "agitation_movement")) {
                    score -= 12.0;
                }
            } else {
                oppSupportVal *= 2.5;
                oppMediaVal *= 2.0;
                if (oneOf(card.getCategory(), "scandal", "scandal_accusation", "agitation", "agitation_movement", "media_narrative")) {
                    score += 18.0;
                }
            }
        } else if (profile.getStyle() == AiStyle.AGGRESSIVE_BIDDER) {
            selfCoinsVal *= 2.0;
            selfMoraleVal *= 1.8;
            if ("organization_resource".equals(card.getCategory())) {
                score += 12.0;
            }
        }

        score += selfSupportVal;
        score += selfMediaVal;
        score += selfMoraleVal;
        score -= selfCorruptionVal;
        score += selfCoinsVal;

        score -= oppSupportVal;
        score -= oppMediaVal;
        score += oppCorruptionVal;

        score += intentFit(intent, card.getCategory()) * weight(profile, "intentFit");
        score += categoryFitScore(party, opponent, card.getCategory(), profile);
        score += needScore(stats, card.getCategory(), profile);
        score += ideologyFitScore(party, card);
        score += electionTimingScore(session, card.getCategory(), profile);

        if (stats.getCoins() < card.getCost()) {
            score -= weight(profile, "unaffordableBasePenalty") + (card.getCost() - stats.getCoins());
        } else if (stats.getCoins() < threshold(profile, "needCoinsLow")) {
            score -= card.getCost() * weight(profile, "lowCoinCostPenalty");
        }

        score += card.getCardKey().hashCode() % 7 * 0.01;
        return score;
    }

    private double scoreReaction(PartyState party, NewsReactionDefinition reaction, AiIntent intent) {
        PartyStats stats = party.getStats();
        AiProfile profile = profileFor(party);
        Map<String, Object> effects = partyEffect(reaction.getEffects(), "playerParty");
        double score = reaction.getWeight();

        score += intValue(effects.get("publicSupport")) * weight(profile, "selfPublicSupport");
        score += intValue(effects.get("mediaImage")) * (weight(profile, "selfMediaBase") + profile.getMediaPreference());
        score += intValue(effects.get("partyMorale")) * weight(profile, "selfMorale");
        score -= intValue(effects.get("corruptionScore")) * (weight(profile, "selfCorruptionPenaltyBase") + profile.getIdeologyStrictness());
        score += intValue(effects.get("coins")) * weight(profile, "selfCoins");

        if (intent == AiIntent.GAIN_SUPPORT || intent == AiIntent.PREPARE_ELECTION) {
            score += intValue(effects.get("publicSupport")) * weight(profile, "reactionIntentBoost");
        }
        if (intent == AiIntent.DEFEND_IMAGE || intent == AiIntent.SURVIVE_SCANDAL) {
            score += intValue(effects.get("mediaImage")) * weight(profile, "reactionIntentBoost");
            score -= Math.max(0, intValue(effects.get("corruptionScore"))) * weight(profile, "reactionIntentBoost");
        }
        if (intent == AiIntent.RESTORE_MORALE) {
            score += intValue(effects.get("partyMorale")) * weight(profile, "reactionIntentBoost");
        }
        if (stats.getPublicSupport() < threshold(profile, "reactionSupportCrisis")) {
            score += intValue(effects.get("publicSupport")) * weight(profile, "reactionCrisisSupportBoost");
        }

        score -= doubleValue(reaction.getRisk().get("chance")) * (weight(profile, "reactionRiskBase")
                - Math.min(weight(profile, "reactionRiskToleranceDiscount"),
                        profile.getRiskTolerance() * weight(profile, "reactionRiskToleranceDiscount")));
        score += reaction.getReactionKey().hashCode() % 5 * 0.01;
        return score;
    }

    private double intentFit(AiIntent intent, String category) {
        return switch (intent) {
            case GAIN_SUPPORT, PREPARE_ELECTION -> oneOf(category, "positive_service", "governance", "media_narrative") ? 1 : 0;
            case RESTORE_MORALE -> oneOf(category, "organization_resource", "positive_service", "ideology_identity") ? 1 : 0;
            case ATTACK_RIVAL, FORCE_NO_CONFIDENCE -> oneOf(category, "scandal", "scandal_accusation", "agitation", "agitation_movement", "media_narrative") ? 1 : 0;
            case DEFEND_IMAGE, SURVIVE_SCANDAL -> oneOf(category, "defensive_counter", "media_narrative", "positive_service") ? 1 : 0;
            case RAISE_FUNDS -> "organization_resource".equals(category) ? 1 : 0;
        };
    }

    private double categoryFitScore(PartyState party, PartyState opponent, String category, AiProfile profile) {
        double score = 0;
        if (party.getRole() == PartyRole.GOVERNMENT && oneOf(category, "governance", "defensive_counter")) {
            score += weight(profile, "roleCategoryFit");
        }
        if (party.getRole() != PartyRole.GOVERNMENT
                && oneOf(category, "scandal", "scandal_accusation", "agitation", "agitation_movement", "positive_service")) {
            score += weight(profile, "roleCategoryFit");
        }
        if (party.getRole() != PartyRole.GOVERNMENT
                && opponent.getStats().getCorruptionScore() > threshold(profile, "opponentCorruptionAttack")
                && oneOf(category, "scandal", "scandal_accusation")) {
            score += weight(profile, "opponentScandalWeakness") * profile.getScandalPreference();
        }
        if ("positive_service".equals(category) || "governance".equals(category)) {
            score += weight(profile, "welfareCategoryFit") * profile.getWelfarePreference();
        }
        if ("media_narrative".equals(category)) {
            score += weight(profile, "mediaCategoryFit") * profile.getMediaPreference();
        }
        score += preference(profile, category) * weight(profile, "categoryPreference");
        return score;
    }

    private double needScore(PartyStats stats, String category, AiProfile profile) {
        double score = 0;
        if (stats.getPartyMorale() < threshold(profile, "needMoraleLow")
                && oneOf(category, "organization_resource", "positive_service")) {
            score += weight(profile, "needMoraleBoost");
        }
        if (stats.getMediaImage() < threshold(profile, "needMediaLow")
                && oneOf(category, "media_narrative", "defensive_counter")) {
            score += weight(profile, "needMediaBoost");
        }
        if (stats.getPublicSupport() < threshold(profile, "needSupportLow")
                && oneOf(category, "positive_service", "governance", "agitation", "agitation_movement")) {
            score += weight(profile, "needSupportBoost");
        }
        if (stats.getCorruptionScore() > threshold(profile, "needCorruptionHigh") && "defensive_counter".equals(category)) {
            score += weight(profile, "needCorruptionDefenseBoost");
        }
        if (stats.getCoins() < threshold(profile, "needCoinsLow") && "organization_resource".equals(category)) {
            score += weight(profile, "needLowCoinFundBoost");
        }
        return score;
    }

    @SuppressWarnings("unchecked")
    private double ideologyFitScore(PartyState party, CardDefinition card) {
        if (party.getIdeology() == null || card.getIdeologyTags() == null) {
            return 0;
        }
        AiProfile profile = profileFor(party);
        Object strongFit = card.getIdeologyTags().get("strongFit");
        Object weakFit = card.getIdeologyTags().get("weakFit");
        String ideology = party.getIdeology().name();

        if (strongFit instanceof List<?> list && list.contains(ideology)) {
            return weight(profile, "ideologyStrongFit") * profile.getIdeologyStrictness();
        }
        if (weakFit instanceof List<?> list && list.contains(ideology)) {
            return weight(profile, "ideologyWeakFit") * profile.getIdeologyStrictness();
        }
        Ideology partyIdeology = party.getIdeology();
        if (partyIdeology == Ideology.ANTI_CORRUPTION && oneOf(card.getCategory(), "scandal", "scandal_accusation")) {
            return weight(profile, "ideologyCategoryFit") * profile.getIdeologyStrictness();
        }
        if (partyIdeology == Ideology.DEVELOPMENT_FIRST && "governance".equals(card.getCategory())) {
            return weight(profile, "ideologyCategoryFit") * profile.getIdeologyStrictness();
        }
        if (partyIdeology == Ideology.REGIONAL_PRIDE && "ideology_identity".equals(card.getCategory())) {
            return weight(profile, "ideologyCategoryFit") * profile.getIdeologyStrictness();
        }
        return 0;
    }

    private double electionTimingScore(GameSession session, String category, AiProfile profile) {
        int monthsLeft = Math.max(0, 60 - session.getMonthInCycle() + 1);
        if (monthsLeft > threshold(profile, "electionWindowMonths")) {
            return 0;
        }
        if (oneOf(category, "positive_service", "media_narrative", "governance")) {
            return weight(profile, "electionCategoryBoost");
        }
        if (oneOf(category, "scandal", "scandal_accusation")) {
            return weight(profile, "electionScandalPenalty");
        }
        return 0;
    }

    @SuppressWarnings("unchecked")
    private Map<String, Object> partyEffect(Map<String, Object> effects, String key) {
        Object value = effects.get(key);
        if (value instanceof Map<?, ?> map) {
            return (Map<String, Object>) map;
        }
        Object scheduled = effects.get("scheduled");
        if (scheduled instanceof List<?> list && !list.isEmpty() && list.get(0) instanceof Map<?, ?> scheduledMap) {
            Object nestedEffects = scheduledMap.get("effects");
            if (nestedEffects instanceof Map<?, ?> nestedMap && nestedMap.get(key) instanceof Map<?, ?> partyMap) {
                return (Map<String, Object>) partyMap;
            }
        }
        return Map.of();
    }

    private AiProfile profileFor(PartyState party) {
        return party.getAiProfile() == null ? AiProfile.defaultForRole(party.getRole()) : party.getAiProfile();
    }

    private double threshold(AiProfile profile, String key) {
        return profileValue(profile.getIntentThresholds(), AiProfile.defaultIntentThresholds(), key);
    }

    private double weight(AiProfile profile, String key) {
        return profileValue(profile.getScoringWeights(), AiProfile.defaultScoringWeights(), key);
    }

    private double preference(AiProfile profile, String category) {
        if (profile.getCategoryPreferences() == null) {
            return 0;
        }
        return profile.getCategoryPreferences().getOrDefault(category, 0.0);
    }

    private double profileValue(Map<String, Double> overrides, Map<String, Double> defaults, String key) {
        if (overrides != null && overrides.get(key) != null) {
            return overrides.get(key);
        }
        return defaults.getOrDefault(key, 0.0);
    }

    private boolean oneOf(String value, String... options) {
        for (String option : options) {
            if (option.equals(value)) {
                return true;
            }
        }
        return false;
    }

    private int intValue(Object value) {
        if (value instanceof Number number) {
            return number.intValue();
        }
        return 0;
    }

    private double doubleValue(Object value) {
        if (value instanceof Number number) {
            return number.doubleValue();
        }
        return 0;
    }
}
