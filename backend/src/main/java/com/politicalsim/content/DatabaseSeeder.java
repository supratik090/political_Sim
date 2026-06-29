package com.politicalsim.content;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

import java.io.File;
import java.util.List;

@Component
@Order(1)
public class DatabaseSeeder implements CommandLineRunner {

    private static final Logger log = LoggerFactory.getLogger(DatabaseSeeder.class);

    private final CardDefinitionRepository cardRepository;
    private final NewsDefinitionRepository newsRepository;
    private final MonthlyIssueDefinitionRepository issueRepository;
    private final ScenarioDefinitionRepository scenarioRepository;

    public DatabaseSeeder(CardDefinitionRepository cardRepository,
                          NewsDefinitionRepository newsRepository,
                          MonthlyIssueDefinitionRepository issueRepository,
                          ScenarioDefinitionRepository scenarioRepository) {
        this.cardRepository = cardRepository;
        this.newsRepository = newsRepository;
        this.issueRepository = issueRepository;
        this.scenarioRepository = scenarioRepository;
    }

    @Override
    public void run(String... args) throws Exception {
        log.info("Checking database seed files for initial loading...");

        File seedDir = new File("../seed-data/startup");
        if (!seedDir.exists()) {
            log.warn("Seed directory not found at '../seed-data/startup'. Skipping seed data initialization.");
            return;
        }

        ObjectMapper mapper = new ObjectMapper();
        mapper.registerModule(new JavaTimeModule());

        // 1. Seed Scenarios
        if (scenarioRepository.count() == 0) {
            File scenariosFile = new File(seedDir, "scenarios.json");
            if (scenariosFile.exists()) {
                log.info("Seeding Scenarios from scenarios.json...");
                List<ScenarioDefinition> scenarios = mapper.readValue(scenariosFile, new TypeReference<List<ScenarioDefinition>>() {});
                scenarioRepository.saveAll(scenarios);
                log.info("Successfully seeded {} scenarios.", scenarios.size());
            } else {
                log.warn("scenarios.json not found in seed directory.");
            }
        } else {
            log.info("Scenarios already seeded (count: {}). Skipping.", scenarioRepository.count());
        }

        // 2. Seed Cards
        if (cardRepository.count() == 0) {
            File cardsFile = new File(seedDir, "cards.json");
            if (cardsFile.exists()) {
                log.info("Seeding Cards from cards.json...");
                List<CardDefinition> cards = mapper.readValue(cardsFile, new TypeReference<List<CardDefinition>>() {});
                cardRepository.saveAll(cards);
                log.info("Successfully seeded {} cards.", cards.size());
            } else {
                log.warn("cards.json not found in seed directory.");
            }
        } else {
            log.info("Cards already seeded (count: {}). Skipping.", cardRepository.count());
        }

        // 3. Seed News
        if (newsRepository.count() == 0) {
            File newsFile = new File(seedDir, "news.json");
            if (newsFile.exists()) {
                log.info("Seeding News from news.json...");
                List<NewsDefinition> news = mapper.readValue(newsFile, new TypeReference<List<NewsDefinition>>() {});
                newsRepository.saveAll(news);
                log.info("Successfully seeded {} news.", news.size());
            } else {
                log.warn("news.json not found in seed directory.");
            }
        } else {
            log.info("News already seeded (count: {}). Skipping.", newsRepository.count());
        }

        // 4. Seed Monthly Issues
        if (issueRepository.count() == 0) {
            File issuesFile = new File(seedDir, "issues.json");
            if (issuesFile.exists()) {
                log.info("Seeding Monthly Issues from issues.json...");
                List<MonthlyIssueDefinition> issues = mapper.readValue(issuesFile, new TypeReference<List<MonthlyIssueDefinition>>() {});
                issueRepository.saveAll(issues);
                log.info("Successfully seeded {} monthly issues.", issues.size());
            } else {
                log.warn("issues.json not found in seed directory.");
            }
        } else {
            log.info("Monthly Issues already seeded (count: {}). Skipping.", issueRepository.count());
        }

        log.info("Database seeding check complete.");
    }
}
