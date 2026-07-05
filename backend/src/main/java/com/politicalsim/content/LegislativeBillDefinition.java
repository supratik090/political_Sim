package com.politicalsim.content;

import java.util.LinkedHashMap;
import java.util.Map;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "legislative_bill_definitions")
public class LegislativeBillDefinition {
    @Id
    private String id;

    @Indexed
    private String scenarioKey;

    @Indexed
    private String billKey;

    private String name;
    private String description;
    private String proposingRole; // "GOVERNMENT" or "OPPOSITION"
    private int pointsPassed;
    private int pointsFailed;
    private Map<String, Object> effectsPassed = new LinkedHashMap<>();
    private Map<String, Object> effectsFailed = new LinkedHashMap<>();
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

    public String getBillKey() {
        return billKey;
    }

    public void setBillKey(String billKey) {
        this.billKey = billKey;
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

    public String getProposingRole() {
        return proposingRole;
    }

    public void setProposingRole(String proposingRole) {
        this.proposingRole = proposingRole;
    }

    public int getPointsPassed() {
        return pointsPassed;
    }

    public void setPointsPassed(int pointsPassed) {
        this.pointsPassed = pointsPassed;
    }

    public int getPointsFailed() {
        return pointsFailed;
    }

    public void setPointsFailed(int pointsFailed) {
        this.pointsFailed = pointsFailed;
    }

    public Map<String, Object> getEffectsPassed() {
        return effectsPassed;
    }

    public void setEffectsPassed(Map<String, Object> effectsPassed) {
        this.effectsPassed = effectsPassed;
    }

    public Map<String, Object> getEffectsFailed() {
        return effectsFailed;
    }

    public void setEffectsFailed(Map<String, Object> effectsFailed) {
        this.effectsFailed = effectsFailed;
    }

    public boolean isActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
}
