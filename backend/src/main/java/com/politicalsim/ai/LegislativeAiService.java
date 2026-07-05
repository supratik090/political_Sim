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

        // 3. Coalition / Alliance Check (Accepted Cooperation Offers)
        boolean isAlly = session.getCooperationOffers().stream()
                .anyMatch(offer -> offer.getStatus() == CooperationOffer.OfferStatus.ACCEPTED &&
                        ((offer.getSenderPartyId().equals(party.getId()) && offer.getRecipientPartyId().equals(proposerId)) ||
                         (offer.getSenderPartyId().equals(proposerId) && offer.getRecipientPartyId().equals(party.getId()))));
        if (isAlly) {
            return "YES";
        }

        // 4. Same Government Coalition Check
        PartyState proposer = session.getParties().stream()
                .filter(p -> p.getId().equals(proposerId))
                .findFirst().orElse(null);
        if (proposer == null) {
            return "ABSTAIN";
        }
        if (party.getRole() == PartyRole.GOVERNMENT && proposer.getRole() == PartyRole.GOVERNMENT) {
            return "YES";
        }

        // 5. Utility / Popularity Check (Effects Evaluation)
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
        if (billDef == null) {
            return "ABSTAIN";
        }

        int supportEffect = 0;
        int mediaEffect = 0;
        int corruptionEffect = 0;
        if (billDef.getEffectsPassed() != null) {
            supportEffect = intValue(billDef.getEffectsPassed().get("publicSupport"));
            mediaEffect = intValue(billDef.getEffectsPassed().get("mediaImage"));
            corruptionEffect = intValue(billDef.getEffectsPassed().get("corruptionScore"));
        }

        boolean isPopular = (supportEffect > 0 || mediaEffect > 0) && corruptionEffect <= 0;
        boolean isHighlyUnpopular = (supportEffect < 0 || mediaEffect < 0 || corruptionEffect > 5);

        // Opposition vs Government
        if (proposer.getRole() == PartyRole.GOVERNMENT) {
            if (party.getRole() == PartyRole.OPPOSITION) {
                if (isHighlyUnpopular) {
                    return "NO";
                }
                if (isPopular && supportEffect >= 3) {
                    return "YES"; // Too popular to oppose
                }
                return "NO"; // Oppose government bills by default
            } else {
                // Independent / Third party
                if (isPopular) return "YES";
                if (isHighlyUnpopular) return "NO";
                return "ABSTAIN";
            }
        } else {
            // Proposer is Opposition/others
            if (party.getRole() == PartyRole.GOVERNMENT) {
                return "NO"; // Government opposes opposition bills by default
            } else if (party.getRole() == PartyRole.OPPOSITION) {
                if (isHighlyUnpopular) {
                    return "ABSTAIN"; // Opposition unity but too unpopular
                }
                return "YES"; // Opposition unity
            } else {
                // Independent / Third party
                if (isPopular) return "YES";
                return "ABSTAIN";
            }
        }
    }

    private int intValue(Object val) {
        if (val instanceof Number) {
            return ((Number) val).intValue();
        }
        return 0;
    }
}
