package com.politicalsim.game;

import com.politicalsim.party.PartyState;
import com.politicalsim.party.PartyStats;
import com.politicalsim.publicmood.PublicState;
import com.politicalsim.content.CardDefinition;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import org.springframework.data.annotation.Id;
import org.springframework.data.annotation.Transient;
import org.springframework.data.mongodb.core.mapping.Document;
import com.fasterxml.jackson.annotation.JsonProperty;

@Document(collection = "game_sessions")
public class GameSession {

    @Id
    private String id;
    private String userId;
    private String scenarioKey;
    private String scenarioName;
    private String stateName;
    private int turnNumber;
    private int monthInCycle;
    private LocalDate currentDate;
    private GameStatus status;
    private String createdAt = java.time.Instant.now().toString();
    private String playerPartyId;
    private boolean isMultiplayer;
    private String joinCode;
    private Map<String, String> humanPlayerMap = new LinkedHashMap<>();
    private java.time.LocalDateTime turnStartTime;
    private Integer turnDurationSeconds;
    private List<String> playerPartyIds = new ArrayList<>();
    private List<PartyState> parties = new ArrayList<>();
    private PartyState governmentParty;
    private PartyState oppositionParty;
    private PublicState publicState;
    private int activeHumanPlayerIndex;
    private List<RoundSubmission> currentRoundSubmissions = new ArrayList<>();
    private List<RoundSubmission> lastRoundSubmissions = new ArrayList<>();
    private List<DelayedEffect> delayedEffects = new ArrayList<>();
    private Map<String, Map<String, Integer>> cardUsageByParty = new LinkedHashMap<>();
    private Map<String, List<String>> firedHiddenRuleKeysByParty = new LinkedHashMap<>();
    private Map<String, Map<String, Integer>> lastMetricDeltas = new LinkedHashMap<>();
    private List<String> lastRoundCommentary = new ArrayList<>();
    private List<String> pendingResults = new ArrayList<>();
    private List<String> lastResults = new ArrayList<>();

    private String currentRewardKey;
    private String currentRewardName;
    private String currentRewardDescription;
    private String activeCrisisKey;
    private String activeCrisisName;
    private String activeCrisisDescription;
    private int activeCrisisTurnsLeft;
    private List<String> usedRewardKeys = new ArrayList<>();
    private Map<String, Integer> partyRoundWins = new LinkedHashMap<>();
    private Map<String, List<HeldReward>> partyHeldRewards = new LinkedHashMap<>();
    private Map<String, Integer> lastRoundBids = new LinkedHashMap<>();
    private Map<String, Map<String, Integer>> grudges = new LinkedHashMap<>();
    private Map<String, Map<String, Integer>> projectContributionsThisTurn = new LinkedHashMap<>();
    private String lastRoundBiddingMetric;
    private String lastRoundWinnerPartyId;
    @Transient
    private List<CardDefinition> gameCards = new ArrayList<>();
    @Transient
    private List<Object> gameIssues = new ArrayList<>();
    private boolean lastElectionHeld;
    private String lastElectionWinner;
    private Map<String, Integer> lastElectionVoteShares = new LinkedHashMap<>();
    private Map<String, PartyStats> turnStartStats = new LinkedHashMap<>();
    private List<CooperationOffer> cooperationOffers = new ArrayList<>();
    private List<NonAggressionPact> activePacts = new ArrayList<>();
    private List<LobbyPledge> lobbyPledges = new ArrayList<>();
    private List<LegislativeBillState> bills = new ArrayList<>();
    private Map<String, String> billVotes = new LinkedHashMap<>();
    private int lastBillProposedTurn = 0;
    private String proposedBillKeyThisTurn;
    private String activeEventKey;

    private String lastResolvedBillKey;
    private double lastBillYesVotes;
    private double lastBillNoVotes;
    private double lastBillAbstainVotes;
    private Map<String, String> lastBillPartyVotes = new LinkedHashMap<>();



    public String getId() {
        return id;
    }

    @JsonProperty("isMultiplayer")
    public boolean isMultiplayer() {
        return isMultiplayer;
    }

