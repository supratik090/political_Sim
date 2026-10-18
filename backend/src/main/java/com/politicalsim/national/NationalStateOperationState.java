package com.politicalsim.national;

import java.util.HashMap;
import java.util.Map;

public class NationalStateOperationState {
    private String stateCode;
    private String stateName;
    private String scenarioKey;
    private boolean isActive = true;
    private String activatedVia = "ALLIANCE";
    private String rulingParty;
    private String oppositionParty;
    private int totalLokSabhaSeats;
    private int totalAssemblySeats;
    private int electionTurn;
    private String electionMonth;
    private int turnsToElection;
    private String electionPhase = "NORMAL"; // NORMAL, PRE_ELECTION, CAMPAIGN, FINAL_SPRINT, ELECTION_DAY

    private double stateFunds = 5.0; // in Cr
    private int stateWorkers = 25000;
    private int stateVolunteers = 10000;
    private int stateDonors = 500;
    private double netIncomePerTurn = 0.5; // in Cr per turn

    private Map<String, Double> voteSplits = new HashMap<>();
    private Map<String, Integer> projectedLokSabhaSeats = new HashMap<>();
    private Map<String, Double> baselineVoteSplits = new HashMap<>();
    private Map<String, Integer> baselineLokSabhaSeats = new HashMap<>();

    private int momentumTurns = 0;
    private double momentumMultiplier = 1.0;
    private String activeIssueId;
    private String activeIssueAction;
    private int issueStreak = 0;

    private boolean electionCompleted = false;
    private Map<String, Object> lastElectionResult;
    private Map<String, String> resolvedNewsReactions = new HashMap<>();
    private Map<String, Object> lastNewsResolution = new HashMap<>();
    private boolean skippedThisTurn = false;
    private boolean doneThisTurn = false;

    // State Infrastructure & Regional Operations
    private Map<String, Integer> buildings = new HashMap<>();
    private Map<String, Integer> wings = new HashMap<>();
    private Map<String, RegionalOperationState> regions = new HashMap<>();
    private java.util.List<NationalActivityLogEntry> activityLog = new java.util.ArrayList<>();

    public void updateElectionPhase(int currentTurn) {
        this.turnsToElection = Math.max(0, this.electionTurn - currentTurn);
        if (this.turnsToElection == 0 && !this.electionCompleted) {
            this.electionPhase = "ELECTION_DAY";
        } else if (this.turnsToElection <= 3) {
            this.electionPhase = "FINAL_SPRINT";
        } else if (this.turnsToElection <= 6) {
            this.electionPhase = "CAMPAIGN";
        } else if (this.turnsToElection <= 12) {
            this.electionPhase = "PRE_ELECTION";
        } else {
            this.electionPhase = "NORMAL";
        }
    }

    public void normalizeVoteSplits() {
        if (voteSplits == null || voteSplits.isEmpty()) return;
        double sum = 0.0;
        for (Double v : voteSplits.values()) {
            if (v != null) sum += v;
        }
        if (sum > 0) {
            for (Map.Entry<String, Double> entry : voteSplits.entrySet()) {
                double normalized = Math.round((entry.getValue() / sum) * 1000.0) / 10.0;
                voteSplits.put(entry.getKey(), normalized);
            }
        }
    }

    // Getters and Setters
    public String getStateCode() { return stateCode; }
    public void setStateCode(String stateCode) { this.stateCode = stateCode; }

    public String getStateName() { return stateName; }
    public void setStateName(String stateName) { this.stateName = stateName; }

    public String getScenarioKey() { return scenarioKey; }
    public void setScenarioKey(String scenarioKey) { this.scenarioKey = scenarioKey; }

    public boolean isActive() { return isActive; }
    public void setActive(boolean active) { isActive = active; }

    public String getActivatedVia() { return activatedVia; }
    public void setActivatedVia(String activatedVia) { this.activatedVia = activatedVia; }

    public String getRulingParty() { return rulingParty; }
    public void setRulingParty(String rulingParty) { this.rulingParty = rulingParty; }

    public String getOppositionParty() { return oppositionParty; }
    public void setOppositionParty(String oppositionParty) { this.oppositionParty = oppositionParty; }

    public int getTotalLokSabhaSeats() { return totalLokSabhaSeats; }
    public void setTotalLokSabhaSeats(int totalLokSabhaSeats) { this.totalLokSabhaSeats = totalLokSabhaSeats; }

    public int getTotalAssemblySeats() { return totalAssemblySeats; }
    public void setTotalAssemblySeats(int totalAssemblySeats) { this.totalAssemblySeats = totalAssemblySeats; }

    public int getElectionTurn() { return electionTurn; }
    public void setElectionTurn(int electionTurn) { this.electionTurn = electionTurn; }

    public String getElectionMonth() { return electionMonth; }
    public void setElectionMonth(String electionMonth) { this.electionMonth = electionMonth; }

    public int getTurnsToElection() { return turnsToElection; }
    public void setTurnsToElection(int turnsToElection) { this.turnsToElection = turnsToElection; }

