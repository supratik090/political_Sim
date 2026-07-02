package com.politicalsim.content;

import java.util.List;

import org.springframework.cache.annotation.Cacheable;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface NewsDefinitionRepository extends MongoRepository<NewsDefinition, String> {

    @Cacheable(value = "newsDefinitions", key = "#scenarioKey")
    List<NewsDefinition> findByScenarioKeyOrderByTypeAscTitleAsc(String scenarioKey);
}
