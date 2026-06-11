package com.politicalsim.content;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class IssueOptionDefinition {

    private String optionKey;
    private String text;
    private int cost;
    private Map<String, Object> effects = new LinkedHashMap<>();
    private List<Map<String, Object>> delayedEffects = new ArrayList<>();
    private Map<String, Object> risk = new LinkedHashMap<>();

    public String getOptionKey() {
        return optionKey;
    }

    public void setOptionKey(String optionKey) {
        this.optionKey = optionKey;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public int getCost() {
        return cost;
    }

    public void setCost(int cost) {
        this.cost = cost;
    }

    public Map<String, Object> getEffects() {
        return effects;
    }

    public void setEffects(Map<String, Object> effects) {
        this.effects = effects;
    }

    public List<Map<String, Object>> getDelayedEffects() {
        return delayedEffects;
    }

    public void setDelayedEffects(List<Map<String, Object>> delayedEffects) {
        this.delayedEffects = delayedEffects;
    }

    public Map<String, Object> getRisk() {
        return risk;
    }

    public void setRisk(Map<String, Object> risk) {
        this.risk = risk;
    }
}
