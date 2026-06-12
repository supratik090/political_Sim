package com.politicalsim.ai;

public enum AiStyle {
    STRENGTH_BUILDER,
    AGGRESSIVE_ATTACKER,
    LATE_STRIKER,
    AGGRESSIVE_BIDDER,
    BALANCED_STRATEGIST,
    
    // Legacy enums kept for DB deserialization backward compatibility
    CAUTIOUS_GOVERNOR,
    AGGRESSIVE_POPULIST,
    REGIONAL_KINGMAKER,
    MEDIA_MACHINE,
    ORGANIZATION_BUILDER
}
