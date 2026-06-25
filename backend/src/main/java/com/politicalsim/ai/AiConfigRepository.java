package com.politicalsim.ai;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;
import java.util.Optional;

@Repository
public interface AiConfigRepository extends MongoRepository<AiTuningConfig, String> {

    /** Returns the highest-version active config document. */
    Optional<AiTuningConfig> findTopByActiveTrueOrderByVersionDesc();

    /** Useful for admin: fetch a specific version. */
    Optional<AiTuningConfig> findByVersion(int version);
}
