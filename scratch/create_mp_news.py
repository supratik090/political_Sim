import json
from pathlib import Path

# Define the scenario metadata
scenario_key = "madhya_pradesh_2001"
short_code = "mp2001"

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

# We will populate news_items month by month
# 2001
# 2001-01: Digvijaya Singh at Davos
nk = f"{short_code}_2001_01_davos_summit"
news_items.append({
    "newsKey": nk, "month": "2001-01",
    "title": "CM Digvijaya Singh Represents State at World Economic Forum in Davos (2001-01)",
    "description": "Chief Minister Digvijaya Singh attends the Davos summit, showcasing Madhya Pradesh's pioneering work in decentralized governance, Panchayati Raj, and the Education Guarantee Scheme. The visit projects a reformist image globally, but opposition leaders question the domestic benefits of such trips.",
    "issueTags": ["governance", "politics"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "davos_summit",
        "The CM showcases decentralized development policies in Davos to attract foreign direct investment and partnerships.",
        "The BJP opposition criticizes the foreign visit as self-promotion while the state struggles with high rural illiteracy.",
        "Both treasury and opposition benches agree to form a joint committee to follow up on foreign investment leads.",
        "The CM's office declines to release the exact details and cost of the international delegation's travel expenses.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        12, "Bureaucratic delays stall the foreign investment cell, drawing local media criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The criticism is dismissed by industry groups who support global outreach.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        8, "Partisan bickering stalls the joint investment follow-up committee's progress.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-02: Power grid disputes
nk = f"{short_code}_2001_02_power_bifurcation"
news_items.append({
    "newsKey": nk, "month": "2001-02",
    "title": "Standoff Over Division of Electricity Board Assets with Chhattisgarh (2001-02)",
    "description": "Friction mounts between Madhya Pradesh and the newly formed state of Chhattisgarh over the division of the former MP Electricity Board. Chhattisgarh controls coal-rich power plants, leaving MP facing immediate power deficits and debt sharing disputes.",
    "issueTags": ["infrastructure", "politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "power_bifurcation",
        "The MP government petitions the Centre to intervene and mandate a fair sharing of power assets and debts.",
        "Opposition BJP MLAs hold protests accusing the Congress government of failing to protect MP's energy interests during bifurcation.",
        "Both governments agree to a round of bilateral ministerial talks to settle the division of electricity board liabilities.",
        "The MP Power Department declines to issue a statement on the potential impact on daily power supply.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpIdentityMemory": 1}, {"mpStabilityMemory": -1},
        14, "The central intervention is delayed, leaving MP to purchase expensive power from external grids.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "Protests turn violent in Indore, leading to negative press regarding public order.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Bilateral talks break down as Chhattisgarh rejects the proposed debt division formula.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-03: Right to recall local bodies
nk = f"{short_code}_2001_03_right_to_recall"
news_items.append({
    "newsKey": nk, "month": "2001-03",
    "title": "Voters Exercise 'Right to Recall' in Anuppur Municipality (2001-03)",
    "description": "In a first for the nation, the electorate in Anuppur uses the newly legislated 'Right to Recall' to remove their municipal council president. While the Congress government hails it as a triumph of grassroots democracy, critics call it a source of political instability.",
    "issueTags": ["governance", "politics"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "right_to_recall",
        "The state government implements guidelines to streamline recall votes and promises further decentralization.",
        "Opposition parties demand that the recall provision also apply to MLAs and MPs, not just local body chiefs.",
        "An all-party consultative committee meets to review the recall mechanism and prevent its abuse for personal vendettas.",
        "The State Election Commission declines to comment on requests to schedule more recall votes in other districts.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpRuralTrustMemory": -1}, {"mpStabilityMemory": 1}, {"mpStabilityMemory": -1},
        13, "Administrative overheads delay local body operations in districts with pending recall petitions.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The demand is criticized by constitutional experts as unfeasible, weakening the opposition's stance.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "The committee fails to reach a consensus, leaving the existing local law unchanged.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-04: Pani Roko Abhiyan
nk = f"{short_code}_2001_04_pani_roko_campaign"
news_items.append({
    "newsKey": nk, "month": "2001-04",
    "title": "Government Launches 'Pani Roko Abhiyan' Amid Drought Warnings (2001-04)",
    "description": "With early warnings of a weak monsoon, the state government launches the 'Pani Roko Abhiyan' (Stop the Water Campaign), mobilizing rural communities to build check dams and harvest rainwater. The initiative is praised for community involvement but criticized for low funding.",
    "issueTags": ["rural", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "pani_roko_campaign",
        "The state releases emergency funds to village panchayats to construct low-cost water harvesting structures.",
        "BJP leaders demand a major state-funded canal project instead of shifting the water conservation burden to dry villages.",
        "A joint assembly panel tours the drought-prone Malwa region to monitor check-dam construction progress.",
        "The Irrigation Department declines to provide a target completion count for the rainwater harvesting units.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -3},
        {"mpRuralTrustMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        14, "Corruption at the local level results in substandard check dams that wash away in the first rains.", {"partyMorale": -2, "corruptionScore": 2, "mediaImage": -2, "publicSupport": -2},
        12, "The demands are labeled by the ruling party as elite posturing that ignores local empowerment.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Logistical constraints prevent the assembly panel from visiting the most remote tribal hamlets.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-05: Reallocation of officers
nk = f"{short_code}_2001_05_officer_reallocation"
news_items.append({
    "newsKey": nk, "month": "2001-05",
    "title": "Disputes Arise Over Reallocation of Civil Service Officers (2001-05)",
    "description": "Tensions mount between Bhopal and Raipur as several senior IAS and IPS officers contest their cadre allocations to Chhattisgarh. The state administration faces a temporary logjam as key posts in Bhopal remain under litigation.",
    "issueTags": ["governance", "politics"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "officer_reallocation",
        "The Chief Secretary initiates talks with the Home Ministry to establish a smooth cadre-swap mechanism.",
        "Opposition leaders accuse the government of using the reallocation process to sideline non-pliant officers.",
        "A joint committee of civil services representatives meets to resolve pending cadre grievances amicably.",
        "The Department of Personnel declines to comment on the number of vacant administrative posts in the districts.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 1},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpCorruptionMemory": 1}, {"mpStabilityMemory": -1},
        13, "Delays in cadre swaps leave key border districts without senior police officers for several weeks.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The allegations are dismissed by the central cadre authority, weakening the opposition's claims.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "The swap committee talks stall as both state cadres refuse to accept surplus junior officers.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-06: Education Guarantee Scheme
nk = f"{short_code}_2001_06_egs_recognition"
news_items.append({
    "newsKey": nk, "month": "2001-06",
    "title": "Education Guarantee Scheme Receives International Acclaim (2001-06)",
    "description": "The state's Education Guarantee Scheme (EGS), which ensures a primary school within 1 km of any habitation upon demand, receives recognition from international development bodies. The government celebrates this as validation of its rural empowerment policies.",
    "issueTags": ["rural", "governance"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "egs_recognition",
        "The government announces additional budgetary support to upgrade EGS centers with permanent buildings.",
        "BJP leaders claim EGS schools lack qualified teachers and are used to provide patronage jobs to Congress workers.",
        "The Assembly holds a special discussion on education quality, agreeing to set up local parent-teacher audit boards.",
        "The Education Department declines to publish the drop-out rates in EGS schools over the past two years.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpRuralTrustMemory": -1}, {"mpCorruptionMemory": 1}, {"mpRuralTrustMemory": -1},
        14, "Funding constraints delay the construction of permanent buildings in remote tribal areas.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "The criticism is seen as an attack on rural teachers, sparking a minor backlash from teacher unions.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Parent-teacher audit boards face bureaucratic resistance and fail to meet in several districts.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-07: Flooding in Narmada valley
nk = f"{short_code}_2001_07_narmada_floods"
news_items.append({
    "newsKey": nk, "month": "2001-07",
    "title": "Heavy Monsoon Rains Trigger Flooding in Narmada Valley (2001-07)",
    "description": "Torrential monsoon rains cause the Narmada river to overflow, inundating low-lying villages and agricultural land in Hoshangabad and Narsinghpur. The state machinery is deployed to evacuate residents, amidst allegations of delayed relief response.",
    "issueTags": ["rural", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "narmada_floods",
        "The administration coordinates emergency rescues with the state disaster response units and sets up relief camps.",
        "Opposition parties criticize the government for failing to implement adequate flood-warning systems in vulnerable areas.",
        "A joint relief committee is established with representatives from all major parties to oversee aid distribution.",
        "The District Collector's office declines to estimate the total crop and property damage in the first week.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"mpStabilityMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        15, "Relief materials are delayed by damaged road networks, leading to protests by affected villagers.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The opposition's protests are labeled as politicizing a natural disaster, drawing public disapproval.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disputes over relief beneficiary lists stall aid distribution in several affected talukas.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-08: Ekta Parishad land rights
nk = f"{short_code}_2001_08_ekta_parishad_land"
news_items.append({
    "newsKey": nk, "month": "2001-08",
    "title": "Ekta Parishad Organizes Tribal Land Rights Rally in Chambal (2001-08)",
    "description": "Thousands of tribal and landless farmers, mobilized by the activist group Ekta Parishad, march in Morena to demand the implementation of land reforms and the distribution of land titles. The protest puts pressure on the government's pro-poor agenda.",
    "issueTags": ["protest", "rural"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "land_rights"},
    "reactionOptions": create_reactions(
        nk, "ekta_parishad_land",
        "The government agrees to set up district-level task forces to verify tribal land claims and expedite title deeds.",
        "Opposition leaders support the rally, demanding the government immediately hand over forest land to cultivators.",
        "A multi-party land advisory council is formed to draft a balanced land distribution policy for tribal regions.",
        "The Revenue Department declines to comment on the number of pending land dispute cases in Morena district.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -2},
        {"mpRuralTrustMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        16, "Local land mafias physically intimidate tribal claimants, stalling the verification task forces.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        13, "Landowner lobbies strongly oppose the demands, leading to counter-protests in the Chambal valley.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The advisory council's recommendations are delayed by disagreements between pro-tribal and pro-landlord members.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-09: Naxalite violence in Balaghat
nk = f"{short_code}_2001_09_balaghat_naxal"
news_items.append({
    "newsKey": nk, "month": "2001-09",
    "title": "Naxalite Activity Intensifies in Balaghat Border Region (2001-09)",
    "description": "Reports of increased Naxalite movement and intimidation in the forested areas of Balaghat district raise security concerns. The state government faces pressure to coordinate counter-insurgency operations with neighboring Maharashtra and Chhattisgarh.",
    "issueTags": ["security_crisis", "protest"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "balaghat_naxal",
        "The state police deploys additional special task force units to Balaghat and strengthens joint border patrolling.",
        "The BJP opposition demands a comprehensive security sweep and accuses the CM of being soft on left-wing extremism.",
        "A joint resolution is passed in the assembly supporting development initiatives in Naxal-affected tribal belts.",
        "The Home Department declines to comment on the specific deployment strength of security forces in Balaghat.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"mpStabilityMemory": -1}, {"mpIdentityMemory": 1}, {"mpStabilityMemory": -1},
        18, "An ambush by insurgents injures state police personnel, raising questions about operational intelligence.", {"partyMorale": -3, "corruptionScore": 0, "mediaImage": -3, "publicSupport": -3},
        14, "The aggressive security demands provoke protests from local human rights activists in Bhopal.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Developmental funds are diverted due to administrative bottlenecks, leaving tribal youths disgruntled.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-10: By-election Sabalgarh
nk = f"{short_code}_2001_10_byelection_sabalgarh"
news_items.append({
    "newsKey": nk, "month": "2001-10",
    "title": "High-Stakes Assembly By-Election Announced in Sabalgarh (2001-10)",
    "description": "An assembly by-election in Sabalgarh becomes a referendum on the Congress government's rural policies. Both Congress and BJP deploy senior leaders to campaign, highlighting the rising political temperatures in northern MP.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "byelection_sabalgarh",
        "The ruling Congress campaigns on its decentralization record and panchayat empowerment reforms.",
        "The BJP launches a campaign focusing on power shortages and the state of rural roads under the current regime.",
        "Both parties sign a code of conduct agreement with the Election Commission to ensure peaceful voting.",
        "The party coordinators refuse to comment on reports of factional disputes over candidate selection.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        13, "Low voter turnout in rural pockets limits the impact of the government's positive campaign.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "Factional infighting within the local BJP unit weakens the impact of the anti-incumbency campaign.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Minor clashes between party workers break out on polling day, drawing negative press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-11: First anniversary of bifurcation
nk = f"{short_code}_2001_11_bifurcation_anniversary"
news_items.append({
    "newsKey": nk, "month": "2001-11",
    "title": "Bifurcation Anniversary Highlights State's Financial Deficit (2001-11)",
    "description": "On the first anniversary of Chhattisgarh's creation, economic analyses show Madhya Pradesh facing a severe budget deficit due to the loss of industrial revenues and mineral reserves. The opposition blames the government's fiscal mismanagement.",
    "issueTags": ["economy", "politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "bifurcation_anniversary",
        "The Finance Minister announces a fiscal rationalization plan and requests additional special grants from the Centre.",
        "BJP leaders demand a white paper on the state's debt status and criticize the government's tax policies.",
        "A joint legislative committee is formed to identify potential new revenue sources and non-tax avenues.",
        "The state treasury declines to release the monthly details of public debt accumulation to the media.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpCorruptionMemory": 1}, {"mpStabilityMemory": -1},
        14, "New tax proposals draw protests from local trader associations in Bhopal and Indore.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        11, "The demand is dismissed as politically motivated, failing to gather support from industrial bodies.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "The revenue committee's report is delayed due to partisan gridlock over tax proposals.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-12: Fertilizer shortages Malwa
nk = f"{short_code}_2001_12_fertilizer_protest"
news_items.append({
    "newsKey": nk, "month": "2001-12",
    "title": "Winter Crop Sowing Hit by Fertilizer Shortages in Malwa (2001-12)",
    "description": "Farmers in the fertile Malwa region hold demonstrations protesting the shortage of urea and phosphate fertilizers during the critical winter crop sowing season. The shortage threatens crop yields, causing severe rural anxiety.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "fertilizer_protest",
        "The Agriculture Department coordinates with the central pool to release emergency buffer stocks of urea.",
        "BJP leaders demand a complete waiver of cooperative dues for farmers affected by the supply failure.",
        "A multi-party delegation meets the Central Agriculture Minister to demand an increased fertilizer quota for MP.",
        "The Cooperative Department declines to give a timeline for when urea shipments will reach local distribution centers.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"mpRuralTrustMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        15, "Hoarding by black-market traders results in continued high prices despite the emergency release.", {"partyMorale": -2, "corruptionScore": 2, "mediaImage": -2, "publicSupport": -2},
        13, "The demands are criticized as fiscally irresponsible by economists, limiting their political gain.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The central delegation's meeting yields only partial promises, failing to resolve the immediate crisis.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-12"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002
# 2002-01: Bhopal Conference Dalit Declaration
nk = f"{short_code}_2002_01_bhopal_declaration"
news_items.append({
    "newsKey": nk, "month": "2002-01",
    "title": "Bhopal Conference Formulates Dalit and Tribal Empowerment Agenda (2002-01)",
    "description": "The state government hosts the landmark Bhopal Conference, bringing together intellectuals and activists to draft the 'Bhopal Declaration'. The agenda focuses on land distribution and promoting private sector diversity for Dalits and tribals.",
    "issueTags": ["governance", "identity"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "bhopal_declaration",
        "The state government adopts the declaration and announces a roadmap to distribute land titles to Dalit families.",
        "BJP leaders accuse the government of playing identity politics to divide voters ahead of the assembly elections.",
        "A joint committee of Dalit and tribal legislators is formed to oversee the legislative implementation of the agenda.",
        "The CM's office declines to share the estimated cost of hosting the two-day conference in Bhopal.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpRuralTrustMemory": -1}, {"mpIdentityMemory": 1}, {"mpStabilityMemory": -1},
        14, "Implementation encounters resistance from local revenue officers, delaying the land distribution process.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The criticism alienates several Dalit community leaders, backfiring on the opposition's outreach.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The legislative committee's deliberations are slowed by disagreements over specific reservation quotas.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-02: Godhra aftermath communal ban
nk = f"{short_code}_2002_02_communal_vigilance"
news_items.append({
    "newsKey": nk, "month": "2002-02",
    "title": "State Government Imposes Ban on Communal Rallies After Godhra Incident (2002-02)",
    "description": "Following the Godhra train burning in neighboring Gujarat, the MP government places districts bordering Gujarat on high alert and bans communal rallies. The move maintains peace but draws protests from right-wing organizations.",
    "issueTags": ["identity", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "communal_vigilance",
        "The Home Department deploys rapid reaction police forces to border districts and enforces strict peace committee meetings.",
        "Right-wing groups criticize the ban as a suppression of majority rights and demand its immediate revocation.",
        "All major parties issue a joint appeal for communal harmony and participate in peace marches across major cities.",
        "The police administration declines to share details on the number of preventive arrests made in border towns.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": -1, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"mpStabilityMemory": -1}, {"mpIdentityMemory": 1}, {"mpStabilityMemory": -1},
        15, "Isolated clashes in a border village result in minor property damage, testing the police force.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The demands provoke protests from secular groups, leading to localized tensions.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Logistical issues delay peace marches in some rural sub-divisions, reducing their public impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-03: Power Board transmission losses
nk = f"{short_code}_2002_03_transmission_losses"
news_items.append({
    "newsKey": nk, "month": "2002-03",
    "title": "Electricity Board Warns of Mounting Transmission Losses (2002-03)",
    "description": "The MP State Electricity Board reports a significant rise in transmission and distribution losses, largely attributed to power theft in rural and industrial sectors. The board warns that unscheduled load shedding will be necessary.",
    "issueTags": ["infrastructure", "economy"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "transmission_losses",
        "The Power Department launches an anti-theft drive and installs metered transformers in high-loss zones.",
        "Opposition BJP MLAs protest against the anti-theft drive, calling it harassment of poor rural consumers.",
        "A joint legislative committee is set up to study power sector reforms and draft a subsidy structure.",
        "The State Electricity Board declines to publish a schedule of the planned rural power cuts.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"mpStabilityMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        16, "The anti-theft drive triggers clashes between enforcement teams and villagers in Bhind district.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "Industrial bodies criticize the opposition's stance, arguing it defends illegal power tapping.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The committee's recommendations are delayed as members disagree on the level of rural power tariffs.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-04: Dalit land distribution
nk = f"{short_code}_2002_04_dalit_land"
news_items.append({
    "newsKey": nk, "month": "2002-04",
    "title": "Government Begins Dalit Land Allocation Under Bhopal Agenda (2002-04)",
    "description": "In line with the Bhopal Declaration, the state government initiates a program to allocate surplus government land to landless Dalit and tribal families. The move is praised by social activists but faces local administrative hurdles.",
    "issueTags": ["rural", "identity"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "land_rights"},
    "reactionOptions": create_reactions(
        nk, "dalit_land",
        "The Revenue Department orders district collectors to identify government land and hand over possession certificates.",
        "Opposition parties claim that the distributed land is mostly infertile and lacks irrigation access.",
        "A multi-party land review board is established to verify the quality and title deeds of the allocated plots.",
        "The Land Records Commissioner declines to release the total acreage of land distributed so far.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpRuralTrustMemory": -1}, {"mpIdentityMemory": 1}, {"mpStabilityMemory": -1},
        14, "Encroachments by local landowners prevent Dalit families from taking physical possession of the plots.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        12, "The criticism is dismissed by beneficiary groups who welcome even minor land ownership.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The review board's work is slowed down by missing cadastral maps in remote tribal blocks.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-05: Indore water crisis
nk = f"{short_code}_2002_05_indore_water"
news_items.append({
    "newsKey": nk, "month": "2002-05",
    "title": "Severe Summer Water Shortage Triggers Rationing in Indore (2002-05)",
    "description": "An intense heatwave in May depletes the Yashwant Sagar reservoir, forcing Indore's municipal corporation to implement strict water rationing. Residents protest over irregular supply, turning the water scarcity into a political issue.",
    "issueTags": ["rural", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "indore_water",
        "The government deploys municipal water tankers to affected wards and fast-tracks the Narmada water pipeline project phase.",
        "BJP leaders organize dharnas outside municipal offices, accusing the Congress administration of water mismanagement.",
        "A joint civic coordination council is formed to oversee equitable water distribution across all wards.",
        "The Indore Municipal Corporation declines to publish the daily water supply schedule for residential areas.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"mpRuralTrustMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        15, "Logistical failures result in uneven tanker distribution, sparking minor protests in poorer wards.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "Protests lead to brief traffic disruptions in Indore, drawing criticism from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Tanker coordination is hit by staff shortages, leaving several high-priority wards dry.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-06: Governor-CM disputes
nk = f"{short_code}_2002_06_governor_standoff"
news_items.append({
    "newsKey": nk, "month": "2002-06",
    "title": "Public Standoff Escalates Between CM and Governor Bhai Mahavir (2002-06)",
    "description": "Tensions peak between Chief Minister Digvijaya Singh and Governor Bhai Mahavir over the appointment of university vice-chancellors. The Governor accuses the state administration of politicizing academic institutions, while the CM defends executive prerogative.",
    "issueTags": ["governance", "politics"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "governor_standoff",
        "The government defends the university appointments in the assembly and seeks constitutional clarification.",
        "Opposition BJP leaders support the Governor's stance, calling for the immediate removal of tainted VC candidates.",
        "A joint committee of academic experts and legislators is proposed to draft new VC selection guidelines.",
        "The Higher Education Department declines to comment on the delay in university administrative appointments.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpCorruptionMemory": 1}, {"mpStabilityMemory": -1},
        14, "The Governor rejects the state's panel of names again, prolonging the administrative impasse.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The campaign fails to resonate with students who are more concerned about exam delays.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "The proposed academic committee is boycotted by student unions, stalling VC selection guidelines.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-07: Narmada dam heights
nk = f"{short_code}_2002_07_narmada_height"
news_items.append({
    "newsKey": nk, "month": "2002-07",
    "title": "Inter-State Dispute Over Sardar Sarovar Dam Height Intensifies (2002-07)",
    "description": "The Narmada Control Authority's decision to raise the Sardar Sarovar dam height sparks controversy in MP. The state government faces pressure to demand full resettlement of affected families before construction proceeds, while Gujarat pushes for early height clearance.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "land_rights"},
    "reactionOptions": create_reactions(
        nk, "narmada_height",
        "The state government demands that Gujarat provide complete rehabilitation funding before further construction is cleared.",
        "BJP leaders accuse the Congress government of slow rehabilitation work, delaying crucial irrigation benefits.",
        "A joint ministerial panel from MP and Gujarat is formed to audit resettlement colonies and address family grievances.",
        "The Narmada Rehabilitation Department declines to specify the number of families still awaiting resettlement packages.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"mpRuralTrustMemory": -1}, {"mpIdentityMemory": 1}, {"mpStabilityMemory": -1},
        15, "Protests by rehabilitation groups block state highways, drawing police intervention and negative press.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "Rehabilitation activists criticize the opposition's focus on speedy dam completion over family rights.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The ministerial audit is delayed as Gujarat officials dispute the number of eligible displaced families.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-08: Sadak Andolan road protest
nk = f"{short_code}_2002_08_sadak_andolan"
news_items.append({
    "newsKey": nk, "month": "2002-08",
    "title": "Opposition Launches 'Sadak Andolan' Protesting Highway Conditions (2002-08)",
    "description": "The opposition BJP launches a statewide 'Sadak Andolan' (Road Protest), staging symbolic planting of paddy in waterlogged craters on state and national highways. The campaign strikes a chord with motorists, highlighting infrastructure neglect.",
    "issueTags": ["infrastructure", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "sadak_andolan",
        "The Public Works Department announces a fast-track road repair program and releases funds to state road corporations.",
        "BJP leaders lead mass rallies on highways, demanding the immediate resignation of the state PWD Minister.",
        "An all-party highway monitoring committee is set up to inspect and report on major road repair quality.",
        "The PWD office declines to publish the list of road contractors currently blacklisted for poor quality work.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"mpStabilityMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        16, "Monsoon rains wash away the early patch repairs, exposing the government to further public ridicule.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        13, "Police resort to mild lathicharge to disperse protestors blocking national highways, drawing minor criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The highway monitoring committee's inspections are delayed by bureaucratic non-cooperation.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-09: Government employees strike
nk = f"{short_code}_2002_09_employees_strike"
news_items.append({
    "newsKey": nk, "month": "2002-09",
    "title": "State Government Employees Launch Indefinite Strike (2002-09)",
    "description": "Over 4 lakh state government employees launch an indefinite strike, demanding dearness allowance parity with central government staff. The strike paralyzes administrative offices, courts, and government schools across MP.",
    "issueTags": ["protest", "economy"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "employees_strike",
        "The CM initiates negotiations with union leaders and offers a phased implementation of dearness allowance.",
        "Opposition parties support the strikers, demanding the government immediately clear all pending allowances.",
        "A joint legislative-employee arbitration board is set up to negotiate salary scales within fiscal constraints.",
        "The administration invokes the Essential Services Maintenance Act (ESMA) and refuses to negotiate with strikers.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"mpStabilityMemory": -1}, {"mpCorruptionMemory": 1}, {"mpStabilityMemory": -1},
        14, "Fiscal constraints force the state to borrow further to fund the salary compromise, increasing debt.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "The demands are criticized by agricultural unions who argue public money should prioritize farm relief.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Arbitration talks break down as employee unions reject the proposed phased payment schedule.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-10: Corruption allegations in rural schemes
nk = f"{short_code}_2002_10_rural_graft"
news_items.append({
    "newsKey": nk, "month": "2002-10",
    "title": "Corruption Allegations Surface in Rural Development Schemes (2002-10)",
    "description": "Allegations of irregularities and inflated billing surface in the implementation of rural watershed and road development programs. The opposition BJP demands a CBI inquiry, accusing the ruling party of utilizing rural funds for campaign purposes.",
    "issueTags": ["corruption", "rural"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "corruption"},
    "reactionOptions": create_reactions(
        nk, "rural_graft",
        "The Rural Development Department suspends several local engineers and orders an audit of the disputed works.",
        "Opposition leaders demand a judicial probe and stage dharnas outside district collectorates.",
        "A multi-party public accounts subcommittee is tasked with reviewing rural development expenditures.",
        "The Rural Development Minister declines to comment on the specific audit findings to the press.",
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpCorruptionMemory": -1}, {"mpCorruptionMemory": 1}, {"mpStabilityMemory": -1},
        15, "Local contractors protest the suspensions, halting ongoing development works in several blocks.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The protests turn partisan, leading to counter-accusations against local BJP panchayat chiefs.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "The public accounts subcommittee's meetings are delayed by the non-submission of local records.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-11: Gyandoot portal e-governance
nk = f"{short_code}_2002_11_gyandoot_portal"
news_items.append({
    "newsKey": nk, "month": "2002-11",
    "title": "Gyandoot E-Governance Portal Wins National Recognition (2002-11)",
    "description": "The state's Gyandoot project, an intranet-based portal providing rural citizens access to land records, crop prices, and welfare forms, wins a national e-governance award. The government highlights it as digital empowerment of farmers.",
    "issueTags": ["governance", "rural"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "gyandoot_portal",
        "The IT Department announces plans to expand Gyandoot kiosks to all remaining gram panchayats in the state.",
        "BJP leaders claim the kiosks are non-functional due to frequent power outages and lack of staff training.",
        "A joint legislative committee on technology is formed to monitor rural kiosk operations and training.",
        "The IT Department declines to publish the monthly transaction volumes of the Gyandoot kiosks.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpRuralTrustMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        13, "Kiosks in remote tribal blocks report connectivity issues, drawing local complaints.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The criticism is dismissed by IT experts who support the decentralization technology.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "The technology committee's recommendations are delayed due to budget allocation disputes.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-12: Dhar Bhojshala shrine access
nk = f"{short_code}_2002_12_bhojshala_shrine"
news_items.append({
    "newsKey": nk, "month": "2002-12",
    "title": "Tensions Rise Over Access to Dhar Bhojshala Shrine (2002-12)",
    "description": "Communal tensions simmer in Dhar district as right-wing groups demand daily access to the Dhar Bhojshala-Kamal Maula Mosque monument for Hindu prayers. The site is currently managed by the ASI with restricted access for both communities.",
    "issueTags": ["identity", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "bhojshala_shrine",
        "The state government deploys additional police units to Dhar and coordinates with the ASI to maintain the status quo.",
        "BJP leaders support the demand, calling for the restoration of Hindu rights at the historical site.",
        "A joint peace committee of local community leaders is formed to negotiate access terms amicably.",
        "The District Magistrate declines to comment on the security arrangements and restrictions around the monument.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": -1, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"mpStabilityMemory": -1}, {"mpIdentityMemory": 1}, {"mpStabilityMemory": -1},
        16, "Isolated stone-pelting incidents occur near the monument, drawing sharp national media coverage.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        14, "The support leads to counter-protests by minority groups, raising communal temperatures.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Local peace talks are boycotted by hardline representatives, failing to resolve the standoff.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-12"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003
# 2003-01: Bhojshala dispute intensifies
nk = f"{short_code}_2003_01_bhojshala_protests"
news_items.append({
    "newsKey": nk, "month": "2003-01",
    "title": "Bhojshala Protest Organizers Call for Dhar Bandh (2003-01)",
    "description": "Organizers of the Bhojshala agitation call for a Dhar district bandh to press their demands for Hindu prayers at the shrine. The bandh is partially successful, but security remains tight to prevent communal clashes.",
    "issueTags": ["identity", "protest"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "bhojshala_protests",
        "The state police detains key protest leaders preventively to maintain law and order during the bandh.",
        "Opposition BJP MLAs criticize the detentions, calling them an authoritarian suppression of peaceful devotion.",
        "A multi-party delegation meets the Union Culture Minister to seek an ASI-mediated solution for Bhojshala.",
        "The Home Minister declines to make a statement in the assembly regarding the security situation in Dhar.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"mpStabilityMemory": -1}, {"mpIdentityMemory": 1}, {"mpStabilityMemory": -1},
        15, "The preventive detentions spark minor scuffles between protestors and police in Dhar town.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        13, "The criticism is labeled as opportunistic by the ruling party, failing to gain wider support.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The central meeting is postponed, leaving the state administration to manage the local standoff alone.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-02: Cow protection measures
nk = f"{short_code}_2003_02_cow_protection"
news_items.append({
    "newsKey": nk, "month": "2003-02",
    "title": "Government Announces Cow Protection and Goshala Subsidies (2003-02)",
    "description": "In a move seen as countering the BJP's Hindutva campaign, the Congress government announces cow protection measures, including increased subsidies for rural goshalas (cow shelters). The policy shift sparks debates on secular priorities.",
    "issueTags": ["politics", "identity"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "cow_protection",
        "The Animal Husbandry Department issues orders to release the goshala subsidies to certified local trusts.",
        "BJP leaders call the move a political gimmick and demand a complete ban on cow slaughter instead.",
        "All-party representatives support the goshala funding, agreeing to set up oversight boards for animal welfare.",
        "The Animal Husbandry Minister declines to comment on whether the funding is politically motivated.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpIdentityMemory": -1}, {"mpIdentityMemory": 1}, {"mpStabilityMemory": -1},
        14, "Reports emerge of local trusts misappropriating goshala funds, drawing critical media coverage.", {"partyMorale": -2, "corruptionScore": 2, "mediaImage": -2, "publicSupport": -2},
        12, "The demands are criticized by secular allies who accuse the BJP of moving the goalposts.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Oversight boards are delayed by a lack of volunteers in several remote districts.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-03: Uma Bharti named CM candidate
nk = f"{short_code}_2003_03_uma_bharti_campaign"
news_items.append({
    "newsKey": nk, "month": "2003-03",
    "title": "BJP Formally Names Uma Bharti as CM Candidate (2003-03)",
    "description": "The BJP central leadership formally names Uma Bharti as its CM candidate for the upcoming assembly elections. She launches a statewide tour, targeting the Congress government's infrastructure record and power supply failures.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "uma_bharti_campaign",
        "Congress leaders highlight the government's literacy and decentralized panchayat achievements in response.",
        "BJP state units launch coordinated campaign rallies in major cities, showcasing Uma Bharti's leadership.",
        "Both parties agree to limit campaign hoardings in heritage zones during the pre-election phase.",
        "The Congress spokesperson declines to comment on the opposition's CM candidate choice.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpIdentityMemory": 1}, {"mpStabilityMemory": -1},
        13, "Internal Congress factional squabbles over constituency planning dilute the impact of their counter-campaign.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "Uma Bharti's aggressive campaign statements spark a minor controversy, drawing negative press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "The hoarding agreement is violated by local party workers in Bhopal, drawing minor municipal fines.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-04: Bhojshala ASI order
nk = f"{short_code}_2003_04_bhojshala_asi_order"
news_items.append({
    "newsKey": nk, "month": "2003-04",
    "title": "ASI Permits Tuesday Prayers at Bhojshala Shrine (2003-04)",
    "description": "The Archaeological Survey of India issues an order permitting Hindu prayers at the Bhojshala monument on Tuesdays, while Friday prayers remain for Muslims. The compromise eases communal tensions slightly, though both sides claim incomplete victory.",
    "issueTags": ["identity", "governance"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "bhojshala_asi_order",
        "The state government implements security arrangements to ensure peaceful conduct of Tuesday prayers in Dhar.",
        "BJP leaders welcome the order but maintain their demand for full access to the historic site.",
        "A joint peace march is organized by local community elders to celebrate the compromise and promote harmony.",
        "The state administration declines to make a statement on the ASI's compromise formula.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": -1, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpIdentityMemory": 1}, {"mpStabilityMemory": -1},
        12, "Security overheads strain local police units, leading to minor administrative delays in other services.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The ongoing demands are criticized as communal posturing, alienating moderate voters.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Attendance at the peace march is low due to localized rain, limiting its public visibility.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-05: Power shortage rural
nk = f"{short_code}_2003_05_rural_power_crisis"
news_items.append({
    "newsKey": nk, "month": "2003-05",
    "title": "Rural Power Cuts Spark Protests in Malwa and Bundelkhand (2003-05)",
    "description": "As temperatures rise in May, rural power supply drops to less than 6 hours a day in several districts of Malwa and Bundelkhand. Angry farmers block roads and protest outside electricity substations, demanding immediate relief.",
    "issueTags": ["rural", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "rural_power_crisis",
        "The Power Minister announces a temporary diversion of industrial power to supply rural agriculture feeders.",
        "BJP leaders lead farmers' marches, accusing the Congress government of completely destroying the state's power infrastructure.",
        "A joint assembly committee meets to negotiate a temporary power-purchase agreement with neighboring states.",
        "The Electricity Board spokesperson declines to comment on the duration of daily load shedding in rural blocks.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"mpRuralTrustMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        16, "Industrial associations protest the diversion, warning of job losses and factory shutdowns.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "Some marches turn violent, resulting in damage to electricity board property and police action.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Neighboring states refuse to sell power due to their own summer deficits, stalling negotiations.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-06: Janadesh Yatra
nk = f"{short_code}_2003_06_janadesh_yatra"
news_items.append({
    "newsKey": nk, "month": "2003-06",
    "title": "Uma Bharti Launches 'Janadesh Yatra' Campaign Tour (2003-06)",
    "description": "BJP's CM candidate Uma Bharti launches her 'Janadesh Yatra', a statewide campaign tour to mobilize voters. The tour focuses on the Congress government's failure to provide basic infrastructure (sadak, bijli, paani) over the last decade.",
    "issueTags": ["politics", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "janadesh_yatra",
        "Congress leaders organize block-level meetings to highlight the state's welfare and decentralization models.",
        "BJP units organize mass receptions for the yatra, consolidating support in rural constituencies.",
        "Both parties agree to avoid provocative language during campaign rallies to prevent local tensions.",
        "The CM's office declines to comment on the turnout and impact of the Janadesh Yatra.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        14, "Internal Congress squabbles over campaign allocations undermine their block meetings.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "Logistical coordination failures delay the yatra in Bundelkhand, drawing mild local criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        8, "A minor code violation by a local worker leads to a warning from the Election Commission.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-07: Vikas Yatra
nk = f"{short_code}_2003_07_vikas_yatra"
news_items.append({
    "newsKey": nk, "month": "2003-07",
    "title": "Congress Counters with Statewide 'Vikas Yatra' (2003-07)",
    "description": "To counter the BJP's campaign, Chief Minister Digvijaya Singh launches the 'Vikas Yatra', touring districts to inaugurate development projects and highlighting the achievements of Panchayati Raj, primary education, and health missions.",
    "issueTags": ["politics", "governance"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "vikas_yatra",
        "The state administration fast-tracks the inauguration of pending rural school and road projects.",
        "BJP leaders call the Vikas Yatra a waste of public funds and demand the immediate restoration of power supply.",
        "A joint committee is formed to review the code of conduct rules for government-funded inaugurations.",
        "The government spokesperson declines to share the total promotional expenditure of the Vikas Yatra.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpRuralTrustMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        13, "Poor road conditions on the CM's route highlight the opposition's campaign, drawing media focus.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The protest is dismissed as routine opposition posturing, failing to gather neutral voter attention.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "The code review is delayed by the non-participation of senior opposition leaders.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-08: Floods in Rewa and Satna
nk = f"{short_code}_2003_08_rewa_floods"
news_items.append({
    "newsKey": nk, "month": "2003-08",
    "title": "Heavy Rains Cause Flash Flooding in Rewa and Satna (2003-08)",
    "description": "Flash floods triggered by heavy monsoon rains displace thousands of families in Rewa and Satna districts. The administration deploys rescue teams, but opposition leaders accuse the government of slow relief distribution.",
    "issueTags": ["rural", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "rewa_floods",
        "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations.",
        "BJP leaders criticize the relief effort, accusing local officers of bias in distributing aid packages.",
        "A joint legislative relief committee is established to supervise rehabilitation work in Rewa division.",
        "The District Collector declines to release the official crop loss estimates in the first week.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"mpStabilityMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        14, "Logistical failures delay the delivery of tents to remote villages, drawing local protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        12, "The criticism leads to minor scuffles at distribution centers, disrupting relief work.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "The joint committee's operations are slowed down by missing block-level beneficiary records.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-09: Election announced
nk = f"{short_code}_2003_09_election_announced"
news_items.append({
    "newsKey": nk, "month": "2003-09",
    "title": "Election Commission Announces MP Assembly Polls for November (2003-09)",
    "description": "The Election Commission of India announces that assembly polls for the 230 seats of Madhya Pradesh will be held on November 27. The model code of conduct comes into immediate effect, halting new policy announcements.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "election_announced",
        "The ruling Congress focuses on finalizing its candidate list and preparing its election manifesto.",
        "The BJP launches its poll campaign, focusing on infrastructure deficits and promoting Uma Bharti's leadership.",
        "Both parties agree to a joint liaison committee to resolve any model code of conduct disputes quickly.",
        "The party heads decline to comment on the internal selection process for key controversial seats.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        13, "Disgruntled Congress leaders threaten to run as independent candidates in several constituencies.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "Factional squabbles in the BJP's Gwalior unit delay candidate selection in several seats.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Liaison talks break down as both sides trade code violation accusations before the commission.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-10: Power rebate announcement controversy
nk = f"{short_code}_2003_10_power_rebate"
news_items.append({
    "newsKey": nk, "month": "2003-10",
    "title": "Government's Power Rebate Scheme Draws Election Commission Notice (2003-10)",
    "description": "A pre-existing cabinet decision to waive electricity interest dues for small farmers is implemented, drawing a notice from the Election Commission following a BJP complaint. The scheme becomes a flashpoint in the election campaign.",
    "issueTags": ["politics", "rural"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "power_rebate",
        "The state government defends the scheme before the EC as an ongoing policy and requests clearance to proceed.",
        "BJP leaders accuse the Congress of using public resources to buy votes in violation of the model code.",
        "Both parties agree to submit the issue to an independent judicial arbitrator appointed by the EC.",
        "The Power Department declines to comment on the implementation status of the rebate scheme.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpRuralTrustMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        14, "The EC orders a temporary freeze on the rebate scheme, neutralizing its immediate electoral advantage.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The BJP's opposition to the rebate is labeled as anti-farmer by ruling party campaign materials.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "The arbitration process takes too long, failing to resolve the issue before polling day.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-11: Election campaign voting
nk = f"{short_code}_2003_11_assembly_polls"
news_items.append({
    "newsKey": nk, "month": "2003-11",
    "title": "High Turnout Recorded in MP Assembly Elections (2003-11)",
    "description": "Madhya Pradesh records a historic turnout of 67.25% in the assembly elections held on November 27. The high turnout, especially in rural areas, leaves both Congress and BJP claiming confidence in victory.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "assembly_polls",
        "Congress leaders express confidence in their rural development record and grassroots organization.",
        "BJP leaders state the high turnout is a clear public mandate against ten years of Congress misrule.",
        "All parties congratulate the election machinery for conducting peaceful and clean polls.",
        "The party spokespersons decline to comment on early exit poll predictions that favor the BJP.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        13, "Isolated voting booth delay complaints draw minor negative media coverage.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "Overconfident statements by some local BJP candidates trigger minor factional friction.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        8, "Minor disputes over EVM security storage rooms are reported by local observers.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-12: BJP victory Uma sworn in
nk = f"{short_code}_2003_12_landslide_victory"
news_items.append({
    "newsKey": nk, "month": "2003-12",
    "title": "BJP Wins Landslide in MP; Uma Bharti Sworn in as CM (2003-12)",
    "description": "The BJP wins a massive victory in the MP assembly elections, securing 173 out of 230 seats, while the Congress is reduced to 38. Uma Bharti is sworn in as the first woman Chief Minister of the state, ending Digvijaya Singh's decade-long rule.",
    "issueTags": ["politics", "governance"],
    "weights": {"baseSelectionWeight": 1.3, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "landslide_victory",
        "Chief Minister Uma Bharti promises immediate reforms in the power sector and prioritizes road repair works.",
        "The defeated Congress accepts the mandate, stating they will act as a responsible opposition in the house.",
        "The new assembly holds its first session with all parties agreeing to cooperate on the state's financial health.",
        "The outgoing CM's office declines to make any further public statements following the formal handover of power.",
        {"partyMorale": 4, "corruptionScore": 0, "mediaImage": 4, "publicSupport": 4},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 0, "mediaImage": -3, "publicSupport": -3},
        {"mpStabilityMemory": -2}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        15, "Delays in cabinet allocation spark early lobbying and minor murmurs among senior BJP MLAs.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "Internal Congress recriminations over candidate selection leak to the press, causing embarrassment.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over the assembly speaker selection mar the cooperative spirit of the first session.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-12"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004
# 2004-01: Land review order
nk = f"{short_code}_2004_01_land_review"
news_items.append({
    "newsKey": nk, "month": "2004-01",
    "title": "New Government Orders Review of Congress-Era Land Distributions (2004-01)",
    "description": "Chief Minister Uma Bharti orders a comprehensive review of land distributed to Dalit and tribal families under the previous Congress administration's Bhopal Agenda. The government alleges massive irregularities, while Congress calls the review anti-Dalit.",
    "issueTags": ["land_rights", "politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "land_rights"},
    "reactionOptions": create_reactions(
        nk, "land_review",
        "The Revenue Department sets up inquiry committees to verify land titles and reclaim illegally occupied government plots.",
        "Congress opposition leaders organize rallies protesting the review, claiming it aims to dispossess poor families.",
        "A joint legislative review panel is formed to oversee the verification process and ensure fair titles are protected.",
        "The Chief Minister's office declines to comment on the number of land titles currently under investigation.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpRuralTrustMemory": 1}, {"mpRuralTrustMemory": -1}, {"mpStabilityMemory": -1},
        14, "Protests by beneficiary groups delay the inquiry committees' operations in southern districts.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "The protests are labeled by the ruling party as defending illegal encroachment of government lands.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The review panel's work is stalled due to non-cooperation by local revenue record keepers.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-02: Industrial policy Pithampur
nk = f"{short_code}_2004_02_industrial_policy"
news_items.append({
    "newsKey": nk, "month": "2004-02",
    "title": "Government Announces New Industrial Policy for Pithampur Hub (2004-02)",
    "description": "The state government unveils a new industrial policy, offering tax concessions and fast-tracked land allotments to attract manufacturing investments to the Pithampur industrial area near Indore. Business chambers welcome the policy.",
    "issueTags": ["infrastructure", "economy"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "industrial_policy",
        "The Industry Department establishes a single-window clearance cell to process investment applications rapidly.",
        "Opposition leaders claim the policy favors large corporate houses at the expense of local small-scale industries.",
        "A joint government-industry coordination committee is formed to monitor infrastructure upgrades in Pithampur.",
        "The Industry Minister declines to share the estimated revenue loss due to the new tax concessions.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpCorruptionMemory": 1}, {"mpStabilityMemory": -1},
        13, "Administrative delays stall the single-window clearance cell, drawing criticism from investors.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "Small-scale industry unions distance themselves from the opposition's protests, weakening the criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Coordination meetings are delayed by disagreements over municipal tax sharing inside the industrial zone.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-03: Lok Sabha election campaign
nk = f"{short_code}_2004_03_loksabha_campaign"
news_items.append({
    "newsKey": nk, "month": "2004-03",
    "title": "Lok Sabha Campaign Intensifies Across Madhya Pradesh (2004-03)",
    "description": "Campaigning for the 2004 general elections picks up pace in MP. The ruling BJP seeks to capitalize on its recent assembly victory, while the Congress tries to regain lost ground by focusing on national secular themes.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "loksabha_campaign",
        "The BJP campaigns on a platform of developmental progress and the 'India Shining' national theme.",
        "Congress leaders focus on rural unemployment and criticize the BJP's economic policies in campaign rallies.",
        "Both parties agree to limit loudspeaker usage during late hours to avoid disturbing students during exams.",
        "The state election coordinators decline to comment on reports of internal candidate disputes.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        12, "The 'India Shining' theme fails to connect with poor rural voters, drawing mild press criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "Factional squabbles within the Congress's state unit limit the reach of their rural campaigns.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Local campaign workers violate the loudspeaker timings in Gwalior, drawing warnings from the EC.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-04: Polling Lok Sabha
nk = f"{short_code}_2004_04_loksabha_polls"
news_items.append({
    "newsKey": nk, "month": "2004-04",
    "title": "Voting Held for Lok Sabha Seats in MP (2004-04)",
    "description": "Polling is held across MP's 29 Lok Sabha constituencies. Security is tight, particularly in the Naxal-affected Balaghat and Chambal regions, to ensure peaceful voting under the supervision of central observers.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "loksabha_polls",
        "The state administration coordinates logistics and deploys home guards to assist central security forces.",
        "Opposition parties watch voting closely, raising concerns over alleged local administration bias in rural booths.",
        "All parties issue a joint statement appreciating the peaceful conduct of elections in tribal zones.",
        "The State Election Commissioner declines to comment on the final voter turnout figures in the first day.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        13, "Voting delays due to EVM malfunctions in some booths draw local complaints and press criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The allegations are dismissed by independent observers, neutralizing the opposition's claims.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        8, "Minor disputes over election duty staff accommodation are reported in tribal blocks.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-05: Uma Bharti resignation offer
nk = f"{short_code}_2004_05_resignation_offer"
news_items.append({
    "newsKey": nk, "month": "2004-05",
    "title": "CM Uma Bharti Briefly Submits Resignation Over National Politics (2004-05)",
    "description": "In a dramatic move, CM Uma Bharti submits her resignation to the Governor in protest against the possibility of Sonia Gandhi becoming Prime Minister of India. She later withdraws it after the national political situation stabilizes.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "resignation_offer",
        "The Chief Minister's office clarifies the resignation was a symbolic protest and announces the resumption of work.",
        "Congress leaders label the resignation offer a theatrical stunt that ignored the administrative needs of MP.",
        "BJP and Congress leaders agree to maintain legislative decorum and avoid personal attacks in the house.",
        "The BJP state office declines to comment on internal discussions regarding the symbolic resignation.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        14, "The dramatic move raises questions about state administrative stability, drawing critical editorials.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The criticism is dismissed by nationalistic voters who support Bharti's symbolic stance.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Bickering over the incident disrupts the next day's assembly proceedings, drawing negative press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-06: Bundelkhand water security package
nk = f"{short_code}_2004_06_bundelkhand_water"
news_items.append({
    "newsKey": nk, "month": "2004-06",
    "title": "Government Announces Water Security Package for Bundelkhand (2004-06)",
    "description": "To address chronic drought in the Bundelkhand region, the state government announces a special water security package. The project funds local lake restorations and tank construction, aiming to improve groundwater levels.",
    "issueTags": ["rural", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "bundelkhand_water",
        "The Water Resources Department releases special funds to village panchayats in Tikamgarh and Chhatarpur.",
        "Congress opposition leaders claim the package is underfunded and demand major canal networking projects instead.",
        "A joint committee of Bundelkhand MLAs is formed to monitor the execution and quality of local tank restorations.",
        "The Irrigation Department declines to provide a target timeline for the completion of the lake restorations.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"mpRuralTrustMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        15, "Local administrative delays stall fund releases to several remote village panchayats.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The opposition's demands are dismissed by local councils who prefer decentralized water management.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "The joint monitoring committee's inspections are slowed down by extreme summer temperatures.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-07: Bhopal lake demolition drive
nk = f"{short_code}_2004_07_bhopal_lake_cleanup"
news_items.append({
    "newsKey": nk, "month": "2004-07",
    "title": "Demolition Drive Launched Near Bhopal Lakes (2004-07)",
    "description": "Following a High Court order, the Bhopal Municipal Corporation launches a demolition drive against illegal commercial encroachments around the Upper Lake. The drive aims to protect the city's primary drinking water source.",
    "issueTags": ["infrastructure", "protest"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "bhopal_lake_cleanup",
        "The municipal corporation carries out the demolitions and announces plans to build a protective buffer zone.",
        "Opposition leaders protest the drive, claiming it displaces small local vendors without alternative relocation.",
        "A joint committee of municipal and trader representatives is formed to negotiate relocation sites.",
        "The Municipal Commissioner declines to share the list of commercial properties exempted from the demolition.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpCorruptionMemory": 1}, {"mpStabilityMemory": -1},
        13, "Clashes between vendors and municipal police lead to temporary suspension of the cleanup drive.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "Environmental groups criticize the opposition's stance, arguing it defends lake polluters.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Relocation site selection is delayed due to high land acquisition costs, leaving vendors stranded.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-08: Hubli warrant Uma resigns Babulal Gaur CM
nk = f"{short_code}_2004_08_bharti_resigns"
news_items.append({
    "newsKey": nk, "month": "2004-08",
    "title": "Uma Bharti Resigns; Babulal Gaur Sworn in as CM (2004-08)",
    "description": "Uma Bharti resigns as Chief Minister after a Karnataka court issues a non-bailable warrant against her in connection with a 1994 rioting case in Hubli. Babulal Gaur is sworn in as the 16th Chief Minister of Madhya Pradesh.",
    "issueTags": ["politics", "governance"],
    "weights": {"baseSelectionWeight": 1.3, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "bharti_resigns",
        "The new CM Babulal Gaur promises continuity in development schemes and pledges to improve state highways.",
        "Congress opposition leaders call the change a sign of internal BJP instability and demand fresh elections.",
        "The assembly passes a resolution thanking Uma Bharti for her service and welcoming the new CM.",
        "The CM's office declines to comment on the ongoing legal proceedings of the Hubli court case.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -2}, {"mpStabilityMemory": 1}, {"mpStabilityMemory": -1},
        15, "Uma Bharti's loyalists in the cabinet express early discontent, threatening minor administrative friction.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        13, "The demand for fresh elections is rejected by political observers, limiting the opposition's momentum.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Bickering over the resolution wording disrupts the first assembly session under the new CM.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-09: Babulal Gaur road repair focus
nk = f"{short_code}_2004_09_gaur_roads"
news_items.append({
    "newsKey": nk, "month": "2004-09",
    "title": "CM Babulal Gaur Announces Special Road Repair Drive (2004-09)",
    "description": "Chief Minister Babulal Gaur announces a high-profile road repair drive, promising to make major state highways pothole-free within three months. The initiative, dubbed 'Gaur roads', aims to address the public's key infrastructure concern.",
    "issueTags": ["infrastructure", "governance"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "gaur_roads",
        "The PWD releases special emergency funds and starts round-the-clock repair works on the Bhopal-Indore highway.",
        "Congress opposition leaders claim the road repairs are cosmetic and ignore structural quality standards.",
        "A joint assembly panel is established to monitor highway work quality and audit contractor expenses.",
        "The PWD office declines to release the contractor-wise budget allocations for the repair drive.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpCorruptionMemory": 1}, {"mpStabilityMemory": -1},
        14, "Late monsoon showers wash away newly laid asphalt, drawing critical local media coverage.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        11, "The criticism is dismissed by motorist associations who welcome any immediate road improvement.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "The monitoring panel's work is slowed down by delays in submitting laboratory test reports.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-10: Power subsidy restructuring
nk = f"{short_code}_2004_10_subsidy_restructuring"
news_items.append({
    "newsKey": nk, "month": "2004-10",
    "title": "Government Restructures Rural Power Subsidies (2004-10)",
    "description": "The state government restructures the power subsidy program, limiting free electricity to small farmers with land holdings below 5 acres. The move aims to cut fiscal deficit but draws protests from farmer unions.",
    "issueTags": ["rural", "economy"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "subsidy_restructuring",
        "The state releases guidelines to identify eligible small farmers and promises targeted irrigation support.",
        "Congress opposition leaders protest the restriction, demanding continuation of power subsidies for all cultivators.",
        "A joint committee is formed to negotiate the land-holding threshold and draft a balanced farm package.",
        "The Finance Department declines to comment on the estimated annual savings from the restructuring.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"mpRuralTrustMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        15, "Delays in verification leave many eligible small farmers without subsidized bills, sparking local protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The demands are criticized by urban voter groups who support fiscal reforms and deficit cuts.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Committee talks break down as members disagree on the definition of marginal land holdings.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-11: Land allotment irregularities Congress raise
nk = f"{short_code}_2004_11_allotment_scandal"
news_items.append({
    "newsKey": nk, "month": "2004-11",
    "title": "Congress Raises Questions on BJP Land Allotments in Bhopal (2004-11)",
    "description": "The opposition Congress raises allegations of irregularities in the allotment of premium commercial land plots to trusts aligned with right-wing groups in Bhopal. The government denies the charges, claiming all rules were followed.",
    "issueTags": ["corruption", "politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "corruption"},
    "reactionOptions": create_reactions(
        nk, "allotment_scandal",
        "The Urban Development Department orders a departmental inquiry to verify the allotment procedure of the disputed plots.",
        "Congress opposition leaders demand a judicial probe and stage protests outside the municipal offices.",
        "A multi-party legislative subcommittee is formed to review land allotment guidelines for religious and social trusts.",
        "The Urban Development Minister declines to release the bid details and allotment prices of the plots.",
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpCorruptionMemory": -1}, {"mpCorruptionMemory": 1}, {"mpStabilityMemory": -1},
        14, "The departmental inquiry is criticized as a whitewash by local newspapers, affecting media image.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -1},
        12, "The protests are labeled by the ruling party as an attack on legitimate social organizations.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "The legislative subcommittee's meetings are delayed by the non-submission of municipal records.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-12: Bhopal Gas tragedy 20th anniversary
nk = f"{short_code}_2004_12_gas_anniversary"
news_items.append({
    "newsKey": nk, "month": "2004-12",
    "title": "State Observes 20th Anniversary of Bhopal Gas Tragedy (2004-12)",
    "description": "On the 20th anniversary of the Bhopal Gas disaster, survivors' groups and international activists organize rallies demanding complete environmental cleanup of the Union Carbide site. The government faces scrutiny over slow rehabilitation efforts.",
    "issueTags": ["protest", "governance"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "gas_anniversary",
        "The state government announces a special medical aid package and pledges to coordinate toxic waste disposal with central agencies.",
        "Opposition parties criticize the government for failing to secure adequate compensation and cleanup funds from the parent company.",
        "A joint legislative-survivor liaison committee is formed to monitor health services and clean-up operations.",
        "The Bhopal Gas Relief Department declines to share the status of clean-up funds spent over the past decade.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"mpStabilityMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        15, "Delays in chemical waste disposal coordinate tests trigger fresh protests by local residents.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The opposition's criticism is dismissed by central authorities who highlight existing legal settlements.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over survivor representative selection stall the liaison committee's first meeting.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-12"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005
# 2005-01: Uma Bharti public friction with Gaur
nk = f"{short_code}_2005_01_party_factionalism"
news_items.append({
    "newsKey": nk, "month": "2005-01",
    "title": "Internal Friction Mounts in State BJP (2005-01)",
    "description": "Reports of growing factionalism within the state BJP emerge as supporters of former CM Uma Bharti openly criticize Chief Minister Babulal Gaur's working style. The public disagreements create administrative uncertainty in Bhopal.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "party_factionalism",
        "CM Babulal Gaur meets central BJP leaders in New Delhi and seeks intervention to maintain state party discipline.",
        "Congress opposition leaders call the infighting a proof that the BJP administration is too divided to govern.",
        "Senior state BJP leaders hold a closed-door meeting to address concerns and project a united front.",
        "The BJP state spokesperson declines to comment on the reports of factional disputes.",
        {"partyMorale": 1, "corruptionScore": 0, "mediaImage": 1, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        14, "Leaks from the Delhi meeting fuel further media speculation about leadership changes.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The criticism is ignored by voters who view it as standard opposition exploitation of internal issues.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Several key legislators skip the unity meeting, diluting its positive impact in the press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-02: Municipal corporation elections
nk = f"{short_code}_2005_02_municipal_polls"
news_items.append({
    "newsKey": nk, "month": "2005-02",
    "title": "Municipal Corporation Election Results Announced (2005-02)",
    "description": "Results for several key municipal corporations are announced. While the BJP retains control of major cities like Indore and Bhopal, the Congress makes significant gains in Jabalpur and Gwalior, indicating shifting urban voter sentiment.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "municipal_polls",
        "The BJP government welcomes the urban mandates and promises to accelerate infrastructure funding for all corporations.",
        "Congress leaders hail their gains as a clear rejection of the Babulal Gaur administration's urban development record.",
        "Both parties agree to cooperate on municipal tax reforms to improve local body finances.",
        "The State Election Commissioner declines to comment on requests to review voting counts in disputed wards.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        13, "Disputes over specific ward project allocations stall municipal council meetings in Jabalpur.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The Congress claims are labeled as exaggerated by political observers, limiting their public impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Disagreements over the tax sharing formula stall the municipal finance reforms.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-03: Budget session farm debt walkout
nk = f"{short_code}_2005_03_budget_walkout"
news_items.append({
    "newsKey": nk, "month": "2005-03",
    "title": "Opposition Stages Assembly Walkout Over Rising Farm Debt (2005-03)",
    "description": "During the assembly's budget session, opposition Congress MLAs stage a dramatic walkout, protesting the government's refusal to waive cooperative loans for dryland farmers. The walkout draws attention to rising agricultural distress.",
    "issueTags": ["politics", "rural"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "budget_walkout",
        "The Finance Minister announces an interest subvention scheme on farm loans to provide immediate relief.",
        "Congress leaders lead protests outside district banks, demanding a complete loan waiver for small farmers.",
        "A joint assembly panel is established to evaluate crop damage and recommend credit restructuring options.",
        "The Agriculture Minister declines to comment on the farm loan waiver demands during the budget press meet.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"mpRuralTrustMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        14, "Implementation delays at local cooperative banks prevent many small farmers from getting subvention certificates.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "Some bank protests lead to localized scuffles, drawing criticism from depositor groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "The joint panel's field visits are delayed by lack of administrative vehicle support.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-04: Thermal power plants MOU
nk = f"{short_code}_2004_04_thermal_mous"
news_items.append({
    "newsKey": nk, "month": "2005-04",
    "title": "Government Signs MOUs for Thermal Power Plants (2005-04)",
    "description": "To address the state's chronic electricity deficit, the government signs MOUs with private power companies to set up thermal power projects. Environmentalists and farmers raise concerns over land acquisition and water usage.",
    "issueTags": ["infrastructure", "economy"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "thermal_mous",
        "The Power Department coordinates environmental clearances and promises fair land compensation packages.",
        "Opposition leaders demand that the MOUs be tabled in the assembly for public review and scrutiny.",
        "A joint environment-industry oversight panel is formed to review project water sharing guidelines.",
        "The Energy Minister declines to share the details of private developer concessions under the MOUs.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpCorruptionMemory": 1}, {"mpStabilityMemory": -1},
        14, "Local farmer protests against land acquisition stall the initial survey work in Singrauli.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        11, "The demand is dismissed as obstructionist by business groups who support power expansion.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Oversight panel meetings stall as developer representatives dispute the water allocation caps.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-05: Heatwave Chambal water tankers
nk = f"{short_code}_2005_05_chambal_drought"
news_items.append({
    "newsKey": nk, "month": "2005-05",
    "title": "Severe Heatwave Triggers Drinking Water Crisis in Chambal (2005-05)",
    "description": "An intense heatwave in May dries up local wells and ponds in the Chambal region, leading to a critical drinking water crisis. The administration deploys emergency water tankers, but remote hamlets report major shortages.",
    "issueTags": ["rural", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "chambal_drought",
        "The Public Health Engineering Department releases emergency funds to drill borewells and deploy private tankers.",
        "Congress opposition leaders hold dharnas outside administrative offices, accusing the PWD of failing to prepare.",
        "A joint water task force is formed to manage daily supply allocations to the worst-affected blocks.",
        "The Public Health Engineering Minister declines to give a timeline for restoring piped water supply.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"mpRuralTrustMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        14, "Private water tanker operators charge illegal premiums, drawing local public anger and media focus.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        12, "Protests are labeled by the ruling party as creating public panic, limiting their wider impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Task force coordination fails as local block officers report a lack of fuel for water tankers.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-06: Doctors strike
nk = f"{short_code}_2005_06_doctors_strike"
news_items.append({
    "newsKey": nk, "month": "2005-06",
    "title": "Junior Doctors in Government Hospitals Strike (2005-06)",
    "description": "Junior doctors in major government medical colleges and hospitals launch a strike, demanding better stipends and security in wards. The strike paralyzes emergency services, drawing criticism from patient advocacy groups.",
    "issueTags": ["protest", "governance"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "doctors_strike",
        "The Health Department initiates talks with strike representatives and offers a partial stipend hike.",
        "Congress leaders support the doctors, demanding the government immediately meet all safety requirements.",
        "A joint committee of health administrators, doctors, and legislators is formed to negotiate safety terms.",
        "The Health Minister invokes the ESMA act, threatening to expel striking junior doctors from colleges.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"mpStabilityMemory": -1}, {"mpCorruptionMemory": 1}, {"mpStabilityMemory": -1},
        14, "The stipend hike proposal is rejected by striking associations, prolonging the healthcare deadlock.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "Strikers distance themselves from political parties, limiting the opposition's campaign mileage.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Committee talks break down as doctor representatives demand immediate installation of CCTV cameras.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-07: Babulal Gaur cabinet comments rift
nk = f"{short_code}_2005_07_cabinet_friction"
news_items.append({
    "newsKey": nk, "month": "2005-07",
    "title": "CM Babulal Gaur's Comments Spark Cabinet Tension (2005-07)",
    "description": "Chief Minister Babulal Gaur makes candid remarks during a public meeting, criticizing the performance of several cabinet ministers. The comments provoke anger from Uma Bharti's loyalists in the cabinet, fueling talks of a leadership change.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "cabinet_friction",
        "CM Gaur issues a clarification statement to the press and holds a cabinet reconciliation dinner in Bhopal.",
        "Congress opposition leaders claim the public bickering shows the state government is completely paralyzed.",
        "Senior state party leaders hold a closed-door coordination meet to resolve differences among ministers.",
        "The CM's office declines to comment on reports of letters sent to the party's central high command.",
        {"partyMorale": 1, "corruptionScore": 0, "mediaImage": 1, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        14, "Several key ministers boycott the reconciliation dinner, highlighting the ongoing split.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The criticism is dismissed as political opportunism by voters who support local BJP legislators.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "The coordination meeting ends without any agreement on ministerial portfolio reallocations.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-08: Shipra river flooding Ujjain
nk = f"{short_code}_2005_08_ujjain_floods"
news_items.append({
    "newsKey": nk, "month": "2005-08",
    "title": "Heavy Rains Trigger Flooding of Shipra River in Ujjain (2005-08)",
    "description": "Continuous heavy rainfall causes the Shipra river in Ujjain to rise rapidly, flooding the low-lying ghats and surrounding residential areas. The administration executes evacuations, but residents complain of inadequate shelter facilities.",
    "issueTags": ["rural", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "ujjain_floods",
        "The municipal administration sets up emergency shelters in public schools and provides cooked meals.",
        "Opposition leaders visit the flooded ghats, accusing the administration of ignoring warnings and slow rescue.",
        "A joint legislative-trust committee is established to supervise relief work and plan ghat drain upgrades.",
        "The District Collector declines to release estimate figures for municipal property damage in the first week.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"mpStabilityMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        14, "Shelter facilities report shortage of drinking water, drawing critical local newspaper coverage.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        12, "The visit is labeled as campaign posturing by ruling party spokespersons, limiting its impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Ghat drainage plans are delayed due to disputes over the municipal trust's fund sharing.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-09: Cooperative bank scam
nk = f"{short_code}_2005_09_bank_scandal"
news_items.append({
    "newsKey": nk, "month": "2005-09",
    "title": "Irregularities Uncovered in State Cooperative Banks (2005-09)",
    "description": "A financial audit uncovers major irregularities and illegal credit extensions in state-run cooperative banks, leading to temporary freezes on farmer deposits. The opposition Congress demands a judicial probe into cooperative board members.",
    "issueTags": ["corruption", "rural"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "corruption"},
    "reactionOptions": create_reactions(
        nk, "bank_scandal",
        "The Cooperative Department suspends the boards of the irregular banks and orders a forensic audit.",
        "Congress opposition leaders demand a judicial probe and stage protests outside bank head offices.",
        "A multi-party legislative subcommittee is formed to draft credit guidelines for cooperative institutions.",
        "The Cooperative Minister declines to comment on the total volume of frozen farmer deposits.",
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpCorruptionMemory": -1}, {"mpCorruptionMemory": 1}, {"mpStabilityMemory": -1},
        15, "The forensic audit is delayed, prolonging the freeze on farmer accounts and drawing public anger.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "Bank protests lead to minor property damage at a rural branch, drawing public disapproval.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Subcommittee talks are slowed down by disagreements over government representation on bank boards.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-10: BJP leadership change speculation
nk = f"{short_code}_2005_10_leadership_speculation"
news_items.append({
    "newsKey": nk, "month": "2005-10",
    "title": "BJP High Command Steps in Amid State Leadership Speculation (2005-10)",
    "description": "As internal factionalism persists in Bhopal, senior BJP national leaders arrive to consult with state legislators. The consultations fuel speculation that the party's central leadership is planning to replace Babulal Gaur.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "leadership_speculation",
        "CM Gaur states he continues to enjoy the party's support and focus remains on highway development projects.",
        "Congress opposition leaders claim the ongoing BJP leadership crisis has completely paralyzed the state administration.",
        "State party leaders agree to maintain unity and issue a joint statement supporting the party's decision.",
        "The state BJP office declines to comment on the central leaders' discussions in Bhopal.",
        {"partyMorale": 1, "corruptionScore": 0, "mediaImage": 1, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        14, "Leaks from the consultations fuel further media rumors, creating minor administrative delays.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        11, "The allegations are dismissed as political posturing, failing to gather wider public attention.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "The unity statement is delayed due to disagreements over the wording of state leadership support.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-11: Babulal Gaur resigns Shivraj CM
nk = f"{short_code}_2005_11_chouhan_sworn_in"
news_items.append({
    "newsKey": nk, "month": "2005-11",
    "title": "Babulal Gaur Resigns; Shivraj Singh Chouhan Sworn in as CM (2005-11)",
    "description": "Babulal Gaur resigns as Chief Minister following directives from the BJP national leadership. Shivraj Singh Chouhan is elected leader of the legislature party and sworn in as the 17th Chief Minister of Madhya Pradesh.",
    "issueTags": ["politics", "governance"],
    "weights": {"baseSelectionWeight": 1.3, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "chouhan_sworn_in",
        "The new CM Shivraj Singh Chouhan announces a five-point development agenda, focusing on agriculture and rural welfare.",
        "Congress opposition leaders claim the third CM in two years shows the BJP's complete failure to provide stability.",
        "The assembly passes a resolution welcoming the new CM and promising cooperative legislative work.",
        "The BJP spokesperson declines to comment on details of the internal party discussions that led to Gaur's resignation.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"mpStabilityMemory": -2}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        14, "Minor portfolios delays spark early murmurs among some senior BJP legislators.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "The stability claims are ignored by voters who welcome Chouhan's developmental promises.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Disagreements over committee seat allocations disrupt the first day of assembly sessions.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-12: Panchamrut agenda
nk = f"{short_code}_2005_12_panchamrut_agenda"
news_items.append({
    "newsKey": nk, "month": "2005-12",
    "title": "CM Chouhan Launches 'Panchamrut' Development Program (2005-12)",
    "description": "Chief Minister Shivraj Singh Chouhan launches the 'Panchamrut' program, a development initiative focusing on five key areas: infrastructure, agriculture, health, education, and social security. The program aims to boost rural growth.",
    "issueTags": ["governance", "rural"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "panchamrut_agenda",
        "The government releases special budgetary allocations to launch the Panchamrut projects across all blocks.",
        "Opposition leaders call the program a rebranding of old schemes and demand clear project timelines.",
        "A joint government-expert advisory board is formed to track the implementation of the Panchamrut targets.",
        "The CM's office declines to publish the project-wise funding breakdown for the Panchamrut program.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"mpRuralTrustMemory": -1}, {"mpRuralTrustMemory": 1}, {"mpStabilityMemory": -1},
        13, "Budgetary constraints delay project launches in several remote tribal blocks.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The criticism is ignored by rural organizations who support the target sectors.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "The advisory board's first review meeting is delayed due to missing department reports.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
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
    "sourceNotes": "Government: INC/Digvijaya Singh CM through Dec 2003, then BJP (Uma Bharti CM Dec 2003 - Aug 2004, Babulal Gaur CM Aug 2004 - Nov 2005, Shivraj Singh Chouhan CM from Nov 2005 through the end of this period). Opposition: BJP until Dec 2003, then INC. Main issues: Decentralized governance, bifurcation challenges with Chhattisgarh, the Dalit Bhopal Declaration, Dhar Bhojshala communal disputes, and the chronic infrastructure issues (sadak, bijli, paani) that led to the historic 2003 power shift. Built programmatically matching the schema and calibration constraints.",
    "defaults": {
        "weights": {
            "baseSelectionWeight": 1.0,
            "reactionProfile": "default"
        }
    },
    "newsItems": news_items
}

output_path = Path("seed-data/review/madhya_pradesh_2001_news.json")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(json.dumps(data, indent=2))
print("Successfully generated madhya_pradesh_2001_news.json with", len(news_items), "news items!")