    @JsonProperty("isMultiplayer")
    public void setMultiplayer(boolean multiplayer) {
        isMultiplayer = multiplayer;
    }

    public String getJoinCode() {
        return joinCode;
    }

    public void setJoinCode(String joinCode) {
        this.joinCode = joinCode;
    }

    public Map<String, String> getHumanPlayerMap() {
        if (humanPlayerMap == null) {
            humanPlayerMap = new LinkedHashMap<>();
        }
        return humanPlayerMap;
    }

    public void setHumanPlayerMap(Map<String, String> humanPlayerMap) {
        this.humanPlayerMap = humanPlayerMap;
    }

    public java.time.LocalDateTime getTurnStartTime() {
        return turnStartTime;
    }

    public void setTurnStartTime(java.time.LocalDateTime turnStartTime) {
        this.turnStartTime = turnStartTime;
    }

    public Integer getTurnDurationSeconds() {
        return turnDurationSeconds;
    }

    public void setTurnDurationSeconds(Integer turnDurationSeconds) {
        this.turnDurationSeconds = turnDurationSeconds;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getScenarioKey() {
        return scenarioKey;
    }

    public void setScenarioKey(String scenarioKey) {
        this.scenarioKey = scenarioKey;
    }

    public String getScenarioName() {
        if (scenarioName == null || scenarioName.isBlank()) {
            if (scenarioKey != null) {
                String[] parts = scenarioKey.split("_");
                StringBuilder sb = new StringBuilder();
                for (String p : parts) {
                    if (p.length() > 0) {
                        sb.append(Character.toUpperCase(p.charAt(0))).append(p.substring(1)).append(" ");
                    }
                }
                return sb.toString().trim();
            }
        }
        return scenarioName;
    }

    public void setScenarioName(String scenarioName) {
        this.scenarioName = scenarioName;
    }

    public String getStateName() {
        return stateName;
    }

    public void setStateName(String stateName) {
        this.stateName = stateName;
    }

    public int getTurnNumber() {
        return turnNumber;
    }

    public void setTurnNumber(int turnNumber) {
        this.turnNumber = turnNumber;
    }

    public int getMonthInCycle() {
        return monthInCycle;
    }

    public void setMonthInCycle(int monthInCycle) {
        this.monthInCycle = monthInCycle;
    }

    public LocalDate getCurrentDate() {
        return currentDate;
    }

    public void setCurrentDate(LocalDate currentDate) {
        this.currentDate = currentDate;
    }

    public GameStatus getStatus() {
        return status;
    }

    public void setStatus(GameStatus status) {
        this.status = status;
    }

    public String getPlayerPartyId() {
        return playerPartyId;
    }

    public void setPlayerPartyId(String playerPartyId) {
        this.playerPartyId = playerPartyId;
    }

    public List<String> getPlayerPartyIds() {
        return playerPartyIds;
    }

    public void setPlayerPartyIds(List<String> playerPartyIds) {
        this.playerPartyIds = playerPartyIds;
    }

    public List<PartyState> getParties() {
        return parties;
    }

    public void setParties(List<PartyState> parties) {
        this.parties = parties;
    }

    public PartyState getGovernmentParty() {
        return governmentParty;
    }

    public void setGovernmentParty(PartyState governmentParty) {
        this.governmentParty = governmentParty;
    }

    public PartyState getOppositionParty() {
        return oppositionParty;
    }

    public void setOppositionParty(PartyState oppositionParty) {
        this.oppositionParty = oppositionParty;
    }

    public PublicState getPublicState() {
        return publicState;
    }

    public void setPublicState(PublicState publicState) {
        this.publicState = publicState;
    }

    public int getActiveHumanPlayerIndex() {
        return activeHumanPlayerIndex;
    }

    public void setActiveHumanPlayerIndex(int activeHumanPlayerIndex) {
        this.activeHumanPlayerIndex = activeHumanPlayerIndex;
    }

    public List<RoundSubmission> getCurrentRoundSubmissions() {
        return currentRoundSubmissions;
    }

    public void setCurrentRoundSubmissions(List<RoundSubmission> currentRoundSubmissions) {
        this.currentRoundSubmissions = currentRoundSubmissions;
    }

    public List<RoundSubmission> getLastRoundSubmissions() {
        return lastRoundSubmissions;
    }

    public void setLastRoundSubmissions(List<RoundSubmission> lastRoundSubmissions) {
        this.lastRoundSubmissions = lastRoundSubmissions;
    }

    public List<DelayedEffect> getDelayedEffects() {
        return delayedEffects;
    }

    public void setDelayedEffects(List<DelayedEffect> delayedEffects) {
        this.delayedEffects = delayedEffects;
    }

    public Map<String, Map<String, Integer>> getCardUsageByParty() {
        return cardUsageByParty;
    }

    public void setCardUsageByParty(Map<String, Map<String, Integer>> cardUsageByParty) {
        this.cardUsageByParty = cardUsageByParty;
    }

    public Map<String, List<String>> getFiredHiddenRuleKeysByParty() {
        return firedHiddenRuleKeysByParty;
    }

    public void setFiredHiddenRuleKeysByParty(Map<String, List<String>> firedHiddenRuleKeysByParty) {
        this.firedHiddenRuleKeysByParty = firedHiddenRuleKeysByParty;
    }

    public Map<String, Map<String, Integer>> getLastMetricDeltas() {
        return lastMetricDeltas;
    }

    public void setLastMetricDeltas(Map<String, Map<String, Integer>> lastMetricDeltas) {
        this.lastMetricDeltas = lastMetricDeltas;
    }

    public List<String> getLastRoundCommentary() {
        return lastRoundCommentary;
    }

    public void setLastRoundCommentary(List<String> lastRoundCommentary) {
        this.lastRoundCommentary = lastRoundCommentary;
    }

    public List<String> getPendingResults() {
        return pendingResults;
    }

    public void setPendingResults(List<String> pendingResults) {
        this.pendingResults = pendingResults;
    }

    public List<String> getLastResults() {
        return lastResults;
    }

    public void setLastResults(List<String> lastResults) {
        this.lastResults = lastResults;
    }

    public String getCurrentRewardKey() {
        return currentRewardKey;
    }

    public void setCurrentRewardKey(String currentRewardKey) {
        this.currentRewardKey = currentRewardKey;
    }

    public String getCurrentRewardName() {
        return currentRewardName;
    }

    public void setCurrentRewardName(String currentRewardName) {
        this.currentRewardName = currentRewardName;
    }

    public String getCurrentRewardDescription() {
        return currentRewardDescription;
    }

    public void setCurrentRewardDescription(String currentRewardDescription) {
        this.currentRewardDescription = currentRewardDescription;
    }

    public List<String> getUsedRewardKeys() {
        return usedRewardKeys;
    }

    public void setUsedRewardKeys(List<String> usedRewardKeys) {
        this.usedRewardKeys = usedRewardKeys;
    }

    public Map<String, Integer> getPartyRoundWins() {
        return partyRoundWins;
    }

    public void setPartyRoundWins(Map<String, Integer> partyRoundWins) {
        this.partyRoundWins = partyRoundWins;
    }

    public Map<String, List<HeldReward>> getPartyHeldRewards() {
        return partyHeldRewards;
    }

    public void setPartyHeldRewards(Map<String, List<HeldReward>> partyHeldRewards) {
        this.partyHeldRewards = partyHeldRewards;
    }

    public Map<String, Integer> getLastRoundBids() {
        return lastRoundBids;
    }

    public void setLastRoundBids(Map<String, Integer> lastRoundBids) {
        this.lastRoundBids = lastRoundBids;
    }

    public String getLastRoundBiddingMetric() {
        return lastRoundBiddingMetric;
    }

    public void setLastRoundBiddingMetric(String lastRoundBiddingMetric) {
        this.lastRoundBiddingMetric = lastRoundBiddingMetric;
    }

    public String getLastRoundWinnerPartyId() {
        return lastRoundWinnerPartyId;
    }

    public void setLastRoundWinnerPartyId(String lastRoundWinnerPartyId) {
        this.lastRoundWinnerPartyId = lastRoundWinnerPartyId;
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    public List<CardDefinition> getGameCards() {
        return gameCards;
    }

    public void setGameCards(List<CardDefinition> gameCards) {
        this.gameCards = gameCards;
    }

    public List<Object> getGameIssues() {
        return gameIssues;
    }

    public void setGameIssues(List<Object> gameIssues) {
        this.gameIssues = gameIssues;
    }

    public String getActiveCrisisKey() {
        return activeCrisisKey;
    }

    public void setActiveCrisisKey(String activeCrisisKey) {
        this.activeCrisisKey = activeCrisisKey;
    }

    public String getActiveCrisisName() {
        return activeCrisisName;
    }

    public void setActiveCrisisName(String activeCrisisName) {
        this.activeCrisisName = activeCrisisName;
    }

    public String getActiveCrisisDescription() {
        return activeCrisisDescription;
    }

    public void setActiveCrisisDescription(String activeCrisisDescription) {
        this.activeCrisisDescription = activeCrisisDescription;
    }

    public int getActiveCrisisTurnsLeft() {
        return activeCrisisTurnsLeft;
    }

    public void setActiveCrisisTurnsLeft(int activeCrisisTurnsLeft) {
        this.activeCrisisTurnsLeft = activeCrisisTurnsLeft;
    }

    public String getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(String createdAt) {
        this.createdAt = createdAt;
    }

    public Map<String, Map<String, Integer>> getGrudges() {
        if (grudges == null) {
            grudges = new LinkedHashMap<>();
        }
        return grudges;
    }

    public void setGrudges(Map<String, Map<String, Integer>> grudges) {
        this.grudges = grudges;
    }

    public Map<String, Map<String, Integer>> getProjectContributionsThisTurn() {
        if (projectContributionsThisTurn == null) {
            projectContributionsThisTurn = new LinkedHashMap<>();
        }
        return projectContributionsThisTurn;
    }

    public void setProjectContributionsThisTurn(Map<String, Map<String, Integer>> projectContributionsThisTurn) {
        this.projectContributionsThisTurn = projectContributionsThisTurn;
    }

    public boolean isLastElectionHeld() {
        return lastElectionHeld;
    }

    public void setLastElectionHeld(boolean lastElectionHeld) {
        this.lastElectionHeld = lastElectionHeld;
    }

    public String getLastElectionWinner() {
        return lastElectionWinner;
    }

    public void setLastElectionWinner(String lastElectionWinner) {
        this.lastElectionWinner = lastElectionWinner;
    }

    public Map<String, Integer> getLastElectionVoteShares() {
        if (lastElectionVoteShares == null) {
            lastElectionVoteShares = new java.util.LinkedHashMap<>();
        }
        return lastElectionVoteShares;
    }

    public void setLastElectionVoteShares(Map<String, Integer> lastElectionVoteShares) {
        this.lastElectionVoteShares = lastElectionVoteShares;
    }

    public Map<String, PartyStats> getTurnStartStats() {
        if (turnStartStats == null) {
            turnStartStats = new java.util.LinkedHashMap<>();
        }
        return turnStartStats;
    }

    public void setTurnStartStats(Map<String, PartyStats> turnStartStats) {
        this.turnStartStats = turnStartStats;
    }

    public List<CooperationOffer> getCooperationOffers() {
        if (cooperationOffers == null) {
            cooperationOffers = new ArrayList<>();
        }
        return cooperationOffers;
    }

    public void setCooperationOffers(List<CooperationOffer> cooperationOffers) {
        this.cooperationOffers = cooperationOffers;
    }

    public List<NonAggressionPact> getActivePacts() {
        if (activePacts == null) {
            activePacts = new ArrayList<>();
        }
        return activePacts;
    }

    public void setActivePacts(List<NonAggressionPact> activePacts) {
        this.activePacts = activePacts;
    }

    public List<LobbyPledge> getLobbyPledges() {
        if (lobbyPledges == null) {
            lobbyPledges = new ArrayList<>();
        }
        return lobbyPledges;
    }

    public void setLobbyPledges(List<LobbyPledge> lobbyPledges) {
        this.lobbyPledges = lobbyPledges;
    }

    private int tripleImpactTurn;

    public int getTripleImpactTurn() {
        return tripleImpactTurn;
    }

    public void setTripleImpactTurn(int tripleImpactTurn) {
        this.tripleImpactTurn = tripleImpactTurn;
    }

    private String secretMetric;
    private String lastRoundSecretMetric;
    private java.util.List<String> secretMetricSequence = new java.util.ArrayList<>();

    public String getSecretMetric() {
        return secretMetric;
    }

    public void setSecretMetric(String secretMetric) {
        this.secretMetric = secretMetric;
    }

    public String getLastRoundSecretMetric() {
        return lastRoundSecretMetric;
    }

    public void setLastRoundSecretMetric(String lastRoundSecretMetric) {
        this.lastRoundSecretMetric = lastRoundSecretMetric;
    }

    public java.util.List<String> getSecretMetricSequence() {
        if (secretMetricSequence == null) {
            secretMetricSequence = new java.util.ArrayList<>();
        }
        return secretMetricSequence;
    }

    public void setSecretMetricSequence(java.util.List<String> secretMetricSequence) {
        this.secretMetricSequence = secretMetricSequence;
    }

    public List<LegislativeBillState> getBills() {
        if (bills == null) {
            bills = new ArrayList<>();
        }
        return bills;
    }

    public void setBills(List<LegislativeBillState> bills) {
        this.bills = bills;
    }

    public Map<String, String> getBillVotes() {
        if (billVotes == null) {
            billVotes = new LinkedHashMap<>();
        }
        return billVotes;
    }

    public void setBillVotes(Map<String, String> billVotes) {
        this.billVotes = billVotes;
    }

    public int getLastBillProposedTurn() {
        return lastBillProposedTurn;
    }

    public void setLastBillProposedTurn(int lastBillProposedTurn) {
        this.lastBillProposedTurn = lastBillProposedTurn;
    }

    public String getProposedBillKeyThisTurn() {
        return proposedBillKeyThisTurn;
    }

    public void setProposedBillKeyThisTurn(String proposedBillKeyThisTurn) {
        this.proposedBillKeyThisTurn = proposedBillKeyThisTurn;
    }

    public String getActiveEventKey() {
        return activeEventKey;
    }

    public void setActiveEventKey(String activeEventKey) {
        this.activeEventKey = activeEventKey;
    }

    public String getLastResolvedBillKey() {
        return lastResolvedBillKey;
    }

    public void setLastResolvedBillKey(String lastResolvedBillKey) {
        this.lastResolvedBillKey = lastResolvedBillKey;
    }

    public double getLastBillYesVotes() {
        return lastBillYesVotes;
    }

    public void setLastBillYesVotes(double lastBillYesVotes) {
        this.lastBillYesVotes = lastBillYesVotes;
    }

    public double getLastBillNoVotes() {
        return lastBillNoVotes;
    }

    public void setLastBillNoVotes(double lastBillNoVotes) {
        this.lastBillNoVotes = lastBillNoVotes;
    }

    public double getLastBillAbstainVotes() {
        return lastBillAbstainVotes;
    }

    public void setLastBillAbstainVotes(double lastBillAbstainVotes) {
        this.lastBillAbstainVotes = lastBillAbstainVotes;
    }

    public Map<String, String> getLastBillPartyVotes() {
        return lastBillPartyVotes;
    }

    public void setLastBillPartyVotes(Map<String, String> lastBillPartyVotes) {
        this.lastBillPartyVotes = lastBillPartyVotes;
    }

    private Map<String, Integer> billLobbyFailCounts = new java.util.HashMap<>();

    public Map<String, Integer> getBillLobbyFailCounts() {
        if (billLobbyFailCounts == null) {
            billLobbyFailCounts = new java.util.HashMap<>();
        }
        return billLobbyFailCounts;
    }

    public void setBillLobbyFailCounts(Map<String, Integer> billLobbyFailCounts) {
        this.billLobbyFailCounts = billLobbyFailCounts;
    }
}
