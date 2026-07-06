package com.politicalsim.ai;

import com.politicalsim.content.CardDefinition;
import com.politicalsim.content.NewsReactionDefinition;
import com.politicalsim.game.RewardDefinition;
import com.politicalsim.game.GameSession;
import com.politicalsim.game.RoundSubmission;
import com.politicalsim.party.BuildingProject;
import com.politicalsim.party.Ideology;
import com.politicalsim.party.PartyRole;
import com.politicalsim.party.PartyState;
import com.politicalsim.party.PartyStats;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import com.politicalsim.game.CooperationOffer;
import com.politicalsim.game.NonAggressionPact;
import com.politicalsim.game.LegislativeBillState;
import com.politicalsim.party.ProjectState;
import com.politicalsim.content.LegislativeBillDefinition;
import com.politicalsim.content.LegislativeBillDefinitionRepository;
import org.springframework.stereotype.Service;

@Service
public class AiDecisionService {

    private final LegislativeBillDefinitionRepository billRepository;

    public AiDecisionService() {
        this.billRepository = null;
    }

    public AiDecisionService(LegislativeBillDefinitionRepository billRepository) {
        this.billRepository = billRepository;
    }

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
        // opponent may be null when ALL other active parties have non-aggression pacts with this party
        boolean hasTargetableOpponent = opponent != null;

        // Coin Crisis Override (coins <= 80)
        if (stats.getCoins() <= 80) return AiIntent.RAISE_FUNDS;

        // ── CHANGE 1: Survival override — thresholds scale with riskTolerance ───────
        // Cautious parties (low riskTolerance) panic earlier; bold ones push slightly longer.
        // riskTolerance range 0.0-1.0; factor maps to threshold multiplier 1.1 (cautious) → 0.9 (bold).
        double survivalFactor = 1.1 - (profile.getRiskTolerance() * 0.2);
        if (stats.getPublicSupport() < Math.round(20 * survivalFactor)) return AiIntent.GAIN_SUPPORT;
        if (stats.getPartyMorale()   < Math.round(22 * survivalFactor)) return AiIntent.RESTORE_MORALE;
        if (stats.getCorruptionScore() > Math.round(80 / survivalFactor)) return AiIntent.SURVIVE_SCANDAL;
        if (stats.getCoins()          < Math.round(35 * survivalFactor)) return AiIntent.RAISE_FUNDS;
        // ─────────────────────────────────────────────────────────────────────────────

        if (party.getRole() != PartyRole.GOVERNMENT) {
            int mySupport = stats.getPublicSupport();
            int maxOtherSupport = 0;
            for (PartyState p : session.getParties()) {
                if (!p.getId().equals(party.getId()) && p.isActive() && p.getRole() != PartyRole.DEFEATED) {
                    if (p.getStats().getPublicSupport() > maxOtherSupport) {
                        maxOtherSupport = p.getStats().getPublicSupport();
                    }
                }
            }
            if (mySupport > maxOtherSupport + 5) {
                return AiIntent.FORCE_NO_CONFIDENCE;
            }
        }

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

        // ── CHANGE 7: Election window fix ────────────────────────────────────────────
        // Previously used (60 - monthInCycle) which resets every cycle and is always
        // large, so PREPARE_ELECTION was effectively never triggered before turn 55.
        // Now uses actual turns remaining in the game.
        int turnsRemaining = Math.max(0, 60 - session.getTurnNumber());
        if (turnsRemaining <= (int) threshold(profile, "electionWindowMonths")
                && stats.getPublicSupport() < threshold(profile, "electionSupportTarget")) {
            return AiIntent.PREPARE_ELECTION;
        }
        // Broad election surge: all parties push support in the final 10 turns
        if (turnsRemaining <= 10 && stats.getPublicSupport() < 50) {
            return AiIntent.PREPARE_ELECTION;
        }
        // ─────────────────────────────────────────────────────────────────────────────

        // Only consider attacking if there is actually a targetable opponent (no active NAP)
        if (hasTargetableOpponent
                && opponent.getStats().getCorruptionScore() > threshold(profile, "opponentCorruptionAttack")
                && profile.getScandalPreference() >= threshold(profile, "scandalAttackPreference")) {
            return AiIntent.ATTACK_RIVAL;
        }
        if (stats.getPublicSupport() < threshold(profile, "lowSupport")) {
            return AiIntent.GAIN_SUPPORT;
        }

