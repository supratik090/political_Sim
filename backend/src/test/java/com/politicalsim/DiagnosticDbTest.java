package com.politicalsim;

import com.politicalsim.game.GameSession;
import com.politicalsim.game.GameSessionRepository;
import com.politicalsim.party.ControllerType;
import com.politicalsim.party.PartyState;
import com.politicalsim.game.RoundSubmission;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Disabled;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import com.politicalsim.content.CardDefinition;
import com.politicalsim.content.CardDefinitionRepository;
import com.politicalsim.content.NewsDefinition;
import com.politicalsim.content.NewsDefinitionRepository;
import com.politicalsim.content.MonthlyIssueDefinition;
import com.politicalsim.content.MonthlyIssueDefinitionRepository;
import com.politicalsim.content.ScenarioDefinition;
import com.politicalsim.content.ScenarioDefinitionRepository;

@SpringBootTest
class DiagnosticDbTest {

    @Autowired
    private GameSessionRepository repository;

    @Autowired
    private CardDefinitionRepository cardRepository;

    @Autowired
    private NewsDefinitionRepository newsRepository;

    @Autowired
    private MonthlyIssueDefinitionRepository issueRepository;

    @Autowired
    private ScenarioDefinitionRepository scenarioDefinitionRepository;

    // ──────────────────────────────────────────────────────────────────────────
    // Test 1: Scenario Key Inventory
    // ──────────────────────────────────────────────────────────────────────────
    @Test
    @Disabled("Diagnostic/Interactive test — enable manually when needed")
    void printAvailableScenarioKeysInDb() {
        System.out.println("\n========== DB SCENARIO KEYS LIST START ==========");

        List<ScenarioDefinition> scenarios = scenarioDefinitionRepository.findAll();
        System.out.println("Total ScenarioDefinitions in DB: " + scenarios.size());
        for (ScenarioDefinition s : scenarios) {
            System.out.printf("  %-30s  name=%-30s  active=%s%n",
                    s.getScenarioKey(), s.getName(), s.isActive());
        }

        List<String> newsKeys = newsRepository.findAll().stream()
                .map(NewsDefinition::getScenarioKey).filter(java.util.Objects::nonNull)
                .distinct().sorted().collect(Collectors.toList());
        System.out.println("News keys   : " + newsKeys);

        List<String> cardKeys = cardRepository.findAll().stream()
                .map(CardDefinition::getScenarioKey).filter(java.util.Objects::nonNull)
                .distinct().sorted().collect(Collectors.toList());
        System.out.println("Card keys   : " + cardKeys);

        List<String> issueKeys = issueRepository.findAll().stream()
                .map(MonthlyIssueDefinition::getScenarioKey).filter(java.util.Objects::nonNull)
                .distinct().sorted().collect(Collectors.toList());
        System.out.println("Issue keys  : " + issueKeys);

        System.out.println("========== DB SCENARIO KEYS LIST END ==========\n");
    }

