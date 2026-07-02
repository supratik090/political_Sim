package com.politicalsim.content;

import java.util.List;

import org.springframework.cache.annotation.Cacheable;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface CardDefinitionRepository extends MongoRepository<CardDefinition, String> {

    @Cacheable(value = "cardDefinitions", key = "#scenarioKey")
    List<CardDefinition> findByScenarioKeyOrderByCategoryAscNameAsc(String scenarioKey);
}
