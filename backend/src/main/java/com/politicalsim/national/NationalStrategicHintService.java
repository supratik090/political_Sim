package com.politicalsim.national;

import org.springframework.stereotype.Service;

import java.util.*;
import java.util.stream.Collectors;

/**
 * NationalStrategicHintService
 * Backend Dynamic AI Strategy & Tactical Advisor Engine.
 * Generates turn-by-turn guidance evaluating:
 * - Actions the player has taken vs actions NOT taken this turn
 * - Dynamic player stats (morale collapse, treasury depletion, corruption/greed heat)
 * - 272 Lok Sabha majority gap and alliance progression
 * - Concrete state-level battleground transfers, infrastructure buildings, and tactical issue actions.
 */
@Service
public class NationalStrategicHintService {

    public Map<String, Object> generateStrategicHints(NationalGame game) {
        if (game == null) return Collections.emptyMap();

        int currentSeason = game.getCurrentSeason();
        String playerPartyKey = (game.getPartyKey() != null ? game.getPartyKey() : "ydp").toLowerCase();
        String playerPartyKeyUpper = playerPartyKey.toUpperCase();

        List<NationalPartyState> partyStates = game.getPartyStates() != null ? game.getPartyStates() : Collections.emptyList();
        NationalPartyState playerState = game.findPartyState(playerPartyKey);

        double currentFunds = playerState != null ? playerState.getFunds() : game.getPlayerFunds();
        int currentMorale = playerState != null ? playerState.getMorale() : 70;
        int currentCorruption = playerState != null ? playerState.getCorruption() : game.getPlayerCorruption();
        int currentWorkers = playerState != null ? playerState.getWorkers() : 50000;
        int currentVolunteers = playerState != null ? playerState.getVolunteers() : 15000;
        int initialSeats = playerState != null ? (int) playerState.getSeats() : 0;

        Map<String, Integer> projSeatsMap = game.getNationalProjectedSeats() != null
                ? game.getNationalProjectedSeats()
                : Collections.emptyMap();
        int playerProjSeats = projSeatsMap.getOrDefault(playerPartyKeyUpper, initialSeats);

        // ── 1. ALLIANCE & MAJORITY CALCULATION ──────────────────────────────────
        List<NationalAlliance> alliances = game.getAlliances() != null ? game.getAlliances() : Collections.emptyList();
        NationalAlliance playerAlliance = game.findPlayerAlliance(playerPartyKey);
        boolean isAllianceLeader = playerAlliance != null && playerPartyKey.equalsIgnoreCase(playerAlliance.getLeaderPartyKey());

        int totalAllianceSeats = playerProjSeats;
        if (playerAlliance != null && playerAlliance.getMembers() != null) {
            Set<String> memberKeys = new HashSet<>();
            if (playerAlliance.getLeaderPartyKey() != null) memberKeys.add(playerAlliance.getLeaderPartyKey());
            for (NationalAllianceMember m : playerAlliance.getMembers()) {
                if (m.getPartyKey() != null) memberKeys.add(m.getPartyKey());
            }

            int sum = 0;
            for (String mk : memberKeys) {
                String mkUpper = mk.toUpperCase();
                if (projSeatsMap.containsKey(mkUpper)) {
                    sum += projSeatsMap.get(mkUpper);
                } else {
                    NationalPartyState ps = game.findPartyState(mk);
                    sum += ps != null ? (int) ps.getSeats() : 0;
                }
            }
            totalAllianceSeats = sum;
        }

        int majorityGap = Math.max(0, 272 - totalAllianceSeats);
        boolean hasMajority = totalAllianceSeats >= 272;

        // ── 2. ACTIONS TAKEN VS NOT TAKEN THIS TURN ─────────────────────────────
        // Action 1: Coalition
        boolean isCoalitionDone = false;
        if (game.getPendingRequests() != null) {
            isCoalitionDone = game.getPendingRequests().stream()
                    .anyMatch(r -> r.getCreatedAtSeason() == currentSeason || "ACCEPTED".equalsIgnoreCase(r.getStatus()) || "REJECTED".equalsIgnoreCase(r.getStatus()));
        }

        // Action 2: Finance
        boolean isFinanceDone = game.getCommittedFinanceCard() != null && !game.getCommittedFinanceCard().isEmpty();

        // Action 3: Events & Issues
        List<String> eventIds = game.getCurrentSeasonEventIds() != null ? game.getCurrentSeasonEventIds() : Collections.emptyList();
        Map<String, String> resolvedEvents = game.getResolvedEventReactions() != null ? game.getResolvedEventReactions() : Collections.emptyMap();
        int pendingEventsCount = Math.max(0, eventIds.size() - resolvedEvents.size());
        boolean isThemeActionDone = game.getActiveThemeAction() != null && !game.getActiveThemeAction().isEmpty();
        boolean isEventsDone = pendingEventsCount == 0 || isThemeActionDone;

        // Action 4: States (Only eligible / unlocked states count for turn completion)
        Map<String, NationalStateOperationState> stateOps = game.getStateOperations() != null ? game.getStateOperations() : Collections.emptyMap();
        List<NationalStateOperationState> eligibleStates = new ArrayList<>();
        List<NationalStateOperationState> lockedStates = new ArrayList<>();
        for (NationalStateOperationState st : stateOps.values()) {
            if (NationalGameService.isStateEligibleForPlayer(game, st)) {
                eligibleStates.add(st);
            } else {
                lockedStates.add(st);
            }
        }

        int totalStates = eligibleStates.size();
        int playedStatesCount = 0;
        int skippedStatesCount = 0;
        for (NationalStateOperationState st : eligibleStates) {
            if (st.isDoneThisTurn()) playedStatesCount++;
            else if (st.isSkippedThisTurn()) skippedStatesCount++;
        }
        int completedStatesCount = playedStatesCount + skippedStatesCount;
        boolean allStatesCompleted = totalStates > 0 && completedStatesCount >= totalStates;
        boolean hasNotPlayedAnyStates = totalStates > 0 && playedStatesCount == 0;

        int doneCount = (isCoalitionDone ? 1 : 0) + (isFinanceDone ? 1 : 0) + (isEventsDone ? 1 : 0) + (allStatesCompleted ? 1 : 0);
        boolean isAllFourDone = doneCount == 4;

        // ── 3. DYNAMIC STATS EVALUATION (MORALE, TREASURY, CORRUPTION) ──────────
        List<String> urgentWarnings = new ArrayList<>();

        // Morale Evaluation & Guidance
        Map<String, Object> moraleStatus = new HashMap<>();
        moraleStatus.put("morale", currentMorale);
        if (currentMorale < 45) {
            moraleStatus.put("trend", "CRITICAL");
            moraleStatus.put("badge", "CRITICAL MORALE COLLAPSE ⚠️");
            moraleStatus.put("badgeColor", "#ef4444");
            moraleStatus.put("advice", "Cadre morale is collapsed at " + currentMorale + "%. Grassroots turnout in state elections suffers severe penalties. Avoid high-scrutiny cards, respond favorably to popular civic crises, and execute public rallies immediately.");
            urgentWarnings.add("CRITICAL CADRE MORALE (" + currentMorale + "%): Severe turnout penalty active across all states. Restore morale via grassroots actions.");
        } else if (currentMorale < 60) {
            moraleStatus.put("trend", "LOW");
            moraleStatus.put("badge", "LOW CADRE MORALE ⚠️");
            moraleStatus.put("badgeColor", "#f59e0b");
            moraleStatus.put("advice", "Cadre morale is low at " + currentMorale + "%. Party workers are dispirited. Prioritize worker-centric rallies, padayatras, and community outreach.");
            urgentWarnings.add("LOW CADRE MORALE (" + currentMorale + "%): Dispirited party workers reducing campaign effectiveness.");
        } else if (currentMorale < 75) {
            moraleStatus.put("trend", "HEALTHY");
            moraleStatus.put("badge", "HEALTHY CADRE MORALE ✓");
            moraleStatus.put("badgeColor", "#10b981");
            moraleStatus.put("advice", "Cadre morale is stable at " + currentMorale + "%. Workers are active and responsive to regional campaign orders.");
        } else {
            moraleStatus.put("trend", "EXCELLENT");
            moraleStatus.put("badge", "HIGH MOMENTUM 🔥");
            moraleStatus.put("badgeColor", "#38bdf8");
            moraleStatus.put("advice", "Cadres are energized at " + currentMorale + "%! Your campaigns receive +15% amplification on state voting swings.");
        }

        // Treasury & Greed Evaluation
        int greedHeat = game.getMegaFinanceHeat();
        Map<String, Object> treasuryStatus = new HashMap<>();
        treasuryStatus.put("funds", Math.round(currentFunds * 10.0) / 10.0);
        treasuryStatus.put("corruption", currentCorruption);
        treasuryStatus.put("greedHeat", greedHeat);

        if (greedHeat >= 3 || currentCorruption > 35) {
            treasuryStatus.put("alertLevel", "HIGH_SCRUTINY");
            treasuryStatus.put("advice", "High Scrutiny Alert (Heat " + greedHeat + "/4, Corruption " + currentCorruption + "%). Investigative agencies and press are probing party accounts. Avoid mega corporate cards to cool down heat.");
            urgentWarnings.add("HIGH MEDIA/CORRUPTION SCRUTINY (Heat " + greedHeat + "/4): Avoid corporate mega-finance cards to prevent election scandal leaks.");
        } else if (currentFunds < 18.0) {
            treasuryStatus.put("alertLevel", "LOW_RESERVES");
            treasuryStatus.put("advice", "Treasury is depleted (₹" + String.format(Locale.US, "%.1f", currentFunds) + " Cr). Inability to fund regional campaigns will stall expansion. Select high-inflow fundraising cards.");
            urgentWarnings.add("TREASURY DEFICIT: Party reserves below ₹18 Cr. Secure campaign cash before state election deadlines.");
        } else {
            treasuryStatus.put("alertLevel", "STABLE");
            treasuryStatus.put("advice", "Treasury reserves are healthy at ₹" + String.format(Locale.US, "%.1f", currentFunds) + " Cr. Maintain balanced expansion.");
        }

        // State Action Alert (Urge player if eligible states unplayed)
        if (hasNotPlayedAnyStates) {
            urgentWarnings.add("⚠️ UNPLAYED ELIGIBLE STATES: You have not taken action in any of your " + totalStates + " eligible battleground states this turn! Inaction concedes regional ground to rivals.");
        }
        if (!isFinanceDone) {
            urgentWarnings.add("⚠️ TREASURY ACTION PENDING: You have not chosen a Finance Strategy Card this turn. Select a card to fund ongoing party machinery.");
        }
        if (pendingEventsCount > 0) {
            urgentWarnings.add("⚠️ UNRESOLVED CRISES: " + pendingEventsCount + " National Event Reaction(s) pending response.");
        }

        // ── 4. EXECUTIVE SUMMARY ────────────────────────────────────────────────
        String strategicPhase;
        String phaseTitle;
        if (currentSeason > 40 || majorityGap <= 30) {
            strategicPhase = "ENDGAME";
            phaseTitle = "Phase 3: Endgame & 272 Threshold";
        } else if (currentSeason > 15) {
            strategicPhase = "EXPANSION";
            phaseTitle = "Phase 2: Regional Expansion";
        } else {
            strategicPhase = "FOUNDATION";
            phaseTitle = "Phase 1: Grassroots Foundation";
        }

        String topObjective;
        if (hasMajority) {
            topObjective = "Majority threshold secured! Your alliance controls " + totalAllianceSeats + " projected seats (272 required). Maintain coalition harmony and prepare for Lok Sabha floor test.";
        } else if (playerAlliance == null) {
            topObjective = "Form a Coalition Front immediately. Without alliance partners, you cannot bridge the " + majorityGap + "-seat gap to the 272 Lok Sabha majority.";
        } else if (majorityGap > 100) {
            topObjective = "Expand Coalition Front into high-seat battlegrounds (UP, Bihar, Maharashtra) to close your " + majorityGap + "-seat deficit.";
        } else {
            topObjective = "Final sprint to power: Only " + majorityGap + " more seats needed to cross 272. Target upcoming state assembly polls to swing close constituencies.";
        }

        Map<String, Object> summary = new HashMap<>();
        summary.put("strategicPhase", strategicPhase);
        summary.put("phaseTitle", phaseTitle);
        summary.put("topObjective", topObjective);
        summary.put("majorityGap", majorityGap);
        summary.put("totalAllianceSeats", totalAllianceSeats);
        summary.put("targetSeats", 272);
        summary.put("hasMajority", hasMajority);
        summary.put("currentSeason", currentSeason);
        summary.put("doneCount", doneCount);
        summary.put("isAllFourDone", isAllFourDone);
        summary.put("moraleStatus", moraleStatus);
        summary.put("treasuryStatus", treasuryStatus);

        // ── 5. DIRECTIVE 1: COALITION FRONT GUIDANCE ────────────────────────────
        int cabinetUsed = playerAlliance != null ? playerAlliance.getTotalCabinetPromised() : 0;
        int stateUsed = playerAlliance != null ? playerAlliance.getTotalStatePromised() : 0;
        int cabinetLeft = Math.max(0, 20 - cabinetUsed);
        int stateLeft = Math.max(0, 50 - stateUsed);

        // Find promising unaligned parties
        List<NationalPartyState> unalignedParties = partyStates.stream()
                .filter(p -> {
                    String pk = p.getPartyKey() != null ? p.getPartyKey().toLowerCase() : "";
                    if (pk.equals(playerPartyKey)) return false;
                    if (pk.equals("bjp") || pk.equals("inc")) return false; // Major rival leaders
                    if (playerAlliance != null && playerAlliance.getMembers() != null) {
                        return playerAlliance.getMembers().stream().noneMatch(m -> pk.equalsIgnoreCase(m.getPartyKey()));
                    }
                    return true;
                })
                .sorted((a, b) -> {
                    int aSeats = projSeatsMap.getOrDefault(a.getPartyKey().toUpperCase(), (int) a.getSeats());
                    int bSeats = projSeatsMap.getOrDefault(b.getPartyKey().toUpperCase(), (int) b.getSeats());
                    if (bSeats != aSeats) return bSeats - aSeats;
                    return a.getMorale() - b.getMorale();
                })
                .collect(Collectors.toList());

        NationalPartyState topRecruit = !unalignedParties.isEmpty() ? unalignedParties.get(0) : null;
        int targetSeats = topRecruit != null
                ? projSeatsMap.getOrDefault(topRecruit.getPartyKey().toUpperCase(), (int) topRecruit.getSeats())
                : 0;

        String coalitionRec;
        String coalitionTip;
        String coalitionBadge;
        String coalitionBadgeColor;

        if (playerAlliance == null) {
            coalitionBadge = "NO FRONT FORMED ⚠️";
            coalitionBadgeColor = "#f59e0b";
            coalitionRec = "You are currently contesting alone. Bridge the " + majorityGap + "-seat gap by founding an alliance front and recruiting regional powerhouses.";
            coalitionTip = topRecruit != null
                    ? "Invite " + (topRecruit.getPartyName() != null ? topRecruit.getPartyName() : topRecruit.getPartyKey().toUpperCase()) +
                      " (+" + targetSeats + " Projected Seats). Offer 2 Cabinet Ministers, 4 MoS slots, and ₹" + String.format(Locale.US, "%.1f", Math.min(3.0, currentFunds * 0.15)) + " Cr joining bonus."
                    : "Form a new alliance front and invite regional partners.";
        } else if (isAllianceLeader) {
            if (isCoalitionDone) {
                coalitionBadge = "FRONT COMMITTED ✓";
                coalitionBadgeColor = "#10b981";
                coalitionRec = "Coalition negotiations resolved for this turn. Member contracts are locked.";
                coalitionTip = "Save capital and cabinet quotas for upcoming state election campaigns.";
            } else if (majorityGap <= 0) {
                coalitionBadge = "MAJORITY ALLIANCE ⚡";
                coalitionBadgeColor = "#38bdf8";
                coalitionRec = "Alliance controls " + totalAllianceSeats + " projected seats. Quotas are stable.";
                coalitionTip = "Confirm front strategy to lock in current federal aid bonuses.";
            } else if (cabinetLeft >= 2 && topRecruit != null) {
                coalitionBadge = "SLOTS AVAILABLE (" + cabinetLeft + " Cab / " + stateLeft + " MoS)";
                coalitionBadgeColor = "#38bdf8";
                coalitionRec = "Recruit " + (topRecruit.getPartyName() != null ? topRecruit.getPartyName() : topRecruit.getPartyKey().toUpperCase()) +
                               " (" + targetSeats + " Projected Seats). You have " + cabinetLeft + " Cabinet and " + stateLeft + " State minister slots available.";
                String bonus = currentFunds > 30 ? "₹2.5 Cr" : "₹1.0 Cr";
                coalitionTip = "Recommended Contract: 2 Cabinet Ministers, 3 State Ministers, " + bonus + " joining bonus.";
            } else {
                coalitionBadge = "QUOTA RESTRICTED";
                coalitionBadgeColor = "#f59e0b";
                coalitionRec = "Cabinet minister quota is nearly exhausted (" + cabinetLeft + " left). Do not over-promise beyond 20 Cabinet slots or coalition partners will breach contracts.";
                coalitionTip = "Click 'Confirm Front Strategy' to lock in existing partner bonuses without adding new liabilities.";
            }
        } else {
            coalitionBadge = "ALLIANCE MEMBER";
            coalitionBadgeColor = "#10b981";
            coalitionRec = "You are a constituent party of " + playerAlliance.getAllianceName() + ". Fulfill contracts to secure recurring federal transfers.";
            coalitionTip = "Confirm front strategy to receive seasonal aid and shared rally swing boosts.";
        }

        Map<String, Object> coalitionAction = new HashMap<>();
        coalitionAction.put("title", "Action 1: Coalition & Front Politics");
        coalitionAction.put("isDone", isCoalitionDone);
        coalitionAction.put("status", isCoalitionDone ? "COMPLETED" : "PENDING");
        coalitionAction.put("badge", coalitionBadge);
        coalitionAction.put("badgeColor", coalitionBadgeColor);
        coalitionAction.put("recommendation", coalitionRec);
        coalitionAction.put("actionTip", coalitionTip);
        coalitionAction.put("cabinetLeft", cabinetLeft);
        coalitionAction.put("stateLeft", stateLeft);
        coalitionAction.put("subTab", "coalition");
        if (topRecruit != null) {
            Map<String, Object> targetMap = new HashMap<>();
            targetMap.put("partyKey", topRecruit.getPartyKey());
            targetMap.put("partyName", topRecruit.getPartyName());
            targetMap.put("projectedSeats", targetSeats);
            coalitionAction.put("targetParty", targetMap);
        }

        // ── 6. DIRECTIVE 2: FINANCE & TREASURY GUIDANCE ─────────────────────────
        String financeRec;
        String financeTip;
        String financeBadge;
        String financeBadgeColor;
        String financePosture;

        if (isFinanceDone) {
            financeBadge = "CARD COMMITTED ✓";
            financeBadgeColor = "#10b981";
            financePosture = "COMMITTED";
            financeRec = "Finance card '" + game.getCommittedFinanceCard() + "' is committed for this turn.";
            financeTip = "Treasury adjustments and cadre morale changes will be finalized when ending the turn.";
        } else if (greedHeat >= 3 || currentCorruption > 35) {
            financePosture = "COOL_DOWN";
            financeBadge = "COOL DOWN REQUIRED ⚠️";
            financeBadgeColor = "#ef4444";
            financeRec = "High Corruption & Media Scrutiny (Heat " + greedHeat + "/4, Corruption " + currentCorruption + "%). Cadres are restless and journalists are probing corporate ties.";
            financeTip = "Select 'Grassroots Micro-Donation Drive' or 'Campus Union Collection'. Avoid corporate mega-cards to cool scrutiny heat.";
        } else if (currentFunds < 22.0) {
            financePosture = "CAPITAL_INFLOW";
            financeBadge = "CAPITAL INFLOW NEEDED 💰";
            financeBadgeColor = "#f59e0b";
            financeRec = "Treasury reserves are low (₹" + String.format(Locale.US, "%.1f", currentFunds) + " Cr). You need funds to finance state campaign pushes and building construction.";
            financeTip = "Select high-yield financing such as 'Corporate Dinner' or 'Diaspora Fundraiser' to inject ₹12-18 Cr into party reserves.";
        } else if (currentMorale < 55) {
            financePosture = "CADRE_MORALE";
            financeBadge = "BOOST MORALE 🚩";
            financeBadgeColor = "#ec4899";
            financeRec = "Cadre morale has dropped to " + currentMorale + "%. Low morale penalizes voting swings across all state battlegrounds.";
            financeTip = "Select worker-centric funding cards that offer morale bonuses and volunteer surges over raw cash.";
        } else {
            financePosture = "BALANCED";
            financeBadge = "STEADY EXPANSION ✓";
            financeBadgeColor = "#10b981";
            financeRec = "Treasury is stable at ₹" + String.format(Locale.US, "%.1f", currentFunds) + " Cr with low corruption (" + currentCorruption + "%).";
            financeTip = "Choose balanced strategy cards like 'Party Subscription Drive' or 'SME Chamber Summit' to steadily grow cadres and funds simultaneously.";
        }

        Map<String, Object> financeAction = new HashMap<>();
        financeAction.put("title", "Action 2: Treasury & Strategy Cards");
        financeAction.put("isDone", isFinanceDone);
        financeAction.put("status", isFinanceDone ? "COMPLETED" : "PENDING");
        financeAction.put("badge", financeBadge);
        financeAction.put("badgeColor", financeBadgeColor);
        financeAction.put("posture", financePosture);
        financeAction.put("recommendation", financeRec);
        financeAction.put("actionTip", financeTip);
        financeAction.put("subTab", "finance");

        // ── 7. DIRECTIVE 3: NATIONAL EVENTS & ISSUES GUIDANCE ───────────────────
        String eventsRec;
        String eventsTip;
        String eventsBadge;
        String eventsBadgeColor;

        // Identify primary rival party to target
        NationalPartyState topRival = null;
        int maxRivalSeats = -1;
        Set<String> alliedKeys = new HashSet<>();
        if (playerAlliance != null && playerAlliance.getMembers() != null) {
            for (NationalAllianceMember m : playerAlliance.getMembers()) {
                if (m.getPartyKey() != null) alliedKeys.add(m.getPartyKey().toUpperCase());
            }
        }
        alliedKeys.add(playerPartyKey.toUpperCase());

        for (NationalPartyState ps : game.getPartyStates()) {
            String pk = ps.getPartyKey() != null ? ps.getPartyKey().toUpperCase() : "";
            if (!alliedKeys.contains(pk)) {
                int s = (int) ps.getSeats();
                if (s > maxRivalSeats) {
                    maxRivalSeats = s;
                    topRival = ps;
                }
            }
        }

        String targetPartyTip;
        if (game.getTargetPartyKey() != null && !game.getTargetPartyKey().trim().isEmpty()) {
            targetPartyTip = "Offensive focused against " + game.getTargetPartyKey().toUpperCase() + ". Campaign actions will inflict cadre desertions and vote split decay upon them.";
        } else if (topRival != null) {
            targetPartyTip = "Target " + topRival.getPartyName() + " (" + topRival.getPartyKey().toUpperCase() + ", " + topRival.getSeats() + " seats) to inflict morale and vote split decay on your main rival.";
        } else {
            targetPartyTip = "Select a key rival party to focus your campaign theme offensive.";
        }

        String mediaSocialTip;
        if (game.isMediaSocialCommitted()) {
            double totalSp = 0.0;
            if (game.getMediaSocialSpend() != null) {
                for (Double v : game.getMediaSocialSpend().values()) {
                    if (v != null) totalSp += v;
                }
            }
            mediaSocialTip = "Digital Media & Social Campaign committed (₹" + String.format(Locale.US, "%.1f", totalSp) + " Cr). Viral breakthrough roll and cadre conversions will resolve at season end.";
        } else if (currentFunds < 18.0) {
            mediaSocialTip = "Treasury is tight (₹" + String.format(Locale.US, "%.1f", currentFunds) + " Cr). Allocate ₹1.0 - ₹2.0 Cr in WhatsApp & Social Ads to avoid cash burn.";
        } else {
            mediaSocialTip = "Healthy reserves. Allocate ₹2.5 - ₹3.5 Cr across Influencers, Podcasts & WhatsApp to maximize viral breakthrough odds (up to 45%) without exceeding the ₹6.0 Cr scrutiny limit.";
        }

        boolean isPlayerRuling = game.isPlayerInPower();

        if (pendingEventsCount > 0) {
            eventsBadge = pendingEventsCount + " PENDING CRISES ⚠️";
            eventsBadgeColor = "#ef4444";
            eventsRec = pendingEventsCount + " National Event Reaction" + (pendingEventsCount > 1 ? "s are" : " is") + " awaiting your response. Failure to respond cedes national news narrative.";
            eventsTip = "Choose options that maximize Public Support and Cadre Morale while keeping Corruption Risk under 20%. Reject bribe or kickback options.";
        } else if (game.getActiveThemeKey() != null && !game.getActiveThemeKey().isEmpty()) {
            if (isThemeActionDone) {
                eventsBadge = "THEME ACTION ACTIVE ✓";
                eventsBadgeColor = "#10b981";
                eventsRec = isPlayerRuling
                    ? "Governance Blitz action committed! Direct delivery consolidated for this turn."
                    : "Campaign theme action mobilized! Anti-regime offensive executed against target rival.";
                eventsTip = "Conviction streak maintained (+15% national rally swing bonus active).";
            } else {
                eventsBadge = isPlayerRuling ? "GOVERNANCE READY 🏛️" : "THEME READY 📢";
                eventsBadgeColor = "#38bdf8";
                eventsRec = isPlayerRuling
                    ? "Ruling Coalition: Deploy Governance Blitz (Highways / DBT Welfare) to consolidate federal dominance."
                    : "Opposition Front: Mobilize campaign agitations against " + (topRival != null ? topRival.getPartyName() : "the ruling alliance") + " to erode their voter base.";
                eventsTip = "Trigger the theme action to preserve your conviction streak and inflict damage on your chosen target.";
            }
        } else {
            eventsBadge = "HORIZON STABLE ✓";
            eventsBadgeColor = "#10b981";
            eventsRec = isPlayerRuling
                ? "No urgent crises. Deploy governance blitz and allocate social media blitz to consolidate national lead."
                : "Public opinion is stable. Select an agitation theme and allocate digital media to recruit cadres.";
            eventsTip = "Use this window to launch digital media blitz (podcasts & WhatsApp) and push volunteer recruitment.";
        }

        Map<String, Object> eventsAction = new HashMap<>();
        eventsAction.put("title", "Action 3: National Crises, Themes & Social Media");
        eventsAction.put("isDone", isEventsDone);
        eventsAction.put("status", isEventsDone ? "COMPLETED" : "PENDING");
        eventsAction.put("badge", eventsBadge);
        eventsAction.put("badgeColor", eventsBadgeColor);
        eventsAction.put("pendingCount", pendingEventsCount);
        eventsAction.put("recommendation", eventsRec);
        eventsAction.put("actionTip", eventsTip);
        eventsAction.put("targetPartyTip", targetPartyTip);
        eventsAction.put("mediaSocialTip", mediaSocialTip);
        eventsAction.put("subTab", "events");

        // ── 8. DIRECTIVE 4: BATTLEGROUND STATE OPERATIONS & DOSSIER ─────────────
        List<Map<String, Object>> rankedStates = new ArrayList<>();

        for (NationalStateOperationState st : eligibleStates) {
            int turns = st.getTurnsToElection();
            int seats = st.getTotalLokSabhaSeats() > 0 ? st.getTotalLokSabhaSeats() : 20;
            double funds = st.getStateFunds();
            int workers = st.getStateWorkers();

            int urgencyScore = 0;
            String urgencyBadge = "NORMAL 🗓️";
            String urgencyColor = "#94a3b8";

            if (turns <= 3) {
                urgencyScore += 100;
                urgencyBadge = "FINAL SPRINT ⚡";
                urgencyColor = "#ef4444";
            } else if (turns <= 6) {
                urgencyScore += 60;
                urgencyBadge = "CAMPAIGN ⚔️";
                urgencyColor = "#f59e0b";
            } else if (turns <= 12) {
                urgencyScore += 30;
                urgencyBadge = "PRE-ELECTION 🗓️";
                urgencyColor = "#38bdf8";
            }
            urgencyScore += (int) (seats * 0.8);
            if (funds < 1.5) urgencyScore += 15;
            if (workers < 10000) urgencyScore += 10;

            // Resource transfer calculation
            double safeHqReserve = 15.0;
            double availableHqFunds = Math.max(0.0, currentFunds - safeHqReserve);
            double recTransferFunds = 0.0;
            if (funds < 1.5) {
                recTransferFunds = Math.min(3.5, Math.max(1.5, availableHqFunds * 0.3));
            } else if (funds < 3.0 && turns <= 6) {
                recTransferFunds = Math.min(2.0, availableHqFunds * 0.2);
            }
            recTransferFunds = Math.round(recTransferFunds * 10.0) / 10.0;

            int recTransferWorkers = 0;
            if (workers < 10000) {
                recTransferWorkers = Math.min(15000, (int) (currentWorkers * 0.2));
            } else if (workers < 20000 && turns <= 6) {
                recTransferWorkers = Math.min(8000, (int) (currentWorkers * 0.1));
            }

            // Infrastructure Recommendation
            Map<String, Object> recInfra = new HashMap<>();
            boolean hasHq = st.getBuildings() != null && st.getBuildings().getOrDefault("state_party_hq", 0) > 0;
            String sc = st.getStateCode() != null ? st.getStateCode().toUpperCase() : "";

            if (!hasHq) {
                recInfra.put("key", "state_party_hq");
                recInfra.put("name", "State Party HQ");
                recInfra.put("cost", 1.0);
                recInfra.put("yield", "+₹0.15 Cr/turn, +1.0% Baseline Support");
                recInfra.put("reason", "Establishes permanent party secretariat and recurring revenue in state capital.");
            } else if (sc.equals("UP") || sc.equals("BR") || sc.equals("RJ")) {
                recInfra.put("key", "farmers_rural_wing");
                recInfra.put("name", "Farmers' & Rural Wing");
                recInfra.put("cost", 0.25);
                recInfra.put("yield", "+2.5% Rural Swing, +150 Cadres/turn");
                recInfra.put("reason", "Critical for agrarian heartland voting base and Kisan sabha mobilization.");
            } else if (sc.equals("MH") || sc.equals("WB") || sc.equals("TN")) {
                recInfra.put("key", "labour_union_liaison_office");
                recInfra.put("name", "Labour Union Liaison Office");
                recInfra.put("cost", 0.30);
                recInfra.put("yield", "+2.5% Urban/Labour Swing, +200 Cadres/turn");
                recInfra.put("reason", "Crucial for capturing industrial belt and organized working-class voters.");
            } else {
                recInfra.put("key", "regional_divisional_office");
                recInfra.put("name", "Regional Divisional Office");
                recInfra.put("cost", 0.50);
                recInfra.put("yield", "+₹0.08 Cr/turn, +0.6% State Support");
                recInfra.put("reason", "Expands organizational presence across secondary divisional centers.");
            }

            // Tactical Action & Issue Stance Recommendation
            Map<String, Object> recAction = new HashMap<>();
            String stance;
            if (sc.equals("UP")) {
                recAction.put("actionKey", "agitation");
                recAction.put("actionName", "Sugarcane Arrears & Rural Distress Agitation");
                recAction.put("cost", "₹0.6 Cr + 4,000 Workers");
                recAction.put("reason", "Mobilizes western and central UP farmer belts, generating high turnout swing.");
                stance = "Champion rural debt relief, timely cane dues payment, and expansion of youth employment exams.";
            } else if (sc.equals("BR")) {
                recAction.put("actionKey", "rally");
                recAction.put("actionName", "Statewide Employment Adhikar Rally");
                recAction.put("cost", "₹0.5 Cr + 3,500 Workers");
                recAction.put("reason", "Resonates powerfully with youth across Seemanchal, Magadh, and Mithila.");
                stance = "Focus aggressively on teacher recruitment transparency, flood compensation, and stopping distress migration.";
            } else if (sc.equals("MH")) {
                recAction.put("actionKey", "padayatra");
                recAction.put("actionName", "Vidarbha-Marathwada Irrigation & Farmers Padayatra");
                recAction.put("cost", "₹0.7 Cr + 5,000 Workers");
                recAction.put("reason", "Builds enduring cadre loyalty across agrarian distress drought belts.");
                stance = "Balance Mumbai-MMR infrastructure modernization with agrarian MSP guarantees across Vidarbha.";
            } else if (sc.equals("WB")) {
                recAction.put("actionKey", "dharna");
                recAction.put("actionName", "Civil Rights & Industrial Revival Dharna");
                recAction.put("cost", "₹0.4 Cr + 2,500 Workers");
                recAction.put("reason", "Penetrates municipal wards and tea garden belts with minimal capital overhead.");
                stance = "Advocate revival of manufacturing hubs, jute mill rehabilitation, and protection of local cultural identity.";
            } else if (sc.equals("RJ")) {
                recAction.put("actionKey", "rally");
                recAction.put("actionName", "Eastern Rajasthan Canal Project (ERCP) Kisan Rally");
                recAction.put("cost", "₹0.5 Cr + 3,000 Workers");
                recAction.put("reason", "Water security is the definitive swing issue across 13 eastern districts.");
                stance = "Demands national project status for ERCP drinking water networks and rural subsidy protection.";
            } else if (sc.equals("AS")) {
                recAction.put("actionKey", "padayatra");
                recAction.put("actionName", "Brahmaputra Flood Relief & Tea Tribe Padayatra");
                recAction.put("cost", "₹0.4 Cr + 2,000 Workers");
                recAction.put("reason", "Deepens grassroots presence across upper Assam and Barak Valley.");
                stance = "Emphasize permanent flood embankment engineering and fair daily wage revisions for tea workers.";
            } else if (sc.equals("TN")) {
                recAction.put("actionKey", "agitation");
                recAction.put("actionName", "Federal Autonomy & Cauvery Rights Campaign");
                recAction.put("cost", "₹0.6 Cr + 4,000 Workers");
                recAction.put("reason", "Taps directly into state pride, cooperative federalism, and delta agriculture.");
                stance = "Strong defense of state legislative rights, welfare scheme preservation, and industrial manufacturing incentives.";
            } else {
                recAction.put("actionKey", "rally");
                recAction.put("actionName", "Constituency Workers Conclave & Mass Rally");
                recAction.put("cost", "₹0.4 Cr + 2,500 Workers");
                recAction.put("reason", "Mobilizes existing sympathizers and tests local ward organizational preparedness.");
                stance = "Highlight regional economic development, clean governance, and price stabilization.";
            }

            String turnStatus = st.isDoneThisTurn() ? "DONE" : (st.isSkippedThisTurn() ? "SKIPPED" : "PENDING");

            Map<String, Object> stateItem = new HashMap<>();
            stateItem.put("stateCode", st.getStateCode());
            stateItem.put("stateName", st.getStateName() != null ? st.getStateName() : st.getStateCode());
            stateItem.put("totalLokSabhaSeats", seats);
            stateItem.put("electionPhase", st.getElectionPhase());
            stateItem.put("turnsToElection", turns);
            stateItem.put("stateFunds", funds);
            stateItem.put("stateWorkers", workers);
            stateItem.put("turnStatus", turnStatus);
            stateItem.put("urgencyScore", urgencyScore);
            stateItem.put("urgencyBadge", urgencyBadge);
            stateItem.put("urgencyColor", urgencyColor);
            stateItem.put("recTransferFunds", recTransferFunds);
            stateItem.put("recTransferWorkers", recTransferWorkers);
            stateItem.put("recInfra", recInfra);
            stateItem.put("recAction", recAction);
            stateItem.put("politicalStance", stance);

            rankedStates.add(stateItem);
        }

        // Sort states by urgencyScore descending
        rankedStates.sort((a, b) -> ((Integer) b.get("urgencyScore")).compareTo((Integer) a.get("urgencyScore")));

        Map<String, Object> topState = !rankedStates.isEmpty() ? rankedStates.get(0) : null;
        String statesBadge;
        String statesBadgeColor;
        String statesRec;
        String statesTip;

        if (totalStates == 0) {
            statesBadge = "NO ACTIVE THEATERS 🔒";
            statesBadgeColor = "#94a3b8";
            statesRec = "No regional state operations are active for your party. Enter into alliances under Action 1 to unlock regional state campaigns.";
            statesTip = !lockedStates.isEmpty()
                    ? "Form alliances with state parties (e.g. DMK, AIADMK, AITC, AGP) to unlock regional battlegrounds and Lok Sabha seats."
                    : "Form regional alliances under Action 1 to unlock battleground states.";
        } else if (allStatesCompleted) {
            statesBadge = "ALL STATES RESOLVED ✓";
            statesBadgeColor = "#10b981";
            statesRec = "All " + totalStates + " active state operations have been addressed for this turn.";
            statesTip = "Review national standing or proceed to end the turn.";
        } else if (hasNotPlayedAnyStates) {
            statesBadge = "NO STATES PLAYED ⚠️";
            statesBadgeColor = "#ef4444";
            statesRec = "CRITICAL: You have not taken action in any state this turn! Rivals will erode your base uncontested.";
            statesTip = topState != null
                    ? "Immediately open " + topState.get("stateName") + " (" + topState.get("totalLokSabhaSeats") + " Lok Sabha Seats). Transfer ₹" +
                      topState.get("recTransferFunds") + " Cr and deploy " + ((Map<?, ?>) topState.get("recAction")).get("actionName") + "."
                    : "Open your highest priority state in State Operations.";
        } else {
            int pendingCount = totalStates - completedStatesCount;
            statesBadge = pendingCount + " STATES PENDING";
            statesBadgeColor = "#f59e0b";
            statesRec = playedStatesCount + " states mobilized, " + pendingCount + " states remaining.";
            statesTip = topState != null
                    ? "Focus on " + topState.get("stateName") + " (" + topState.get("urgencyBadge") + "). Build " +
                      ((Map<?, ?>) topState.get("recInfra")).get("name") + " and transfer funds."
                    : "Complete remaining state directives.";
        }

        Map<String, Object> statesAction = new HashMap<>();
        statesAction.put("title", "Action 4: Battleground State Ground Wars");
        statesAction.put("isDone", allStatesCompleted);
        statesAction.put("status", allStatesCompleted ? "COMPLETED" : "PENDING");
        statesAction.put("badge", statesBadge);
        statesAction.put("badgeColor", statesBadgeColor);
        statesAction.put("unplayedCount", totalStates - completedStatesCount);
        statesAction.put("hasNotPlayedAnyStates", hasNotPlayedAnyStates);
        statesAction.put("recommendation", statesRec);
        statesAction.put("actionTip", statesTip);
        statesAction.put("topStateCode", topState != null ? topState.get("stateCode") : null);
        statesAction.put("subTab", "states");

        // ── 9. ASSEMBLE FULL HINT PAYLOAD ───────────────────────────────────────
        Map<String, Object> actions = new HashMap<>();
        actions.put("coalition", coalitionAction);
        actions.put("finance", financeAction);
        actions.put("events", eventsAction);
        actions.put("states", statesAction);

        Map<String, Object> result = new HashMap<>();
        result.put("summary", summary);
        result.put("actions", actions);
        result.put("rankedStates", rankedStates);
        result.put("urgentWarnings", urgentWarnings);

        return result;
    }
}
