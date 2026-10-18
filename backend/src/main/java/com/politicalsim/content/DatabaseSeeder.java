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
    private final ScenarioDefinitionRepository scenarioRepository;
    private final LegislativeBillDefinitionRepository billRepository;
    private final FactionDefinitionRepository factionRepository;
    private final NationalConfigRepository nationalConfigRepository;
    private final NationalEventRepository nationalEventRepository;
    private final NationalThemeRepository nationalThemeRepository;
    private final StateInfrastructureDefinitionRepository infrastructureRepository;

    public DatabaseSeeder(CardDefinitionRepository cardRepository,
                          NewsDefinitionRepository newsRepository,
                          ScenarioDefinitionRepository scenarioRepository,
                          LegislativeBillDefinitionRepository billRepository,
                          FactionDefinitionRepository factionRepository,
                          NationalConfigRepository nationalConfigRepository,
                          NationalEventRepository nationalEventRepository,
                          NationalThemeRepository nationalThemeRepository,
                          StateInfrastructureDefinitionRepository infrastructureRepository) {
        this.cardRepository = cardRepository;
        this.newsRepository = newsRepository;
        this.scenarioRepository = scenarioRepository;
        this.billRepository = billRepository;
        this.factionRepository = factionRepository;
        this.nationalConfigRepository = nationalConfigRepository;
        this.nationalEventRepository = nationalEventRepository;
        this.nationalThemeRepository = nationalThemeRepository;
        this.infrastructureRepository = infrastructureRepository;
    }

    @Override
    public void run(String... args) throws Exception {
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
                performSeeding();
            } catch (Exception e) {
                log.error("Error during background database seeding", e);
            }
        });
    }

    private void performSeeding() throws Exception {
        log.info("Checking database seed files for initial loading in background...");

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

        // 4. Seed Legislative Bills
        if (billRepository.count() == 0) {
            File billsFile = new File(seedDir, "bills.json");
            if (billsFile.exists()) {
                log.info("Seeding Legislative Bills from bills.json...");
                List<LegislativeBillDefinition> bills = mapper.readValue(billsFile, new TypeReference<List<LegislativeBillDefinition>>() {});
                billRepository.saveAll(bills);
                log.info("Successfully seeded {} legislative bills.", bills.size());
            } else {
                log.warn("bills.json not found in seed directory.");
            }
        } else {
            log.info("Legislative Bills already seeded (count: {}). Skipping.", billRepository.count());
        }

        // 5. Seed Factions
        if (factionRepository.count() == 0) {
            File factionsFile = new File(seedDir, "factions.json");
            if (factionsFile.exists()) {
                log.info("Seeding Factions from factions.json...");
                List<FactionDefinition> factions = mapper.readValue(factionsFile, new TypeReference<List<FactionDefinition>>() {});
                factionRepository.saveAll(factions);
                log.info("Successfully seeded {} factions.", factions.size());
            } else {
                log.warn("factions.json not found in seed directory.");
            }
        } else {
            log.info("Factions already seeded (count: {}). Skipping.", factionRepository.count());
        }

        // 6. Seed / Sync National Configs
        File nationalDir = new File("../seed-data/national/national_configs");
        if (nationalDir.exists() && nationalDir.isDirectory()) {
            File[] configFiles = nationalDir.listFiles((dir, name) -> name.endsWith(".json"));
            if (configFiles != null) {
                for (File cfgFile : configFiles) {
                    try {
                        log.info("Syncing NationalConfig from {}...", cfgFile.getName());
                        NationalConfig cfg = mapper.readValue(cfgFile, NationalConfig.class);
                        var existing = nationalConfigRepository.findByEra(cfg.getEra());
                        if (existing.isPresent()) {
                            cfg.setId(existing.get().getId());
                        }
                        nationalConfigRepository.save(cfg);
                        log.info("Successfully synced NationalConfig for era {}.", cfg.getEra());
                    } catch (Exception ex) {
                        log.error("Failed to seed/sync NationalConfig from " + cfgFile.getName(), ex);
                    }
                }
            }
        } else {
            log.warn("National configs seed directory not found at '../seed-data/national/national_configs'.");
        }

        // 7. Seed / Sync National Events
        File eventsDir = new File("../seed-data/national/national_events");
        if (eventsDir.exists() && eventsDir.isDirectory()) {
            File[] eventFiles = eventsDir.listFiles((dir, name) -> name.endsWith(".json"));
            if (eventFiles != null) {
                for (File evtFile : eventFiles) {
                    try {
                        log.info("Syncing NationalEvents from {}...", evtFile.getName());
                        List<NationalEvent> evts = mapper.readValue(evtFile, new TypeReference<List<NationalEvent>>() {});
                        for (NationalEvent e : evts) {
                            nationalEventRepository.save(e);
                        }
                        log.info("Successfully synced {} NationalEvents from {}.", evts.size(), evtFile.getName());
                    } catch (Exception ex) {
                        log.error("Failed to seed NationalEvents from " + evtFile.getName(), ex);
                    }
                }
            }
        }

        // 8. Seed / Sync National Themes
        File themesDir = new File("../seed-data/national/national_themes");
        if (themesDir.exists() && themesDir.isDirectory()) {
            File[] themeFiles = themesDir.listFiles((dir, name) -> name.endsWith(".json"));
            if (themeFiles != null) {
                for (File thmFile : themeFiles) {
                    try {
                        log.info("Syncing NationalThemes from {}...", thmFile.getName());
                        List<NationalTheme> thms = mapper.readValue(thmFile, new TypeReference<List<NationalTheme>>() {});
                        for (NationalTheme t : thms) {
                            nationalThemeRepository.save(t);
                        }
                        log.info("Successfully synced {} NationalThemes from {}.", thms.size(), thmFile.getName());
                    } catch (Exception ex) {
                        log.error("Failed to seed NationalThemes from " + thmFile.getName(), ex);
                    }
                }
            }
        }

        // 9. Seed / Sync State Infrastructure Definitions
        File infraFile = new File("../seed-data/national/state_infrastructure.json");
        if (infraFile.exists()) {
            try {
                log.info("Syncing StateInfrastructureDefinitions from {}...", infraFile.getName());
                List<StateInfrastructureDefinition> items = mapper.readValue(infraFile, new TypeReference<List<StateInfrastructureDefinition>>() {});
                for (StateInfrastructureDefinition item : items) {
                    infrastructureRepository.findByKey(item.getKey())
                        .ifPresent(existing -> item.setId(existing.getId()));
                    infrastructureRepository.save(item);
                }
                log.info("Successfully synced {} StateInfrastructureDefinitions.", items.size());
            } catch (Exception ex) {
                log.error("Failed to seed StateInfrastructureDefinitions from " + infraFile.getName(), ex);
            }
        }

        log.info("Database seeding check complete.");
    }
}

