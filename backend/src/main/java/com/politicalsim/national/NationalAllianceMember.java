package com.politicalsim.national;

public class NationalAllianceMember {
    private String partyKey;
    private int joinedAtSeason;
    private int seats;
    private int morale;
    private NationalContract contract;

    public String getPartyKey() { return partyKey; }
    public void setPartyKey(String partyKey) { this.partyKey = partyKey; }
    public int getJoinedAtSeason() { return joinedAtSeason; }
    public void setJoinedAtSeason(int joinedAtSeason) { this.joinedAtSeason = joinedAtSeason; }
    public int getSeats() { return seats; }
    public void setSeats(int seats) { this.seats = seats; }
    public int getMorale() { return morale; }
    public void setMorale(int morale) { this.morale = morale; }
    public NationalContract getContract() { return contract; }
    public void setContract(NationalContract contract) { this.contract = contract; }
}
