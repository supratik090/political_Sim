package com.politicalsim.party;

import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;
import java.util.Optional;

public interface PartyManagementRepository extends MongoRepository<PartyManagementState, String> {

    Optional<PartyManagementState> findByGameIdAndPartyId(String gameId, String partyId);

    List<PartyManagementState> findByGameId(String gameId);

    void deleteByGameId(String gameId);
}
