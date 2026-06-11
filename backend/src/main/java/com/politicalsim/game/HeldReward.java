package com.politicalsim.game;

public class HeldReward {
    private String rewardKey;
    private String name;
    private String description;
    private int turnsLeft; // Starts at 5, expires when 0
    private boolean requiresTarget;
    private String allowedTargets; // "self", "opponent", "any"

    public HeldReward() {}

    public HeldReward(String rewardKey, String name, String description, int turnsLeft, boolean requiresTarget, String allowedTargets) {
        this.rewardKey = rewardKey;
        this.name = name;
        this.description = description;
        this.turnsLeft = turnsLeft;
        this.requiresTarget = requiresTarget;
        this.allowedTargets = allowedTargets;
    }

    public String getRewardKey() {
        return rewardKey;
    }

    public void setRewardKey(String rewardKey) {
        this.rewardKey = rewardKey;
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

    public int getTurnsLeft() {
        return turnsLeft;
    }

    public void setTurnsLeft(int turnsLeft) {
        this.turnsLeft = turnsLeft;
    }

    public boolean isRequiresTarget() {
        return requiresTarget;
    }

    public void setRequiresTarget(boolean requiresTarget) {
        this.requiresTarget = requiresTarget;
    }

    public String getAllowedTargets() {
        return allowedTargets;
    }

    public void setAllowedTargets(String allowedTargets) {
        this.allowedTargets = allowedTargets;
    }
}
