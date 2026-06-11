package com.politicalsim.content;

import java.util.ArrayList;
import java.util.List;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "monthly_issue_definitions")
public class MonthlyIssueDefinition {

    @Id
    private String id;

    @Indexed
    private String scenarioKey;

    private String issueKey;
    private List<String> roleAllowed = new ArrayList<>();
    private String category;
    private String title;
    private String description;
    private double weight = 1.0;
    private List<IssueOptionDefinition> options = new ArrayList<>();
    private boolean active = true;

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

    public String getIssueKey() {
        return issueKey;
    }

    public void setIssueKey(String issueKey) {
        this.issueKey = issueKey;
    }

    public List<String> getRoleAllowed() {
        return roleAllowed;
    }

    public void setRoleAllowed(List<String> roleAllowed) {
        this.roleAllowed = roleAllowed;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
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

    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }

    public List<IssueOptionDefinition> getOptions() {
        return options;
    }

    public void setOptions(List<IssueOptionDefinition> options) {
        this.options = options;
    }

    public boolean isActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
}
