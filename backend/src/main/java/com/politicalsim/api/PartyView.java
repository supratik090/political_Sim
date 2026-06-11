package com.politicalsim.api;

import com.politicalsim.ai.AiProfile;
import com.politicalsim.party.ControllerType;
import com.politicalsim.party.Ideology;
import com.politicalsim.party.PartyRole;
import com.politicalsim.party.PartyStats;
import com.politicalsim.party.PartyState;
import java.util.List;

public record PartyView(
        String id,
        String name,
        PartyRole role,
        ControllerType controllerType,
        String humanPlayerLabel,
        String color,
        String symbol,
        Ideology ideology,
        AiProfile aiProfile,
        PartyStats stats,
        boolean playerControlled
) {
    public static PartyView from(PartyState party, String playerPartyId) {
        return from(party, List.of(playerPartyId));
    }

    public static PartyView from(PartyState party, List<String> playerPartyIds) {
        return new PartyView(
                party.getId(),
                party.getName(),
                party.getRole(),
                party.getControllerType(),
                party.getHumanPlayerLabel(),
                party.getColor(),
                party.getSymbol(),
                party.getIdeology(),
                party.getAiProfile(),
                party.getStats(),
                playerPartyIds.contains(party.getId())
        );
    }
}
