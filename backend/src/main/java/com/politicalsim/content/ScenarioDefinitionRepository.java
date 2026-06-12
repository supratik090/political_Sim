package com.politicalsim.content;

import java.util.List;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface ScenarioDefinitionRepository extends MongoRepository<ScenarioDefinition, String> {

    List<ScenarioDefinition> findByScenarioKey(String scenarioKey);
}
