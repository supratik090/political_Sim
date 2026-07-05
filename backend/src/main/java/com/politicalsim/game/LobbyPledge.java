package com.politicalsim.game;

public class LobbyPledge {
    private String partyId;
    private String billKey;

    public LobbyPledge() {}

    public LobbyPledge(String partyId, String billKey) {
        this.partyId = partyId;
        this.billKey = billKey;
    }

    public String getPartyId() {
        return partyId;
    }

    public void setPartyId(String partyId) {
        this.partyId = partyId;
    }

    public String getBillKey() {
        return billKey;
    }

    public void setBillKey(String billKey) {
        this.billKey = billKey;
    }
}
