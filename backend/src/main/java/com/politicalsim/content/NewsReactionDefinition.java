package com.politicalsim.content;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class NewsReactionDefinition {

    private String reactionKey;
    private String text;
    private List<String> roleAllowed = new ArrayList<>();
    private Map<String, Object> effects = new LinkedHashMap<>();
    private Map<String, Object> hiddenEffects = new LinkedHashMap<>();
    private Map<String, Object> risk = new LinkedHashMap<>();
    private int weight = 1;

    public String getReactionKey() {
        return reactionKey;
    }

    public void setReactionKey(String reactionKey) {
        this.reactionKey = reactionKey;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public List<String> getRoleAllowed() {
        return roleAllowed;
    }

    public void setRoleAllowed(List<String> roleAllowed) {
        this.roleAllowed = roleAllowed;
    }

    public Map<String, Object> getEffects() {
        return effects;
    }

    public void setEffects(Map<String, Object> effects) {
        this.effects = effects;
    }

    public Map<String, Object> getHiddenEffects() {
        return hiddenEffects;
    }

    public void setHiddenEffects(Map<String, Object> hiddenEffects) {
        this.hiddenEffects = hiddenEffects;
    }

    public Map<String, Object> getRisk() {
        return risk;
    }

    public void setRisk(Map<String, Object> risk) {
        this.risk = risk;
    }

    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }
}
