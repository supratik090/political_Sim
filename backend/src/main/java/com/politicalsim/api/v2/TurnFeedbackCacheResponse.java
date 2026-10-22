package com.politicalsim.api.v2;

import java.util.LinkedHashMap;
import java.util.Map;

/**
 * Pre-populated Turn Feedback Cache DTO.
 * Contains pre-computed feedback for all breaking news options and available cards in the current turn.
 */
public class TurnFeedbackCacheResponse {
    private int turnNumber;
    private String partyId;
    private Map<String, NewsFeedbackResponse> news = new LinkedHashMap<>();
    private Map<String, CardFeedbackResponse> cards = new LinkedHashMap<>();

    public TurnFeedbackCacheResponse() {
    }

    public TurnFeedbackCacheResponse(int turnNumber, String partyId) {
        this.turnNumber = turnNumber;
        this.partyId = partyId;
    }

    public int getTurnNumber() {
        return turnNumber;
    }

    public void setTurnNumber(int turnNumber) {
        this.turnNumber = turnNumber;
    }

    public String getPartyId() {
        return partyId;
    }

    public void setPartyId(String partyId) {
        this.partyId = partyId;
    }

    public Map<String, NewsFeedbackResponse> getNews() {
        return news;
    }

    public void setNews(Map<String, NewsFeedbackResponse> news) {
        this.news = news;
    }

    public Map<String, CardFeedbackResponse> getCards() {
        return cards;
    }

    public void setCards(Map<String, CardFeedbackResponse> cards) {
        this.cards = cards;
    }
}