    // ──────────────────────────────────────────────────────────────────────────
    // Test 2: Recent 5 Game Sessions (summary)
    // ──────────────────────────────────────────────────────────────────────────
    @Test
    void printLastGameSessionDetails() {
        final String TARGET_SCENARIO = "bihar_2001";
        System.out.println("\n╔══════════════════════════════════════════════════════════════╗");
        System.out.println(  "║      BIHAR 2001 — LAST LOST GAME SESSION AUTOPSY             ║");
        System.out.println(  "╚══════════════════════════════════════════════════════════════╝");

        List<GameSession> allSessions = repository.findAllByOrderByCurrentDateDesc();
        if (allSessions.isEmpty()) {
            System.out.println("❌ No game sessions found in database!");
            return;
        }

        // Priority 1: Bihar 2001 session that ended very early (turn < 2) — any status
        GameSession session = allSessions.stream()
                .filter(s -> TARGET_SCENARIO.equals(s.getScenarioKey()))
                .filter(s -> s.getTurnNumber() < 2)
                .filter(s -> s.getStatus() != com.politicalsim.game.GameStatus.ACTIVE)
                .findFirst()
                .orElse(null);

        if (session == null) {
            // Priority 2: most recent Bihar 2001 loss (any turn)
            session = allSessions.stream()
                    .filter(s -> TARGET_SCENARIO.equals(s.getScenarioKey()))
                    .filter(s -> s.getStatus() == com.politicalsim.game.GameStatus.DEFEAT
                              || s.getStatus() == com.politicalsim.game.GameStatus.GAME_OVER
                              || s.getStatus() == com.politicalsim.game.GameStatus.FORFEITED)
                    .findFirst()
                    .orElse(null);
            if (session != null) {
                System.out.println("⚠️  No turn-1 Bihar 2001 session found — showing most recent Bihar 2001 loss (turn " + session.getTurnNumber() + ").");
            }
        }

        if (session == null) {
            // Fallback: any Bihar 2001 session regardless of status
            session = allSessions.stream()
                    .filter(s -> TARGET_SCENARIO.equals(s.getScenarioKey()))
                    .findFirst()
                    .orElse(null);
            if (session == null) {
                System.out.println("❌ No Bihar 2001 game session found at all!");
                System.out.println("Available scenario keys:");
                allSessions.stream()
                        .map(GameSession::getScenarioKey)
                        .filter(java.util.Objects::nonNull)
                        .distinct().sorted()
                        .forEach(k -> System.out.println("   - " + k));
                return;
            }
            System.out.println("⚠️  No lost Bihar 2001 session found — showing most recent Bihar 2001 session instead.");
        }

        // ── Session header ──────────────────────────────────────────────
        System.out.println("\n📋 SESSION DETAILS");
        System.out.println("  ID       : " + session.getId());
        System.out.println("  Scenario : " + session.getScenarioKey() + " (" + session.getScenarioName() + ")");
        System.out.println("  Status   : " + session.getStatus() + "  ← WHY YOU LOST");
        System.out.println("  Turn     : " + session.getTurnNumber());
        System.out.println("  Created  : " + session.getCreatedAt());

        // ── Final party stats ────────────────────────────────────────────
        System.out.println("\n📊 FINAL PARTY STATS AT END OF LAST ROUND:");
        System.out.printf("  %-26s %-10s %-9s %6s %7s %11s %7s %9s  %-30s%n",
                "Party", "Ctrl", "Status", "Coins", "Morale", "Corruption", "Media", "Support%", "Last Δ");
        System.out.println("  " + "─".repeat(110));
        for (PartyState p : session.getParties()) {
            String deltaStr = "—";
            if (session.getLastMetricDeltas() != null && session.getLastMetricDeltas().containsKey(p.getId())) {
                Object raw = session.getLastMetricDeltas().get(p.getId());
                deltaStr = raw != null ? raw.toString() : "—";
            }
            String statusIcon = p.isActive() ? "✅ ALIVE" : "❌ OUT";
            System.out.printf("  %-26s %-10s %-9s %6d %7d %11d %7d %8d%%  %-30s%n",
                    p.getName(), p.getControllerType(), statusIcon,
                    p.getStats().getCoins(), p.getStats().getPartyMorale(),
                    p.getStats().getCorruptionScore(), p.getStats().getMediaImage(),
                    p.getStats().getPublicSupport(), deltaStr);
        }

        // ── Identify the human player ────────────────────────────────────
        PartyState humanParty = session.getParties().stream()
                .filter(p -> p.getControllerType() == com.politicalsim.party.ControllerType.HUMAN)
                .findFirst().orElse(null);

        if (humanParty != null) {
            System.out.println("\n🕹️  YOUR PARTY (HUMAN): " + humanParty.getName());
            System.out.println("   Final support  : " + humanParty.getStats().getPublicSupport() + "%");
            System.out.println("   Final coins     : " + humanParty.getStats().getCoins());
            System.out.println("   Final morale    : " + humanParty.getStats().getPartyMorale());
            System.out.println("   Final corruption: " + humanParty.getStats().getCorruptionScore() + "%");
            System.out.println("   Still active?   : " + (humanParty.isActive() ? "YES" : "NO — ELIMINATED"));
        }

        // ── Last round card submissions ─────────────────────────────────
        System.out.println("\n⚙️  LAST ROUND — WHAT EVERY PARTY PLAYED:");
        if (session.getLastRoundSubmissions() != null && !session.getLastRoundSubmissions().isEmpty()) {
            for (RoundSubmission sub : session.getLastRoundSubmissions()) {
                String marker = (humanParty != null && humanParty.getName().equals(sub.getPartyName()))
                        ? " ◀ YOU" : "";
                System.out.println("  ┌─ [" + sub.getPartyName() + "]" + marker);
                System.out.println("  │  Card   : " + sub.getCardName() + " (key: " + sub.getCardKey() + ")");
                System.out.println("  │  Bid    : " + sub.getBid());
                System.out.println("  │  Intent : " + sub.getAiIntent());
                if (sub.getAiDecisionBasis() != null && !sub.getAiDecisionBasis().isBlank()) {
                    System.out.println("  │  Basis  : " + sub.getAiDecisionBasis());
                }
                System.out.println("  └─────────────────────────────────");
            }
        } else {
            System.out.println("  (no last-round submission data stored)");
        }

        // ── Last round commentary ────────────────────────────────────────
        System.out.println("\n📰 LAST ROUND COMMENTARY / EVENT LOG:");
        if (session.getLastRoundCommentary() != null && !session.getLastRoundCommentary().isEmpty()) {
            int idx = 1;
            for (String line : session.getLastRoundCommentary()) {
                System.out.printf("  [%2d] %s%n", idx++, line);
            }
        } else {
            System.out.println("  (no commentary stored for the last round)");
        }

        // ── Card usage totals ────────────────────────────────────────────
        System.out.println("\n🃏 FULL GAME CARD USAGE BY PARTY:");
        if (session.getCardUsageByParty() != null && !session.getCardUsageByParty().isEmpty()) {
            for (PartyState p : session.getParties()) {
                Map<String, Integer> usage = session.getCardUsageByParty().get(p.getId());
                if (usage == null || usage.isEmpty()) continue;
                System.out.println("  [" + p.getName() + "]");
                usage.entrySet().stream()
                        .sorted((a, b) -> b.getValue() - a.getValue())
                        .forEach(e -> System.out.printf("     %-50s  ×%d%n", e.getKey(), e.getValue()));
            }
        } else {
            System.out.println("  (no card usage data stored)");
        }

        // ── Quick defeat diagnosis ────────────────────────────────────────
        System.out.println("\n🔍 DEFEAT DIAGNOSIS:");
        if (humanParty != null) {
            int support  = humanParty.getStats().getPublicSupport();
            int coins    = humanParty.getStats().getCoins();
            int morale   = humanParty.getStats().getPartyMorale();
            int corrupt  = humanParty.getStats().getCorruptionScore();
            boolean dead = !humanParty.isActive();

            if (session.getStatus() == com.politicalsim.game.GameStatus.DEFEAT) {
                System.out.println("  ❗ Game ended with DEFEAT — you lost the election.");
            } else if (session.getStatus() == com.politicalsim.game.GameStatus.GAME_OVER) {
                System.out.println("  ❗ Game ended with GAME_OVER — check if party was eliminated mid-game.");
            } else if (session.getStatus() == com.politicalsim.game.GameStatus.FORFEITED) {
                System.out.println("  ❗ Game was FORFEITED — session abandoned.");
            }

            if (support < 15) {
                System.out.printf("  📉 Support collapsed to %d%% — below the survival threshold.%n", support);
            }
            if (coins > 80 && dead) {
                System.out.printf("  💰 Coin hoarding: left %d coins unspent despite being eliminated.%n", coins);
            }
            if (morale < 15) {
                System.out.printf("  😤 Party morale was critically low (%d) — may have caused effectiveness penalties.%n", morale);
            }
            if (corrupt > 75) {
                System.out.printf("  🔥 Corruption at %d%% — likely triggered scandal/penalty events.%n", corrupt);
            }
            if (support >= 15 && !dead) {
                System.out.println("  📊 Your party was alive but the election result went against you — opponents had higher cumulative support.");
            }
        } else {
            System.out.println("  (no HUMAN party found in session — cannot diagnose)");
        }

        System.out.println("\n╚══════════════════════════════════════════════════════════════╝");
        System.out.println(  "                      AUTOPSY COMPLETE");
        System.out.println(  "╚══════════════════════════════════════════════════════════════╝\n");
    }

