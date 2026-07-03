package com.politicalsim.api;

import com.politicalsim.game.GameSession;
import com.politicalsim.game.GameStatus;
import java.time.LocalDate;
import java.util.List;

public record GameSessionSummary(
        String id,
        String scenarioKey,
        String scenarioName,
        LocalDate currentDate,
        int turnNumber,
        GameStatus status,
        String createdAt,
        String playerPartyId,
        boolean isMultiplayer,
        String joinCode,
        String lastElectionWinner,
        List<SimplifiedPartyView> parties
) {
    public static GameSessionSummary from(GameSession session) {
        return new GameSessionSummary(
                session.getId(),
                session.getScenarioKey(),
                session.getScenarioName(),
                session.getCurrentDate(),
                session.getTurnNumber(),
                session.getStatus(),
                session.getCreatedAt(),
                session.getPlayerPartyId(),
                session.isMultiplayer(),
                session.getJoinCode(),
                session.getLastElectionWinner(),
                session.getParties() == null ? List.of() : session.getParties().stream()
                        .map(p -> SimplifiedPartyView.from(p, session.getPlayerPartyIds()))
                        .toList()
        );
    }
}
