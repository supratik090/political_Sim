package com.politicalsim.party;

public class ProjectState {
    private String id = java.util.UUID.randomUUID().toString();
    private String projectKey;
    private int progressPercent;
    private String targetPartyId;
    private String targetPartyName;
    private boolean justCompleted;

    // Static metadata icons for all project keys
    private static final java.util.Map<String, String> PROJECT_ICONS = java.util.Map.ofEntries(
        java.util.Map.entry("PARTY_HQ",           "🏢"),
        java.util.Map.entry("IT_CELL",            "💻"),
        java.util.Map.entry("CADRE_OFFICE",       "🏘️"),
        java.util.Map.entry("THINK_TANK",         "🧠"),
        java.util.Map.entry("TRAINING_ACADEMY",   "🏫"),
        java.util.Map.entry("YOUTH_WING",         "✊"),
        java.util.Map.entry("MEGA_RALLY",         "📢"),
        java.util.Map.entry("PRIME_LEADER_VISIT", "⭐"),
        java.util.Map.entry("FOUNDATION_DAY",     "🎉"),
        java.util.Map.entry("PARTY_CONGRESS",     "🤝"),
        java.util.Map.entry("DISSENT_NEWSPAPER",  "📰"),
        java.util.Map.entry("MEDIA_HOUSE",        "📺"),
        java.util.Map.entry("PARTY_DISSENT",      "📣"),
        java.util.Map.entry("CORRUPTION_EXPOSE",  "🔍"),
        java.util.Map.entry("CAMPAIGN_SABOTAGE",  "💣"),
        java.util.Map.entry("AUDIT_HARASSMENT",   "💼"),
        java.util.Map.entry("MEDIA_SMEAR",        "📻"),
        java.util.Map.entry("WHISTLEBLOWER_FORUM","🔍"),
        java.util.Map.entry("CITIZEN_OUTREACH",   "🤝"),
        java.util.Map.entry("PROTEST_STRIKE",     "✊"),
        java.util.Map.entry("LEAK_INTERNAL_MEMO", "📄")
    );

    /** Build a human-readable yield description from the config benefits. */
    private static String buildYieldDesc(BuildingProject.ProjectConfig c, boolean requiresTarget) {
        if (c == null) return "Completed project.";
        java.util.List<String> parts = new java.util.ArrayList<>();
        if (c.benefitCoins   != 0) parts.add((c.benefitCoins   > 0 ? "+" : "") + c.benefitCoins   + " Coins");
        if (c.benefitMorale  != 0) parts.add((c.benefitMorale  > 0 ? "+" : "") + c.benefitMorale  + " Morale");
        if (c.benefitMedia   != 0) parts.add((c.benefitMedia   > 0 ? "+" : "") + c.benefitMedia   + " Media Image");
        if (c.benefitCorruption != 0) parts.add((c.benefitCorruption > 0 ? "+" : "") + c.benefitCorruption + " Corruption");
        if (c.benefitSupport != 0) parts.add((c.benefitSupport > 0 ? "+" : "") + c.benefitSupport + "% Support");
        if (parts.isEmpty()) return "No direct yield.";
        String suffix = requiresTarget ? " to Target per turn" : " per turn";
        return "Yields: " + String.join(", ", parts) + suffix;
    }

    public ProjectState() {
        this.id = java.util.UUID.randomUUID().toString();
    }

    public ProjectState(String projectKey) {
        this.id = java.util.UUID.randomUUID().toString();
        this.projectKey = projectKey;
        this.progressPercent = 0;
        this.targetPartyId = null;
        this.targetPartyName = null;
    }

    public ProjectState(String id, String projectKey, int progressPercent, String targetPartyId, String targetPartyName) {
        this.id = id != null ? id : java.util.UUID.randomUUID().toString();
        this.projectKey = projectKey;
        this.progressPercent = progressPercent;
        this.targetPartyId = targetPartyId;
        this.targetPartyName = targetPartyName;
    }

    // ── Computed metadata ─────────────────────────────────────────────────────

    /** Human-readable project name from building_projects.json config. */
    public String getName() {
        if (projectKey == null) return "Unknown Project";
        try {
            BuildingProject bp = BuildingProject.valueOf(projectKey);
            return bp.getName();
        } catch (IllegalArgumentException e) {
            return projectKey;
        }
    }

    /** Emoji icon for the project. */
    public String getIcon() {
        return PROJECT_ICONS.getOrDefault(projectKey, "🏗️");
    }

    /** Human-readable yield description derived from config benefit values. */
    public String getYieldDesc() {
        if (projectKey == null) return "Completed project.";
        try {
            BuildingProject bp = BuildingProject.valueOf(projectKey);
            BuildingProject.ProjectConfig c = BuildingProject.getConfigs().get(bp);
            return buildYieldDesc(c, bp.isRequiresTarget());
        } catch (IllegalArgumentException e) {
            return "Completed project.";
        }
    }

    // ── Standard getters / setters ────────────────────────────────────────────

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getProjectKey() {
        return projectKey;
    }

    public void setProjectKey(String projectKey) {
        this.projectKey = projectKey;
    }

    public int getProgressPercent() {
        return progressPercent;
    }

    public void setProgressPercent(int progressPercent) {
        int oldVal = this.progressPercent;
        this.progressPercent = Math.min(100, Math.max(0, progressPercent));
        if (oldVal < 100 && this.progressPercent == 100) {
            this.justCompleted = true;
        }
    }

    public boolean isJustCompleted() {
        return justCompleted;
    }

    public void setJustCompleted(boolean justCompleted) {
        this.justCompleted = justCompleted;
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

    private int completionTurn;
    private String managingFactionKey = "None";
    private int frozenTurnsRemaining = 0;

    public int getCompletionTurn() {
        return completionTurn;
    }

    public void setCompletionTurn(int completionTurn) {
        this.completionTurn = completionTurn;
    }

    public String getManagingFactionKey() {
        return managingFactionKey;
    }

    public void setManagingFactionKey(String managingFactionKey) {
        this.managingFactionKey = managingFactionKey != null ? managingFactionKey : "None";
    }

    public int getFrozenTurnsRemaining() {
        return frozenTurnsRemaining;
    }

    public void setFrozenTurnsRemaining(int frozenTurnsRemaining) {
        this.frozenTurnsRemaining = frozenTurnsRemaining;
    }
}