    // ──────────────────────────────────────────────────────────────────────────
    // Test 3: Deep AI Performance Analyzer — most recent game of any scenario
    // ──────────────────────────────────────────────────────────────────────────
    @Test
    @Disabled("Diagnostic/Interactive test — enable manually when needed")
    void analyzeAiPerformanceInLastGame() {
        System.out.println("\n========== AI PERFORMANCE DEEP ANALYSIS ==========");

        List<GameSession> all = repository.findAllByOrderByCurrentDateDesc();
        if (all.isEmpty()) {
            System.out.println("No sessions found.");
            return;
        }

        // Try uttar pradesh first, fall back to most recent
        GameSession session = all.stream()
                .filter(g -> g.getScenarioKey() != null && g.getScenarioKey().contains("uttar"))
                .findFirst()
                .orElse(all.get(0));

        System.out.printf("%n📋 GAME: %s (%s)  |  Status: %s  |  Turn: %d  |  ID: %s%n",
                session.getScenarioKey(), session.getScenarioName(),
                session.getStatus(), session.getTurnNumber(), session.getId());

        // ── Final stats table ──
        System.out.println("\n📊 FINAL PARTY STATS:");
        System.out.printf("  %-25s %-12s %-8s %-8s %-8s %-12s %-8s %-8s%n",
                "Party", "Controller", "Status", "Coins", "Morale", "Corruption", "Media", "Support%");
        System.out.println("  " + "─".repeat(95));
        for (PartyState p : session.getParties()) {
            System.out.printf("  %-25s %-12s %-8s %-8d %-8d %-12d %-8d %-8d%%%n",
                    p.getName(), p.getControllerType(),
                    p.isActive() ? "✅ ALIVE" : "❌ OUT",
                    p.getStats().getCoins(), p.getStats().getPartyMorale(),
                    p.getStats().getCorruptionScore(), p.getStats().getMediaImage(),
                    p.getStats().getPublicSupport());
        }

        // ── Card usage ──
        System.out.println("\n🃏 AI CARD USAGE TOTALS:");
        for (PartyState p : session.getParties()) {
            if (p.getControllerType() != ControllerType.COMPUTER) continue;
            System.out.println("  [" + p.getName() + " — " + (p.isActive() ? "SURVIVED" : "ELIMINATED") + "]");
            Map<String, Integer> usage = session.getCardUsageByParty() == null ? null
                    : session.getCardUsageByParty().get(p.getId());
            if (usage == null || usage.isEmpty()) {
                System.out.println("    (no usage data)");
            } else {
                usage.entrySet().stream()
                        .sorted((a, b) -> b.getValue() - a.getValue())
                        .forEach(e -> System.out.printf("    %-50s  ×%d%n", e.getKey(), e.getValue()));
            }
        }

        // ── Last round submissions ──
        System.out.println("\n⚙️  LAST ROUND AI DECISIONS:");
        if (session.getLastRoundSubmissions() != null) {
            for (RoundSubmission sub : session.getLastRoundSubmissions()) {
                System.out.println("  [" + sub.getPartyName() + "]");
                System.out.println("    Card   : " + sub.getCardName() + " (" + sub.getCardKey() + ")");
                System.out.println("    Intent : " + sub.getAiIntent());
                System.out.println("    Basis  : " + sub.getAiDecisionBasis());
            }
        }

        // ── Last round commentary ──
        System.out.println("\n📰 LAST ROUND FULL COMMENTARY:");
        if (session.getLastRoundCommentary() != null) {
            session.getLastRoundCommentary().forEach(c -> System.out.println("  " + c));
        }

        // ── Mistake analysis ──
        System.out.println("\n🔍 AI MISTAKE ANALYSIS:");
        for (PartyState p : session.getParties()) {
            if (p.getControllerType() != ControllerType.COMPUTER) continue;

            int coins    = p.getStats().getCoins();
            int support  = p.getStats().getPublicSupport();
            int morale   = p.getStats().getPartyMorale();
            int corrupt  = p.getStats().getCorruptionScore();
            boolean dead = !p.isActive();

            System.out.println("\n  ┌─ " + p.getName() + " (" + (dead ? "ELIMINATED" : "SURVIVED") + ")");
            System.out.printf(  "  │  Final: Coins=%d  Support=%d%%  Morale=%d  Corruption=%d%%%n",
                    coins, support, morale, corrupt);

            boolean flagged = false;

            // Coin hoarding
            if (dead && coins > 100) {
                System.out.printf(  "  │  🚨 COIN HOARDING: Eliminated with %d coins unspent!%n", coins);
                System.out.println("  │     Root cause: AI intent probably stuck on RAISE_FUNDS instead of switching");
                System.out.println("  │     to GAIN_SUPPORT when support fell dangerously low.");
                System.out.println("  │     Fix: Lower 'lowCoins' threshold so RAISE_FUNDS doesn't trigger needlessly.");
                System.out.println("  │     Fix: Ensure intent switches to GAIN_SUPPORT before support reaches 15%.");
                flagged = true;
            } else if (dead && coins > 50) {
                System.out.printf(  "  │  ⚠️  PARTIAL COIN HOARDING: Eliminated with %d coins — some misallocation.%n", coins);
                flagged = true;
            }

            // High coins + low support = worst case misalignment
            if (coins > 60 && support < 15) {
                System.out.printf(  "  │  🎯 CRITICAL MISALIGNMENT: %d coins but only %d%% support!%n", coins, support);
                System.out.println("  │     AI collected wealth instead of converting it to voter support.");
                System.out.println("  │     Fix: Add explicit GAIN_SUPPORT intent trigger when support < 20%,");
                System.out.println("  │     regardless of coin levels, with higher priority than RAISE_FUNDS.");
                flagged = true;
            }

            // Support collapse
            if (support < 10) {
                System.out.printf(  "  │  📉 SUPPORT COLLAPSE: Final support %d%% — below 10%% elimination threshold.%n", support);
                System.out.println("  │     AI failed to prioritise survival cards when approaching defeat.");
                flagged = true;
            }

            // Morale collapse
            if (morale < 15) {
                System.out.printf(  "  │  😤 MORALE CRISIS: Final morale %d — party collapse imminent.%n", morale);
                flagged = true;
            }

            // Corruption runaway
            if (corrupt > 80) {
                System.out.printf(  "  │  🔥 CORRUPTION RUNAWAY: %d%% — near scandal defeat threshold.%n", corrupt);
                flagged = true;
            }

            // Card variety check
            Map<String, Integer> usage = session.getCardUsageByParty() == null ? null
                    : session.getCardUsageByParty().get(p.getId());
            if (usage != null) {
                long overused = usage.values().stream().filter(v -> v >= 3).count();
                if (overused > 0) {
                    System.out.printf("  │  🔁 CARD OVERUSE: %d card(s) played 3+ times — low tactical variety.%n", overused);
                    System.out.println("  │     Exhausting cards early leaves weak options for critical late turns.");
                    flagged = true;
                }
            }

            // Project freeze despite healthy resources
            if (dead && coins > 150 && morale > 40) {
                System.out.println("  │  🏗️  WASTED BUILDING BUDGET: Had resources to build but may have been frozen.");
                System.out.println("  │     Projects yield passive coins/support over 10 turns — could have helped.");
                flagged = true;
            }

            if (!flagged) {
                System.out.println("  │  ✅ No major mistakes detected.");
            }
            System.out.println("  └───────────────────────────────");
        }

        System.out.println("\n========== ANALYSIS COMPLETE ==========\n");
    }

