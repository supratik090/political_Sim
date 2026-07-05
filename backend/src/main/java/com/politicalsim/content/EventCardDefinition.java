package com.politicalsim.content;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "event_card_definitions")
public class EventCardDefinition {
    @Id
    private String id;

    @Indexed
    private String scenarioKey;

    @Indexed
    private String eventKey;

    private String name;
    private String description;
    private List<EventOption> options = new ArrayList<>();
    private boolean active = true;

    public static class EventOption {
        private String optionKey;
        private String text;
        private Map<String, Object> cost = new LinkedHashMap<>();
        private Map<String, Object> effects = new LinkedHashMap<>();

        public String getOptionKey() {
            return optionKey;
        }

        public void setOptionKey(String optionKey) {
            this.optionKey = optionKey;
        }

        public String getText() {
            return text;
        }

        public void setText(String text) {
            this.text = text;
        }

        public Map<String, Object> getCost() {
            return cost;
        }

        public void setCost(Map<String, Object> cost) {
            this.cost = cost;
        }

        public Map<String, Object> getEffects() {
            return effects;
        }

        public void setEffects(Map<String, Object> effects) {
            this.effects = effects;
        }
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getScenarioKey() {
        return scenarioKey;
    }

    public void setScenarioKey(String scenarioKey) {
        this.scenarioKey = scenarioKey;
    }

    public String getEventKey() {
        return eventKey;
    }

    public void setEventKey(String eventKey) {
        this.eventKey = eventKey;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<EventOption> getOptions() {
        return options;
    }

    public void setOptions(List<EventOption> options) {
        this.options = options;
    }

    public boolean isActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
}
