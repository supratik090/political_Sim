package com.politicalsim.admin;

import com.politicalsim.content.CardDefinition;
import com.politicalsim.content.CardDefinitionRepository;
import com.politicalsim.content.MonthlyIssueDefinition;
import com.politicalsim.content.MonthlyIssueDefinitionRepository;
import com.politicalsim.content.NewsDefinition;
import com.politicalsim.content.NewsDefinitionRepository;
import com.politicalsim.content.ScenarioDefinition;
import com.politicalsim.content.ScenarioDefinitionRepository;
import com.politicalsim.content.LegislativeBillDefinition;
import com.politicalsim.content.LegislativeBillDefinitionRepository;
import com.politicalsim.content.EventCardDefinition;
import com.politicalsim.content.EventCardDefinitionRepository;
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


@RestController
@RequestMapping("/api/admin")
public class AdminContentController {

    private final ScenarioDefinitionRepository scenarioRepository;
    private final CardDefinitionRepository cardRepository;
    private final NewsDefinitionRepository newsRepository;
    private final MonthlyIssueDefinitionRepository issueRepository;
    private final LegislativeBillDefinitionRepository billRepository;
    private final EventCardDefinitionRepository eventRepository;

    public AdminContentController(
            ScenarioDefinitionRepository scenarioRepository,
            CardDefinitionRepository cardRepository,
            NewsDefinitionRepository newsRepository,
            MonthlyIssueDefinitionRepository issueRepository,
            LegislativeBillDefinitionRepository billRepository,
            EventCardDefinitionRepository eventRepository
    ) {
        this.scenarioRepository = scenarioRepository;
        this.cardRepository = cardRepository;
        this.newsRepository = newsRepository;
        this.issueRepository = issueRepository;
        this.billRepository = billRepository;
        this.eventRepository = eventRepository;
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

    @GetMapping("/issues")
    public List<MonthlyIssueDefinition> listIssues(@RequestParam(required = false) String scenarioKey) {
        if (scenarioKey == null || scenarioKey.isBlank()) {
            return issueRepository.findAll();
        }
        return issueRepository.findByScenarioKeyOrderByCategoryAscTitleAsc(scenarioKey);
    }

    @GetMapping("/issues/{id}")
    public MonthlyIssueDefinition getIssue(@PathVariable String id) {
        return issueRepository.findById(id)
                .orElseThrow(() -> notFound("Issue item not found: " + id));
    }

    @PostMapping("/issues")
    @ResponseStatus(HttpStatus.CREATED)
    public MonthlyIssueDefinition createIssue(@RequestBody MonthlyIssueDefinition issue) {
        DefinitionCache.clearAll();
        issue.setId(null);
        return issueRepository.save(issue);
    }

    @PutMapping("/issues/{id}")
    public MonthlyIssueDefinition updateIssue(@PathVariable String id, @RequestBody MonthlyIssueDefinition issue) {
        requireIssue(id);
        DefinitionCache.clearAll();
        issue.setId(id);
        return issueRepository.save(issue);
    }

    @DeleteMapping("/issues/{id}")
    public Map<String, String> deleteIssue(@PathVariable String id) {
        requireIssue(id);
        DefinitionCache.clearAll();
        issueRepository.deleteById(id);
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

    // --- EVENT CARDS ENDPOINTS ---
    @GetMapping("/events")
    public List<EventCardDefinition> listEvents(@RequestParam(required = false) String scenarioKey) {
        if (scenarioKey == null || scenarioKey.isBlank()) {
            return eventRepository.findAll();
        }
        return eventRepository.findByScenarioKey(scenarioKey);
    }

    @GetMapping("/events/{id}")
    public EventCardDefinition getEvent(@PathVariable String id) {
        return eventRepository.findById(id)
                .orElseThrow(() -> notFound("Event card not found: " + id));
    }

    @PostMapping("/events")
    @ResponseStatus(HttpStatus.CREATED)
    public EventCardDefinition createEvent(@RequestBody EventCardDefinition event) {
        DefinitionCache.clearAll();
        event.setId(null);
        return eventRepository.save(event);
    }

    @PutMapping("/events/{id}")
    public EventCardDefinition updateEvent(@PathVariable String id, @RequestBody EventCardDefinition event) {
        requireEvent(id);
        DefinitionCache.clearAll();
        event.setId(id);
        return eventRepository.save(event);
    }

    @DeleteMapping("/events/{id}")
    public Map<String, String> deleteEvent(@PathVariable String id) {
        requireEvent(id);
        DefinitionCache.clearAll();
        eventRepository.deleteById(id);
        return Map.of("status", "deleted", "id", id);
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

    private void requireIssue(String id) {
        if (!issueRepository.existsById(id)) {
            throw notFound("Issue item not found: " + id);
        }
    }

    private void requireBill(String id) {
        if (!billRepository.existsById(id)) {
            throw notFound("Bill not found: " + id);
        }
    }

    private void requireEvent(String id) {
        if (!eventRepository.existsById(id)) {
            throw notFound("Event card not found: " + id);
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
