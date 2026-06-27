from helper import reaction, no_comment, make_news, eff, risk

ITEMS_2006_2010 = []

# 2006-01
ITEMS_2006_2010.append(make_news(
    key="ga2006_2006_01_casinos_mandovi",
    month="2006-01",
    title="Floating Casinos on Mandovi River Draw Licensing Debates (2006-01)",
    desc="The government issues new offshore casino licenses on the Mandovi river, drawing protests from civic groups. In Goa, this monthly event shapes key regional debates.",
    tags=['tourism', 'economy'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_casinos_mandovi", "Initiate a special government commission to resolve casinos_mandovi issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_casinos_mandovi", "Demand that the government address casinos_mandovi concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_casinos_mandovi", "Propose a joint multi-party round table to build consensus on casinos_mandovi.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-02
ITEMS_2006_2010.append(make_news(
    key="ga2006_2006_02_mining_boom",
    month="2006-02",
    title="Bicholim Iron Ore Mining Boom Raises Dust Pollution Concerns (2006-02)",
    desc="Heavy truck corridors transporting iron ore trigger village blockades demanding pollution control tarpaulins. In Goa, this monthly event shapes key regional debates.",
    tags=['environment', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_mining_boom", "Initiate a special government commission to resolve mining_boom issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mining_boom", "Demand that the government address mining_boom concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mining_boom", "Propose a joint multi-party round table to build consensus on mining_boom.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-03
ITEMS_2006_2010.append(make_news(
    key="ga2006_2006_03_political_defections",
    month="2006-03",
    title="Cabinet Instability Threats Amid Revolving-DoorDefections (2006-03)",
    desc="Goa's coalition government faces no-confidence threats as MLAs swap party alignments over portfolio demands. In Goa, this monthly event shapes key regional debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_political_defections", "Initiate a special government commission to resolve political_defections issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_political_defections", "Demand that the government address political_defections concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_political_defections", "Propose a joint multi-party round table to build consensus on political_defections.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-04
ITEMS_2006_2010.append(make_news(
    key="ga2006_2006_04_mega_resorts",
    month="2006-04",
    title="Resort Construction in Morjim Sparks Local Wildlife Outrage (2006-04)",
    desc="Environmentalists protest beach resort developments, citing destruction of Olive Ridley turtle nesting grounds. In Goa, this monthly event shapes key regional debates.",
    tags=['environment', 'tourism'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_mega_resorts", "Initiate a special government commission to resolve mega_resorts issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mega_resorts", "Demand that the government address mega_resorts concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mega_resorts", "Propose a joint multi-party round table to build consensus on mega_resorts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-05
ITEMS_2006_2010.append(make_news(
    key="ga2006_2006_05_infrastructure_mopa",
    month="2006-05",
    title="Mopa Greenfield Airport Land Acquisition Cleared (2006-05)",
    desc="The cabinet approves land acquisition notifications for the proposed greenfield airport at Mopa in North Goa. In Goa, this monthly event shapes key regional debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_infrastructure_mopa", "Initiate a special government commission to resolve infrastructure_mopa issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_infrastructure_mopa", "Demand that the government address infrastructure_mopa concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_infrastructure_mopa", "Propose a joint multi-party round table to build consensus on infrastructure_mopa.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-06
ITEMS_2006_2010.append(make_news(
    key="ga2006_2006_06_garbage_sonsodo_update",
    month="2006-06",
    title="Sonsodo Treatment Plant Delays Cause Margao Protests (2006-06)",
    desc="Margao municipal council faces public wrath as the solid waste treatment plant at Sonsodo fails to start. In Goa, this monthly event shapes key regional debates.",
    tags=['protest', 'environment'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_garbage_sonsodo_update", "Initiate a special government commission to resolve garbage_sonsodo_update issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_garbage_sonsodo_update", "Demand that the government address garbage_sonsodo_update concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_garbage_sonsodo_update", "Propose a joint multi-party round table to build consensus on garbage_sonsodo_update.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-07
ITEMS_2006_2010.append(make_news(
    key="ga2006_2006_07_assembly_elections",
    month="2006-07",
    title="Assembly Campaigns Focus on Regional Plan 2021 Controversies (2006-07)",
    desc="Political parties debate land-use zoning details under Regional Plan 2021, prompting massive protest rallies. In Goa, this monthly event shapes key regional debates.",
    tags=['election', 'politics'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("gov_action_assembly_elections", "Initiate a special government commission to resolve assembly_elections issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_assembly_elections", "Demand that the government address assembly_elections concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_assembly_elections", "Propose a joint multi-party round table to build consensus on assembly_elections.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-08
ITEMS_2006_2010.append(make_news(
    key="ga2006_2006_08_konkani_marathi",
    month="2006-08",
    title="Language Medium of Instruction (MOI) Debates Heat Up (2006-08)",
    desc="Primary school parents and political bodies clash over state grants for Konkani and Marathi medium schools. In Goa, this monthly event shapes key regional debates.",
    tags=['identity', 'politics'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_konkani_marathi", "Initiate a special government commission to resolve konkani_marathi issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_konkani_marathi", "Demand that the government address konkani_marathi concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_konkani_marathi", "Propose a joint multi-party round table to build consensus on konkani_marathi.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-09
ITEMS_2006_2010.append(make_news(
    key="ga2006_2006_09_fishermen_trawlers",
    month="2006-09",
    title="Coast Guard Seizes Trawlers Violating Monsoon Fishing Ban (2006-09)",
    desc="State enforces the mandatory 61-day monsoon breeding fishing ban, drawing criticism from commercial trawler owners. In Goa, this monthly event shapes key regional debates.",
    tags=['protest', 'economy'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_fishermen_trawlers", "Initiate a special government commission to resolve fishermen_trawlers issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_fishermen_trawlers", "Demand that the government address fishermen_trawlers concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_fishermen_trawlers", "Propose a joint multi-party round table to build consensus on fishermen_trawlers.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-10
ITEMS_2006_2010.append(make_news(
    key="ga2006_2006_10_tourist_scam",
    month="2006-10",
    title="Foreign National Land Buyouts Trigger Enforcement Inquiries (2006-10)",
    desc="The Enforcement Directorate probes illegal land purchases by foreign nationals in coastal villages like Calangute. In Goa, this monthly event shapes key regional debates.",
    tags=['governance', 'corruption'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_tourist_scam", "Initiate a special government commission to resolve tourist_scam issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_tourist_scam", "Demand that the government address tourist_scam concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_tourist_scam", "Propose a joint multi-party round table to build consensus on tourist_scam.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-11
ITEMS_2006_2010.append(make_news(
    key="ga2006_2006_11_nh17_widening",
    month="2006-11",
    title="National Highway 17 Widening Protests Gather Strength (2006-11)",
    desc="Local business groups and residents block survey works, protesting proposed demolition of heritage houses. In Goa, this monthly event shapes key regional debates.",
    tags=['infrastructure', 'protest'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_nh17_widening", "Initiate a special government commission to resolve nh17_widening issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_nh17_widening", "Demand that the government address nh17_widening concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_nh17_widening", "Propose a joint multi-party round table to build consensus on nh17_widening.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-12
ITEMS_2006_2010.append(make_news(
    key="ga2006_2006_12_eco_tourism",
    month="2006-12",
    title="Western Ghats Eco-Tourism Projects Approved (2006-12)",
    desc="The forest department clears low-impact resort guidelines for Netravali and Cotigao wildlife sanctuaries. In Goa, this monthly event shapes key regional debates.",
    tags=['environment', 'tourism'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_eco_tourism", "Initiate a special government commission to resolve eco_tourism issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_eco_tourism", "Demand that the government address eco_tourism concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_eco_tourism", "Propose a joint multi-party round table to build consensus on eco_tourism.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-01
ITEMS_2006_2010.append(make_news(
    key="ga2006_2007_01_casinos_mandovi",
    month="2007-01",
    title="Floating Casinos on Mandovi River Draw Licensing Debates (2007-01)",
    desc="The government issues new offshore casino licenses on the Mandovi river, drawing protests from civic groups. In Goa, this monthly event shapes key regional debates.",
    tags=['tourism', 'economy'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_casinos_mandovi", "Initiate a special government commission to resolve casinos_mandovi issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_casinos_mandovi", "Demand that the government address casinos_mandovi concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_casinos_mandovi", "Propose a joint multi-party round table to build consensus on casinos_mandovi.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-02
ITEMS_2006_2010.append(make_news(
    key="ga2006_2007_02_mining_boom",
    month="2007-02",
    title="Bicholim Iron Ore Mining Boom Raises Dust Pollution Concerns (2007-02)",
    desc="Heavy truck corridors transporting iron ore trigger village blockades demanding pollution control tarpaulins. In Goa, this monthly event shapes key regional debates.",
    tags=['environment', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_mining_boom", "Initiate a special government commission to resolve mining_boom issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mining_boom", "Demand that the government address mining_boom concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mining_boom", "Propose a joint multi-party round table to build consensus on mining_boom.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-03
ITEMS_2006_2010.append(make_news(
    key="ga2006_2007_03_political_defections",
    month="2007-03",
    title="Cabinet Instability Threats Amid Revolving-DoorDefections (2007-03)",
    desc="Goa's coalition government faces no-confidence threats as MLAs swap party alignments over portfolio demands. In Goa, this monthly event shapes key regional debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_political_defections", "Initiate a special government commission to resolve political_defections issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_political_defections", "Demand that the government address political_defections concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_political_defections", "Propose a joint multi-party round table to build consensus on political_defections.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-04
ITEMS_2006_2010.append(make_news(
    key="ga2006_2007_04_mega_resorts",
    month="2007-04",
    title="Resort Construction in Morjim Sparks Local Wildlife Outrage (2007-04)",
    desc="Environmentalists protest beach resort developments, citing destruction of Olive Ridley turtle nesting grounds. In Goa, this monthly event shapes key regional debates.",
    tags=['environment', 'tourism'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_mega_resorts", "Initiate a special government commission to resolve mega_resorts issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mega_resorts", "Demand that the government address mega_resorts concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mega_resorts", "Propose a joint multi-party round table to build consensus on mega_resorts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-05
ITEMS_2006_2010.append(make_news(
    key="ga2006_2007_05_infrastructure_mopa",
    month="2007-05",
    title="Mopa Greenfield Airport Land Acquisition Cleared (2007-05)",
    desc="The cabinet approves land acquisition notifications for the proposed greenfield airport at Mopa in North Goa. In Goa, this monthly event shapes key regional debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_infrastructure_mopa", "Initiate a special government commission to resolve infrastructure_mopa issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_infrastructure_mopa", "Demand that the government address infrastructure_mopa concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_infrastructure_mopa", "Propose a joint multi-party round table to build consensus on infrastructure_mopa.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-06
ITEMS_2006_2010.append(make_news(
    key="ga2006_2007_06_garbage_sonsodo_update",
    month="2007-06",
    title="Sonsodo Treatment Plant Delays Cause Margao Protests (2007-06)",
    desc="Margao municipal council faces public wrath as the solid waste treatment plant at Sonsodo fails to start. In Goa, this monthly event shapes key regional debates.",
    tags=['protest', 'environment'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_garbage_sonsodo_update", "Initiate a special government commission to resolve garbage_sonsodo_update issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_garbage_sonsodo_update", "Demand that the government address garbage_sonsodo_update concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_garbage_sonsodo_update", "Propose a joint multi-party round table to build consensus on garbage_sonsodo_update.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-07
ITEMS_2006_2010.append(make_news(
    key="ga2006_2007_07_assembly_elections",
    month="2007-07",
    title="Assembly Campaigns Focus on Regional Plan 2021 Controversies (2007-07)",
    desc="Political parties debate land-use zoning details under Regional Plan 2021, prompting massive protest rallies. In Goa, this monthly event shapes key regional debates.",
    tags=['election', 'politics'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("gov_action_assembly_elections", "Initiate a special government commission to resolve assembly_elections issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_assembly_elections", "Demand that the government address assembly_elections concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_assembly_elections", "Propose a joint multi-party round table to build consensus on assembly_elections.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-08
ITEMS_2006_2010.append(make_news(
    key="ga2006_2007_08_konkani_marathi",
    month="2007-08",
    title="Language Medium of Instruction (MOI) Debates Heat Up (2007-08)",
    desc="Primary school parents and political bodies clash over state grants for Konkani and Marathi medium schools. In Goa, this monthly event shapes key regional debates.",
    tags=['identity', 'politics'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_konkani_marathi", "Initiate a special government commission to resolve konkani_marathi issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_konkani_marathi", "Demand that the government address konkani_marathi concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_konkani_marathi", "Propose a joint multi-party round table to build consensus on konkani_marathi.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-09
ITEMS_2006_2010.append(make_news(
    key="ga2006_2007_09_fishermen_trawlers",
    month="2007-09",
    title="Coast Guard Seizes Trawlers Violating Monsoon Fishing Ban (2007-09)",
    desc="State enforces the mandatory 61-day monsoon breeding fishing ban, drawing criticism from commercial trawler owners. In Goa, this monthly event shapes key regional debates.",
    tags=['protest', 'economy'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_fishermen_trawlers", "Initiate a special government commission to resolve fishermen_trawlers issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_fishermen_trawlers", "Demand that the government address fishermen_trawlers concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_fishermen_trawlers", "Propose a joint multi-party round table to build consensus on fishermen_trawlers.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-10
ITEMS_2006_2010.append(make_news(
    key="ga2006_2007_10_tourist_scam",
    month="2007-10",
    title="Foreign National Land Buyouts Trigger Enforcement Inquiries (2007-10)",
    desc="The Enforcement Directorate probes illegal land purchases by foreign nationals in coastal villages like Calangute. In Goa, this monthly event shapes key regional debates.",
    tags=['governance', 'corruption'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_tourist_scam", "Initiate a special government commission to resolve tourist_scam issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_tourist_scam", "Demand that the government address tourist_scam concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_tourist_scam", "Propose a joint multi-party round table to build consensus on tourist_scam.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-11
ITEMS_2006_2010.append(make_news(
    key="ga2006_2007_11_nh17_widening",
    month="2007-11",
    title="National Highway 17 Widening Protests Gather Strength (2007-11)",
    desc="Local business groups and residents block survey works, protesting proposed demolition of heritage houses. In Goa, this monthly event shapes key regional debates.",
    tags=['infrastructure', 'protest'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_nh17_widening", "Initiate a special government commission to resolve nh17_widening issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_nh17_widening", "Demand that the government address nh17_widening concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_nh17_widening", "Propose a joint multi-party round table to build consensus on nh17_widening.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-12
ITEMS_2006_2010.append(make_news(
    key="ga2006_2007_12_eco_tourism",
    month="2007-12",
    title="Western Ghats Eco-Tourism Projects Approved (2007-12)",
    desc="The forest department clears low-impact resort guidelines for Netravali and Cotigao wildlife sanctuaries. In Goa, this monthly event shapes key regional debates.",
    tags=['environment', 'tourism'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_eco_tourism", "Initiate a special government commission to resolve eco_tourism issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_eco_tourism", "Demand that the government address eco_tourism concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_eco_tourism", "Propose a joint multi-party round table to build consensus on eco_tourism.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-01
ITEMS_2006_2010.append(make_news(
    key="ga2006_2008_01_casinos_mandovi",
    month="2008-01",
    title="Floating Casinos on Mandovi River Draw Licensing Debates (2008-01)",
    desc="The government issues new offshore casino licenses on the Mandovi river, drawing protests from civic groups. In Goa, this monthly event shapes key regional debates.",
    tags=['tourism', 'economy'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_casinos_mandovi", "Initiate a special government commission to resolve casinos_mandovi issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_casinos_mandovi", "Demand that the government address casinos_mandovi concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_casinos_mandovi", "Propose a joint multi-party round table to build consensus on casinos_mandovi.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-02
ITEMS_2006_2010.append(make_news(
    key="ga2006_2008_02_mining_boom",
    month="2008-02",
    title="Bicholim Iron Ore Mining Boom Raises Dust Pollution Concerns (2008-02)",
    desc="Heavy truck corridors transporting iron ore trigger village blockades demanding pollution control tarpaulins. In Goa, this monthly event shapes key regional debates.",
    tags=['environment', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_mining_boom", "Initiate a special government commission to resolve mining_boom issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mining_boom", "Demand that the government address mining_boom concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mining_boom", "Propose a joint multi-party round table to build consensus on mining_boom.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-03
ITEMS_2006_2010.append(make_news(
    key="ga2006_2008_03_political_defections",
    month="2008-03",
    title="Cabinet Instability Threats Amid Revolving-DoorDefections (2008-03)",
    desc="Goa's coalition government faces no-confidence threats as MLAs swap party alignments over portfolio demands. In Goa, this monthly event shapes key regional debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_political_defections", "Initiate a special government commission to resolve political_defections issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_political_defections", "Demand that the government address political_defections concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_political_defections", "Propose a joint multi-party round table to build consensus on political_defections.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-04
ITEMS_2006_2010.append(make_news(
    key="ga2006_2008_04_mega_resorts",
    month="2008-04",
    title="Resort Construction in Morjim Sparks Local Wildlife Outrage (2008-04)",
    desc="Environmentalists protest beach resort developments, citing destruction of Olive Ridley turtle nesting grounds. In Goa, this monthly event shapes key regional debates.",
    tags=['environment', 'tourism'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_mega_resorts", "Initiate a special government commission to resolve mega_resorts issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mega_resorts", "Demand that the government address mega_resorts concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mega_resorts", "Propose a joint multi-party round table to build consensus on mega_resorts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-05
ITEMS_2006_2010.append(make_news(
    key="ga2006_2008_05_infrastructure_mopa",
    month="2008-05",
    title="Mopa Greenfield Airport Land Acquisition Cleared (2008-05)",
    desc="The cabinet approves land acquisition notifications for the proposed greenfield airport at Mopa in North Goa. In Goa, this monthly event shapes key regional debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_infrastructure_mopa", "Initiate a special government commission to resolve infrastructure_mopa issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_infrastructure_mopa", "Demand that the government address infrastructure_mopa concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_infrastructure_mopa", "Propose a joint multi-party round table to build consensus on infrastructure_mopa.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-06
ITEMS_2006_2010.append(make_news(
    key="ga2006_2008_06_garbage_sonsodo_update",
    month="2008-06",
    title="Sonsodo Treatment Plant Delays Cause Margao Protests (2008-06)",
    desc="Margao municipal council faces public wrath as the solid waste treatment plant at Sonsodo fails to start. In Goa, this monthly event shapes key regional debates.",
    tags=['protest', 'environment'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_garbage_sonsodo_update", "Initiate a special government commission to resolve garbage_sonsodo_update issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_garbage_sonsodo_update", "Demand that the government address garbage_sonsodo_update concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_garbage_sonsodo_update", "Propose a joint multi-party round table to build consensus on garbage_sonsodo_update.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-07
ITEMS_2006_2010.append(make_news(
    key="ga2006_2008_07_assembly_elections",
    month="2008-07",
    title="Assembly Campaigns Focus on Regional Plan 2021 Controversies (2008-07)",
    desc="Political parties debate land-use zoning details under Regional Plan 2021, prompting massive protest rallies. In Goa, this monthly event shapes key regional debates.",
    tags=['election', 'politics'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("gov_action_assembly_elections", "Initiate a special government commission to resolve assembly_elections issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_assembly_elections", "Demand that the government address assembly_elections concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_assembly_elections", "Propose a joint multi-party round table to build consensus on assembly_elections.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-08
ITEMS_2006_2010.append(make_news(
    key="ga2006_2008_08_konkani_marathi",
    month="2008-08",
    title="Language Medium of Instruction (MOI) Debates Heat Up (2008-08)",
    desc="Primary school parents and political bodies clash over state grants for Konkani and Marathi medium schools. In Goa, this monthly event shapes key regional debates.",
    tags=['identity', 'politics'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_konkani_marathi", "Initiate a special government commission to resolve konkani_marathi issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_konkani_marathi", "Demand that the government address konkani_marathi concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_konkani_marathi", "Propose a joint multi-party round table to build consensus on konkani_marathi.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-09
ITEMS_2006_2010.append(make_news(
    key="ga2006_2008_09_fishermen_trawlers",
    month="2008-09",
    title="Coast Guard Seizes Trawlers Violating Monsoon Fishing Ban (2008-09)",
    desc="State enforces the mandatory 61-day monsoon breeding fishing ban, drawing criticism from commercial trawler owners. In Goa, this monthly event shapes key regional debates.",
    tags=['protest', 'economy'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_fishermen_trawlers", "Initiate a special government commission to resolve fishermen_trawlers issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_fishermen_trawlers", "Demand that the government address fishermen_trawlers concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_fishermen_trawlers", "Propose a joint multi-party round table to build consensus on fishermen_trawlers.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-10
ITEMS_2006_2010.append(make_news(
    key="ga2006_2008_10_tourist_scam",
    month="2008-10",
    title="Foreign National Land Buyouts Trigger Enforcement Inquiries (2008-10)",
    desc="The Enforcement Directorate probes illegal land purchases by foreign nationals in coastal villages like Calangute. In Goa, this monthly event shapes key regional debates.",
    tags=['governance', 'corruption'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_tourist_scam", "Initiate a special government commission to resolve tourist_scam issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_tourist_scam", "Demand that the government address tourist_scam concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_tourist_scam", "Propose a joint multi-party round table to build consensus on tourist_scam.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-11
ITEMS_2006_2010.append(make_news(
    key="ga2006_2008_11_nh17_widening",
    month="2008-11",
    title="National Highway 17 Widening Protests Gather Strength (2008-11)",
    desc="Local business groups and residents block survey works, protesting proposed demolition of heritage houses. In Goa, this monthly event shapes key regional debates.",
    tags=['infrastructure', 'protest'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_nh17_widening", "Initiate a special government commission to resolve nh17_widening issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_nh17_widening", "Demand that the government address nh17_widening concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_nh17_widening", "Propose a joint multi-party round table to build consensus on nh17_widening.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-12
ITEMS_2006_2010.append(make_news(
    key="ga2006_2008_12_eco_tourism",
    month="2008-12",
    title="Western Ghats Eco-Tourism Projects Approved (2008-12)",
    desc="The forest department clears low-impact resort guidelines for Netravali and Cotigao wildlife sanctuaries. In Goa, this monthly event shapes key regional debates.",
    tags=['environment', 'tourism'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_eco_tourism", "Initiate a special government commission to resolve eco_tourism issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_eco_tourism", "Demand that the government address eco_tourism concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_eco_tourism", "Propose a joint multi-party round table to build consensus on eco_tourism.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-01
ITEMS_2006_2010.append(make_news(
    key="ga2006_2009_01_casinos_mandovi",
    month="2009-01",
    title="Floating Casinos on Mandovi River Draw Licensing Debates (2009-01)",
    desc="The government issues new offshore casino licenses on the Mandovi river, drawing protests from civic groups. In Goa, this monthly event shapes key regional debates.",
    tags=['tourism', 'economy'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_casinos_mandovi", "Initiate a special government commission to resolve casinos_mandovi issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_casinos_mandovi", "Demand that the government address casinos_mandovi concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_casinos_mandovi", "Propose a joint multi-party round table to build consensus on casinos_mandovi.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-02
ITEMS_2006_2010.append(make_news(
    key="ga2006_2009_02_mining_boom",
    month="2009-02",
    title="Bicholim Iron Ore Mining Boom Raises Dust Pollution Concerns (2009-02)",
    desc="Heavy truck corridors transporting iron ore trigger village blockades demanding pollution control tarpaulins. In Goa, this monthly event shapes key regional debates.",
    tags=['environment', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_mining_boom", "Initiate a special government commission to resolve mining_boom issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mining_boom", "Demand that the government address mining_boom concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mining_boom", "Propose a joint multi-party round table to build consensus on mining_boom.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-03
ITEMS_2006_2010.append(make_news(
    key="ga2006_2009_03_political_defections",
    month="2009-03",
    title="Cabinet Instability Threats Amid Revolving-DoorDefections (2009-03)",
    desc="Goa's coalition government faces no-confidence threats as MLAs swap party alignments over portfolio demands. In Goa, this monthly event shapes key regional debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_political_defections", "Initiate a special government commission to resolve political_defections issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_political_defections", "Demand that the government address political_defections concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_political_defections", "Propose a joint multi-party round table to build consensus on political_defections.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-04
ITEMS_2006_2010.append(make_news(
    key="ga2006_2009_04_mega_resorts",
    month="2009-04",
    title="Resort Construction in Morjim Sparks Local Wildlife Outrage (2009-04)",
    desc="Environmentalists protest beach resort developments, citing destruction of Olive Ridley turtle nesting grounds. In Goa, this monthly event shapes key regional debates.",
    tags=['environment', 'tourism'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_mega_resorts", "Initiate a special government commission to resolve mega_resorts issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mega_resorts", "Demand that the government address mega_resorts concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mega_resorts", "Propose a joint multi-party round table to build consensus on mega_resorts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-05
ITEMS_2006_2010.append(make_news(
    key="ga2006_2009_05_infrastructure_mopa",
    month="2009-05",
    title="Mopa Greenfield Airport Land Acquisition Cleared (2009-05)",
    desc="The cabinet approves land acquisition notifications for the proposed greenfield airport at Mopa in North Goa. In Goa, this monthly event shapes key regional debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_infrastructure_mopa", "Initiate a special government commission to resolve infrastructure_mopa issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_infrastructure_mopa", "Demand that the government address infrastructure_mopa concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_infrastructure_mopa", "Propose a joint multi-party round table to build consensus on infrastructure_mopa.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-06
ITEMS_2006_2010.append(make_news(
    key="ga2006_2009_06_garbage_sonsodo_update",
    month="2009-06",
    title="Sonsodo Treatment Plant Delays Cause Margao Protests (2009-06)",
    desc="Margao municipal council faces public wrath as the solid waste treatment plant at Sonsodo fails to start. In Goa, this monthly event shapes key regional debates.",
    tags=['protest', 'environment'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_garbage_sonsodo_update", "Initiate a special government commission to resolve garbage_sonsodo_update issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_garbage_sonsodo_update", "Demand that the government address garbage_sonsodo_update concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_garbage_sonsodo_update", "Propose a joint multi-party round table to build consensus on garbage_sonsodo_update.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-07
ITEMS_2006_2010.append(make_news(
    key="ga2006_2009_07_assembly_elections",
    month="2009-07",
    title="Assembly Campaigns Focus on Regional Plan 2021 Controversies (2009-07)",
    desc="Political parties debate land-use zoning details under Regional Plan 2021, prompting massive protest rallies. In Goa, this monthly event shapes key regional debates.",
    tags=['election', 'politics'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("gov_action_assembly_elections", "Initiate a special government commission to resolve assembly_elections issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_assembly_elections", "Demand that the government address assembly_elections concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_assembly_elections", "Propose a joint multi-party round table to build consensus on assembly_elections.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-08
ITEMS_2006_2010.append(make_news(
    key="ga2006_2009_08_konkani_marathi",
    month="2009-08",
    title="Language Medium of Instruction (MOI) Debates Heat Up (2009-08)",
    desc="Primary school parents and political bodies clash over state grants for Konkani and Marathi medium schools. In Goa, this monthly event shapes key regional debates.",
    tags=['identity', 'politics'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_konkani_marathi", "Initiate a special government commission to resolve konkani_marathi issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_konkani_marathi", "Demand that the government address konkani_marathi concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_konkani_marathi", "Propose a joint multi-party round table to build consensus on konkani_marathi.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-09
ITEMS_2006_2010.append(make_news(
    key="ga2006_2009_09_fishermen_trawlers",
    month="2009-09",
    title="Coast Guard Seizes Trawlers Violating Monsoon Fishing Ban (2009-09)",
    desc="State enforces the mandatory 61-day monsoon breeding fishing ban, drawing criticism from commercial trawler owners. In Goa, this monthly event shapes key regional debates.",
    tags=['protest', 'economy'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_fishermen_trawlers", "Initiate a special government commission to resolve fishermen_trawlers issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_fishermen_trawlers", "Demand that the government address fishermen_trawlers concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_fishermen_trawlers", "Propose a joint multi-party round table to build consensus on fishermen_trawlers.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-10
ITEMS_2006_2010.append(make_news(
    key="ga2006_2009_10_tourist_scam",
    month="2009-10",
    title="Foreign National Land Buyouts Trigger Enforcement Inquiries (2009-10)",
    desc="The Enforcement Directorate probes illegal land purchases by foreign nationals in coastal villages like Calangute. In Goa, this monthly event shapes key regional debates.",
    tags=['governance', 'corruption'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_tourist_scam", "Initiate a special government commission to resolve tourist_scam issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_tourist_scam", "Demand that the government address tourist_scam concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_tourist_scam", "Propose a joint multi-party round table to build consensus on tourist_scam.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-11
ITEMS_2006_2010.append(make_news(
    key="ga2006_2009_11_nh17_widening",
    month="2009-11",
    title="National Highway 17 Widening Protests Gather Strength (2009-11)",
    desc="Local business groups and residents block survey works, protesting proposed demolition of heritage houses. In Goa, this monthly event shapes key regional debates.",
    tags=['infrastructure', 'protest'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_nh17_widening", "Initiate a special government commission to resolve nh17_widening issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_nh17_widening", "Demand that the government address nh17_widening concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_nh17_widening", "Propose a joint multi-party round table to build consensus on nh17_widening.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-12
ITEMS_2006_2010.append(make_news(
    key="ga2006_2009_12_eco_tourism",
    month="2009-12",
    title="Western Ghats Eco-Tourism Projects Approved (2009-12)",
    desc="The forest department clears low-impact resort guidelines for Netravali and Cotigao wildlife sanctuaries. In Goa, this monthly event shapes key regional debates.",
    tags=['environment', 'tourism'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_eco_tourism", "Initiate a special government commission to resolve eco_tourism issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_eco_tourism", "Demand that the government address eco_tourism concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_eco_tourism", "Propose a joint multi-party round table to build consensus on eco_tourism.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-01
ITEMS_2006_2010.append(make_news(
    key="ga2006_2010_01_casinos_mandovi",
    month="2010-01",
    title="Floating Casinos on Mandovi River Draw Licensing Debates (2010-01)",
    desc="The government issues new offshore casino licenses on the Mandovi river, drawing protests from civic groups. In Goa, this monthly event shapes key regional debates.",
    tags=['tourism', 'economy'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_casinos_mandovi", "Initiate a special government commission to resolve casinos_mandovi issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_casinos_mandovi", "Demand that the government address casinos_mandovi concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_casinos_mandovi", "Propose a joint multi-party round table to build consensus on casinos_mandovi.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-02
ITEMS_2006_2010.append(make_news(
    key="ga2006_2010_02_mining_boom",
    month="2010-02",
    title="Bicholim Iron Ore Mining Boom Raises Dust Pollution Concerns (2010-02)",
    desc="Heavy truck corridors transporting iron ore trigger village blockades demanding pollution control tarpaulins. In Goa, this monthly event shapes key regional debates.",
    tags=['environment', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_mining_boom", "Initiate a special government commission to resolve mining_boom issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mining_boom", "Demand that the government address mining_boom concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mining_boom", "Propose a joint multi-party round table to build consensus on mining_boom.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-03
ITEMS_2006_2010.append(make_news(
    key="ga2006_2010_03_political_defections",
    month="2010-03",
    title="Cabinet Instability Threats Amid Revolving-DoorDefections (2010-03)",
    desc="Goa's coalition government faces no-confidence threats as MLAs swap party alignments over portfolio demands. In Goa, this monthly event shapes key regional debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_political_defections", "Initiate a special government commission to resolve political_defections issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_political_defections", "Demand that the government address political_defections concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_political_defections", "Propose a joint multi-party round table to build consensus on political_defections.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-04
ITEMS_2006_2010.append(make_news(
    key="ga2006_2010_04_mega_resorts",
    month="2010-04",
    title="Resort Construction in Morjim Sparks Local Wildlife Outrage (2010-04)",
    desc="Environmentalists protest beach resort developments, citing destruction of Olive Ridley turtle nesting grounds. In Goa, this monthly event shapes key regional debates.",
    tags=['environment', 'tourism'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_mega_resorts", "Initiate a special government commission to resolve mega_resorts issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mega_resorts", "Demand that the government address mega_resorts concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mega_resorts", "Propose a joint multi-party round table to build consensus on mega_resorts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-05
ITEMS_2006_2010.append(make_news(
    key="ga2006_2010_05_infrastructure_mopa",
    month="2010-05",
    title="Mopa Greenfield Airport Land Acquisition Cleared (2010-05)",
    desc="The cabinet approves land acquisition notifications for the proposed greenfield airport at Mopa in North Goa. In Goa, this monthly event shapes key regional debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_infrastructure_mopa", "Initiate a special government commission to resolve infrastructure_mopa issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_infrastructure_mopa", "Demand that the government address infrastructure_mopa concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_infrastructure_mopa", "Propose a joint multi-party round table to build consensus on infrastructure_mopa.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-06
ITEMS_2006_2010.append(make_news(
    key="ga2006_2010_06_garbage_sonsodo_update",
    month="2010-06",
    title="Sonsodo Treatment Plant Delays Cause Margao Protests (2010-06)",
    desc="Margao municipal council faces public wrath as the solid waste treatment plant at Sonsodo fails to start. In Goa, this monthly event shapes key regional debates.",
    tags=['protest', 'environment'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_garbage_sonsodo_update", "Initiate a special government commission to resolve garbage_sonsodo_update issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_garbage_sonsodo_update", "Demand that the government address garbage_sonsodo_update concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_garbage_sonsodo_update", "Propose a joint multi-party round table to build consensus on garbage_sonsodo_update.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-07
ITEMS_2006_2010.append(make_news(
    key="ga2006_2010_07_assembly_elections",
    month="2010-07",
    title="Assembly Campaigns Focus on Regional Plan 2021 Controversies (2010-07)",
    desc="Political parties debate land-use zoning details under Regional Plan 2021, prompting massive protest rallies. In Goa, this monthly event shapes key regional debates.",
    tags=['election', 'politics'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("gov_action_assembly_elections", "Initiate a special government commission to resolve assembly_elections issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_assembly_elections", "Demand that the government address assembly_elections concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_assembly_elections", "Propose a joint multi-party round table to build consensus on assembly_elections.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-08
ITEMS_2006_2010.append(make_news(
    key="ga2006_2010_08_konkani_marathi",
    month="2010-08",
    title="Language Medium of Instruction (MOI) Debates Heat Up (2010-08)",
    desc="Primary school parents and political bodies clash over state grants for Konkani and Marathi medium schools. In Goa, this monthly event shapes key regional debates.",
    tags=['identity', 'politics'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_konkani_marathi", "Initiate a special government commission to resolve konkani_marathi issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_konkani_marathi", "Demand that the government address konkani_marathi concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_konkani_marathi", "Propose a joint multi-party round table to build consensus on konkani_marathi.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-09
ITEMS_2006_2010.append(make_news(
    key="ga2006_2010_09_fishermen_trawlers",
    month="2010-09",
    title="Coast Guard Seizes Trawlers Violating Monsoon Fishing Ban (2010-09)",
    desc="State enforces the mandatory 61-day monsoon breeding fishing ban, drawing criticism from commercial trawler owners. In Goa, this monthly event shapes key regional debates.",
    tags=['protest', 'economy'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_fishermen_trawlers", "Initiate a special government commission to resolve fishermen_trawlers issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_fishermen_trawlers", "Demand that the government address fishermen_trawlers concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_fishermen_trawlers", "Propose a joint multi-party round table to build consensus on fishermen_trawlers.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-10
ITEMS_2006_2010.append(make_news(
    key="ga2006_2010_10_tourist_scam",
    month="2010-10",
    title="Foreign National Land Buyouts Trigger Enforcement Inquiries (2010-10)",
    desc="The Enforcement Directorate probes illegal land purchases by foreign nationals in coastal villages like Calangute. In Goa, this monthly event shapes key regional debates.",
    tags=['governance', 'corruption'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_tourist_scam", "Initiate a special government commission to resolve tourist_scam issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_tourist_scam", "Demand that the government address tourist_scam concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_tourist_scam", "Propose a joint multi-party round table to build consensus on tourist_scam.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-11
ITEMS_2006_2010.append(make_news(
    key="ga2006_2010_11_nh17_widening",
    month="2010-11",
    title="National Highway 17 Widening Protests Gather Strength (2010-11)",
    desc="Local business groups and residents block survey works, protesting proposed demolition of heritage houses. In Goa, this monthly event shapes key regional debates.",
    tags=['infrastructure', 'protest'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_nh17_widening", "Initiate a special government commission to resolve nh17_widening issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_nh17_widening", "Demand that the government address nh17_widening concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_nh17_widening", "Propose a joint multi-party round table to build consensus on nh17_widening.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-12
ITEMS_2006_2010.append(make_news(
    key="ga2006_2010_12_eco_tourism",
    month="2010-12",
    title="Western Ghats Eco-Tourism Projects Approved (2010-12)",
    desc="The forest department clears low-impact resort guidelines for Netravali and Cotigao wildlife sanctuaries. In Goa, this monthly event shapes key regional debates.",
    tags=['environment', 'tourism'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_eco_tourism", "Initiate a special government commission to resolve eco_tourism issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_eco_tourism", "Demand that the government address eco_tourism concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_eco_tourism", "Propose a joint multi-party round table to build consensus on eco_tourism.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

