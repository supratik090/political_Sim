package com.politicalsim.api;

import java.util.List;
import java.util.Map;

/**
 * Request body for locking party management allocations.
 * Sent when the player clicks "Lock Allocations" in Action 3.
 */
public class PartyManagementLockRequest {

    /** How many patronage point cards were allocated to factions this turn */
    private int patronageUsed;

    /**
     * Map of { postKey -> factionKey } for posts allocated this turn.
     * e.g. { "SECRETARY": "veteran", "FUND_MANAGER": "youth" }
     */
    private Map<String, String> postAssignments;

    /**
     * Full faction snapshot: key, loyalty, influence, post, patronage, active.
     * Used to update FactionState in the party.
     */
    private List<Map<String, Object>> factions;

    /**
     * Project assignments: { projectKey -> factionKey }
     */
    private Map<String, String> projects;

    public int getPatronageUsed() { return patronageUsed; }
    public void setPatronageUsed(int patronageUsed) { this.patronageUsed = patronageUsed; }

    public Map<String, String> getPostAssignments() { return postAssignments; }
    public void setPostAssignments(Map<String, String> postAssignments) { this.postAssignments = postAssignments; }

    public List<Map<String, Object>> getFactions() { return factions; }
    public void setFactions(List<Map<String, Object>> factions) { this.factions = factions; }

    public Map<String, String> getProjects() { return projects; }
    public void setProjects(Map<String, String> projects) { this.projects = projects; }
}
