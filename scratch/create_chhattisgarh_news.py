import json
from pathlib import Path

# Define the scenario metadata
scenario_key = "chhattisgarh_2001"
short_code = "cg2001"

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
    "title": "Chhattisgarh disputes MP Over Division of Electricity Board Assets (2001-01)",
    "description": "Friction mounts between Chhattisgarh and Madhya Pradesh over the division of power board assets and liabilities. The dispute threatens the energy supply stability of the newly carved state, leading to bureaucratic friction in Raipur.",
    "issueTags": ["governance", "politics"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "asset_sharing",
        "The Ajit Jogi government petitions the Union Power Ministry to resolve the division of electricity board funds.",
        "Opposition BJP leaders demand a white paper on the state's initial electricity liabilities and MP's delay tactics.",
        "Both state power departments agree to set up a bilateral liaison team to divide liabilities smoothly.",
        "The Chhattisgarh Power Secretary declines to comment on the state's current energy reserve levels.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        12, "Central intervention is delayed, forcing the state to purchase high-cost power from external grids.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The BJP demand is labeled as pre-election grandstanding by local business groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        8, "Liaison talks break down as MP rejects the proposed liability sharing ratio.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-02: Tribal outreach Bastar
nk = f"{short_code}_2001_02_tribal_outreach"
news_items.append({
    "newsKey": nk, "month": "2001-02",
    "title": "CM Jogi Holds Tribal Conventions in Bastar Region (2001-02)",
    "description": "Chief Minister Ajit Jogi holds a series of mass rallies in Bastar, announcing accelerated land verification and welfare schemes for tribal villages. The outreach aims to counter BJP's influence in the southern tribal belt.",
    "issueTags": ["identity", "rural"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "tribal_outreach",
        "The Revenue Department launches special camps in Bastar to verify tribal land claims and distribute titles.",
        "Opposition BJP leaders claim the welfare schemes are mere paper announcements without budgetary support.",
        "A joint committee of tribal MLAs is formed to monitor the execution of the Bastar welfare package.",
        "The Welfare Department spokesperson declines to share the district-wise allocations for the Bastar schemes.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhIdentityMemory": 1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "Local land records are found to be missing, stalling the verification camps and drawing protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The BJP criticism fails to gain traction as local tribal councils welcome the welfare announcements.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Committee inspections are delayed by a lack of administrative vehicles in remote blocks.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-03: Forest produce policy
nk = f"{short_code}_2001_03_forest_produce"
news_items.append({
    "newsKey": nk, "month": "2001-03",
    "title": "State Lifts Limits on Tendu Leaf Gathering (2001-03)",
    "description": "The state government announces a new forest produce policy, lifting limits on tendu leaf gathering by local cooperative societies. The policy aims to improve the livelihoods of tribal forest dwellers.",
    "issueTags": ["rural", "identity"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "forest_produce",
        "The Forest Department issues guidelines guaranteeing cooperative ownership of minor forest produce.",
        "Opposition leaders demand that the government immediately raise the minimum support price for tendu leaves.",
        "A joint committee of forest officials and cooperative heads is formed to monitor tendu leaf prices.",
        "The Chief Conservator of Forests declines to comment on the volume of tendu leaves collected in state depots.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhIdentityMemory": 1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "Private traders bypass cooperatives and buy leaves at low rates, drawing local protests.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        12, "The demand for higher support prices is labeled as fiscally unfeasible during a revenue deficit.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Committee pricing discussions stall due to disagreements over transportation subsidy caps.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-04: Naxalite violence Dantewada
nk = f"{short_code}_2001_04_dantewada_violence"
news_items.append({
    "newsKey": nk, "month": "2001-04",
    "title": "Naxalite Attack Reported in Dantewada District (2001-04)",
    "description": "A group of armed Naxalites attacks a police patrol in the forests of Dantewada district, resulting in casualties and loss of weapons. The attack highlights security vulnerabilities in Chhattisgarh's southern interior.",
    "issueTags": ["security_crisis", "rural"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "dantewada_violence",
        "The Home Department deploys special anti-naxal forces to Dantewada and strengthens intelligence networks.",
        "Opposition BJP leaders criticize the government, claiming the administration is failing to secure rural roads in Dantewada.",
        "A joint assembly resolution is passed condemning the violence and supporting development in forest areas.",
        "The DGP office declines to comment on the specific weapons lost during the Dantewada ambush.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": -1, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"chhattisgarhSecurityMemory": 1}, {"chhattisgarhStabilityMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        16, "An operational failure during searches leads to minor civilian harassment, drawing local protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The BJP criticism is labeled as politicizing security, drawing disapproval from police associations.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Developmental funds for Dantewada are delayed due to administrative bottlenecks, leaving locals disgruntled.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-05: Local tax protest Raipur
nk = f"{short_code}_2001_05_raipur_tax"
news_items.append({
    "newsKey": nk, "month": "2001-05",
    "title": "Raipur Traders Protest Against New Commercial Taxes (2001-05)",
    "description": "Trader associations in Raipur hold protests against the state's newly introduced entry taxes. The traders demand simplified tax filing and waiver of transit duties.",
    "issueTags": ["economy", "protest"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "raipur_tax",
        "The Excise Department conducts workshops for traders and promises a simplified entry filing process.",
        "Opposition leaders support the traders, demanding a postponement of the new commercial taxes.",
        "A joint legislative-trader coordination panel is formed to review entry tax slabs and address issues.",
        "The Finance Minister declines to comment on the projected revenue impact of the new commercial taxes.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhCorruptionMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "Training workshops report low attendance, leaving many traders confused about the tax process.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "The opposition's demands are dismissed by economists who support modernizing the state's tax system.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Committee discussions stall as members fail to agree on transit tax exemption limits.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-06: Heavy rains road damage
nk = f"{short_code}_2001_06_raipur_rains"
news_items.append({
    "newsKey": nk, "month": "2001-06",
    "title": "Monsoon Rains Damage Raipur-Bilaspur Highway (2001-06)",
    "description": "Early monsoon showers cause waterlogging and damage to arterial sections of the Raipur-Bilaspur highway. The opposition BJP raises concerns over poor municipal preparation and road maintenance.",
    "issueTags": ["infrastructure", "governance"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "raipur_rains",
        "The Public Works Department launches emergency repair works and orders clearing of highway drains.",
        "Opposition leaders stage protests at waterlogged crossings, accusing the highway commissioner of corruption.",
        "A joint civic coordination council is formed with representatives from all parties to monitor repair quality.",
        "The Raipur Mayor declines to release the budget figures allocated for pre-monsoon highway clearing.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhStabilityMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        13, "Substandard patch repairs wash away in the next shower, drawing local press criticism.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        11, "The protests cause minor traffic blocks, drawing complaints from local merchant groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Drainage inspections are delayed by a lack of labor teams in the highway engineering department.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-07: Farmers fertilizer protest Durg
nk = f"{short_code}_2001_07_fertilizer_durg"
news_items.append({
    "newsKey": nk, "month": "2001-07",
    "title": "Farmers Protest Fertilizer Delays in Durg (2001-07)",
    "description": "Cultivators in the agricultural block of Durg hold demonstrations, protesting the high prices and slow distribution of fertilizer during the Kharif sowing season. The delays threaten rural economic stability.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "fertilizer_durg",
        "The Agriculture Department releases subsidized fertilizer quotas to local cooperative societies in Durg.",
        "Opposition leaders join the farm rallies, demanding a complete waiver of distribution charges.",
        "A joint assembly committee is established to audit cooperative fertilizer supply chains in Durg.",
        "The Cooperative Registrar declines to comment on the volume of urea available in Durg godowns.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "Substandard distribution in some blocks leads to crop damage, sparking fresh protests.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        12, "The opposition's demands are labeled as fiscally unfeasible during a revenue deficit.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Audit inspections are delayed by a lack of transport in remote block offices.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-08: Forest department restrictions Sarguja
nk = f"{short_code}_2001_08_forest_rights"
news_items.append({
    "newsKey": nk, "month": "2001-08",
    "title": "Forest Restrictions Spark Protests in Sarguja (2001-08)",
    "description": "Tribal villagers in Sarguja hold protests against new forest department regulations restricting the gathering of dry wood and minor forest produce. The regulations provoke anger over traditional forest rights.",
    "issueTags": ["rural", "identity"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "land_rights"},
    "reactionOptions": create_reactions(
        nk, "forest_rights",
        "The Forest Department issues guidelines to permit traditional gathering of minor produce by local tribal communities in Sarguja.",
        "Opposition BJP leaders support the villagers, demanding the immediate withdrawal of all forest department guards in Sarguja.",
        "A joint committee of forest officials and tribal representatives is formed to draft sustainable forest guidelines in Sarguja.",
        "The Chief Conservator of Forests declines to comment on the number of local villagers booked under forest acts in Sarguja.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -2},
        {"chhattisgarhIdentityMemory": 1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        15, "Local forest guards ignore the new guidelines, leading to fresh scuffles in remote beats of Sarguja.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        12, "The demands are criticized by conservation groups who warn against unregulated wood cutting in Sarguja.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Joint committee meetings are delayed by the non-participation of environmental NGOs.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-09: Reservations policy ST priority
nk = f"{short_code}_2001_09_reservation_policy"
news_items.append({
    "newsKey": nk, "month": "2001-09",
    "title": "Government Outlines ST Reservation Policy for District Jobs (2001-09)",
    "description": "The Ajit Jogi cabinet approves a draft reservation policy, prioritizing Scheduled Tribes for district-level government jobs in scheduled areas. The policy triggers immediate polarization across the state.",
    "issueTags": ["politics", "identity"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "reservation_policy",
        "The state government defends the policy as a constitutional step to protect tribal employment rights.",
        "Opposition non-tribal groups organize rallies protesting the policy, calling it discriminatory and illegal.",
        "A joint legislative committee is formed to review the reservation draft and propose balanced job quotas.",
        "The Chief Minister's office declines to comment on the legal validity of the high reservation criteria.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 0, "mediaImage": -3, "publicSupport": -3},
        {"chhattisgarhIdentityMemory": 2}, {"chhattisgarhIdentityMemory": -2}, {"chhattisgarhStabilityMemory": -1},
        16, "Protests by non-tribal associations lead to road blockades in urban pockets of Raipur.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "Counter-rallies by tribal student unions trigger localized scuffles in Bilaspur college campuses.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over reservation definition details stall the legislative committee's first meeting.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-10: Anti-reservation Bilaspur
nk = f"{short_code}_2001_10_bilaspur_rallies"
news_items.append({
    "newsKey": nk, "month": "2001-10",
    "title": "Anti-Reservation Groups Call for Bilaspur Bandh (2001-10)",
    "description": "A coalition of non-tribal student and commercial organizations calls for a Bilaspur bandh to protest the new district reservation quotas. The bandh paralyzes businesses and public transport in the city.",
    "issueTags": ["identity", "protest"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "bilaspur_rallies",
        "The administration deploys heavy police units to ensure peace and detains key protest leaders preventively in Bilaspur.",
        "Opposition non-tribal leaders support the bandh, demanding the immediate revocation of the draft reservation policy.",
        "A multi-party delegation meets the Governor to seek a consensus-based resolution to the reservation crisis.",
        "The Home Department spokesperson declines to comment on the number of preventive arrests made in Bilaspur.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 0, "mediaImage": -3, "publicSupport": -3},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhIdentityMemory": -1}, {"chhattisgarhStabilityMemory": -1},
        15, "Clashes between pro and anti-quota groups in Bilaspur outskirts lead to stone-pelting and injuries.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The support leads to counter-protests by tribal groups, raising communal temperatures.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Governor's schedule conflicts delay the multi-party delegation's meeting, stalling progress.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-11: First statehood anniversary
nk = f"{short_code}_2001_11_statehood_anniversary"
news_items.append({
    "newsKey": nk, "month": "2001-11",
    "title": "Chhattisgarh Observes First Anniversary of Statehood (2001-11)",
    "description": "On the first anniversary of Chhattisgarh's creation, the state government hosts a high-profile celebration in Raipur, showcasing rural electrification and tribal welfare schemes. Opposition BJP boycotted the official functions.",
    "issueTags": ["politics", "identity"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "statehood_anniversary",
        "The state government fast-tracks the launch of pending rural road and electricity projects in Bastar.",
        "Opposition BJP leaders state the first year was marked by social division and administrative failure.",
        "All parties agree to participate in a special assembly session to discuss state developmental goals.",
        "The Chief Secretary's office declines to release the total expenditure on the statehood anniversary celebration.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhIdentityMemory": -1}, {"chhattisgarhStabilityMemory": -1},
        13, "Contractor shortages delay the road projects in remote blocks, drawing minor media criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The BJP boycott is criticized by tribal groups who welcome the new statehood recognition.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "The special assembly session is disrupted by shouting matches over the ST reservation policy.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-12: Fiscal deficit bifurcation
nk = f"{short_code}_2001_12_fiscal_deficit"
news_items.append({
    "newsKey": nk, "month": "2001-12",
    "title": "Government Faces Budget Deficit Amid Transition Constraints (2001-12)",
    "description": "Chhattisgarh's state finance department reports a widening budget deficit, largely attributed to high transition costs and delayed tax reallocations from MP. The opposition BJP blames the government's fiscal mismanagement.",
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
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhCorruptionMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "New tax proposals draw protests from local trader associations in Raipur and Bilaspur.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        11, "The demand is dismissed as politically motivated, failing to gather support from industrial bodies.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "The revenue committee's report is delayed due to partisan gridlock over tax proposals.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-12"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002
# 2002-01: BJP demands local recruitment quota clarification
nk = f"{short_code}_2002_01_recruitment_demands"
news_items.append({
    "newsKey": nk, "month": "2002-01",
    "title": "BJP Demands Immediate Local Recruitment Quota Clarification (2002-01)",
    "description": "Opposition BJP leaders demand the immediate implementation of the district-level reservation policy, accusing the Jogi government of deliberately delaying job recruitment. The demand intensifies social division in the state.",
    "issueTags": ["politics", "identity"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "recruitment_demands",
        "The CM announces the start of ST reservation verification in all district circle offices.",
        "Non-tribal organizations call for counter-protests, warning of state-wide agitations against the policy.",
        "A joint legislative panel is set up to negotiate job quotas and verify candidate definitions.",
        "The Personnel Department declines to comment on the estimated number of vacant job posts.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhIdentityMemory": 1}, {"chhattisgarhIdentityMemory": -1}, {"chhattisgarhStabilityMemory": -1},
        14, "Circle offices report major records are missing or mutilated, stalling the verification process.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "Protests block main rail routes, drawing complaints from local merchant groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Committee talks break down over terms of representation, failing to draft any reform guidelines.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-02: Jogi engineers defections 12 BJP MLAs
nk = f"{short_code}_2002_02_mla_defections"
news_items.append({
    "newsKey": nk, "month": "2002-02",
    "title": "Ajit Jogi Engineers Defection of 12 BJP MLAs (2002-02)",
    "description": "In a major political maneuver, CM Ajit Jogi brings 12 BJP MLAs into the ruling Congress party, cementing his legislative majority. The defections draw intense criticism from BJP leaders who allege horse-trading.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "mla_defections",
        "The CM welcomes the new MLAs and asserts the defections reflect trust in Congress policies.",
        "Opposition BJP leaders stage sit-ins, demanding a judicial probe into bribery and horse-trading allegations.",
        "A joint multi-party assembly committee is formed to review anti-defection rules and guidelines.",
        "The state Congress office declines to comment on the specific promises made to the defecting MLAs.",
        {"partyMorale": 3, "corruptionScore": 1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhStabilityMemory": -2}, {"chhattisgarhCorruptionMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        15, "Local party workers clash in Raipur following the defection announcements, drawing critical editorials.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        13, "The BJP sit-ins block roads in Raipur, drawing complaints from commuter organizations.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Liaison committee talks break down as members fail to agree on the definition of anti-defection splits.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-03: State employees strike DA
nk = f"{short_code}_2002_03_employees_strike"
news_items.append({
    "newsKey": nk, "month": "2002-03",
    "title": "State Government Employees Launch Indefinite Strike (2002-03)",
    "description": "Over 2 lakh state government employees in Chhattisgarh launch an indefinite strike, demanding dearness allowance parity with central government staff. The strike paralyzes administrative offices in Raipur.",
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
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhCorruptionMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "The phased release proposal is rejected by union hardliners, extending the administrative strike.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "Rural voter groups criticize the opposition's stance, arguing employee salaries consume too much tax.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Committee discussions stall as members fail to agree on the definition of base salary scales.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-04: Korba water shortage heatwave
nk = f"{short_code}_2002_04_korba_water"
news_items.append({
    "newsKey": nk, "month": "2002-04",
    "title": "Severe Summer Water Shortage Triggers Rationing in Korba (2002-04)",
    "description": "An intense heatwave in April depletes local reservoirs, forcing Korba's municipal corporation to implement strict water rationing. Residents protest over irregular supply, turning the water scarcity into a political issue.",
    "issueTags": ["rural", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "korba_water",
        "The government deploys municipal water tankers to affected wards and fast-tracks the Korba water pipeline project.",
        "Opposition leaders stage dharnas outside municipal offices, accusing the Congress administration of water mismanagement.",
        "A joint civic coordination council is formed to oversee equitable water distribution across all wards.",
        "The Korba Municipal Corporation declines to publish the daily water supply schedule for residential areas.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"chhattisgarhRuralTrustMemory": -1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        15, "Logistical failures result in uneven tanker distribution, sparking minor protests in poorer wards.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "Protests lead to brief traffic disruptions in Korba, drawing criticism from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Tanker coordination is hit by staff shortages, leaving several high-priority wards dry.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-05: Reservation litigation High Court
nk = f"{short_code}_2002_05_reservation_litigation"
news_items.append({
    "newsKey": nk, "month": "2002-05",
    "title": "High Court Hears Challenge to District ST Reservation Quotas (2002-05)",
    "description": "The Bilaspur High Court begins hearings on several petitions challenging the constitutional validity of the high ST reservation quotas in state recruitments. The legal challenge halts pending hiring drives, causing frustration among youth.",
    "issueTags": ["politics", "identity"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "reservation_litigation",
        "The Advocate General defends the state's reservation criteria as necessary for tribal employment promotion.",
        "Opposition BJP leaders accuse the government of drafting a legally flawed policy that hurts local candidates.",
        "A joint committee of legal experts and legislators is formed to study constitutional recruitment options.",
        "The Personnel Department declines to comment on the number of recruitment drives currently suspended.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhIdentityMemory": 1}, {"chhattisgarhIdentityMemory": -1}, {"chhattisgarhStabilityMemory": -1},
        14, "The court requests further records, extending the recruitment freeze and drawing critical editorials.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "The criticism is dismissed as political posturing, failing to gather support from student unions.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Legal expert meetings stall due to non-cooperation by former commission members.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-06: Tribal rallies pro reservation Jagdalpur
nk = f"{short_code}_2002_06_tribal_rallies"
news_items.append({
    "newsKey": nk, "month": "2002-06",
    "title": "Adivasi Groups Organize Rallies in Jagdalpur Supporting Quotas (2002-06)",
    "description": "Tribal and indigenous organizations hold massive rallies in Jagdalpur, demanding the immediate implementation of the district-level reservation criteria. The rallies highlight the rising pro-quota pressure in the south.",
    "issueTags": ["identity", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "tribal_rallies",
        "The CM publicly reaffirms the government's commitment to the ST reservation records in Jagdalpur.",
        "Opposition non-tribal leaders accuse the government of capitulating to extremist pressure and polarizing society.",
        "A joint convention of tribal and non-tribal representatives is organized to seek a compromise formula in Jagdalpur.",
        "The state Congress spokesperson declines to comment on reports of internal cabinet differences over the policy.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhIdentityMemory": 2}, {"chhattisgarhIdentityMemory": -1}, {"chhattisgarhStabilityMemory": -1},
        14, "Leaks from the cabinet consultations fuel further media speculation about leadership changes.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The counter-rallies disrupt traffic, drawing complaints from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "The compromise convention is boycotted by hardline representatives, failing to resolve the standoff.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-07: Clashes curfew Bilaspur
nk = f"{short_code}_2002_07_bilaspur_clashes"
news_items.append({
    "newsKey": nk, "month": "2002-07",
    "title": "Clashes in Bilaspur Over Reservation Policy (2002-07)",
    "description": "Clashes between pro and anti-reservation groups turn violent in Bilaspur, leading to stone-pelting, arson, and several casualties. The administration imposes a curfew in sensitive sectors of the city.",
    "issueTags": ["identity", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "bilaspur_clashes",
        "The state police enforces strict curfew protocols and deploys rapid action forces to sensitive sectors in Bilaspur.",
        "Opposition BJP leaders blame the government's handling of the policy for the loss of lives and demand CM's resignation.",
        "All major parties issue a joint appeal for peace and participate in harmony marches after curfew relaxation in Bilaspur.",
        "The Home Minister declines to give a detailed statement in the assembly on the casualties of the Bilaspur riots.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": -1, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"chhattisgarhStabilityMemory": -2}, {"chhattisgarhIdentityMemory": -1}, {"chhattisgarhStabilityMemory": -1},
        16, "Isolated curfew violations spark scuffles in outer wards, drawing national media criticism.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The CM's resignation demands provoke minor scuffles between party workers, raising communal temperatures.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Local peace talks are boycotted by hardline representatives, failing to resolve the standoff.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-08: High Court stays reservation quotas
nk = f"{short_code}_2002_08_court_stay"
news_items.append({
    "newsKey": nk, "month": "2002-08",
    "title": "Bilaspur High Court Stays District Reservation Notification (2002-08)",
    "description": "In a major blow to the government, the Bilaspur High Court stays the notification of the ST-prioritized reservation policy, terming the criteria unconstitutional. The ruling forces a suspension of all ongoing district recruitments.",
    "issueTags": ["politics", "governance"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "court_stay",
        "The government announces plans to appeal the stay in the Supreme Court and initiates legal consultations.",
        "Opposition BJP leaders demand that the government call a special assembly session to draft a new law.",
        "A joint committee of legal experts and legislators is formed to draft new recruitment guidelines.",
        "The Personnel Department declines to comment on the number of vacant job posts affected by the stay.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhIdentityMemory": -1}, {"chhattisgarhIdentityMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        15, "The Supreme Court declines to lift the stay immediately, leaving the recruitment process frozen.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The BJP demand is criticized as political opportunism, failing to gather support from student unions.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Legal expert meetings stall due to non-cooperation by former commission members.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-09: Drought relief Rajnandgaon
nk = f"{short_code}_2002_09_rajnandgaon_drought"
news_items.append({
    "newsKey": nk, "month": "2002-09",
    "title": "Dry Spell Triggers Drought Anxiety in Rajnandgaon (2002-09)",
    "description": "A prolonged dry spell in September depletes local ponds and threatens standing paddy crops in the Rajnandgaon division. Cultivators demand immediate state support, raising rural economic distress.",
    "issueTags": ["rural", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "rajnandgaon_drought",
        "The Agriculture Department releases emergency relief funds and orders tank repair works in Rajnandgaon.",
        "Opposition BJP leaders demand a complete waiver of crop loans for farmers in drought-affected blocks.",
        "A joint assembly panel is established to evaluate crop damage and coordinate relief with central teams.",
        "The Irrigation Department declines to specify the daily water distribution schedule in dry districts.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "Local administrative delays stall relief disbursement in remote villages, drawing protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The demands are labeled by the ruling party as fiscally irresponsible during a revenue deficit.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The central team's visit is delayed, stalling the disbursement of joint relief funds.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-10: Naxalite ambush Dantewada bus
nk = f"{short_code}_2002_10_bus_ambush"
news_items.append({
    "newsKey": nk, "month": "2002-10",
    "title": "Naxalite Bus Ambush in Dantewada Triggers Security Alert (2002-10)",
    "description": "An armed group of Naxalites ambushes a state transport bus in the Dantewada forest, resulting in several civilian casualties. The incident prompts the state to launch a high-alert combing operation in the area.",
    "issueTags": ["security_crisis", "rural"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "bus_ambush",
        "The state police deploys additional special task units and establishes checkpoints on forest roads in Dantewada.",
        "Opposition BJP leaders criticize the government, claiming the administration is failing to secure rural roads.",
        "A joint legislative-police panel is formed to monitor border area security and rehabilitation progress in Dantewada.",
        "The DGP office declines to comment on the specific weapons lost during the Dantewada bus ambush.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"chhattisgarhSecurityMemory": 1}, {"chhattisgarhStabilityMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        16, "An operational failure during searches leads to minor civilian harassment, drawing local protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The BJP criticism is labeled as politicizing security, drawing disapproval from police associations.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over search protocols delay the joint panel's field visits.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-11: VC Shukla factional criticism
nk = f"{short_code}_2002_11_shukla_friction"
news_items.append({
    "newsKey": nk, "month": "2002-11",
    "title": "V.C. Shukla Criticizes CM Jogi's Factional Dominance (2002-11)",
    "description": "Internal friction grows in the ruling Congress as VC Shukla openly criticizes Chief Minister Ajit Jogi's high-handedness and control over the state Congress unit. The dissent threatens party unity ahead of the elections.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "shukla_friction",
        "CM Ajit Jogi holds a cabinet coordination meet and reiterates the need for party unity.",
        "Opposition BJP leaders call the infighting a proof that the Congress administration is too divided to govern.",
        "Senior Congress leaders hold a closed-door meeting to address concerns and project a united front.",
        "The state Congress spokesperson declines to comment on reports of seat-sharing disputes with VC Shukla.",
        {"partyMorale": 1, "corruptionScore": 0, "mediaImage": 1, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "Leaks from the coordination meeting fuel further media speculation about leadership changes.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The criticism is ignored by voters who view it as standard opposition exploitation of internal issues.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Several key legislators skip the unity meeting, diluting its positive impact in the press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-12: Winter seed supply delays
nk = f"{short_code}_2002_12_seed_delays"
news_items.append({
    "newsKey": nk, "month": "2002-12",
    "title": "Winter Crop Sowing Hit by Seed Distribution Delays (2002-12)",
    "description": "Farmers in Raipur and Durg districts protest against delays in cooperative seed and fertilizer distribution for the Rabi crop. The supply bottleneck threatens the winter harvest, causing local agrarian concern.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "seed_delays",
        "The Agriculture Department fast-tracks the shipment of wheat seeds to local cooperative depots.",
        "Opposition BJP leaders stage protests, demanding the immediate clearing of seed dealer dues.",
        "A joint committee is formed to negotiate local fertilizer tariffs and coordinate crop credit packages.",
        "The Cooperative Registrar declines to comment on the number of depots currently without seed stocks.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "Private seed dealers refuse to release stocks due to government payment delays, stalling delivery.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The protests lead to minor traffic blockades, drawing complaints from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Cooperative board disputes over distribution priority list stall seed allocation in several blocks.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-12"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003
# 2003-01: NCP Jaggi murder case Raipur
nk = f"{short_code}_2003_01_jaggi_murder"
news_items.append({
    "newsKey": nk, "month": "2003-01",
    "title": "NCP Leader Ram Avtar Jaggi Murdered in Raipur (2003-01)",
    "description": "In a shocking development, state NCP treasurer Ram Avtar Jaggi is shot dead in Raipur. Opposition BJP and NCP leaders immediately demand a CBI probe, alleging the involvement of senior Congress leaders.",
    "issueTags": ["politics", "corruption"],
    "weights": {"baseSelectionWeight": 1.3, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "jaggi_murder",
        "The state government orders a high-level police probe and promises to capture the culprits quickly.",
        "Opposition BJP and NCP leaders call for a state-wide bandh, accusing CM Jogi's inner circle of conspiracy.",
        "A joint assembly panel is established to review security protocols for political leaders in the capital.",
        "The Raipur Police Commissioner declines to share the details of suspects detained for the murder.",
        {"partyMorale": 1, "corruptionScore": 1, "mediaImage": 1, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"chhattisgarhStabilityMemory": -2}, {"chhattisgarhCorruptionMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        16, "Police investigation delays fuel media speculation, drawing national press criticism.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The bandh turns violent in Raipur, leading to minor clashes and public property damage.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Panel discussions are disrupted by shouting matches over political victimization claims.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-02: VC Shukla joins NCP
nk = f"{short_code}_2003_02_shukla_ncp"
news_items.append({
    "newsKey": nk, "month": "2003-02",
    "title": "VC Shukla Resigns Congress, Joins NCP (2003-02)",
    "description": "Veteran leader Vidya Charan Shukla resigns from the Congress and joins the NCP, splitting the Congress vote bank. The move significantly alters the political calculus ahead of the assembly elections.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "shukla_ncp",
        "Congress leaders downplay the resignation, claiming party unity remains solid under Ajit Jogi.",
        "NCP and BJP units welcome the move, predicting a complete rout of the Congress in the upcoming polls.",
        "Both parties agree to focus their campaigns on developmental performance rather than personal attacks.",
        "The state Congress office declines to comment on reports of seat-sharing talks with minor allies.",
        {"partyMorale": 1, "corruptionScore": 0, "mediaImage": 1, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "Leaks about candidate selections fuel further media speculation about local party dissent.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "The BJP predictions are dismissed by voters who view them as standard pre-election posturing.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Local campaign workers violate the code of conduct, drawing warnings from the EC.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-03: BJP Parivartan Yatra
nk = f"{short_code}_2003_03_parivartan_yatra"
news_items.append({
    "newsKey": nk, "month": "2003-03",
    "title": "BJP Launches State-Wide Parivartan Yatra (2003-03)",
    "description": "The opposition BJP launches a state-wide 'Parivartan Yatra' (Change Tour) targeting the Jogi government's corruption and law and order record. The yatra draws large crowds in rural Raipur and Bilaspur divisions.",
    "issueTags": ["politics", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "parivartan_yatra",
        "Congress leaders organize block-level rallies to highlight the state's infrastructure and welfare achievements.",
        "BJP units organize mass receptions for the yatra, consolidating support in rural constituencies.",
        "Both parties agree to avoid provocative language during campaign rallies to prevent local tensions.",
        "The CM's office declines to comment on the turnout and impact of the BJP yatra.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "Internal Congress factional squabbles over rally allocations undermine their block meetings.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "Logistical coordination failures delay the yatra in Raipur, drawing mild local criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        8, "A minor code violation by a local worker leads to a warning from the Election Commission.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-04: Jogi borewell subsidies water funds
nk = f"{short_code}_2003_04_water_subsidies"
news_items.append({
    "newsKey": nk, "month": "2003-04",
    "title": "CM Jogi Announces Borewell Subsidies for Farmers (2003-04)",
    "description": "Chief Minister Ajit Jogi announces plans to subsidize borewell drilling and pump sets for farmers in dry districts. The government also releases emergency drinking water funds for Raipur municipal areas.",
    "issueTags": ["rural", "governance"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "water_subsidies",
        "The government sets up a block-level grievance cell to fast-track borewell subsidies to poor farmers.",
        "Opposition BJP leaders criticize the announcement, calling it a pre-poll bribe that ignores long-term canal irrigation.",
        "A joint assembly committee is established to audit borewell subsidy allocations and ensure fair distribution.",
        "The Agriculture Department declines to specify the district-wise allocations for the pump set subsidies.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhRuralTrustMemory": -1}, {"chhattisgarhStabilityMemory": -1},
        13, "Substandard pump distribution in some blocks leads to low efficiency, sparking fresh protests.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        11, "The BJP criticism fails to gain traction as local farmer councils welcome the pump subsidies.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Audit inspections are delayed by a lack of transport in remote block offices.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-05: VAT protest traders
nk = f"{short_code}_2003_05_vat_protest"
news_items.append({
    "newsKey": nk, "month": "2003-05",
    "title": "Local Traders Protest Against Early VAT Proposals (2003-05)",
    "description": "Trader associations in Raipur and Bilaspur hold protests against the state's early proposal to introduce Value Added Tax (VAT). The traders demand simplified tax slabs and postponement of the policy.",
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
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhCorruptionMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "Training workshops report low attendance, leaving many traders confused about the new system.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "The opposition's demands are dismissed by economists who support modernizing the tax system.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Committee discussions stall as members fail to agree on the definition of tax slabs.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-06: MOUs industrialization displacement
nk = f"{short_code}_2003_06_steel_mous"
news_items.append({
    "newsKey": nk, "month": "2003-06",
    "title": "Government Signs Steel Plant MOUs Amid Displacement Fears (2003-06)",
    "description": "The state government signs several MOUs with private steel and power corporations for land acquisition in Raigarh. Tribal rights groups hold protests, warning of massive agricultural land displacement.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "land_rights"},
    "reactionOptions": create_reactions(
        nk, "steel_mous",
        "The Mines Department announces strict rehabilitation guidelines and promises fair compensation packages in Raigarh.",
        "Opposition BJP leaders join the protests, demanding that the MOUs be tabled in the assembly for public review.",
        "A joint committee of mining officials, tribal representatives, and legislators is formed to monitor rehabilitation in Raigarh.",
        "The Industry Minister declines to release the specific land acreage required for the new steel projects.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"chhattisgarhRuralTrustMemory": -1}, {"chhattisgarhIdentityMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        15, "Local protests block initial survey work in Raigarh, drawing police intervention.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The demands are criticized as anti-development by business groups who support industrial expansion.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over the committee's representation delay its first review meeting.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-07: Gastroenteritis Sarguja
nk = f"{short_code}_2003_07_gastro_outbreak"
news_items.append({
    "newsKey": nk, "month": "2003-07",
    "title": "Gastroenteritis Outbreak Reported in Sarguja Tribal Hamlets (2003-07)",
    "description": "A severe gastroenteritis outbreak in the forested blocks of Sarguja district causes several casualties. Local health clinics report shortages of clean drinking water and emergency medicines.",
    "issueTags": ["rural", "governance"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "gastro_outbreak",
        "The Health Department deploys mobile medical camps and sends emergency drug consignments to Sarguja.",
        "Opposition BJP leaders visit the affected blocks, accusing the government of ignoring primary health centers.",
        "A joint legislative-medical panel is formed to review rural healthcare infrastructure and drug supply chains.",
        "The Health Directorate declines to release the official casualty figures from the Sarguja outbreak.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "Mobile camps face fuel shortages, leaving remote tribal hamlets unreached during the peak outbreak.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The BJP statements are labeled as political posturing, failing to gather wider neutral attention.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Committee field visits are delayed by heavy rainfall in southern forest zones.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-08: Mahanadi floods Dhamtari
nk = f"{short_code}_2003_08_mahanadi_floods"
news_items.append({
    "newsKey": nk, "month": "2003-08",
    "title": "Mahanadi River Overflow Displaces Families in Dhamtari (2003-08)",
    "description": "Continuous heavy rains cause the Mahanadi river to overflow, inundating low-lying residential areas in Dhamtari. The administration deploys rescue teams to evacuate affected families.",
    "issueTags": ["rural", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "mahanadi_floods",
        "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations in Dhamtari.",
        "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages to Mahanadi victims.",
        "A joint legislative relief committee is established to supervise rehabilitation work in Dhamtari division.",
        "The district collector declines to release the official crop loss estimates in the first week for Dhamtari.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "Logistical failures delay the delivery of tents to remote villages, drawing local protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        12, "The criticism leads to minor scuffles at distribution centers, disrupting relief work.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over relief beneficiary lists stall aid distribution in several affected talukas.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-09: Korba coal land acquisition
nk = f"{short_code}_2003_09_korba_protest"
news_items.append({
    "newsKey": nk, "month": "2003-09",
    "title": "Tribal Families Protest Land Acquisition in Korba (2003-09)",
    "description": "Tribal families in Korba hold demonstrations protesting the acquisition of their agricultural land for a new coal mining project. The protestors demand fair market-value compensation and job guarantees.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "land_rights"},
    "reactionOptions": create_reactions(
        nk, "korba_protest",
        "The land acquisition officer sets up a verification cell to review compensation claims and job listings in Korba.",
        "Opposition BJP leaders join the protests, demanding that the land acquisition process be suspended immediately in Korba.",
        "A joint committee of land officials and local panchayat chiefs is formed to verify the value of the acquired plots in Korba.",
        "The Korba District Collector declines to release the total acreage of land scheduled for acquisition.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -2},
        {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhRuralTrustMemory": -1}, {"chhattisgarhStabilityMemory": -1},
        14, "Administrative delays stall the verification cell, drawing fresh protests outside the collectorate.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The BJP protests lead to minor traffic blockades, drawing complaints from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Verification is delayed due to missing land records in the revenue office, stalling progress.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-10: Election dates announced
nk = f"{short_code}_2003_10_polls_announced"
news_items.append({
    "newsKey": nk, "month": "2003-10",
    "title": "Election Commission Announces Assembly Polls for Chhattisgarh (2003-10)",
    "description": "The Election Commission of India announces that the first legislative assembly elections for Chhattisgarh will be held in December 2003. The model code of conduct comes into immediate effect.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "polls_announced",
        "The ruling Congress focuses on finalizing its candidate list and preparing its election manifesto.",
        "Opposition BJP units launch campaigns, targeting the Congress's corruption and law and order record.",
        "Both parties agree to a joint liaison committee to resolve model code of conduct disputes quickly.",
        "The party heads decline to comment on the internal selection process for controversial seats.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhIdentityMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        13, "Disgruntled Congress leaders threaten to run as independent candidates in several constituencies.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "Factional squabbles in the BJP's Raipur unit delay candidate selection in several seats.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Liaison talks break down as both sides trade code violation accusations before the commission.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-11: Campaigning elections
nk = f"{short_code}_2003_11_campaigning"
news_items.append({
    "newsKey": nk, "month": "2003-11",
    "title": "High-Stakes Assembly Campaigns Peak in Chhattisgarh (2003-11)",
    "description": "Campaigning for the 90 assembly seats in Chhattisgarh reaches a fever pitch. BJP and Congress clash over the legacy of the first statehood government, with high voter turnouts anticipated.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "campaigning",
        "Congress campaigns on its state-building records and rural electrification schemes.",
        "Opposition BJP leaders launch coordinated campaigns, promising clean governance and ST reservations.",
        "Both parties agree to limit loudspeaker usage during late hours to avoid disturbing students.",
        "The party coordinators decline to comment on reports of seat-sharing disputes.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        13, "Internal Congress factional squabbles over campaign allocations undermine their block meetings.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "Logistical coordination failures delay the BJP campaigns, drawing mild local criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Local campaign workers violate the loudspeaker timings in Raipur, drawing warnings from the EC.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-12: BJP victory Raman Singh sworn in
nk = f"{short_code}_2003_12_bjp_victory"
news_items.append({
    "newsKey": nk, "month": "2003-12",
    "title": "BJP Wins Assembly Elections; Raman Singh Sworn in as CM (2003-12)",
    "description": "The BJP secures a majority in the assembly, winning 50 out of 90 seats. Raman Singh is sworn in as the Chief Minister of Chhattisgarh, promising to reform public services and tackle Left-wing extremism.",
    "issueTags": ["politics", "governance"],
    "weights": {"baseSelectionWeight": 1.3, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "bjp_victory",
        "The new CM Raman Singh promises continuity in development and pledges to reform the food distribution networks.",
        "Opposition Congress leaders state they will act as a strong watchdog in the assembly and protect local welfare.",
        "The assembly passes a resolution thanking the electors and welcoming the new CM Raman Singh.",
        "The CM's office declines to comment on reports of pending legal queries regarding the previous Jogi cabinet.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhStabilityMemory": -2}, {"chhattisgarhStabilityMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        15, "Rebel MLAs demand key portfolios in the new cabinet, threatening minor administrative friction.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        13, "Protests by Congress workers in Raipur outskirts lead to stone-pelting and curfew warnings.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Bickering over the resolution wording disrupts the first assembly session under the new CM.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-12"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004
# 2004-01: Raman Singh wins Dongargaon by-election
nk = f"{short_code}_2004_01_dongargaon_byelection"
news_items.append({
    "newsKey": nk, "month": "2004-01",
    "title": "CM Raman Singh Wins Dongargaon By-Election (2004-01)",
    "description": "Chief Minister Raman Singh wins the Dongargaon assembly by-election with a comfortable margin, cementing his mandate as leader of the BJP legislative party and entry into the assembly.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "dongargaon_byelection",
        "The BJP welcomes the mandate and vows to focus on rural developmental initiatives in Dongargaon.",
        "Opposition Congress leaders claim the win was achieved through government machinery and resource mobilization.",
        "Both parties agree to cooperate on rural road project monitoring committees in the Dongargaon division.",
        "The State Election Commissioner declines to comment on requests to review voting counts in disputed Dongargaon blocks.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        13, "Disputes over specific block project allocations stall municipal council meetings.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The Congress claims are labeled as exaggerated by political observers, limiting their public impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Disagreements over the tax sharing formula stall the municipal finance reforms.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-02: Small manufacturing subsidies Urla
nk = f"{short_code}_2004_02_urla_subsidies"
news_items.append({
    "newsKey": nk, "month": "2004-02",
    "title": "Government Announces Subsidies for Urla Manufacturing Units (2004-02)",
    "description": "The state government announces a rationalization of local taxes and power tariffs for manufacturing units in the Urla industrial area. The policy aims to support local industrial growth.",
    "issueTags": ["infrastructure", "economy"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "urla_subsidies",
        "The Finance Department implements tax adjustments and establishes a single-window system for Urla units.",
        "Opposition leaders claim the policy favors large corporate houses at the expense of local small-scale units.",
        "A joint government-industry coordination committee is formed to monitor infrastructure upgrades in the Urla zones.",
        "The Industry Minister declines to share the estimated revenue loss due to the new tax concessions for Urla.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhCorruptionMemory": 1}, {"chhattisgarhStabilityMemory": -1},
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
    "title": "Lok Sabha Campaign Intensifies Across Chhattisgarh (2004-03)",
    "description": "Campaigning for the 2004 general elections picks up pace in Chhattisgarh. The opposition Congress targets the BJP government's performance, while the BJP focuses on national development themes.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "loksabha_campaign",
        "The BJP campaigns on a platform of developmental progress and the 'India Shining' national theme.",
        "Opposition Congress leaders focus on rural unemployment and criticize the BJP's economic policies.",
        "Both parties agree to limit loudspeaker usage during late hours to prevent disturbing students during exams.",
        "The state election coordinators decline to comment on reports of internal candidate disputes.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        12, "The 'India Shining' theme fails to connect with poor rural voters, drawing mild press criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "Factional squabbles within the Congress's state unit limit the reach of their rural campaigns.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Local campaign workers violate the loudspeaker timings in Raipur, drawing warnings from the EC.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-04: Polling Lok Sabha
nk = f"{short_code}_2004_04_loksabha_polls"
news_items.append({
    "newsKey": nk, "month": "2004-04",
    "title": "Voting Held for Lok Sabha Seats in Chhattisgarh (2004-04)",
    "description": "Polling is held across Chhattisgarh's 11 Lok Sabha constituencies. Security is tight, particularly in the Naxal-affected districts, to ensure peaceful voting under the supervision of central observers.",
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
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        13, "Voting delays due to EVM malfunctions in some booths draw local complaints and press criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The allegations are dismissed by independent observers, neutralizing the opposition's claims.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        8, "Minor disputes over election duty staff accommodation are reported in tribal blocks.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-05: PDS rice reforms launch
nk = f"{short_code}_2004_05_pds_reforms"
news_items.append({
    "newsKey": nk, "month": "2004-05",
    "title": "Government Launches Structural Reforms of PDS (2004-05)",
    "description": "Chief Minister Raman Singh announces major structural reforms for the Public Distribution System (PDS), aiming to eliminate middlemen and ensure subsidized rice reaches tribal families. The reform is hailed as a major social initiative.",
    "issueTags": ["rural", "governance"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "pds_reforms",
        "The Food Department implements computerization of ration cards and expands grain subsidies in tribal blocks.",
        "Opposition Congress leaders claim the reforms are a rebranding of central schemes without local budget support.",
        "A joint assembly panel is established to audit PDS grain warehouses and prevent black marketing.",
        "The Food Secretary declines to comment on the volume of rice currently allocated for local distribution.",
        {"partyMorale": 3, "corruptionScore": -1, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhRuralTrustMemory": 2}, {"chhattisgarhRuralTrustMemory": -1}, {"chhattisgarhStabilityMemory": -1},
        13, "Ration card enrollment system errors delay grain distribution in remote villages, drawing minor protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The Congress criticism fails to gain traction as local tribal panchayats welcome the grain quotas.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Audit inspections are delayed by a lack of transport in remote block offices.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-06: Illegal sand mining Bilaspur
nk = f"{short_code}_2004_06_sand_mining"
news_items.append({
    "newsKey": nk, "month": "2004-06",
    "title": "High Court Notice Over Illegal Sand Mining in Bilaspur (2004-06)",
    "description": "The Bilaspur High Court issues notices to the state government over unregulated sand mining in local river beds. Environmentalists accuse local administrations of colluding with mining mafias.",
    "issueTags": ["governance", "corruption"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "sand_mining",
        "The Mines Department suspends sand lease contracts and orders strict patrolling of Bilaspur river beds.",
        "Opposition Congress leaders demand a judicial inquiry, alleging that local BJP leaders benefit from the sand trade.",
        "A joint committee of municipal and environmental representatives is formed to draft sand mining guidelines in Bilaspur.",
        "The Mines Director declines to release the list of contractors currently holding sand leases in Bilaspur.",
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhCorruptionMemory": -1}, {"chhattisgarhCorruptionMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "Enforcement delays trigger fresh complaints from environmental groups, leading to court warnings.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The Congress claims are labeled as politically motivated, failing to gather wider neutral attention.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Committee guidelines are delayed by disagreements over municipal tax sharing inside the zone.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-07: Bailadila mining displacement
nk = f"{short_code}_2004_07_bailadila_displacement"
news_items.append({
    "newsKey": nk, "month": "2004-07",
    "title": "Tribal Groups Protest Iron Ore Mining in Bailadila (2004-07)",
    "description": "Tribal families in Bailadila hold demonstrations protesting the expansion of iron ore mining blocks on forested hills. The protestors demand protection of sacred tribal sites and forest land rights.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "land_rights"},
    "reactionOptions": create_reactions(
        nk, "bailadila_displacement",
        "The Mines Department sets up a consultation cell to review tribal land claims in Bailadila.",
        "Opposition Congress leaders join the protests, demanding that the mining expansion be suspended immediately in Bailadila.",
        "A joint committee of land officials and local panchayat chiefs is formed to verify tribal claims in Bailadila.",
        "The District Collector declines to release the total acreage of land scheduled for mining expansion in Bailadila.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -2},
        {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhRuralTrustMemory": -1}, {"chhattisgarhStabilityMemory": -1},
        14, "Administrative delays stall the verification cell, drawing fresh protests outside the collectorate.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The Congress protests lead to minor traffic blockades, drawing complaints from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Verification is delayed due to missing land records in the revenue office, stalling progress.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-08: Congress protests bribery allegations
nk = f"{short_code}_2004_08_bribery_allegations"
news_items.append({
    "newsKey": nk, "month": "2004-08",
    "title": "Congress Alleges Bribery in 2003 Election Transitions (2004-08)",
    "description": "Opposition Congress leaders stage demonstrations in Raipur, alleging that the BJP used illegal funds to secure independent MLA support during the 2003 cabinet formation. The government dismisses the claims as baseless slander.",
    "issueTags": ["politics", "corruption"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "bribery_allegations",
        "The government defends its transition integrity and states the allegations are politically motivated.",
        "Opposition Congress leaders demand a judicial probe and table a resolution in the assembly.",
        "Both parties agree to a formal assembly debate on clean governance guidelines to maintain decorum.",
        "The state BJP office declines to comment on reports of central party coordination meetings.",
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhCorruptionMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "Leaks from the party consultations fuel further media speculation about transition deals.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The judicial probe demand is rejected by the Speaker, limiting the opposition's legislative traction.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Assembly debate is disrupted by shouting matches, preventing the passage of the clean governance draft.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-09: Janjgir-Champa floods
nk = f"{short_code}_2004_09_janjgir_floods"
news_items.append({
    "newsKey": nk, "month": "2004-09",
    "title": "Flash Floods Displace Families in Janjgir-Champa (2004-09)",
    "description": "Late monsoon rains cause the Hasdeo river to rise, inundating agricultural tracts and displacing families in Janjgir-Champa district. The administration coordinates relief distribution, amidst complaints of slow response.",
    "issueTags": ["rural", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "janjgir_floods",
        "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations in Janjgir-Champa.",
        "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages to Hasdeo flood victims.",
        "A joint legislative relief committee is established to supervise rehabilitation work in Janjgir-Champa.",
        "The District Collector declines to release the official crop loss estimates in the first week for Janjgir-Champa.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "Logistical failures delay the delivery of tents to remote villages, drawing local protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        12, "The criticism leads to minor scuffles at distribution centers, disrupting relief work.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over relief beneficiary lists stall aid distribution in several affected talukas.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-10: Raman Singh local body campaign
nk = f"{short_code}_2004_10_localbody_campaign"
news_items.append({
    "newsKey": nk, "month": "2004-10",
    "title": "CM Raman Singh Launches Local Body Outreach (2004-10)",
    "description": "Chief Minister Raman Singh launches a statewide campaign tour, touring districts to inaugurate development projects and highlighting the achievements of urban and tribal welfare missions. The tour aims to build municipal election momentum.",
    "issueTags": ["politics", "governance"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "localbody_campaign",
        "The state administration fast-tracks the inauguration of pending municipal school and road projects.",
        "Opposition leaders call the outreach a waste of public funds and demand the immediate restoration of power supply.",
        "A joint committee is formed to review the code of conduct rules for government-funded local inaugurations.",
        "The government spokesperson declines to share the total promotional expenditure of the local body tour.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhRuralTrustMemory": -1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        13, "Poor road conditions on the CM's route highlight the opposition's campaign, drawing media focus.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The protest is dismissed as routine opposition posturing, failing to gather neutral voter attention.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "The code review is delayed by the non-participation of senior opposition leaders.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-11: Urban local body elections
nk = f"{short_code}_2004_11_local_polls"
news_items.append({
    "newsKey": nk, "month": "2004-11",
    "title": "Mixed Results Recorded in Urban Local Body Elections (2004-11)",
    "description": "Results for the statewide urban local body elections are announced, showing a closely contested layout. The BJP retains major municipal corporations like Raipur, while the Congress wins key municipal councils.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "local_polls",
        "The BJP government welcomes the mandate and vows to focus on urban developmental initiatives.",
        "Opposition Congress leaders claim the results show strong public rejection of the government's urban policies.",
        "Both parties agree to cooperate on urban development project monitoring committees in the municipalities.",
        "The State Election Commissioner declines to comment on requests to review voting counts in disputed municipal wards.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        13, "Disputes over specific block project allocations stall municipal council meetings.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The Congress claims are labeled as exaggerated by political observers, limiting their public impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Disagreements over the tax sharing formula stall the municipal finance reforms.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-12: Drought relief package
nk = f"{short_code}_2004_12_drought_package"
news_items.append({
    "newsKey": nk, "month": "2004-12",
    "title": "Government Announces Special Agricultural Relief Package (2004-12)",
    "description": "CM Raman Singh cabinet approves a special financial package for drought-affected blocks, offering power tariff waivers and crop insurance payouts to farmers. The announcement aims to mitigate rural economic distress.",
    "issueTags": ["rural", "governance"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "drought_package",
        "The Agriculture Department sets up emergency cells to distribute the relief and crop insurance payouts.",
        "Opposition Congress leaders claim the package is delayed and fails to cover non-loanee farmers.",
        "A joint committee is formed to negotiate central drought relief matches and coordinate allocations.",
        "The Cooperative Registrar declines to comment on the number of farmers currently registered for payouts.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhRuralTrustMemory": 2}, {"chhattisgarhRuralTrustMemory": -1}, {"chhattisgarhStabilityMemory": -1},
        13, "Logistical bottlenecks delay payouts in remote tribal zones, drawing localized protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The Congress criticism is ignored by farm organizations who welcome the tariff waivers, limiting its impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Verification is delayed due to missing land records in the cooperative office, stalling progress.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-12"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005
# 2005-01: Tsunami relief package
nk = f"{short_code}_2005_01_tsunami_aid"
news_items.append({
    "newsKey": nk, "month": "2005-01",
    "title": "State Announces Tsunami Relief Package (2005-01)",
    "description": "Chhattisgarh government announces a ₹7 crore aid package for southern tsunami victims. CM Raman Singh personally coordinates the rehabilitation plan, which includes adopting affected coastal villages.",
    "issueTags": ["governance", "politics"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "tsunami_aid",
        "The state administration coordinates the relief funds and dispatches rehabilitation materials to Chennai.",
        "Opposition leaders claim that local tribal welfare funds are being diverted for external political gains.",
        "Both parties agree to a joint resolution appreciating the humanitarian gesture of the state.",
        "The state relief director declines to release the itemized transit costs of the tsunami aid cargo.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhStabilityMemory": 1}, {"chhattisgarhRuralTrustMemory": -1}, {"chhattisgarhStabilityMemory": -1},
        12, "Transit delays hold up cargo trains in neighboring zones, drawing mild local press criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The diversion allegations are dismissed by local civic groups who support the humanitarian aid.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        8, "Minor disputes over dispatch logistics are reported in state warehouse departments.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-02: Factional bickering BJP unit
nk = f"{short_code}_2005_02_factional_bickering"
news_items.append({
    "newsKey": nk, "month": "2005-02",
    "title": "Factional Bickering Reported in State BJP Unit (2005-02)",
    "description": "Internal friction grows in the ruling BJP as senior leaders criticize CM Raman Singh's choice of cabinet portfolios. The bickering threatens party unity ahead of the upcoming legislative sessions.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "factional_bickering",
        "CM Raman Singh holds a cabinet coordination meet and reiterates the need for party discipline.",
        "Opposition Congress leaders call the infighting a proof that the BJP administration is too divided to govern.",
        "Senior BJP leaders hold a closed-door meeting to address concerns and project a united front.",
        "The state BJP spokesperson declines to comment on reports of seat-sharing disputes inside the unit.",
        {"partyMorale": 1, "corruptionScore": 0, "mediaImage": 1, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "Leaks from the coordination meeting fuel further media speculation about leadership changes.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The criticism is ignored by voters who view it as standard opposition exploitation of internal issues.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Several key legislators skip the unity meeting, diluting its positive impact in the press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-03: VAT implementation Raipur strike
nk = f"{short_code}_2005_03_vat_strike"
news_items.append({
    "newsKey": nk, "month": "2005-03",
    "title": "VAT Implementation Triggers Traders' Strike in Raipur (2005-03)",
    "description": "Value Added Tax (VAT) goes into effect, triggering a statewide strike by trader associations. Shops and commercial establishments remain shut in Raipur, disrupting local business.",
    "issueTags": ["protest", "economy"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "vat_strike",
        "The CM initiates negotiations with trader leaders and offers a simplified filing process.",
        "Opposition Congress leaders support the traders, demanding a rollback of the VAT system.",
        "A joint government-trader advisory panel is formed to review specific tax slabs and address issues.",
        "The Excise Department declines to comment on the number of businesses currently complying with VAT registration.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhCorruptionMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "The simplified rules proposal is rejected by union hardliners, extending the business shutdown.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The demands are criticized by consumer groups who argue VAT will reduce middleman price manipulation.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Advisory panel talks break down as trader representatives demand exemption for small retail shops.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-04: Bhilai summer water crisis
nk = f"{short_code}_2005_04_bhilai_water"
news_items.append({
    "newsKey": nk, "month": "2005-04",
    "title": "Drinking Water Crisis Reported in Bhilai Wards (2005-04)",
    "description": "An intense summer heatwave in April dries up local wells in Bhilai, leading to a critical drinking water crisis. Residents in housing colonies protest over irregular municipal tanker supply, demanding immediate relief.",
    "issueTags": ["rural", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "bhilai_water",
        "The Public Health Engineering Department releases emergency funds to deploy water tankers and drill borewells.",
        "Opposition Congress leaders lead protests outside PHE offices, accusing the BJP government of failing to prepare.",
        "A joint water task force is formed to manage daily supply allocations to the worst-affected blocks.",
        "The Public Health Engineering Minister declines to give a timeline for restoring piped water supply.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"chhattisgarhRuralTrustMemory": -1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "Private water tanker operators charge illegal premiums, drawing local public anger and media focus.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        12, "Protests are labeled by the ruling party as creating public panic, limiting their wider impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Task force coordination fails as local block officers report a lack of fuel for water tankers.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-05: Coal block JVs tribal rallies
nk = f"{short_code}_2005_05_coal_mous"
news_items.append({
    "newsKey": nk, "month": "2005-05",
    "title": "Coal Block JV Agreements Trigger Tribal Rallies (2005-05)",
    "description": "The state government signs joint venture agreements for coal block development. Adivasi rights groups hold protests, warning of massive tribal displacement and ecological damage in forest corridors.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "land_rights"},
    "reactionOptions": create_reactions(
        nk, "coal_mous",
        "The Mines Department announces strict rehabilitation guidelines and promises fair compensation packages for the coal blocks.",
        "Opposition Congress leaders join the protests, demanding that the JV agreements be tabled in the assembly for review.",
        "A joint committee of mining officials, Adivasi representatives, and legislators is formed to monitor rehabilitation for the JVs.",
        "The Mines Minister declines to release the specific land acreage required for the new coal block developments.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"chhattisgarhRuralTrustMemory": -1}, {"chhattisgarhIdentityMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        15, "Local protests block initial survey work in the coal zones, drawing police intervention.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The demands are criticized as anti-development by business groups who support industrial expansion.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over the committee's representation delay its first review meeting.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-06: Salwa Judum launch Bastar
nk = f"{short_code}_2005_06_salwa_judum"
news_items.append({
    "newsKey": nk, "month": "2005-06",
    "title": "Salwa Judum Movement Launched in Bastar (2005-06)",
    "description": "A counter-insurgency civil vigilance movement named Salwa Judum begins in Bastar as a public march against Naxalite violence. The movement receives support from state authorities who view it as a peace initiative.",
    "issueTags": ["security_crisis", "identity"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "salwa_judum",
        "The state police coordinates vigilance checks and provides security to Salwa Judum rallies.",
        "Opposition Congress leaders express caution, warning against arming civilians and creating parallel law enforcement.",
        "A joint assembly safety committee is formed to monitor security levels in the Salwa Judum camps.",
        "The Home Minister declines to comment on the specific weapons allocated to local special police officers.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"chhattisgarhSecurityMemory": 1}, {"chhattisgarhStabilityMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        15, "Salwa Judum camp coordination faces logistical delays, leaving several remote villages unmonitored.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The Congress warnings are labeled as soft on terror, drawing disapproval from police associations.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over camp management protocols delay the joint safety panel's field visits.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-07: Cabinet bickering PDS checks
nk = f"{short_code}_2005_07_pds_friction"
news_items.append({
    "newsKey": nk, "month": "2005-07",
    "title": "CM Raman Singh Faces Cabinet Friction Over PDS Checks (2005-07)",
    "description": "Internal differences emerge in the Raman Singh cabinet over introducing stricter monitoring for PDS rice distributions. Allied ministers claim that checks are disrupting supply to rural dealers.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "pds_friction",
        "CM Raman Singh holds a cabinet coordination meet and offers minor modifications to PDS check rules.",
        "Opposition Congress leaders claim the public bickering shows the state government is completely paralyzed.",
        "Senior state BJP leaders hold a closed-door meeting to address concerns and project a united front.",
        "The state BJP spokesperson declines to comment on reports of seat-sharing disputes inside the cabinet.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 1, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "Leaks from the coordination meeting fuel further media speculation about leadership changes.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The criticism is ignored by voters who view it as standard opposition exploitation of internal issues.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Several key legislators skip the unity meeting, diluting its positive impact in the press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-08: Flash floods Indravati
nk = f"{short_code}_2005_08_indravati_floods"
news_items.append({
    "newsKey": nk, "month": "2005-08",
    "title": "Flash Floods in Indravati Basin Damage Crops in Bastar (2005-08)",
    "description": "Continuous heavy rainfall in August causes the Indravati river to overflow, inundating agricultural land and damaging standing crops in Bastar district. The administration coordinates evacuations.",
    "issueTags": ["rural", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "indravati_floods",
        "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations in Bastar.",
        "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages to Indravati victims.",
        "A joint legislative relief committee is established to supervise rehabilitation work in Bastar division.",
        "The District Collector declines to release the official crop loss estimates in the first week for Bastar.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        14, "Logistical failures delay the delivery of tents to remote villages, drawing local protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        12, "The criticism leads to minor scuffles at distribution centers, disrupting relief work.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over relief beneficiary lists stall aid distribution in several affected talukas.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-09: Financial irregularities cooperative land banks
nk = f"{short_code}_2005_09_bank_irregularities"
news_items.append({
    "newsKey": nk, "month": "2005-09",
    "title": "Irregularities Uncovered in Rural Cooperative Land Banks (2005-09)",
    "description": "A cooperative department audit uncovers major irregularities and illegal credit extensions in local land mortgage banks. The opposition Congress demands a judicial probe, alleging favoritism.",
    "issueTags": ["corruption", "rural"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "corruption"},
    "reactionOptions": create_reactions(
        nk, "bank_irregularities",
        "The Cooperative Department suspends the boards of the irregular banks and orders a forensic audit.",
        "Opposition Congress leaders demand a judicial probe and stage protests outside bank head offices.",
        "A multi-party legislative subcommittee is formed to draft credit guidelines for cooperative institutions.",
        "The Cooperative Minister declines to comment on the total volume of frozen farmer deposits.",
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhCorruptionMemory": -1}, {"chhattisgarhCorruptionMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        15, "The forensic audit is delayed, prolonging the freeze on farmer accounts and drawing public anger.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "Bank protests lead to minor property damage at a rural branch, drawing public disapproval.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Subcommittee talks are slowed down by disagreements over government representation on bank boards.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-10: Lok Suraj campaign launch
nk = f"{short_code}_2005_10_lok_suraj"
news_items.append({
    "newsKey": nk, "month": "2005-10",
    "title": "CM Raman Singh Launches 'Lok Suraj' Campaign (2005-10)",
    "description": "Chief Minister Raman Singh launches the 'Lok Suraj' outreach campaign, setting up special grievance redressal camps in rural districts. The campaign aims to improve administrative access.",
    "issueTags": ["governance", "rural"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "lok_suraj",
        "The government releases special budgetary allocations to launch the grievance redressal camps across all blocks.",
        "Opposition Congress leaders call the program a rebranding of old schemes and demand clear project timelines.",
        "A joint government-expert advisory board is formed to track the implementation of the Lok Suraj targets.",
        "The CM's office declines to publish the project-wise funding breakdown for the outreach program.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhRuralTrustMemory": -1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
        13, "Budgetary constraints delay project launches in several remote tribal blocks.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The Congress criticism is ignored by rural organizations who support the target sectors.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "The advisory board's first review meeting is delayed due to missing department reports.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-11: Sipat thermal project displacement
nk = f"{short_code}_2005_11_sipat_displacement"
news_items.append({
    "newsKey": nk, "month": "2005-11",
    "title": "Tribal Families Protest Near Sipat Thermal Project (2005-11)",
    "description": "Tribal families in Sipat hold demonstrations protesting the land acquisition for a major NTPC power project. The protestors demand fair compensation packages and guarantees of employment.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "land_rights"},
    "reactionOptions": create_reactions(
        nk, "sipat_displacement",
        "The land acquisition officer sets up a verification cell to review compensation claims and job listings for the Sipat project.",
        "Opposition Congress leaders join the protests, demanding that the land acquisition process be suspended immediately for the Sipat project.",
        "A joint committee of land officials and local panchayat chiefs is formed to verify the value of the acquired plots for the Sipat project.",
        "The District Collector declines to release the total acreage of land scheduled for acquisition.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -2},
        {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhRuralTrustMemory": -1}, {"chhattisgarhStabilityMemory": -1},
        14, "Administrative delays stall the verification cell, drawing fresh protests outside the collectorate.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The Congress protests lead to minor traffic blockades, drawing complaints from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
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
        "The BJP government welcomes the mandate and vows to focus on rural developmental initiatives.",
        "Opposition Congress leaders claim their win shows strong public rejection of the government's urban policies.",
        "Both parties agree to cooperate on rural road project monitoring committees in the constituencies.",
        "The State Election Commissioner declines to comment on requests to review voting counts in disputed by-election booths.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"chhattisgarhStabilityMemory": -1}, {"chhattisgarhRuralTrustMemory": 1}, {"chhattisgarhStabilityMemory": -1},
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
    "sourceNotes": "Government: Congress led by Ajit Jogi CM until December 2003. Then BJP led by Raman Singh CM through December 2005. Opposition: BJP until Dec 2003, then Congress. Main issues: tribal land forest rights, PDS rice reforms, V.C. Shukla defections, Naxalite security threats, and Salwa Judum movement launched in June 2005. Built programmatically matching the schema and calibration constraints.",
    "defaults": {
        "weights": {
            "baseSelectionWeight": 1.0,
            "reactionProfile": "default"
        }
    },
    "newsItems": news_items
}

output_path = Path("seed-data/review/chhattisgarh_2001_news.json")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(json.dumps(data, indent=2))
print("Successfully generated chhattisgarh_2001_news.json with", len(news_items), "news items!")
