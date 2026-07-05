package com.politicalsim.content;

import java.util.List;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface EventCardDefinitionRepository extends MongoRepository<EventCardDefinition, String> {
    List<EventCardDefinition> findByScenarioKey(String scenarioKey);
    List<EventCardDefinition> findByScenarioKeyAndActiveTrue(String scenarioKey);
}
