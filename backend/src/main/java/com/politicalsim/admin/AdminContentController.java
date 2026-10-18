package com.politicalsim.admin;

import com.politicalsim.content.CardDefinition;
import com.politicalsim.content.CardDefinitionRepository;
import com.politicalsim.content.NewsDefinition;
import com.politicalsim.content.NewsDefinitionRepository;
import com.politicalsim.content.ScenarioDefinition;
import com.politicalsim.content.ScenarioDefinitionRepository;
import com.politicalsim.content.LegislativeBillDefinition;
import com.politicalsim.content.LegislativeBillDefinitionRepository;
import java.util.List;
import java.util.Map;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.server.ResponseStatusException;
import com.politicalsim.content.DefinitionCache;
import com.politicalsim.content.NationalConfig;
import com.politicalsim.content.NationalConfigRepository;


@RestController
@RequestMapping("/api/admin")
public class AdminContentController {

    private final ScenarioDefinitionRepository scenarioRepository;
    private final CardDefinitionRepository cardRepository;
    private final NewsDefinitionRepository newsRepository;
    private final LegislativeBillDefinitionRepository billRepository;
    private final com.politicalsim.content.FactionDefinitionRepository factionRepository;
    private final NationalConfigRepository nationalConfigRepository;
    private final com.politicalsim.content.NationalEventRepository nationalEventRepository;
    private final com.politicalsim.content.NationalThemeRepository nationalThemeRepository;
    private final com.politicalsim.content.StateInfrastructureDefinitionRepository infrastructureRepository;

    public AdminContentController(
            ScenarioDefinitionRepository scenarioRepository,
            CardDefinitionRepository cardRepository,
            NewsDefinitionRepository newsRepository,
            LegislativeBillDefinitionRepository billRepository,
            com.politicalsim.content.FactionDefinitionRepository factionRepository,
            NationalConfigRepository nationalConfigRepository,
            com.politicalsim.content.NationalEventRepository nationalEventRepository,
            com.politicalsim.content.NationalThemeRepository nationalThemeRepository,
            com.politicalsim.content.StateInfrastructureDefinitionRepository infrastructureRepository
    ) {
        this.scenarioRepository = scenarioRepository;
        this.cardRepository = cardRepository;
        this.newsRepository = newsRepository;
        this.billRepository = billRepository;
        this.factionRepository = factionRepository;
        this.nationalConfigRepository = nationalConfigRepository;
        this.nationalEventRepository = nationalEventRepository;
        this.nationalThemeRepository = nationalThemeRepository;
        this.infrastructureRepository = infrastructureRepository;
    }

    @GetMapping("/scenarios")
    public List<ScenarioDefinition> listScenarios() {
        return scenarioRepository.findAll();
    }

    @GetMapping("/scenarios/{id}")
    public ScenarioDefinition getScenario(@PathVariable String id) {
        return scenarioRepository.findById(id)
                .orElseThrow(() -> notFound("Scenario not found: " + id));
    }

    @PostMapping("/scenarios")
    @ResponseStatus(HttpStatus.CREATED)
    public ScenarioDefinition createScenario(@RequestBody ScenarioDefinition scenario) {
        DefinitionCache.clearAll();
        scenario.setId(null);
        return scenarioRepository.save(scenario);
    }

    @PutMapping("/scenarios/{id}")
    public ScenarioDefinition updateScenario(@PathVariable String id, @RequestBody ScenarioDefinition scenario) {
        requireScenario(id);
        DefinitionCache.clearAll();
        scenario.setId(id);
        return scenarioRepository.save(scenario);
    }

    @DeleteMapping("/scenarios/{id}")
    public Map<String, String> deleteScenario(@PathVariable String id) {
        requireScenario(id);
        DefinitionCache.clearAll();
        scenarioRepository.deleteById(id);
        return Map.of("status", "deleted", "id", id);
    }

    @GetMapping("/cards")
    public List<CardDefinition> listCards(@RequestParam(required = false) String scenarioKey) {
        if (scenarioKey == null || scenarioKey.isBlank()) {
            return cardRepository.findAll();
        }
        return cardRepository.findByScenarioKeyOrderByCategoryAscNameAsc(scenarioKey);
    }

    @GetMapping("/cards/{id}")
    public CardDefinition getCard(@PathVariable String id) {
        return cardRepository.findById(id)
                .orElseThrow(() -> notFound("Card not found: " + id));
    }