    public String getElectionPhase() { return electionPhase; }
    public void setElectionPhase(String electionPhase) { this.electionPhase = electionPhase; }

    public double getStateFunds() { return stateFunds; }
    public void setStateFunds(double stateFunds) { this.stateFunds = stateFunds; }

    public int getStateWorkers() { return stateWorkers; }
    public void setStateWorkers(int stateWorkers) { this.stateWorkers = stateWorkers; }

    public int getStateVolunteers() { return stateVolunteers; }
    public void setStateVolunteers(int stateVolunteers) { this.stateVolunteers = stateVolunteers; }

    public int getStateDonors() { return stateDonors; }
    public void setStateDonors(int stateDonors) { this.stateDonors = stateDonors; }

    public Map<String, Double> getVoteSplits() { return voteSplits; }
    public void setVoteSplits(Map<String, Double> voteSplits) { this.voteSplits = voteSplits; }

    public Map<String, Integer> getProjectedLokSabhaSeats() { return projectedLokSabhaSeats; }
    public void setProjectedLokSabhaSeats(Map<String, Integer> projectedLokSabhaSeats) { this.projectedLokSabhaSeats = projectedLokSabhaSeats; }

    public Map<String, Double> getBaselineVoteSplits() { return baselineVoteSplits; }
    public void setBaselineVoteSplits(Map<String, Double> baselineVoteSplits) { this.baselineVoteSplits = baselineVoteSplits; }

    public Map<String, Integer> getBaselineLokSabhaSeats() { return baselineLokSabhaSeats; }
    public void setBaselineLokSabhaSeats(Map<String, Integer> baselineLokSabhaSeats) { this.baselineLokSabhaSeats = baselineLokSabhaSeats; }

    public int getMomentumTurns() { return momentumTurns; }
    public void setMomentumTurns(int momentumTurns) { this.momentumTurns = momentumTurns; }

    public double getMomentumMultiplier() { return momentumMultiplier; }
    public void setMomentumMultiplier(double momentumMultiplier) { this.momentumMultiplier = momentumMultiplier; }

    public String getActiveIssueId() { return activeIssueId; }
    public void setActiveIssueId(String activeIssueId) { this.activeIssueId = activeIssueId; }

    public String getActiveIssueAction() { return activeIssueAction; }
    public void setActiveIssueAction(String activeIssueAction) { this.activeIssueAction = activeIssueAction; }

    public int getIssueStreak() { return issueStreak; }
    public void setIssueStreak(int issueStreak) { this.issueStreak = issueStreak; }

    public boolean isElectionCompleted() { return electionCompleted; }
    public void setElectionCompleted(boolean electionCompleted) { this.electionCompleted = electionCompleted; }

    public Map<String, Object> getLastElectionResult() { return lastElectionResult; }
    public void setLastElectionResult(Map<String, Object> lastElectionResult) { this.lastElectionResult = lastElectionResult; }

    public Map<String, String> getResolvedNewsReactions() { return resolvedNewsReactions; }
    public void setResolvedNewsReactions(Map<String, String> resolvedNewsReactions) { this.resolvedNewsReactions = resolvedNewsReactions; }

    public boolean isSkippedThisTurn() { return skippedThisTurn; }
    public void setSkippedThisTurn(boolean skippedThisTurn) { this.skippedThisTurn = skippedThisTurn; }

    public boolean isDoneThisTurn() { return doneThisTurn; }
    public void setDoneThisTurn(boolean doneThisTurn) { this.doneThisTurn = doneThisTurn; }

    public Map<String, Object> getLastNewsResolution() { return lastNewsResolution; }
    public void setLastNewsResolution(Map<String, Object> lastNewsResolution) { this.lastNewsResolution = lastNewsResolution; }

    public Map<String, Integer> getBuildings() { return buildings; }
    public void setBuildings(Map<String, Integer> buildings) { this.buildings = buildings; }

    public Map<String, Integer> getWings() { return wings; }
    public void setWings(Map<String, Integer> wings) { this.wings = wings; }

    public Map<String, RegionalOperationState> getRegions() { return regions; }
    public void setRegions(Map<String, RegionalOperationState> regions) { this.regions = regions; }

    public double getNetIncomePerTurn() { return netIncomePerTurn; }
    public void setNetIncomePerTurn(double netIncomePerTurn) { this.netIncomePerTurn = netIncomePerTurn; }

    public java.util.List<NationalActivityLogEntry> getActivityLog() { return activityLog; }
    public void setActivityLog(java.util.List<NationalActivityLogEntry> activityLog) { this.activityLog = activityLog; }

    public void addActivityLog(int season, String event, String detail) {
        if (this.activityLog == null) {
            this.activityLog = new java.util.ArrayList<>();
        }
        NationalActivityLogEntry entry = new NationalActivityLogEntry();
        entry.setSeason(season);
        entry.setEvent(event);
        entry.setDetail(detail);
        entry.setTimestamp(java.time.Instant.now().toString());
        this.activityLog.add(0, entry); // most recent first
    }
}
