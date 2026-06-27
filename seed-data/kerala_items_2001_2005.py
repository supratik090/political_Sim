from helper import reaction, no_comment, make_news, eff, risk

ITEMS_2001_2005 = []

# 2001-01
ITEMS_2001_2005.append(make_news(
    key="kl2001_2001_01_remittance_boom",
    month="2001-01",
    title="Gulf Remittance Boom Fuels Local Construction and Land Rush (2001-01)",
    desc="Remittances from Non-Resident Keralites (NRKs) surge, boosting real estate and banking reserves in Malabar. In Kerala, this monthly event shapes key state development debates.",
    tags=['economy'],
    base_w=1.15, profile="economy",
    reactions=[
        reaction("gov_action_remittance_boom", "Initiate a special government commission to resolve remittance_boom issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_remittance_boom", "Demand that the government address remittance_boom concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_remittance_boom", "Propose a joint multi-party round table to build consensus on remittance_boom.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-02
ITEMS_2001_2005.append(make_news(
    key="kl2001_2001_02_plantation_strikes",
    month="2001-02",
    title="Idukki Tea Plantation Workers Strike Over Minimum Wage (2001-02)",
    desc="Thousands of tea leaf pluckers in Munnar block factory entrances, demanding daily wage raises and medical benefits. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'economy'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_plantation_strikes", "Initiate a special government commission to resolve plantation_strikes issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_plantation_strikes", "Demand that the government address plantation_strikes concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_plantation_strikes", "Propose a joint multi-party round table to build consensus on plantation_strikes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-03
ITEMS_2001_2005.append(make_news(
    key="kl2001_2001_03_political_violence",
    month="2001-03",
    title="Clashes Between CPM and RSS Cadres Reported in Kannur (2001-03)",
    desc="Kannur district reports localized clashes, prompting peace committee meetings and police patrol deployments. In Kerala, this monthly event shapes key state development debates.",
    tags=['security_crisis'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("gov_action_political_violence", "Initiate a special government commission to resolve political_violence issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_political_violence", "Demand that the government address political_violence concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_political_violence", "Propose a joint multi-party round table to build consensus on political_violence.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-04
ITEMS_2001_2005.append(make_news(
    key="kl2001_2001_04_tourism_campaign",
    month="2001-04",
    title="God's Own Country Tourism Branding Campaigns Launched (2001-04)",
    desc="The state tourism department launches international marketing campaigns to attract luxury house-boat travelers. In Kerala, this monthly event shapes key state development debates.",
    tags=['tourism', 'economy'],
    base_w=1.25, profile="economy",
    reactions=[
        reaction("gov_action_tourism_campaign", "Initiate a special government commission to resolve tourism_campaign issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_tourism_campaign", "Demand that the government address tourism_campaign concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_tourism_campaign", "Propose a joint multi-party round table to build consensus on tourism_campaign.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-05
ITEMS_2001_2005.append(make_news(
    key="kl2001_2001_05_marad_clashes",
    month="2001-05",
    title="Marad Beach Communal Clashes Trigger High Tension (2001-05)",
    desc="Violent clashes at Marad fishing village in Kozhikode lead to police curfew deployments and judicial inquiries. In Kerala, this monthly event shapes key state development debates.",
    tags=['security_crisis', 'identity'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("gov_action_marad_clashes", "Initiate a special government commission to resolve marad_clashes issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_marad_clashes", "Demand that the government address marad_clashes concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_marad_clashes", "Propose a joint multi-party round table to build consensus on marad_clashes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-06
ITEMS_2001_2005.append(make_news(
    key="kl2001_2001_06_panchayat_funding",
    month="2001-06",
    title="Decentralized Planning Allocations Handed to Village Panchayats (2001-06)",
    desc="The government delegates 35% of state plan funds to local bodies under the People's Plan Campaign. In Kerala, this monthly event shapes key state development debates.",
    tags=['governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_panchayat_funding", "Initiate a special government commission to resolve panchayat_funding issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_panchayat_funding", "Demand that the government address panchayat_funding concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_panchayat_funding", "Propose a joint multi-party round table to build consensus on panchayat_funding.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-07
ITEMS_2001_2005.append(make_news(
    key="kl2001_2001_07_hartal_protests",
    month="2001-07",
    title="Trade Unions Call State-Wide Hartal Over Fuel Price Hikes (2001-07)",
    desc="A joint committee of trade unions calls a 24-hour hartal, shutting down transport and shops across districts. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'economy'],
    base_w=1.15, profile="protest",
    reactions=[
        reaction("gov_action_hartal_protests", "Initiate a special government commission to resolve hartal_protests issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_hartal_protests", "Demand that the government address hartal_protests concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_hartal_protests", "Propose a joint multi-party round table to build consensus on hartal_protests.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-08
ITEMS_2001_2005.append(make_news(
    key="kl2001_2001_08_cashew_industry",
    month="2001-08",
    title="Kollam Cashew Processing Factories Face Credit Squeeze (2001-08)",
    desc="Traditional cashew processing units report supply shortages of raw nuts, demanding emergency loan guarantees. In Kerala, this monthly event shapes key state development debates.",
    tags=['economy', 'rural'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_cashew_industry", "Initiate a special government commission to resolve cashew_industry issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cashew_industry", "Demand that the government address cashew_industry concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cashew_industry", "Propose a joint multi-party round table to build consensus on cashew_industry.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-09
ITEMS_2001_2005.append(make_news(
    key="kl2001_2001_09_silent_valley",
    month="2001-09",
    title="Silent Valley Buffer Zone Forest Protection Mandated (2001-09)",
    desc="Environmental groups welcome new boundaries around Silent Valley National Park, restricting tourist cottages. In Kerala, this monthly event shapes key state development debates.",
    tags=['environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_silent_valley", "Initiate a special government commission to resolve silent_valley issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_silent_valley", "Demand that the government address silent_valley concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_silent_valley", "Propose a joint multi-party round table to build consensus on silent_valley.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-10
ITEMS_2001_2005.append(make_news(
    key="kl2001_2001_10_state_lottery",
    month="2001-10",
    title="State Lottery Distribution Regulations Tightened (2001-10)",
    desc="Finance department institutes checks to stop paper ticket smuggling from neighboring states, protecting local agents. In Kerala, this monthly event shapes key state development debates.",
    tags=['governance', 'economy'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_state_lottery", "Initiate a special government commission to resolve state_lottery issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_state_lottery", "Demand that the government address state_lottery concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_state_lottery", "Propose a joint multi-party round table to build consensus on state_lottery.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-11
ITEMS_2001_2005.append(make_news(
    key="kl2001_2001_11_education_reforms",
    month="2001-11",
    title="Self-Financing Professional College Bills Stir Debates (2001-11)",
    desc="Proposed laws regulating seat sharing and fees in private self-financing engineering colleges draw protests. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'education'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_education_reforms", "Initiate a special government commission to resolve education_reforms issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_education_reforms", "Demand that the government address education_reforms concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_education_reforms", "Propose a joint multi-party round table to build consensus on education_reforms.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-12
ITEMS_2001_2005.append(make_news(
    key="kl2001_2001_12_water_scarcity",
    month="2001-12",
    title="Summer Water Depletions in Palakkad Draw Crop Panic (2001-12)",
    desc="Decreasing reservoir levels in the Bharathapuzha basin spark crop concerns, leading to inter-state water requests. In Kerala, this monthly event shapes key state development debates.",
    tags=['rural', 'environment'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_water_scarcity", "Initiate a special government commission to resolve water_scarcity issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_water_scarcity", "Demand that the government address water_scarcity concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_water_scarcity", "Propose a joint multi-party round table to build consensus on water_scarcity.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-01
ITEMS_2001_2005.append(make_news(
    key="kl2001_2002_01_remittance_boom",
    month="2002-01",
    title="Gulf Remittance Boom Fuels Local Construction and Land Rush (2002-01)",
    desc="Remittances from Non-Resident Keralites (NRKs) surge, boosting real estate and banking reserves in Malabar. In Kerala, this monthly event shapes key state development debates.",
    tags=['economy'],
    base_w=1.15, profile="economy",
    reactions=[
        reaction("gov_action_remittance_boom", "Initiate a special government commission to resolve remittance_boom issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_remittance_boom", "Demand that the government address remittance_boom concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_remittance_boom", "Propose a joint multi-party round table to build consensus on remittance_boom.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-02
ITEMS_2001_2005.append(make_news(
    key="kl2001_2002_02_plantation_strikes",
    month="2002-02",
    title="Idukki Tea Plantation Workers Strike Over Minimum Wage (2002-02)",
    desc="Thousands of tea leaf pluckers in Munnar block factory entrances, demanding daily wage raises and medical benefits. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'economy'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_plantation_strikes", "Initiate a special government commission to resolve plantation_strikes issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_plantation_strikes", "Demand that the government address plantation_strikes concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_plantation_strikes", "Propose a joint multi-party round table to build consensus on plantation_strikes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-03
ITEMS_2001_2005.append(make_news(
    key="kl2001_2002_03_political_violence",
    month="2002-03",
    title="Clashes Between CPM and RSS Cadres Reported in Kannur (2002-03)",
    desc="Kannur district reports localized clashes, prompting peace committee meetings and police patrol deployments. In Kerala, this monthly event shapes key state development debates.",
    tags=['security_crisis'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("gov_action_political_violence", "Initiate a special government commission to resolve political_violence issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_political_violence", "Demand that the government address political_violence concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_political_violence", "Propose a joint multi-party round table to build consensus on political_violence.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-04
ITEMS_2001_2005.append(make_news(
    key="kl2001_2002_04_tourism_campaign",
    month="2002-04",
    title="God's Own Country Tourism Branding Campaigns Launched (2002-04)",
    desc="The state tourism department launches international marketing campaigns to attract luxury house-boat travelers. In Kerala, this monthly event shapes key state development debates.",
    tags=['tourism', 'economy'],
    base_w=1.25, profile="economy",
    reactions=[
        reaction("gov_action_tourism_campaign", "Initiate a special government commission to resolve tourism_campaign issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_tourism_campaign", "Demand that the government address tourism_campaign concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_tourism_campaign", "Propose a joint multi-party round table to build consensus on tourism_campaign.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-05
ITEMS_2001_2005.append(make_news(
    key="kl2001_2002_05_marad_clashes",
    month="2002-05",
    title="Marad Beach Communal Clashes Trigger High Tension (2002-05)",
    desc="Violent clashes at Marad fishing village in Kozhikode lead to police curfew deployments and judicial inquiries. In Kerala, this monthly event shapes key state development debates.",
    tags=['security_crisis', 'identity'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("gov_action_marad_clashes", "Initiate a special government commission to resolve marad_clashes issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_marad_clashes", "Demand that the government address marad_clashes concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_marad_clashes", "Propose a joint multi-party round table to build consensus on marad_clashes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-06
ITEMS_2001_2005.append(make_news(
    key="kl2001_2002_06_panchayat_funding",
    month="2002-06",
    title="Decentralized Planning Allocations Handed to Village Panchayats (2002-06)",
    desc="The government delegates 35% of state plan funds to local bodies under the People's Plan Campaign. In Kerala, this monthly event shapes key state development debates.",
    tags=['governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_panchayat_funding", "Initiate a special government commission to resolve panchayat_funding issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_panchayat_funding", "Demand that the government address panchayat_funding concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_panchayat_funding", "Propose a joint multi-party round table to build consensus on panchayat_funding.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-07
ITEMS_2001_2005.append(make_news(
    key="kl2001_2002_07_hartal_protests",
    month="2002-07",
    title="Trade Unions Call State-Wide Hartal Over Fuel Price Hikes (2002-07)",
    desc="A joint committee of trade unions calls a 24-hour hartal, shutting down transport and shops across districts. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'economy'],
    base_w=1.15, profile="protest",
    reactions=[
        reaction("gov_action_hartal_protests", "Initiate a special government commission to resolve hartal_protests issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_hartal_protests", "Demand that the government address hartal_protests concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_hartal_protests", "Propose a joint multi-party round table to build consensus on hartal_protests.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-08
ITEMS_2001_2005.append(make_news(
    key="kl2001_2002_08_cashew_industry",
    month="2002-08",
    title="Kollam Cashew Processing Factories Face Credit Squeeze (2002-08)",
    desc="Traditional cashew processing units report supply shortages of raw nuts, demanding emergency loan guarantees. In Kerala, this monthly event shapes key state development debates.",
    tags=['economy', 'rural'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_cashew_industry", "Initiate a special government commission to resolve cashew_industry issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cashew_industry", "Demand that the government address cashew_industry concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cashew_industry", "Propose a joint multi-party round table to build consensus on cashew_industry.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-09
ITEMS_2001_2005.append(make_news(
    key="kl2001_2002_09_silent_valley",
    month="2002-09",
    title="Silent Valley Buffer Zone Forest Protection Mandated (2002-09)",
    desc="Environmental groups welcome new boundaries around Silent Valley National Park, restricting tourist cottages. In Kerala, this monthly event shapes key state development debates.",
    tags=['environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_silent_valley", "Initiate a special government commission to resolve silent_valley issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_silent_valley", "Demand that the government address silent_valley concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_silent_valley", "Propose a joint multi-party round table to build consensus on silent_valley.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-10
ITEMS_2001_2005.append(make_news(
    key="kl2001_2002_10_state_lottery",
    month="2002-10",
    title="State Lottery Distribution Regulations Tightened (2002-10)",
    desc="Finance department institutes checks to stop paper ticket smuggling from neighboring states, protecting local agents. In Kerala, this monthly event shapes key state development debates.",
    tags=['governance', 'economy'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_state_lottery", "Initiate a special government commission to resolve state_lottery issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_state_lottery", "Demand that the government address state_lottery concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_state_lottery", "Propose a joint multi-party round table to build consensus on state_lottery.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-11
ITEMS_2001_2005.append(make_news(
    key="kl2001_2002_11_education_reforms",
    month="2002-11",
    title="Self-Financing Professional College Bills Stir Debates (2002-11)",
    desc="Proposed laws regulating seat sharing and fees in private self-financing engineering colleges draw protests. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'education'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_education_reforms", "Initiate a special government commission to resolve education_reforms issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_education_reforms", "Demand that the government address education_reforms concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_education_reforms", "Propose a joint multi-party round table to build consensus on education_reforms.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-12
ITEMS_2001_2005.append(make_news(
    key="kl2001_2002_12_water_scarcity",
    month="2002-12",
    title="Summer Water Depletions in Palakkad Draw Crop Panic (2002-12)",
    desc="Decreasing reservoir levels in the Bharathapuzha basin spark crop concerns, leading to inter-state water requests. In Kerala, this monthly event shapes key state development debates.",
    tags=['rural', 'environment'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_water_scarcity", "Initiate a special government commission to resolve water_scarcity issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_water_scarcity", "Demand that the government address water_scarcity concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_water_scarcity", "Propose a joint multi-party round table to build consensus on water_scarcity.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-01
ITEMS_2001_2005.append(make_news(
    key="kl2001_2003_01_remittance_boom",
    month="2003-01",
    title="Gulf Remittance Boom Fuels Local Construction and Land Rush (2003-01)",
    desc="Remittances from Non-Resident Keralites (NRKs) surge, boosting real estate and banking reserves in Malabar. In Kerala, this monthly event shapes key state development debates.",
    tags=['economy'],
    base_w=1.15, profile="economy",
    reactions=[
        reaction("gov_action_remittance_boom", "Initiate a special government commission to resolve remittance_boom issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_remittance_boom", "Demand that the government address remittance_boom concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_remittance_boom", "Propose a joint multi-party round table to build consensus on remittance_boom.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-02
ITEMS_2001_2005.append(make_news(
    key="kl2001_2003_02_plantation_strikes",
    month="2003-02",
    title="Idukki Tea Plantation Workers Strike Over Minimum Wage (2003-02)",
    desc="Thousands of tea leaf pluckers in Munnar block factory entrances, demanding daily wage raises and medical benefits. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'economy'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_plantation_strikes", "Initiate a special government commission to resolve plantation_strikes issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_plantation_strikes", "Demand that the government address plantation_strikes concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_plantation_strikes", "Propose a joint multi-party round table to build consensus on plantation_strikes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-03
ITEMS_2001_2005.append(make_news(
    key="kl2001_2003_03_political_violence",
    month="2003-03",
    title="Clashes Between CPM and RSS Cadres Reported in Kannur (2003-03)",
    desc="Kannur district reports localized clashes, prompting peace committee meetings and police patrol deployments. In Kerala, this monthly event shapes key state development debates.",
    tags=['security_crisis'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("gov_action_political_violence", "Initiate a special government commission to resolve political_violence issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_political_violence", "Demand that the government address political_violence concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_political_violence", "Propose a joint multi-party round table to build consensus on political_violence.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-04
ITEMS_2001_2005.append(make_news(
    key="kl2001_2003_04_tourism_campaign",
    month="2003-04",
    title="God's Own Country Tourism Branding Campaigns Launched (2003-04)",
    desc="The state tourism department launches international marketing campaigns to attract luxury house-boat travelers. In Kerala, this monthly event shapes key state development debates.",
    tags=['tourism', 'economy'],
    base_w=1.25, profile="economy",
    reactions=[
        reaction("gov_action_tourism_campaign", "Initiate a special government commission to resolve tourism_campaign issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_tourism_campaign", "Demand that the government address tourism_campaign concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_tourism_campaign", "Propose a joint multi-party round table to build consensus on tourism_campaign.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-05
ITEMS_2001_2005.append(make_news(
    key="kl2001_2003_05_marad_clashes",
    month="2003-05",
    title="Marad Beach Communal Clashes Trigger High Tension (2003-05)",
    desc="Violent clashes at Marad fishing village in Kozhikode lead to police curfew deployments and judicial inquiries. In Kerala, this monthly event shapes key state development debates.",
    tags=['security_crisis', 'identity'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("gov_action_marad_clashes", "Initiate a special government commission to resolve marad_clashes issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_marad_clashes", "Demand that the government address marad_clashes concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_marad_clashes", "Propose a joint multi-party round table to build consensus on marad_clashes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-06
ITEMS_2001_2005.append(make_news(
    key="kl2001_2003_06_panchayat_funding",
    month="2003-06",
    title="Decentralized Planning Allocations Handed to Village Panchayats (2003-06)",
    desc="The government delegates 35% of state plan funds to local bodies under the People's Plan Campaign. In Kerala, this monthly event shapes key state development debates.",
    tags=['governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_panchayat_funding", "Initiate a special government commission to resolve panchayat_funding issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_panchayat_funding", "Demand that the government address panchayat_funding concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_panchayat_funding", "Propose a joint multi-party round table to build consensus on panchayat_funding.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-07
ITEMS_2001_2005.append(make_news(
    key="kl2001_2003_07_hartal_protests",
    month="2003-07",
    title="Trade Unions Call State-Wide Hartal Over Fuel Price Hikes (2003-07)",
    desc="A joint committee of trade unions calls a 24-hour hartal, shutting down transport and shops across districts. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'economy'],
    base_w=1.15, profile="protest",
    reactions=[
        reaction("gov_action_hartal_protests", "Initiate a special government commission to resolve hartal_protests issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_hartal_protests", "Demand that the government address hartal_protests concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_hartal_protests", "Propose a joint multi-party round table to build consensus on hartal_protests.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-08
ITEMS_2001_2005.append(make_news(
    key="kl2001_2003_08_cashew_industry",
    month="2003-08",
    title="Kollam Cashew Processing Factories Face Credit Squeeze (2003-08)",
    desc="Traditional cashew processing units report supply shortages of raw nuts, demanding emergency loan guarantees. In Kerala, this monthly event shapes key state development debates.",
    tags=['economy', 'rural'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_cashew_industry", "Initiate a special government commission to resolve cashew_industry issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cashew_industry", "Demand that the government address cashew_industry concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cashew_industry", "Propose a joint multi-party round table to build consensus on cashew_industry.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-09
ITEMS_2001_2005.append(make_news(
    key="kl2001_2003_09_silent_valley",
    month="2003-09",
    title="Silent Valley Buffer Zone Forest Protection Mandated (2003-09)",
    desc="Environmental groups welcome new boundaries around Silent Valley National Park, restricting tourist cottages. In Kerala, this monthly event shapes key state development debates.",
    tags=['environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_silent_valley", "Initiate a special government commission to resolve silent_valley issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_silent_valley", "Demand that the government address silent_valley concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_silent_valley", "Propose a joint multi-party round table to build consensus on silent_valley.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-10
ITEMS_2001_2005.append(make_news(
    key="kl2001_2003_10_state_lottery",
    month="2003-10",
    title="State Lottery Distribution Regulations Tightened (2003-10)",
    desc="Finance department institutes checks to stop paper ticket smuggling from neighboring states, protecting local agents. In Kerala, this monthly event shapes key state development debates.",
    tags=['governance', 'economy'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_state_lottery", "Initiate a special government commission to resolve state_lottery issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_state_lottery", "Demand that the government address state_lottery concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_state_lottery", "Propose a joint multi-party round table to build consensus on state_lottery.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-11
ITEMS_2001_2005.append(make_news(
    key="kl2001_2003_11_education_reforms",
    month="2003-11",
    title="Self-Financing Professional College Bills Stir Debates (2003-11)",
    desc="Proposed laws regulating seat sharing and fees in private self-financing engineering colleges draw protests. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'education'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_education_reforms", "Initiate a special government commission to resolve education_reforms issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_education_reforms", "Demand that the government address education_reforms concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_education_reforms", "Propose a joint multi-party round table to build consensus on education_reforms.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-12
ITEMS_2001_2005.append(make_news(
    key="kl2001_2003_12_water_scarcity",
    month="2003-12",
    title="Summer Water Depletions in Palakkad Draw Crop Panic (2003-12)",
    desc="Decreasing reservoir levels in the Bharathapuzha basin spark crop concerns, leading to inter-state water requests. In Kerala, this monthly event shapes key state development debates.",
    tags=['rural', 'environment'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_water_scarcity", "Initiate a special government commission to resolve water_scarcity issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_water_scarcity", "Demand that the government address water_scarcity concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_water_scarcity", "Propose a joint multi-party round table to build consensus on water_scarcity.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-01
ITEMS_2001_2005.append(make_news(
    key="kl2001_2004_01_remittance_boom",
    month="2004-01",
    title="Gulf Remittance Boom Fuels Local Construction and Land Rush (2004-01)",
    desc="Remittances from Non-Resident Keralites (NRKs) surge, boosting real estate and banking reserves in Malabar. In Kerala, this monthly event shapes key state development debates.",
    tags=['economy'],
    base_w=1.15, profile="economy",
    reactions=[
        reaction("gov_action_remittance_boom", "Initiate a special government commission to resolve remittance_boom issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_remittance_boom", "Demand that the government address remittance_boom concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_remittance_boom", "Propose a joint multi-party round table to build consensus on remittance_boom.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-02
ITEMS_2001_2005.append(make_news(
    key="kl2001_2004_02_plantation_strikes",
    month="2004-02",
    title="Idukki Tea Plantation Workers Strike Over Minimum Wage (2004-02)",
    desc="Thousands of tea leaf pluckers in Munnar block factory entrances, demanding daily wage raises and medical benefits. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'economy'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_plantation_strikes", "Initiate a special government commission to resolve plantation_strikes issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_plantation_strikes", "Demand that the government address plantation_strikes concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_plantation_strikes", "Propose a joint multi-party round table to build consensus on plantation_strikes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-03
ITEMS_2001_2005.append(make_news(
    key="kl2001_2004_03_political_violence",
    month="2004-03",
    title="Clashes Between CPM and RSS Cadres Reported in Kannur (2004-03)",
    desc="Kannur district reports localized clashes, prompting peace committee meetings and police patrol deployments. In Kerala, this monthly event shapes key state development debates.",
    tags=['security_crisis'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("gov_action_political_violence", "Initiate a special government commission to resolve political_violence issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_political_violence", "Demand that the government address political_violence concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_political_violence", "Propose a joint multi-party round table to build consensus on political_violence.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-04
ITEMS_2001_2005.append(make_news(
    key="kl2001_2004_04_tourism_campaign",
    month="2004-04",
    title="God's Own Country Tourism Branding Campaigns Launched (2004-04)",
    desc="The state tourism department launches international marketing campaigns to attract luxury house-boat travelers. In Kerala, this monthly event shapes key state development debates.",
    tags=['tourism', 'economy'],
    base_w=1.25, profile="economy",
    reactions=[
        reaction("gov_action_tourism_campaign", "Initiate a special government commission to resolve tourism_campaign issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_tourism_campaign", "Demand that the government address tourism_campaign concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_tourism_campaign", "Propose a joint multi-party round table to build consensus on tourism_campaign.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-05
ITEMS_2001_2005.append(make_news(
    key="kl2001_2004_05_marad_clashes",
    month="2004-05",
    title="Marad Beach Communal Clashes Trigger High Tension (2004-05)",
    desc="Violent clashes at Marad fishing village in Kozhikode lead to police curfew deployments and judicial inquiries. In Kerala, this monthly event shapes key state development debates.",
    tags=['security_crisis', 'identity'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("gov_action_marad_clashes", "Initiate a special government commission to resolve marad_clashes issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_marad_clashes", "Demand that the government address marad_clashes concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_marad_clashes", "Propose a joint multi-party round table to build consensus on marad_clashes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-06
ITEMS_2001_2005.append(make_news(
    key="kl2001_2004_06_panchayat_funding",
    month="2004-06",
    title="Decentralized Planning Allocations Handed to Village Panchayats (2004-06)",
    desc="The government delegates 35% of state plan funds to local bodies under the People's Plan Campaign. In Kerala, this monthly event shapes key state development debates.",
    tags=['governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_panchayat_funding", "Initiate a special government commission to resolve panchayat_funding issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_panchayat_funding", "Demand that the government address panchayat_funding concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_panchayat_funding", "Propose a joint multi-party round table to build consensus on panchayat_funding.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-07
ITEMS_2001_2005.append(make_news(
    key="kl2001_2004_07_hartal_protests",
    month="2004-07",
    title="Trade Unions Call State-Wide Hartal Over Fuel Price Hikes (2004-07)",
    desc="A joint committee of trade unions calls a 24-hour hartal, shutting down transport and shops across districts. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'economy'],
    base_w=1.15, profile="protest",
    reactions=[
        reaction("gov_action_hartal_protests", "Initiate a special government commission to resolve hartal_protests issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_hartal_protests", "Demand that the government address hartal_protests concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_hartal_protests", "Propose a joint multi-party round table to build consensus on hartal_protests.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-08
ITEMS_2001_2005.append(make_news(
    key="kl2001_2004_08_cashew_industry",
    month="2004-08",
    title="Kollam Cashew Processing Factories Face Credit Squeeze (2004-08)",
    desc="Traditional cashew processing units report supply shortages of raw nuts, demanding emergency loan guarantees. In Kerala, this monthly event shapes key state development debates.",
    tags=['economy', 'rural'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_cashew_industry", "Initiate a special government commission to resolve cashew_industry issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cashew_industry", "Demand that the government address cashew_industry concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cashew_industry", "Propose a joint multi-party round table to build consensus on cashew_industry.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-09
ITEMS_2001_2005.append(make_news(
    key="kl2001_2004_09_silent_valley",
    month="2004-09",
    title="Silent Valley Buffer Zone Forest Protection Mandated (2004-09)",
    desc="Environmental groups welcome new boundaries around Silent Valley National Park, restricting tourist cottages. In Kerala, this monthly event shapes key state development debates.",
    tags=['environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_silent_valley", "Initiate a special government commission to resolve silent_valley issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_silent_valley", "Demand that the government address silent_valley concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_silent_valley", "Propose a joint multi-party round table to build consensus on silent_valley.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-10
ITEMS_2001_2005.append(make_news(
    key="kl2001_2004_10_state_lottery",
    month="2004-10",
    title="State Lottery Distribution Regulations Tightened (2004-10)",
    desc="Finance department institutes checks to stop paper ticket smuggling from neighboring states, protecting local agents. In Kerala, this monthly event shapes key state development debates.",
    tags=['governance', 'economy'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_state_lottery", "Initiate a special government commission to resolve state_lottery issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_state_lottery", "Demand that the government address state_lottery concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_state_lottery", "Propose a joint multi-party round table to build consensus on state_lottery.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-11
ITEMS_2001_2005.append(make_news(
    key="kl2001_2004_11_education_reforms",
    month="2004-11",
    title="Self-Financing Professional College Bills Stir Debates (2004-11)",
    desc="Proposed laws regulating seat sharing and fees in private self-financing engineering colleges draw protests. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'education'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_education_reforms", "Initiate a special government commission to resolve education_reforms issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_education_reforms", "Demand that the government address education_reforms concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_education_reforms", "Propose a joint multi-party round table to build consensus on education_reforms.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-12
ITEMS_2001_2005.append(make_news(
    key="kl2001_2004_12_water_scarcity",
    month="2004-12",
    title="Summer Water Depletions in Palakkad Draw Crop Panic (2004-12)",
    desc="Decreasing reservoir levels in the Bharathapuzha basin spark crop concerns, leading to inter-state water requests. In Kerala, this monthly event shapes key state development debates.",
    tags=['rural', 'environment'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_water_scarcity", "Initiate a special government commission to resolve water_scarcity issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_water_scarcity", "Demand that the government address water_scarcity concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_water_scarcity", "Propose a joint multi-party round table to build consensus on water_scarcity.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-01
ITEMS_2001_2005.append(make_news(
    key="kl2001_2005_01_remittance_boom",
    month="2005-01",
    title="Gulf Remittance Boom Fuels Local Construction and Land Rush (2005-01)",
    desc="Remittances from Non-Resident Keralites (NRKs) surge, boosting real estate and banking reserves in Malabar. In Kerala, this monthly event shapes key state development debates.",
    tags=['economy'],
    base_w=1.15, profile="economy",
    reactions=[
        reaction("gov_action_remittance_boom", "Initiate a special government commission to resolve remittance_boom issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_remittance_boom", "Demand that the government address remittance_boom concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_remittance_boom", "Propose a joint multi-party round table to build consensus on remittance_boom.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-02
ITEMS_2001_2005.append(make_news(
    key="kl2001_2005_02_plantation_strikes",
    month="2005-02",
    title="Idukki Tea Plantation Workers Strike Over Minimum Wage (2005-02)",
    desc="Thousands of tea leaf pluckers in Munnar block factory entrances, demanding daily wage raises and medical benefits. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'economy'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_plantation_strikes", "Initiate a special government commission to resolve plantation_strikes issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_plantation_strikes", "Demand that the government address plantation_strikes concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_plantation_strikes", "Propose a joint multi-party round table to build consensus on plantation_strikes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-03
ITEMS_2001_2005.append(make_news(
    key="kl2001_2005_03_political_violence",
    month="2005-03",
    title="Clashes Between CPM and RSS Cadres Reported in Kannur (2005-03)",
    desc="Kannur district reports localized clashes, prompting peace committee meetings and police patrol deployments. In Kerala, this monthly event shapes key state development debates.",
    tags=['security_crisis'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("gov_action_political_violence", "Initiate a special government commission to resolve political_violence issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_political_violence", "Demand that the government address political_violence concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_political_violence", "Propose a joint multi-party round table to build consensus on political_violence.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-04
ITEMS_2001_2005.append(make_news(
    key="kl2001_2005_04_tourism_campaign",
    month="2005-04",
    title="God's Own Country Tourism Branding Campaigns Launched (2005-04)",
    desc="The state tourism department launches international marketing campaigns to attract luxury house-boat travelers. In Kerala, this monthly event shapes key state development debates.",
    tags=['tourism', 'economy'],
    base_w=1.25, profile="economy",
    reactions=[
        reaction("gov_action_tourism_campaign", "Initiate a special government commission to resolve tourism_campaign issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_tourism_campaign", "Demand that the government address tourism_campaign concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_tourism_campaign", "Propose a joint multi-party round table to build consensus on tourism_campaign.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-05
ITEMS_2001_2005.append(make_news(
    key="kl2001_2005_05_marad_clashes",
    month="2005-05",
    title="Marad Beach Communal Clashes Trigger High Tension (2005-05)",
    desc="Violent clashes at Marad fishing village in Kozhikode lead to police curfew deployments and judicial inquiries. In Kerala, this monthly event shapes key state development debates.",
    tags=['security_crisis', 'identity'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("gov_action_marad_clashes", "Initiate a special government commission to resolve marad_clashes issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_marad_clashes", "Demand that the government address marad_clashes concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_marad_clashes", "Propose a joint multi-party round table to build consensus on marad_clashes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-06
ITEMS_2001_2005.append(make_news(
    key="kl2001_2005_06_panchayat_funding",
    month="2005-06",
    title="Decentralized Planning Allocations Handed to Village Panchayats (2005-06)",
    desc="The government delegates 35% of state plan funds to local bodies under the People's Plan Campaign. In Kerala, this monthly event shapes key state development debates.",
    tags=['governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_panchayat_funding", "Initiate a special government commission to resolve panchayat_funding issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_panchayat_funding", "Demand that the government address panchayat_funding concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_panchayat_funding", "Propose a joint multi-party round table to build consensus on panchayat_funding.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-07
ITEMS_2001_2005.append(make_news(
    key="kl2001_2005_07_hartal_protests",
    month="2005-07",
    title="Trade Unions Call State-Wide Hartal Over Fuel Price Hikes (2005-07)",
    desc="A joint committee of trade unions calls a 24-hour hartal, shutting down transport and shops across districts. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'economy'],
    base_w=1.15, profile="protest",
    reactions=[
        reaction("gov_action_hartal_protests", "Initiate a special government commission to resolve hartal_protests issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_hartal_protests", "Demand that the government address hartal_protests concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_hartal_protests", "Propose a joint multi-party round table to build consensus on hartal_protests.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-08
ITEMS_2001_2005.append(make_news(
    key="kl2001_2005_08_cashew_industry",
    month="2005-08",
    title="Kollam Cashew Processing Factories Face Credit Squeeze (2005-08)",
    desc="Traditional cashew processing units report supply shortages of raw nuts, demanding emergency loan guarantees. In Kerala, this monthly event shapes key state development debates.",
    tags=['economy', 'rural'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_cashew_industry", "Initiate a special government commission to resolve cashew_industry issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cashew_industry", "Demand that the government address cashew_industry concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cashew_industry", "Propose a joint multi-party round table to build consensus on cashew_industry.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-09
ITEMS_2001_2005.append(make_news(
    key="kl2001_2005_09_silent_valley",
    month="2005-09",
    title="Silent Valley Buffer Zone Forest Protection Mandated (2005-09)",
    desc="Environmental groups welcome new boundaries around Silent Valley National Park, restricting tourist cottages. In Kerala, this monthly event shapes key state development debates.",
    tags=['environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_silent_valley", "Initiate a special government commission to resolve silent_valley issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_silent_valley", "Demand that the government address silent_valley concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_silent_valley", "Propose a joint multi-party round table to build consensus on silent_valley.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-10
ITEMS_2001_2005.append(make_news(
    key="kl2001_2005_10_state_lottery",
    month="2005-10",
    title="State Lottery Distribution Regulations Tightened (2005-10)",
    desc="Finance department institutes checks to stop paper ticket smuggling from neighboring states, protecting local agents. In Kerala, this monthly event shapes key state development debates.",
    tags=['governance', 'economy'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_state_lottery", "Initiate a special government commission to resolve state_lottery issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_state_lottery", "Demand that the government address state_lottery concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_state_lottery", "Propose a joint multi-party round table to build consensus on state_lottery.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-11
ITEMS_2001_2005.append(make_news(
    key="kl2001_2005_11_education_reforms",
    month="2005-11",
    title="Self-Financing Professional College Bills Stir Debates (2005-11)",
    desc="Proposed laws regulating seat sharing and fees in private self-financing engineering colleges draw protests. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'education'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_education_reforms", "Initiate a special government commission to resolve education_reforms issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_education_reforms", "Demand that the government address education_reforms concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_education_reforms", "Propose a joint multi-party round table to build consensus on education_reforms.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-12
ITEMS_2001_2005.append(make_news(
    key="kl2001_2005_12_water_scarcity",
    month="2005-12",
    title="Summer Water Depletions in Palakkad Draw Crop Panic (2005-12)",
    desc="Decreasing reservoir levels in the Bharathapuzha basin spark crop concerns, leading to inter-state water requests. In Kerala, this monthly event shapes key state development debates.",
    tags=['rural', 'environment'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_water_scarcity", "Initiate a special government commission to resolve water_scarcity issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_water_scarcity", "Demand that the government address water_scarcity concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_water_scarcity", "Propose a joint multi-party round table to build consensus on water_scarcity.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