    @Test
    @Disabled("Diagnostic/Interactive test — enable manually when needed")
    void printYdpSupportChangeForAndhra2001() {
        System.out.println("\n========== YDP SUPPORT CHANGE FOR ANDHRA 2001 ==========");
        // Find the most recent game session for Andhra 2001 scenario
        GameSession session = repository.findAllByOrderByCurrentDateDesc().stream()
                .filter(s -> s.getScenarioKey() != null && s.getScenarioKey().contains("andhra_pradesh_2001"))
                .findFirst()
                .orElse(null);
        if (session == null) {
            System.out.println("No Andhra 2001 game session found.");
            return;
        }
        // Identify YDP party id
        String ydpId = session.getParties().stream()
                .filter(p -> p.getName().toLowerCase().contains("youth") || p.getName().toLowerCase().contains("ydp"))
                .map(p -> p.getId())
                .findFirst()
                .orElse(null);
        if (ydpId == null) {
            System.out.println("YDP party not found in session.");
            return;
        }
        // Get last metric delta for YDP support if available
        Integer delta = null;
        if (session.getLastMetricDeltas() != null && session.getLastMetricDeltas().containsKey(ydpId)) {
            Map<String, Integer> partyDelta = session.getLastMetricDeltas().get(ydpId);
            if (partyDelta != null) {
                delta = partyDelta.get("support");
            }
        }
        // Get current support
        int currentSupport = session.getParties().stream()
                .filter(p -> p.getId().equals(ydpId))
                .mapToInt(p -> p.getStats().getPublicSupport())
                .findFirst()
                .orElse(-1);
        System.out.println("YDP current support: " + currentSupport + "%");
        if (delta != null) {
            System.out.println("Last round support delta for YDP: " + delta + "%");
        } else {
            System.out.println("No support delta data available for YDP.");
        }
        System.out.println("========== END YDP SUPPORT ANALYSIS ==========");
    }

