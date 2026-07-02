package com.politicalsim.api.telemetry.repository;

import com.politicalsim.api.ChatMessage;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ChatMessageRepository extends MongoRepository<ChatMessage, String> {
    // Additional query methods can be added here if needed
}
