package com.politicalsim.national;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.index.Indexed;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;

@Document(collection = "national_games")
public class NationalGame {
    @Id
    private String id;
    
    @Indexed
    private String userId;
    
    private int era;
    private String partyKey;
    private String partyName;
    private String partyShortName;
    private String partyColor;
    private int currentSeason = 1;
    private String status;
    private double playerFunds;
    private int playerCorruption = 0;

    public int getPlayerCorruption() { return playerCorruption; }
    public void setPlayerCorruption(int playerCorruption) { this.playerCorruption = playerCorruption; }
    
    private List<NationalAlliance> alliances = new ArrayList<>();
    private List<NationalCoalitionRequest> pendingRequests = new ArrayList<>();
    private List<NationalPartyState> partyStates = new ArrayList<>();

    // Finance strategy cards & anti-greed engine
    private String committedFinanceCard;
    private int megaFinanceHeat = 0;
    private List<String> visibleFinanceCardIds = new ArrayList<>();
    private String lastSeasonFinanceReport;

    // Events, Themes & Majority Government System (272 seats threshold)
    private String rulingAllianceKey = "NDA";
    private List<String> currentSeasonEventIds = new ArrayList<>();
    private Map<String, String> resolvedEventReactions = new HashMap<>(); // eventId -> optionId
    private String activeThemeKey;
    private String activeThemeAction;
    private int themePersistenceStreak = 0;
    private String lastThemeKey;
    private String targetPartyKey;
    private String themeTargetReport;

    // Media & Social Campaigns (FB/Insta, YouTubers, Podcasts, WhatsApp Networks)
    private Map<String, Double> mediaSocialSpend = new HashMap<>();
    private Map<String, Object> mediaSocialReport = new HashMap<>();
    private boolean mediaSocialCommitted = false;

    public String getTargetPartyKey() { return targetPartyKey; }
    public void setTargetPartyKey(String targetPartyKey) { this.targetPartyKey = targetPartyKey; }

    public String getThemeTargetReport() { return themeTargetReport; }
    public void setThemeTargetReport(String themeTargetReport) { this.themeTargetReport = themeTargetReport; }

    public Map<String, Double> getMediaSocialSpend() { return mediaSocialSpend; }
    public void setMediaSocialSpend(Map<String, Double> mediaSocialSpend) { this.mediaSocialSpend = mediaSocialSpend; }

    public Map<String, Object> getMediaSocialReport() { return mediaSocialReport; }
    public void setMediaSocialReport(Map<String, Object> mediaSocialReport) { this.mediaSocialReport = mediaSocialReport; }

    public boolean isMediaSocialCommitted() { return mediaSocialCommitted; }
    public void setMediaSocialCommitted(boolean mediaSocialCommitted) { this.mediaSocialCommitted = mediaSocialCommitted; }

    // State Operations & Regional Base Building (UP, Bihar, Maharashtra, etc.)
    private Map<String, NationalStateOperationState> stateOperations = new HashMap<>();
    private Map<String, Integer> nationalProjectedSeats = new HashMap<>();
    private Map<String, Integer> previousProjectedSeats = new HashMap<>();

    // National Election & No-Confidence Motion Resolution
    private Map<String, Object> nationalElectionResult;
    private boolean noConfidenceCalled = false;
    private String winnerAllianceKey;
    private boolean isPlayerVictory = false;
    private Map<String, Object> strategicHints;

    public Map<String, Object> getStrategicHints() { return strategicHints; }
    public void setStrategicHints(Map<String, Object> strategicHints) { this.strategicHints = strategicHints; }

    public Map<String, Object> getNationalElectionResult() { return nationalElectionResult; }
    public void setNationalElectionResult(Map<String, Object> nationalElectionResult) { this.nationalElectionResult = nationalElectionResult; }

    public boolean isNoConfidenceCalled() { return noConfidenceCalled; }
    public void setNoConfidenceCalled(boolean noConfidenceCalled) { this.noConfidenceCalled = noConfidenceCalled; }

    public String getWinnerAllianceKey() { return winnerAllianceKey; }
    public void setWinnerAllianceKey(String winnerAllianceKey) { this.winnerAllianceKey = winnerAllianceKey; }

    public boolean isPlayerVictory() { return isPlayerVictory; }
    public void setPlayerVictory(boolean isPlayerVictory) { this.isPlayerVictory = isPlayerVictory; }

    public Map<String, Integer> getPreviousProjectedSeats() { return previousProjectedSeats; }
    public void setPreviousProjectedSeats(Map<String, Integer> previousProjectedSeats) { this.previousProjectedSeats = previousProjectedSeats; }

    public Map<String, NationalStateOperationState> getStateOperations() { return stateOperations; }
    public void setStateOperations(Map<String, NationalStateOperationState> stateOperations) { this.stateOperations = stateOperations; }

    public Map<String, Integer> getNationalProjectedSeats() { return nationalProjectedSeats; }
    public void setNationalProjectedSeats(Map<String, Integer> nationalProjectedSeats) { this.nationalProjectedSeats = nationalProjectedSeats; }

    public String getRulingAllianceKey() { return rulingAllianceKey; }
    public void setRulingAllianceKey(String rulingAllianceKey) { this.rulingAllianceKey = rulingAllianceKey; }

    public List<String> getCurrentSeasonEventIds() { return currentSeasonEventIds; }
    public void setCurrentSeasonEventIds(List<String> currentSeasonEventIds) { this.currentSeasonEventIds = currentSeasonEventIds; }

