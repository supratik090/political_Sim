package com.politicalsim.party;

public enum BuildingProject {
    PARTY_HQ("Party Headquarters", 100, 10, 0, 10, 0, 12, 0, 0, 3, 0, false),
    IT_CELL("IT Cell (Digital Bureau)", 60, 0, 10, 0, 0, 0, 0, 0, 2, 1, false),
    CADRE_OFFICE("District Cadre Offices", 50, 5, 10, 0, 0, 0, 4, 0, 0, 1, false),
    THINK_TANK("Policy Research Think Tank", 40, 10, 0, 5, 0, 2, 0, 0, 4, 0, false),
    TRAINING_ACADEMY("Grassroots Training Academy", 45, 5, 0, 5, 0, 0, 5, 0, 0, 0, false),
    YOUTH_WING("Youth Wing Network", 35, 5, 5, 5, 0, 0, 3, 0, 0, 1, false),
    
    // New Positive Projects (Yields to Self)
    MEGA_RALLY("Mega Rally", 60, 0, 0, 10, 1, 8, 0, 0, 1, 1, false),
    PRIME_LEADER_VISIT("Prime Leader Visit", 60, 0, 10, 10, 0, 10, 0, -1, 1, 2, false),
    FOUNDATION_DAY("Foundation Day Celebration", 40, 15, 0, 0, 0, 6, 2, 0, 0, 1, false),
    PARTY_CONGRESS("Party Congress", 100, 0, 10, 10, 1, 12, 2, 0, 2, 1, false),

    // Offensive Projects (Requires Target = true, Yields/Drains target)
    DISSENT_NEWSPAPER("Dissenting Newspaper", 65, 15, 0, 0, 0, 0, 0, 0, 0, -1, true),
    MEDIA_HOUSE("Hostile Media House", 55, 0, 10, 0, 0, 0, 0, 0, -4, 0, true),
    PARTY_DISSENT("Encourage Rank Dissent", 45, 25, 0, 0, 0, 0, -3, 0, 0, 0, true),
    CORRUPTION_EXPOSE("Expose Corruption Center", 40, 0, 5, 0, 0, 0, 0, 3, 0, 0, true),
    
    // New Offensive Projects (Yields/Drains target)
    CAMPAIGN_SABOTAGE("Campaign Sabotage", 30, 0, 0, 10, 0, -5, -2, 0, -1, 0, true),
    AUDIT_HARASSMENT("Audit Harassment", 40, 0, 10, 0, 0, -8, -1, 1, 0, 0, true),
    MEDIA_SMEAR("Media Smear Campaign", 40, 0, 10, 0, 0, -6, 0, 0, -2, -1, true);

    private final String name;
    private final int costCoins;
    private final int costMorale;
    private final int costCorruption;
    private final int costMedia;
    private final int costSupport;
    private final int benefitCoins;
    private final int benefitMorale;
    private final int benefitCorruption;
    private final int benefitMedia;
    private final int benefitSupport;
    private final boolean requiresTarget;

    BuildingProject(String name, int costCoins, int costMorale, int costCorruption, int costMedia, int costSupport,
                    int benefitCoins, int benefitMorale, int benefitCorruption, int benefitMedia, int benefitSupport,
                    boolean requiresTarget) {
        this.name = name;
        this.costCoins = costCoins;
        this.costMorale = costMorale;
        this.costCorruption = costCorruption;
        this.costMedia = costMedia;
        this.costSupport = costSupport;
        this.benefitCoins = benefitCoins;
        this.benefitMorale = benefitMorale;
        this.benefitCorruption = benefitCorruption;
        this.benefitMedia = benefitMedia;
        this.benefitSupport = benefitSupport;
        this.requiresTarget = requiresTarget;
    }

    public String getName() {
        return name;
    }

    public int getCostCoins() {
        return costCoins;
    }

    public int getCostMorale() {
        return costMorale;
    }

    public int getCostCorruption() {
        return costCorruption;
    }

    public int getCostMedia() {
        return costMedia;
    }

    public int getCostSupport() {
        return costSupport;
    }

    public int getBenefitCoins() {
        return benefitCoins;
    }

    public int getBenefitMorale() {
        return benefitMorale;
    }

    public int getBenefitCorruption() {
        return benefitCorruption;
    }

    public int getBenefitMedia() {
        return benefitMedia;
    }

    public int getBenefitSupport() {
        return benefitSupport;
    }

    public boolean isRequiresTarget() {
        return requiresTarget;
    }
}

