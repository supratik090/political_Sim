package com.politicalsim.api.v2;

public class CardFeedbackRequest {
    private String partyId;
    private String cardKey;
    private String targetPartyId;

    public CardFeedbackRequest() {
    }

    public CardFeedbackRequest(String partyId, String cardKey, String targetPartyId) {
        this.partyId = partyId;
        this.cardKey = cardKey;
        this.targetPartyId = targetPartyId;
    }

    public String getPartyId() {
        return partyId;
    }

    public void setPartyId(String partyId) {
        this.partyId = partyId;
    }

    public String getCardKey() {
        return cardKey;
    }

    public void setCardKey(String cardKey) {
        this.cardKey = cardKey;
    }

    public String getTargetPartyId() {
        return targetPartyId;
    }

    public void setTargetPartyId(String targetPartyId) {
        this.targetPartyId = targetPartyId;
    }
}
