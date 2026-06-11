package com.politicalsim.content;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "card_definitions")
public class CardDefinition {

    @Id
    private String id;

    @Indexed
    private String scenarioKey;

    private String cardKey;
    private String name;
    private String category;
    private List<String> roleAllowed = new ArrayList<>();
    private int cost;
    private int maxUsesPerCycle = 2;
    private Map<String, Object> target = new LinkedHashMap<>();
    private Map<String, Object> visibleEffects = new LinkedHashMap<>();
    private Map<String, Object> hiddenEffects = new LinkedHashMap<>();
    private Map<String, Object> riskRoll = new LinkedHashMap<>();
    private Map<String, Object> ideologyTags = new LinkedHashMap<>();
    private Map<String, Object> timing = new LinkedHashMap<>();
    private Map<String, Object> weights = new LinkedHashMap<>();
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

    public String getCardKey() {
        return cardKey;
    }

    public void setCardKey(String cardKey) {
        this.cardKey = cardKey;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public List<String> getRoleAllowed() {
        return roleAllowed;
    }

    public void setRoleAllowed(List<String> roleAllowed) {
        this.roleAllowed = roleAllowed;
    }

    public int getCost() {
        return cost;
    }

    public void setCost(int cost) {
        this.cost = cost;
    }

    public int getMaxUsesPerCycle() {
        return maxUsesPerCycle;
    }

    public void setMaxUsesPerCycle(int maxUsesPerCycle) {
        this.maxUsesPerCycle = maxUsesPerCycle;
    }

    public Map<String, Object> getTarget() {
        return target;
    }

    public void setTarget(Map<String, Object> target) {
        this.target = target;
    }

    public Map<String, Object> getVisibleEffects() {
        return visibleEffects;
    }

    public void setVisibleEffects(Map<String, Object> visibleEffects) {
        this.visibleEffects = visibleEffects;
    }

    public Map<String, Object> getHiddenEffects() {
        return hiddenEffects;
    }

    public void setHiddenEffects(Map<String, Object> hiddenEffects) {
        this.hiddenEffects = hiddenEffects;
    }

    public Map<String, Object> getRiskRoll() {
        return riskRoll;
    }

    public void setRiskRoll(Map<String, Object> riskRoll) {
        this.riskRoll = riskRoll;
    }

    public Map<String, Object> getIdeologyTags() {
        return ideologyTags;
    }

    public void setIdeologyTags(Map<String, Object> ideologyTags) {
        this.ideologyTags = ideologyTags;
    }

    public Map<String, Object> getTiming() {
        return timing;
    }

    public void setTiming(Map<String, Object> timing) {
        this.timing = timing;
    }

    public Map<String, Object> getWeights() {
        return weights;
    }

    public void setWeights(Map<String, Object> weights) {
        this.weights = weights;
    }

    public boolean isActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
}
