package com.politicalsim.content;

import java.util.Optional;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface ScenarioDefinitionRepository extends MongoRepository<ScenarioDefinition, String> {

    Optional<ScenarioDefinition> findByScenarioKey(String scenarioKey);
}
