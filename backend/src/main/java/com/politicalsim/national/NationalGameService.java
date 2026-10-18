package com.politicalsim.national;

import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;
import java.util.*;
import java.time.Instant;

@Service
public class NationalGameService {

    @Autowired
    private NationalGameRepository repository;

    @Autowired
    private com.politicalsim.content.NationalEventRepository nationalEventRepository;

    @Autowired
    private com.politicalsim.content.NationalThemeRepository nationalThemeRepository;

    @Autowired
    private com.politicalsim.content.NewsDefinitionRepository newsDefinitionRepository;

    @Autowired
    private com.politicalsim.content.StateInfrastructureDefinitionRepository infrastructureRepository;

    @Autowired
    private com.politicalsim.content.NationalConfigRepository nationalConfigRepository;

    @Autowired
    private NationalStrategicHintService hintService;

    public void refreshStrategicHints(NationalGame game) {
        if (game != null && hintService != null) {
            try {
                game.setStrategicHints(hintService.generateStrategicHints(game));
            } catch (Exception e) {
                // Ignore hint generation failures gracefully
            }
        }
    }

    public Map<String, Object> getStrategicHints(String gameId) {
        NationalGame game = findGame(gameId);
        normalizeGameAllianceStates(game);
        if (hintService != null) {
            Map<String, Object> hints = hintService.generateStrategicHints(game);
            game.setStrategicHints(hints);
            return hints;
        }
        return Collections.emptyMap();
    }

    private String resolveTargetName(NationalPartyState target) {
        if (target == null) return "Party";
        if (target.getPartyName() != null && !target.getPartyName().trim().isEmpty()) {
            return target.getPartyName().trim();
        }
        if (target.getShortName() != null && !target.getShortName().trim().isEmpty()) {
            return target.getShortName().trim();
        }
        if (target.getPartyKey() != null && !target.getPartyKey().trim().isEmpty()) {
            return target.getPartyKey().toUpperCase().trim();
        }
        return "Party";
    }

    private NationalGame findGame(String gameId) {
        if (gameId == null || gameId.trim().isEmpty() || "undefined".equalsIgnoreCase(gameId) || "null".equalsIgnoreCase(gameId)) {
            return repository.findAll().stream()
                .filter(g -> "ACTIVE".equals(g.getStatus()))
                .findFirst()
                .orElseThrow(() -> new RuntimeException("Active national game not found"));
        }
        return repository.findById(gameId)
            .or(() -> repository.findByUserIdAndStatus(gameId, "ACTIVE"))
            .or(() -> repository.findByUserId(gameId))
            .orElseGet(() -> repository.findAll().stream()
                .filter(g -> "ACTIVE".equals(g.getStatus()))
                .findFirst()
                .orElseThrow(() -> new RuntimeException("Game not found with id: " + gameId)));
    }

    public NationalGame startGame(String userId, int era, String partyKey, List<Map<String, Object>> configParties, List<Map<String, Object>> configStateSeatData) {
        // Archive any previous active games for this user so a brand new clean game is initialized
        List<NationalGame> existingGames = repository.findAllByUserId(userId);
        if (existingGames != null) {
            for (NationalGame oldGame : existingGames) {
                if ("ACTIVE".equals(oldGame.getStatus())) {
                    oldGame.setStatus("ARCHIVED");
                    repository.save(oldGame);
                }
            }
        }
        
        NationalGame game = new NationalGame();
        game.setUserId(userId);
        game.setEra(era);
        game.setPartyKey(partyKey);
        game.setCurrentSeason(1);
        game.setStatus("ACTIVE");
        game.setAlliances(new ArrayList<>());
        game.setPendingRequests(new ArrayList<>());
        game.setCommittedFinanceCard(null);
        game.setMegaFinanceHeat(0);
        game.setVisibleFinanceCardIds(NationalFinanceCardDefinition.pickRandomVisibleCardIds(6));
        game.setRulingAllianceKey("NDA");
        game.setCurrentSeasonEventIds(new ArrayList<>());
        game.setResolvedEventReactions(new HashMap<>());
        game.setActiveThemeKey(null);
        game.setActiveThemeAction(null);
        game.setThemePersistenceStreak(0);
        game.setLastThemeKey(null);
        game.setCreatedAt(Instant.now().toString());
        
        List<NationalPartyState> states = new ArrayList<>();
        
        for (Map<String, Object> configParty : configParties) {
            String pKey = (String) configParty.get("partyKey");
            
            NationalPartyState state = new NationalPartyState();
            state.setPartyKey(pKey);
            String pName = null;
            if (configParty.containsKey("name") && configParty.get("name") instanceof String) {
                pName = (String) configParty.get("name");
            } else if (configParty.containsKey("partyName") && configParty.get("partyName") instanceof String) {
                pName = (String) configParty.get("partyName");
            }
            if (pName == null || pName.trim().isEmpty() || "null".equalsIgnoreCase(pName.trim())) {
                pName = (String) configParty.get("shortName");
            }
            if (pName == null || pName.trim().isEmpty() || "null".equalsIgnoreCase(pName.trim())) {
                pName = pKey != null ? pKey.toUpperCase() : "Party";
            }
            state.setPartyName(pName);
            state.setShortName((String) configParty.get("shortName"));
            state.setColor((String) configParty.get("color"));
            state.setIdeology((String) configParty.get("ideology"));
            
            int seats = 0;
            if (configStateSeatData != null) {
                for (Map<String, Object> stateSeat : configStateSeatData) {
                    Object initSeatsObj = stateSeat.get("initialSeats");
                    if (initSeatsObj instanceof Map) {
                        Map<String, Object> initSeatsMap = (Map<String, Object>) initSeatsObj;
                        Object pSeats = initSeatsMap.get(pKey);
                        if (pSeats instanceof Number) {
                            seats += ((Number) pSeats).intValue();
                        }
                    } else if (pKey.equals(stateSeat.get("partyKey"))) {
                        Object initSeats = stateSeat.get("initialSeats");
                        if (initSeats instanceof Number) {
                            seats += ((Number) initSeats).intValue();
                        }
                    }
                }
            }
            state.setSeats(seats);
            
            double partyFunds = 5.0;
            if (configParty.containsKey("declaredFundsCr") && configParty.get("declaredFundsCr") instanceof Number) {
                partyFunds = ((Number) configParty.get("declaredFundsCr")).doubleValue();
            } else if (configParty.containsKey("fundsCr") && configParty.get("fundsCr") instanceof Number) {
                partyFunds = ((Number) configParty.get("fundsCr")).doubleValue();
            } else if (configParty.containsKey("initialFunds") && configParty.get("initialFunds") instanceof Number) {
                partyFunds = ((Number) configParty.get("initialFunds")).doubleValue();
            } else if (configParty.containsKey("funds") && configParty.get("funds") instanceof Number) {
                partyFunds = ((Number) configParty.get("funds")).doubleValue();
            } else if (seats > 0) {
                partyFunds = Math.max(1.0, Math.round((seats * 0.5) * 10.0) / 10.0);
            }
            state.setFunds(partyFunds);
            state.setStartingFunds(partyFunds);
            
            int workers = 50000;
            if (configParty.containsKey("workers") && configParty.get("workers") instanceof Number) {
                workers = ((Number) configParty.get("workers")).intValue();
            }
            state.setWorkers(workers);
            
            int volunteers = 15000;
            if (configParty.containsKey("volunteers") && configParty.get("volunteers") instanceof Number) {
                volunteers = ((Number) configParty.get("volunteers")).intValue();
            }
            state.setVolunteers(volunteers);
            
            int donors = 1000;
            if (configParty.containsKey("donors") && configParty.get("donors") instanceof Number) {
                donors = ((Number) configParty.get("donors")).intValue();
            }
            state.setDonors(donors);
            
            int morale = 70;
            if (configParty.containsKey("initialMorale")) {
                Object mm = configParty.get("initialMorale");
                if (mm instanceof Number) {
                    morale = ((Number) mm).intValue();
                }
            } else if (configParty.containsKey("initialContent")) {
                Object mc = configParty.get("initialContent");
                if (mc instanceof Number) {
                    morale = ((Number) mc).intValue();
                }
            }
            state.setMorale(morale);
            
            boolean isPlayer = pKey.equals(partyKey);
            state.setPlayerParty(isPlayer);
            if (isPlayer) {
                game.setPartyName(state.getPartyName());
                game.setPartyShortName(state.getShortName());
                game.setPartyColor(state.getColor());
                game.setPlayerFunds(state.getFunds());
                game.setPlayerCorruption(0);
            }
            
            state.setCorruption(0);
            
            String initAll = (String) configParty.get("initialAllianceKey");
            state.setPreSeededAllianceKey(initAll);
            if (initAll != null && !initAll.equalsIgnoreCase("UNALIGNED") && !initAll.equalsIgnoreCase("INDEPENDENT")) {
                state.setCurrentAllianceId(initAll);
            } else {
                state.setCurrentAllianceId(null);
            }
            state.setPreSeededAllianceLeader(false);
            
            states.add(state);
        }
        
        game.setPartyStates(states);
        game.setRulingAllianceKey(game.determineRulingAllianceKey());

        List<com.politicalsim.content.NationalEvent> initEvts = nationalEventRepository.findByEraAndSeason(game.getEra(), 1);
        if (initEvts == null || initEvts.isEmpty()) {
            initEvts = nationalEventRepository.findByEra(game.getEra());
        }
        if (initEvts != null) {
            List<String> evtIds = new ArrayList<>();
            for (com.politicalsim.content.NationalEvent e : initEvts) {
                evtIds.add(e.getId());
            }
            game.setCurrentSeasonEventIds(evtIds);
        }
        initializeStateOperations(game);

        game.setUpdatedAt(Instant.now().toString());
        return repository.save(game);
    }

    public NationalGame createAlliance(String gameId, String allianceName, String color) {
        NationalGame game = findGame(gameId);
        
        NationalAlliance existing = game.findPlayerAlliance(game.getPartyKey());
        if (existing != null) {
            throw new RuntimeException("Player already leads an active alliance.");
        }
        
        NationalPartyState playerState = game.findPartyState(game.getPartyKey());
        
        NationalAlliance alliance = new NationalAlliance();
        alliance.setAllianceId(UUID.randomUUID().toString());
        alliance.setAllianceName(allianceName);
        alliance.setColor(color != null && !color.isEmpty() ? color : "#38bdf8");
        alliance.setLeaderPartyKey(game.getPartyKey());
        alliance.setFormedAtSeason(game.getCurrentSeason());
        double seatsCount = playerState != null ? playerState.getSeats() : 0.0;
        alliance.setFederalAidPerSeason(0.0);
        alliance.setAllianceFundBalance(0.0);
        
        // Add player party as first constituent member of the alliance
        if (playerState != null) {
            NationalAllianceMember leaderMember = new NationalAllianceMember();
            leaderMember.setPartyKey(playerState.getPartyKey());
            leaderMember.setJoinedAtSeason(game.getCurrentSeason());
            leaderMember.setSeats(playerState.getSeats());
            leaderMember.setMorale(playerState.getMorale());
            
            NationalContract leaderContract = new NationalContract();
            leaderContract.setJoiningBonus(0);
            leaderContract.setRecurringPerSeason(0);
            leaderContract.setCabinetMinistersPromised(0);
            leaderContract.setStateMinistersPromised(0);
            leaderContract.setDurationSeasons(-1);
            leaderContract.setBroken(false);
            leaderMember.setContract(leaderContract);
            
            alliance.getMembers().add(leaderMember);
            
            // The party RETAINS its funds upon joining/forming a coalition!
            // Do NOT zero out playerState.funds or game.playerFunds.
            playerState.setCurrentAllianceId(alliance.getAllianceId());
        }
        
        String leaderName = playerState != null ? playerState.getPartyName() : game.getPartyKey();
        double partyFunds = playerState != null ? playerState.getFunds() : 0.0;
        logEntry(alliance, game.getCurrentSeason(), "ALLIANCE_FORMED", "Alliance " + allianceName + " formed by " + leaderName + " (" + (int)seatsCount + " seats). Party retained ₹" + String.format("%.1f", partyFunds) + " Cr in party treasury. Front operates on direct party funds.");
        
        game.getAlliances().add(alliance);
        
        game.setUpdatedAt(Instant.now().toString());
        return repository.save(game);
    }

    public NationalCoalitionActionResponse inviteParty(String gameId, String targetPartyKey, NationalContract contract) {
        NationalGame game = findGame(gameId);
        NationalAlliance alliance = game.findPlayerAlliance(game.getPartyKey());
        if (alliance == null) {
            return NationalCoalitionActionResponse.refusal(
                CoalitionResponseCode.REFUSED_NO_ACTIVE_ALLIANCE,
                "You must first create an alliance front before sending coalition invitations.",
                game
            );
        }

        NationalPartyState target = game.findPartyState(targetPartyKey);
        NationalPartyState player = game.findPartyState(game.getPartyKey());

        if (target == null) {
            return NationalCoalitionActionResponse.refusal(
                CoalitionResponseCode.ERROR,
                "Target party '" + targetPartyKey + "' not found in the current game.",
                game
            );
        }

        // Recurring per season is removed from the player-facing UI — always 0
        contract.setRecurringPerSeason(0);

        // Record the invite attempt in the request log
        String targetName = resolveTargetName(target);
        NationalCoalitionRequest req = new NationalCoalitionRequest();
        req.setRequestId(UUID.randomUUID().toString());
        req.setDirection("OUTGOING");
        req.setFromPartyKey(game.getPartyKey());
        req.setToAllianceId(alliance.getAllianceId());
        req.setOfferedJoiningBonus(contract.getJoiningBonus());
        req.setRequestedJoiningBonus(contract.getJoiningBonus());
        req.setRequestedRecurringPerSeason(0);
        req.setRequestedCabinetMinisters(contract.getCabinetMinistersPromised());
        req.setRequestedStateMinisters(contract.getStateMinistersPromised());
        req.setStatus("PENDING");
        req.setCreatedAtSeason(game.getCurrentSeason());
        game.getPendingRequests().add(req);
        logEntry(alliance, game.getCurrentSeason(), "INVITE_SENT", "Invite sent to " + targetName);

        // Run the full Coalition Simulation Engine
        NationalCoalitionActionResponse engineResult = evaluateCoalitionInvite(target, player, contract, alliance, game);

        if (engineResult == null) {
            // null = ACCEPT
            req.setStatus("ACCEPTED");

            NationalAllianceMember member = new NationalAllianceMember();
            member.setPartyKey(targetPartyKey);
            member.setJoinedAtSeason(game.getCurrentSeason());
            member.setSeats(target.getSeats());
            member.setMorale(target.getMorale());
            member.setContract(contract);

            alliance.getMembers().add(member);
            alliance.setTotalCabinetPromised(alliance.getTotalCabinetPromised() + contract.getCabinetMinistersPromised());
            alliance.setTotalStatePromised(alliance.getTotalStatePromised() + contract.getStateMinistersPromised());

            // Joining bonus paid directly from player party funds (alliance has no separate funds)
            if (player != null && contract.getJoiningBonus() > 0) {
                player.setFunds(Math.max(0.0, Math.round((player.getFunds() - contract.getJoiningBonus()) * 10.0) / 10.0));
                game.setPlayerFunds(player.getFunds());
            }
            if (target != null && contract.getJoiningBonus() > 0) {
                target.setFunds(Math.round((target.getFunds() + contract.getJoiningBonus()) * 10.0) / 10.0);
            }
            target.setCurrentAllianceId(alliance.getAllianceId());

            String logMsg = targetName + " joined the alliance with ₹"
                + String.format("%.1f", contract.getJoiningBonus()) + " Cr joining bonus paid from party treasury, "
                + contract.getCabinetMinistersPromised() + " Cabinet post(s), "
                + contract.getStateMinistersPromised() + " State post(s).";
            logEntry(alliance, game.getCurrentSeason(), "PARTY_JOINED", logMsg);

            game.setUpdatedAt(Instant.now().toString());
            NationalGame saved = repository.save(game);
            return NationalCoalitionActionResponse.success(
                CoalitionResponseCode.ACCEPTED,
                "✅ " + targetName + " has accepted your coalition invitation and formally joined " + alliance.getAllianceName() + "!",
                saved
            );
        } else if (engineResult.getResponseCode() == CoalitionResponseCode.COUNTER_PROPOSAL) {
            req.setStatus("COUNTER");
            target.setMorale(Math.max(0, target.getMorale() - 2)); // slight morale dip for negotiating
            logEntry(alliance, game.getCurrentSeason(), "COUNTER_RECEIVED",
                targetName + " sent a counter proposal.");
            game.setUpdatedAt(Instant.now().toString());
            engineResult.setGame(repository.save(game));
            return engineResult;
        } else {
            req.setStatus("REJECTED");
            target.setMorale(Math.max(0, target.getMorale() - 5)); // morale dip for being rejected
            logEntry(alliance, game.getCurrentSeason(), "INVITE_REJECTED",
                targetName + " rejected the coalition invite.");
            game.setUpdatedAt(Instant.now().toString());
            engineResult.setGame(repository.save(game));
            return engineResult;
        }
    }
    
    // ─────────────────────────────────────────────────────────────────────
    // COALITION SIMULATION ENGINE  (v2)
    // ─────────────────────────────────────────────────────────────────────

    /** Master entry point — returns a full NationalCoalitionActionResponse */
    private NationalCoalitionActionResponse evaluateCoalitionInvite(
            NationalPartyState target, NationalPartyState inviter,
            NationalContract contract, NationalAlliance alliance,
            NationalGame game) {

        String targetName = resolveTargetName(target);

        // ── STEP 1: Hard Gate Checks ──────────────────────────────────────
        if (target != null) {
            String ca = target.getCurrentAllianceId();
            if (ca != null && !ca.equalsIgnoreCase("UNALIGNED") && !ca.equalsIgnoreCase("INDEPENDENT")) {
                return NationalCoalitionActionResponse.refusal(
                    CoalitionResponseCode.REFUSED_ALREADY_IN_ALLIANCE,
                    targetName + " is already part of another coalition front and cannot be invited at this time.",
                    game
                );
            }
        }
        if (alliance != null && (alliance.getTotalCabinetPromised() + contract.getCabinetMinistersPromised()) > 20) {
            return NationalCoalitionActionResponse.refusal(
                CoalitionResponseCode.REFUSED_CABINET_CAP_EXCEEDED,
                "Your alliance has already promised " + alliance.getTotalCabinetPromised() + " Cabinet posts. You cannot offer more without first removing a current member.",
                game
            );
        }
        if (alliance != null && (alliance.getTotalStatePromised() + contract.getStateMinistersPromised()) > 50) {
            return NationalCoalitionActionResponse.refusal(
                CoalitionResponseCode.REFUSED_STATE_MINISTER_CAP_EXCEEDED,
                "You've already committed " + alliance.getTotalStatePromised() + " State Minister posts. Reduce existing allocations before making new offers.",
                game
            );
        }
        if (inviter != null && inviter.getFunds() < contract.getJoiningBonus()) {
            return NationalCoalitionActionResponse.refusal(
                CoalitionResponseCode.REFUSED_INSUFFICIENT_FUNDS,
                "Your party treasury only has ₹" + String.format("%.1f", inviter.getFunds()) + " Cr — not enough to pay the ₹" + String.format("%.1f", contract.getJoiningBonus()) + " Cr joining bonus you offered.",
                game
            );
        }

        // ── STEP 2: Compute individual scores ─────────────────────────────
        int ideologyScore      = computeIdeologyScore(inviter, target);
        int seatScore          = computeSeatScore(alliance, game, target);
        int coalMoraleScore    = computeCoalitionMoraleScore(alliance, game);
        int targetMoraleScore  = computeTargetMoraleScore(target);
        int ministerScore      = computeMinisterScore(contract);
        int financialScore     = computeJoiningBonusScore(contract, target);
        int desperationBonus   = computeDesperationBonus(target, contract);
        int loyaltyPenalty     = computeLoyaltyPenalty(target);

        int totalScore = ideologyScore + seatScore + coalMoraleScore + targetMoraleScore
                       + ministerScore + financialScore + desperationBonus + loyaltyPenalty;

        // ── STEP 3: Decision ───────────────────────────────────────────────
        NationalContract demanded = buildCounterProposal(new NationalContract(), target);
        boolean meetsDemands = contract.getJoiningBonus() >= (demanded.getJoiningBonus() - 0.05)
                && contract.getCabinetMinistersPromised() >= demanded.getCabinetMinistersPromised()
                && contract.getStateMinistersPromised() >= demanded.getStateMinistersPromised();

        if (loyaltyPenalty < 0) {
            CoalitionResponseCode primaryCode = CoalitionResponseCode.REFUSED_LOYALTY_BOND;
            String rejectMsg = buildRefusalMessage(targetName, primaryCode, contract, target, alliance, game);
            return NationalCoalitionActionResponse.refusal(primaryCode, rejectMsg, game);
        }

        // Accept if natural alignment/offer is decisive (>= 60) OR if player meets the party's counter-proposal demands!
        if (totalScore >= 60 || meetsDemands) {
            // ACCEPT
            return null; // signals caller to proceed with acceptance
        }

        // Determine the dominant reason for the score being low
        CoalitionResponseCode primaryCode = detectPrimaryRefusalCode(
            ideologyScore, seatScore, targetMoraleScore, totalScore, loyaltyPenalty,
            target, contract, alliance, game);

        // If the party is open to negotiations, issue the counter proposal
        if (totalScore >= 20 || ideologyScore >= 0) {
            String counterMsg = buildCounterMessage(targetName, demanded);
            return NationalCoalitionActionResponse.counter(counterMsg, demanded, game);
        }

        // REJECT — below 20 with negative ideological clash
        String rejectMsg = buildRefusalMessage(targetName, primaryCode, contract, target, alliance, game);
        return NationalCoalitionActionResponse.refusal(primaryCode, rejectMsg, game);
    }

    // ── Ideology compatibility matrix ─────────────────────────────────────
    private static final String[] IDEOLOGIES = {
        "WELFARE_POPULIST","DEVELOPMENT_FIRST","REGIONAL_PRIDE",
        "ANTI_CORRUPTION","IDENTITY_POLITICS","UNITY_PLATFORM"
    };
    private static final int[][] IDEOLOGY_MATRIX = {
        // WEL  DEV  REG  ANC  IDN  UNI
        {  30,  10,   5,  15,   0,  20 }, // WELFARE_POPULIST
        {  10,  30,   0,  10, -10,  20 }, // DEVELOPMENT_FIRST
        {   5,   0,  30,   5,   5,  10 }, // REGIONAL_PRIDE
        {  15,  10,   5,  30,  -5,  20 }, // ANTI_CORRUPTION
        {   0, -10,   5,  -5,  30,   0 }, // IDENTITY_POLITICS
        {  20,  20,  10,  20,   0,  30 }, // UNITY_PLATFORM
    };

    private int computeIdeologyScore(NationalPartyState inviter, NationalPartyState target) {
        if (inviter == null || target == null) return 0;
        String inv = (inviter.getIdeology() != null ? inviter.getIdeology() : "").toUpperCase().replace(" ", "_");
        String tgt = (target.getIdeology()  != null ? target.getIdeology()  : "").toUpperCase().replace(" ", "_");
        int iRow = indexOfIdeology(inv);
        int iCol = indexOfIdeology(tgt);
        if (iRow < 0 || iCol < 0) return 0;
        return IDEOLOGY_MATRIX[iRow][iCol];
    }

    private int indexOfIdeology(String name) {
        for (int i = 0; i < IDEOLOGIES.length; i++) {
            if (IDEOLOGIES[i].equals(name)) return i;
        }
        return -1;
    }

    private int computeSeatScore(NationalAlliance alliance, NationalGame game, NationalPartyState target) {
        if (alliance == null || target == null) return 0;
        int totalSeats = game.getPartyStates().stream()
            .filter(p -> alliance.getMembers().stream().anyMatch(m -> m.getPartyKey().equals(p.getPartyKey())))
            .mapToInt(NationalPartyState::getSeats).sum();
        int tSeats = Math.max(1, target.getSeats());
        double ratio = (double) totalSeats / tSeats;
        if (ratio >= 3.0) return 20;
        if (ratio >= 2.0) return 10;
        if (ratio >= 1.5) return  5;
        if (ratio >= 1.0) return  0;
        return -20;
    }

    private int computeCoalitionMoraleScore(NationalAlliance alliance, NationalGame game) {
        if (alliance == null || alliance.getMembers().isEmpty()) return 0;
        double avg = alliance.getMembers().stream()
            .mapToInt(m -> {
                NationalPartyState ps = game.findPartyState(m.getPartyKey());
                return ps != null ? ps.getMorale() : 50;
            }).average().orElse(50.0);
        if (avg >= 75) return 10;
        if (avg >= 60) return  5;
        if (avg >= 45) return  0;
        if (avg >= 30) return -5;
        return -10;
    }

