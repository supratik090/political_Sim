package com.politicalsim.national;

public class NationalContract {
    private double joiningBonus;
    private double recurringPerSeason;
    private int cabinetMinistersPromised;
    private int stateMinistersPromised;
    private int durationSeasons;
    private boolean isBroken;
    private String breakReason;

    public double getJoiningBonus() { return joiningBonus; }
    public void setJoiningBonus(double joiningBonus) { this.joiningBonus = joiningBonus; }
    public double getRecurringPerSeason() { return recurringPerSeason; }
    public void setRecurringPerSeason(double recurringPerSeason) { this.recurringPerSeason = recurringPerSeason; }
    public int getCabinetMinistersPromised() { return cabinetMinistersPromised; }
    public void setCabinetMinistersPromised(int cabinetMinistersPromised) { this.cabinetMinistersPromised = cabinetMinistersPromised; }
    public int getStateMinistersPromised() { return stateMinistersPromised; }
    public void setStateMinistersPromised(int stateMinistersPromised) { this.stateMinistersPromised = stateMinistersPromised; }
    public int getDurationSeasons() { return durationSeasons; }
    public void setDurationSeasons(int durationSeasons) { this.durationSeasons = durationSeasons; }
    public boolean isBroken() { return isBroken; }
    public void setBroken(boolean isBroken) { this.isBroken = isBroken; }
    public String getBreakReason() { return breakReason; }
    public void setBreakReason(String breakReason) { this.breakReason = breakReason; }
}
