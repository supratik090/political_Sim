package com.politicalsim.party;

import java.util.ArrayList;
import java.util.List;

public class FactionState {
    private String key; // veteran, youth, trade_union
    private String name;
    private boolean active = true;
    private int loyalty = 70;
    private int influence = 30;
    private List<String> post ; // "Secretary Post", "Fund Manager Post", etc.
    private int patronage = 0; // patronage points assigned
    private int frozenTurnsRemaining = 0;
    private java.util.Map<String, Integer> frozenPosts = new java.util.HashMap<>();
    private java.util.List<Integer> frozenPatronageTurns = new java.util.ArrayList<>();

    public FactionState() {
        this.frozenPosts = new java.util.HashMap<>();
        this.frozenPatronageTurns = new java.util.ArrayList<>();
    }

    public FactionState(String key, String name, int loyalty, int influence) {
        this.key = key;
        this.name = name;
        this.loyalty = loyalty;
        this.influence = influence;
        this.active = true;
        this.post = new ArrayList<>();
        this.patronage = 0;
        this.frozenTurnsRemaining = 0;
        this.frozenPosts = new java.util.HashMap<>();
        this.frozenPatronageTurns = new java.util.ArrayList<>();
    }

    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public boolean isActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    public int getLoyalty() {
        return loyalty;
    }

    public void setLoyalty(int loyalty) {
        this.loyalty = Math.min(100, Math.max(0, loyalty));
    }

    public int getInfluence() {
        return influence;
    }

    public void setInfluence(int influence) {
        this.influence = Math.max(0, influence);
    }

    public List<String> getPost() {
        return post;
    }

    public void setPost(List<String> post) {
        this.post = post;
    }

    public int getPatronage() {
        return patronage;
    }

    public void setPatronage(int patronage) {
        this.patronage = Math.max(0, patronage);
    }

    public int getFrozenTurnsRemaining() {
        return frozenTurnsRemaining;
    }

    public void setFrozenTurnsRemaining(int frozenTurnsRemaining) {
        this.frozenTurnsRemaining = frozenTurnsRemaining;
    }

    public java.util.Map<String, Integer> getFrozenPosts() {
        if (frozenPosts == null) frozenPosts = new java.util.HashMap<>();
        return frozenPosts;
    }

    public void setFrozenPosts(java.util.Map<String, Integer> frozenPosts) {
        this.frozenPosts = frozenPosts;
    }

    public java.util.List<Integer> getFrozenPatronageTurns() {
        if (frozenPatronageTurns == null) frozenPatronageTurns = new java.util.ArrayList<>();
        return frozenPatronageTurns;
    }

    public void setFrozenPatronageTurns(java.util.List<Integer> frozenPatronageTurns) {
        this.frozenPatronageTurns = frozenPatronageTurns;
    }
}
