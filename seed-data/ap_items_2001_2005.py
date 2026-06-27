from helper import reaction, no_comment, make_news, eff, risk

ITEMS_2001_2005 = []

# 2001-01
ITEMS_2001_2005.append(make_news(
    key="ap2001_2001_01_cyberabad_it",
    month="2001-01",
    title="Cyberabad Tech Hub Phase 1 Inaugurated in Hyderabad (2001-01)",
    desc="Chief Minister Chandrababu Naidu inaugurates new IT towers, pitching Hyderabad as an international technology hub. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_cyberabad_it", "Initiate a special government commission to resolve cyberabad_it issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cyberabad_it", "Demand that the government address cyberabad_it concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cyberabad_it", "Propose a joint multi-party round table to build consensus on cyberabad_it.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-02
ITEMS_2001_2005.append(make_news(
    key="ap2001_2001_02_farmer_suicides",
    month="2001-02",
    title="Rural Distress and Crop Failure Trigger Protests (2001-02)",
    desc="Rayalaseema and Telangana districts report severe cotton crop failure, sparking farmer protests and debt concerns. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['rural', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_farmer_suicides", "Initiate a special government commission to resolve farmer_suicides issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_farmer_suicides", "Demand that the government address farmer_suicides concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_farmer_suicides", "Propose a joint multi-party round table to build consensus on farmer_suicides.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-03
ITEMS_2001_2005.append(make_news(
    key="ap2001_2001_03_trs_formation",
    month="2001-03",
    title="K. Chandrashekar Rao Formulates TRS to Demand Telangana Statehood (2001-03)",
    desc="KCR resigns from TDP and forms the Telangana Rashtra Samithi (TRS), renewing the agitation for separate statehood. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_trs_formation", "Initiate a special government commission to resolve trs_formation issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_trs_formation", "Demand that the government address trs_formation concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_trs_formation", "Propose a joint multi-party round table to build consensus on trs_formation.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-04
ITEMS_2001_2005.append(make_news(
    key="ap2001_2001_04_naxal_attack",
    month="2001-04",
    title="Landmine Attack Targetting Politicians Triggers Alert (2001-04)",
    desc="Naxalite landmine attack in Chittoor district targets high-profile politicians, placing security forces on high alert. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['security_crisis'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("gov_action_naxal_attack", "Initiate a special government commission to resolve naxal_attack issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_naxal_attack", "Demand that the government address naxal_attack concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_naxal_attack", "Propose a joint multi-party round table to build consensus on naxal_attack.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-05
ITEMS_2001_2005.append(make_news(
    key="ap2001_2001_05_ysr_padayatra",
    month="2001-05",
    title="YSR Launches Historical Padayatra Across Andhra Districts (2001-05)",
    desc="Congress leader YS Rajasekhara Reddy starts a 1,500 km walkathon to connect with rural voters face-to-face. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_ysr_padayatra", "Initiate a special government commission to resolve ysr_padayatra issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_ysr_padayatra", "Demand that the government address ysr_padayatra concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_ysr_padayatra", "Propose a joint multi-party round table to build consensus on ysr_padayatra.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-06
ITEMS_2001_2005.append(make_news(
    key="ap2001_2001_06_microfinance_crisis",
    month="2001-06",
    title="Microfinance Debt Exploitation Sparks Regulatory Concerns (2001-06)",
    desc="Reports of high interest rates charged by private micro-lenders in rural areas prompt calls for government regulations. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['economy', 'rural'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_microfinance_crisis", "Initiate a special government commission to resolve microfinance_crisis issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_microfinance_crisis", "Demand that the government address microfinance_crisis concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_microfinance_crisis", "Propose a joint multi-party round table to build consensus on microfinance_crisis.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-07
ITEMS_2001_2005.append(make_news(
    key="ap2001_2001_07_irrigation_protests",
    month="2001-07",
    title="Nagarjuna Sagar Water Sharing Disputes Spark Protests (2001-07)",
    desc="Farmers block canal pathways, protesting against diversion of upstream water to municipal zones during summers. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_irrigation_protests", "Initiate a special government commission to resolve irrigation_protests issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_irrigation_protests", "Demand that the government address irrigation_protests concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_irrigation_protests", "Propose a joint multi-party round table to build consensus on irrigation_protests.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-08
ITEMS_2001_2005.append(make_news(
    key="ap2001_2001_08_power_subsidy_demand",
    month="2001-08",
    title="Opposition Demands Free Power Supply for Agriculture (2001-08)",
    desc="Congress and Left parties organize assembly boycotts, demanding free electricity for drought-hit farmers. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics', 'rural'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("gov_action_power_subsidy_demand", "Initiate a special government commission to resolve power_subsidy_demand issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_power_subsidy_demand", "Demand that the government address power_subsidy_demand concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_power_subsidy_demand", "Propose a joint multi-party round table to build consensus on power_subsidy_demand.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-09
ITEMS_2001_2005.append(make_news(
    key="ap2001_2001_09_godavari_pushkaram",
    month="2001-09",
    title="Godavari Pushkaram Pilgrimage Draws Record Crowds (2001-09)",
    desc="Millions arrive for holy dips in Rajahmundry, prompting emergency crowd management and transport deployments. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['identity'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_godavari_pushkaram", "Initiate a special government commission to resolve godavari_pushkaram issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_godavari_pushkaram", "Demand that the government address godavari_pushkaram concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_godavari_pushkaram", "Propose a joint multi-party round table to build consensus on godavari_pushkaram.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-10
ITEMS_2001_2005.append(make_news(
    key="ap2001_2001_10_industrial_park",
    month="2001-10",
    title="Visakhapatnam Pharma City Land Acquisitions Approved (2001-10)",
    desc="The government clears land notices to construct a large pharmaceutical cluster in Vizag, drawing local objections. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['infrastructure', 'land_rights'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_industrial_park", "Initiate a special government commission to resolve industrial_park issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_industrial_park", "Demand that the government address industrial_park concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_industrial_park", "Propose a joint multi-party round table to build consensus on industrial_park.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-11
ITEMS_2001_2005.append(make_news(
    key="ap2001_2001_11_tribal_rights",
    month="2001-11",
    title="Agency Area Tribal Land Alienation Protests Erupt (2001-11)",
    desc="Tribal organizations in Adilabad protest against non-tribal encroachments on forest lands in scheduled areas. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['protest', 'identity'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_tribal_rights", "Initiate a special government commission to resolve tribal_rights issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_tribal_rights", "Demand that the government address tribal_rights concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_tribal_rights", "Propose a joint multi-party round table to build consensus on tribal_rights.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-12
ITEMS_2001_2005.append(make_news(
    key="ap2001_2001_12_cooperative_bank",
    month="2001-12",
    title="Cooperative Bank Scams Spark Depositor Outrage (2001-12)",
    desc="Audits expose illegal lending practices by board directors of urban cooperative banks, leading to customer panic. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['corruption', 'economy'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_cooperative_bank", "Initiate a special government commission to resolve cooperative_bank issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cooperative_bank", "Demand that the government address cooperative_bank concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cooperative_bank", "Propose a joint multi-party round table to build consensus on cooperative_bank.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-01
ITEMS_2001_2005.append(make_news(
    key="ap2001_2002_01_cyberabad_it",
    month="2002-01",
    title="Cyberabad Tech Hub Phase 1 Inaugurated in Hyderabad (2002-01)",
    desc="Chief Minister Chandrababu Naidu inaugurates new IT towers, pitching Hyderabad as an international technology hub. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_cyberabad_it", "Initiate a special government commission to resolve cyberabad_it issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cyberabad_it", "Demand that the government address cyberabad_it concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cyberabad_it", "Propose a joint multi-party round table to build consensus on cyberabad_it.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-02
ITEMS_2001_2005.append(make_news(
    key="ap2001_2002_02_farmer_suicides",
    month="2002-02",
    title="Rural Distress and Crop Failure Trigger Protests (2002-02)",
    desc="Rayalaseema and Telangana districts report severe cotton crop failure, sparking farmer protests and debt concerns. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['rural', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_farmer_suicides", "Initiate a special government commission to resolve farmer_suicides issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_farmer_suicides", "Demand that the government address farmer_suicides concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_farmer_suicides", "Propose a joint multi-party round table to build consensus on farmer_suicides.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-03
ITEMS_2001_2005.append(make_news(
    key="ap2001_2002_03_trs_formation",
    month="2002-03",
    title="K. Chandrashekar Rao Formulates TRS to Demand Telangana Statehood (2002-03)",
    desc="KCR resigns from TDP and forms the Telangana Rashtra Samithi (TRS), renewing the agitation for separate statehood. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_trs_formation", "Initiate a special government commission to resolve trs_formation issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_trs_formation", "Demand that the government address trs_formation concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_trs_formation", "Propose a joint multi-party round table to build consensus on trs_formation.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-04
ITEMS_2001_2005.append(make_news(
    key="ap2001_2002_04_naxal_attack",
    month="2002-04",
    title="Landmine Attack Targetting Politicians Triggers Alert (2002-04)",
    desc="Naxalite landmine attack in Chittoor district targets high-profile politicians, placing security forces on high alert. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['security_crisis'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("gov_action_naxal_attack", "Initiate a special government commission to resolve naxal_attack issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_naxal_attack", "Demand that the government address naxal_attack concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_naxal_attack", "Propose a joint multi-party round table to build consensus on naxal_attack.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-05
ITEMS_2001_2005.append(make_news(
    key="ap2001_2002_05_ysr_padayatra",
    month="2002-05",
    title="YSR Launches Historical Padayatra Across Andhra Districts (2002-05)",
    desc="Congress leader YS Rajasekhara Reddy starts a 1,500 km walkathon to connect with rural voters face-to-face. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_ysr_padayatra", "Initiate a special government commission to resolve ysr_padayatra issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_ysr_padayatra", "Demand that the government address ysr_padayatra concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_ysr_padayatra", "Propose a joint multi-party round table to build consensus on ysr_padayatra.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-06
ITEMS_2001_2005.append(make_news(
    key="ap2001_2002_06_microfinance_crisis",
    month="2002-06",
    title="Microfinance Debt Exploitation Sparks Regulatory Concerns (2002-06)",
    desc="Reports of high interest rates charged by private micro-lenders in rural areas prompt calls for government regulations. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['economy', 'rural'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_microfinance_crisis", "Initiate a special government commission to resolve microfinance_crisis issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_microfinance_crisis", "Demand that the government address microfinance_crisis concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_microfinance_crisis", "Propose a joint multi-party round table to build consensus on microfinance_crisis.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-07
ITEMS_2001_2005.append(make_news(
    key="ap2001_2002_07_irrigation_protests",
    month="2002-07",
    title="Nagarjuna Sagar Water Sharing Disputes Spark Protests (2002-07)",
    desc="Farmers block canal pathways, protesting against diversion of upstream water to municipal zones during summers. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_irrigation_protests", "Initiate a special government commission to resolve irrigation_protests issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_irrigation_protests", "Demand that the government address irrigation_protests concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_irrigation_protests", "Propose a joint multi-party round table to build consensus on irrigation_protests.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-08
ITEMS_2001_2005.append(make_news(
    key="ap2001_2002_08_power_subsidy_demand",
    month="2002-08",
    title="Opposition Demands Free Power Supply for Agriculture (2002-08)",
    desc="Congress and Left parties organize assembly boycotts, demanding free electricity for drought-hit farmers. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics', 'rural'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("gov_action_power_subsidy_demand", "Initiate a special government commission to resolve power_subsidy_demand issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_power_subsidy_demand", "Demand that the government address power_subsidy_demand concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_power_subsidy_demand", "Propose a joint multi-party round table to build consensus on power_subsidy_demand.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-09
ITEMS_2001_2005.append(make_news(
    key="ap2001_2002_09_godavari_pushkaram",
    month="2002-09",
    title="Godavari Pushkaram Pilgrimage Draws Record Crowds (2002-09)",
    desc="Millions arrive for holy dips in Rajahmundry, prompting emergency crowd management and transport deployments. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['identity'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_godavari_pushkaram", "Initiate a special government commission to resolve godavari_pushkaram issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_godavari_pushkaram", "Demand that the government address godavari_pushkaram concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_godavari_pushkaram", "Propose a joint multi-party round table to build consensus on godavari_pushkaram.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-10
ITEMS_2001_2005.append(make_news(
    key="ap2001_2002_10_industrial_park",
    month="2002-10",
    title="Visakhapatnam Pharma City Land Acquisitions Approved (2002-10)",
    desc="The government clears land notices to construct a large pharmaceutical cluster in Vizag, drawing local objections. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['infrastructure', 'land_rights'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_industrial_park", "Initiate a special government commission to resolve industrial_park issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_industrial_park", "Demand that the government address industrial_park concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_industrial_park", "Propose a joint multi-party round table to build consensus on industrial_park.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-11
ITEMS_2001_2005.append(make_news(
    key="ap2001_2002_11_tribal_rights",
    month="2002-11",
    title="Agency Area Tribal Land Alienation Protests Erupt (2002-11)",
    desc="Tribal organizations in Adilabad protest against non-tribal encroachments on forest lands in scheduled areas. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['protest', 'identity'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_tribal_rights", "Initiate a special government commission to resolve tribal_rights issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_tribal_rights", "Demand that the government address tribal_rights concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_tribal_rights", "Propose a joint multi-party round table to build consensus on tribal_rights.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-12
ITEMS_2001_2005.append(make_news(
    key="ap2001_2002_12_cooperative_bank",
    month="2002-12",
    title="Cooperative Bank Scams Spark Depositor Outrage (2002-12)",
    desc="Audits expose illegal lending practices by board directors of urban cooperative banks, leading to customer panic. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['corruption', 'economy'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_cooperative_bank", "Initiate a special government commission to resolve cooperative_bank issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cooperative_bank", "Demand that the government address cooperative_bank concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cooperative_bank", "Propose a joint multi-party round table to build consensus on cooperative_bank.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-01
ITEMS_2001_2005.append(make_news(
    key="ap2001_2003_01_cyberabad_it",
    month="2003-01",
    title="Cyberabad Tech Hub Phase 1 Inaugurated in Hyderabad (2003-01)",
    desc="Chief Minister Chandrababu Naidu inaugurates new IT towers, pitching Hyderabad as an international technology hub. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_cyberabad_it", "Initiate a special government commission to resolve cyberabad_it issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cyberabad_it", "Demand that the government address cyberabad_it concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cyberabad_it", "Propose a joint multi-party round table to build consensus on cyberabad_it.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-02
ITEMS_2001_2005.append(make_news(
    key="ap2001_2003_02_farmer_suicides",
    month="2003-02",
    title="Rural Distress and Crop Failure Trigger Protests (2003-02)",
    desc="Rayalaseema and Telangana districts report severe cotton crop failure, sparking farmer protests and debt concerns. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['rural', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_farmer_suicides", "Initiate a special government commission to resolve farmer_suicides issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_farmer_suicides", "Demand that the government address farmer_suicides concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_farmer_suicides", "Propose a joint multi-party round table to build consensus on farmer_suicides.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-03
ITEMS_2001_2005.append(make_news(
    key="ap2001_2003_03_trs_formation",
    month="2003-03",
    title="K. Chandrashekar Rao Formulates TRS to Demand Telangana Statehood (2003-03)",
    desc="KCR resigns from TDP and forms the Telangana Rashtra Samithi (TRS), renewing the agitation for separate statehood. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_trs_formation", "Initiate a special government commission to resolve trs_formation issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_trs_formation", "Demand that the government address trs_formation concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_trs_formation", "Propose a joint multi-party round table to build consensus on trs_formation.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-04
ITEMS_2001_2005.append(make_news(
    key="ap2001_2003_04_naxal_attack",
    month="2003-04",
    title="Landmine Attack Targetting Politicians Triggers Alert (2003-04)",
    desc="Naxalite landmine attack in Chittoor district targets high-profile politicians, placing security forces on high alert. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['security_crisis'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("gov_action_naxal_attack", "Initiate a special government commission to resolve naxal_attack issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_naxal_attack", "Demand that the government address naxal_attack concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_naxal_attack", "Propose a joint multi-party round table to build consensus on naxal_attack.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-05
ITEMS_2001_2005.append(make_news(
    key="ap2001_2003_05_ysr_padayatra",
    month="2003-05",
    title="YSR Launches Historical Padayatra Across Andhra Districts (2003-05)",
    desc="Congress leader YS Rajasekhara Reddy starts a 1,500 km walkathon to connect with rural voters face-to-face. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_ysr_padayatra", "Initiate a special government commission to resolve ysr_padayatra issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_ysr_padayatra", "Demand that the government address ysr_padayatra concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_ysr_padayatra", "Propose a joint multi-party round table to build consensus on ysr_padayatra.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-06
ITEMS_2001_2005.append(make_news(
    key="ap2001_2003_06_microfinance_crisis",
    month="2003-06",
    title="Microfinance Debt Exploitation Sparks Regulatory Concerns (2003-06)",
    desc="Reports of high interest rates charged by private micro-lenders in rural areas prompt calls for government regulations. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['economy', 'rural'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_microfinance_crisis", "Initiate a special government commission to resolve microfinance_crisis issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_microfinance_crisis", "Demand that the government address microfinance_crisis concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_microfinance_crisis", "Propose a joint multi-party round table to build consensus on microfinance_crisis.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-07
ITEMS_2001_2005.append(make_news(
    key="ap2001_2003_07_irrigation_protests",
    month="2003-07",
    title="Nagarjuna Sagar Water Sharing Disputes Spark Protests (2003-07)",
    desc="Farmers block canal pathways, protesting against diversion of upstream water to municipal zones during summers. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_irrigation_protests", "Initiate a special government commission to resolve irrigation_protests issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_irrigation_protests", "Demand that the government address irrigation_protests concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_irrigation_protests", "Propose a joint multi-party round table to build consensus on irrigation_protests.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-08
ITEMS_2001_2005.append(make_news(
    key="ap2001_2003_08_power_subsidy_demand",
    month="2003-08",
    title="Opposition Demands Free Power Supply for Agriculture (2003-08)",
    desc="Congress and Left parties organize assembly boycotts, demanding free electricity for drought-hit farmers. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics', 'rural'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("gov_action_power_subsidy_demand", "Initiate a special government commission to resolve power_subsidy_demand issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_power_subsidy_demand", "Demand that the government address power_subsidy_demand concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_power_subsidy_demand", "Propose a joint multi-party round table to build consensus on power_subsidy_demand.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-09
ITEMS_2001_2005.append(make_news(
    key="ap2001_2003_09_godavari_pushkaram",
    month="2003-09",
    title="Godavari Pushkaram Pilgrimage Draws Record Crowds (2003-09)",
    desc="Millions arrive for holy dips in Rajahmundry, prompting emergency crowd management and transport deployments. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['identity'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_godavari_pushkaram", "Initiate a special government commission to resolve godavari_pushkaram issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_godavari_pushkaram", "Demand that the government address godavari_pushkaram concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_godavari_pushkaram", "Propose a joint multi-party round table to build consensus on godavari_pushkaram.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-10
ITEMS_2001_2005.append(make_news(
    key="ap2001_2003_10_industrial_park",
    month="2003-10",
    title="Visakhapatnam Pharma City Land Acquisitions Approved (2003-10)",
    desc="The government clears land notices to construct a large pharmaceutical cluster in Vizag, drawing local objections. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['infrastructure', 'land_rights'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_industrial_park", "Initiate a special government commission to resolve industrial_park issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_industrial_park", "Demand that the government address industrial_park concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_industrial_park", "Propose a joint multi-party round table to build consensus on industrial_park.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-11
ITEMS_2001_2005.append(make_news(
    key="ap2001_2003_11_tribal_rights",
    month="2003-11",
    title="Agency Area Tribal Land Alienation Protests Erupt (2003-11)",
    desc="Tribal organizations in Adilabad protest against non-tribal encroachments on forest lands in scheduled areas. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['protest', 'identity'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_tribal_rights", "Initiate a special government commission to resolve tribal_rights issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_tribal_rights", "Demand that the government address tribal_rights concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_tribal_rights", "Propose a joint multi-party round table to build consensus on tribal_rights.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-12
ITEMS_2001_2005.append(make_news(
    key="ap2001_2003_12_cooperative_bank",
    month="2003-12",
    title="Cooperative Bank Scams Spark Depositor Outrage (2003-12)",
    desc="Audits expose illegal lending practices by board directors of urban cooperative banks, leading to customer panic. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['corruption', 'economy'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_cooperative_bank", "Initiate a special government commission to resolve cooperative_bank issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cooperative_bank", "Demand that the government address cooperative_bank concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cooperative_bank", "Propose a joint multi-party round table to build consensus on cooperative_bank.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-01
ITEMS_2001_2005.append(make_news(
    key="ap2001_2004_01_cyberabad_it",
    month="2004-01",
    title="Cyberabad Tech Hub Phase 1 Inaugurated in Hyderabad (2004-01)",
    desc="Chief Minister Chandrababu Naidu inaugurates new IT towers, pitching Hyderabad as an international technology hub. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_cyberabad_it", "Initiate a special government commission to resolve cyberabad_it issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cyberabad_it", "Demand that the government address cyberabad_it concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cyberabad_it", "Propose a joint multi-party round table to build consensus on cyberabad_it.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-02
ITEMS_2001_2005.append(make_news(
    key="ap2001_2004_02_farmer_suicides",
    month="2004-02",
    title="Rural Distress and Crop Failure Trigger Protests (2004-02)",
    desc="Rayalaseema and Telangana districts report severe cotton crop failure, sparking farmer protests and debt concerns. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['rural', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_farmer_suicides", "Initiate a special government commission to resolve farmer_suicides issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_farmer_suicides", "Demand that the government address farmer_suicides concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_farmer_suicides", "Propose a joint multi-party round table to build consensus on farmer_suicides.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-03
ITEMS_2001_2005.append(make_news(
    key="ap2001_2004_03_trs_formation",
    month="2004-03",
    title="K. Chandrashekar Rao Formulates TRS to Demand Telangana Statehood (2004-03)",
    desc="KCR resigns from TDP and forms the Telangana Rashtra Samithi (TRS), renewing the agitation for separate statehood. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_trs_formation", "Initiate a special government commission to resolve trs_formation issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_trs_formation", "Demand that the government address trs_formation concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_trs_formation", "Propose a joint multi-party round table to build consensus on trs_formation.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-04
ITEMS_2001_2005.append(make_news(
    key="ap2001_2004_04_naxal_attack",
    month="2004-04",
    title="Landmine Attack Targetting Politicians Triggers Alert (2004-04)",
    desc="Naxalite landmine attack in Chittoor district targets high-profile politicians, placing security forces on high alert. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['security_crisis'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("gov_action_naxal_attack", "Initiate a special government commission to resolve naxal_attack issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_naxal_attack", "Demand that the government address naxal_attack concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_naxal_attack", "Propose a joint multi-party round table to build consensus on naxal_attack.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-05
ITEMS_2001_2005.append(make_news(
    key="ap2001_2004_05_ysr_padayatra",
    month="2004-05",
    title="YSR Launches Historical Padayatra Across Andhra Districts (2004-05)",
    desc="Congress leader YS Rajasekhara Reddy starts a 1,500 km walkathon to connect with rural voters face-to-face. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_ysr_padayatra", "Initiate a special government commission to resolve ysr_padayatra issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_ysr_padayatra", "Demand that the government address ysr_padayatra concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_ysr_padayatra", "Propose a joint multi-party round table to build consensus on ysr_padayatra.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-06
ITEMS_2001_2005.append(make_news(
    key="ap2001_2004_06_microfinance_crisis",
    month="2004-06",
    title="Microfinance Debt Exploitation Sparks Regulatory Concerns (2004-06)",
    desc="Reports of high interest rates charged by private micro-lenders in rural areas prompt calls for government regulations. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['economy', 'rural'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_microfinance_crisis", "Initiate a special government commission to resolve microfinance_crisis issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_microfinance_crisis", "Demand that the government address microfinance_crisis concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_microfinance_crisis", "Propose a joint multi-party round table to build consensus on microfinance_crisis.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-07
ITEMS_2001_2005.append(make_news(
    key="ap2001_2004_07_irrigation_protests",
    month="2004-07",
    title="Nagarjuna Sagar Water Sharing Disputes Spark Protests (2004-07)",
    desc="Farmers block canal pathways, protesting against diversion of upstream water to municipal zones during summers. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_irrigation_protests", "Initiate a special government commission to resolve irrigation_protests issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_irrigation_protests", "Demand that the government address irrigation_protests concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_irrigation_protests", "Propose a joint multi-party round table to build consensus on irrigation_protests.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-08
ITEMS_2001_2005.append(make_news(
    key="ap2001_2004_08_power_subsidy_demand",
    month="2004-08",
    title="Opposition Demands Free Power Supply for Agriculture (2004-08)",
    desc="Congress and Left parties organize assembly boycotts, demanding free electricity for drought-hit farmers. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics', 'rural'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("gov_action_power_subsidy_demand", "Initiate a special government commission to resolve power_subsidy_demand issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_power_subsidy_demand", "Demand that the government address power_subsidy_demand concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_power_subsidy_demand", "Propose a joint multi-party round table to build consensus on power_subsidy_demand.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-09
ITEMS_2001_2005.append(make_news(
    key="ap2001_2004_09_godavari_pushkaram",
    month="2004-09",
    title="Godavari Pushkaram Pilgrimage Draws Record Crowds (2004-09)",
    desc="Millions arrive for holy dips in Rajahmundry, prompting emergency crowd management and transport deployments. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['identity'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_godavari_pushkaram", "Initiate a special government commission to resolve godavari_pushkaram issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_godavari_pushkaram", "Demand that the government address godavari_pushkaram concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_godavari_pushkaram", "Propose a joint multi-party round table to build consensus on godavari_pushkaram.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-10
ITEMS_2001_2005.append(make_news(
    key="ap2001_2004_10_industrial_park",
    month="2004-10",
    title="Visakhapatnam Pharma City Land Acquisitions Approved (2004-10)",
    desc="The government clears land notices to construct a large pharmaceutical cluster in Vizag, drawing local objections. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['infrastructure', 'land_rights'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_industrial_park", "Initiate a special government commission to resolve industrial_park issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_industrial_park", "Demand that the government address industrial_park concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_industrial_park", "Propose a joint multi-party round table to build consensus on industrial_park.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-11
ITEMS_2001_2005.append(make_news(
    key="ap2001_2004_11_tribal_rights",
    month="2004-11",
    title="Agency Area Tribal Land Alienation Protests Erupt (2004-11)",
    desc="Tribal organizations in Adilabad protest against non-tribal encroachments on forest lands in scheduled areas. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['protest', 'identity'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_tribal_rights", "Initiate a special government commission to resolve tribal_rights issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_tribal_rights", "Demand that the government address tribal_rights concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_tribal_rights", "Propose a joint multi-party round table to build consensus on tribal_rights.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-12
ITEMS_2001_2005.append(make_news(
    key="ap2001_2004_12_cooperative_bank",
    month="2004-12",
    title="Cooperative Bank Scams Spark Depositor Outrage (2004-12)",
    desc="Audits expose illegal lending practices by board directors of urban cooperative banks, leading to customer panic. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['corruption', 'economy'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_cooperative_bank", "Initiate a special government commission to resolve cooperative_bank issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cooperative_bank", "Demand that the government address cooperative_bank concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cooperative_bank", "Propose a joint multi-party round table to build consensus on cooperative_bank.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-01
ITEMS_2001_2005.append(make_news(
    key="ap2001_2005_01_cyberabad_it",
    month="2005-01",
    title="Cyberabad Tech Hub Phase 1 Inaugurated in Hyderabad (2005-01)",
    desc="Chief Minister Chandrababu Naidu inaugurates new IT towers, pitching Hyderabad as an international technology hub. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_cyberabad_it", "Initiate a special government commission to resolve cyberabad_it issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cyberabad_it", "Demand that the government address cyberabad_it concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cyberabad_it", "Propose a joint multi-party round table to build consensus on cyberabad_it.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-02
ITEMS_2001_2005.append(make_news(
    key="ap2001_2005_02_farmer_suicides",
    month="2005-02",
    title="Rural Distress and Crop Failure Trigger Protests (2005-02)",
    desc="Rayalaseema and Telangana districts report severe cotton crop failure, sparking farmer protests and debt concerns. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['rural', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_farmer_suicides", "Initiate a special government commission to resolve farmer_suicides issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_farmer_suicides", "Demand that the government address farmer_suicides concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_farmer_suicides", "Propose a joint multi-party round table to build consensus on farmer_suicides.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-03
ITEMS_2001_2005.append(make_news(
    key="ap2001_2005_03_trs_formation",
    month="2005-03",
    title="K. Chandrashekar Rao Formulates TRS to Demand Telangana Statehood (2005-03)",
    desc="KCR resigns from TDP and forms the Telangana Rashtra Samithi (TRS), renewing the agitation for separate statehood. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_trs_formation", "Initiate a special government commission to resolve trs_formation issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_trs_formation", "Demand that the government address trs_formation concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_trs_formation", "Propose a joint multi-party round table to build consensus on trs_formation.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-04
ITEMS_2001_2005.append(make_news(
    key="ap2001_2005_04_naxal_attack",
    month="2005-04",
    title="Landmine Attack Targetting Politicians Triggers Alert (2005-04)",
    desc="Naxalite landmine attack in Chittoor district targets high-profile politicians, placing security forces on high alert. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['security_crisis'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("gov_action_naxal_attack", "Initiate a special government commission to resolve naxal_attack issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_naxal_attack", "Demand that the government address naxal_attack concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_naxal_attack", "Propose a joint multi-party round table to build consensus on naxal_attack.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-05
ITEMS_2001_2005.append(make_news(
    key="ap2001_2005_05_ysr_padayatra",
    month="2005-05",
    title="YSR Launches Historical Padayatra Across Andhra Districts (2005-05)",
    desc="Congress leader YS Rajasekhara Reddy starts a 1,500 km walkathon to connect with rural voters face-to-face. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_ysr_padayatra", "Initiate a special government commission to resolve ysr_padayatra issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_ysr_padayatra", "Demand that the government address ysr_padayatra concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_ysr_padayatra", "Propose a joint multi-party round table to build consensus on ysr_padayatra.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-06
ITEMS_2001_2005.append(make_news(
    key="ap2001_2005_06_microfinance_crisis",
    month="2005-06",
    title="Microfinance Debt Exploitation Sparks Regulatory Concerns (2005-06)",
    desc="Reports of high interest rates charged by private micro-lenders in rural areas prompt calls for government regulations. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['economy', 'rural'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_microfinance_crisis", "Initiate a special government commission to resolve microfinance_crisis issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_microfinance_crisis", "Demand that the government address microfinance_crisis concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_microfinance_crisis", "Propose a joint multi-party round table to build consensus on microfinance_crisis.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-07
ITEMS_2001_2005.append(make_news(
    key="ap2001_2005_07_irrigation_protests",
    month="2005-07",
    title="Nagarjuna Sagar Water Sharing Disputes Spark Protests (2005-07)",
    desc="Farmers block canal pathways, protesting against diversion of upstream water to municipal zones during summers. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_irrigation_protests", "Initiate a special government commission to resolve irrigation_protests issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_irrigation_protests", "Demand that the government address irrigation_protests concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_irrigation_protests", "Propose a joint multi-party round table to build consensus on irrigation_protests.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-08
ITEMS_2001_2005.append(make_news(
    key="ap2001_2005_08_power_subsidy_demand",
    month="2005-08",
    title="Opposition Demands Free Power Supply for Agriculture (2005-08)",
    desc="Congress and Left parties organize assembly boycotts, demanding free electricity for drought-hit farmers. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics', 'rural'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("gov_action_power_subsidy_demand", "Initiate a special government commission to resolve power_subsidy_demand issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_power_subsidy_demand", "Demand that the government address power_subsidy_demand concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_power_subsidy_demand", "Propose a joint multi-party round table to build consensus on power_subsidy_demand.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-09
ITEMS_2001_2005.append(make_news(
    key="ap2001_2005_09_godavari_pushkaram",
    month="2005-09",
    title="Godavari Pushkaram Pilgrimage Draws Record Crowds (2005-09)",
    desc="Millions arrive for holy dips in Rajahmundry, prompting emergency crowd management and transport deployments. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['identity'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_godavari_pushkaram", "Initiate a special government commission to resolve godavari_pushkaram issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_godavari_pushkaram", "Demand that the government address godavari_pushkaram concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_godavari_pushkaram", "Propose a joint multi-party round table to build consensus on godavari_pushkaram.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-10
ITEMS_2001_2005.append(make_news(
    key="ap2001_2005_10_industrial_park",
    month="2005-10",
    title="Visakhapatnam Pharma City Land Acquisitions Approved (2005-10)",
    desc="The government clears land notices to construct a large pharmaceutical cluster in Vizag, drawing local objections. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['infrastructure', 'land_rights'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_industrial_park", "Initiate a special government commission to resolve industrial_park issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_industrial_park", "Demand that the government address industrial_park concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_industrial_park", "Propose a joint multi-party round table to build consensus on industrial_park.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-11
ITEMS_2001_2005.append(make_news(
    key="ap2001_2005_11_tribal_rights",
    month="2005-11",
    title="Agency Area Tribal Land Alienation Protests Erupt (2005-11)",
    desc="Tribal organizations in Adilabad protest against non-tribal encroachments on forest lands in scheduled areas. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['protest', 'identity'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_tribal_rights", "Initiate a special government commission to resolve tribal_rights issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_tribal_rights", "Demand that the government address tribal_rights concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_tribal_rights", "Propose a joint multi-party round table to build consensus on tribal_rights.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-12
ITEMS_2001_2005.append(make_news(
    key="ap2001_2005_12_cooperative_bank",
    month="2005-12",
    title="Cooperative Bank Scams Spark Depositor Outrage (2005-12)",
    desc="Audits expose illegal lending practices by board directors of urban cooperative banks, leading to customer panic. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['corruption', 'economy'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_cooperative_bank", "Initiate a special government commission to resolve cooperative_bank issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cooperative_bank", "Demand that the government address cooperative_bank concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cooperative_bank", "Propose a joint multi-party round table to build consensus on cooperative_bank.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

