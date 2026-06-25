package com.politicalsim.ai;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import java.util.concurrent.atomic.AtomicReference;

/**
 * Loads the active AI tuning config from MongoDB and caches it in memory.
 * <p>
 * Design decisions:
 * <ul>
 *   <li>No runtime flag — the service ALWAYS uses MongoDB as its source.</li>
 *   <li>Cached in a single AtomicReference; refreshed on every call to
 *       {@link #refresh()} (or explicitly by admin tooling).</li>
 *   <li>If MongoDB has no {@code active=true} document at all, a built-in
 *       fallback instance with all default values is returned so the game
 *       never crashes on a missing config.</li>
 *   <li>The cached instance is immutable at runtime; callers must NOT mutate it.</li>
 * </ul>
 */
@Service
public class AiConfigService {

    private static final Logger log = LoggerFactory.getLogger(AiConfigService.class);

    private final AiConfigRepository repository;
    private final AtomicReference<AiTuningConfig> cache = new AtomicReference<>(new AiTuningConfig());

    public AiConfigService(AiConfigRepository repository) {
        this.repository = repository;
        refresh(); // Load on startup
    }

    /**
     * Returns the current cached config.
     * This is the hot path — called on every AI decision; the AtomicReference
     * read is non-blocking and extremely cheap.
     */
    public AiTuningConfig get() {
        return cache.get();
    }

    /**
     * Reloads the latest active config from MongoDB and updates the cache.
     * Call this after an admin approves a new config version.
     * Thread-safe — uses compareAndSet-equivalent via AtomicReference.set.
     */
    public AiTuningConfig refresh() {
        AiTuningConfig loaded = repository.findTopByActiveTrueOrderByVersionDesc()
                .orElseGet(() -> {
                    log.warn("No active AI config found in MongoDB — using built-in defaults.");
                    return new AiTuningConfig();
                });
        cache.set(loaded);
        log.info("AI config loaded: version={} description='{}'", loaded.getVersion(), loaded.getDescription());
        return loaded;
    }

    /**
     * Convenience: returns the version string of the currently cached config.
     * Used to stamp into GameSession at game creation.
     */
    public String currentVersionLabel() {
        AiTuningConfig cfg = cache.get();
        return "v" + cfg.getVersion() + " — " + cfg.getDescription();
    }

    /**
     * Loads a specific version by number (for admin diff tooling).
     * Does NOT affect the cached version.
     */
    public AiTuningConfig loadVersion(int version) {
        return repository.findByVersion(version)
                .orElseThrow(() -> new IllegalArgumentException("AI config version not found: " + version));
    }

    /**
     * Saves a new config document and refreshes the cache so it is immediately active.
     * The caller is responsible for setting {@code active=true} and the correct version number.
     */
    public AiTuningConfig save(AiTuningConfig config) {
        AiTuningConfig saved = repository.save(config);
        refresh();
        return saved;
    }
}
