package com.politicalsim.national;

public class NationalCoalitionRequest {
    private String requestId;
    private String direction;
    private String fromPartyKey;
    private String toAllianceId;
    private double offeredJoiningBonus;
    private double requestedJoiningBonus;
    private double requestedRecurringPerSeason;
    private int requestedCabinetMinisters;
    private int requestedStateMinisters;
    private String status;
    private int createdAtSeason;

    public String getRequestId() { return requestId; }
    public void setRequestId(String requestId) { this.requestId = requestId; }
    public String getDirection() { return direction; }
    public void setDirection(String direction) { this.direction = direction; }
    public String getFromPartyKey() { return fromPartyKey; }
    public void setFromPartyKey(String fromPartyKey) { this.fromPartyKey = fromPartyKey; }
    public String getToAllianceId() { return toAllianceId; }
    public void setToAllianceId(String toAllianceId) { this.toAllianceId = toAllianceId; }
    public double getOfferedJoiningBonus() { return offeredJoiningBonus; }
    public void setOfferedJoiningBonus(double offeredJoiningBonus) { this.offeredJoiningBonus = offeredJoiningBonus; }
    public double getRequestedJoiningBonus() { return requestedJoiningBonus; }
    public void setRequestedJoiningBonus(double requestedJoiningBonus) { this.requestedJoiningBonus = requestedJoiningBonus; }
    public double getRequestedRecurringPerSeason() { return requestedRecurringPerSeason; }
    public void setRequestedRecurringPerSeason(double requestedRecurringPerSeason) { this.requestedRecurringPerSeason = requestedRecurringPerSeason; }
    public int getRequestedCabinetMinisters() { return requestedCabinetMinisters; }
    public void setRequestedCabinetMinisters(int requestedCabinetMinisters) { this.requestedCabinetMinisters = requestedCabinetMinisters; }
    public int getRequestedStateMinisters() { return requestedStateMinisters; }
    public void setRequestedStateMinisters(int requestedStateMinisters) { this.requestedStateMinisters = requestedStateMinisters; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
    public int getCreatedAtSeason() { return createdAtSeason; }
    public void setCreatedAtSeason(int createdAtSeason) { this.createdAtSeason = createdAtSeason; }
}
