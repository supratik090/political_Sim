package com.politicalsim.api;

import com.politicalsim.content.ScenarioDefinition;

public class ScenarioProgressView {
    private String scenarioKey;
    private String name;
    private String stateName;
    private String description;
    private String status; // "LOCKED", "AVAILABLE", "IN_PROGRESS", "WON"
    private ScenarioDefinition scenarioDefinition;

    public ScenarioProgressView() {
    }

    public ScenarioProgressView(String scenarioKey, String name, String stateName, String description, String status, ScenarioDefinition scenarioDefinition) {
        this.scenarioKey = scenarioKey;
        this.name = name;
        this.stateName = stateName;
        this.description = description;
        this.status = status;
        this.scenarioDefinition = scenarioDefinition;
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

    public String getStateName() {
        return stateName;
    }

    public void setStateName(String stateName) {
        this.stateName = stateName;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public ScenarioDefinition getScenarioDefinition() {
        return scenarioDefinition;
    }

    public void setScenarioDefinition(ScenarioDefinition scenarioDefinition) {
        this.scenarioDefinition = scenarioDefinition;
    }
}
