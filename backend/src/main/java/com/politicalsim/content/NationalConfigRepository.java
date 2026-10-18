package com.politicalsim.content;

import java.util.Optional;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface NationalConfigRepository extends MongoRepository<NationalConfig, String> {
    Optional<NationalConfig> findByEra(int era);
    boolean existsByEra(int era);
}
