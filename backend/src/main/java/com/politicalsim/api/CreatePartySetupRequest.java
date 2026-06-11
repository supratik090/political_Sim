package com.politicalsim.api;

import com.politicalsim.ai.AiProfile;
import com.politicalsim.party.ControllerType;
import com.politicalsim.party.Ideology;
import com.politicalsim.party.PartyRole;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

public class CreatePartySetupRequest {

    @NotBlank
    private String partyName;

    @NotNull
    private PartyRole role;

    @NotNull
    private ControllerType controllerType;

    private String humanPlayerLabel;
    private String partyKey;
    private String color;
    private String symbol;

    @NotNull
    private Ideology ideology;
    private AiProfile aiProfile;
    private com.politicalsim.party.PartyStats startingStats;

    public String getPartyName() {
        return partyName;
    }

    public void setPartyName(String partyName) {
        this.partyName = partyName;
    }

    public PartyRole getRole() {
        return role;
    }

    public void setRole(PartyRole role) {
        this.role = role;
    }

    public ControllerType getControllerType() {
        return controllerType;
    }

    public void setControllerType(ControllerType controllerType) {
        this.controllerType = controllerType;
    }

    public String getHumanPlayerLabel() {
        return humanPlayerLabel;
    }

    public void setHumanPlayerLabel(String humanPlayerLabel) {
        this.humanPlayerLabel = humanPlayerLabel;
    }

    public String getPartyKey() {
        return partyKey;
    }

    public void setPartyKey(String partyKey) {
        this.partyKey = partyKey;
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

    public com.politicalsim.party.PartyStats getStartingStats() {
        return startingStats;
    }

    public void setStartingStats(com.politicalsim.party.PartyStats startingStats) {
        this.startingStats = startingStats;
    }
}
