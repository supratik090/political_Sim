package com.politicalsim.national;

public class NationalPartyState {
    private String partyKey;
    private String partyName;
    private String shortName;
    private String color;
    private String ideology;
    private int seats;
    private int morale;
    private double funds;
    private double startingFunds;
    private int workers;
    private int volunteers;
    private int donors;
    private String currentAllianceId;
    private boolean isPlayerParty;
    private boolean isPreSeededAllianceLeader;
    private String preSeededAllianceKey;
    private int corruption = 0;
    private int deltaSeats = 0;
    private int deltaMorale = 0;
    private double deltaFunds = 0.0;
    private int deltaCorruption = 0;
    private int deltaWorkers = 0;
    private int deltaVolunteers = 0;
    private int deltaDonors = 0;
    private int projectedSeats = 0;
    private boolean gainingMomentum = false;
    private double donationsPerTurn = 0.0;

    public int getProjectedSeats() { return projectedSeats; }
    public void setProjectedSeats(int projectedSeats) { this.projectedSeats = projectedSeats; }
    public boolean isGainingMomentum() { return gainingMomentum; }
    public void setGainingMomentum(boolean gainingMomentum) { this.gainingMomentum = gainingMomentum; }
    public double getDonationsPerTurn() { return donationsPerTurn; }
    public void setDonationsPerTurn(double donationsPerTurn) { this.donationsPerTurn = donationsPerTurn; }

    public int getDeltaSeats() { return deltaSeats; }
    public void setDeltaSeats(int deltaSeats) { this.deltaSeats = deltaSeats; }
    public int getDeltaMorale() { return deltaMorale; }
    public void setDeltaMorale(int deltaMorale) { this.deltaMorale = deltaMorale; }
    public double getDeltaFunds() { return deltaFunds; }
    public void setDeltaFunds(double deltaFunds) { this.deltaFunds = deltaFunds; }
    public int getDeltaCorruption() { return deltaCorruption; }
    public void setDeltaCorruption(int deltaCorruption) { this.deltaCorruption = deltaCorruption; }
    public int getDeltaWorkers() { return deltaWorkers; }
    public void setDeltaWorkers(int deltaWorkers) { this.deltaWorkers = deltaWorkers; }
    public int getDeltaVolunteers() { return deltaVolunteers; }
    public void setDeltaVolunteers(int deltaVolunteers) { this.deltaVolunteers = deltaVolunteers; }
    public int getDeltaDonors() { return deltaDonors; }
    public void setDeltaDonors(int deltaDonors) { this.deltaDonors = deltaDonors; }
    public double getStartingFunds() { return startingFunds; }
    public void setStartingFunds(double startingFunds) { this.startingFunds = startingFunds; }

    public int getCorruption() { return corruption; }
    public void setCorruption(int corruption) { this.corruption = corruption; }

    public String getPartyKey() { return partyKey; }
    public void setPartyKey(String partyKey) { this.partyKey = partyKey; }
    public String getPartyName() { return partyName; }
    public void setPartyName(String partyName) { this.partyName = partyName; }
    public String getShortName() { return shortName; }
    public void setShortName(String shortName) { this.shortName = shortName; }
    public String getColor() { return color; }
    public void setColor(String color) { this.color = color; }
    public String getIdeology() { return ideology; }
    public void setIdeology(String ideology) { this.ideology = ideology; }
    public int getSeats() { return seats; }
    public void setSeats(int seats) { this.seats = seats; }
    public int getMorale() { return morale; }
    public void setMorale(int morale) { this.morale = morale; }
    public double getFunds() { return funds; }
    public void setFunds(double funds) { this.funds = funds; }
    public int getWorkers() { return workers; }
    public void setWorkers(int workers) { this.workers = workers; }
    public int getVolunteers() { return volunteers; }
    public void setVolunteers(int volunteers) { this.volunteers = volunteers; }
    public int getDonors() { return donors; }
    public void setDonors(int donors) { this.donors = donors; }
    public String getCurrentAllianceId() { return currentAllianceId; }
    public void setCurrentAllianceId(String currentAllianceId) { this.currentAllianceId = currentAllianceId; }
    public boolean isPlayerParty() { return isPlayerParty; }
    public void setPlayerParty(boolean isPlayerParty) { this.isPlayerParty = isPlayerParty; }
    public boolean isPreSeededAllianceLeader() { return isPreSeededAllianceLeader; }
    public void setPreSeededAllianceLeader(boolean isPreSeededAllianceLeader) { this.isPreSeededAllianceLeader = isPreSeededAllianceLeader; }
    public String getPreSeededAllianceKey() { return preSeededAllianceKey; }
    public void setPreSeededAllianceKey(String preSeededAllianceKey) { this.preSeededAllianceKey = preSeededAllianceKey; }
}
