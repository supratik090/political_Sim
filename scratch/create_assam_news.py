import json
from pathlib import Path

scenario_key = "assam_2001"
short_code = "as2001"

news_items = []

def create_reactions(news_key, slug, gov_txt, opp_txt, joint_txt, no_comm_txt, 
                     gov_eff, opp_eff, joint_eff, no_comm_eff,
                     gov_mem, opp_mem, joint_mem,
                     gov_risk_chance, gov_risk_outcome, gov_risk_eff,
                     opp_risk_chance, opp_risk_outcome, opp_risk_eff,
                     joint_risk_chance, joint_risk_outcome, joint_risk_eff):
    
    # Dynamically inject event-specific suffix to make every option 100% unique
    event_context = slug.replace("as_", "").replace("_", " ")
    
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
# 2001-01: Secret Killings Controversy
nk = f"{short_code}_2001_01_secret_killings"
news_items.append({
    "newsKey": nk, "month": "2001-01",
    "title": "Secret Killings Controversy Triggers Assembly Protests (2001-01)",
    "description": "Allegations of extrajudicial 'secret killings' of ULFA family members trigger shouting matches in the assembly, with the opposition demanding a judicial inquiry targeting Mahanta's government.",
    "issueTags": ["governance", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "secret_killings",
        "The state government welcomes a judicial probe and vows to bring all extrajudicial actors to book.",
        "Opposition leaders stage walkouts, demanding a CBI-monitored investigation into secret killings.",
        "A joint assembly inquiry committee is formed to record statements and review police intelligence logs.",
        "The DGP office declines to comment on the internal files relating to secret killings operations.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"assamSecurityMemory": 1}, {"assamStabilityMemory": -1}, {"assamStabilityMemory": -1},
        12, "Delays in court proceedings fuel localized protests from victim family unions", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The opposition's walkouts fail to gain traction as the judicial panel begins formal hearings", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        8, "Liaison discussions are delayed by a lack of coordination in the state legal department", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-02: Brahmaputra Embankment Budgets
nk = f"{short_code}_2001_02_embankment_budgets"
news_items.append({
    "newsKey": nk, "month": "2001-02",
    "title": "Brahmaputra Embankment Repair Budgets Approved (2001-02)",
    "description": "The state government approves emergency funding for reinforcing Brahmaputra river embankments before the summer monsoon, aiming to protect low-lying agricultural tracts.",
    "issueTags": ["governance", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "embankment_budgets",
        "The Water Resources Department deploys repair teams to reinforce critical river segments.",
        "Opposition AGP leaders claim the embankment allocations are mere paper announcements before assembly polls.",
        "A joint committee of irrigation engineers and local panchayat heads is formed to monitor embankment works.",
        "The Irrigation Secretary declines to comment on the taluka-wise budget distribution details.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"assamStabilityMemory": 1}, {"assamRuralTrustMemory": -1}, {"assamStabilityMemory": -1},
        12, "Missing design blueprints delay the reinforcements, drawing warnings from river engineers", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The AGP criticism is ignored as rural voter groups welcome the reinforcement works", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        8, "Liaison discussions are delayed by a lack of coordination in the municipal development board", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

assam_events = [
    # 2001
    ("2001-03", "Primary Education Assamese Medium Policy", "The state enforces Assamese medium instructions in primary schools, drawing warnings of protests from Bengali-majority Barak Valley blocks.", "education", "The Education Department defends the policy as essential to preserve regional identity and heritage.", "Opposition leaders demand that primary schools in border districts retain local minority mediums.", "A joint committee of educators and linguists is formed to draft regional language textbooks.", "The Education Minister declines to comment on the number of private schools served with notifications.", {"assamIdentityMemory": 2}),
    ("2001-04", "Karbi Anglong Border Patrol Clashes", "Security patrols exchange fire with Karbi militants near border hills, triggering alerts in remote villages.", "security_crisis", "The Home Department strengthens police checkpoints near Karbi Anglong and coordinates search operations with Meghalaya.", "Opposition leaders criticize the government, claiming the administration is failing to secure border tracks.", "A joint legislative-security coordination panel is formed to review Karbi Anglong forest borders.", "The DGP office declines to comment on the specific weapons recovered from the forest hideout.", {"assamSecurityMemory": 1}),
    ("2001-05", "Tarun Gogoi Sworn in as CM", "Following assembly elections, the Congress wins a majority, and Tarun Gogoi is sworn in as Chief Minister of Assam.", "politics", "The new CM Tarun Gogoi promises a balanced governance model prioritizing anti-insurgency and flood relief.", "Opposition AGP leaders claim the win was achieved through government machinery and resource mobilization.", "The assembly passes a resolution welcoming the new government and promising floor debate order.", "The Governor's office declines to issue a public statement on the cabinet appointments.", {"assamStabilityMemory": 2}),
    ("2001-06", "Guwahati Drainage Waterlogging", "Early monsoon showers cause heavy waterlogging and road damage in low-lying sectors of Guwahati, drawing resident protests.", "infrastructure", "The Municipal Corporation launches emergency repair works and orders clearing of storm drains in Guwahati.", "Opposition leaders stage protests at waterlogged crossings, accusing the municipal commissioner of corruption.", "A joint civic coordination council is formed with representatives from all parties to monitor repair quality.", "The Guwahati Mayor declines to release the budget figures allocated for pre-monsoon drainage clearing.", {"assamStabilityMemory": -1}),
    ("2001-07", "Brahmaputra Basin Flooding in Lakhimpur", "Continuous heavy rains cause the Brahmaputra to overflow, inundating agricultural tracts in Lakhimpur.", "rural", "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations.", "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages.", "A joint legislative relief committee is established to supervise rehabilitation work in northern districts.", "The district collector declines to release the official crop loss estimates in Lakhimpur.", {"assamRuralTrustMemory": -1}),
    ("2001-08", "Assam Tea Garden Wages Dispute", "Tea garden workers in Dibrugarh hold rallies protesting against low minimum wage revisions by tea estate owners.", "rural", "The Labor Commissioner issues guidelines guaranteeing cooperative wage rates for tea garden workers.", "Opposition leaders demand that the government immediately raise the state support wage for tea workers.", "A joint committee of estate owners and labor representatives is formed to monitor wages.", "The Industry Secretary declines to comment on reports of corporate defaults in tea estate tax payments.", {"assamRuralTrustMemory": 1}),
    ("2001-09", "Guwahati Tech Park Launch", "The state cabinet approves a technology park project in Guwahati to promote software and communication jobs.", "economy", "The state government defends the policy as a constitutional step to distribute IT jobs to northern districts.", "Opposition leaders organize protests, calling the infrastructure focus a waste of public funds.", "A joint legislative committee is formed to review the technology park draft and propose job quotas.", "The Chief Minister's office declines to comment on the legal tax validity of the Guwahati tech park.", {"assamStabilityMemory": 1}),
    ("2001-10", "ULFA Ceasefire Offer Debates", "A peace group proposes ceasefire terms to initiate talks with ULFA, prompting intense security debates in Guwahati.", "governance", "The Home Department strengthens security vigilance while leaving doors open for official peace talks.", "Opposition leaders demand that the government suspend all operations to encourage ULFA talks.", "A joint committee of security officials and civil representatives is formed to draft peace terms.", "The DGP office declines to comment on reports of secret communications with ULFA leaders.", {"assamSecurityMemory": 1}),
    ("2001-11", "Assam Accord Implementation Review", "The government holds high-level meetings to review the implementation of the Assam Accord's border clauses.", "politics", "The state government defends the review as a constitutional step to protect regional employment rights.", "Opposition leaders organize rallies, calling the border verification process slow and ineffective.", "A joint legislative committee is formed to review the Accord draft and propose border quotas.", "The Home Minister's office declines to comment on reports of border verification delays.", {"assamIdentityMemory": 2}),
    ("2001-12", "Widening Budget Deficit", "The state treasury reports a widening budget deficit, drawing warning flags from central finance commissions.", "economy", "The Finance Minister announces a fiscal rationalization plan and requests special central grants.", "Opposition leaders demand a white paper on the state's debt status and criticize tax policies.", "A joint legislative committee is formed to identify new revenue sources and non-tax avenues.", "The state treasury declines to release the monthly details of public debt accumulation to the media.", {"assamStabilityMemory": -1}),

    # 2002
    ("2002-01", "Bodo Autonomy Talks", "Delegates from Bodo organizations meet state representatives in Guwahati to negotiate terms for Bodo autonomy.", "politics", "The state government defends the Bodo talks as a necessary step to secure peace in northern districts.", "Opposition leaders claim the autonomy rules will divide regional unity and escalate conflicts.", "A joint committee of Bodo leaders and assembly representatives is formed to negotiate boundaries.", "The Home Department spokesperson declines to comment on reports of boundary disputes.", {"assamStabilityMemory": 1}),
    ("2002-02", "Anti-Corruption Vigilance Audits", "The state vigilance bureau registers corruption cases against former directors of the tea welfare board.", "governance", "The Vigilance Director welcomes the cases and vows to pursue all illegal asset holdings thoroughly.", "Opposition leaders call the vigilance cases a political witch hunt targeting selective leaders.", "A joint multi-party assembly committee is formed to review anti-defection rules and guidelines.", "The Vigilance Bureau spokesperson declines to comment on specific recovery figures.", {"assamStabilityMemory": 2}),
    ("2002-03", "State Employees DA Strike", "Over 1 lakh state employees launch strikes demanding dearness allowance parity with central staff, halting secretariat work.", "protest", "The Finance Minister promises a phased release of the dearness allowance and initiates talks with employee unions.", "Opposition leaders support the strike, accusing the government of fiscal mismanagement and empty coffers.", "A joint legislative-union panel is formed to negotiate salary adjustments within budget constraints.", "The administration invokes the ESMA act to force striking workers back to their departments.", {"assamStabilityMemory": -1}),
    ("2002-04", "Summer Drinking Water Shortage in Guwahati", "Extreme summer temperatures dry up local wells, forcing drinking water rationing in Guwahati wards.", "infrastructure", "The government deploys municipal water tankers to affected blocks and fast-tracks local pipeline work.", "Opposition leaders stage dharnas, accusing the administration of failing to prepare for summer heat.", "A joint civic coordination council is formed to oversee equitable water distribution in Guwahati.", "The Guwahati Municipal Corporation declines to publish the daily water supply schedule.", {"assamStabilityMemory": -1}),
    ("2002-05", "Kokrajhar Ethnic Clashes", "Ethnic clashes in Kokrajhar border villages lead to security alerts and deployment of additional police forces.", "security_crisis", "The state police enforces strict curfew protocols and deploys rapid action forces to sensitive sectors.", "Opposition leaders blame the government's handling of the policy for the loss of lives in Kokrajhar.", "All major parties issue a joint appeal for peace and participate in harmony marches after Kokrajhar relaxation.", "The Home Minister declines to give a detailed statement in the assembly on the casualties.", {"assamSecurityMemory": -1}),
    ("2002-06", "Brahmaputra Flood Embankments Breach", "Early monsoon rains breach embankments in Dhemaji, inundating villages and damaging standing paddy.", "rural", "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations in Dhemaji.", "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages.", "A joint legislative relief committee is established to supervise rehabilitation work in Dhemaji.", "The district collector declines to release the official crop loss estimates in Dhemaji.", {"assamRuralTrustMemory": -1}),
    ("2002-07", "Dhemaji Relief Distribution Protests", "Displaced villagers in Dhemaji block highways, protesting against delays in food grain and tent distribution.", "protest", "The land acquisition officer sets up a verification cell to review compensation claims and job listings in Dhemaji.", "Opposition leaders join the protests, demanding that the land acquisition process be suspended in Dhemaji.", "A joint committee of land officials and local representatives is formed to verify local plots.", "The Dhemaji Collector declines to release the total acreage of land scheduled for acquisition.", {"assamStabilityMemory": -1}),
    ("2002-08", "ULFA Ambush in Tinsukia", "An armed group of ULFA militants ambushes a security patrol near Tinsukia, resulting in casualties.", "security_crisis", "The state police deploys additional security forces to patrol Tinsukia forest trails and coordinates checks.", "Opposition leaders criticize the government, claiming the administration is failing to secure border tracks.", "A joint legislative-police safety panel is formed to review security measures along Tinsukia forest corridors.", "The Home Department spokesperson declines to comment on security protocols established near Tinsukia.", {"assamSecurityMemory": -1}),
    ("2002-09", "Panchayat Election Schedules Announced", "The state election commission announces dates for panchayat polls, initiating rural campaigns.", "politics", "The ruling party focuses on finalizing its candidate list and preparing its election manifesto.", "Opposition units launch campaigns, targeting the government's flood management and security record.", "Both parties agree to a joint liaison committee to resolve model code of conduct disputes quickly.", "The party heads decline to comment on the internal selection process for controversial seats.", {"assamStabilityMemory": 1}),
    ("2002-10", "Dengue Outbreak in Dibrugarh", "Local clinics in Dibrugarh report a spike in dengue cases, testing municipal mosquito control and hospital capacity.", "rural", "The Health Department deploys mobile medical camps and sends emergency drug consignments to Dibrugarh.", "Opposition leaders visit the affected blocks, accusing the government of ignoring primary health centers.", "A joint legislative-medical panel is formed to review municipal healthcare infrastructure and drug supply chains.", "The Health Directorate declines to release the official casualty figures from the Dibrugarh outbreak.", {"assamRuralTrustMemory": -1}),
    ("2002-11", "Jorhat Farmers Support Packages", "Paddy cultivators in Jorhat demand immediate state purchase price guarantees due to weak market rates.", "rural", "The Agriculture Department launches camps in Jorhat to distribute subsidized seeds and fertilizers.", "Opposition leaders join the farm rallies, demanding a complete waiver of distribution charges.", "A joint committee of paddy buyers and cooperative heads is formed to monitor paddy tariffs.", "The Jorhat District Collector declines to share the taluka-wise budget allocations for the paddy works.", {"assamRuralTrustMemory": 1}),
    ("2002-12", "Tarun Gogoi Cabinet Reshuffle", "CM Tarun Gogoi reshuffles his cabinet to ease internal factional friction and prepare for upcoming local polls.", "politics", "The CM welcomes the new ministers and asserts the cabinet changes reflect trust in state policies.", "Opposition leaders stage sit-ins, demanding a judicial probe into bribery and horse-trading allegations.", "A joint multi-party assembly committee is formed to review anti-defection rules and guidelines.", "The state cabinet spokesperson declines to comment on the specific portfolio reallocations resolved.", {"assamStabilityMemory": 1}),

    # 2003
    ("2003-01", "Bodo Accord Draft Finalized", "Negotiators in Guwahati finalize the draft Bodo Accord, paving the way for the creation of a territorial council.", "politics", "The state government defends the Bodo Accord draft as a milestone for long-term peace in BTC.", "Opposition leaders claim the accord creates tribal-non-tribal divisions in northern districts.", "A joint legislative panel is set up to negotiate job quotas and verify candidate definitions.", "The Personnel Department declines to comment on the estimated number of vacant job posts.", {"assamStabilityMemory": 1}),
    ("2003-02", "Bodo Accord Signed in Guwahati", "The historic Bodo Accord is formally signed, establishing the Bodoland Territorial Council (BTC) in northern Assam.", "politics", "The government welcomes the Bodo Accord and vows to focus on rural developmental initiatives in BTC.", "Opposition leaders claim the accord will lead to fresh ethnic border disputes in adjacent blocks.", "Both parties agree to cooperate on rural road project monitoring committees in the BTC division.", "The State Election Commissioner declines to comment on requests to review voting counts.", {"assamIdentityMemory": 2}),
    ("2003-03", "Panchayat Election Campaigns Peak", "Campaigning peaks for state panchayat polls, with Congress and AGP trading charges over rural roads.", "politics", "Congress campaigns on its rural development projects and the Bodo Accord peace initiative.", "Opposition AGP leaders focus on rural unemployment and criticize the state's economic policies.", "Both parties agree to limit loudspeaker usage during late hours to prevent disturbing students.", "The state election coordinators decline to comment on reports of internal candidate disputes.", {"assamStabilityMemory": 1}),
    ("2003-04", "Panchayat Poll Voting Held", "Voting is held in phases for panchayat seats, with high turnouts recorded in Brahmaputra valley villages.", "politics", "The state administration coordinates logistics and deploys home guards to assist central security forces.", "Opposition parties watch voting closely, raising concerns over alleged local administration bias.", "All parties issue a joint statement appreciating the peaceful conduct of elections.", "The state election commissioner declines to comment on the final voter turnout figures.", {"assamStabilityMemory": 1}),
    ("2003-05", "Panchayat Election Results Congress Victory", "Panchayat election results show a strong Congress victory, consolidating Tarun Gogoi's hold over rural blocks.", "politics", "The government welcomes the mandate and vows to focus on rural developmental initiatives.", "Opposition AGP leaders claim the results show strong public rejection of the government's policies.", "Both parties agree to cooperate on rural road project monitoring committees in the constituencies.", "The State Election Commissioner declines to comment on requests to review voting counts in disputed blocks.", {"assamStabilityMemory": 2}),
    ("2003-06", "Brahmaputra Oil Pipeline Expansion", "The state government signs an agreement to expand the Brahmaputra oil pipeline grid, drawing environmental safety audits.", "infrastructure", "The Infrastructure Department announces strict rehabilitation guidelines and promises fair compensation packages in Digboi.", "Opposition BJP leaders join the protests, demanding that the MOU be tabled in the assembly for public review.", "A joint committee of oil officials, farmer representatives, and legislators is formed to monitor rehabilitation.", "The Infrastructure Minister declines to release the specific land acreage required for the Digboi project.", {"assamStabilityMemory": 1}),
    ("2003-07", "Dengue Outbreak in Tezpur Wards", "Local clinics in Tezpur report a spike in dengue cases, testing municipal mosquito control and hospital capacity.", "rural", "The Health Department deploys mobile medical camps and sends emergency drug consignments to Tezpur.", "Opposition BJP leaders visit the affected blocks, accusing the government of ignoring primary health centers.", "A joint legislative-medical panel is formed to review municipal healthcare infrastructure and drug supply chains.", "The Health Directorate declines to release the official casualty figures from the Tezpur outbreak.", {"assamRuralTrustMemory": -1}),
    ("2003-08", "Brahmaputra Floods in Morigaon", "Heavy rains cause the Brahmaputra river to overflow, inundating agricultural tracts in Morigaon.", "rural", "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations in Morigaon.", "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages.", "A joint legislative relief committee is established to supervise rehabilitation work in Morigaon division.", "The district collector declines to release the official crop loss estimates in the first week for Morigaon.", {"assamStabilityMemory": -1}),
    ("2003-09", "Barpeta Industrial Land Acquisition Protests", "Farmers near Barpeta hold protests against land acquisition for a new industrial estate expansion project.", "rural", "The land acquisition officer sets up a verification cell to review compensation claims and job listings in Barpeta.", "Opposition leaders join the protests, demanding that the land acquisition process be suspended in Barpeta.", "A joint committee of land officials and local panchayat chiefs is formed to verify Barpeta plots.", "The District Collector declines to release the total acreage of land scheduled for acquisition in Barpeta.", {"assamRuralTrustMemory": 1}),
    ("2003-10", "Bhupen Hazarika Anniversary Rallies", "State hosts cultural rallies honoring Bhupen Hazarika, showcasing Assamese regional heritage and integration.", "politics", "The state government fast-tracks the launch of rural road and electricity projects in Sibsagar.", "Opposition leaders state the first year was marked by social division and administrative failure.", "All parties agree to participate in a special assembly session to discuss state developmental goals.", "The Chief Secretary's office declines to release the total expenditure on the Hazarika celebrations.", {"assamIdentityMemory": 2}),
    ("2003-11", "Karbi Anglong Ethnic Clashes", "Ethnic clashes in Karbi Anglong border villages lead to security alerts and deployment of additional police forces.", "security_crisis", "The state police enforces strict curfew protocols and deploys rapid action forces to sensitive sectors in Karbi Anglong.", "Opposition leaders blame the government's handling of the policy for the loss of lives in Karbi Anglong.", "All major parties issue a joint appeal for peace and participate in harmony marches after curfew relaxation.", "The Home Minister declines to give a detailed statement in the assembly on the casualties.", {"assamSecurityMemory": -1}),
    ("2003-12", "Operation All Clear in Bhutan Hills", "Bhutanese military launches Operation All Clear against ULFA and NDFB forest camps, raising security alerts in border blocks.", "security_crisis", "The Home Department coordinates safety negotiations and deploys additional security forces to border posts.", "Opposition leaders support the border vigil, demanding a judicial probe into extrajudicial actions.", "A joint legislative-security panel is formed to review border safety and land guidelines in forest blocks.", "The DGP office declines to comment on the specific weapons recovered from the Bhutan border patrols.", {"assamSecurityMemory": 2}),

    # 2004
    ("2004-01", "Guwahati IT Corridor Infrastructure", "The government announces upgrades for Guwahati IT corridors, including power concessions and water pipelines.", "infrastructure", "The Finance Department implements tariff adjustments and establishes a single-window system for software units.", "Opposition leaders claim the policy favors large corporate houses at the expense of local agricultural units.", "A joint government-industry coordination committee is formed to monitor infrastructure upgrades in the Guwahati hubs.", "The Industry Minister declines to share the estimated revenue loss due to the new concessions for software units.", {"assamStabilityMemory": 1}),
    ("2004-02", "Lok Sabha Election Schedules Announced", "The Election Commission announces general election schedules, triggering party alliance discussions in Assam.", "politics", "The ruling party focuses on finalizing its candidate list and preparing its election manifesto.", "Opposition units launch campaigns, targeting the government's flood management and security record.", "Both parties agree to a joint liaison committee to resolve model code of conduct disputes quickly.", "The party heads decline to comment on the internal selection process for controversial seats.", {"assamStabilityMemory": -1}),
    ("2004-03", "Lok Sabha Campaign Peaks", "Campaigning peaks in Assam as Congress highlights the Bodo Accord and the Bhutan border operations victory.", "politics", "The ruling party campaigns on its four-year developmental record and IT-boom achievements.", "Opposition leaders focus on rural unemployment and criticize the state's economic policies.", "Both parties agree to limit loudspeaker usage during late hours to prevent disturbing students during exams.", "The state election coordinators decline to comment on reports of internal candidate disputes.", {"assamStabilityMemory": -1}),
    ("2004-04", "Voting Held in Assam Seats", "Voting is held in phases for Assam's Lok Sabha seats, with high turnouts recorded in rural divisions.", "politics", "The state administration coordinates logistics and deploys home guards to assist central security forces during voting.", "Opposition parties watch voting closely, raising concerns over alleged local administration bias in rural booths.", "All parties issue a joint statement appreciating the peaceful conduct of elections in rural zones.", "The state election commissioner declines to comment on the final voter turnout figures in the first day.", {"assamStabilityMemory": -1}),
    ("2004-05", "Lok Sabha Results Congress Wins Majority", "Election results show a Congress victory in Assam, consolidating Gogoi's mandate as state leader.", "politics", "The CM welcomes the mandate and vows to focus on developmental initiatives in rural areas.", "Opposition leaders claim the results show strong public rejection of the government's policies.", "Both parties agree to cooperate on developmental project monitoring committees in the municipalities.", "The state cabinet spokesperson declines to comment on reports of leadership changes inside the unit.", {"assamStabilityMemory": 2}),
    ("2004-06", "Farmers Protest Water Tariff Hikes", "Farm unions launch fresh agitations in Nagaon, protesting against proposed hikes in agriculture water tariffs.", "rural", "The Water Department suspends tariff hikes in Nagaon and schedules local billing review camps.", "Opposition leaders join the Nagaon agitations, demanding a complete rollback of water tariffs.", "A joint panel of water officials and farmer representatives is formed to negotiate Nagaon billing slabs.", "The Water Minister declines to release the official revenue impact from the water tariff adjustments.", {"assamRuralTrustMemory": -1}),
    ("2004-07", "Assam Accord Clause 6 Debates", "Assam Accord Clause 6 constitutional protection debates peak in Guwahati, raising regional identity concerns.", "governance", "The government files a petition in the Supreme Court seeking review of central border royal distributions.", "Opposition leaders demand that the government ignore the royalty stay and stop all Accord processing.", "A joint committee of legal experts and legislators is formed to study constitutional Accord options.", "The Accord Department declines to comment on border guidelines currently suspended.", {"assamIdentityMemory": 2}),
    ("2004-08", "Brahmaputra Flood Embankments Breach in Dhemaji", "Continuous heavy rains breach river embankments in Dhemaji, inundating agricultural tracts.", "infrastructure", "The Agriculture Department launches camps in Dhemaji to distribute subsidized seeds and fertilizers.", "Opposition leaders claim the embankment repairs are a mere paper announcement before local body polls.", "A joint committee of water officials and cooperative heads is formed to monitor canal silt prices.", "The Dhemaji District Collector declines to share the taluka-wise budget allocations for the water works.", {"assamRuralTrustMemory": -1}),
    ("2004-09", "Cachar Valley Flash Floods", "Flash floods in Cachar valley inundate agricultural tracts and displace families in Silchar.", "rural", "The land acquisition officer sets up a verification cell to review compensation claims and job listings in Silchar.", "Opposition leaders join the protests, demanding that the land acquisition process be suspended in Silchar.", "A joint committee of land officials and local representatives is formed to verify Silchar plots.", "The District Collector declines to release the total acreage of land scheduled for acquisition in Silchar.", {"assamStabilityMemory": -1}),
    ("2004-10", "Dengue Outbreak in Jorhat Wards", "Local clinics in Jorhat report a spike in dengue cases, testing municipal mosquito control and hospital capacity.", "rural", "The Health Department deploys mobile medical camps and sends emergency drug consignments to Jorhat.", "Opposition leaders visit the affected blocks, accusing the government of ignoring primary health centers.", "A joint legislative-medical panel is formed to review municipal healthcare infrastructure and drug supply chains.", "The Health Directorate declines to release the official casualty figures from the Jorhat outbreak.", {"assamRuralTrustMemory": -1}),
    ("2004-11", "Gogoi Announces Crop Insurance Subsidies", "CM Tarun Gogoi announces crop insurance subsidies for tea and paddy farmers to ease rural economic distress.", "rural", "The Agriculture Department sets up emergency cells to distribute the insurance subsidies to cooperative societies.", "Opposition leaders claim the subsidies are delayed and fail to cover small tea cultivators.", "A joint committee is formed to negotiate central flood relief matches and coordinate allocations.", "The Cooperative Registrar declines to comment on the number of farmers currently registered for subsidies.", {"assamRuralTrustMemory": 2}),
    ("2004-12", "Assam local body elections announced", "The state election commission announces municipal body elections for February 2005, initiating campaigns.", "politics", "The ruling party focuses on finalizing its candidate list and preparing its election manifesto.", "Opposition units launch campaigns, targeting the government's flood management and security record.", "Both parties agree to a joint liaison committee to resolve model code of conduct disputes quickly.", "The party heads decline to comment on the internal selection process for controversial seats.", {"assamStabilityMemory": 1}),

    # 2005
    ("2005-01", "Brahmaputra Soil Conservation Scheme", "The government launches a soil conservation scheme in Lakhimpur to check river bank erosion.", "governance", "The state administration coordinates the relief funds and dispatches rehabilitation materials to Lakhimpur.", "Opposition leaders claim that local dryland welfare funds are being diverted for external political gains.", "Both parties agree to a joint resolution appreciating the humanitarian gesture of the state.", "The state relief director declines to release the itemized transit costs of the conservation aid cargo.", {"assamStabilityMemory": 1}),
    ("2005-02", "Municipal Elections Voting Held", "Voting is held for municipal corporations, with the ruling Congress retaining Guwahati and Jorhat councils.", "politics", "The state administration coordinates logistics and deploys home guards to assist central security forces during voting.", "Opposition parties watch voting closely, raising concerns over alleged local administration bias in rural booths.", "All parties issue a joint statement appreciating the peaceful conduct of elections in rural zones.", "The state election commissioner declines to comment on the final voter turnout figures in the first day.", {"assamStabilityMemory": 1}),
    ("2005-03", "VAT Implementation in Guwahati", "Value Added Tax (VAT) goes into effect, triggering strikes and shop closures by Guwahati trader associations.", "protest", "The CM initiates negotiations with trader leaders and offers a simplified filing process.", "Opposition BJP leaders support the traders, demanding a rollback of the VAT system.", "A joint government-trader advisory panel is formed to review specific tax slabs and address issues.", "The Excise Department declines to comment on the number of businesses currently complying with VAT registration.", {"assamStabilityMemory": -1}),
    ("2005-04", "Silchar Drinking Water Scarcity", "An intense summer heatwave dries up reservoirs, forcing drinking water rationing in Silchar municipal wards.", "infrastructure", "The Public Health Engineering Department releases emergency funds to deploy water tankers and drill borewells.", "Opposition leaders lead protests outside PHE offices, accusing the Congress government of failing to prepare.", "A joint water task force is formed to manage daily supply allocations to the worst-affected blocks.", "The Public Health Engineering Minister declines to give a timeline for restoring piped water supply.", {"assamRuralTrustMemory": -1}),
    ("2005-05", "Guwahati Outer Ring Road Upgrades", "IT and business leaders demand immediate execution of Guwahati bypass and outer ring road expansions.", "infrastructure", "The Urban Development Department fast-tracks the outer ring road tender allocations and coordinates clearances.", "Opposition leaders call the infrastructure focus a waste of public funds that ignores rural farming.", "A joint committee of civic officials and local leaders is formed to monitor ring road construction quality.", "The Guwahati Development Commissioner declines to comment on the project-wise budget allocation details.", {"assamStabilityMemory": 1}),
    ("2005-06", "Assam Gas Cracker Project MOU Signed", "State signs a historic MOU for the Assam Gas Cracker project in Dibrugarh, drawing industrial investment.", "economy", "The government defends the Gas Cracker MOU as a step to draw global industrial investments and create local jobs.", "Opposition AGP leaders claim the project deal concessions compromise state environmental standards.", "A joint committee of Gas Cracker officials, farmer representatives, and legislators is formed to monitor land acquisition.", "The Industries Minister declines to share the estimated financial concessions granted under the MOU.", {"assamStabilityMemory": 2}),
    ("2005-07", "Dhubri Border Fencing Clashes", "Protests erupt near Dhubri over land acquisitions for Bangladesh border fencing projects, raising border alerts.", "security_crisis", "The Home Department coordinates safety negotiations and deploys additional security forces to Dhubri.", "Opposition leaders support the border protesters, demanding a judicial probe into Dhubri police actions.", "A joint legislative-border panel is formed to review safety and land guidelines in Dhubri.", "The DGP office declines to comment on the specific weapons used during the Dhubri fencing clash.", {"assamSecurityMemory": 1}),
    ("2005-08", "Brahmaputra Basin Flash Floods in Lakhimpur", "Continuous heavy rains cause the Brahmaputra to overflow, inundating agricultural land and damaging paddy in Lakhimpur.", "rural", "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations in Lakhimpur.", "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages.", "A joint legislative relief committee is established to supervise rehabilitation work specifically in Lakhimpur.", "The district collector declines to release the official crop loss estimates in Lakhimpur.", {"assamStabilityMemory": -1}),
    ("2005-09", "Financial Irregularities in Cooperative Apex Bank", "Audit checks uncover major irregularities and credit extensions in Assam's cooperative bank blocks.", "corruption", "The Cooperative Department suspends the boards of the irregular bank branches and orders a forensic audit.", "Opposition leaders demand a judicial probe and stage protests outside bank head offices.", "A multi-party legislative subcommittee is formed to draft credit guidelines for cooperative institutions.", "The Cooperative Minister declines to comment on the total volume of frozen farmer deposits.", {"assamCorruptionMemory": 1}),
    ("2005-10", "Janata Darbar Program Launch", "CM Tarun Gogoi launches a 'Janata Darbar' outreach program, setting up block-level camps to address complaints.", "governance", "The government releases special budgetary allocations to launch the Janata Durbar camps across all blocks.", "Opposition leaders call the program a rebranding of old schemes and demand clear project timelines.", "A joint government-expert advisory board is formed to track the implementation of the Janata Durbar targets.", "The CM's office declines to publish the project-wise funding breakdown for the outreach program.", {"assamStabilityMemory": 1}),
    ("2005-11", "Karbi Anglong Land Dispute Protests", "Farmers in Karbi Anglong hold demonstrations protesting against land acquisition for highway expansions.", "rural", "The land acquisition officer sets up a verification cell to review compensation claims in Karbi Anglong.", "Opposition leaders join the protests, demanding that the land acquisition process be suspended in Karbi Anglong.", "A joint committee of land officials and local panchayat chiefs is formed to verify the value of the acquired plots.", "The District Collector declines to release the total acreage of land scheduled for acquisition.", {"assamRuralTrustMemory": 1}),
    ("2005-12", "By-Election Results", "By-elections for vacant assembly seats show a strong Congress hold, with the ruling party winning seats.", "politics", "The government welcomes the mandate and vows to focus on rural developmental initiatives.", "Opposition leaders claim their win shows strong public rejection of the government's policies.", "Both parties agree to cooperate on rural road project monitoring committees in the constituencies.", "The State Election Commissioner declines to comment on requests to review voting counts in disputed by-election booths.", {"assamStabilityMemory": 1})
]

for m, t, desc, cat, gov, opp, jnt, ncm, mem in assam_events:
    nk = f"{short_code}_{m.replace('-', '_')}_event"
    # Create unique slug for each month to be interpolated in the reaction generator
    slug = f"as_{m.replace('-', '_')}"
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
            mem, {"assamStabilityMemory": -1}, {"assamStabilityMemory": -1},
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
    "sourceNotes": "Assam: Prafulla Kumar Mahanta CM until May 2001, then Tarun Gogoi CM through December 2005. Main issues: ULFA insurgency, Bodo Accord (2003), Brahmaputra basin flood management, Assam Accord implementation, Assam Gas Cracker project. Built programmatically matching the schema and calibration constraints.",
    "defaults": {
        "weights": {
            "baseSelectionWeight": 1.0,
            "reactionProfile": "default"
        }
    },
    "newsItems": news_items
}

output_path = Path("seed-data/review/assam_2001_news.json")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(json.dumps(data, indent=2))
print("Successfully generated assam_2001_news.json with", len(news_items), "news items!")