    private int computeTargetMoraleScore(NationalPartyState target) {
        if (target == null) return 0;
        int m = target.getMorale();
        if (m >= 85) return -15;
        if (m >= 70) return  -8;
        if (m >= 55) return   0;
        if (m >= 40) return   8;
        return 15;
    }

    private int computeMinisterScore(NationalContract contract) {
        int cabinet = Math.min(contract.getCabinetMinistersPromised() * 8, 24);
        int state   = Math.min(contract.getStateMinistersPromised()   * 2, 10);
        return cabinet + state;
    }

    /** Joining bonus evaluated as % of target party's own funds */
    private int computeJoiningBonusScore(NationalContract contract, NationalPartyState target) {
        double bonus = contract.getJoiningBonus();
        if (bonus <= 0) return 0;
        double funds = (target != null && target.getFunds() > 0) ? target.getFunds() : 1.0;
        double pct = (bonus / funds) * 100.0;
        if (pct >= 60) return 20;
        if (pct >= 40) return 15;
        if (pct >= 20) return 10;
        if (pct >= 10) return  5;
        return 2; // nominal — some offer better than none
    }

    private int computeDesperationBonus(NationalPartyState target, NationalContract contract) {
        if (target == null) return 0;
        // Only applies when there's a financial offer
        if (contract.getJoiningBonus() <= 0) return 0;
        double startF = (target.getStartingFunds() > 0) ? target.getStartingFunds() : target.getFunds();
        if (startF <= 0) return 0;
        double dropPct = ((startF - target.getFunds()) / startF) * 100.0;
        if (dropPct > 50.0) return 20; // critical fund collapse (>50% drop)
        if (dropPct > 30.0) return 12; // desperate (>30% drop)
        if (dropPct > 20.0) return  5; // tight (>20% drop)
        return 0; // comfortable/growing
    }

    private int computeLoyaltyPenalty(NationalPartyState target) {
        if (target == null) return 0;
        String seed = target.getPreSeededAllianceKey();
        if (seed == null) return 0;
        String upper = seed.toUpperCase();
        if (upper.equals("UNALIGNED") || upper.equals("INDEPENDENT") || upper.isEmpty()) return 0;
        return -40;
    }

    private CoalitionResponseCode detectPrimaryRefusalCode(
            int ideologyScore, int seatScore, int targetMoraleScore, int totalScore,
            int loyaltyPenalty, NationalPartyState target, NationalContract contract,
            NationalAlliance alliance, NationalGame game) {

        if (loyaltyPenalty < 0) return CoalitionResponseCode.REFUSED_LOYALTY_BOND;
        if (ideologyScore < 0)  return CoalitionResponseCode.REFUSED_IDEOLOGY_CLASH;
        if (seatScore < 0)      return CoalitionResponseCode.REFUSED_COALITION_TOO_WEAK;
        if (targetMoraleScore <= -8) return CoalitionResponseCode.REFUSED_HIGH_MORALE_INDEPENDENT;
        double startF = (target != null && target.getStartingFunds() > 0) ? target.getStartingFunds() : (target != null ? target.getFunds() : 0);
        double dropPct = (startF > 0 && target != null) ? ((startF - target.getFunds()) / startF) * 100.0 : 0;
        if (target != null && dropPct <= 10.0 && contract.getJoiningBonus() < 1.0)
            return CoalitionResponseCode.REFUSED_FINANCIALLY_SECURE;
        return CoalitionResponseCode.REFUSED_UNATTRACTIVE_TERMS;
    }

    private NationalContract buildCounterProposal(NationalContract offered, NationalPartyState target) {
        int tSeats = (target != null) ? Math.max(1, target.getSeats()) : 1;
        double tFunds = (target != null && target.getFunds() > 0) ? target.getFunds() : 5.0;

        NationalContract counter = new NationalContract();
        double offeredBonus = (offered != null) ? offered.getJoiningBonus() : 0.0;
        int offeredCabinet = (offered != null) ? offered.getCabinetMinistersPromised() : 0;
        int offeredState = (offered != null) ? offered.getStateMinistersPromised() : 0;

        double baseBonus = Math.min(30.0, Math.max(1.0, Math.round((tFunds * 0.30) * 10.0) / 10.0));
        int baseCabinet = Math.max(1, (int) Math.ceil(tSeats / 20.0));
        int baseState = Math.max(1, (int) Math.ceil(tSeats / 10.0));

        counter.setJoiningBonus(Math.max(offeredBonus, baseBonus));
        counter.setRecurringPerSeason(0); // recurring removed from UI
        counter.setCabinetMinistersPromised(Math.max(offeredCabinet, baseCabinet));
        counter.setStateMinistersPromised(Math.max(offeredState, baseState));
        counter.setDurationSeasons(-1);
        counter.setBroken(false);
        return counter;
    }

    private String buildCounterMessage(String targetName, NationalContract counter) {
        return "🤝 " + targetName + " is open to joining, but wants better terms — they're asking for ₹"
            + String.format("%.1f", counter.getJoiningBonus()) + " Cr joining bonus, "
            + counter.getCabinetMinistersPromised() + " Cabinet posts, and "
            + counter.getStateMinistersPromised() + " State Minister posts.";
    }

    private String buildRefusalMessage(String targetName, CoalitionResponseCode code,
            NationalContract contract, NationalPartyState target,
            NationalAlliance alliance, NationalGame game) {
        switch (code) {
            case REFUSED_IDEOLOGY_CLASH:
                return "⛔ " + targetName + " declined: Their political platform is too different from your coalition's direction. A merger would alienate their core voters.";
            case REFUSED_COALITION_TOO_WEAK: {
                int aSeats = (alliance != null) ? game.getPartyStates().stream()
                    .filter(p -> alliance.getMembers().stream().anyMatch(m -> m.getPartyKey().equals(p.getPartyKey())))
                    .mapToInt(NationalPartyState::getSeats).sum() : 0;
                int tSeats = (target != null) ? target.getSeats() : 0;
                return "⛔ " + targetName + " declined: Your alliance (" + aSeats + " seats) doesn't yet have enough parliamentary weight to give them meaningful cover compared to their " + tSeats + " seats. Grow your coalition first.";
            }
            case REFUSED_HIGH_MORALE_INDEPENDENT: {
                int morale = (target != null) ? target.getMorale() : 80;
                return "⛔ " + targetName + " declined: With strong internal morale (" + morale + "/100) and grassroots momentum, their leadership sees no reason to give up their independent identity right now.";
            }
            case REFUSED_FINANCIALLY_SECURE: {
                double funds = (target != null) ? target.getFunds() : 0;
                return "⛔ " + targetName + " declined: They are financially stable (₹" + String.format("%.1f", funds) + " Cr in reserves) and found your offer underwhelming. Try increasing the joining bonus or offering more ministry portfolios.";
            }
            case REFUSED_LOYALTY_BOND:
                return "⛔ " + targetName + " declined: They have deep historical ties to another political bloc. Breaking that loyalty requires a truly extraordinary offer.";
            case REFUSED_UNATTRACTIVE_TERMS:
            default: {
                NationalContract counter = buildCounterProposal(contract, target);
                return "⛔ " + targetName + " rejected the offer. To bring them on board, consider offering at least "
                    + counter.getCabinetMinistersPromised() + " Cabinet post(s) or a joining bonus of ₹"
                    + String.format("%.1f", counter.getJoiningBonus()) + " Cr.";
            }
        }
    }


    public NationalGame respondToRequest(String gameId, String requestId, boolean accept) {
        NationalGame game = findGame(gameId);
        
        NationalCoalitionRequest request = game.getPendingRequests().stream()
            .filter(r -> r.getRequestId().equals(requestId) && "INCOMING".equals(r.getDirection()))
            .findFirst().orElseThrow(() -> new RuntimeException("Incoming request not found"));
            
        NationalAlliance alliance = game.findPlayerAlliance(game.getPartyKey());
        if (alliance == null) {
            throw new RuntimeException("No active alliance led by player.");
        }
        
        NationalPartyState playerState = game.findPartyState(game.getPartyKey());
        
        if (accept) {
            if (alliance.getTotalCabinetPromised() + request.getRequestedCabinetMinisters() > 20) {
                throw new RuntimeException("Exceeds max cabinet ministers (20).");
            }
            if (alliance.getTotalStatePromised() + request.getRequestedStateMinisters() > 50) {
                throw new RuntimeException("Exceeds max state ministers (50).");
            }
            if (playerState != null && playerState.getFunds() < request.getRequestedJoiningBonus()) {
                throw new RuntimeException("Insufficient party funds for joining bonus.");
            }
            
            NationalContract contract = new NationalContract();
            contract.setJoiningBonus(request.getRequestedJoiningBonus());
            contract.setRecurringPerSeason(request.getRequestedRecurringPerSeason());
            contract.setCabinetMinistersPromised(request.getRequestedCabinetMinisters());
            contract.setStateMinistersPromised(request.getRequestedStateMinisters());
            contract.setDurationSeasons(-1);
            contract.setBroken(false);
            
            NationalPartyState target = game.findPartyState(request.getFromPartyKey());
            
            NationalAllianceMember member = new NationalAllianceMember();
            member.setPartyKey(request.getFromPartyKey());
            member.setJoinedAtSeason(game.getCurrentSeason());
            member.setSeats(target != null ? target.getSeats() : 0);
            member.setMorale(target != null ? target.getMorale() : 70);
            member.setContract(contract);
            
            alliance.getMembers().add(member);
            alliance.setTotalCabinetPromised(alliance.getTotalCabinetPromised() + contract.getCabinetMinistersPromised());
            alliance.setTotalStatePromised(alliance.getTotalStatePromised() + contract.getStateMinistersPromised());
            if (playerState != null && contract.getJoiningBonus() > 0) {
                playerState.setFunds(Math.max(0.0, Math.round((playerState.getFunds() - contract.getJoiningBonus()) * 10.0) / 10.0));
                game.setPlayerFunds(playerState.getFunds());
            }
            if (target != null && contract.getJoiningBonus() > 0) {
                target.setFunds(Math.round((target.getFunds() + contract.getJoiningBonus()) * 10.0) / 10.0);
            }
            
            if (target != null) {
                target.setCurrentAllianceId(alliance.getAllianceId());
            }
            
            request.setStatus("ACCEPTED");
            logEntry(alliance, game.getCurrentSeason(), "REQUEST_ACCEPTED", "Accepted join request from " + resolveTargetName(target));
        } else {
            request.setStatus("REJECTED");
            NationalPartyState target = game.findPartyState(request.getFromPartyKey());
            logEntry(alliance, game.getCurrentSeason(), "REQUEST_REJECTED", "Rejected join request from " + resolveTargetName(target));
        }
        
        game.setUpdatedAt(Instant.now().toString());
        return repository.save(game);
    }

    public NationalGame removeParty(String gameId, String targetPartyKey) {
        NationalGame game = findGame(gameId);
        NationalAlliance alliance = game.findPlayerAlliance(game.getPartyKey());
        if (alliance == null) throw new RuntimeException("No active alliance.");
        
        NationalAllianceMember member = alliance.getMembers().stream()
            .filter(m -> m.getPartyKey().equals(targetPartyKey)).findFirst().orElseThrow();
            
        member.getContract().setBroken(true);
        member.getContract().setBreakReason("REMOVED_BY_LEADER");
        
        NationalPartyState target = game.findPartyState(targetPartyKey);
        if (target != null) {
            target.setMorale(Math.max(0, target.getMorale() - 25));
            target.setCurrentAllianceId(null);
        }
        
        NationalPartyState player = game.findPartyState(game.getPartyKey());
        if (player != null) {
            player.setMorale(Math.max(0, player.getMorale() - 5));
        }
        
        alliance.setTotalCabinetPromised(Math.max(0, alliance.getTotalCabinetPromised() - member.getContract().getCabinetMinistersPromised()));
        alliance.setTotalStatePromised(Math.max(0, alliance.getTotalStatePromised() - member.getContract().getStateMinistersPromised()));
        
        alliance.getMembers().remove(member);
        
        logEntry(alliance, game.getCurrentSeason(), "PARTY_REMOVED", resolveTargetName(target) + " was removed from the alliance.");
        
        game.setUpdatedAt(Instant.now().toString());
        return repository.save(game);
    }

    public NationalGame dissolveAlliance(String gameId) {
        NationalGame game = findGame(gameId);
        NationalAlliance alliance = game.findPlayerAlliance(game.getPartyKey());
        if (alliance == null) throw new RuntimeException("No active alliance.");
        
        for (NationalAllianceMember member : alliance.getMembers()) {
            member.getContract().setBroken(true);
            member.getContract().setBreakReason("ALLIANCE_DISSOLVED");
            NationalPartyState target = game.findPartyState(member.getPartyKey());
            if (target != null) {
                target.setMorale(Math.max(0, target.getMorale() - 20));
                target.setCurrentAllianceId(null);
            }
        }
        
        NationalPartyState player = game.findPartyState(game.getPartyKey());
        if (player != null) {
            player.setMorale(Math.max(0, player.getMorale() - 10));
            player.setCurrentAllianceId(null);
        }
        
        logEntry(alliance, game.getCurrentSeason(), "ALLIANCE_DISSOLVED", "Alliance was dissolved by the leader.");
        game.getAlliances().remove(alliance);
        
        game.setUpdatedAt(Instant.now().toString());
        return repository.save(game);
    }

    public NationalGame leaveAlliance(String gameId) {
        NationalGame game = findGame(gameId);
        
        NationalAlliance found = null;
        for (NationalAlliance a : game.getAlliances()) {
            boolean isMember = a.getMembers().stream().anyMatch(m -> m.getPartyKey().equals(game.getPartyKey()));
            if (isMember) {
                found = a;
                break;
            }
        }
        
        if (found != null) {
            NationalPartyState player = game.findPartyState(game.getPartyKey());
            if (player != null) {
                player.setMorale(Math.max(0, player.getMorale() - 15));
                player.setCurrentAllianceId(null);
            }
            
            found.getMembers().removeIf(m -> m.getPartyKey().equals(game.getPartyKey()));
            logEntry(found, game.getCurrentSeason(), "PLAYER_LEFT", "Player left the alliance.");
        }
        
        game.setUpdatedAt(Instant.now().toString());
        return repository.save(game);
    }

    public NationalGame reallocateResources(String gameId, List<Map<String, Object>> newAllocations) {
        NationalGame game = findGame(gameId);
        NationalAlliance alliance = game.findPlayerAlliance(game.getPartyKey());
        if (alliance == null) throw new RuntimeException("No active alliance.");
        
        int tempTotalCab = 0;
        int tempTotalState = 0;
        
        for (Map<String, Object> alloc : newAllocations) {
            int cab = ((Number) alloc.get("cabinetMinistersPromised")).intValue();
            int state = ((Number) alloc.get("stateMinistersPromised")).intValue();
            tempTotalCab += cab;
            tempTotalState += state;
        }
        
        if (tempTotalCab > 20) throw new RuntimeException("Exceeds total cabinet ministers cap.");
        if (tempTotalState > 50) throw new RuntimeException("Exceeds total state ministers cap.");
        
        for (Map<String, Object> alloc : newAllocations) {
            String pk = (String) alloc.get("partyKey");
            double recurring = alloc.containsKey("recurringPerSeason") && alloc.get("recurringPerSeason") instanceof Number
                ? ((Number) alloc.get("recurringPerSeason")).doubleValue() : 0.0;

            int cab = ((Number) alloc.get("cabinetMinistersPromised")).intValue();
            int state = ((Number) alloc.get("stateMinistersPromised")).intValue();
            
            NationalAllianceMember member = alliance.getMembers().stream()
                .filter(m -> m.getPartyKey().equals(pk)).findFirst().orElse(null);
                
            if (member != null) {
                member.getContract().setRecurringPerSeason(recurring);
                member.getContract().setCabinetMinistersPromised(cab);
                member.getContract().setStateMinistersPromised(state);
            }
        }
        
        alliance.setTotalCabinetPromised(tempTotalCab);
        alliance.setTotalStatePromised(tempTotalState);
        logEntry(alliance, game.getCurrentSeason(), "RESOURCES_REALLOCATED", "Resources reallocated for alliance members.");
        
        game.setUpdatedAt(Instant.now().toString());
        return repository.save(game);
    }

    // ── Supporting Data & Structures for State Elections ──────────────────────
    public static class HistoricalElectionData {
        public String stateCode;
        public String stateName;
        public int electionTurn;
        public String winnerParty;
        public String rivalParty;
        public int totalAssemblySeats;
        public int winnerAssemblySeats;
        public String headline;
        public String narrative;

        public HistoricalElectionData(String stateCode, String stateName, int electionTurn, String winnerParty, String rivalParty, int totalAssemblySeats, int winnerAssemblySeats, String headline, String narrative) {
            this.stateCode = stateCode;
            this.stateName = stateName;
            this.electionTurn = electionTurn;
            this.winnerParty = winnerParty;
            this.rivalParty = rivalParty;
            this.totalAssemblySeats = totalAssemblySeats;
            this.winnerAssemblySeats = winnerAssemblySeats;
            this.headline = headline;
            this.narrative = narrative;
        }
    }

    private static final Map<String, HistoricalElectionData> HISTORICAL_ELECTIONS = new HashMap<>();
    static {
        HISTORICAL_ELECTIONS.put("ASSAM", new HistoricalElectionData("ASSAM", "Assam", 5, "INC", "AGP", 126, 71,
            "Assam Assembly Verdict: Tarun Gogoi Leads Congress to Clear Majority!",
            "Congress secured 71 of 126 seats in Assam, decisively defeating the incumbent Asom Gana Parishad (AGP). The victory revitalizes the Congress party in the Northeast."));
        HISTORICAL_ELECTIONS.put("KERALA", new HistoricalElectionData("KERALA", "Kerala", 5, "INC", "CPIM", 140, 99,
            "Kerala Assembly Verdict: UDF Front Storms to Power with 99 Seats!",
            "A powerful anti-incumbency wave swept the United Democratic Front (UDF) led by Congress to power, restricting the Left Democratic Front (LDF) to 40 seats."));
        HISTORICAL_ELECTIONS.put("TAMIL_NADU", new HistoricalElectionData("TAMIL_NADU", "Tamil Nadu", 5, "AIADMK", "DMK", 234, 196,
            "Tamil Nadu Assembly Verdict: AIADMK Front Scores Landslide Triumph!",
            "J. Jayalalithaa's AIADMK coalition won 196 of 234 assembly seats, comprehensively defeating the DMK front in one of Tamil Nadu's most decisive verdicts."));
        HISTORICAL_ELECTIONS.put("WEST_BENGAL", new HistoricalElectionData("WEST_BENGAL", "West Bengal", 5, "CPIM", "TMC", 294, 199,
            "West Bengal Assembly Verdict: Historic 6th Landslide for Left Front!",
            "Buddhadeb Bhattacharjee steered the CPI(M)-led Left Front to 199 seats, holding off Mamata Banerjee's Trinamool Congress and Congress challenge."));
        HISTORICAL_ELECTIONS.put("PUNJAB", new HistoricalElectionData("PUNJAB", "Punjab", 14, "INC", "SAD", 117, 62,
            "Punjab Assembly Verdict: Captain Amarinder Singh Propels Congress to Victory!",
            "Congress unseated the Shiromani Akali Dal-BJP government by winning 62 seats, restoring Congress control in the border state."));
        HISTORICAL_ELECTIONS.put("GUJARAT", new HistoricalElectionData("GUJARAT", "Gujarat", 24, "BJP", "INC", 182, 127,
            "Gujarat Assembly Verdict: Narendra Modi Powers BJP to Two-Thirds Sweep!",
            "BJP secured 127 of 182 seats in high-turnout Gujarat assembly polls, consolidating Narendra Modi's national stature."));
        HISTORICAL_ELECTIONS.put("MADHYA_PRADESH", new HistoricalElectionData("MADHYA_PRADESH", "Madhya Pradesh", 35, "BJP", "INC", 230, 173,
            "Madhya Pradesh Assembly Verdict: Uma Bharti's BJP Routs 10-Year Congress Rule!",
            "BJP dismantled the Digvijaya Singh government, capturing a massive 173 seats in Madhya Pradesh with promises of roads, power, and water reform."));
        HISTORICAL_ELECTIONS.put("RAJASTHAN", new HistoricalElectionData("RAJASTHAN", "Rajasthan", 36, "BJP", "INC", 200, 120,
            "Rajasthan Assembly Verdict: Vasundhara Raje Clinches Decisive Win for BJP!",
            "BJP crossed the majority mark with 120 seats, dislodging the Ashok Gehlot-led Congress government in the desert state."));
        HISTORICAL_ELECTIONS.put("DELHI", new HistoricalElectionData("DELHI", "Delhi", 36, "INC", "BJP", 70, 47,
            "Delhi Assembly Verdict: Sheila Dikshit Wins Historic Second Term for Congress!",
            "Sheila Dikshit defended Delhi for Congress with 47 seats, highlighting rapid urban development, flyovers, and green transport."));
        HISTORICAL_ELECTIONS.put("ANDHRA_PRADESH", new HistoricalElectionData("ANDHRA_PRADESH", "Andhra Pradesh", 40, "INC", "TDP", 294, 185,
            "Andhra Pradesh Assembly Verdict: YSR Padayatra Wave Propels Congress Landslide!",
            "Dr. Y.S. Rajasekhara Reddy ended N. Chandrababu Naidu's nine-year tenure as Congress claimed 185 assembly seats."));
        HISTORICAL_ELECTIONS.put("ODISHA", new HistoricalElectionData("ODISHA", "Odisha", 40, "BJD", "INC", 147, 93,
            "Odisha Assembly Verdict: Naveen Patnaik's BJD-BJP Alliance Re-elected!",
            "Naveen Patnaik retained Odisha comfortably, with the BJD-BJP alliance securing 93 seats against Congress."));
        HISTORICAL_ELECTIONS.put("KARNATAKA", new HistoricalElectionData("KARNATAKA", "Karnataka", 41, "BJP", "INC", 224, 79,
            "Karnataka Assembly Verdict: BJP Emerges Single Largest, Coalition Negotiations Begin!",
            "Karnataka delivered a fractured mandate with BJP winning 79 seats, Congress 65, and JD(S) 58, ushering in post-poll coalition drama."));
        HISTORICAL_ELECTIONS.put("JHARKHAND", new HistoricalElectionData("JHARKHAND", "Jharkhand", 50, "BJP", "JMM", 81, 36,
            "Jharkhand Assembly Verdict: NDA Clinches Narrow Edge in Debut Assembly Elections!",
            "BJP and JD(U) secured 36 seats in tribal-dominated Jharkhand, narrowly edging ahead of JMM and Congress to stake claim."));
        HISTORICAL_ELECTIONS.put("HARYANA", new HistoricalElectionData("HARYANA", "Haryana", 50, "INC", "INLD", 90, 67,
            "Haryana Assembly Verdict: Congress Wave Crushes INLD with Two-Thirds Sweep!",
            "Bhupinder Singh Hooda's Congress bagged 67 of 90 assembly seats, decimating the Chautala clan's INLD in Haryana."));
    }

