package com.politicalsim.game;

import com.politicalsim.party.PartyState;
import com.politicalsim.party.ProjectState;
import java.util.ArrayList;
import java.util.List;

public class CooperationResolver {
    private final GameService gameService;

    public CooperationResolver(GameService gameService) {
        this.gameService = gameService;
    }

    public void validateOfferSenderAssets(GameSession session, PartyState sender, CooperationOffer offer) {
        if (offer.getType() == CooperationOffer.OfferType.EXCHANGE) {
            if (sender.getStats().getCoins() < offer.getOfferedCoins()) {
                throw new IllegalArgumentException(sender.getName() + " does not have enough Coins to offer (" + offer.getOfferedCoins() + ").");
            }
            if (sender.getStats().getPartyMorale() < offer.getOfferedMorale()) {
                throw new IllegalArgumentException(sender.getName() + " does not have enough Morale to offer (" + offer.getOfferedMorale() + ").");
            }
            if (sender.getStats().getPublicSupport() < offer.getOfferedSupport()) {
                throw new IllegalArgumentException(sender.getName() + " does not have enough Support to offer (" + offer.getOfferedSupport() + "%).");
            }
            if (offer.getOfferedBuildingKeys() != null) {
                for (String key : offer.getOfferedBuildingKeys()) {
                    boolean hasCompleted = sender.getProjects().stream()
                        .anyMatch(p -> p.getProjectKey().equals(key) && p.getProgressPercent() >= 100);
                    if (!hasCompleted) {
                        throw new IllegalArgumentException(sender.getName() + " does not own a completed building: " + key);
                    }
                }
            }
        } else if (offer.getType() == CooperationOffer.OfferType.LOBBYING) {
            if (sender.getStats().getCoins() < offer.getOfferedCoins()) {
                throw new IllegalArgumentException(sender.getName() + " does not have enough Coins to offer (" + offer.getOfferedCoins() + ").");
            }
            if (sender.getStats().getPartyMorale() < offer.getOfferedMorale()) {
                throw new IllegalArgumentException(sender.getName() + " does not have enough Morale to offer (" + offer.getOfferedMorale() + ").");
            }
            if (sender.getStats().getMediaImage() < offer.getOfferedMedia()) {
                throw new IllegalArgumentException(sender.getName() + " does not have enough Media Image to offer (" + offer.getOfferedMedia() + ").");
            }
            if (offer.getOfferedBuildingKeys() != null) {
                for (String key : offer.getOfferedBuildingKeys()) {
                    boolean hasCompleted = sender.getProjects().stream()
                        .anyMatch(p -> p.getProjectKey().equals(key) && p.getProgressPercent() >= 100);
                    if (!hasCompleted) {
                        throw new IllegalArgumentException(sender.getName() + " does not own a completed building: " + key);
                    }
                }
            }
        } else if (offer.getType() == CooperationOffer.OfferType.NON_AGGRESSION && offer.isSenderPaysPact()) {
            validatePactPayment(sender, offer);
        }
    }

    public void validateOfferRecipientAssets(GameSession session, PartyState recipient, CooperationOffer offer) {
        if (offer.getType() == CooperationOffer.OfferType.EXCHANGE) {
            if (recipient.getStats().getCoins() < offer.getRequestedCoins()) {
                throw new IllegalArgumentException(recipient.getName() + " does not have enough Coins to pay (" + offer.getRequestedCoins() + ").");
            }
            if (recipient.getStats().getPartyMorale() < offer.getRequestedMorale()) {
                throw new IllegalArgumentException(recipient.getName() + " does not have enough Morale to pay (" + offer.getRequestedMorale() + ").");
            }
            if (recipient.getStats().getPublicSupport() < offer.getRequestedSupport()) {
                throw new IllegalArgumentException(recipient.getName() + " does not have enough Support to pay (" + offer.getRequestedSupport() + "%).");
            }
        } else if (offer.getType() == CooperationOffer.OfferType.NON_AGGRESSION && !offer.isSenderPaysPact()) {
            validatePactPayment(recipient, offer);
        }
    }

