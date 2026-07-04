package com.politicalsim.game;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface GameSessionContentRepository extends MongoRepository<GameSessionContent, String> {
}
