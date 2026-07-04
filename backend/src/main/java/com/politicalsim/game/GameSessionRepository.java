package com.politicalsim.game;

import com.politicalsim.party.PartyState;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

import java.util.ArrayList;
import java.util.List;

public interface GameSessionRepository extends MongoRepository<GameSession, String> {

    List<GameSession> findAllByOrderByCurrentDateDesc();
    List<GameSession> findByScenarioKeyAndStatus(String scenarioKey, GameStatus status);
    List<GameSession> findByScenarioKeyAndStatusAndUserId(String scenarioKey, GameStatus status, String userId);
    // The Dynamic Method: pass either GameSession.class or GameSessionDTO.class
    @Query(value = "{ $or: [ { 'userId': ?0 }, { $expr: { $in: [ ?0, { $map: { input: { $objectToArray: { $ifNull: [ '$humanPlayerMap', {} ] } }, in: '$$this.v' } } ] } } ] }", sort = "{ 'currentDate': -1 }")
    <T> List<T> findAllByUserIdOrderByCurrentDateDesc(String userId, Class<T> type);
    List<GameSession> findByJoinCode(String joinCode);
    List<GameSession> findByJoinCodeAndStatus(String joinCode, GameStatus status);
    List<GameSession> findByStatus(GameStatus status);

    public record ProgressPartyDTO(String id) {}

    public record ProgressGameDTO(
            String scenarioKey,
            GameStatus status,
            List<String> playerPartyIds,
            ProgressPartyDTO governmentParty
    ) {}

    @Query(value = "{ $or: [ { 'userId': ?0 }, { $expr: { $in: [ ?0, { $map: { input: { $objectToArray: { $ifNull: [ '$humanPlayerMap', {} ] } }, in: '$$this.v' } } ] } } ] }",
           fields = "{ 'scenarioKey': 1, 'status': 1, 'playerPartyIds': 1, 'governmentParty.id': 1 }")
    List<ProgressGameDTO> findProgressGamesByUserId(String userId);

    public record GameSessionDTO(
            String id,
            String scenarioKey,
            String userId,
            GameStatus  status,
            PartyState governmentParty,
            List<String> playerPartyIds ,
            List<PartyState> parties,
            java.time.LocalDate currentDate, // or your date type
            Boolean active
    ) {
        public GameSessionDTO {
            if (active == null) {
                active = false; // Fallback default if missing in DB
            }
        }
    }

    /**
     * Fetch only the lightweight summary fields for a specific user.
     * Excludes heavy embedded arrays (gameCards, gameIssues, round submissions, etc.)
     * that cause full documents to be ~500KB each.
     */
    @Query(value = "{ $or: [ { 'userId': ?0 }, { $expr: { $in: [ ?0, { $map: { input: { $objectToArray: { $ifNull: [ '$humanPlayerMap', {} ] } }, in: '$$this.v' } } ] } } ] }",
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