    private void createElectionVerdictEvent(NationalGame game, int targetSeason, String stateCode, String stateName, String winnerParty, int assemblySeatsWon, int totalAssemblySeats, String headline, String narrative) {
        try {
            com.politicalsim.content.NationalEvent event = new com.politicalsim.content.NationalEvent();
            String evtId = "ELECTION_" + stateCode.toUpperCase() + "_S" + targetSeason + "_" + UUID.randomUUID().toString().substring(0, 8);
            event.setId(evtId);
            event.setEventKey("ELECTION_VERDICT_" + stateCode.toUpperCase());
            event.setEra(game.getEra());
            event.setSeason(targetSeason);
            event.setType("ELECTION_VERDICT");
            event.setIcon("🗳️");
            event.setTitle(headline);
            event.setSummary("Decisive assembly election verdict in " + stateName + ". " + winnerParty + " secured " + assemblySeatsWon + "/" + totalAssemblySeats + " assembly seats, shifting political momentum across India.");
            event.setNarrative(narrative != null ? narrative : "Electoral results in " + stateName + " reflect deep shifts in voter sentiment. Parties are now calibrating their national coalition alliances.");

            List<Map<String, Object>> rulingOptions = new ArrayList<>();
            Map<String, Object> rOpt1 = new HashMap<>();
            rOpt1.put("optionId", "CELEBRATE_MOMENTUM");
            rOpt1.put("label", "Celebrate Verdict & Capitalize on State Momentum");
            rOpt1.put("description", "Leverage state election momentum for national campaign fundraising and volunteer drive.");
            rOpt1.put("effects", Map.of("fundsPct", 0.08, "volunteersPct", 0.12, "moraleDelta", 8));
            rulingOptions.add(rOpt1);

            Map<String, Object> rOpt2 = new HashMap<>();
            rOpt2.put("optionId", "CONSOLIDATE_CADRE");
            rOpt2.put("label", "Consolidate Alliance Machinery & Local Governance");
            rOpt2.put("description", "Focus on grassroots governance delivery to guard against future anti-incumbency.");
            rOpt2.put("effects", Map.of("workersPct", 0.10, "donorsPct", 0.05, "moraleDelta", 4));
            rulingOptions.add(rOpt2);
            event.setRulingReactionOptions(rulingOptions);

            List<Map<String, Object>> oppOptions = new ArrayList<>();
            Map<String, Object> oOpt1 = new HashMap<>();
            oOpt1.put("optionId", "LAUNCH_REVIEW");
            oOpt1.put("label", "Conduct Grassroots Audit & Reform Campaign Front");
            oOpt1.put("description", "Rally opposition cadres around people's issues and revamp regional messaging.");
            oOpt1.put("effects", Map.of("workersPct", 0.12, "volunteersPct", 0.15, "moraleDelta", 5));
            oppOptions.add(oOpt1);

            Map<String, Object> oOpt2 = new HashMap<>();
            oOpt2.put("optionId", "AGGRESSIVE_COUNTER");
            oOpt2.put("label", "Aggressive Nationwide Agitation on Public Issues");
            oOpt2.put("description", "Take to the streets against incumbent policies to seize national narrative.");
            oOpt2.put("effects", Map.of("fundsPct", -0.05, "volunteersPct", 0.20, "moraleDelta", 6));
            oppOptions.add(oOpt2);
            event.setOppositionReactionOptions(oppOptions);

            nationalEventRepository.save(event);

            if (game.getCurrentSeasonEventIds() == null) {
                game.setCurrentSeasonEventIds(new ArrayList<>());
            }
            if (!game.getCurrentSeasonEventIds().contains(evtId)) {
                game.getCurrentSeasonEventIds().add(0, evtId);
            }
        } catch (Exception e) {
            System.err.println("Could not create election verdict event: " + e.getMessage());
        }
    }

    private void simulateAiPartyOperations(NationalGame game, int currentSeason) {
        if (game.getStateOperations() == null || game.getStateOperations().isEmpty()) return;
        String playerKey = (game.getPartyKey() != null ? game.getPartyKey() : "YDP").toUpperCase();

        for (NationalStateOperationState state : game.getStateOperations().values()) {
            if (state.getVoteSplits() == null) continue;

            List<NationalPartyState> eligibleAiParties = new ArrayList<>();
            for (NationalPartyState ps : game.getPartyStates()) {
                if (ps.isPlayerParty() || ps.getPartyKey().equalsIgnoreCase(playerKey)) continue;
                String pk = ps.getPartyKey().toUpperCase();
                if (state.getVoteSplits().containsKey(pk) || "BJP".equals(pk) || "INC".equals(pk)) {
                    eligibleAiParties.add(ps);
                }
            }

            for (NationalPartyState aiParty : eligibleAiParties) {
                String aiKey = aiParty.getPartyKey().toUpperCase();
                double aiFunds = aiParty.getFunds();
                int aiWorkers = aiParty.getWorkers();

                int priority = 0;
                int turnsToElection = state.getTurnsToElection();
                if (turnsToElection <= 3) priority += 50;
                else if (turnsToElection <= 6) priority += 35;
                else if (turnsToElection <= 12) priority += 20;
                else priority += 5;

                double aiShare = state.getVoteSplits().getOrDefault(aiKey, 0.0);
                double highestOtherShare = 0.0;
                for (Map.Entry<String, Double> entry : state.getVoteSplits().entrySet()) {
                    if (!entry.getKey().equalsIgnoreCase(aiKey) && !"UNDECIDED".equalsIgnoreCase(entry.getKey())) {
                        if (entry.getValue() > highestOtherShare) highestOtherShare = entry.getValue();
                    }
                }
                if (Math.abs(highestOtherShare - aiShare) <= 8.0) {
                    priority += 30; // close battleground
                }
                priority += Math.min(25, state.getTotalLokSabhaSeats() / 2);

                if (priority >= 25 && aiFunds >= 2.0 && aiWorkers >= 5000) {
                    double spendFunds = Math.min(5.0, Math.min(aiFunds * 0.35, 5.0));
                    spendFunds = Math.round(spendFunds * 10.0) / 10.0;
                    int spendWorkers = Math.min(15000, Math.min((int)(aiWorkers * 0.25), 15000));

                    if (spendFunds >= 1.0 && spendWorkers >= 2000) {
                        aiParty.setFunds(Math.max(0.5, Math.round((aiParty.getFunds() - spendFunds) * 10.0) / 10.0));

                        double voteGain = Math.round(((spendFunds * 0.4) + (spendWorkers / 6000.0 * 0.3)) * 10.0) / 10.0;
                        voteGain = Math.min(3.5, Math.max(0.4, voteGain));

                        Map<String, Double> votes = new HashMap<>(state.getVoteSplits());
                        double currentAiVote = votes.getOrDefault(aiKey, 0.0);
                        votes.put(aiKey, currentAiVote + voteGain);

                        double undecided = votes.getOrDefault("UNDECIDED", 5.0);
                        if (undecided > voteGain) {
                            votes.put("UNDECIDED", undecided - voteGain);
                        } else {
                            votes.put("UNDECIDED", Math.max(1.0, undecided * 0.5));
                            double remainder = voteGain - (undecided * 0.5);
                            double rivalTotal = 0.0;
                            for (Map.Entry<String, Double> e : votes.entrySet()) {
                                if (!e.getKey().equalsIgnoreCase(aiKey) && !"UNDECIDED".equalsIgnoreCase(e.getKey())) {
                                    rivalTotal += e.getValue();
                                }
                            }
                            if (rivalTotal > 0) {
                                for (Map.Entry<String, Double> e : new HashMap<>(votes).entrySet()) {
                                    if (!e.getKey().equalsIgnoreCase(aiKey) && !"UNDECIDED".equalsIgnoreCase(e.getKey())) {
                                        double drop = (e.getValue() / rivalTotal) * remainder;
                                        votes.put(e.getKey(), Math.max(1.0, e.getValue() - drop));
                                    }
                                }
                            }
                        }
                        state.setVoteSplits(votes);
                        state.normalizeVoteSplits();

                        if (state.getRegions() != null && !state.getRegions().isEmpty()) {
                            for (RegionalOperationState reg : state.getRegions().values()) {
                                double currentSup = reg.getSupportPercentage();
                                double penalty = Math.min(1.2, voteGain * 0.25);
                                reg.setSupportPercentage(Math.max(0.0, Math.round((currentSup - penalty) * 10.0) / 10.0));
                            }
                        }

                        state.addActivityLog(currentSeason, "AI_CAMPAIGN",
                            aiParty.getPartyName() + " (" + aiKey + ") transferred ₹" + spendFunds + " Cr & deployed "
                            + String.format("%,d", spendWorkers) + " cadre in " + state.getStateName()
                            + " to build ground support (+" + voteGain + "% vote swing).");

                        NationalAlliance playerAlliance = game.findPlayerAlliance(playerKey);
                        if (playerAlliance != null) {
                            logEntry(playerAlliance, currentSeason, "AI_CAMPAIGN_DETECTED",
                                "⚠️ Intelligence Report: " + aiParty.getPartyName() + " (" + aiKey + ") transferred ₹"
                                + spendFunds + " Cr & " + String.format("%,d", spendWorkers) + " cadre in "
                                + state.getStateName() + " (+" + voteGain + "% swing).");
                        }
                    }
                }
            }
        }
    }

