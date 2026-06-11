package com.politicalsim.game;

public record RewardDefinition(
    String key,
    String name,
    String description,
    boolean requiresTarget,
    String allowedTargets, // "self", "opponent", "any"
    int coinsEffect,
    int moraleEffect,
    int corruptionEffect,
    int mediaEffect,
    int publicSupportEffect
) {}
