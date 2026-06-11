package com.politicalsim.content;

import com.politicalsim.party.PartyStats;
import com.politicalsim.publicmood.PublicState;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "scenario_definitions")
public class ScenarioDefinition {

    @Id
    private String id;

    @Indexed(unique = true)
    private String scenarioKey;

    private String name;
    private String description;
    private String stateName;
    private LocalDate startDate;
    private int cycleLengthMonths = 60;
    private String governmentPartyName;
    private String oppositionPartyName;
    private String thirdPartyName;
    private PartyStats governmentStartingStats;
    private PartyStats oppositionStartingStats;
    private PartyStats thirdPartyStartingStats;
    private List<ScenarioPartyDefinition> politicalParties = new ArrayList<>();
    private PublicState publicState;
    private Map<String, Object> ruleWeights = new LinkedHashMap<>();
    private boolean active = true;

    public String getId() {
        return id;
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

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getStateName() {
        return stateName;
    }

    public void setStateName(String stateName) {
        this.stateName = stateName;
    }

    public LocalDate getStartDate() {
        return startDate;
    }

    public void setStartDate(LocalDate startDate) {
        this.startDate = startDate;
    }

    public int getCycleLengthMonths() {
        return cycleLengthMonths;
    }

    public void setCycleLengthMonths(int cycleLengthMonths) {
        this.cycleLengthMonths = cycleLengthMonths;
    }

    public String getGovernmentPartyName() {
        return governmentPartyName;
    }

    public void setGovernmentPartyName(String governmentPartyName) {
        this.governmentPartyName = governmentPartyName;
    }

    public String getOppositionPartyName() {
        return oppositionPartyName;
    }

    public void setOppositionPartyName(String oppositionPartyName) {
        this.oppositionPartyName = oppositionPartyName;
    }

    public String getThirdPartyName() {
        return thirdPartyName;
    }

    public void setThirdPartyName(String thirdPartyName) {
        this.thirdPartyName = thirdPartyName;
    }

    public PartyStats getGovernmentStartingStats() {
        return governmentStartingStats;
    }

    public void setGovernmentStartingStats(PartyStats governmentStartingStats) {
        this.governmentStartingStats = governmentStartingStats;
    }

    public PartyStats getOppositionStartingStats() {
        return oppositionStartingStats;
    }

    public void setOppositionStartingStats(PartyStats oppositionStartingStats) {
        this.oppositionStartingStats = oppositionStartingStats;
    }

    public PartyStats getThirdPartyStartingStats() {
        return thirdPartyStartingStats;
    }

    public void setThirdPartyStartingStats(PartyStats thirdPartyStartingStats) {
        this.thirdPartyStartingStats = thirdPartyStartingStats;
    }

    public List<ScenarioPartyDefinition> getPoliticalParties() {
        return politicalParties;
    }

    public void setPoliticalParties(List<ScenarioPartyDefinition> politicalParties) {
        this.politicalParties = politicalParties;
    }

    public PublicState getPublicState() {
        return publicState;
    }

    public void setPublicState(PublicState publicState) {
        this.publicState = publicState;
    }

    public Map<String, Object> getRuleWeights() {
        return ruleWeights;
    }

    public void setRuleWeights(Map<String, Object> ruleWeights) {
        this.ruleWeights = ruleWeights;
    }

    public boolean isActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
}