    @PostMapping("/cards")
    @ResponseStatus(HttpStatus.CREATED)
    public CardDefinition createCard(@RequestBody CardDefinition card) {
        DefinitionCache.clearAll();
        card.setId(null);
        return cardRepository.save(card);
    }

    @PutMapping("/cards/{id}")
    public CardDefinition updateCard(@PathVariable String id, @RequestBody CardDefinition card) {
        requireCard(id);
        DefinitionCache.clearAll();
        card.setId(id);
        return cardRepository.save(card);
    }

    @DeleteMapping("/cards/{id}")
    public Map<String, String> deleteCard(@PathVariable String id) {
        requireCard(id);
        DefinitionCache.clearAll();
        cardRepository.deleteById(id);
        return Map.of("status", "deleted", "id", id);
    }

    @GetMapping("/news")
    public List<NewsDefinition> listNews(@RequestParam(required = false) String scenarioKey) {
        if (scenarioKey == null || scenarioKey.isBlank()) {
            return newsRepository.findAll();
        }
        return newsRepository.findByScenarioKeyOrderByTypeAscTitleAsc(scenarioKey);
    }

    @GetMapping("/news/{id}")
    public NewsDefinition getNews(@PathVariable String id) {
        return newsRepository.findById(id)
                .orElseThrow(() -> notFound("News item not found: " + id));
    }

    @PostMapping("/news")
    @ResponseStatus(HttpStatus.CREATED)
    public NewsDefinition createNews(@RequestBody NewsDefinition news) {
        DefinitionCache.clearAll();
        news.setId(null);
        return newsRepository.save(news);
    }

    @PutMapping("/news/{id}")
    public NewsDefinition updateNews(@PathVariable String id, @RequestBody NewsDefinition news) {
        requireNews(id);
        DefinitionCache.clearAll();
        news.setId(id);
        return newsRepository.save(news);
    }

    @DeleteMapping("/news/{id}")
    public Map<String, String> deleteNews(@PathVariable String id) {
        requireNews(id);
        DefinitionCache.clearAll();
        newsRepository.deleteById(id);
        return Map.of("status", "deleted", "id", id);
    }

    // --- LEGISLATIVE BILLS ENDPOINTS ---
    @GetMapping("/bills")
    public List<LegislativeBillDefinition> listBills(@RequestParam(required = false) String scenarioKey) {
        if (scenarioKey == null || scenarioKey.isBlank()) {
            return billRepository.findAll();
        }
        return billRepository.findByScenarioKey(scenarioKey);
    }

    @GetMapping("/bills/{id}")
    public LegislativeBillDefinition getBill(@PathVariable String id) {
        return billRepository.findById(id)
                .orElseThrow(() -> notFound("Bill not found: " + id));
    }

    @PostMapping("/bills")
    @ResponseStatus(HttpStatus.CREATED)
    public LegislativeBillDefinition createBill(@RequestBody LegislativeBillDefinition bill) {
        DefinitionCache.clearAll();
        bill.setId(null);
        return billRepository.save(bill);
    }

    @PutMapping("/bills/{id}")
    public LegislativeBillDefinition updateBill(@PathVariable String id, @RequestBody LegislativeBillDefinition bill) {
        requireBill(id);
        DefinitionCache.clearAll();
        bill.setId(id);
        return billRepository.save(bill);
    }

    @DeleteMapping("/bills/{id}")
    public Map<String, String> deleteBill(@PathVariable String id) {
        requireBill(id);
        DefinitionCache.clearAll();
        billRepository.deleteById(id);
        return Map.of("status", "deleted", "id", id);
    }

    @GetMapping("/factions")
    public List<com.politicalsim.content.FactionDefinition> listFactions() {
        return factionRepository.findAll();
    }

    @GetMapping("/factions/{id}")
    public com.politicalsim.content.FactionDefinition getFaction(@PathVariable String id) {
        return factionRepository.findById(id)
                .orElseThrow(() -> notFound("Faction not found: " + id));
    }

    @PostMapping("/factions")
    public com.politicalsim.content.FactionDefinition createFaction(@RequestBody com.politicalsim.content.FactionDefinition faction) {
        DefinitionCache.clearAll();
        return factionRepository.save(faction);
    }

