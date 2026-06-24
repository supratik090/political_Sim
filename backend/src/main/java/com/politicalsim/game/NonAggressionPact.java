package com.politicalsim.game;

public class NonAggressionPact {
    private String id;
    private String partyAId;
    private String partyAName;
    private String partyBId;
    private String partyBName;
    private int turnsRemaining;

    public NonAggressionPact() {}

    public NonAggressionPact(String id, String partyAId, String partyAName, String partyBId, String partyBName, int turnsRemaining) {
        this.id = id;
        this.partyAId = partyAId;
        this.partyAName = partyAName;
        this.partyBId = partyBId;
        this.partyBName = partyBName;
        this.turnsRemaining = turnsRemaining;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getPartyAId() {
        return partyAId;
    }

    public void setPartyAId(String partyAId) {
        this.partyAId = partyAId;
    }

    public String getPartyAName() {
        return partyAName;
    }

    public void setPartyAName(String partyAName) {
        this.partyAName = partyAName;
    }

    public String getPartyBId() {
        return partyBId;
    }

    public void setPartyBId(String partyBId) {
        this.partyBId = partyBId;
    }

    public String getPartyBName() {
        return partyBName;
    }

    public void setPartyBName(String partyBName) {
        this.partyBName = partyBName;
    }

    public int getTurnsRemaining() {
        return turnsRemaining;
    }

    public void setTurnsRemaining(int turnsRemaining) {
        this.turnsRemaining = turnsRemaining;
    }
}
