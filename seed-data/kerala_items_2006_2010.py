from helper import reaction, no_comment, make_news, eff, risk

ITEMS_2006_2010 = []

# 2006-01
ITEMS_2006_2010.append(make_news(
    key="kl2006_2006_01_munnar_evictions",
    month="2006-01",
    title="Munnar Encroachment Demolition Drives Launched by VS Government (2006-01)",
    desc="CM VS Achuthanandan sends special task forces to demolish illegal luxury resorts constructed on forest land. In Kerala, this monthly event shapes key state development debates.",
    tags=['governance', 'land_rights'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_munnar_evictions", "Initiate a special government commission to resolve munnar_evictions issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_munnar_evictions", "Demand that the government address munnar_evictions concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_munnar_evictions", "Propose a joint multi-party round table to build consensus on munnar_evictions.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-02
ITEMS_2006_2010.append(make_news(
    key="kl2006_2006_02_smartcity_kochi",
    month="2006-02",
    title="SmartCity Kochi IT Project Joint Venture Agreement Signed (2006-02)",
    desc="The state cabinet signs the final joint venture agreement with Dubai Internet City for the long-delayed IT park. In Kerala, this monthly event shapes key state development debates.",
    tags=['infrastructure', 'economy'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_smartcity_kochi", "Initiate a special government commission to resolve smartcity_kochi issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_smartcity_kochi", "Demand that the government address smartcity_kochi concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_smartcity_kochi", "Propose a joint multi-party round table to build consensus on smartcity_kochi.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-03
ITEMS_2006_2010.append(make_news(
    key="kl2006_2006_03_endosulfan_ban",
    month="2006-03",
    title="Kasaragod Endosulfan Pesticide Ban Agitations Gain Strength (2006-03)",
    desc="Victims and green groups demand comprehensive rehabilitation packages and permanent bans on chemical spraying. In Kerala, this monthly event shapes key state development debates.",
    tags=['environment', 'protest'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_endosulfan_ban", "Initiate a special government commission to resolve endosulfan_ban issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_endosulfan_ban", "Demand that the government address endosulfan_ban concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_endosulfan_ban", "Propose a joint multi-party round table to build consensus on endosulfan_ban.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-04
ITEMS_2006_2010.append(make_news(
    key="kl2006_2006_04_vizhinjam_port",
    month="2006-04",
    title="Vizhinjam Deepwater Port Bid Tenders Cleared (2006-04)",
    desc="The government clears global tenders for the proposed transshipment port near Trivandrum, attracting developer interest. In Kerala, this monthly event shapes key state development debates.",
    tags=['infrastructure'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_vizhinjam_port", "Initiate a special government commission to resolve vizhinjam_port issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_vizhinjam_port", "Demand that the government address vizhinjam_port concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_vizhinjam_port", "Propose a joint multi-party round table to build consensus on vizhinjam_port.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-05
ITEMS_2006_2010.append(make_news(
    key="kl2006_2006_05_coir_subsidies",
    month="2006-05",
    title="Coir Weaving Cooperatives Receive Modernization Grants (2006-05)",
    desc="Traditional coir mat weavers welcome modern machinery subsidies, though unions express fears of job displacement. In Kerala, this monthly event shapes key state development debates.",
    tags=['rural', 'economy'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_coir_subsidies", "Initiate a special government commission to resolve coir_subsidies issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_coir_subsidies", "Demand that the government address coir_subsidies concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_coir_subsidies", "Propose a joint multi-party round table to build consensus on coir_subsidies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-06
ITEMS_2006_2010.append(make_news(
    key="kl2006_2006_06_sabarmala_crowds",
    month="2006-06",
    title="Sabarimala Pilgrimage Safety Audits Initiated (2006-06)",
    desc="Following heavy pilgrim traffic, the High Court directs state agencies to upgrade trekking pathways and facilities. In Kerala, this monthly event shapes key state development debates.",
    tags=['identity'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_sabarmala_crowds", "Initiate a special government commission to resolve sabarmala_crowds issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_sabarmala_crowds", "Demand that the government address sabarmala_crowds concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_sabarmala_crowds", "Propose a joint multi-party round table to build consensus on sabarmala_crowds.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-07
ITEMS_2006_2010.append(make_news(
    key="kl2006_2006_07_land_reforms",
    month="2006-07",
    title="Harrisons Malayalam Land Lease Disputes Trigger Inquiries (2006-07)",
    desc="Special officers probe century-old British land leases in plantations, drawing support from landless groups. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_land_reforms", "Initiate a special government commission to resolve land_reforms issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_land_reforms", "Demand that the government address land_reforms concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_land_reforms", "Propose a joint multi-party round table to build consensus on land_reforms.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-08
ITEMS_2006_2010.append(make_news(
    key="kl2006_2006_08_school_it",
    month="2006-08",
    title="IT @ School Project Mandates Free Open-Source Software (2006-08)",
    desc="Kerala education department mandates GNU/Linux operating systems in all state schools, phasing out commercial software. In Kerala, this monthly event shapes key state development debates.",
    tags=['education'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_school_it", "Initiate a special government commission to resolve school_it issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_school_it", "Demand that the government address school_it concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_school_it", "Propose a joint multi-party round table to build consensus on school_it.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-09
ITEMS_2006_2010.append(make_news(
    key="kl2006_2006_09_chital_fever",
    month="2006-09",
    title="Chikungunya Outbreak Sparks Healthcare Deployments (2006-09)",
    desc="Heavy mosquito breeding in rubber plantation zones leads to fever outbreaks, prompting medical camps. In Kerala, this monthly event shapes key state development debates.",
    tags=['governance'],
    base_w=1.15, profile="health_crisis",
    reactions=[
        reaction("gov_action_chital_fever", "Initiate a special government commission to resolve chital_fever issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_chital_fever", "Demand that the government address chital_fever concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_chital_fever", "Propose a joint multi-party round table to build consensus on chital_fever.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-10
ITEMS_2006_2010.append(make_news(
    key="kl2006_2006_10_kseb_privatization",
    month="2006-10",
    title="State Electricity Board Reorganization Protests Erupt (2006-10)",
    desc="KSEB employee unions organize protests, opposing restructuring and demand state public utility guarantees. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'economy'],
    base_w=1.25, profile="protest",
    reactions=[
        reaction("gov_action_kseb_privatization", "Initiate a special government commission to resolve kseb_privatization issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_kseb_privatization", "Demand that the government address kseb_privatization concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_kseb_privatization", "Propose a joint multi-party round table to build consensus on kseb_privatization.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-11
ITEMS_2006_2010.append(make_news(
    key="kl2006_2006_11_paddy_protection",
    month="2006-11",
    title="Kerala Paddy Land and Wetland Conservation Act Passed (2006-11)",
    desc="The assembly passes strict laws banning the conversion of traditional paddy fields for commercial buildings. In Kerala, this monthly event shapes key state development debates.",
    tags=['environment', 'rural'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_paddy_protection", "Initiate a special government commission to resolve paddy_protection issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_paddy_protection", "Demand that the government address paddy_protection concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_paddy_protection", "Propose a joint multi-party round table to build consensus on paddy_protection.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-12
ITEMS_2006_2010.append(make_news(
    key="kl2006_2006_12_gulf_layoffs",
    month="2006-12",
    title="Global Financial Crisis Triggers NRK Return Concerns (2006-12)",
    desc="Return of migrant workers from Dubai due to construction shutdowns prompts calls for NRI welfare packages. In Kerala, this monthly event shapes key state development debates.",
    tags=['economy'],
    base_w=1.25, profile="economy",
    reactions=[
        reaction("gov_action_gulf_layoffs", "Initiate a special government commission to resolve gulf_layoffs issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_gulf_layoffs", "Demand that the government address gulf_layoffs concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_gulf_layoffs", "Propose a joint multi-party round table to build consensus on gulf_layoffs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-01
ITEMS_2006_2010.append(make_news(
    key="kl2006_2007_01_munnar_evictions",
    month="2007-01",
    title="Munnar Encroachment Demolition Drives Launched by VS Government (2007-01)",
    desc="CM VS Achuthanandan sends special task forces to demolish illegal luxury resorts constructed on forest land. In Kerala, this monthly event shapes key state development debates.",
    tags=['governance', 'land_rights'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_munnar_evictions", "Initiate a special government commission to resolve munnar_evictions issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_munnar_evictions", "Demand that the government address munnar_evictions concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_munnar_evictions", "Propose a joint multi-party round table to build consensus on munnar_evictions.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-02
ITEMS_2006_2010.append(make_news(
    key="kl2006_2007_02_smartcity_kochi",
    month="2007-02",
    title="SmartCity Kochi IT Project Joint Venture Agreement Signed (2007-02)",
    desc="The state cabinet signs the final joint venture agreement with Dubai Internet City for the long-delayed IT park. In Kerala, this monthly event shapes key state development debates.",
    tags=['infrastructure', 'economy'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_smartcity_kochi", "Initiate a special government commission to resolve smartcity_kochi issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_smartcity_kochi", "Demand that the government address smartcity_kochi concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_smartcity_kochi", "Propose a joint multi-party round table to build consensus on smartcity_kochi.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-03
ITEMS_2006_2010.append(make_news(
    key="kl2006_2007_03_endosulfan_ban",
    month="2007-03",
    title="Kasaragod Endosulfan Pesticide Ban Agitations Gain Strength (2007-03)",
    desc="Victims and green groups demand comprehensive rehabilitation packages and permanent bans on chemical spraying. In Kerala, this monthly event shapes key state development debates.",
    tags=['environment', 'protest'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_endosulfan_ban", "Initiate a special government commission to resolve endosulfan_ban issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_endosulfan_ban", "Demand that the government address endosulfan_ban concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_endosulfan_ban", "Propose a joint multi-party round table to build consensus on endosulfan_ban.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-04
ITEMS_2006_2010.append(make_news(
    key="kl2006_2007_04_vizhinjam_port",
    month="2007-04",
    title="Vizhinjam Deepwater Port Bid Tenders Cleared (2007-04)",
    desc="The government clears global tenders for the proposed transshipment port near Trivandrum, attracting developer interest. In Kerala, this monthly event shapes key state development debates.",
    tags=['infrastructure'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_vizhinjam_port", "Initiate a special government commission to resolve vizhinjam_port issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_vizhinjam_port", "Demand that the government address vizhinjam_port concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_vizhinjam_port", "Propose a joint multi-party round table to build consensus on vizhinjam_port.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-05
ITEMS_2006_2010.append(make_news(
    key="kl2006_2007_05_coir_subsidies",
    month="2007-05",
    title="Coir Weaving Cooperatives Receive Modernization Grants (2007-05)",
    desc="Traditional coir mat weavers welcome modern machinery subsidies, though unions express fears of job displacement. In Kerala, this monthly event shapes key state development debates.",
    tags=['rural', 'economy'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_coir_subsidies", "Initiate a special government commission to resolve coir_subsidies issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_coir_subsidies", "Demand that the government address coir_subsidies concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_coir_subsidies", "Propose a joint multi-party round table to build consensus on coir_subsidies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-06
ITEMS_2006_2010.append(make_news(
    key="kl2006_2007_06_sabarmala_crowds",
    month="2007-06",
    title="Sabarimala Pilgrimage Safety Audits Initiated (2007-06)",
    desc="Following heavy pilgrim traffic, the High Court directs state agencies to upgrade trekking pathways and facilities. In Kerala, this monthly event shapes key state development debates.",
    tags=['identity'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_sabarmala_crowds", "Initiate a special government commission to resolve sabarmala_crowds issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_sabarmala_crowds", "Demand that the government address sabarmala_crowds concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_sabarmala_crowds", "Propose a joint multi-party round table to build consensus on sabarmala_crowds.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-07
ITEMS_2006_2010.append(make_news(
    key="kl2006_2007_07_land_reforms",
    month="2007-07",
    title="Harrisons Malayalam Land Lease Disputes Trigger Inquiries (2007-07)",
    desc="Special officers probe century-old British land leases in plantations, drawing support from landless groups. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_land_reforms", "Initiate a special government commission to resolve land_reforms issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_land_reforms", "Demand that the government address land_reforms concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_land_reforms", "Propose a joint multi-party round table to build consensus on land_reforms.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-08
ITEMS_2006_2010.append(make_news(
    key="kl2006_2007_08_school_it",
    month="2007-08",
    title="IT @ School Project Mandates Free Open-Source Software (2007-08)",
    desc="Kerala education department mandates GNU/Linux operating systems in all state schools, phasing out commercial software. In Kerala, this monthly event shapes key state development debates.",
    tags=['education'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_school_it", "Initiate a special government commission to resolve school_it issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_school_it", "Demand that the government address school_it concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_school_it", "Propose a joint multi-party round table to build consensus on school_it.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-09
ITEMS_2006_2010.append(make_news(
    key="kl2006_2007_09_chital_fever",
    month="2007-09",
    title="Chikungunya Outbreak Sparks Healthcare Deployments (2007-09)",
    desc="Heavy mosquito breeding in rubber plantation zones leads to fever outbreaks, prompting medical camps. In Kerala, this monthly event shapes key state development debates.",
    tags=['governance'],
    base_w=1.15, profile="health_crisis",
    reactions=[
        reaction("gov_action_chital_fever", "Initiate a special government commission to resolve chital_fever issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_chital_fever", "Demand that the government address chital_fever concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_chital_fever", "Propose a joint multi-party round table to build consensus on chital_fever.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-10
ITEMS_2006_2010.append(make_news(
    key="kl2006_2007_10_kseb_privatization",
    month="2007-10",
    title="State Electricity Board Reorganization Protests Erupt (2007-10)",
    desc="KSEB employee unions organize protests, opposing restructuring and demand state public utility guarantees. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'economy'],
    base_w=1.25, profile="protest",
    reactions=[
        reaction("gov_action_kseb_privatization", "Initiate a special government commission to resolve kseb_privatization issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_kseb_privatization", "Demand that the government address kseb_privatization concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_kseb_privatization", "Propose a joint multi-party round table to build consensus on kseb_privatization.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-11
ITEMS_2006_2010.append(make_news(
    key="kl2006_2007_11_paddy_protection",
    month="2007-11",
    title="Kerala Paddy Land and Wetland Conservation Act Passed (2007-11)",
    desc="The assembly passes strict laws banning the conversion of traditional paddy fields for commercial buildings. In Kerala, this monthly event shapes key state development debates.",
    tags=['environment', 'rural'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_paddy_protection", "Initiate a special government commission to resolve paddy_protection issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_paddy_protection", "Demand that the government address paddy_protection concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_paddy_protection", "Propose a joint multi-party round table to build consensus on paddy_protection.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-12
ITEMS_2006_2010.append(make_news(
    key="kl2006_2007_12_gulf_layoffs",
    month="2007-12",
    title="Global Financial Crisis Triggers NRK Return Concerns (2007-12)",
    desc="Return of migrant workers from Dubai due to construction shutdowns prompts calls for NRI welfare packages. In Kerala, this monthly event shapes key state development debates.",
    tags=['economy'],
    base_w=1.25, profile="economy",
    reactions=[
        reaction("gov_action_gulf_layoffs", "Initiate a special government commission to resolve gulf_layoffs issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_gulf_layoffs", "Demand that the government address gulf_layoffs concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_gulf_layoffs", "Propose a joint multi-party round table to build consensus on gulf_layoffs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-01
ITEMS_2006_2010.append(make_news(
    key="kl2006_2008_01_munnar_evictions",
    month="2008-01",
    title="Munnar Encroachment Demolition Drives Launched by VS Government (2008-01)",
    desc="CM VS Achuthanandan sends special task forces to demolish illegal luxury resorts constructed on forest land. In Kerala, this monthly event shapes key state development debates.",
    tags=['governance', 'land_rights'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_munnar_evictions", "Initiate a special government commission to resolve munnar_evictions issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_munnar_evictions", "Demand that the government address munnar_evictions concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_munnar_evictions", "Propose a joint multi-party round table to build consensus on munnar_evictions.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-02
ITEMS_2006_2010.append(make_news(
    key="kl2006_2008_02_smartcity_kochi",
    month="2008-02",
    title="SmartCity Kochi IT Project Joint Venture Agreement Signed (2008-02)",
    desc="The state cabinet signs the final joint venture agreement with Dubai Internet City for the long-delayed IT park. In Kerala, this monthly event shapes key state development debates.",
    tags=['infrastructure', 'economy'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_smartcity_kochi", "Initiate a special government commission to resolve smartcity_kochi issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_smartcity_kochi", "Demand that the government address smartcity_kochi concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_smartcity_kochi", "Propose a joint multi-party round table to build consensus on smartcity_kochi.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-03
ITEMS_2006_2010.append(make_news(
    key="kl2006_2008_03_endosulfan_ban",
    month="2008-03",
    title="Kasaragod Endosulfan Pesticide Ban Agitations Gain Strength (2008-03)",
    desc="Victims and green groups demand comprehensive rehabilitation packages and permanent bans on chemical spraying. In Kerala, this monthly event shapes key state development debates.",
    tags=['environment', 'protest'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_endosulfan_ban", "Initiate a special government commission to resolve endosulfan_ban issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_endosulfan_ban", "Demand that the government address endosulfan_ban concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_endosulfan_ban", "Propose a joint multi-party round table to build consensus on endosulfan_ban.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-04
ITEMS_2006_2010.append(make_news(
    key="kl2006_2008_04_vizhinjam_port",
    month="2008-04",
    title="Vizhinjam Deepwater Port Bid Tenders Cleared (2008-04)",
    desc="The government clears global tenders for the proposed transshipment port near Trivandrum, attracting developer interest. In Kerala, this monthly event shapes key state development debates.",
    tags=['infrastructure'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_vizhinjam_port", "Initiate a special government commission to resolve vizhinjam_port issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_vizhinjam_port", "Demand that the government address vizhinjam_port concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_vizhinjam_port", "Propose a joint multi-party round table to build consensus on vizhinjam_port.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-05
ITEMS_2006_2010.append(make_news(
    key="kl2006_2008_05_coir_subsidies",
    month="2008-05",
    title="Coir Weaving Cooperatives Receive Modernization Grants (2008-05)",
    desc="Traditional coir mat weavers welcome modern machinery subsidies, though unions express fears of job displacement. In Kerala, this monthly event shapes key state development debates.",
    tags=['rural', 'economy'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_coir_subsidies", "Initiate a special government commission to resolve coir_subsidies issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_coir_subsidies", "Demand that the government address coir_subsidies concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_coir_subsidies", "Propose a joint multi-party round table to build consensus on coir_subsidies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-06
ITEMS_2006_2010.append(make_news(
    key="kl2006_2008_06_sabarmala_crowds",
    month="2008-06",
    title="Sabarimala Pilgrimage Safety Audits Initiated (2008-06)",
    desc="Following heavy pilgrim traffic, the High Court directs state agencies to upgrade trekking pathways and facilities. In Kerala, this monthly event shapes key state development debates.",
    tags=['identity'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_sabarmala_crowds", "Initiate a special government commission to resolve sabarmala_crowds issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_sabarmala_crowds", "Demand that the government address sabarmala_crowds concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_sabarmala_crowds", "Propose a joint multi-party round table to build consensus on sabarmala_crowds.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-07
ITEMS_2006_2010.append(make_news(
    key="kl2006_2008_07_land_reforms",
    month="2008-07",
    title="Harrisons Malayalam Land Lease Disputes Trigger Inquiries (2008-07)",
    desc="Special officers probe century-old British land leases in plantations, drawing support from landless groups. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_land_reforms", "Initiate a special government commission to resolve land_reforms issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_land_reforms", "Demand that the government address land_reforms concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_land_reforms", "Propose a joint multi-party round table to build consensus on land_reforms.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-08
ITEMS_2006_2010.append(make_news(
    key="kl2006_2008_08_school_it",
    month="2008-08",
    title="IT @ School Project Mandates Free Open-Source Software (2008-08)",
    desc="Kerala education department mandates GNU/Linux operating systems in all state schools, phasing out commercial software. In Kerala, this monthly event shapes key state development debates.",
    tags=['education'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_school_it", "Initiate a special government commission to resolve school_it issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_school_it", "Demand that the government address school_it concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_school_it", "Propose a joint multi-party round table to build consensus on school_it.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-09
ITEMS_2006_2010.append(make_news(
    key="kl2006_2008_09_chital_fever",
    month="2008-09",
    title="Chikungunya Outbreak Sparks Healthcare Deployments (2008-09)",
    desc="Heavy mosquito breeding in rubber plantation zones leads to fever outbreaks, prompting medical camps. In Kerala, this monthly event shapes key state development debates.",
    tags=['governance'],
    base_w=1.15, profile="health_crisis",
    reactions=[
        reaction("gov_action_chital_fever", "Initiate a special government commission to resolve chital_fever issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_chital_fever", "Demand that the government address chital_fever concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_chital_fever", "Propose a joint multi-party round table to build consensus on chital_fever.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-10
ITEMS_2006_2010.append(make_news(
    key="kl2006_2008_10_kseb_privatization",
    month="2008-10",
    title="State Electricity Board Reorganization Protests Erupt (2008-10)",
    desc="KSEB employee unions organize protests, opposing restructuring and demand state public utility guarantees. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'economy'],
    base_w=1.25, profile="protest",
    reactions=[
        reaction("gov_action_kseb_privatization", "Initiate a special government commission to resolve kseb_privatization issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_kseb_privatization", "Demand that the government address kseb_privatization concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_kseb_privatization", "Propose a joint multi-party round table to build consensus on kseb_privatization.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-11
ITEMS_2006_2010.append(make_news(
    key="kl2006_2008_11_paddy_protection",
    month="2008-11",
    title="Kerala Paddy Land and Wetland Conservation Act Passed (2008-11)",
    desc="The assembly passes strict laws banning the conversion of traditional paddy fields for commercial buildings. In Kerala, this monthly event shapes key state development debates.",
    tags=['environment', 'rural'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_paddy_protection", "Initiate a special government commission to resolve paddy_protection issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_paddy_protection", "Demand that the government address paddy_protection concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_paddy_protection", "Propose a joint multi-party round table to build consensus on paddy_protection.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-12
ITEMS_2006_2010.append(make_news(
    key="kl2006_2008_12_gulf_layoffs",
    month="2008-12",
    title="Global Financial Crisis Triggers NRK Return Concerns (2008-12)",
    desc="Return of migrant workers from Dubai due to construction shutdowns prompts calls for NRI welfare packages. In Kerala, this monthly event shapes key state development debates.",
    tags=['economy'],
    base_w=1.25, profile="economy",
    reactions=[
        reaction("gov_action_gulf_layoffs", "Initiate a special government commission to resolve gulf_layoffs issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_gulf_layoffs", "Demand that the government address gulf_layoffs concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_gulf_layoffs", "Propose a joint multi-party round table to build consensus on gulf_layoffs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-01
ITEMS_2006_2010.append(make_news(
    key="kl2006_2009_01_munnar_evictions",
    month="2009-01",
    title="Munnar Encroachment Demolition Drives Launched by VS Government (2009-01)",
    desc="CM VS Achuthanandan sends special task forces to demolish illegal luxury resorts constructed on forest land. In Kerala, this monthly event shapes key state development debates.",
    tags=['governance', 'land_rights'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_munnar_evictions", "Initiate a special government commission to resolve munnar_evictions issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_munnar_evictions", "Demand that the government address munnar_evictions concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_munnar_evictions", "Propose a joint multi-party round table to build consensus on munnar_evictions.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-02
ITEMS_2006_2010.append(make_news(
    key="kl2006_2009_02_smartcity_kochi",
    month="2009-02",
    title="SmartCity Kochi IT Project Joint Venture Agreement Signed (2009-02)",
    desc="The state cabinet signs the final joint venture agreement with Dubai Internet City for the long-delayed IT park. In Kerala, this monthly event shapes key state development debates.",
    tags=['infrastructure', 'economy'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_smartcity_kochi", "Initiate a special government commission to resolve smartcity_kochi issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_smartcity_kochi", "Demand that the government address smartcity_kochi concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_smartcity_kochi", "Propose a joint multi-party round table to build consensus on smartcity_kochi.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-03
ITEMS_2006_2010.append(make_news(
    key="kl2006_2009_03_endosulfan_ban",
    month="2009-03",
    title="Kasaragod Endosulfan Pesticide Ban Agitations Gain Strength (2009-03)",
    desc="Victims and green groups demand comprehensive rehabilitation packages and permanent bans on chemical spraying. In Kerala, this monthly event shapes key state development debates.",
    tags=['environment', 'protest'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_endosulfan_ban", "Initiate a special government commission to resolve endosulfan_ban issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_endosulfan_ban", "Demand that the government address endosulfan_ban concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_endosulfan_ban", "Propose a joint multi-party round table to build consensus on endosulfan_ban.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-04
ITEMS_2006_2010.append(make_news(
    key="kl2006_2009_04_vizhinjam_port",
    month="2009-04",
    title="Vizhinjam Deepwater Port Bid Tenders Cleared (2009-04)",
    desc="The government clears global tenders for the proposed transshipment port near Trivandrum, attracting developer interest. In Kerala, this monthly event shapes key state development debates.",
    tags=['infrastructure'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_vizhinjam_port", "Initiate a special government commission to resolve vizhinjam_port issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_vizhinjam_port", "Demand that the government address vizhinjam_port concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_vizhinjam_port", "Propose a joint multi-party round table to build consensus on vizhinjam_port.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-05
ITEMS_2006_2010.append(make_news(
    key="kl2006_2009_05_coir_subsidies",
    month="2009-05",
    title="Coir Weaving Cooperatives Receive Modernization Grants (2009-05)",
    desc="Traditional coir mat weavers welcome modern machinery subsidies, though unions express fears of job displacement. In Kerala, this monthly event shapes key state development debates.",
    tags=['rural', 'economy'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_coir_subsidies", "Initiate a special government commission to resolve coir_subsidies issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_coir_subsidies", "Demand that the government address coir_subsidies concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_coir_subsidies", "Propose a joint multi-party round table to build consensus on coir_subsidies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-06
ITEMS_2006_2010.append(make_news(
    key="kl2006_2009_06_sabarmala_crowds",
    month="2009-06",
    title="Sabarimala Pilgrimage Safety Audits Initiated (2009-06)",
    desc="Following heavy pilgrim traffic, the High Court directs state agencies to upgrade trekking pathways and facilities. In Kerala, this monthly event shapes key state development debates.",
    tags=['identity'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_sabarmala_crowds", "Initiate a special government commission to resolve sabarmala_crowds issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_sabarmala_crowds", "Demand that the government address sabarmala_crowds concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_sabarmala_crowds", "Propose a joint multi-party round table to build consensus on sabarmala_crowds.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-07
ITEMS_2006_2010.append(make_news(
    key="kl2006_2009_07_land_reforms",
    month="2009-07",
    title="Harrisons Malayalam Land Lease Disputes Trigger Inquiries (2009-07)",
    desc="Special officers probe century-old British land leases in plantations, drawing support from landless groups. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_land_reforms", "Initiate a special government commission to resolve land_reforms issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_land_reforms", "Demand that the government address land_reforms concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_land_reforms", "Propose a joint multi-party round table to build consensus on land_reforms.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-08
ITEMS_2006_2010.append(make_news(
    key="kl2006_2009_08_school_it",
    month="2009-08",
    title="IT @ School Project Mandates Free Open-Source Software (2009-08)",
    desc="Kerala education department mandates GNU/Linux operating systems in all state schools, phasing out commercial software. In Kerala, this monthly event shapes key state development debates.",
    tags=['education'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_school_it", "Initiate a special government commission to resolve school_it issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_school_it", "Demand that the government address school_it concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_school_it", "Propose a joint multi-party round table to build consensus on school_it.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-09
ITEMS_2006_2010.append(make_news(
    key="kl2006_2009_09_chital_fever",
    month="2009-09",
    title="Chikungunya Outbreak Sparks Healthcare Deployments (2009-09)",
    desc="Heavy mosquito breeding in rubber plantation zones leads to fever outbreaks, prompting medical camps. In Kerala, this monthly event shapes key state development debates.",
    tags=['governance'],
    base_w=1.15, profile="health_crisis",
    reactions=[
        reaction("gov_action_chital_fever", "Initiate a special government commission to resolve chital_fever issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_chital_fever", "Demand that the government address chital_fever concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_chital_fever", "Propose a joint multi-party round table to build consensus on chital_fever.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-10
ITEMS_2006_2010.append(make_news(
    key="kl2006_2009_10_kseb_privatization",
    month="2009-10",
    title="State Electricity Board Reorganization Protests Erupt (2009-10)",
    desc="KSEB employee unions organize protests, opposing restructuring and demand state public utility guarantees. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'economy'],
    base_w=1.25, profile="protest",
    reactions=[
        reaction("gov_action_kseb_privatization", "Initiate a special government commission to resolve kseb_privatization issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_kseb_privatization", "Demand that the government address kseb_privatization concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_kseb_privatization", "Propose a joint multi-party round table to build consensus on kseb_privatization.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-11
ITEMS_2006_2010.append(make_news(
    key="kl2006_2009_11_paddy_protection",
    month="2009-11",
    title="Kerala Paddy Land and Wetland Conservation Act Passed (2009-11)",
    desc="The assembly passes strict laws banning the conversion of traditional paddy fields for commercial buildings. In Kerala, this monthly event shapes key state development debates.",
    tags=['environment', 'rural'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_paddy_protection", "Initiate a special government commission to resolve paddy_protection issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_paddy_protection", "Demand that the government address paddy_protection concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_paddy_protection", "Propose a joint multi-party round table to build consensus on paddy_protection.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-12
ITEMS_2006_2010.append(make_news(
    key="kl2006_2009_12_gulf_layoffs",
    month="2009-12",
    title="Global Financial Crisis Triggers NRK Return Concerns (2009-12)",
    desc="Return of migrant workers from Dubai due to construction shutdowns prompts calls for NRI welfare packages. In Kerala, this monthly event shapes key state development debates.",
    tags=['economy'],
    base_w=1.25, profile="economy",
    reactions=[
        reaction("gov_action_gulf_layoffs", "Initiate a special government commission to resolve gulf_layoffs issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_gulf_layoffs", "Demand that the government address gulf_layoffs concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_gulf_layoffs", "Propose a joint multi-party round table to build consensus on gulf_layoffs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-01
ITEMS_2006_2010.append(make_news(
    key="kl2006_2010_01_munnar_evictions",
    month="2010-01",
    title="Munnar Encroachment Demolition Drives Launched by VS Government (2010-01)",
    desc="CM VS Achuthanandan sends special task forces to demolish illegal luxury resorts constructed on forest land. In Kerala, this monthly event shapes key state development debates.",
    tags=['governance', 'land_rights'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_munnar_evictions", "Initiate a special government commission to resolve munnar_evictions issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_munnar_evictions", "Demand that the government address munnar_evictions concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_munnar_evictions", "Propose a joint multi-party round table to build consensus on munnar_evictions.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-02
ITEMS_2006_2010.append(make_news(
    key="kl2006_2010_02_smartcity_kochi",
    month="2010-02",
    title="SmartCity Kochi IT Project Joint Venture Agreement Signed (2010-02)",
    desc="The state cabinet signs the final joint venture agreement with Dubai Internet City for the long-delayed IT park. In Kerala, this monthly event shapes key state development debates.",
    tags=['infrastructure', 'economy'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_smartcity_kochi", "Initiate a special government commission to resolve smartcity_kochi issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_smartcity_kochi", "Demand that the government address smartcity_kochi concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_smartcity_kochi", "Propose a joint multi-party round table to build consensus on smartcity_kochi.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-03
ITEMS_2006_2010.append(make_news(
    key="kl2006_2010_03_endosulfan_ban",
    month="2010-03",
    title="Kasaragod Endosulfan Pesticide Ban Agitations Gain Strength (2010-03)",
    desc="Victims and green groups demand comprehensive rehabilitation packages and permanent bans on chemical spraying. In Kerala, this monthly event shapes key state development debates.",
    tags=['environment', 'protest'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_endosulfan_ban", "Initiate a special government commission to resolve endosulfan_ban issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_endosulfan_ban", "Demand that the government address endosulfan_ban concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_endosulfan_ban", "Propose a joint multi-party round table to build consensus on endosulfan_ban.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-04
ITEMS_2006_2010.append(make_news(
    key="kl2006_2010_04_vizhinjam_port",
    month="2010-04",
    title="Vizhinjam Deepwater Port Bid Tenders Cleared (2010-04)",
    desc="The government clears global tenders for the proposed transshipment port near Trivandrum, attracting developer interest. In Kerala, this monthly event shapes key state development debates.",
    tags=['infrastructure'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_vizhinjam_port", "Initiate a special government commission to resolve vizhinjam_port issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_vizhinjam_port", "Demand that the government address vizhinjam_port concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_vizhinjam_port", "Propose a joint multi-party round table to build consensus on vizhinjam_port.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-05
ITEMS_2006_2010.append(make_news(
    key="kl2006_2010_05_coir_subsidies",
    month="2010-05",
    title="Coir Weaving Cooperatives Receive Modernization Grants (2010-05)",
    desc="Traditional coir mat weavers welcome modern machinery subsidies, though unions express fears of job displacement. In Kerala, this monthly event shapes key state development debates.",
    tags=['rural', 'economy'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_coir_subsidies", "Initiate a special government commission to resolve coir_subsidies issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_coir_subsidies", "Demand that the government address coir_subsidies concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_coir_subsidies", "Propose a joint multi-party round table to build consensus on coir_subsidies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-06
ITEMS_2006_2010.append(make_news(
    key="kl2006_2010_06_sabarmala_crowds",
    month="2010-06",
    title="Sabarimala Pilgrimage Safety Audits Initiated (2010-06)",
    desc="Following heavy pilgrim traffic, the High Court directs state agencies to upgrade trekking pathways and facilities. In Kerala, this monthly event shapes key state development debates.",
    tags=['identity'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_sabarmala_crowds", "Initiate a special government commission to resolve sabarmala_crowds issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_sabarmala_crowds", "Demand that the government address sabarmala_crowds concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_sabarmala_crowds", "Propose a joint multi-party round table to build consensus on sabarmala_crowds.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-07
ITEMS_2006_2010.append(make_news(
    key="kl2006_2010_07_land_reforms",
    month="2010-07",
    title="Harrisons Malayalam Land Lease Disputes Trigger Inquiries (2010-07)",
    desc="Special officers probe century-old British land leases in plantations, drawing support from landless groups. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_land_reforms", "Initiate a special government commission to resolve land_reforms issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_land_reforms", "Demand that the government address land_reforms concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_land_reforms", "Propose a joint multi-party round table to build consensus on land_reforms.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-08
ITEMS_2006_2010.append(make_news(
    key="kl2006_2010_08_school_it",
    month="2010-08",
    title="IT @ School Project Mandates Free Open-Source Software (2010-08)",
    desc="Kerala education department mandates GNU/Linux operating systems in all state schools, phasing out commercial software. In Kerala, this monthly event shapes key state development debates.",
    tags=['education'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_school_it", "Initiate a special government commission to resolve school_it issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_school_it", "Demand that the government address school_it concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_school_it", "Propose a joint multi-party round table to build consensus on school_it.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-09
ITEMS_2006_2010.append(make_news(
    key="kl2006_2010_09_chital_fever",
    month="2010-09",
    title="Chikungunya Outbreak Sparks Healthcare Deployments (2010-09)",
    desc="Heavy mosquito breeding in rubber plantation zones leads to fever outbreaks, prompting medical camps. In Kerala, this monthly event shapes key state development debates.",
    tags=['governance'],
    base_w=1.15, profile="health_crisis",
    reactions=[
        reaction("gov_action_chital_fever", "Initiate a special government commission to resolve chital_fever issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_chital_fever", "Demand that the government address chital_fever concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_chital_fever", "Propose a joint multi-party round table to build consensus on chital_fever.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-10
ITEMS_2006_2010.append(make_news(
    key="kl2006_2010_10_kseb_privatization",
    month="2010-10",
    title="State Electricity Board Reorganization Protests Erupt (2010-10)",
    desc="KSEB employee unions organize protests, opposing restructuring and demand state public utility guarantees. In Kerala, this monthly event shapes key state development debates.",
    tags=['protest', 'economy'],
    base_w=1.25, profile="protest",
    reactions=[
        reaction("gov_action_kseb_privatization", "Initiate a special government commission to resolve kseb_privatization issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_kseb_privatization", "Demand that the government address kseb_privatization concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_kseb_privatization", "Propose a joint multi-party round table to build consensus on kseb_privatization.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-11
ITEMS_2006_2010.append(make_news(
    key="kl2006_2010_11_paddy_protection",
    month="2010-11",
    title="Kerala Paddy Land and Wetland Conservation Act Passed (2010-11)",
    desc="The assembly passes strict laws banning the conversion of traditional paddy fields for commercial buildings. In Kerala, this monthly event shapes key state development debates.",
    tags=['environment', 'rural'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_paddy_protection", "Initiate a special government commission to resolve paddy_protection issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_paddy_protection", "Demand that the government address paddy_protection concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_paddy_protection", "Propose a joint multi-party round table to build consensus on paddy_protection.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-12
ITEMS_2006_2010.append(make_news(
    key="kl2006_2010_12_gulf_layoffs",
    month="2010-12",
    title="Global Financial Crisis Triggers NRK Return Concerns (2010-12)",
    desc="Return of migrant workers from Dubai due to construction shutdowns prompts calls for NRI welfare packages. In Kerala, this monthly event shapes key state development debates.",
    tags=['economy'],
    base_w=1.25, profile="economy",
    reactions=[
        reaction("gov_action_gulf_layoffs", "Initiate a special government commission to resolve gulf_layoffs issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_gulf_layoffs", "Demand that the government address gulf_layoffs concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_gulf_layoffs", "Propose a joint multi-party round table to build consensus on gulf_layoffs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"keralaStabilityMemory": 2}, weight=0.2)
    ]
))