    @PutMapping("/factions/{id}")
    public com.politicalsim.content.FactionDefinition updateFaction(@PathVariable String id, @RequestBody com.politicalsim.content.FactionDefinition faction) {
        requireFaction(id);
        faction.setId(id);
        DefinitionCache.clearAll();
        return factionRepository.save(faction);
    }

    @DeleteMapping("/factions/{id}")
    public Map<String, String> deleteFaction(@PathVariable String id) {
        requireFaction(id);
        DefinitionCache.clearAll();
        factionRepository.deleteById(id);
        return Map.of("status", "deleted", "id", id);
    }

    // --- NATIONAL CONFIGS ENDPOINTS ---
    @GetMapping("/national-configs")
    public List<NationalConfig> listNationalConfigs() {
        return nationalConfigRepository.findAll();
    }

    @GetMapping("/national-configs/{id}")
    public NationalConfig getNationalConfig(@PathVariable String id) {
        return nationalConfigRepository.findById(id)
                .or(() -> {
                    try {
                        int era = Integer.parseInt(id);
                        return nationalConfigRepository.findByEra(era);
                    } catch (NumberFormatException e) {
                        return java.util.Optional.empty();
                    }
                })
                .orElseThrow(() -> notFound("National config not found: " + id));
    }

    @PostMapping("/national-configs")
    @ResponseStatus(HttpStatus.CREATED)
    public NationalConfig createNationalConfig(@RequestBody NationalConfig config) {
        DefinitionCache.clearAll();
        config.setId(null);
        return nationalConfigRepository.save(config);
    }

    @PutMapping("/national-configs/{id}")
    public NationalConfig updateNationalConfig(@PathVariable String id, @RequestBody NationalConfig config) {
        NationalConfig existing = nationalConfigRepository.findById(id)
                .or(() -> {
                    try {
                        int era = Integer.parseInt(id);
                        return nationalConfigRepository.findByEra(era);
                    } catch (NumberFormatException e) {
                        return java.util.Optional.empty();
                    }
                })
                .orElseThrow(() -> notFound("National config not found: " + id));

        config.setId(existing.getId());
        DefinitionCache.clearAll();
        return nationalConfigRepository.save(config);
    }

    @DeleteMapping("/national-configs/{id}")
    public Map<String, String> deleteNationalConfig(@PathVariable String id) {
        NationalConfig existing = getNationalConfig(id);
        DefinitionCache.clearAll();
        nationalConfigRepository.deleteById(existing.getId());
        return Map.of("status", "deleted", "id", id);
    }

    // ── NATIONAL EVENTS CRUD ──────────────────────────────────────────────
    @GetMapping("/national-events")
    public List<com.politicalsim.content.NationalEvent> listNationalEvents(@RequestParam(required = false) Integer era) {
        if (era != null) {
            return nationalEventRepository.findByEra(era);
        }
        return nationalEventRepository.findAll();
    }

    @GetMapping("/national-events/{id}")
    public com.politicalsim.content.NationalEvent getNationalEvent(@PathVariable String id) {
        return nationalEventRepository.findById(id)
                .orElseThrow(() -> notFound("NationalEvent not found: " + id));
    }

    @PostMapping("/national-events")
    @ResponseStatus(HttpStatus.CREATED)
    public com.politicalsim.content.NationalEvent createNationalEvent(@RequestBody com.politicalsim.content.NationalEvent event) {
        event.setId(null);
        return nationalEventRepository.save(event);
    }

    @PutMapping("/national-events/{id}")
    public com.politicalsim.content.NationalEvent updateNationalEvent(@PathVariable String id, @RequestBody com.politicalsim.content.NationalEvent event) {
        if (!nationalEventRepository.existsById(id)) {
            throw notFound("NationalEvent not found: " + id);
        }
        event.setId(id);
        return nationalEventRepository.save(event);
    }

    @DeleteMapping("/national-events/{id}")
    public Map<String, String> deleteNationalEvent(@PathVariable String id) {
        if (!nationalEventRepository.existsById(id)) {
            throw notFound("NationalEvent not found: " + id);
        }
        nationalEventRepository.deleteById(id);
        return Map.of("status", "deleted", "id", id);
    }

    // ── NATIONAL THEMES CRUD ──────────────────────────────────────────────
    @GetMapping("/national-themes")
    public List<com.politicalsim.content.NationalTheme> listNationalThemes(@RequestParam(required = false) Integer era) {
        if (era != null) {
            return nationalThemeRepository.findByActiveErasContaining(era);
        }
        return nationalThemeRepository.findAll();
    }

