package com.politicalsim.content;

import java.util.List;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface LegislativeBillDefinitionRepository extends MongoRepository<LegislativeBillDefinition, String> {
    List<LegislativeBillDefinition> findByScenarioKey(String scenarioKey);
    List<LegislativeBillDefinition> findByScenarioKeyAndActiveTrue(String scenarioKey);
}
