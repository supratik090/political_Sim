package com.politicalsim.content;

import java.util.List;
import java.util.Optional;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface StateInfrastructureDefinitionRepository extends MongoRepository<StateInfrastructureDefinition, String> {
    Optional<StateInfrastructureDefinition> findByKey(String key);
    List<StateInfrastructureDefinition> findByCategory(String category);
    List<StateInfrastructureDefinition> findByScope(String scope);
}