    public NationalGame advanceSeason(String gameId) {
        NationalGame game = findGame(gameId);
        if (game.getNationalElectionResult() != null || "COMPLETED_VICTORY".equals(game.getStatus()) || "COMPLETED_DEFEATED".equals(game.getStatus())) {
            throw new RuntimeException("The national election has already concluded. Game session is complete.");
        }
        int currentSeason = game.getCurrentSeason();
        String playerKey = (game.getPartyKey() != null ? game.getPartyKey() : "YDP").toUpperCase();

        // ── Snapshot old party stats for exact turn-by-turn delta calculation ──
        Map<String, Map<String, Object>> prevStats = new HashMap<>();
        if (game.getPartyStates() != null) {
            for (NationalPartyState p : game.getPartyStates()) {
                Map<String, Object> map = new HashMap<>();
                map.put("seats", p.getSeats());
                map.put("morale", p.getMorale());
                map.put("funds", p.getFunds());
                map.put("corruption", p.getCorruption());
                map.put("workers", p.getWorkers());
                map.put("volunteers", p.getVolunteers());
                map.put("donors", p.getDonors());
                prevStats.put(p.getPartyKey().toUpperCase(), map);
            }
        }

        // ── 0. Recurring Alliance Aid & Corporate Donations ─────────────────
        for (NationalAlliance alliance : game.getAlliances()) {
            NationalPartyState leadParty = game.findPartyState(alliance.getLeaderPartyKey());
            for (NationalAllianceMember member : alliance.getMembers()) {
                if (member.getContract() != null && member.getContract().getRecurringPerSeason() > 0 
                        && !member.getPartyKey().equalsIgnoreCase(alliance.getLeaderPartyKey())) {
                    double recurring = member.getContract().getRecurringPerSeason();
                    if (leadParty != null) {
                        if (leadParty.getFunds() >= recurring) {
                            leadParty.setFunds(Math.max(0.0, Math.round((leadParty.getFunds() - recurring) * 10.0) / 10.0));
                            NationalPartyState target = game.findPartyState(member.getPartyKey());
                            if (target != null) {
                                target.setFunds(Math.round((target.getFunds() + recurring) * 10.0) / 10.0);
                            }
                        } else {
                            member.getContract().setBroken(true);
                            member.getContract().setBreakReason("PAYMENT_MISSED");
                            NationalPartyState target = game.findPartyState(member.getPartyKey());
                            if (target != null) {
                                target.setMorale(Math.max(0, target.getMorale() - 30));
                            }
                        }
                    }
                }
            }
            logEntry(alliance, currentSeason, "SEASON_ADVANCED", "Advancing season resolution for season " + currentSeason);
        }

        // Ensure projected seats and momentum are up to date for donation evaluation
        recalculateNationalProjectedSeats(game);

        NationalAlliance pAlliance = game.findPlayerAlliance(game.getPartyKey());
        for (NationalPartyState party : game.getPartyStates()) {
            boolean gainingMomentum = isPartyGainingMomentum(game, party);
            double donations = calculatePartyDonation(game, party);
            party.setDonationsPerTurn(donations);
            party.setGainingMomentum(gainingMomentum);
            party.setFunds(Math.round((party.getFunds() + donations) * 10.0) / 10.0);

            if (party.isPlayerParty() || (game.getPartyKey() != null && party.getPartyKey().equalsIgnoreCase(game.getPartyKey()))) {
                party.setPlayerParty(true);
                game.setPlayerFunds(party.getFunds());
                game.setPlayerCorruption(party.getCorruption());

                if (pAlliance != null) {
                    int pSeats = party.getProjectedSeats();
                    String momentumSuffix = gainingMomentum ? " (including +₹0.25 Cr/seat Momentum Surge Bonus)" : "";
                    logEntry(pAlliance, currentSeason, "PARTY_DONATIONS_COLLECTED",
                        "Collected ₹" + String.format(Locale.US, "%.1f", donations) + " Cr in party donations based on " 
                        + pSeats + " projected Lok Sabha seats @ ₹" + (gainingMomentum ? "0.75" : "0.50") + " Cr/seat" + momentumSuffix + ".");
                }
            }
        }

        // ── 1. Evaluate Player State Operations (UP, Bihar, Maharashtra) ────
        normalizeGameAllianceStates(game);
        if (game.getStateOperations() != null) {
            for (NationalStateOperationState state : game.getStateOperations().values()) {
                boolean wasSkipped = state.isSkippedThisTurn();
                boolean wasDone = state.isDoneThisTurn();

                state.updateElectionPhase(currentSeason);

                // Calculate Infrastructure Yields
                double monthlyCashDelta = 0.0;
                double totalWorkersPct = 0.0;
                double totalVolunteersPct = 0.0;
                double totalDonorsPct = 0.0;

                if (state.getBuildings() != null) {
                    for (Map.Entry<String, Integer> b : state.getBuildings().entrySet()) {
                        com.politicalsim.content.StateInfrastructureDefinition def = infrastructureRepository.findByKey(b.getKey()).orElse(null);
                        if (def != null) {
                            int count = b.getValue();
                            monthlyCashDelta += def.getMonthlyCashOutput() * count;
                            totalWorkersPct += def.getWorkersPercentMonthly() * count;
                            totalVolunteersPct += def.getVolunteersPercentMonthly() * count;
                            totalDonorsPct += def.getDonorsPercentMonthly() * count;
                        }
                    }
                }

                if (state.getRegions() != null && !state.getRegions().isEmpty()) {
                    for (RegionalOperationState reg : state.getRegions().values()) {
                        if (reg.getBuildings() != null) {
                            for (Map.Entry<String, Integer> b : reg.getBuildings().entrySet()) {
                                com.politicalsim.content.StateInfrastructureDefinition def = infrastructureRepository.findByKey(b.getKey()).orElse(null);
                                if (def != null) {
                                    int count = b.getValue();
                                    monthlyCashDelta += def.getMonthlyCashOutput() * count;
                                    totalWorkersPct += def.getWorkersPercentMonthly() * count;
                                    totalVolunteersPct += def.getVolunteersPercentMonthly() * count;
                                    totalDonorsPct += def.getDonorsPercentMonthly() * count;
                                }
                            }
                        }
                        if (reg.getWings() != null) {
                            for (Map.Entry<String, Integer> w : reg.getWings().entrySet()) {
                                com.politicalsim.content.StateInfrastructureDefinition def = infrastructureRepository.findByKey(w.getKey()).orElse(null);
                                if (def != null) {
                                    int count = w.getValue();
                                    monthlyCashDelta += def.getMonthlyCashOutput() * count;
                                    totalWorkersPct += def.getWorkersPercentMonthly() * count;
                                    totalVolunteersPct += def.getVolunteersPercentMonthly() * count;
                                    totalDonorsPct += def.getDonorsPercentMonthly() * count;
                                }
                            }
                        }

                        // Regional Turn-by-Turn Momentum: applied only if not skipped
                        double delta = 0.0;
                        if (!wasSkipped) {
                            delta += reg.getAllocatedFunds() * 0.4;
                            delta += (reg.getAllocatedWorkers() / 2000.0) * 0.25;
                            delta += (reg.getAllocatedVolunteers() / 5000.0) * 0.2;
                        }

                        // Passive building support bonuses always apply even if skipped!
                        if (reg.getWings() != null) {
                            for (Map.Entry<String, Integer> w : reg.getWings().entrySet()) {
                                com.politicalsim.content.StateInfrastructureDefinition def = infrastructureRepository.findByKey(w.getKey()).orElse(null);
                                if (def != null) delta += def.getMonthlySupportBonus() * w.getValue();
                            }
                        }
                        if (reg.getBuildings() != null) {
                            for (Map.Entry<String, Integer> b : reg.getBuildings().entrySet()) {
                                com.politicalsim.content.StateInfrastructureDefinition def = infrastructureRepository.findByKey(b.getKey()).orElse(null);
                                if (def != null) delta += def.getMonthlySupportBonus() * b.getValue();
                            }
                        }
                        if (state.getBuildings() != null && state.getBuildings().containsKey("state_party_hq")) {
                            delta += 0.2; // State HQ coordinates state-wide operations (+0.2% / turn)
                        }

                        if (wasSkipped && reg.getAllocatedFunds() <= 0 && reg.getAllocatedWorkers() <= 0 && reg.getAllocatedVolunteers() <= 0) {
                            delta -= 0.15; // natural decay if completely unstaffed
                        }

                        delta = Math.min(2.5, Math.max(-1.0, delta));
                        double updatedSup = Math.min(92.0, Math.max(0.0, Math.round((reg.getSupportPercentage() + delta) * 10.0) / 10.0));
                        reg.setSupportPercentage(updatedSup);
                    }

                    syncRegionalSupportToStateVoteSplits(state, playerKey);
                    recalculateProjectedSeats(state);
                }

                // Passive Relative Percentage Increases
                int deltaWorkers = (int) Math.round(state.getStateWorkers() * (totalWorkersPct / 100.0));
                int deltaVolunteers = (int) Math.round(state.getStateVolunteers() * (totalVolunteersPct / 100.0));
                int deltaDonors = (int) Math.round(state.getStateDonors() * (totalDonorsPct / 100.0));

                double netIncome = Math.round((0.5 + monthlyCashDelta) * 100.0) / 100.0;
                state.setNetIncomePerTurn(netIncome);
                state.setStateFunds(Math.max(0.0, Math.round((state.getStateFunds() + 0.5 + monthlyCashDelta) * 10.0) / 10.0));
                state.setStateWorkers(state.getStateWorkers() + deltaWorkers);
                state.setStateVolunteers(state.getStateVolunteers() + deltaVolunteers);
                state.setStateDonors(state.getStateDonors() + deltaDonors);

                if (wasSkipped) {
                    state.addActivityLog(currentSeason, "STATE_SKIPPED",
                        "Player skipped active campaign operations. Infrastructure yields collected: +₹"
                        + netIncome + " Cr treasury, cadre growth.");
                } else {
                    state.addActivityLog(currentSeason, "PLAYER_ACTION",
                        "Player completed strategic operations in " + state.getStateName()
                        + ". Infrastructure yields collected: +₹" + netIncome + " Cr.");
                }
            }
        }

        // ── 2. AI Turn in Active States (BJP, Congress, regional rivals) ───
        simulateAiPartyOperations(game, currentSeason);

        // ── 3. Recalculate State & National Projected Seats ───────────────
        if (game.getStateOperations() != null) {
            for (NationalStateOperationState s : game.getStateOperations().values()) {
                syncRegionalSupportToStateVoteSplits(s, playerKey);
                recalculateProjectedSeats(s);
            }
            recalculateNationalProjectedSeats(game);
        }

        // ── 4. Finance Card Resolution & Greed Evaluation ───────────────────
        NationalPartyState playerState = game.findPartyState(game.getPartyKey());
        if (playerState != null && game.getCommittedFinanceCard() != null) {
            NationalFinanceCardDefinition card = NationalFinanceCardDefinition.findById(game.getCommittedFinanceCard());
            if (card != null) {
                double startFunds = playerState.getStartingFunds() > 0 ? playerState.getStartingFunds() : Math.max(1.0, playerState.getFunds());
                double deltaFunds = Math.round((startFunds * card.getPctFunds()) * 10.0) / 10.0;
                int deltaWorkers = (int) Math.round(playerState.getWorkers() * card.getPctWorkers());
                int deltaVolunteers = (int) Math.round(playerState.getVolunteers() * card.getPctVolunteers());
                int deltaDonors = (int) Math.round(playerState.getDonors() * card.getPctDonors());

                int currentHeat = game.getMegaFinanceHeat();
                if (card.isMegaFinance()) {
                    currentHeat = Math.min(5, currentHeat + 1);
                } else if (card.isGrassroots()) {
                    currentHeat = Math.max(0, currentHeat - 1);
                } else {
                    if (currentHeat > 0) currentHeat = Math.max(0, currentHeat - 1);
                }

                int extraCorruption = 0;
                int extraMoraleBacklash = 0;
                if (currentHeat == 2) {
                    extraCorruption = 2;
                    extraMoraleBacklash = 2;
                } else if (currentHeat == 3) {
                    extraCorruption = 5;
                    extraMoraleBacklash = 5;
                } else if (currentHeat >= 4) {
                    extraCorruption = 10;
                    extraMoraleBacklash = 10;
                }

                playerState.setFunds(Math.round((playerState.getFunds() + deltaFunds) * 10.0) / 10.0);
                playerState.setWorkers(playerState.getWorkers() + deltaWorkers);
                playerState.setVolunteers(playerState.getVolunteers() + deltaVolunteers);
                playerState.setDonors(playerState.getDonors() + deltaDonors);
                playerState.setCorruption(Math.min(100, Math.max(0, playerState.getCorruption() + card.getDeltaCorruption() + extraCorruption)));
                playerState.setMorale(Math.min(100, Math.max(0, playerState.getMorale() + card.getDeltaMorale() - extraMoraleBacklash)));

                game.setPlayerFunds(playerState.getFunds());
                game.setPlayerCorruption(playerState.getCorruption());
                game.setMegaFinanceHeat(currentHeat);

                String report = "Season " + currentSeason + " Finance Operation: '" + card.getName() + "' resolved.";
                game.setLastSeasonFinanceReport(report);

                NationalAlliance playerAlliance = game.findPlayerAlliance(game.getPartyKey());
                if (playerAlliance != null) {
                    logEntry(playerAlliance, currentSeason, "FINANCE_CARD_RESOLVED", report);
                }
            }
        } else if (playerState != null) {
            if (game.getMegaFinanceHeat() > 0) {
                game.setMegaFinanceHeat(Math.max(0, game.getMegaFinanceHeat() - 1));
            }
        }
        game.setCommittedFinanceCard(null);
        game.setVisibleFinanceCardIds(NationalFinanceCardDefinition.pickRandomVisibleCardIds(6));

        // ── 5. Resolve National Events & Themes ───────────────────────────
        List<String> alliancePartyKeys = new ArrayList<>();
        NationalAlliance playerAllianceObj = game.findPlayerAlliance(game.getPartyKey());
        if (playerAllianceObj != null && playerAllianceObj.getMembers() != null) {
            for (NationalAllianceMember m : playerAllianceObj.getMembers()) {
                alliancePartyKeys.add(m.getPartyKey());
            }
        }
        if (!alliancePartyKeys.contains(game.getPartyKey())) {
            alliancePartyKeys.add(game.getPartyKey());
        }

        if (game.getResolvedEventReactions() != null && !game.getResolvedEventReactions().isEmpty()) {
            for (Map.Entry<String, String> entry : game.getResolvedEventReactions().entrySet()) {
                String eventId = entry.getKey();
                String optionId = entry.getValue();
                com.politicalsim.content.NationalEvent event = nationalEventRepository.findById(eventId).orElse(null);
                if (event != null) {
                    Map<String, Object> chosenOpt = null;
                    if (event.getRulingReactionOptions() != null) {
                        for (Map<String, Object> opt : event.getRulingReactionOptions()) {
                            if (optionId.equals(opt.get("optionId"))) { chosenOpt = opt; break; }
                        }
                    }
                    if (chosenOpt == null && event.getOppositionReactionOptions() != null) {
                        for (Map<String, Object> opt : event.getOppositionReactionOptions()) {
                            if (optionId.equals(opt.get("optionId"))) { chosenOpt = opt; break; }
                        }
                    }
                    if (chosenOpt != null && chosenOpt.get("effects") instanceof Map) {
                        Map<String, Object> eff = (Map<String, Object>) chosenOpt.get("effects");
                        double fPct = ((Number) eff.getOrDefault("fundsPct", 0.0)).doubleValue();
                        double wPct = ((Number) eff.getOrDefault("workersPct", 0.0)).doubleValue();
                        double vPct = ((Number) eff.getOrDefault("volunteersPct", 0.0)).doubleValue();
                        double dPct = ((Number) eff.getOrDefault("donorsPct", 0.0)).doubleValue();
                        int mDelta = ((Number) eff.getOrDefault("moraleDelta", 0)).intValue();
                        int cDelta = ((Number) eff.getOrDefault("corruptionDelta", 0)).intValue();

                        for (String pk : alliancePartyKeys) {
                            NationalPartyState ps = game.findPartyState(pk);
                            if (ps != null) {
                                double fBase = ps.getStartingFunds() > 0 ? ps.getStartingFunds() : Math.max(1.0, ps.getFunds());
                                double dF = Math.round((fBase * fPct) * 10.0) / 10.0;
                                int dW = (int) Math.round(ps.getWorkers() * wPct);
                                int dV = (int) Math.round(ps.getVolunteers() * vPct);
                                int dD = (int) Math.round(ps.getDonors() * dPct);

                                ps.setFunds(Math.round((ps.getFunds() + dF) * 10.0) / 10.0);
                                ps.setWorkers(ps.getWorkers() + dW);
                                ps.setVolunteers(ps.getVolunteers() + dV);
                                ps.setDonors(ps.getDonors() + dD);
                                ps.setCorruption(Math.min(100, Math.max(0, ps.getCorruption() + cDelta)));
                                ps.setMorale(Math.min(100, Math.max(0, ps.getMorale() + mDelta)));
                            }
                        }
                        if (playerAllianceObj != null) {
                            logEntry(playerAllianceObj, currentSeason, "EVENT_RESOLVED",
                                "Alliance reacted to '" + event.getTitle() + "': " + chosenOpt.get("label"));
                        }
                    }
                }
            }
        }

        if (game.getActiveThemeKey() != null && game.getActiveThemeAction() != null) {
            String thmKey = game.getActiveThemeKey();
            com.politicalsim.content.NationalTheme theme = nationalThemeRepository.findById(thmKey)
                .orElseGet(() -> nationalThemeRepository.findAll().stream()
                    .filter(t -> thmKey.equalsIgnoreCase(t.getThemeKey()) || thmKey.equalsIgnoreCase(t.getId()))
                    .findFirst().orElse(null));

            if (theme != null && theme.getActionEffects() != null && theme.getActionEffects().containsKey(game.getActiveThemeAction())) {
                int streak = game.getThemePersistenceStreak();
                if (thmKey.equalsIgnoreCase(game.getLastThemeKey())) {
                    streak++;
                } else {
                    streak = 1;
                }
                game.setThemePersistenceStreak(streak);
                game.setLastThemeKey(thmKey);

                double streakMultiplier = 1.0;
                if (streak == 2) streakMultiplier = 1.2;
                else if (streak == 3) streakMultiplier = 1.5;
                else if (streak == 4) streakMultiplier = 2.0;
                else if (streak >= 5) streakMultiplier = 2.5;

                Map<String, Object> actionData = theme.getActionEffects().get(game.getActiveThemeAction());
                double fPct = ((Number) actionData.getOrDefault("fundsPct", 0.0)).doubleValue();
                double wPct = ((Number) actionData.getOrDefault("workersPct", 0.0)).doubleValue() * streakMultiplier;
                double vPct = ((Number) actionData.getOrDefault("volunteersPct", 0.0)).doubleValue() * streakMultiplier;
                double dPct = ((Number) actionData.getOrDefault("donorsPct", 0.0)).doubleValue() * streakMultiplier;
                int mDelta = (int) Math.round(((Number) actionData.getOrDefault("moraleDelta", 0)).intValue() * streakMultiplier);
                int cDelta = ((Number) actionData.getOrDefault("corruptionDelta", 0)).intValue();

                if (streak >= 5) {
                    vPct += 0.40;
                    mDelta += 25;
                }

                for (String pk : alliancePartyKeys) {
                    NationalPartyState ps = game.findPartyState(pk);
                    if (ps != null) {
                        double fBase = ps.getStartingFunds() > 0 ? ps.getStartingFunds() : Math.max(1.0, ps.getFunds());
                        double dF = Math.round((fBase * fPct) * 10.0) / 10.0;
                        int dW = (int) Math.round(ps.getWorkers() * wPct);
                        int dV = (int) Math.round(ps.getVolunteers() * vPct);
                        int dD = (int) Math.round(ps.getDonors() * dPct);

                        ps.setFunds(Math.round((ps.getFunds() + dF) * 10.0) / 10.0);
                        ps.setWorkers(ps.getWorkers() + dW);
                        ps.setVolunteers(ps.getVolunteers() + dV);
                        ps.setDonors(ps.getDonors() + dD);
                        ps.setCorruption(Math.min(100, Math.max(0, ps.getCorruption() + cDelta)));
                        ps.setMorale(Math.min(100, Math.max(0, ps.getMorale() + mDelta)));
                    }
                }

                if (playerAllianceObj != null) {
                    String actionLabel = (String) actionData.getOrDefault("label", game.getActiveThemeAction());
                    logEntry(playerAllianceObj, currentSeason, "THEME_ACTION_RESOLVED",
                        "Alliance mobilized on '" + theme.getTitle() + "' with " + actionLabel + " (Streak: " + streak + " turns).");
                }

                // ── Resolve Negative Impact on Target Party ──
                if (game.getTargetPartyKey() != null && !game.getTargetPartyKey().trim().isEmpty()) {
                    String targetKey = game.getTargetPartyKey();
                    NationalPartyState targetPs = game.findPartyState(targetKey);
                    if (targetPs != null && !targetPs.isPlayerParty()) {
                        int penaltyMorale = Math.min(18, 4 + streak * 2);
                        int lostWorkers = Math.min((int)(targetPs.getWorkers() * 0.15), (int)(2500 + streak * 1500));
                        int lostVolunteers = Math.min((int)(targetPs.getVolunteers() * 0.15), (int)(1200 + streak * 800));
                        double lostFunds = Math.min(targetPs.getFunds() * 0.1, Math.round((0.4 + streak * 0.3) * 10.0) / 10.0);

                        targetPs.setMorale(Math.max(5, targetPs.getMorale() - penaltyMorale));
                        targetPs.setWorkers(Math.max(1000, targetPs.getWorkers() - lostWorkers));
                        targetPs.setVolunteers(Math.max(500, targetPs.getVolunteers() - lostVolunteers));
                        targetPs.setFunds(Math.max(0.0, Math.round((targetPs.getFunds() - lostFunds) * 10.0) / 10.0));

                        // State-level vote erosion in overlapping states
                        if (game.getStateOperations() != null) {
                            for (NationalStateOperationState st : game.getStateOperations().values()) {
                                if (st.getVoteSplits() != null && st.getVoteSplits().containsKey(targetKey.toUpperCase())) {
                                    double curSplit = st.getVoteSplits().get(targetKey.toUpperCase());
                                    double eroded = Math.max(1.0, Math.round((curSplit - (0.5 + streak * 0.2)) * 10.0) / 10.0);
                                    st.getVoteSplits().put(targetKey.toUpperCase(), eroded);
                                    st.normalizeVoteSplits();
                                    recalculateProjectedSeats(st);
                                }
                            }
                        }

                        String targetReport = "Theme offensive targeted " + targetPs.getPartyName() +
                            " (" + targetKey.toUpperCase() + "): Inflicted -" + penaltyMorale + "% Morale, -" + lostWorkers + " Cadre desertion, and -₹" + String.format(Locale.US, "%.1f", lostFunds) + " Cr donor loss.";
                        game.setThemeTargetReport(targetReport);
                        if (playerAllianceObj != null) {
                            logEntry(playerAllianceObj, currentSeason, "THEME_TARGET_ATTACK", targetReport);
                        }
                    }
                }
            }
        }

        // ── Resolve Media & Social Campaign Blitz ──
        if (game.isMediaSocialCommitted() && game.getMediaSocialSpend() != null && !game.getMediaSocialSpend().isEmpty()) {
            Map<String, Double> mSpend = game.getMediaSocialSpend();
            double totalSpend = 0.0;
            double effectiveSpend = 0.0;
            String topChannel = "Social Ads";
            double maxSpend = 0.0;

            for (Map.Entry<String, Double> e : mSpend.entrySet()) {
                double sp = e.getValue() != null ? e.getValue() : 0.0;
                totalSpend += sp;
                if (sp > maxSpend) {
                    maxSpend = sp;
                    topChannel = e.getKey().replace('_', ' ').toUpperCase();
                }
                if (sp <= 3.0) {
                    effectiveSpend += sp;
                } else {
                    effectiveSpend += 3.0 + Math.pow(sp - 3.0, 0.6);
                }
            }
            totalSpend = Math.round(totalSpend * 10.0) / 10.0;
            effectiveSpend = Math.round(effectiveSpend * 10.0) / 10.0;

            // Deduct funds from player
            NationalPartyState pState = game.findPartyState(game.getPartyKey());
            if (pState != null) {
                pState.setFunds(Math.max(0.0, Math.round((pState.getFunds() - totalSpend) * 10.0) / 10.0));
                game.setPlayerFunds(pState.getFunds());
            }

            // Excessive spend scrutiny penalty
            boolean heatAdded = false;
            if (totalSpend > 6.0) {
                game.setMegaFinanceHeat(Math.min(4, game.getMegaFinanceHeat() + 1));
                heatAdded = true;
            }

            // Calculate Viral Roll
            double viralOdds = 0.18;
            if (maxSpend >= 2.5) viralOdds += 0.07;
            if (game.getResolvedEventReactions() != null && !game.getResolvedEventReactions().isEmpty()) viralOdds += 0.10;
            if (game.getActiveThemeAction() != null) viralOdds += 0.10;
            viralOdds = Math.min(0.45, viralOdds);

            boolean isViral = Math.random() < viralOdds;
            int workersGained = (int) Math.round(effectiveSpend * 4000);
            int volunteersGained = (int) Math.round(effectiveSpend * 2200);
            int moraleBonus = Math.min(8, (int) Math.round(effectiveSpend * 1.5));

            int viralBonusWorkers = 0;
            int viralBonusVolunteers = 0;
            if (isViral) {
                viralBonusWorkers = (int) (12000 + Math.random() * 18000);
                viralBonusVolunteers = (int) (5000 + Math.random() * 8000);
                moraleBonus += 8;
                workersGained += viralBonusWorkers;
                volunteersGained += viralBonusVolunteers;
            }

            if (pState != null) {
                pState.setWorkers(pState.getWorkers() + workersGained);
                pState.setVolunteers(pState.getVolunteers() + volunteersGained);
                pState.setMorale(Math.min(100, pState.getMorale() + moraleBonus));
            }

            Map<String, Object> finalReport = new HashMap<>();
            finalReport.put("totalSpend", totalSpend);
            finalReport.put("effectiveSpend", effectiveSpend);
            finalReport.put("workersRecruited", workersGained);
            finalReport.put("volunteersGained", volunteersGained);
            finalReport.put("moraleBonus", moraleBonus);
            finalReport.put("viralTriggered", isViral);
            finalReport.put("viralChannel", topChannel);
            finalReport.put("viralBonusWorkers", viralBonusWorkers);
            finalReport.put("heatIncreased", heatAdded);

            String logMsg;
            if (isViral) {
                logMsg = "🔥 VIRAL BREAKTHROUGH: Social campaign on " + topChannel + " went viral! Recruited +" + workersGained + " cadres (+" + viralBonusWorkers + " viral surge) and boosted morale by +" + moraleBonus + "%.";
            } else {
                logMsg = "Digital Media & Social Campaign deployed across 4 channels (₹" + totalSpend + " Cr). Converted +" + workersGained + " workers and +" + volunteersGained + " volunteers.";
            }
            finalReport.put("summary", logMsg);
            game.setMediaSocialReport(finalReport);

            if (playerAllianceObj != null) {
                logEntry(playerAllianceObj, currentSeason, isViral ? "MEDIA_VIRAL_POST" : "MEDIA_CAMPAIGN_RESOLVED", logMsg);
            }

            // Reset spend allocation for next season
            game.setMediaSocialSpend(new HashMap<>());
            game.setMediaSocialCommitted(false);
        }

        // ── Seat Swings Morale Impact: 10 Lok Sabha seats projected swing -> 5% morale change ──
        if (game.getPreviousProjectedSeats() != null && !game.getPreviousProjectedSeats().isEmpty()) {
            for (NationalPartyState p : game.getPartyStates()) {
                String pk = p.getPartyKey().toUpperCase();
                int oldSeats = game.getPreviousProjectedSeats().getOrDefault(pk, p.getSeats());
                int newSeats = game.getNationalProjectedSeats().getOrDefault(pk, p.getSeats());
                int seatDelta = newSeats - oldSeats;
                if (seatDelta != 0) {
                    int moraleDelta = (int) Math.round((seatDelta / 10.0) * 5.0);
                    if (moraleDelta != 0) {
                        p.setMorale(Math.min(100, Math.max(5, p.getMorale() + moraleDelta)));
                        if (playerAllianceObj != null && (p.isPlayerParty() || pk.equalsIgnoreCase(playerKey))) {
                            logEntry(playerAllianceObj, currentSeason, "PROJECTED_SEATS_SWING",
                                "National seat projections updated: " + pk + " " + (seatDelta >= 0 ? "+" : "") + seatDelta
                                + " Lok Sabha seats (" + (moraleDelta >= 0 ? "+" : "") + moraleDelta + "% party morale effect).");
                        }
                    }
                }
            }
        }
        game.setPreviousProjectedSeats(new HashMap<>(game.getNationalProjectedSeats()));

        // Update Majority Status & Clean Actions
        game.setRulingAllianceKey(game.determineRulingAllianceKey());
        game.setResolvedEventReactions(new HashMap<>());
        game.setActiveThemeAction(null);

        // ── 6. Scheduled State Elections (Playable vs Historical) ───────────
        List<Map<String, Object>> scheduledElections = new ArrayList<>();
        if (nationalConfigRepository != null) {
            com.politicalsim.content.NationalConfig nConf = nationalConfigRepository.findByEra(game.getEra()).orElse(null);
            if (nConf != null && nConf.getStateElections() != null) {
                scheduledElections = nConf.getStateElections();
            }
        }

        for (Map<String, Object> se : scheduledElections) {
            int eTurn = ((Number) se.getOrDefault("electionTurn", -1)).intValue();
            String sCode = (String) se.get("stateCode");
            if (eTurn == currentSeason && sCode != null) {
                sCode = sCode.toUpperCase();
                if (game.getStateOperations() != null && game.getStateOperations().containsKey(sCode)) {
                    NationalStateOperationState activeSt = game.getStateOperations().get(sCode);
                    if (!activeSt.isElectionCompleted()) {
                        resolveStateElection(game, activeSt);
                        Map<String, Object> res = activeSt.getLastElectionResult();
                        String winner = res != null ? (String) res.get("winnerParty") : "Ruling Party";
                        int winSeats = 0;
                        if (res != null && res.get("assemblySeats") instanceof Map) {
                            Map<String, Object> aSeats = (Map<String, Object>) res.get("assemblySeats");
                            Object ws = aSeats.get(winner);
                            if (ws instanceof Number) winSeats = ((Number) ws).intValue();
                        }
                        createElectionVerdictEvent(game, currentSeason + 1, sCode, activeSt.getStateName(), winner,
                            winSeats, activeSt.getTotalAssemblySeats(),
                            activeSt.getStateName() + " Assembly Verdict: " + winner + " Sweeps State!",
                            "Assembly election concluded in " + activeSt.getStateName() + ". " + winner + " secured decisive victory with " + winSeats + " seats.");
                    }
                } else {
                    HistoricalElectionData hist = HISTORICAL_ELECTIONS.get(sCode);
                    if (hist != null) {
                        NationalPartyState winParty = game.findPartyState(hist.winnerParty);
                        if (winParty != null) {
                            winParty.setMorale(Math.min(100, winParty.getMorale() + 6));
                            winParty.setFunds(Math.round((winParty.getFunds() + 3.0) * 10.0) / 10.0);
                        }
                        NationalPartyState rivalParty = game.findPartyState(hist.rivalParty);
                        if (rivalParty != null) {
                            rivalParty.setMorale(Math.max(5, rivalParty.getMorale() - 4));
                        }

                        createElectionVerdictEvent(game, currentSeason + 1, sCode, hist.stateName, hist.winnerParty,
                            hist.winnerAssemblySeats, hist.totalAssemblySeats,
                            hist.headline, hist.narrative);

                        if (playerAllianceObj != null) {
                            logEntry(playerAllianceObj, currentSeason, "HISTORIC_ELECTION_RESOLVED",
                                "🗳️ " + hist.stateName + " Assembly Election concluded: " + hist.winnerParty
                                + " achieved historic victory (" + hist.winnerAssemblySeats + "/" + hist.totalAssemblySeats + " seats).");
                        }
                    }
                }
            }
        }

        // ── 7. Advance Season Counter & Next Events ─────────────────────────
        if (currentSeason >= 60) {
            resolveNationalElection(game, "TURN_60_SCHEDULED_ELECTION");
            game.setUpdatedAt(Instant.now().toString());
            return repository.save(game);
        }

        game.setCurrentSeason(currentSeason + 1);

        if (game.getStateOperations() != null) {
            for (NationalStateOperationState s : game.getStateOperations().values()) {
                boolean eligible = isStateEligibleForPlayer(game, s);
                s.setActive(eligible);
                s.setDoneThisTurn(false);
                s.setActiveIssueAction(null);
                s.updateElectionPhase(game.getCurrentSeason());
                if (!eligible) {
                    s.setSkippedThisTurn(true);
                } else {
                    s.setSkippedThisTurn(false);
                }
            }
        }

        List<com.politicalsim.content.NationalEvent> nextEvts = nationalEventRepository.findByEraAndSeason(game.getEra(), game.getCurrentSeason());
        if (nextEvts == null || nextEvts.isEmpty()) {
            nextEvts = nationalEventRepository.findByEra(game.getEra());
        }
        if (nextEvts != null) {
            List<String> nextEvtIds = game.getCurrentSeasonEventIds() != null ? new ArrayList<>(game.getCurrentSeasonEventIds()) : new ArrayList<>();
            for (com.politicalsim.content.NationalEvent e : nextEvts) {
                if (!nextEvtIds.contains(e.getId())) {
                    nextEvtIds.add(e.getId());
                }
            }
            game.setCurrentSeasonEventIds(nextEvtIds);
        }

        // ── Finalize Turn-by-Turn Deltas for Every Party State ──
        if (game.getPartyStates() != null) {
            for (NationalPartyState p : game.getPartyStates()) {
                Map<String, Object> old = prevStats.get(p.getPartyKey().toUpperCase());
                if (old != null) {
                    int oldSeats = ((Number) old.get("seats")).intValue();
                    int oldMorale = ((Number) old.get("morale")).intValue();
                    double oldFunds = ((Number) old.get("funds")).doubleValue();
                    int oldCorruption = ((Number) old.get("corruption")).intValue();
                    int oldWorkers = ((Number) old.get("workers")).intValue();
                    int oldVolunteers = ((Number) old.get("volunteers")).intValue();
                    int oldDonors = ((Number) old.get("donors")).intValue();

                    p.setDeltaSeats(p.getSeats() - oldSeats);
                    p.setDeltaMorale(p.getMorale() - oldMorale);
                    p.setDeltaFunds(Math.round((p.getFunds() - oldFunds) * 10.0) / 10.0);
                    p.setDeltaCorruption(p.getCorruption() - oldCorruption);
                    p.setDeltaWorkers(p.getWorkers() - oldWorkers);
                    p.setDeltaVolunteers(p.getVolunteers() - oldVolunteers);
                    p.setDeltaDonors(p.getDonors() - oldDonors);
                }
                if (p.isPlayerParty() || (game.getPartyKey() != null && p.getPartyKey().equalsIgnoreCase(game.getPartyKey()))) {
                    p.setPlayerParty(true);
                    game.setPlayerFunds(p.getFunds());
                    game.setPlayerCorruption(p.getCorruption());
                }
            }
        }

        refreshStrategicHints(game);
        game.setUpdatedAt(Instant.now().toString());
        return repository.save(game);
    }

    public int getPlayerAllianceProjectedSeats(NationalGame game) {
        if (game == null) return 0;
        String playerKey = (game.getPartyKey() != null ? game.getPartyKey() : "YDP").toUpperCase();
        Map<String, Integer> projected = game.getNationalProjectedSeats();
        if (projected == null || projected.isEmpty()) {
            recalculateNationalProjectedSeats(game);
            projected = game.getNationalProjectedSeats();
        }
        Set<String> allianceParties = new HashSet<>();
        allianceParties.add(playerKey);

        NationalAlliance playerAlliance = game.findPlayerAlliance(playerKey);
        if (playerAlliance != null && playerAlliance.getMembers() != null) {
            for (NationalAllianceMember m : playerAlliance.getMembers()) {
                if (m.getPartyKey() != null) {
                    allianceParties.add(m.getPartyKey().toUpperCase());
                }
            }
        }

        int totalSeats = 0;
        if (projected != null) {
            for (String pk : allianceParties) {
                totalSeats += projected.getOrDefault(pk, 0);
            }
        }
        return totalSeats;
    }

    public NationalGame callNoConfidenceVote(String gameId) {
        NationalGame game = findGame(gameId);
        if (game.getNationalElectionResult() != null || "COMPLETED_VICTORY".equals(game.getStatus()) || "COMPLETED_DEFEATED".equals(game.getStatus())) {
            throw new RuntimeException("The national election has already concluded.");
        }

        int playerAllianceSeats = getPlayerAllianceProjectedSeats(game);
        if (playerAllianceSeats <= 272) {
            throw new IllegalStateException("Cannot challenge No-Confidence Vote: Player Alliance commands "
                + playerAllianceSeats + " projected seats, but strictly > 272 seats are required.");
        }

        game.setNoConfidenceCalled(true);
        resolveNationalElection(game, "NO_CONFIDENCE_MOTION");
        game.setUpdatedAt(Instant.now().toString());
        return repository.save(game);
    }

    public void resolveNationalElection(NationalGame game, String triggerReason) {
        if (game == null) return;
        recalculateNationalProjectedSeats(game);

        Map<String, Integer> currentProjected = game.getNationalProjectedSeats() != null 
            ? new HashMap<>(game.getNationalProjectedSeats()) 
            : new HashMap<>();

        Map<String, Double> partyScores = new HashMap<>();
        double totalScore = 0.0;

        for (NationalPartyState p : game.getPartyStates()) {
            String pKey = p.getPartyKey().toUpperCase();
            int baseSeats = currentProjected.getOrDefault(pKey, p.getSeats());
            double moraleMod = (p.getMorale() - 50) * 0.12;
            double fundsMod = Math.min(10.0, (p.getFunds() / 10.0) * 2.0);
            double cadreMod = Math.min(8.0, (p.getWorkers() / 50000.0) * 2.0 + (p.getVolunteers() / 25000.0) * 2.0);
            double corrPenalty = p.getCorruption() > 25 ? (p.getCorruption() - 25) * 0.25 : 0.0;
            double score = Math.max(0.5, (double) baseSeats + moraleMod + fundsMod + cadreMod - corrPenalty);
            partyScores.put(pKey, score);
            totalScore += score;
        }

        if (totalScore <= 0.0) totalScore = 1.0;

        // Distribute exactly 543 seats using Largest Remainder Method (Hare-Niemeyer Quota)
        int seatsDistributed = 0;
        Map<String, Integer> allocatedSeats = new HashMap<>();
        Map<String, Double> remainders = new HashMap<>();

        for (NationalPartyState p : game.getPartyStates()) {
            String pKey = p.getPartyKey().toUpperCase();
            double quota = (partyScores.get(pKey) / totalScore) * 543.0;
            int floorSeats = (int) Math.floor(quota);
            allocatedSeats.put(pKey, floorSeats);
            remainders.put(pKey, quota - floorSeats);
            seatsDistributed += floorSeats;
        }

        int remainingSeats = 543 - seatsDistributed;
        List<Map.Entry<String, Double>> sortedRemainders = new ArrayList<>(remainders.entrySet());
        sortedRemainders.sort((a, b) -> Double.compare(b.getValue(), a.getValue()));

        for (int i = 0; i < remainingSeats && i < sortedRemainders.size(); i++) {
            String pKey = sortedRemainders.get(i).getKey();
            allocatedSeats.put(pKey, allocatedSeats.get(pKey) + 1);
        }

        // Apply allocated seats to party states
        for (NationalPartyState p : game.getPartyStates()) {
            String pKey = p.getPartyKey().toUpperCase();
            int won = allocatedSeats.getOrDefault(pKey, p.getSeats());
            p.setSeats(won);
        }
        game.setNationalProjectedSeats(new HashMap<>(allocatedSeats));

        // Group seats by Alliance
        String playerKey = (game.getPartyKey() != null ? game.getPartyKey() : "YDP").toUpperCase();
        NationalAlliance playerAlliance = game.findPlayerAlliance(playerKey);
        String playerAllianceId = playerAlliance != null ? playerAlliance.getAllianceId() : "PLAYER_FRONT";
        String playerAllianceName = playerAlliance != null ? playerAlliance.getAllianceName() : "Player Alliance";

        Set<String> playerAllianceParties = new HashSet<>();
        playerAllianceParties.add(playerKey);
        if (playerAlliance != null && playerAlliance.getMembers() != null) {
            for (NationalAllianceMember m : playerAlliance.getMembers()) {
                if (m.getPartyKey() != null) playerAllianceParties.add(m.getPartyKey().toUpperCase());
            }
        }

        int playerAllianceSeats = 0;
        for (String pk : playerAllianceParties) {
            playerAllianceSeats += allocatedSeats.getOrDefault(pk, 0);
        }

        // Tally all alliances
        Map<String, Integer> allianceSeatTotals = new HashMap<>();
        Map<String, String> allianceNames = new HashMap<>();
        Map<String, String> allianceColors = new HashMap<>();

        if (game.getAlliances() != null) {
            for (NationalAlliance a : game.getAlliances()) {
                int aSeats = 0;
                if (a.getMembers() != null) {
                    for (NationalAllianceMember m : a.getMembers()) {
                        String mKey = m.getPartyKey() != null ? m.getPartyKey().toUpperCase() : "";
                        aSeats += allocatedSeats.getOrDefault(mKey, 0);
                    }
                }
                allianceSeatTotals.put(a.getAllianceId(), aSeats);
                allianceNames.put(a.getAllianceId(), a.getAllianceName());
                allianceColors.put(a.getAllianceId(), a.getColor() != null ? a.getColor() : "#38bdf8");
            }
        }

        // If player alliance not already tallied
        if (!allianceSeatTotals.containsKey(playerAllianceId)) {
            allianceSeatTotals.put(playerAllianceId, playerAllianceSeats);
            allianceNames.put(playerAllianceId, playerAllianceName);
            allianceColors.put(playerAllianceId, playerAlliance != null && playerAlliance.getColor() != null ? playerAlliance.getColor() : "#10b981");
        } else {
            allianceSeatTotals.put(playerAllianceId, playerAllianceSeats);
        }

        // Find Winning Alliance
        String topAllianceId = playerAllianceId;
        int maxSeats = -1;
        for (Map.Entry<String, Integer> entry : allianceSeatTotals.entrySet()) {
            if (entry.getValue() > maxSeats) {
                maxSeats = entry.getValue();
                topAllianceId = entry.getKey();
            }
        }

        // Majority rule: does any alliance have >= 272?
        String majorityAllianceId = null;
        for (Map.Entry<String, Integer> entry : allianceSeatTotals.entrySet()) {
            if (entry.getValue() >= 272) {
                majorityAllianceId = entry.getKey();
                break;
            }
        }

        String winningAllianceId = majorityAllianceId != null ? majorityAllianceId : topAllianceId;
        String winningAllianceName = allianceNames.getOrDefault(winningAllianceId, winningAllianceId);

        // Win evaluation: player alliance >= 272 seats -> player wins!
        // At turn 60 scheduled election: if player alliance has >= 272, or is in power and has the most seats -> player wins!
        boolean isPlayerVictory = (playerAllianceSeats >= 272)
            || (winningAllianceId.equalsIgnoreCase(playerAllianceId) && playerAllianceSeats >= 272)
            || ("TURN_60_SCHEDULED_ELECTION".equals(triggerReason) && game.isPlayerInPower() && winningAllianceId.equalsIgnoreCase(playerAllianceId));

        game.setWinnerAllianceKey(winningAllianceId);
        game.setPlayerVictory(isPlayerVictory);
        game.setStatus(isPlayerVictory ? "COMPLETED_VICTORY" : "COMPLETED_DEFEATED");
        game.setRulingAllianceKey(winningAllianceId);

        // Build breakdowns for UI
        List<Map<String, Object>> partyBreakdownList = new ArrayList<>();
        for (NationalPartyState p : game.getPartyStates()) {
            String pKey = p.getPartyKey().toUpperCase();
            int won = allocatedSeats.getOrDefault(pKey, p.getSeats());
            int prev = currentProjected.getOrDefault(pKey, p.getSeats());
            int delta = won - prev;

            Map<String, Object> pMap = new HashMap<>();
            pMap.put("partyKey", p.getPartyKey());
            pMap.put("partyName", p.getPartyName());
            pMap.put("shortName", p.getShortName());
            pMap.put("color", p.getColor());
            pMap.put("seatsWon", won);
            pMap.put("projectedSeats", prev);
            pMap.put("seatDelta", delta);
            pMap.put("morale", p.getMorale());
            pMap.put("funds", p.getFunds());
            pMap.put("workers", p.getWorkers());
            pMap.put("corruption", p.getCorruption());
            pMap.put("isPlayerParty", p.isPlayerParty());
            pMap.put("allianceId", p.getCurrentAllianceId());
            partyBreakdownList.add(pMap);
        }

        List<Map<String, Object>> allianceBreakdownList = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : allianceSeatTotals.entrySet()) {
            String aId = entry.getKey();
            int aSeats = entry.getValue();
            Map<String, Object> aMap = new HashMap<>();
            aMap.put("allianceId", aId);
            aMap.put("allianceName", allianceNames.getOrDefault(aId, aId));
            aMap.put("color", allianceColors.getOrDefault(aId, "#64748b"));
            aMap.put("totalSeats", aSeats);
            aMap.put("hasMajority", aSeats >= 272);
            aMap.put("isPlayerAlliance", aId.equalsIgnoreCase(playerAllianceId));
            allianceBreakdownList.add(aMap);
        }

