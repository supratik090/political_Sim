package com.politicalsim.party;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.index.Indexed;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

/**
 * Dedicated MongoDB document for tracking a party's Party Management state
 * (faction card allocation). Stored separately from GameSession to keep the
 * main document lean and avoid repeated large reads for this feature.
 *
 * Collection: party_management_state
 */
@Document(collection = "party_management_state")
public class PartyManagementState {

    @Id
    private String id;

    @Indexed
    private String gameId;

    @Indexed
    private String partyId;

    /**
     * How many Patronage Point cards are currently unallocated in the player's hand.
     * +1 is added every turn during resolution, deducted when player assigns one.
     */
    private int unallocatedPatronagePoints = 1;

    private Map<String, Integer> allocatedPatronagePoints ;

    /**
     * Ordered list of all posts scheduled for this party for the entire game.
     * Loaded and shuffled at game start with pre-assigned turns.
     * Status transitions: PENDING -> AVAILABLE (on availableOnTurn) -> ASSIGNED (when allocated).
     */
    private List<ScheduledPost> posts = new ArrayList<>();

    public PartyManagementState() {}

    public PartyManagementState(String gameId, String partyId) {
        this.gameId = gameId;
        this.partyId = partyId;
        this.unallocatedPatronagePoints = 1;
        this.posts = new ArrayList<>();
        this.allocatedPatronagePoints = new ConcurrentHashMap<>();
    }

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getGameId() { return gameId; }
    public void setGameId(String gameId) { this.gameId = gameId; }

    public String getPartyId() { return partyId; }
    public void setPartyId(String partyId) { this.partyId = partyId; }

    public int getUnallocatedPatronagePoints() { return unallocatedPatronagePoints; }
    public void setUnallocatedPatronagePoints(int unallocatedPatronagePoints) {
        this.unallocatedPatronagePoints = Math.max(0, unallocatedPatronagePoints);
    }

    public List<ScheduledPost> getPosts() {
        if (posts == null) posts = new ArrayList<>();
        return posts;
    }
    public void setPosts(List<ScheduledPost> posts) { this.posts = posts; }

    /**
     * Convenience: return only posts with status AVAILABLE (in the player's hand but unassigned).
     */
    public List<ScheduledPost> getAvailablePosts() {
        return getPosts().stream()
                .filter(p -> p.getStatus() == ScheduledPost.Status.AVAILABLE)
                .toList();
    }

    /**
     * Convenience: return only posts with status ASSIGNED (already given to a faction).
     */
    public List<ScheduledPost> getAssignedPosts() {
        return getPosts().stream()
                .filter(p -> p.getStatus() == ScheduledPost.Status.ASSIGNED)
                .toList();
    }

    public Map<String, Integer> getAllocatedPatronagePoints() {
        return allocatedPatronagePoints;
    }

    public void setAllocatedPatronagePoints(Map<String, Integer> allocatedPatronagePoints) {
        this.allocatedPatronagePoints = allocatedPatronagePoints;
    }
}
