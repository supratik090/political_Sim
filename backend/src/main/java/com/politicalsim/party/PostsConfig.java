package com.politicalsim.party;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;

/**
 * Registry of all political posts available in the game, loaded dynamically from JSON config.
 * Each post has a unique key, display name, loyalty boost, and resource yields
 * applied when the post is assigned to a faction.
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

    public static final List<PostDefinition> ALL_POSTS = new CopyOnWriteArrayList<>();

    static {
        loadConfigsFromClasspath();
    }

    private static void loadConfigsFromClasspath() {
        try {
            ObjectMapper mapper = new ObjectMapper();
            InputStream stream = PostsConfig.class.getResourceAsStream("/config/posts_config.json");
            if (stream != null) {
                List<PostDefinition> loaded = mapper.readValue(stream, new TypeReference<List<PostDefinition>>() {});
                ALL_POSTS.addAll(loaded);
            } else {
                System.err.println("⚠️ posts_config.json not found on classpath!");
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.err.println("❌ Failed to parse posts_config.json: " + e.getMessage());
        }
    }

    /**
     * Returns a shuffled copy of the posts with turn numbers assigned.
     * Turn 1 gets the first 2 posts (Secretary + Fund Manager to guarantee useful start),
     * then one post every 5 turns (turn 5, 10, 15, ...) in random order.
     */
    public static List<ScheduledPost> buildScheduledPosts() {
        List<PostDefinition> shuffled = new ArrayList<>(ALL_POSTS);
        // Keep Secretary and Fund Manager at the front for Turn 1
        PostDefinition secretary = findByKey("SECRETARY", shuffled);
        PostDefinition fundManager = findByKey("FUND_MANAGER", shuffled);
        if (secretary != null) shuffled.remove(secretary);
        if (fundManager != null) shuffled.remove(fundManager);
        Collections.shuffle(shuffled);

        List<PostDefinition> ordered = new ArrayList<>();
        if (secretary != null) ordered.add(secretary);
        if (fundManager != null) ordered.add(fundManager);
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
     * Find a PostDefinition by its display name.
     */
    public static PostDefinition findByName(String name) {
        return ALL_POSTS.stream().filter(p -> p.name().equalsIgnoreCase(name)).findFirst().orElse(null);
    }

    private PostsConfig() {}
}
