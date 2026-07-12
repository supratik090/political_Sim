import json
from pathlib import Path

# Define the scenario metadata
scenario_key = "karnataka_2001"
short_code = "ka2001"

news_items = []

# Helper to generate reactions
def create_reactions(news_key, slug, gov_txt, opp_txt, joint_txt, no_comm_txt, 
                     gov_eff, opp_eff, joint_eff, no_comm_eff,
                     gov_mem, opp_mem, joint_mem,
                     gov_risk_chance, gov_risk_outcome, gov_risk_eff,
                     opp_risk_chance, opp_risk_outcome, opp_risk_eff,
                     joint_risk_chance, joint_risk_outcome, joint_risk_eff):
    
    return [
        {
            "reactionKey": f"{news_key}__gov_action_{slug}",
            "text": gov_txt,
            "roleAllowed": ["GOVERNMENT"],
            "effects": {"playerParty": gov_eff},
            "hiddenEffects": {"publicMemory": gov_mem},
            "risk": {
                "chance": gov_risk_chance,
                "badOutcome": gov_risk_outcome,
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
                "badOutcome": opp_risk_outcome,
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
                "badOutcome": joint_risk_outcome,
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
# 2001-01: Bangalore IT corridor expansion
nk = f"{short_code}_2001_01_it_expansion"
news_items.append({
    "newsKey": nk, "month": "2001-01",
    "title": "Bangalore IT Corridor Infrastructure Allocation Approved (2001-01)",
    "description": "The S. M. Krishna government approves massive infrastructure allocations and tax concessions for the expansion of the IT corridor in Bangalore. The move solidifies the city's position as India's Silicon Valley.",
    "issueTags": ["governance", "economy"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "it_expansion",
        "The state government defends the allocation as a step to draw global technology investments to Bangalore.",
        "Opposition BJP leaders criticize the infrastructure focus, claiming it ignores rural agrarian interests.",
        "A joint committee of IT captains and urban planners is formed to draft the Bangalore master plan.",
        "The IT Secretary declines to comment on the estimated value of tax concessions granted to software firms.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": 1}, {"karnatakaRuralTrustMemory": -1}, {"karnatakaStabilityMemory": -1},
        12, "Delays in land acquisition spark localized protests from suburban farmer groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The BJP criticism fails to gain traction as urban youth welcome the software job opportunities.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        8, "Liaison discussions are delayed by a lack of coordination in the municipal planning board.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-02: Farmer conventions Mandya
nk = f"{short_code}_2001_02_farmer_conventions"
news_items.append({
    "newsKey": nk, "month": "2001-02",
    "title": "CM Krishna Holds Farmer Conventions in Mandya (2001-02)",
    "description": "Chief Minister S. M. Krishna holds a series of mass rallies in Mandya, announcing crop support packages and canal desiltation works. The outreach aims to secure the party's rural base in the Old Mysore region.",
    "issueTags": ["rural", "politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "farmer_conventions",
        "The Agriculture Department launches camps in Mandya to distribute subsidized seeds and fertilizers.",
        "Opposition JD(S) leaders claim the packages are mere paper announcements ahead of local elections.",
        "A joint committee of sugar mill owners and sugarcane cultivators is formed to monitor crop tariffs.",
        "The Mandya District Collector declines to share the taluka-wise budget allocations for the water works.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaRuralTrustMemory": 1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        14, "Local warehouse shortages delay seed delivery, drawing protests from Mandya farmer groups.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The JD(S) criticism fails as sugar mills release pending payments to sugarcane farmers.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Committee pricing discussions stall as mill owners cite weak international sugar tariffs.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-03: Primary education Kannada medium
nk = f"{short_code}_2001_03_language_policy"
news_items.append({
    "newsKey": nk, "month": "2001-03",
    "title": "State Enforces Kannada Medium in Primary Schools (2001-03)",
    "description": "The state government enforces the mandatory Kannada medium policy in primary schools, drawing warnings of legal challenges from private English-medium school managements in urban zones.",
    "issueTags": ["identity", "politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "language_policy",
        "The Education Department defends the policy as essential to preserve regional identity and local heritage.",
        "Opposition BJP leaders demand exemptions for schools in border districts with minority languages.",
        "A joint committee of educators and linguists is formed to draft standardized Kannada textbooks.",
        "The Education Minister declines to comment on the number of private schools served with notice.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaIdentityMemory": 2}, {"karnatakaIdentityMemory": -1}, {"karnatakaStabilityMemory": -1},
        14, "Private school managements secure a high court stay, halting the immediate implementation of the rules.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        12, "The BJP demands are labeled as anti-Kannada by regional activist groups, weakening their stance.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Textbook drafts are delayed by disputes over dialect standardization in Northern districts.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-04: Forest patrol Veerappan Chamrajnagar
nk = f"{short_code}_2001_04_forest_clashes"
news_items.append({
    "newsKey": nk, "month": "2001-04",
    "title": "STF Patrol Clashes with Veerappan Associates in Chamrajnagar (2001-04)",
    "description": "A Special Task Force (STF) patrol exchanges fire with associates of the forest brigand Veerappan in the jungles of Chamrajnagar. The skirmish triggers fresh alerts in forest border villages.",
    "issueTags": ["security_crisis", "rural"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "forest_clashes",
        "The Home Department strengthens STF forest deployment and coordinates search operations with Tamil Nadu.",
        "Opposition BJP leaders criticize the government, claiming the administration is failing to secure border tracks in Chamrajnagar.",
        "A joint legislative-security coordination panel is formed to review border area vigilance.",
        "The DGP office declines to comment on the specific weapons recovered from the jungle hideout.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"karnatakaSecurityMemory": 1}, {"karnatakaStabilityMemory": 1}, {"karnatakaStabilityMemory": -1},
        16, "An operational failure during searches leads to minor civilian harassment, drawing local protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The BJP criticism is labeled as politicizing security, drawing disapproval from police associations.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over search protocols delay the joint panel's field visits.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-05: Local tax protest Bangalore
nk = f"{short_code}_2001_05_bangalore_tax"
news_items.append({
    "newsKey": nk, "month": "2001-05",
    "title": "Bangalore Traders Protest Municipal Octroi Taxes (2001-05)",
    "description": "Trader associations in Bangalore hold protests against the municipal corporation's octroi transit taxes. The traders demand simplified tax filing and waiver of transit duties.",
    "issueTags": ["economy", "protest"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "bangalore_tax",
        "The Excise Department conducts workshops for traders and promises a simplified entry filing process.",
        "Opposition leaders support the traders, demanding a postponement of the municipal octroi taxes.",
        "A joint legislative-trader coordination panel is formed to review octroi tax slabs and address issues.",
        "The Finance Minister declines to comment on the projected revenue impact of the new octroi rules.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": -1}, {"karnatakaCorruptionMemory": 1}, {"karnatakaStabilityMemory": -1},
        14, "Training workshops report low attendance, leaving many traders confused about the tax process.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "The opposition's demands are dismissed by economists who support modernizing the state's tax system.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Committee discussions stall as members fail to agree on transit tax exemption limits.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-06: Heavy rains waterlogging Bangalore
nk = f"{short_code}_2001_06_waterlogging"
news_items.append({
    "newsKey": nk, "month": "2001-06",
    "title": "Monsoon Rains Cause Waterlogging in Low-Lying Bangalore Areas (2001-06)",
    "description": "Early monsoon showers cause waterlogging and damage to roads in low-lying sectors of Bangalore. The opposition BJP raises concerns over poor municipal drainage preparations.",
    "issueTags": ["infrastructure", "governance"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "waterlogging",
        "The Municipal Corporation launches emergency repair works and orders clearing of storm drains in low-lying wards.",
        "Opposition leaders stage protests at waterlogged crossings, accusing the municipal commissioner of corruption.",
        "A joint civic coordination council is formed with representatives from all parties to monitor drainage repair quality.",
        "The Bangalore Mayor declines to release the budget figures allocated for pre-monsoon drain cleaning.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": -1}, {"karnatakaStabilityMemory": 1}, {"karnatakaStabilityMemory": -1},
        13, "Substandard patch repairs wash away in the next shower, drawing local press criticism.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        11, "The protests cause minor traffic blocks, drawing complaints from local merchant groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Drainage inspections are delayed by a lack of labor teams in the municipal engineering department.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-07: Farmers seed Belgaum
nk = f"{short_code}_2001_07_seed_belgaum"
news_items.append({
    "newsKey": nk, "month": "2001-07",
    "title": "Farmers Protest Seed Distribution Delays in Belgaum (2001-07)",
    "description": "Cultivators in the agricultural block of Belgaum hold demonstrations, protesting the high prices and slow distribution of seeds during the crucial Kharif sowing season. The delays threaten rural economic stability.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "seed_belgaum",
        "The Agriculture Department releases subsidized seed quotas to local cooperative societies in Belgaum.",
        "Opposition leaders join the farm rallies, demanding a complete waiver of seed distribution charges.",
        "A joint assembly committee is established to audit cooperative seed supply chains in Belgaum.",
        "The Cooperative Registrar declines to comment on the volume of seeds available in Belgaum godowns.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"karnatakaRuralTrustMemory": 1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        14, "Substandard seed distribution in some blocks leads to low germination rates, sparking fresh protests.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        12, "The opposition's demands are labeled as fiscally unfeasible during a revenue deficit.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Audit inspections are delayed by a lack of transport in remote block offices.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-08: Forest department restrictions Kodagu
nk = f"{short_code}_2001_08_forest_rights"
news_items.append({
    "newsKey": nk, "month": "2001-08",
    "title": "Forest Restrictions Spark Protests in Kodagu (2001-08)",
    "description": "Tribal villagers in Kodagu hold protests against new forest department regulations restricting the gathering of dry wood and minor forest produce. The regulations provoke anger over traditional forest rights.",
    "issueTags": ["rural", "identity"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "land_rights"},
    "reactionOptions": create_reactions(
        nk, "forest_rights",
        "The Forest Department issues guidelines to permit traditional gathering of minor produce by local tribal communities in Kodagu.",
        "Opposition BJP leaders support the villagers, demanding the immediate withdrawal of all forest department guards in Kodagu.",
        "A joint committee of forest officials and tribal representatives is formed to draft sustainable forest guidelines in Kodagu.",
        "The Chief Conservator of Forests declines to comment on the number of local villagers booked under forest acts in Kodagu.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -2},
        {"karnatakaIdentityMemory": 1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        15, "Local forest guards ignore the new guidelines, leading to fresh scuffles in remote beats of Kodagu.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        12, "The demands are criticized by conservation groups who warn against unregulated wood cutting in Kodagu.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Joint committee meetings are delayed by the non-participation of environmental NGOs.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-09: IT policy Hubli software parks
nk = f"{short_code}_2001_09_hubli_it"
news_items.append({
    "newsKey": nk, "month": "2001-09",
    "title": "Government Outlines IT Policy to Promote Hubli Software Parks (2001-09)",
    "description": "The state cabinet approves a new IT policy, prioritizing Hubli and Mysore for software park developments to disperse tech growth beyond Bangalore. The policy triggers intense discussions on infrastructure parity.",
    "issueTags": ["politics", "economy"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "hubli_it",
        "The state government defends the policy as a necessary step to distribute technological jobs to Tier-2 cities.",
        "Opposition BJP leaders organize rallies protesting the policy, calling it a political layout ignoring rural needs.",
        "A joint legislative committee is formed to review the IT draft and propose balanced infrastructure quotas.",
        "The Chief Minister's office declines to comment on the legal tax validity of the software parks in Hubli.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 0, "mediaImage": -3, "publicSupport": -3},
        {"karnatakaIdentityMemory": 2}, {"karnatakaIdentityMemory": -2}, {"karnatakaStabilityMemory": -1},
        16, "Protests by non-tribal associations lead to road blockades in urban pockets of Hubli.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "Counter-rallies by local student unions trigger localized scuffles in college campuses.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over resource definitions stall the legislative committee's first meeting.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-10: Kabini reservoir water release
nk = f"{short_code}_2001_10_kabini_water"
news_items.append({
    "newsKey": nk, "month": "2001-10",
    "title": "Protests Over Delayed Cauvery Water Release from Kabini (2001-10)",
    "description": "Farmers in the Kabini river basin stage demonstrations, protesting against early releases of water to Tamil Nadu. The protests threaten rural peace and lead to heavy security deployments near the dam.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "kabini_water",
        "The administration deploys heavy police units to ensure peace and detains key protest leaders preventively near Kabini.",
        "Opposition leaders support the protests, demanding the immediate closure of all Kabini reservoir sluice gates.",
        "A multi-party delegation meets the Governor to seek a consensus-based resolution to the Cauvery water crisis.",
        "The Home Department spokesperson declines to comment on the number of preventive arrests made near Kabini.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 0, "mediaImage": -3, "publicSupport": -3},
        {"karnatakaStabilityMemory": -1}, {"karnatakaIdentityMemory": -1}, {"karnatakaStabilityMemory": -1},
        15, "Clashes between pro and anti-release groups near Kabini lead to stone-pelting and injuries.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The support leads to counter-protests by agricultural groups, raising communal temperatures.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Governor's schedule conflicts delay the multi-party delegation's meeting, stalling progress.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-11: Rajyotsava celebrations
nk = f"{short_code}_2001_11_rajyotsava"
news_items.append({
    "newsKey": nk, "month": "2001-11",
    "title": "Karnataka Celebrates Rajyotsava Day (2001-11)",
    "description": "On Karnataka Rajyotsava day, the S. M. Krishna government hosts high-profile celebrations in Bangalore, showcasing state-of-the-art technology parks and regional welfare projects. Opposition BJP boycotted the official functions.",
    "issueTags": ["politics", "identity"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "rajyotsava",
        "The state government fast-tracks the launch of pending rural road and electricity projects in Mysore.",
        "Opposition BJP leaders state the first year was marked by social division and administrative failure.",
        "All parties agree to participate in a special assembly session to discuss state developmental goals.",
        "The Chief Secretary's office declines to release the total expenditure on the Rajyotsava celebrations.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": -1}, {"karnatakaIdentityMemory": -1}, {"karnatakaStabilityMemory": -1},
        13, "Contractor shortages delay the road projects in remote blocks, drawing minor media criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The BJP boycott is criticized by regional groups who welcome the new Rajyotsava recognition.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "The special assembly session is disrupted by shouting matches over the Cauvery water policy.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-12: Fiscal deficit infrastructure
nk = f"{short_code}_2001_12_fiscal_deficit"
news_items.append({
    "newsKey": nk, "month": "2001-12",
    "title": "Government Faces Budget Deficit Amid Transition Constraints (2001-12)",
    "description": "Karnataka's state finance department reports a widening budget deficit, largely attributed to high transition costs and delayed tax reallocations from central pools. The opposition BJP blames the government's fiscal mismanagement.",
    "issueTags": ["economy", "politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "fiscal_deficit",
        "The Finance Minister announces a fiscal rationalization plan and requests special central grants.",
        "BJP leaders demand a white paper on the state's debt status and criticize the government's tax policies.",
        "A joint legislative committee is formed to identify new revenue sources and non-tax avenues.",
        "The state treasury declines to release the monthly details of public debt accumulation to the media.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": -1}, {"karnatakaCorruptionMemory": 1}, {"karnatakaStabilityMemory": -1},
        14, "New tax proposals draw protests from local trader associations in Bangalore and Hubli.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        11, "The demand is dismissed as politically motivated, failing to gather support from industrial bodies.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "The revenue committee's report is delayed due to partisan gridlock over tax proposals.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-12"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002
# 2002-01: BJP demands drought relief North Karnataka
nk = f"{short_code}_2002_01_drought_relief"
news_items.append({
    "newsKey": nk, "month": "2002-01",
    "title": "BJP Demands Immediate Drought Relief for North Karnataka (2002-01)",
    "description": "Opposition BJP leaders demand the immediate implementation of drought relief packages, accusing the Krishna government of deliberately delaying job recruitment. The demand intensifies social division in the state.",
    "issueTags": ["politics", "identity"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "drought_relief",
        "The CM announces the start of ST reservation verification in all district circle offices.",
        "Non-tribal organizations call for counter-protests, warning of state-wide agitations against the policy.",
        "A joint legislative panel is set up to negotiate job quotas and verify candidate definitions.",
        "The Personnel Department declines to comment on the estimated number of vacant job posts.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaIdentityMemory": 1}, {"karnatakaIdentityMemory": -1}, {"karnatakaStabilityMemory": -1},
        14, "Circle offices report major records are missing or mutilated, stalling the verification process.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "Protests block main rail routes, drawing complaints from local merchant groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Committee talks break down over terms of representation, failing to draft any reform guidelines.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-02: Cauvery water Mandya Bandh
nk = f"{short_code}_2002_02_mandya_bandh"
news_items.append({
    "newsKey": nk, "month": "2002-02",
    "title": "Cauvery Dispute Triggers Massive Bandh in Mandya (2002-02)",
    "description": "A total shutdown is observed in Mandya district as farmers and activist groups protest against Tamil Nadu's demands for Cauvery water release. The bandh disrupts transportation and commercial operations.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "mandya_bandh",
        "The government deploys heavy security forces to Mandya and monitors water levels closely.",
        "Opposition JD(S) leaders lead the rallies in Mandya, demanding that no water be released under any conditions.",
        "A joint delegation of all Karnataka parties meets the Prime Minister to present the state's water distress.",
        "The Water Resources Minister declines to comment on the daily inflow levels at the KRS dam.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": -1, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaRuralTrustMemory": 1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        15, "Clashes near key canals lead to police cane charges, drawing localized media criticism.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        13, "JD(S) statements provoke minor scuffles between party workers, raising regional temperatures.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "PM's scheduled appointment conflicts delay the joint delegation's meet, stalling progress.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-03: State employees strike DA
nk = f"{short_code}_2002_03_employees_strike"
news_items.append({
    "newsKey": nk, "month": "2002-03",
    "title": "State Government Employees Launch Indefinite Strike (2002-03)",
    "description": "Over 2 lakh state government employees in Karnataka launch an indefinite strike, demanding dearness allowance parity with central government staff. The strike paralyzes administrative offices in Bangalore.",
    "issueTags": ["protest", "economy"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "employees_strike",
        "The Finance Minister promises a phased release of the dearness allowance and initiates talks with employee unions.",
        "BJP opposition leaders support the strike, accusing the government of fiscal mismanagement and empty coffers.",
        "A joint legislative-union panel is formed to negotiate salary adjustments within budget constraints.",
        "The administration invokes the ESMA act to force striking workers back to their departments.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"karnatakaStabilityMemory": -1}, {"karnatakaCorruptionMemory": 1}, {"karnatakaStabilityMemory": -1},
        14, "The phased release proposal is rejected by union hardliners, extending the administrative strike.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "Rural voter groups criticize the opposition's stance, arguing employee salaries consume too much tax.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Committee discussions stall as members fail to agree on the definition of base salary scales.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-04: Gulbarga water shortage heatwave
nk = f"{short_code}_2002_04_gulbarga_water"
news_items.append({
    "newsKey": nk, "month": "2002-04",
    "title": "Severe Summer Water Shortage Triggers Rationing in Gulbarga (2002-04)",
    "description": "An intense heatwave in April depletes local reservoirs, forcing Gulbarga's municipal corporation to implement strict water rationing. Residents protest over irregular supply, turning the water scarcity into a political issue.",
    "issueTags": ["rural", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "gulbarga_water",
        "The government deploys municipal water tankers to affected wards and fast-tracks the Gulbarga water pipeline project.",
        "Opposition leaders stage dharnas outside municipal offices, accusing the Congress administration of water mismanagement.",
        "A joint civic coordination council is formed to oversee equitable water distribution across all wards.",
        "The Gulbarga Municipal Corporation declines to publish the daily water supply schedule for residential areas.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"karnatakaRuralTrustMemory": -1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        15, "Logistical failures result in uneven tanker distribution, sparking minor protests in poorer wards.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "Protests lead to brief traffic disruptions in Gulbarga, drawing criticism from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Tanker coordination is hit by staff shortages, leaving several high-priority wards dry.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-05: Language policy challenge High Court
nk = f"{short_code}_2002_05_language_litigation"
news_items.append({
    "newsKey": nk, "month": "2002-05",
    "title": "High Court Hears Challenge to Primary Kannada Policy (2002-05)",
    "description": "The Bangalore High Court begins hearings on several petitions challenging the mandatory Kannada medium policy in primary schools. The legal challenge halts new registration permissions, causing frustration among parents.",
    "issueTags": ["politics", "identity"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "language_litigation",
        "The Advocate General defends the state's language criteria as necessary for local culture promotion.",
        "Opposition BJP leaders accuse the government of drafting a legally flawed policy that hurts minority language students.",
        "A joint committee of legal experts and legislators is formed to study constitutional medium options.",
        "The Education Department declines to comment on the number of new school permits currently suspended.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaIdentityMemory": 1}, {"karnatakaIdentityMemory": -1}, {"karnatakaStabilityMemory": -1},
        14, "The court requests further records, extending the permit freeze and drawing critical editorials.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "The criticism is dismissed as political posturing, failing to gather support from student unions.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Legal expert meetings stall due to non-cooperation by former commission members.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-06: Shimoga farmers loan waivers
nk = f"{short_code}_2002_06_shimoga_protest"
news_items.append({
    "newsKey": nk, "month": "2002-06",
    "title": "Shimoga Farmers Stage Rallies Demanding Loan Waivers (2002-06)",
    "description": "Cultivators in Shimoga district hold massive rallies, demanding the immediate waiver of agricultural loans due to consecutive dry seasons. The protests reflect growing agrarian distress in the Malnad region.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "shimoga_protest",
        "The CM announces interest waiver packages for cooperative loans in affected districts.",
        "Opposition BJP leaders accuse the government of offering cosmetic reliefs that ignore principal loan amounts.",
        "A joint convention of banking heads and farm representatives is organized to seek a credit restructuring formula.",
        "The state Congress spokesperson declines to comment on reports of seat-sharing disputes inside regional offices.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaRuralTrustMemory": 2}, {"karnatakaRuralTrustMemory": -1}, {"karnatakaStabilityMemory": -1},
        14, "Leaks from the bank consultations fuel further media speculation about cooperative defaults.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The counter-rallies disrupt traffic, drawing complaints from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "The credit convention is boycotted by private bank representatives, failing to resolve the standoff.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-07: Cauvery monitoring authority directive
nk = f"{short_code}_2002_07_cauvery_directive"
news_items.append({
    "newsKey": nk, "month": "2002-07",
    "title": "Cauvery Monitoring Authority Directs Water Release (2002-07)",
    "description": "The Cauvery Monitoring Authority directs Karnataka to release immediate water to Tamil Nadu. The directive triggers widespread protests and political polarization across the state.",
    "issueTags": ["rural", "politics"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "cauvery_directive",
        "The S. M. Krishna government files a petition in the Supreme Court seeking review of the water release directive.",
        "Opposition JD(S) leaders demand that the government ignore the directive and stop all reservoir outflows.",
        "A joint committee of water experts and legal advisors is formed to draft the state's legal reply.",
        "The Chief Secretary declines to comment on the volume of water currently stored in the KRS reservoir.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": -1, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"karnatakaRuralTrustMemory": -2}, {"karnatakaIdentityMemory": 1}, {"karnatakaStabilityMemory": -1},
        16, "Protests by farmer groups block state highways, leading to minor clashes and press criticism.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "JD(S) statements provoke minor scuffles between party workers, raising regional temperatures.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Local water talks are boycotted by hardline representatives, failing to resolve the standoff.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-08: Veerappan abducts H Nagappa Chamarajanagar
nk = f"{short_code}_2002_08_nagappa_abduction"
news_items.append({
    "newsKey": nk, "month": "2002-08",
    "title": "Veerappan Kidnaps Former Minister H. Nagappa (2002-08)",
    "description": "In a major security crisis, forest brigand Veerappan abducts former minister H. Nagappa from his farmhouse in Chamarajanagar. The incident triggers a high security alert in the southern border zones.",
    "issueTags": ["security_crisis", "politics"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "nagappa_abduction",
        "The S. M. Krishna government deploys additional STF units and establishes a high-level coordination team with Tamil Nadu.",
        "Opposition BJP leaders accuse the government of failing to protect citizens and demand a CBI probe into border security.",
        "A joint multi-party coordination council is formed to oversee the hostage negotiation strategy.",
        "The Home Department declines to comment on the contents of the first audio cassette received from Veerappan.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaSecurityMemory": -1}, {"karnatakaStabilityMemory": -1}, {"karnatakaStabilityMemory": -1},
        15, "STF search operations in deep forest hideouts fail to yield results, drawing critical editorials.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The BJP demands are dismissed as political opportunism by regional activist groups, weakening their stance.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Liaison expert meetings stall due to non-cooperation by former commission members.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-09: Mandya farmers block highways Cauvery
nk = f"{short_code}_2002_09_highway_blockade"
news_items.append({
    "newsKey": nk, "month": "2002-09",
    "title": "Mandya Farmers Block Bangalore-Mysore Highway (2002-09)",
    "description": "Protests over the Cauvery water dispute intensify as Mandya farmers block the Bangalore-Mysore highway, halting transport and tourism. The protestors demand the immediate withdrawal of water release commitments.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "highway_blockade",
        "The government deploys municipal security forces and initiates discussions with farmer union leaders.",
        "Opposition BJP leaders support the blockade, demanding a complete halt to all Cauvery water outflows.",
        "A joint assembly panel is established to evaluate water storage and coordinate relief with central teams.",
        "The Irrigation Department declines to specify the daily water release schedule to the press.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"karnatakaRuralTrustMemory": 1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        14, "Local administrative delays stall the farmer talks, extending the highway blockade in Mandya.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The demands are labeled by the ruling party as fiscally irresponsible during a revenue deficit.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The central team's visit is delayed, stalling the disbursement of joint relief funds.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-10: STF Chengadi forest search
nk = f"{short_code}_2002_10_chengadi_search"
news_items.append({
    "newsKey": nk, "month": "2002-10",
    "title": "STF Intensifies Searches in Chengadi Forest (2002-10)",
    "description": "Special Task Force operations are intensified in the Chengadi forest area following reports of Veerappan's movements. The prolonged search operation tests the patience of the local administration.",
    "issueTags": ["security_crisis", "rural"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "chengadi_search",
        "The state police deploys additional checkpoints and coordinates vigilance checks with forest patrol units.",
        "Opposition leaders demand that the state immediately release funds to support local border village development.",
        "A joint legislative-police panel is formed to monitor border area security and rehabilitation progress in forest blocks.",
        "The Home Department declines to comment on the specific details of the ongoing security deployments.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"karnatakaSecurityMemory": 1}, {"karnatakaStabilityMemory": 1}, {"karnatakaStabilityMemory": -1},
        16, "Leaks from the security operations fuel media speculation, drawing minor party confusion.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        13, "The demands are criticized as ignoring national security imperatives, drawing mild media pushback.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Liaison panel meetings are postponed due to border security alerts in neighboring divisions.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-11: Veerappan negotiator deadline
nk = f"{short_code}_2002_11_negotiator_deadline"
news_items.append({
    "newsKey": nk, "month": "2002-11",
    "title": "Veerappan Negotiator Deadline Passes Without Consensus (2002-11)",
    "description": "The deadline set by Veerappan to release Kolathur Mani to act as a negotiator passes. The state government cites legal and constitutional constraints in releasing Mani, extending the hostage crisis.",
    "issueTags": ["politics", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "negotiator_deadline",
        "The CM holds a cabinet coordination meet and reiterates the need for legal adherence in hostage situations.",
        "Opposition BJP leaders call the deadlock a proof that the Congress administration is too weak to handle brigands.",
        "Senior coalition leaders hold a closed-door meeting to address concerns and project a united front.",
        "The state Congress spokesperson declines to comment on reports of secret emissary talks.",
        {"partyMorale": 1, "corruptionScore": 0, "mediaImage": 1, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": -1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        14, "Leaks from the coordination meeting fuel further media speculation about leadership changes.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The criticism is ignored by voters who view it as standard opposition exploitation of internal issues.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Several key legislators skip the unity meeting, diluting its positive impact in the press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-12: Nagappa body found Chengadi
nk = f"{short_code}_2002_12_nagappa_tragedy"
news_items.append({
    "newsKey": nk, "month": "2002-12",
    "title": "H. Nagappa Found Dead in Chengadi Forest (2002-12)",
    "description": "The hostage crisis ends in tragedy as the body of former minister H. Nagappa is discovered in the Chengadi forest. Widespread grief and public anger sweep Chamarajanagar and Mysore districts.",
    "issueTags": ["security_crisis", "politics"],
    "weights": {"baseSelectionWeight": 1.3, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "nagappa_tragedy",
        "The government announces a state funeral for Nagappa and orders an immediate high-level inquiry.",
        "Opposition BJP leaders demand the resignation of the Home Minister and call for a state-wide bandh.",
        "The assembly holds a special condolence session with all parties appealing for calm and regional peace.",
        "The Home Department declines to comment on the medical details of the post-mortem report.",
        {"partyMorale": 1, "corruptionScore": 0, "mediaImage": 1, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"karnatakaSecurityMemory": -2}, {"karnatakaStabilityMemory": -1}, {"karnatakaStabilityMemory": -1},
        15, "Clashes between party supporters during the bandh lead to minor injuries in Mysore outskirts.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The resignation demands provoke minor scuffles between party workers, raising political temperatures.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Condolence discussions are disrupted by shouting matches over security lapses, halting proceedings.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-12"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003
# 2003-01: Krishna cabinet Nagappa compensation STF hike
nk = f"{short_code}_2003_01_stf_upgrade"
news_items.append({
    "newsKey": nk, "month": "2003-01",
    "title": "Government Announces Compensation for Nagappa's Family (2003-01)",
    "description": "In a bid to restore confidence, the cabinet approves financial compensation for H. Nagappa's family and allocates special funds to upgrade STF tracking equipment and forest weaponry.",
    "issueTags": ["governance", "politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "stf_upgrade",
        "The government sets up a special forest patrol command and coordinates search techniques with central forces.",
        "Opposition BJP leaders call the funds delayed, claiming the upgrades should have been done before the abduction.",
        "A joint legislative safety committee is established to audit STF forest equipment allocations.",
        "The DGP office declines to release the technical details of the new tracking equipment purchased.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaSecurityMemory": 1}, {"karnatakaStabilityMemory": -1}, {"karnatakaStabilityMemory": -1},
        14, "Administrative delays stall the equipment procurement, drawing critical media editorials.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "The BJP demands are dismissed as political posturing, failing to gather wider neutral attention.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Disagreements over resource allocation priorities stall the joint safety committee's first meeting.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-02: North Karnataka drought
nk = f"{short_code}_2003_02_north_drought"
news_items.append({
    "newsKey": nk, "month": "2003-02",
    "title": "Severe Drought Conditions Hit North Karnataka (2003-02)",
    "description": "consecutive failed monsoons trigger critical drinking water shortages in Gulbarga and Bijapur districts. The administration deploys water tankers to the worst-affected villages.",
    "issueTags": ["rural", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "north_drought",
        "The Agriculture Department releases emergency relief funds and orders tank repair works in Gulbarga.",
        "Opposition BJP leaders demand a complete waiver of crop loans for farmers in drought-affected blocks.",
        "A joint assembly panel is established to evaluate crop damage and coordinate relief with central teams.",
        "The Irrigation Department declines to specify the daily water distribution schedule in dry districts.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"karnatakaRuralTrustMemory": 1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        14, "Local administrative delays stall relief disbursement in remote villages, drawing protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The demands are labeled by the ruling party as fiscally irresponsible during a revenue deficit.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The central team's visit is delayed, stalling the disbursement of joint relief funds.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-03: BJP Ryot Yatra farmer suicides
nk = f"{short_code}_2003_03_ryot_yatra"
news_items.append({
    "newsKey": nk, "month": "2003-03",
    "title": "BJP Launches Ryot Yatra Targeting Farmer Suicides (2003-03)",
    "description": "Opposition BJP launches a 'Ryot Yatra' (Farmer Tour) in Mandya, highlighting sugarcane farmer distress and suicides due to debt. The tour draws high participation from rural communities.",
    "issueTags": ["rural", "politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "ryot_yatra",
        "Congress leaders organize block-level meetings to highlight the state's cooperative insurance schemes.",
        "BJP units organize mass receptions for the yatra, consolidating support in rural constituencies.",
        "Both parties agree to avoid provocative language during campaign rallies to prevent local tensions.",
        "The CM's office declines to comment on the turnout and impact of the BJP yatra.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": -1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        14, "Internal Congress factional squabbles over campaign allocations undermine their block meetings.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "Logistical coordination failures delay the yatra in Mandya, drawing mild local criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        8, "A minor code violation by a local worker leads to a warning from the Election Commission.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-04: Emergency water funds S. M. Krishna
nk = f"{short_code}_2003_04_emergency_water"
news_items.append({
    "newsKey": nk, "month": "2003-04",
    "title": "Government Releases Emergency Funds for Rural Employment (2003-04)",
    "description": "Chief Minister S. M. Krishna releases emergency water and employment funds for rural blocks. The funds aim to provide work under dry relief schemes and check distress migration.",
    "issueTags": ["rural", "governance"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "emergency_water",
        "The government sets up a block-level grievance cell to fast-track employment payouts in dry zones.",
        "Opposition BJP leaders criticize the announcement, calling it a pre-poll layout that ignores long-term canal irrigation.",
        "A joint assembly committee is established to audit rural employment allocations and ensure fair distribution.",
        "The Rural Development Department declines to specify the district-wise allocations for the relief works.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaRuralTrustMemory": 1}, {"karnatakaRuralTrustMemory": -1}, {"karnatakaStabilityMemory": -1},
        13, "Substandard work distribution in some blocks leads to low pay efficiency, sparking local protests.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        11, "The BJP criticism fails to gain traction as local panchayats welcome the relief employment.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Audit inspections are delayed by a lack of transport in remote block offices.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-05: VAT protest traders
nk = f"{short_code}_2003_05_vat_protest"
news_items.append({
    "newsKey": nk, "month": "2003-05",
    "title": "Local Traders Protest Against Early VAT Proposals (2003-05)",
    "description": "Trader associations in Bangalore and Hubli hold protests against the state's early proposal to introduce Value Added Tax (VAT). The traders demand simplified tax slabs and postponement of the policy.",
    "issueTags": ["economy", "protest"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "vat_protest",
        "The Excise Department conducts training workshops for traders and promises a simplified filing process.",
        "Opposition leaders support the traders, demanding a postponement of VAT until system readiness is achieved.",
        "A joint legislative-trader coordination panel is formed to review tax slabs and address grievances.",
        "The Finance Minister declines to comment on the projected revenue impact of the new VAT system.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": -1}, {"karnatakaCorruptionMemory": 1}, {"karnatakaStabilityMemory": -1},
        14, "Training workshops report low attendance, leaving many traders confused about the new system.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "The opposition's demands are dismissed by economists who support modernizing the tax system.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Committee discussions stall as members fail to agree on the definition of tax slabs.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-06: Devanahalli airport MOUs
nk = f"{short_code}_2003_06_airport_mous"
news_items.append({
    "newsKey": nk, "month": "2003-06",
    "title": "Government Signs Devanahalli Airport MOU (2003-06)",
    "description": "The state government signs the initial memorandum of understanding (MOU) for the Bangalore international airport at Devanahalli. Suburban farmers hold protests warning of massive land displacements.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "land_rights"},
    "reactionOptions": create_reactions(
        nk, "airport_mous",
        "The Infrastructure Department announces strict rehabilitation guidelines and promises fair compensation packages in Devanahalli.",
        "Opposition BJP leaders join the protests, demanding that the MOU be tabled in the assembly for public review.",
        "A joint committee of aviation officials, farmer representatives, and legislators is formed to monitor rehabilitation.",
        "The Infrastructure Minister declines to release the specific land acreage required for the Devanahalli airport project.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"karnatakaRuralTrustMemory": -1}, {"karnatakaIdentityMemory": 1}, {"karnatakaStabilityMemory": -1},
        15, "Local protests block initial survey work in Devanahalli, drawing police intervention.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The demands are criticized as anti-development by business groups who support international aviation connectivity.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over the committee's representation delay its first review meeting.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-07: Dengue outbreak Hubli-Dharwad
nk = f"{short_code}_2003_07_dengue_outbreak"
news_items.append({
    "newsKey": nk, "month": "2003-07",
    "title": "Dengue Outbreak Reported in Hubli-Dharwad (2003-07)",
    "description": "A severe dengue outbreak in Hubli-Dharwad municipal zones causes several casualties. Local health clinics report shortages of mosquito control units and emergency medicines.",
    "issueTags": ["rural", "governance"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "dengue_outbreak",
        "The Health Department deploys mobile medical camps and sends emergency drug consignments to Hubli-Dharwad.",
        "Opposition BJP leaders visit the affected blocks, accusing the government of ignoring primary health centers.",
        "A joint legislative-medical panel is formed to review municipal healthcare infrastructure and drug supply chains.",
        "The Health Directorate declines to release the official casualty figures from the Hubli-Dharwad outbreak.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"karnatakaRuralTrustMemory": 1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        14, "Mobile camps face fuel shortages, leaving remote municipal hamlets unreached during the peak outbreak.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The BJP statements are labeled as political posturing, failing to gather wider neutral attention.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Committee field visits are delayed by heavy rainfall in northern river zones.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-08: Krishna basin floods Bagalkot
nk = f"{short_code}_2003_08_krishna_floods"
news_items.append({
    "newsKey": nk, "month": "2003-08",
    "title": "Krishna River Overflow Displaces Families in Bagalkot (2003-08)",
    "description": "Continuous heavy rains cause the Krishna river to overflow, inundating low-lying residential areas in Bagalkot. The administration deploys rescue teams to evacuate affected families.",
    "issueTags": ["rural", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "krishna_floods",
        "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations in Bagalkot.",
        "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages to Krishna river victims.",
        "A joint legislative relief committee is established to supervise rehabilitation work in Bagalkot division.",
        "The district collector declines to release the official crop loss estimates in the first week for Bagalkot.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"karnatakaStabilityMemory": -1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        14, "Logistical failures delay the delivery of tents to remote villages, drawing local protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        12, "The criticism leads to minor scuffles at distribution centers, disrupting relief work.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over relief beneficiary lists stall aid distribution in several affected talukas.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-09: Industrial park land protest Bidadi
nk = f"{short_code}_2003_09_bidadi_protest"
news_items.append({
    "newsKey": nk, "month": "2003-09",
    "title": "Farmers Protest Industrial Land Acquisition in Bidadi (2003-09)",
    "description": "Farmers in Bidadi hold demonstrations protesting the acquisition of their agricultural land for a new industrial township. The protestors demand fair market-value compensation and job guarantees.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "land_rights"},
    "reactionOptions": create_reactions(
        nk, "bidadi_protest",
        "The land acquisition officer sets up a verification cell to review compensation claims and job listings in Bidadi.",
        "Opposition JD(S) leaders join the protests, demanding that the land acquisition process be suspended immediately in Bidadi.",
        "A joint committee of land officials and local panchayat chiefs is formed to verify the value of the acquired plots in Bidadi.",
        "The District Collector declines to release the total acreage of land scheduled for acquisition in Bidadi.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -2},
        {"karnatakaRuralTrustMemory": 1}, {"karnatakaRuralTrustMemory": -1}, {"karnatakaStabilityMemory": -1},
        14, "Administrative delays stall the verification cell, drawing fresh protests outside the collectorate.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The JD(S) protests lead to minor traffic blockades, drawing complaints from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Verification is delayed due to missing land records in the revenue office, stalling progress.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-10: Yashaswini health scheme rural
nk = f"{short_code}_2003_10_yashaswini_scheme"
news_items.append({
    "newsKey": nk, "month": "2003-10",
    "title": "CM Krishna Launches Yashaswini Health Scheme (2003-10)",
    "description": "Chief Minister S. M. Krishna launches the 'Yashaswini' health insurance scheme, offering subsidized surgeries to cooperative dairy farmers. Rural organizations welcome the health security measure.",
    "issueTags": ["governance", "identity"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "yashaswini_scheme",
        "The government nominates panel hospitals and schedules the registration drive across all cooperative societies.",
        "Opposition BJP leaders claim the scheme is cosmetic and fails to upgrade physical primary health centers.",
        "A joint committee of assembly members and medical representatives is formed to oversee clinic quality.",
        "The Cooperative Union Secretary declines to release the names of nominated hospitals before formal notifications.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaIdentityMemory": 1}, {"karnatakaIdentityMemory": -1}, {"karnatakaStabilityMemory": -1},
        13, "Hospital enrollment disputes delay the scheme's launch in northern blocks, drawing minor press criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The BJP criticism is ignored by cooperative unions who welcome the surgery subsidies.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Policy implementation is delayed due to disagreements over hospital fee reimbursement scales.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-11: Naxalite Western Ghats
nk = f"{short_code}_2003_11_wghats_naxal"
news_items.append({
    "newsKey": nk, "month": "2003-11",
    "title": "Naxalite Activity Reported in Western Ghats (2003-11)",
    "description": "Reports of minor Naxalite assemblies in the forests of Chikmagalur and Udupi trigger security alerts. The state police deploys anti-naxal forces to monitor remote hill trails.",
    "issueTags": ["security_crisis", "rural"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "wghats_naxal",
        "The state police deploys additional security forces to patrol hill lines and coordinates checks with forest teams.",
        "Opposition BJP leaders criticize the government, claiming the administration is failing to secure Western Ghats trails.",
        "A joint legislative-police safety panel is formed to review security measures along forest corridors.",
        "The Home Department spokesperson declines to comment on security protocols established near Udupi border posts.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"karnatakaSecurityMemory": 1}, {"karnatakaStabilityMemory": 1}, {"karnatakaStabilityMemory": -1},
        15, "Security patrols face logistical delays, leaving several remote hill trails unmonitored.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The BJP criticism is labeled as politicizing security, drawing disapproval from police associations.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over search protocols delay the joint panel's field visits.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-12: Krishna dissolves assembly early
nk = f"{short_code}_2003_12_dissolution"
news_items.append({
    "newsKey": nk, "month": "2003-12",
    "title": "CM Krishna Decides on Early Assembly Dissolution (2003-12)",
    "description": "Chief Minister S. M. Krishna decides to dissolve the legislative assembly early, seeking a fresh mandate alongside the Lok Sabha elections. The decision catches the opposition parties by surprise.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.3, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "dissolution",
        "The government defends the early dissolution as a step to align state and central voting timelines.",
        "Opposition BJP and JD(S) leaders claim the early polls are a desperate attempt to bypass drought accountability.",
        "The assembly passes a resolution thanking S. M. Krishna for his service and welcoming the elections.",
        "The CM's office declines to comment on reports of seat-sharing talks with minor regional parties.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": -2}, {"karnatakaStabilityMemory": 1}, {"karnatakaStabilityMemory": -1},
        15, "Rebel MLAs protest candidate changes, threatening minor local administrative friction.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        13, "The BJP claims are supported by North Karnataka farm unions, generating localized media focus.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Bickering over candidate listings disrupts the first party strategy sessions.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-12"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004
# 2004-01: Assembly elections announced candidate screening
nk = f"{short_code}_2004_01_polls_announced"
news_items.append({
    "newsKey": nk, "month": "2004-01",
    "title": "Election Commission Announces Karnataka Assembly Dates (2004-01)",
    "description": "The Election Commission of India announces that the Karnataka Legislative Assembly elections will be held in April and May 2004. Candidate screening begins across all major party blocks.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "polls_announced",
        "The ruling Congress focuses on finalizing its candidate list and preparing its election manifesto.",
        "Opposition BJP units launch campaigns, targeting the Congress's drought management and infrastructure policies.",
        "Both parties agree to a joint liaison committee to resolve model code of conduct disputes quickly.",
        "The party heads decline to comment on the internal selection process for controversial seats.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": -1}, {"karnatakaIdentityMemory": 1}, {"karnatakaStabilityMemory": -1},
        13, "Disgruntled Congress leaders threaten to run as independent candidates in several constituencies.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "Factional squabbles in the BJP's Hubli unit delay candidate selection in several seats.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Liaison talks break down as both sides trade code violation accusations before the commission.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-02: Bangalore electronics city upgrades
nk = f"{short_code}_2004_02_electronics_city"
news_items.append({
    "newsKey": nk, "month": "2004-02",
    "title": "Government Announces Upgrades for Bangalore Electronics City (2004-02)",
    "description": "The state government announces a rationalization of local power tariffs and water pipelines for software units in Bangalore Electronics City. The policy aims to support local technology growth.",
    "issueTags": ["infrastructure", "economy"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "electronics_city",
        "The Finance Department implements tariff adjustments and establishes a single-window system for software units.",
        "Opposition leaders claim the policy favors large corporate houses at the expense of local agricultural units.",
        "A joint government-industry coordination committee is formed to monitor infrastructure upgrades in the electronics hubs.",
        "The Industry Minister declines to share the estimated revenue loss due to the new concessions for software units.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": -1}, {"karnatakaCorruptionMemory": 1}, {"karnatakaStabilityMemory": -1},
        13, "Administrative delays stall the single-window clearance cell, drawing criticism from investors.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "Local farmer unions distance themselves from the opposition's protests, weakening the criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Coordination meetings are delayed by disagreements over municipal tax sharing inside the zone.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-03: Campaign peaks Lok Sabha/Assembly
nk = f"{short_code}_2004_03_campaign_peaks"
news_items.append({
    "newsKey": nk, "month": "2004-03",
    "title": "Assembly and Lok Sabha Campaign Peaks in Karnataka (2004-03)",
    "description": "High-stakes election campaigning peaks in Karnataka. The BJP focuses on anti-incumbency and drought, while the Congress highlights its Bangalore development and rural health achievements.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "campaign_peaks",
        "The Congress campaigns on its five-year developmental record and IT-boom achievements.",
        "Opposition BJP-JD(S) leaders focus on rural unemployment and criticize the Congress's economic policies.",
        "Both parties agree to limit loudspeaker usage during late hours to prevent disturbing students during exams.",
        "The state election coordinators decline to comment on reports of internal candidate disputes.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": -1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        12, "The campaign themes fail to connect with poor rural voters, drawing mild press criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "Factional squabbles within the Congress's state unit limit the reach of their rural campaigns.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Local campaign workers violate the loudspeaker timings in Bangalore, drawing warnings from the EC.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-04: Voting held in phases
nk = f"{short_code}_2004_04_voting_phases"
news_items.append({
    "newsKey": nk, "month": "2004-04",
    "title": "Voting Held for Assembly and Lok Sabha in Karnataka (2004-04)",
    "description": "Polling is held across Karnataka's assembly constituencies. Security is tight, particularly in the border forest districts, to ensure peaceful voting under the supervision of central observers.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "voting_phases",
        "The state administration coordinates logistics and deploys home guards to assist central security forces during voting.",
        "Opposition parties watch voting closely, raising concerns over alleged local administration bias in rural booths.",
        "All parties issue a joint statement appreciating the peaceful conduct of elections in forest zones.",
        "The state election commissioner declines to comment on the final voter turnout figures in the first day.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": -1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        13, "Voting delays due to EVM malfunctions in some booths draw local complaints and press criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The allegations are dismissed by independent observers, neutralizing the opposition's claims.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        8, "Minor disputes over election duty staff accommodation are reported in northern blocks.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-05: Hung assembly Dharam Singh CM
nk = f"{short_code}_2004_05_coalition_formed"
news_items.append({
    "newsKey": nk, "month": "2004-05",
    "title": "Hung Assembly in Karnataka; Dharam Singh Sworn in as CM (2004-05)",
    "description": "Elections yield a fractured mandate. To prevent the BJP from forming government, the Congress and JD(S) establish a coalition. Dharam Singh is sworn in as Chief Minister of the coalition.",
    "issueTags": ["politics", "governance"],
    "weights": {"baseSelectionWeight": 1.3, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "coalition_formed",
        "The new CM Dharam Singh promises a balanced governance model prioritizing both agriculture and IT.",
        "Opposition BJP leaders call the coalition unholy and predict its early collapse due to internal conflicts.",
        "The assembly passes a resolution welcoming the new coalition and promising floor debate order.",
        "The Governor's office declines to issue a public statement on the invite decisions.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": -2}, {"karnatakaStabilityMemory": 1}, {"karnatakaStabilityMemory": -1},
        15, "Rebel MLAs demand key portfolios in the new cabinet, threatening minor administrative friction.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        13, "Protests by BJP workers in Bangalore outskirts lead to stone-pelting and curfew warnings.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Bickering over the resolution wording disrupts the first assembly session under the new CM.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-06: Siddaramaiah Deputy CM cabinet friction
nk = f"{short_code}_2004_06_siddaramaiah_deputy"
news_items.append({
    "newsKey": nk, "month": "2004-06",
    "title": "Siddaramaiah Sworn in as Deputy CM (2004-06)",
    "description": "Siddaramaiah of the JD(S) is sworn in as Deputy Chief Minister. Friction immediately starts between Congress and JD(S) over portfolio allocation and control of local boards.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "siddaramaiah_deputy",
        "CM Dharam Singh holds a cabinet coordination meet and reiterates the need for alliance unity.",
        "Opposition BJP leaders call the infighting a proof that the coalition is too divided to govern.",
        "Senior leaders from both parties hold a closed-door meeting to project a united front.",
        "The state Congress spokesperson declines to comment on reports of portfolio division disputes.",
        {"partyMorale": 1, "corruptionScore": 0, "mediaImage": 1, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": -1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        14, "Leaks from the coordination meeting fuel further media speculation about leadership changes.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The criticism is ignored by voters who view it as standard opposition exploitation of internal issues.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Several key legislators skip the unity meeting, diluting its positive impact in the press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-07: Cauvery tribunal Mysore protests
nk = f"{short_code}_2004_07_mysore_protests"
news_items.append({
    "newsKey": nk, "month": "2004-07",
    "title": "Cauvery Tribunal Hearings Trigger Protests in Mysore (2004-07)",
    "description": "As the Cauvery Water Disputes Tribunal resumes hearings, farmer organizations in Mysore stage demonstrations. The protestors warn of statewide bandhs if the state's storage is not prioritized.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "mysore_protests",
        "The state government sends senior legal counsels to present irrigation data before the tribunal.",
        "Opposition BJP leaders stage protests, demanding that the coalition stop water outflow immediately.",
        "A joint assembly committee is established to audit reservoir water storage levels in the basin.",
        "The Irrigation Secretary declines to share the daily water release figures to the press.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"karnatakaRuralTrustMemory": 1}, {"karnatakaRuralTrustMemory": -1}, {"karnatakaStabilityMemory": -1},
        14, "Local administrative delays stall the farmer talks, extending the protests in Mysore.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The demands are labeled by the ruling party as fiscally irresponsible during a revenue deficit.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The central team's visit is delayed, stalling the disbursement of joint relief funds.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-08: Congress-JD(S) coordination committee
nk = f"{short_code}_2004_08_coordination_committee"
news_items.append({
    "newsKey": nk, "month": "2004-08",
    "title": "Coalition Establishes Joint Coordination Committee (2004-08)",
    "description": "To address growing policy differences, Congress and JD(S) form a joint coordination committee under JD(S) Chief H. D. Deve Gowda. The committee aims to streamline policy approvals.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "coordination_committee",
        "The committee holds its first meet and outlines guidelines for joint policy approvals.",
        "Opposition BJP leaders call the committee a parallel government that dilutes the CM's authority.",
        "All coalition legislators sign a pledge to follow the coordination committee's policy guidelines.",
        "The coordination committee spokesperson declines to share the details of portfolio disputes resolved.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": -1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        14, "Leaks from the coordination meeting fuel further media speculation about local cabinet disputes.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The BJP criticism is ignored by coalition voters, limiting its wider political impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Several key legislators skip the coordination meeting, diluting its positive impact in the press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-09: Belgaum Bagalkot flash floods
nk = f"{short_code}_2004_09_northern_floods"
news_items.append({
    "newsKey": nk, "month": "2004-09",
    "title": "Flash Floods Inundate Villages in Belgaum and Bagalkot (2004-09)",
    "description": "Continuous heavy rainfall in September causes the Krishna river to rise, inundating agricultural tracts and displacing families in Belgaum and Bagalkot. The administration coordinates relief distribution.",
    "issueTags": ["rural", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "northern_floods",
        "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations in Belgaum.",
        "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages to Krishna flood victims.",
        "A joint legislative relief committee is established to supervise rehabilitation work in northern districts.",
        "The District Collector declines to release the official crop loss estimates in the first week for northern districts.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"karnatakaStabilityMemory": -1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        14, "Logistical failures delay the delivery of tents to remote villages, drawing local protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        12, "The criticism leads to minor scuffles at distribution centers, disrupting relief work.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over relief beneficiary lists stall aid distribution in several affected talukas.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-10: Veerappan shot dead Operation Cocoon
nk = f"{short_code}_2004_10_operation_cocoon"
news_items.append({
    "newsKey": nk, "month": "2004-10",
    "title": "Veerappan Shot Dead in Operation Cocoon (2004-10)",
    "description": "In a massive victory for law enforcement, the forest brigand Veerappan is shot dead by the STF in Operation Cocoon. Celebrations erupt in Chamarajanagar and Mysore districts.",
    "issueTags": ["security_crisis", "politics"],
    "weights": {"baseSelectionWeight": 1.3, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "operation_cocoon",
        "The state government congratulates the STF team and announces promotions for key officers involved.",
        "Opposition leaders welcome the news and demand that the state immediately release funds for forest village redevelopment.",
        "All parties pass an assembly resolution appreciating the joint operations of Karnataka and Tamil Nadu STFs.",
        "The DGP office declines to share the specific tactical details of the Operation Cocoon ambush.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaSecurityMemory": 2}, {"karnatakaStabilityMemory": 1}, {"karnatakaStabilityMemory": -1},
        13, "Select promotions trigger minor resentment in the lower ranks of the police force.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The BJP demands are labeled as political posturing, failing to gather wider neutral attention.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Disagreements over the resolution wording delay its introduction in the assembly by several days.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-11: State corporations nomination clash
nk = f"{short_code}_2004_11_corporations_clash"
news_items.append({
    "newsKey": nk, "month": "2004-11",
    "title": "Coalition Allies Clash Over Nominations to State Boards (2004-11)",
    "description": "Friction mounts in the coalition as Congress and JD(S) clash over the nomination of members to profitable state-run corporations and boards. The deadlock delays administrative appointments.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "corporations_clash",
        "CM Dharam Singh holds a coordination meet to negotiate a seat-sharing ratio for the boards.",
        "Opposition BJP leaders claim the boards disputes show the coalition is purely focused on distribution of spoils.",
        "All parties agree to form a joint panel to verify candidate qualifications before board nominations.",
        "The Chief Secretary's office declines to comment on the number of boards currently without chiefs.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": -1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        14, "Leaks from the coordination meeting fuel further media speculation about local cabinet disputes.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The BJP claims are dismissed by coalition supporters, limiting their public impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Liaison panel negotiations stall as both sides trade candidate verification complaints.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-12: Crop loan interest waivers
nk = f"{short_code}_2004_12_interest_waivers"
news_items.append({
    "newsKey": nk, "month": "2004-12",
    "title": "Government Announces Crop Loan Interest Waivers (2004-12)",
    "description": "CM Dharam Singh announces a waiver of interest on crop loans for dryland farmers in drought-hit North Karnataka districts. The announcement aims to mitigate rural economic distress.",
    "issueTags": ["rural", "governance"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "interest_waivers",
        "The Agriculture Department sets up emergency cells to distribute the interest waivers to cooperative societies.",
        "Opposition BJP leaders claim the waivers are delayed and fail to cover non-loanee dryland farmers.",
        "A joint committee is formed to negotiate central drought relief matches and coordinate allocations.",
        "The Cooperative Registrar declines to comment on the number of farmers currently registered for waivers.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaRuralTrustMemory": 2}, {"karnatakaRuralTrustMemory": -1}, {"karnatakaStabilityMemory": -1},
        13, "Logistical bottlenecks delay payouts in remote tribal zones, drawing localized protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The BJP criticism is ignored by farm organizations who welcome the interest waivers, limiting its impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Verification is delayed due to missing land records in the cooperative office, stalling progress.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-12"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005
# 2005-01: Tsunami relief package coastal zones
nk = f"{short_code}_2005_01_tsunami_aid"
news_items.append({
    "newsKey": nk, "month": "2005-01",
    "title": "State Announces Tsunami Relief Package (2005-01)",
    "description": "Karnataka government announces a major relief package and sends medical teams to tsunami-hit coastal zones. The CM coordinates the rehabilitation plan, which includes adopting affected villages.",
    "issueTags": ["governance", "politics"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "tsunami_aid",
        "The state administration coordinates the relief funds and dispatches rehabilitation materials to coastal blocks.",
        "Opposition leaders claim that local dryland welfare funds are being diverted for external political gains.",
        "Both parties agree to a joint resolution appreciating the humanitarian gesture of the state.",
        "The state relief director declines to release the itemized transit costs of the tsunami aid cargo.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": 1}, {"karnatakaRuralTrustMemory": -1}, {"karnatakaStabilityMemory": -1},
        12, "Transit delays hold up cargo trains in neighboring zones, drawing mild local press criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The diversion allegations are dismissed by local civic groups who support the humanitarian aid.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        8, "Minor disputes over dispatch logistics are reported in state warehouse departments.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-02: Siddaramaiah AHINDA conventions
nk = f"{short_code}_2005_02_ahinda_friction"
news_items.append({
    "newsKey": nk, "month": "2005-02",
    "title": "Siddaramaiah Hosts AHINDA Conventions (2005-02)",
    "description": "Deputy CM Siddaramaiah hosts a series of AHINDA (Minorities, Backward Classes, and Dalits) conventions, raising friction with JD(S) supremo Deve Gowda who views it as factional mobilization.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "ahinda_friction",
        "CM Dharam Singh holds a cabinet coordination meet in Bangalore and calls for restraint over public AHINDA conventions.",
        "Opposition BJP leaders call the AHINDA rallies proof that the coalition is completely fragmented.",
        "Congress and JD(S) senior leaders hold a closed-door coordination meeting in Bangalore to resolve the AHINDA dispute.",
        "The state Congress spokesperson declines to comment on reports of seat-sharing disputes inside the unit.",
        {"partyMorale": 1, "corruptionScore": 0, "mediaImage": 1, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": -1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        14, "Leaks from the coordination meeting fuel further media speculation about leadership changes.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The criticism is ignored by voters who view it as standard opposition exploitation of internal issues.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Several key legislators skip the unity meeting, diluting its positive impact in the press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-03: VAT implementation Bangalore strike
nk = f"{short_code}_2005_03_vat_strike"
news_items.append({
    "newsKey": nk, "month": "2005-03",
    "title": "VAT Implementation Triggers Traders' Strike in Bangalore (2005-03)",
    "description": "Value Added Tax (VAT) goes into effect, triggering a statewide strike by trader associations. Shops and commercial establishments remain shut in Bangalore, disrupting local business.",
    "issueTags": ["protest", "economy"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "vat_strike",
        "The CM initiates negotiations with trader leaders and offers a simplified filing process.",
        "Opposition BJP leaders support the traders, demanding a rollback of the VAT system.",
        "A joint government-trader advisory panel is formed to review specific tax slabs and address issues.",
        "The Excise Department declines to comment on the number of businesses currently complying with VAT registration.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"karnatakaStabilityMemory": -1}, {"karnatakaCorruptionMemory": 1}, {"karnatakaStabilityMemory": -1},
        14, "The simplified rules proposal is rejected by union hardliners, extending the business shutdown.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The demands are criticized by consumer groups who argue VAT will reduce middleman price manipulation.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Advisory panel talks break down as trader representatives demand exemption for small retail shops.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-04: Hubli water shortage
nk = f"{short_code}_2005_04_hubli_water"
news_items.append({
    "newsKey": nk, "month": "2005-04",
    "title": "Drinking Water Crisis Reported in Hubli Wards (2005-04)",
    "description": "An intense summer heatwave in April dries up local wells in Hubli, leading to a critical drinking water crisis. Residents in housing colonies protest over irregular municipal tanker supply, demanding immediate relief.",
    "issueTags": ["rural", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "hubli_water",
        "The Public Health Engineering Department releases emergency funds to deploy water tankers and drill borewells.",
        "Opposition leaders lead protests outside PHE offices, accusing the BJP government of failing to prepare.",
        "A joint water task force is formed to manage daily supply allocations to the worst-affected blocks.",
        "The Public Health Engineering Minister declines to give a timeline for restoring piped water supply.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"karnatakaRuralTrustMemory": -1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        14, "Private water tanker operators charge illegal premiums, drawing local public anger and media focus.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        12, "Protests are labeled by the ruling party as creating public panic, limiting their wider impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Task force coordination fails as local block officers report a lack of fuel for water tankers.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-05: Bangalore IT leaders demand ring road
nk = f"{short_code}_2005_05_ring_road"
news_items.append({
    "newsKey": nk, "month": "2005-05",
    "title": "IT Leaders Demand Bangalore Outer Ring Road Upgrades (2005-05)",
    "description": "Prominent IT leaders in Bangalore issue a memorandum demanding immediate execution of the outer ring road projects to check traffic gridlocks. The tech leaders warn of shifting future investments.",
    "issueTags": ["infrastructure", "economy"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "ring_road",
        "The Urban Development Department fast-tracks the outer ring road tender allocations and coordinates clearances.",
        "Opposition leaders call the infrastructure focus a waste of public funds that ignores dryland agriculture.",
        "A joint committee of civic officials and IT leaders is formed to monitor the outer ring road construction quality.",
        "The Bangalore Development Commissioner declines to comment on the project-wise budget allocation details.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": 1}, {"karnatakaRuralTrustMemory": -1}, {"karnatakaStabilityMemory": -1},
        13, "Land acquisition litigation in suburban blocks delays road work, drawing tech industry criticism.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The opposition's criticism fails as rural organizations welcome the improved connectivity to Bangalore hubs.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Committee inspections are delayed by a lack of coordination in the municipal engineering department.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-06: Kumaraswamy raises concerns Congress dominance
nk = f"{short_code}_2005_06_coalition_friction"
news_items.append({
    "newsKey": nk, "month": "2005-06",
    "title": "Kumaraswamy Warns Allies Against Coalition Dominance (2005-06)",
    "description": "JD(S) leader H. D. Kumaraswamy publicly warns the Congress against dominating policy decisions in the coalition, raising speculation of a potential alignment review inside his party.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "coalition_friction",
        "CM Dharam Singh holds a coordination meet and reiterates the need for alliance cooperation.",
        "Opposition BJP leaders state the public bickering shows the state government is completely paralyzed.",
        "Senior leaders from both parties hold a closed-door meeting to project a united front against opposition criticism.",
        "The state BJP spokesperson declines to comment on reports of seat-sharing disputes inside the unit.",
        {"partyMorale": 1, "corruptionScore": 0, "mediaImage": 1, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": -1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        14, "Leaks from the coordination meeting fuel further media speculation about leadership changes.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The criticism is ignored by voters who view it as standard opposition exploitation of internal issues.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Several key legislators skip the unity meeting, diluting its positive impact in the press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-07: Siddaramaiah dismissed Deputy CM
nk = f"{short_code}_2005_07_siddaramaiah_dismissed"
news_items.append({
    "newsKey": nk, "month": "2005-07",
    "title": "Deputy CM Siddaramaiah Dismissed from Cabinet (2005-07)",
    "description": "On the advice of the JD(S) leadership, CM Dharam Singh dismisses Deputy CM Siddaramaiah from the cabinet following his participation in AHINDA rallies. The dismissal triggers intense political instability.",
    "issueTags": ["politics", "governance"],
    "weights": {"baseSelectionWeight": 1.3, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "siddaramaiah_dismissed",
        "The CM announces minor portfolio reallocations to JD(S) nominees to ensure cabinet continuity.",
        "Siddaramaiah and his supporters hold mass rallies in Mysore, calling the dismissal an insult to backward classes.",
        "The assembly holds a special session with all parties agreeing to keep floor debates orderly.",
        "The Governor's office declines to issue a public statement on the cabinet dismissal notifications.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 0, "mediaImage": -3, "publicSupport": -3},
        {"karnatakaStabilityMemory": -2}, {"karnatakaIdentityMemory": 1}, {"karnatakaStabilityMemory": -1},
        15, "Dissident MLAs threaten to withdraw support, raising minor administrative friction.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        13, "Protests by AHINDA workers in Mysore outskirts lead to stone-pelting and curfew warnings.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Bickering over the resolution wording disrupts the first assembly session under the new cabinet.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-08: Krishna basin floods Athani
nk = f"{short_code}_2005_08_athani_floods"
news_items.append({
    "newsKey": nk, "month": "2005-08",
    "title": "Flash Floods in Krishna Basin Inundate Villages in Athani (2005-08)",
    "description": "Continuous heavy rainfall in August causes the Krishna river to overflow, inundating agricultural land and damaging standing crops in Athani. The administration coordinates evacuations.",
    "issueTags": ["rural", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "athani_floods",
        "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations in Athani.",
        "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages to Athani flood victims.",
        "A joint legislative relief committee is established to supervise rehabilitation work specifically in the Athani blocks.",
        "The district collector declines to release the official crop loss estimates in the first week for Athani.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"karnatakaStabilityMemory": -1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        14, "Logistical failures delay the delivery of tents to remote villages, drawing local protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        12, "The criticism leads to minor scuffles at distribution centers, disrupting relief work.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over relief beneficiary lists stall aid distribution in several affected talukas.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-09: Financial irregularities cooperative apex bank
nk = f"{short_code}_2005_09_bank_irregularities"
news_items.append({
    "newsKey": nk, "month": "2005-09",
    "title": "Irregularities Uncovered in Cooperative Apex Bank (2005-09)",
    "description": "A cooperative department audit uncovers major irregularities and illegal credit extensions in the state cooperative apex bank. The opposition BJP demands a judicial probe, alleging favoritism.",
    "issueTags": ["corruption", "rural"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "corruption"},
    "reactionOptions": create_reactions(
        nk, "bank_irregularities",
        "The Cooperative Department suspends the boards of the irregular bank branches and orders a forensic audit.",
        "Opposition BJP leaders demand a judicial probe and stage protests outside bank head offices.",
        "A multi-party legislative subcommittee is formed to draft credit guidelines for cooperative institutions.",
        "The Cooperative Minister declines to comment on the total volume of frozen farmer deposits.",
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaCorruptionMemory": -1}, {"karnatakaCorruptionMemory": 1}, {"karnatakaStabilityMemory": -1},
        15, "The forensic audit is delayed, prolonging the freeze on farmer accounts and drawing public anger.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "Bank protests lead to minor property damage at a rural branch, drawing public disapproval.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Subcommittee talks are slowed down by disagreements over government representation on bank boards.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-10: Suvarna Gramodaya program launch
nk = f"{short_code}_2005_10_suvarna_gramodaya"
news_items.append({
    "newsKey": nk, "month": "2005-10",
    "title": "CM Dharam Singh Launches 'Suvarna Gramodaya' Program (2005-10)",
    "description": "Chief Minister Dharam Singh launches the 'Suvarna Gramodaya' rural development program, setting up special grievance redressal and infrastructure camps. The campaign aims to improve administrative access.",
    "issueTags": ["governance", "rural"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "suvarna_gramodaya",
        "The government releases special budgetary allocations to launch the Suvarna Gramodaya camps across all blocks.",
        "Opposition BJP leaders call the program a rebranding of old schemes and demand clear project timelines.",
        "A joint government-expert advisory board is formed to track the implementation of the Suvarna Gramodaya targets.",
        "The CM's office declines to publish the project-wise funding breakdown for the outreach program.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaRuralTrustMemory": -1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        13, "Budgetary constraints delay project launches in several remote rural blocks.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The BJP criticism is ignored by rural organizations who support the target sectors.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "The advisory board's first review meeting is delayed due to missing department reports.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-11: Mangalore SEZ land protest
nk = f"{short_code}_2005_11_mangalore_sez"
news_items.append({
    "newsKey": nk, "month": "2005-11",
    "title": "Farmers Protest Near Mangalore SEZ Project (2005-11)",
    "description": "Farmers in Mangalore hold demonstrations protesting the land acquisition for a major Special Economic Zone (SEZ) project. The protestors demand fair compensation packages and guarantees of employment.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "land_rights"},
    "reactionOptions": create_reactions(
        nk, "mangalore_sez",
        "The land acquisition officer sets up a verification cell to review compensation claims and job listings for the Mangalore project.",
        "Opposition BJP leaders join the protests, demanding that the land acquisition process be suspended immediately in Mangalore.",
        "A joint committee of land officials and local panchayat chiefs is formed to verify the value of the acquired plots for the Mangalore SEZ.",
        "The District Collector declines to release the total acreage of land scheduled for acquisition.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -2},
        {"karnatakaRuralTrustMemory": 1}, {"karnatakaRuralTrustMemory": -1}, {"karnatakaStabilityMemory": -1},
        14, "Administrative delays stall the verification cell, drawing fresh protests outside the collectorate.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The BJP protests lead to minor traffic blockades, drawing complaints from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Verification is delayed due to missing land records in the revenue office, stalling progress.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-12: By-elections
nk = f"{short_code}_2005_12_byelections"
news_items.append({
    "newsKey": nk, "month": "2005-12",
    "title": "By-Election Results Announced; BJP and Congress Share Seats (2005-12)",
    "description": "Results for high-stakes assembly by-elections are announced. The BJP and Congress win one seat each, reflecting a closely contested political landscape as both sides claim momentum heading into the next year.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "byelections",
        "The BJP welcomes the mandate and vows to focus on rural developmental initiatives.",
        "Opposition Congress leaders claim their win shows strong public rejection of the government's urban policies.",
        "Both parties agree to cooperate on rural road project monitoring committees in the constituencies.",
        "The State Election Commissioner declines to comment on requests to review voting counts in disputed blocks.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"karnatakaStabilityMemory": -1}, {"karnatakaRuralTrustMemory": 1}, {"karnatakaStabilityMemory": -1},
        13, "Disputes over specific block project allocations stall municipal council meetings.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The Congress claims are labeled as exaggerated by political observers, limiting their public impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Disagreements over the tax sharing formula stall the municipal finance reforms.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-12"], "crisisTriggerKey": None, "crisisDuration": 2
})

# Save output
data = {
    "reviewStatus": "draft",
    "scenarioKey": scenario_key,
    "period": {
        "startMonth": "2001-01",
        "endMonth": "2005-12",
        "months": 60
    },
    "sourceNotes": "Government: Congress led by S. M. Krishna CM until May 2004. Then Congress-JD(S) coalition led by Dharam Singh CM through December 2005. Opposition: BJP/JD(S) until May 2004, then BJP. Main issues: Bangalore IT corridor growth, Cauvery river water sharing with Tamil Nadu, H. Nagappa abduction and murder by Veerappan (2002), Operation Cocoon (2004) shooting Veerappan, coalition friction, and Siddaramaiah's AHINDA conventions. Built programmatically matching the schema and calibration constraints.",
    "defaults": {
        "weights": {
            "baseSelectionWeight": 1.0,
            "reactionProfile": "default"
        }
    },
    "newsItems": news_items
}

output_path = Path("seed-data/review/karnataka_2001_news.json")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(json.dumps(data, indent=2))
print("Successfully generated karnataka_2001_news.json with", len(news_items), "news items!")
