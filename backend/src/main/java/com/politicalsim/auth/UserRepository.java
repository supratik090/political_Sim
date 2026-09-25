package com.politicalsim.auth;

import org.springframework.data.mongodb.repository.MongoRepository;
import java.util.Optional;

public interface UserRepository extends MongoRepository<User, String> {
    Optional<User> findByEmail(String email);
    Optional<User> findByNameIgnoreCase(String name);
    boolean existsByEmail(String email);
}
