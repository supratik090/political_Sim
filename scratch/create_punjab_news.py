import json
from pathlib import Path

# Define the scenario metadata
scenario_key = "punjab_2001"
short_code = "pb2001"

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
# 2001-01: Free power to farmers SAD
nk = f"{short_code}_2001_01_free_power"
news_items.append({
    "newsKey": nk, "month": "2001-01",
    "title": "CM Badal Announces Continued Free Electricity for Tubewells (2001-01)",
    "description": "Chief Minister Parkash Singh Badal announces that the state government will continue providing free power to agricultural tubewells, despite rising concerns over the mounting deficits of the Punjab State Electricity Board. Opposition Congress leaders warn of impending financial collapse.",
    "issueTags": ["rural", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "free_power",
        "The SAD government releases special grants to the electricity board to cover agricultural power subsidies.",
        "Opposition Congress leaders demand a cap on free power for wealthy landowners to protect state finances.",
        "All-party representatives agree to set up a legislative commission to study power sector restructuring.",
        "The State Electricity Board officials decline to comment on the projected annual deficit under the free power policy.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": 1}, {"punjabStabilityMemory": -1},
        14, "Financial institutions delay credit lines to Punjab due to the subsidy burden, drawing negative editorials.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The demand alienates the farmer base in rural constituencies, drawing local protests.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Restructuring talks stall as members disagree on the level of government equity in the board.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-02: SGPC budget dispute
nk = f"{short_code}_2001_02_sgpc_budget"
news_items.append({
    "newsKey": nk, "month": "2001-02",
    "title": "SGPC Budget Session Marred by Factional Bickering (2001-02)",
    "description": "The budget session of the Shiromani Gurdwara Parbandhak Committee (SGPC) faces disruptions as rival factions within the Shiromani Akali Dal challenge the leadership's spending priorities. The public dispute highlights growing political tensions over religious body control.",
    "issueTags": ["politics", "identity"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "sgpc_budget",
        "SAD Chief Badal holds closed-door meetings to reconcile factions and passes the SGPC budget with a majority.",
        "Opposition Congress leaders demand transparency and judicial oversight in the management of historical Gurdwara funds.",
        "A joint committee of religious elders and political leaders is formed to review Gurdwara administration rules.",
        "The SGPC executive committee declines to comment on specific allegations of financial irregularities raised by members.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabIdentityMemory": 1}, {"punjabCorruptionMemory": 1}, {"punjabIdentityMemory": -1},
        13, "Disgruntled faction leaders walk out, carrying their protests to regional media outlets.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The demand is criticized as political interference in Sikh religious affairs, drawing minor backlash.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Committee talks break down over terms of representation, failing to draft any reform guidelines.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-03: Cotton bollworm Bhatinda
nk = f"{short_code}_2001_03_cotton_bollworm"
news_items.append({
    "newsKey": nk, "month": "2001-03",
    "title": "Bollworm Infestation Hits Cotton Crop in Bhatinda (2001-03)",
    "description": "Cotton growers in Bhatinda and Mansa districts report widespread crop damage due to a severe bollworm infestation. Farmers hold demonstrations accusing the state agriculture department of failing to supply quality pesticides.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "cotton_bollworm",
        "The Agriculture Department announces compensation grants and initiates investigations into spurious pesticide distributors.",
        "Congress opposition leaders visit affected fields, demanding a complete waiver of canal water cess for cotton growers.",
        "A joint assembly committee is formed to evaluate the crop damage and coordinate relief measures with central teams.",
        "The Director of Agriculture declines to specify the estimated acreage of crop damage in the Malwa region.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"punjabRuralTrustMemory": 1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        14, "Pesticide dealer lobbies protest the investigations, disrupting supply chains in other districts.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        12, "The demands are labeled by the ruling coalition as fiscally unfeasible during a revenue deficit.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The central team's visit is delayed, stalling the disbursement of joint relief funds.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-04: Wheat procurement storage
nk = f"{short_code}_2001_04_wheat_storage"
news_items.append({
    "newsKey": nk, "month": "2001-04",
    "title": "Wheat Procurement Suffer Storage Constraints (2001-04)",
    "description": "As the spring wheat harvest peaks, state procurement agencies report a severe shortage of covered storage space in grain markets. Millions of tons of wheat are stored in the open, risking damage from unseasonal rains.",
    "issueTags": ["rural", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "wheat_storage",
        "The Food and Civil Supplies Department leases private warehouses and fast-tracks grain movement to central pools.",
        "Congress opposition leaders hold protests at grain markets, accusing the government of logistical incompetence.",
        "A joint legislative-farmer task force is formed to monitor grain lifting and resolve local market bottlenecks.",
        "The Food Commissioner declines to release figures on the volume of wheat currently stored without rain covers.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"punjabRuralTrustMemory": 1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        13, "Rail wagon shortages delay grain movement, leaving open yards vulnerable to brief showers.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        11, "The protests lead to minor traffic blocks near mandis, drawing criticism from local traders.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Task force meetings are delayed by the non-participation of transport union representatives.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-05: Employees DA strike
nk = f"{short_code}_2001_05_da_strike"
news_items.append({
    "newsKey": nk, "month": "2001-05",
    "title": "Government Employees Strike Over Dearness Allowance Delays (2001-05)",
    "description": "State government employees in Punjab go on strike, protesting against the delay in the release of dearness allowance installments. The strike halts work in treasury offices, schools, and administrative departments.",
    "issueTags": ["protest", "economy"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "da_strike",
        "The Finance Minister promises a phased release of the dearness allowance and initiates talks with employee unions.",
        "Opposition leaders support the strike, accusing the Badal administration of empty coffers and fiscal failure.",
        "A joint legislative-union panel is formed to negotiate salary adjustments within budget constraints.",
        "The administration invokes the ESMA act to force striking workers back to their departments.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"punjabStabilityMemory": 1}, {"punjabCorruptionMemory": 1}, {"punjabStabilityMemory": -1},
        14, "The phased release proposal is rejected by union hardliners, extending the administrative strike.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "Rural voter groups criticize the opposition's stance, arguing employee salaries consume too much tax.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Committee discussions stall as members fail to agree on the definition of base salary scales.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-06: Akali Dal factionalism SGPC
nk = f"{short_code}_2001_06_sgpc_factionalism"
news_items.append({
    "newsKey": nk, "month": "2001-06",
    "title": "Akali Factions Clash Over SGPC Committee Appointments (2001-06)",
    "description": "Rival groups within the Shiromani Akali Dal openly challenge CM Badal's control over SGPC appointments, accusing his faction of autocracy. The internal struggle creates a public debate over the independence of religious bodies.",
    "issueTags": ["politics", "identity"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "sgpc_factionalism",
        "SAD Chief Badal holds reconciliation meets with dissident leaders and reiterates the need for party unity.",
        "Opposition Congress leaders call the clash a proof that the Akali Dal uses religious bodies for political power.",
        "A joint convention of Sikh intellectuals is organized to discuss reforms in Gurdwara administrative appointments.",
        "The SGPC President declines to comment on the internal factional disputes to regional reporters.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"punjabIdentityMemory": 1}, {"punjabIdentityMemory": -1}, {"punjabIdentityMemory": -1},
        14, "Leaks from the reconciliation meeting fuel further factional speculation, drawing negative press.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The criticism is dismissed as political interference by orthodox voters, neutralizing its impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "The reform convention is boycotted by major factions, failing to reach any administrative consensus.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-07: Border area farmers BSF restrictions
nk = f"{short_code}_2001_07_border_restrictions"
news_items.append({
    "newsKey": nk, "month": "2001-07",
    "title": "Border Farmers Protest Against BSF Security Restrictions (2001-07)",
    "description": "Farmers with agricultural lands beyond the international border fence hold protests near Ferozepur, complaining of restricted entry hours and harassment during security checks by the BSF. The issue highlights the challenges of border farming.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "border_restrictions",
        "The state government petitions the Home Ministry to streamline gate pass timings and ease checks for farmers.",
        "Opposition leaders join the protests, demanding the state immediately pay compensation for land locked behind fences.",
        "A joint border liaison panel is formed to facilitate communication between BSF commanders and local village panchayats.",
        "The District Magistrate declines to comment on the security protocols established near the international border.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"punjabRuralTrustMemory": 1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        13, "Central clearance is delayed, leaving border gate timings unchanged during the sowing season.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The demands are criticized as ignoring national security imperatives, drawing mild media pushback.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Liaison panel meetings are postponed due to border security alerts in neighboring divisions.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-08: Ludhiana industrial waste Satluj
nk = f"{short_code}_2001_08_satluj_pollution"
news_items.append({
    "newsKey": nk, "month": "2001-08",
    "title": "High Court Directs Action Against Satluj River Polluters (2001-08)",
    "description": "The Punjab and Haryana High Court issues directives to shut down Ludhiana dye industries discharging untreated chemical waste into the Buddha Nullah, which flows into the Satluj river. The order triggers panic among industrial units.",
    "issueTags": ["infrastructure", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "satluj_pollution",
        "The state Pollution Control Board orders dye units to connect to common effluent treatment plants or face closure.",
        "Opposition leaders criticize the board, claiming the sudden closure threatens the livelihoods of thousands of factory workers.",
        "A joint committee of environment officials and industrial chambers is set up to negotiate compliance timelines.",
        "The Pollution Control Board spokesperson declines to publish the list of industrial units facing closure notices.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabStabilityMemory": -1}, {"punjabCorruptionMemory": 1}, {"punjabStabilityMemory": -1},
        14, "Enforcement delays trigger fresh complaints from environmental groups, leading to court warnings.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "Environmentalists criticize the opposition's stance, accusing them of shielding river polluters.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Effluent plant construction is delayed by disputes over municipal land acquisition in Ludhiana.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-09: Post 9/11 alert border
nk = f"{short_code}_2001_09_security_alert"
news_items.append({
    "newsKey": nk, "month": "2001-09",
    "title": "High Alert Imposed in Border Districts Post-9/11 (2001-09)",
    "description": "Following the September 11 attacks, the Ministry of Home Affairs directs Punjab to impose a high alert in districts bordering Pakistan. Security is beefed up around vital installations, creating local commercial disruptions.",
    "issueTags": ["security_crisis", "identity"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "security_alert",
        "The state police deploys additional security forces to border towns and establishes joint checkpoints with central units.",
        "Opposition Congress leaders demand that the state immediately release funds to support border tourism units hit by restrictions.",
        "A joint peace and security council is formed with representatives from all parties to maintain local confidence.",
        "The Home Department declines to comment on the specific deployment strength of the state police forces.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"punjabStabilityMemory": -1}, {"punjabIdentityMemory": 1}, {"punjabStabilityMemory": -1},
        15, "Security checks result in long traffic queues on border highways, drawing local merchant protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The demands are dismissed by border commanders who prioritize security over business interests.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Security restrictions prevent the joint council from touring high-priority border installations.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-10: Barnala faction criticism
nk = f"{short_code}_2001_10_barnala_dissent"
news_items.append({
    "newsKey": nk, "month": "2001-10",
    "title": "S.S. Barnala's Faction Steps Up Criticism of SAD Alliance (2001-10)",
    "description": "Dissent within the ruling Shiromani Akali Dal grows as supporters of Surjit Singh Barnala criticize the terms of the alliance with the BJP. The public criticism threatens coalition cohesion ahead of the assembly elections.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "barnala_dissent",
        "CM Badal holds coordination meetings with state BJP leaders to reaffirm coalition commitments.",
        "Congress opposition leaders state the coalition's internal rift shows they are unfit for another term.",
        "Senior leaders from SAD and BJP form a joint coordination committee to draft a common poll agenda.",
        "The SAD state spokesperson declines to comment on reports of seat-sharing disputes with the BJP.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"punjabStabilityMemory": -1}, {"punjabIdentityMemory": -1}, {"punjabStabilityMemory": -1},
        14, "Leaks from the coordination meeting fuel further media rumors, creating minor party confusion.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The criticism fails to resonate with voters who are more concerned about local developmental issues.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "The joint committee's deliberations are delayed by disagreements over Gurdaspur area seat sharing.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-11: Ranjit Sagar Dam rehabilitation
nk = f"{short_code}_2001_11_ranjit_sagar"
news_items.append({
    "newsKey": nk, "month": "2001-11",
    "title": "Rehabilitation Disputes Persist Over Ranjit Sagar Dam (2001-11)",
    "description": "Though the Ranjit Sagar Dam (Thein Dam) is operational, families displaced by the project hold demonstrations in Pathankot. The protestors demand the immediate release of promised government jobs and rehabilitation plots.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "land_rights"},
    "reactionOptions": create_reactions(
        nk, "ranjit_sagar",
        "The government directs the rehabilitation officer to release job letters to eligible displaced candidates.",
        "Opposition Congress leaders join the protests, demanding a judicial inquiry into land acquisition payouts.",
        "A joint committee of Pathankot MLAs is formed to verify pending claims and oversee resettlement allotments.",
        "The Irrigation Department declines to comment on the number of displaced families still awaiting rehabilitation.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -2},
        {"punjabRuralTrustMemory": 1}, {"punjabRuralTrustMemory": -1}, {"punjabStabilityMemory": -1},
        14, "Administrative bottlenecks delay the issuance of job letters, leading to continued protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The demands are labeled by the ruling party as politicizing completed infrastructure accomplishments.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The verification process is slowed down by missing revenue records in border villages.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2001-12: Operation Parakram border tension
nk = f"{short_code}_2001_12_border_mobilization"
news_items.append({
    "newsKey": nk, "month": "2001-12",
    "title": "Troop Mobilization on Border Triggers Local Panic (2001-12)",
    "description": "Following the Parliament attacks, massive deployment of Indian troops along the Punjab border (Operation Parakram) creates high tension. Residents in border villages start evacuating, and agricultural activities are restricted.",
    "issueTags": ["security_crisis", "rural"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "border_mobilization",
        "The state administration sets up emergency shelter centers in safer districts and coordinates civil defense drills.",
        "Congress opposition leaders demand that the state immediately release special cash relief for displaced border families.",
        "All-party representatives issue a joint resolution supporting national defense and calling for calm.",
        "The Home Department declines to comment on the security restrictions placed on border farming activities.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": -1, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"punjabStabilityMemory": -1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        16, "Inadequate facilities at the shelter centers spark protests by evacuated villagers near Amritsar.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The demand is criticized as creating panic during a national security crisis, drawing media criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over the shelter centers' management delay aid distribution in border talukas.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2001-12"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002
# 2002-01: Assembly election campaign
nk = f"{short_code}_2002_01_election_campaign"
news_items.append({
    "newsKey": nk, "month": "2002-01",
    "title": "Assembly Election Campaign Reaches Peak in Punjab (2002-01)",
    "description": "With polling scheduled for February, election campaigning reaches a peak across Punjab. The opposition Congress focuses on the state's rising debt, while the ruling Akali Dal campaigns on farm subsidies and free power.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "election_campaign",
        "The SAD government highlights its free power policy and showcases rural development schemes.",
        "The Congress launches a campaign focusing on fiscal health, administrative reforms, and transparency.",
        "Both parties agree to a joint campaign code of conduct to prevent clashes in sensitive constituencies.",
        "The state election coordinators decline to comment on internal party candidate selection disputes.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"punjabRuralTrustMemory": -1}, {"punjabStabilityMemory": 1}, {"punjabStabilityMemory": -1},
        13, "SAD's farm campaign fails to attract urban traders who are concerned about fiscal deficits.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "Factional squabbles in the Congress's Patiala unit delay campaign coordination in several blocks.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Minor code violations by local workers lead to warnings from the Election Commission.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-02: Election Congress victory Amarinder CM
nk = f"{short_code}_2002_02_congress_victory"
news_items.append({
    "newsKey": nk, "month": "2002-02",
    "title": "Congress Wins Punjab Polls; Amarinder Singh Sworn in as CM (2002-02)",
    "description": "The Indian National Congress wins a majority in the Punjab assembly elections. Captain Amarinder Singh is sworn in as the new Chief Minister of Punjab, promising to clean up administration and restore fiscal discipline.",
    "issueTags": ["politics", "governance"],
    "weights": {"baseSelectionWeight": 1.3, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "congress_victory",
        "Chief Minister Amarinder Singh promises an immediate crackdown on corruption and reviews state expenditures.",
        "The defeated SAD accepts the mandate, stating they will vigilantly protect rural interests as opposition.",
        "All parties agree to cooperate on a joint resolution demanding central packages for border districts.",
        "The outgoing CM Parkash Singh Badal's office declines to issue any public statements on the election results.",
        {"partyMorale": 4, "corruptionScore": 0, "mediaImage": 4, "publicSupport": 4},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 0, "mediaImage": -3, "publicSupport": -3},
        {"punjabStabilityMemory": -2}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        15, "Delays in cabinet allocation spark early murmurs among senior Congress MLAs.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "Internal SAD recriminations over urban candidate selection leak to the press, causing embarrassment.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over the assembly speaker selection mar the cooperative spirit of the first session.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-03: Bureaucracy reshuffle review
nk = f"{short_code}_2002_03_governance_review"
news_items.append({
    "newsKey": nk, "month": "2002-03",
    "title": "New CM Orders Reshuffle of Senior Bureaucracy (2002-03)",
    "description": "Chief Minister Amarinder Singh orders a major reshuffle of the state's senior administrative and police officers. The government reviews previous SAD-era financial commitments, alleging fiscal irregularities.",
    "issueTags": ["governance", "politics"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "governance_review",
        "The administration appoints new department heads and initiates audits of disputed tenders.",
        "Opposition SAD leaders criticize the reshuffle, calling it a political purge of neutral officers.",
        "A joint committee is formed to draft guidelines for institutional transfers and postings.",
        "The Chief Secretary's office declines to comment on the specific audit findings of the tenders.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabStabilityMemory": -1}, {"punjabStabilityMemory": 1}, {"punjabStabilityMemory": -1},
        13, "Administrative delays stall routine approvals during the cadre transition phase.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The criticism is ignored by the public who expect a change in administrative style.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Committee talks break down over terms of officer representation, failing to draft guidelines.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-04: PPSC scam Ravi Sidhu arrested
nk = f"{short_code}_2002_04_ppsc_scam"
news_items.append({
    "newsKey": nk, "month": "2002-04",
    "title": "PPSC Chairman Arrested in High-Profile Corruption Case (2002-04)",
    "description": "The Punjab Vigilance Bureau arrests PPSC Chairman Ravi Sidhu in connection with a massive recruitment scam. Cash worth crores is recovered from his locker, sending shockwaves through the state administration.",
    "issueTags": ["corruption", "governance"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "corruption"},
    "reactionOptions": create_reactions(
        nk, "ppsc_scam",
        "The CM orders a complete vigilance probe into all recruitments conducted during Sidhu's tenure.",
        "Opposition SAD leaders demand that the probe be monitored by a sitting High Court judge.",
        "A multi-party legislative subcommittee is formed to recommend reforms in the state public service recruitment process.",
        "The Vigilance Bureau spokesperson declines to comment on the list of candidates under investigation.",
        {"partyMorale": 3, "corruptionScore": -2, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabCorruptionMemory": -2}, {"punjabCorruptionMemory": 1}, {"punjabStabilityMemory": -1},
        15, "Vigilance actions are delayed by legal challenges in the High Court, drawing minor media criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "The demand is seen as a defense of the corruption accused, drawing public disapproval.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Subcommittee meetings stall due to non-cooperation by former commission members.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-05: Revocation of free power
nk = f"{short_code}_2002_05_power_tariff_revocation"
news_items.append({
    "newsKey": nk, "month": "2002-05",
    "title": "Government Revokes Free Power to Agriculture (2002-05)",
    "description": "Fulfilling a commitment to restore fiscal health, the Congress government revokes the policy of free power to tubewells, introducing a flat tariff for agricultural consumers. The decision triggers protests by farmer unions.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "power_tariff_revocation",
        "The government defends the tariff as necessary for quality power supply and promises targeted tubewell subsidies.",
        "SAD opposition leaders hold mass rallies, calling the decision a betrayal of Punjab's farmers.",
        "A joint committee is formed to negotiate the power tariff rates and draft crop credit packages.",
        "The Power Department declines to comment on the number of tubewell connections facing tariff enforcement.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"punjabRuralTrustMemory": -2}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        16, "Enforcement officers face violent resistance from farmer groups in Sangrur, drawing bad press.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The rallies block main rail routes, drawing protests from local merchant associations.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Tariff negotiation meetings stall as farmer representatives reject any tariff above zero.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-06: PPSC recruitments cancelled
nk = f"{short_code}_2002_06_recruitments_cancelled"
news_items.append({
    "newsKey": nk, "month": "2002-06",
    "title": "Government Cancels 639 PPSC Recruitments (2002-06)",
    "description": "Following the vigilance probe into the PPSC scam, the state government cancels 639 recruitments of civil service officers appointed during Sidhu's tenure. Affected candidates challenge the decision in court.",
    "issueTags": ["governance", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "recruitments_cancelled",
        "The Personnel Department defends the cancellation in court and announces plans for a clean re-examination.",
        "Opposition leaders claim the cancellation is too sweeping, punishing honest candidates along with the corrupt.",
        "A joint assembly committee is formed to review the candidate credentials and filter out tainted appointments.",
        "The Advocate General declines to comment on the state's legal strategy for the candidate petitions.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabCorruptionMemory": -1}, {"punjabCorruptionMemory": 1}, {"punjabStabilityMemory": -1},
        14, "The High Court stays the cancellation of some officers, drawing critical editorials on executive overreach.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "The opposition's support for the candidates is criticized as defending backdoor entrants.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The review process is delayed due to missing files in the PPSC secret section.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-07: Drought anxiety delay monsoon
nk = f"{short_code}_2002_07_drought_anxiety"
news_items.append({
    "newsKey": nk, "month": "2002-07",
    "title": "Monsoon Delays Spark Drought Anxiety in Rural Belts (2002-07)",
    "description": "A prolonged dry spell in July depletes reservoirs and threatens standing paddy crops in central Punjab. Farmers run tubewells on expensive diesel, raising agrarian distress amidst power supply restrictions.",
    "issueTags": ["rural", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "drought_anxiety",
        "The state releases emergency canal water releases and requests a central drought-relief package.",
        "SAD leaders demand immediate cash subsidies for diesel purchases to support crop irrigation.",
        "A joint legislative panel tours Patiala and Ludhiana districts to assess crop health and coordinate aid.",
        "The Irrigation Department declines to specify the daily canal water distribution schedule to border blocks.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"punjabRuralTrustMemory": -1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        15, "Delay in central drought aid release limits the state's capacity to subsidize diesel purchases.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The demands are criticized as fiscally unfeasible, softening their political advantage.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "The legislative panel's tours are disrupted by sudden localized showers in Patiala.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-08: Urban power cuts
nk = f"{short_code}_2002_08_urban_power_cuts"
news_items.append({
    "newsKey": nk, "month": "2002-08",
    "title": "Urban Areas Face Unscheduled Power Cuts (2002-08)",
    "description": "As the summer demand peaks, major cities in Punjab face unscheduled load shedding of up to 4 hours a day. Small-scale industrial units in Jalandhar and Ludhiana protest against the power supply cuts.",
    "issueTags": ["infrastructure", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "urban_power_cuts",
        "The Power Ministry purchases short-term power from external grids and schedules maintenance shutdowns.",
        "Opposition leaders stage dharnas outside power board offices, accusing the Congress government of infrastructure neglect.",
        "A joint committee of power board officials and industrial chambers is set up to negotiate supply slots.",
        "The Electricity Board declines to publish a daily schedule of the planned urban power cuts.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"punjabStabilityMemory": -1}, {"punjabStabilityMemory": 1}, {"punjabStabilityMemory": -1},
        14, "Expensive short-term power purchases increase the electricity board's deficit, drawing criticism.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "Protestors block local roads in Ludhiana, drawing complaints from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Disagreements over power tariffs for small-scale units stall the joint slot negotiations.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-09: Corruption case against former SAD ministers
nk = f"{short_code}_2002_09_sad_graft"
news_items.append({
    "newsKey": nk, "month": "2002-09",
    "title": "Vigilance Bureau Files Graft Cases Against Former SAD Ministers (2002-09)",
    "description": "The Punjab Vigilance Bureau registers cases of disproportionate assets and corruption against several former ministers of the SAD-BJP coalition. The opposition BJP calls the actions politically motivated vendetta.",
    "issueTags": ["corruption", "politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "corruption"},
    "reactionOptions": create_reactions(
        nk, "sad_graft",
        "The government defends the vigilance actions as a necessary clean-up of administration and promises due process.",
        "Opposition SAD leaders hold protests, demanding the immediate dissolution of the Vigilance Bureau.",
        "A multi-party legislative subcommittee is proposed to review vigilance investigation procedures.",
        "The Vigilance Bureau Director declines to release specific details of the seized assets to the press.",
        {"partyMorale": 3, "corruptionScore": -1, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabCorruptionMemory": -1}, {"punjabCorruptionMemory": 1}, {"punjabStabilityMemory": -1},
        15, "Delayed court proceedings allow the accused to secure anticipatory bail, weakening the media image.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The demands are criticized as defending corruption, drawing negative editorials in local press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Subcommittee talks break down due to partisan standoffs over political case definitions.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-10: Rice procurement moisture FCI
nk = f"{short_code}_2002_10_rice_procurement"
news_items.append({
    "newsKey": nk, "month": "2002-10",
    "title": "Rice Procurement Delayed Over Moisture Limit Disputes (2002-10)",
    "description": "Rice procurement in Punjab grain markets is delayed as the FCI refuses to buy grains with moisture content exceeding 17 percent. Farmers and millers protest, demanding relaxation of procurement specifications.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "rice_procurement",
        "The state government requests the Centre to temporarily relax moisture specifications for Punjab crop pools.",
        "SAD leaders lead dharnas at procurement offices, accusing the Congress government of failing to protect farmers.",
        "A joint state-FCI-farmer coordination panel is formed to check moisture levels at major mandis.",
        "The Food Department declines to provide a timeline for the resumption of crop procurement at grain markets.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"punjabRuralTrustMemory": -1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        14, "The Centre rejects the request, leaving the state to handle mounting grain market backlogs.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "Some dharnas turn violent, resulting in police action and damage to procurement records.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Moisture testing equipment calibration disputes stall the coordination panel's field checks.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-11: SGPC executive elections Badal wins
nk = f"{short_code}_2002_11_sgpc_elections"
news_items.append({
    "newsKey": nk, "month": "2002-11",
    "title": "Badal's Faction Retains Control of SGPC Executive (2002-11)",
    "description": "In a high-stakes contest, Parkash Singh Badal's faction retains control of the SGPC executive, defeating the state government-backed candidates. The result represents a major political setback for the Congress administration.",
    "issueTags": ["politics", "identity"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "sgpc_elections",
        "The CM states the government respects the SGPC mandate and denies any official role in religious contests.",
        "Opposition SAD leaders hail the result as a victory for Sikh autonomy and defeat of Congress interference.",
        "All parties agree to pass a assembly resolution supporting the preservation of historical Sikh shrines.",
        "The State Congress office declines to comment on the defeat of the candidates they supported.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"punjabIdentityMemory": -1}, {"punjabIdentityMemory": 1}, {"punjabIdentityMemory": -1},
        14, "Leaks showing state government resources were used in the campaign draw negative editorials.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        12, "The statements provoke minor scuffles between party workers during victory rallies, drawing bad press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Disagreements over the resolution wording delay its passage in the assembly.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2002-12: Sugarcane SAP rail roko
nk = f"{short_code}_2002_12_sugarcane_strike"
news_items.append({
    "newsKey": nk, "month": "2002-12",
    "title": "Farmers Launch 'Rail Roko' Protesting Sugarcane Prices (2002-12)",
    "description": "Sugarcane growers in Punjab block railway tracks in Jalandhar and Phagwara, protesting the state government's decision to freeze the State Agreed Price (SAP). The strike disrupts long-distance train services, causing public anger.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "sugarcane_strike",
        "The Agriculture Minister initiates talks with farmer unions and announces a minor bonus payment per quintal.",
        "Opposition SAD leaders join the rail blockade, demanding the immediate clearing of sugar mill dues.",
        "A joint state-miller-farmer committee is formed to negotiate the sugarcane SAP for the next season.",
        "The administration deploys police forces to clear the tracks under the Railway Act, refusing negotiations.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"punjabRuralTrustMemory": -1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        15, "Private sugar mill owners refuse to cover the bonus payouts, stalling the strike settlement.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        13, "The blockade causes cargo delays, drawing strong protests from local merchant associations.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Committee talks break down as millers report major export losses due to pricing regulations.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2002-12"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003
# 2003-01: Agricultural diversification mission
nk = f"{short_code}_2003_01_diversification_mission"
news_items.append({
    "newsKey": nk, "month": "2003-01",
    "title": "Government Launches Agricultural Diversification Mission (2003-01)",
    "description": "To address declining groundwater tables, the Punjab government launches a diversification mission, offering subsidies to farmers who shift from water-intensive paddy to oilseeds, maize, and pulses. Agro-experts welcome the initiative.",
    "issueTags": ["rural", "governance"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "diversification_mission",
        "The Agriculture Department establishes model diversification farms and releases seed subsidies to gram panchayats.",
        "BJP and SAD opposition leaders claim the crop subsidies are too low to offset the secure MSP of rice and wheat.",
        "A joint assembly panel is set up to study crop pricing dynamics and propose central MSP allocations.",
        "The Directorate of Agriculture declines to publish the target acreage for crop diversification this season.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabRuralTrustMemory": -1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        13, "Supply chain shortages in hybrid maize seeds delay sowing in several southern blocks.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The criticism is rejected by farm experts who support groundwater protection programs.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "The assembly panel's recommendations are delayed due to missing agriculture department reports.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-02: Akali Dal vendetta rally
nk = f"{short_code}_2003_02_vendetta_protests"
news_items.append({
    "newsKey": nk, "month": "2003-02",
    "title": "Akali Dal Holds Mass Rallies Protesting 'Political Vendetta' (2003-02)",
    "description": "Shiromani Akali Dal leaders organize massive rallies in Patiala, accusing the Congress government of using the Vigilance Bureau to wage a campaign of political vendetta against opposition ministers. The protest draws high rural participation.",
    "issueTags": ["politics", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "vendetta_protests",
        "The government defends the vigilance actions as a necessary clean-up of administration and promises due process.",
        "SAD Chief Badal leads the rallies, demanding the immediate dismissal of vigilance officers.",
        "A joint committee is formed to negotiate code of conduct guidelines for administrative investigation agencies.",
        "The CM's spokesperson declines to comment on the scale of the Patiala protest rallies.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"punjabStabilityMemory": -1}, {"punjabCorruptionMemory": 1}, {"punjabStabilityMemory": -1},
        14, "Leaks from the vigilance bureau fuel further media rumors, creating minor party confusion.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "Minor clashes between party workers break out on polling day, drawing negative press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "The coordination panel's work is stalled by non-participation of senior opposition leaders.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-03: Vigilance files chargesheet against Badal
nk = f"{short_code}_2003_03_badal_chargesheet"
news_items.append({
    "newsKey": nk, "month": "2003-03",
    "title": "Vigilance Bureau Files Corruption Chargesheet Against Badal (2003-03)",
    "description": "The Punjab Vigilance Bureau files a formal corruption and disproportionate assets chargesheet against former CM Parkash Singh Badal. The chargesheet alleges accumulation of assets worth crores through illegal means.",
    "issueTags": ["corruption", "politics"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "corruption"},
    "reactionOptions": create_reactions(
        nk, "badal_chargesheet",
        "The prosecution requests the court to fast-track the trial and opposes any regular bail for the accused.",
        "SAD leaders accuse the government of fabricating evidence and stage protests outside the court premises.",
        "Both parties agree to limit political statements regarding the court case to maintain judicial independence.",
        "The Vigilance Director declines to comment on the timeline of the judicial trial to reporters.",
        {"partyMorale": 3, "corruptionScore": -1, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabCorruptionMemory": -1}, {"punjabCorruptionMemory": 1}, {"punjabStabilityMemory": -1},
        15, "The court grants bail to Badal, which is presented by the opposition as a major moral victory.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        13, "The court protests lead to minor traffic blocks near the court, drawing complaints from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "The political truce is violated within days by local party workers, drawing minor fines.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-04: Wheat procurement smooth
nk = f"{short_code}_2003_04_wheat_harvest"
news_items.append({
    "newsKey": nk, "month": "2003-04",
    "title": "Smooth Wheat Procurement Eases Rural Economic Anxiety (2003-04)",
    "description": "State procurement agencies report a smooth start to the spring wheat procurement season, with quick payments made to farmers. The efficient crop lifting provides immediate relief to the rural economy.",
    "issueTags": ["rural", "governance"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "wheat_harvest",
        "The Food Department releases special funds to ensure farmer payments are credited within 48 hours.",
        "SAD leaders state that the smooth procurement is due to the infrastructure built by the previous government.",
        "A joint committee is formed to study crop pricing dynamics and propose central MSP allocations.",
        "The Food Commissioner declines to release the daily grain lifting statistics to regional newspapers.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabRuralTrustMemory": 1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        12, "Minor delays in grain bag supply in border districts draw localized farmer complaints.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The opposition claims are dismissed by neutral observers who credit the current administration.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Disagreements over the committee's scope delay the study of long-term crop pricing.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-05: Municipal elections
nk = f"{short_code}_2003_05_municipal_polls"
news_items.append({
    "newsKey": nk, "month": "2003-05",
    "title": "Congress Wins Majority in Municipal Corporation Elections (2003-05)",
    "description": "The ruling Congress wins a majority of seats in the municipal corporation elections held in Patiala and Jalandhar. However, the opposition SAD-BJP coalition makes significant gains in smaller rural towns.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "municipal_polls",
        "The Congress welcomes the urban mandates and promises to accelerate municipal development funding.",
        "SAD leaders claim their rural gains show growing public dissatisfaction with Congress policies.",
        "Both parties agree to cooperate on municipal reforms to improve local body finances.",
        "The State Election Commissioner declines to comment on requests to review voting counts in disputed wards.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"punjabStabilityMemory": -1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        13, "Disputes over ward project allocations stall municipal council meetings in Jalandhar.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The SAD claims are labeled as exaggerated by political observers, limiting their public impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Disagreements over the tax sharing formula stall the municipal finance reforms.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-06: Raids on Badal family properties
nk = f"{short_code}_2003_06_badal_raids"
news_items.append({
    "newsKey": nk, "month": "2003-06",
    "title": "Vigilance Bureau Raids Badal Family Properties in Muktsar (2003-06)",
    "description": "The Punjab Vigilance Bureau conducts high-profile raids on the residences of former CM Parkash Singh Badal and his family in Muktsar district. The raids trigger intense political sparring between Congress and SAD.",
    "issueTags": ["corruption", "politics"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "badal_raids",
        "The government defends the raids as a necessary step to uncover illegally acquired assets and promises due process.",
        "SAD leaders hold protests near the raided sites, calling the action a crude attempt to intimidate the opposition.",
        "All parties agree to keep political worker protests peaceful to prevent law and order breakdowns.",
        "The Vigilance Director declines to comment on the specific list of documents and assets seized during the raids.",
        {"partyMorale": 3, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabCorruptionMemory": -1}, {"punjabCorruptionMemory": 1}, {"punjabStabilityMemory": -1},
        15, "Leaks of raid details to the press spark accusations of a media trial, drawing court warnings.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -1},
        12, "The protests lead to minor traffic blockades in Muktsar, drawing complaints from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Minor clashes between party workers break out on polling day, drawing negative press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-07: Cotton whitefly Malwa
nk = f"{short_code}_2003_07_cotton_pest"
news_items.append({
    "newsKey": nk, "month": "2003-07",
    "title": "Whitefly Attack Reported in Malwa Cotton Belt (2003-07)",
    "description": "Cotton farmers in Ferozepur and Muktsar districts report early signs of whitefly attack on their crops. The agriculture department deploys monitoring teams to check the spread and advise on pesticide usage.",
    "issueTags": ["rural", "governance"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "cotton_pest",
        "The Agriculture Department provides subsidized pesticides and organizes farmers' training camps.",
        "Opposition SAD leaders claim the government's response is too slow and demand cash compensation for crop losses.",
        "A joint state-agriculture university task force is formed to monitor pesticide quality and distribution.",
        "The Director of Agriculture declines to estimate the total cotton acreage affected by the whitefly attack.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"punjabRuralTrustMemory": 1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        14, "Pesticide distribution delays in remote blocks spark minor complaints from local councils.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The opposition's demands are labeled as fiscally irresponsible during a revenue deficit.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Task force meetings are delayed by the non-participation of transport union representatives.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-08: Ghaggar river floods
nk = f"{short_code}_2003_08_ghaggar_floods"
news_items.append({
    "newsKey": nk, "month": "2003-08",
    "title": "Monsoon Floods Displace Families in Ghaggar Basin (2003-08)",
    "description": "Heavy rains cause the Ghaggar river to overflow, inundating agricultural land and displacing families in Patiala and Sangrur districts. The administration coordinates rescue operations and relief distribution.",
    "issueTags": ["rural", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "ghaggar_floods",
        "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations.",
        "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages.",
        "A joint legislative relief committee is established to supervise rehabilitation work in Patiala division.",
        "The District Collector declines to release the official crop loss estimates in the first week.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"punjabStabilityMemory": -1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        14, "Logistical failures delay the delivery of tents to remote villages, drawing local protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        12, "The criticism leads to minor scuffles at distribution centers, disrupting relief work.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over relief beneficiary lists stall aid distribution in several affected talukas.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-09: Congress internal rebellion Bhattal
nk = f"{short_code}_2003_09_congress_dissidents"
news_items.append({
    "newsKey": nk, "month": "2003-09",
    "title": "Congress Dissidents Demand CM Replacement (2003-09)",
    "description": "Internal friction peaks in the ruling Congress party as a faction of MLAs led by Rajinder Kaur Bhattal demands the replacement of CM Amarinder Singh. The dissidents travel to Delhi to consult with the party high command.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "congress_dissidents",
        "CM Amarinder Singh meets central leaders in New Delhi and seeks intervention to maintain state party discipline.",
        "Opposition SAD leaders state the internal Congress rift shows the government is too divided to govern.",
        "State Congress leaders hold a closed-door meeting to address concerns and project a united front.",
        "The Congress state spokesperson declines to comment on the reports of factional disputes.",
        {"partyMorale": 1, "corruptionScore": 0, "mediaImage": 1, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"punjabStabilityMemory": -1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        14, "Leaks from the Delhi meeting fuel further media speculation about leadership changes.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The criticism is ignored by voters who view it as standard opposition exploitation of internal issues.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Several key legislators skip the unity meeting, diluting its positive impact in the press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-10: Agro processing single window
nk = f"{short_code}_2003_10_agro_investment"
news_items.append({
    "newsKey": nk, "month": "2003-10",
    "title": "Single-Window System Launched for Agro-Processing Units (2003-10)",
    "description": "To boost private investment in agriculture, the government launches a single-window system for agro-processing projects. The policy offers fast-track land allotments and tax concessions for food processing hubs.",
    "issueTags": ["infrastructure", "economy"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "agro_investment",
        "The Industry Department establishes a single-window clearance cell to process investment applications rapidly.",
        "Opposition leaders claim the policy favors large corporate houses at the expense of local small-scale industries.",
        "A joint government-industry coordination committee is formed to monitor infrastructure upgrades in the hubs.",
        "The Industry Minister declines to share the estimated revenue loss due to the new tax concessions.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabStabilityMemory": -1}, {"punjabCorruptionMemory": 1}, {"punjabStabilityMemory": -1},
        13, "Administrative delays stall the single-window clearance cell, drawing criticism from investors.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "Small-scale industry unions distance themselves from the opposition's protests, weakening the criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Coordination meetings are delayed by disagreements over municipal tax sharing inside the zone.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-11: Sukhbir Badal arrested
nk = f"{short_code}_2003_11_sukhbir_arrest"
news_items.append({
    "newsKey": nk, "month": "2003-11",
    "title": "Sukhbir Singh Badal Arrested in Vigilance Probe (2003-11)",
    "description": "The Punjab Vigilance Bureau arrests senior SAD leader Sukhbir Singh Badal in connection with the ongoing disproportionate assets case. SAD workers hold demonstrations across the state, protesting the arrest.",
    "issueTags": ["corruption", "politics"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "sukhbir_arrest",
        "The government defends the arrest as a legal step and warns against any attempts to disrupt public order.",
        "SAD leaders hold protests near the vigilance office, calling the arrest a politically motivated vendetta.",
        "All parties agree to keep political worker protests peaceful to prevent law and order breakdowns.",
        "The Vigilance Director declines to comment on the specific list of documents and assets seized during the arrest.",
        {"partyMorale": 3, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabCorruptionMemory": -1}, {"punjabCorruptionMemory": 1}, {"punjabStabilityMemory": -1},
        15, "Leaks of arrest details to the press spark accusations of a media trial, drawing court warnings.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -1},
        12, "The protests lead to minor traffic blockades in Patiala, drawing complaints from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Minor clashes between party workers break out on polling day, drawing negative press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2003-12: Congress truce Bhattal Deputy CM package
nk = f"{short_code}_2003_12_congress_truce"
news_items.append({
    "newsKey": nk, "month": "2003-12",
    "title": "Congress High Command Proposes Truce in Punjab Unit (2003-12)",
    "description": "To resolve the internal leadership crisis, the Congress central high command proposes a power-sharing arrangement in Punjab. Dissident leader Rajinder Kaur Bhattal is tipped to be appointed Deputy CM.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "congress_truce",
        "CM Amarinder Singh welcomes the high command's guidance and coordinates with Bhattal to plan the cabinet restructuring.",
        "Opposition SAD leaders claim the power-sharing show proves the Congress cares more about portfolios than governance.",
        "State Congress leaders issue a joint statement expressing full faith in the central high command and promising unity.",
        "The CM's office declines to comment on reports of specific portfolio reallocations under the truce.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"punjabStabilityMemory": -1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        14, "Leaks from the consultations fuel further media rumors, creating minor administrative delays.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        11, "The allegations are dismissed as political posturing, failing to gather wider public attention.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "The unity statement is delayed due to disagreements over the wording of state leadership support.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2003-12"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004
# 2004-01: Bhattal Deputy CM
nk = f"{short_code}_2004_01_bhattal_deputy_cm"
news_items.append({
    "newsKey": nk, "month": "2004-01",
    "title": "Rajinder Kaur Bhattal Sworn in as Deputy CM (2004-01)",
    "description": "Rajinder Kaur Bhattal is formally sworn in as the Deputy Chief Minister of Punjab, in line with the high command's truce formula. The appointment aims to end months of factionalism within the ruling party.",
    "issueTags": ["politics", "governance"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "bhattal_deputy_cm",
        "The CM allocates key portfolios to Bhattal and announces a coordinated focus on state welfare schemes.",
        "Opposition SAD leaders call the appointment a compromise that yields two power centers in government.",
        "All parties pass an assembly resolution welcoming the Deputy CM and promising cooperative work.",
        "The Governor's office declines to share the protocol details of the cabinet swearing-in ceremony.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"punjabStabilityMemory": -1}, {"punjabStabilityMemory": 1}, {"punjabStabilityMemory": -1},
        14, "Leaks from the Delhi meeting fuel further media speculation about leadership changes.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The criticism is ignored by voters who view it as standard opposition exploitation of internal issues.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Several key legislators skip the unity meeting, diluting its positive impact in the press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-02: Tax rationalization Ludhiana
nk = f"{short_code}_2004_02_tax_rationalization"
news_items.append({
    "newsKey": nk, "month": "2004-02",
    "title": "Government Announces Tax Relief for Ludhiana Industries (2004-02)",
    "description": "The state government announces a rationalization of local taxes and power tariffs for hosiery and bicycle manufacturing units in Ludhiana. The policy aims to support local industrial growth.",
    "issueTags": ["infrastructure", "economy"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "tax_rationalization",
        "The Finance Department implements tax adjustments and establishes a single-window system for industrial units.",
        "Opposition leaders claim the policy favors large corporate houses at the expense of local small-scale units.",
        "A joint government-industry coordination committee is formed to monitor infrastructure upgrades in the hubs.",
        "The Industry Minister declines to share the estimated revenue loss due to the new tax concessions.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabStabilityMemory": -1}, {"punjabCorruptionMemory": 1}, {"punjabStabilityMemory": -1},
        13, "Administrative delays stall the single-window clearance cell, drawing criticism from investors.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "Small-scale industry unions distance themselves from the opposition's protests, weakening the criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Coordination meetings are delayed by disagreements over municipal tax sharing inside the zone.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-03: Lok Sabha campaign Gwalior Gwalior? No, Punjab!
nk = f"{short_code}_2004_03_loksabha_campaign"
news_items.append({
    "newsKey": nk, "month": "2004-03",
    "title": "Lok Sabha Campaign Intensifies Across Punjab (2004-03)",
    "description": "Campaigning for the 2004 general elections picks up pace in Punjab. The opposition SAD-BJP alliance targets the Congress government's performance, while the Congress focuses on national stability themes.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "loksabha_campaign",
        "The Congress campaigns on its anti-corruption record and fiscal rationalization achievements.",
        "SAD-BJP units launch coordinated campaign rallies in major cities, showcasing Badal's leadership.",
        "Both parties agree to limit loudspeaker usage during late hours to avoid disturbing students during exams.",
        "The state election coordinators decline to comment on reports of internal candidate disputes.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"punjabStabilityMemory": -1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        13, "Internal Congress factional squabbles over campaign allocations undermine their block meetings.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "Logistical coordination failures delay the SAD campaigns, drawing mild local criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        8, "A minor code violation by a local worker leads to a warning from the Election Commission.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-04: Polling Lok Sabha Punjab
nk = f"{short_code}_2004_04_loksabha_polls"
news_items.append({
    "newsKey": nk, "month": "2004-04",
    "title": "Voting Held for Lok Sabha Seats in Punjab (2004-04)",
    "description": "Polling is held across Punjab's 13 Lok Sabha constituencies. Security is tight, particularly in the border areas, to ensure peaceful voting under the supervision of central observers.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "loksabha_polls",
        "The state administration coordinates logistics and deploys home guards to assist central security forces.",
        "Opposition parties watch voting closely, raising concerns over alleged local administration bias in rural booths.",
        "All parties issue a joint statement appreciating the peaceful conduct of elections in border zones.",
        "The State Election Commissioner declines to comment on the final voter turnout figures in the first day.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"punjabStabilityMemory": -1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        13, "Voting delays due to EVM malfunctions in some booths draw local complaints and press criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The allegations are dismissed by independent observers, neutralizing the opposition's claims.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        8, "Minor disputes over election duty staff accommodation are reported in border blocks.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-05: Amarinder Singh rejects resignation calls
nk = f"{short_code}_2004_05_resignation_demands"
news_items.append({
    "newsKey": nk, "month": "2004-05",
    "title": "CM Rejects Resignation Demands After Lok Sabha Results (2004-05)",
    "description": "Following poor Congress results in Punjab's Lok Sabha seats (SAD-BJP won majority), CM Amarinder Singh rejects resignation calls from the opposition. He states his government retains a full mandate in the assembly.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "resignation_demands",
        "The CM holds cabinet meetings to review the results and announces plans to accelerate developmental projects.",
        "Opposition SAD leaders stage protests, claiming the general election results represent a rejection of the government.",
        "All parties agree to keep legislative debates focused on the state's upcoming annual budget.",
        "The Congress state office declines to comment on reports of leadership reviews by the high command.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"punjabStabilityMemory": -1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        14, "Leaks from the cabinet review spark minor factional speculation, drawing critical editorials.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The protests are labeled by the ruling party as creating political instability, limiting their impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Budget sessions are delayed by a day due to heated bickering over seat arrangements.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-06: SYL canal Supreme Court directive
nk = f"{short_code}_2004_06_syl_canal"
news_items.append({
    "newsKey": nk, "month": "2004-06",
    "title": "Supreme Court Directs Punjab to Construct SYL Canal (2004-06)",
    "description": "The Supreme Court of India directs the Punjab government to complete the construction of the Sutlej-Yamuna Link (SYL) canal and hand over the work to a central agency. The order provokes intense political anxiety in the state.",
    "issueTags": ["rural", "protest"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "land_rights"},
    "reactionOptions": create_reactions(
        nk, "syl_canal",
        "The state government seeks legal options to file a review petition and calls for an all-party consensus meet.",
        "Opposition SAD leaders demand that the state completely refuse to construct the canal to protect its water rights.",
        "All parties agree to pass a joint legislative resolution stating Punjab has no surplus water to share.",
        "The Irrigation Department spokesperson declines to comment on the court's timeline for the canal work.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": -1, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"punjabRuralTrustMemory": -1}, {"punjabIdentityMemory": 1}, {"punjabStabilityMemory": -1},
        15, "The review petition is dismissed, leaving the state administration facing immediate court deadlines.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "The opposition's demands provoke a strong backlash from neighboring Haryana, drawing national media focus.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over the resolution wording delay its introduction in the assembly by several days.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-07: Punjab Termination of Agreements Act
nk = f"{short_code}_2004_07_water_act"
news_items.append({
    "newsKey": nk, "month": "2004-07",
    "title": "Assembly Passes Punjab Termination of Agreements Act (2004-07)",
    "description": "In a bold move, the Punjab Assembly unanimously passes the Termination of Agreements Act, cancelling all water-sharing pacts with Haryana and Rajasthan. The act triggers a major federal conflict with the Centre.",
    "issueTags": ["politics", "identity"],
    "weights": {"baseSelectionWeight": 1.3, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "water_act",
        "The state government defends the act as a constitutional right to protect the state's agrarian future.",
        "Opposition leaders welcome the act but demand that the government prepare for potential central sanctions.",
        "All parties agree to form a joint delegation to meet the Prime Minister and explain Punjab's water position.",
        "The CM's office declines to comment on reports of the Governor's delay in signing the bill.",
        {"partyMorale": 4, "corruptionScore": 0, "mediaImage": 4, "publicSupport": 4},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 3, "corruptionScore": -1, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": -3, "corruptionScore": 0, "mediaImage": -3, "publicSupport": -3},
        {"punjabRuralTrustMemory": 2}, {"punjabIdentityMemory": 1}, {"punjabStabilityMemory": -1},
        16, "The Centre refers the act to the Supreme Court, creating a long-drawn legal dispute for the state.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        14, "The support leads to counter-protests in Haryana, disrupting highway traffic into Punjab.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over the delegation composition delay the meeting with the Prime Minister.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-08: Cotton bumper crop Malwa
nk = f"{short_code}_2004_08_cotton_bumper"
news_items.append({
    "newsKey": nk, "month": "2004-08",
    "title": "Bumper Cotton Crop Recorded in Malwa Region (2004-08)",
    "description": "Cotton growers in the Malwa belt report record yields this season, attributing it to good weather and effective pest management. The agricultural success brings immediate economic relief to rural households.",
    "issueTags": ["rural", "economy"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "cotton_bumper",
        "The Agriculture Department releases additional storage space and promises smooth marketing support.",
        "SAD leaders state that the bumper yield is due to the seed policies introduced by the previous administration.",
        "A joint assembly panel is established to study market pricing dynamics and propose central MSP allocations.",
        "The Agriculture Commissioner declines to release the official crop yield estimates to the press.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabRuralTrustMemory": 1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        12, "Minor delays in grain bag supply in border districts draw localized farmer complaints.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The opposition claims are dismissed by neutral observers who credit the current administration.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Disagreements over the committee's scope delay the study of long-term crop pricing.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-09: SGPC elections Badal wins again
nk = f"{short_code}_2004_09_sgpc_mandate"
news_items.append({
    "newsKey": nk, "month": "2004-09",
    "title": "Badal's Faction Wins Landslide in SGPC General Elections (2004-09)",
    "description": "In the general elections for the SGPC, Parkash Singh Badal's faction wins a landslide victory, securing a massive majority of the executive seats. The victory cements Badal's position as the primary representative of Sikh interests.",
    "issueTags": ["politics", "identity"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "sgpc_mandate",
        "The CM states the government respects the SGPC mandate and denies any official role in religious contests.",
        "Opposition SAD leaders hail the result as a victory for Sikh autonomy and defeat of Congress interference.",
        "All parties agree to pass an assembly resolution supporting the preservation of historical Sikh shrines.",
        "The State Congress office declines to comment on the defeat of the candidates they supported.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"punjabIdentityMemory": -1}, {"punjabIdentityMemory": 1}, {"punjabIdentityMemory": -1},
        14, "Leaks showing state government resources were used in the campaign draw negative editorials.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        12, "The statements provoke minor scuffles between party workers during victory rallies, drawing bad press.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Disagreements over the resolution wording delay its passage in the assembly.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-10: Paddy procurement payments
nk = f"{short_code}_2004_10_paddy_payments"
news_items.append({
    "newsKey": nk, "month": "2004-10",
    "title": "Government Assures Paddy Payments Within 72 Hours (2004-10)",
    "description": "As the autumn paddy harvesting begins, the state government announces a new payment system, promising to credit crop procurement payments to farmers within 72 hours of crop lifting. The policy aims to reduce middleman delays.",
    "issueTags": ["rural", "governance"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "paddy_payments",
        "The Food and Civil Supplies Department monitors the payments through digital bank accounts.",
        "Opposition SAD leaders claim the 72-hour promise is ignored at local mandis where payments remain delayed.",
        "A joint committee is formed to study crop pricing dynamics and propose central MSP allocations.",
        "The Food Department declines to release the daily payment figures for border district markets.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabRuralTrustMemory": 1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        13, "Bank delays leave many farmers without payments after a week, drawing local protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        11, "The criticism is ignored by farmers who welcome the new digital billing, limiting its impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Disagreements over the committee's scope delay the study of long-term crop pricing.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-11: PM Manmohan Singh visit
nk = f"{short_code}_2004_11_pm_visit"
news_items.append({
    "newsKey": nk, "month": "2004-11",
    "title": "PM Manmohan Singh Announces Border Development Package (2004-11)",
    "description": "During his visit to Amritsar, Prime Minister Manmohan Singh announces a special central package for the development of border districts in Punjab. The package funds road networks and border area schools, boosting local sentiment.",
    "issueTags": ["politics", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "pm_visit",
        "The state government coordinates the project planning and sets up local implementation cells.",
        "Opposition SAD leaders claim the package is underfunded and demand a complete waiver of central loans instead.",
        "A joint committee of border MLAs is formed to monitor the execution of the central package.",
        "The state planning board declines to share the estimated state share of funding for the package.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabStabilityMemory": -1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        13, "Administrative delays stall the local implementation cells, drawing criticism from border councils.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The criticism is dismissed by industry bodies who support the border infrastructure expansion.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Coordination meetings are delayed by disagreements over municipal tax sharing inside the zone.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2004-12: Rice millers strike custom rates
nk = f"{short_code}_2004_12_millers_strike"
news_items.append({
    "newsKey": nk, "month": "2004-12",
    "title": "Rice Millers Launch Strike Over Custom Milling Rates (2004-12)",
    "description": "Rice millers in Punjab go on strike, refusing to process custom milled rice for the central pool. The millers demand an increase in milling charges to offset rising labor and power costs, delaying crop movement.",
    "issueTags": ["protest", "economy"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "millers_strike",
        "The Food Department initiates talks with miller associations and offers a minor increase in milling charges.",
        "Opposition leaders support the millers, demanding that the state cover their operational deficits.",
        "A joint government-miller coordination committee is formed to negotiate the custom milling rates.",
        "The Food commissioner declines to release figures on the volume of rice currently stored in mill yards.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"punjabStabilityMemory": -1}, {"punjabCorruptionMemory": 1}, {"punjabStabilityMemory": -1},
        14, "Private sugar mill owners refuse to cover the payouts, stalling the strike settlement.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The demands are criticized by agricultural unions who argue public money should prioritize farm relief.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Committee discussions stall as employee unions reject the proposed phased payment schedule.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2004-12"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005
# 2005-01: VAT implementation announcement
nk = f"{short_code}_2005_01_vat_announcement"
news_items.append({
    "newsKey": nk, "month": "2005-01",
    "title": "Government Announces VAT Implementation Starting April (2005-01)",
    "description": "The Punjab government announces that Value Added Tax (VAT) will be implemented from April 1, replacing the old sales tax system. Local trader associations oppose the decision, warning of business closures.",
    "issueTags": ["economy", "politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "vat_announcement",
        "The Excise Department conducts training workshops for traders and promises a simplified filing process.",
        "Opposition leaders support the traders, demanding a postponement of VAT until system readiness is achieved.",
        "A joint legislative-trader coordination panel is formed to review tax slabs and address grievances.",
        "The Finance Minister declines to comment on the projected revenue impact of the new VAT system.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabStabilityMemory": -1}, {"punjabCorruptionMemory": 1}, {"punjabStabilityMemory": -1},
        14, "Training workshops report low attendance, leaving many traders confused about the new system.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        12, "The opposition's demands are dismissed by economists who support modernizing the tax system.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Committee discussions stall as members fail to agree on the definition of tax slabs.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-01"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-02: Police cross-border drug crackdown
nk = f"{short_code}_2005_02_drug_crackdown"
news_items.append({
    "newsKey": nk, "month": "2005-02",
    "title": "Police Crack Down on Border Drug Smuggling Networks (2005-02)",
    "description": "Punjab Police launch a coordinated crackdown on cross-border drug smuggling networks in Amritsar and Ferozepur districts. Several high-profile arrests are made, drawing attention to border security gaps.",
    "issueTags": ["security_crisis", "governance"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "drug_crackdown",
        "The state police deploys additional checkpoints and coordinates vigilance checks with border security units.",
        "Opposition leaders demand that the state immediately release funds to support rehabilitation centers.",
        "A joint legislative-police panel is formed to monitor border area security and rehabilitation progress.",
        "The Home Department declines to comment on the specific details of the ongoing investigations.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"punjabStabilityMemory": -1}, {"punjabIdentityMemory": 1}, {"punjabStabilityMemory": -1},
        14, "Leaks from the investigations fuel media speculation, drawing minor party confusion.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -1},
        12, "The demands are criticized as ignoring national security imperatives, drawing mild media pushback.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        9, "Liaison panel meetings are postponed due to border security alerts in neighboring divisions.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-02"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-03: Budget session opposition walkout debt
nk = f"{short_code}_2005_03_budget_session"
news_items.append({
    "newsKey": nk, "month": "2005-03",
    "title": "Opposition Stages Assembly Walkout Over State Debt (2005-03)",
    "description": "During the assembly's budget session, opposition SAD-BJP MLAs stage a walkout, protesting against the government's rising public debt and high power tariffs. The walkout draws attention to the state's fiscal health.",
    "issueTags": ["politics", "economy"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "budget_session",
        "The Finance Minister announces a fiscal rationalization plan and requests additional special grants from the Centre.",
        "SAD leaders demand a white paper on the state's debt status and criticize the government's tax policies.",
        "A joint legislative committee is formed to identify potential new revenue sources and non-tax avenues.",
        "The state treasury declines to release the monthly details of public debt accumulation to the media.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 1},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabStabilityMemory": -1}, {"punjabCorruptionMemory": 1}, {"punjabStabilityMemory": -1},
        14, "New tax proposals draw protests from local trader associations in Amritsar and Ludhiana.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        11, "The demand is dismissed as politically motivated, failing to gather support from industrial bodies.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "The revenue committee's report is delayed due to partisan gridlock over tax proposals.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-03"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-04: VAT implementation trader strike
nk = f"{short_code}_2005_04_vat_strike"
news_items.append({
    "newsKey": nk, "month": "2005-04",
    "title": "VAT Implementation Triggers Traders' Strike (2005-04)",
    "description": "Value Added Tax (VAT) goes into effect on April 1, triggering a statewide strike by trader associations. Shops and commercial establishments remain shut in Amritsar, Ludhiana, and Jalandhar, disrupting business.",
    "issueTags": ["protest", "economy"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "vat_strike",
        "The CM initiates negotiations with trader leaders and offers a phased implementation of VAT filing rules.",
        "Opposition leaders support the traders, demanding a complete rollback of the VAT system.",
        "A joint government-trader advisory panel is formed to review specific tax slabs and address issues.",
        "The Excise Department declines to comment on the number of businesses currently complying with VAT registration.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"punjabStabilityMemory": -1}, {"punjabCorruptionMemory": 1}, {"punjabStabilityMemory": -1},
        14, "The phased rules proposal is rejected by union hardliners, extending the business shutdown.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "The demands are criticized by consumer groups who argue VAT will reduce middleman price manipulation.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Advisory panel talks break down as trader representatives demand exemption for small retail shops.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-04"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-05: Summer heatwave drinking water Kandi
nk = f"{short_code}_2005_05_kandi_water"
news_items.append({
    "newsKey": nk, "month": "2005-05",
    "title": "Drinking Water Crisis Reported in Kandi Region (2005-05)",
    "description": "An intense summer heatwave in May dries up local wells in the sub-mountainous Kandi region. Residents in Hoshiarpur and Ropar districts protest over irregular drinking water supply, demanding immediate relief.",
    "issueTags": ["rural", "infrastructure"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "rural"},
    "reactionOptions": create_reactions(
        nk, "kandi_water",
        "The Public Health Engineering Department releases emergency funds to deploy water tankers and drill borewells.",
        "SAD leaders lead protests outside PHE offices, accusing the Congress government of failing to prepare.",
        "A joint water task force is formed to manage daily supply allocations to the worst-affected blocks.",
        "The Public Health Engineering Minister declines to give a timeline for restoring piped water supply.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"punjabRuralTrustMemory": -1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        14, "Private water tanker operators charge illegal premiums, drawing local public anger and media focus.", {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        12, "Protests are labeled by the ruling party as creating public panic, limiting their wider impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Task force coordination fails as local block officers report a lack of fuel for water tankers.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-05"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-06: Mohali international airport MOU
nk = f"{short_code}_2005_06_mohali_airport"
news_items.append({
    "newsKey": nk, "month": "2005-06",
    "title": "MOU Signed for Mohali International Airport Project (2005-06)",
    "description": "The Punjab government signs an MOU with central aviation authorities to set up an international airport in Mohali (SAS Nagar). The project is expected to boost local real estate and connectivity in the Chandigarh capital region.",
    "issueTags": ["infrastructure", "economy"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "mohali_airport",
        "The state government fast-tracks land acquisition and plans a major connectivity corridor to Mohali.",
        "Opposition leaders claim the land acquisition is done at low prices, hurting local farmers.",
        "A joint committee of Greater Mohali Development Authority and local farmers is set up to negotiate compensation.",
        "The Aviation Department declines to comment on the project's target completion timeline.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabStabilityMemory": -1}, {"punjabRuralTrustMemory": -1}, {"punjabStabilityMemory": -1},
        13, "Real estate speculation drives land prices up, delaying acquisition and drawing local criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The compensation claims are dismissed by developers who support industrial corridor expansion.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Compensation negotiation meetings stall as farm representatives demand double the market rate.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-06"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-07: Summer power cuts
nk = f"{short_code}_2005_07_industrial_power_cuts"
news_items.append({
    "newsKey": nk, "month": "2005-07",
    "title": "Power Shortage Limits Supply in Industrial Hubs (2005-07)",
    "description": "As the summer agricultural demand peaks, state power generation deficit forces the board to impose power cuts on industrial units in Ludhiana and Mandi Gobindgarh. Industrial bodies warning of job losses and plant closures.",
    "issueTags": ["infrastructure", "protest"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "industrial_power_cuts",
        "The Power Ministry purchases short-term power from external grids and schedules maintenance shutdowns.",
        "Opposition leaders stage dharnas outside power board offices, accusing the Congress government of infrastructure neglect.",
        "A joint committee of power board officials and industrial chambers is set up to negotiate supply slots.",
        "The Electricity Board declines to publish a daily schedule of the planned urban power cuts.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"punjabStabilityMemory": -1}, {"punjabStabilityMemory": 1}, {"punjabStabilityMemory": -1},
        14, "Expensive short-term power purchases increase the electricity board's deficit, drawing criticism.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -2},
        12, "Protestors block local roads in Ludhiana, drawing complaints from commuter groups.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Disagreements over power tariffs for small-scale units stall the joint slot negotiations.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-07"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-08: Flash floods Sutlej Ropar
nk = f"{short_code}_2005_08_sutlej_floods"
news_items.append({
    "newsKey": nk, "month": "2005-08",
    "title": "Flash Floods in Sutlej Damage Crops in Ropar (2005-08)",
    "description": "Continuous heavy rainfall in August causes the Sutlej river to overflow, inundating low-lying agricultural land and damaging standing crops in Ropar and Ferozepur districts. The administration coordinates evacuations.",
    "issueTags": ["rural", "security_crisis"],
    "weights": {"baseSelectionWeight": 1.25, "reactionProfile": "security_crisis"},
    "reactionOptions": create_reactions(
        nk, "sutlej_floods",
        "The administration sets up temporary relief camps and coordinates with local NGOs to distribute dry rations.",
        "Opposition leaders criticize the relief effort, accusing local officers of bias in distributing aid packages.",
        "A joint legislative relief committee is established to supervise rehabilitation work in Ropar division.",
        "The District Collector declines to release the official crop loss estimates in the first week.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -3, "corruptionScore": 1, "mediaImage": -3, "publicSupport": -3},
        {"punjabStabilityMemory": -1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        14, "Logistical failures delay the delivery of tents to remote villages, drawing local protests.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        12, "The criticism leads to minor scuffles at distribution centers, disrupting relief work.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Disagreements over relief beneficiary lists stall aid distribution in several affected talukas.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-08"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-09: Cooperative land bank audit irregularities
nk = f"{short_code}_2005_09_cooperative_scandal"
news_items.append({
    "newsKey": nk, "month": "2005-09",
    "title": "Irregularities Uncovered in Cooperative Mortgage Banks (2005-09)",
    "description": "A cooperative department audit uncovers major irregularities and illegal credit extensions in local land mortgage banks. The opposition SAD demands a judicial probe, alleging that credit allocations favored ruling party loyalists.",
    "issueTags": ["corruption", "rural"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "corruption"},
    "reactionOptions": create_reactions(
        nk, "cooperative_scandal",
        "The Cooperative Department suspends the boards of the irregular banks and orders a forensic audit.",
        "SAD opposition leaders demand a judicial probe and stage protests outside bank head offices.",
        "A multi-party legislative subcommittee is formed to draft credit guidelines for cooperative institutions.",
        "The Cooperative Minister declines to comment on the total volume of frozen farmer deposits.",
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabCorruptionMemory": -1}, {"punjabCorruptionMemory": 1}, {"punjabStabilityMemory": -1},
        15, "The forensic audit is delayed, prolonging the freeze on farmer accounts and drawing public anger.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        13, "Bank protests lead to minor property damage at a rural branch, drawing public disapproval.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        10, "Subcommittee talks are slowed down by disagreements over government representation on bank boards.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-09"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-10: Peace initiative visit Pak Punjab
nk = f"{short_code}_2005_10_peace_initiative"
news_items.append({
    "newsKey": nk, "month": "2005-10",
    "title": "CM Amarinder Singh Visits Pakistan's Punjab Province (2005-10)",
    "description": "In a high-profile peace initiative, CM Amarinder Singh leads a goodwill delegation to Lahore in Pakistan's Punjab province. The visit promotes cultural exchanges and trade discussions, drawing positive national press.",
    "issueTags": ["politics", "identity"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "peace_initiative",
        "The government highlights the visit as a success for Punjabi cultural ties and border trade negotiations.",
        "Opposition BJP leaders criticize the visit, claiming it dilutes security concerns and cross-border infiltration issues.",
        "A joint legislative-farmer task force is formed to monitor border trade progress and lobby central clearance.",
        "The CM's office declines to release the exact travel expenses of the Lahore delegation to the media.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabIdentityMemory": 1}, {"punjabIdentityMemory": -1}, {"punjabStabilityMemory": -1},
        13, "Trade talks are stalled by central custom department objections in Delhi, drawing local criticism.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The criticism is dismissed by peace advocacy groups who support the cross-border cultural ties.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        9, "Task force meetings are delayed by the non-participation of transport union representatives.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-10"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-11: Basmati contract farming
nk = f"{short_code}_2005_11_contract_farming"
news_items.append({
    "newsKey": nk, "month": "2005-11",
    "title": "Government Launches Basmati Contract Farming Scheme (2005-11)",
    "description": "The Punjab government launches a contract farming scheme for basmati rice, partnering with private agro-firms to guarantee purchase prices for farmers. The scheme aims to encourage diversification away from standard paddy.",
    "issueTags": ["rural", "economy"],
    "weights": {"baseSelectionWeight": 1.15, "reactionProfile": "governance"},
    "reactionOptions": create_reactions(
        nk, "contract_farming",
        "The Agriculture Department sets up contract registration centers and registers corporate crop buyers.",
        "Opposition SAD leaders claim the contracts favor corporations and lack legal protection for small farmers.",
        "A joint assembly panel is established to monitor contract execution and draft model buyer agreements.",
        "The Agriculture Commissioner declines to release the list of private firms registered under the scheme.",
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 3},
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 1, "mediaImage": -2, "publicSupport": -2},
        {"punjabRuralTrustMemory": 1}, {"punjabRuralTrustMemory": -1}, {"punjabStabilityMemory": -1},
        13, "Disputes over crop quality grading at mandis lead to minor farmer protests against private buyers.", {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The compensation claims are dismissed by developers who support industrial corridor expansion.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
        10, "Compensation negotiation meetings stall as farm representatives demand double the market rate.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}
    ),
    "type": "external", "monthTags": ["2005-11"], "crisisTriggerKey": None, "crisisDuration": 2
})

# 2005-12: By-elections
nk = f"{short_code}_2005_12_byelections_polls"
news_items.append({
    "newsKey": nk, "month": "2005-12",
    "title": "By-Election Results Announced; Congress and SAD Share Seats (2005-12)",
    "description": "Results for high-stakes assembly by-elections are announced. Congress and the opposition SAD win one seat each, reflecting a closely contested political landscape as both sides claim a momentum advantage.",
    "issueTags": ["politics"],
    "weights": {"baseSelectionWeight": 1.2, "reactionProfile": "politics"},
    "reactionOptions": create_reactions(
        nk, "byelections_polls",
        "The Congress government welcomes the mandate and vows to focus on rural developmental initiatives.",
        "SAD leaders claim their win shows strong public rejection of Congress's urban policies.",
        "Both parties agree to cooperate on rural road project monitoring committees in the constituencies.",
        "The State Election Commissioner declines to comment on requests to review voting counts in disputed blocks.",
        {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2},
        {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2},
        {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2},
        {"punjabStabilityMemory": -1}, {"punjabRuralTrustMemory": 1}, {"punjabStabilityMemory": -1},
        13, "Disputes over specific block project allocations stall municipal council meetings.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1},
        11, "The SAD claims are labeled as exaggerated by political observers, limiting their public impact.", {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1},
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
    "sourceNotes": "Government: SAD/BJP coalition led by Parkash Singh Badal CM until Feb 2002, then Congress led by Captain Amarinder Singh CM from Feb 2002 through the end of this period. Opposition: Congress until Feb 2002, then SAD/BJP coalition. Main issues: Farm subsidies (free power tubewells), PPSC recruitment scandal (Ravi Sidhu arrest), vigilance actions against rivals, water agreements termination (Termination of Agreements Act 2004), SGPC elections, and cross-border peace initiative. Built programmatically matching the schema and calibration constraints.",
    "defaults": {
        "weights": {
            "baseSelectionWeight": 1.0,
            "reactionProfile": "default"
        }
    },
    "newsItems": news_items
}

output_path = Path("seed-data/review/punjab_2001_news.json")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(json.dumps(data, indent=2))
print("Successfully generated punjab_2001_news.json with", len(news_items), "news items!")
