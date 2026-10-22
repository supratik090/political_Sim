package com.politicalsim.api.v2;

public class NewsFeedbackRequest {
    private String partyId;
    private String newsKey;
    private String reactionKey;

    public NewsFeedbackRequest() {
    }

    public NewsFeedbackRequest(String partyId, String newsKey, String reactionKey) {
        this.partyId = partyId;
        this.newsKey = newsKey;
        this.reactionKey = reactionKey;
    }

    public String getPartyId() {
        return partyId;
    }

    public void setPartyId(String partyId) {
        this.partyId = partyId;
    }

    public String getNewsKey() {
        return newsKey;
    }

    public void setNewsKey(String newsKey) {
        this.newsKey = newsKey;
    }

    public String getReactionKey() {
        return reactionKey;
    }

    public void setReactionKey(String reactionKey) {
        this.reactionKey = reactionKey;
    }
}
