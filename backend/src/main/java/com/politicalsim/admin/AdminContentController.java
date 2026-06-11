package com.politicalsim.admin;

import com.politicalsim.content.CardDefinition;
import com.politicalsim.content.CardDefinitionRepository;
import com.politicalsim.content.MonthlyIssueDefinition;
import com.politicalsim.content.MonthlyIssueDefinitionRepository;
import com.politicalsim.content.NewsDefinition;
import com.politicalsim.content.NewsDefinitionRepository;
import com.politicalsim.content.ScenarioDefinition;
import com.politicalsim.content.ScenarioDefinitionRepository;
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

@RestController
@RequestMapping("/api/admin")
public class AdminContentController {

    private final ScenarioDefinitionRepository scenarioRepository;
    private final CardDefinitionRepository cardRepository;
    private final NewsDefinitionRepository newsRepository;
    private final MonthlyIssueDefinitionRepository issueRepository;

    public AdminContentController(
            ScenarioDefinitionRepository scenarioRepository,
            CardDefinitionRepository cardRepository,
            NewsDefinitionRepository newsRepository,
            MonthlyIssueDefinitionRepository issueRepository
    ) {
        this.scenarioRepository = scenarioRepository;
        this.cardRepository = cardRepository;
        this.newsRepository = newsRepository;
        this.issueRepository = issueRepository;
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
        scenario.setId(null);
        return scenarioRepository.save(scenario);
    }

    @PutMapping("/scenarios/{id}")
    public ScenarioDefinition updateScenario(@PathVariable String id, @RequestBody ScenarioDefinition scenario) {
        requireScenario(id);
        scenario.setId(id);
        return scenarioRepository.save(scenario);
    }

    @DeleteMapping("/scenarios/{id}")
    public Map<String, String> deleteScenario(@PathVariable String id) {
        requireScenario(id);
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
        card.setId(null);
        return cardRepository.save(card);
    }

    @PutMapping("/cards/{id}")
    public CardDefinition updateCard(@PathVariable String id, @RequestBody CardDefinition card) {
        requireCard(id);
        card.setId(id);
        return cardRepository.save(card);
    }

    @DeleteMapping("/cards/{id}")
    public Map<String, String> deleteCard(@PathVariable String id) {
        requireCard(id);
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
        news.setId(null);
        return newsRepository.save(news);
    }

    @PutMapping("/news/{id}")
    public NewsDefinition updateNews(@PathVariable String id, @RequestBody NewsDefinition news) {
        requireNews(id);
        news.setId(id);
        return newsRepository.save(news);
    }

    @DeleteMapping("/news/{id}")
    public Map<String, String> deleteNews(@PathVariable String id) {
        requireNews(id);
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
        issue.setId(null);
        return issueRepository.save(issue);
    }

    @PutMapping("/issues/{id}")
    public MonthlyIssueDefinition updateIssue(@PathVariable String id, @RequestBody MonthlyIssueDefinition issue) {
        requireIssue(id);
        issue.setId(id);
        return issueRepository.save(issue);
    }

    @DeleteMapping("/issues/{id}")
    public Map<String, String> deleteIssue(@PathVariable String id) {
        requireIssue(id);
        issueRepository.deleteById(id);
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

    private ResponseStatusException notFound(String message) {
        return new ResponseStatusException(HttpStatus.NOT_FOUND, message);
    }
}
