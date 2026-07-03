package com.politicalsim.game;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;
import java.util.List;

public interface GameSessionRepository extends MongoRepository<GameSession, String> {

    List<GameSession> findAllByOrderByCurrentDateDesc();
    List<GameSession> findByScenarioKeyAndStatus(String scenarioKey, GameStatus status);
    List<GameSession> findByScenarioKeyAndStatusAndUserId(String scenarioKey, GameStatus status, String userId);
    List<GameSession> findAllByUserIdOrderByCurrentDateDesc(String userId);
    List<GameSession> findByJoinCodeAndStatus(String joinCode, GameStatus status);
    List<GameSession> findByStatus(GameStatus status);

    /**
     * Fetch only the lightweight summary fields for a specific user.
     * Excludes heavy embedded arrays (gameCards, gameIssues, round submissions, etc.)
     * that cause full documents to be ~500KB each.
     */
    @Query(value = "{ 'userId': ?0 }",
           fields = "{ 'scenarioKey': 1, 'scenarioName': 1, 'currentDate': 1, 'turnNumber': 1," +
                    " 'status': 1, 'createdAt': 1, 'playerPartyId': 1, 'isMultiplayer': 1," +
                    " 'joinCode': 1, 'lastElectionWinner': 1, 'playerPartyIds': 1," +
                    " 'parties.id': 1, 'parties.name': 1, 'parties.role': 1," +
                    " 'parties.controllerType': 1, 'parties.color': 1, 'parties.symbol': 1, 'parties.ideology': 1 }")
    List<GameSession> findSummariesByUserId(String userId);

    /**
     * Fetch only lightweight summary fields for all sessions (admin / no-userId path).
     */
    @Query(value = "{}",
           fields = "{ 'scenarioKey': 1, 'scenarioName': 1, 'currentDate': 1, 'turnNumber': 1," +
                    " 'status': 1, 'createdAt': 1, 'playerPartyId': 1, 'isMultiplayer': 1," +
                    " 'joinCode': 1, 'lastElectionWinner': 1, 'playerPartyIds': 1," +
                    " 'parties.id': 1, 'parties.name': 1, 'parties.role': 1," +
                    " 'parties.controllerType': 1, 'parties.color': 1, 'parties.symbol': 1, 'parties.ideology': 1 }",
           sort = "{ 'currentDate': -1 }")
    List<GameSession> findAllSummaries();
}
