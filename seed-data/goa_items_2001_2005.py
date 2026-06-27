from helper import reaction, no_comment, make_news, eff, risk

ITEMS_2001_2005 = []

# 2001-01
ITEMS_2001_2005.append(make_news(
    key="ga2001_2001_01_tourism_growth",
    month="2001-01",
    title="Foreign Tourist Arrivals Surge Along Coastal Belts (2001-01)",
    desc="Charter flights from Europe increase, bringing high foreign tourist footfall. Shack owners demand simplified seasonal permits. In Goa, this monthly event shapes key regional debates.",
    tags=['tourism', 'economy'],
    base_w=1.15, profile="economy",
    reactions=[
        reaction("gov_action_tourism_growth", "Initiate a special government commission to resolve tourism_growth issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_tourism_growth", "Demand that the government address tourism_growth concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_tourism_growth", "Propose a joint multi-party round table to build consensus on tourism_growth.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-02
ITEMS_2001_2005.append(make_news(
    key="ga2001_2001_02_mining_disputes",
    month="2001-02",
    title="Iron Ore Transport Barge Operators Launch Strike (2001-02)",
    desc="Barge operators on the Mandovi river strike over shipping rates, halting iron ore transport to Mormugao port. In Goa, this monthly event shapes key regional debates.",
    tags=['economy', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_mining_disputes", "Initiate a special government commission to resolve mining_disputes issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mining_disputes", "Demand that the government address mining_disputes concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mining_disputes", "Propose a joint multi-party round table to build consensus on mining_disputes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-03
ITEMS_2001_2005.append(make_news(
    key="ga2001_2001_03_political_alliance",
    month="2001-03",
    title="MGP and Congress Hold Cabinet Coordination Talks (2001-03)",
    desc="Goa's coalition partners hold crucial talks to ensure stability amid rumors of opposition horse-trading. In Goa, this monthly event shapes key regional debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_political_alliance", "Initiate a special government commission to resolve political_alliance issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_political_alliance", "Demand that the government address political_alliance concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_political_alliance", "Propose a joint multi-party round table to build consensus on political_alliance.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-04
ITEMS_2001_2005.append(make_news(
    key="ga2001_2001_04_crz_violations",
    month="2001-04",
    title="Coastal Regulation Zone Violations Draw Court Focus (2001-04)",
    desc="The High Court issues notices to beachfront resorts violating the 200-meter no-development zone guidelines. In Goa, this monthly event shapes key regional debates.",
    tags=['environment', 'governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_crz_violations", "Initiate a special government commission to resolve crz_violations issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_crz_violations", "Demand that the government address crz_violations concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_crz_violations", "Propose a joint multi-party round table to build consensus on crz_violations.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-05
ITEMS_2001_2005.append(make_news(
    key="ga2001_2001_05_infrastructure_zuari",
    month="2001-05",
    title="Zuari Bridge Repairs Restrict Heavy Vehicle Movement (2001-05)",
    desc="Aging infrastructure forces the government to restrict heavy commercial vehicles on the vital Zuari bridge. In Goa, this monthly event shapes key regional debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_infrastructure_zuari", "Initiate a special government commission to resolve infrastructure_zuari issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_infrastructure_zuari", "Demand that the government address infrastructure_zuari concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_infrastructure_zuari", "Propose a joint multi-party round table to build consensus on infrastructure_zuari.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-06
ITEMS_2001_2005.append(make_news(
    key="ga2001_2001_06_garbage_sonsodo",
    month="2001-06",
    title="Sonsodo Garbage Dump Fires Trigger Local Outrage (2001-06)",
    desc="Unmanaged municipal waste at the Sonsodo site in Margao catches fire, causing health concerns and protests. In Goa, this monthly event shapes key regional debates.",
    tags=['protest', 'environment'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_garbage_sonsodo", "Initiate a special government commission to resolve garbage_sonsodo issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_garbage_sonsodo", "Demand that the government address garbage_sonsodo concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_garbage_sonsodo", "Propose a joint multi-party round table to build consensus on garbage_sonsodo.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-07
ITEMS_2001_2005.append(make_news(
    key="ga2001_2001_07_panchayat_reservations",
    month="2001-07",
    title="Panchayat Election Ward Reservations Finalized (2001-07)",
    desc="The State Election Commission announces block ward reservations, sparking protests from local political rivals. In Goa, this monthly event shapes key regional debates.",
    tags=['election', 'politics'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("gov_action_panchayat_reservations", "Initiate a special government commission to resolve panchayat_reservations issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_panchayat_reservations", "Demand that the government address panchayat_reservations concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_panchayat_reservations", "Propose a joint multi-party round table to build consensus on panchayat_reservations.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-08
ITEMS_2001_2005.append(make_news(
    key="ga2001_2001_08_portuguese_heritage",
    month="2001-08",
    title="Conservationists Seek Funding for Old Goa Heritage Sites (2001-08)",
    desc="NGOs and church groups appeal for state-funded restorations of deteriorating UNESCO heritage structures. In Goa, this monthly event shapes key regional debates.",
    tags=['identity', 'tourism'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_portuguese_heritage", "Initiate a special government commission to resolve portuguese_heritage issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_portuguese_heritage", "Demand that the government address portuguese_heritage concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_portuguese_heritage", "Propose a joint multi-party round table to build consensus on portuguese_heritage.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-09
ITEMS_2001_2005.append(make_news(
    key="ga2001_2001_09_fishermen_clash",
    month="2001-09",
    title="Tensions Erupt Between Traditional Fishermen and Trawlers (2001-09)",
    desc="Traditional Ramponkar fishermen block jetties, protesting against illegal night-trawling by mechanized boats. In Goa, this monthly event shapes key regional debates.",
    tags=['protest', 'economy'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_fishermen_clash", "Initiate a special government commission to resolve fishermen_clash issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_fishermen_clash", "Demand that the government address fishermen_clash concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_fishermen_clash", "Propose a joint multi-party round table to build consensus on fishermen_clash.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-10
ITEMS_2001_2005.append(make_news(
    key="ga2001_2001_10_sez_scam",
    month="2001-10",
    title="Industrial Land Allotments Trigger Land Scam Accusations (2001-10)",
    desc="Opposition parties accuse the cabinet of allotting premium industrial plots in Verna to shell companies. In Goa, this monthly event shapes key regional debates.",
    tags=['governance', 'corruption'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_sez_scam", "Initiate a special government commission to resolve sez_scam issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_sez_scam", "Demand that the government address sez_scam concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_sez_scam", "Propose a joint multi-party round table to build consensus on sez_scam.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-11
ITEMS_2001_2005.append(make_news(
    key="ga2001_2001_11_mining_royalties",
    month="2001-11",
    title="Village Panchayats Demand Share of Iron Ore Royalties (2001-11)",
    desc="Sanguem and Bicholim village councils demand direct funding from mining companies to fix broken rural roads. In Goa, this monthly event shapes key regional debates.",
    tags=['rural', 'economy'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_mining_royalties", "Initiate a special government commission to resolve mining_royalties issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mining_royalties", "Demand that the government address mining_royalties concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mining_royalties", "Propose a joint multi-party round table to build consensus on mining_royalties.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-12
ITEMS_2001_2005.append(make_news(
    key="ga2001_2001_12_konkan_railway",
    month="2001-12",
    title="Konkan Railway Expansion Plans Draw Land Use Debates (2001-12)",
    desc="Farmers protest double-tracking plans, citing destruction of khazan agricultural lands and water channels. In Goa, this monthly event shapes key regional debates.",
    tags=['infrastructure', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_konkan_railway", "Initiate a special government commission to resolve konkan_railway issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_konkan_railway", "Demand that the government address konkan_railway concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_konkan_railway", "Propose a joint multi-party round table to build consensus on konkan_railway.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-01
ITEMS_2001_2005.append(make_news(
    key="ga2001_2002_01_tourism_growth",
    month="2002-01",
    title="Foreign Tourist Arrivals Surge Along Coastal Belts (2002-01)",
    desc="Charter flights from Europe increase, bringing high foreign tourist footfall. Shack owners demand simplified seasonal permits. In Goa, this monthly event shapes key regional debates.",
    tags=['tourism', 'economy'],
    base_w=1.15, profile="economy",
    reactions=[
        reaction("gov_action_tourism_growth", "Initiate a special government commission to resolve tourism_growth issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_tourism_growth", "Demand that the government address tourism_growth concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_tourism_growth", "Propose a joint multi-party round table to build consensus on tourism_growth.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-02
ITEMS_2001_2005.append(make_news(
    key="ga2001_2002_02_mining_disputes",
    month="2002-02",
    title="Iron Ore Transport Barge Operators Launch Strike (2002-02)",
    desc="Barge operators on the Mandovi river strike over shipping rates, halting iron ore transport to Mormugao port. In Goa, this monthly event shapes key regional debates.",
    tags=['economy', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_mining_disputes", "Initiate a special government commission to resolve mining_disputes issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mining_disputes", "Demand that the government address mining_disputes concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mining_disputes", "Propose a joint multi-party round table to build consensus on mining_disputes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-03
ITEMS_2001_2005.append(make_news(
    key="ga2001_2002_03_political_alliance",
    month="2002-03",
    title="MGP and Congress Hold Cabinet Coordination Talks (2002-03)",
    desc="Goa's coalition partners hold crucial talks to ensure stability amid rumors of opposition horse-trading. In Goa, this monthly event shapes key regional debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_political_alliance", "Initiate a special government commission to resolve political_alliance issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_political_alliance", "Demand that the government address political_alliance concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_political_alliance", "Propose a joint multi-party round table to build consensus on political_alliance.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-04
ITEMS_2001_2005.append(make_news(
    key="ga2001_2002_04_crz_violations",
    month="2002-04",
    title="Coastal Regulation Zone Violations Draw Court Focus (2002-04)",
    desc="The High Court issues notices to beachfront resorts violating the 200-meter no-development zone guidelines. In Goa, this monthly event shapes key regional debates.",
    tags=['environment', 'governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_crz_violations", "Initiate a special government commission to resolve crz_violations issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_crz_violations", "Demand that the government address crz_violations concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_crz_violations", "Propose a joint multi-party round table to build consensus on crz_violations.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-05
ITEMS_2001_2005.append(make_news(
    key="ga2001_2002_05_infrastructure_zuari",
    month="2002-05",
    title="Zuari Bridge Repairs Restrict Heavy Vehicle Movement (2002-05)",
    desc="Aging infrastructure forces the government to restrict heavy commercial vehicles on the vital Zuari bridge. In Goa, this monthly event shapes key regional debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_infrastructure_zuari", "Initiate a special government commission to resolve infrastructure_zuari issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_infrastructure_zuari", "Demand that the government address infrastructure_zuari concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_infrastructure_zuari", "Propose a joint multi-party round table to build consensus on infrastructure_zuari.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-06
ITEMS_2001_2005.append(make_news(
    key="ga2001_2002_06_garbage_sonsodo",
    month="2002-06",
    title="Sonsodo Garbage Dump Fires Trigger Local Outrage (2002-06)",
    desc="Unmanaged municipal waste at the Sonsodo site in Margao catches fire, causing health concerns and protests. In Goa, this monthly event shapes key regional debates.",
    tags=['protest', 'environment'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_garbage_sonsodo", "Initiate a special government commission to resolve garbage_sonsodo issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_garbage_sonsodo", "Demand that the government address garbage_sonsodo concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_garbage_sonsodo", "Propose a joint multi-party round table to build consensus on garbage_sonsodo.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-07
ITEMS_2001_2005.append(make_news(
    key="ga2001_2002_07_panchayat_reservations",
    month="2002-07",
    title="Panchayat Election Ward Reservations Finalized (2002-07)",
    desc="The State Election Commission announces block ward reservations, sparking protests from local political rivals. In Goa, this monthly event shapes key regional debates.",
    tags=['election', 'politics'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("gov_action_panchayat_reservations", "Initiate a special government commission to resolve panchayat_reservations issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_panchayat_reservations", "Demand that the government address panchayat_reservations concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_panchayat_reservations", "Propose a joint multi-party round table to build consensus on panchayat_reservations.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-08
ITEMS_2001_2005.append(make_news(
    key="ga2001_2002_08_portuguese_heritage",
    month="2002-08",
    title="Conservationists Seek Funding for Old Goa Heritage Sites (2002-08)",
    desc="NGOs and church groups appeal for state-funded restorations of deteriorating UNESCO heritage structures. In Goa, this monthly event shapes key regional debates.",
    tags=['identity', 'tourism'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_portuguese_heritage", "Initiate a special government commission to resolve portuguese_heritage issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_portuguese_heritage", "Demand that the government address portuguese_heritage concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_portuguese_heritage", "Propose a joint multi-party round table to build consensus on portuguese_heritage.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-09
ITEMS_2001_2005.append(make_news(
    key="ga2001_2002_09_fishermen_clash",
    month="2002-09",
    title="Tensions Erupt Between Traditional Fishermen and Trawlers (2002-09)",
    desc="Traditional Ramponkar fishermen block jetties, protesting against illegal night-trawling by mechanized boats. In Goa, this monthly event shapes key regional debates.",
    tags=['protest', 'economy'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_fishermen_clash", "Initiate a special government commission to resolve fishermen_clash issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_fishermen_clash", "Demand that the government address fishermen_clash concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_fishermen_clash", "Propose a joint multi-party round table to build consensus on fishermen_clash.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-10
ITEMS_2001_2005.append(make_news(
    key="ga2001_2002_10_sez_scam",
    month="2002-10",
    title="Industrial Land Allotments Trigger Land Scam Accusations (2002-10)",
    desc="Opposition parties accuse the cabinet of allotting premium industrial plots in Verna to shell companies. In Goa, this monthly event shapes key regional debates.",
    tags=['governance', 'corruption'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_sez_scam", "Initiate a special government commission to resolve sez_scam issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_sez_scam", "Demand that the government address sez_scam concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_sez_scam", "Propose a joint multi-party round table to build consensus on sez_scam.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-11
ITEMS_2001_2005.append(make_news(
    key="ga2001_2002_11_mining_royalties",
    month="2002-11",
    title="Village Panchayats Demand Share of Iron Ore Royalties (2002-11)",
    desc="Sanguem and Bicholim village councils demand direct funding from mining companies to fix broken rural roads. In Goa, this monthly event shapes key regional debates.",
    tags=['rural', 'economy'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_mining_royalties", "Initiate a special government commission to resolve mining_royalties issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mining_royalties", "Demand that the government address mining_royalties concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mining_royalties", "Propose a joint multi-party round table to build consensus on mining_royalties.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2002-12
ITEMS_2001_2005.append(make_news(
    key="ga2001_2002_12_konkan_railway",
    month="2002-12",
    title="Konkan Railway Expansion Plans Draw Land Use Debates (2002-12)",
    desc="Farmers protest double-tracking plans, citing destruction of khazan agricultural lands and water channels. In Goa, this monthly event shapes key regional debates.",
    tags=['infrastructure', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_konkan_railway", "Initiate a special government commission to resolve konkan_railway issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_konkan_railway", "Demand that the government address konkan_railway concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_konkan_railway", "Propose a joint multi-party round table to build consensus on konkan_railway.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-01
ITEMS_2001_2005.append(make_news(
    key="ga2001_2003_01_tourism_growth",
    month="2003-01",
    title="Foreign Tourist Arrivals Surge Along Coastal Belts (2003-01)",
    desc="Charter flights from Europe increase, bringing high foreign tourist footfall. Shack owners demand simplified seasonal permits. In Goa, this monthly event shapes key regional debates.",
    tags=['tourism', 'economy'],
    base_w=1.15, profile="economy",
    reactions=[
        reaction("gov_action_tourism_growth", "Initiate a special government commission to resolve tourism_growth issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_tourism_growth", "Demand that the government address tourism_growth concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_tourism_growth", "Propose a joint multi-party round table to build consensus on tourism_growth.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-02
ITEMS_2001_2005.append(make_news(
    key="ga2001_2003_02_mining_disputes",
    month="2003-02",
    title="Iron Ore Transport Barge Operators Launch Strike (2003-02)",
    desc="Barge operators on the Mandovi river strike over shipping rates, halting iron ore transport to Mormugao port. In Goa, this monthly event shapes key regional debates.",
    tags=['economy', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_mining_disputes", "Initiate a special government commission to resolve mining_disputes issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mining_disputes", "Demand that the government address mining_disputes concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mining_disputes", "Propose a joint multi-party round table to build consensus on mining_disputes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-03
ITEMS_2001_2005.append(make_news(
    key="ga2001_2003_03_political_alliance",
    month="2003-03",
    title="MGP and Congress Hold Cabinet Coordination Talks (2003-03)",
    desc="Goa's coalition partners hold crucial talks to ensure stability amid rumors of opposition horse-trading. In Goa, this monthly event shapes key regional debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_political_alliance", "Initiate a special government commission to resolve political_alliance issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_political_alliance", "Demand that the government address political_alliance concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_political_alliance", "Propose a joint multi-party round table to build consensus on political_alliance.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-04
ITEMS_2001_2005.append(make_news(
    key="ga2001_2003_04_crz_violations",
    month="2003-04",
    title="Coastal Regulation Zone Violations Draw Court Focus (2003-04)",
    desc="The High Court issues notices to beachfront resorts violating the 200-meter no-development zone guidelines. In Goa, this monthly event shapes key regional debates.",
    tags=['environment', 'governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_crz_violations", "Initiate a special government commission to resolve crz_violations issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_crz_violations", "Demand that the government address crz_violations concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_crz_violations", "Propose a joint multi-party round table to build consensus on crz_violations.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-05
ITEMS_2001_2005.append(make_news(
    key="ga2001_2003_05_infrastructure_zuari",
    month="2003-05",
    title="Zuari Bridge Repairs Restrict Heavy Vehicle Movement (2003-05)",
    desc="Aging infrastructure forces the government to restrict heavy commercial vehicles on the vital Zuari bridge. In Goa, this monthly event shapes key regional debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_infrastructure_zuari", "Initiate a special government commission to resolve infrastructure_zuari issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_infrastructure_zuari", "Demand that the government address infrastructure_zuari concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_infrastructure_zuari", "Propose a joint multi-party round table to build consensus on infrastructure_zuari.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-06
ITEMS_2001_2005.append(make_news(
    key="ga2001_2003_06_garbage_sonsodo",
    month="2003-06",
    title="Sonsodo Garbage Dump Fires Trigger Local Outrage (2003-06)",
    desc="Unmanaged municipal waste at the Sonsodo site in Margao catches fire, causing health concerns and protests. In Goa, this monthly event shapes key regional debates.",
    tags=['protest', 'environment'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_garbage_sonsodo", "Initiate a special government commission to resolve garbage_sonsodo issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_garbage_sonsodo", "Demand that the government address garbage_sonsodo concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_garbage_sonsodo", "Propose a joint multi-party round table to build consensus on garbage_sonsodo.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-07
ITEMS_2001_2005.append(make_news(
    key="ga2001_2003_07_panchayat_reservations",
    month="2003-07",
    title="Panchayat Election Ward Reservations Finalized (2003-07)",
    desc="The State Election Commission announces block ward reservations, sparking protests from local political rivals. In Goa, this monthly event shapes key regional debates.",
    tags=['election', 'politics'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("gov_action_panchayat_reservations", "Initiate a special government commission to resolve panchayat_reservations issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_panchayat_reservations", "Demand that the government address panchayat_reservations concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_panchayat_reservations", "Propose a joint multi-party round table to build consensus on panchayat_reservations.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-08
ITEMS_2001_2005.append(make_news(
    key="ga2001_2003_08_portuguese_heritage",
    month="2003-08",
    title="Conservationists Seek Funding for Old Goa Heritage Sites (2003-08)",
    desc="NGOs and church groups appeal for state-funded restorations of deteriorating UNESCO heritage structures. In Goa, this monthly event shapes key regional debates.",
    tags=['identity', 'tourism'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_portuguese_heritage", "Initiate a special government commission to resolve portuguese_heritage issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_portuguese_heritage", "Demand that the government address portuguese_heritage concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_portuguese_heritage", "Propose a joint multi-party round table to build consensus on portuguese_heritage.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-09
ITEMS_2001_2005.append(make_news(
    key="ga2001_2003_09_fishermen_clash",
    month="2003-09",
    title="Tensions Erupt Between Traditional Fishermen and Trawlers (2003-09)",
    desc="Traditional Ramponkar fishermen block jetties, protesting against illegal night-trawling by mechanized boats. In Goa, this monthly event shapes key regional debates.",
    tags=['protest', 'economy'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_fishermen_clash", "Initiate a special government commission to resolve fishermen_clash issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_fishermen_clash", "Demand that the government address fishermen_clash concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_fishermen_clash", "Propose a joint multi-party round table to build consensus on fishermen_clash.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-10
ITEMS_2001_2005.append(make_news(
    key="ga2001_2003_10_sez_scam",
    month="2003-10",
    title="Industrial Land Allotments Trigger Land Scam Accusations (2003-10)",
    desc="Opposition parties accuse the cabinet of allotting premium industrial plots in Verna to shell companies. In Goa, this monthly event shapes key regional debates.",
    tags=['governance', 'corruption'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_sez_scam", "Initiate a special government commission to resolve sez_scam issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_sez_scam", "Demand that the government address sez_scam concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_sez_scam", "Propose a joint multi-party round table to build consensus on sez_scam.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-11
ITEMS_2001_2005.append(make_news(
    key="ga2001_2003_11_mining_royalties",
    month="2003-11",
    title="Village Panchayats Demand Share of Iron Ore Royalties (2003-11)",
    desc="Sanguem and Bicholim village councils demand direct funding from mining companies to fix broken rural roads. In Goa, this monthly event shapes key regional debates.",
    tags=['rural', 'economy'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_mining_royalties", "Initiate a special government commission to resolve mining_royalties issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mining_royalties", "Demand that the government address mining_royalties concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mining_royalties", "Propose a joint multi-party round table to build consensus on mining_royalties.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2003-12
ITEMS_2001_2005.append(make_news(
    key="ga2001_2003_12_konkan_railway",
    month="2003-12",
    title="Konkan Railway Expansion Plans Draw Land Use Debates (2003-12)",
    desc="Farmers protest double-tracking plans, citing destruction of khazan agricultural lands and water channels. In Goa, this monthly event shapes key regional debates.",
    tags=['infrastructure', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_konkan_railway", "Initiate a special government commission to resolve konkan_railway issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_konkan_railway", "Demand that the government address konkan_railway concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_konkan_railway", "Propose a joint multi-party round table to build consensus on konkan_railway.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-01
ITEMS_2001_2005.append(make_news(
    key="ga2001_2004_01_tourism_growth",
    month="2004-01",
    title="Foreign Tourist Arrivals Surge Along Coastal Belts (2004-01)",
    desc="Charter flights from Europe increase, bringing high foreign tourist footfall. Shack owners demand simplified seasonal permits. In Goa, this monthly event shapes key regional debates.",
    tags=['tourism', 'economy'],
    base_w=1.15, profile="economy",
    reactions=[
        reaction("gov_action_tourism_growth", "Initiate a special government commission to resolve tourism_growth issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_tourism_growth", "Demand that the government address tourism_growth concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_tourism_growth", "Propose a joint multi-party round table to build consensus on tourism_growth.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-02
ITEMS_2001_2005.append(make_news(
    key="ga2001_2004_02_mining_disputes",
    month="2004-02",
    title="Iron Ore Transport Barge Operators Launch Strike (2004-02)",
    desc="Barge operators on the Mandovi river strike over shipping rates, halting iron ore transport to Mormugao port. In Goa, this monthly event shapes key regional debates.",
    tags=['economy', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_mining_disputes", "Initiate a special government commission to resolve mining_disputes issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mining_disputes", "Demand that the government address mining_disputes concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mining_disputes", "Propose a joint multi-party round table to build consensus on mining_disputes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-03
ITEMS_2001_2005.append(make_news(
    key="ga2001_2004_03_political_alliance",
    month="2004-03",
    title="MGP and Congress Hold Cabinet Coordination Talks (2004-03)",
    desc="Goa's coalition partners hold crucial talks to ensure stability amid rumors of opposition horse-trading. In Goa, this monthly event shapes key regional debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_political_alliance", "Initiate a special government commission to resolve political_alliance issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_political_alliance", "Demand that the government address political_alliance concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_political_alliance", "Propose a joint multi-party round table to build consensus on political_alliance.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-04
ITEMS_2001_2005.append(make_news(
    key="ga2001_2004_04_crz_violations",
    month="2004-04",
    title="Coastal Regulation Zone Violations Draw Court Focus (2004-04)",
    desc="The High Court issues notices to beachfront resorts violating the 200-meter no-development zone guidelines. In Goa, this monthly event shapes key regional debates.",
    tags=['environment', 'governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_crz_violations", "Initiate a special government commission to resolve crz_violations issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_crz_violations", "Demand that the government address crz_violations concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_crz_violations", "Propose a joint multi-party round table to build consensus on crz_violations.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-05
ITEMS_2001_2005.append(make_news(
    key="ga2001_2004_05_infrastructure_zuari",
    month="2004-05",
    title="Zuari Bridge Repairs Restrict Heavy Vehicle Movement (2004-05)",
    desc="Aging infrastructure forces the government to restrict heavy commercial vehicles on the vital Zuari bridge. In Goa, this monthly event shapes key regional debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_infrastructure_zuari", "Initiate a special government commission to resolve infrastructure_zuari issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_infrastructure_zuari", "Demand that the government address infrastructure_zuari concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_infrastructure_zuari", "Propose a joint multi-party round table to build consensus on infrastructure_zuari.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-06
ITEMS_2001_2005.append(make_news(
    key="ga2001_2004_06_garbage_sonsodo",
    month="2004-06",
    title="Sonsodo Garbage Dump Fires Trigger Local Outrage (2004-06)",
    desc="Unmanaged municipal waste at the Sonsodo site in Margao catches fire, causing health concerns and protests. In Goa, this monthly event shapes key regional debates.",
    tags=['protest', 'environment'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_garbage_sonsodo", "Initiate a special government commission to resolve garbage_sonsodo issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_garbage_sonsodo", "Demand that the government address garbage_sonsodo concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_garbage_sonsodo", "Propose a joint multi-party round table to build consensus on garbage_sonsodo.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-07
ITEMS_2001_2005.append(make_news(
    key="ga2001_2004_07_panchayat_reservations",
    month="2004-07",
    title="Panchayat Election Ward Reservations Finalized (2004-07)",
    desc="The State Election Commission announces block ward reservations, sparking protests from local political rivals. In Goa, this monthly event shapes key regional debates.",
    tags=['election', 'politics'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("gov_action_panchayat_reservations", "Initiate a special government commission to resolve panchayat_reservations issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_panchayat_reservations", "Demand that the government address panchayat_reservations concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_panchayat_reservations", "Propose a joint multi-party round table to build consensus on panchayat_reservations.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-08
ITEMS_2001_2005.append(make_news(
    key="ga2001_2004_08_portuguese_heritage",
    month="2004-08",
    title="Conservationists Seek Funding for Old Goa Heritage Sites (2004-08)",
    desc="NGOs and church groups appeal for state-funded restorations of deteriorating UNESCO heritage structures. In Goa, this monthly event shapes key regional debates.",
    tags=['identity', 'tourism'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_portuguese_heritage", "Initiate a special government commission to resolve portuguese_heritage issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_portuguese_heritage", "Demand that the government address portuguese_heritage concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_portuguese_heritage", "Propose a joint multi-party round table to build consensus on portuguese_heritage.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-09
ITEMS_2001_2005.append(make_news(
    key="ga2001_2004_09_fishermen_clash",
    month="2004-09",
    title="Tensions Erupt Between Traditional Fishermen and Trawlers (2004-09)",
    desc="Traditional Ramponkar fishermen block jetties, protesting against illegal night-trawling by mechanized boats. In Goa, this monthly event shapes key regional debates.",
    tags=['protest', 'economy'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_fishermen_clash", "Initiate a special government commission to resolve fishermen_clash issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_fishermen_clash", "Demand that the government address fishermen_clash concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_fishermen_clash", "Propose a joint multi-party round table to build consensus on fishermen_clash.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-10
ITEMS_2001_2005.append(make_news(
    key="ga2001_2004_10_sez_scam",
    month="2004-10",
    title="Industrial Land Allotments Trigger Land Scam Accusations (2004-10)",
    desc="Opposition parties accuse the cabinet of allotting premium industrial plots in Verna to shell companies. In Goa, this monthly event shapes key regional debates.",
    tags=['governance', 'corruption'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_sez_scam", "Initiate a special government commission to resolve sez_scam issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_sez_scam", "Demand that the government address sez_scam concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_sez_scam", "Propose a joint multi-party round table to build consensus on sez_scam.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-11
ITEMS_2001_2005.append(make_news(
    key="ga2001_2004_11_mining_royalties",
    month="2004-11",
    title="Village Panchayats Demand Share of Iron Ore Royalties (2004-11)",
    desc="Sanguem and Bicholim village councils demand direct funding from mining companies to fix broken rural roads. In Goa, this monthly event shapes key regional debates.",
    tags=['rural', 'economy'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_mining_royalties", "Initiate a special government commission to resolve mining_royalties issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mining_royalties", "Demand that the government address mining_royalties concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mining_royalties", "Propose a joint multi-party round table to build consensus on mining_royalties.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2004-12
ITEMS_2001_2005.append(make_news(
    key="ga2001_2004_12_konkan_railway",
    month="2004-12",
    title="Konkan Railway Expansion Plans Draw Land Use Debates (2004-12)",
    desc="Farmers protest double-tracking plans, citing destruction of khazan agricultural lands and water channels. In Goa, this monthly event shapes key regional debates.",
    tags=['infrastructure', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_konkan_railway", "Initiate a special government commission to resolve konkan_railway issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_konkan_railway", "Demand that the government address konkan_railway concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_konkan_railway", "Propose a joint multi-party round table to build consensus on konkan_railway.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-01
ITEMS_2001_2005.append(make_news(
    key="ga2001_2005_01_tourism_growth",
    month="2005-01",
    title="Foreign Tourist Arrivals Surge Along Coastal Belts (2005-01)",
    desc="Charter flights from Europe increase, bringing high foreign tourist footfall. Shack owners demand simplified seasonal permits. In Goa, this monthly event shapes key regional debates.",
    tags=['tourism', 'economy'],
    base_w=1.15, profile="economy",
    reactions=[
        reaction("gov_action_tourism_growth", "Initiate a special government commission to resolve tourism_growth issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_tourism_growth", "Demand that the government address tourism_growth concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_tourism_growth", "Propose a joint multi-party round table to build consensus on tourism_growth.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-02
ITEMS_2001_2005.append(make_news(
    key="ga2001_2005_02_mining_disputes",
    month="2005-02",
    title="Iron Ore Transport Barge Operators Launch Strike (2005-02)",
    desc="Barge operators on the Mandovi river strike over shipping rates, halting iron ore transport to Mormugao port. In Goa, this monthly event shapes key regional debates.",
    tags=['economy', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_mining_disputes", "Initiate a special government commission to resolve mining_disputes issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mining_disputes", "Demand that the government address mining_disputes concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mining_disputes", "Propose a joint multi-party round table to build consensus on mining_disputes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-03
ITEMS_2001_2005.append(make_news(
    key="ga2001_2005_03_political_alliance",
    month="2005-03",
    title="MGP and Congress Hold Cabinet Coordination Talks (2005-03)",
    desc="Goa's coalition partners hold crucial talks to ensure stability amid rumors of opposition horse-trading. In Goa, this monthly event shapes key regional debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_political_alliance", "Initiate a special government commission to resolve political_alliance issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_political_alliance", "Demand that the government address political_alliance concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_political_alliance", "Propose a joint multi-party round table to build consensus on political_alliance.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-04
ITEMS_2001_2005.append(make_news(
    key="ga2001_2005_04_crz_violations",
    month="2005-04",
    title="Coastal Regulation Zone Violations Draw Court Focus (2005-04)",
    desc="The High Court issues notices to beachfront resorts violating the 200-meter no-development zone guidelines. In Goa, this monthly event shapes key regional debates.",
    tags=['environment', 'governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_crz_violations", "Initiate a special government commission to resolve crz_violations issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_crz_violations", "Demand that the government address crz_violations concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_crz_violations", "Propose a joint multi-party round table to build consensus on crz_violations.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-05
ITEMS_2001_2005.append(make_news(
    key="ga2001_2005_05_infrastructure_zuari",
    month="2005-05",
    title="Zuari Bridge Repairs Restrict Heavy Vehicle Movement (2005-05)",
    desc="Aging infrastructure forces the government to restrict heavy commercial vehicles on the vital Zuari bridge. In Goa, this monthly event shapes key regional debates.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_infrastructure_zuari", "Initiate a special government commission to resolve infrastructure_zuari issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_infrastructure_zuari", "Demand that the government address infrastructure_zuari concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_infrastructure_zuari", "Propose a joint multi-party round table to build consensus on infrastructure_zuari.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-06
ITEMS_2001_2005.append(make_news(
    key="ga2001_2005_06_garbage_sonsodo",
    month="2005-06",
    title="Sonsodo Garbage Dump Fires Trigger Local Outrage (2005-06)",
    desc="Unmanaged municipal waste at the Sonsodo site in Margao catches fire, causing health concerns and protests. In Goa, this monthly event shapes key regional debates.",
    tags=['protest', 'environment'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_garbage_sonsodo", "Initiate a special government commission to resolve garbage_sonsodo issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_garbage_sonsodo", "Demand that the government address garbage_sonsodo concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_garbage_sonsodo", "Propose a joint multi-party round table to build consensus on garbage_sonsodo.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-07
ITEMS_2001_2005.append(make_news(
    key="ga2001_2005_07_panchayat_reservations",
    month="2005-07",
    title="Panchayat Election Ward Reservations Finalized (2005-07)",
    desc="The State Election Commission announces block ward reservations, sparking protests from local political rivals. In Goa, this monthly event shapes key regional debates.",
    tags=['election', 'politics'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("gov_action_panchayat_reservations", "Initiate a special government commission to resolve panchayat_reservations issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_panchayat_reservations", "Demand that the government address panchayat_reservations concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_panchayat_reservations", "Propose a joint multi-party round table to build consensus on panchayat_reservations.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-08
ITEMS_2001_2005.append(make_news(
    key="ga2001_2005_08_portuguese_heritage",
    month="2005-08",
    title="Conservationists Seek Funding for Old Goa Heritage Sites (2005-08)",
    desc="NGOs and church groups appeal for state-funded restorations of deteriorating UNESCO heritage structures. In Goa, this monthly event shapes key regional debates.",
    tags=['identity', 'tourism'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_portuguese_heritage", "Initiate a special government commission to resolve portuguese_heritage issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_portuguese_heritage", "Demand that the government address portuguese_heritage concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_portuguese_heritage", "Propose a joint multi-party round table to build consensus on portuguese_heritage.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-09
ITEMS_2001_2005.append(make_news(
    key="ga2001_2005_09_fishermen_clash",
    month="2005-09",
    title="Tensions Erupt Between Traditional Fishermen and Trawlers (2005-09)",
    desc="Traditional Ramponkar fishermen block jetties, protesting against illegal night-trawling by mechanized boats. In Goa, this monthly event shapes key regional debates.",
    tags=['protest', 'economy'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_fishermen_clash", "Initiate a special government commission to resolve fishermen_clash issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_fishermen_clash", "Demand that the government address fishermen_clash concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_fishermen_clash", "Propose a joint multi-party round table to build consensus on fishermen_clash.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-10
ITEMS_2001_2005.append(make_news(
    key="ga2001_2005_10_sez_scam",
    month="2005-10",
    title="Industrial Land Allotments Trigger Land Scam Accusations (2005-10)",
    desc="Opposition parties accuse the cabinet of allotting premium industrial plots in Verna to shell companies. In Goa, this monthly event shapes key regional debates.",
    tags=['governance', 'corruption'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_sez_scam", "Initiate a special government commission to resolve sez_scam issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_sez_scam", "Demand that the government address sez_scam concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_sez_scam", "Propose a joint multi-party round table to build consensus on sez_scam.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-11
ITEMS_2001_2005.append(make_news(
    key="ga2001_2005_11_mining_royalties",
    month="2005-11",
    title="Village Panchayats Demand Share of Iron Ore Royalties (2005-11)",
    desc="Sanguem and Bicholim village councils demand direct funding from mining companies to fix broken rural roads. In Goa, this monthly event shapes key regional debates.",
    tags=['rural', 'economy'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_mining_royalties", "Initiate a special government commission to resolve mining_royalties issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_mining_royalties", "Demand that the government address mining_royalties concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_mining_royalties", "Propose a joint multi-party round table to build consensus on mining_royalties.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2005-12
ITEMS_2001_2005.append(make_news(
    key="ga2001_2005_12_konkan_railway",
    month="2005-12",
    title="Konkan Railway Expansion Plans Draw Land Use Debates (2005-12)",
    desc="Farmers protest double-tracking plans, citing destruction of khazan agricultural lands and water channels. In Goa, this monthly event shapes key regional debates.",
    tags=['infrastructure', 'protest'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_konkan_railway", "Initiate a special government commission to resolve konkan_railway issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_konkan_railway", "Demand that the government address konkan_railway concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_konkan_railway", "Propose a joint multi-party round table to build consensus on konkan_railway.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"goaLocalStabilityMemory": 2}, weight=0.2)
    ]
))

