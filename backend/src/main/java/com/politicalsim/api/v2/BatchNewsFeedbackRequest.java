package com.politicalsim.api.v2;

import java.util.Map;

public class BatchNewsFeedbackRequest {
    private String partyId;
    private Map<String, String> selectedNewsReactions;

    public BatchNewsFeedbackRequest() {
    }

    public BatchNewsFeedbackRequest(String partyId, Map<String, String> selectedNewsReactions) {
        this.partyId = partyId;
        this.selectedNewsReactions = selectedNewsReactions;
    }

    public String getPartyId() {
        return partyId;
    }

    public void setPartyId(String partyId) {
        this.partyId = partyId;
    }

    public Map<String, String> getSelectedNewsReactions() {
        return selectedNewsReactions;
    }

    public void setSelectedNewsReactions(Map<String, String> selectedNewsReactions) {
        this.selectedNewsReactions = selectedNewsReactions;
    }
}
