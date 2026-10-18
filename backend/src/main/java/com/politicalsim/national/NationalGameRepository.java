package com.politicalsim.national;

import org.springframework.data.mongodb.repository.MongoRepository;
import java.util.List;
import java.util.Optional;

public interface NationalGameRepository extends MongoRepository<NationalGame, String> {
    Optional<NationalGame> findByUserIdAndStatus(String userId, String status);
    Optional<NationalGame> findFirstByUserIdAndStatusOrderByCreatedAtDesc(String userId, String status);
    Optional<NationalGame> findByUserId(String userId);
    List<NationalGame> findAllByUserId(String userId);
    boolean existsByUserIdAndStatus(String userId, String status);
}
