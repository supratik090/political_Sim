package com.politicalsim.content;

import java.util.List;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface MonthlyIssueDefinitionRepository extends MongoRepository<MonthlyIssueDefinition, String> {

    /** Sorted query — used only for admin/seeding views */
    List<MonthlyIssueDefinition> findByScenarioKeyOrderByCategoryAscTitleAsc(String scenarioKey);

    /** Unsorted query — used for per-game random sampling */
    List<MonthlyIssueDefinition> findByScenarioKey(String scenarioKey);
}
