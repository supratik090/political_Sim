package com.politicalsim.party;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.InputStream;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public enum BuildingProject {
    PARTY_HQ,
    IT_CELL,
    CADRE_OFFICE,
    THINK_TANK,
    TRAINING_ACADEMY,
    YOUTH_WING,
    MEGA_RALLY,
    PRIME_LEADER_VISIT,
    FOUNDATION_DAY,
    PARTY_CONGRESS,
    DISSENT_NEWSPAPER,
    MEDIA_HOUSE,
    PARTY_DISSENT,
    CORRUPTION_EXPOSE,
    CAMPAIGN_SABOTAGE,
    AUDIT_HARASSMENT,
    MEDIA_SMEAR,
    WHISTLEBLOWER_FORUM,
    CITIZEN_OUTREACH,
    PROTEST_STRIKE,
    LEAK_INTERNAL_MEMO;

    public static class ProjectConfig {
        public String name;
        public int costCoins;
        public int costMorale;
        public int costCorruption;
        public int costMedia;
        public int costSupport;
        public int benefitCoins;
        public int benefitMorale;
        public int benefitCorruption;
        public int benefitMedia;
        public int benefitSupport;
        public boolean requiresTarget;
    }

    private static final Map<BuildingProject, ProjectConfig> configs = new ConcurrentHashMap<>();

    static {
        loadConfigsFromClasspath();
    }

    public static void initializeConfigs(Map<String, ProjectConfig> rawConfigs) {
        configs.clear();
        for (Map.Entry<String, ProjectConfig> entry : rawConfigs.entrySet()) {
            try {
                BuildingProject project = BuildingProject.valueOf(entry.getKey());
                configs.put(project, entry.getValue());
            } catch (IllegalArgumentException e) {
                // Ignore key mismatch
            }
        }
    }

    private static void loadConfigsFromClasspath() {
        try {
            ObjectMapper mapper = new ObjectMapper();
            InputStream stream = BuildingProject.class.getResourceAsStream("/config/building_projects.json");
            if (stream != null) {
                Map<String, ProjectConfig> raw = mapper.readValue(stream, new TypeReference<Map<String, ProjectConfig>>() {});
                initializeConfigs(raw);
            } else {
                System.err.println("⚠️ building_projects.json not found on classpath!");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.err.println("❌ Failed to parse building_projects.json: " + e.getMessage());
        }
    }

    public String getName() {
        ProjectConfig c = configs.get(this);
        return c != null ? c.name : this.name();
    }

    public int getCostCoins() {
        ProjectConfig c = configs.get(this);
        return c != null ? c.costCoins : 0;
    }

    public int getCostMorale() {
        ProjectConfig c = configs.get(this);
        return c != null ? c.costMorale : 0;
    }

    public int getCostCorruption() {
        ProjectConfig c = configs.get(this);
        return c != null ? c.costCorruption : 0;
    }

    public int getCostMedia() {
        ProjectConfig c = configs.get(this);
        return c != null ? c.costMedia : 0;
    }

    public int getCostSupport() {
        ProjectConfig c = configs.get(this);
        return c != null ? c.costSupport : 0;
    }

    public int getBenefitCoins() {
        ProjectConfig c = configs.get(this);
        return c != null ? c.benefitCoins : 0;
    }

    public int getBenefitMorale() {
        ProjectConfig c = configs.get(this);
        return c != null ? c.benefitMorale : 0;
    }

    public int getBenefitCorruption() {
        ProjectConfig c = configs.get(this);
        return c != null ? c.benefitCorruption : 0;
    }

    public int getBenefitMedia() {
        ProjectConfig c = configs.get(this);
        return c != null ? c.benefitMedia : 0;
    }

    public int getBenefitSupport() {
        ProjectConfig c = configs.get(this);
        return c != null ? c.benefitSupport : 0;
    }

    public boolean isRequiresTarget() {
        ProjectConfig c = configs.get(this);
        return c != null ? c.requiresTarget : false;
    }

    public static Map<BuildingProject, ProjectConfig> getConfigs() {
        return configs;
    }
}
