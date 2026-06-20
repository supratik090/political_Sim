package com.politicalsim.content;

import com.politicalsim.party.ControllerType;
import com.politicalsim.party.Ideology;
import com.politicalsim.party.PartyRole;
import com.politicalsim.party.PartyStats;
import com.politicalsim.publicmood.PublicState;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class ScenarioSeeder implements CommandLineRunner {

    private final ScenarioDefinitionRepository scenarioRepository;

    public ScenarioSeeder(ScenarioDefinitionRepository scenarioRepository) {
        this.scenarioRepository = scenarioRepository;
    }

    @Override
    public void run(String... args) throws Exception {
        // 2001 Era Scenarios
        seedScenario("west_bengal_2000", "West Bengal 2000", "West Bengal",
                "Fictionalized Indian state scenario inspired by long incumbency, organized cadre politics, rural unrest, and a rising opposition mood.",
                260, 56, 60, 48, 42,
                145, 52, 20, 44, 30,
                120, 52, 16, 42, 10,
                18, 2001);

        seedScenario("maharashtra_2001", "Maharashtra 2001", "Maharashtra",
                "Western coalition politics, urban-rural divides, and co-operative sugar lobby rivalries.",
                250, 70, 40, 50, 44,
                150, 55, 25, 45, 32,
                110, 50, 20, 40, 14,
                10, 2001);

        seedScenario("uttar_pradesh_2001", "Uttar Pradesh 2001", "Uttar Pradesh",
                "Gangetic plains heartland campaign, identity alliances, and grassroots mobilizations.",
                240, 65, 45, 48, 40,
                160, 60, 28, 42, 30,
                130, 55, 18, 45, 20,
                10, 2001);

        seedScenario("tamil_nadu_2001", "Tamil Nadu 2001", "Tamil Nadu",
                "Dravidian self-respect movements, welfare populism premiums, and cinematic campaigns.",
                270, 78, 35, 62, 48,
                140, 50, 22, 40, 28,
                100, 48, 15, 38, 14,
                10, 2001);

        seedScenario("rajasthan_2001", "Rajasthan 2001", "Rajasthan",
                "Desert borderlands contest, alternating power cycles, and royalty narratives.",
                230, 62, 42, 46, 38,
                155, 58, 24, 44, 34,
                115, 50, 14, 40, 18,
                10, 2001);

        // 2006 Era Scenarios
        seedScenario("west_bengal_2006", "West Bengal 2006", "West Bengal",
                "Bengal campaign during a period of massive industrialization debates and intense agricultural activism.",
                250, 60, 50, 55, 45,
                150, 55, 20, 48, 32,
                110, 50, 15, 40, 13,
                10, 2006);

        seedScenario("maharashtra_2006", "Maharashtra 2006", "Maharashtra",
                "Maharashtra politics defined by complex multi-polar coalitions, urban infrastructure push, and rural distress.",
                240, 68, 42, 52, 42,
                160, 58, 26, 44, 34,
                120, 52, 18, 42, 14,
                10, 2006);

        seedScenario("uttar_pradesh_2006", "Uttar Pradesh 2006", "Uttar Pradesh",
                "UP elections with shifting caste alliances, law and order debates, and infrastructure promises.",
                230, 62, 48, 46, 38,
                170, 62, 30, 45, 34,
                140, 55, 20, 40, 18,
                10, 2006);

        seedScenario("tamil_nadu_2006", "Tamil Nadu 2006", "Tamil Nadu",
                "Tamil Nadu campaign with aggressive freebie schemes, regional pride assertions, and intense bipolar rivalry.",
                260, 80, 38, 64, 46,
                150, 55, 24, 42, 32,
                110, 46, 12, 36, 12,
                10, 2006);

        seedScenario("rajasthan_2006", "Rajasthan 2006", "Rajasthan",
                "Rajasthan's traditional bi-annual power shift contest with development promises vs. anti-incumbency.",
                220, 60, 45, 48, 36,
                165, 60, 22, 46, 36,
                120, 48, 16, 38, 18,
                10, 2006);
    }

    private void seedScenario(String key, String name, String stateName, String description,
            int govCoins, int govMorale, int govCorruption, int govMedia, int govSupport,
            int oppCoins, int oppMorale, int oppCorruption, int oppMedia, int oppSupport,
            int thirdCoins, int thirdMorale, int thirdCorruption, int thirdMedia, int thirdSupport,
            int undecided, int startYear) {

        List<ScenarioDefinition> existing = scenarioRepository.findByScenarioKey(key);
        if (!existing.isEmpty()) {
            if (existing.size() > 1) {
                // Clean up duplicates if any exist in the database
                for (int i = 1; i < existing.size(); i++) {
                    scenarioRepository.delete(existing.get(i));
                }
            }
            return;
        }

        ScenarioDefinition scenario = new ScenarioDefinition();
        scenario.setScenarioKey(key);
        scenario.setName(name);
        scenario.setDescription(description);
        scenario.setStateName(stateName);
        scenario.setStartDate(LocalDate.of(startYear, 1, 1));
        scenario.setCycleLengthMonths(60);
        scenario.setGovernmentPartyName("Tiger Front");
        scenario.setOppositionPartyName("Elephant Congress");
        scenario.setThirdPartyName("Peacock Party");
        scenario.setGovernmentStartingStats(new PartyStats(govCoins, govMorale, govCorruption, govMedia, govSupport));
        scenario.setOppositionStartingStats(new PartyStats(oppCoins, oppMorale, oppCorruption, oppMedia, oppSupport));
        scenario.setThirdPartyStartingStats(new PartyStats(thirdCoins, thirdMorale, thirdCorruption, thirdMedia, thirdSupport));

        List<ScenarioPartyDefinition> parties = new ArrayList<>();
        
        ScenarioPartyDefinition gov = new ScenarioPartyDefinition();
        gov.setPartyKey("tiger_front");
        gov.setName("Tiger Front");
        gov.setStartingRole(PartyRole.GOVERNMENT);
        gov.setDefaultControllerType(ControllerType.COMPUTER);
        gov.setIdeology(Ideology.DEVELOPMENT_FIRST);
        gov.setStartingStats(new PartyStats(govCoins, govMorale, govCorruption, govMedia, govSupport));
        gov.setColor("#E15554");
        gov.setSymbol("Tiger");
        parties.add(gov);

        ScenarioPartyDefinition opp = new ScenarioPartyDefinition();
        opp.setPartyKey("elephant_congress");
        opp.setName("Elephant Congress");
        opp.setStartingRole(PartyRole.OPPOSITION);
        opp.setDefaultControllerType(ControllerType.HUMAN);
        opp.setIdeology(Ideology.ANTI_CORRUPTION);
        opp.setStartingStats(new PartyStats(oppCoins, oppMorale, oppCorruption, oppMedia, oppSupport));
        opp.setColor("#3F88C5");
        opp.setSymbol("Elephant");
        parties.add(opp);

        ScenarioPartyDefinition third = new ScenarioPartyDefinition();
        third.setPartyKey("peacock_party");
        third.setName("Peacock Party");
        third.setStartingRole(PartyRole.THIRD_PARTY);
        third.setDefaultControllerType(ControllerType.COMPUTER);
        third.setIdeology(Ideology.REGIONAL_PRIDE);
        third.setStartingStats(new PartyStats(thirdCoins, thirdMorale, thirdCorruption, thirdMedia, thirdSupport));
        third.setColor("#17B890");
        third.setSymbol("Peacock");
        parties.add(third);

        scenario.setPoliticalParties(parties);

        PublicState publicState = new PublicState();
        publicState.setUndecidedSupport(undecided);
        publicState.setMood("Watchful");
        publicState.setMainIssues(List.of("Jobs", "Rural distress", "Cadre dominance"));
        publicState.setMemoryHint("Voters remember long incumbency, but the opposition still needs credibility.");
        scenario.setPublicState(publicState);

        Map<String, Object> ruleWeights = new LinkedHashMap<>();
        ruleWeights.put("antiIncumbencyGrowthPerTurn", 1.0);
        ruleWeights.put("scandalFatigueLimit", 5.0);
        ruleWeights.put("noConfidenceSupportThreshold", 35.0);
        ruleWeights.put("noConfidenceMoraleThreshold", 35.0);
        ruleWeights.put("electionCoinReductionPercent", 70.0);
        ruleWeights.put("publicMemoryDecayPerTurn", 0.4);
        scenario.setRuleWeights(ruleWeights);
        scenario.setActive(true);

        scenarioRepository.save(scenario);
    }
}