    public void validatePactPayment(PartyState payer, CooperationOffer offer) {
        String res = offer.getPactPaymentResource();
        int val = offer.getPactPaymentValue();
        if ("COINS".equalsIgnoreCase(res) && payer.getStats().getCoins() < val) {
            throw new IllegalArgumentException(payer.getName() + " does not have enough Coins (" + val + ").");
        }
        if ("MORALE".equalsIgnoreCase(res) && payer.getStats().getPartyMorale() < val) {
            throw new IllegalArgumentException(payer.getName() + " does not have enough Morale (" + val + ").");
        }
        if ("SUPPORT".equalsIgnoreCase(res) && payer.getStats().getPublicSupport() < val) {
            throw new IllegalArgumentException(payer.getName() + " does not have enough Support (" + val + "%).");
        }
        if ("COMPLETED_BUILDING".equalsIgnoreCase(res) && offer.getPactPaymentBuildingKeys() != null) {
            for (String key : offer.getPactPaymentBuildingKeys()) {
                boolean hasCompleted = payer.getProjects().stream()
                    .anyMatch(p -> p.getProjectKey().equals(key) && p.getProgressPercent() >= 100);
                if (!hasCompleted) {
                    throw new IllegalArgumentException(payer.getName() + " does not own completed building: " + key);
                }
            }
        }
    }

    public String getOfferDescription(CooperationOffer offer) {
        if (offer.getType() == CooperationOffer.OfferType.LOBBYING) {
            StringBuilder sb = new StringBuilder();
            sb.append("Lobbying support for bill '").append(offer.getLobbyBillKey()).append("' (Offers: ");
            List<String> itemsOffered = new ArrayList<>();
            if (offer.getOfferedCoins() > 0) itemsOffered.add(offer.getOfferedCoins() + " Coins");
            if (offer.getOfferedMorale() > 0) itemsOffered.add(offer.getOfferedMorale() + " Morale");
            if (offer.getOfferedMedia() > 0) itemsOffered.add(offer.getOfferedMedia() + " Media Image");
            if (offer.getOfferedBuildingKeys() != null && !offer.getOfferedBuildingKeys().isEmpty()) {
                itemsOffered.add("Buildings: " + offer.getOfferedBuildingKeys());
            }
            if (offer.getDurationTurns() > 0) {
                itemsOffered.add(offer.getDurationTurns() + "-turn Non-Aggression Pact");
            }
            sb.append(String.join(", ", itemsOffered)).append(")");
            return sb.toString();
        }
        if (offer.getType() == CooperationOffer.OfferType.NON_AGGRESSION) {
            StringBuilder sb = new StringBuilder();
            sb.append(offer.getDurationTurns()).append("-turn Non-Aggression Pact");
            if (offer.getPactPaymentValue() > 0 || (offer.getPactPaymentBuildingKeys() != null && !offer.getPactPaymentBuildingKeys().isEmpty())) {
                String payerName = offer.isSenderPaysPact() ? offer.getSenderPartyName() : offer.getRecipientPartyName();
                sb.append(" with payment of ");
                if (offer.getPactPaymentBuildingKeys() != null && !offer.getPactPaymentBuildingKeys().isEmpty()) {
                    sb.append("Buildings: ").append(offer.getPactPaymentBuildingKeys());
                } else {
                    sb.append(offer.getPactPaymentValue()).append(" ").append(offer.getPactPaymentResource());
                }
                sb.append(" paid by ").append(payerName);
            }
            return sb.toString();
        } else {
            StringBuilder sb = new StringBuilder();
            sb.append("Exchanging (Offers: ");
            List<String> itemsOffered = new ArrayList<>();
            if (offer.getOfferedCoins() > 0) itemsOffered.add(offer.getOfferedCoins() + " Coins");
            if (offer.getOfferedMorale() > 0) itemsOffered.add(offer.getOfferedMorale() + " Morale");
            if (offer.getOfferedSupport() > 0) itemsOffered.add(offer.getOfferedSupport() + "% Support");
            if (offer.getOfferedBuildingKeys() != null && !offer.getOfferedBuildingKeys().isEmpty()) {
                itemsOffered.add("Buildings: " + offer.getOfferedBuildingKeys());
            }
            sb.append(String.join(", ", itemsOffered));
            
            sb.append(" for Requests: ");
            List<String> itemsRequested = new ArrayList<>();
            if (offer.getRequestedCoins() > 0) itemsRequested.add(offer.getRequestedCoins() + " Coins");
            if (offer.getRequestedSupport() > 0) itemsRequested.add(offer.getRequestedSupport() + "% Support");
            if (offer.getRequestedMorale() > 0) itemsRequested.add(offer.getRequestedMorale() + " Morale");
            sb.append(String.join(", ", itemsRequested)).append(")");
            return sb.toString();
        }
    }

