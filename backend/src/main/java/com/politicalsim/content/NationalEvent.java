package com.politicalsim.content;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "national_events")
public class NationalEvent {

    @Id
    private String id;
    private String eventKey;
    private String title;
    private String type; // e.g. POLITICAL_SHAKEUP, PARLIAMENTARY_BILL, ECONOMIC_CRISIS
    private int era = 2001;
    private int season = 1;
    private String icon = "🎓";
    private String summary;
    private String narrative;

    // Section 1: Contextual effects based on Government Standing and Ideology Affinity
    private Map<String, Object> contextualEffects = new LinkedHashMap<>();

    // Section 2: 4 Reaction options tailored for Ruling party vs 4 for Opposition
    private List<Map<String, Object>> rulingReactionOptions = new ArrayList<>();
    private List<Map<String, Object>> oppositionReactionOptions = new ArrayList<>();

    public NationalEvent() {}

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getEventKey() { return eventKey; }
    public void setEventKey(String eventKey) { this.eventKey = eventKey; }

    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }

    public String getType() { return type; }
    public void setType(String type) { this.type = type; }

    public int getEra() { return era; }
    public void setEra(int era) { this.era = era; }

    public int getSeason() { return season; }
    public void setSeason(int season) { this.season = season; }

    public String getIcon() { return icon; }
    public void setIcon(String icon) { this.icon = icon; }

    public String getSummary() { return summary; }
    public void setSummary(String summary) { this.summary = summary; }

    public String getNarrative() { return narrative; }
    public void setNarrative(String narrative) { this.narrative = narrative; }

    public Map<String, Object> getContextualEffects() { return contextualEffects; }
    public void setContextualEffects(Map<String, Object> contextualEffects) { this.contextualEffects = contextualEffects; }

    public List<Map<String, Object>> getRulingReactionOptions() { return rulingReactionOptions; }
    public void setRulingReactionOptions(List<Map<String, Object>> rulingReactionOptions) { this.rulingReactionOptions = rulingReactionOptions; }

    public List<Map<String, Object>> getOppositionReactionOptions() { return oppositionReactionOptions; }
    public void setOppositionReactionOptions(List<Map<String, Object>> oppositionReactionOptions) { this.oppositionReactionOptions = oppositionReactionOptions; }
}
