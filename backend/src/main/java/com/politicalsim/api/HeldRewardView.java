package com.politicalsim.api;

import com.politicalsim.game.HeldReward;

public record HeldRewardView(
    String rewardKey,
    String name,
    String description,
    int turnsLeft,
    boolean requiresTarget,
    String allowedTargets
) {
    public static HeldRewardView from(HeldReward reward) {
        return new HeldRewardView(
            reward.getRewardKey(),
            reward.getName(),
            reward.getDescription(),
            reward.getTurnsLeft(),
            reward.isRequiresTarget(),
            reward.getAllowedTargets()
        );
    }
}