    public void executeCooperationTrade(GameSession session, CooperationOffer offer) {
        PartyState sender = gameService.findParty(session, offer.getSenderPartyId());
        PartyState recipient = gameService.findParty(session, offer.getRecipientPartyId());
        
        if (offer.getType() == CooperationOffer.OfferType.EXCHANGE) {
            // Transfer Offered Resources (Sender -> Recipient)
            if (offer.getOfferedCoins() > 0) {
                sender.getStats().setCoins(sender.getStats().getCoins() - offer.getOfferedCoins());
                recipient.getStats().setCoins(recipient.getStats().getCoins() + offer.getOfferedCoins());
            }
            if (offer.getOfferedMorale() > 0) {
                sender.getStats().setPartyMorale(sender.getStats().getPartyMorale() - offer.getOfferedMorale());
                recipient.getStats().setPartyMorale(recipient.getStats().getPartyMorale() + offer.getOfferedMorale());
            }
            if (offer.getOfferedSupport() > 0) {
                sender.getStats().setPublicSupport(sender.getStats().getPublicSupport() - offer.getOfferedSupport());
                recipient.getStats().setPublicSupport(recipient.getStats().getPublicSupport() + offer.getOfferedSupport());
            }
            if (offer.getOfferedBuildingKeys() != null && !offer.getOfferedBuildingKeys().isEmpty()) {
                for (String bkey : offer.getOfferedBuildingKeys()) {
                    ProjectState pState = sender.getProjects().stream()
                        .filter(p -> p.getProjectKey().equals(bkey) && p.getProgressPercent() >= 100)
                        .findFirst().orElse(null);
                    if (pState != null) {
                        sender.getProjects().remove(pState);
                        recipient.getProjects().add(pState);
                    }
                }
            }
            
            // Transfer Requested Resources (Recipient -> Sender)
            if (offer.getRequestedCoins() > 0) {
                recipient.getStats().setCoins(recipient.getStats().getCoins() - offer.getRequestedCoins());
                sender.getStats().setCoins(sender.getStats().getCoins() + offer.getRequestedCoins());
            }
            if (offer.getRequestedSupport() > 0) {
                recipient.getStats().setPublicSupport(recipient.getStats().getPublicSupport() - offer.getRequestedSupport());
                sender.getStats().setPublicSupport(sender.getStats().getPublicSupport() + offer.getRequestedSupport());
            }
            if (offer.getRequestedMorale() > 0) {
                recipient.getStats().setPartyMorale(recipient.getStats().getPartyMorale() - offer.getRequestedMorale());
                sender.getStats().setPartyMorale(sender.getStats().getPartyMorale() + offer.getRequestedMorale());
            }
        } else if (offer.getType() == CooperationOffer.OfferType.NON_AGGRESSION) {
            if (offer.getPactPaymentValue() > 0 || (offer.getPactPaymentBuildingKeys() != null && !offer.getPactPaymentBuildingKeys().isEmpty())) {
                PartyState payer = offer.isSenderPaysPact() ? sender : recipient;
                PartyState payee = offer.isSenderPaysPact() ? recipient : sender;
                String res = offer.getPactPaymentResource();
                int val = offer.getPactPaymentValue();
                
                if ("COINS".equalsIgnoreCase(res)) {
                    payer.getStats().setCoins(payer.getStats().getCoins() - val);
                    payee.getStats().setCoins(payee.getStats().getCoins() + val);
                } else if ("MORALE".equalsIgnoreCase(res)) {
                    payer.getStats().setPartyMorale(payer.getStats().getPartyMorale() - val);
                    payee.getStats().setPartyMorale(payee.getStats().getPartyMorale() + val);
                } else if ("SUPPORT".equalsIgnoreCase(res)) {
                    payer.getStats().setPublicSupport(payer.getStats().getPublicSupport() - val);
                    payee.getStats().setPublicSupport(payee.getStats().getPublicSupport() + val);
                } else if ("COMPLETED_BUILDING".equalsIgnoreCase(res) && offer.getPactPaymentBuildingKeys() != null) {
                    for (String bkey : offer.getPactPaymentBuildingKeys()) {
                        ProjectState pState = payer.getProjects().stream()
                            .filter(p -> p.getProjectKey().equals(bkey) && p.getProgressPercent() >= 100)
                            .findFirst().orElse(null);
                        if (pState != null) {
                            payer.getProjects().remove(pState);
                            payee.getProjects().add(pState);
                        }
                    }
                }
            }
            
            NonAggressionPact pact = new NonAggressionPact(
                java.util.UUID.randomUUID().toString(),
                sender.getId(),
                sender.getName(),
                recipient.getId(),
                recipient.getName(),
                offer.getDurationTurns()
            );
            session.getActivePacts().add(pact);
        } else if (offer.getType() == CooperationOffer.OfferType.LOBBYING) {
            // Transfer Offered Resources (Sender -> Recipient)
            if (offer.getOfferedCoins() > 0) {
                sender.getStats().setCoins(sender.getStats().getCoins() - offer.getOfferedCoins());
                recipient.getStats().setCoins(recipient.getStats().getCoins() + offer.getOfferedCoins());
            }
            if (offer.getOfferedMorale() > 0) {
                sender.getStats().setPartyMorale(sender.getStats().getPartyMorale() - offer.getOfferedMorale());
                recipient.getStats().setPartyMorale(recipient.getStats().getPartyMorale() + offer.getOfferedMorale());
            }
            if (offer.getOfferedMedia() > 0) {
                sender.getStats().setMediaImage(Math.max(0, sender.getStats().getMediaImage() - offer.getOfferedMedia()));
                recipient.getStats().setMediaImage(Math.min(100, recipient.getStats().getMediaImage() + offer.getOfferedMedia()));
            }
            if (offer.getOfferedBuildingKeys() != null && !offer.getOfferedBuildingKeys().isEmpty()) {
                for (String bkey : offer.getOfferedBuildingKeys()) {
                    ProjectState pState = sender.getProjects().stream()
                        .filter(p -> p.getProjectKey().equals(bkey) && p.getProgressPercent() >= 100)
                        .findFirst().orElse(null);
                    if (pState != null) {
                        sender.getProjects().remove(pState);
                        recipient.getProjects().add(pState);
                    }
                }
            }

            // If non-aggression pact offered along with lobbying
            if (offer.getDurationTurns() > 0) {
                NonAggressionPact pact = new NonAggressionPact(
                    java.util.UUID.randomUUID().toString(),
                    sender.getId(),
                    sender.getName(),
                    recipient.getId(),
                    recipient.getName(),
                    offer.getDurationTurns()
                );
                session.getActivePacts().add(pact);
            }

            // Create binding vote pledge
            session.getLobbyPledges().add(new LobbyPledge(recipient.getId(), offer.getLobbyBillKey()));
        }
    }
}
