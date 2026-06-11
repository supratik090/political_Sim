package com.politicalsim.content;

import java.util.List;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface NewsDefinitionRepository extends MongoRepository<NewsDefinition, String> {

    List<NewsDefinition> findByScenarioKeyOrderByTypeAscTitleAsc(String scenarioKey);
}
