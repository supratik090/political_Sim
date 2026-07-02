package com.politicalsim.api.telemetry;

import com.politicalsim.api.ChatMessage;
import com.politicalsim.api.telemetry.repository.ChatMessageRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ChatTelemetryService {

    private final ChatMessageRepository chatMessageRepository;

    @Autowired
    public ChatTelemetryService(ChatMessageRepository chatMessageRepository) {
        this.chatMessageRepository = chatMessageRepository;
    }

    public void saveMessage(String gameId, ChatMessage message) {
        // Attach gameId to message via a field if needed, otherwise just store raw message
        // For simplicity we store the message as-is; you can extend ChatMessage with a gameId field later.
        chatMessageRepository.save(message);
    }

    public long countMessages() {
        return chatMessageRepository.count();
    }

    public long countMessagesLastHours(int hours) {
        // Assuming timestamp is stored as ISO string, we query by date.
        // This simple implementation uses MongoTemplate; for now we fallback to count all.
        return chatMessageRepository.count(); // Placeholder – detailed time query can be added later.
    }
}
