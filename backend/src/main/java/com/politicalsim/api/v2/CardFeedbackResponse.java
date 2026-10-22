package com.politicalsim.api.v2;

import java.util.Map;

public class CardFeedbackResponse {
    private String cardKey;
    private String targetPartyId;
    private int cost;
    private boolean tripleMultiplier;
    private String tripleReason;
    private boolean backfired;
    private String headline;
    private String narrative;
    private Map<String, Integer> selfDeltas;
    private Map<String, Integer> opponentDeltas;
    private int riskChance;
    private boolean rollHit;
    private int crisisDurationDelta;

    public CardFeedbackResponse() {
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

    public int getCost() {
        return cost;
    }

    public void setCost(int cost) {
        this.cost = cost;
    }

    public boolean isTripleMultiplier() {
        return tripleMultiplier;
    }

    public void setTripleMultiplier(boolean tripleMultiplier) {
        this.tripleMultiplier = tripleMultiplier;
    }

    public String getTripleReason() {
        return tripleReason;
    }

    public void setTripleReason(String tripleReason) {
        this.tripleReason = tripleReason;
    }

    public boolean isBackfired() {
        return backfired;
    }

    public void setBackfired(boolean backfired) {
        this.backfired = backfired;
    }

    public String getHeadline() {
        return headline;
    }

    public void setHeadline(String headline) {
        this.headline = headline;
    }

    public String getNarrative() {
        return narrative;
    }

    public void setNarrative(String narrative) {
        this.narrative = narrative;
    }

    public Map<String, Integer> getSelfDeltas() {
        return selfDeltas;
    }

    public void setSelfDeltas(Map<String, Integer> selfDeltas) {
        this.selfDeltas = selfDeltas;
    }

    public Map<String, Integer> getOpponentDeltas() {
        return opponentDeltas;
    }

    public void setOpponentDeltas(Map<String, Integer> opponentDeltas) {
        this.opponentDeltas = opponentDeltas;
    }

    public int getRiskChance() {
        return riskChance;
    }

    public void setRiskChance(int riskChance) {
        this.riskChance = riskChance;
    }

    public boolean isRollHit() {
        return rollHit;
    }

    public void setRollHit(boolean rollHit) {
        this.rollHit = rollHit;
    }

    public int getCrisisDurationDelta() {
        return crisisDurationDelta;
    }

    public void setCrisisDurationDelta(int crisisDurationDelta) {
        this.crisisDurationDelta = crisisDurationDelta;
    }
}
