package com.politicalsim.content;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "state_infrastructure_definitions")
public class StateInfrastructureDefinition {

    @Id
    private String id;
    private String key;
    private String name;
    private String category; // BUILDING or WING
    private String scope;    // STATE or REGION
    private String icon = "🏢";
    private String description;
    
    // Upfront Construction Cost (Max 1.0 Cr, no worker requirement)
    private double costFunds = 0.0;
    
    // Monthly Cash Generation (Always cash positive)
    private double monthlyCashOutput = 0.0; // in Cr
    
    // Relative monthly percentage increases to pools
    private double workersPercentMonthly = 0.0;   // e.g. 1.0 = +1.0% state/regional cadres
    private double volunteersPercentMonthly = 0.0;// e.g. 1.5 = +1.5% state/regional volunteers
    private double donorsPercentMonthly = 0.0;    // e.g. 1.0 = +1.0% state/regional donors
    
    // Support Bonuses: Explicit distinction between One-Time vs Recurring per season
    private double instantSupportBonus = 0.0; // One-time boost upon establishment
    private double monthlySupportBonus = 0.0; // Recurring boost per turn
    
    private int maxAllowedPerScope = 1;

    public StateInfrastructureDefinition() {}

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getKey() { return key; }
    public void setKey(String key) { this.key = key; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getCategory() { return category; }
    public void setCategory(String category) { this.category = category; }

    public String getScope() { return scope; }
    public void setScope(String scope) { this.scope = scope; }

    public String getIcon() { return icon; }
    public void setIcon(String icon) { this.icon = icon; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    public double getCostFunds() { return costFunds; }
    public void setCostFunds(double costFunds) { this.costFunds = costFunds; }

    public double getMonthlyCashOutput() { return monthlyCashOutput; }
    public void setMonthlyCashOutput(double monthlyCashOutput) { this.monthlyCashOutput = monthlyCashOutput; }

    public double getWorkersPercentMonthly() { return workersPercentMonthly; }
    public void setWorkersPercentMonthly(double workersPercentMonthly) { this.workersPercentMonthly = workersPercentMonthly; }

    public double getVolunteersPercentMonthly() { return volunteersPercentMonthly; }
    public void setVolunteersPercentMonthly(double volunteersPercentMonthly) { this.volunteersPercentMonthly = volunteersPercentMonthly; }

    public double getDonorsPercentMonthly() { return donorsPercentMonthly; }
    public void setDonorsPercentMonthly(double donorsPercentMonthly) { this.donorsPercentMonthly = donorsPercentMonthly; }

    public double getInstantSupportBonus() { return instantSupportBonus; }
    public void setInstantSupportBonus(double instantSupportBonus) { this.instantSupportBonus = instantSupportBonus; }

    public double getMonthlySupportBonus() { return monthlySupportBonus; }
    public void setMonthlySupportBonus(double monthlySupportBonus) { this.monthlySupportBonus = monthlySupportBonus; }

    public double getSupportBonus() {
        return instantSupportBonus > 0 ? instantSupportBonus : monthlySupportBonus;
    }

    public int getMaxAllowedPerScope() { return maxAllowedPerScope; }
    public void setMaxAllowedPerScope(int maxAllowedPerScope) { this.maxAllowedPerScope = maxAllowedPerScope; }
}