    @Test
    @Disabled("Diagnostic/Interactive test — enable manually when needed")
    void printYdpProjectsInfo() {
        System.out.println("\n========== YDP PROJECTS INFO ===========");
        GameSession session = repository.findAllByOrderByCurrentDateDesc().stream()
                .filter(s -> s.getScenarioKey() != null && s.getScenarioKey().contains("andhra_pradesh_2001"))
                .findFirst()
                .orElse(null);
        if (session == null) {
            System.out.println("No Andhra 2001 game session found.");
            return;
        }
        PartyState ydp = session.getParties().stream()
                .filter(p -> p.getName().toLowerCase().contains("youth") || p.getName().toLowerCase().contains("ydp"))
                .findFirst()
                .orElse(null);
        if (ydp == null) {
            System.out.println("YDP party not found.");
            return;
        }
        if (ydp.getProjects() == null || ydp.getProjects().isEmpty()) {
            System.out.println("YDP has no projects.");
            return;
        }
        for (var proj : ydp.getProjects()) {
            com.politicalsim.party.BuildingProject def = com.politicalsim.party.BuildingProject.valueOf(proj.getProjectKey());
            int prog = proj.getProgressPercent();
            System.out.printf("  - %s : %d%% completed (Benefits: Coins=%d, Morale=%d, Media=%d, Corruption=%d, Support=%d)\n",
                    def.getName(), prog, def.getBenefitCoins(), def.getBenefitMorale(), def.getBenefitMedia(),
                    def.getBenefitCorruption(), def.getBenefitSupport());
        }
    }

