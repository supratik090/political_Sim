from helper import reaction, no_comment, make_news, eff, risk

ITEMS_2006_2010 = []

# 2006-01
ITEMS_2006_2010.append(make_news(
    key="dl2006_2006_01_cwg_scam",
    month="2006-01",
    title="Commonwealth Games Preparations Face Corruption Allegations (2006-01)",
    desc="CAG reports expose severe inflation of procurement costs for sports equipment, triggering street protests. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['corruption', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_cwg_scam", "Initiate a special government commission to resolve cwg_scam issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cwg_scam", "Demand that the government address cwg_scam concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cwg_scam", "Propose a joint multi-party round table to build consensus on cwg_scam.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-02
ITEMS_2006_2010.append(make_news(
    key="dl2006_2006_02_metro_phase_2",
    month="2006-02",
    title="Metro Phase 2 Connects Gurgaon and Noida to Capital (2006-02)",
    desc="Noida and Gurgaon metro links open, transforming cross-border NCR transit but driving up suburban property rates. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_metro_phase_2", "Initiate a special government commission to resolve metro_phase_2 issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_metro_phase_2", "Demand that the government address metro_phase_2 concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_metro_phase_2", "Propose a joint multi-party round table to build consensus on metro_phase_2.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-03
ITEMS_2006_2010.append(make_news(
    key="dl2006_2006_03_brt_corridor",
    month="2006-03",
    title="Bus Rapid Transit (BRT) Corridor Sparks Traffic Chaos (2006-03)",
    desc="The experimental BRT corridor in South Delhi draws severe flak from car owners citing massive bottleneck jams. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_brt_corridor", "Initiate a special government commission to resolve brt_corridor issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_brt_corridor", "Demand that the government address brt_corridor concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_brt_corridor", "Propose a joint multi-party round table to build consensus on brt_corridor.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-04
ITEMS_2006_2010.append(make_news(
    key="dl2006_2006_04_delhi_blasts_2008",
    month="2006-04",
    title="Serial Blasts Rock Connaught Place and Karol Bagh (2006-04)",
    desc="Terror attacks in busy shopping hubs trigger a curfew-like situation and demands for strict anti-terror laws. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['security_crisis'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("gov_action_delhi_blasts_2008", "Initiate a special government commission to resolve delhi_blasts_2008 issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_delhi_blasts_2008", "Demand that the government address delhi_blasts_2008 concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_delhi_blasts_2008", "Propose a joint multi-party round table to build consensus on delhi_blasts_2008.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-05
ITEMS_2006_2010.append(make_news(
    key="dl2006_2006_05_colony_regularization",
    month="2006-05",
    title="Provisional Regularization Certificates Issued to Colonies (2006-05)",
    desc="The government distributes regularization certificates to over 1,200 unauthorized colonies ahead of polls. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_colony_regularization", "Initiate a special government commission to resolve colony_regularization issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_colony_regularization", "Demand that the government address colony_regularization concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_colony_regularization", "Propose a joint multi-party round table to build consensus on colony_regularization.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-06
ITEMS_2006_2010.append(make_news(
    key="dl2006_2006_06_power_tariffs",
    month="2006-06",
    title="BSES Power Tariff Hike Sparks Resident Welfare Protests (2006-06)",
    desc="Resident Welfare Associations (RWAs) launch 'no tariff bill' campaigns against privatized discom price hikes. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['protest', 'economy'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_power_tariffs", "Initiate a special government commission to resolve power_tariffs issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_power_tariffs", "Demand that the government address power_tariffs concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_power_tariffs", "Propose a joint multi-party round table to build consensus on power_tariffs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-07
ITEMS_2006_2010.append(make_news(
    key="dl2006_2006_07_yamuna_cleaning",
    month="2006-07",
    title="Yamuna Cleaning Project Labeled Ineffective by Green Panels (2006-07)",
    desc="Despite high budget spending, river pollution levels rise, drawing strict remarks from the green tribunal. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_yamuna_cleaning", "Initiate a special government commission to resolve yamuna_cleaning issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_yamuna_cleaning", "Demand that the government address yamuna_cleaning concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_yamuna_cleaning", "Propose a joint multi-party round table to build consensus on yamuna_cleaning.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-08
ITEMS_2006_2010.append(make_news(
    key="dl2006_2006_08_mcd_sealing",
    month="2006-08",
    title="Commercial Sealing Eviction Drives Spark Merchant Strikes (2006-08)",
    desc="Supreme Court-mandated sealing of illegal commercial shops in residential areas triggers city-wide market shutdowns. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_mcd_sealing", "Initiate a special government commission to resolve mcd_sealing issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mcd_sealing", "Demand that the government address mcd_sealing concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mcd_sealing", "Propose a joint multi-party round table to build consensus on mcd_sealing.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-09
ITEMS_2006_2010.append(make_news(
    key="dl2006_2006_09_low_floor_buses",
    month="2006-09",
    title="Red low-floor DTC Buses Introduced to Replace Bluelines (2006-09)",
    desc="Transport department rolls out air-conditioned DTC buses, officially phasing out the accident-prone Bluelines. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_low_floor_buses", "Initiate a special government commission to resolve low_floor_buses issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_low_floor_buses", "Demand that the government address low_floor_buses concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_low_floor_buses", "Propose a joint multi-party round table to build consensus on low_floor_buses.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-10
ITEMS_2006_2010.append(make_news(
    key="dl2006_2006_10_hospital_swine_flu",
    month="2006-10",
    title="Swine Flu Outbreak Triggers Hospital Bed Scarcity (2006-10)",
    desc="Delhi hospitals report heavy rush for H1N1 testing kits and isolation wards, prompting emergency directives. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_hospital_swine_flu", "Initiate a special government commission to resolve hospital_swine_flu issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_hospital_swine_flu", "Demand that the government address hospital_swine_flu concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_hospital_swine_flu", "Propose a joint multi-party round table to build consensus on hospital_swine_flu.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-11
ITEMS_2006_2010.append(make_news(
    key="dl2006_2006_11_admission_nursery",
    month="2006-11",
    title="Nursery School EWS Quota Admissions Trigger Scandals (2006-11)",
    desc="Allegations of fake income certificates to secure seats under the 25% EWS quota spark school inspections. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['identity', 'corruption'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_admission_nursery", "Initiate a special government commission to resolve admission_nursery issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_admission_nursery", "Demand that the government address admission_nursery concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_admission_nursery", "Propose a joint multi-party round table to build consensus on admission_nursery.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-12
ITEMS_2006_2010.append(make_news(
    key="dl2006_2006_12_cwg_opening",
    month="2006-12",
    title="NCT Celebrates Opening of 2010 Commonwealth Games (2006-12)",
    desc="Despite pre-event controversies, the opening ceremony at Jawaharlal Nehru Stadium draws global acclaim. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['politics'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("gov_action_cwg_opening", "Initiate a special government commission to resolve cwg_opening issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cwg_opening", "Demand that the government address cwg_opening concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cwg_opening", "Propose a joint multi-party round table to build consensus on cwg_opening.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-01
ITEMS_2006_2010.append(make_news(
    key="dl2006_2007_01_cwg_scam",
    month="2007-01",
    title="Commonwealth Games Preparations Face Corruption Allegations (2007-01)",
    desc="CAG reports expose severe inflation of procurement costs for sports equipment, triggering street protests. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['corruption', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_cwg_scam", "Initiate a special government commission to resolve cwg_scam issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cwg_scam", "Demand that the government address cwg_scam concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cwg_scam", "Propose a joint multi-party round table to build consensus on cwg_scam.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-02
ITEMS_2006_2010.append(make_news(
    key="dl2006_2007_02_metro_phase_2",
    month="2007-02",
    title="Metro Phase 2 Connects Gurgaon and Noida to Capital (2007-02)",
    desc="Noida and Gurgaon metro links open, transforming cross-border NCR transit but driving up suburban property rates. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_metro_phase_2", "Initiate a special government commission to resolve metro_phase_2 issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_metro_phase_2", "Demand that the government address metro_phase_2 concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_metro_phase_2", "Propose a joint multi-party round table to build consensus on metro_phase_2.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-03
ITEMS_2006_2010.append(make_news(
    key="dl2006_2007_03_brt_corridor",
    month="2007-03",
    title="Bus Rapid Transit (BRT) Corridor Sparks Traffic Chaos (2007-03)",
    desc="The experimental BRT corridor in South Delhi draws severe flak from car owners citing massive bottleneck jams. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_brt_corridor", "Initiate a special government commission to resolve brt_corridor issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_brt_corridor", "Demand that the government address brt_corridor concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_brt_corridor", "Propose a joint multi-party round table to build consensus on brt_corridor.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-04
ITEMS_2006_2010.append(make_news(
    key="dl2006_2007_04_delhi_blasts_2008",
    month="2007-04",
    title="Serial Blasts Rock Connaught Place and Karol Bagh (2007-04)",
    desc="Terror attacks in busy shopping hubs trigger a curfew-like situation and demands for strict anti-terror laws. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['security_crisis'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("gov_action_delhi_blasts_2008", "Initiate a special government commission to resolve delhi_blasts_2008 issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_delhi_blasts_2008", "Demand that the government address delhi_blasts_2008 concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_delhi_blasts_2008", "Propose a joint multi-party round table to build consensus on delhi_blasts_2008.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-05
ITEMS_2006_2010.append(make_news(
    key="dl2006_2007_05_colony_regularization",
    month="2007-05",
    title="Provisional Regularization Certificates Issued to Colonies (2007-05)",
    desc="The government distributes regularization certificates to over 1,200 unauthorized colonies ahead of polls. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_colony_regularization", "Initiate a special government commission to resolve colony_regularization issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_colony_regularization", "Demand that the government address colony_regularization concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_colony_regularization", "Propose a joint multi-party round table to build consensus on colony_regularization.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-06
ITEMS_2006_2010.append(make_news(
    key="dl2006_2007_06_power_tariffs",
    month="2007-06",
    title="BSES Power Tariff Hike Sparks Resident Welfare Protests (2007-06)",
    desc="Resident Welfare Associations (RWAs) launch 'no tariff bill' campaigns against privatized discom price hikes. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['protest', 'economy'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_power_tariffs", "Initiate a special government commission to resolve power_tariffs issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_power_tariffs", "Demand that the government address power_tariffs concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_power_tariffs", "Propose a joint multi-party round table to build consensus on power_tariffs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-07
ITEMS_2006_2010.append(make_news(
    key="dl2006_2007_07_yamuna_cleaning",
    month="2007-07",
    title="Yamuna Cleaning Project Labeled Ineffective by Green Panels (2007-07)",
    desc="Despite high budget spending, river pollution levels rise, drawing strict remarks from the green tribunal. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_yamuna_cleaning", "Initiate a special government commission to resolve yamuna_cleaning issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_yamuna_cleaning", "Demand that the government address yamuna_cleaning concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_yamuna_cleaning", "Propose a joint multi-party round table to build consensus on yamuna_cleaning.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-08
ITEMS_2006_2010.append(make_news(
    key="dl2006_2007_08_mcd_sealing",
    month="2007-08",
    title="Commercial Sealing Eviction Drives Spark Merchant Strikes (2007-08)",
    desc="Supreme Court-mandated sealing of illegal commercial shops in residential areas triggers city-wide market shutdowns. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_mcd_sealing", "Initiate a special government commission to resolve mcd_sealing issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mcd_sealing", "Demand that the government address mcd_sealing concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mcd_sealing", "Propose a joint multi-party round table to build consensus on mcd_sealing.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-09
ITEMS_2006_2010.append(make_news(
    key="dl2006_2007_09_low_floor_buses",
    month="2007-09",
    title="Red low-floor DTC Buses Introduced to Replace Bluelines (2007-09)",
    desc="Transport department rolls out air-conditioned DTC buses, officially phasing out the accident-prone Bluelines. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_low_floor_buses", "Initiate a special government commission to resolve low_floor_buses issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_low_floor_buses", "Demand that the government address low_floor_buses concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_low_floor_buses", "Propose a joint multi-party round table to build consensus on low_floor_buses.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-10
ITEMS_2006_2010.append(make_news(
    key="dl2006_2007_10_hospital_swine_flu",
    month="2007-10",
    title="Swine Flu Outbreak Triggers Hospital Bed Scarcity (2007-10)",
    desc="Delhi hospitals report heavy rush for H1N1 testing kits and isolation wards, prompting emergency directives. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_hospital_swine_flu", "Initiate a special government commission to resolve hospital_swine_flu issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_hospital_swine_flu", "Demand that the government address hospital_swine_flu concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_hospital_swine_flu", "Propose a joint multi-party round table to build consensus on hospital_swine_flu.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-11
ITEMS_2006_2010.append(make_news(
    key="dl2006_2007_11_admission_nursery",
    month="2007-11",
    title="Nursery School EWS Quota Admissions Trigger Scandals (2007-11)",
    desc="Allegations of fake income certificates to secure seats under the 25% EWS quota spark school inspections. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['identity', 'corruption'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_admission_nursery", "Initiate a special government commission to resolve admission_nursery issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_admission_nursery", "Demand that the government address admission_nursery concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_admission_nursery", "Propose a joint multi-party round table to build consensus on admission_nursery.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-12
ITEMS_2006_2010.append(make_news(
    key="dl2006_2007_12_cwg_opening",
    month="2007-12",
    title="NCT Celebrates Opening of 2010 Commonwealth Games (2007-12)",
    desc="Despite pre-event controversies, the opening ceremony at Jawaharlal Nehru Stadium draws global acclaim. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['politics'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("gov_action_cwg_opening", "Initiate a special government commission to resolve cwg_opening issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cwg_opening", "Demand that the government address cwg_opening concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cwg_opening", "Propose a joint multi-party round table to build consensus on cwg_opening.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-01
ITEMS_2006_2010.append(make_news(
    key="dl2006_2008_01_cwg_scam",
    month="2008-01",
    title="Commonwealth Games Preparations Face Corruption Allegations (2008-01)",
    desc="CAG reports expose severe inflation of procurement costs for sports equipment, triggering street protests. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['corruption', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_cwg_scam", "Initiate a special government commission to resolve cwg_scam issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cwg_scam", "Demand that the government address cwg_scam concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cwg_scam", "Propose a joint multi-party round table to build consensus on cwg_scam.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-02
ITEMS_2006_2010.append(make_news(
    key="dl2006_2008_02_metro_phase_2",
    month="2008-02",
    title="Metro Phase 2 Connects Gurgaon and Noida to Capital (2008-02)",
    desc="Noida and Gurgaon metro links open, transforming cross-border NCR transit but driving up suburban property rates. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_metro_phase_2", "Initiate a special government commission to resolve metro_phase_2 issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_metro_phase_2", "Demand that the government address metro_phase_2 concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_metro_phase_2", "Propose a joint multi-party round table to build consensus on metro_phase_2.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-03
ITEMS_2006_2010.append(make_news(
    key="dl2006_2008_03_brt_corridor",
    month="2008-03",
    title="Bus Rapid Transit (BRT) Corridor Sparks Traffic Chaos (2008-03)",
    desc="The experimental BRT corridor in South Delhi draws severe flak from car owners citing massive bottleneck jams. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_brt_corridor", "Initiate a special government commission to resolve brt_corridor issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_brt_corridor", "Demand that the government address brt_corridor concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_brt_corridor", "Propose a joint multi-party round table to build consensus on brt_corridor.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-04
ITEMS_2006_2010.append(make_news(
    key="dl2006_2008_04_delhi_blasts_2008",
    month="2008-04",
    title="Serial Blasts Rock Connaught Place and Karol Bagh (2008-04)",
    desc="Terror attacks in busy shopping hubs trigger a curfew-like situation and demands for strict anti-terror laws. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['security_crisis'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("gov_action_delhi_blasts_2008", "Initiate a special government commission to resolve delhi_blasts_2008 issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_delhi_blasts_2008", "Demand that the government address delhi_blasts_2008 concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_delhi_blasts_2008", "Propose a joint multi-party round table to build consensus on delhi_blasts_2008.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-05
ITEMS_2006_2010.append(make_news(
    key="dl2006_2008_05_colony_regularization",
    month="2008-05",
    title="Provisional Regularization Certificates Issued to Colonies (2008-05)",
    desc="The government distributes regularization certificates to over 1,200 unauthorized colonies ahead of polls. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_colony_regularization", "Initiate a special government commission to resolve colony_regularization issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_colony_regularization", "Demand that the government address colony_regularization concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_colony_regularization", "Propose a joint multi-party round table to build consensus on colony_regularization.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-06
ITEMS_2006_2010.append(make_news(
    key="dl2006_2008_06_power_tariffs",
    month="2008-06",
    title="BSES Power Tariff Hike Sparks Resident Welfare Protests (2008-06)",
    desc="Resident Welfare Associations (RWAs) launch 'no tariff bill' campaigns against privatized discom price hikes. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['protest', 'economy'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_power_tariffs", "Initiate a special government commission to resolve power_tariffs issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_power_tariffs", "Demand that the government address power_tariffs concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_power_tariffs", "Propose a joint multi-party round table to build consensus on power_tariffs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-07
ITEMS_2006_2010.append(make_news(
    key="dl2006_2008_07_yamuna_cleaning",
    month="2008-07",
    title="Yamuna Cleaning Project Labeled Ineffective by Green Panels (2008-07)",
    desc="Despite high budget spending, river pollution levels rise, drawing strict remarks from the green tribunal. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_yamuna_cleaning", "Initiate a special government commission to resolve yamuna_cleaning issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_yamuna_cleaning", "Demand that the government address yamuna_cleaning concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_yamuna_cleaning", "Propose a joint multi-party round table to build consensus on yamuna_cleaning.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-08
ITEMS_2006_2010.append(make_news(
    key="dl2006_2008_08_mcd_sealing",
    month="2008-08",
    title="Commercial Sealing Eviction Drives Spark Merchant Strikes (2008-08)",
    desc="Supreme Court-mandated sealing of illegal commercial shops in residential areas triggers city-wide market shutdowns. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_mcd_sealing", "Initiate a special government commission to resolve mcd_sealing issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mcd_sealing", "Demand that the government address mcd_sealing concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mcd_sealing", "Propose a joint multi-party round table to build consensus on mcd_sealing.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-09
ITEMS_2006_2010.append(make_news(
    key="dl2006_2008_09_low_floor_buses",
    month="2008-09",
    title="Red low-floor DTC Buses Introduced to Replace Bluelines (2008-09)",
    desc="Transport department rolls out air-conditioned DTC buses, officially phasing out the accident-prone Bluelines. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_low_floor_buses", "Initiate a special government commission to resolve low_floor_buses issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_low_floor_buses", "Demand that the government address low_floor_buses concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_low_floor_buses", "Propose a joint multi-party round table to build consensus on low_floor_buses.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-10
ITEMS_2006_2010.append(make_news(
    key="dl2006_2008_10_hospital_swine_flu",
    month="2008-10",
    title="Swine Flu Outbreak Triggers Hospital Bed Scarcity (2008-10)",
    desc="Delhi hospitals report heavy rush for H1N1 testing kits and isolation wards, prompting emergency directives. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_hospital_swine_flu", "Initiate a special government commission to resolve hospital_swine_flu issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_hospital_swine_flu", "Demand that the government address hospital_swine_flu concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_hospital_swine_flu", "Propose a joint multi-party round table to build consensus on hospital_swine_flu.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-11
ITEMS_2006_2010.append(make_news(
    key="dl2006_2008_11_admission_nursery",
    month="2008-11",
    title="Nursery School EWS Quota Admissions Trigger Scandals (2008-11)",
    desc="Allegations of fake income certificates to secure seats under the 25% EWS quota spark school inspections. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['identity', 'corruption'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_admission_nursery", "Initiate a special government commission to resolve admission_nursery issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_admission_nursery", "Demand that the government address admission_nursery concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_admission_nursery", "Propose a joint multi-party round table to build consensus on admission_nursery.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-12
ITEMS_2006_2010.append(make_news(
    key="dl2006_2008_12_cwg_opening",
    month="2008-12",
    title="NCT Celebrates Opening of 2010 Commonwealth Games (2008-12)",
    desc="Despite pre-event controversies, the opening ceremony at Jawaharlal Nehru Stadium draws global acclaim. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['politics'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("gov_action_cwg_opening", "Initiate a special government commission to resolve cwg_opening issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cwg_opening", "Demand that the government address cwg_opening concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cwg_opening", "Propose a joint multi-party round table to build consensus on cwg_opening.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-01
ITEMS_2006_2010.append(make_news(
    key="dl2006_2009_01_cwg_scam",
    month="2009-01",
    title="Commonwealth Games Preparations Face Corruption Allegations (2009-01)",
    desc="CAG reports expose severe inflation of procurement costs for sports equipment, triggering street protests. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['corruption', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_cwg_scam", "Initiate a special government commission to resolve cwg_scam issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cwg_scam", "Demand that the government address cwg_scam concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cwg_scam", "Propose a joint multi-party round table to build consensus on cwg_scam.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-02
ITEMS_2006_2010.append(make_news(
    key="dl2006_2009_02_metro_phase_2",
    month="2009-02",
    title="Metro Phase 2 Connects Gurgaon and Noida to Capital (2009-02)",
    desc="Noida and Gurgaon metro links open, transforming cross-border NCR transit but driving up suburban property rates. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_metro_phase_2", "Initiate a special government commission to resolve metro_phase_2 issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_metro_phase_2", "Demand that the government address metro_phase_2 concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_metro_phase_2", "Propose a joint multi-party round table to build consensus on metro_phase_2.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-03
ITEMS_2006_2010.append(make_news(
    key="dl2006_2009_03_brt_corridor",
    month="2009-03",
    title="Bus Rapid Transit (BRT) Corridor Sparks Traffic Chaos (2009-03)",
    desc="The experimental BRT corridor in South Delhi draws severe flak from car owners citing massive bottleneck jams. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_brt_corridor", "Initiate a special government commission to resolve brt_corridor issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_brt_corridor", "Demand that the government address brt_corridor concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_brt_corridor", "Propose a joint multi-party round table to build consensus on brt_corridor.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-04
ITEMS_2006_2010.append(make_news(
    key="dl2006_2009_04_delhi_blasts_2008",
    month="2009-04",
    title="Serial Blasts Rock Connaught Place and Karol Bagh (2009-04)",
    desc="Terror attacks in busy shopping hubs trigger a curfew-like situation and demands for strict anti-terror laws. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['security_crisis'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("gov_action_delhi_blasts_2008", "Initiate a special government commission to resolve delhi_blasts_2008 issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_delhi_blasts_2008", "Demand that the government address delhi_blasts_2008 concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_delhi_blasts_2008", "Propose a joint multi-party round table to build consensus on delhi_blasts_2008.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-05
ITEMS_2006_2010.append(make_news(
    key="dl2006_2009_05_colony_regularization",
    month="2009-05",
    title="Provisional Regularization Certificates Issued to Colonies (2009-05)",
    desc="The government distributes regularization certificates to over 1,200 unauthorized colonies ahead of polls. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_colony_regularization", "Initiate a special government commission to resolve colony_regularization issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_colony_regularization", "Demand that the government address colony_regularization concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_colony_regularization", "Propose a joint multi-party round table to build consensus on colony_regularization.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-06
ITEMS_2006_2010.append(make_news(
    key="dl2006_2009_06_power_tariffs",
    month="2009-06",
    title="BSES Power Tariff Hike Sparks Resident Welfare Protests (2009-06)",
    desc="Resident Welfare Associations (RWAs) launch 'no tariff bill' campaigns against privatized discom price hikes. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['protest', 'economy'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_power_tariffs", "Initiate a special government commission to resolve power_tariffs issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_power_tariffs", "Demand that the government address power_tariffs concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_power_tariffs", "Propose a joint multi-party round table to build consensus on power_tariffs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-07
ITEMS_2006_2010.append(make_news(
    key="dl2006_2009_07_yamuna_cleaning",
    month="2009-07",
    title="Yamuna Cleaning Project Labeled Ineffective by Green Panels (2009-07)",
    desc="Despite high budget spending, river pollution levels rise, drawing strict remarks from the green tribunal. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_yamuna_cleaning", "Initiate a special government commission to resolve yamuna_cleaning issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_yamuna_cleaning", "Demand that the government address yamuna_cleaning concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_yamuna_cleaning", "Propose a joint multi-party round table to build consensus on yamuna_cleaning.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-08
ITEMS_2006_2010.append(make_news(
    key="dl2006_2009_08_mcd_sealing",
    month="2009-08",
    title="Commercial Sealing Eviction Drives Spark Merchant Strikes (2009-08)",
    desc="Supreme Court-mandated sealing of illegal commercial shops in residential areas triggers city-wide market shutdowns. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_mcd_sealing", "Initiate a special government commission to resolve mcd_sealing issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mcd_sealing", "Demand that the government address mcd_sealing concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mcd_sealing", "Propose a joint multi-party round table to build consensus on mcd_sealing.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-09
ITEMS_2006_2010.append(make_news(
    key="dl2006_2009_09_low_floor_buses",
    month="2009-09",
    title="Red low-floor DTC Buses Introduced to Replace Bluelines (2009-09)",
    desc="Transport department rolls out air-conditioned DTC buses, officially phasing out the accident-prone Bluelines. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_low_floor_buses", "Initiate a special government commission to resolve low_floor_buses issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_low_floor_buses", "Demand that the government address low_floor_buses concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_low_floor_buses", "Propose a joint multi-party round table to build consensus on low_floor_buses.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-10
ITEMS_2006_2010.append(make_news(
    key="dl2006_2009_10_hospital_swine_flu",
    month="2009-10",
    title="Swine Flu Outbreak Triggers Hospital Bed Scarcity (2009-10)",
    desc="Delhi hospitals report heavy rush for H1N1 testing kits and isolation wards, prompting emergency directives. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_hospital_swine_flu", "Initiate a special government commission to resolve hospital_swine_flu issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_hospital_swine_flu", "Demand that the government address hospital_swine_flu concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_hospital_swine_flu", "Propose a joint multi-party round table to build consensus on hospital_swine_flu.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-11
ITEMS_2006_2010.append(make_news(
    key="dl2006_2009_11_admission_nursery",
    month="2009-11",
    title="Nursery School EWS Quota Admissions Trigger Scandals (2009-11)",
    desc="Allegations of fake income certificates to secure seats under the 25% EWS quota spark school inspections. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['identity', 'corruption'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_admission_nursery", "Initiate a special government commission to resolve admission_nursery issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_admission_nursery", "Demand that the government address admission_nursery concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_admission_nursery", "Propose a joint multi-party round table to build consensus on admission_nursery.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-12
ITEMS_2006_2010.append(make_news(
    key="dl2006_2009_12_cwg_opening",
    month="2009-12",
    title="NCT Celebrates Opening of 2010 Commonwealth Games (2009-12)",
    desc="Despite pre-event controversies, the opening ceremony at Jawaharlal Nehru Stadium draws global acclaim. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['politics'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("gov_action_cwg_opening", "Initiate a special government commission to resolve cwg_opening issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cwg_opening", "Demand that the government address cwg_opening concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cwg_opening", "Propose a joint multi-party round table to build consensus on cwg_opening.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-01
ITEMS_2006_2010.append(make_news(
    key="dl2006_2010_01_cwg_scam",
    month="2010-01",
    title="Commonwealth Games Preparations Face Corruption Allegations (2010-01)",
    desc="CAG reports expose severe inflation of procurement costs for sports equipment, triggering street protests. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['corruption', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_cwg_scam", "Initiate a special government commission to resolve cwg_scam issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cwg_scam", "Demand that the government address cwg_scam concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cwg_scam", "Propose a joint multi-party round table to build consensus on cwg_scam.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-02
ITEMS_2006_2010.append(make_news(
    key="dl2006_2010_02_metro_phase_2",
    month="2010-02",
    title="Metro Phase 2 Connects Gurgaon and Noida to Capital (2010-02)",
    desc="Noida and Gurgaon metro links open, transforming cross-border NCR transit but driving up suburban property rates. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_metro_phase_2", "Initiate a special government commission to resolve metro_phase_2 issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_metro_phase_2", "Demand that the government address metro_phase_2 concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_metro_phase_2", "Propose a joint multi-party round table to build consensus on metro_phase_2.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-03
ITEMS_2006_2010.append(make_news(
    key="dl2006_2010_03_brt_corridor",
    month="2010-03",
    title="Bus Rapid Transit (BRT) Corridor Sparks Traffic Chaos (2010-03)",
    desc="The experimental BRT corridor in South Delhi draws severe flak from car owners citing massive bottleneck jams. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_brt_corridor", "Initiate a special government commission to resolve brt_corridor issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_brt_corridor", "Demand that the government address brt_corridor concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_brt_corridor", "Propose a joint multi-party round table to build consensus on brt_corridor.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-04
ITEMS_2006_2010.append(make_news(
    key="dl2006_2010_04_delhi_blasts_2008",
    month="2010-04",
    title="Serial Blasts Rock Connaught Place and Karol Bagh (2010-04)",
    desc="Terror attacks in busy shopping hubs trigger a curfew-like situation and demands for strict anti-terror laws. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['security_crisis'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("gov_action_delhi_blasts_2008", "Initiate a special government commission to resolve delhi_blasts_2008 issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_delhi_blasts_2008", "Demand that the government address delhi_blasts_2008 concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_delhi_blasts_2008", "Propose a joint multi-party round table to build consensus on delhi_blasts_2008.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-05
ITEMS_2006_2010.append(make_news(
    key="dl2006_2010_05_colony_regularization",
    month="2010-05",
    title="Provisional Regularization Certificates Issued to Colonies (2010-05)",
    desc="The government distributes regularization certificates to over 1,200 unauthorized colonies ahead of polls. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_colony_regularization", "Initiate a special government commission to resolve colony_regularization issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_colony_regularization", "Demand that the government address colony_regularization concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_colony_regularization", "Propose a joint multi-party round table to build consensus on colony_regularization.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-06
ITEMS_2006_2010.append(make_news(
    key="dl2006_2010_06_power_tariffs",
    month="2010-06",
    title="BSES Power Tariff Hike Sparks Resident Welfare Protests (2010-06)",
    desc="Resident Welfare Associations (RWAs) launch 'no tariff bill' campaigns against privatized discom price hikes. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['protest', 'economy'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_power_tariffs", "Initiate a special government commission to resolve power_tariffs issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_power_tariffs", "Demand that the government address power_tariffs concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_power_tariffs", "Propose a joint multi-party round table to build consensus on power_tariffs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-07
ITEMS_2006_2010.append(make_news(
    key="dl2006_2010_07_yamuna_cleaning",
    month="2010-07",
    title="Yamuna Cleaning Project Labeled Ineffective by Green Panels (2010-07)",
    desc="Despite high budget spending, river pollution levels rise, drawing strict remarks from the green tribunal. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_yamuna_cleaning", "Initiate a special government commission to resolve yamuna_cleaning issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_yamuna_cleaning", "Demand that the government address yamuna_cleaning concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_yamuna_cleaning", "Propose a joint multi-party round table to build consensus on yamuna_cleaning.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-08
ITEMS_2006_2010.append(make_news(
    key="dl2006_2010_08_mcd_sealing",
    month="2010-08",
    title="Commercial Sealing Eviction Drives Spark Merchant Strikes (2010-08)",
    desc="Supreme Court-mandated sealing of illegal commercial shops in residential areas triggers city-wide market shutdowns. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_mcd_sealing", "Initiate a special government commission to resolve mcd_sealing issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mcd_sealing", "Demand that the government address mcd_sealing concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mcd_sealing", "Propose a joint multi-party round table to build consensus on mcd_sealing.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-09
ITEMS_2006_2010.append(make_news(
    key="dl2006_2010_09_low_floor_buses",
    month="2010-09",
    title="Red low-floor DTC Buses Introduced to Replace Bluelines (2010-09)",
    desc="Transport department rolls out air-conditioned DTC buses, officially phasing out the accident-prone Bluelines. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_low_floor_buses", "Initiate a special government commission to resolve low_floor_buses issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_low_floor_buses", "Demand that the government address low_floor_buses concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_low_floor_buses", "Propose a joint multi-party round table to build consensus on low_floor_buses.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-10
ITEMS_2006_2010.append(make_news(
    key="dl2006_2010_10_hospital_swine_flu",
    month="2010-10",
    title="Swine Flu Outbreak Triggers Hospital Bed Scarcity (2010-10)",
    desc="Delhi hospitals report heavy rush for H1N1 testing kits and isolation wards, prompting emergency directives. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_hospital_swine_flu", "Initiate a special government commission to resolve hospital_swine_flu issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_hospital_swine_flu", "Demand that the government address hospital_swine_flu concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_hospital_swine_flu", "Propose a joint multi-party round table to build consensus on hospital_swine_flu.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-11
ITEMS_2006_2010.append(make_news(
    key="dl2006_2010_11_admission_nursery",
    month="2010-11",
    title="Nursery School EWS Quota Admissions Trigger Scandals (2010-11)",
    desc="Allegations of fake income certificates to secure seats under the 25% EWS quota spark school inspections. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['identity', 'corruption'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_admission_nursery", "Initiate a special government commission to resolve admission_nursery issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_admission_nursery", "Demand that the government address admission_nursery concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_admission_nursery", "Propose a joint multi-party round table to build consensus on admission_nursery.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-12
ITEMS_2006_2010.append(make_news(
    key="dl2006_2010_12_cwg_opening",
    month="2010-12",
    title="NCT Celebrates Opening of 2010 Commonwealth Games (2010-12)",
    desc="Despite pre-event controversies, the opening ceremony at Jawaharlal Nehru Stadium draws global acclaim. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['politics'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("gov_action_cwg_opening", "Initiate a special government commission to resolve cwg_opening issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cwg_opening", "Demand that the government address cwg_opening concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cwg_opening", "Propose a joint multi-party round table to build consensus on cwg_opening.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

