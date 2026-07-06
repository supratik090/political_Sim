package com.politicalsim.content;

import java.util.LinkedHashMap;
import java.util.Map;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "faction_definitions")
public class FactionDefinition {

    @Id
    private String id;

    @Indexed
    private String scenarioKey;

    @Indexed
    private String factionKey; // veteran, youth, trade_union

    private String name;
    private int startingLoyalty = 70;
    private int startingInfluence = 30;

    private Map<String, Object> satisfiedEffects = new LinkedHashMap<>();
    private Map<String, Object> rebelliousEffects = new LinkedHashMap<>();

    public FactionDefinition() {
    }

    public FactionDefinition(String scenarioKey, String factionKey, String name, int startingLoyalty, int startingInfluence) {
        this.scenarioKey = scenarioKey;
        this.factionKey = factionKey;
        this.name = name;
        this.startingLoyalty = startingLoyalty;
        this.startingInfluence = startingInfluence;
    }

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

    public String getFactionKey() {
        return factionKey;
    }

    public void setFactionKey(String factionKey) {
        this.factionKey = factionKey;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getStartingLoyalty() {
        return startingLoyalty;
    }

    public void setStartingLoyalty(int startingLoyalty) {
        this.startingLoyalty = startingLoyalty;
    }

    public int getStartingInfluence() {
        return startingInfluence;
    }

    public void setStartingInfluence(int startingInfluence) {
        this.startingInfluence = startingInfluence;
    }

    public Map<String, Object> getSatisfiedEffects() {
        return satisfiedEffects;
    }

    public void setSatisfiedEffects(Map<String, Object> satisfiedEffects) {
        this.satisfiedEffects = satisfiedEffects;
    }

    public Map<String, Object> getRebelliousEffects() {
        return rebelliousEffects;
    }

    public void setRebelliousEffects(Map<String, Object> rebelliousEffects) {
        this.rebelliousEffects = rebelliousEffects;
    }
}