    @Test
    @Disabled("Diagnostic/Interactive test — enable manually when needed")
    void printYdpPassiveYieldTotals() {

        // Find the most recent Andhra 2001 session
        GameSession session = repository.findAllByOrderByCurrentDateDesc().stream()
                .filter(s -> s.getScenarioKey() != null && s.getScenarioKey().contains("andhra_pradesh_2001"))
                .findFirst()
                .orElse(null);
        if (session == null) {
            System.out.println("No Andhra 2001 game session found.");
            return;
        }
        // Locate YDP party
        PartyState ydp = session.getParties().stream()
                .filter(p -> p.getName().toLowerCase().contains("youth") || p.getName().toLowerCase().contains("ydp"))
                .findFirst()
                .orElse(null);
        if (ydp == null) {
            System.out.println("YDP party not found.");
            return;
        }
        // Sum passive yields from all funded projects (including partial progress)
        int totalCoins = 0, totalMorale = 0, totalMedia = 0, totalCorruption = 0, totalSupport = 0;
        if (ydp.getProjects() != null) {
            for (var proj : ydp.getProjects()) {
                if (proj.getProgressPercent() <= 0) continue;
                com.politicalsim.party.BuildingProject def = com.politicalsim.party.BuildingProject.valueOf(proj.getProjectKey());
                double factor = proj.getProgressPercent() / 100.0;
                totalCoins += (int) Math.round(def.getBenefitCoins() * factor);
                totalMorale += (int) Math.round(def.getBenefitMorale() * factor);
                totalMedia += (int) Math.round(def.getBenefitMedia() * factor);
                totalCorruption += (int) Math.round(def.getBenefitCorruption() * factor);
                totalSupport += (int) Math.round(def.getBenefitSupport() * factor);
            }
        }
        System.out.println("YDP total passive yields from all projects this turn:");
        System.out.println("  Coins: " + totalCoins + " | Morale: " + totalMorale + " | Media: " + totalMedia + " | Corruption: " + totalCorruption + " | Support: " + totalSupport + "%");
        System.out.println("========== END YDP PASSIVE YIELD TOTALS ==========");
    }

