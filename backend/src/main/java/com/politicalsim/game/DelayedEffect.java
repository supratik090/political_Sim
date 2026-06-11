package com.politicalsim.game;

import java.util.LinkedHashMap;
import java.util.Map;

public class DelayedEffect {

    private String id;
    private int dueTurnNumber;
    private String sourceType;
    private String sourceKey;
    private String sourceName;
    private String targetPartyId;
    private String targetPartyName;
    private int chance = 100;
    private Map<String, Object> effects = new LinkedHashMap<>();
    private String commentary;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public int getDueTurnNumber() {
        return dueTurnNumber;
    }

    public void setDueTurnNumber(int dueTurnNumber) {
        this.dueTurnNumber = dueTurnNumber;
    }

    public String getSourceType() {
        return sourceType;
    }

    public void setSourceType(String sourceType) {
        this.sourceType = sourceType;
    }

    public String getSourceKey() {
        return sourceKey;
    }

    public void setSourceKey(String sourceKey) {
        this.sourceKey = sourceKey;
    }

    public String getSourceName() {
        return sourceName;
    }

    public void setSourceName(String sourceName) {
        this.sourceName = sourceName;
    }

    public String getTargetPartyId() {
        return targetPartyId;
    }

    public void setTargetPartyId(String targetPartyId) {
        this.targetPartyId = targetPartyId;
    }

    public String getTargetPartyName() {
        return targetPartyName;
    }

    public void setTargetPartyName(String targetPartyName) {
        this.targetPartyName = targetPartyName;
    }

    public int getChance() {
        return chance;
    }

    public void setChance(int chance) {
        this.chance = chance;
    }

    public Map<String, Object> getEffects() {
        return effects;
    }

    public void setEffects(Map<String, Object> effects) {
        this.effects = effects;
    }

    public String getCommentary() {
        return commentary;
    }

    public void setCommentary(String commentary) {
        this.commentary = commentary;
    }
}
