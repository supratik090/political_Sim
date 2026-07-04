package com.politicalsim.game;

import com.politicalsim.content.CardDefinition;
import com.politicalsim.content.MonthlyIssueDefinition;
import java.util.List;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "game_session_contents")
public class GameSessionContent {
    @Id
    private String id;
    private List<CardDefinition> gameCards;
    private List<MonthlyIssueDefinition> gameIssues;

    public GameSessionContent() {}

    public GameSessionContent(String id, List<CardDefinition> gameCards, List<MonthlyIssueDefinition> gameIssues) {
        this.id = id;
        this.gameCards = gameCards;
        this.gameIssues = gameIssues;
    }

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public List<CardDefinition> getGameCards() { return gameCards; }
    public void setGameCards(List<CardDefinition> gameCards) { this.gameCards = gameCards; }

    public List<MonthlyIssueDefinition> getGameIssues() { return gameIssues; }
    public void setGameIssues(List<MonthlyIssueDefinition> gameIssues) { this.gameIssues = gameIssues; }
}
