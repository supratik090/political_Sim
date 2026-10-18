package com.politicalsim.content;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "national_configs")
public class NationalConfig {

    @Id
    private String id;

    @Indexed(unique = true)
    private int era;

    private String title;
    private String description;
    private List<String> supportedIdeologies = new ArrayList<>();
    private List<Map<String, Object>> alliances = new ArrayList<>();
    private List<Map<String, Object>> parties = new ArrayList<>();
    private List<Map<String, Object>> stateSeatData = new ArrayList<>();
    private List<Map<String, Object>> legislativeBills = new ArrayList<>();
    private List<Map<String, Object>> seasons = new ArrayList<>();
    private List<Map<String, Object>> stateElections = new ArrayList<>();
    private List<Map<String, Object>> stateIssues = new ArrayList<>();

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public int getEra() {
        return era;
    }

    public void setEra(int era) {
        this.era = era;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<String> getSupportedIdeologies() {
        return supportedIdeologies;
    }

    public void setSupportedIdeologies(List<String> supportedIdeologies) {
        this.supportedIdeologies = supportedIdeologies;
    }

    public List<Map<String, Object>> getAlliances() {
        return alliances;
    }

    public void setAlliances(List<Map<String, Object>> alliances) {
        this.alliances = alliances;
    }

    public List<Map<String, Object>> getParties() {
        return parties;
    }

    public void setParties(List<Map<String, Object>> parties) {
        this.parties = parties;
    }

    public List<Map<String, Object>> getStateSeatData() {
        return stateSeatData;
    }

    public void setStateSeatData(List<Map<String, Object>> stateSeatData) {
        this.stateSeatData = stateSeatData;
    }

    public List<Map<String, Object>> getLegislativeBills() {
        return legislativeBills;
    }

    public void setLegislativeBills(List<Map<String, Object>> legislativeBills) {
        this.legislativeBills = legislativeBills;
    }

    public List<Map<String, Object>> getSeasons() {
        return seasons;
    }

    public void setSeasons(List<Map<String, Object>> seasons) {
        this.seasons = seasons;
    }

    public List<Map<String, Object>> getStateElections() {
        return stateElections;
    }

    public void setStateElections(List<Map<String, Object>> stateElections) {
        this.stateElections = stateElections;
    }

    public List<Map<String, Object>> getStateIssues() {
        return stateIssues;
    }

    public void setStateIssues(List<Map<String, Object>> stateIssues) {
        this.stateIssues = stateIssues;
    }
}