    public Map<String, String> getResolvedEventReactions() { return resolvedEventReactions; }
    public void setResolvedEventReactions(Map<String, String> resolvedEventReactions) { this.resolvedEventReactions = resolvedEventReactions; }

    public String getActiveThemeKey() { return activeThemeKey; }
    public void setActiveThemeKey(String activeThemeKey) { this.activeThemeKey = activeThemeKey; }

    public String getActiveThemeAction() { return activeThemeAction; }
    public void setActiveThemeAction(String activeThemeAction) { this.activeThemeAction = activeThemeAction; }

    public int getThemePersistenceStreak() { return themePersistenceStreak; }
    public void setThemePersistenceStreak(int themePersistenceStreak) { this.themePersistenceStreak = themePersistenceStreak; }

    public String getLastThemeKey() { return lastThemeKey; }
    public void setLastThemeKey(String lastThemeKey) { this.lastThemeKey = lastThemeKey; }

    public String determineRulingAllianceKey() {
        if (alliances != null) {
            for (NationalAlliance a : alliances) {
                int totalSeats = 0;
                if (a.getMembers() != null && partyStates != null) {
                    for (NationalAllianceMember m : a.getMembers()) {
                        NationalPartyState ps = findPartyState(m.getPartyKey());
                        if (ps != null) totalSeats += ps.getSeats();
                    }
                }
                if (totalSeats >= 272) {
                    return a.getAllianceId();
                }
            }
        }
        return rulingAllianceKey != null ? rulingAllianceKey : "NDA";
    }

    public boolean isPlayerInPower() {
        NationalPartyState player = findPartyState(partyKey);
        if (player == null) return false;
        String curRuling = determineRulingAllianceKey();
        String playerAllianceId = player.getCurrentAllianceId();
        if (playerAllianceId == null) return false;
        return playerAllianceId.equalsIgnoreCase(curRuling);
    }

    public String getCommittedFinanceCard() { return committedFinanceCard; }
    public void setCommittedFinanceCard(String committedFinanceCard) { this.committedFinanceCard = committedFinanceCard; }

    public int getMegaFinanceHeat() { return megaFinanceHeat; }
    public void setMegaFinanceHeat(int megaFinanceHeat) { this.megaFinanceHeat = megaFinanceHeat; }

    public List<String> getVisibleFinanceCardIds() { return visibleFinanceCardIds; }
    public void setVisibleFinanceCardIds(List<String> visibleFinanceCardIds) { this.visibleFinanceCardIds = visibleFinanceCardIds; }

    public String getLastSeasonFinanceReport() { return lastSeasonFinanceReport; }
    public void setLastSeasonFinanceReport(String lastSeasonFinanceReport) { this.lastSeasonFinanceReport = lastSeasonFinanceReport; }
    
    private String createdAt = java.time.Instant.now().toString();
    private String updatedAt;

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }
    public String getUserId() { return userId; }
    public void setUserId(String userId) { this.userId = userId; }
    public int getEra() { return era; }
    public void setEra(int era) { this.era = era; }
    public String getPartyKey() { return partyKey; }
    public void setPartyKey(String partyKey) { this.partyKey = partyKey; }
    public String getPartyName() { return partyName; }
    public void setPartyName(String partyName) { this.partyName = partyName; }
    public String getPartyShortName() { return partyShortName; }
    public void setPartyShortName(String partyShortName) { this.partyShortName = partyShortName; }
    public String getPartyColor() { return partyColor; }
    public void setPartyColor(String partyColor) { this.partyColor = partyColor; }
    public int getCurrentSeason() { return currentSeason; }
    public void setCurrentSeason(int currentSeason) { this.currentSeason = currentSeason; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
    public double getPlayerFunds() { return playerFunds; }
    public void setPlayerFunds(double playerFunds) { this.playerFunds = playerFunds; }
    public List<NationalAlliance> getAlliances() { return alliances; }
    public void setAlliances(List<NationalAlliance> alliances) { this.alliances = alliances; }
    public List<NationalCoalitionRequest> getPendingRequests() { return pendingRequests; }
    public void setPendingRequests(List<NationalCoalitionRequest> pendingRequests) { this.pendingRequests = pendingRequests; }
    public List<NationalPartyState> getPartyStates() { return partyStates; }
    public void setPartyStates(List<NationalPartyState> partyStates) { this.partyStates = partyStates; }
    public String getCreatedAt() { return createdAt; }
    public void setCreatedAt(String createdAt) { this.createdAt = createdAt; }
    public String getUpdatedAt() { return updatedAt; }
    public void setUpdatedAt(String updatedAt) { this.updatedAt = updatedAt; }

    public NationalPartyState findPartyState(String partyKey) {
        if (partyStates == null || partyKey == null) return null;
        return partyStates.stream()
            .filter(p -> partyKey.equalsIgnoreCase(p.getPartyKey()))
            .findFirst().orElse(null);
    }

    public NationalAlliance findPlayerAlliance(String playerPartyKey) {
        if (alliances == null || playerPartyKey == null) return null;
        return alliances.stream()
            .filter(a -> playerPartyKey.equalsIgnoreCase(a.getLeaderPartyKey()) ||
                (a.getMembers() != null && a.getMembers().stream().anyMatch(m -> playerPartyKey.equalsIgnoreCase(m.getPartyKey()))))
            .findFirst().orElse(null);
    }
}
