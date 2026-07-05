package com.politicalsim.content;

import java.util.concurrent.ConcurrentHashMap;
import java.util.List;
import java.util.ArrayList;

public class DefinitionCache {
    public static final ConcurrentHashMap<String, List<CardDefinition>> cardsCache = new ConcurrentHashMap<>();
    public static final ConcurrentHashMap<String, List<NewsDefinition>> newsCache = new ConcurrentHashMap<>();
    public static final ConcurrentHashMap<String, List<MonthlyIssueDefinition>> issuesCache = new ConcurrentHashMap<>();
    public static final ConcurrentHashMap<String, List<LegislativeBillDefinition>> billsCache = new ConcurrentHashMap<>();
    public static final ConcurrentHashMap<String, List<EventCardDefinition>> eventsCache = new ConcurrentHashMap<>();

    public static List<LegislativeBillDefinition> getBillsForScenario(LegislativeBillDefinitionRepository repository, String scenarioKey) {
        String key = scenarioKey == null ? "default" : scenarioKey;
        return billsCache.computeIfAbsent(key, k -> {
            List<LegislativeBillDefinition> list = repository.findByScenarioKey(k);
            if (list.isEmpty() && !k.equals("default")) {
                list = repository.findByScenarioKey("default");
            }
            return list;
        });
    }

    public static List<EventCardDefinition> getEventsForScenario(EventCardDefinitionRepository repository, String scenarioKey) {
        String key = scenarioKey == null ? "default" : scenarioKey;
        return eventsCache.computeIfAbsent(key, k -> {
            List<EventCardDefinition> list = repository.findByScenarioKey(k);
            if (list.isEmpty() && !k.equals("default")) {
                list = repository.findByScenarioKey("default");
            }
            return list;
        });
    }

    public static void clearAll() {
        cardsCache.clear();
        newsCache.clear();
        issuesCache.clear();
        billsCache.clear();
        eventsCache.clear();
        com.politicalsim.game.GameSessionService.clearCaches();
    }
}
