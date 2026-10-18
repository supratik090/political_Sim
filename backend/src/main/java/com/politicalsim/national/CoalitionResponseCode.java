package com.politicalsim.national;

public enum CoalitionResponseCode {
    ACCEPTED("Offer accepted! The party has formally joined your coalition front."),
    COUNTER_PROPOSAL("The party is open to joining but wants better terms — a counter proposal has been generated."),
    REFUSED_IDEOLOGY_CLASH("Refused: Fundamental ideological incompatibility between the coalition and this party."),
    REFUSED_COALITION_TOO_WEAK("Refused: The inviting coalition does not yet have enough parliamentary seats to be attractive."),
    REFUSED_HIGH_MORALE_INDEPENDENT("Refused: The party has high morale and prefers to remain independent."),
    REFUSED_FINANCIALLY_SECURE("Refused: The party is financially comfortable and found the offer unattractive."),
    REFUSED_LOYALTY_BOND("Refused: The party has deep historical ties to an existing political bloc."),
    REFUSED_UNATTRACTIVE_TERMS("Refused: The offered terms are not enticing enough to sway their leadership."),
    REFUSED_INSUFFICIENT_FUNDS("Refused: Your alliance treasury does not have sufficient funds to cover the promised joining bonus."),
    REFUSED_CABINET_CAP_EXCEEDED("Refused: Promised Cabinet Minister positions would exceed the constitutional limit of 20 per alliance."),
    REFUSED_STATE_MINISTER_CAP_EXCEEDED("Refused: Promised State Minister positions would exceed the constitutional limit of 50 per alliance."),
    REFUSED_NO_ACTIVE_ALLIANCE("Refused: You must first establish an active alliance front before inviting other parties."),
    REFUSED_ALREADY_IN_ALLIANCE("Refused: This party is already aligned with a coalition front."),
    REFUSED_INSUFFICIENT_SEATS("Refused: Your coalition lacks sufficient parliamentary seats relative to their standing."),
    BREAKAWAY_DETECTED("A pre-seeded party has left its alliance due to internal pressure."),
    SUCCESS("Operation completed successfully."),
    ERROR("An unexpected error occurred.");

    private final String defaultMessage;

    CoalitionResponseCode(String defaultMessage) {
        this.defaultMessage = defaultMessage;
    }

    public String getDefaultMessage() {
        return defaultMessage;
    }
}

