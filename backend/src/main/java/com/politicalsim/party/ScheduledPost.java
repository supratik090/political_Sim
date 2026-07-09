package com.politicalsim.party;

/**
 * Represents a political post that has been scheduled for delivery to a party's
 * faction management deck. Posts are pre-scheduled at game startup and become
 * AVAILABLE on their designated turn.
 */
public class ScheduledPost {

    public enum Status {
        PENDING,    // Not yet available - turn hasn't arrived
        AVAILABLE,  // In the unallocated deck, player can assign it
        ASSIGNED    // Assigned to a faction
    }

    private String postKey;         // Unique key e.g. "SECRETARY"
    private String postName;        // Display name e.g. "Secretary"
    private int availableOnTurn;    // Turn number when this becomes AVAILABLE
    private Status status = Status.PENDING;
    private String assignedFactionKey; // null unless status == ASSIGNED

    public ScheduledPost() {}

    public ScheduledPost(String postKey, String postName, int availableOnTurn) {
        this.postKey = postKey;
        this.postName = postName;
        this.availableOnTurn = availableOnTurn;
        this.status = Status.PENDING;
    }

    public String getPostKey() { return postKey; }
    public void setPostKey(String postKey) { this.postKey = postKey; }

    public String getPostName() { return postName; }
    public void setPostName(String postName) { this.postName = postName; }

    public int getAvailableOnTurn() { return availableOnTurn; }
    public void setAvailableOnTurn(int availableOnTurn) { this.availableOnTurn = availableOnTurn; }

    public Status getStatus() { return status; }
    public void setStatus(Status status) { this.status = status; }

    public String getAssignedFactionKey() { return assignedFactionKey; }
    public void setAssignedFactionKey(String assignedFactionKey) { this.assignedFactionKey = assignedFactionKey; }
}
