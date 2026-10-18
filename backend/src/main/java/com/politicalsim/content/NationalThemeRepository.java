package com.politicalsim.content;

import java.util.List;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface NationalThemeRepository extends MongoRepository<NationalTheme, String> {
    List<NationalTheme> findByActiveErasContaining(int era);
}
