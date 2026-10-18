package com.politicalsim.national;

import java.util.ArrayList;
import java.util.List;

public class NationalAlliance {
    private String allianceId;
    private String allianceName;
    private String color;
    private String leaderPartyKey;
    private int formedAtSeason;
    private double allianceFundBalance;
    private double federalAidPerSeason;
    private int totalCabinetPromised;
    private int totalStatePromised;
    private List<NationalAllianceMember> members = new ArrayList<>();
    private List<NationalActivityLogEntry> activityLog = new ArrayList<>();

    public String getAllianceId() { return allianceId; }
    public void setAllianceId(String allianceId) { this.allianceId = allianceId; }
    public String getAllianceName() { return allianceName; }
    public void setAllianceName(String allianceName) { this.allianceName = allianceName; }
    public String getColor() { return color; }
    public void setColor(String color) { this.color = color; }
    public String getLeaderPartyKey() { return leaderPartyKey; }
    public void setLeaderPartyKey(String leaderPartyKey) { this.leaderPartyKey = leaderPartyKey; }
    public int getFormedAtSeason() { return formedAtSeason; }
    public void setFormedAtSeason(int formedAtSeason) { this.formedAtSeason = formedAtSeason; }
    public double getAllianceFundBalance() { return allianceFundBalance; }
    public void setAllianceFundBalance(double allianceFundBalance) { this.allianceFundBalance = allianceFundBalance; }
    public double getFederalAidPerSeason() { return federalAidPerSeason; }
    public void setFederalAidPerSeason(double federalAidPerSeason) { this.federalAidPerSeason = federalAidPerSeason; }
    public int getTotalCabinetPromised() { return totalCabinetPromised; }
    public void setTotalCabinetPromised(int totalCabinetPromised) { this.totalCabinetPromised = totalCabinetPromised; }
    public int getTotalStatePromised() { return totalStatePromised; }
    public void setTotalStatePromised(int totalStatePromised) { this.totalStatePromised = totalStatePromised; }
    public List<NationalAllianceMember> getMembers() { return members; }
    public void setMembers(List<NationalAllianceMember> members) { this.members = members; }
    public List<NationalActivityLogEntry> getActivityLog() { return activityLog; }
    public void setActivityLog(List<NationalActivityLogEntry> activityLog) { this.activityLog = activityLog; }
}
