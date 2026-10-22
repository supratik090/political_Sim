package com.politicalsim.api.v2;

import java.util.Map;

public class NewsFeedbackResponse {
    private String newsKey;
    private String reactionKey;
    private boolean backfired;
    private String headline;
    private String narrative;
    private Map<String, Integer> netDeltas;
    private int coinAward;
    private int riskChance;
    private boolean rollHit;
    private int crisisDurationDelta;
    private boolean tripleMultiplier;

    public NewsFeedbackResponse() {
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

    public Map<String, Integer> getNetDeltas() {
        return netDeltas;
    }

    public void setNetDeltas(Map<String, Integer> netDeltas) {
        this.netDeltas = netDeltas;
    }

    public int getCoinAward() {
        return coinAward;
    }

    public void setCoinAward(int coinAward) {
        this.coinAward = coinAward;
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

    public boolean isTripleMultiplier() {
        return tripleMultiplier;
    }

    public void setTripleMultiplier(boolean tripleMultiplier) {
        this.tripleMultiplier = tripleMultiplier;
    }
}
