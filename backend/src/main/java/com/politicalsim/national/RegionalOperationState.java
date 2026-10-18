package com.politicalsim.national;

import java.util.HashMap;
import java.util.Map;

public class RegionalOperationState {
    private String regionId;
    private String regionName;
    private int lokSabhaSeats;
    private int assemblySeats;
    private String description;

    // Monthly resources allocated by player to this region
    private double allocatedFunds = 0.0;
    private int allocatedWorkers = 0;
    private int allocatedVolunteers = 0;

    // Player party support percentage in this specific region (0.0 to 100.0)
    private double supportPercentage = 0.0;

    // Constructed buildings (key -> count)
    private Map<String, Integer> buildings = new HashMap<>();

    // Established wings / forums (key -> count/level)
    private Map<String, Integer> wings = new HashMap<>();

    public RegionalOperationState() {}

    public RegionalOperationState(String regionId, String regionName, int lokSabhaSeats, int assemblySeats, String description) {
        this.regionId = regionId;
        this.regionName = regionName;
        this.lokSabhaSeats = lokSabhaSeats;
        this.assemblySeats = assemblySeats;
        this.description = description;
    }

    public String getRegionId() { return regionId; }
    public void setRegionId(String regionId) { this.regionId = regionId; }

    public String getRegionName() { return regionName; }
    public void setRegionName(String regionName) { this.regionName = regionName; }

    public int getLokSabhaSeats() { return lokSabhaSeats; }
    public void setLokSabhaSeats(int lokSabhaSeats) { this.lokSabhaSeats = lokSabhaSeats; }

    public int getAssemblySeats() { return assemblySeats; }
    public void setAssemblySeats(int assemblySeats) { this.assemblySeats = assemblySeats; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    public double getAllocatedFunds() { return allocatedFunds; }
    public void setAllocatedFunds(double allocatedFunds) { this.allocatedFunds = allocatedFunds; }

    public int getAllocatedWorkers() { return allocatedWorkers; }
    public void setAllocatedWorkers(int allocatedWorkers) { this.allocatedWorkers = allocatedWorkers; }

    public int getAllocatedVolunteers() { return allocatedVolunteers; }
    public void setAllocatedVolunteers(int allocatedVolunteers) { this.allocatedVolunteers = allocatedVolunteers; }

    public double getSupportPercentage() { return supportPercentage; }
    public void setSupportPercentage(double supportPercentage) { this.supportPercentage = supportPercentage; }

    public Map<String, Integer> getBuildings() { return buildings; }
    public void setBuildings(Map<String, Integer> buildings) { this.buildings = buildings; }

    public Map<String, Integer> getWings() { return wings; }
    public void setWings(Map<String, Integer> wings) { this.wings = wings; }
}
