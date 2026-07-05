package com.politicalsim.game;

public class LegislativeBillState {
    private String billKey;
    private String status = "NOT_PROPOSED"; // NOT_PROPOSED, PENDING_VOTE, PASSED, FAILED
    private String proposedByPartyId;
    private int turnProposed;
    private int turnResolved;

    public LegislativeBillState() {}

    public LegislativeBillState(String billKey) {
        this.billKey = billKey;
    }

    public String getBillKey() {
        return billKey;
    }

    public void setBillKey(String billKey) {
        this.billKey = billKey;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getProposedByPartyId() {
        return proposedByPartyId;
    }

    public void setProposedByPartyId(String proposedByPartyId) {
        this.proposedByPartyId = proposedByPartyId;
    }

    public int getTurnProposed() {
        return turnProposed;
    }

    public void setTurnProposed(int turnProposed) {
        this.turnProposed = turnProposed;
    }

    public int getTurnResolved() {
        return turnResolved;
    }

    public void setTurnResolved(int turnResolved) {
        this.turnResolved = turnResolved;
    }
}
