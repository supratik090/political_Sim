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
    @Disabled("Diagnostic/Interactive test")
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
    @Disabled("Diagnostic/Interactive test")
    void printLastGameSessionDetails() {
        System.out.println("\n========== DB DIAGNOSTIC TEST START ==========");
        List<GameSession> sessions = repository.findAllByOrderByCurrentDateDesc();
        if (sessions.isEmpty()) {
            System.out.println("No game sessions found in database!");
            return;
        }

        int count = Math.min(sessions.size(), 5);
        System.out.println("Found " + sessions.size() + " total sessions. Printing top " + count + ":");
        for (int i = 0; i < count; i++) {
            GameSession session = sessions.get(i);
            System.out.println("\n------------------------------------------------");
            System.out.println("Game #" + (i + 1) + " ID: " + session.getId());
            System.out.println("Scenario : " + session.getScenarioKey() + " (" + session.getScenarioName() + ")");
            System.out.println("Status   : " + session.getStatus() + "  |  Turn: " + session.getTurnNumber());
            System.out.println("Created  : " + session.getCreatedAt());

            System.out.println("\n--- Party Stats ---");
            for (PartyState p : session.getParties()) {
                String delta = "";
                if (session.getLastMetricDeltas() != null && session.getLastMetricDeltas().containsKey(p.getId())) {
                    delta = "  Δ" + session.getLastMetricDeltas().get(p.getId());
                }
                System.out.printf("  %-25s  %-9s  %-8s  coins=%-5d  morale=%-4d  corruption=%-4d  media=%-4d  support=%d%%%s%n",
                        p.getName(), p.getControllerType(), p.isActive() ? "ACTIVE" : "DEFEATED",
                        p.getStats().getCoins(), p.getStats().getPartyMorale(),
                        p.getStats().getCorruptionScore(), p.getStats().getMediaImage(),
                        p.getStats().getPublicSupport(), delta);
            }

            System.out.println("\n--- Last Round Submissions ---");
            if (session.getLastRoundSubmissions() != null) {
                for (RoundSubmission sub : session.getLastRoundSubmissions()) {
                    System.out.println("  [" + sub.getPartyName() + "] Card: " + sub.getCardName()
                            + "  Intent: " + sub.getAiIntent() + "  Bid: " + sub.getBid());
                    if (sub.getAiDecisionBasis() != null) {
                        System.out.println("    → " + sub.getAiDecisionBasis());
                    }
                }
            }

            System.out.println("\n--- Last Round Commentary ---");
            if (session.getLastRoundCommentary() != null) {
                session.getLastRoundCommentary().forEach(c -> System.out.println("  " + c));
            }
        }
        System.out.println("\n========== DB DIAGNOSTIC TEST END ==========\n");
    }

    // ──────────────────────────────────────────────────────────────────────────
    // Test 3: Deep AI Performance Analyzer — most recent game of any scenario
    // ──────────────────────────────────────────────────────────────────────────
    @Test
    @Disabled("Diagnostic/Interactive test")
    void analyzeAiPerformanceInLastGame() {
        System.out.println("\n========== AI PERFORMANCE DEEP ANALYSIS ==========");

        List<GameSession> all = repository.findAllByOrderByCurrentDateDesc();
        if (all.isEmpty()) {
            System.out.println("No sessions found.");
            return;
        }

        // Try west_bengal_2001 first, fall back to most recent
        GameSession session = all.stream()
                .filter(g -> g.getScenarioKey() != null && g.getScenarioKey().contains("2001"))
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
    @Disabled("Diagnostic/Interactive test")
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
}
