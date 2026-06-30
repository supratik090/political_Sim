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

    public boolean isCrisisActive(PartyState party) {
        int coins = party.getStats().getCoins();
        int morale = party.getStats().getPartyMorale();
        
        boolean wasBroke = party.isBrokeStateActive();
        
        if (!wasBroke) {
            // Activation
            if (coins < 50 || morale < 15) {
                return true;
            }
            return false;
        } else {
            // Deactivation (Safe limits)
            if (coins >= 80 && morale >= 35) {
                return false;
            }
            return true;
        }
    }

    public void executeCrisisResponse(GameSession session, PartyState party, RoundSubmission currentSubmission) {
        int coins = party.getStats().getCoins();
        int morale = party.getStats().getPartyMorale();

        // 1. Save Coins (If Coin Broke)
        if (coins < 50) {
            currentSubmission.setCardKey("no_card");
            currentSubmission.setCardName("No Card (Pass Turn)");
            currentSubmission.setTargetPartyId(null);
            currentSubmission.setBid(0);
        }

        // 2. Liquidation Pipeline (If Morale Broke)
        if (morale < 15) {
            int targetCoins = 100;
            
            // Liquidate projects until we have 100 Coins
            while (party.getStats().getCoins() < targetCoins) {
                boolean liquidated = liquidateLowestUtilityProject(party);
                if (!liquidated) {
                    break; // No more projects to liquidate
                }
            }
            
            // If we managed to get 100 Coins, initiate Fire Sale
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
                
                // Remove project
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
        // Find best target (wealthiest or highest morale)
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
