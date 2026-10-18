package com.politicalsim.national;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/national/games")
@CrossOrigin(origins = "*")
public class NationalGameController {

    @Autowired
    private NationalGameService gameService;

    @PostMapping("/start")
    public ResponseEntity<?> startGame(@RequestBody Map<String, Object> body) {
        try {
            String userId = (String) body.get("userId");
            int era = ((Number) body.get("era")).intValue();
            String partyKey = (String) body.get("partyKey");
            List<Map<String, Object>> parties = (List<Map<String, Object>>) body.get("parties");
            List<Map<String, Object>> stateSeatData = (List<Map<String, Object>>) body.get("stateSeatData");
            
            NationalGame game = gameService.startGame(userId, era, partyKey, parties, stateSeatData);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/{userId}")
    public ResponseEntity<?> getGame(@PathVariable String userId) {
        return gameService.getGame(userId)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping("/{id}/alliance/create")
    public ResponseEntity<?> createAlliance(@PathVariable String id, @RequestBody Map<String, Object> body) {
        try {
            String allianceName = (String) body.get("allianceName");
            String color = (String) body.get("color");
            NationalGame game = gameService.createAlliance(id, allianceName, color);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/alliance/invite")
    public ResponseEntity<?> inviteParty(@PathVariable String id, @RequestBody Map<String, Object> body) {
        try {
            String targetPartyKey = (String) body.get("targetPartyKey");
            
            NationalContract contract = new NationalContract();
            contract.setJoiningBonus(((Number) body.getOrDefault("joiningBonus", 0)).doubleValue());
            contract.setRecurringPerSeason(((Number) body.getOrDefault("recurringPerSeason", 0)).doubleValue());
            contract.setCabinetMinistersPromised(((Number) body.getOrDefault("cabinetMinistersPromised", 0)).intValue());
            contract.setStateMinistersPromised(((Number) body.getOrDefault("stateMinistersPromised", 0)).intValue());
            contract.setDurationSeasons(((Number) body.getOrDefault("durationSeasons", -1)).intValue());
            contract.setBroken(false);
            
            NationalCoalitionActionResponse response = gameService.inviteParty(id, targetPartyKey, contract);
            return ResponseEntity.ok(response);
        } catch (Exception e) {
            return ResponseEntity.ok(NationalCoalitionActionResponse.refusal(
                CoalitionResponseCode.ERROR,
                "Failed to send coalition invitation: " + e.getMessage(),
                null
            ));
        }
    }

    @PostMapping("/{id}/alliance/respond-request")
    public ResponseEntity<?> respondToRequest(@PathVariable String id, @RequestBody Map<String, Object> body) {
        try {
            String requestId = (String) body.get("requestId");
            boolean accept = (Boolean) body.get("accept");
            NationalGame game = gameService.respondToRequest(id, requestId, accept);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @DeleteMapping("/{id}/alliance/remove-party")
    public ResponseEntity<?> removeParty(@PathVariable String id, @RequestBody Map<String, Object> body) {
        try {
            String targetPartyKey = (String) body.get("targetPartyKey");
            NationalGame game = gameService.removeParty(id, targetPartyKey);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @DeleteMapping("/{id}/alliance/dissolve")
    public ResponseEntity<?> dissolveAlliance(@PathVariable String id) {
        try {
            NationalGame game = gameService.dissolveAlliance(id);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/alliance/leave")
    public ResponseEntity<?> leaveAlliance(@PathVariable String id) {
        try {
            NationalGame game = gameService.leaveAlliance(id);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PutMapping("/{id}/alliance/reallocate")
    public ResponseEntity<?> reallocateResources(@PathVariable String id, @RequestBody Map<String, Object> body) {
        try {
            List<Map<String, Object>> allocations = (List<Map<String, Object>>) body.get("allocations");
            NationalGame game = gameService.reallocateResources(id, allocations);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/season/advance")
    public ResponseEntity<?> advanceSeason(@PathVariable String id) {
        try {
            NationalGame game = gameService.advanceSeason(id);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/no-confidence")
    public ResponseEntity<?> callNoConfidenceVote(@PathVariable String id) {
        try {
            NationalGame game = gameService.callNoConfidenceVote(id);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/ai/process-requests")
    public ResponseEntity<?> processAiRequests(@PathVariable String id) {
        try {
            NationalGame game = gameService.processAiRequests(id);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/{id}/finance/cards")
    public ResponseEntity<?> getFinanceCards(@PathVariable String id) {
        try {
            // Return all 9 cards with qualitative attributes only (no hidden numbers)
            List<Map<String, Object>> cards = NationalFinanceCardDefinition.getAllCards().stream().map(c -> {
                Map<String, Object> map = new java.util.HashMap<>();
                map.put("id", c.getId());
                map.put("name", c.getName());
                map.put("icon", c.getIcon());
                map.put("category", c.getCategory());
                map.put("tagline", c.getTagline());
                map.put("description", c.getDescription());
                map.put("treasuryRating", c.getTreasuryRating());
                map.put("cadreRating", c.getCadreRating());
                map.put("moraleRating", c.getMoraleRating());
                map.put("scrutinyRating", c.getScrutinyRating());
                map.put("strategicNote", c.getStrategicNote());
                map.put("megaFinance", c.isMegaFinance());
                map.put("grassroots", c.isGrassroots());
                return map;
            }).collect(java.util.stream.Collectors.toList());

            return ResponseEntity.ok(cards);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/finance/play")
    public ResponseEntity<?> playFinanceCard(@PathVariable String id, @RequestBody Map<String, Object> body) {
        try {
            String cardId = (String) body.get("cardId");
            NationalGame game = gameService.playFinanceCard(id, cardId);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/finance/cancel")
    public ResponseEntity<?> cancelFinanceCard(@PathVariable String id) {
        try {
            NationalGame game = gameService.cancelFinanceCard(id);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/{id}/events")
    public ResponseEntity<?> getSeasonEvents(@PathVariable String id) {
        try {
            List<Map<String, Object>> events = gameService.getSeasonEvents(id);
            return ResponseEntity.ok(events);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/events/respond")
    public ResponseEntity<?> respondToEvent(@PathVariable String id, @RequestBody Map<String, Object> body) {
        try {
            String eventId = (String) body.get("eventId");
            String optionId = (String) body.get("optionId");
            NationalGame game = gameService.respondToEvent(id, eventId, optionId);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/{id}/themes")
    public ResponseEntity<?> getSeasonThemes(@PathVariable String id) {
        try {
            Map<String, Object> themes = gameService.getSeasonThemes(id);
            return ResponseEntity.ok(themes);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/themes/target-party")
    public ResponseEntity<?> setTargetParty(@PathVariable String id, @RequestBody Map<String, Object> body) {
        try {
            String targetPartyKey = (String) body.get("targetPartyKey");
            NationalGame game = gameService.setTargetParty(id, targetPartyKey);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/themes/action")
    public ResponseEntity<?> chooseThemeAction(@PathVariable String id, @RequestBody Map<String, Object> body) {
        try {
            String themeKey = (String) body.get("themeKey");
            String actionKey = (String) body.get("actionKey");
            String targetPartyKey = (String) body.get("targetPartyKey");
            NationalGame game = gameService.chooseThemeAction(id, themeKey, actionKey, targetPartyKey);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/media-social/allocate")
    public ResponseEntity<?> allocateMediaSocial(@PathVariable String id, @RequestBody Map<String, Object> body) {
        try {
            @SuppressWarnings("unchecked")
            Map<String, Object> rawAllocations = (Map<String, Object>) body.getOrDefault("allocations", java.util.Collections.emptyMap());
            Map<String, Double> allocations = new java.util.HashMap<>();
            for (Map.Entry<String, Object> entry : rawAllocations.entrySet()) {
                if (entry.getValue() instanceof Number) {
                    allocations.put(entry.getKey(), ((Number) entry.getValue()).doubleValue());
                }
            }
            boolean commit = Boolean.TRUE.equals(body.get("commit"));
            NationalGame game = gameService.allocateMediaSocial(id, allocations, commit);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/media-social/cancel")
    public ResponseEntity<?> cancelMediaSocial(@PathVariable String id) {
        try {
            NationalGame game = gameService.cancelMediaSocial(id);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    // ─────────────────────────────────────────────────────────────────────────
    // STATE OPERATIONS ENDPOINTS (UP, BIHAR, MAHARASHTRA)
    // ─────────────────────────────────────────────────────────────────────────

    @GetMapping("/{id}/states")
    public ResponseEntity<?> getStateOperations(@PathVariable String id) {
        try {
            List<Map<String, Object>> states = gameService.getStateOperations(id);
            return ResponseEntity.ok(states);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/{id}/states/{stateCode}")
    public ResponseEntity<?> getStateDetail(@PathVariable String id, @PathVariable String stateCode) {
        try {
            Map<String, Object> detail = gameService.getStateDetail(id, stateCode);
            return ResponseEntity.ok(detail);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/states/{stateCode}/news/react")
    public ResponseEntity<?> reactStateNews(@PathVariable String id, @PathVariable String stateCode, @RequestBody Map<String, Object> body) {
        try {
            String newsKey = (String) body.get("newsKey");
            String optionKey = (String) body.get("optionKey");
            NationalGame game = gameService.reactStateNews(id, stateCode, newsKey, optionKey);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/states/{stateCode}/issues/action")
    public ResponseEntity<?> actOnStateIssue(@PathVariable String id, @PathVariable String stateCode, @RequestBody Map<String, Object> body) {
        try {
            String issueId = (String) body.get("issueId");
            String actionKey = (String) body.get("actionKey");
            NationalGame game = gameService.actOnStateIssue(id, stateCode, issueId, actionKey);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/states/{stateCode}/allocate")
    public ResponseEntity<?> allocateStateResources(@PathVariable String id, @PathVariable String stateCode, @RequestBody Map<String, Object> body) {
        try {
            double funds = ((Number) body.getOrDefault("funds", 0.0)).doubleValue();
            int workers = ((Number) body.getOrDefault("workers", 0)).intValue();
            int volunteers = ((Number) body.getOrDefault("volunteers", 0)).intValue();
            NationalGame game = gameService.allocateStateResources(id, stateCode, funds, workers, volunteers);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/states/{stateCode}/campaign")
    public ResponseEntity<?> executeCampaignPush(@PathVariable String id, @PathVariable String stateCode, @RequestBody Map<String, Object> body) {
        try {
            String actionType = (String) body.get("actionType");
            NationalGame game = gameService.executeCampaignPush(id, stateCode, actionType);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/states/{stateCode}/skip")
    public ResponseEntity<?> skipState(@PathVariable String id, @PathVariable String stateCode) {
        try {
            NationalGame game = gameService.skipState(id, stateCode);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/states/{stateCode}/complete")
    public ResponseEntity<?> completeState(@PathVariable String id, @PathVariable String stateCode) {
        try {
            NationalGame game = gameService.completeState(id, stateCode);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/{id}/states/infrastructure/catalog")
    public ResponseEntity<?> getInfrastructureCatalog() {
        try {
            return ResponseEntity.ok(gameService.getInfrastructureCatalog());
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/states/{stateCode}/infrastructure/build")
    public ResponseEntity<?> buildInfrastructure(@PathVariable String id, @PathVariable String stateCode, @RequestBody Map<String, Object> body) {
        try {
            String infraKey = (String) body.get("infraKey");
            String regionId = (String) body.get("regionId");
            NationalGame game = gameService.buildInfrastructure(id, stateCode, infraKey, regionId);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/states/{stateCode}/regions/allocate")
    public ResponseEntity<?> allocateRegionalResources(@PathVariable String id, @PathVariable String stateCode, @RequestBody Map<String, Object> body) {
        try {
            String regionId = (String) body.get("regionId");
            double funds = ((Number) body.getOrDefault("allocatedFunds", 0.0)).doubleValue();
            int workers = ((Number) body.getOrDefault("allocatedWorkers", 0)).intValue();
            int volunteers = ((Number) body.getOrDefault("allocatedVolunteers", 0)).intValue();
            NationalGame game = gameService.allocateRegionalResources(id, stateCode, regionId, funds, workers, volunteers);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @PostMapping("/{id}/states/{stateCode}/regions/allocate-batch")
    public ResponseEntity<?> allocateBatchRegionalResources(@PathVariable String id, @PathVariable String stateCode, @RequestBody Map<String, Object> body) {
        try {
            @SuppressWarnings("unchecked")
            Map<String, Map<String, Object>> allocations = (Map<String, Map<String, Object>>) body.get("allocations");
            NationalGame game = gameService.allocateBatchRegionalResources(id, stateCode, allocations);
            return ResponseEntity.ok(game);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }

    @GetMapping("/{id}/hints")
    public ResponseEntity<?> getStrategicHints(@PathVariable String id) {
        try {
            Map<String, Object> hints = gameService.getStrategicHints(id);
            return ResponseEntity.ok(hints);
        } catch (Exception e) {
            return ResponseEntity.internalServerError().body(Map.of("error", e.getMessage()));
        }
    }
}

