package com.politicalsim.api;

import com.politicalsim.game.GameStatus;
import com.politicalsim.content.CardDefinition;
import com.politicalsim.content.NewsDefinition;
import com.politicalsim.game.DelayedEffect;
import com.politicalsim.game.RoundSubmission;
import com.politicalsim.publicmood.PublicState;
import com.politicalsim.game.CooperationOffer;
import com.politicalsim.game.NonAggressionPact;
import java.time.LocalDate;
import com.politicalsim.party.PartyManagementState;
import java.time.LocalDateTime;

import java.util.List;
import java.util.Map;

public record TurnView(
        String gameId,
        String scenarioKey,
        String stateName,
        int turnNumber,
        int monthInCycle,
        int monthsUntilMandatoryElection,
        LocalDate currentDate,
        GameStatus status,
        List<PartyView> parties,
        String activeHumanPartyId,
        String activeHumanPartyName,
        int activeHumanPlayerIndex,
        PartyView governmentParty,
        PartyView oppositionParty,
        List<CardDefinition> availableCards,
        List<NewsDefinition> currentNews,
        Object currentIssue,
        PublicState publicState,
        boolean noConfidenceAvailable,
        String noConfidenceReason,
        Map<String, Map<String, Integer>> cardUsageByParty,
        List<RoundSubmission> currentRoundSubmissions,
        List<RoundSubmission> lastRoundSubmissions,
        Map<String, Map<String, Integer>> lastMetricDeltas,
        List<String> lastRoundCommentary,
        List<DelayedEffect> delayedEffects,
        List<String> pendingResults,
        List<String> lastResults,
        String currentRewardName,
        String currentRewardDescription,
        String currentRewardKey,
        Map<String, Integer> partyRoundWins,
        Map<String, Integer> lastRoundBids,
        String lastRoundBiddingMetric,
        String lastRoundWinnerPartyId,
        String biddingMetric,
        List<HeldRewardView> activePlayerHeldRewards,
        String activeCrisisKey,
        String activeCrisisName,
        String activeCrisisDescription,
        int activeCrisisTurnsLeft,
        boolean lastElectionHeld,
        String lastElectionWinner,
        Map<String, Integer> lastElectionVoteShares,
        List<CooperationOffer> cooperationOffers,
        List<NonAggressionPact> activePacts,
        boolean tripleImpactActive,
        boolean lastRoundProjectLimitsRefreshed,
        String lastRoundSecretMetric,
        boolean isMultiplayer,
        String joinCode,
        Map<String, String> humanPlayerMap,
        LocalDateTime turnStartTime,
        Integer turnDurationSeconds,
        List<com.politicalsim.game.LegislativeBillState> bills,
        Map<String, String> billVotes,
        String proposedBillKeyThisTurn,
        String activeEventKey,
        List<com.politicalsim.game.LobbyPledge> lobbyPledges,
        String lastResolvedBillKey,
        double lastBillYesVotes,
        double lastBillNoVotes,
        double lastBillAbstainVotes,
        Map<String, String> lastBillPartyVotes,
        PartyManagementState partyManagementState
) {
}