        // When fully pact-locked (no targetable opponent), aggressive styles fall back to self-improvement
        return switch (profile.getStyle()) {
            case STRENGTH_BUILDER -> AiIntent.RESTORE_MORALE;
            case AGGRESSIVE_ATTACKER -> hasTargetableOpponent ? AiIntent.ATTACK_RIVAL : AiIntent.GAIN_SUPPORT;
            case LATE_STRIKER -> (hasTargetableOpponent && session.getTurnNumber() >= 40) ? AiIntent.ATTACK_RIVAL : AiIntent.GAIN_SUPPORT;
            case AGGRESSIVE_BIDDER -> AiIntent.RAISE_FUNDS;
            case BALANCED_STRATEGIST -> stats.getPublicSupport() < 30 ? AiIntent.GAIN_SUPPORT : AiIntent.RESTORE_MORALE;
            default -> AiIntent.RESTORE_MORALE;
        };
    }

    private double intentEffectsFit(AiIntent intent, CardDefinition card, Map<String, Object> selfEffects, Map<String, Object> opponentEffects, AiProfile profile) {
        int netCoinEffect = 0;
        if (selfEffects.containsKey("coins")) {
            int visibleCoins = intValue(selfEffects.get("coins"));
            if (visibleCoins < 0) {
                netCoinEffect = -card.getCost();
            } else {
                netCoinEffect = visibleCoins - card.getCost();
            }
        } else {
            netCoinEffect = -card.getCost();
        }
        
        int netMoraleEffect = intValue(selfEffects.get("partyMorale"));
        int netSupportEffect = intValue(selfEffects.get("publicSupport"));
        int netCorruptionEffect = intValue(selfEffects.get("corruptionScore"));
        int netMediaEffect = intValue(selfEffects.get("mediaImage"));

        return switch (intent) {
            case RAISE_FUNDS -> {
                if (netCoinEffect > 0) {
                    yield netCoinEffect * 0.3; // Becomes netCoinEffect * 2.4 when multiplied by 8.0 weight
                } else if (netCoinEffect < 0) {
                    yield netCoinEffect * 0.25; // Becomes netCoinEffect * 2.0 penalty
                } else {
                    yield 0.0;
                }
            }
            case RESTORE_MORALE -> {
                if (netMoraleEffect > 0) {
                    yield netMoraleEffect * 0.4; // Becomes netMoraleEffect * 3.2
                } else if (netMoraleEffect < 0) {
                    yield netMoraleEffect * 0.3; // Becomes netMoraleEffect * 2.4 penalty
                } else {
                    yield 0.0;
                }
            }
            case GAIN_SUPPORT, PREPARE_ELECTION -> {
                if (netSupportEffect > 0) {
                    yield netSupportEffect * 0.5; // Becomes netSupportEffect * 4.0
                } else if (netSupportEffect < 0) {
                    yield netSupportEffect * 0.4; // Becomes netSupportEffect * 3.2 penalty
                } else {
                    yield 0.0;
                }
            }
            case DEFEND_IMAGE -> {
                if (netMediaEffect > 0) {
                    yield netMediaEffect * 0.4; // Becomes netMediaEffect * 3.2
                } else if (netMediaEffect < 0) {
                    yield netMediaEffect * 0.3; // Becomes netMediaEffect * 2.4 penalty
                } else {
                    yield 0.0;
                }
            }
            case SURVIVE_SCANDAL -> {
                if (netCorruptionEffect < 0) {
                    yield -netCorruptionEffect * 0.5; // Becomes -netCorruptionEffect * 4.0
                } else if (netCorruptionEffect > 0) {
                    yield -netCorruptionEffect * 0.4; // Becomes -netCorruptionEffect * 3.2 penalty
                } else {
                    yield 0.0;
                }
            }
            case ATTACK_RIVAL, FORCE_NO_CONFIDENCE -> {
                int oppSupportDamage = -intValue(opponentEffects.get("publicSupport"));
                int oppMediaDamage = -intValue(opponentEffects.get("mediaImage"));
                int oppMoraleDamage = -intValue(opponentEffects.get("partyMorale"));
                int oppCoinsDamage = -intValue(opponentEffects.get("coins"));
                int oppCorruptionGain = intValue(opponentEffects.get("corruptionScore"));

                double offensiveScore = 0.0;
                if (oppSupportDamage > 0) offensiveScore += oppSupportDamage * 0.4;
                if (oppMediaDamage > 0) offensiveScore += oppMediaDamage * 0.2;
                if (oppMoraleDamage > 0) offensiveScore += oppMoraleDamage * 0.2;
                if (oppCoinsDamage > 0) offensiveScore += oppCoinsDamage * 0.2;
                if (oppCorruptionGain > 0) offensiveScore += oppCorruptionGain * 0.2;
                yield offensiveScore;
            }
            default -> 0.0;
        };
    }

    private double scoreCard(GameSession session, PartyState party, PartyState opponent, CardDefinition card, AiIntent intent) {
        PartyStats stats = party.getStats();
        AiProfile profile = profileFor(party);
        Map<String, Object> selfEffects = partyEffect(card.getVisibleEffects(), "selfParty");
        Map<String, Object> opponentEffects = partyEffect(card.getVisibleEffects(), "opponentParty");

        double score = doubleValue(card.getWeights().get("basePlayWeight"));
        score += doubleValue(card.getWeights().get("aiPriorityWeight")) * weight(profile, "cardAiPriority");

        if (intent == AiIntent.FORCE_NO_CONFIDENCE && card.getCardKey() != null && card.getCardKey().contains("no_confidence")) {
            score += 200.0;
        }

        // ── CHANGE 2: Progressive card diversity penalty ──────────────────────────────
        // Applies to ALL parties (human cards are never scored here, only AI cards are).
        // Penalise cards that have been used once to encourage spreading usage over 60 turns.
        // Cards used ≥ 3 times are already filtered out of getAvailableCardsForParty().
        if (!"no_card".equals(card.getCardKey()) && session.getCardUsageByParty() != null) {
            Map<String, Integer> myUsage = session.getCardUsageByParty().get(party.getId());
            if (myUsage != null) {
                int timesUsed = myUsage.getOrDefault(card.getCardKey(), 0);
                if (timesUsed == 1) score -= 8.0;   // Mild: used once — prefer fresh cards
                if (timesUsed == 2) score -= 35.0;  // Strong: used twice — very strong deterrent
            }
        }
        // Penalize playing the exact same card as last turn (consecutive repeat deterrent)
        if (!"no_card".equals(card.getCardKey()) && session.getLastRoundSubmissions() != null) {
            for (RoundSubmission lastSub : session.getLastRoundSubmissions()) {
                if (lastSub.getPartyId().equals(party.getId())) {
                    if (card.getCardKey().equals(lastSub.getCardKey())) {
                        score -= 20.0; // (was 35; combined with diversity penalty above = effective 55 for same-card repeat)
                        break;
                    }
                }
            }
        }
        // ─────────────────────────────────────────────────────────────────────────────
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

        // ── CHANGE 6: Attacker health factor ─────────────────────────────────────────
        // Scale down ALL opponent-targeting score components when the attacker is weak.
        // A party at 15% support will score attack cards much lower than a party at 40%,
        // making self-buff cards naturally win without needing a hard block.
        double attackerHealthFactor = Math.min(1.0, stats.getPublicSupport() / 30.0);
        oppSupportVal    *= attackerHealthFactor;
        oppMediaVal      *= attackerHealthFactor;
        oppCorruptionVal *= attackerHealthFactor;
        // ─────────────────────────────────────────────────────────────────────────────

        // Dynamic target evaluation within card scoring:
        // Adjust score based on our grudges and targeted weaknesses of the chosen opponent candidate
        if (requiresTarget(card)) {
            PartyState targetOpponent = chooseOpponent(session, party, card);
            if (targetOpponent != null) {
                // Grudge vendetta boost (also scaled by attacker health)
                Map<String, Map<String, Integer>> grudges = session.getGrudges();
                if (grudges != null) {
                    Map<String, Integer> myGrudges = grudges.get(party.getId());
                    if (myGrudges != null) {
                        int grudge = myGrudges.getOrDefault(targetOpponent.getId(), 0);
                        score += grudge * 3.0 * attackerHealthFactor;
                    }
                }

                // Opponent vulnerability attack boosts (also scaled by attacker health)
                PartyStats tStats = targetOpponent.getStats();
                if (intValue(opponentEffects.get("coins")) < 0 && tStats.getCoins() <= 25) {
                    score += 15.0 * attackerHealthFactor;
                }
                if (intValue(opponentEffects.get("partyMorale")) < 0 && tStats.getPartyMorale() <= 20) {
                    score += 15.0 * attackerHealthFactor;
                }
                if (intValue(opponentEffects.get("corruptionScore")) > 0 && tStats.getCorruptionScore() >= 75) {
                    score += 15.0 * attackerHealthFactor;
                }
                if (intValue(opponentEffects.get("publicSupport")) < 0 && tStats.getPublicSupport() <= 12) {
                    score += 10.0 * attackerHealthFactor;
                }
            } else {
                // If a card requires an opponent target but all active opponents have pacts, penalize heavily.
                score -= 100.0;
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

        score += intentEffectsFit(intent, card, selfEffects, opponentEffects, profile) * weight(profile, "intentFit");
        score += categoryFitScore(party, opponent, card.getCategory(), profile);
        score += needScore(stats, card, selfEffects, profile);
        score += ideologyFitScore(party, card);
        score += electionTimingScore(session, card.getCategory(), profile);

        // ── CHANGE 3: Intent-to-card consistency enforcement ─────────────────────────
        // When intent is self-recovery, heavily penalise cards whose primary effect is
        // damaging an opponent's public support (attack cards). This ensures the AI
        // doesn't waste a recovery turn playing an aggressive card.
        boolean isSelfRecoveryIntent = intent == AiIntent.GAIN_SUPPORT
                || intent == AiIntent.RESTORE_MORALE
                || intent == AiIntent.RAISE_FUNDS
                || intent == AiIntent.SURVIVE_SCANDAL
                || intent == AiIntent.DEFEND_IMAGE
                || intent == AiIntent.PREPARE_ELECTION;
        boolean isPrimaryAttackCard = requiresTarget(card)
                && intValue(partyEffect(card.getVisibleEffects(), "opponentParty").get("publicSupport")) < 0;
        if (isSelfRecoveryIntent && isPrimaryAttackCard) {
            score -= 50.0;
        }
        // ─────────────────────────────────────────────────────────────────────────────

        int netCoinEffect = 0;
        if (selfEffects.containsKey("coins")) {
            int visibleCoins = intValue(selfEffects.get("coins"));
            if (visibleCoins < 0) {
                // Negative coin change represents the card cost itself (offset by the engine)
                netCoinEffect = -card.getCost();
            } else {
                netCoinEffect = visibleCoins - card.getCost();
            }
        } else {
            netCoinEffect = -card.getCost();
        }

        if (stats.getCoins() < card.getCost()) {
            score -= weight(profile, "unaffordableBasePenalty") + (card.getCost() - stats.getCoins());
        } else if (stats.getCoins() <= 80 && netCoinEffect > 0) {
            // Encourage playing coin-generating cards when in crisis (coins <= 80)
            score += netCoinEffect * 4.0;
        } else if (stats.getCoins() < 100 && netCoinEffect > 0) {
            // Encourage playing coin-generating cards when in minor shortage
            score += netCoinEffect * 2.5;
        } else {
            // Apply dynamic, progressive coin safety penalty to prevent spending down to critical levels
            int remainingCoins = stats.getCoins() + netCoinEffect;
            if (remainingCoins < 25) {
                score -= 80.0 + (25 - remainingCoins) * 3.0; // Critical danger of bankruptcy/elimination
            } else if (remainingCoins < 50) {
                score -= 40.0; // High risk warning
            } else if (remainingCoins < 75) {
                score -= 20.0; // Moderate resource protection
            } else if (remainingCoins < 100) {
                score -= 5.0;  // Precautionary soft penalty
            } else if (stats.getCoins() < threshold(profile, "needCoinsLow")) {
                score -= card.getCost() * weight(profile, "lowCoinCostPenalty");
            }
        }

        // Apply dynamic morale safety/recovery logic
        int netMoraleEffect = 0;
        if (selfEffects.containsKey("partyMorale")) {
            netMoraleEffect = intValue(selfEffects.get("partyMorale"));
        }

        if (stats.getPartyMorale() < 50 && netMoraleEffect > 0) {
            // Encourage playing morale-restoring cards when in crisis
            score += netMoraleEffect * 3.0;
        } else if (netMoraleEffect < 0) {
            // Apply dynamic morale safety penalty to prevent playing cards that drop morale below safety levels
            int remainingMorale = stats.getPartyMorale() + netMoraleEffect;
            if (remainingMorale < 15) {
                score -= 100.0 + (15 - remainingMorale) * 4.0; // Critical danger of morale collapse/defeat
            } else if (remainingMorale < 25) {
                score -= 50.0;  // High risk
            } else if (remainingMorale < 35) {
                score -= 25.0;  // Moderate risk
            } else if (remainingMorale < 50) {
                score -= 10.0;  // Soft precaution
            }
        }

        // Apply dynamic support safety/recovery logic
        int netSupportEffect = 0;
        if (selfEffects.containsKey("publicSupport")) {
            netSupportEffect = intValue(selfEffects.get("publicSupport"));
        }

        if (stats.getPublicSupport() < 25 && netSupportEffect > 0) {
            // Encourage playing support-restoring cards when in crisis
            score += netSupportEffect * 4.0;
        } else if (netSupportEffect < 0) {
            // Apply dynamic support safety penalty to prevent playing cards that drop support below safety levels
            int remainingSupport = stats.getPublicSupport() + netSupportEffect;
            if (remainingSupport < 6) {
                score -= 100.0 + (6 - remainingSupport) * 5.0; // Critical danger of support defeat (< 5% is defeat)
            } else if (remainingSupport < 10) {
                score -= 50.0;  // High risk
            } else if (remainingSupport < 15) {
                score -= 25.0;  // Moderate risk
            } else if (remainingSupport < 20) {
                score -= 10.0;  // Soft precaution
            }
        }

        // Apply dynamic corruption safety logic
        int netCorruptionEffect = 0;
        if (selfEffects.containsKey("corruptionScore")) {
            netCorruptionEffect = intValue(selfEffects.get("corruptionScore"));
        }

        if (stats.getCorruptionScore() > 60 && netCorruptionEffect < 0) {
            // Encourage playing corruption-reducing cards when in danger
            score += -netCorruptionEffect * 4.0;
        } else if (netCorruptionEffect > 0) {
            // Apply dynamic corruption safety penalty to prevent playing cards that increase corruption above safety levels
            int remainingCorruption = stats.getCorruptionScore() + netCorruptionEffect;
            if (remainingCorruption > 90) {
                score -= 100.0 + (remainingCorruption - 90) * 5.0; // Critical danger of corruption defeat (> 95% is defeat)
            } else if (remainingCorruption > 80) {
                score -= 50.0;  // High risk
            } else if (remainingCorruption > 70) {
                score -= 25.0;  // Moderate risk
            }
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
        
        int moraleEffect = intValue(effects.get("partyMorale"));
        double selfMoraleWeight = weight(profile, "selfMorale");
        if (moraleEffect < 0) {
            int currentMorale = stats.getPartyMorale();
            if (currentMorale < 20) {
                selfMoraleWeight *= 8.0;
            } else if (currentMorale < 35) {
                selfMoraleWeight *= 4.0;
            } else if (currentMorale < 50) {
                selfMoraleWeight *= 2.0;
            }
        }
        score += moraleEffect * selfMoraleWeight;
        
        score -= intValue(effects.get("corruptionScore")) * (weight(profile, "selfCorruptionPenaltyBase") + profile.getIdeologyStrictness());
        
        int coinEffect = intValue(effects.get("coins"));
        double selfCoinsWeight = weight(profile, "selfCoins");
        if (coinEffect < 0) {
            int currentCoins = stats.getCoins();
            if (currentCoins < 30) {
                selfCoinsWeight *= 8.0;
            } else if (currentCoins < 50) {
                selfCoinsWeight *= 4.0;
            } else if (currentCoins < 75) {
                selfCoinsWeight *= 2.0;
            }
        }
        score += coinEffect * selfCoinsWeight;

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
        // Only consider opponent's corruption if there is a targetable opponent (no NAP covering everyone)
        if (opponent != null
                && party.getRole() != PartyRole.GOVERNMENT
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

    private double needScore(PartyStats stats, CardDefinition card, Map<String, Object> selfEffects, AiProfile profile) {
        double score = 0;
        
        // Calculate net coin effect
        int netCoinEffect = 0;
        if (selfEffects.containsKey("coins")) {
            int visibleCoins = intValue(selfEffects.get("coins"));
            if (visibleCoins < 0) {
                netCoinEffect = -card.getCost();
            } else {
                netCoinEffect = visibleCoins - card.getCost();
            }
        } else {
            netCoinEffect = -card.getCost();
        }
        
        int netMoraleEffect = intValue(selfEffects.get("partyMorale"));
        int netSupportEffect = intValue(selfEffects.get("publicSupport"));
        int netCorruptionEffect = intValue(selfEffects.get("corruptionScore"));
        int netMediaEffect = intValue(selfEffects.get("mediaImage"));

        if (stats.getPartyMorale() < threshold(profile, "needMoraleLow")) {
            if (netMoraleEffect > 0) {
                score += netMoraleEffect * (weight(profile, "needMoraleBoost") / 3.0);
            } else if (netMoraleEffect < 0) {
                score += netMoraleEffect * (weight(profile, "needMoraleBoost") / 4.0);
            }
        }
        if (stats.getMediaImage() < threshold(profile, "needMediaLow")) {
            if (netMediaEffect > 0) {
                score += netMediaEffect * (weight(profile, "needMediaBoost") / 3.0);
            } else if (netMediaEffect < 0) {
                score += netMediaEffect * (weight(profile, "needMediaBoost") / 4.0);
            }
        }
        if (stats.getPublicSupport() < threshold(profile, "needSupportLow")) {
            if (netSupportEffect > 0) {
                score += netSupportEffect * (weight(profile, "needSupportBoost") / 3.0);
            } else if (netSupportEffect < 0) {
                score += netSupportEffect * (weight(profile, "needSupportBoost") / 4.0);
            }
        }
        if (stats.getCorruptionScore() > threshold(profile, "needCorruptionHigh")) {
            if (netCorruptionEffect < 0) {
                score += -netCorruptionEffect * (weight(profile, "needCorruptionDefenseBoost") / 3.0);
            } else if (netCorruptionEffect > 0) {
                score += -netCorruptionEffect * (weight(profile, "needCorruptionDefenseBoost") / 4.0);
            }
        }
        if (stats.getCoins() < threshold(profile, "needCoinsLow")) {
            if (netCoinEffect > 0) {
                score += netCoinEffect * (weight(profile, "needLowCoinFundBoost") / 3.0);
            } else if (netCoinEffect < 0) {
                score += netCoinEffect * (weight(profile, "needLowCoinFundBoost") / 4.0);
            }
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
        // ── CHANGE 7 (electionTimingScore): use turnsRemaining not monthInCycle ───────
        // monthInCycle resets each 60-month cycle, so 60 - monthInCycle is always large
        // and the election window was never reached mid-game. Now use game-wide turns.
        int turnsRemaining = Math.max(0, 60 - session.getTurnNumber());
        if (turnsRemaining > threshold(profile, "electionWindowMonths")) {
            return 0;
        }
        if (oneOf(category, "positive_service", "media_narrative", "governance")) {
            return weight(profile, "electionCategoryBoost");
        }
        if (oneOf(category, "scandal", "scandal_accusation")) {
            return weight(profile, "electionScandalPenalty");
        }
        return 0;
        // ─────────────────────────────────────────────────────────────────────────────
    }

    @SuppressWarnings("unchecked")
    private Map<String, Object> partyEffect(Map<String, Object> effects, String key) {
        if (effects == null) {
            return Map.of();
        }
        Object value = effects.get(key);
        if (value == null && "playerParty".equals(key)) {
            value = effects.get("selfParty");
        } else if (value == null && "selfParty".equals(key)) {
            value = effects.get("playerParty");
        }
        if (value instanceof Map<?, ?> map) {
            return (Map<String, Object>) map;
        }
        Object scheduled = effects.get("scheduled");
        if (scheduled instanceof List<?> list && !list.isEmpty() && list.get(0) instanceof Map<?, ?> scheduledMap) {
            Object nestedEffects = scheduledMap.get("effects");
            if (nestedEffects instanceof Map<?, ?> nestedMap) {
                Object partyMap = nestedMap.get(key);
                if (partyMap == null && "playerParty".equals(key)) {
                    partyMap = nestedMap.get("selfParty");
                } else if (partyMap == null && "selfParty".equals(key)) {
                    partyMap = nestedMap.get("playerParty");
                }
                if (partyMap instanceof Map<?, ?> pMap) {
                    return (Map<String, Object>) pMap;
                }
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

    public PartyState chooseOpponent(GameSession session, PartyState actor, CardDefinition card) {
        java.util.List<PartyState> candidates = session.getParties().stream()
                .filter(PartyState::isActive)
                .filter(p -> !p.getId().equals(actor.getId()))
                .filter(p -> {
                    if (session.getActivePacts() != null) {
                        for (NonAggressionPact pact : session.getActivePacts()) {
                            if ((pact.getPartyAId().equals(actor.getId()) && pact.getPartyBId().equals(p.getId()))
                                    || (pact.getPartyAId().equals(p.getId()) && pact.getPartyBId().equals(actor.getId()))) {
                                return false;
                            }
                        }
                    }
                    return true;
                })
                .toList();

        if (candidates.isEmpty()) {
            return null;
        }

        PartyState bestCandidate = null;
        double highestScore = -9999.0;

        for (PartyState candidate : candidates) {
            PartyStats cStats = candidate.getStats();
            double score = 0;

            // 1. Leader bias (base target score scales with public support)
            score += cStats.getPublicSupport() * 1.5;

            // 2. Grudge history check (retaliation)
            Map<String, Map<String, Integer>> grudges = session.getGrudges();
            if (grudges != null) {
                Map<String, Integer> myGrudges = grudges.get(actor.getId());
                if (myGrudges != null) {
                    int grudgeLevel = myGrudges.getOrDefault(candidate.getId(), 0);
                    score += grudgeLevel * 10.0;
                }
            }

            // 3. Opponent Weaknesses check (Killer Instinct targeting)
            if (card != null) {
                Map<String, Object> oppEffects = partyEffect(card.getVisibleEffects(), "opponentParty");
                
                if (intValue(oppEffects.get("coins")) < 0) {
                    score += (100 - cStats.getCoins()) * 1.0;
                    if (cStats.getCoins() <= 25) {
                        score += 35.0; // Coins warning knockout
                    }
                }
                
                if (intValue(oppEffects.get("partyMorale")) < 0) {
                    score += (100 - cStats.getPartyMorale()) * 1.0;
                    if (cStats.getPartyMorale() <= 20) {
                        score += 35.0; // Morale warning knockout
                    }
                }

                if (intValue(oppEffects.get("corruptionScore")) > 0) {
                    score += cStats.getCorruptionScore() * 1.0;
                    if (cStats.getCorruptionScore() >= 75) {
                        score += 35.0; // Corruption warning knockout
                    }
                }

                if (intValue(oppEffects.get("publicSupport")) < 0) {
                    if (cStats.getPublicSupport() <= 12) {
                        score += 25.0; // Support warning knockout
                    }
                }
            }

            if (score > highestScore) {
                highestScore = score;
                bestCandidate = candidate;
            }
        }

        return bestCandidate;
    }

    public PartyState chooseOpponentForProject(GameSession session, PartyState actor, BuildingProject projectDef) {
        java.util.List<PartyState> candidates = session.getParties().stream()
                .filter(PartyState::isActive)
                .filter(p -> !p.getId().equals(actor.getId()))
                .filter(p -> {
                    if (session.getActivePacts() != null) {
                        for (NonAggressionPact pact : session.getActivePacts()) {
                            if ((pact.getPartyAId().equals(actor.getId()) && pact.getPartyBId().equals(p.getId()))
                                    || (pact.getPartyAId().equals(p.getId()) && pact.getPartyBId().equals(actor.getId()))) {
                                return false;
                            }
                        }
                    }
                    return true;
                })
                .toList();

        if (candidates.isEmpty()) {
            return null;
        }

        PartyState bestCandidate = null;
        double highestScore = -9999.0;

        for (PartyState candidate : candidates) {
            PartyStats cStats = candidate.getStats();
            double score = 0;

            // 1. Leader bias
            score += cStats.getPublicSupport() * 1.5;

            // 2. Grudges
            Map<String, Map<String, Integer>> grudges = session.getGrudges();
            if (grudges != null) {
                Map<String, Integer> myGrudges = grudges.get(actor.getId());
                if (myGrudges != null) {
                    int grudgeLevel = myGrudges.getOrDefault(candidate.getId(), 0);
                    score += grudgeLevel * 10.0;
                }
            }

            // 3. Project-specific weaknesses
            if (projectDef != null) {
                if (projectDef.getBenefitMorale() < 0) {
                    score += (100 - cStats.getPartyMorale()) * 1.0;
                    if (cStats.getPartyMorale() <= 20) score += 35.0;
                }
                if (projectDef.getBenefitMedia() < 0) {
                    score += (100 - cStats.getMediaImage()) * 1.0;
                }
                if (projectDef.getBenefitCorruption() > 0) {
                    score += cStats.getCorruptionScore() * 1.0;
                    if (cStats.getCorruptionScore() >= 75) score += 35.0;
                }
                if (projectDef.getBenefitSupport() < 0) {
                    if (cStats.getPublicSupport() <= 12) score += 25.0;
                }
            }

            if (score > highestScore) {
                highestScore = score;
                bestCandidate = candidate;
            }
        }

        return bestCandidate;
    }

    private boolean requiresTarget(CardDefinition card) {
        if (card == null || card.getTarget() == null) {
            return false;
        }
        Object declaredTarget = card.getTarget().get("opponentParty");
        return Boolean.TRUE.equals(declaredTarget) || !partyEffect(card.getVisibleEffects(), "opponentParty").isEmpty();
    }

    public double evaluateRewardUtility(GameSession session, PartyState party, RewardDefinition reward) {
        if (reward == null) {
            return 0.0;
        }

        PartyStats stats = party.getStats();
        double utility = 0.0;

        // 1. Coins benefit
        if (reward.coinsEffect() > 0) {
            if (stats.getCoins() <= 40) {
                utility += 0.8;
            } else if (stats.getCoins() <= 70) {
                utility += 0.4;
            } else {
                utility += 0.1;
            }
        }

        // 2. Morale benefit
        if (reward.moraleEffect() > 0) {
            if (stats.getPartyMorale() <= 30) {
                utility += 0.8;
            } else if (stats.getPartyMorale() <= 60) {
                utility += 0.4;
            } else {
                utility += 0.1;
            }
        }

        // 3. Corruption reduction (negative benefit is good for self)
        if (reward.corruptionEffect() < 0 && "self".equals(reward.allowedTargets())) {
            if (stats.getCorruptionScore() >= 60) {
                utility += 0.9;
            } else if (stats.getCorruptionScore() >= 30) {
                utility += 0.4;
            } else {
                utility += 0.1;
            }
        }

        // 4. Media image benefit
        if (reward.mediaEffect() > 0) {
            if (stats.getMediaImage() <= 35) {
                utility += 0.7;
            } else if (stats.getMediaImage() <= 70) {
                utility += 0.3;
            } else {
                utility += 0.1;
            }
        }

        // 5. Support benefit
        if (reward.publicSupportEffect() > 0) {
            if (stats.getPublicSupport() <= 20) {
                utility += 0.9;
            } else if (stats.getPublicSupport() <= 35) {
                utility += 0.5;
            } else {
                utility += 0.2;
            }
        }

        // 6. Hostile / Sabotage rewards
        if ("opponent".equals(reward.allowedTargets())) {
            PartyState leadOpponent = session.getParties().stream()
                    .filter(p -> p.isActive() && !p.getId().equals(party.getId()))
                    .max(java.util.Comparator.comparingInt(p -> p.getStats().getPublicSupport()))
                    .orElse(null);
            
            if (leadOpponent != null) {
                if (leadOpponent.getStats().getPublicSupport() >= 35) {
                    utility += 0.6;
                } else {
                    utility += 0.3;
                }

                if (reward.moraleEffect() < 0 && leadOpponent.getStats().getPartyMorale() <= 30) {
                    utility += 0.5;
                }
                if (reward.coinsEffect() < 0 && leadOpponent.getStats().getCoins() <= 30) {
                    utility += 0.5;
                }
                if (reward.corruptionEffect() > 0 && leadOpponent.getStats().getCorruptionScore() >= 65) {
                    utility += 0.5;
                }
            }
        }

        return utility;
    }

    public double calculateExchangeUtility(PartyState party, int coins, int morale, int support, List<String> buildings, GameSession session, boolean isIncoming) {
        double coinMultiplier = 1.0;
        double moraleMultiplier = 1.0;
        double supportMultiplier = 1.0;
        
        int currentCoins = party.getStats().getCoins();
        int currentMorale = party.getStats().getPartyMorale();
        int currentSupport = party.getStats().getPublicSupport();
        
        if (isIncoming) {
            if (currentCoins < 30) coinMultiplier = 10.0;
            else if (currentCoins < 50) coinMultiplier = 5.0;
            else if (currentCoins < 75) coinMultiplier = 3.0;
            else if (currentCoins < 100) coinMultiplier = 2.0;

            if (currentMorale < 20) moraleMultiplier = 8.0;
            else if (currentMorale < 30) moraleMultiplier = 4.0;
            else if (currentMorale < 40) moraleMultiplier = 2.5;
            else if (currentMorale < 50) moraleMultiplier = 1.8;

            if (currentSupport < 10) supportMultiplier = 12.0;
            else if (currentSupport < 15) supportMultiplier = 7.0;
            else if (currentSupport < 20) supportMultiplier = 4.0;
            else if (currentSupport < 25) supportMultiplier = 2.5;
        } else {
            if (currentCoins < 30) coinMultiplier = 15.0;
            else if (currentCoins < 50) coinMultiplier = 8.0;
            else if (currentCoins < 75) coinMultiplier = 4.0;
            else if (currentCoins < 100) coinMultiplier = 2.5;

            if (currentMorale < 20) moraleMultiplier = 10.0;
            else if (currentMorale < 30) moraleMultiplier = 5.0;
            else if (currentMorale < 40) moraleMultiplier = 3.0;
            else if (currentMorale < 50) moraleMultiplier = 2.0;

            if (currentSupport < 10) supportMultiplier = 15.0;
            else if (currentSupport < 15) supportMultiplier = 8.0;
            else if (currentSupport < 20) supportMultiplier = 5.0;
            else if (currentSupport < 25) supportMultiplier = 3.0;
        }
        
        double total = coins * coinMultiplier;
        total += morale * 20.0 * moraleMultiplier;
        total += support * 50.0 * supportMultiplier;
        
        if (buildings != null) {
            int remainingTurns = Math.max(0, 60 - session.getTurnNumber());
            for (String key : buildings) {
                try {
                    BuildingProject def = BuildingProject.valueOf(key);
                    double yieldVal = def.getBenefitCoins() 
                                    + def.getBenefitMorale() * 20.0 
                                    + def.getBenefitSupport() * 50.0 
                                    + def.getBenefitMedia() * 20.0 
                                    - def.getBenefitCorruption() * 20.0;
                    total += yieldVal * remainingTurns;
                } catch (Exception e) {
                    // Ignore invalid enum
                }
            }
        }
        
        return total;
    }

    public boolean evaluateCooperationOffer(GameSession session, PartyState recipient, CooperationOffer offer) {
        if (offer.getType() == CooperationOffer.OfferType.NON_AGGRESSION) {
            // Pact safety value is 5 coins per turn
            double pactValue = 5.0 * offer.getDurationTurns();
            
            // Grudge discount
            Map<String, Map<String, Integer>> grudges = session.getGrudges();
            int grudgeVal = 0;
            if (grudges != null && grudges.containsKey(recipient.getId())) {
                grudgeVal = grudges.get(recipient.getId()).getOrDefault(offer.getSenderPartyId(), 0);
            }
            pactValue -= grudgeVal * 2.0;
            
            // Early game bonus
            if (session.getTurnNumber() <= 20) {
                pactValue += 15.0;
            }
            
            if (offer.isSenderPaysPact()) {
                // AI receives payment
                if (grudgeVal > 25) {
                    return false; // AI refuses pact with hated enemies
                }
                return true; // Net positive safety + free resources
            } else {
                // AI has to pay
                double paymentCost = 0;
                String res = offer.getPactPaymentResource();
                int val = offer.getPactPaymentValue();
                
                if ("COINS".equalsIgnoreCase(res)) {
                    if (recipient.getStats().getCoins() - val < 20) return false;
                    paymentCost = calculateExchangeUtility(recipient, val, 0, 0, null, session, false);
                } else if ("MORALE".equalsIgnoreCase(res)) {
                    if (recipient.getStats().getPartyMorale() - val < 18) return false;
                    paymentCost = calculateExchangeUtility(recipient, 0, val, 0, null, session, false);
                } else if ("SUPPORT".equalsIgnoreCase(res)) {
                    if (recipient.getStats().getPublicSupport() - val < 10) return false;
                    paymentCost = calculateExchangeUtility(recipient, 0, 0, val, null, session, false);
                } else if ("COMPLETED_BUILDING".equalsIgnoreCase(res)) {
                    paymentCost = calculateExchangeUtility(recipient, 0, 0, 0, offer.getPactPaymentBuildingKeys(), session, false);
                }
                
                return pactValue >= paymentCost;
            }
        } else if (offer.getType() == CooperationOffer.OfferType.EXCHANGE) {
            double receivedUtility = calculateExchangeUtility(recipient, offer.getOfferedCoins(), offer.getOfferedMorale(), offer.getOfferedSupport(), offer.getOfferedBuildingKeys(), session, true);
            double givenUtility = calculateExchangeUtility(recipient, offer.getRequestedCoins(), offer.getRequestedMorale(), offer.getRequestedSupport(), null, session, false);
            
            // Safety limits check
            if (recipient.getStats().getCoins() - offer.getRequestedCoins() < 20) return false;
            if (recipient.getStats().getPartyMorale() - offer.getRequestedMorale() < 18) return false;
            if (recipient.getStats().getPublicSupport() - offer.getRequestedSupport() < 10) return false;
            
            // FIRE SALE ACCEPTANCE RULE:
            // If the sender is offering exactly 100 Coins for 10 Morale, it's a Fire Sale.
            // As long as the recipient has healthy Morale (> 30), they will accept it.
            if (offer.getOfferedCoins() == 100 && offer.getRequestedMorale() == 10 && 
                offer.getOfferedMorale() == 0 && offer.getOfferedSupport() == 0 && 
                offer.getRequestedCoins() == 0) {
                if (recipient.getStats().getPartyMorale() >= 30) {
                    return true;
                }
            }

            return receivedUtility >= 1.05 * givenUtility;
        } else if (offer.getType() == CooperationOffer.OfferType.LOBBYING) {
            double receivedUtility = calculateExchangeUtility(recipient, offer.getOfferedCoins(), offer.getOfferedMorale(), 0, offer.getOfferedBuildingKeys(), session, true);
            receivedUtility += offer.getOfferedMedia() * 20.0;
            receivedUtility += offer.getDurationTurns() * 5.0;

            double givenUtility = calculateExchangeUtility(recipient, 25, 0, 0, null, session, false);

            Map<String, Map<String, Integer>> grudges = session.getGrudges();
            int grudgeVal = 0;
            if (grudges != null && grudges.containsKey(recipient.getId())) {
                grudgeVal = grudges.get(recipient.getId()).getOrDefault(offer.getSenderPartyId(), 0);
            }
            double hateFactor = 1.0 + (grudgeVal / 50.0);

            if (recipient.getStats().getCoins() < 25) {
                return false;
            }

            return receivedUtility >= givenUtility * hateFactor * 1.1;
        }
        return false;
    }

    public List<String> rankAndSelectProjectsToRetain(List<String> completedProjectKeys) {
        if (completedProjectKeys == null || completedProjectKeys.isEmpty()) {
            return new ArrayList<>();
        }
        List<String> sorted = new ArrayList<>(completedProjectKeys);
        sorted.sort((left, right) -> Double.compare(
            scoreProjectForRetention(right),
            scoreProjectForRetention(left)
        ));
        if (sorted.size() > 5) {
            return sorted.subList(0, 5);
        }
        return sorted;
    }

    public double scoreProjectForRetention(String projectKey) {
        try {
            BuildingProject project = BuildingProject.valueOf(projectKey);
            double score = 0.0;
            score += project.getCostCoins();
            score += project.getCostMorale() * 2.0;
            score += project.getCostMedia() * 2.0;
            score += project.getCostCorruption() * 2.0;
            score += project.getCostSupport() * 5.0;
            
            score += project.getBenefitCoins() * 10.0;
            score += project.getBenefitMorale() * 20.0;
            score += project.getBenefitMedia() * 20.0;
            score -= project.getBenefitCorruption() * 20.0;
            score += project.getBenefitSupport() * 50.0;
            return score;
        } catch (Exception e) {
            return 0.0;
        }
    }

    public String chooseBillToPropose(GameSession session, PartyState party) {
        if (billRepository == null) {
            return null;
        }
        if (session.getProposedBillKeyThisTurn() != null && !session.getProposedBillKeyThisTurn().isEmpty()) {
            return null;
        }

        String myRoleStr = party.getRole() == PartyRole.GOVERNMENT ? "GOVERNMENT" : "OPPOSITION";
        List<LegislativeBillDefinition> allBills = com.politicalsim.content.DefinitionCache.getBillsForScenario(billRepository, session.getScenarioKey());
        List<LegislativeBillState> currentSessionBills = session.getBills();
        
        List<String> eligibleBillKeys = currentSessionBills.stream()
                .filter(b -> "NOT_PROPOSED".equals(b.getStatus()))
                .map(LegislativeBillState::getBillKey)
                .toList();

        List<LegislativeBillDefinition> proposePool = allBills.stream()
                .filter(b -> eligibleBillKeys.contains(b.getBillKey()))
                .filter(b -> myRoleStr.equalsIgnoreCase(b.getProposingRole()))
                .toList();

        if (proposePool.isEmpty()) {
            return null;
        }

        AiIntent intent = chooseIntent(session, party, null);
        LegislativeBillDefinition bestBill = null;
        double bestUtility = -9999.0;

        for (LegislativeBillDefinition bill : proposePool) {
            double utility = scoreBillForAi(session, party, bill, intent);
            if (utility > bestUtility) {
                bestUtility = utility;
                bestBill = bill;
            }
        }

        if (bestBill != null && bestUtility > 0.0) {
            return bestBill.getBillKey();
        }
        return null;
    }

    public double scoreBillForAi(GameSession session, PartyState party, LegislativeBillDefinition bill, AiIntent intent) {
        Map<String, Object> passedEffects = bill.getEffectsPassed();
        if (passedEffects == null) {
            return 0.0;
        }

        double utility = intentBillEffectsFit(intent, passedEffects);

        int supportEffect = intValue(passedEffects.get("publicSupport"));
        int moraleEffect = intValue(passedEffects.get("partyMorale"));
        int mediaEffect = intValue(passedEffects.get("mediaImage"));
        int corruptionEffect = intValue(passedEffects.get("corruptionScore"));
        int coinsEffect = intValue(passedEffects.get("coins"));

        utility += supportEffect * 2.5;
        utility += moraleEffect * 1.5;
        utility += mediaEffect * 1.5;
        utility -= corruptionEffect * 2.0;
        utility += coinsEffect * 0.1;

        return utility;
    }

    private double intentBillEffectsFit(AiIntent intent, Map<String, Object> effects) {
        int coins = intValue(effects.get("coins"));
        int morale = intValue(effects.get("partyMorale"));
        int support = intValue(effects.get("publicSupport"));
        int corruption = intValue(effects.get("corruptionScore"));
        int media = intValue(effects.get("mediaImage"));

        double fit = 0.0;
        switch (intent) {
            case RAISE_FUNDS:
                if (coins > 0) fit += coins * 3.0;
                break;
            case GAIN_SUPPORT:
            case PREPARE_ELECTION:
                if (support > 0) fit += support * 5.0;
                break;
            case RESTORE_MORALE:
                if (morale > 0) fit += morale * 3.0;
                break;
            case DEFEND_IMAGE:
                if (media > 0) fit += media * 3.0;
                break;
            case SURVIVE_SCANDAL:
                if (corruption < 0) fit += Math.abs(corruption) * 4.0;
                break;
            default:
                break;
        }
        return fit;
    }

    public String chooseFactionCrisisChoice(GameSession session, PartyState party) {
        PartyStats stats = party.getStats();
        if (stats.getCoins() >= 55 && stats.getMediaImage() >= 25) {
            return "A";
        }
        if (stats.getPartyMorale() >= 25 && stats.getPublicSupport() >= 8) {
            return "B";
        }
        return "C";
    }

    public void makeFactionAllocations(GameSession session, PartyState party, RoundSubmission submission) {
        List<com.politicalsim.party.FactionState> factions = party.getFactions();
        if (factions == null || factions.isEmpty()) {
            return;
        }

        int availablePatronage = 1;
        List<String> unassignedProjectKeys = new ArrayList<>();
        if (party.getProjects() != null) {
            for (ProjectState p : party.getProjects()) {
                if (p.getProgressPercent() == 100 && (p.getManagingFactionKey() == null || p.getManagingFactionKey().equals("None") || p.getManagingFactionKey().isEmpty())) {
                    unassignedProjectKeys.add(p.getProjectKey());
                }
            }
        }

        List<String> assignedPosts = new ArrayList<>();
        for (com.politicalsim.party.FactionState f : factions) {
            if (f.isActive() && f.getPost() != null && !f.getPost().equals("None") && !f.getPost().isEmpty()) {
                assignedPosts.add(f.getPost());
            }
        }
        List<String> availablePosts = new ArrayList<>();
        if (!assignedPosts.contains("Secretary Post")) {
            availablePosts.add("Secretary Post");
        }
        if (!assignedPosts.contains("Fund Manager Post")) {
            availablePosts.add("Fund Manager Post");
        }

        List<com.politicalsim.party.FactionState> activeFactions = new ArrayList<>();
        for (com.politicalsim.party.FactionState f : factions) {
            if (f.isActive()) {
                activeFactions.add(f);
            }
        }
        if (activeFactions.isEmpty()) {
            return;
        }

        List<Map<String, Object>> factionStatesList = new ArrayList<>();
        Map<String, String> projectAssignments = new java.util.HashMap<>();

        List<SimFaction> simFactions = new ArrayList<>();
        for (com.politicalsim.party.FactionState f : activeFactions) {
            simFactions.add(new SimFaction(f));
        }

        AiProfile profile = profileFor(party);
        boolean balanced = profile.getStyle() == AiStyle.STRENGTH_BUILDER || profile.getStyle() == AiStyle.BALANCED_STRATEGIST;

        for (SimFaction sf : simFactions) {
            if (sf.loyalty < 35) {
                if (availablePatronage > 0) {
                    sf.patronage += 1;
                    sf.loyalty = Math.min(100, sf.loyalty + 5);
                    availablePatronage--;
                } else if (!availablePosts.isEmpty()) {
                    String post = availablePosts.remove(0);
                    sf.post = post;
                    sf.loyalty = Math.min(100, sf.loyalty + 15);
                }
            }
        }

        while (!availablePosts.isEmpty()) {
            String post = availablePosts.remove(0);
            SimFaction target = null;
            if (balanced) {
                simFactions.sort((a, b) -> {
                    boolean aHas = a.post != null && !a.post.equals("None");
                    boolean bHas = b.post != null && !b.post.equals("None");
                    if (aHas != bHas) return aHas ? 1 : -1;
                    return Integer.compare(a.loyalty, b.loyalty);
                });
                target = simFactions.get(0);
            } else {
                if (post.equals("Fund Manager Post")) {
                    target = findSimFactionByKey(simFactions, "veteran");
                } else {
                    target = findSimFactionByKey(simFactions, "youth");
                }
                if (target == null || (target.post != null && !target.post.equals("None"))) {
                    simFactions.sort((a, b) -> Integer.compare(a.loyalty, b.loyalty));
                    target = simFactions.get(0);
                }
            }
            if (target != null) {
                target.post = post;
                target.loyalty = Math.min(100, target.loyalty + 15);
            }
        }

        while (availablePatronage > 0) {
            SimFaction target = null;
            if (balanced) {
                simFactions.sort((a, b) -> Integer.compare(a.loyalty, b.loyalty));
                target = simFactions.get(0);
            } else {
                String preferredKey = profile.getStyle() == AiStyle.AGGRESSIVE_BIDDER ? "veteran" : "youth";
                target = findSimFactionByKey(simFactions, preferredKey);
                if (target == null) {
                    simFactions.sort((a, b) -> Integer.compare(b.influence, a.influence));
                    target = simFactions.get(0);
                }
            }
            if (target != null) {
                target.patronage += 1;
                target.loyalty = Math.min(100, target.loyalty + 5);
            }
            availablePatronage--;
        }

        for (String projKey : unassignedProjectKeys) {
            SimFaction target = null;
            if (balanced) {
                simFactions.sort((a, b) -> Integer.compare(a.projectCount, b.projectCount));
                target = simFactions.get(0);
            } else {
                String preferredKey = profile.getStyle() == AiStyle.AGGRESSIVE_BIDDER ? "veteran" : "youth";
                target = findSimFactionByKey(simFactions, preferredKey);
                if (target == null) {
                    simFactions.sort((a, b) -> Integer.compare(b.influence, a.influence));
                    target = simFactions.get(0);
                }
            }
            if (target != null) {
                target.projectCount++;
                projectAssignments.put(projKey, target.key);
            }
        }

        recalculateSimInfluences(simFactions, party);

        for (SimFaction sf : simFactions) {
            Map<String, Object> fMap = new java.util.HashMap<>();
            fMap.put("key", sf.key);
            fMap.put("name", sf.name);
            fMap.put("loyalty", sf.loyalty);
            fMap.put("influence", sf.influence);
            fMap.put("post", sf.post);
            fMap.put("patronage", sf.patronage);
            fMap.put("active", true);
            factionStatesList.add(fMap);
        }

        for (com.politicalsim.party.FactionState f : factions) {
            if (!f.isActive()) {
                Map<String, Object> fMap = new java.util.HashMap<>();
                fMap.put("key", f.getKey());
                fMap.put("name", f.getName());
                fMap.put("loyalty", 0);
                fMap.put("influence", 0);
                fMap.put("post", "None");
                fMap.put("patronage", 0);
                fMap.put("active", false);
                factionStatesList.add(fMap);
            }
        }

        Map<String, Object> allocationsMap = new java.util.HashMap<>();
        allocationsMap.put("factions", factionStatesList);
        allocationsMap.put("projects", projectAssignments);
        submission.setAllocations(allocationsMap);
    }

    private SimFaction findSimFactionByKey(List<SimFaction> list, String key) {
        for (SimFaction sf : list) {
            if (sf.key.equals(key)) return sf;
        }
        return null;
    }

    private void recalculateSimInfluences(List<SimFaction> simFactions, PartyState party) {
        double totalYieldSum = 0.0;
        Map<String, Double> yieldSums = new java.util.HashMap<>();

        for (SimFaction sf : simFactions) {
            double factor = 1.0;
            if (sf.loyalty >= 90) factor = 2.0;
            else if (sf.loyalty >= 80) factor = 1.5;
            else if (sf.loyalty >= 50) factor = 1.0;
            else if (sf.loyalty >= 30) factor = 0.5;
            else factor = 0.0;

            int coinsYield = sf.patronage * 2 + (sf.post.equals("Fund Manager Post") ? 8 : 0);
            int moraleYield = sf.patronage * 1 + (sf.post.equals("Secretary Post") ? 6 : 0);
            int corruptionYield = sf.patronage * -1 + (sf.post.equals("None") ? 0 : 2);
            int mediaYield = sf.patronage * 1;

            coinsYield += sf.projectCount * 2;
            moraleYield += sf.projectCount * 2;

            double coinsVal = Math.round(coinsYield * factor);
            double supportVal = Math.abs((sf.loyalty >= 50 ? (sf.influence * 0.01) : -(sf.influence * 0.01)) * factor);
            double moraleVal = Math.round(moraleYield * factor);
            double corruptionVal = Math.round(corruptionYield * (2.0 - factor));
            double mediaVal = Math.round(mediaYield * factor);

            double sum = coinsVal + supportVal * 10.0 + moraleVal + Math.abs(corruptionVal) + mediaVal;
            yieldSums.put(sf.key, sum);
            totalYieldSum += sum;
        }

        if (totalYieldSum > 0.0) {
            int remainingInfluence = 100;
            for (int i = 0; i < simFactions.size(); i++) {
                SimFaction sf = simFactions.get(i);
                if (i == simFactions.size() - 1) {
                    sf.influence = remainingInfluence;
                } else {
                    int inf = (int) Math.round((yieldSums.get(sf.key) / totalYieldSum) * 100.0);
                    sf.influence = Math.max(1, inf);
                    remainingInfluence -= sf.influence;
                }
            }
        }
    }

    private static class SimFaction {
        String key;
        String name;
        int loyalty;
        int influence;
        String post;
        int patronage;
        int projectCount = 0;

        SimFaction(com.politicalsim.party.FactionState f) {
            this.key = f.getKey();
            this.name = f.getName();
            this.loyalty = Math.max(0, f.getLoyalty() - 2);
            this.influence = f.getInfluence();
            this.post = f.getPost() == null ? "None" : f.getPost();
            this.patronage = f.getPatronage();
        }
    }
}
