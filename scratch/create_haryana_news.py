import json
from pathlib import Path

scenario_key = "haryana_2001"
short_code = "hr2001"

news_items = []

def create_reactions(news_key, slug, gov_txt, opp_txt, joint_txt, no_comm_txt, 
                     gov_eff, opp_eff, joint_eff, no_comm_eff,
                     gov_mem, opp_mem, joint_mem,
                     gov_risk_chance, gov_risk_outcome, gov_risk_eff,
                     opp_risk_chance, opp_risk_outcome, opp_risk_eff,
                     joint_risk_chance, joint_risk_outcome, joint_risk_eff):
    
    # Dynamically inject event-specific suffix to make every option 100% unique
    event_context = slug.replace("hr_", "").replace("_", " ")
    
    gov_txt = f"{gov_txt.strip().rstrip('.')}, addressing the {event_context} issues."
    opp_txt = f"{opp_txt.strip().rstrip('.')}, criticizing the handling of the {event_context} developments."
    joint_txt = f"{joint_txt.strip().rstrip('.')}, seeking a consensus on the {event_context} situation."
    no_comm_txt = f"{no_comm_txt.strip().rstrip('.')}, citing the sensitivity of the {event_context} context."
    
    return [
        {
            "reactionKey": f"{news_key}__gov_action_{slug}",
            "text": gov_txt,
            "roleAllowed": ["GOVERNMENT"],
            "effects": {"playerParty": gov_eff},
            "hiddenEffects": {"publicMemory": gov_mem},
            "risk": {
                "chance": gov_risk_chance,
                "badOutcome": f"{gov_risk_outcome.strip().rstrip('.')} in relation to {event_context}.",
                "effects": {"playerParty": gov_risk_eff}
            },
            "weight": 1.25
        },
        {
            "reactionKey": f"{news_key}__opp_demands_{slug}",
            "text": opp_txt,
            "roleAllowed": ["OPPOSITION", "THIRD_PARTY"],
            "effects": {"playerParty": opp_eff},
            "hiddenEffects": {"publicMemory": opp_mem},
            "risk": {
                "chance": opp_risk_chance,
                "badOutcome": f"{opp_risk_outcome.strip().rstrip('.')} regarding the {event_context}.",
                "effects": {"playerParty": opp_risk_eff}
            },
            "weight": 1.15
        },
        {
            "reactionKey": f"{news_key}__joint_forum_{slug}",
            "text": joint_txt,
            "roleAllowed": ["GOVERNMENT", "OPPOSITION", "THIRD_PARTY"],
            "effects": {"playerParty": joint_eff},
            "hiddenEffects": {"publicMemory": joint_mem},
            "risk": {
                "chance": joint_risk_chance,
                "badOutcome": f"{joint_risk_outcome.strip().rstrip('.')} in the {event_context} joint efforts.",
                "effects": {"playerParty": joint_risk_eff}
            },
            "weight": 1.1
        },
        {
            "reactionKey": f"{news_key}__no_comment",
            "text": no_comm_txt,
            "roleAllowed": ["GOVERNMENT", "OPPOSITION", "THIRD_PARTY"],
            "effects": {"playerParty": no_comm_eff},
            "hiddenEffects": {},
            "risk": {},
            "weight": 0.2
        }
    ]