        String headline;
        String narrative;
        if (isPlayerVictory) {
            headline = "⚡ MANDATE " + (2024 + game.getCurrentSeason() / 12) + ": "
                + playerAllianceName.toUpperCase() + " CLAIMS ABSOLUTE MAJORITY WITH " + playerAllianceSeats + " SEATS!";
            narrative = "In a stunning nationwide democratic victory, " + playerAllianceName
                + " crossed the magic 272-seat mark, capturing " + playerAllianceSeats + " Lok Sabha seats. "
                + "The coalition has successfully formed the Union Government in New Delhi.";
        } else {
            headline = "⚡ MANDATE " + (2024 + game.getCurrentSeason() / 12) + ": "
                + winningAllianceName.toUpperCase() + " WINS LOK SABHA POWER WITH " + allianceSeatTotals.getOrDefault(winningAllianceId, 0) + " SEATS.";
            narrative = "The electorate delivered a decisive verdict. " + winningAllianceName
                + " secured the federal government with " + allianceSeatTotals.getOrDefault(winningAllianceId, 0) + " seats. "
                + playerAllianceName + " fell short of the 272-seat majority threshold (" + playerAllianceSeats + " seats).";
        }

        Map<String, Object> result = new HashMap<>();
        result.put("triggerReason", triggerReason);
        result.put("season", game.getCurrentSeason());
        result.put("totalSeats", 543);
        result.put("majorityThreshold", 272);
        result.put("isPlayerVictory", isPlayerVictory);
        result.put("winningAllianceKey", winningAllianceId);
        result.put("winningAllianceName", winningAllianceName);
        result.put("winningAllianceSeats", allianceSeatTotals.getOrDefault(winningAllianceId, 0));
        result.put("playerAllianceKey", playerAllianceId);
        result.put("playerAllianceName", playerAllianceName);
        result.put("playerAllianceSeats", playerAllianceSeats);
        result.put("headline", headline);
        result.put("narrative", narrative);
        result.put("partyBreakdown", partyBreakdownList);
        result.put("allianceBreakdown", allianceBreakdownList);

        game.setNationalElectionResult(result);

