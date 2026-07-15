package com.politicalsim.ai;

import com.politicalsim.game.GameSession;
import com.politicalsim.game.RoundSubmission;
import com.politicalsim.party.PartyState;
import com.politicalsim.party.ProjectState;
import com.politicalsim.game.CooperationOffer;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.UUID;

@Service
public class BrokeFightBackService {

    /**
     * Returns true when the AI party is in distress and should activate crisis response.
     * Uses the unified defeat-hazard thresholds (Coins ≤30, Morale ≤20, Support ≤10, Corruption ≥75).
     */
    public boolean isCrisisActive(PartyState party) {
        return party.hasDefeatHazard();
    }

    /**
     * AI crisis response: take emergency loan if not yet taken, buy recovery pack if affordable,
     * and fall back to legacy liquidation / fire-sale tactics.
     */
    public void executeCrisisResponse(GameSession session, PartyState party, RoundSubmission currentSubmission) {
        // 1. Take emergency loan (once per game, only during defeat hazard)
        if (!party.isLoanTaken()) {
            party.getStats().setCoins(party.getStats().getCoins() + 150);
            party.setLoanTaken(true);
            party.setLoanRepaymentTurnsLeft(10);
        }

        // 2. Buy Recovery Pack if affordable (80 coins) and still in defeat hazard
        if (party.hasDefeatHazard() && party.getStats().getCoins() >= 80) {
            party.getStats().setCoins(party.getStats().getCoins() - 80);
            party.getStats().setPartyMorale(Math.min(100, party.getStats().getPartyMorale() + 20));
            party.getStats().setCorruptionScore(Math.max(0, party.getStats().getCorruptionScore() - 20));
            party.getStats().setPublicSupport(party.getStats().getPublicSupport() + 5);
            party.getStats().setMediaImage(Math.min(100, party.getStats().getMediaImage() + 20));
        }

        int coins = party.getStats().getCoins();
        int morale = party.getStats().getPartyMorale();

        // 3. Save Coins (pass turn if still coin-broke after loan)
        if (coins < 50) {
            currentSubmission.setCardKey("no_card");
            currentSubmission.setCardName("No Card (Pass Turn)");
            currentSubmission.setTargetPartyId(null);
            currentSubmission.setBid(0);
        }

        // 4. Liquidation Pipeline (if morale still critically low)
        if (morale < 15) {
            int targetCoins = 100;

            while (party.getStats().getCoins() < targetCoins) {
                boolean liquidated = liquidateLowestUtilityProject(party);
                if (!liquidated) {
                    break;
                }
            }

            if (party.getStats().getCoins() >= targetCoins) {
                initiateFireSale(session, party, targetCoins, 10);
            }
        }
    }

    private boolean liquidateLowestUtilityProject(PartyState party) {
        ProjectState worstProject = party.getProjects().stream()
                .filter(p -> p.getProgressPercent() >= 100)
                .min(Comparator.comparingDouble(p -> {
                    try {
                        com.politicalsim.party.BuildingProject def = com.politicalsim.party.BuildingProject.valueOf(p.getProjectKey());
                        return def.getBenefitCoins()
                             + def.getBenefitMorale() * 20.0
                             + def.getBenefitSupport() * 50.0
                             + def.getBenefitMedia() * 20.0
                             - def.getBenefitCorruption() * 20.0;
                    } catch (Exception e) {
                        return Double.MAX_VALUE;
                    }
                }))
                .orElse(null);

        if (worstProject != null) {
            try {
                com.politicalsim.party.BuildingProject def = com.politicalsim.party.BuildingProject.valueOf(worstProject.getProjectKey());
                // Refund 50% of original cost
                int refund = (def.getCostCoins() + def.getCostMorale() * 20 + def.getCostSupport() * 50) / 2;
                party.getStats().setCoins(party.getStats().getCoins() + refund);

                worstProject.setProgressPercent(0);
                worstProject.setCompletionTurn(0);
                return true;
            } catch (Exception e) {
                return false;
            }
        }
        return false;
    }

    private void initiateFireSale(GameSession session, PartyState party, int offeredCoins, int requestedMorale) {
        // Find best target (highest morale)
        PartyState bestTarget = session.getParties().stream()
                .filter(p -> !p.getId().equals(party.getId()) && p.isActive())
                .max(Comparator.comparingInt(p -> p.getStats().getPartyMorale()))
                .orElse(null);

        if (bestTarget != null) {
            // Reserve coins immediately so we don't spend them elsewhere
            party.getStats().setCoins(party.getStats().getCoins() - offeredCoins);

            CooperationOffer offer = new CooperationOffer();
            offer.setId(UUID.randomUUID().toString());
            offer.setTurnCreated(session.getTurnNumber());
            offer.setStatus(CooperationOffer.OfferStatus.PENDING);
            offer.setType(CooperationOffer.OfferType.EXCHANGE);
            offer.setSenderPartyId(party.getId());
            offer.setSenderPartyName(party.getName());
            offer.setRecipientPartyId(bestTarget.getId());
            offer.setRecipientPartyName(bestTarget.getName());
            offer.setDurationTurns(0);

            offer.setOfferedCoins(offeredCoins);
            offer.setRequestedMorale(requestedMorale);

            if (session.getCooperationOffers() == null) {
                session.setCooperationOffers(new ArrayList<>());
            }
            session.getCooperationOffers().add(offer);
        }
    }
}
