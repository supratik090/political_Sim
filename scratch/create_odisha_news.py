import json
from pathlib import Path

scenario_key = "odisha_2001"
short_code = "od2001"

news_items = []

def create_reactions(news_key, slug, gov_txt, opp_txt, joint_txt, no_comm_txt, 
                     gov_eff, opp_eff, joint_eff, no_comm_eff,
                     gov_mem, opp_mem, joint_mem,
                     gov_risk_chance, gov_risk_outcome, gov_risk_eff,
                     opp_risk_chance, opp_risk_outcome, opp_risk_eff,
                     joint_risk_chance, joint_risk_outcome, joint_risk_eff):
    
    # Dynamically inject event-specific suffix to make every option 100% unique
    event_context = slug.replace("od_", "").replace("_", " ")
    
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
# 2001-01: Super Cyclone Rehabilitation
nk = f"{short_code}_2001_01_cyclone_rehab"
news_items.append({
    "newsKey": nk, "month": "2001-01",
    "title": "Cyclone Rehabilitation Progress Audited (2001-01)",
    "description": "Chief Minister Naveen Patnaik orders a comprehensive audit of post-super cyclone shelter construction and relief distribution, vowing transparency and action against corrupt officers.",
    "issueTags": ["governance", "rural"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "cyclone_rehab",
        "The state government defends the audit as a critical step to ensure that cyclone aid reaches genuine beneficiaries.",
        "Opposition Congress leaders claim the audit is a political exercise to delay actual shelter delivery.",
        "A joint committee of civic representatives and audit teams is formed to monitor district-wise shelter works.",
        "The Relief Commissioner declines to comment on the volume of unutilized central rehabilitation funds.",
        {"partyMorale": 3, "corruptionScore": -1, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"odishaStabilityMemory": 1}, {"odishaStabilityMemory": -1}, {"odishaStabilityMemory": -1},
        12, "Delays in verification camps spark localized protests from coastal villager groups", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The Congress criticism is ignored as rural voter groups welcome transparency audits", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        8, "Audit coordination is delayed by a lack of transport in remote coastal blocks", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-02: BJD-BJP alliance coordination
nk = f"{short_code}_2001_02_alliance_meet"
news_items.append({
    "newsKey": nk, "month": "2001-02",
    "title": "BJD-BJP Alliance Coordination Meeting Held (2001-02)",
    "description": "Leaders of the BJD and BJP meet in Bhubaneswar to coordinate municipal poll strategies, reaffirming their coalition program and mutual support across seats.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "alliance_meet",
        "Alliance leaders welcome the coordination and vow to focus on clean governance targets.",
        "Opposition Congress leaders claim the BJD-BJP alliance is based on opportunistic power sharing.",
        "Both parties agree to establish a joint campaign monitoring desk for municipal elections.",
        "The alliance spokespersons decline to comment on reports of seat sharing friction in Cuttack.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"odishaStabilityMemory": 1}, {"odishaStabilityMemory": -1}, {"odishaStabilityMemory": -1},
        12, "Rebel candidates in several wards threaten to run as independents, causing minor friction", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The Congress claims fail as candidate lists are successfully integrated across divisions", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        8, "Liaison coordination meetings are delayed by a lack of attendance from local district chiefs", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

odisha_events = [
    # 2001
    ("2001-03", "Primary Education Mother Tongue Focus", "The state government drafts rules emphasizing mother tongue instruction in primary tribal schools, drawing praise from cultural groups.", "education", "The Education Department defends regional language instructions as essential to improve tribal literacy.", "Opposition leaders demand that English instruction start early to prepare students for national jobs.", "A joint committee of tribal educators and linguists is formed to draft school syllabus guidelines.", "The Education Director declines to comment on the budget allocated for printing tribal language books.", {"odishaIdentityMemory": 2}),
    ("2001-04", "Simlipal Tiger Reserve Patrols", "Anti-poaching patrols clash with local illegal loggers inside Simlipal reserve, triggering forest boundary disputes.", "security_crisis", "The Forest Department strengthens forest guard units and initiates checks near border trails.", "Opposition leaders accuse the government of failing to protect biodiversity in Simlipal.", "A joint legislative-forest panel is formed to review security measures along Simlipal boundaries.", "The Chief Conservator of Forests declines to comment on the number of local loggers arrested in Simlipal.", {"odishaSecurityMemory": 1}),
    ("2001-05", "Cuttack Trader Entry Tax Protests", "Trader associations in Cuttack hold strikes protesting against newly proposed commercial entry taxes.", "protest", "The Commercial Tax Department conducts workshops for traders and promises a simplified entry filing process.", "Opposition leaders support the traders, demanding a rollback of the Cuttack transit taxes.", "A joint legislative-trader panel is formed to review tax slabs and address issues.", "The Finance Minister declines to comment on the projected revenue impact of the new entry taxes.", {"odishaStabilityMemory": -1}),
    ("2001-06", "Bhubaneswar Drainage Waterlogging", "Early monsoon showers cause severe waterlogging in commercial sectors of Bhubaneswar, drawing resident protests.", "infrastructure", "The Municipal Corporation launches emergency repair works and orders clearing of storm drains in Bhubaneswar.", "Opposition leaders stage protests at waterlogged crossings, accusing the municipal commissioner of corruption.", "A joint civic coordination council is formed with representatives from all parties to monitor repair quality.", "The Bhubaneswar Mayor declines to release the budget figures allocated for pre-monsoon drainage clearing.", {"odishaStabilityMemory": -1}),
    ("2001-07", "Farmers Fertilizer Distribution Protests", "Cultivators in Bargarh hold protests against high prices and delays in cooperative fertilizer distribution during sowing.", "rural", "The Agriculture Department releases subsidized fertilizer quotas to local cooperative societies in Bargarh.", "Opposition leaders join the farm rallies, demanding a complete waiver of distribution charges.", "A joint assembly committee is established to audit cooperative fertilizer supply chains in Bargarh.", "The Cooperative Registrar declines to comment on the volume of urea available in Bargarh godowns.", {"odishaRuralTrustMemory": 1}),
    ("2001-08", "Tribal Land Rights Protests in Rayagada", "Tribal groups in Rayagada hold rallies protesting against land encroachment by commercial paper mills.", "rural", "The Land Department launches verification camps in Rayagada to verify tribal land claims and distribute titles.", "Opposition leaders join the rallies, demanding the immediate withdrawal of industrial land leases in Rayagada.", "A joint committee of forest officials and tribal representatives is formed to draft land guidelines.", "The Rayagada Collector declines to comment on the number of local villagers booked under forest acts.", {"odishaRuralTrustMemory": 1}),
    ("2001-09", "Puri Beach Tourism Infrastructure", "The tourism department outlines development plans for Puri beach, prompting environmental audits of local hotels.", "economy", "The state government defends the policy as a constitutional step to draw global tourism investments to Puri.", "Opposition leaders organize protests, calling the infrastructure focus a threat to local fishermen.", "A joint legislative committee is formed to review the Puri beach master plan and protect traditional landings.", "The Tourism Director declines to comment on the estimated value of land concessions granted to hotel developers.", {"odishaIdentityMemory": 1}),
    ("2001-10", "Drought Anxiety in Kalahandi", "A prolonged dry spell in Kalahandi-Balangir-Koraput (KBK) districts depletes ponds and threatens standing paddy.", "rural", "The Agriculture Department releases emergency relief funds and orders tank repair works in Kalahandi.", "Opposition leaders demand a complete waiver of crop loans for KBK farmers.", "A joint assembly panel is established to evaluate crop damage and coordinate relief with central teams.", "The Irrigation Department declines to specify the daily water distribution schedule in Kalahandi.", {"odishaRuralTrustMemory": 1}),
    ("2001-11", "Mining Lease Verification Drive", "The government launches a verification drive on iron ore mining leases to check illegal extraction in Keonjhar.", "governance", "The Mining Department launches special verification camps to inspect lease boundaries in Keonjhar.", "Opposition leaders claim the mining audits are mere paper announcements without punitive action.", "A joint committee of mining officials and local representatives is formed to monitor lease execution.", "The Mining Secretary declines to comment on reports of lease boundary violations in Keonjhar.", {"odishaStabilityMemory": 1}),
    ("2001-12", "Fiscal Deficit Debt Relief", "The state treasury reports a widening budget deficit, drawing warning flags from central finance commissions.", "economy", "The Finance Minister announces a fiscal rationalization plan and requests special central grants.", "Opposition leaders demand a white paper on the state's debt status and criticize tax policies.", "A joint legislative committee is formed to identify new revenue sources and non-tax avenues.", "The state treasury declines to release the monthly details of public debt accumulation to the media.", {"odishaStabilityMemory": -1}),

    # 2002
    ("2002-01", "Balasore Coast Shrimp Farm Disputes", "Local fishermen in Balasore protest against commercial shrimp farming blocks, alleging ecological damage to coasts.", "governance", "The Fisheries Department initiates inspections of Balasore shrimp units and orders ecological checks.", "Opposition leaders support the fishermen, demanding immediate closure of non-compliant commercial units.", "A joint environment committee of scientists and local representatives is formed to audit coastal farms.", "The Fisheries Director declines to release the water toxicity reports for Balasore creeks.", {"odishaStabilityMemory": 1}),
    ("2002-02", "Anti-Corruption Vigilance Bureau Audits", "The state vigilance bureau registers corruption cases against former ministers, raising political temperatures.", "governance", "The Vigilance Director welcomes the cases and vows to pursue all illegal asset holdings thoroughly.", "Opposition leaders call the vigilance cases a political witch hunt targeting selective leaders.", "A joint multi-party assembly committee is formed to review anti-defection rules and guidelines.", "The Vigilance Bureau spokesperson declines to comment on specific recovery figures.", {"odishaStabilityMemory": 2}),
    ("2002-03", "State Employees Strike Over Allowances", "Over 1 lakh state employees launch strikes demanding dearness allowance parity with central staff, halting secretariat work.", "protest", "The Finance Minister promises a phased release of the dearness allowance and initiates talks with employee unions.", "Opposition leaders support the strike, accusing the government of fiscal mismanagement and empty coffers.", "A joint legislative-union panel is formed to negotiate salary adjustments within budget constraints.", "The administration invokes the ESMA act to force striking workers back to their departments.", {"odishaStabilityMemory": -1}),
    ("2002-04", "KBK Drinking Water Tankers", "Extreme summer temperatures dry up local wells, forcing drinking water tanker deployment in Bolangir.", "infrastructure", "The government deploys municipal water tankers to affected blocks and fast-tracks local pipeline work.", "Opposition leaders stage dharnas, accusing the administration of failing to prepare for summer heat.", "A joint civic coordination council is formed to oversee equitable water distribution in Bolangir.", "The Bolangir Municipal Corporation declines to publish the daily water supply schedule.", {"odishaStabilityMemory": -1}),
    ("2002-05", "Hirakud Dam Water Sharing Debate", "Farmers in Sambalpur protest against the allocation of Hirakud dam water to industrial units, demanding irrigation priority.", "rural", "The Irrigation Department suspends industrial allotments and schedules local canal water checks.", "Opposition leaders join the Sambalpur protests, demanding a complete halt of Hirakud water to industries.", "A joint panel of water officials and farmer representatives is formed to negotiate Hirakud canal releases.", "The Irrigation Minister declines to share the daily inflow data for the Hirakud reservoir.", {"odishaRuralTrustMemory": -1}),
    ("2002-06", "Food for Work Program Audits", "A central team audits the state's food-for-work programs, raising flags over rice grain diversion in tribal blocks.", "corruption", "The Relief Commissioner orders a department audit and coordinates checks with block-level officers.", "Opposition leaders claim the audit proves widespread rice diversion and administrative corruption.", "A joint legislative committee is established to audit cooperative rice supply chains.", "The Cooperative Registrar declines to comment on the volume of rice grains available in state depots.", {"odishaCorruptionMemory": 1}),
    ("2002-07", "Tribal Rallies in Koraput", "Tribal organizations in Koraput hold rallies protesting against delayed land verification and forest rights.", "protest", "The land acquisition officer sets up a verification cell to review compensation claims and job listings in Koraput.", "Opposition leaders join the protests, demanding that the land acquisition process be suspended in Koraput.", "A joint committee of land officials and tribal representatives is formed to verify local plots.", "The Koraput Collector declines to release the total acreage of land scheduled for acquisition.", {"odishaStabilityMemory": -1}),
    ("2002-08", "Flood Emergency in Mahanadi Basin", "Heavy rainfall in the upper catchment areas causes the Mahanadi river to overflow, inundating low-lying delta sectors.", "security_crisis", "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations.", "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages.", "A joint legislative relief committee is established to supervise rehabilitation work in delta blocks.", "The district collector declines to release the official crop loss estimates in delta talukas.", {"odishaStabilityMemory": -1}),
    ("2002-09", "Industrial Park Land Allocation Protests", "Farmers near Khurda block highways, protesting against land acquisition for a new industrial estate expansion.", "rural", "The land acquisition officer sets up a verification cell to review compensation claims in Khurda.", "Opposition leaders join the protests, demanding that the land acquisition process be suspended in Khurda.", "A joint committee of land officials and local panchayat chiefs is formed to verify Khurda plots.", "The District Collector declines to release the total acreage of land scheduled for acquisition in Khurda.", {"odishaRuralTrustMemory": 1}),
    ("2002-10", "Dengue Outbreak in Ganjam", "Local clinics in Ganjam report a spike in dengue cases, testing municipal mosquito control and hospital capacity.", "rural", "The Health Department deploys mobile medical camps and sends emergency drug consignments to Ganjam.", "Opposition leaders visit the affected blocks, accusing the government of ignoring primary health centers.", "A joint legislative-medical panel is formed to review municipal healthcare infrastructure and drug supply chains.", "The Health Directorate declines to release the official casualty figures from the Ganjam outbreak.", {"odishaRuralTrustMemory": -1}),
    ("2002-11", "Kalahandi Cotton Farmers Support", "Cotton cultivators in Kalahandi demand immediate state purchase price guarantees due to weak market rates.", "rural", "The Agriculture Department launches camps in Kalahandi to distribute subsidized seeds and fertilizers.", "Opposition leaders join the farm rallies, demanding a complete waiver of distribution charges.", "A joint committee of cotton buyers and cooperative heads is formed to monitor cotton tariffs.", "The Kalahandi District Collector declines to share the taluka-wise budget allocations for the cotton works.", {"odishaRuralTrustMemory": 1}),
    ("2002-12", "Cabinet Reshuffle for Unity", "CM Naveen Patnaik reshuffles his cabinet to ease internal coalition friction and prepare for upcoming local polls.", "politics", "The CM welcomes the new ministers and asserts the cabinet changes reflect trust in state policies.", "Opposition leaders stage sit-ins, demanding a judicial probe into bribery and horse-trading allegations.", "A joint multi-party assembly committee is formed to review anti-defection rules and guidelines.", "The state cabinet spokesperson declines to comment on the specific portfolio reallocations resolved.", {"odishaStabilityMemory": 1}),

    # 2003
    ("2003-01", "Mining Royalty Revision Demands", "Odisha demands revision of iron ore and coal royalties from the center to support state developmental funds.", "governance", "The Finance Minister announces a fiscal rationalization plan and requests special central grants.", "Opposition leaders demand a white paper on the state's debt status and royalty allocations.", "A joint legislative committee is formed to identify new revenue sources and non-tax avenues.", "The state treasury declines to release the monthly details of public debt accumulation to the media.", {"odishaStabilityMemory": 1}),
    ("2003-02", "Cold Wave Damages Pulses Crops", "An intense winter cold wave damages standing pulses crops across Southern Odisha, prompting relief demands.", "rural", "The Agriculture Department releases emergency relief funds and orders crop damage checks in Nayagarh.", "Opposition leaders demand a complete waiver of crop loans for farmers in southern blocks.", "A joint assembly panel is established to evaluate crop damage and coordinate relief with central teams.", "The Irrigation Department declines to specify the daily water distribution schedule in Nayagarh.", {"odishaRuralTrustMemory": 1}),
    ("2003-03", "BJD Jan Sampark Yatra", "CM Naveen Patnaik launches a Jan Sampark Yatra to connect with rural voters and showcase cyclone shelter works.", "politics", "Congress leaders organize block-level meetings to highlight the state's cooperative insurance schemes.", "BJP units organize mass receptions for the yatra, consolidating support in rural constituencies.", "Both parties agree to avoid provocative language during campaign rallies to prevent local tensions.", "The CM's office declines to comment on the turnout and impact of the BJD yatra.", {"odishaStabilityMemory": 1}),
    ("2003-04", "Kalinga Nagar Industrial Development Scheme", "The state cabinet approves infrastructure allocations for Kalinganagar industrial zone, drawing tribal panels.", "economy", "The Industries Department welcomes the Kalinganagar project and vows to focus on local job creation.", "Opposition leaders claim the industrial project ignores agricultural interests in northern districts.", "Both parties agree to cooperate on project monitoring committees in the Kalinganagar zone.", "The State Development Commissioner declines to comment on requests to review land acquisition valuations.", {"odishaStabilityMemory": 1}),
    ("2003-05", "Bhubaneswar Trader VAT Protests", "Trader associations in Bhubaneswar hold strikes protesting against newly proposed commercial entry taxes.", "protest", "The Excise Department conducts training workshops for traders and promises a simplified filing process.", "Opposition leaders support the traders, demanding a postponement of entry taxes until system readiness is achieved.", "A joint legislative-trader coordination panel is formed to review tax slabs and address grievances.", "The Finance Minister declines to comment on the projected revenue impact of the new tax system.", {"odishaStabilityMemory": -1}),
    ("2003-06", "Rourkela Power Grid MOU", "The state government signs an agreement to expand Rourkela grid lines, drawing emissions warnings.", "infrastructure", "The Infrastructure Department announces strict rehabilitation guidelines and promises fair compensation packages in Rourkela.", "Opposition BJP leaders join the protests, demanding that the MOU be tabled in the assembly for public review.", "A joint committee of power officials, farmer representatives, and legislators is formed to monitor rehabilitation.", "The Infrastructure Minister declines to release the specific land acreage required for the Rourkela project.", {"odishaStabilityMemory": 1}),
    ("2003-07", "Dengue Outbreak in Cuttack Wards", "Local clinics in Cuttack report a spike in dengue cases, testing municipal mosquito control and hospital capacity.", "rural", "The Health Department deploys mobile medical camps and sends emergency drug consignments to Cuttack.", "Opposition BJP leaders visit the affected blocks, accusing the government of ignoring primary health centers.", "A joint legislative-medical panel is formed to review municipal healthcare infrastructure and drug supply chains.", "The Health Directorate declines to release the official casualty figures from the Cuttack outbreak.", {"odishaRuralTrustMemory": -1}),
    ("2003-08", "Mahanadi Delta Flooding", "Heavy rains in the upper catchment areas cause the Mahanadi river to rise, inundating crop fields in Kendrapara.", "rural", "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations in Kendrapara.", "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages.", "A joint legislative relief committee is established to supervise rehabilitation work in Kendrapara division.", "The district collector declines to release the official crop loss estimates in the first week for Kendrapara.", {"odishaStabilityMemory": -1}),
    ("2003-09", "Jajpur Industrial Land Acquisition Protests", "Farmers near Jajpur hold protests against land acquisition for steel factory expansion projects.", "rural", "The land acquisition officer sets up a verification cell to review compensation claims and job listings in Jajpur.", "Opposition leaders join the protests, demanding that the land acquisition process be suspended in Jajpur.", "A joint committee of land officials and local panchayat chiefs is formed to verify Jajpur plots.", "The District Collector declines to release the total acreage of land scheduled for acquisition in Jajpur.", {"odishaRuralTrustMemory": 1}),
    ("2003-10", "Gopabandhu Das Birth Anniversary Rallies", "BJD hosts massive rallies on the birth anniversary of Gopabandhu Das, showcasing rural welfare schemes in Puri.", "politics", "The state government fast-tracks the launch of rural road and electricity projects in Puri.", "Opposition leaders state the first year was marked by social division and administrative failure.", "All parties agree to participate in a special assembly session to discuss state developmental goals.", "The Chief Secretary's office declines to release the total expenditure on the Gopabandhu celebrations.", {"odishaStabilityMemory": 1}),
    ("2003-11", "Keonjhar Safety Violations", "Keonjhar iron ore processing factories draw fire over worker safety violations, prompting inspection demands.", "governance", "The Industries Department conducts safety inspections of Keonjhar factories and orders safety upgrades.", "Opposition leaders support the workers, demanding immediate suspension of non-compliant factories.", "A joint safety committee of factory inspectors and union representatives is formed to audit safety compliance.", "The Labor Commissioner declines to release the official accident reports for Keonjhar factories.", {"odishaStabilityMemory": 1}),
    ("2003-12", "Patnaik Decides on Early Polls", "CM Naveen Patnaik decides to dissolve the assembly early, aligning state polls with Lok Sabha elections in 2004.", "politics", "The government defends the early dissolution as a step to align state and central voting timelines.", "Opposition leaders claim the early polls are a desperate attempt to bypass drought accountability.", "The assembly passes a resolution thanking Naveen Patnaik for his service and welcoming the elections.", "The CM's office declines to comment on reports of seat-sharing talks with minor regional parties.", {"odishaStabilityMemory": 1}),

    # 2004
    ("2004-01", "Bhadrak IT Parks Infrastructure", "The government announces upgrades for Bhadrak IT parks, including power concessions and water pipelines.", "infrastructure", "The Finance Department implements tariff adjustments and establishes a single-window system for software units.", "Opposition leaders claim the policy favors large corporate houses at the expense of local agricultural units.", "A joint government-industry coordination committee is formed to monitor infrastructure upgrades in the Bhadrak hubs.", "The Industry Minister declines to share the estimated revenue loss due to the new concessions for software units.", {"odishaStabilityMemory": 1}),
    ("2004-02", "Assembly Election Dates Announced", "The Election Commission announces state assembly elections for April 2004, initiating campaigns.", "politics", "The ruling party focuses on finalizing its candidate list and preparing its election manifesto.", "Opposition units launch campaigns, targeting the government's agrarian and lease management.", "Both parties agree to a joint liaison committee to resolve model code of conduct disputes quickly.", "The party heads decline to comment on the internal selection process for controversial seats.", {"odishaStabilityMemory": -1}),
    ("2004-03", "Odisha Election Campaign Peaks", "Campaigning peaks in Odisha as Naveen Patnaik highlights anti-corruption and cyclone rehabilitation achievements.", "politics", "The ruling party campaigns on its four-year developmental record and IT-boom achievements.", "Opposition leaders focus on rural unemployment and criticize the state's economic policies.", "Both parties agree to limit loudspeaker usage during late hours to prevent disturbing students during exams.", "The state election coordinators decline to comment on reports of internal candidate disputes.", {"odishaStabilityMemory": -1}),
    ("2004-04", "Voting Held in Odisha Seats", "Voting is held in phases for Odisha's assembly and Lok Sabha seats, with high voter turnouts in rural zones.", "politics", "The state administration coordinates logistics and deploys home guards to assist central security forces during voting.", "Opposition parties watch voting closely, raising concerns over alleged local administration bias in rural booths.", "All parties issue a joint statement appreciating the peaceful conduct of elections in rural zones.", "The state election commissioner declines to comment on the final voter turnout figures in the first day.", {"odishaStabilityMemory": -1}),
    ("2004-05", "BJD-BJP Victory; Patnaik Sworn in as CM", "Naveen Patnaik leads BJD-BJP alliance to victory and is sworn in as Chief Minister of Odisha for a second term.", "politics", "The CM Naveen Patnaik promises a balanced governance model prioritizing rural reform and mining infrastructure.", "Opposition Congress leaders claim the win was achieved through government machinery and resource mobilization.", "The assembly passes a resolution welcoming the new government and promising floor debate order.", "The Governor's office declines to issue a public statement on the cabinet appointments.", {"odishaStabilityMemory": 2}),
    ("2004-06", "Farmers Protest Water Tariff Hikes", "Farm unions launch fresh agitations in Sambalpur, protesting against proposed hikes in canal water tariffs.", "rural", "The Water Department suspends tariff hikes in Sambalpur and schedules local billing review camps.", "Opposition leaders join the Sambalpur agitations, demanding a complete rollback of water tariffs.", "A joint panel of water officials and farmer representatives is formed to negotiate Sambalpur billing slabs.", "The Water Minister declines to release the official revenue impact from the water tariff adjustments.", {"odishaRuralTrustMemory": -1}),
    ("2004-07", "Mining Royalty Distribution Debate", "Inter-state mining royalty debates peak after central tariff adjustments, sparking arguments in Bhubaneswar.", "governance", "The government files a petition in the Supreme Court seeking review of central mining royalty distributions.", "Opposition leaders demand that the government ignore the royalty stay and stop all lease processing.", "A joint committee of legal experts and legislators is formed to study constitutional mining options.", "The Mining Department declines to comment on lease guidelines currently suspended.", {"odishaRuralTrustMemory": -1}),
    ("2004-08", "Jagatsinghpur Canal Desiltation", "The government launches a canal desiltation scheme in Jagatsinghpur to improve water flows to coastal farms.", "infrastructure", "The Agriculture Department launches camps in Jagatsinghpur to distribute subsidized seeds and fertilizers.", "Opposition leaders claim the desiltation scheme is a mere paper announcement before local body polls.", "A joint committee of water officials and cooperative heads is formed to monitor canal silt prices.", "The Jagatsinghpur District Collector declines to share the taluka-wise budget allocations for the water works.", {"odishaStabilityMemory": 1}),
    ("2004-09", "Khurda Industrial Land Acquisition Protests", "Farmers near Khurda block highways, protesting against land acquisition for industrial estate extensions.", "rural", "The land acquisition officer sets up a verification cell to review compensation claims and job listings in Khurda.", "Opposition leaders join the protests, demanding that the land acquisition process be suspended in Khurda.", "A joint committee of land officials and local panchayat chiefs is formed to verify the value of the acquired plots.", "The District Collector declines to release the total acreage of land scheduled for acquisition in Khurda.", {"odishaRuralTrustMemory": 1}),
    ("2004-10", "Dengue Outbreak in Balasore", "Local clinics in Balasore report a spike in dengue cases, testing municipal mosquito control and hospital capacity.", "rural", "The Health Department deploys mobile medical camps and sends emergency drug consignments to Balasore.", "Opposition leaders visit the affected blocks, accusing the government of ignoring primary health centers.", "A joint legislative-medical panel is formed to review municipal healthcare infrastructure and drug supply chains.", "The Health Directorate declines to release the official casualty figures from the Balasore outbreak.", {"odishaRuralTrustMemory": -1}),
    ("2004-11", "Patnaik Announces Crop Insurance Packages", "CM Patnaik announces crop insurance subsidies for pulses and paddy farmers to ease rural economic distress.", "rural", "The Agriculture Department sets up emergency cells to distribute the insurance subsidies to cooperative societies.", "Opposition leaders claim the subsidies are delayed and fail to cover small pulses cultivators.", "A joint committee is formed to negotiate central drought relief matches and coordinate allocations.", "The Cooperative Registrar declines to comment on the number of farmers currently registered for subsidies.", {"odishaRuralTrustMemory": 2}),
    ("2004-12", "Odisha Local Body Election Dates Announced", "The Election Commission announces municipal body elections for February 2005, initiating campaigns.", "politics", "The ruling party focuses on finalizing its candidate list and preparing its election manifesto.", "Opposition units launch campaigns, targeting the government's agrarian and lease management.", "Both parties agree to a joint liaison committee to resolve model code of conduct disputes quickly.", "The party heads decline to comment on the internal selection process for controversial seats.", {"odishaStabilityMemory": 1}),

    # 2005
    ("2005-01", "Tsunami Relief Operations in Kendrapara", "Odisha government coordinates relief packages and dispatches medical teams to tsunami-hit coastal zones.", "governance", "The state administration coordinates the relief funds and dispatches rehabilitation materials to coastal blocks.", "Opposition leaders claim that local dryland welfare funds are being diverted for external political gains.", "Both parties agree to a joint resolution appreciating the humanitarian gesture of the state.", "The state relief director declines to release the itemized transit costs of the tsunami aid cargo.", {"odishaStabilityMemory": 1}),
    ("2005-02", "Municipal Elections Voting Held", "Voting is held for municipal corporations, with the ruling BJD retaining major councils like Bhubaneswar.", "politics", "The state administration coordinates logistics and deploys home guards to assist central security forces during voting.", "Opposition parties watch voting closely, raising concerns over alleged local administration bias in rural booths.", "All parties issue a joint statement appreciating the peaceful conduct of elections in rural zones.", "The state election commissioner declines to comment on the final voter turnout figures in the first day.", {"odishaStabilityMemory": 1}),
    ("2005-03", "VAT Implementation in Cuttack", "Value Added Tax (VAT) implementation triggers trader strikes and shop closures across Cuttack.", "protest", "The CM initiates negotiations with trader leaders and offers a simplified filing process.", "Opposition BJP leaders support the traders, demanding a rollback of the VAT system.", "A joint government-trader advisory panel is formed to review specific tax slabs and address issues.", "The Excise Department declines to comment on the number of businesses currently complying with VAT registration.", {"odishaStabilityMemory": -1}),
    ("2005-04", "Sambalpur Drinking Water Scarcity", "An intense summer heatwave dries up canals, forcing drinking water rationing in Sambalpur wards.", "infrastructure", "The Public Health Engineering Department releases emergency funds to deploy water tankers and drill borewells.", "Opposition leaders lead protests outside PHE offices, accusing the BJD government of failing to prepare.", "A joint water task force is formed to manage daily supply allocations to the worst-affected blocks.", "The Public Health Engineering Minister declines to give a timeline for restoring piped water supply.", {"odishaRuralTrustMemory": -1}),
    ("2005-05", "Kalinga Nagar Infrastructure Allocation", "The government announces upgrades for Kalinganagar industrial zone, drawing tribal protests.", "infrastructure", "The Urban Development Department fast-tracks the industrial park tender allocations and coordinates clearances.", "Opposition leaders call the infrastructure focus a waste of public funds that ignores tribal farming.", "A joint committee of civic officials and local leaders is formed to monitor industrial construction quality.", "The Jajpur Development Commissioner declines to comment on the project-wise budget allocation details.", {"odishaStabilityMemory": 1}),
    ("2005-06", "POSCO Steel Project MOU Signed", "Odisha government signs a historic MOU with South Korean steel major POSCO, drawing intense local protests.", "economy", "The government defends the POSCO MOU as a step to draw global steel investments and create local jobs.", "Opposition Congress leaders claim the POSCO deal concessions compromise state minerals.", "A joint committee of POSCO officials, farmer representatives, and legislators is formed to monitor land acquisition.", "The Mining Minister declines to share the estimated mineral concessions granted under the POSCO MOU.", {"odishaStabilityMemory": -1}),
    ("2005-07", "Kalinga Nagar Land Acquisition Clash", "Police clash with tribal protesters opposing land acquisition in Kalinganagar, raising security concerns.", "security_crisis", "The Home Department coordinates safety negotiations and deploys additional security forces to Kalinganagar.", "Opposition leaders support the tribal protesters, demanding a judicial probe into Jajpur police actions.", "A joint legislative-tribal panel is formed to review industrial safety and land guidelines in Jajpur.", "The DGP office declines to comment on the specific weapons used during the Jajpur Kalinganagar clash.", {"odishaSecurityMemory": -1}),
    ("2005-08", "Mahanadi Basin Flash Floods in Cuttack", "Continuous heavy rains cause the Mahanadi river to rise, inundating agricultural land and damaging paddy in Cuttack.", "rural", "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations in Cuttack.", "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages.", "A joint legislative relief committee is established to supervise rehabilitation work specifically in Cuttack.", "The district collector declines to release the official crop loss estimates in Cuttack.", {"odishaStabilityMemory": -1}),
    ("2005-09", "Financial Irregularities in Cooperative Bank", "Audit checks uncover major irregularities and credit extensions in Odisha's cooperative bank blocks.", "corruption", "The Cooperative Department suspends the boards of the irregular bank branches and orders a forensic audit.", "Opposition leaders demand a judicial probe and stage protests outside bank head offices.", "A multi-party legislative subcommittee is formed to draft credit guidelines for cooperative institutions.", "The Cooperative Minister declines to comment on the total volume of frozen farmer deposits.", {"odishaCorruptionMemory": 1}),
    ("2005-10", "Janata Darbar Program Launch", "CM Naveen Patnaik launches a 'Janata Darbar' outreach program, setting up block-level camps to address complaints.", "governance", "The government releases special budgetary allocations to launch the Janata Darbar camps across all blocks.", "Opposition leaders call the program a rebranding of old schemes and demand clear project timelines.", "A joint government-expert advisory board is formed to track the implementation of the Janata Darbar targets.", "The CM's office declines to publish the project-wise funding breakdown for the outreach program.", {"odishaStabilityMemory": 1}),
    ("2005-11", "Gopalpur Port Land Dispute", "Gopalpur farmers hold demonstrations protesting against land acquisition for private port expansions.", "rural", "The land acquisition officer sets up a verification cell to review compensation claims in Gopalpur.", "Opposition leaders join the protests, demanding that the land acquisition process be suspended in Gopalpur.", "A joint committee of land officials and local panchayat chiefs is formed to verify the value of the acquired plots.", "The District Collector declines to release the total acreage of land scheduled for acquisition.", {"odishaRuralTrustMemory": 1}),
    ("2005-12", "By-Election Results", "By-elections for vacant assembly seats show a strong BJD hold, with the ruling party winning seats.", "politics", "The government welcomes the mandate and vows to focus on rural developmental initiatives.", "Opposition leaders claim their win shows strong public rejection of the government's policies.", "Both parties agree to cooperate on rural road project monitoring committees in the constituencies.", "The State Election Commissioner declines to comment on requests to review voting counts in disputed by-election booths.", {"odishaStabilityMemory": 1})
]

for m, t, desc, cat, gov, opp, jnt, ncm, mem in odisha_events:
    nk = f"{short_code}_{m.replace('-', '_')}_event"
    # Create unique slug for each month to be interpolated in the reaction generator
    slug = f"od_{m.replace('-', '_')}"
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
            mem, {"odishaStabilityMemory": -1}, {"odishaStabilityMemory": -1},
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
    "sourceNotes": "Odisha: Naveen Patnaik CM (2001-2005). Main issues: post-super cyclone recovery, mining and industrial lease allocations, POSCO steel plant MOU, Kalinganagar land dispute clashes, Mahanadi basin flood management. Built programmatically matching the schema and calibration constraints.",
    "defaults": {
        "weights": {
            "baseSelectionWeight": 1.0,
            "reactionProfile": "default"
        }
    },
    "newsItems": news_items
}

output_path = Path("seed-data/review/odisha_2001_news.json")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(json.dumps(data, indent=2))
print("Successfully generated odisha_2001_news.json with", len(news_items), "news items!")
