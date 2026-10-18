package com.politicalsim.content;

import java.util.List;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface NationalEventRepository extends MongoRepository<NationalEvent, String> {
    List<NationalEvent> findByEraAndSeason(int era, int season);
    List<NationalEvent> findByEra(int era);
}
