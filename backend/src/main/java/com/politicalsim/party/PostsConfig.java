package com.politicalsim.party;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Static registry of all 15 political posts available in the game.
 * Each post has a unique key, display name, loyalty boost, and resource yields
 * applied when the post is assigned to a faction.
 *
 * On game startup, the full list is shuffled and spread across turns for a party.
 */
public final class PostsConfig {

    public record PostDefinition(
            String key,
            String name,
            String icon,
            String description,
            int loyaltyBoost,
            int coinYieldBonus,    // Extra coins/turn from this post
            int moraleYieldBonus,  // Extra morale/turn from this post
            int mediaYieldBonus    // Extra media/turn from this post
    ) {}

    public static final List<PostDefinition> ALL_POSTS = List.of(
        new PostDefinition("SECRETARY",          "Secretary",               "📋", "Party's chief administrator. Boosts loyalty and morale coordination.",               15, 0,  6, 0),
        new PostDefinition("PRESS_SECRETARY",    "Press Secretary",         "📰", "Manages party communications and media. Improves media image.",                     8,  0,  0, 4),
        new PostDefinition("FUND_MANAGER",       "Fund Manager",            "💰", "Oversees party finances. Significantly boosts coin income.",                        10, 8,  0, 0),
        new PostDefinition("DISTRICT_HEAD",      "District Head",           "🏘️", "Leads party operations in a district. Provides grassroots morale.",                  5,  0,  3, 0),
        new PostDefinition("CAMPAIGN_MANAGER",   "Campaign Manager",        "📣", "Strategizes election campaigns. Boosts support and morale.",                        10, 0,  4, 2),
        new PostDefinition("LEADER_IN_HOUSE",    "Leader in House",         "🏛️", "Represents party in legislative house. Improves public support.",                   8,  2,  2, 0),
        new PostDefinition("CHIEF_WHIP",         "Chief Whip",              "⚖️", "Enforces party discipline. Stabilises loyalty across factions.",                    7,  0,  3, 0),
        new PostDefinition("YOUTH_WING_PRES",    "Youth Wing President",    "✊", "Leads the youth wing. Energises younger members, boosts morale.",                   6,  0,  4, 1),
        new PostDefinition("TRADE_UNION_LIAISON","Trade Union Liaison",     "🤝", "Bridges party and unions. Improves coin yields from labour sectors.",               6,  3,  2, 0),
        new PostDefinition("POLICY_DIRECTOR",    "Policy Director",         "🧠", "Shapes party policy agenda. Increases media image significantly.",                  9,  0,  0, 5),
        new PostDefinition("STATE_COORDINATOR",  "State Coordinator",       "🗺️", "Manages party operations across the state. Improves coins and morale.",             11, 4,  3, 0),
        new PostDefinition("DIGITAL_MEDIA_HEAD", "Digital Media Head",      "💻", "Runs party's digital/social media. Provides strong media boost.",                   7,  0,  0, 6),
        new PostDefinition("ELECTION_STRATEGIST","Election Strategist",     "🗳️", "Plans electoral strategy. Major morale and media improvements.",                   12, 0,  4, 4),
        new PostDefinition("SPOKESPERSON",       "Spokesperson",            "🎤", "Official voice of the party. Boosts media image.",                                  5,  0,  0, 3),
        new PostDefinition("TREASURER",          "Treasurer",               "🏦", "Controls party treasury. Large coin income boost.",                                 14, 10, 0, 0)
    );

    /**
     * Returns a shuffled copy of the 15 posts with turn numbers assigned.
     * Turn 1 gets the first 2 posts (Secretary + Fund Manager to guarantee useful start),
     * then one post every 5 turns (turn 5, 10, 15, ...) in random order.
     *
     * @return List of ScheduledPost in turn-ascending order
     */
    public static List<ScheduledPost> buildScheduledPosts() {
        List<PostDefinition> shuffled = new ArrayList<>(ALL_POSTS);
        // Keep Secretary and Fund Manager at the front for Turn 1
        PostDefinition secretary = findByKey("SECRETARY", shuffled);
        PostDefinition fundManager = findByKey("FUND_MANAGER", shuffled);
        shuffled.remove(secretary);
        shuffled.remove(fundManager);
        Collections.shuffle(shuffled);

        List<PostDefinition> ordered = new ArrayList<>();
        ordered.add(secretary);
        ordered.add(fundManager);
        ordered.addAll(shuffled);

        List<ScheduledPost> result = new ArrayList<>();
        for (int i = 0; i < ordered.size(); i++) {
            PostDefinition def = ordered.get(i);
            int turn;
            if (i == 0 || i == 1) {
                turn = 1; // Both Secretary and Fund Manager available on Turn 1
            } else {
                // Every 5 turns after that: turn 5, 10, 15, ...
                turn = (i - 1) * 5;
            }
            result.add(new ScheduledPost(def.key(), def.name(), turn));
        }
        return result;
    }

    public static PostDefinition findByKey(String key, List<PostDefinition> list) {
        return list.stream().filter(p -> p.key().equals(key)).findFirst().orElse(null);
    }

    public static PostDefinition findByKey(String key) {
        return ALL_POSTS.stream().filter(p -> p.key().equals(key)).findFirst().orElse(null);
    }

    /**
     * Find a PostDefinition by its display name (for backwards-compat with old string-based logic).
     */
    public static PostDefinition findByName(String name) {
        return ALL_POSTS.stream().filter(p -> p.name().equalsIgnoreCase(name)).findFirst().orElse(null);
    }

    private PostsConfig() {}
}
