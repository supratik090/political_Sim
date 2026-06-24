package com.politicalsim.api;

import com.politicalsim.party.Ideology;
import com.politicalsim.party.PartyRole;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class CreateGameRequest {

    private String playerPartyName;

    private PartyRole playerRole;

    private Ideology ideology;

    private String scenarioKey;
    private String stateName;
    private LocalDate startDate;
    private String userId;
    private List<CreatePartySetupRequest> partySetups = new ArrayList<>();

    public String getPlayerPartyName() {
        return playerPartyName;
    }

    public void setPlayerPartyName(String playerPartyName) {
        this.playerPartyName = playerPartyName;
    }

    public PartyRole getPlayerRole() {
        return playerRole;
    }

    public void setPlayerRole(PartyRole playerRole) {
        this.playerRole = playerRole;
    }

    public Ideology getIdeology() {
        return ideology;
    }

    public void setIdeology(Ideology ideology) {
        this.ideology = ideology;
    }

    public String getStateName() {
        return stateName;
    }

    public String getScenarioKey() {
        return scenarioKey;
    }

    public void setScenarioKey(String scenarioKey) {
        this.scenarioKey = scenarioKey;
    }

    public void setStateName(String stateName) {
        this.stateName = stateName;
    }

    public LocalDate getStartDate() {
        return startDate;
    }

    public void setStartDate(LocalDate startDate) {
        this.startDate = startDate;
    }

    public List<CreatePartySetupRequest> getPartySetups() {
        return partySetups;
    }

    public void setPartySetups(List<CreatePartySetupRequest> partySetups) {
        this.partySetups = partySetups;
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    private boolean retainInstitutions;

    public boolean isRetainInstitutions() {
        return retainInstitutions;
    }

    public void setRetainInstitutions(boolean retainInstitutions) {
        this.retainInstitutions = retainInstitutions;
    }
}
