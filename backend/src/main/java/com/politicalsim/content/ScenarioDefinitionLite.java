package com.politicalsim.content;

import java.time.LocalDate;

public record ScenarioDefinitionLite(String id,
                                     String scenarioKey,
                                     String name,
                                     String description,
                                     String stateName,
                                     LocalDate startDate,
                                     int cycleLengthMonths,
                                     String governmentPartyName,
                                     String oppositionPartyName,
                                     String thirdPartyName,
                                     boolean active
) {
    // Canonical constructor override to handle default values cleanly
    public ScenarioDefinitionLite {
        if (cycleLengthMonths == 0) {
            cycleLengthMonths = 60;
        }
        if (null==startDate ) {
            startDate = LocalDate.of(2001,1,1);
        }
    }
}
