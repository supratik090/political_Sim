package com.politicalsim.publicmood;

import java.util.ArrayList;
import java.util.List;

public class PublicState {

    private int undecidedSupport;
    private String mood;
    private List<String> mainIssues = new ArrayList<>();
    private String memoryHint;

    public PublicState() {
    }

    public PublicState(int undecidedSupport, String mood, List<String> mainIssues, String memoryHint) {
        this.undecidedSupport = undecidedSupport;
        this.mood = mood;
        this.mainIssues = mainIssues;
        this.memoryHint = memoryHint;
    }

    public int getUndecidedSupport() {
        return undecidedSupport;
    }

    public void setUndecidedSupport(int undecidedSupport) {
        this.undecidedSupport = undecidedSupport;
    }

    public String getMood() {
        return mood;
    }

    public void setMood(String mood) {
        this.mood = mood;
    }

    public List<String> getMainIssues() {
        return mainIssues;
    }

    public void setMainIssues(List<String> mainIssues) {
        this.mainIssues = mainIssues;
    }

    public String getMemoryHint() {
        return memoryHint;
    }

    public void setMemoryHint(String memoryHint) {
        this.memoryHint = memoryHint;
    }
}
