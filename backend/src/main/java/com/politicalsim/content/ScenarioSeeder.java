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
        // Bihar
        seedScenarioWithParties("bihar_2001", "Bihar 2001", "Bihar",
                "Heartland governance battle amid crime-governance trade-offs, caste arithmetic, and rural development gaps.",
                "RJD", "rjd", "NDA (BJP+JD-U)", "nda_bjpu",
                400, 52, 72, 30, 30,
                400, 58, 38, 48, 36,
                400, 80, 10, 65, 10,
                24, 2001);

        seedScenarioWithParties("bihar_2006", "Bihar 2006", "Bihar",
                "Nitish Kumar's good governance wave confronts Lalu's entrenched social base post-2005 mandate.",
                "JD-U", "jdu", "RJD", "rjd",
                400, 72, 25, 62, 36,
                400, 38, 68, 28, 28,
                400, 80, 10, 65, 10,
                26, 2006);

        // Goa
        seedScenarioWithParties("goa_2001", "Goa 2001", "Goa",
                "India's smallest state battleground — tourism economy, mining royalty politics, and coastal development debates.",
                "INC", "inc", "BJP", "bjp",
                400, 58, 45, 50, 38,
                400, 50, 40, 45, 32,
                400, 80, 10, 65, 10,
                20, 2001);

        seedScenarioWithParties("goa_2006", "Goa 2006", "Goa",
                "Goa's revolving-door politics — coalition instability, mining boom controversies, and resort development tensions.",
                "INC", "inc", "BJP", "bjp",
                400, 55, 50, 48, 36,
                400, 52, 42, 46, 34,
                400, 80, 10, 65, 10,
                20, 2006);

        // Delhi
        seedScenarioWithParties("delhi_2001", "Delhi 2001", "Delhi",
                "National Capital Territory politics — urban infrastructure, power supply, and water politics under Sheila Dikshit.",
                "INC", "inc", "BJP", "bjp",
                400, 68, 35, 62, 48,
                400, 48, 38, 45, 34,
                400, 80, 10, 65, 10,
                8, 2001);

        seedScenarioWithParties("delhi_2006", "Delhi 2006", "Delhi",
                "Delhi mid-term politics — Commonwealth Games preparation, infrastructure boom, and early anti-incumbency signals.",
                "INC", "inc", "BJP", "bjp",
                400, 65, 40, 58, 46,
                400, 50, 35, 48, 34,
                400, 80, 10, 65, 10,
                10, 2006);

        // Andhra Pradesh
        seedScenarioWithParties("andhra_pradesh_2001", "Andhra Pradesh 2001", "Andhra Pradesh",
                "Telugu pride politics — irrigation battles, Chandrababu Naidu's tech-first governance, and Congress revival.",
                "TDP", "tdp", "INC", "inc",
                400, 65, 48, 55, 42,
                400, 48, 38, 45, 28,
                400, 80, 10, 65, 10,
                20, 2001);

        seedScenarioWithParties("andhra_pradesh_2006", "Andhra Pradesh 2006", "Andhra Pradesh",
                "YSR's welfare revolution confronts TDP's development legacy in Andhra's most consequential mid-decade contest.",
                "INC (YSR)", "inc_ysr", "TDP", "tdp",
                400, 72, 42, 58, 42,
                400, 48, 45, 42, 34,
                400, 80, 10, 65, 10,
                14, 2006);

        // Kerala
        seedScenarioWithParties("kerala_2001", "Kerala 2001", "Kerala",
                "God's Own Country elections — LDF vs UDF alternation, labor movement politics, and Gulf remittance economy.",
                "INC-UDF", "inc_udf", "LDF (CPI-M)", "cpi_m_ldf",
                400, 65, 38, 55, 44,
                400, 60, 42, 52, 42,
                400, 80, 10, 65, 10,
                4, 2001);

        seedScenarioWithParties("kerala_2006", "Kerala 2006", "Kerala",
                "VS Achuthanandan's corruption-fight mandate clashes with UDF's development narrative in Kerala's alternating democracy.",
                "LDF (CPI-M)", "cpi_m_ldf", "INC-UDF", "inc_udf",
                400, 72, 35, 58, 44,
                400, 55, 40, 52, 42,
                400, 80, 10, 65, 10,
                4, 2006);
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

    /**
     * Seeds a scenario with real historical party names and keys.
     * Used for new states (Bihar, Goa, Delhi, Andhra Pradesh, Kerala).
     * Stats order: coins, morale, corruptionScore, mediaImage, publicSupport.
     */
    private void seedScenarioWithParties(
            String key, String name, String stateName, String description,
            String govPartyName, String govPartyKey,
            String oppPartyName, String oppPartyKey,
            int govCoins, int govMorale, int govCorruption, int govMedia, int govSupport,
            int oppCoins, int oppMorale, int oppCorruption, int oppMedia, int oppSupport,
            int thirdCoins, int thirdMorale, int thirdCorruption, int thirdMedia, int thirdSupport,
            int undecided, int startYear) {

        List<ScenarioDefinition> existing = scenarioRepository.findByScenarioKey(key);
        if (!existing.isEmpty()) {
            if (existing.size() > 1) {
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
        scenario.setGovernmentPartyName(govPartyName);
        scenario.setOppositionPartyName(oppPartyName);
        scenario.setThirdPartyName("Youth Development Party (YDP)");
        scenario.setGovernmentStartingStats(new PartyStats(govCoins, govMorale, govCorruption, govMedia, govSupport));
        scenario.setOppositionStartingStats(new PartyStats(oppCoins, oppMorale, oppCorruption, oppMedia, oppSupport));
        scenario.setThirdPartyStartingStats(new PartyStats(thirdCoins, thirdMorale, thirdCorruption, thirdMedia, thirdSupport));

        List<ScenarioPartyDefinition> parties = new ArrayList<>();

        ScenarioPartyDefinition gov = new ScenarioPartyDefinition();
        gov.setPartyKey(govPartyKey);
        gov.setName(govPartyName);
        gov.setStartingRole(PartyRole.GOVERNMENT);
        gov.setDefaultControllerType(ControllerType.COMPUTER);
        gov.setIdeology(Ideology.DEVELOPMENT_FIRST);
        gov.setStartingStats(new PartyStats(govCoins, govMorale, govCorruption, govMedia, govSupport));
        gov.setColor("#E15554");
        gov.setSymbol("Flag");
        parties.add(gov);

        ScenarioPartyDefinition opp = new ScenarioPartyDefinition();
        opp.setPartyKey(oppPartyKey);
        opp.setName(oppPartyName);
        opp.setStartingRole(PartyRole.OPPOSITION);
        opp.setDefaultControllerType(ControllerType.COMPUTER);
        opp.setIdeology(Ideology.ANTI_CORRUPTION);
        opp.setStartingStats(new PartyStats(oppCoins, oppMorale, oppCorruption, oppMedia, oppSupport));
        opp.setColor("#3F88C5");
        opp.setSymbol("Hand");
        parties.add(opp);

        ScenarioPartyDefinition third = new ScenarioPartyDefinition();
        third.setPartyKey("ydp");
        third.setName("Youth Development Party (YDP)");
        third.setStartingRole(PartyRole.THIRD_PARTY);
        third.setDefaultControllerType(ControllerType.HUMAN);
        third.setIdeology(Ideology.REGIONAL_PRIDE);
        third.setStartingStats(new PartyStats(thirdCoins, thirdMorale, thirdCorruption, thirdMedia, thirdSupport));
        third.setColor("#17B890");
        third.setSymbol("Star");
        parties.add(third);

        scenario.setPoliticalParties(parties);

        PublicState publicState = new PublicState();
        publicState.setUndecidedSupport(undecided);
        publicState.setMood("Watchful");
        publicState.setMainIssues(List.of("Jobs", "Governance", "Development"));
        publicState.setMemoryHint("Voters weigh the incumbent's track record against the opposition's promises.");
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
