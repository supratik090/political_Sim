import json
from pathlib import Path

scenario_key = "uttaranchal_2001"
short_code = "ua2001"

news_items = []

def create_reactions(news_key, slug, gov_txt, opp_txt, joint_txt, no_comm_txt, 
                     gov_eff, opp_eff, joint_eff, no_comm_eff,
                     gov_mem, opp_mem, joint_mem,
                     gov_risk_chance, gov_risk_outcome, gov_risk_eff,
                     opp_risk_chance, opp_risk_outcome, opp_risk_eff,
                     joint_risk_chance, joint_risk_outcome, joint_risk_eff):
    
    # Dynamically inject event-specific suffix to make every option 100% unique
    event_context = slug.replace("ua_", "").replace("_", " ")
    
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
# 2001-01: Dehradun Capital Controversy
nk = f"{short_code}_2001_01_capital_controversy"
news_items.append({
    "newsKey": nk, "month": "2001-01",
    "title": "Protests Over Gairsain Capital Demands (2001-01)",
    "description": "Statehood activists hold demonstrations in Dehradun, demanding that the permanent capital of the new state be established in Gairsain rather than Dehradun.",
    "issueTags": ["governance", "politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "capital_controversy",
        "The state government defends Dehradun as the temporary administrative setup while studies are conducted.",
        "Opposition Congress leaders support the activists, accusing the BJP of ignoring hill development.",
        "A joint assembly commission is established to evaluate infrastructure requirements in Gairsain.",
        "The Chief Secretary declines to comment on the projected cost of building a capital in Gairsain.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"uttaranchalIdentityMemory": 1}, {"uttaranchalStabilityMemory": -1}, {"uttaranchalStabilityMemory": -1},
        12, "Delays in site surveys spark localized protests from hill activists groups", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The Congress criticism is ignored as the temporary Dehradun office functions smoothly", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        8, "Liaison discussions are delayed by a lack of coordination in the planning commission", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-02: Tehri Dam Project Clearances
nk = f"{short_code}_2001_02_tehri_dam"
news_items.append({
    "newsKey": nk, "month": "2001-02",
    "title": "Tehri Dam Construction Safety Audit Ordered (2001-02)",
    "description": "The state government orders a comprehensive safety and rehabilitation audit for the ongoing Tehri dam project, following environmental warnings of seismic activity in the Bhagirathi valley.",
    "issueTags": ["governance", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "tehri_dam",
        "The Power Department launches special verification camps to monitor rehabilitation files.",
        "Opposition leaders claim the safety audits are mere paper announcements without teeth.",
        "A joint committee of hydel engineers and local representatives is formed to monitor Tehri safety.",
        "The Tehri Project Director declines to comment on specific seismic study metrics.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"uttaranchalStabilityMemory": 1}, {"uttaranchalRuralTrustMemory": -1}, {"uttaranchalStabilityMemory": -1},
        12, "Missing land records delay rehabilitation plots, drawing protests from Tehri displaced groups", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The safety criticism is ignored as grid officials welcome power prospects", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        8, "Liaison discussions are delayed by a lack of coordination in the municipal development board", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

uttaranchal_events = [
    # 2001
    ("2001-03", "Primary School Hill Teacher Quotas", "The state government outlines a draft policy prioritizing local hill candidates for primary teacher postings in remote blocks.", "education", "The Education Department defends local recruitment as essential to reduce teacher absenteeism in remote hills.", "Opposition leaders demand that state recruitments remain open to candidates from plain districts.", "A joint committee of educators and block chiefs is formed to verify candidate qualifications.", "The Education Director declines to comment on the number of vacant teacher posts in hill districts.", {"uttaranchalIdentityMemory": 2}),
    ("2001-04", "Corbett Tiger Reserve Boundary Security", "Security patrols exchange fire with illegal loggers near Corbett boundaries, triggering forest security alerts.", "security_crisis", "The Forest Department strengthens patrol checkpoints near Corbett and coordinates search operations with UP.", "Opposition leaders criticize the government, claiming the administration is failing to secure border tracks.", "A joint legislative-security coordination panel is formed to review Corbett forest borders.", "The Chief Conservator of Forests declines to comment on the specific weapons recovered from loggers.", {"uttaranchalSecurityMemory": 1}),
    ("2001-05", "Haridwar Trader Toll Protests", "Trader associations in Haridwar hold strikes protesting against newly introduced commercial transit tolls.", "protest", "The Excise Department conducts workshops for traders and promises a simplified toll filing process.", "Opposition leaders support the traders, demanding a rollback of the Haridwar transit tolls.", "A joint legislative-trader panel is formed to review toll slabs and address issues.", "The Finance Minister declines to comment on the projected revenue impact of the new tolls.", {"uttaranchalStabilityMemory": -1}),
    ("2001-06", "Dehradun Waterlogging", "Early monsoon showers cause waterlogging and road damage in municipal sectors of Dehradun, drawing complaints.", "infrastructure", "The Municipal Corporation launches emergency repair works and orders clearing of storm drains in Dehradun.", "Opposition leaders stage protests at waterlogged crossings, accusing the municipal commissioner of corruption.", "A joint civic coordination council is formed with representatives from all parties to monitor repair quality.", "The Dehradun Mayor declines to release the budget figures allocated for pre-monsoon drainage clearing.", {"uttaranchalStabilityMemory": -1}),
    ("2001-07", "Farmers Seed Distribution Protests in Udham Singh Nagar", "Farmers in Udham Singh Nagar block highways protesting high prices and delays in seed distribution.", "rural", "The Agriculture Department releases subsidized seed quotas to local cooperative societies in Udham Singh Nagar.", "Opposition leaders join the farm rallies, demanding a complete waiver of seed distribution charges.", "A joint assembly committee is established to audit cooperative seed supply chains.", "The Cooperative Registrar declines to comment on the volume of seeds available in godowns.", {"uttaranchalRuralTrustMemory": 1}),
    ("2001-08", "Nainital Landslide Safety Audits", "Heavy rains trigger landslides near Nainital, prompting demands for audits of hillside commercial construction permits.", "rural", "The Disaster Management cell launches verification camps in Nainital to inspect hillside building permits.", "Opposition leaders demand the immediate suspension of all commercial building permits in Nainital.", "A joint committee of forest officials and local builders is formed to draft safety guidelines.", "The Nainital Collector declines to comment on the number of non-compliant hillside hotels served notices.", {"uttaranchalRuralTrustMemory": 1}),
    ("2001-09", "Char Dham Yatra Highway Projects", "The state government outlines a highway widening project to improve Char Dham yatra connectivity, drawing activist warnings.", "economy", "The state government defends the highway widening as essential to draw global tourism to Char Dham sites.", "Opposition leaders organize protests, calling the widening project a threat to fragile mountain slopes.", "A joint legislative committee is formed to review the highway project draft and propose environment quotas.", "The Tourism Director declines to comment on the estimated value of land concessions granted to contractors.", {"uttaranchalIdentityMemory": 1}),
    ("2001-10", "Koshyari Sworn in as CM", "Nityanand Swami resigns, and Bhagat Singh Koshyari is sworn in as the new Chief Minister of Uttaranchal.", "politics", "The new CM Bhagat Singh Koshyari promises a balanced governance model prioritizing hill roads and clean offices.", "Opposition Congress leaders claim the leadership change reflects internal BJP administrative failure.", "The assembly passes a resolution welcoming the new CM and promising floor debate order.", "The Governor's office declines to issue a public statement on the cabinet reshuffle.", {"uttaranchalStabilityMemory": 1}),
    ("2001-11", "First Statehood Anniversary Rallies", "First statehood anniversary is celebrated, with CM Koshyari highlighting rural road connectivity in Almora.", "politics", "The state government fast-tracks the launch of pending rural road and electricity projects in Almora.", "Opposition leaders state the first year was marked by social division and administrative failure.", "All parties agree to participate in a special assembly session to discuss state developmental goals.", "The Chief Secretary's office declines to release the total expenditure on the statehood celebrations.", {"uttaranchalStabilityMemory": 1}),
    ("2001-12", "Widening Budget Deficit Concerns", "The state treasury reports a widening budget deficit, drawing warning flags from central finance commissions.", "economy", "The Finance Minister announces a fiscal rationalization plan and requests special central grants.", "Opposition leaders demand a white paper on the state's debt status and criticize tax policies.", "A joint legislative committee is formed to identify new revenue sources and non-tax avenues.", "The state treasury declines to release the monthly details of public debt accumulation to the media.", {"uttaranchalStabilityMemory": -1}),

    # 2002
    ("2002-01", "Almora Eco-Tourism Land Leases", "Almora farmers hold demonstrations protesting against eco-tourism land leases granted to private developers.", "governance", "The Tourism Department initiates inspections of Almora resort leases and orders boundary checks.", "Opposition leaders support the farmers, demanding immediate suspension of all private resort leases.", "A joint environment committee of scientists and local representatives is formed to audit leases.", "The Tourism Director declines to release the lease boundary maps for Almora eco-resorts.", {"uttaranchalStabilityMemory": 1}),
    ("2002-02", "First General Assembly Campaigns Peak", "Campaigning peaks for Uttaranchal's first general assembly elections, with Congress targeting the BJP's road record.", "politics", "The ruling BJP focuses on its state-creation record and drafts candidate manifests.", "Opposition Congress units launch campaigns targeting the government's hill road infrastructure delays.", "Both parties agree to a joint liaison committee to resolve model code of conduct disputes quickly.", "The party heads decline to comment on the internal selection process for controversial seats.", {"uttaranchalStabilityMemory": -1}),
    ("2002-03", "Congress Wins; N. D. Tiwari Sworn in as CM", "Election results yield a Congress victory. N. D. Tiwari is sworn in as the first elected CM of the state.", "politics", "The new CM N. D. Tiwari promises a balanced governance model prioritizing industrial growth and hill connectivity.", "Opposition BJP leaders claim the Congress win was achieved through false promises on capital status.", "The assembly passes a resolution welcoming the new government and promising floor debate order.", "The Governor's office declines to issue a public statement on the cabinet appointments.", {"uttaranchalStabilityMemory": 2}),
    ("2002-04", "State Employees Dearness Allowance Strike", "Over 50,000 state employees launch strikes demanding dearness allowance parity with central staff.", "protest", "The Finance Minister promises a phased release of the dearness allowance and initiates talks with employee unions.", "Opposition BJP leaders support the strike, accusing the government of fiscal mismanagement and empty coffers.", "A joint legislative-union panel is formed to negotiate salary adjustments within budget constraints.", "The administration invokes the ESMA act to force striking workers back to their departments.", {"uttaranchalStabilityMemory": -1}),
    ("2002-05", "Tehri Dam Submergence Protests", "Residents of Tehri town hold dharnas protesting against inadequate rehabilitation packages before submergence schedules.", "rural", "The Rehabilitation Department suspends submergence schedules and plans billing review camps in Tehri.", "Opposition leaders join the Tehri protests, demanding a complete rollback of submergence timelines.", "A joint panel of power officials and farmer representatives is formed to negotiate Tehri compensation slabs.", "The Power Minister declines to release the official funding data for Tehri rehabilitation packages.", {"uttaranchalRuralTrustMemory": -1}),
    ("2002-06", "Haridwar Industrial Estate Lands", "The government approves plans for a new industrial estate in Haridwar, drawing displacement warnings from local farmers.", "rural", "The land acquisition officer sets up a verification cell to review compensation claims in Haridwar.", "Opposition leaders join the protests, demanding that the land acquisition process be suspended in Haridwar.", "A joint committee of land officials and local panchayat chiefs is formed to verify the value of the acquired plots.", "The District Collector declines to release the total acreage of land scheduled for acquisition in Haridwar.", {"uttaranchalRuralTrustMemory": 1}),
    ("2002-07", "Dengue Outbreak in Dehradun Slums", "Local clinics in Dehradun report a spike in dengue cases, testing municipal mosquito control and hospital capacity.", "rural", "The Health Department deploys mobile medical camps and sends emergency drug consignments to Dehradun.", "Opposition leaders visit the affected blocks, accusing the government of ignoring primary health centers.", "A joint legislative-medical panel is formed to review municipal healthcare infrastructure and drug supply chains.", "The Health Directorate declines to release the official casualty figures from the Dehradun outbreak.", {"uttaranchalRuralTrustMemory": -1}),
    ("2002-08", "Heavy Monsoon Landslides in Pithoragarh", "Continuous heavy rains trigger landslides in Pithoragarh, block roads and cutting off remote hill villages.", "security_crisis", "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations in Pithoragarh.", "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages.", "A joint legislative relief committee is established to supervise rehabilitation work specifically in Pithoragarh.", "The district collector declines to release the official crop loss estimates in Pithoragarh.", {"uttaranchalStabilityMemory": -1}),
    ("2002-09", "Pantnagar Industrial Zone Infrastructure", "The government announces upgrades for Pantnagar industrial zone, including power concessions and water pipelines.", "infrastructure", "The Finance Department implements tariff adjustments and establishes a single-window system for software units.", "Opposition leaders claim the policy favors large corporate houses at the expense of local agricultural units.", "A joint government-industry coordination committee is formed to monitor infrastructure upgrades in the Pantnagar hubs.", "The Industry Minister declines to share the estimated revenue loss due to the new concessions for software units.", {"uttaranchalStabilityMemory": 1}),
    ("2002-10", "Hill Road Network Upgrades", "The government launches a hill road network upgrade scheme in Almora to improve connectivity to remote hamlets.", "infrastructure", "The Agriculture Department launches camps in Almora to distribute subsidized seeds and fertilizers.", "Opposition leaders claim the road network upgrades are a mere paper announcement before local body polls.", "A joint committee of road officials and cooperative heads is formed to monitor construction prices.", "The Almora District Collector declines to share the taluka-wise budget allocations for the road works.", {"uttaranchalStabilityMemory": 1}),
    ("2002-11", "Haridwar Sugar Mill Tariff Dispute", "Sugarcane cultivators in Haridwar protest against private sugar mills over delayed sugarcane payment dues.", "rural", "The Agriculture Department releases subsidized seed quotas to local cooperative societies in Haridwar.", "Opposition leaders join the farm rallies, demanding a complete waiver of seed distribution charges.", "A joint assembly committee is established to audit cooperative seed supply chains in Haridwar.", "The Cooperative Registrar declines to comment on the volume of seeds available in Haridwar godowns.", {"uttaranchalRuralTrustMemory": 1}),
    ("2002-12", "Tiwari Cabinet Reshuffle", "CM N. D. Tiwari reshuffles his cabinet to ease internal Congress factional friction and prepare for local polls.", "politics", "The CM welcomes the new ministers and asserts the cabinet changes reflect trust in state policies.", "Opposition leaders stage sit-ins, demanding a judicial probe into bribery and horse-trading allegations.", "A joint multi-party assembly committee is formed to review anti-defection rules and guidelines.", "The state cabinet spokesperson declines to comment on the specific portfolio reallocations resolved.", {"uttaranchalStabilityMemory": 1}),

    # 2003
    ("2003-01", "Gairsain Capital Report Tabled", "The committee evaluating permanent capital locations tables its report in the assembly, raising activist reactions.", "politics", "The state government defends the report as a balanced study of regional feasibility and capital requirements.", "Opposition leaders claim the report is a delaying tactic to avoid declaring Gairsain as capital.", "A joint legislative panel is set up to negotiate capital infrastructure plans and verify definitions.", "The Personnel Department declines to comment on the estimated cost of establishing a hill capital.", {"uttaranchalIdentityMemory": 1}),
    ("2003-02", "Cold Wave Damages Mustard Crops", "An intense winter cold wave damages standing mustard crops across Southern plains, prompting relief demands.", "rural", "The Agriculture Department releases emergency relief funds and orders mustard crop damage checks in Haridwar.", "Opposition leaders demand a complete waiver of crop loans for mustard farmers in southern blocks.", "A joint assembly panel is established to evaluate crop damage and coordinate relief with central teams.", "The Irrigation Department declines to specify the daily water distribution schedule in Haridwar.", {"uttaranchalRuralTrustMemory": 1}),
    ("2003-03", "Congress Jan Sampark Yatra", "CM N. D. Tiwari launches a Jan Sampark Yatra to connect with hill voters and showcase highway works.", "politics", "Congress leaders organize block-level meetings to highlight the state's cooperative insurance schemes.", "BJP units organize mass receptions for the yatra, consolidating support in hill constituencies.", "Both parties agree to avoid provocative language during campaign rallies to prevent local tensions.", "The CM's office declines to comment on the turnout and impact of the Congress yatra.", {"uttaranchalStabilityMemory": 1}),
    ("2003-04", "Dehradun IT Park Master Plan", "The state outlines master plan details for a massive technology park in Dehradun, drawing local concerns.", "economy", "The land acquisition officer sets up a verification cell to review compensation claims in Dehradun.", "Opposition leaders join the protests, demanding that the land acquisition process be suspended in Dehradun.", "A joint committee of land officials and local panchayat chiefs is formed to verify the value of the acquired plots.", "The District Collector declines to release the total acreage of land scheduled for acquisition in Dehradun.", {"uttaranchalStabilityMemory": 1}),
    ("2003-05", "Haridwar Trader Toll Strike", "Trader associations in Haridwar hold strikes protesting against the local commercial entry tax implementation.", "protest", "The Excise Department conducts training workshops for traders and promises a simplified filing process.", "Opposition leaders support the traders, demanding a postponement of entry taxes until system readiness is achieved.", "A joint legislative-trader coordination panel is formed to review tax slabs and address grievances.", "The Finance Minister declines to comment on the projected revenue impact of the new tax system.", {"uttaranchalStabilityMemory": -1}),
    ("2003-06", "Rishikesh Hydro Project MOU", "The state government signs an agreement to expand Rishikesh hydro grid capacity, drawing emissions warnings.", "infrastructure", "The Infrastructure Department announces strict rehabilitation guidelines and promises fair compensation packages in Rishikesh.", "Opposition BJP leaders join the protests, demanding that the MOU be tabled in the assembly for public review.", "A joint committee of power officials, farmer representatives, and legislators is formed to monitor rehabilitation.", "The Infrastructure Minister declines to release the specific land acreage required for the Rishikesh project.", {"uttaranchalStabilityMemory": 1}),
    ("2003-07", "Dengue Outbreak in Haridwar Wards", "Local clinics in Haridwar report a spike in dengue cases, testing municipal mosquito control and hospital capacity.", "rural", "The Health Department deploys mobile medical camps and sends emergency drug consignments to Haridwar.", "Opposition BJP leaders visit the affected blocks, accusing the government of ignoring primary health centers.", "A joint legislative-medical panel is formed to review municipal healthcare infrastructure and drug supply chains.", "The Health Directorate declines to release the official casualty figures from the Haridwar outbreak.", {"uttaranchalRuralTrustMemory": -1}),
    ("2003-08", "Almora Cloudburst Relief", "Heavy cloudburst in Almora hills damages properties and blocks highways, prompting emergency relief works.", "rural", "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations in Almora.", "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages.", "A joint legislative relief committee is established to supervise rehabilitation work specifically in Almora.", "The district collector declines to release the official crop loss estimates in Almora.", {"uttaranchalStabilityMemory": -1}),
    ("2003-09", "Chamoli Eco-Zone Land Disputes", "Chamoli farmers hold demonstrations protesting against eco-zone regulations restricting forest timber collection.", "rural", "The land acquisition officer sets up a verification cell to review compensation claims and job listings in Chamoli.", "Opposition leaders join the protests, demanding that the land acquisition process be suspended in Chamoli.", "A joint committee of land officials and local panchayat chiefs is formed to verify Chamoli plots.", "The District Collector declines to release the total acreage of land scheduled for acquisition in Chamoli.", {"uttaranchalRuralTrustMemory": 1}),
    ("2003-10", "Govind Ballabh Pant Anniversary Rallies", "State hosts massive rallies on the birth anniversary of Govind Ballabh Pant, showcasing hill road projects in Nainital.", "politics", "The state government fast-tracks the launch of pending rural road and electricity projects in Nainital.", "Opposition BJP leaders state the first year was marked by social division and administrative failure.", "All parties agree to participate in a special assembly session to discuss state developmental goals.", "The Chief Secretary's office declines to release the total expenditure on the celebrations.", {"uttaranchalIdentityMemory": 2}),
    ("2003-11", "Roorkee Safety Violations", "Roorkee manufacturing factories draw fire over worker safety violations, prompting inspection demands.", "governance", "The Industries Department conducts safety inspections of Roorkee factories and orders safety upgrades.", "Opposition leaders support the workers, demanding immediate suspension of non-compliant factories.", "A joint safety committee of factory inspectors and union representatives is formed to audit safety compliance.", "The Labor Commissioner declines to release the official accident reports for Roorkee factories.", {"uttaranchalStabilityMemory": 1}),
    ("2003-12", "Tiwari Rules Out Early Polls", "CM N. D. Tiwari rules out early dissolution of the assembly, stating the government will complete its term.", "politics", "The government defends the schedule to complete the five-year term and focus on pending projects.", "Opposition leaders claim the government is avoiding polls to delay worker backlash over allowances.", "The assembly passes a resolution thanking the CM for his service and welcoming the developments.", "The CM's office declines to comment on reports of seat-sharing talks with minor regional parties.", {"uttaranchalStabilityMemory": 1}),

    # 2004
    ("2004-01", "Pantnagar SEZ Master Plan Details", "The government announces upgrades for Pantnagar SEZ, including power concessions and water pipelines.", "infrastructure", "The Finance Department implements tariff adjustments and establishes a single-window system for software units.", "Opposition leaders claim the policy favors large corporate houses at the expense of local agricultural units.", "A joint government-industry coordination committee is formed to monitor infrastructure upgrades in the Pantnagar hubs.", "The Industry Minister declines to share the estimated revenue loss due to the new concessions for software units.", {"uttaranchalStabilityMemory": 1}),
    ("2004-02", "Lok Sabha Election Schedules Announced", "The Election Commission announces general election schedules, triggering party alliance discussions in the state.", "politics", "The ruling party focuses on finalizing its candidate list and preparing its election manifesto.", "Opposition units launch campaigns, targeting the government's hill road and infrastructure record.", "Both parties agree to a joint liaison committee to resolve model code of conduct disputes quickly.", "The party heads decline to comment on the internal selection process for controversial seats.", {"uttaranchalStabilityMemory": -1}),
    ("2004-03", "Lok Sabha Campaign Peaks in State", "Campaigning peaks in Uttaranchal as opposition BJP targets Tiwari over hill roads and Pantnagar acquisitions.", "politics", "The ruling party campaigns on its two-year developmental record and Pantnagar's industrial growth.", "Opposition leaders focus on rural unemployment and criticize the state's economic policies.", "Both parties agree to limit loudspeaker usage during late hours to prevent disturbing students during exams.", "The state election coordinators decline to comment on reports of internal candidate disputes.", {"uttaranchalStabilityMemory": -1}),
    ("2004-04", "Voting Held in Hill Constituencies", "Voting is held for Uttaranchal's Lok Sabha seats, with high turnouts recorded in hill divisions.", "politics", "The state administration coordinates logistics and deploys home guards to assist central security forces during voting.", "Opposition parties watch voting closely, raising concerns over alleged local administration bias in rural booths.", "All parties issue a joint statement appreciating the peaceful conduct of elections in rural zones.", "The state election commissioner declines to comment on the final voter turnout figures in the first day.", {"uttaranchalStabilityMemory": -1}),
    ("2004-05", "Lok Sabha Election Results BJP Holds Seats", "Election results show a closely contested layout, with both BJP and Congress winning key Lok Sabha seats.", "politics", "The CM welcomes the mandate and vows to focus on developmental initiatives in rural areas.", "Opposition leaders claim the results show strong public rejection of the government's policies.", "Both parties agree to cooperate on developmental project monitoring committees in the municipalities.", "The state cabinet spokesperson declines to comment on reports of leadership changes inside the unit.", {"uttaranchalStabilityMemory": 2}),
    ("2004-06", "Farmers Protest Haridwar Tariff Hikes", "Farm unions launch fresh agitations in Haridwar, protesting against proposed hikes in agriculture power tariffs.", "rural", "The Power Department suspends tariff hikes in Haridwar and schedules local billing review camps.", "Opposition leaders join the Haridwar agitations, demanding a complete rollback of agricultural tariffs.", "A joint panel of power officials and farmer representatives is formed to negotiate Haridwar billing slabs.", "The Power Minister declines to release the official revenue impact from the agricultural power tariff adjustments.", {"uttaranchalRuralTrustMemory": -1}),
    ("2004-07", "Forest Land Royalty Allocation Disputes", "Inter-state forest royalty debates peak after central policy adjustments, prompting meetings in Dehradun.", "governance", "The government files a petition in the Supreme Court seeking review of central forest royalty distributions.", "Opposition leaders demand that the government ignore the royalty stay and stop all lease processing.", "A joint committee of legal experts and legislators is formed to study constitutional forest options.", "The Forest Department declines to comment on lease guidelines currently suspended.", {"uttaranchalIdentityMemory": 2}),
    ("2004-08", "Roorkee Canal Desiltation", "The government launches a canal desiltation scheme in Roorkee to improve water flows to plains farms.", "infrastructure", "The Agriculture Department launches camps in Roorkee to distribute subsidized seeds and fertilizers.", "Opposition leaders claim the desiltation scheme is a mere paper announcement before local body polls.", "A joint committee of water officials and cooperative heads is formed to monitor canal silt prices.", "The Roorkee District Collector declines to share the taluka-wise budget allocations for the water works.", {"uttaranchalStabilityMemory": 1}),
    ("2004-09", "Udham Singh Nagar Land Acquisition Protests", "Farmers near Udham Singh Nagar block highways, protesting against land acquisition for industrial extensions.", "rural", "The land acquisition officer sets up a verification cell to review compensation claims and job listings in Udham Singh Nagar.", "Opposition leaders join the protests, demanding that the land acquisition process be suspended in Udham Singh Nagar.", "A joint committee of land officials and local panchayat chiefs is formed to verify the value of the acquired plots.", "The District Collector declines to release the total acreage of land scheduled for acquisition in Udham Singh Nagar.", {"uttaranchalRuralTrustMemory": 1}),
    ("2004-10", "Dengue Outbreak in Dehradun Wards", "Municipal wards in Dehradun report a sudden post-monsoon surge in dengue infections, straining local community clinics and drug inventories.", "rural", "The Health Department deploys mobile medical camps and sends emergency drug consignments to Dehradun.", "Opposition leaders visit the affected blocks, accusing the government of ignoring primary health centers.", "A joint legislative-medical panel is formed to review municipal healthcare infrastructure and drug supply chains.", "The Health Directorate declines to release the official casualty figures from the Dehradun outbreak.", {"uttaranchalRuralTrustMemory": -1}),
    ("2004-11", "Tiwari Announces Crop Subsidy Subsidies", "CM Tiwari announces crop insurance subsidies for mustard and wheat farmers to ease rural economic distress.", "rural", "The Agriculture Department sets up emergency cells to distribute the insurance subsidies to cooperative societies.", "Opposition leaders claim the subsidies are delayed and fail to cover small wheat cultivators.", "A joint committee is formed to negotiate central drought relief matches and coordinate allocations.", "The Cooperative Registrar declines to comment on the number of farmers currently registered for subsidies.", {"uttaranchalRuralTrustMemory": 2}),
    ("2004-12", "Uttaranchal Local Body Elections Announced", "The state election commission announces municipal body elections for February 2005, initiating campaigns.", "politics", "The ruling party focuses on finalizing its candidate list and preparing its election manifesto.", "Opposition units launch campaigns, targeting the government's hill road and infrastructure record.", "Both parties agree to a joint liaison committee to resolve model code of conduct disputes quickly.", "The party heads decline to comment on the internal selection process for controversial seats.", {"uttaranchalStabilityMemory": 1}),

    # 2005
    ("2005-01", "Hill Soil Conservation Scheme", "The government launches a soil conservation scheme in Pauri to check landslide road blockages.", "governance", "The state administration coordinates the relief funds and dispatches rehabilitation materials to Pauri.", "Opposition leaders claim that local dryland welfare funds are being diverted for external political gains.", "Both parties agree to a joint resolution appreciating the humanitarian gesture of the state.", "The state relief director declines to release the itemized transit costs of the conservation aid cargo.", {"uttaranchalStabilityMemory": 1}),
    ("2005-02", "Municipal Elections Voting Held", "Voting is held for municipal corporations, with the ruling Congress retaining Dehradun and Haridwar councils.", "politics", "The state administration coordinates logistics and deploys home guards to assist central security forces during voting.", "Opposition parties watch voting closely, raising concerns over alleged local administration bias in rural booths.", "All parties issue a joint statement appreciating the peaceful conduct of elections in rural zones.", "The state election commissioner declines to comment on the final voter turnout figures in the first day.", {"uttaranchalStabilityMemory": 1}),
    ("2005-03", "VAT Implementation in Dehradun", "Value Added Tax (VAT) goes into effect, triggering strikes and shop closures by Dehradun trader associations.", "protest", "The CM initiates negotiations with trader leaders and offers a simplified filing process.", "Opposition BJP leaders support the traders, demanding a rollback of the VAT system.", "A joint government-trader advisory panel is formed to review specific tax slabs and address issues.", "The Excise Department declines to comment on the number of businesses currently complying with VAT registration.", {"uttaranchalStabilityMemory": -1}),
    ("2005-04", "Roorkee Drinking Water Scarcity", "An intense summer heatwave dries up reservoirs, forcing drinking water rationing in Roorkee municipal wards.", "infrastructure", "The Public Health Engineering Department releases emergency funds to deploy water tankers and drill borewells.", "Opposition leaders lead protests outside PHE offices, accusing the Congress government of failing to prepare.", "A joint water task force is formed to manage daily supply allocations to the worst-affected blocks.", "The Public Health Engineering Minister declines to give a timeline for restoring piped water supply.", {"uttaranchalRuralTrustMemory": -1}),
    ("2005-05", "Dehradun Outer Ring Road Upgrades", "Business leaders demand immediate execution of Dehradun bypass and outer ring road expansions.", "infrastructure", "The Urban Development Department fast-tracks the outer ring road tender allocations and coordinates clearances.", "Opposition leaders call the infrastructure focus a waste of public funds that ignores rural farming.", "A joint committee of civic officials and local leaders is formed to monitor ring road construction quality.", "The Dehradun Development Commissioner declines to comment on the project-wise budget allocation details.", {"uttaranchalStabilityMemory": 1}),
    ("2005-06", "Tehri Dam Grid Expansion MOU Signed", "State signs a historic MOU for the Tehri grid line expansion in Rishikesh, drawing industrial power lines.", "economy", "The government defends the Tehri Grid MOU as a step to draw global power investments and create local jobs.", "Opposition BJP leaders claim the project deal concessions compromise state environmental standards.", "A joint committee of Tehri officials, farmer representatives, and legislators is formed to monitor land acquisition.", "The Infrastructure Minister declines to share the estimated financial concessions granted under the MOU.", {"uttaranchalStabilityMemory": 2}),
    ("2005-07", "Koteshwar Dam Land Acquisition Clashes", "Protests erupt near Koteshwar over land acquisitions for new dam projects, raising security alerts.", "security_crisis", "The Home Department coordinates safety negotiations and deploys additional security forces to Koteshwar.", "Opposition leaders support the border protesters, demanding a judicial probe into Koteshwar police actions.", "A joint legislative-border panel is formed to review safety and land guidelines in Koteshwar.", "The DGP office declines to comment on the specific weapons used during the Koteshwar clash.", {"uttaranchalSecurityMemory": 1}),
    ("2005-08", "Pithoragarh Cloudburst Flash Floods", "Continuous heavy rains cause cloudbursts, inundating agricultural land and damaging standing crops in Pithoragarh.", "rural", "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations in Pithoragarh.", "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages.", "A joint legislative relief committee is established to supervise rehabilitation work specifically in Pithoragarh.", "The district collector declines to release the official crop loss estimates in Pithoragarh.", {"uttaranchalStabilityMemory": -1}),
    ("2005-09", "Financial Irregularities in Cooperative Bank", "Audit checks uncover major irregularities and credit extensions in Uttaranchal's cooperative bank blocks.", "corruption", "The Cooperative Department suspends the boards of the irregular bank branches and orders a forensic audit.", "Opposition leaders demand a judicial probe and stage protests outside bank head offices.", "A multi-party legislative subcommittee is formed to draft credit guidelines for cooperative institutions.", "The Cooperative Minister declines to comment on the total volume of frozen farmer deposits.", {"uttaranchalCorruptionMemory": 1}),
    ("2005-10", "Janata Durbar Program Launch", "CM N. D. Tiwari launches a 'Janata Durbar' outreach program, setting up block-level camps to address complaints.", "governance", "The government releases special budgetary allocations to launch the Janata Durbar camps across all blocks.", "Opposition leaders call the program a rebranding of old schemes and demand clear project timelines.", "A joint government-expert advisory board is formed to track the implementation of the Janata Durbar targets.", "The CM's office declines to publish the project-wise funding breakdown for the outreach program.", {"uttaranchalStabilityMemory": 1}),
    ("2005-11", "Rudrapur SEZ Land Dispute", "Rudrapur farmers hold demonstrations protesting against land acquisition for private industrial SEZ expansions.", "rural", "The land acquisition officer sets up a verification cell to review compensation claims in Rudrapur.", "Opposition leaders join the protests, demanding that the land acquisition process be suspended in Rudrapur.", "A joint committee of land officials and local panchayat chiefs is formed to verify the value of the acquired plots.", "The District Collector declines to release the total acreage of land scheduled for acquisition.", {"uttaranchalRuralTrustMemory": 1}),
    ("2005-12", "By-Election Results", "By-elections for vacant assembly seats show a strong Congress hold, with the ruling party winning seats.", "politics", "The government welcomes the mandate and vows to focus on rural developmental initiatives.", "Opposition leaders claim their win shows strong public rejection of the government's policies.", "Both parties agree to cooperate on rural road project monitoring committees in the constituencies.", "The State Election Commissioner declines to comment on requests to review voting counts in disputed by-election booths.", {"uttaranchalStabilityMemory": 1})
]

for m, t, desc, cat, gov, opp, jnt, ncm, mem in uttaranchal_events:
    nk = f"{short_code}_{m.replace('-', '_')}_event"
    # Create unique slug for each month to be interpolated in the reaction generator
    slug = f"ua_{m.replace('-', '_')}"
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
            mem, {"uttaranchalStabilityMemory": -1}, {"uttaranchalStabilityMemory": -1},
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
    "sourceNotes": "Uttaranchal: Nityanand Swami/Bhagat Singh Koshyari CM (2001-2002), then N. D. Tiwari CM through December 2005. Main issues: Gairsain vs Dehradun capital controversy, Tehri dam submergence and safety audits, Char Dham highway projects, Pantnagar industrial expansions, local body elections. Built programmatically matching the schema and calibration constraints.",
    "defaults": {
        "weights": {
            "baseSelectionWeight": 1.0,
            "reactionProfile": "default"
        }
    },
    "newsItems": news_items
}

output_path = Path("seed-data/review/uttaranchal_2001_news.json")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(json.dumps(data, indent=2))
print("Successfully generated uttaranchal_2001_news.json with", len(news_items), "news items!")
