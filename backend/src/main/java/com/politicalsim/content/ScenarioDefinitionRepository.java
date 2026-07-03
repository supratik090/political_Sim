package com.politicalsim.content;

import java.util.List;

import org.springframework.cache.annotation.Cacheable;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface ScenarioDefinitionRepository extends MongoRepository<ScenarioDefinition, String> {

    @Cacheable(value = "scenarioDefinitions", key = "#scenarioKey")
    List<ScenarioDefinition> findByScenarioKey(String scenarioKey);


    @Cacheable(value = "scenarioDefinitionsLite")
    @Query(value = "{}",
            fields = "{ 'id': 1, 'scenarioKey': 1, 'name': 1, 'description': 1, 'stateName': 1, " +
                    "'startDate': 1, 'cycleLengthMonths': 1, 'governmentPartyName': 1, " +
                    "'oppositionPartyName': 1, 'thirdPartyName': 1, 'active': 1 }")
    List<ScenarioDefinitionLite> findAllSdLite();
}
