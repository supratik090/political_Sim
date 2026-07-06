package com.politicalsim.content;

import java.util.List;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface FactionDefinitionRepository extends MongoRepository<FactionDefinition, String> {
    List<FactionDefinition> findByScenarioKey(String scenarioKey);
    List<FactionDefinition> findByScenarioKeyAndFactionKey(String scenarioKey, String factionKey);
}