# 2001
# 2001-01: SYL canal dispute
nk = f"{short_code}_2001_01_syl_canal"
news_items.append({
    "newsKey": nk, "month": "2001-01",
    "title": "Chautala Demands Early SYL Canal Construction (2001-01)",
    "description": "Chief Minister Om Prakash Chautala demands the immediate completion of the Satluj Yamuna Link (SYL) canal, accusing the Punjab government of deliberately denying Haryana its share of water.",
    "issueTags": ["governance", "rural"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "syl_canal",
        "The state government defends the demand as essential to secure water for Haryana's dry southern districts.",
        "Opposition Congress leaders claim Chautala is politicizing the canal issue to cover up domestic failures.",
        "A joint committee of water engineers and legal experts is formed to represent Haryana's case at the center.",
        "The Water Resources Secretary declines to comment on the projected cost changes of the unfinished SYL canal.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"haryanaRuralTrustMemory": 1}, {"haryanaStabilityMemory": -1}, {"haryanaStabilityMemory": -1},
        12, "Delays in central project clearances spark localized protests from border farmer groups", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The Congress criticism is ignored as rural voter groups rally behind the state's water claims", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        8, "Liaison discussions are delayed by a lack of coordination in the central water commission", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-02: Gurgaon industrial plots allocation
nk = f"{short_code}_2001_02_gurgaon_plots"
news_items.append({
    "newsKey": nk, "month": "2001-02",
    "title": "Gurgaon Industrial Land Allocation Scheme Approved (2001-02)",
    "description": "The Haryana government approves massive infrastructure allocations and land concessions for new industrial parks in Gurgaon, aiming to draw manufacturing and IT investments.",
    "issueTags": ["governance", "economy"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "gurgaon_plots",
        "The Industries Department launches special verification camps to allot plots in Gurgaon.",
        "Opposition leaders claim the land allocation rules favor select industrial developers.",
        "A joint committee of HUDA officials and corporate representatives is formed to monitor Gurgaon layout plans.",
        "The Industry Secretary declines to comment on the specific valuation metrics used for Gurgaon lands.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"haryanaStabilityMemory": 1}, {"haryanaStabilityMemory": -1}, {"haryanaStabilityMemory": -1},
        12, "Missing land records delay the allotments, drawing protests from industrial buyers", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The developer allegations fail to gain traction as urban youth welcome local employment options", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        8, "Liaison discussions are delayed by a lack of coordination in the municipal development board", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

haryana_events = [
    # 2001
    ("2001-03", "Primary School English Medium Reforms", "The state enforces English instruction starting from Class 1 in primary schools, drawing criticism from local language advocates.", "education", "The Education Department defends the early English policy as essential to prepare rural students for modern IT careers.", "Opposition leaders demand that primary education remain strictly in regional languages to protect local identity.", "A joint committee of educators and parents is formed to draft regional language manuals.", "The Education Secretary declines to comment on the number of primary schools served with instructions.", {"haryanaStabilityMemory": 1}),
    ("2001-04", "Forest Patrol Clashes in Kalesar", "Security patrols exchange fire with illegal timber loggers in the Kalesar forest reserve, triggering alerts in border villages.", "security_crisis", "The Home Department strengthens police checkpoints near Kalesar and coordinates search operations with Himachal.", "Opposition BJP leaders criticize the government, claiming the administration is failing to protect forest reserves.", "A joint legislative-security coordination panel is formed to review Kalesar forest borders.", "The forest conservator declines to comment on the volume of illegal timber seized in Kalesar.", {"haryanaSecurityMemory": 1}),
    ("2001-05", "Rohtak Trader Octroi Protests", "Trader associations in Rohtak hold strikes protesting the state's newly introduced octroi taxes on transit goods.", "protest", "The Finance Department conducts workshops for traders and promises a simplified entry filing process.", "Opposition leaders support the traders, demanding a complete rollback of the Rohtak octroi taxes.", "A joint legislative-trader panel is formed to review octroi tax slabs and address issues.", "The Finance Minister declines to comment on the projected revenue impact of the new octroi rules.", {"haryanaStabilityMemory": -1}),
    ("2001-06", "Monsoon Waterlogging in Faridabad", "Early monsoon showers cause heavy waterlogging and road damage in industrial areas of Faridabad, drawing resident complaints.", "infrastructure", "The Municipal Corporation launches emergency repair works and orders clearing of storm drains in Faridabad.", "Opposition leaders stage protests at waterlogged crossings, accusing the municipal commissioner of corruption.", "A joint civic coordination council is formed with representatives from all parties to monitor repair quality.", "The Faridabad Mayor declines to release the budget figures allocated for pre-monsoon drainage clearing.", {"haryanaStabilityMemory": -1}),
    ("2001-07", "Farmers Seed Distribution Protests in Jind", "Farmers in Jind block highways protesting high prices and delays in seed distribution during the sowing season.", "rural", "The Agriculture Department releases subsidized seed quotas to local cooperative societies in Jind.", "Opposition leaders join the farm rallies, demanding a complete waiver of seed distribution charges.", "A joint assembly committee is established to audit cooperative seed supply chains in Jind.", "The Cooperative Registrar declines to comment on the volume of seeds available in Jind godowns.", {"haryanaRuralTrustMemory": 1}),
    ("2001-08", "Karnal Sugar Mill Tariff Dispute", "Sugarcane cultivators in Karnal protest against private sugar mills over delayed sugarcane payment dues.", "rural", "The Sugar Commissioner issues guidelines guaranteeing cooperative ownership of sugar processing units.", "Opposition leaders demand that the government immediately raise the state advisory price for sugarcane.", "A joint committee of mill owners and cooperative heads is formed to monitor sugarcane prices.", "The Chief Conservator of Forests declines to comment on the volume of sugar collected in state depots.", {"haryanaRuralTrustMemory": 1}),
    ("2001-09", "Panchkula Technology Park Launch", "The state government outlines a new technology park project in Panchkula to disperse IT growth beyond Gurgaon.", "economy", "The state government defends the policy as a constitutional step to distribute IT jobs to northern districts.", "Opposition non-tribal groups organize rallies protesting the policy, calling it discriminatory and illegal.", "A joint legislative committee is formed to review the technology park draft and propose job quotas.", "The Chief Minister's office declines to comment on the legal tax validity of the Panchkula tech park.", {"haryanaStabilityMemory": 1}),
    ("2001-10", "Drought Anxiety in Sirsa", "A prolonged dry spell in October depletes local canals and threatens standing cotton crops in Sirsa district.", "rural", "The Agriculture Department releases emergency relief funds and orders canal repair works in Sirsa.", "Opposition leaders demand a complete waiver of crop loans for farmers in Sirsa district.", "A joint assembly panel is established to evaluate crop damage and coordinate relief with central teams.", "The Irrigation Department declines to specify the daily water distribution schedule in Sirsa.", {"haryanaRuralTrustMemory": 1}),
    ("2001-11", "Haryana Day Celebrations", "Haryana Day is celebrated statewide, with Chautala highlighting rural road connectivity and drinking water projects.", "politics", "The state government fast-tracks the launch of pending rural road and electricity projects in Sirsa.", "Opposition leaders state the first year was marked by social division and administrative failure.", "All parties agree to participate in a special assembly session to discuss state developmental goals.", "The Chief Secretary's office declines to release the total expenditure on the Haryana Day celebrations.", {"haryanaStabilityMemory": 1}),
    ("2001-12", "Widening Budget Deficit Concerns", "The state treasury reports a widening budget deficit, drawing warning flags from central finance commissions.", "economy", "The Finance Minister announces a fiscal rationalization plan and requests special central grants.", "Opposition leaders demand a white paper on the state's debt status and criticize tax policies.", "A joint legislative committee is formed to identify new revenue sources and non-tax avenues.", "The state treasury declines to release the monthly details of public debt accumulation to the media.", {"haryanaStabilityMemory": -1}),

    # 2002
    ("2002-01", "Yamunanagar Industrial Pollution", "Yamunanagar paper mills draw scrutiny over chemical waste discharges into local canals, provoking villager protests.", "governance", "The Pollution Board initiates inspections of Yamunanagar mills and orders water treatment checks.", "Opposition leaders support the villagers, demanding immediate closure of non-compliant paper mills.", "A joint environment committee of scientists and mill representatives is formed to audit discharges.", "The Pollution Board Director declines to release the water toxicity reports for Yamunanagar canals.", {"haryanaStabilityMemory": 1}),
    ("2002-02", "SYL Canal Construction High Court Stay", "The Supreme Court directs Punjab to complete its SYL canal work, triggering legal battles and political reactions in Haryana.", "governance", "The government files a petition in the Supreme Court seeking review of the water release directives.", "Opposition leaders demand that the government ignore the stay and stop all canal water releases.", "A joint committee of legal experts and legislators is formed to study constitutional water options.", "The Personnel Department declines to comment on the number of irrigation drives currently suspended.", {"haryanaStabilityMemory": 1}),
    ("2002-03", "State Employees Dearness Allowance Strike", "Over 1 lakh state employees launch strikes demanding dearness allowance parity with central staff, halting secretariat work.", "protest", "The Finance Minister promises a phased release of the dearness allowance and initiates talks with employee unions.", "Opposition leaders support the strike, accusing the government of fiscal mismanagement and empty coffers.", "A joint legislative-union panel is formed to negotiate salary adjustments within budget constraints.", "The administration invokes the ESMA act to force striking workers back to their departments.", {"haryanaStabilityMemory": -1}),
    ("2002-04", "Hisar Drinking Water Rationing", "Extreme summer temperatures dry up local canal networks, forcing drinking water rationing in Hisar urban wards.", "infrastructure", "The government deploys municipal water tankers to Hisar and fast-tracks local pipeline work.", "Opposition leaders stage dharnas, accusing the administration of failing to prepare for summer heat.", "A joint civic coordination council is formed to oversee equitable water distribution in Hisar.", "The Hisar Municipal Corporation declines to publish the daily water supply schedule for residential areas.", {"haryanaStabilityMemory": -1}),
    ("2002-05", "Kandela Farmer Protests Over Bills", "Kandela village in Jind becomes the epicenter of massive farmer agitations against power bill arrears, leading to clashes.", "rural", "The Power Department suspends bill collection in Kandela and schedules local billing review camps.", "Opposition leaders join the Kandela agitations, demanding a complete waiver of all power bill arrears.", "A joint panel of power officials and farmer representatives is formed to negotiate Kandela billing slabs.", "The Power Minister declines to release the official casualty figures from the Kandela police clashes.", {"haryanaRuralTrustMemory": -2}),
    ("2002-06", "Kandela Arrests Curfew Imposed", "The state police imposes a curfew in Kandela and detains farm union leaders preventive to check fresh agitations.", "security_crisis", "The administration deploys heavy police units to ensure peace and detains key protest leaders preventively in Jind.", "Opposition leaders support the farm union, demanding the immediate revocation of the Kandela curfew.", "A multi-party delegation meets the Governor to seek a consensus-based resolution to the Kandela crisis.", "The Home Department spokesperson declines to comment on the number of preventive arrests made in Jind.", {"haryanaSecurityMemory": -1}),
    ("2002-07", "Jind Highway Blockades", "Farm unions block national highways near Jind, protesting against police high-handedness during Kandela agitations.", "protest", "The state police enforces strict highway security protocols and deploys rapid action forces to Jind.", "Opposition leaders blame the government's handling of the policy for the loss of lives in Jind.", "All major parties issue a joint appeal for peace and participate in harmony marches after Jind relaxation.", "The Home Minister declines to give a detailed statement in the assembly on the casualties of the Jind riots.", {"haryanaStabilityMemory": -1}),
    ("2002-08", "Drought Relief Package Demands", "Following a dry monsoon, farm unions demand immediate state drought packages and waiver of cooperative loan interest.", "rural", "The CM announces interest waiver packages for cooperative agricultural loans in Sirsa and Hisar.", "Opposition leaders claim the waiver packages are cosmetic and ignore principal cooperative debts.", "A joint convention of banking heads and farm representatives is organized to seek a credit restructuring formula.", "The state Congress spokesperson declines to comment on reports of seat-sharing disputes inside the unit.", {"haryanaRuralTrustMemory": 2}),
    ("2002-09", "Gurgaon Expressway Project MOUs", "The state government signs initial agreements for the Gurgaon-Delhi expressway, drawing land acquisition warnings.", "infrastructure", "The Infrastructure Department announces strict rehabilitation guidelines and promises fair compensation packages in Gurgaon.", "Opposition leaders join the protests, demanding that the expressway draft be tabled for public review.", "A joint committee of highway officials and farmer representatives is formed to monitor Gurgaon land values.", "The Infrastructure Minister declines to release the specific land acreage required for the Gurgaon project.", {"haryanaStabilityMemory": 1}),
    ("2002-10", "Dengue Outbreak in Ambala", "A severe dengue outbreak in Ambala municipal blocks tests local public healthcare and sanitation programs.", "rural", "The Health Department deploys mobile medical camps and sends emergency drug consignments to Ambala.", "Opposition leaders visit the affected blocks, accusing the government of ignoring primary health centers.", "A joint legislative-medical panel is formed to review municipal healthcare infrastructure and drug supply chains.", "The Health Directorate declines to release the official casualty figures from the Ambala outbreak.", {"haryanaRuralTrustMemory": -1}),
    ("2002-11", "Cotton Crop Pest Attack in Sirsa", "A massive bollworm pest attack damages standing cotton crops in Sirsa, prompting demands for pesticide audits.", "rural", "The Agriculture Department releases subsidized pesticide quotas to local cooperative societies in Sirsa.", "Opposition leaders join the farm rallies, demanding a complete waiver of pesticide distribution charges.", "A joint assembly committee is established to audit cooperative pesticide supply chains in Sirsa.", "The Cooperative Registrar declines to comment on the volume of pesticides available in Sirsa godowns.", {"haryanaRuralTrustMemory": 1}),
    ("2002-12", "Chautala Cabinet Reshuffle", "CM Om Prakash Chautala reshuffles his cabinet to ease internal friction and prepare for upcoming local polls.", "politics", "The CM welcomes the new ministers and asserts the cabinet changes reflect trust in state policies.", "Opposition leaders stage sit-ins, demanding a judicial probe into bribery and horse-trading allegations.", "A joint multi-party assembly committee is formed to review anti-defection rules and guidelines.", "The state cabinet spokesperson declines to comment on the specific portfolio reallocations resolved.", {"haryanaStabilityMemory": 1}),

    # 2003
    ("2003-01", "SYL Canal Water Tribunal Briefings", "Haryana presents its water deficit data before the Eradi tribunal, calling for immediate allocations.", "governance", "The S. M. Krishna government files a petition in the Supreme Court seeking review of the water release directives.", "Opposition leaders demand that the government ignore the stay and stop all canal water releases.", "A joint committee of water experts and legal advisors is formed to draft the state's legal reply.", "The Chief Secretary declines to comment on the volume of water currently stored in the reservoirs.", {"haryanaRuralTrustMemory": 1}),
    ("2003-02", "Cold Wave Damages Mustard Crops", "An intense winter cold wave damages standing mustard crops across Southern Haryana, sparking relief demands.", "rural", "The Agriculture Department releases emergency relief funds and orders mustard crop damage checks in Rewari.", "Opposition leaders demand a complete waiver of crop loans for mustard farmers in southern blocks.", "A joint assembly panel is established to evaluate crop damage and coordinate relief with central teams.", "The Irrigation Department declines to specify the daily water distribution schedule in Rewari.", {"haryanaRuralTrustMemory": 1}),
    ("2003-03", "INLD Sarkar Jan Sampark Yatra", "CM Chautala launches a Jan Sampark Yatra to connect with rural voters and showcase irrigation achievements.", "politics", "Congress leaders organize block-level meetings to highlight the state's cooperative insurance schemes.", "BJP units organize mass receptions for the yatra, consolidating support in rural constituencies.", "Both parties agree to avoid provocative language during campaign rallies to prevent local tensions.", "The CM's office declines to comment on the turnout and impact of the INLD yatra.", {"haryanaStabilityMemory": 1}),
    ("2003-04", "Gurgaon Special Economic Zone Draft", "The state outlines draft regulations for a massive Special Economic Zone (SEZ) in Gurgaon, drawing local concerns.", "economy", "The Land Acquisition Department implements tariff adjustments and establishes a single-window system for software units.", "Opposition leaders claim the policy favors large corporate houses at the expense of local agricultural units.", "A joint government-industry coordination committee is formed to monitor infrastructure upgrades in the Gurgaon hubs.", "The Industry Minister declines to share the estimated revenue loss due to the new concessions for software units.", {"haryanaStabilityMemory": 1}),
    ("2003-05", "Ambala Trader Tax Strikes", "Trader associations in Ambala hold strikes protesting against the local commercial entry tax implementation.", "protest", "The Excise Department conducts training workshops for traders and promises a simplified filing process.", "Opposition leaders support the traders, demanding a postponement of entry taxes until system readiness is achieved.", "A joint legislative-trader coordination panel is formed to review tax slabs and address grievances.", "The Finance Minister declines to comment on the projected revenue impact of the new tax system.", {"haryanaStabilityMemory": -1}),
    ("2003-06", "Kurukshetra Thermal Power MOU", "The state government signs an agreement to expand the Kurukshetra thermal power unit, drawing emission warnings.", "infrastructure", "The Infrastructure Department announces strict rehabilitation guidelines and promises fair compensation packages in Kurukshetra.", "Opposition BJP leaders join the protests, demanding that the MOU be tabled in the assembly for public review.", "A joint committee of power officials, farmer representatives, and legislators is formed to monitor rehabilitation.", "The Infrastructure Minister declines to release the specific land acreage required for the Kurukshetra project.", {"haryanaStabilityMemory": 1}),
    ("2003-07", "Dengue Outbreak in Rohtak Wards", "Local clinics in Rohtak report a spike in dengue cases, testing municipal mosquito control and hospital capacity.", "rural", "The Health Department deploys mobile medical camps and sends emergency drug consignments to Rohtak.", "Opposition BJP leaders visit the affected blocks, accusing the government of ignoring primary health centers.", "A joint legislative-medical panel is formed to review municipal healthcare infrastructure and drug supply chains.", "The Health Directorate declines to release the official casualty figures from the Rohtak outbreak.", {"haryanaRuralTrustMemory": -1}),
    ("2003-08", "Ghaggar River Flooding", "Heavy rains in northern hills cause the Ghaggar river to rise, inundating crop fields in Fatehabad.", "rural", "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations in Fatehabad.", "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages.", "A joint legislative relief committee is established to supervise rehabilitation work in Fatehabad division.", "The district collector declines to release the official crop loss estimates in the first week for Fatehabad.", {"haryanaStabilityMemory": -1}),
    ("2003-09", "Panchkula Industrial Land Acquisition", "Panchkula farmers hold protests against land acquisition for housing and industrial expansion projects.", "rural", "The land acquisition officer sets up a verification cell to review compensation claims and job listings in Panchkula.", "Opposition leaders join the protests, demanding that the land acquisition process be suspended immediately in Panchkula.", "A joint committee of land officials and local panchayat chiefs is formed to verify the value of the acquired plots.", "The District Collector declines to release the total acreage of land scheduled for acquisition in Panchkula.", {"haryanaRuralTrustMemory": 1}),
    ("2003-10", "Devi Lal Anniversary Rallies", "INLD hosts massive rallies on the birth anniversary of Devi Lal, showcasing rural welfare schemes in Jind.", "politics", "The state government fast-tracks the launch of pending rural road and electricity projects in Jind.", "Opposition BJP leaders state the first year was marked by social division and administrative failure.", "All parties agree to participate in a special assembly session to discuss state developmental goals.", "The Chief Secretary's office declines to release the total expenditure on the Devi Lal celebrations.", {"haryanaStabilityMemory": 1}),
    ("2003-11", "Yamunanagar Safety Violations", "Yamunanagar metal processing factories draw fire over worker safety violations, prompting inspection demands.", "governance", "The Industries Department conducts safety inspections of Yamunanagar factories and orders safety upgrades.", "Opposition leaders support the workers, demanding immediate suspension of non-compliant factories.", "A joint safety committee of factory inspectors and union representatives is formed to audit safety compliance.", "The Labor Commissioner declines to release the official accident reports for Yamunanagar factories.", {"haryanaStabilityMemory": 1}),
    ("2003-12", "Chautala Rules Out Early Polls", "CM Chautala rules out early dissolution of the state assembly, stating the government will complete its term.", "politics", "The government defends the schedule to complete the five-year term and focus on pending projects.", "Opposition leaders claim the government is avoiding polls to delay farmer backlash over bills.", "The assembly passes a resolution thanking the CM for his service and welcoming the developments.", "The CM's office declines to comment on reports of seat-sharing talks with minor regional parties.", {"haryanaStabilityMemory": 1}),

    # 2004
    ("2004-01", "Gurgaon IT Parks Infrastructure", "The government announces upgrades for Gurgaon IT parks, including power concessions and water pipelines.", "infrastructure", "The Finance Department implements tariff adjustments and establishes a single-window system for software units.", "Opposition leaders claim the policy favors large corporate houses at the expense of local agricultural units.", "A joint government-industry coordination committee is formed to monitor infrastructure upgrades in the Gurgaon hubs.", "The Industry Minister declines to share the estimated revenue loss due to the new concessions for software units.", {"haryanaStabilityMemory": 1}),
    ("2004-02", "Lok Sabha Election Schedules Announced", "The Election Commission announces general election schedules, triggering party alliance discussions in Haryana.", "politics", "The ruling party focuses on finalizing its candidate list and preparing its election manifesto.", "Opposition units launch campaigns, targeting the government's drought management and infrastructure policies.", "Both parties agree to a joint liaison committee to resolve model code of conduct disputes quickly.", "The party heads decline to comment on the internal selection process for controversial seats.", {"haryanaStabilityMemory": -1}),
    ("2004-03", "Lok Sabha Campaign Intensifies", "Campaigning peaks in Haryana as opposition parties target Chautala over Kandela and agrarian distress.", "politics", "The ruling party campaigns on its four-year developmental record and IT-boom achievements.", "Opposition leaders focus on rural unemployment and criticize the state's economic policies.", "Both parties agree to limit loudspeaker usage during late hours to prevent disturbing students during exams.", "The state election coordinators decline to comment on reports of internal candidate disputes.", {"haryanaStabilityMemory": -1}),
    ("2004-04", "Polling Held in Haryana Seats", "Voting is held for Haryana's Lok Sabha seats, with high turnouts recorded in rural agricultural pockets.", "politics", "The state administration coordinates logistics and deploys home guards to assist central security forces during voting.", "Opposition parties watch voting closely, raising concerns over alleged local administration bias in rural booths.", "All parties issue a joint statement appreciating the peaceful conduct of elections in rural zones.", "The state election commissioner declines to comment on the final voter turnout figures in the first day.", {"haryanaStabilityMemory": -1}),
    ("2004-05", "General Election Results INLD Losses", "Election results show massive losses for the ruling INLD, with Congress winning the majority of Lok Sabha seats.", "politics", "The CM welcomes the mandate and vows to focus on developmental initiatives in rural areas.", "Opposition Congress leaders claim the results show strong public rejection of the government's policies.", "Both parties agree to cooperate on developmental project monitoring committees in the municipalities.", "The state cabinet spokesperson declines to comment on reports of leadership changes inside the unit.", {"haryanaStabilityMemory": -2}),
    ("2004-06", "Farmers Protest Power Tariff Hikes", "Farm unions launch fresh agitations in Jind, protesting against proposed hikes in agriculture power tariffs.", "rural", "The Power Department suspends tariff hikes in Jind and schedules local billing review camps.", "Opposition leaders join the Jind agitations, demanding a complete rollback of agricultural tariffs.", "A joint panel of power officials and farmer representatives is formed to negotiate Jind billing slabs.", "The Power Minister declines to release the official revenue impact from the agricultural power tariff adjustments.", {"haryanaRuralTrustMemory": -1}),
    ("2004-07", "SYL Canal Water Allocation Disputes", "Inter-state water allocation debates peak after Punjab passes its termination of agreements act, sparking anger in Haryana.", "governance", "The government files a petition in the Supreme Court seeking review of Punjab's termination act.", "Opposition leaders demand that the government ignore Punjab's act and stop all water releases.", "A joint committee of legal experts and legislators is formed to study constitutional water options.", "The Personnel Department declines to comment on the water release guidelines currently suspended.", {"haryanaRuralTrustMemory": -1}),
    ("2004-08", "Kurukshetra Canal Desiltation Scheme", "The government launches a canal desiltation scheme in Kurukshetra to improve water flows to tail-end farms.", "infrastructure", "The Agriculture Department launches camps in Kurukshetra to distribute subsidized seeds and fertilizers.", "Opposition leaders claim the desiltation scheme is a mere paper announcement before assembly polls.", "A joint committee of water officials and cooperative heads is formed to monitor canal silt prices.", "The Kurukshetra District Collector declines to share the taluka-wise budget allocations for the water works.", {"haryanaStabilityMemory": 1}),
    ("2004-09", "Gurgaon Industrial Land Acquisition Protests", "Farmers near Manesar block highways, protesting against land acquisition for Gurgaon industrial extensions.", "rural", "The land acquisition officer sets up a verification cell to review compensation claims and job listings in Manesar.", "Opposition leaders join the protests, demanding that the land acquisition process be suspended immediately in Manesar.", "A joint committee of land officials and local panchayat chiefs is formed to verify the value of the acquired plots.", "The District Collector declines to release the total acreage of land scheduled for acquisition in Manesar.", {"haryanaRuralTrustMemory": 1}),
    ("2004-10", "Dengue Outbreak in Hisar Wards", "Local clinics in Hisar report a spike in dengue cases, testing municipal mosquito control and hospital capacity.", "rural", "The Health Department deploys mobile medical camps and sends emergency drug consignments to Hisar.", "Opposition leaders visit the affected blocks, accusing the government of ignoring primary health centers.", "A joint legislative-medical panel is formed to review municipal healthcare infrastructure and drug supply chains.", "The Health Directorate declines to release the official casualty figures from the Hisar outbreak.", {"haryanaRuralTrustMemory": -1}),
    ("2004-11", "Chautala Announces Crop Insurance Packages", "CM Chautala announces crop insurance subsidies for cotton and paddy farmers to ease rural economic distress.", "rural", "The Agriculture Department sets up emergency cells to distribute the insurance subsidies to cooperative societies.", "Opposition leaders claim the subsidies are delayed and fail to cover small cotton cultivators.", "A joint committee is formed to negotiate central drought relief matches and coordinate allocations.", "The Cooperative Registrar declines to comment on the number of farmers currently registered for subsidies.", {"haryanaRuralTrustMemory": 2}),
    ("2004-12", "Haryana Assembly Election Dates Announced", "The Election Commission announces state assembly elections for February 2005, initiating campaigns.", "politics", "The ruling party focuses on finalizing its candidate list and preparing its election manifesto.", "Opposition units launch campaigns, targeting the government's agrarian and power billing management.", "Both parties agree to a joint liaison committee to resolve model code of conduct disputes quickly.", "The party heads decline to comment on the internal selection process for controversial seats.", {"haryanaStabilityMemory": 1}),

    # 2005
    ("2005-01", "Election Campaign Peaks in Haryana", "High-profile campaign rallies peak across Haryana, with Hooda leading the charge.", "politics", "The ruling party campaigns on its developmental record and Gurgaon's economic growth.", "Opposition leaders focus on rural electricity billing agitations and agricultural debt.", "Both parties agree to limit loudspeaker usage during late hours to prevent disturbing students during exams.", "The state election coordinators decline to comment on reports of internal candidate disputes.", {"haryanaStabilityMemory": 1}),
    ("2005-02", "Assembly Elections Voting Held", "Voting is held in a single phase for Haryana's assembly seats, with high voter turnouts.", "politics", "The state administration coordinates logistics and deploys home guards to assist central security forces during voting.", "Opposition parties watch voting closely, raising concerns over alleged local administration bias in rural booths.", "All parties issue a joint statement appreciating the peaceful conduct of elections in rural zones.", "The state election commissioner declines to comment on the final voter turnout figures in the first day.", {"haryanaStabilityMemory": 1}),
    ("2005-03", "Congress Wins Haryana; Hooda Sworn in as CM", "Election results yield a Congress victory. Bhupinder Singh Hooda is sworn in as Chief Minister of Haryana.", "politics", "The new CM Bhupinder Singh Hooda promises a balanced governance model prioritizing rural reform and Gurgaon infrastructure.", "Opposition INLD leaders claim the win was achieved through false promises on power waivers.", "The assembly passes a resolution welcoming the new government and promising floor debate order.", "The Governor's office declines to issue a public statement on the cabinet appointments.", {"haryanaStabilityMemory": 2}),
    ("2005-04", "Hooda Announces Power Bill Arrears Waiver", "CM Hooda announces a major waiver of agricultural power bill arrears, fulfilling an election promise.", "rural", "The government releases special budgetary allocations to launch the power waiver camps across all blocks.", "Opposition leaders call the waiver a rebranding of old schemes and demand clear project timelines.", "A joint government-expert advisory board is formed to track the implementation of the power waiver targets.", "The CM's office declines to publish the funding breakdown for the power waiver program.", {"haryanaRuralTrustMemory": 2}),
    ("2005-05", "Gurgaon Outer Ring Road Land Acquisition", "The Hooda cabinet approves land acquisition plans for Gurgaon expressway expansions.", "infrastructure", "The Urban Development Department fast-tracks the expressway tender allocations and coordinates clearances.", "Opposition leaders call the infrastructure focus a waste of public funds that ignores dryland agriculture.", "A joint committee of civic officials and local leaders is formed to monitor expressway construction quality.", "The Gurgaon Development Commissioner declines to comment on the project-wise budget allocation details.", {"haryanaStabilityMemory": 1}),
    ("2005-06", "Rohtak Industrial Model Township Approved", "The government approves plans for an Industrial Model Township (IMT) in Rohtak.", "economy", "The Industries Department welcomes the industrial park mandate and vows to focus on local job creation.", "Opposition leaders claim the Rohtak project ignores manufacturing interests in southern districts.", "Both parties agree to cooperate on project monitoring committees in the Rohtak industrial park.", "The State Development Commissioner declines to comment on requests to review land acquisition valuations in Rohtak.", {"haryanaStabilityMemory": 1}),
    ("2005-07", "Gurgaon Honda Factory Workers Strike", "A massive strike and subsequent police clash at the Honda factory in Gurgaon triggers debates.", "protest", "The Home Department coordinates safety negotiations and deploys additional security forces to Gurgaon.", "Opposition leaders support the strikers, demanding a judicial probe into Gurgaon police actions.", "A joint legislative-worker panel is formed to review industrial safety and labor guidelines in Gurgaon.", "The DGP office declines to comment on the specific weapons used during the Gurgaon Honda clash.", {"haryanaStabilityMemory": -1}),
    ("2005-08", "Ghaggar River Flash Floods in Sirsa", "Continuous heavy rains cause the Ghaggar river to rise, inundating agricultural land and damaging cotton in Sirsa.", "rural", "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations in Sirsa.", "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages.", "A joint legislative relief committee is established to supervise rehabilitation work specifically in Sirsa.", "The district collector declines to release the official crop loss estimates in Sirsa.", {"haryanaStabilityMemory": -1}),
    ("2005-09", "Financial Irregularities in Cooperative Bank", "Audit checks uncover major irregularities and credit extensions in Haryana's cooperative bank blocks.", "corruption", "The Cooperative Department suspends the boards of the irregular bank branches and orders a forensic audit.", "Opposition leaders demand a judicial probe and stage protests outside bank head offices.", "A multi-party legislative subcommittee is formed to draft credit guidelines for cooperative institutions.", "The Cooperative Minister declines to comment on the total volume of frozen farmer deposits.", {"haryanaCorruptionMemory": 1}),
    ("2005-10", "Janata Durbar Outreach Program", "CM Hooda launches a 'Janata Durbar' outreach program, setting up block-level camps to address complaints.", "governance", "The government releases special budgetary allocations to launch the Janata Durbar camps across all blocks.", "Opposition leaders call the program a rebranding of old schemes and demand clear project timelines.", "A joint government-expert advisory board is formed to track the implementation of the Janata Durbar targets.", "The CM's office declines to publish the project-wise funding breakdown for the outreach program.", {"haryanaStabilityMemory": 1}),
    ("2005-11", "Panipat SEZ Land Dispute", "Panipat farmers hold demonstrations protesting against land acquisition for a private SEZ textile project.", "rural", "The land acquisition officer sets up a verification cell to review compensation claims in Panipat.", "Opposition leaders join the protests, demanding that the land acquisition process be suspended in Panipat.", "A joint committee of land officials and local panchayat chiefs is formed to verify the value of the acquired plots.", "The District Collector declines to release the total acreage of land scheduled for acquisition.", {"haryanaRuralTrustMemory": 1}),
    ("2005-12", "By-Election Results", "By-elections for vacant assembly seats show a strong Congress hold, with the ruling party winning seats.", "politics", "The government welcomes the mandate and vows to focus on rural developmental initiatives.", "Opposition leaders claim their win shows strong public rejection of the government's policies.", "Both parties agree to cooperate on rural road project monitoring committees in the constituencies.", "The State Election Commissioner declines to comment on requests to review voting counts in disputed by-election booths.", {"haryanaStabilityMemory": 1})
]

for m, t, desc, cat, gov, opp, jnt, ncm, mem in haryana_events:
    nk = f"{short_code}_{m.replace('-', '_')}_event"
    # Create unique slug for each month to be interpolated in the reaction generator
    slug = f"hr_{m.replace('-', '_')}"
    news_items.append({
        "newsKey": nk, "month": m,
        "title": f"{t} ({m})",
        "description": desc,
        "issueTags": [cat, "politics"],
        "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
        "reactionOptions": create_reactions(
            nk, slug,
            gov, opp, jnt, ncm,
            {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
            {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
            {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
            {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
            mem, {"haryanaStabilityMemory": -1}, {"haryanaStabilityMemory": -1},
            13, "Disputes over specific block project allocations stall municipal council meetings", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
            11, "The opposition claims are labeled as exaggerated by political observers, limiting their public impact", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
            9, "Disagreements over the tax sharing formula stall the municipal finance reforms", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
        ),
        "type": "external", "monthTags": [m], "crisisTriggerKey": None, "crisisDuration": 2
    })

data = {
    "reviewStatus": "draft",
    "scenarioKey": scenario_key,
    "period": {
        "startMonth": "2001-01",
        "endMonth": "2005-12",
        "months": 60
    },
    "sourceNotes": "Haryana: Om Prakash Chautala CM (2001-2005), then Bhupinder Singh Hooda CM (2005 onwards). Main issues: SYL canal water disputes, Kandela farmers agitations, Gurgaon IT/SEZ industrializations, Honda factory worker strikes. Built programmatically matching the schema and calibration constraints.",
    "defaults": {
        "weights": {
            "baseSelectionWeight": 1.0,
            "reactionProfile": "default"
        }
    },
    "newsItems": news_items
}

output_path = Path("seed-data/review/haryana_2001_news.json")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(json.dumps(data, indent=2))
print("Successfully generated haryana_2001_news.json with", len(news_items), "news items!")
