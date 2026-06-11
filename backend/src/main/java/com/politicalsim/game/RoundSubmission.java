package com.politicalsim.game;

import java.util.LinkedHashMap;
import java.util.Map;

public class RoundSubmission {

    private String partyId;
    private String partyName;
    private String targetPartyId;
    private String targetPartyName;
    private String cardKey;
    private String cardName;
    private String aiIntent;
    private String issueKey;
    private String issueTitle;
    private String issueOptionKey;
    private String issueOptionText;
    private Map<String, String> newsReactions = new LinkedHashMap<>();

    public String getPartyId() {
        return partyId;
    }

    public void setPartyId(String partyId) {
        this.partyId = partyId;
    }

    public String getPartyName() {
        return partyName;
    }

    public void setPartyName(String partyName) {
        this.partyName = partyName;
    }

    public String getTargetPartyId() {
        return targetPartyId;
    }

    public void setTargetPartyId(String targetPartyId) {
        this.targetPartyId = targetPartyId;
    }

    public String getTargetPartyName() {
        return targetPartyName;
    }

    public void setTargetPartyName(String targetPartyName) {
        this.targetPartyName = targetPartyName;
    }

    public String getCardKey() {
        return cardKey;
    }

    public void setCardKey(String cardKey) {
        this.cardKey = cardKey;
    }

    public String getCardName() {
        return cardName;
    }

    public void setCardName(String cardName) {
        this.cardName = cardName;
    }

    public String getAiIntent() {
        return aiIntent;
    }

    public void setAiIntent(String aiIntent) {
        this.aiIntent = aiIntent;
    }

    public String getIssueKey() {
        return issueKey;
    }

    public void setIssueKey(String issueKey) {
        this.issueKey = issueKey;
    }

    public String getIssueTitle() {
        return issueTitle;
    }

    public void setIssueTitle(String issueTitle) {
        this.issueTitle = issueTitle;
    }

    public String getIssueOptionKey() {
        return issueOptionKey;
    }

    public void setIssueOptionKey(String issueOptionKey) {
        this.issueOptionKey = issueOptionKey;
    }

    public String getIssueOptionText() {
        return issueOptionText;
    }

    public void setIssueOptionText(String issueOptionText) {
        this.issueOptionText = issueOptionText;
    }

    public Map<String, String> getNewsReactions() {
        return newsReactions;
    }

    public void setNewsReactions(Map<String, String> newsReactions) {
        this.newsReactions = newsReactions;
    }

    private int bid;

    public int getBid() {
        return bid;
    }

    public void setBid(int bid) {
        this.bid = bid;
    }

    private String selectedRewardKey;
    private String rewardTargetPartyId;
    private String rewardTargetPartyName;
    private String rewardName;

    public String getSelectedRewardKey() {
        return selectedRewardKey;
    }

    public void setSelectedRewardKey(String selectedRewardKey) {
        this.selectedRewardKey = selectedRewardKey;
    }

    public String getRewardTargetPartyId() {
        return rewardTargetPartyId;
    }

    public void setRewardTargetPartyId(String rewardTargetPartyId) {
        this.rewardTargetPartyId = rewardTargetPartyId;
    }

    public String getRewardTargetPartyName() {
        return rewardTargetPartyName;
    }

    public void setRewardTargetPartyName(String rewardTargetPartyName) {
        this.rewardTargetPartyName = rewardTargetPartyName;
    }

    public String getRewardName() {
        return rewardName;
    }

    public void setRewardName(String rewardName) {
        this.rewardName = rewardName;
    }
}
