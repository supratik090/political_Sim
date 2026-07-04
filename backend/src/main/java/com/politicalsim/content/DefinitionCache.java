package com.politicalsim.content;

import java.util.concurrent.ConcurrentHashMap;
import java.util.List;

public class DefinitionCache {
    public static final ConcurrentHashMap<String, List<CardDefinition>> cardsCache = new ConcurrentHashMap<>();
    public static final ConcurrentHashMap<String, List<NewsDefinition>> newsCache = new ConcurrentHashMap<>();
    public static final ConcurrentHashMap<String, List<MonthlyIssueDefinition>> issuesCache = new ConcurrentHashMap<>();

    public static void clearAll() {
        cardsCache.clear();
        newsCache.clear();
        issuesCache.clear();
        com.politicalsim.game.GameSessionService.clearCaches();
    }
}
