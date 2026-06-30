package com.politicalsim.game;

import org.springframework.data.mongodb.repository.MongoRepository;
import java.util.List;

public interface GameSessionRepository extends MongoRepository<GameSession, String> {

    List<GameSession> findAllByOrderByCurrentDateDesc();
    List<GameSession> findByScenarioKeyAndStatus(String scenarioKey, GameStatus status);
    List<GameSession> findByScenarioKeyAndStatusAndUserId(String scenarioKey, GameStatus status, String userId);
    List<GameSession> findAllByUserIdOrderByCurrentDateDesc(String userId);
    List<GameSession> findByJoinCodeAndStatus(String joinCode, GameStatus status);
    List<GameSession> findByStatus(GameStatus status);
}
