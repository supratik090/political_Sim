package com.politicalsim.content;

import java.util.List;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface MonthlyIssueDefinitionRepository extends MongoRepository<MonthlyIssueDefinition, String> {

    List<MonthlyIssueDefinition> findByScenarioKeyOrderByCategoryAscTitleAsc(String scenarioKey);
}
