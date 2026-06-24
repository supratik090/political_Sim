package com.politicalsim.party;

public class ProjectState {
    private String id = java.util.UUID.randomUUID().toString();
    private String projectKey;
    private int progressPercent;
    private String targetPartyId;
    private String targetPartyName;
    private boolean justCompleted;

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
}

