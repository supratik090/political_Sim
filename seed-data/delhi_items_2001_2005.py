from helper import reaction, no_comment, make_news, eff, risk

ITEMS_2001_2005 = []

# 2001-01
ITEMS_2001_2005.append(make_news(
    key="dl2001_2001_01_cng_transition",
    month="2001-01",
    title="CNG Transition Mandate Triggers Public Transport Crisis (2001-01)",
    desc="The Supreme Court mandate forcing commercial vehicles to switch to CNG causes massive queues at filling stations. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure', 'environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_cng_transition", "Initiate a special government commission to resolve cng_transition issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cng_transition", "Demand that the government address cng_transition concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cng_transition", "Propose a joint multi-party round table to build consensus on cng_transition.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-02
ITEMS_2001_2005.append(make_news(
    key="dl2001_2001_02_metro_phase_1",
    month="2001-02",
    title="Delhi Metro Phase 1 Trials Begin on Shahdara-Tis Hazari Line (2001-02)",
    desc="The first passenger trial runs on Delhi's new elevated metro corridor draw major crowds and political attention. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_metro_phase_1", "Initiate a special government commission to resolve metro_phase_1 issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_metro_phase_1", "Demand that the government address metro_phase_1 concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_metro_phase_1", "Propose a joint multi-party round table to build consensus on metro_phase_1.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-03
ITEMS_2001_2005.append(make_news(
    key="dl2001_2001_03_power_privatization",
    month="2001-03",
    title="Power Distribution Privatized to BSES and NDPL (2001-03)",
    desc="The government privatizes electricity distribution, aiming to stop load shedding, but consumers complain of high tariffs. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['economy', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_power_privatization", "Initiate a special government commission to resolve power_privatization issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_power_privatization", "Demand that the government address power_privatization concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_power_privatization", "Propose a joint multi-party round table to build consensus on power_privatization.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-04
ITEMS_2001_2005.append(make_news(
    key="dl2001_2001_04_slum_demolition",
    month="2001-04",
    title="Yamuna Pushta Slum Demolitions Cause Protest (2001-04)",
    desc="Large-scale eviction drives along the Yamuna riverbed to create green belts trigger intense protests from rights groups. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_slum_demolition", "Initiate a special government commission to resolve slum_demolition issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_slum_demolition", "Demand that the government address slum_demolition concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_slum_demolition", "Propose a joint multi-party round table to build consensus on slum_demolition.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-05
ITEMS_2001_2005.append(make_news(
    key="dl2001_2001_05_water_tankers",
    month="2001-05",
    title="Water Scarcity in Dwarka Sparks Tanker Mafia Clashes (2001-05)",
    desc="Rapidly developing sub-cities report severe drinking water shortages, leading to clashes over private water tanker supply. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['rural', 'governance'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_water_tankers", "Initiate a special government commission to resolve water_tankers issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_water_tankers", "Demand that the government address water_tankers concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_water_tankers", "Propose a joint multi-party round table to build consensus on water_tankers.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-06
ITEMS_2001_2005.append(make_news(
    key="dl2001_2001_06_unauthorized_colonies",
    month="2001-06",
    title="Unauthorized Colony Residents Demand Regularization (2001-06)",
    desc="Voter organizations in unregistered colonies stage rallies, demanding municipal water and sewage connections. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['politics'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("gov_action_unauthorized_colonies", "Initiate a special government commission to resolve unauthorized_colonies issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_unauthorized_colonies", "Demand that the government address unauthorized_colonies concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_unauthorized_colonies", "Propose a joint multi-party round table to build consensus on unauthorized_colonies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-07
ITEMS_2001_2005.append(make_news(
    key="dl2001_2001_07_blueline_buses",
    month="2001-07",
    title="Blueline Bus Menace Prompts Transport Department Warnings (2001-07)",
    desc="Frequent accidents involving private Blueline buses prompt calls for cancellation of private operator route permits. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_blueline_buses", "Initiate a special government commission to resolve blueline_buses issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_blueline_buses", "Demand that the government address blueline_buses concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_blueline_buses", "Propose a joint multi-party round table to build consensus on blueline_buses.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-08
ITEMS_2001_2005.append(make_news(
    key="dl2001_2001_08_industry_relocation",
    month="2001-08",
    title="Polluting Industries Ordered to Relocate Outside City Borders (2001-08)",
    desc="Supreme Court orders the closure of non-conforming hazardous factories, leading to industrial worker strikes. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['environment', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_industry_relocation", "Initiate a special government commission to resolve industry_relocation issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_industry_relocation", "Demand that the government address industry_relocation concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_industry_relocation", "Propose a joint multi-party round table to build consensus on industry_relocation.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-09
ITEMS_2001_2005.append(make_news(
    key="dl2001_2001_09_delhi_blasts",
    month="2001-09",
    title="Serial Blasts in Markets Cause Security Crisis (2001-09)",
    desc="Pre-Diwali bomb blasts in busy markets of Sarojini Nagar and Paharganj trigger a massive state-wide security alert. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['security_crisis'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("gov_action_delhi_blasts", "Initiate a special government commission to resolve delhi_blasts issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_delhi_blasts", "Demand that the government address delhi_blasts concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_delhi_blasts", "Propose a joint multi-party round table to build consensus on delhi_blasts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-10
ITEMS_2001_2005.append(make_news(
    key="dl2001_2001_10_municipal_reforms",
    month="2001-10",
    title="MCD Decentralization Debates Stall Council Work (2001-10)",
    desc="Proposals to split the Municipal Corporation of Delhi into smaller zones face opposition from local councilors. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_municipal_reforms", "Initiate a special government commission to resolve municipal_reforms issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_municipal_reforms", "Demand that the government address municipal_reforms concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_municipal_reforms", "Propose a joint multi-party round table to build consensus on municipal_reforms.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-11
ITEMS_2001_2005.append(make_news(
    key="dl2001_2001_11_flyover_boom",
    month="2001-11",
    title="Flyover Construction Boom Completed on Ring Road (2001-11)",
    desc="Sheila Dikshit's flyover push speeds up Ring Road traffic, though shopkeepers complain of construction blockades. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_flyover_boom", "Initiate a special government commission to resolve flyover_boom issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_flyover_boom", "Demand that the government address flyover_boom concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_flyover_boom", "Propose a joint multi-party round table to build consensus on flyover_boom.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-12
ITEMS_2001_2005.append(make_news(
    key="dl2001_2001_12_school_infrastructure",
    month="2001-12",
    title="Government School Improvement Program Launched (2001-12)",
    desc="Education department announces new classroom construction and computer labs in state-run secondary schools. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_school_infrastructure", "Initiate a special government commission to resolve school_infrastructure issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_school_infrastructure", "Demand that the government address school_infrastructure concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_school_infrastructure", "Propose a joint multi-party round table to build consensus on school_infrastructure.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-01
ITEMS_2001_2005.append(make_news(
    key="dl2001_2002_01_cng_transition",
    month="2002-01",
    title="CNG Transition Mandate Triggers Public Transport Crisis (2002-01)",
    desc="The Supreme Court mandate forcing commercial vehicles to switch to CNG causes massive queues at filling stations. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure', 'environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_cng_transition", "Initiate a special government commission to resolve cng_transition issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cng_transition", "Demand that the government address cng_transition concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cng_transition", "Propose a joint multi-party round table to build consensus on cng_transition.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-02
ITEMS_2001_2005.append(make_news(
    key="dl2001_2002_02_metro_phase_1",
    month="2002-02",
    title="Delhi Metro Phase 1 Trials Begin on Shahdara-Tis Hazari Line (2002-02)",
    desc="The first passenger trial runs on Delhi's new elevated metro corridor draw major crowds and political attention. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_metro_phase_1", "Initiate a special government commission to resolve metro_phase_1 issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_metro_phase_1", "Demand that the government address metro_phase_1 concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_metro_phase_1", "Propose a joint multi-party round table to build consensus on metro_phase_1.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-03
ITEMS_2001_2005.append(make_news(
    key="dl2001_2002_03_power_privatization",
    month="2002-03",
    title="Power Distribution Privatized to BSES and NDPL (2002-03)",
    desc="The government privatizes electricity distribution, aiming to stop load shedding, but consumers complain of high tariffs. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['economy', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_power_privatization", "Initiate a special government commission to resolve power_privatization issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_power_privatization", "Demand that the government address power_privatization concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_power_privatization", "Propose a joint multi-party round table to build consensus on power_privatization.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-04
ITEMS_2001_2005.append(make_news(
    key="dl2001_2002_04_slum_demolition",
    month="2002-04",
    title="Yamuna Pushta Slum Demolitions Cause Protest (2002-04)",
    desc="Large-scale eviction drives along the Yamuna riverbed to create green belts trigger intense protests from rights groups. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_slum_demolition", "Initiate a special government commission to resolve slum_demolition issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_slum_demolition", "Demand that the government address slum_demolition concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_slum_demolition", "Propose a joint multi-party round table to build consensus on slum_demolition.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-05
ITEMS_2001_2005.append(make_news(
    key="dl2001_2002_05_water_tankers",
    month="2002-05",
    title="Water Scarcity in Dwarka Sparks Tanker Mafia Clashes (2002-05)",
    desc="Rapidly developing sub-cities report severe drinking water shortages, leading to clashes over private water tanker supply. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['rural', 'governance'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_water_tankers", "Initiate a special government commission to resolve water_tankers issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_water_tankers", "Demand that the government address water_tankers concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_water_tankers", "Propose a joint multi-party round table to build consensus on water_tankers.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-06
ITEMS_2001_2005.append(make_news(
    key="dl2001_2002_06_unauthorized_colonies",
    month="2002-06",
    title="Unauthorized Colony Residents Demand Regularization (2002-06)",
    desc="Voter organizations in unregistered colonies stage rallies, demanding municipal water and sewage connections. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['politics'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("gov_action_unauthorized_colonies", "Initiate a special government commission to resolve unauthorized_colonies issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_unauthorized_colonies", "Demand that the government address unauthorized_colonies concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_unauthorized_colonies", "Propose a joint multi-party round table to build consensus on unauthorized_colonies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-07
ITEMS_2001_2005.append(make_news(
    key="dl2001_2002_07_blueline_buses",
    month="2002-07",
    title="Blueline Bus Menace Prompts Transport Department Warnings (2002-07)",
    desc="Frequent accidents involving private Blueline buses prompt calls for cancellation of private operator route permits. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_blueline_buses", "Initiate a special government commission to resolve blueline_buses issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_blueline_buses", "Demand that the government address blueline_buses concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_blueline_buses", "Propose a joint multi-party round table to build consensus on blueline_buses.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-08
ITEMS_2001_2005.append(make_news(
    key="dl2001_2002_08_industry_relocation",
    month="2002-08",
    title="Polluting Industries Ordered to Relocate Outside City Borders (2002-08)",
    desc="Supreme Court orders the closure of non-conforming hazardous factories, leading to industrial worker strikes. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['environment', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_industry_relocation", "Initiate a special government commission to resolve industry_relocation issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_industry_relocation", "Demand that the government address industry_relocation concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_industry_relocation", "Propose a joint multi-party round table to build consensus on industry_relocation.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-09
ITEMS_2001_2005.append(make_news(
    key="dl2001_2002_09_delhi_blasts",
    month="2002-09",
    title="Serial Blasts in Markets Cause Security Crisis (2002-09)",
    desc="Pre-Diwali bomb blasts in busy markets of Sarojini Nagar and Paharganj trigger a massive state-wide security alert. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['security_crisis'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("gov_action_delhi_blasts", "Initiate a special government commission to resolve delhi_blasts issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_delhi_blasts", "Demand that the government address delhi_blasts concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_delhi_blasts", "Propose a joint multi-party round table to build consensus on delhi_blasts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-10
ITEMS_2001_2005.append(make_news(
    key="dl2001_2002_10_municipal_reforms",
    month="2002-10",
    title="MCD Decentralization Debates Stall Council Work (2002-10)",
    desc="Proposals to split the Municipal Corporation of Delhi into smaller zones face opposition from local councilors. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_municipal_reforms", "Initiate a special government commission to resolve municipal_reforms issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_municipal_reforms", "Demand that the government address municipal_reforms concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_municipal_reforms", "Propose a joint multi-party round table to build consensus on municipal_reforms.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-11
ITEMS_2001_2005.append(make_news(
    key="dl2001_2002_11_flyover_boom",
    month="2002-11",
    title="Flyover Construction Boom Completed on Ring Road (2002-11)",
    desc="Sheila Dikshit's flyover push speeds up Ring Road traffic, though shopkeepers complain of construction blockades. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_flyover_boom", "Initiate a special government commission to resolve flyover_boom issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_flyover_boom", "Demand that the government address flyover_boom concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_flyover_boom", "Propose a joint multi-party round table to build consensus on flyover_boom.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-12
ITEMS_2001_2005.append(make_news(
    key="dl2001_2002_12_school_infrastructure",
    month="2002-12",
    title="Government School Improvement Program Launched (2002-12)",
    desc="Education department announces new classroom construction and computer labs in state-run secondary schools. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_school_infrastructure", "Initiate a special government commission to resolve school_infrastructure issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_school_infrastructure", "Demand that the government address school_infrastructure concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_school_infrastructure", "Propose a joint multi-party round table to build consensus on school_infrastructure.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-01
ITEMS_2001_2005.append(make_news(
    key="dl2001_2003_01_cng_transition",
    month="2003-01",
    title="CNG Transition Mandate Triggers Public Transport Crisis (2003-01)",
    desc="The Supreme Court mandate forcing commercial vehicles to switch to CNG causes massive queues at filling stations. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure', 'environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_cng_transition", "Initiate a special government commission to resolve cng_transition issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cng_transition", "Demand that the government address cng_transition concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cng_transition", "Propose a joint multi-party round table to build consensus on cng_transition.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-02
ITEMS_2001_2005.append(make_news(
    key="dl2001_2003_02_metro_phase_1",
    month="2003-02",
    title="Delhi Metro Phase 1 Trials Begin on Shahdara-Tis Hazari Line (2003-02)",
    desc="The first passenger trial runs on Delhi's new elevated metro corridor draw major crowds and political attention. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_metro_phase_1", "Initiate a special government commission to resolve metro_phase_1 issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_metro_phase_1", "Demand that the government address metro_phase_1 concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_metro_phase_1", "Propose a joint multi-party round table to build consensus on metro_phase_1.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-03
ITEMS_2001_2005.append(make_news(
    key="dl2001_2003_03_power_privatization",
    month="2003-03",
    title="Power Distribution Privatized to BSES and NDPL (2003-03)",
    desc="The government privatizes electricity distribution, aiming to stop load shedding, but consumers complain of high tariffs. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['economy', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_power_privatization", "Initiate a special government commission to resolve power_privatization issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_power_privatization", "Demand that the government address power_privatization concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_power_privatization", "Propose a joint multi-party round table to build consensus on power_privatization.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-04
ITEMS_2001_2005.append(make_news(
    key="dl2001_2003_04_slum_demolition",
    month="2003-04",
    title="Yamuna Pushta Slum Demolitions Cause Protest (2003-04)",
    desc="Large-scale eviction drives along the Yamuna riverbed to create green belts trigger intense protests from rights groups. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_slum_demolition", "Initiate a special government commission to resolve slum_demolition issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_slum_demolition", "Demand that the government address slum_demolition concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_slum_demolition", "Propose a joint multi-party round table to build consensus on slum_demolition.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-05
ITEMS_2001_2005.append(make_news(
    key="dl2001_2003_05_water_tankers",
    month="2003-05",
    title="Water Scarcity in Dwarka Sparks Tanker Mafia Clashes (2003-05)",
    desc="Rapidly developing sub-cities report severe drinking water shortages, leading to clashes over private water tanker supply. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['rural', 'governance'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_water_tankers", "Initiate a special government commission to resolve water_tankers issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_water_tankers", "Demand that the government address water_tankers concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_water_tankers", "Propose a joint multi-party round table to build consensus on water_tankers.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-06
ITEMS_2001_2005.append(make_news(
    key="dl2001_2003_06_unauthorized_colonies",
    month="2003-06",
    title="Unauthorized Colony Residents Demand Regularization (2003-06)",
    desc="Voter organizations in unregistered colonies stage rallies, demanding municipal water and sewage connections. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['politics'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("gov_action_unauthorized_colonies", "Initiate a special government commission to resolve unauthorized_colonies issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_unauthorized_colonies", "Demand that the government address unauthorized_colonies concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_unauthorized_colonies", "Propose a joint multi-party round table to build consensus on unauthorized_colonies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-07
ITEMS_2001_2005.append(make_news(
    key="dl2001_2003_07_blueline_buses",
    month="2003-07",
    title="Blueline Bus Menace Prompts Transport Department Warnings (2003-07)",
    desc="Frequent accidents involving private Blueline buses prompt calls for cancellation of private operator route permits. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_blueline_buses", "Initiate a special government commission to resolve blueline_buses issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_blueline_buses", "Demand that the government address blueline_buses concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_blueline_buses", "Propose a joint multi-party round table to build consensus on blueline_buses.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-08
ITEMS_2001_2005.append(make_news(
    key="dl2001_2003_08_industry_relocation",
    month="2003-08",
    title="Polluting Industries Ordered to Relocate Outside City Borders (2003-08)",
    desc="Supreme Court orders the closure of non-conforming hazardous factories, leading to industrial worker strikes. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['environment', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_industry_relocation", "Initiate a special government commission to resolve industry_relocation issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_industry_relocation", "Demand that the government address industry_relocation concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_industry_relocation", "Propose a joint multi-party round table to build consensus on industry_relocation.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-09
ITEMS_2001_2005.append(make_news(
    key="dl2001_2003_09_delhi_blasts",
    month="2003-09",
    title="Serial Blasts in Markets Cause Security Crisis (2003-09)",
    desc="Pre-Diwali bomb blasts in busy markets of Sarojini Nagar and Paharganj trigger a massive state-wide security alert. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['security_crisis'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("gov_action_delhi_blasts", "Initiate a special government commission to resolve delhi_blasts issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_delhi_blasts", "Demand that the government address delhi_blasts concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_delhi_blasts", "Propose a joint multi-party round table to build consensus on delhi_blasts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-10
ITEMS_2001_2005.append(make_news(
    key="dl2001_2003_10_municipal_reforms",
    month="2003-10",
    title="MCD Decentralization Debates Stall Council Work (2003-10)",
    desc="Proposals to split the Municipal Corporation of Delhi into smaller zones face opposition from local councilors. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_municipal_reforms", "Initiate a special government commission to resolve municipal_reforms issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_municipal_reforms", "Demand that the government address municipal_reforms concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_municipal_reforms", "Propose a joint multi-party round table to build consensus on municipal_reforms.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-11
ITEMS_2001_2005.append(make_news(
    key="dl2001_2003_11_flyover_boom",
    month="2003-11",
    title="Flyover Construction Boom Completed on Ring Road (2003-11)",
    desc="Sheila Dikshit's flyover push speeds up Ring Road traffic, though shopkeepers complain of construction blockades. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_flyover_boom", "Initiate a special government commission to resolve flyover_boom issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_flyover_boom", "Demand that the government address flyover_boom concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_flyover_boom", "Propose a joint multi-party round table to build consensus on flyover_boom.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-12
ITEMS_2001_2005.append(make_news(
    key="dl2001_2003_12_school_infrastructure",
    month="2003-12",
    title="Government School Improvement Program Launched (2003-12)",
    desc="Education department announces new classroom construction and computer labs in state-run secondary schools. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_school_infrastructure", "Initiate a special government commission to resolve school_infrastructure issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_school_infrastructure", "Demand that the government address school_infrastructure concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_school_infrastructure", "Propose a joint multi-party round table to build consensus on school_infrastructure.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-01
ITEMS_2001_2005.append(make_news(
    key="dl2001_2004_01_cng_transition",
    month="2004-01",
    title="CNG Transition Mandate Triggers Public Transport Crisis (2004-01)",
    desc="The Supreme Court mandate forcing commercial vehicles to switch to CNG causes massive queues at filling stations. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure', 'environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_cng_transition", "Initiate a special government commission to resolve cng_transition issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cng_transition", "Demand that the government address cng_transition concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cng_transition", "Propose a joint multi-party round table to build consensus on cng_transition.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-02
ITEMS_2001_2005.append(make_news(
    key="dl2001_2004_02_metro_phase_1",
    month="2004-02",
    title="Delhi Metro Phase 1 Trials Begin on Shahdara-Tis Hazari Line (2004-02)",
    desc="The first passenger trial runs on Delhi's new elevated metro corridor draw major crowds and political attention. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_metro_phase_1", "Initiate a special government commission to resolve metro_phase_1 issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_metro_phase_1", "Demand that the government address metro_phase_1 concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_metro_phase_1", "Propose a joint multi-party round table to build consensus on metro_phase_1.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-03
ITEMS_2001_2005.append(make_news(
    key="dl2001_2004_03_power_privatization",
    month="2004-03",
    title="Power Distribution Privatized to BSES and NDPL (2004-03)",
    desc="The government privatizes electricity distribution, aiming to stop load shedding, but consumers complain of high tariffs. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['economy', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_power_privatization", "Initiate a special government commission to resolve power_privatization issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_power_privatization", "Demand that the government address power_privatization concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_power_privatization", "Propose a joint multi-party round table to build consensus on power_privatization.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-04
ITEMS_2001_2005.append(make_news(
    key="dl2001_2004_04_slum_demolition",
    month="2004-04",
    title="Yamuna Pushta Slum Demolitions Cause Protest (2004-04)",
    desc="Large-scale eviction drives along the Yamuna riverbed to create green belts trigger intense protests from rights groups. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_slum_demolition", "Initiate a special government commission to resolve slum_demolition issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_slum_demolition", "Demand that the government address slum_demolition concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_slum_demolition", "Propose a joint multi-party round table to build consensus on slum_demolition.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-05
ITEMS_2001_2005.append(make_news(
    key="dl2001_2004_05_water_tankers",
    month="2004-05",
    title="Water Scarcity in Dwarka Sparks Tanker Mafia Clashes (2004-05)",
    desc="Rapidly developing sub-cities report severe drinking water shortages, leading to clashes over private water tanker supply. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['rural', 'governance'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_water_tankers", "Initiate a special government commission to resolve water_tankers issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_water_tankers", "Demand that the government address water_tankers concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_water_tankers", "Propose a joint multi-party round table to build consensus on water_tankers.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-06
ITEMS_2001_2005.append(make_news(
    key="dl2001_2004_06_unauthorized_colonies",
    month="2004-06",
    title="Unauthorized Colony Residents Demand Regularization (2004-06)",
    desc="Voter organizations in unregistered colonies stage rallies, demanding municipal water and sewage connections. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['politics'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("gov_action_unauthorized_colonies", "Initiate a special government commission to resolve unauthorized_colonies issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_unauthorized_colonies", "Demand that the government address unauthorized_colonies concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_unauthorized_colonies", "Propose a joint multi-party round table to build consensus on unauthorized_colonies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-07
ITEMS_2001_2005.append(make_news(
    key="dl2001_2004_07_blueline_buses",
    month="2004-07",
    title="Blueline Bus Menace Prompts Transport Department Warnings (2004-07)",
    desc="Frequent accidents involving private Blueline buses prompt calls for cancellation of private operator route permits. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_blueline_buses", "Initiate a special government commission to resolve blueline_buses issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_blueline_buses", "Demand that the government address blueline_buses concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_blueline_buses", "Propose a joint multi-party round table to build consensus on blueline_buses.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-08
ITEMS_2001_2005.append(make_news(
    key="dl2001_2004_08_industry_relocation",
    month="2004-08",
    title="Polluting Industries Ordered to Relocate Outside City Borders (2004-08)",
    desc="Supreme Court orders the closure of non-conforming hazardous factories, leading to industrial worker strikes. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['environment', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_industry_relocation", "Initiate a special government commission to resolve industry_relocation issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_industry_relocation", "Demand that the government address industry_relocation concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_industry_relocation", "Propose a joint multi-party round table to build consensus on industry_relocation.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-09
ITEMS_2001_2005.append(make_news(
    key="dl2001_2004_09_delhi_blasts",
    month="2004-09",
    title="Serial Blasts in Markets Cause Security Crisis (2004-09)",
    desc="Pre-Diwali bomb blasts in busy markets of Sarojini Nagar and Paharganj trigger a massive state-wide security alert. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['security_crisis'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("gov_action_delhi_blasts", "Initiate a special government commission to resolve delhi_blasts issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_delhi_blasts", "Demand that the government address delhi_blasts concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_delhi_blasts", "Propose a joint multi-party round table to build consensus on delhi_blasts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-10
ITEMS_2001_2005.append(make_news(
    key="dl2001_2004_10_municipal_reforms",
    month="2004-10",
    title="MCD Decentralization Debates Stall Council Work (2004-10)",
    desc="Proposals to split the Municipal Corporation of Delhi into smaller zones face opposition from local councilors. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_municipal_reforms", "Initiate a special government commission to resolve municipal_reforms issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_municipal_reforms", "Demand that the government address municipal_reforms concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_municipal_reforms", "Propose a joint multi-party round table to build consensus on municipal_reforms.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-11
ITEMS_2001_2005.append(make_news(
    key="dl2001_2004_11_flyover_boom",
    month="2004-11",
    title="Flyover Construction Boom Completed on Ring Road (2004-11)",
    desc="Sheila Dikshit's flyover push speeds up Ring Road traffic, though shopkeepers complain of construction blockades. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_flyover_boom", "Initiate a special government commission to resolve flyover_boom issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_flyover_boom", "Demand that the government address flyover_boom concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_flyover_boom", "Propose a joint multi-party round table to build consensus on flyover_boom.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-12
ITEMS_2001_2005.append(make_news(
    key="dl2001_2004_12_school_infrastructure",
    month="2004-12",
    title="Government School Improvement Program Launched (2004-12)",
    desc="Education department announces new classroom construction and computer labs in state-run secondary schools. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_school_infrastructure", "Initiate a special government commission to resolve school_infrastructure issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_school_infrastructure", "Demand that the government address school_infrastructure concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_school_infrastructure", "Propose a joint multi-party round table to build consensus on school_infrastructure.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-01
ITEMS_2001_2005.append(make_news(
    key="dl2001_2005_01_cng_transition",
    month="2005-01",
    title="CNG Transition Mandate Triggers Public Transport Crisis (2005-01)",
    desc="The Supreme Court mandate forcing commercial vehicles to switch to CNG causes massive queues at filling stations. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure', 'environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_cng_transition", "Initiate a special government commission to resolve cng_transition issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_cng_transition", "Demand that the government address cng_transition concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_cng_transition", "Propose a joint multi-party round table to build consensus on cng_transition.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-02
ITEMS_2001_2005.append(make_news(
    key="dl2001_2005_02_metro_phase_1",
    month="2005-02",
    title="Delhi Metro Phase 1 Trials Begin on Shahdara-Tis Hazari Line (2005-02)",
    desc="The first passenger trial runs on Delhi's new elevated metro corridor draw major crowds and political attention. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_metro_phase_1", "Initiate a special government commission to resolve metro_phase_1 issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_metro_phase_1", "Demand that the government address metro_phase_1 concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_metro_phase_1", "Propose a joint multi-party round table to build consensus on metro_phase_1.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-03
ITEMS_2001_2005.append(make_news(
    key="dl2001_2005_03_power_privatization",
    month="2005-03",
    title="Power Distribution Privatized to BSES and NDPL (2005-03)",
    desc="The government privatizes electricity distribution, aiming to stop load shedding, but consumers complain of high tariffs. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['economy', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_power_privatization", "Initiate a special government commission to resolve power_privatization issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_power_privatization", "Demand that the government address power_privatization concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_power_privatization", "Propose a joint multi-party round table to build consensus on power_privatization.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-04
ITEMS_2001_2005.append(make_news(
    key="dl2001_2005_04_slum_demolition",
    month="2005-04",
    title="Yamuna Pushta Slum Demolitions Cause Protest (2005-04)",
    desc="Large-scale eviction drives along the Yamuna riverbed to create green belts trigger intense protests from rights groups. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_slum_demolition", "Initiate a special government commission to resolve slum_demolition issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_slum_demolition", "Demand that the government address slum_demolition concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_slum_demolition", "Propose a joint multi-party round table to build consensus on slum_demolition.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-05
ITEMS_2001_2005.append(make_news(
    key="dl2001_2005_05_water_tankers",
    month="2005-05",
    title="Water Scarcity in Dwarka Sparks Tanker Mafia Clashes (2005-05)",
    desc="Rapidly developing sub-cities report severe drinking water shortages, leading to clashes over private water tanker supply. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['rural', 'governance'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_water_tankers", "Initiate a special government commission to resolve water_tankers issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_water_tankers", "Demand that the government address water_tankers concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_water_tankers", "Propose a joint multi-party round table to build consensus on water_tankers.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-06
ITEMS_2001_2005.append(make_news(
    key="dl2001_2005_06_unauthorized_colonies",
    month="2005-06",
    title="Unauthorized Colony Residents Demand Regularization (2005-06)",
    desc="Voter organizations in unregistered colonies stage rallies, demanding municipal water and sewage connections. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['politics'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("gov_action_unauthorized_colonies", "Initiate a special government commission to resolve unauthorized_colonies issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_unauthorized_colonies", "Demand that the government address unauthorized_colonies concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_unauthorized_colonies", "Propose a joint multi-party round table to build consensus on unauthorized_colonies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-07
ITEMS_2001_2005.append(make_news(
    key="dl2001_2005_07_blueline_buses",
    month="2005-07",
    title="Blueline Bus Menace Prompts Transport Department Warnings (2005-07)",
    desc="Frequent accidents involving private Blueline buses prompt calls for cancellation of private operator route permits. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_blueline_buses", "Initiate a special government commission to resolve blueline_buses issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_blueline_buses", "Demand that the government address blueline_buses concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_blueline_buses", "Propose a joint multi-party round table to build consensus on blueline_buses.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-08
ITEMS_2001_2005.append(make_news(
    key="dl2001_2005_08_industry_relocation",
    month="2005-08",
    title="Polluting Industries Ordered to Relocate Outside City Borders (2005-08)",
    desc="Supreme Court orders the closure of non-conforming hazardous factories, leading to industrial worker strikes. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['environment', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_industry_relocation", "Initiate a special government commission to resolve industry_relocation issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_industry_relocation", "Demand that the government address industry_relocation concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_industry_relocation", "Propose a joint multi-party round table to build consensus on industry_relocation.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-09
ITEMS_2001_2005.append(make_news(
    key="dl2001_2005_09_delhi_blasts",
    month="2005-09",
    title="Serial Blasts in Markets Cause Security Crisis (2005-09)",
    desc="Pre-Diwali bomb blasts in busy markets of Sarojini Nagar and Paharganj trigger a massive state-wide security alert. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['security_crisis'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("gov_action_delhi_blasts", "Initiate a special government commission to resolve delhi_blasts issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_delhi_blasts", "Demand that the government address delhi_blasts concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_delhi_blasts", "Propose a joint multi-party round table to build consensus on delhi_blasts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-10
ITEMS_2001_2005.append(make_news(
    key="dl2001_2005_10_municipal_reforms",
    month="2005-10",
    title="MCD Decentralization Debates Stall Council Work (2005-10)",
    desc="Proposals to split the Municipal Corporation of Delhi into smaller zones face opposition from local councilors. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_municipal_reforms", "Initiate a special government commission to resolve municipal_reforms issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_municipal_reforms", "Demand that the government address municipal_reforms concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_municipal_reforms", "Propose a joint multi-party round table to build consensus on municipal_reforms.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-11
ITEMS_2001_2005.append(make_news(
    key="dl2001_2005_11_flyover_boom",
    month="2005-11",
    title="Flyover Construction Boom Completed on Ring Road (2005-11)",
    desc="Sheila Dikshit's flyover push speeds up Ring Road traffic, though shopkeepers complain of construction blockades. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_flyover_boom", "Initiate a special government commission to resolve flyover_boom issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_flyover_boom", "Demand that the government address flyover_boom concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_flyover_boom", "Propose a joint multi-party round table to build consensus on flyover_boom.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-12
ITEMS_2001_2005.append(make_news(
    key="dl2001_2005_12_school_infrastructure",
    month="2005-12",
    title="Government School Improvement Program Launched (2005-12)",
    desc="Education department announces new classroom construction and computer labs in state-run secondary schools. In Delhi, this monthly event shapes key NCT urban development debates.",
    tags=['governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_school_infrastructure", "Initiate a special government commission to resolve school_infrastructure issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_school_infrastructure", "Demand that the government address school_infrastructure concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_school_infrastructure", "Propose a joint multi-party round table to build consensus on school_infrastructure.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"delhiUrbanStabilityMemory": 2}, weight=0.2)
    ]
))