    @Test
    @Disabled("Diagnostic/Interactive test — enable manually when needed")
    void exportDatabaseSeedData() throws Exception {
        System.out.println("\n========== EXPORTING SEED DATA ==========");
        java.io.File dir = new java.io.File("../seed-data/startup");
        if (!dir.exists()) {
            dir.mkdirs();
        }
        
        com.fasterxml.jackson.databind.ObjectMapper mapper = new com.fasterxml.jackson.databind.ObjectMapper();
        mapper.registerModule(new com.fasterxml.jackson.datatype.jsr310.JavaTimeModule());
        mapper.enable(com.fasterxml.jackson.databind.SerializationFeature.INDENT_OUTPUT);
        
        List<ScenarioDefinition> scenarios = scenarioDefinitionRepository.findAll();
        mapper.writeValue(new java.io.File(dir, "scenarios.json"), scenarios);
        System.out.println("Exported " + scenarios.size() + " scenarios.");
        
        List<CardDefinition> cards = cardRepository.findAll();
        mapper.writeValue(new java.io.File(dir, "cards.json"), cards);
        System.out.println("Exported " + cards.size() + " cards.");
        
        List<NewsDefinition> news = newsRepository.findAll();
        mapper.writeValue(new java.io.File(dir, "news.json"), news);
        System.out.println("Exported " + news.size() + " news.");
        
        List<MonthlyIssueDefinition> issues = issueRepository.findAll();
        mapper.writeValue(new java.io.File(dir, "issues.json"), issues);
        System.out.println("Exported " + issues.size() + " issues.");
        
        System.out.println("========== EXPORT COMPLETE ==========\n");
    }


    @Test
    @Disabled("Diagnostic/Interactive test — enable manually when needed")
    void printYdpProjectsSupportInfo() {
        System.out.println("\n========== YDP PROJECT SUPPORT INFO ==========");
        GameSession session = repository.findAllByOrderByCurrentDateDesc().stream()
                .filter(s -> s.getScenarioKey() != null && s.getScenarioKey().contains("andhra_pradesh_2001"))
                .findFirst()
                .orElse(null);
        if (session == null) {
            System.out.println("No Andhra 2001 game session found.");
            return;
        }

        PartyState ydp = session.getParties().stream()
                .filter(p -> p.getName().toLowerCase().contains("youth") || p.getName().toLowerCase().contains("ydp"))
                .findFirst()
                .orElse(null);
        if (ydp == null) {
            System.out.println("YDP party not found.");
            return;
        }

        if (ydp.getProjects() == null || ydp.getProjects().isEmpty()) {
            System.out.println("YDP has no projects.");
            return;
        }

        int cumulativeSupport = 0;
        for (var proj : ydp.getProjects()) {
            com.politicalsim.party.BuildingProject def = com.politicalsim.party.BuildingProject.valueOf(proj.getProjectKey());
            int prog = proj.getProgressPercent();                     // progress %
            int supportBenefit = (int) Math.round(def.getBenefitSupport() * prog / 100.0);
            cumulativeSupport += supportBenefit;
            System.out.printf("  - %s : %d%% progress → support benefit = %d%%%n",
                    def.getName(), prog, supportBenefit);
        }
        System.out.println("Cumulative YDP support from all projects (scaled) = " + cumulativeSupport + "%");
        System.out.println("========== END YDP PROJECT SUPPORT INFO ==========");
    }
}
