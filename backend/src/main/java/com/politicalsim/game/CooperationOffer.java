package com.politicalsim.game;

import java.util.ArrayList;
import java.util.List;

public class CooperationOffer {
    public enum OfferType {
        EXCHANGE,
        NON_AGGRESSION
    }

    public enum OfferStatus {
        PENDING,
        ACCEPTED,
        REJECTED,
        EXPIRED
    }

    private String id;
    private String senderPartyId;
    private String senderPartyName;
    private String recipientPartyId;
    private String recipientPartyName;
    private OfferType type;
    
    // Exchange details
    private int offeredCoins;
    private int offeredMorale;
    private int offeredSupport;
    private List<String> offeredBuildingKeys = new ArrayList<>();
    
    private int requestedCoins;
    private int requestedSupport;
    private int requestedMorale;
    
    // Non-aggression details
    private int durationTurns;
    private boolean senderPaysPact; // true if sender pays recipient, false otherwise
    private String pactPaymentResource; // COINS, MORALE, SUPPORT, COMPLETED_BUILDING
    private int pactPaymentValue;
    private List<String> pactPaymentBuildingKeys = new ArrayList<>();
    
    private OfferStatus status;
    private int turnCreated;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getSenderPartyId() {
        return senderPartyId;
    }

    public void setSenderPartyId(String senderPartyId) {
        this.senderPartyId = senderPartyId;
    }

    public String getSenderPartyName() {
        return senderPartyName;
    }

    public void setSenderPartyName(String senderPartyName) {
        this.senderPartyName = senderPartyName;
    }

    public String getRecipientPartyId() {
        return recipientPartyId;
    }

    public void setRecipientPartyId(String recipientPartyId) {
        this.recipientPartyId = recipientPartyId;
    }

    public String getRecipientPartyName() {
        return recipientPartyName;
    }

    public void setRecipientPartyName(String recipientPartyName) {
        this.recipientPartyName = recipientPartyName;
    }

    public OfferType getType() {
        return type;
    }

    public void setType(OfferType type) {
        this.type = type;
    }

    public int getOfferedCoins() {
        return offeredCoins;
    }

    public void setOfferedCoins(int offeredCoins) {
        this.offeredCoins = offeredCoins;
    }

    public int getOfferedMorale() {
        return offeredMorale;
    }

    public void setOfferedMorale(int offeredMorale) {
        this.offeredMorale = offeredMorale;
    }

    public int getOfferedSupport() {
        return offeredSupport;
    }

    public void setOfferedSupport(int offeredSupport) {
        this.offeredSupport = offeredSupport;
    }

    public List<String> getOfferedBuildingKeys() {
        if (offeredBuildingKeys == null) {
            offeredBuildingKeys = new ArrayList<>();
        }
        return offeredBuildingKeys;
    }

    public void setOfferedBuildingKeys(List<String> offeredBuildingKeys) {
        this.offeredBuildingKeys = offeredBuildingKeys;
    }

    public int getRequestedCoins() {
        return requestedCoins;
    }

    public void setRequestedCoins(int requestedCoins) {
        this.requestedCoins = requestedCoins;
    }

    public int getRequestedSupport() {
        return requestedSupport;
    }

    public void setRequestedSupport(int requestedSupport) {
        this.requestedSupport = requestedSupport;
    }

    public int getRequestedMorale() {
        return requestedMorale;
    }

    public void setRequestedMorale(int requestedMorale) {
        this.requestedMorale = requestedMorale;
    }

    public int getDurationTurns() {
        return durationTurns;
    }

    public void setDurationTurns(int durationTurns) {
        this.durationTurns = durationTurns;
    }

    public boolean isSenderPaysPact() {
        return senderPaysPact;
    }

    public void setSenderPaysPact(boolean senderPaysPact) {
        this.senderPaysPact = senderPaysPact;
    }

    public String getPactPaymentResource() {
        return pactPaymentResource;
    }

    public void setPactPaymentResource(String pactPaymentResource) {
        this.pactPaymentResource = pactPaymentResource;
    }

    public int getPactPaymentValue() {
        return pactPaymentValue;
    }

    public void setPactPaymentValue(int pactPaymentValue) {
        this.pactPaymentValue = pactPaymentValue;
    }

    public List<String> getPactPaymentBuildingKeys() {
        if (pactPaymentBuildingKeys == null) {
            pactPaymentBuildingKeys = new ArrayList<>();
        }
        return pactPaymentBuildingKeys;
    }

    public void setPactPaymentBuildingKeys(List<String> pactPaymentBuildingKeys) {
        this.pactPaymentBuildingKeys = pactPaymentBuildingKeys;
    }

    public OfferStatus getStatus() {
        return status;
    }

    public void setStatus(OfferStatus status) {
        this.status = status;
    }

    public int getTurnCreated() {
        return turnCreated;
    }

    public void setTurnCreated(int turnCreated) {
        this.turnCreated = turnCreated;
    }
}
