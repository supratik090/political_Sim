package com.politicalsim.party;

import com.politicalsim.ai.AiProfile;

public class PartyState {

    private String id;
    private String name;
    private PartyRole role;
    private ControllerType controllerType = ControllerType.COMPUTER;
    private String humanPlayerLabel;
    private String color;
    private String symbol;
    private Ideology ideology;
    private AiProfile aiProfile;
    private PartyStats stats;
    private boolean active = true;
    private boolean brokeStateActive = false;
    private int assemblySeatShare = 0;
    private java.util.List<ProjectState> projects = defaultProjectsList();

    private static java.util.List<ProjectState> defaultProjectsList() {
        java.util.List<ProjectState> list = new java.util.ArrayList<>();
        for (BuildingProject p : BuildingProject.values()) {
            list.add(new ProjectState(p.name()));
        }
        return list;
    }

    public PartyState() {
    }

    public PartyState(String id, String name, PartyRole role, Ideology ideology, PartyStats stats) {
        this.id = id;
        this.name = name;
        this.role = role;
        this.ideology = ideology;
        this.stats = stats;
    }

    public PartyState(String id, String name, PartyRole role, ControllerType controllerType, String humanPlayerLabel,
            Ideology ideology, PartyStats stats) {
        this.id = id;
        this.name = name;
        this.role = role;
        this.controllerType = controllerType;
        this.humanPlayerLabel = humanPlayerLabel;
        this.ideology = ideology;
        this.stats = stats;
    }

    public PartyState(String id, String name, PartyRole role, ControllerType controllerType, String humanPlayerLabel,
            String color, String symbol, Ideology ideology, AiProfile aiProfile, PartyStats stats) {
        this.id = id;
        this.name = name;
        this.role = role;
        this.controllerType = controllerType;
        this.humanPlayerLabel = humanPlayerLabel;
        this.color = color;
        this.symbol = symbol;
        this.ideology = ideology;
        this.aiProfile = aiProfile;
        this.stats = stats;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

    public PartyStats getStats() {
        return stats;
    }

    public void setStats(PartyStats stats) {
        this.stats = stats;
    }

    public boolean isActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    public boolean isBrokeStateActive() {
        return brokeStateActive;
    }

    public void setBrokeStateActive(boolean brokeStateActive) {
        this.brokeStateActive = brokeStateActive;
    }

    public java.util.List<ProjectState> getProjects() {
        if (projects == null) {
            projects = defaultProjectsList();
        }
        return projects;
    }

    public void setProjects(java.util.List<ProjectState> projects) {
        this.projects = projects;
    }

    public int getAssemblySeatShare() {
        return assemblySeatShare;
    }

    public void setAssemblySeatShare(int assemblySeatShare) {
        this.assemblySeatShare = assemblySeatShare;
    }

    private boolean factionCrisisTriggered = false;
    private String activeFactionCrisisKey = null;
    private int factionPowerCap = 100;
    private String cappedFactionKey = null;

    public boolean isFactionCrisisTriggered() {
        return factionCrisisTriggered;
    }

    public void setFactionCrisisTriggered(boolean factionCrisisTriggered) {
        this.factionCrisisTriggered = factionCrisisTriggered;
    }

    public String getActiveFactionCrisisKey() {
        return activeFactionCrisisKey;
    }

    public void setActiveFactionCrisisKey(String activeFactionCrisisKey) {
        this.activeFactionCrisisKey = activeFactionCrisisKey;
    }

    public int getFactionPowerCap() {
        return factionPowerCap;
    }

    public void setFactionPowerCap(int factionPowerCap) {
        this.factionPowerCap = factionPowerCap;
    }

    public String getCappedFactionKey() {
        return cappedFactionKey;
    }

    public void setCappedFactionKey(String cappedFactionKey) {
        this.cappedFactionKey = cappedFactionKey;
    }

    private java.util.List<FactionState> factions = new java.util.ArrayList<>();

    public java.util.List<FactionState> getFactions() {
        if (factions == null) {
            factions = new java.util.ArrayList<>();
        }
        return factions;
    }

    public void setFactions(java.util.List<FactionState> factions) {
        this.factions = factions;
    }
}