    @GetMapping("/national-themes/{id}")
    public com.politicalsim.content.NationalTheme getNationalTheme(@PathVariable String id) {
        return nationalThemeRepository.findById(id)
                .orElseThrow(() -> notFound("NationalTheme not found: " + id));
    }

    @PostMapping("/national-themes")
    @ResponseStatus(HttpStatus.CREATED)
    public com.politicalsim.content.NationalTheme createNationalTheme(@RequestBody com.politicalsim.content.NationalTheme theme) {
        theme.setId(null);
        return nationalThemeRepository.save(theme);
    }

    @PutMapping("/national-themes/{id}")
    public com.politicalsim.content.NationalTheme updateNationalTheme(@PathVariable String id, @RequestBody com.politicalsim.content.NationalTheme theme) {
        if (!nationalThemeRepository.existsById(id)) {
            throw notFound("NationalTheme not found: " + id);
        }
        theme.setId(id);
        return nationalThemeRepository.save(theme);
    }

    @DeleteMapping("/national-themes/{id}")
    public Map<String, String> deleteNationalTheme(@PathVariable String id) {
        if (!nationalThemeRepository.existsById(id)) {
            throw notFound("NationalTheme not found: " + id);
        }
        nationalThemeRepository.deleteById(id);
        return Map.of("status", "deleted", "id", id);
    }

    // ── STATE INFRASTRUCTURE CRUD ──────────────────────────────────────────
    @GetMapping("/infrastructure-definitions")
    public List<com.politicalsim.content.StateInfrastructureDefinition> listInfrastructureDefinitions() {
        return infrastructureRepository.findAll();
    }

    @GetMapping("/infrastructure-definitions/{id}")
    public com.politicalsim.content.StateInfrastructureDefinition getInfrastructureDefinition(@PathVariable String id) {
        return infrastructureRepository.findById(id)
                .orElseThrow(() -> notFound("Infrastructure definition not found: " + id));
    }

    @PostMapping("/infrastructure-definitions")
    @ResponseStatus(HttpStatus.CREATED)
    public com.politicalsim.content.StateInfrastructureDefinition createInfrastructureDefinition(@RequestBody com.politicalsim.content.StateInfrastructureDefinition def) {
        def.setId(null);
        return infrastructureRepository.save(def);
    }

    @PutMapping("/infrastructure-definitions/{id}")
    public com.politicalsim.content.StateInfrastructureDefinition updateInfrastructureDefinition(@PathVariable String id, @RequestBody com.politicalsim.content.StateInfrastructureDefinition def) {
        if (!infrastructureRepository.existsById(id)) {
            throw notFound("Infrastructure definition not found: " + id);
        }
        def.setId(id);
        return infrastructureRepository.save(def);
    }

    @DeleteMapping("/infrastructure-definitions/{id}")
    public Map<String, String> deleteInfrastructureDefinition(@PathVariable String id) {
        if (!infrastructureRepository.existsById(id)) {
            throw notFound("Infrastructure definition not found: " + id);
        }
        infrastructureRepository.deleteById(id);
        return Map.of("status", "deleted", "id", id);
    }

    private void requireFaction(String id) {
        if (!factionRepository.existsById(id)) {
            throw notFound("Faction not found: " + id);
        }
    }

    private void requireScenario(String id) {
        if (!scenarioRepository.existsById(id)) {
            throw notFound("Scenario not found: " + id);
        }
    }

    private void requireCard(String id) {
        if (!cardRepository.existsById(id)) {
            throw notFound("Card not found: " + id);
        }
    }

    private void requireNews(String id) {
        if (!newsRepository.existsById(id)) {
            throw notFound("News item not found: " + id);
        }
    }

    private void requireBill(String id) {
        if (!billRepository.existsById(id)) {
            throw notFound("Bill not found: " + id);
        }
    }

    private ResponseStatusException notFound(String message) {
        return new ResponseStatusException(HttpStatus.NOT_FOUND, message);
    }

    @PostMapping("/cache/reload")
    public Map<String, String> reloadCaches() {
        DefinitionCache.clearAll();
        return Map.of("status", "success", "message", "All static caches reloaded and cleared.");
    }
}
