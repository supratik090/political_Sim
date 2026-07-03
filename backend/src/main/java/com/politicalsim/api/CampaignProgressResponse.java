package com.politicalsim.api;

import java.util.List;

public class CampaignProgressResponse {
    private int currentEra;
    private List<ScenarioProgressView> scenarios;

    public CampaignProgressResponse() {
    }

    public CampaignProgressResponse(int currentEra, List<ScenarioProgressView> scenarios) {
        this.currentEra = currentEra;
        this.scenarios = scenarios;
    }

    public int getCurrentEra() {
        return currentEra;
    }

    public void setCurrentEra(int currentEra) {
        this.currentEra = currentEra;
    }

    public List<ScenarioProgressView> getScenarios() {
        return scenarios;
    }

}
