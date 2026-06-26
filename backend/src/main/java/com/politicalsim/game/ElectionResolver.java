package com.politicalsim.game;

import com.politicalsim.party.PartyRole;
import com.politicalsim.party.PartyState;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class ElectionResolver {
    private final RoundResolutionEngine engine;

    public ElectionResolver(RoundResolutionEngine engine) {
        this.engine = engine;
    }

    public void conductElection(GameSession session, String reason, boolean isNoConfidenceElection) {
        // Distribute undecided support proportionally to all active parties so undecided becomes 0
        if (session.getPublicState() != null) {
            int undecided = session.getPublicState().getUndecidedSupport();
            if (undecided > 0) {
                int totalActiveSupport = session.getParties().stream()
                        .filter(PartyState::isActive)
                        .mapToInt(p -> p.getStats().getPublicSupport())
                        .sum();
                if (totalActiveSupport > 0) {
                    int distributed = 0;
                    List<PartyState> activeParties = new ArrayList<>(session.getParties().stream()
                            .filter(PartyState::isActive)
                            .toList());
                    // Sort to handle rounding remainder cleanly
                    activeParties.sort(Comparator.comparingInt((PartyState p) -> p.getStats().getPublicSupport()).reversed());
                    for (int i = 0; i < activeParties.size(); i++) {
                        PartyState party = activeParties.get(i);
                        int share;
                        if (i == activeParties.size() - 1) {
                            share = undecided - distributed;
                        } else {
                            share = (int) Math.round((double) party.getStats().getPublicSupport() * undecided / totalActiveSupport);
                        }
                        party.getStats().setPublicSupport(party.getStats().getPublicSupport() + share);
                        distributed += share;
                    }
                }
                session.getPublicState().setUndecidedSupport(0);
            }
        }

        List<PartyState> ranking = new ArrayList<>(session.getParties().stream()
                .filter(PartyState::isActive)
                .toList());
        ranking.sort(Comparator.comparingInt((PartyState party) -> party.getStats().getPublicSupport()).reversed());

        PartyState winner = ranking.get(0);
        PartyState runnerUp = ranking.size() > 1 ? ranking.get(1) : winner;
        for (PartyState party : ranking) {
            if (party.getId().equals(winner.getId())) {
                party.setRole(PartyRole.GOVERNMENT);
                party.getStats().setCoins(100);
                party.getStats().setPartyMorale(engine.clamp(party.getStats().getPartyMorale() + 5));
            } else if (party.getId().equals(runnerUp.getId())) {
                party.setRole(PartyRole.OPPOSITION);
                party.getStats().setCoins(75);
            } else {
                party.setRole(PartyRole.THIRD_PARTY);
                party.getStats().setCoins(75);
            }
        }

        session.setGovernmentParty(winner);
        session.setOppositionParty(runnerUp);
        session.getLastRoundCommentary().add(reason + " " + winner.getName() + " forms the government with "
                + winner.getStats().getPublicSupport() + "% support. Coin reserves reset: Government party gets 100 coins, other active parties get 75 coins.");

        // Save election results for the banner
        session.setLastElectionWinner(winner.getName());
        session.setLastElectionHeld(true);
        Map<String, Integer> voteShares = new LinkedHashMap<>();
        for (PartyState party : ranking) {
            voteShares.put(party.getName(), party.getStats().getPublicSupport());
        }
        if (session.getPublicState() != null) {
            voteShares.put("Undecided Voters", session.getPublicState().getUndecidedSupport());
        }
        session.setLastElectionVoteShares(voteShares);
        
        boolean humanWon = session.getPlayerPartyIds().contains(winner.getId());
        if (humanWon) {
            if (isNoConfidenceElection && session.getTurnNumber() < 60) {
                session.getLastRoundCommentary().add("🎉 Your No-Confidence Motion succeeded! You have won the early election and formed the government. You must now survive the next 60 months in office.");
                session.setLastResults(List.of("No-Confidence Successful: You formed the government!"));
            } else {
                session.setStatus(GameStatus.VICTORY);
                session.getLastRoundCommentary().add("🏆 VICTORY: You have successfully completed the 60-month campaign and won the election! Your party forms a stable government.");
                session.setLastResults(List.of("Victory: You won the election!"));
            }
        } else {
            session.setStatus(GameStatus.DEFEAT);
            session.getLastRoundCommentary().add("❌ DEFEAT: You did not win the election. " + winner.getName() + " has formed the government.");
            session.setLastResults(List.of("Defeat: You lost the election."));

            // Mark the human player as DEFEATED!
            for (PartyState party : session.getParties()) {
                if (session.getPlayerPartyIds().contains(party.getId())) {
                    party.setRole(com.politicalsim.party.PartyRole.DEFEATED);
                    party.setActive(false);
                    int supportToMove = party.getStats().getPublicSupport();
                    party.getStats().setPublicSupport(0);
                    session.getPublicState().setUndecidedSupport(session.getPublicState().getUndecidedSupport() + supportToMove);
                }
            }
        }
    }
}
