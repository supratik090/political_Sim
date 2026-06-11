package com.politicalsim.content;

import com.politicalsim.ai.AiProfile;
import com.politicalsim.party.Ideology;
import com.politicalsim.party.ControllerType;
import com.politicalsim.party.PartyRole;
import com.politicalsim.party.PartyStats;

public class ScenarioPartyDefinition {

    private String partyKey;
    private String name;
    private PartyRole startingRole;
    private ControllerType defaultControllerType = ControllerType.COMPUTER;
    private String color;
    private String symbol;
    private Ideology ideology;
    private AiProfile aiProfile;
    private PartyStats startingStats;

    public String getPartyKey() {
        return partyKey;
    }

    public void setPartyKey(String partyKey) {
        this.partyKey = partyKey;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PartyRole getStartingRole() {
        return startingRole;
    }

    public void setStartingRole(PartyRole startingRole) {
        this.startingRole = startingRole;
    }

    public ControllerType getDefaultControllerType() {
        return defaultControllerType;
    }

    public void setDefaultControllerType(ControllerType defaultControllerType) {
        this.defaultControllerType = defaultControllerType;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public Ideology getIdeology() {
        return ideology;
    }

    public void setIdeology(Ideology ideology) {
        this.ideology = ideology;
    }

    public AiProfile getAiProfile() {
        return aiProfile;
    }

    public void setAiProfile(AiProfile aiProfile) {
        this.aiProfile = aiProfile;
    }

    public PartyStats getStartingStats() {
        return startingStats;
    }

    public void setStartingStats(PartyStats startingStats) {
        this.startingStats = startingStats;
    }
}