        if (playerAlliance != null) {
            logEntry(playerAlliance, game.getCurrentSeason(), "NATIONAL_ELECTION_CONCLUDED", headline);
        }
    }

    public NationalGame playFinanceCard(String gameId, String cardId) {
        NationalGame game = findGame(gameId);
        if (game.getCommittedFinanceCard() != null) {
            throw new RuntimeException("A finance operation card has already been committed this season. It will be evaluated when advancing the season.");
        }
        NationalFinanceCardDefinition card = NationalFinanceCardDefinition.findById(cardId);
        if (card == null) {
            throw new RuntimeException("Invalid finance card: " + cardId);
        }
        game.setCommittedFinanceCard(card.getId());
        game.setUpdatedAt(Instant.now().toString());
        return repository.save(game);
    }

    public NationalGame cancelFinanceCard(String gameId) {
        NationalGame game = findGame(gameId);
        game.setCommittedFinanceCard(null);
        game.setUpdatedAt(Instant.now().toString());
        return repository.save(game);
    }


    public NationalGame processAiRequests(String gameId) {
        NationalGame game = findGame(gameId);
        NationalAlliance alliance = game.findPlayerAlliance(game.getPartyKey());
        
        if (alliance != null) {
            for (NationalPartyState party : game.getPartyStates()) {
                if (party.getCurrentAllianceId() == null && !party.isPlayerParty()) {
                    if (party.getMorale() < 50) {
                        double chance = party.getMorale() < 35 ? 0.6 : 0.25;
                        if (Math.random() < chance) {
                            NationalCoalitionRequest req = new NationalCoalitionRequest();
                            req.setRequestId(UUID.randomUUID().toString());
                            req.setDirection("INCOMING");
                            req.setFromPartyKey(party.getPartyKey());
                            req.setToAllianceId(alliance.getAllianceId());
                            req.setRequestedJoiningBonus(Math.max(0.5, Math.round((party.getSeats() * 0.1) * 10.0) / 10.0));
                            req.setRequestedRecurringPerSeason(Math.max(0.1, Math.round((party.getSeats() * 0.03) * 10.0) / 10.0));
                            req.setRequestedCabinetMinisters(Math.max(1, party.getSeats() / 15));
                            req.setRequestedStateMinisters(Math.max(1, party.getSeats() / 8));
                            req.setStatus("PENDING");
                            req.setCreatedAtSeason(game.getCurrentSeason());
                            
                            game.getPendingRequests().add(req);
                            logEntry(alliance, game.getCurrentSeason(), "REQUEST_RECEIVED", "Received coalition request from " + resolveTargetName(party));
                        }
                    }
                }
            }
        }
        
        game.setUpdatedAt(Instant.now().toString());
        return repository.save(game);
    }

    public List<Map<String, Object>> getSeasonEvents(String gameId) {
        NationalGame game = findGame(gameId);
        normalizeGameAllianceStates(game);
        boolean isRuling = game.isPlayerInPower();
        List<String> eventIds = game.getCurrentSeasonEventIds();
        if (eventIds == null || eventIds.isEmpty()) {
            List<com.politicalsim.content.NationalEvent> evts = nationalEventRepository.findByEraAndSeason(game.getEra(), game.getCurrentSeason());
            if (evts == null || evts.isEmpty()) evts = nationalEventRepository.findByEra(game.getEra());
            if (evts != null && !evts.isEmpty()) {
                eventIds = new ArrayList<>();
                for (com.politicalsim.content.NationalEvent e : evts) eventIds.add(e.getId());
                game.setCurrentSeasonEventIds(eventIds);
                repository.save(game);
            }
        }
        if (eventIds == null) return Collections.emptyList();

        List<Map<String, Object>> result = new ArrayList<>();
        for (String eId : eventIds) {
            com.politicalsim.content.NationalEvent event = nationalEventRepository.findById(eId).orElse(null);
            if (event != null) {
                Map<String, Object> map = new HashMap<>();
                map.put("id", event.getId());
                map.put("eventKey", event.getEventKey());
                map.put("title", event.getTitle());
                map.put("type", event.getType());
                map.put("icon", event.getIcon());
                map.put("summary", event.getSummary());
                map.put("narrative", event.getNarrative());
                map.put("contextualEffects", event.getContextualEffects());
                map.put("isRulingPlayer", isRuling);
                map.put("playerRole", isRuling ? "RULING" : "OPPOSITION");
                map.put("rulingAllianceKey", game.getRulingAllianceKey());
                map.put("options", isRuling ? event.getRulingReactionOptions() : event.getOppositionReactionOptions());
                map.put("selectedOptionId", game.getResolvedEventReactions() != null ? game.getResolvedEventReactions().get(event.getId()) : null);
                result.add(map);
            }
        }
        return result;
    }

    public Map<String, Object> getSeasonThemes(String gameId) {
        NationalGame game = findGame(gameId);
        normalizeGameAllianceStates(game);
        List<com.politicalsim.content.NationalTheme> allThemes = nationalThemeRepository.findByActiveErasContaining(game.getEra());
        if (allThemes == null || allThemes.isEmpty()) {
            allThemes = nationalThemeRepository.findAll();
        }
        boolean isRuling = game.isPlayerInPower();

        // Separate or prioritize themes based on whether player is in government or opposition
        List<com.politicalsim.content.NationalTheme> activeDeck = allThemes.stream()
            .filter(t -> {
                String type = t.getThemeType() != null ? t.getThemeType() : "AGITATION";
                if (isRuling) {
                    return "GOVERNANCE".equalsIgnoreCase(type) || "DEVELOPMENT".equalsIgnoreCase(t.getCategory());
                } else {
                    return !"GOVERNANCE".equalsIgnoreCase(type);
                }
            })
            .collect(java.util.stream.Collectors.toList());

        if (activeDeck.isEmpty()) {
            activeDeck = allThemes;
        }

        Map<String, Object> response = new HashMap<>();
        response.put("themes", activeDeck);
        response.put("allThemes", allThemes);
        response.put("isPlayerInPower", isRuling);
        response.put("activeThemeKey", game.getActiveThemeKey());
        response.put("activeThemeAction", game.getActiveThemeAction());
        response.put("targetPartyKey", game.getTargetPartyKey());
        response.put("themeTargetReport", game.getThemeTargetReport());
        response.put("themePersistenceStreak", game.getThemePersistenceStreak());
        response.put("lastThemeKey", game.getLastThemeKey());
        response.put("mediaSocialSpend", game.getMediaSocialSpend());
        response.put("mediaSocialReport", game.getMediaSocialReport());
        response.put("mediaSocialCommitted", game.isMediaSocialCommitted());
        return response;
    }

    public NationalGame respondToEvent(String gameId, String eventId, String optionId) {
        NationalGame game = findGame(gameId);
        if (game.getResolvedEventReactions() == null) {
            game.setResolvedEventReactions(new HashMap<>());
        }
        if (game.getResolvedEventReactions().containsKey(eventId)) {
            throw new RuntimeException("Decision has already been committed for this event and is locked for this season.");
        }
        com.politicalsim.content.NationalEvent event = nationalEventRepository.findById(eventId)
            .orElseThrow(() -> new RuntimeException("Event not found: " + eventId));
        boolean isRuling = game.isPlayerInPower();
        List<Map<String, Object>> options = isRuling ? event.getRulingReactionOptions() : event.getOppositionReactionOptions();
        boolean valid = options != null && options.stream().anyMatch(o -> optionId.equals(o.get("optionId")) || optionId.equals(o.get("id")));
        if (!valid) {
            throw new RuntimeException("Invalid option '" + optionId + "' for player role: " + (isRuling ? "RULING" : "OPPOSITION"));
        }
        game.getResolvedEventReactions().put(eventId, optionId);
        game.setUpdatedAt(Instant.now().toString());
        refreshStrategicHints(game);
        return repository.save(game);
    }

    public NationalGame setTargetParty(String gameId, String targetPartyKey) {
        NationalGame game = findGame(gameId);
        game.setTargetPartyKey(targetPartyKey);
        game.setUpdatedAt(Instant.now().toString());
        refreshStrategicHints(game);
        return repository.save(game);
    }

    public NationalGame chooseThemeAction(String gameId, String themeKey, String actionKey, String targetPartyKey) {
        NationalGame game = findGame(gameId);
        if (game.getActiveThemeAction() != null) {
            throw new RuntimeException("A campaign theme action has already been committed and is locked for this season.");
        }
        if (themeKey != null) {
            com.politicalsim.content.NationalTheme theme = nationalThemeRepository.findById(themeKey)
                .orElseGet(() -> nationalThemeRepository.findAll().stream()
                    .filter(t -> themeKey.equalsIgnoreCase(t.getThemeKey()) || themeKey.equalsIgnoreCase(t.getId()))
                    .findFirst().orElse(null));
            if (theme == null) {
                throw new RuntimeException("Theme not found: " + themeKey);
            }
            if (actionKey != null && (theme.getActionEffects() == null || !theme.getActionEffects().containsKey(actionKey))) {
                throw new RuntimeException("Invalid action '" + actionKey + "' for theme: " + themeKey);
            }
        }
        game.setActiveThemeKey(themeKey);
        game.setActiveThemeAction(actionKey);
        if (targetPartyKey != null && !targetPartyKey.trim().isEmpty()) {
            game.setTargetPartyKey(targetPartyKey);
        }
        game.setUpdatedAt(Instant.now().toString());
        refreshStrategicHints(game);
        return repository.save(game);
    }

    public NationalGame chooseThemeAction(String gameId, String themeKey, String actionKey) {
        return chooseThemeAction(gameId, themeKey, actionKey, null);
    }

    public NationalGame allocateMediaSocial(String gameId, Map<String, Double> allocations, boolean commit) {
        NationalGame game = findGame(gameId);
        if (allocations == null) allocations = new HashMap<>();

        double totalSpend = 0.0;
        for (Double v : allocations.values()) {
            if (v != null && v > 0) totalSpend += v;
        }
        totalSpend = Math.round(totalSpend * 10.0) / 10.0;

        NationalPartyState playerState = game.findPartyState(game.getPartyKey());
        double curFunds = playerState != null ? playerState.getFunds() : game.getPlayerFunds();
        if (totalSpend > curFunds) {
            throw new RuntimeException("Insufficient treasury funds! Allocating ₹" + totalSpend + " Cr requires more than available reserves of ₹" + curFunds + " Cr.");
        }

        game.setMediaSocialSpend(allocations);
        game.setMediaSocialCommitted(commit);

        Map<String, Object> preview = evaluateMediaSocialPreview(game, allocations, totalSpend);
        game.setMediaSocialReport(preview);

        game.setUpdatedAt(Instant.now().toString());
        refreshStrategicHints(game);
        return repository.save(game);
    }

    public NationalGame cancelMediaSocial(String gameId) {
        NationalGame game = findGame(gameId);
        game.setMediaSocialSpend(new HashMap<>());
        game.setMediaSocialCommitted(false);
        game.setMediaSocialReport(new HashMap<>());
        game.setUpdatedAt(Instant.now().toString());
        refreshStrategicHints(game);
        return repository.save(game);
    }

    private Map<String, Object> evaluateMediaSocialPreview(NationalGame game, Map<String, Double> allocations, double totalSpend) {
        Map<String, Object> rep = new HashMap<>();
        rep.put("totalSpend", totalSpend);

        double effectiveSpend = 0.0;
        boolean hasExcessiveChannel = false;
        String topChannel = "Social Ads";
        double maxChannelSpend = 0.0;

        for (Map.Entry<String, Double> e : allocations.entrySet()) {
            double sp = e.getValue() != null ? e.getValue() : 0.0;
            if (sp > maxChannelSpend) {
                maxChannelSpend = sp;
                topChannel = e.getKey().replace('_', ' ').toUpperCase();
            }
            if (sp <= 3.0) {
                effectiveSpend += sp;
            } else {
                hasExcessiveChannel = true;
                effectiveSpend += 3.0 + Math.pow(sp - 3.0, 0.6);
            }
        }
        effectiveSpend = Math.round(effectiveSpend * 10.0) / 10.0;
        rep.put("effectiveSpend", effectiveSpend);

        boolean excessiveTotalSpend = totalSpend > 6.0;
        rep.put("excessiveSpend", excessiveTotalSpend);
        rep.put("saturationWarning", hasExcessiveChannel || excessiveTotalSpend);

        double viralOdds = 0.18;
        if (maxChannelSpend >= 2.5) viralOdds += 0.07;
        if (game.getResolvedEventReactions() != null && !game.getResolvedEventReactions().isEmpty()) {
            viralOdds += 0.10;
        }
        if (game.getActiveThemeAction() != null) {
            viralOdds += 0.10;
        }
        viralOdds = Math.min(0.45, Math.round(viralOdds * 100.0) / 100.0);
        rep.put("viralOdds", viralOdds);
        rep.put("topChannel", topChannel);

        int estWorkers = (int) Math.round(effectiveSpend * 4000);
        int estVolunteers = (int) Math.round(effectiveSpend * 2200);
        rep.put("estimatedWorkers", estWorkers);
        rep.put("estimatedVolunteers", estVolunteers);
        return rep;
    }

    public Optional<NationalGame> getGame(String userId) {
        Optional<NationalGame> opt = repository.findFirstByUserIdAndStatusOrderByCreatedAtDesc(userId, "ACTIVE")
            .or(() -> repository.findByUserIdAndStatus(userId, "ACTIVE"));
        opt.ifPresent(this::normalizeGameAllianceStates);
        return opt;
    }

    private void normalizeGameAllianceStates(NationalGame game) {
        if (game == null || game.getPartyStates() == null) return;
        boolean modified = false;

        // Backfill startingFunds for party states if previously uninitialized
        for (NationalPartyState p : game.getPartyStates()) {
            if (p.getStartingFunds() <= 0 && p.getFunds() > 0) {
                p.setStartingFunds(p.getFunds());
                modified = true;
            }
        }

        if (game.getVisibleFinanceCardIds() == null || game.getVisibleFinanceCardIds().isEmpty()) {
            game.setVisibleFinanceCardIds(NationalFinanceCardDefinition.pickRandomVisibleCardIds(6));
            modified = true;
        }

        if (game.getRulingAllianceKey() == null) {
            game.setRulingAllianceKey(game.determineRulingAllianceKey());
            modified = true;
        }

        if (game.getResolvedEventReactions() == null) {
            game.setResolvedEventReactions(new HashMap<>());
            modified = true;
        }

        if (game.getCurrentSeasonEventIds() == null || game.getCurrentSeasonEventIds().isEmpty()) {
            List<com.politicalsim.content.NationalEvent> initEvts = nationalEventRepository.findByEraAndSeason(game.getEra(), game.getCurrentSeason());
            if (initEvts == null || initEvts.isEmpty()) {
                initEvts = nationalEventRepository.findByEra(game.getEra());
            }
            if (initEvts != null && !initEvts.isEmpty()) {
                List<String> evtIds = new ArrayList<>();
                for (com.politicalsim.content.NationalEvent e : initEvts) {
                    evtIds.add(e.getId());
                }
                game.setCurrentSeasonEventIds(evtIds);
                modified = true;
            }
        }

        if (game.getCurrentSeason() <= 1 && (game.getAlliances() == null || game.getAlliances().isEmpty())) {
            for (NationalPartyState p : game.getPartyStates()) {
                if (p.getCurrentAllianceId() == null && p.getPreSeededAllianceKey() != null) {
                    String seed = p.getPreSeededAllianceKey();
                    if (!seed.equalsIgnoreCase("UNALIGNED") && !seed.equalsIgnoreCase("INDEPENDENT")) {
                        p.setCurrentAllianceId(seed);
                        modified = true;
                    }
                }
            }
        }

        if (game.getStateOperations() == null || game.getStateOperations().isEmpty()) {
            initializeStateOperations(game);
            modified = true;
        }

        if (modified) {
            try {
                repository.save(game);
            } catch (Exception ignored) {}
        }
    }

    private void logEntry(NationalAlliance alliance, int season, String event, String detail) {
        NationalActivityLogEntry entry = new NationalActivityLogEntry();
        entry.setSeason(season);
        entry.setEvent(event);
        entry.setDetail(detail);
        entry.setTimestamp(Instant.now().toString());
        alliance.getActivityLog().add(0, entry);
        if (alliance.getActivityLog().size() > 50) {
            alliance.getActivityLog().subList(50, alliance.getActivityLog().size()).clear();
        }
    }

    // ─────────────────────────────────────────────────────────────────────────
    // STATE OPERATIONS ENGINE (UP, BIHAR, MAHARASHTRA)
    // ─────────────────────────────────────────────────────────────────────────

    public void initializeStateOperations(NationalGame game) {
        if (game == null) return;
        if (game.getStateOperations() == null) {
            game.setStateOperations(new HashMap<>());
        }
        Map<String, NationalStateOperationState> ops = game.getStateOperations();
        String playerKey = (game.getPartyKey() != null ? game.getPartyKey() : "YDP").toUpperCase();

        if (!ops.containsKey("UP")) {
            NationalStateOperationState up = new NationalStateOperationState();
            up.setStateCode("UP");
            up.setStateName("Uttar Pradesh");
            up.setScenarioKey("uttar_pradesh_2001");
            up.setRulingParty("BJP");
            up.setOppositionParty("SP");
            up.setTotalLokSabhaSeats(80);
            up.setTotalAssemblySeats(403);
            up.setElectionTurn(15);
            up.setElectionMonth("March 2002");
            up.setStateFunds(6.0);
            up.setStateWorkers(35000);
            up.setStateVolunteers(18000);
            up.setStateDonors(850);
            Map<String, Double> upVotes = new HashMap<>();
            upVotes.put("BJP", 34.0);
            upVotes.put("SP", 30.0);
            upVotes.put("BSP", 16.0);
            upVotes.put("INC", 10.0);
            upVotes.put("RLD", 3.0);
            if (!upVotes.containsKey(playerKey)) {
                upVotes.put(playerKey, 0.0);
            }
            upVotes.put("UNDECIDED", 10.0);
            up.setVoteSplits(upVotes);
            initUttarPradeshRegions(up, playerKey);
            up.updateElectionPhase(game.getCurrentSeason());
            recalculateProjectedSeats(up);
            up.setBaselineVoteSplits(new HashMap<>(upVotes));
            up.setBaselineLokSabhaSeats(new HashMap<>(up.getProjectedLokSabhaSeats()));
            ops.put("UP", up);
        } else {
            NationalStateOperationState existingUp = ops.get("UP");
            if (existingUp != null && (existingUp.getRegions() == null || existingUp.getRegions().isEmpty())) {
                initUttarPradeshRegions(existingUp, playerKey);
            }
        }

        if (!ops.containsKey("BIHAR")) {
            NationalStateOperationState bihar = new NationalStateOperationState();
            bihar.setStateCode("BIHAR");
            bihar.setStateName("Bihar");
            bihar.setScenarioKey("bihar_2001");
            bihar.setRulingParty("JD(U)");
            bihar.setOppositionParty("RJD");
            bihar.setTotalLokSabhaSeats(40);
            bihar.setTotalAssemblySeats(243);
            bihar.setElectionTurn(50);
            bihar.setElectionMonth("February 2005");
            bihar.setStateFunds(4.5);
            bihar.setStateWorkers(22000);
            bihar.setStateVolunteers(11000);
            bihar.setStateDonors(600);
            Map<String, Double> biharVotes = new HashMap<>();
            biharVotes.put("JD(U)", 38.0);
            biharVotes.put("BJP", 26.0);
            biharVotes.put("RJD", 16.0);
            biharVotes.put("INC", 7.0);
            if (!biharVotes.containsKey(playerKey)) {
                biharVotes.put(playerKey, 0.0);
            }
            biharVotes.put("UNDECIDED", 10.0);
            bihar.setVoteSplits(biharVotes);
            initBiharRegions(bihar, playerKey);
            bihar.updateElectionPhase(game.getCurrentSeason());
            recalculateProjectedSeats(bihar);
            bihar.setBaselineVoteSplits(new HashMap<>(biharVotes));
            bihar.setBaselineLokSabhaSeats(new HashMap<>(bihar.getProjectedLokSabhaSeats()));
            ops.put("BIHAR", bihar);
        } else {
            NationalStateOperationState existingBihar = ops.get("BIHAR");
            if (existingBihar != null && (existingBihar.getRegions() == null || existingBihar.getRegions().isEmpty())) {
                initBiharRegions(existingBihar, playerKey);
            }
        }

        if (!ops.containsKey("MAHARASHTRA")) {
            NationalStateOperationState mh = new NationalStateOperationState();
            mh.setStateCode("MAHARASHTRA");
            mh.setStateName("Maharashtra");
            mh.setScenarioKey("maharashtra_2001");
            mh.setRulingParty("INC");
            mh.setOppositionParty("SHS");
            mh.setTotalLokSabhaSeats(48);
            mh.setTotalAssemblySeats(288);
            mh.setElectionTurn(46);
            mh.setElectionMonth("October 2004");
            mh.setStateFunds(5.5);
            mh.setStateWorkers(28000);
            mh.setStateVolunteers(14000);
            mh.setStateDonors(750);
            Map<String, Double> mhVotes = new HashMap<>();
            mhVotes.put("BJP", 25.0);
            mhVotes.put("SHS", 24.0);
            mhVotes.put("INC", 22.0);
            mhVotes.put("NCP", 17.0);
            if (!mhVotes.containsKey(playerKey)) {
                mhVotes.put(playerKey, 0.0);
            }
            mhVotes.put("UNDECIDED", 10.0);
            mh.setVoteSplits(mhVotes);
            initMaharashtraRegions(mh, playerKey);
            mh.updateElectionPhase(game.getCurrentSeason());
            recalculateProjectedSeats(mh);
            mh.setBaselineVoteSplits(new HashMap<>(mhVotes));
            mh.setBaselineLokSabhaSeats(new HashMap<>(mh.getProjectedLokSabhaSeats()));
            ops.put("MAHARASHTRA", mh);
        } else {
            NationalStateOperationState existingMh = ops.get("MAHARASHTRA");
            if (existingMh != null && (existingMh.getRegions() == null || existingMh.getRegions().isEmpty())) {
                initMaharashtraRegions(existingMh, playerKey);
            }
        }

        if (!ops.containsKey("WEST_BENGAL")) {
            NationalStateOperationState wb = new NationalStateOperationState();
            wb.setStateCode("WEST_BENGAL");
            wb.setStateName("West Bengal");
            wb.setScenarioKey("west_bengal_2001");
            wb.setRulingParty("CPIM");
            wb.setOppositionParty("AITC");
            wb.setTotalLokSabhaSeats(42);
            wb.setTotalAssemblySeats(294);
            wb.setElectionTurn(5);
            wb.setElectionMonth("May 2001");
            wb.setStateFunds(5.0);
            wb.setStateWorkers(32000);
            wb.setStateVolunteers(16000);
            wb.setStateDonors(700);
            Map<String, Double> wbVotes = new HashMap<>();
            wbVotes.put("CPIM", 44.0);
            wbVotes.put("AITC", 31.0);
            wbVotes.put("INC", 9.0);
            wbVotes.put("BJP", 6.0);
            if (!wbVotes.containsKey(playerKey)) {
                wbVotes.put(playerKey, 0.0);
            }
            wbVotes.put("UNDECIDED", 10.0);
            wb.setVoteSplits(wbVotes);
            initWestBengalRegions(wb, playerKey);
            wb.updateElectionPhase(game.getCurrentSeason());
            recalculateProjectedSeats(wb);
            wb.setBaselineVoteSplits(new HashMap<>(wbVotes));
            wb.setBaselineLokSabhaSeats(new HashMap<>(wb.getProjectedLokSabhaSeats()));
            ops.put("WEST_BENGAL", wb);
        } else {
            NationalStateOperationState existingWb = ops.get("WEST_BENGAL");
            if (existingWb != null && (existingWb.getRegions() == null || existingWb.getRegions().isEmpty())) {
                initWestBengalRegions(existingWb, playerKey);
            }
        }

        if (!ops.containsKey("RAJASTHAN")) {
            NationalStateOperationState rj = new NationalStateOperationState();
            rj.setStateCode("RAJASTHAN");
            rj.setStateName("Rajasthan");
            rj.setScenarioKey("rajasthan_2001");
            rj.setRulingParty("INC");
            rj.setOppositionParty("BJP");
            rj.setTotalLokSabhaSeats(25);
            rj.setTotalAssemblySeats(200);
            rj.setElectionTurn(36);
            rj.setElectionMonth("December 2003");
            rj.setStateFunds(4.8);
            rj.setStateWorkers(24000);
            rj.setStateVolunteers(12000);
            rj.setStateDonors(650);
            Map<String, Double> rjVotes = new HashMap<>();
            rjVotes.put("INC", 38.0);
            rjVotes.put("BJP", 36.0);
            rjVotes.put("BSP", 6.0);
            if (!rjVotes.containsKey(playerKey)) {
                rjVotes.put(playerKey, 0.0);
            }
            rjVotes.put("UNDECIDED", 10.0);
            rj.setVoteSplits(rjVotes);
            initRajasthanRegions(rj, playerKey);
            rj.updateElectionPhase(game.getCurrentSeason());
            recalculateProjectedSeats(rj);
            rj.setBaselineVoteSplits(new HashMap<>(rjVotes));
            rj.setBaselineLokSabhaSeats(new HashMap<>(rj.getProjectedLokSabhaSeats()));
            ops.put("RAJASTHAN", rj);
        } else {
            NationalStateOperationState existingRj = ops.get("RAJASTHAN");
            if (existingRj != null && (existingRj.getRegions() == null || existingRj.getRegions().isEmpty())) {
                initRajasthanRegions(existingRj, playerKey);
            }
        }

        if (!ops.containsKey("ASSAM")) {
            NationalStateOperationState as = new NationalStateOperationState();
            as.setStateCode("ASSAM");
            as.setStateName("Assam");
            as.setScenarioKey("assam_2001");
            as.setRulingParty("AGP");
            as.setOppositionParty("INC");
            as.setTotalLokSabhaSeats(14);
            as.setTotalAssemblySeats(126);
            as.setElectionTurn(5);
            as.setElectionMonth("May 2001");
            as.setStateFunds(3.5);
            as.setStateWorkers(18000);
            as.setStateVolunteers(9000);
            as.setStateDonors(450);
            Map<String, Double> asVotes = new HashMap<>();
            asVotes.put("INC", 36.0);
            asVotes.put("AGP", 24.0);
            asVotes.put("BJP", 12.0);
            asVotes.put("AIUDF", 8.0);
            if (!asVotes.containsKey(playerKey)) {
                asVotes.put(playerKey, 0.0);
            }
            asVotes.put("UNDECIDED", 10.0);
            as.setVoteSplits(asVotes);
            initAssamRegions(as, playerKey);
            as.updateElectionPhase(game.getCurrentSeason());
            recalculateProjectedSeats(as);
            as.setBaselineVoteSplits(new HashMap<>(asVotes));
            as.setBaselineLokSabhaSeats(new HashMap<>(as.getProjectedLokSabhaSeats()));
            ops.put("ASSAM", as);
        } else {
            NationalStateOperationState existingAs = ops.get("ASSAM");
            if (existingAs != null && (existingAs.getRegions() == null || existingAs.getRegions().isEmpty())) {
                initAssamRegions(existingAs, playerKey);
            }
        }

        if (!ops.containsKey("TAMIL_NADU")) {
            NationalStateOperationState tn = new NationalStateOperationState();
            tn.setStateCode("TAMIL_NADU");
            tn.setStateName("Tamil Nadu");
            tn.setScenarioKey("tamil_nadu_2001");
            tn.setRulingParty("DMK");
            tn.setOppositionParty("AIADMK");
            tn.setTotalLokSabhaSeats(39);
            tn.setTotalAssemblySeats(234);
            tn.setElectionTurn(5);
            tn.setElectionMonth("May 2001");
            tn.setStateFunds(6.0);
            tn.setStateWorkers(30000);
            tn.setStateVolunteers(15000);
            tn.setStateDonors(800);
            Map<String, Double> tnVotes = new HashMap<>();
            tnVotes.put("AIADMK", 40.0);
            tnVotes.put("DMK", 36.0);
            tnVotes.put("PMK", 6.0);
            tnVotes.put("INC", 5.0);
            tnVotes.put("BJP", 3.0);
            if (!tnVotes.containsKey(playerKey)) {
                tnVotes.put(playerKey, 0.0);
            }
            tnVotes.put("UNDECIDED", 10.0);
            tn.setVoteSplits(tnVotes);
            initTamilNaduRegions(tn, playerKey);
            tn.updateElectionPhase(game.getCurrentSeason());
            recalculateProjectedSeats(tn);
            tn.setBaselineVoteSplits(new HashMap<>(tnVotes));
            tn.setBaselineLokSabhaSeats(new HashMap<>(tn.getProjectedLokSabhaSeats()));
            ops.put("TAMIL_NADU", tn);
        } else {
            NationalStateOperationState existingTn = ops.get("TAMIL_NADU");
            if (existingTn != null && (existingTn.getRegions() == null || existingTn.getRegions().isEmpty())) {
                initTamilNaduRegions(existingTn, playerKey);
            }
        }

        for (NationalStateOperationState s : ops.values()) {
            if (s.getBaselineVoteSplits() == null || s.getBaselineVoteSplits().isEmpty()) {
                if (s.getVoteSplits() != null) {
                    s.setBaselineVoteSplits(new HashMap<>(s.getVoteSplits()));
                }
            }
            if (s.getBaselineLokSabhaSeats() == null || s.getBaselineLokSabhaSeats().isEmpty()) {
                if (s.getProjectedLokSabhaSeats() != null) {
                    s.setBaselineLokSabhaSeats(new HashMap<>(s.getProjectedLokSabhaSeats()));
                }
            }
            boolean eligible = isStateEligibleForPlayer(game, s);
            s.setActive(eligible);
            if (!eligible && !s.isDoneThisTurn()) {
                s.setSkippedThisTurn(true);
            }
        }

        recalculateNationalProjectedSeats(game);
        refreshStrategicHints(game);
    }

    private void initUttarPradeshRegions(NationalStateOperationState up, String playerKey) {
        if (up.getRegions() == null) {
            up.setRegions(new HashMap<>());
        }
        Map<String, RegionalOperationState> regs = up.getRegions();
        double baseSup = up.getVoteSplits() != null ? up.getVoteSplits().getOrDefault(playerKey, 0.0) : 0.0;
        if (!regs.containsKey("paschim_pradesh")) {
            RegionalOperationState r = new RegionalOperationState("paschim_pradesh", "Paschim Pradesh (Western UP)", 26, 136, "Agrarian sugar belt, Jat-Muslim dynamics, high farmer mobilization (BKU), and NCR industrial-urban hubs.");
            r.setSupportPercentage(baseSup);
            regs.put("paschim_pradesh", r);
        }
        if (!regs.containsKey("rohilkhand")) {
            RegionalOperationState r = new RegionalOperationState("rohilkhand", "Rohilkhand & Upper Plains", 10, 52, "Upper Gangetic plains, brass & artisanal handicraft centres, high minority concentration, and intense triangular contests.");
            r.setSupportPercentage(baseSup);
            regs.put("rohilkhand", r);
        }
        if (!regs.containsKey("awadh")) {
            RegionalOperationState r = new RegionalOperationState("awadh", "Awadh (Central UP)", 14, 73, "State capital corridor around Lucknow, administrative hub, and traditional socialist and royal political bastions.");
            r.setSupportPercentage(baseSup);
            regs.put("awadh", r);
        }
        if (!regs.containsKey("bundelkhand")) {
            RegionalOperationState r = new RegionalOperationState("bundelkhand", "Bundelkhand", 4, 19, "Drought-prone rugged southern plateau, severe water distress, agrarian poverty, and strong distinct cultural identity.");
            r.setSupportPercentage(baseSup);
            regs.put("bundelkhand", r);
        }
        if (!regs.containsKey("purvanchal")) {
            RegionalOperationState r = new RegionalOperationState("purvanchal", "Purvanchal (Eastern UP)", 26, 123, "Varanasi-Gorakhpur Bhojpuri heartland, dense rural population, weaver clusters, intense caste polarization, and high out-migration.");
            r.setSupportPercentage(baseSup);
            regs.put("purvanchal", r);
        }
        distributeDefaultCadres(up, regs);
    }

    private void initBiharRegions(NationalStateOperationState bihar, String playerKey) {
        if (bihar.getRegions() == null) {
            bihar.setRegions(new HashMap<>());
        }
        Map<String, RegionalOperationState> regs = bihar.getRegions();
        double baseSup = bihar.getVoteSplits() != null ? bihar.getVoteSplits().getOrDefault(playerKey, 0.0) : 0.0;
        if (!regs.containsKey("tirhut_champaran")) {
            RegionalOperationState r = new RegionalOperationState("tirhut_champaran", "Tirhut & Champaran (North-West Bihar)", 10, 59, "Historic Champaran indigo heartland and Gandak basin; sugar mills, dense agrarian population, and acute flood vulnerability.");
            r.setSupportPercentage(baseSup);
            regs.put("tirhut_champaran", r);
        }
        if (!regs.containsKey("mithilanchal")) {
            RegionalOperationState r = new RegionalOperationState("mithilanchal", "Mithilanchal (North-East Plains)", 8, 50, "Kosi river floodplains, Maithili cultural core around Darbhanga-Madhubani, and intricate social-caste balancing.");
            r.setSupportPercentage(baseSup);
            regs.put("mithilanchal", r);
        }
        if (!regs.containsKey("seemanchal")) {
            RegionalOperationState r = new RegionalOperationState("seemanchal", "Seemanchal (Eastern Border Belt)", 4, 24, "Purnia-Kishanganj corridor bordering Bengal & Nepal; high minority population, chronic erosion, and heavy labor out-migration.");
            r.setSupportPercentage(baseSup);
            regs.put("seemanchal", r);
        }
        if (!regs.containsKey("magadh")) {
            RegionalOperationState r = new RegionalOperationState("magadh", "Magadh (South-Central Bihar)", 10, 60, "State capital corridor around Patna and Gaya; ancient administrative centre, educational hubs, and intense Kurmi-Yadav-Dalit competition.");
            r.setSupportPercentage(baseSup);
            regs.put("magadh", r);
        }
        if (!regs.containsKey("bhojpur_anga")) {
            RegionalOperationState r = new RegionalOperationState("bhojpur_anga", "Bhojpur & Anga (South-West & South-East Bihar)", 8, 50, "Bhojpuri heartland along the Son river combined with Bhagalpur silk belt; rich agrarian heritage and deep political mobilization.");
            r.setSupportPercentage(baseSup);
            regs.put("bhojpur_anga", r);
        }
        distributeDefaultCadres(bihar, regs);
    }

    private void distributeDefaultCadres(NationalStateOperationState state, Map<String, RegionalOperationState> regs) {
        int nRegs = regs.size();
        if (nRegs > 0) {
            int totalAllocWorkers = regs.values().stream().mapToInt(RegionalOperationState::getAllocatedWorkers).sum();
            int totalAllocVols = regs.values().stream().mapToInt(RegionalOperationState::getAllocatedVolunteers).sum();
            if (totalAllocWorkers == 0 && state.getStateWorkers() > 0) {
                int equalWorkers = state.getStateWorkers() / nRegs;
                for (RegionalOperationState r : regs.values()) {
                    r.setAllocatedWorkers(equalWorkers);
                }
            }
            if (totalAllocVols == 0 && state.getStateVolunteers() > 0) {
                int equalVols = state.getStateVolunteers() / nRegs;
                for (RegionalOperationState r : regs.values()) {
                    r.setAllocatedVolunteers(equalVols);
                }
            }
        }
    }

    private void initMaharashtraRegions(NationalStateOperationState mh, String playerKey) {
        if (mh.getRegions() == null) {
            mh.setRegions(new HashMap<>());
        }
        Map<String, RegionalOperationState> regs = mh.getRegions();
        double baseSup = mh.getVoteSplits() != null ? mh.getVoteSplits().getOrDefault(playerKey, 0.0) : 0.0;
        if (!regs.containsKey("vidarbha")) {
            RegionalOperationState r = new RegionalOperationState("vidarbha", "Vidarbha", 10, 62, "Eastern Maharashtra agrarian & cotton belt; high farmer distress with acute political volatility.");
            r.setSupportPercentage(baseSup);
            regs.put("vidarbha", r);
        }
        if (!regs.containsKey("marathwada")) {
            RegionalOperationState r = new RegionalOperationState("marathwada", "Marathwada", 8, 46, "Drought-prone central plateau; intense social mobilization and deep caste competition.");
            r.setSupportPercentage(baseSup);
            regs.put("marathwada", r);
        }
        if (!regs.containsKey("mumbai_konkan")) {
            RegionalOperationState r = new RegionalOperationState("mumbai_konkan", "Greater Mumbai and Konkan", 12, 75, "Financial capital and coastal belt; dense urban infrastructure, high business and media influence.");
            r.setSupportPercentage(baseSup);
            regs.put("mumbai_konkan", r);
        }
        if (!regs.containsKey("north_maharashtra")) {
            RegionalOperationState r = new RegionalOperationState("north_maharashtra", "North Maharashtra and Khandesh", 7, 47, "Khandesh & tribal belt; agricultural produce markets and cooperative banking networks.");
            r.setSupportPercentage(baseSup);
            regs.put("north_maharashtra", r);
        }
        if (!regs.containsKey("western_maharashtra")) {
            RegionalOperationState r = new RegionalOperationState("western_maharashtra", "Western Maharashtra", 11, 58, "Sugar belt and cooperative heartland; prosperous rural institutions and influential political networks.");
            r.setSupportPercentage(baseSup);
            regs.put("western_maharashtra", r);
        }
        distributeDefaultCadres(mh, regs);
    }

    private void initWestBengalRegions(NationalStateOperationState wb, String playerKey) {
        if (wb.getRegions() == null) {
            wb.setRegions(new HashMap<>());
        }
        Map<String, RegionalOperationState> regs = wb.getRegions();
        double baseSup = wb.getVoteSplits() != null ? wb.getVoteSplits().getOrDefault(playerKey, 0.0) : 0.0;
        if (!regs.containsKey("kolkata_urban")) {
            RegionalOperationState r = new RegionalOperationState("kolkata_urban", "Greater Kolkata & South 24 Parganas", 8, 56, "Dense urban metropolis, state intellectual & cultural core, port trade hubs, and Sundarbans delta coastal belt.");
            r.setSupportPercentage(baseSup);
            regs.put("kolkata_urban", r);
        }
        if (!regs.containsKey("burdwan_industrial")) {
            RegionalOperationState r = new RegionalOperationState("burdwan_industrial", "Burdwan, Hooghly & Industrial Belt", 9, 63, "Asansol-Durgapur coal-steel industrial heartland, jute mills along the Hooghly river, and dense trade union mobilization.");
            r.setSupportPercentage(baseSup);
            regs.put("burdwan_industrial", r);
        }
        if (!regs.containsKey("north_bengal")) {
            RegionalOperationState r = new RegionalOperationState("north_bengal", "North Bengal & Dooars", 8, 54, "Darjeeling tea garden estates, Dooars foothills, Siliguri strategic transit corridor, and Koch-Rajbongshi sub-regional dynamics.");
            r.setSupportPercentage(baseSup);
            regs.put("north_bengal", r);
        }
        if (!regs.containsKey("medinipur_junglemahal")) {
            RegionalOperationState r = new RegionalOperationState("medinipur_junglemahal", "Medinipur & Junglemahal", 9, 64, "Southwestern red-soil forests, Santhal tribal belts, rural agricultural cooperatives, and fierce agrarian party strongholds.");
            r.setSupportPercentage(baseSup);
            regs.put("medinipur_junglemahal", r);
        }
        if (!regs.containsKey("murshidabad_nadia")) {
            RegionalOperationState r = new RegionalOperationState("murshidabad_nadia", "Murshidabad, Nadia & Border Plains", 8, 57, "Porous international border belt along Bangladesh, rich silk & handicraft clusters, dense minority population, and riverine erosion.");
            r.setSupportPercentage(baseSup);
            regs.put("murshidabad_nadia", r);
        }
        distributeDefaultCadres(wb, regs);
    }

    private void initRajasthanRegions(NationalStateOperationState rj, String playerKey) {
        if (rj.getRegions() == null) {
            rj.setRegions(new HashMap<>());
        }
        Map<String, RegionalOperationState> regs = rj.getRegions();
        double baseSup = rj.getVoteSplits() != null ? rj.getVoteSplits().getOrDefault(playerKey, 0.0) : 0.0;
        if (!regs.containsKey("marwar_thar")) {
            RegionalOperationState r = new RegionalOperationState("marwar_thar", "Marwar & Thar Desert (Western RJ)", 6, 48, "Jodhpur-Bikaner desert heartland; acute drinking water distress, solar-wind potential, and vocal Rajput-Jat agrarian competition.");
            r.setSupportPercentage(baseSup);
            regs.put("marwar_thar", r);
        }
        if (!regs.containsKey("mewar_vagad")) {
            RegionalOperationState r = new RegionalOperationState("mewar_vagad", "Mewar & Vagad (Southern Tribal Belt)", 5, 40, "Udaipur-Banswara hilly tribal belt (Bhils); strong traditional heritage, zinc-marble mining, and cooperative rural networks.");
            r.setSupportPercentage(baseSup);
            regs.put("mewar_vagad", r);
        }
        if (!regs.containsKey("dhundhar_jaipur")) {
            RegionalOperationState r = new RegionalOperationState("dhundhar_jaipur", "Dhundhar & Jaipur Metropolis", 5, 42, "State capital region, handicraft and gem-jewelry export powerhouse, tourism gateway, and rapid peri-urban expansion.");
            r.setSupportPercentage(baseSup);
            regs.put("dhundhar_jaipur", r);
        }
        if (!regs.containsKey("shekhawati")) {
            RegionalOperationState r = new RegionalOperationState("shekhawati", "Shekhawati & Northern Plains", 4, 34, "Sikar-Jhunjhunu merchant and defense personnel recruitment belt; high rural literacy and influential Jat farmer mobilization.");
            r.setSupportPercentage(baseSup);
            regs.put("shekhawati", r);
        }
        if (!regs.containsKey("haroti_matsya")) {
            RegionalOperationState r = new RegionalOperationState("haroti_matsya", "Hadoti & Matsya (Eastern Belt)", 5, 36, "Kota-Chambal fertile agricultural basin, national education coaching hub, and eastern mustard belt with Gujjar-Meena dynamics.");
            r.setSupportPercentage(baseSup);
            regs.put("haroti_matsya", r);
        }
        distributeDefaultCadres(rj, regs);
    }

    private void initAssamRegions(NationalStateOperationState as, String playerKey) {
        if (as.getRegions() == null) {
            as.setRegions(new HashMap<>());
        }
        Map<String, RegionalOperationState> regs = as.getRegions();
        double baseSup = as.getVoteSplits() != null ? as.getVoteSplits().getOrDefault(playerKey, 0.0) : 0.0;
        if (!regs.containsKey("brahmaputra_upper")) {
            RegionalOperationState r = new RegionalOperationState("brahmaputra_upper", "Upper Assam (Dibrugarh-Jorhat)", 3, 28, "Historic Ahom cultural core, premier tea garden estates, crude oil & gas facilities (Digboi), and vocal student union leadership.");
            r.setSupportPercentage(baseSup);
            regs.put("brahmaputra_upper", r);
        }
        if (!regs.containsKey("brahmaputra_central")) {
            RegionalOperationState r = new RegionalOperationState("brahmaputra_central", "Central Assam & Guwahati Gateway", 3, 26, "Commercial and administrative metropolis, Northeast transit hub, multi-ethnic plains, and rapid urban growth.");
            r.setSupportPercentage(baseSup);
            regs.put("brahmaputra_central", r);
        }
        if (!regs.containsKey("brahmaputra_lower")) {
            RegionalOperationState r = new RegionalOperationState("brahmaputra_lower", "Lower Assam (Dhubri-Barpeta)", 3, 28, "Flood-prone riverine char plains, jute agriculture, dense minority settlements, and acute border-land sensitivity.");
            r.setSupportPercentage(baseSup);
            regs.put("brahmaputra_lower", r);
        }
        if (!regs.containsKey("barak_valley")) {
            RegionalOperationState r = new RegionalOperationState("barak_valley", "Barak Valley (Silchar-Karimganj)", 2, 20, "Bengali-majority southern valley across Borail hills; distinct linguistic identity, tea estates, and cross-border commerce.");
            r.setSupportPercentage(baseSup);
            regs.put("barak_valley", r);
        }
        if (!regs.containsKey("bodoland_hills")) {
            RegionalOperationState r = new RegionalOperationState("bodoland_hills", "Bodoland & Karbi-Dima Hasao Hills", 3, 24, "Autonomous territorial councils under Sixth Schedule; Bodo, Karbi, and Dimasa indigenous tribal aspirations and forest hills.");
            r.setSupportPercentage(baseSup);
            regs.put("bodoland_hills", r);
        }
        distributeDefaultCadres(as, regs);
    }

    private void initTamilNaduRegions(NationalStateOperationState tn, String playerKey) {
        if (tn.getRegions() == null) {
            tn.setRegions(new HashMap<>());
        }
        Map<String, RegionalOperationState> regs = tn.getRegions();
        double baseSup = tn.getVoteSplits() != null ? tn.getVoteSplits().getOrDefault(playerKey, 0.0) : 0.0;
        if (!regs.containsKey("chennai_north_corridor")) {
            RegionalOperationState r = new RegionalOperationState("chennai_north_corridor", "Chennai Metro & Northern Coast", 8, 48, "Automotive manufacturing hub ('Detroit of Asia'), port logistics, film & media capital, and organized working-class voters.");
            r.setSupportPercentage(baseSup);
            regs.put("chennai_north_corridor", r);
        }
        if (!regs.containsKey("kongu_nadu")) {
            RegionalOperationState r = new RegionalOperationState("kongu_nadu", "Kongu Nadu (Western Tamil Nadu)", 8, 50, "Coimbatore-Tirupur textile export powerhouse, engineering MSMEs, poultry farms, and strong Gounder agrarian community networks.");
            r.setSupportPercentage(baseSup);
            regs.put("kongu_nadu", r);
        }
        if (!regs.containsKey("cauvery_delta")) {
            RegionalOperationState r = new RegionalOperationState("cauvery_delta", "Cauvery Delta (Thanjavur-Trichy)", 8, 46, "Historic rice bowl of Tamil Nadu, Dravidian ideological heartland, ancient temple towns, and acute interstate water sharing distress.");
            r.setSupportPercentage(baseSup);
            regs.put("cauvery_delta", r);
        }
        if (!regs.containsKey("madurai_south")) {
            RegionalOperationState r = new RegionalOperationState("madurai_south", "Madurai & Southern Plains", 8, 48, "Cultural and spiritual epicentre of Tamil language; agriculture, Thevar-Dalit caste polarization, and passionate political mobilization.");
            r.setSupportPercentage(baseSup);
            regs.put("madurai_south", r);
        }
        if (!regs.containsKey("coastal_kanyakumari")) {
            RegionalOperationState r = new RegionalOperationState("coastal_kanyakumari", "Coastal South & Western Ghats", 7, 42, "Tirunelveli-Kanyakumari corridor; wind energy fields, fishing hamlets, rubber plantations, and diverse multi-faith demographics.");
            r.setSupportPercentage(baseSup);
            regs.put("coastal_kanyakumari", r);
        }
        distributeDefaultCadres(tn, regs);
    }

    public void syncRegionalSupportToStateVoteSplits(NationalStateOperationState state, String playerKey) {
        if (state == null || state.getRegions() == null || state.getRegions().isEmpty()) return;
        int totalSeats = 0;
        double weightedSupport = 0.0;
        for (RegionalOperationState r : state.getRegions().values()) {
            int seats = r.getLokSabhaSeats() > 0 ? r.getLokSabhaSeats() : 1;
            totalSeats += seats;
            weightedSupport += r.getSupportPercentage() * seats;
        }
        if (totalSeats > 0) {
            double avg = Math.round((weightedSupport / totalSeats) * 10.0) / 10.0;
            if (state.getVoteSplits() != null) {
                state.getVoteSplits().put(playerKey, avg);
                state.normalizeVoteSplits();
            }
        }
    }

    public void recalculateProjectedSeats(NationalStateOperationState state) {
        if (state == null || state.getVoteSplits() == null) return;
        Map<String, Double> votes = state.getVoteSplits();
        int totalSeats = state.getTotalLokSabhaSeats();
        Map<String, Integer> projected = new HashMap<>();
        double totalPartyVotes = 0.0;
        for (Map.Entry<String, Double> e : votes.entrySet()) {
            if (!"UNDECIDED".equalsIgnoreCase(e.getKey()) && e.getValue() != null) {
                totalPartyVotes += e.getValue();
            }
        }
        if (totalPartyVotes <= 0) return;
        int assignedSeats = 0;
        String topParty = null;
        double topShare = -1.0;
        for (Map.Entry<String, Double> e : votes.entrySet()) {
            if ("UNDECIDED".equalsIgnoreCase(e.getKey())) continue;
            int seats = (int) Math.round((e.getValue() / totalPartyVotes) * totalSeats);
            projected.put(e.getKey(), seats);
            assignedSeats += seats;
            if (e.getValue() > topShare) {
                topShare = e.getValue();
                topParty = e.getKey();
            }
        }
        int diff = totalSeats - assignedSeats;
        if (topParty != null && diff != 0) {
            projected.put(topParty, Math.max(0, projected.getOrDefault(topParty, 0) + diff));
        }
        state.setProjectedLokSabhaSeats(projected);
    }

    public void recalculateNationalProjectedSeats(NationalGame game) {
        if (game == null) return;
        Map<String, Integer> nationalProj = new HashMap<>();

        if (game.getPartyStates() != null) {
            for (NationalPartyState p : game.getPartyStates()) {
                String k = p.getPartyKey() != null ? p.getPartyKey().toUpperCase() : "";
                nationalProj.put(k, p.getSeats());
            }
        }

        if (game.getStateOperations() != null) {
            Map<String, Integer> netDeltas = new HashMap<>();
            for (NationalStateOperationState s : game.getStateOperations().values()) {
                Map<String, Integer> currentSeats = s.getProjectedLokSabhaSeats();
                Map<String, Integer> baseSeats = s.getBaselineLokSabhaSeats();
                if (currentSeats != null) {
                    for (Map.Entry<String, Integer> entry : currentSeats.entrySet()) {
                        String party = entry.getKey().toUpperCase();
                        int cur = entry.getValue() != null ? entry.getValue() : 0;
                        int base = (baseSeats != null && baseSeats.containsKey(party)) ? baseSeats.get(party) : cur;
                        int delta = cur - base;
                        netDeltas.put(party, netDeltas.getOrDefault(party, 0) + delta);
                    }
                }
            }
            for (Map.Entry<String, Integer> d : netDeltas.entrySet()) {
                String party = d.getKey();
                int currentNat = nationalProj.getOrDefault(party, 0);
                nationalProj.put(party, Math.max(0, currentNat + d.getValue()));
            }
        }

        game.setNationalProjectedSeats(nationalProj);

        // Synchronize projected seats, momentum flag, and per-turn donation on all party states
        if (game.getPartyStates() != null) {
            for (NationalPartyState p : game.getPartyStates()) {
                String k = p.getPartyKey() != null ? p.getPartyKey().toUpperCase() : "";
                int proj = nationalProj.getOrDefault(k, p.getSeats());
                p.setProjectedSeats(proj);
                boolean momentum = isPartyGainingMomentum(game, p);
                p.setGainingMomentum(momentum);
                p.setDonationsPerTurn(calculatePartyDonation(game, p));
            }
        }
    }

    public boolean isPartyGainingMomentum(NationalGame game, NationalPartyState party) {
        if (party == null || game == null) return false;
        String pk = (party.getPartyKey() != null ? party.getPartyKey() : "").toUpperCase();

        // 1. Projected seats growth vs actual baseline seats
        Map<String, Integer> projectedMap = game.getNationalProjectedSeats();
        int projSeats = (projectedMap != null && projectedMap.containsKey(pk)) ? projectedMap.get(pk) : party.getSeats();
        if (projSeats > party.getSeats()) {
            return true;
        }

        // 2. Projected seats swing vs previous turn
        if (game.getPreviousProjectedSeats() != null && game.getPreviousProjectedSeats().containsKey(pk)) {
            int prevSeats = game.getPreviousProjectedSeats().get(pk);
            if (projSeats > prevSeats) {
                return true;
            }
        }

        // 3. State-level operation momentum (issue campaign streak or vote share growth)
        if (game.getStateOperations() != null) {
            for (NationalStateOperationState s : game.getStateOperations().values()) {
                if (party.isPlayerParty() || (game.getPartyKey() != null && pk.equalsIgnoreCase(game.getPartyKey()))) {
                    if (s.getMomentumMultiplier() > 1.0 || s.getMomentumTurns() > 0) {
                        return true;
                    }
                }
                if (s.getVoteSplits() != null && s.getBaselineVoteSplits() != null) {
                    double cur = s.getVoteSplits().getOrDefault(pk, 0.0);
                    double base = s.getBaselineVoteSplits().getOrDefault(pk, 0.0);
                    if (cur > base + 0.5) {
                        return true;
                    }
                }
            }
        }

        // 4. Campaign theme persistence streak (player party)
        if ((party.isPlayerParty() || (game.getPartyKey() != null && pk.equalsIgnoreCase(game.getPartyKey())))
                && game.getThemePersistenceStreak() >= 2) {
            return true;
        }

        // 5. Morale surge (high morale >= 75 or positive morale growth)
        if (party.getMorale() >= 75 || party.getDeltaMorale() > 0) {
            return true;
        }

        return false;
    }

    public double calculatePartyDonation(NationalGame game, NationalPartyState party) {
        if (party == null) return 0.0;
        String pk = (party.getPartyKey() != null ? party.getPartyKey() : "").toUpperCase();
        Map<String, Integer> projectedMap = game != null ? game.getNationalProjectedSeats() : null;
        int projSeats = (projectedMap != null && projectedMap.containsKey(pk)) ? projectedMap.get(pk) : party.getSeats();

        boolean gainingMomentum = isPartyGainingMomentum(game, party);
        // Base donation: ₹0.5 Cr per projected seat. Momentum surge bonus: +₹0.25 Cr per projected seat (total ₹0.75 Cr)
        double ratePerSeat = gainingMomentum ? 0.75 : 0.50;
        double donation = projSeats > 0 ? (projSeats * ratePerSeat) : 0.5;
        return Math.round(donation * 10.0) / 10.0;
    }

    private void resolveStateElection(NationalGame game, NationalStateOperationState state) {
        state.setElectionCompleted(true);
        state.setElectionPhase("ELECTION_DAY");

        Map<String, Double> votes = new HashMap<>(state.getVoteSplits());
        Double undecided = votes.getOrDefault("UNDECIDED", 10.0);
        votes.remove("UNDECIDED");

        String playerKey = (game.getPartyKey() != null ? game.getPartyKey() : "YDP").toUpperCase();
        double playerShare = votes.getOrDefault(playerKey, 0.0);
        double momentumBonus = Math.max(0.0, (state.getMomentumMultiplier() - 1.0) * 4.0);
        double allocatedToPlayer = Math.min(undecided * 0.6, (undecided * (playerShare > 0 ? (playerShare / 100.0) : 0.1)) + momentumBonus);
        votes.put(playerKey, Math.round((playerShare + allocatedToPlayer) * 10.0) / 10.0);

        double remainingUndecided = Math.max(0.0, undecided - allocatedToPlayer);
        double rivalSum = 0.0;
        for (Map.Entry<String, Double> e : votes.entrySet()) {
            if (!e.getKey().equalsIgnoreCase(playerKey)) {
                rivalSum += e.getValue();
            }
        }
        if (rivalSum > 0) {
            for (Map.Entry<String, Double> e : new HashMap<>(votes).entrySet()) {
                if (!e.getKey().equalsIgnoreCase(playerKey)) {
                    double add = (e.getValue() / rivalSum) * remainingUndecided;
                    votes.put(e.getKey(), Math.round((e.getValue() + add) * 10.0) / 10.0);
                }
            }
        }
        state.setVoteSplits(votes);
        state.normalizeVoteSplits();

        int totalAssembly = state.getTotalAssemblySeats();
        Map<String, Integer> assemblySeats = new HashMap<>();
        String winnerParty = null;
        double maxVote = -1.0;
        int seatsAssigned = 0;

        for (Map.Entry<String, Double> e : state.getVoteSplits().entrySet()) {
            if ("UNDECIDED".equalsIgnoreCase(e.getKey())) continue;
            if (e.getValue() > maxVote) {
                maxVote = e.getValue();
                winnerParty = e.getKey();
            }
            int s = (int) Math.round((e.getValue() / 100.0) * totalAssembly);
            assemblySeats.put(e.getKey(), s);
            seatsAssigned += s;
        }

        int diff = totalAssembly - seatsAssigned;
        if (winnerParty != null && diff != 0) {
            assemblySeats.put(winnerParty, assemblySeats.getOrDefault(winnerParty, 0) + diff);
        }

        boolean playerWon = playerKey.equalsIgnoreCase(winnerParty);
        NationalPartyState playerState = game.findPartyState(game.getPartyKey());
        NationalAlliance playerAlliance = game.findPlayerAlliance(game.getPartyKey());
        boolean allianceWon = false;
        if (playerAlliance != null && playerAlliance.getMembers() != null) {
            for (NationalAllianceMember m : playerAlliance.getMembers()) {
                if (m.getPartyKey().equalsIgnoreCase(winnerParty)) {
                    allianceWon = true;
                    break;
                }
            }
        }

        int moraleChange = (playerWon || allianceWon) ? 6 : -3;
        double donorBonus = (playerWon || allianceWon) ? 4.0 : 0.0;

        if (playerState != null) {
            playerState.setMorale(Math.min(100, Math.max(0, playerState.getMorale() + moraleChange)));
            playerState.setFunds(Math.round((playerState.getFunds() + donorBonus) * 10.0) / 10.0);
            game.setPlayerFunds(playerState.getFunds());
        }

        Map<String, Object> result = new HashMap<>();
        result.put("electionTurn", game.getCurrentSeason());
        result.put("stateCode", state.getStateCode());
        result.put("stateName", state.getStateName());
        result.put("winnerParty", winnerParty);
        result.put("isPlayerVictory", playerWon || allianceWon);
        result.put("assemblySeats", assemblySeats);
        result.put("finalVoteSplits", new HashMap<>(state.getVoteSplits()));
        result.put("moraleChange", moraleChange);
        result.put("donorBonus", donorBonus);
        result.put("headline", state.getStateName() + " Assembly Election Verdict: " + winnerParty + " emerges victorious!");

        state.setLastElectionResult(result);
        recalculateProjectedSeats(state);
        recalculateNationalProjectedSeats(game);

        state.addActivityLog(game.getCurrentSeason(), "ELECTION_RESOLVED",
            state.getStateName() + " Assembly Election concluded: " + winnerParty + " won victory with "
            + assemblySeats.getOrDefault(winnerParty, 0) + "/" + totalAssembly + " seats.");

        if (playerAlliance != null) {
            logEntry(playerAlliance, game.getCurrentSeason(), "STATE_ELECTION_RESOLVED",
                state.getStateName() + " Assembly Election concluded. Winner: " + winnerParty + ". National morale effect: " + (moraleChange >= 0 ? "+" : "") + moraleChange);
        }
    }

    public List<Map<String, Object>> getStateOperations(String gameId) {
        NationalGame game = findGame(gameId);
        normalizeGameAllianceStates(game);
        initializeStateOperations(game);

        String playerKey = (game.getPartyKey() != null ? game.getPartyKey() : "YDP").toUpperCase();
        Set<String> playerAllianceParties = new HashSet<>();
        playerAllianceParties.add(playerKey);
        NationalAlliance playerAlliance = game.findPlayerAlliance(game.getPartyKey());
        if (playerAlliance != null && playerAlliance.getMembers() != null) {
            for (NationalAllianceMember m : playerAlliance.getMembers()) {
                if (m.getPartyKey() != null) {
                    playerAllianceParties.add(m.getPartyKey().toUpperCase());
                }
            }
        }

        List<Map<String, Object>> list = new ArrayList<>();
        for (NationalStateOperationState s : game.getStateOperations().values()) {
            Map<String, Object> map = new HashMap<>();
            map.put("stateCode", s.getStateCode());
            map.put("stateName", s.getStateName());
            map.put("scenarioKey", s.getScenarioKey());
            map.put("rulingParty", s.getRulingParty());
            map.put("oppositionParty", s.getOppositionParty());
            map.put("totalLokSabhaSeats", s.getTotalLokSabhaSeats());
            map.put("totalAssemblySeats", s.getTotalAssemblySeats());
            map.put("electionTurn", s.getElectionTurn());
            map.put("electionMonth", s.getElectionMonth());
            map.put("turnsToElection", s.getTurnsToElection());
            map.put("electionPhase", s.getElectionPhase());
            map.put("stateFunds", s.getStateFunds());
            map.put("stateWorkers", s.getStateWorkers());
            map.put("stateVolunteers", s.getStateVolunteers());
            map.put("stateDonors", s.getStateDonors());
            map.put("voteSplits", s.getVoteSplits());
            map.put("projectedLokSabhaSeats", s.getProjectedLokSabhaSeats());
            map.put("baselineVoteSplits", s.getBaselineVoteSplits());
            map.put("baselineLokSabhaSeats", s.getBaselineLokSabhaSeats());
            map.put("momentumTurns", s.getMomentumTurns());
            map.put("momentumMultiplier", s.getMomentumMultiplier());
            map.put("issueStreak", s.getIssueStreak());
            map.put("electionCompleted", s.isElectionCompleted());
            map.put("lastElectionResult", s.getLastElectionResult());
            map.put("doneThisTurn", s.isDoneThisTurn());
            map.put("netIncomePerTurn", s.getNetIncomePerTurn());
            map.put("buildings", s.getBuildings());
            map.put("wings", s.getWings());
            map.put("regions", s.getRegions());
            map.put("activityLog", s.getActivityLog());

            // ── Dynamic State Eligibility & Alliance Unlock Evaluation ──
            Map<String, Object> elig = evaluateStateEligibility(game, s);
            boolean isEligible = Boolean.TRUE.equals(elig.get("isEligible"));
            s.setActive(isEligible);
            if (!isEligible) {
                s.setSkippedThisTurn(true);
            }
            map.put("isActive", isEligible);
            map.put("isEligible", isEligible);
            map.put("isPlayerActive", elig.get("isPlayerActive"));
            map.put("unlockedByPartner", elig.get("unlockedByPartner"));
            map.put("isNewlyUnlocked", elig.get("isNewlyUnlocked"));
            map.put("unlockingParties", elig.get("unlockingParties"));
            map.put("skippedThisTurn", s.isSkippedThisTurn());

            double playerVote = s.getVoteSplits() != null ? s.getVoteSplits().getOrDefault(playerKey, 0.0) : 0.0;
            double allianceVote = 0.0;
            if (s.getVoteSplits() != null) {
                for (String allyKey : playerAllianceParties) {
                    allianceVote += s.getVoteSplits().getOrDefault(allyKey, 0.0);
                }
            }
            map.put("playerVoteShare", Math.round(playerVote * 10.0) / 10.0);
            map.put("allianceVoteShare", Math.round(allianceVote * 10.0) / 10.0);

            list.add(map);
        }

        // Sort: eligible states first (with newly unlocked on top), then inactive/locked states
        list.sort((a, b) -> {
            boolean eligA = Boolean.TRUE.equals(a.get("isEligible"));
            boolean eligB = Boolean.TRUE.equals(b.get("isEligible"));
            if (eligA != eligB) {
                return eligA ? -1 : 1; // Active/Eligible first
            }
            boolean newlyA = Boolean.TRUE.equals(a.get("isNewlyUnlocked"));
            boolean newlyB = Boolean.TRUE.equals(b.get("isNewlyUnlocked"));
            if (newlyA != newlyB) {
                return newlyA ? -1 : 1; // Newly unlocked first
            }
            Double shareA = (Double) a.getOrDefault("allianceVoteShare", 0.0);
            Double shareB = (Double) b.getOrDefault("allianceVoteShare", 0.0);
            return shareB.compareTo(shareA);
        });

        return list;
    }

    public static Map<String, Object> evaluateStateEligibility(NationalGame game, NationalStateOperationState s) {
        String playerKey = (game != null && game.getPartyKey() != null ? game.getPartyKey() : "YDP").toUpperCase();

        boolean hasVoteSplits = s != null && s.getVoteSplits() != null && !s.getVoteSplits().isEmpty();

        // 1. Direct player presence
        double playerVote = (s != null && hasVoteSplits) ? s.getVoteSplits().getOrDefault(playerKey, 0.0) : 0.0;
        int playerSeats = (s != null && s.getProjectedLokSabhaSeats() != null) ? s.getProjectedLokSabhaSeats().getOrDefault(playerKey, 0) : 0;
        boolean isPlayerActive = playerVote > 0.0 || playerSeats > 0
                || (s != null && s.getRulingParty() != null && playerKey.equalsIgnoreCase(s.getRulingParty()))
                || (s != null && s.getOppositionParty() != null && playerKey.equalsIgnoreCase(s.getOppositionParty()));

        // If mock state has no voteSplits and no ruling/opposition party, fallback to s.isActive()
        if (s != null && !hasVoteSplits && s.getRulingParty() == null && s.getOppositionParty() == null) {
            isPlayerActive = s.isActive();
        }

        // 2. Coalition / Alliance partner presence
        List<String> unlockingPartners = new ArrayList<>();
        List<String> newlyJoinedUnlockingPartners = new ArrayList<>();
        if (game != null && s != null) {
            NationalAlliance playerAlliance = game.findPlayerAlliance(playerKey);
            if (playerAlliance != null && playerAlliance.getMembers() != null) {
                for (NationalAllianceMember m : playerAlliance.getMembers()) {
                    if (m.getPartyKey() == null) continue;
                    String mKey = m.getPartyKey().toUpperCase();
                    if (mKey.equalsIgnoreCase(playerKey)) continue;

                    double mVote = hasVoteSplits ? s.getVoteSplits().getOrDefault(mKey, 0.0) : 0.0;
                    int mSeats = s.getProjectedLokSabhaSeats() != null ? s.getProjectedLokSabhaSeats().getOrDefault(mKey, 0) : 0;
                    boolean partnerInState = mVote > 0.0 || mSeats > 0
                            || (s.getRulingParty() != null && mKey.equalsIgnoreCase(s.getRulingParty()))
                            || (s.getOppositionParty() != null && mKey.equalsIgnoreCase(s.getOppositionParty()));

                    if (partnerInState) {
                        unlockingPartners.add(mKey);
                        if (m.getJoinedAtSeason() == game.getCurrentSeason()) {
                            newlyJoinedUnlockingPartners.add(mKey);
                        }
                    }
                }
            }
        }

        boolean isEligible = isPlayerActive || !unlockingPartners.isEmpty();
        boolean isNewlyUnlocked = !isPlayerActive && !newlyJoinedUnlockingPartners.isEmpty();
        String unlockedBy = null;
        if (!isPlayerActive && !unlockingPartners.isEmpty()) {
            unlockedBy = String.join(", ", unlockingPartners);
        }

        // Potential unlocking parties (state-level key players with >= 5% vote split or ruling/opp)
        List<String> unlockingParties = new ArrayList<>();
        if (s != null && s.getVoteSplits() != null) {
            for (Map.Entry<String, Double> entry : s.getVoteSplits().entrySet()) {
                String p = entry.getKey();
                if (p == null || "UNDECIDED".equalsIgnoreCase(p) || p.equalsIgnoreCase(playerKey)) continue;
                if (entry.getValue() != null && entry.getValue() >= 5.0) {
                    if (!unlockingParties.contains(p)) unlockingParties.add(p);
                }
            }
        }
        if (s != null && s.getRulingParty() != null && !s.getRulingParty().equalsIgnoreCase(playerKey) && !unlockingParties.contains(s.getRulingParty())) {
            unlockingParties.add(s.getRulingParty());
        }
        if (s != null && s.getOppositionParty() != null && !s.getOppositionParty().equalsIgnoreCase(playerKey) && !unlockingParties.contains(s.getOppositionParty())) {
            unlockingParties.add(s.getOppositionParty());
        }

        Map<String, Object> result = new HashMap<>();
        result.put("isEligible", isEligible);
        result.put("isPlayerActive", isPlayerActive);
        result.put("unlockedByPartner", unlockedBy);
        result.put("isNewlyUnlocked", isNewlyUnlocked);
        result.put("unlockingParties", unlockingParties);
        return result;
    }

    public static boolean isStateEligibleForPlayer(NationalGame game, NationalStateOperationState s) {
        if (game == null || s == null) return true;
        Map<String, Object> res = evaluateStateEligibility(game, s);
        return Boolean.TRUE.equals(res.get("isEligible"));
    }

    public Map<String, Object> getStateDetail(String gameId, String stateCode) {
        NationalGame game = findGame(gameId);
        normalizeGameAllianceStates(game);
        initializeStateOperations(game);

        if (stateCode == null || !game.getStateOperations().containsKey(stateCode.toUpperCase())) {
            throw new RuntimeException("State operation not found for: " + stateCode);
        }

        NationalStateOperationState state = game.getStateOperations().get(stateCode.toUpperCase());
        Map<String, Object> detail = new HashMap<>();
        detail.put("state", state);
        detail.put("issues", NationalStateIssueDefinition.getIssuesForState(state.getStateCode()));
        detail.put("tacticalActions", NationalStateIssueDefinition.getTacticalActions());

        // Fetch corresponding news for the state
        List<com.politicalsim.content.NewsDefinition> newsList = newsDefinitionRepository
            .findByScenarioKeyOrderByTypeAscTitleAsc(state.getScenarioKey());

        com.politicalsim.content.NewsDefinition activeNews = null;
        if (newsList != null && !newsList.isEmpty()) {
            int turnIndex = Math.max(0, game.getCurrentSeason() - 1) % newsList.size();
            activeNews = newsList.get(turnIndex);
        }
        detail.put("activeNews", activeNews);
        detail.put("resolvedNewsReaction", activeNews != null ? state.getResolvedNewsReactions().get(activeNews.getNewsKey()) : null);
        detail.put("lastNewsResolution", state.getLastNewsResolution());

        // Calculate Monthly Infrastructure Yields & Net Income per turn
        double monthlyCashDelta = 0.0;
        if (state.getBuildings() != null) {
            for (Map.Entry<String, Integer> b : state.getBuildings().entrySet()) {
                com.politicalsim.content.StateInfrastructureDefinition def = infrastructureRepository.findByKey(b.getKey()).orElse(null);
                if (def != null) monthlyCashDelta += def.getMonthlyCashOutput() * b.getValue();
            }
        }
        if (state.getRegions() != null) {
            for (RegionalOperationState reg : state.getRegions().values()) {
                if (reg.getBuildings() != null) {
                    for (Map.Entry<String, Integer> b : reg.getBuildings().entrySet()) {
                        com.politicalsim.content.StateInfrastructureDefinition def = infrastructureRepository.findByKey(b.getKey()).orElse(null);
                        if (def != null) monthlyCashDelta += def.getMonthlyCashOutput() * b.getValue();
                    }
                }
                if (reg.getWings() != null) {
                    for (Map.Entry<String, Integer> w : reg.getWings().entrySet()) {
                        com.politicalsim.content.StateInfrastructureDefinition def = infrastructureRepository.findByKey(w.getKey()).orElse(null);
                        if (def != null) monthlyCashDelta += def.getMonthlyCashOutput() * w.getValue();
                    }
                }
            }
        }
        double netIncome = Math.round((0.5 + monthlyCashDelta) * 100.0) / 100.0;
        state.setNetIncomePerTurn(netIncome);
        detail.put("netIncomePerTurn", netIncome);
        detail.put("monthlyCashOutput", Math.round(monthlyCashDelta * 100.0) / 100.0);
        detail.put("doneThisTurn", state.isDoneThisTurn());
        detail.put("skippedThisTurn", state.isSkippedThisTurn());

        return detail;
    }

    public NationalGame reactStateNews(String gameId, String stateCode, String newsKey, String optionKey) {
        NationalGame game = findGame(gameId);
        normalizeGameAllianceStates(game);
        initializeStateOperations(game);

        String sc = stateCode.toUpperCase();
        NationalStateOperationState state = game.getStateOperations().get(sc);
        if (state == null) throw new RuntimeException("State not found: " + stateCode);

        if (state.getResolvedNewsReactions() != null && state.getResolvedNewsReactions().containsKey(newsKey)) {
            throw new RuntimeException("A reaction has already been committed for this news item and is locked for this turn.");
        }

        state.getResolvedNewsReactions().put(newsKey, optionKey);

        // Find news item and chosen reaction option from repository
        com.politicalsim.content.NewsReactionDefinition chosenOption = null;
        List<com.politicalsim.content.NewsDefinition> newsList = newsDefinitionRepository
            .findByScenarioKeyOrderByTypeAscTitleAsc(state.getScenarioKey());
        if (newsList != null) {
            for (com.politicalsim.content.NewsDefinition n : newsList) {
                if (newsKey.equalsIgnoreCase(n.getNewsKey())) {
                    if (n.getReactionOptions() != null) {
                        for (com.politicalsim.content.NewsReactionDefinition ro : n.getReactionOptions()) {
                            if (optionKey.equalsIgnoreCase(ro.getReactionKey()) || optionKey.equalsIgnoreCase(ro.getOptionKey())) {
                                chosenOption = ro;
                                break;
                            }
                        }
                    }
                    break;
                }
            }
        }

        double baseSupport = 1.0;
        int moraleBonus = 1;
        if (chosenOption != null && chosenOption.getEffects() != null) {
            @SuppressWarnings("unchecked")
            Map<String, Object> eff = (Map<String, Object>) chosenOption.getEffects().get("playerParty");
            if (eff == null) {
                @SuppressWarnings("unchecked")
                Map<String, Object> selfEff = (Map<String, Object>) chosenOption.getEffects().get("selfParty");
                eff = selfEff;
            }
            if (eff != null) {
                if (eff.get("publicSupport") instanceof Number) {
                    baseSupport = ((Number) eff.get("publicSupport")).doubleValue();
                }
                if (eff.get("partyMorale") instanceof Number) {
                    moraleBonus = ((Number) eff.get("partyMorale")).intValue();
                }
            }
        }

        // Evaluate risk roll (if option carries a backlash risk)
        boolean riskTriggered = false;
        String badOutcomeDesc = null;
        double riskSupportPenalty = 0.0;
        int riskMoralePenalty = 0;

        if (chosenOption != null && chosenOption.getRisk() != null && !chosenOption.getRisk().isEmpty()) {
            Map<String, Object> riskMap = chosenOption.getRisk();
            int chance = 0;
            if (riskMap.get("chance") instanceof Number) {
                chance = ((Number) riskMap.get("chance")).intValue();
            }
            if (chance > 0) {
                long seed = (game.getId() + ":" + game.getCurrentSeason() + ":" + sc + ":" + newsKey + ":" + optionKey).hashCode();
                int roll = Math.abs(new Random(seed).nextInt(100));
                if (roll < chance) {
                    riskTriggered = true;
                    badOutcomeDesc = (String) riskMap.get("badOutcome");
                    if (riskMap.get("effects") instanceof Map<?, ?>) {
                        @SuppressWarnings("unchecked")
                        Map<String, Object> rEff = (Map<String, Object>) ((Map<?, ?>) riskMap.get("effects")).get("playerParty");
                        if (rEff != null) {
                            if (rEff.get("publicSupport") instanceof Number) {
                                riskSupportPenalty = ((Number) rEff.get("publicSupport")).doubleValue();
                            }
                            if (rEff.get("partyMorale") instanceof Number) {
                                riskMoralePenalty = ((Number) rEff.get("partyMorale")).intValue();
                            }
                        }
                    }
                    if (riskSupportPenalty == 0.0) {
                        riskSupportPenalty = -1.5;
                    }
                }
            }
        }

        // Net vote impact
        double netSupportDelta = baseSupport + riskSupportPenalty;
        if (netSupportDelta > 0 && state.getMomentumMultiplier() > 1.0) {
            netSupportDelta *= state.getMomentumMultiplier();
        }
        netSupportDelta = Math.round(netSupportDelta * 10.0) / 10.0;

        String playerKey = (game.getPartyKey() != null ? game.getPartyKey() : "YDP").toUpperCase();
        Map<String, Double> votes = state.getVoteSplits();
        double currentShare = votes.getOrDefault(playerKey, 0.0);
        double newShare = Math.max(0.0, Math.round((currentShare + netSupportDelta) * 10.0) / 10.0);
        votes.put(playerKey, newShare);

        // Adjust UNDECIDED pool
        Double undecided = votes.getOrDefault("UNDECIDED", 10.0);
        if (netSupportDelta > 0) {
            double take = Math.min(undecided - 5.0, netSupportDelta);
            if (take > 0) {
                votes.put("UNDECIDED", Math.round((undecided - take) * 10.0) / 10.0);
            }
        } else if (netSupportDelta < 0) {
            votes.put("UNDECIDED", Math.round((undecided - netSupportDelta) * 10.0) / 10.0);
        }

        // Update player party morale
        NationalPartyState playerState = game.findPartyState(playerKey);
        if (playerState != null) {
            int netMorale = moraleBonus + riskMoralePenalty;
            playerState.setMorale(Math.max(5, Math.min(100, playerState.getMorale() + netMorale)));
        }

        // Store resolution outcome for UI transparency
        Map<String, Object> resolution = new HashMap<>();
        resolution.put("newsKey", newsKey);
        resolution.put("optionKey", optionKey);
        resolution.put("riskTriggered", riskTriggered);
        resolution.put("badOutcome", badOutcomeDesc);
        resolution.put("baseSupport", baseSupport);
        resolution.put("riskSupportPenalty", riskSupportPenalty);
        resolution.put("netSupportDelta", netSupportDelta);
        state.setLastNewsResolution(resolution);

        state.normalizeVoteSplits();
        recalculateProjectedSeats(state);
        recalculateNationalProjectedSeats(game);

        game.setUpdatedAt(Instant.now().toString());
        return repository.save(game);
    }

    public NationalGame actOnStateIssue(String gameId, String stateCode, String issueId, String actionKey) {
        NationalGame game = findGame(gameId);
        normalizeGameAllianceStates(game);
        initializeStateOperations(game);

        String sc = stateCode.toUpperCase();
        NationalStateOperationState state = game.getStateOperations().get(sc);
        if (state == null) throw new RuntimeException("State not found: " + stateCode);

        if (state.getActiveIssueAction() != null) {
            throw new RuntimeException("An issue tactical action has already been deployed for " + state.getStateName() + " and is locked for this turn.");
        }

        // Find action
        Map<String, Object> chosenAction = null;
        for (Map<String, Object> act : NationalStateIssueDefinition.getTacticalActions()) {
            if (actionKey.equalsIgnoreCase((String) act.get("key"))) {
                chosenAction = act;
                break;
            }
        }
        if (chosenAction == null) throw new RuntimeException("Tactical action not found: " + actionKey);

        double costCr = ((Number) chosenAction.getOrDefault("costCr", 0.5)).doubleValue();
        if (state.getStateFunds() < costCr) {
            throw new RuntimeException("Insufficient state funds! Need ₹" + costCr + " Cr, available: ₹" + state.getStateFunds() + " Cr.");
        }
        state.setStateFunds(Math.round((state.getStateFunds() - costCr) * 10.0) / 10.0);

        // Calculate momentum
        if (issueId.equalsIgnoreCase(state.getActiveIssueId())) {
            state.setIssueStreak(state.getIssueStreak() + 1);
        } else {
            state.setIssueStreak(1);
            state.setActiveIssueId(issueId);
        }
        state.setActiveIssueAction(actionKey);
        state.setMomentumTurns(state.getMomentumTurns() + 1);

        double streakMultiplier = 1.0;
        int streak = state.getIssueStreak();
        if (streak == 2) streakMultiplier = 1.2;
        else if (streak == 3) streakMultiplier = 1.5;
        else if (streak == 4) streakMultiplier = 2.0;
        else if (streak >= 5) streakMultiplier = 2.5;
        state.setMomentumMultiplier(streakMultiplier);

        double baseSupport = ((Number) chosenAction.getOrDefault("baseSupportDelta", 1.0)).doubleValue();
        double delta = Math.round((baseSupport * streakMultiplier) * 10.0) / 10.0;

        String playerKey = (game.getPartyKey() != null ? game.getPartyKey() : "YDP").toUpperCase();
        Map<String, Double> votes = state.getVoteSplits();
        double currentShare = votes.getOrDefault(playerKey, 0.0);
        votes.put(playerKey, Math.round((currentShare + delta) * 10.0) / 10.0);

        Double undecided = votes.getOrDefault("UNDECIDED", 10.0);
        if (undecided > 10.0) {
            votes.put("UNDECIDED", Math.max(10.0, Math.round((undecided - delta) * 10.0) / 10.0));
        }

        state.normalizeVoteSplits();
        recalculateProjectedSeats(state);
        recalculateNationalProjectedSeats(game);

        game.setUpdatedAt(Instant.now().toString());
        return repository.save(game);
    }

    public NationalGame allocateStateResources(String gameId, String stateCode, double funds, int workers, int volunteers) {
        NationalGame game = findGame(gameId);
        normalizeGameAllianceStates(game);
        initializeStateOperations(game);

        String sc = stateCode.toUpperCase();
        NationalStateOperationState state = game.getStateOperations().get(sc);
        if (state == null) throw new RuntimeException("State not found: " + stateCode);

        NationalPartyState playerState = game.findPartyState(game.getPartyKey());
        if (playerState == null) throw new RuntimeException("Player party state not found.");

        if (funds > 0) {
            if (playerState.getFunds() < funds) {
                throw new RuntimeException("Insufficient party funds! Have: ₹" + playerState.getFunds() + " Cr, Requested: ₹" + funds + " Cr.");
            }
            playerState.setFunds(Math.round((playerState.getFunds() - funds) * 10.0) / 10.0);
            game.setPlayerFunds(playerState.getFunds());
            state.setStateFunds(Math.round((state.getStateFunds() + funds) * 10.0) / 10.0);
        }

        if (workers > 0) {
            if (playerState.getWorkers() < workers) {
                throw new RuntimeException("Insufficient cadre workers!");
            }
            playerState.setWorkers(playerState.getWorkers() - workers);
            state.setStateWorkers(state.getStateWorkers() + workers);
        }

        if (volunteers > 0) {
            if (playerState.getVolunteers() < volunteers) {
                throw new RuntimeException("Insufficient volunteers!");
            }
            playerState.setVolunteers(playerState.getVolunteers() - volunteers);
            state.setStateVolunteers(state.getStateVolunteers() + volunteers);
        }

        game.setUpdatedAt(Instant.now().toString());
        return repository.save(game);
    }

    public NationalGame executeCampaignPush(String gameId, String stateCode, String actionType) {
        NationalGame game = findGame(gameId);
        normalizeGameAllianceStates(game);
        initializeStateOperations(game);

        String sc = stateCode.toUpperCase();
        NationalStateOperationState state = game.getStateOperations().get(sc);
        if (state == null) throw new RuntimeException("State not found: " + stateCode);

        String act = actionType != null ? actionType.toUpperCase() : "";
        double costCr = 0.0;
        double supportDelta = 0.0;

        switch (act) {
            case "MEGA_RALLY":
                costCr = 5.0;
                supportDelta = 3.5;
                if (state.getStateFunds() < costCr) throw new RuntimeException("Need ₹5 Cr in state treasury for Mega Rally.");
                state.setStateFunds(Math.round((state.getStateFunds() - costCr) * 10.0) / 10.0);
                state.setStateVolunteers(state.getStateVolunteers() + 5000);
                break;
            case "AD_BLITZ":
                costCr = 3.0;
                supportDelta = 2.2;
                if (state.getStateFunds() < costCr) throw new RuntimeException("Need ₹3 Cr in state treasury for Ad Blitz.");
                state.setStateFunds(Math.round((state.getStateFunds() - costCr) * 10.0) / 10.0);
                break;
            case "LEADER_VISIT":
                costCr = 2.0;
                supportDelta = 2.0;
                if (state.getStateFunds() < costCr) throw new RuntimeException("Need ₹2 Cr in state treasury for Leader Visit.");
                state.setStateFunds(Math.round((state.getStateFunds() - costCr) * 10.0) / 10.0);
                NationalPartyState p = game.findPartyState(game.getPartyKey());
                if (p != null) p.setMorale(Math.min(100, p.getMorale() + 5));
                break;
            case "VOTER_CONTACT":
                if (state.getStateWorkers() < 100 || state.getStateVolunteers() < 200) {
                    throw new RuntimeException("Need at least 100 workers and 200 volunteers in state for Voter Contact Drive.");
                }
                supportDelta = 1.6;
                break;
            default:
                throw new RuntimeException("Unknown campaign action: " + actionType);
        }

        String playerKey = (game.getPartyKey() != null ? game.getPartyKey() : "YDP").toUpperCase();
        Map<String, Double> votes = state.getVoteSplits();
        double currentShare = votes.getOrDefault(playerKey, 0.0);
        votes.put(playerKey, Math.round((currentShare + supportDelta) * 10.0) / 10.0);

        Double undecided = votes.getOrDefault("UNDECIDED", 10.0);
        if (undecided > 10.0) {
            votes.put("UNDECIDED", Math.max(10.0, Math.round((undecided - supportDelta) * 10.0) / 10.0));
        }

        state.normalizeVoteSplits();
        recalculateProjectedSeats(state);
        recalculateNationalProjectedSeats(game);

        game.setUpdatedAt(Instant.now().toString());
        return repository.save(game);
    }

    public NationalGame skipState(String gameId, String stateCode) {
        NationalGame game = findGame(gameId);
        normalizeGameAllianceStates(game);
        initializeStateOperations(game);

        String sc = stateCode.toUpperCase();
        NationalStateOperationState state = game.getStateOperations().get(sc);
        if (state != null) {
            state.setSkippedThisTurn(true);
            state.setDoneThisTurn(false);
        }

        game.setUpdatedAt(Instant.now().toString());
        return repository.save(game);
    }

    public NationalGame completeState(String gameId, String stateCode) {
        NationalGame game = findGame(gameId);
        normalizeGameAllianceStates(game);
        initializeStateOperations(game);

        String sc = stateCode.toUpperCase();
        NationalStateOperationState state = game.getStateOperations().get(sc);
        if (state != null) {
            state.setDoneThisTurn(true);
            state.setSkippedThisTurn(false);
        }

        game.setUpdatedAt(Instant.now().toString());
        return repository.save(game);
    }

    public List<com.politicalsim.content.StateInfrastructureDefinition> getInfrastructureCatalog() {
        return infrastructureRepository.findAll();
    }

    public NationalGame buildInfrastructure(String gameId, String stateCode, String infraKey, String regionId) {
        NationalGame game = findGame(gameId);
        normalizeGameAllianceStates(game);
        initializeStateOperations(game);

        String sc = stateCode.toUpperCase();
        NationalStateOperationState state = game.getStateOperations().get(sc);
        if (state == null) throw new RuntimeException("State not found: " + stateCode);

        com.politicalsim.content.StateInfrastructureDefinition def = infrastructureRepository.findByKey(infraKey)
            .orElseThrow(() -> new RuntimeException("Infrastructure definition not found: " + infraKey));

        if (state.getStateFunds() < def.getCostFunds()) {
            throw new RuntimeException("Insufficient state treasury funds! Requires ₹" + def.getCostFunds() + " Cr, available: ₹" + String.format("%.1f", state.getStateFunds()) + " Cr.");
        }

        String playerKey = (game.getPartyKey() != null ? game.getPartyKey() : "YDP").toUpperCase();

        if ("STATE".equalsIgnoreCase(def.getScope())) {
            if (state.getBuildings() == null) state.setBuildings(new HashMap<>());
            int currentCount = state.getBuildings().getOrDefault(infraKey, 0);
            if (currentCount >= def.getMaxAllowedPerScope()) {
                throw new RuntimeException("Maximum limit of " + def.getMaxAllowedPerScope() + " reached for " + def.getName() + " in this state.");
            }
            state.getBuildings().put(infraKey, currentCount + 1);

            double instantBonus = def.getInstantSupportBonus();
            if (instantBonus > 0) {
                if (state.getRegions() != null) {
                    for (RegionalOperationState r : state.getRegions().values()) {
                        r.setSupportPercentage(Math.min(95.0, r.getSupportPercentage() + instantBonus));
                    }
                }
                syncRegionalSupportToStateVoteSplits(state, playerKey);
                recalculateProjectedSeats(state);
                recalculateNationalProjectedSeats(game);
            }
        } else {
            if (regionId == null || state.getRegions() == null || !state.getRegions().containsKey(regionId)) {
                throw new RuntimeException("Valid regionId required for " + def.getName());
            }
            RegionalOperationState reg = state.getRegions().get(regionId);
            if (reg.getBuildings() == null) reg.setBuildings(new HashMap<>());
            if (reg.getWings() == null) reg.setWings(new HashMap<>());

            Map<String, Integer> targetMap = "WING".equalsIgnoreCase(def.getCategory()) ? reg.getWings() : reg.getBuildings();
            int currentCount = targetMap.getOrDefault(infraKey, 0);
            if (currentCount >= def.getMaxAllowedPerScope()) {
                throw new RuntimeException("Maximum limit of " + def.getMaxAllowedPerScope() + " reached for " + def.getName() + " in " + reg.getRegionName());
            }
            targetMap.put(infraKey, currentCount + 1);

            double instantBonus = def.getInstantSupportBonus();
            if (instantBonus > 0) {
                reg.setSupportPercentage(Math.min(95.0, reg.getSupportPercentage() + instantBonus));
                syncRegionalSupportToStateVoteSplits(state, playerKey);
                recalculateProjectedSeats(state);
                recalculateNationalProjectedSeats(game);
            }
        }

        // Deduct monetary cost
        state.setStateFunds(Math.max(0.0, Math.round((state.getStateFunds() - def.getCostFunds()) * 10.0) / 10.0));

        game.setUpdatedAt(Instant.now().toString());
        return repository.save(game);
    }

    public NationalGame allocateRegionalResources(String gameId, String stateCode, String regionId, double funds, int workers, int volunteers) {
        NationalGame game = findGame(gameId);
        normalizeGameAllianceStates(game);
        initializeStateOperations(game);

        String sc = stateCode.toUpperCase();
        NationalStateOperationState state = game.getStateOperations().get(sc);
        if (state == null) throw new RuntimeException("State not found: " + stateCode);

        if (state.getRegions() == null || !state.getRegions().containsKey(regionId)) {
            throw new RuntimeException("Region not found: " + regionId);
        }

        RegionalOperationState reg = state.getRegions().get(regionId);
        reg.setAllocatedFunds(Math.max(0.0, Math.round(funds * 10.0) / 10.0));
        reg.setAllocatedWorkers(Math.max(0, workers));
        reg.setAllocatedVolunteers(Math.max(0, volunteers));

        game.setUpdatedAt(Instant.now().toString());
        return repository.save(game);
    }

    public NationalGame allocateBatchRegionalResources(String gameId, String stateCode, Map<String, Map<String, Object>> allocations) {
        NationalGame game = findGame(gameId);
        normalizeGameAllianceStates(game);
        initializeStateOperations(game);

        String sc = stateCode.toUpperCase();
        NationalStateOperationState state = game.getStateOperations().get(sc);
        if (state == null) throw new RuntimeException("State not found: " + stateCode);
        if (state.getRegions() == null) throw new RuntimeException("No regions found for state: " + stateCode);

        if (allocations != null) {
            for (Map.Entry<String, Map<String, Object>> entry : allocations.entrySet()) {
                String regionId = entry.getKey();
                Map<String, Object> alloc = entry.getValue();
                if (state.getRegions().containsKey(regionId)) {
                    RegionalOperationState reg = state.getRegions().get(regionId);
                    double funds = ((Number) alloc.getOrDefault("funds", alloc.getOrDefault("allocatedFunds", 0.0))).doubleValue();
                    int workers = ((Number) alloc.getOrDefault("workers", alloc.getOrDefault("allocatedWorkers", 0))).intValue();
                    int volunteers = ((Number) alloc.getOrDefault("volunteers", alloc.getOrDefault("allocatedVolunteers", 0))).intValue();
                    reg.setAllocatedFunds(Math.max(0.0, Math.round(funds * 10.0) / 10.0));
                    reg.setAllocatedWorkers(Math.max(0, workers));
                    reg.setAllocatedVolunteers(Math.max(0, volunteers));
                }
            }
        }

        game.setUpdatedAt(Instant.now().toString());
        return repository.save(game);
    }
}

