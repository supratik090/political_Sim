package com.politicalsim.content;

import java.util.List;

import org.springframework.cache.annotation.Cacheable;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface ScenarioDefinitionRepository extends MongoRepository<ScenarioDefinition, String> {

    @Cacheable(value = "scenarioDefinitions", key = "#scenarioKey")
    List<ScenarioDefinition> findByScenarioKey(String scenarioKey);
}
