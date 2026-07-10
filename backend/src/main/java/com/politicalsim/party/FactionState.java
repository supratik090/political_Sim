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

    public FactionState() {
    }

    public FactionState(String key, String name, int loyalty, int influence) {
        this.key = key;
        this.name = name;
        this.loyalty = loyalty;
        this.influence = influence;
        this.active = true;
        this.post = new ArrayList<>();
        this.patronage = 0;
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
}
