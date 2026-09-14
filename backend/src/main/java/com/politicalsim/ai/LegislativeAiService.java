package com.politicalsim.ai;

import com.politicalsim.content.DefinitionCache;
import com.politicalsim.content.LegislativeBillDefinition;
import com.politicalsim.content.LegislativeBillDefinitionRepository;
import com.politicalsim.game.CooperationOffer;
import com.politicalsim.game.GameSession;
import com.politicalsim.game.LegislativeBillState;
import com.politicalsim.party.PartyRole;
import com.politicalsim.party.PartyState;
import org.springframework.stereotype.Service;

@Service
public class LegislativeAiService {

    private final LegislativeBillDefinitionRepository billRepository;

    public LegislativeAiService(LegislativeBillDefinitionRepository billRepository) {
        this.billRepository = billRepository;
    }

    public String evaluateAiBillVote(GameSession session, PartyState party, String activeBillKey) {
        // 1. Diplomatic / Lobby Pledge Check
        boolean hasPledge = session.getLobbyPledges().stream()
                .anyMatch(p -> p.getBillKey().equals(activeBillKey) && p.getPartyId().equals(party.getId()));
        if (hasPledge) {
            return "YES";
        }

        // 2. Proposer Check
        LegislativeBillState billState = session.getBills().stream()
                .filter(b -> b.getBillKey().equals(activeBillKey))
                .findFirst().orElse(null);
        if (billState == null) {
            return "ABSTAIN";
        }
        String proposerId = billState.getProposedByPartyId();
        if (proposerId == null) {
            return "ABSTAIN";
        }
        if (party.getId().equals(proposerId)) {
            return "YES";
        }

        PartyState proposer = session.getParties().stream()
                .filter(p -> p.getId().equals(proposerId))
                .findFirst().orElse(null);
        if (proposer == null) {
            return "ABSTAIN";
        }

        // 3. Coalition / Alliance Check (Accepted Cooperation Offers)
        boolean isAlly = session.getCooperationOffers().stream()
                .anyMatch(offer -> offer.getStatus() == CooperationOffer.OfferStatus.ACCEPTED &&
                        ((offer.getSenderPartyId().equals(party.getId()) && offer.getRecipientPartyId().equals(proposerId)) ||
                         (offer.getSenderPartyId().equals(proposerId) && offer.getRecipientPartyId().equals(party.getId()))));

        // 4. Utility / Effects Evaluation
        LegislativeBillDefinition billDef = null;
        if (billRepository != null) {
            billDef = DefinitionCache.getBillsForScenario(billRepository, session.getScenarioKey()).stream()
                    .filter(b -> b.getBillKey().equals(activeBillKey))
                    .findFirst()
                    .orElseGet(() -> DefinitionCache.getBillsForScenario(billRepository, "default").stream()
                            .filter(b -> b.getBillKey().equals(activeBillKey))
                            .findFirst()
                            .orElse(null));
        }

        // Calculate scores: self-gain (effectsSupporters) vs sponsor-gain (effectsSponsor + pointsPassed)
        double selfGain = evaluateEffectsScore(billDef != null ? billDef.getEffectsSupporters() : null);
        double sponsorGain = evaluateEffectsScore(billDef != null ? billDef.getEffectsSponsor() : null) + (billDef != null ? billDef.getPointsPassed() * 1.5 : 0);
        double opponentPenalty = evaluateEffectsScore(billDef != null ? billDef.getEffectsOpponents() : null);

        // Evaluate standings
        boolean aiNearDefeat = party.hasDefeatHazard() || party.getStats().getPublicSupport() < 25 || party.getStats().getPartyMorale() < 30 || party.getStats().getCoins() < 25;

        int rivalMaxSupport = session.getParties().stream()
                .filter(p -> p.isActive() && !p.getId().equals(proposer.getId()))
                .mapToInt(p -> p.getStats().getPublicSupport())
                .max().orElse(0);
        int rivalMaxCoins = session.getParties().stream()
                .filter(p -> p.isActive() && !p.getId().equals(proposer.getId()))
                .mapToInt(p -> p.getStats().getCoins())
                .max().orElse(0);

        boolean proposerInStrongPosition = proposer.getStats().getPublicSupport() >= rivalMaxSupport || proposer.getStats().getCoins() >= rivalMaxCoins + 25;
        boolean proposerDominant = proposer.getStats().getPublicSupport() >= rivalMaxSupport + 15 || proposer.getStats().getCoins() >= 2 * Math.max(1, rivalMaxCoins);

        boolean aiInStrongPosition = party.getStats().getPublicSupport() >= 35 && party.getStats().getCoins() >= 80;

        // STRATEGIC EVALUATION RULES:

        // A. Proposer is Dominant -> Aggressively vote NO to defeat the bill and block their lead (unless ally or desperate)
        if (proposerDominant && !isAlly) {
            if (aiNearDefeat && selfGain >= 12.0) {
                return "YES"; // Pragmatic exception: near defeat, grab high gains to survive
            }
            return "NO"; // Refuse bill to block dominant sponsor
        }

        // B. AI Party is Near Defeat -> Vote YES on any positive gain bill to survive and get max resources
        if (aiNearDefeat) {
            if (selfGain > 0.0) {
                return "YES"; // Grab resources to survive
            }
        }

        // C. AI Party is in Strong Position -> Deny bills that give large benefits to rival sponsors
        if (aiInStrongPosition && !isAlly) {
            if (sponsorGain > selfGain * 1.4) {
                return "NO"; // Deny bill to keep rivals down
            }
        }

        // D. Sponsor is in Strong Position -> Prefer NO unless supporter benefit is substantial
        if (proposerInStrongPosition && !isAlly) {
            if (selfGain < sponsorGain * 0.7) {
                return "NO";
            }
        }

        // E. Allies / Same Faction Support
        if (isAlly || (party.getRole() == PartyRole.GOVERNMENT && proposer.getRole() == PartyRole.GOVERNMENT)) {
            if (selfGain + opponentPenalty >= -5.0) {
                return "YES";
            }
        }

        // F. General Benefit Thresholds
        if (selfGain >= 8.0) {
            return "YES"; // Significant supporter gain
        } else if (selfGain <= 0.0) {
            return "NO"; // Negative or zero supporter gain
        }

        // G. Opposition vs Government baseline
        if (party.getRole() == PartyRole.OPPOSITION && proposer.getRole() == PartyRole.GOVERNMENT) {
            return selfGain >= 10.0 ? "YES" : "NO";
        }

        return selfGain > 0 ? "YES" : "NO";
    }

    private double evaluateEffectsScore(java.util.Map<String, Object> effects) {
        if (effects == null || effects.isEmpty()) return 0.0;
        double score = 0.0;
        score += intValue(effects.get("coins")) * 0.5;
        score += intValue(effects.get("publicSupport")) * 3.0;
        score += intValue(effects.get("mediaImage")) * 1.5;
        score += intValue(effects.get("partyMorale")) * 1.5;
        score -= intValue(effects.get("corruptionScore")) * 1.5;
        return score;
    }

    private int intValue(Object val) {
        if (val instanceof Number) {
            return ((Number) val).intValue();
        }
        return 0;
    }
}
