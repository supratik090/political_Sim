package com.politicalsim.content;

import java.util.List;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface CardDefinitionRepository extends MongoRepository<CardDefinition, String> {

    List<CardDefinition> findByScenarioKeyOrderByCategoryAscNameAsc(String scenarioKey);
}
