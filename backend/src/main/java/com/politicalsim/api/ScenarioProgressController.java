package com.politicalsim.api;

import com.politicalsim.game.GameService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/scenarios")
public class ScenarioProgressController {

    private final GameService gameService;

    public ScenarioProgressController(GameService gameService) {
        this.gameService = gameService;
    }

    @GetMapping("/progress")
    public CampaignProgressResponse getProgress(@RequestParam(required = false) String userId) {
        return gameService.getCampaignProgress(userId);
    }
}
