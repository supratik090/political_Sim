package com.politicalsim.content;

import com.fasterxml.jackson.annotation.JsonAlias;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "news_definitions")
public class NewsDefinition {

    @Id
    private String id;

    @Indexed
    private String scenarioKey;

    @JsonAlias({"newsKey", "issueKey"})
    private String newsKey;
    private String type;
    private String title;
    private String description;
    private List<String> monthTags = new ArrayList<>();
    private List<String> issueTags = new ArrayList<>();
    private String crisisTriggerKey;
    private int crisisDuration;

    @JsonAlias({"reactionOptions", "options"})
    private List<NewsReactionDefinition> reactionOptions = new ArrayList<>();
    private Map<String, Object> weights = new LinkedHashMap<>();
    private boolean active = true;

    public String getCrisisTriggerKey() {
        return crisisTriggerKey;
    }

    public void setCrisisTriggerKey(String crisisTriggerKey) {
        this.crisisTriggerKey = crisisTriggerKey;
    }

    public int getCrisisDuration() {
        return crisisDuration;
    }

    public void setCrisisDuration(int crisisDuration) {
        this.crisisDuration = crisisDuration;
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

    public String getNewsKey() {
        return newsKey;
    }

    public void setNewsKey(String newsKey) {
        this.newsKey = newsKey;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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

    public List<String> getMonthTags() {
        return monthTags;
    }

    public void setMonthTags(List<String> monthTags) {
        this.monthTags = monthTags;
    }

    public List<String> getIssueTags() {
        return issueTags;
    }

    public void setIssueTags(List<String> issueTags) {
        this.issueTags = issueTags;
    }

    public List<NewsReactionDefinition> getReactionOptions() {
        return reactionOptions;
    }

    public void setReactionOptions(List<NewsReactionDefinition> reactionOptions) {
        this.reactionOptions = reactionOptions;
    }

    public List<NewsReactionDefinition> getOptions() {
        return reactionOptions;
    }

    public void setOptions(List<NewsReactionDefinition> options) {
        this.reactionOptions = options;
    }

    public String getIssueKey() {
        return newsKey;
    }

    public void setIssueKey(String issueKey) {
        this.newsKey = issueKey;
    }

    public Map<String, Object> getWeights() {
        return weights;
    }

    public void setWeights(Map<String, Object> weights) {
        this.weights = weights;
    }

    public boolean isActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
}
