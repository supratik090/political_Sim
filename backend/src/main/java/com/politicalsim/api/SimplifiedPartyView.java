package com.politicalsim.api;

import com.politicalsim.party.ControllerType;
import com.politicalsim.party.Ideology;
import com.politicalsim.party.PartyRole;
import com.politicalsim.party.PartyState;
import java.util.List;

public record SimplifiedPartyView(
        String id,
        String name,
        PartyRole role,
        ControllerType controllerType,
        String color,
        String symbol,
        Ideology ideology,
        boolean playerControlled
) {
    public static SimplifiedPartyView from(PartyState party, List<String> playerPartyIds) {
        return new SimplifiedPartyView(
                party.getId(),
                party.getName(),
                party.getRole(),
                party.getControllerType(),
                party.getColor(),
                party.getSymbol(),
                party.getIdeology(),
                playerPartyIds != null && playerPartyIds.contains(party.getId())
        );
    }
}
