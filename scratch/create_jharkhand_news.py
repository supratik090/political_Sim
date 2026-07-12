import json
from pathlib import Path

# Define the scenario metadata
scenario_key = "jharkhand_2001"
short_code = "jh2001"

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
# 2001-01: Asset sharing disputes
nk = f"{short_code}_2001_01_asset_sharing"
news_items.append({
    "newsKey": nk, "month": "2001-01",
    "title": "State Administration disputes Bihar Over Division of Treasury Liabilities (2001-01)",
    "description": "Friction mounts between Jharkhand and Bihar over the allocation of pension liabilities and division of treasury assets. The dispute threatens the fiscal startup of the newly carved state, leading to bureaucratic friction in Ranchi.",
    "issueTags": ["governance", "politics"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "asset_sharing",
        "The Babulal Marandi government petitions the Union Finance Ministry to resolve the division of treasury funds.",
        "Opposition JMM leaders demand a white paper on the state's initial asset liabilities and Bihar's delay tactics.",
        "Both state finance departments agree to set up a bilateral liaison team to divide liabilities smoothly.",
        "The Jharkhand Finance Secretary declines to comment on the state's current cash reserve levels.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandStabilityMemory": -1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        12, "Central intervention is delayed, forcing the state to utilize high-interest overdrafts.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The JMM demand is labeled as pre-election grandstanding by local business groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        8, "Liaison talks break down as Bihar rejects the proposed liability sharing ratio.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-02: Tribal outreach Santhal Pargana
nk = f"{short_code}_2001_02_tribal_outreach"
news_items.append({
    "newsKey": nk, "month": "2001-02",
    "title": "CM Marandi Launches Tribal Welfare Schemes in Santhal Pargana (2001-02)",
    "description": "Chief Minister Babulal Marandi holds a series of mass rallies in Santhal Pargana, announcing accelerated land verification and welfare schemes for Adivasi villages. The outreach aims to counter JMM's influence in the region.",
    "issueTags": ["identity", "rural"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "tribal_outreach",
        "The Revenue Department launches special camps in Dumka to verify tribal land claims and distribute titles.",
        "Opposition leaders claim the welfare schemes are mere paper announcements without budgetary support.",
        "A joint committee of tribal MLAs is formed to monitor the execution of the Santhal Pargana package.",
        "The Welfare Department spokesperson declines to share the district-wise allocations for the new schemes.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandIdentityMemory": 1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "Local land records are found to be missing, stalling the verification camps and drawing protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The JMM criticism fails to gain traction as local tribal councils welcome the welfare announcements.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Committee inspections are delayed by a lack of administrative vehicles in remote blocks.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-03: Panchayat election reservation debate
nk = f"{short_code}_2001_03_panchayat_elections"
news_items.append({
    "newsKey": nk, "month": "2001-03",
    "title": "Panchayat Poll Preparations Stalled Over Tribal Reservation Debate (2001-03)",
    "description": "State election commission preparations for the first panchayat polls face delays due to intense debates over Scheduled Tribe seat reservations. Tribal groups demand exclusive reservation in scheduled areas, while non-tribals demand parity.",
    "issueTags": ["politics", "identity"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "panchayat_elections",
        "The government introduces a bill guaranteeing PESA-compliant reservations in Scheduled Areas.",
        "Opposition JMM leaders demand the immediate scheduling of elections with full Adivasi seat priority.",
        "A multi-party consultative committee is formed to negotiate the reservation quota for non-tribal groups.",
        "The State Election Commission declines to comment on the tentative timeline for scheduling the local body polls.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandIdentityMemory": 1}, {"jharkhandIdentityMemory": -1}, {"jharkhandStabilityMemory": -1},
        14, "Non-tribal organizations stage protests, blocking highways and stalling bill implementation.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        12, "The JMM demand is criticized by OBC organizations as ignoring backward caste populations.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Consultative talks break down as members fail to agree on reservation limits in urban blocks.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-04: Naxalite violence Chatra
nk = f"{short_code}_2001_04_chatra_violence"
news_items.append({
    "newsKey": nk, "month": "2001-04",
    "title": "Naxalite Attack Reported in Chatra District (2001-04)",
    "description": "A group of armed Naxalites attacks a police patrol in the forests of Chatra district, resulting in casualties and loss of weapons. The attack highlights security vulnerabilities in Jharkhand's rural interior.",
    "issueTags": ["security_crisis", "rural"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "chatra_violence",
        "The Home Department deploys special anti-naxal forces to Chatra and strengthens intelligence networks.",
        "Opposition JMM leaders criticize the government, claiming the administration is failing to secure rural roads in Chatra.",
        "A joint assembly resolution is passed condemning the violence and supporting development in forest areas.",
        "The DGP office declines to comment on the specific weapons lost during the Chatra ambush.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": -1, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"jharkhandSecurityMemory": 1}, {"jharkhandStabilityMemory": 1}, {"jharkhandStabilityMemory": -1},
        16, "An operational failure during searches leads to minor civilian harassment, drawing local protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The JMM criticism is labeled as politicizing security, drawing disapproval from police associations.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Developmental funds for Chatra are delayed due to administrative bottlenecks, leaving locals disgruntled.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-05: JMM language education protest
nk = f"{short_code}_2001_05_language_protest"
news_items.append({
    "newsKey": nk, "month": "2001-05",
    "title": "JMM Demands Tribal Language Education in Schools (2001-05)",
    "description": "The opposition JMM launches protests across Ranchi and Dumka, demanding the introduction of Santhali, Mundari, and Kurukh languages in state primary schools. The campaign gains wide support among tribal student unions.",
    "issueTags": ["identity", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "language_protest",
        "The Education Department announces a pilot project to introduce tribal languages in selected primary schools.",
        "JMM leaders stage sit-ins, demanding a formal timeline for implementing language education statewide.",
        "A joint committee of linguists and educators is formed to draft primary school textbooks in Adivasi scripts.",
        "The Education Minister declines to comment on the cost of recruiting tribal language teachers.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -2},
        {"jharkhandIdentityMemory": 1}, {"jharkhandIdentityMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "Lack of standardized scripts for some tribal dialects delays textbook printing, drawing protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The sit-ins disrupt traffic in Ranchi, drawing complaints from commuter organizations.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Linguist committee meetings are delayed by disagreements over script standards for Santhali.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-06: Heavy rains road damage Ranchi
nk = f"{short_code}_2001_06_ranchi_rains"
news_items.append({
    "newsKey": nk, "month": "2001-06",
    "title": "Heavy Monsoon Rains Damage Ranchi Infrastructure (2001-06)",
    "description": "Early monsoon showers cause waterlogging and damage to arterial roads in the capital city of Ranchi. The opposition BJP's coalition partners raise concerns over poor municipal preparation and drainage maintenance.",
    "issueTags": ["infrastructure", "governance"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "ranchi_rains",
        "The Municipal Corporation launches emergency repair works and orders clearing of storm drains in low-lying wards.",
        "Opposition leaders stage protests at waterlogged crossings, accusing the municipal commissioner of corruption.",
        "A joint civic coordination council is formed with representatives from all parties to monitor drainage repair quality.",
        "The Ranchi Mayor declines to release the budget figures allocated for pre-monsoon drain cleaning.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandStabilityMemory": -1}, {"jharkhandStabilityMemory": 1}, {"jharkhandStabilityMemory": -1},
        13, "Substandard patch repairs wash away in the next shower, drawing local press criticism.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        11, "The protests cause minor traffic blocks, drawing complaints from local merchant groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Drainage inspections are delayed by a lack of labor teams in the municipal engineering department.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-07: Farmers seed cost protest
nk = f"{short_code}_2001_07_seed_costs"
news_items.append({
    "newsKey": nk, "month": "2001-07",
    "title": "Farmers Protest Rising Fertilizer Costs (2001-07)",
    "description": "Cultivators in the agricultural blocks of Palamu and Garhwa hold demonstrations, protesting the high prices of quality seeds and urea during the crucial Kharif sowing season. The protests threaten rural economic stability.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "seed_costs",
        "The Agriculture Department releases subsidized seed packets and urea quotas to local cooperative societies.",
        "Opposition leaders join the farm rallies, demanding a complete waiver of seed distribution charges.",
        "A joint assembly committee is established to audit cooperative seed supply chains and check black marketing.",
        "The Cooperative Registrar declines to comment on the volume of urea available in district godowns.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"jharkhandRuralTrustMemory": 1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "Substandard seed distribution in some blocks leads to low germination rates, sparking fresh protests.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        12, "The opposition's demands are labeled as fiscally unfeasible during a revenue deficit.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Audit inspections are delayed by a lack of transport in remote block offices.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-08: Forest department restrictions West Singhbhum
nk = f"{short_code}_2001_08_forest_rights"
news_items.append({
    "newsKey": nk, "month": "2001-08",
    "title": "Forest Restrictions Spark Protests in West Singhbhum (2001-08)",
    "description": "Tribal villagers in West Singhbhum hold protests against new forest department regulations restricting the gathering of dry wood and minor forest produce. The regulations provoke anger over traditional forest rights.",
    "issueTags": ["rural", "identity"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "land_rights"},
    "reactionOptions": create_reactions(
        nk, "forest_rights",
        "The Forest Department issues guidelines to permit traditional gathering of minor produce by local tribal communities.",
        "Opposition JMM leaders support the villagers, demanding the immediate withdrawal of all forest department guards.",
        "A joint committee of forest officials and tribal representatives is formed to draft sustainable forest guidelines.",
        "The Chief Conservator of Forests declines to comment on the number of local villagers booked under forest acts.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -2},
        {"jharkhandIdentityMemory": 1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        15, "Local forest guards ignore the new guidelines, leading to fresh scuffles in remote beats.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        12, "The demands are criticized by conservation groups who warn against unregulated wood cutting.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Joint committee meetings are delayed by the non-participation of environmental NGOs.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-09: Domicile policy draft 1932 khatian
nk = f"{short_code}_2001_09_domicile_policy"
news_items.append({
    "newsKey": nk, "month": "2001-09",
    "title": "Government Releases Draft Domicile Policy Based on 1932 Land Records (2001-09)",
    "description": "The Babulal Marandi cabinet approves a draft domicile policy, prioritizing candidates with ancestors listed in the 1932 khatian land records for district-level government jobs. The policy triggers immediate polarization across the state.",
    "issueTags": ["politics", "identity"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "domicile_policy",
        "The state government defends the policy as a constitutional step to protect indigenous (Moolvasi) rights.",
        "Opposition non-tribal groups organize rallies protesting the policy, calling it discriminatory and illegal.",
        "A joint legislative committee is formed to review the domicile draft and propose balanced job quotas.",
        "The Chief Minister's office declines to comment on the legal validity of the 1932 khatian criteria.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 0, "mediaImage": -3, "publicSupport": -3},
        {"jharkhandIdentityMemory": 2}, {"jharkhandIdentityMemory": -2}, {"jharkhandStabilityMemory": -1},
        16, "Protests by non-tribal organizations lead to road blockades in urban pockets of Dhanbad.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "Counter-rallies by tribal student unions trigger localized scuffles in Ranchi college campuses.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over the definition of 'Moolvasi' stall the legislative committee's first meeting.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-10: Ranchi Bandh anti-domicile
nk = f"{short_code}_2001_10_ranchi_bandh"
news_items.append({
    "newsKey": nk, "month": "2001-10",
    "title": "Anti-Domicile Groups Call for Ranchi Bandh (2001-10)",
    "description": "A coalition of non-tribal student and commercial organizations calls for a Ranchi bandh to protest the 1932 khatian domicile policy. The bandh paralyzes businesses and public transport in the capital.",
    "issueTags": ["identity", "protest"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "ranchi_bandh",
        "The administration deploys heavy police units to ensure peace and detains key protest leaders preventively.",
        "Opposition non-tribal leaders support the bandh, demanding the immediate revocation of the draft policy.",
        "A multi-party delegation meets the Governor to seek a consensus-based resolution to the domicile crisis.",
        "The Home Department spokesperson declines to comment on the number of preventive arrests made in Ranchi.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 0, "mediaImage": -3, "publicSupport": -3},
        {"jharkhandStabilityMemory": -1}, {"jharkhandIdentityMemory": -1}, {"jharkhandStabilityMemory": -1},
        15, "Clashes between pro and anti-domicile groups in Ranchi outskirts lead to stone-pelting and injuries.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The support leads to counter-protests by tribal groups, raising communal temperatures.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Governor's schedule conflicts delay the multi-party delegation's meeting, stalling progress.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-11: First statehood anniversary
nk = f"{short_code}_2001_11_statehood_anniversary"
news_items.append({
    "newsKey": nk, "month": "2001-11",
    "title": "Jharkhand Observes First Anniversary of Statehood (2001-11)",
    "description": "On the first anniversary of Jharkhand's creation, the state government hosts a high-profile celebration in Ranchi, showcasing rural electrification and tribal welfare schemes. Opposition JMM boycotted the official functions.",
    "issueTags": ["politics", "identity"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "statehood_anniversary",
        "The state government fast-tracks the launch of pending rural road and electricity projects.",
        "Opposition JMM leaders state the first year was marked by social division and administrative failure.",
        "All parties agree to participate in a special assembly session to discuss state developmental goals.",
        "The Chief Secretary's office declines to release the total expenditure on the statehood anniversary celebration.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandStabilityMemory": -1}, {"jharkhandIdentityMemory": -1}, {"jharkhandStabilityMemory": -1},
        13, "Contractor shortages delay the road projects in remote blocks, drawing minor media criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The JMM boycott is criticized by tribal groups who welcome the new statehood recognition.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "The special assembly session is disrupted by shouting matches over the domicile policy.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-12: Fiscal deficit bifurcation
nk = f"{short_code}_2001_12_fiscal_deficit"
news_items.append({
    "newsKey": nk, "month": "2001-12",
    "title": "Government Faces Budget Deficit Amid Transition Constraints (2001-12)",
    "description": "Jharkhand's state finance department reports a widening budget deficit, largely attributed to high transition costs and delayed tax reallocations from Bihar. The opposition JMM blames the government's fiscal mismanagement.",
    "issueTags": ["economy", "politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "fiscal_deficit",
        "The Finance Minister announces a fiscal rationalization plan and requests special central grants.",
        "JMM leaders demand a white paper on the state's debt status and criticize the government's tax policies.",
        "A joint legislative committee is formed to identify new revenue sources and non-tax avenues.",
        "The state treasury declines to release the monthly details of public debt accumulation to the media.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandStabilityMemory": -1}, {"jharkhandCorruptionMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "New tax proposals draw protests from local trader associations in Ranchi and Dhanbad.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        11, "The demand is dismissed as politically motivated, failing to gather support from industrial bodies.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "The revenue committee's report is delayed due to partisan gridlock over tax proposals.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-12"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002
# 2002-01: JMM demands implementation of 1932 khatian
nk = f"{short_code}_2002_01_domicile_demands"
news_items.append({
    "newsKey": nk, "month": "2002-01",
    "title": "JMM Demands Immediate Implementation of 1932 Domicile Policy (2002-01)",
    "description": "Opposition JMM leaders demand the immediate implementation of the 1932 khatian domicile policy, accusing the BJP government of deliberately delaying job recruitment. The demand intensifies social division in the state.",
    "issueTags": ["politics", "identity"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "domicile_demands",
        "The CM announces the start of data verification of 1932 land records in all circle offices.",
        "Non-tribal organizations call for counter-protests, warning of state-wide agitations against the policy.",
        "A joint legislative panel is set up to negotiate job quotas and verify candidate definitions.",
        "The Personnel Department declines to comment on the estimated number of vacant job posts.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandIdentityMemory": 1}, {"jharkhandIdentityMemory": -1}, {"jharkhandStabilityMemory": -1},
        14, "Circle offices report major records are missing or mutilated, stalling the verification process.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "Protests block main rail routes, drawing complaints from local merchant groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Committee talks break down over terms of representation, failing to draft any reform guidelines.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-02: Jamshedpur recruitment clashes
nk = f"{short_code}_2002_02_jamshedpur_clashes"
news_items.append({
    "newsKey": nk, "month": "2002-02",
    "title": "Clashes in Jamshedpur Over Local Reservation Policy (2002-02)",
    "description": "Tensions turn violent in Jamshedpur as pro-domicile and anti-domicile student groups clash during a local recruitment drive. Several people are injured, highlighting the growing social rift over job reservations.",
    "issueTags": ["identity", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "jamshedpur_clashes",
        "The state police deploys additional security forces to Jamshedpur and bans assemblies near recruitment centers.",
        "Opposition JMM leaders blame the government's indecisiveness for the social violence and demand immediate rules.",
        "A joint peace committee of local community leaders is formed to restore harmony in Jamshedpur.",
        "The District Magistrate declines to comment on the number of students detained during the scuffles.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": -1, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"jharkhandStabilityMemory": -1}, {"jharkhandIdentityMemory": -1}, {"jharkhandStabilityMemory": -1},
        15, "Security checks result in long traffic queues, drawing protests from local merchant associations.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The JMM statements provoke minor scuffles between party workers, raising communal temperatures.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Local peace talks are boycotted by hardline representatives, failing to resolve the standoff.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-03: State employees strike DA
nk = f"{short_code}_2002_03_employees_strike"
news_items.append({
    "newsKey": nk, "month": "2002-03",
    "title": "State Government Employees Launch Indefinite Strike (2002-03)",
    "description": "Over 2 lakh state government employees in Jharkhand launch an indefinite strike, demanding dearness allowance parity with central government staff. The strike paralyzes administrative offices in Ranchi.",
    "issueTags": ["protest", "economy"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "employees_strike",
        "The Finance Minister promises a phased release of the dearness allowance and initiates talks with employee unions.",
        "JMM opposition leaders support the strike, accusing the government of fiscal mismanagement and empty coffers.",
        "A joint legislative-union panel is formed to negotiate salary adjustments within budget constraints.",
        "The administration invokes the ESMA act to force striking workers back to their departments.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"jharkhandStabilityMemory": -1}, {"jharkhandCorruptionMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "The phased release proposal is rejected by union hardliners, extending the administrative strike.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "Rural voter groups criticize the opposition's stance, arguing employee salaries consume too much tax.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Committee discussions stall as members fail to agree on the definition of base salary scales.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-04: Dhanbad water shortage heatwave
nk = f"{short_code}_2002_04_dhanbad_water"
news_items.append({
    "newsKey": nk, "month": "2002-04",
    "title": "Severe Summer Water Shortage Triggers Rationing in Dhanbad (2002-04)",
    "description": "An intense heatwave in April depletes local reservoirs, forcing Dhanbad's municipal corporation to implement strict water rationing. Residents protest over irregular supply, turning the water scarcity into a political issue.",
    "issueTags": ["rural", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "dhanbad_water",
        "The government deploys municipal water tankers to affected wards and fast-tracks the Maithon water pipeline project.",
        "Opposition leaders stage dharnas outside municipal offices, accusing the BJP administration of water mismanagement.",
        "A joint civic coordination council is formed to oversee equitable water distribution across all wards.",
        "The Dhanbad Municipal Corporation declines to publish the daily water supply schedule for residential areas.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"jharkhandRuralTrustMemory": -1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        15, "Logistical failures result in uneven tanker distribution, sparking minor protests in poorer wards.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "Protests lead to brief traffic disruptions in Dhanbad, drawing criticism from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Tanker coordination is hit by staff shortages, leaving several high-priority wards dry.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-05: Domicile litigation High Court
nk = f"{short_code}_2002_05_domicile_litigation"
news_items.append({
    "newsKey": nk, "month": "2002-05",
    "title": "High Court Hears Challenge to Domicile Policy Validity (2002-05)",
    "description": "The Ranchi High Court begins hearings on several petitions challenging the constitutional validity of the 1932 khatian domicile policy. The legal challenge halts pending government recruitment drives, causing frustration among youth.",
    "issueTags": ["politics", "identity"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "domicile_litigation",
        "The Advocate General defends the state's domicile criteria as necessary for local employment promotion.",
        "Opposition JMM leaders accuse the government of drafting a legally flawed policy that hurts tribal candidates.",
        "A joint committee of legal experts and legislators is formed to study constitutional recruitment options.",
        "The Personnel Department declines to comment on the number of recruitment drives currently suspended.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandIdentityMemory": 1}, {"jharkhandIdentityMemory": -1}, {"jharkhandStabilityMemory": -1},
        14, "The court requests further records, extending the recruitment freeze and drawing critical editorials.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "The criticism is dismissed as political posturing, failing to gather support from student unions.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Legal expert meetings stall due to non-cooperation by former commission members.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-06: Tribal rallies pro reservation
nk = f"{short_code}_2002_06_tribal_rallies"
news_items.append({
    "newsKey": nk, "month": "2002-06",
    "title": "Adivasi Groups Organize Rallies Supporting Domicile Policy (2002-06)",
    "description": "Tribal and indigenous organizations hold massive rallies in Ranchi, demanding the immediate implementation of the 1932 land record criteria. The rallies highlight the rising pro-domicile pressure on the state government.",
    "issueTags": ["identity", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "tribal_rallies",
        "The CM publicly reaffirms the government's commitment to the 1932 khatian records in tribal areas.",
        "Opposition non-tribal leaders accuse the government of capitulating to extremist pressure and polarizing society.",
        "A joint convention of tribal and non-tribal representatives is organized to seek a compromise formula in Ranchi.",
        "The state BJP spokesperson declines to comment on reports of internal cabinet differences over the policy.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandIdentityMemory": 2}, {"jharkhandIdentityMemory": -1}, {"jharkhandStabilityMemory": -1},
        14, "Leaks from the cabinet consultations fuel further media speculation about leadership changes.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The counter-rallies disrupt traffic, drawing complaints from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "The compromise convention is boycotted by hardline representatives, failing to resolve the standoff.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-07: Ranchi riots curfew
nk = f"{short_code}_2002_07_ranchi_riots"
news_items.append({
    "newsKey": nk, "month": "2002-07",
    "title": "Violent Riots Erupt in Ranchi Over Domicile Policy (2002-07)",
    "description": "Clashes between pro and anti-domicile groups turn violent in Ranchi, leading to stone-pelting, arson, and several casualties. The administration imposes a curfew in sensitive sectors of the capital city.",
    "issueTags": ["identity", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "ranchi_riots",
        "The state police enforces strict curfew protocols and deploys rapid action forces to sensitive sectors.",
        "Opposition JMM leaders blame the government's handling of the policy for the loss of lives and demand CM's resignation.",
        "All major parties issue a joint appeal for peace and participate in harmony marches after curfew relaxation.",
        "The Home Minister declines to give a detailed statement in the assembly on the casualties of the riots.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": -1, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"jharkhandStabilityMemory": -2}, {"jharkhandIdentityMemory": -1}, {"jharkhandStabilityMemory": -1},
        16, "Isolated curfew violations spark scuffles in outer wards, drawing national media criticism.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The CM's resignation demands provoke minor scuffles between party workers, raising communal temperatures.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Local peace talks are boycotted by hardline representatives, failing to resolve the standoff.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-08: High Court stays domicile policy
nk = f"{short_code}_2002_08_court_stay"
news_items.append({
    "newsKey": nk, "month": "2002-08",
    "title": "Ranchi High Court Stays Domicile Notification (2002-08)",
    "description": "In a major blow to the government, the Ranchi High Court stays the notification of the 1932 khatian domicile policy, terming the criteria unconstitutional. The ruling forces a suspension of all ongoing district recruitments.",
    "issueTags": ["politics", "governance"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "court_stay",
        "The government announces plans to appeal the stay in the Supreme Court and initiates legal consultations.",
        "Opposition JMM leaders demand that the government call a special assembly session to draft a new law.",
        "A joint committee of legal experts and legislators is formed to draft new recruitment guidelines.",
        "The Personnel Department declines to comment on the number of vacant job posts affected by the stay.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandIdentityMemory": -1}, {"jharkhandIdentityMemory": 1}, {"jharkhandStabilityMemory": -1},
        15, "The Supreme Court declines to lift the stay immediately, leaving the recruitment process frozen.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The JMM demand is criticized as political opportunism, failing to gather support from student unions.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Legal expert meetings stall due to non-cooperation by former commission members.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-09: Drought anxiety Palamu
nk = f"{short_code}_2002_09_palamu_drought"
news_items.append({
    "newsKey": nk, "month": "2002-09",
    "title": "Dry Spell Triggers Drought Anxiety in Palamu (2002-09)",
    "description": "A prolonged dry spell in September depletes local ponds and threatens standing paddy crops in the Palamu division. Cultivators demand immediate state support, raising rural economic distress.",
    "issueTags": ["rural", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "palamu_drought",
        "The Agriculture Department releases emergency relief funds and orders tank repair works in Palamu.",
        "Opposition JMM leaders demand a complete waiver of crop loans for farmers in drought-affected blocks.",
        "A joint assembly panel is established to evaluate crop damage and coordinate relief with central teams.",
        "The Irrigation Department declines to specify the daily water distribution schedule in dry districts.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"jharkhandRuralTrustMemory": 1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "Local administrative delays stall relief disbursement in remote villages, drawing protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The demands are labeled by the ruling party as fiscally irresponsible during a revenue deficit.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The central team's visit is delayed, stalling the disbursement of joint relief funds.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-10: Naxalite ambush Latehar
nk = f"{short_code}_2002_10_latehar_ambush"
news_items.append({
    "newsKey": nk, "month": "2002-10",
    "title": "Naxalite Ambush in Latehar Forest Triggers Security Alert (2002-10)",
    "description": "An armed group of Naxalites ambushes a security force vehicle in the Latehar forest, resulting in several police casualties. The incident prompts the state to launch a high-alert combing operation in the area.",
    "issueTags": ["security_crisis", "rural"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "latehar_ambush",
        "The state police deploys additional special task units and establishes checkpoints on forest roads.",
        "Opposition JMM leaders criticize the government, claiming the administration is failing to secure the Latehar forest tracts.",
        "A joint legislative-police panel is formed to monitor border area security and rehabilitation progress in Latehar.",
        "The DGP office declines to comment on the specific weapons lost during the Latehar ambush.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"jharkhandSecurityMemory": 1}, {"jharkhandStabilityMemory": 1}, {"jharkhandStabilityMemory": -1},
        16, "An operational failure during searches leads to minor civilian harassment, drawing local protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The JMM criticism is labeled as politicizing security, drawing disapproval from police associations.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over search protocols delay the joint panel's field visits.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-11: Speaker coalition rebellion khatian
nk = f"{short_code}_2002_11_coalition_friction"
news_items.append({
    "newsKey": nk, "month": "2002-11",
    "title": "Coalition Partners Criticize CM Marandi's Domicile Stance (2002-11)",
    "description": "Internal friction grows in the ruling coalition as AJSU and Speaker Inder Singh Namdhari criticize Chief Minister Babulal Marandi's stubborn stance on the domicile policy. The dissent threatens the stability of the government.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "coalition_friction",
        "CM Babulal Marandi holds a cabinet coordination meet and reiterates the need for alliance unity.",
        "Opposition JMM leaders call the infighting a proof that the BJP administration is too divided to govern.",
        "Senior BJP leaders hold a closed-door meeting to address concerns and project a united front.",
        "The state BJP spokesperson declines to comment on reports of seat-sharing disputes with AJSU.",
        {"partyMorale": 1, "corruptionScore": 0, "mediaImage": 1, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandStabilityMemory": -1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "Leaks from the coordination meeting fuel further media speculation about leadership changes.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The criticism is ignored by voters who view it as standard opposition exploitation of internal issues.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Several key legislators skip the unity meeting, diluting its positive impact in the press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-12: Seed distribution delays
nk = f"{short_code}_2002_12_seed_delays"
news_items.append({
    "newsKey": nk, "month": "2002-12",
    "title": "Winter Crop Sowing Hit by Seed Distribution Delays (2002-12)",
    "description": "Farmers in Ranchi and Hazaribagh districts protest against delays in cooperative seed and fertilizer distribution for the Rabi crop. The supply bottleneck threatens the winter harvest, causing local agrarian concern.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "seed_delays",
        "The Agriculture Department fast-tracks the shipment of wheat seeds to local cooperative depots.",
        "Opposition JMM leaders stage protests, demanding the immediate clearing of seed dealer dues.",
        "A joint committee is formed to negotiate local fertilizer tariffs and coordinate crop credit packages.",
        "The Cooperative Registrar declines to comment on the number of depots currently without seed stocks.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"jharkhandRuralTrustMemory": 1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "Private seed dealers refuse to release stocks due to government payment delays, stalling delivery.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The protests lead to minor traffic blockades, drawing complaints from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Cooperative board disputes over distribution priority list stall seed allocation in several blocks.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-12"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003
# 2003-01: Cabinet rift CM replacement
nk = f"{short_code}_2003_01_cabinet_rebellion"
news_items.append({
    "newsKey": nk, "month": "2003-01",
    "title": "Rebel Ministers Demand Babulal Marandi's Replacement (2003-01)",
    "description": "Internal rift peaks in the ruling coalition as several rebel ministers openly demand the replacement of CM Babulal Marandi. The ministers accuse the CM of high-handedness and failure to resolve the domicile legal deadlock.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "cabinet_rebellion",
        "CM Babulal Marandi meets central BJP leaders in New Delhi to discuss state coalition stability.",
        "Opposition JMM leaders state the internal BJP rift shows the government is too divided to govern.",
        "Senior coalition leaders hold a closed-door meeting to address concerns and project a united front.",
        "The state BJP spokesperson declines to comment on reports of seat-sharing disputes with rebel ministers.",
        {"partyMorale": 1, "corruptionScore": 0, "mediaImage": 1, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandStabilityMemory": -1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "Leaks from the Delhi meeting fuel further media speculation about leadership changes.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The criticism is ignored by voters who view it as standard opposition exploitation of internal issues.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Several key legislators skip the unity meeting, diluting its positive impact in the press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-02: Shibu Soren campaign tour
nk = f"{short_code}_2003_02_soren_campaign"
news_items.append({
    "newsKey": nk, "month": "2003-02",
    "title": "JMM Chief Shibu Soren Launches State Campaign Tour (2003-02)",
    "description": "JMM Chief Shibu Soren launches a major campaign tour across Jharkhand, targeting the BJP government's developmental record and social divisions. The tour draws high participation from tribal communities in Santhal Pargana.",
    "issueTags": ["politics", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "soren_campaign",
        "BJP leaders organize block-level meetings to highlight the state's welfare and decentralization models.",
        "JMM units organize mass receptions for the yatra, consolidating support in rural constituencies.",
        "Both parties agree to avoid provocative language during campaign rallies to prevent local tensions.",
        "The CM's office declines to comment on the turnout and impact of the Soren campaign tour.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandStabilityMemory": -1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "Internal BJP factional squabbles over campaign allocations undermine their block meetings.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "Logistical coordination failures delay the yatra in Dumka, drawing mild local criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        8, "A minor code violation by a local worker leads to a warning from the Election Commission.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-03: Marandi resigns Arjun Munda CM
nk = f"{short_code}_2003_03_munda_sworn_in"
news_items.append({
    "newsKey": nk, "month": "2003-03",
    "title": "Babulal Marandi Resigns; Arjun Munda Sworn in as CM (2003-03)",
    "description": "Faced with a cabinet rebellion, Babulal Marandi resigns as Chief Minister. Arjun Munda is sworn in as the 2nd Chief Minister of Jharkhand, promising to restore coalition stability and address the domicile policy concerns.",
    "issueTags": ["politics", "governance"],
    "weights": {"baseSelectionWeight": 1.3, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "munda_sworn_in",
        "The new CM Arjun Munda promises continuity in development schemes and pledges to improve rural infrastructure.",
        "Opposition JMM leaders call the change a sign of internal BJP instability and demand fresh elections.",
        "The assembly passes a resolution thanking Babulal Marandi for his service and welcoming the new CM.",
        "The CM's office declines to comment on the ongoing legal proceedings of the domicile policy in court.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandStabilityMemory": -2}, {"jharkhandStabilityMemory": 1}, {"jharkhandStabilityMemory": -1},
        15, "Rebel ministers demand key portfolios in the new cabinet, threatening minor administrative friction.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        13, "The demand for fresh elections is rejected by political observers, limiting the opposition's momentum.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Bickering over the resolution wording disrupts the first assembly session under the new CM.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-04: Munda balanced domicile water funds
nk = f"{short_code}_2003_04_balanced_policy"
news_items.append({
    "newsKey": nk, "month": "2003-04",
    "title": "CM Munda Proposes Balanced Domicile Solution (2003-04)",
    "description": "Chief Minister Arjun Munda announces plans to draft a balanced domicile policy, incorporating views from both tribal and non-tribal groups. The government also releases emergency drinking water funds for dry blocks.",
    "issueTags": ["identity", "governance"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "balanced_policy",
        "The government sets up a cabinet subcommittee to consult with all community representatives.",
        "Opposition JMM leaders criticize the consultation, calling it a delay tactic that ignores Adivasi rights.",
        "A joint convention of tribal and non-tribal representatives is organized to seek a compromise formula for CM Arjun Munda.",
        "The Personnel Department declines to comment on the tentative timeline for completing the consultations.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandIdentityMemory": 1}, {"jharkhandIdentityMemory": -1}, {"jharkhandStabilityMemory": -1},
        13, "Hardline groups boycott the cabinet subcommittee, stalling the consultation process.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The JMM criticism fails to gain traction as local community councils welcome the consultations.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "The compromise convention is boycotted by hardline representatives, failing to resolve the standoff.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-05: VAT protest traders
nk = f"{short_code}_2003_05_vat_protest"
news_items.append({
    "newsKey": nk, "month": "2003-05",
    "title": "Local Traders Protest Against Early VAT Proposals (2003-05)",
    "description": "Trader associations in Ranchi and Jamshedpur hold protests against the state's early proposal to introduce Value Added Tax (VAT). The traders demand simplified tax slabs and postponement of the policy.",
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
        {"jharkhandStabilityMemory": -1}, {"jharkhandCorruptionMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "Training workshops report low attendance, leaving many traders confused about the new system.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "The opposition's demands are dismissed by economists who support modernizing the tax system.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Committee discussions stall as members fail to agree on the definition of tax slabs.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-06: MOUs mining displacement
nk = f"{short_code}_2003_06_mining_mous"
news_items.append({
    "newsKey": nk, "month": "2003-06",
    "title": "Government Signs Mining MOUs Amid Displacement Concerns (2003-06)",
    "description": "The state government signs several MOUs with private and central mining corporations for coal and iron ore extraction. Adivasi rights groups hold protests, warning of massive tribal displacement and ecological damage.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "land_rights"},
    "reactionOptions": create_reactions(
        nk, "mining_mous",
        "The Mines Department announces strict rehabilitation guidelines and promises fair compensation packages.",
        "Opposition JMM leaders join the protests, demanding that the MOUs be tabled in the assembly for public review.",
        "A joint committee of mining officials, Adivasi representatives, and legislators is formed to monitor rehabilitation.",
        "The Mines Minister declines to release the specific land acreage required for the new mining projects.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"jharkhandRuralTrustMemory": -1}, {"jharkhandIdentityMemory": 1}, {"jharkhandStabilityMemory": -1},
        15, "Local protests block initial survey work in West Singhbhum, drawing police intervention.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The demands are criticized as anti-development by business groups who support industrial expansion.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over the committee's representation delay its first review meeting.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-07: Malaria outbreak Simdega
nk = f"{short_code}_2003_07_malaria_outbreak"
news_items.append({
    "newsKey": nk, "month": "2003-07",
    "title": "Malaria Outbreak Reported in Simdega Tribal Blocks (2003-07)",
    "description": "A severe malaria outbreak in the forested blocks of Simdega district causes several casualties. Local health clinics report shortages of anti-malarial drugs, prompting criticism of state rural healthcare.",
    "issueTags": ["rural", "governance"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "malaria_outbreak",
        "The Health Department deploys mobile medical camps and sends emergency drug consignments to Simdega.",
        "Opposition JMM leaders visit the affected blocks, accusing the government of ignoring primary health centers.",
        "A joint legislative-medical panel is formed to review rural healthcare infrastructure and drug supply chains.",
        "The Health Directorate declines to release the official casualty figures from the Simdega outbreak.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"jharkhandRuralTrustMemory": 1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "Mobile camps face fuel shortages, leaving remote tribal hamlets unreached during the peak outbreak.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The JMM statements are labeled as political posturing, failing to gather wider neutral attention.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Committee field visits are delayed by heavy rainfall in southern forest zones.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-08: Subarnarekha floods
nk = f"{short_code}_2003_08_subarnarekha_floods"
news_items.append({
    "newsKey": nk, "month": "2003-08",
    "title": "Subarnarekha River Overflow Displaces Families in East Singhbhum (2003-08)",
    "description": "Continuous heavy rains cause the Subarnarekha river to overflow, inundating low-lying residential areas in East Singhbhum. The administration deploys rescue teams to evacuate affected families.",
    "issueTags": ["rural", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "subarnarekha_floods",
        "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations in East Singhbhum.",
        "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages to Subarnarekha victims.",
        "A joint legislative relief committee is established to supervise rehabilitation work in East Singhbhum.",
        "The district collector declines to release the official crop loss estimates in the first week for East Singhbhum.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"jharkhandStabilityMemory": -1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "Logistical failures delay the delivery of tents to remote villages, drawing local protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        12, "The criticism leads to minor scuffles at distribution centers, disrupting relief work.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over relief beneficiary lists stall aid distribution in several affected talukas.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-09: Hazaribagh coal land protest
nk = f"{short_code}_2003_09_hazaribagh_protest"
news_items.append({
    "newsKey": nk, "month": "2003-09",
    "title": "Tribal Families Protest Land Acquisition in Hazaribagh (2003-09)",
    "description": "Tribal families in Hazaribagh hold demonstrations protesting the acquisition of their agricultural land for a new coal mining project. The protestors demand fair market-value compensation and job guarantees.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "land_rights"},
    "reactionOptions": create_reactions(
        nk, "hazaribagh_protest",
        "The land acquisition officer sets up a verification cell to review compensation claims and job listings in Hazaribagh.",
        "Opposition JMM leaders join the protests, demanding that the land acquisition process be suspended immediately in Hazaribagh.",
        "A joint committee of land officials and local panchayat chiefs is formed to verify the value of the acquired plots in Hazaribagh.",
        "The Hazaribagh District Collector declines to release the total acreage of land scheduled for acquisition.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -2},
        {"jharkhandRuralTrustMemory": 1}, {"jharkhandRuralTrustMemory": -1}, {"jharkhandStabilityMemory": -1},
        14, "Administrative delays stall the verification cell, drawing fresh protests outside the collectorate.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The JMM protests lead to minor traffic blockades, drawing complaints from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Verification is delayed due to missing land records in the revenue office, stalling progress.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-10: Tribal advisory council reforms
nk = f"{short_code}_2003_10_tribal_council"
news_items.append({
    "newsKey": nk, "month": "2003-10",
    "title": "Cabinet Approves Tribal Advisory Council Reforms (2003-10)",
    "description": "The Arjun Munda cabinet approves administrative reforms for the Tribal Advisory Council (TAC), increasing the representation of local community leaders in policy drafting. Adivasi organizations welcome the move.",
    "issueTags": ["governance", "identity"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "tribal_council",
        "The government nominates new TAC members and schedules the first council meet to draft tribal policies.",
        "Opposition JMM leaders claim the reforms are cosmetic and fail to grant real decision-making powers to the council.",
        "A joint committee of assembly members and TAC representatives is formed to oversee policy implementation.",
        "The TAC Secretary declines to release the names of nominees before the formal notification is signed.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandIdentityMemory": 1}, {"jharkhandIdentityMemory": -1}, {"jharkhandStabilityMemory": -1},
        13, "Nominee selection disputes delay the first council meeting, drawing minor press criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The JMM criticism is ignored by tribal councils who welcome the new representatives.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Policy implementation is delayed due to disagreements over resource allocation guidelines.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-11: Giridih railway track Naxal
nk = f"{short_code}_2003_11_giridih_sabotage"
news_items.append({
    "newsKey": nk, "month": "2003-11",
    "title": "Naxalite Sabotage Disrupts Coal Transport in Giridih (2003-11)",
    "description": "Naxalites blow up a section of railway track in Giridih district, disrupting coal transport from local mines to thermal power stations. The incident raises security concerns along key infrastructure corridors.",
    "issueTags": ["security_crisis", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "giridih_sabotage",
        "The state police deploys additional security forces to patrol railway lines and coordinates track repairs with railway teams.",
        "Opposition JMM leaders criticize the government, claiming the administration is failing to secure railway tracks in Giridih.",
        "A joint legislative-railway safety panel is formed to review security measures along coal transport corridors.",
        "The Home Department spokesperson declines to comment on the security protocols established near railway lines.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"jharkhandSecurityMemory": 1}, {"jharkhandStabilityMemory": 1}, {"jharkhandStabilityMemory": -1},
        15, "Security patrols face logistical delays, leaving several remote track sections unmonitored.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The JMM criticism is labeled as politicizing security, drawing disapproval from police associations.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over search protocols delay the joint panel's field visits.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-12: PMGSY road connectivity rural
nk = f"{short_code}_2003_12_rural_roads"
news_items.append({
    "newsKey": nk, "month": "2003-12",
    "title": "Government Launches PMGSY Road Projects in Tribal Areas (2003-12)",
    "description": "The state government launches a series of road projects under the Pradhan Mantri Gram Sadak Yojana (PMGSY), connecting remote tribal villages in Khunti and Gumla to block headquarters. The projects aim to improve market access.",
    "issueTags": ["rural", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "rural_roads",
        "The Rural Development Department releases special funds and fast-tracks contractor bids for the road projects.",
        "Opposition JMM leaders claim the road projects are delayed and fail to cover the remotest forest hamlets.",
        "A joint committee of local MLAs is formed to monitor the execution and quality of the road works.",
        "The Rural Development Minister declines to release the contractor-wise budget allocations for the projects.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandStabilityMemory": -1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        13, "Contractor shortages delay the road projects in remote blocks, drawing minor media criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The JMM criticism is ignored by local councils who welcome the road connectivity, limiting its impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Committee inspections are delayed by a lack of administrative vehicles in remote blocks.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-12"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004
# 2004-01: Cabinet reshuffle AJSU
nk = f"{short_code}_2004_01_cabinet_reshuffle"
news_items.append({
    "newsKey": nk, "month": "2004-01",
    "title": "CM Munda Announces Cabinet Reshuffle (2004-01)",
    "description": "Chief Minister Arjun Munda announces a cabinet reshuffle, allocating key portfolios to AJSU and independent MLAs. The reshuffle aims to pacify coalition partners ahead of the Lok Sabha elections.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "cabinet_reshuffle",
        "The CM allocates key portfolios to coalition partners and announces a coordinated focus on welfare schemes.",
        "Opposition JMM leaders call the reshuffle a compromise that yields two power centers in government.",
        "All parties pass an assembly resolution welcoming the new ministers and promising cooperative work.",
        "The Governor's office declines to share the protocol details of the cabinet swearing-in ceremony.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandStabilityMemory": -1}, {"jharkhandStabilityMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "Leaks from the Delhi meeting fuel further media speculation about leadership changes.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The criticism is ignored by voters who view it as standard opposition exploitation of internal issues.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Several key legislators skip the unity meeting, diluting its positive impact in the press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-02: Industrial subsidies Adityapur
nk = f"{short_code}_2004_02_adityapur_subsidies"
news_items.append({
    "newsKey": nk, "month": "2004-02",
    "title": "Government Announces Subsidies for Adityapur Manufacturing Units (2004-02)",
    "description": "The state government announces a rationalization of local taxes and power tariffs for manufacturing units in the Adityapur industrial area. The policy aims to support local industrial growth.",
    "issueTags": ["infrastructure", "economy"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "adityapur_subsidies",
        "The Finance Department implements tax adjustments and establishes a single-window system for industrial units.",
        "Opposition leaders claim the policy favors large corporate houses at the expense of local small-scale units.",
        "A joint government-industry coordination committee is formed to monitor infrastructure upgrades in the Adityapur zones.",
        "The Industry Minister declines to share the estimated revenue loss due to the new tax concessions for Adityapur.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandStabilityMemory": -1}, {"jharkhandCorruptionMemory": 1}, {"jharkhandStabilityMemory": -1},
        13, "Administrative delays stall the single-window clearance cell, drawing criticism from investors.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "Small-scale industry unions distance themselves from the opposition's protests, weakening the criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Coordination meetings are delayed by disagreements over municipal tax sharing inside the zone.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-03: Lok Sabha campaign
nk = f"{short_code}_2004_03_loksabha_campaign"
news_items.append({
    "newsKey": nk, "month": "2004-03",
    "title": "Lok Sabha Campaign Intensifies Across Jharkhand (2004-03)",
    "description": "Campaigning for the 2004 general elections picks up pace in Jharkhand. The opposition JMM-Congress alliance targets the BJP government's performance, while the BJP focuses on national development themes.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "loksabha_campaign",
        "The BJP campaigns on a platform of developmental progress and the 'India Shining' national theme.",
        "Opposition JMM-Congress leaders focus on rural unemployment and criticize the BJP's economic policies.",
        "Both parties agree to limit loudspeaker usage during late hours to prevent disturbing students during exams.",
        "The state election coordinators decline to comment on reports of internal candidate disputes.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandStabilityMemory": -1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        12, "The 'India Shining' theme fails to connect with poor rural voters, drawing mild press criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "Factional squabbles within the Congress's state unit limit the reach of their rural campaigns.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Local campaign workers violate the loudspeaker timings in Ranchi, drawing warnings from the EC.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-04: Polling Lok Sabha
nk = f"{short_code}_2004_04_loksabha_polls"
news_items.append({
    "newsKey": nk, "month": "2004-04",
    "title": "Voting Held for Lok Sabha Seats in Jharkhand (2004-04)",
    "description": "Polling is held across Jharkhand's 14 Lok Sabha constituencies. Security is tight, particularly in the Naxal-affected districts, to ensure peaceful voting under the supervision of central observers.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "loksabha_polls",
        "The state administration coordinates logistics and deploys home guards to assist central security forces during Lok Sabha voting.",
        "Opposition parties watch voting closely, raising concerns over alleged local administration bias in rural booths during Lok Sabha polls.",
        "All parties issue a joint statement appreciating the peaceful conduct of elections in tribal zones during Lok Sabha voting.",
        "The state election commissioner declines to comment on the final voter turnout figures in the first day of Lok Sabha polls.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandStabilityMemory": -1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        13, "Voting delays due to EVM malfunctions in some booths draw local complaints and press criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The allegations are dismissed by independent observers, neutralizing the opposition's claims.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        8, "Minor disputes over election duty staff accommodation are reported in tribal blocks.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-05: Soren Union Coal Minister
nk = f"{short_code}_2004_05_soren_union"
news_items.append({
    "newsKey": nk, "month": "2004-05",
    "title": "Shibu Soren Appointed Union Coal Minister (2004-05)",
    "description": "Following the UPA's victory at the Centre, JMM Chief Shibu Soren is appointed Union Minister of Coal and Mines. The appointment boosts JMM's political influence in coal-rich Jharkhand.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "soren_union",
        "JMM leaders celebrate the appointment and promise to lobby for increased coal royalty rates for Jharkhand.",
        "BJP state leaders claim that Soren's central role will not resolve the state's ongoing governance issues under Arjun Munda.",
        "Both parties agree to support a joint resolution demanding central coal royalty adjustments for Soren's department.",
        "The jmm state office declines to comment on reports of internal party portfolio discussions for the new cabinet.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandIdentityMemory": 1}, {"jharkhandStabilityMemory": -1}, {"jharkhandStabilityMemory": -1},
        13, "Central approval for the royalty hike is delayed, drawing localized criticism from local unions.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The BJP criticism is ignored by tribal voters who celebrate Soren's cabinet rank, limiting its impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Disagreements over the resolution wording delay its introduction in the assembly by several days.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-06: Supreme Court notice illegal sand mining
nk = f"{short_code}_2004_06_sand_mining"
news_items.append({
    "newsKey": nk, "month": "2004-06",
    "title": "Supreme Court Notices State Over Illegal Sand Mining (2004-06)",
    "description": "The Supreme Court of India issues notices to the state government over unregulated sand mining in river beds. Environmentalists accuse local administrations of colluding with mining mafias.",
    "issueTags": ["governance", "corruption"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "sand_mining",
        "The Mines Department suspends sand lease contracts and orders strict patrolling of river beds.",
        "Opposition JMM leaders demand a judicial inquiry, alleging that local BJP leaders benefit from the sand trade.",
        "A joint committee of municipal and environmental representatives is formed to draft sand mining guidelines.",
        "The Mines Director declines to release the list of contractors currently holding sand leases.",
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandCorruptionMemory": -1}, {"jharkhandCorruptionMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "Enforcement delays trigger fresh complaints from environmental groups, leading to court warnings.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The JMM claims are labeled as politically motivated, failing to gather wider neutral attention.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Committee guidelines are delayed by disagreements over municipal tax sharing inside the zone.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-07: Soren Chirudih warrant resigns
nk = f"{short_code}_2004_07_soren_warrant"
news_items.append({
    "newsKey": nk, "month": "2004-07",
    "title": "Chirudih Warrant Forces Shibu Soren's Resignation (2004-07)",
    "description": "An arrest warrant issued by a Jamtara court in connection with the 1975 Chirudih massacre case forces Shibu Soren to resign as Union Coal Minister. The development triggers a major political controversy in Jharkhand.",
    "issueTags": ["politics", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "soren_warrant",
        "JMM leaders defend Soren, claiming the 30-year-old case is politically resurrected to damage the party.",
        "BJP state leaders demand Soren's immediate arrest and criticize the UPA for shielding a criminal accused.",
        "All parties agree to keep political protests peaceful and prevent clashes in Jamtara district.",
        "The JMM spokesperson declines to comment on Soren's current whereabouts to the media.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandIdentityMemory": 1}, {"jharkhandStabilityMemory": -1}, {"jharkhandStabilityMemory": -1},
        15, "Soren's surrender is delayed, drawing sharp critical national editorials on the rule of law.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        13, "The protests lead to minor traffic blockades, drawing complaints from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Minor clashes between party workers break out on polling day, drawing negative press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-08: Dumka JMM protests soren warrant
nk = f"{short_code}_2004_08_dumka_protests"
news_items.append({
    "newsKey": nk, "month": "2004-08",
    "title": "JMM Holds Mass Protests in Dumka Supporting Soren (2004-08)",
    "description": "JMM supporters organize massive rallies in Dumka following Shibu Soren's surrender to the judicial custody. The protestors call for a Santhal Pargana bandh, accusing the BJP of political vendetta.",
    "issueTags": ["politics", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "dumka_protests",
        "The state police deploys additional security forces to Dumka and maintains peace during the bandh.",
        "JMM leaders lead the rallies, demanding Soren's immediate release and withdrawal of all charges.",
        "All major parties agree to avoid provocative language during campaign rallies to prevent local tensions.",
        "The District Magistrate declines to comment on the security arrangements around the Dumka jail.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandStabilityMemory": -1}, {"jharkhandIdentityMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "Clashes between pro and anti-domicile groups in Dumka outskirts lead to stone-pelting and injuries.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        12, "Logistical coordination failures delay the rallies, drawing mild local criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        8, "A minor code violation by a local worker leads to a warning from the Election Commission.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-09: Sahebganj flash floods
nk = f"{short_code}_2004_09_sahebganj_floods"
news_items.append({
    "newsKey": nk, "month": "2004-09",
    "title": "Flash Floods Displace Families in Sahebganj (2004-09)",
    "description": "Late monsoon rains cause the Ganga river to rise, inundating agricultural tracts and displacing families in Sahebganj district. The administration coordinates relief distribution, amidst complaints of slow response.",
    "issueTags": ["rural", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "sahebganj_floods",
        "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations in Sahebganj.",
        "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages to Ganga flood victims.",
        "A joint legislative relief committee is established to supervise rehabilitation work in Sahebganj.",
        "The district collector declines to release the official crop loss estimates in the first week for Sahebganj.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"jharkhandStabilityMemory": -1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "Logistical failures delay the delivery of tents to remote villages, drawing local protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        12, "The criticism leads to minor scuffles at distribution centers, disrupting relief work.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over relief beneficiary lists stall aid distribution in several affected talukas.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-10: Munda campaign outreach
nk = f"{short_code}_2004_10_munda_outreach"
news_items.append({
    "newsKey": nk, "month": "2004-10",
    "title": "CM Munda Launches Pre-Poll Outreach Tour (2004-10)",
    "description": "Chief Minister Arjun Munda launches a statewide campaign tour, touring districts to inaugurate development projects and highlighting the achievements of road and tribal welfare missions. The tour aims to build pre-election momentum.",
    "issueTags": ["politics", "governance"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "munda_outreach",
        "The state administration fast-tracks the inauguration of pending rural school and road projects.",
        "Opposition leaders call the outreach a waste of public funds and demand the immediate restoration of power supply.",
        "A joint committee is formed to review the code of conduct rules for government-funded inaugurations.",
        "The government spokesperson declines to share the total promotional expenditure of the outreach tour.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandRuralTrustMemory": -1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        13, "Poor road conditions on the CM's route highlight the opposition's campaign, drawing media focus.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The protest is dismissed as routine opposition posturing, failing to gather neutral voter attention.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "The code review is delayed by the non-participation of senior opposition leaders.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-11: Soren returns to Union Cabinet
nk = f"{short_code}_2004_11_soren_returns"
news_items.append({
    "newsKey": nk, "month": "2004-11",
    "title": "Shibu Soren Returns to Union Cabinet After Bail (2004-11)",
    "description": "After securing bail from the High Court in the Chirudih case, Shibu Soren returns to the Union Cabinet as Coal Minister. JMM workers celebrate the return, while BJP calls it a compromise on administrative standards.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "soren_returns",
        "JMM leaders welcome Soren's return and promise to prioritize state mining royalty adjustments.",
        "BJP state leaders claim that Soren's central role will not resolve the state's ongoing governance issues after his return.",
        "Both parties agree to support a joint resolution demanding central coal royalty adjustments after Soren's return.",
        "The jmm state office declines to comment on reports of internal party portfolio discussions after Soren's return.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandIdentityMemory": 1}, {"jharkhandStabilityMemory": -1}, {"jharkhandStabilityMemory": -1},
        13, "Central approval for the royalty hike is delayed, drawing localized criticism from local unions.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The BJP criticism is ignored by tribal voters who celebrate Soren's cabinet rank, limiting its impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Disagreements over the resolution wording delay its introduction in the assembly by several days.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-12: Assembly elections announced
nk = f"{short_code}_2004_12_polls_announced"
news_items.append({
    "newsKey": nk, "month": "2004-12",
    "title": "Election Commission Announces Assembly Polls for Jharkhand (2004-12)",
    "description": "The Election Commission of India announces that the first legislative assembly elections for Jharkhand will be held in three phases in February 2005. The model code of conduct comes into immediate effect.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "polls_announced",
        "The ruling BJP focuses on finalizing its candidate list and preparing its election manifesto.",
        "Opposition JMM-Congress units launch campaigns, targeting the BJP's domicile policy handling.",
        "Both parties agree to a joint liaison committee to resolve model code of conduct disputes quickly.",
        "The party heads decline to comment on the internal selection process for controversial seats.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandStabilityMemory": -1}, {"jharkhandIdentityMemory": 1}, {"jharkhandStabilityMemory": -1},
        13, "Disgruntled BJP leaders threaten to run as independent candidates in several constituencies.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "Factional squabbles in the JMM's Dumka unit delay candidate selection in several seats.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Liaison talks break down as both sides trade code violation accusations before the commission.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-12"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005
# 2005-01: Candidate selection seat sharing
nk = f"{short_code}_2005_01_seat_sharing"
news_items.append({
    "newsKey": nk, "month": "2005-01",
    "title": "Parties Finalize Candidate Lists for Assembly Elections (2005-01)",
    "description": "As the election dates approach, both the BJP-led NDA and the JMM-Congress alliance finalize their seat-sharing arrangements. Independent candidates crop up in several seats, threatening alliance math.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "seat_sharing",
        "The BJP campaigns on its three-year developmental record and stability under Arjun Munda.",
        "Opposition JMM-Congress leaders launch coordinated campaigns, promising Adivasi rights and jobs.",
        "Both parties agree to limit loudspeaker usage during late hours to prevent disturbing students.",
        "The party coordinators decline to comment on reports of seat-sharing disputes.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandStabilityMemory": -1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        13, "Internal BJP factional squabbles over campaign allocations undermine their block meetings.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "Logistical coordination failures delay the JMM campaigns, drawing mild local criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Local campaign workers violate the loudspeaker timings in Ranchi, drawing warnings from the EC.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-02: Voting Assembly elections
nk = f"{short_code}_2005_02_assembly_polls"
news_items.append({
    "newsKey": nk, "month": "2005-02",
    "title": "High Turnout Recorded in Jharkhand Assembly Elections (2005-02)",
    "description": "Jharkhand records a high voter turnout in the three-phase assembly elections held in February. Security is tight, particularly in the Naxal-affected districts, to ensure peaceful voting under central supervision.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "assembly_polls",
        "The state administration coordinates logistics and deploys home guards to assist central security forces during Assembly voting.",
        "Opposition parties watch voting closely, raising concerns over alleged local administration bias in rural booths during Assembly polls.",
        "All parties issue a joint statement appreciating the peaceful conduct of elections in tribal zones during Assembly voting.",
        "The state election commissioner declines to comment on the final voter turnout figures in the first day of Assembly polls.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandStabilityMemory": -1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        13, "Voting delays due to EVM malfunctions in some booths draw local complaints and press criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The allegations are dismissed by independent observers, neutralizing the opposition's claims.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        8, "Minor disputes over election duty staff accommodation are reported in tribal blocks.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-03: Hung assembly Soren sworn in 10 days Munda CM
nk = f"{short_code}_2005_03_government_drama"
news_items.append({
    "newsKey": nk, "month": "2005-03",
    "title": "Political Drama Ends; Arjun Munda Sworn in as CM After Soren Resigns (2005-03)",
    "description": "Following a hung assembly, Governor Sibtey Razi controversially swears in JMM's Shibu Soren as CM on March 2. However, Soren fails to secure majority support and resigns after 10 days; Arjun Munda is sworn back in as CM on March 12.",
    "issueTags": ["politics", "governance"],
    "weights": {"baseSelectionWeight": 1.3, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "government_drama",
        "The returning CM Arjun Munda promises stability and schedules an early vote of confidence in the house.",
        "Opposition JMM leaders state they will act as a strong watchdog in the assembly and protest the governor's treatment.",
        "The assembly holds a special session with all parties agreeing to keep floor debates orderly.",
        "The Governor's office declines to issue a public statement on the controversial swearing-in decisions.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 0, "mediaImage": -3, "publicSupport": -3},
        {"jharkhandStabilityMemory": -2}, {"jharkhandStabilityMemory": 1}, {"jharkhandStabilityMemory": -1},
        15, "Independent MLAs demand key portfolios in the cabinet, threatening minor administrative friction.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        13, "Protests by JMM workers in Ranchi outskirts lead to stone-pelting and curfew warnings.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Bickering over the resolution wording disrupts the first assembly session under the new CM.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-04: VAT strike traders
nk = f"{short_code}_2005_04_vat_strike"
news_items.append({
    "newsKey": nk, "month": "2005-04",
    "title": "VAT Implementation Triggers Traders' Strike in Ranchi (2005-04)",
    "description": "Value Added Tax (VAT) goes into effect on April 1, triggering a statewide strike by trader associations. Shops and commercial establishments remain shut in Ranchi and Dhanbad, disrupting business.",
    "issueTags": ["protest", "economy"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "vat_strike",
        "The CM initiates negotiations with trader leaders and offers a simplified filing process.",
        "Opposition JMM-Congress leaders support the traders, demanding a rollback of the VAT system.",
        "A joint government-trader advisory panel is formed to review specific tax slabs and address issues.",
        "The Excise Department declines to comment on the number of businesses currently complying with VAT registration.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"jharkhandStabilityMemory": -1}, {"jharkhandCorruptionMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "The simplified rules proposal is rejected by union hardliners, extending the business shutdown.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The demands are criticized by consumer groups who argue VAT will reduce middleman price manipulation.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Advisory panel talks break down as trader representatives demand exemption for small retail shops.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-05: Jamshedpur summer water crisis
nk = f"{short_code}_2005_05_jamshedpur_water"
news_items.append({
    "newsKey": nk, "month": "2005-05",
    "title": "Drinking Water Crisis Reported in Jamshedpur Wards (2005-05)",
    "description": "An intense summer heatwave in May dries up local wells in Jamshedpur, leading to a critical drinking water crisis. Residents in housing colonies protest over irregular municipal tanker supply, demanding immediate relief.",
    "issueTags": ["rural", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "jamshedpur_water",
        "The Public Health Engineering Department releases emergency funds to deploy water tankers and drill borewells.",
        "Opposition JMM leaders lead protests outside PHE offices, accusing the BJP government of failing to prepare.",
        "A joint water task force is formed to manage daily supply allocations to the worst-affected blocks.",
        "The Public Health Engineering Minister declines to give a timeline for restoring piped water supply.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"jharkhandRuralTrustMemory": -1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "Private water tanker operators charge illegal premiums, drawing local public anger and media focus.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        12, "Protests are labeled by the ruling party as creating public panic, limiting their wider impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Task force coordination fails as local block officers report a lack of fuel for water tankers.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-06: Latehar naxal parallel courts
nk = f"{short_code}_2005_06_latehar_vigilance"
news_items.append({
    "newsKey": nk, "month": "2005-06",
    "title": "Police Increase Vigilance in Latehar Forest Blocks (2005-06)",
    "description": "Reports of Naxalite groups organizing parallel courts (Jan Adalats) in forested blocks of Latehar prompt the state police to deploy additional task forces. The police establish temporary camps to reassure local villagers.",
    "issueTags": ["security_crisis", "rural"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "latehar_vigilance",
        "The state police deploys additional checkpoints and coordinates vigilance checks with forest patrol units.",
        "Opposition JMM leaders demand that the state immediately release funds to support local primary schools in Latehar.",
        "A joint legislative-police panel is formed to monitor border area security and rehabilitation progress in forest blocks.",
        "The Home Department declines to comment on the specific details of the ongoing security deployments.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"jharkhandSecurityMemory": 1}, {"jharkhandStabilityMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "Leaks from the security operations fuel media speculation, drawing minor party confusion.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The demands are criticized as ignoring national security imperatives, drawing mild media pushback.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Liaison panel meetings are postponed due to border security alerts in neighboring divisions.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-07: Cabinet bickering independent MLAs
nk = f"{short_code}_2005_07_cabinet_friction"
news_items.append({
    "newsKey": nk, "month": "2005-07",
    "title": "CM Munda Faces Demands from Cabinet Allies (2005-07)",
    "description": "Internal friction grows in the ruling coalition as AJSU and independent cabinet ministers demand additional developmental portfolios. The demands trigger speculation of portfolio reallocations to prevent cabinet collapse.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "cabinet_friction",
        "CM Munda holds a cabinet coordination meet and offers minor portfolio reallocations to pacify allies.",
        "Opposition JMM leaders claim the public bickering shows the state government is completely paralyzed.",
        "Senior state BJP leaders hold a closed-door meeting to address concerns and project a united front.",
        "The state BJP spokesperson declines to comment on reports of seat-sharing disputes with independent MLAs.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 1, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandStabilityMemory": -1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "Leaks from the coordination meeting fuel further media speculation about leadership changes.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The criticism is ignored by voters who view it as standard opposition exploitation of internal issues.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Several key legislators skip the unity meeting, diluting its positive impact in the press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-08: Flash floods Damodar river Ramgarh
nk = f"{short_code}_2005_08_ramgarh_floods"
news_items.append({
    "newsKey": nk, "month": "2005-08",
    "title": "Flash Floods in Damodar Basin Damage Crops in Ramgarh (2005-08)",
    "description": "Continuous heavy rainfall in August causes the Damodar river to overflow, inundating low-lying agricultural land and damaging standing crops in Ramgarh district. The administration coordinates evacuations.",
    "issueTags": ["rural", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "ramgarh_floods",
        "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations in Ramgarh.",
        "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages to Damodar victims.",
        "A joint legislative relief committee is established to supervise rehabilitation work in Ramgarh division.",
        "The district collector declines to release the official crop loss estimates in the first week for Ramgarh.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"jharkhandStabilityMemory": -1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        14, "Logistical failures delay the delivery of tents to remote villages, drawing local protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        12, "The criticism leads to minor scuffles at distribution centers, disrupting relief work.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over relief beneficiary lists stall aid distribution in several affected talukas.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-09: Financial irregularities cooperative bank Ranchi
nk = f"{short_code}_2005_09_bank_irregularities"
news_items.append({
    "newsKey": nk, "month": "2005-09",
    "title": "Irregularities Uncovered in Rural Cooperative Banks (2005-09)",
    "description": "A cooperative department audit uncovers major irregularities and illegal credit extensions in local land mortgage banks in Ranchi. The opposition JMM demands a judicial probe, alleging favoritism.",
    "issueTags": ["corruption", "rural"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "corruption"},
    "reactionOptions": create_reactions(
        nk, "bank_irregularities",
        "The Cooperative Department suspends the boards of the irregular banks and orders a forensic audit.",
        "Opposition JMM leaders demand a judicial probe and stage protests outside bank head offices.",
        "A multi-party legislative subcommittee is formed to draft credit guidelines for cooperative institutions.",
        "The Cooperative Minister declines to comment on the total volume of frozen farmer deposits.",
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandCorruptionMemory": -1}, {"jharkhandCorruptionMemory": 1}, {"jharkhandStabilityMemory": -1},
        15, "The forensic audit is delayed, prolonging the freeze on farmer accounts and drawing public anger.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "Bank protests lead to minor property damage at a rural branch, drawing public disapproval.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Subcommittee talks are slowed down by disagreements over government representation on bank boards.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-10: Sarkar Aapke Dwar campaign launch
nk = f"{short_code}_2005_10_outreach_campaign"
news_items.append({
    "newsKey": nk, "month": "2005-10",
    "title": "CM Munda Launches 'Sarkar Aapke Dwar' Campaign (2005-10)",
    "description": "Chief Minister Arjun Munda launches the 'Sarkar Aapke Dwar' (Government at your door) outreach campaign, setting up special grievance redressal camps in rural districts. The campaign aims to improve administrative access.",
    "issueTags": ["governance", "rural"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "outreach_campaign",
        "The government releases special budgetary allocations to launch the grievance redressal camps across all blocks.",
        "Opposition JMM leaders call the program a rebranding of old schemes and demand clear project timelines.",
        "A joint government-expert advisory board is formed to track the implementation of the campaign targets.",
        "The CM's office declines to publish the project-wise funding breakdown for the outreach program.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandRuralTrustMemory": -1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        13, "Budgetary constraints delay project launches in several remote tribal blocks.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The JMM criticism is ignored by rural organizations who support the target sectors.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "The advisory board's first review meeting is delayed due to missing department reports.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-11: NTPC power project displacement
nk = f"{short_code}_2005_11_ntpc_displacement"
news_items.append({
    "newsKey": nk, "month": "2005-11",
    "title": "Tribal Families Protest Near NTPC Power Project (2005-11)",
    "description": "Tribal families in North Karanpura hold demonstrations protesting the land acquisition for a major NTPC power project. The protestors demand fair compensation packages and guarantees of employment.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "land_rights"},
    "reactionOptions": create_reactions(
        nk, "ntpc_displacement",
        "The land acquisition officer sets up a verification cell to review compensation claims and job listings for the NTPC project.",
        "Opposition JMM leaders join the protests, demanding that the land acquisition process be suspended immediately for the NTPC project.",
        "A joint committee of land officials and local panchayat chiefs is formed to verify the value of the acquired plots for the NTPC project.",
        "The District Collector declines to release the total acreage of land scheduled for acquisition.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -2},
        {"jharkhandRuralTrustMemory": 1}, {"jharkhandRuralTrustMemory": -1}, {"jharkhandStabilityMemory": -1},
        14, "Administrative delays stall the verification cell, drawing fresh protests outside the collectorate.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The JMM protests lead to minor traffic blockades, drawing complaints from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Verification is delayed due to missing land records in the revenue office, stalling progress.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-12: By-elections
nk = f"{short_code}_2005_12_byelections"
news_items.append({
    "newsKey": nk, "month": "2005-12",
    "title": "By-Election Results Announced; BJP and JMM Share Seats (2005-12)",
    "description": "Results for high-stakes assembly by-elections are announced. The BJP-led NDA and JMM win one seat each, reflecting a closely contested political landscape as both sides claim momentum heading into the next year.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "byelections",
        "The BJP government welcomes the mandate and vows to focus on rural developmental initiatives.",
        "Opposition JMM leaders claim their win shows strong public rejection of the government's urban policies.",
        "Both parties agree to cooperate on rural road project monitoring committees in the constituencies.",
        "The State Election Commissioner declines to comment on requests to review voting counts in disputed blocks.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"jharkhandStabilityMemory": -1}, {"jharkhandRuralTrustMemory": 1}, {"jharkhandStabilityMemory": -1},
        13, "Disputes over specific block project allocations stall municipal council meetings.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The JMM claims are labeled as exaggerated by political observers, limiting their public impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
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
    "sourceNotes": "Government: BJP coalition led by Babulal Marandi CM until March 2003, then BJP coalition led by Arjun Munda CM until March 2005. Briefly Shibu Soren (JMM) CM for 10 days in March 2005, then Arjun Munda CM returned from March 12, 2005 through the end of the period. Opposition: JMM/Congress until March 2005, then BJP (during 10 days of Soren), then JMM/Congress. Main issues: Domicile policy (1932 khatian land records), tribal land forest rights, Naxalite security threats, and political stability drama of March 2005. Built programmatically matching the schema and calibration constraints.",
    "defaults": {
        "weights": {
            "baseSelectionWeight": 1.0,
            "reactionProfile": "default"
        }
    },
    "newsItems": news_items
}

output_path = Path("seed-data/review/jharkhand_2001_news.json")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(json.dumps(data, indent=2))
print("Successfully generated jharkhand_2001_news.json with", len(news_items), "news items!")
