package com.politicalsim.api;

import java.util.LinkedHashMap;
import java.util.Map;

public class TurnAdvanceRequest {

    private String selectedCardKey;
    private String targetPartyId;
    private String selectedIssueOptionKey;
    private Map<String, String> selectedNewsReactions = new LinkedHashMap<>();

    public String getSelectedCardKey() {
        return selectedCardKey;
    }

    public void setSelectedCardKey(String selectedCardKey) {
        this.selectedCardKey = selectedCardKey;
    }

    public String getTargetPartyId() {
        return targetPartyId;
    }

    public void setTargetPartyId(String targetPartyId) {
        this.targetPartyId = targetPartyId;
    }

    public String getSelectedIssueOptionKey() {
        return selectedIssueOptionKey;
    }

    public void setSelectedIssueOptionKey(String selectedIssueOptionKey) {
        this.selectedIssueOptionKey = selectedIssueOptionKey;
    }

    public Map<String, String> getSelectedNewsReactions() {
        return selectedNewsReactions;
    }

    public void setSelectedNewsReactions(Map<String, String> selectedNewsReactions) {
        this.selectedNewsReactions = selectedNewsReactions;
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
    private String proposedBillKey;
    private String billVote; // "YES", "NO", "ABSTAIN"
    private String selectedEventOptionKey;
    private boolean whipIssued;

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

    public String getProposedBillKey() {
        return proposedBillKey;
    }

    public void setProposedBillKey(String proposedBillKey) {
        this.proposedBillKey = proposedBillKey;
    }

    public String getBillVote() {
        return billVote;
    }

    public void setBillVote(String billVote) {
        this.billVote = billVote;
    }

    public String getSelectedEventOptionKey() {
        return selectedEventOptionKey;
    }

    public void setSelectedEventOptionKey(String selectedEventOptionKey) {
        this.selectedEventOptionKey = selectedEventOptionKey;
    }

    public boolean isWhipIssued() {
        return whipIssued;
    }

    public void setWhipIssued(boolean whipIssued) {
        this.whipIssued = whipIssued;
    }
}
