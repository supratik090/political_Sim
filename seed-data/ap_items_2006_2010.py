from helper import reaction, no_comment, make_news, eff, risk

ITEMS_2006_2010 = []

# 2006-01
ITEMS_2006_2010.append(make_news(
    key="ap2006_2006_01_aarogyasri_launch",
    month="2006-01",
    title="Aarogyasri Health Insurance Scheme Rolled Out (2006-01)",
    desc="YSR government launches the cashless health insurance scheme for BPL families, earning major rural popularity. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['welfare', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_aarogyasri_launch", "Initiate a special government commission to resolve aarogyasri_launch issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_aarogyasri_launch", "Demand that the government address aarogyasri_launch concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_aarogyasri_launch", "Propose a joint multi-party round table to build consensus on aarogyasri_launch.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-02
ITEMS_2006_2010.append(make_news(
    key="ap2006_2006_02_jalayagnam_audits",
    month="2006-02",
    title="Jalayagnam Irrigation Projects Face Pricing Inquiries (2006-02)",
    desc="Opposition TDP submits files to the vigilance commission, alleging massive cost escalations in canal tenders. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['corruption', 'infrastructure'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_jalayagnam_audits", "Initiate a special government commission to resolve jalayagnam_audits issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_jalayagnam_audits", "Demand that the government address jalayagnam_audits concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_jalayagnam_audits", "Propose a joint multi-party round table to build consensus on jalayagnam_audits.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-03
ITEMS_2006_2010.append(make_news(
    key="ap2006_2006_03_telangana_agitations",
    month="2006-03",
    title="KCR Begins Indefinite Fast Demanding Telangana Statehood (2006-03)",
    desc="Telangana statehood protests paralyze Hyderabad as students and employees launch joint strike programs. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics', 'protest'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_telangana_agitations", "Initiate a special government commission to resolve telangana_agitations issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_telangana_agitations", "Demand that the government address telangana_agitations concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_telangana_agitations", "Propose a joint multi-party round table to build consensus on telangana_agitations.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-04
ITEMS_2006_2010.append(make_news(
    key="ap2006_2006_04_satyam_collapse",
    month="2006-04",
    title="Satyam Computer Services Financial Fraud Shockwave (2006-04)",
    desc="Chairman Ramalinga Raju confesses to inflating accounts of the IT giant, raising concerns over corporate layoffs. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['economy', 'corruption'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_satyam_collapse", "Initiate a special government commission to resolve satyam_collapse issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_satyam_collapse", "Demand that the government address satyam_collapse concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_satyam_collapse", "Propose a joint multi-party round table to build consensus on satyam_collapse.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-05
ITEMS_2006_2010.append(make_news(
    key="ap2006_2006_05_ysr_helicopter",
    month="2006-05",
    title="Helicopter Crash of CM YS Rajasekhara Reddy Triggers Vacuum (2006-05)",
    desc="The tragic death of YSR in a helicopter crash in Nallamala forest creates a massive leadership crisis in AP. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_ysr_helicopter", "Initiate a special government commission to resolve ysr_helicopter issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_ysr_helicopter", "Demand that the government address ysr_helicopter concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_ysr_helicopter", "Propose a joint multi-party round table to build consensus on ysr_helicopter.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-06
ITEMS_2006_2010.append(make_news(
    key="ap2006_2006_06_indiramma_housing",
    month="2006-06",
    title="Indiramma Housing Scheme Launches Phase 3 Allocations (2006-06)",
    desc="The government releases housing subsidies for rural families, though local panels report minor ward favoritism. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['welfare'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_indiramma_housing", "Initiate a special government commission to resolve indiramma_housing issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_indiramma_housing", "Demand that the government address indiramma_housing concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_indiramma_housing", "Propose a joint multi-party round table to build consensus on indiramma_housing.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-07
ITEMS_2006_2010.append(make_news(
    key="ap2006_2006_07_coastal_corridor",
    month="2006-07",
    title="PCPIR Coastal Corridor Land Acquisitions Blocked (2006-07)",
    desc="Farmers in Kakinada clash with police, protesting land acquisition notices for the proposed petroleum corridor. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_coastal_corridor", "Initiate a special government commission to resolve coastal_corridor issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_coastal_corridor", "Demand that the government address coastal_corridor concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_coastal_corridor", "Propose a joint multi-party round table to build consensus on coastal_corridor.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-08
ITEMS_2006_2010.append(make_news(
    key="ap2006_2006_08_pavala_vaddi",
    month="2006-08",
    title="Pavala Vaddi Interest Subsidies for Self-Help Groups (2006-08)",
    desc="DWACRA women groups welcome the low-interest loan scheme, boosting rural micro-credit availability. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['rural', 'welfare'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_pavala_vaddi", "Initiate a special government commission to resolve pavala_vaddi issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_pavala_vaddi", "Demand that the government address pavala_vaddi concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_pavala_vaddi", "Propose a joint multi-party round table to build consensus on pavala_vaddi.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-09
ITEMS_2006_2010.append(make_news(
    key="ap2006_2006_09_naxal_surrenders",
    month="2006-09",
    title="Greyhounds Special Operations Lead to Naxal Deflations (2006-09)",
    desc="Special anti-Naxal police squads conduct operations in forest borders, leading to surrenders of area commanders. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['security_crisis'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("gov_action_naxal_surrenders", "Initiate a special government commission to resolve naxal_surrenders issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_naxal_surrenders", "Demand that the government address naxal_surrenders concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_naxal_surrenders", "Propose a joint multi-party round table to build consensus on naxal_surrenders.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-10
ITEMS_2006_2010.append(make_news(
    key="ap2006_2006_10_obulapuram_mining",
    month="2006-10",
    title="Obulapuram Mining Company Iron Ore Exports Stalled (2006-10)",
    desc="The Supreme Court halts mining operations along the Bellary border, citing forest boundary violations. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['environment', 'corruption'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_obulapuram_mining", "Initiate a special government commission to resolve obulapuram_mining issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_obulapuram_mining", "Demand that the government address obulapuram_mining concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_obulapuram_mining", "Propose a joint multi-party round table to build consensus on obulapuram_mining.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-11
ITEMS_2006_2010.append(make_news(
    key="ap2006_2006_11_fee_reimbursement",
    month="2006-11",
    title="Higher Education Fee Reimbursement Scheme Starts Trials (2006-11)",
    desc="Government pledges to reimburse college fees for backward class students, facing treasury clearance delays. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['welfare', 'education'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_fee_reimbursement", "Initiate a special government commission to resolve fee_reimbursement issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_fee_reimbursement", "Demand that the government address fee_reimbursement concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_fee_reimbursement", "Propose a joint multi-party round table to build consensus on fee_reimbursement.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2006-12
ITEMS_2006_2010.append(make_news(
    key="ap2006_2006_12_hyderabad_blasts",
    month="2006-12",
    title="Double Bomb Blasts in Hyderabad Cause Panic (2006-12)",
    desc="Terror attacks at Lumbini Park and Gokul Chat trigger curfew alerts and massive police combing operations. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['security_crisis'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("gov_action_hyderabad_blasts", "Initiate a special government commission to resolve hyderabad_blasts issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_hyderabad_blasts", "Demand that the government address hyderabad_blasts concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_hyderabad_blasts", "Propose a joint multi-party round table to build consensus on hyderabad_blasts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-01
ITEMS_2006_2010.append(make_news(
    key="ap2006_2007_01_aarogyasri_launch",
    month="2007-01",
    title="Aarogyasri Health Insurance Scheme Rolled Out (2007-01)",
    desc="YSR government launches the cashless health insurance scheme for BPL families, earning major rural popularity. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['welfare', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_aarogyasri_launch", "Initiate a special government commission to resolve aarogyasri_launch issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_aarogyasri_launch", "Demand that the government address aarogyasri_launch concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_aarogyasri_launch", "Propose a joint multi-party round table to build consensus on aarogyasri_launch.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-02
ITEMS_2006_2010.append(make_news(
    key="ap2006_2007_02_jalayagnam_audits",
    month="2007-02",
    title="Jalayagnam Irrigation Projects Face Pricing Inquiries (2007-02)",
    desc="Opposition TDP submits files to the vigilance commission, alleging massive cost escalations in canal tenders. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['corruption', 'infrastructure'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_jalayagnam_audits", "Initiate a special government commission to resolve jalayagnam_audits issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_jalayagnam_audits", "Demand that the government address jalayagnam_audits concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_jalayagnam_audits", "Propose a joint multi-party round table to build consensus on jalayagnam_audits.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-03
ITEMS_2006_2010.append(make_news(
    key="ap2006_2007_03_telangana_agitations",
    month="2007-03",
    title="KCR Begins Indefinite Fast Demanding Telangana Statehood (2007-03)",
    desc="Telangana statehood protests paralyze Hyderabad as students and employees launch joint strike programs. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics', 'protest'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_telangana_agitations", "Initiate a special government commission to resolve telangana_agitations issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_telangana_agitations", "Demand that the government address telangana_agitations concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_telangana_agitations", "Propose a joint multi-party round table to build consensus on telangana_agitations.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-04
ITEMS_2006_2010.append(make_news(
    key="ap2006_2007_04_satyam_collapse",
    month="2007-04",
    title="Satyam Computer Services Financial Fraud Shockwave (2007-04)",
    desc="Chairman Ramalinga Raju confesses to inflating accounts of the IT giant, raising concerns over corporate layoffs. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['economy', 'corruption'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_satyam_collapse", "Initiate a special government commission to resolve satyam_collapse issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_satyam_collapse", "Demand that the government address satyam_collapse concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_satyam_collapse", "Propose a joint multi-party round table to build consensus on satyam_collapse.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-05
ITEMS_2006_2010.append(make_news(
    key="ap2006_2007_05_ysr_helicopter",
    month="2007-05",
    title="Helicopter Crash of CM YS Rajasekhara Reddy Triggers Vacuum (2007-05)",
    desc="The tragic death of YSR in a helicopter crash in Nallamala forest creates a massive leadership crisis in AP. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_ysr_helicopter", "Initiate a special government commission to resolve ysr_helicopter issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_ysr_helicopter", "Demand that the government address ysr_helicopter concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_ysr_helicopter", "Propose a joint multi-party round table to build consensus on ysr_helicopter.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-06
ITEMS_2006_2010.append(make_news(
    key="ap2006_2007_06_indiramma_housing",
    month="2007-06",
    title="Indiramma Housing Scheme Launches Phase 3 Allocations (2007-06)",
    desc="The government releases housing subsidies for rural families, though local panels report minor ward favoritism. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['welfare'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_indiramma_housing", "Initiate a special government commission to resolve indiramma_housing issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_indiramma_housing", "Demand that the government address indiramma_housing concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_indiramma_housing", "Propose a joint multi-party round table to build consensus on indiramma_housing.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-07
ITEMS_2006_2010.append(make_news(
    key="ap2006_2007_07_coastal_corridor",
    month="2007-07",
    title="PCPIR Coastal Corridor Land Acquisitions Blocked (2007-07)",
    desc="Farmers in Kakinada clash with police, protesting land acquisition notices for the proposed petroleum corridor. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_coastal_corridor", "Initiate a special government commission to resolve coastal_corridor issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_coastal_corridor", "Demand that the government address coastal_corridor concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_coastal_corridor", "Propose a joint multi-party round table to build consensus on coastal_corridor.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-08
ITEMS_2006_2010.append(make_news(
    key="ap2006_2007_08_pavala_vaddi",
    month="2007-08",
    title="Pavala Vaddi Interest Subsidies for Self-Help Groups (2007-08)",
    desc="DWACRA women groups welcome the low-interest loan scheme, boosting rural micro-credit availability. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['rural', 'welfare'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_pavala_vaddi", "Initiate a special government commission to resolve pavala_vaddi issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_pavala_vaddi", "Demand that the government address pavala_vaddi concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_pavala_vaddi", "Propose a joint multi-party round table to build consensus on pavala_vaddi.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-09
ITEMS_2006_2010.append(make_news(
    key="ap2006_2007_09_naxal_surrenders",
    month="2007-09",
    title="Greyhounds Special Operations Lead to Naxal Deflations (2007-09)",
    desc="Special anti-Naxal police squads conduct operations in forest borders, leading to surrenders of area commanders. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['security_crisis'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("gov_action_naxal_surrenders", "Initiate a special government commission to resolve naxal_surrenders issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_naxal_surrenders", "Demand that the government address naxal_surrenders concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_naxal_surrenders", "Propose a joint multi-party round table to build consensus on naxal_surrenders.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-10
ITEMS_2006_2010.append(make_news(
    key="ap2006_2007_10_obulapuram_mining",
    month="2007-10",
    title="Obulapuram Mining Company Iron Ore Exports Stalled (2007-10)",
    desc="The Supreme Court halts mining operations along the Bellary border, citing forest boundary violations. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['environment', 'corruption'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_obulapuram_mining", "Initiate a special government commission to resolve obulapuram_mining issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_obulapuram_mining", "Demand that the government address obulapuram_mining concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_obulapuram_mining", "Propose a joint multi-party round table to build consensus on obulapuram_mining.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-11
ITEMS_2006_2010.append(make_news(
    key="ap2006_2007_11_fee_reimbursement",
    month="2007-11",
    title="Higher Education Fee Reimbursement Scheme Starts Trials (2007-11)",
    desc="Government pledges to reimburse college fees for backward class students, facing treasury clearance delays. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['welfare', 'education'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_fee_reimbursement", "Initiate a special government commission to resolve fee_reimbursement issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_fee_reimbursement", "Demand that the government address fee_reimbursement concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_fee_reimbursement", "Propose a joint multi-party round table to build consensus on fee_reimbursement.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2007-12
ITEMS_2006_2010.append(make_news(
    key="ap2006_2007_12_hyderabad_blasts",
    month="2007-12",
    title="Double Bomb Blasts in Hyderabad Cause Panic (2007-12)",
    desc="Terror attacks at Lumbini Park and Gokul Chat trigger curfew alerts and massive police combing operations. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['security_crisis'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("gov_action_hyderabad_blasts", "Initiate a special government commission to resolve hyderabad_blasts issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_hyderabad_blasts", "Demand that the government address hyderabad_blasts concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_hyderabad_blasts", "Propose a joint multi-party round table to build consensus on hyderabad_blasts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-01
ITEMS_2006_2010.append(make_news(
    key="ap2006_2008_01_aarogyasri_launch",
    month="2008-01",
    title="Aarogyasri Health Insurance Scheme Rolled Out (2008-01)",
    desc="YSR government launches the cashless health insurance scheme for BPL families, earning major rural popularity. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['welfare', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_aarogyasri_launch", "Initiate a special government commission to resolve aarogyasri_launch issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_aarogyasri_launch", "Demand that the government address aarogyasri_launch concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_aarogyasri_launch", "Propose a joint multi-party round table to build consensus on aarogyasri_launch.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-02
ITEMS_2006_2010.append(make_news(
    key="ap2006_2008_02_jalayagnam_audits",
    month="2008-02",
    title="Jalayagnam Irrigation Projects Face Pricing Inquiries (2008-02)",
    desc="Opposition TDP submits files to the vigilance commission, alleging massive cost escalations in canal tenders. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['corruption', 'infrastructure'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_jalayagnam_audits", "Initiate a special government commission to resolve jalayagnam_audits issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_jalayagnam_audits", "Demand that the government address jalayagnam_audits concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_jalayagnam_audits", "Propose a joint multi-party round table to build consensus on jalayagnam_audits.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-03
ITEMS_2006_2010.append(make_news(
    key="ap2006_2008_03_telangana_agitations",
    month="2008-03",
    title="KCR Begins Indefinite Fast Demanding Telangana Statehood (2008-03)",
    desc="Telangana statehood protests paralyze Hyderabad as students and employees launch joint strike programs. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics', 'protest'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_telangana_agitations", "Initiate a special government commission to resolve telangana_agitations issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_telangana_agitations", "Demand that the government address telangana_agitations concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_telangana_agitations", "Propose a joint multi-party round table to build consensus on telangana_agitations.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-04
ITEMS_2006_2010.append(make_news(
    key="ap2006_2008_04_satyam_collapse",
    month="2008-04",
    title="Satyam Computer Services Financial Fraud Shockwave (2008-04)",
    desc="Chairman Ramalinga Raju confesses to inflating accounts of the IT giant, raising concerns over corporate layoffs. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['economy', 'corruption'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_satyam_collapse", "Initiate a special government commission to resolve satyam_collapse issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_satyam_collapse", "Demand that the government address satyam_collapse concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_satyam_collapse", "Propose a joint multi-party round table to build consensus on satyam_collapse.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-05
ITEMS_2006_2010.append(make_news(
    key="ap2006_2008_05_ysr_helicopter",
    month="2008-05",
    title="Helicopter Crash of CM YS Rajasekhara Reddy Triggers Vacuum (2008-05)",
    desc="The tragic death of YSR in a helicopter crash in Nallamala forest creates a massive leadership crisis in AP. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_ysr_helicopter", "Initiate a special government commission to resolve ysr_helicopter issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_ysr_helicopter", "Demand that the government address ysr_helicopter concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_ysr_helicopter", "Propose a joint multi-party round table to build consensus on ysr_helicopter.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-06
ITEMS_2006_2010.append(make_news(
    key="ap2006_2008_06_indiramma_housing",
    month="2008-06",
    title="Indiramma Housing Scheme Launches Phase 3 Allocations (2008-06)",
    desc="The government releases housing subsidies for rural families, though local panels report minor ward favoritism. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['welfare'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_indiramma_housing", "Initiate a special government commission to resolve indiramma_housing issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_indiramma_housing", "Demand that the government address indiramma_housing concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_indiramma_housing", "Propose a joint multi-party round table to build consensus on indiramma_housing.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-07
ITEMS_2006_2010.append(make_news(
    key="ap2006_2008_07_coastal_corridor",
    month="2008-07",
    title="PCPIR Coastal Corridor Land Acquisitions Blocked (2008-07)",
    desc="Farmers in Kakinada clash with police, protesting land acquisition notices for the proposed petroleum corridor. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_coastal_corridor", "Initiate a special government commission to resolve coastal_corridor issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_coastal_corridor", "Demand that the government address coastal_corridor concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_coastal_corridor", "Propose a joint multi-party round table to build consensus on coastal_corridor.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-08
ITEMS_2006_2010.append(make_news(
    key="ap2006_2008_08_pavala_vaddi",
    month="2008-08",
    title="Pavala Vaddi Interest Subsidies for Self-Help Groups (2008-08)",
    desc="DWACRA women groups welcome the low-interest loan scheme, boosting rural micro-credit availability. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['rural', 'welfare'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_pavala_vaddi", "Initiate a special government commission to resolve pavala_vaddi issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_pavala_vaddi", "Demand that the government address pavala_vaddi concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_pavala_vaddi", "Propose a joint multi-party round table to build consensus on pavala_vaddi.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-09
ITEMS_2006_2010.append(make_news(
    key="ap2006_2008_09_naxal_surrenders",
    month="2008-09",
    title="Greyhounds Special Operations Lead to Naxal Deflations (2008-09)",
    desc="Special anti-Naxal police squads conduct operations in forest borders, leading to surrenders of area commanders. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['security_crisis'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("gov_action_naxal_surrenders", "Initiate a special government commission to resolve naxal_surrenders issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_naxal_surrenders", "Demand that the government address naxal_surrenders concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_naxal_surrenders", "Propose a joint multi-party round table to build consensus on naxal_surrenders.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-10
ITEMS_2006_2010.append(make_news(
    key="ap2006_2008_10_obulapuram_mining",
    month="2008-10",
    title="Obulapuram Mining Company Iron Ore Exports Stalled (2008-10)",
    desc="The Supreme Court halts mining operations along the Bellary border, citing forest boundary violations. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['environment', 'corruption'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_obulapuram_mining", "Initiate a special government commission to resolve obulapuram_mining issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_obulapuram_mining", "Demand that the government address obulapuram_mining concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_obulapuram_mining", "Propose a joint multi-party round table to build consensus on obulapuram_mining.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-11
ITEMS_2006_2010.append(make_news(
    key="ap2006_2008_11_fee_reimbursement",
    month="2008-11",
    title="Higher Education Fee Reimbursement Scheme Starts Trials (2008-11)",
    desc="Government pledges to reimburse college fees for backward class students, facing treasury clearance delays. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['welfare', 'education'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_fee_reimbursement", "Initiate a special government commission to resolve fee_reimbursement issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_fee_reimbursement", "Demand that the government address fee_reimbursement concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_fee_reimbursement", "Propose a joint multi-party round table to build consensus on fee_reimbursement.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2008-12
ITEMS_2006_2010.append(make_news(
    key="ap2006_2008_12_hyderabad_blasts",
    month="2008-12",
    title="Double Bomb Blasts in Hyderabad Cause Panic (2008-12)",
    desc="Terror attacks at Lumbini Park and Gokul Chat trigger curfew alerts and massive police combing operations. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['security_crisis'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("gov_action_hyderabad_blasts", "Initiate a special government commission to resolve hyderabad_blasts issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_hyderabad_blasts", "Demand that the government address hyderabad_blasts concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_hyderabad_blasts", "Propose a joint multi-party round table to build consensus on hyderabad_blasts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-01
ITEMS_2006_2010.append(make_news(
    key="ap2006_2009_01_aarogyasri_launch",
    month="2009-01",
    title="Aarogyasri Health Insurance Scheme Rolled Out (2009-01)",
    desc="YSR government launches the cashless health insurance scheme for BPL families, earning major rural popularity. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['welfare', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_aarogyasri_launch", "Initiate a special government commission to resolve aarogyasri_launch issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_aarogyasri_launch", "Demand that the government address aarogyasri_launch concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_aarogyasri_launch", "Propose a joint multi-party round table to build consensus on aarogyasri_launch.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-02
ITEMS_2006_2010.append(make_news(
    key="ap2006_2009_02_jalayagnam_audits",
    month="2009-02",
    title="Jalayagnam Irrigation Projects Face Pricing Inquiries (2009-02)",
    desc="Opposition TDP submits files to the vigilance commission, alleging massive cost escalations in canal tenders. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['corruption', 'infrastructure'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_jalayagnam_audits", "Initiate a special government commission to resolve jalayagnam_audits issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_jalayagnam_audits", "Demand that the government address jalayagnam_audits concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_jalayagnam_audits", "Propose a joint multi-party round table to build consensus on jalayagnam_audits.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-03
ITEMS_2006_2010.append(make_news(
    key="ap2006_2009_03_telangana_agitations",
    month="2009-03",
    title="KCR Begins Indefinite Fast Demanding Telangana Statehood (2009-03)",
    desc="Telangana statehood protests paralyze Hyderabad as students and employees launch joint strike programs. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics', 'protest'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_telangana_agitations", "Initiate a special government commission to resolve telangana_agitations issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_telangana_agitations", "Demand that the government address telangana_agitations concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_telangana_agitations", "Propose a joint multi-party round table to build consensus on telangana_agitations.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-04
ITEMS_2006_2010.append(make_news(
    key="ap2006_2009_04_satyam_collapse",
    month="2009-04",
    title="Satyam Computer Services Financial Fraud Shockwave (2009-04)",
    desc="Chairman Ramalinga Raju confesses to inflating accounts of the IT giant, raising concerns over corporate layoffs. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['economy', 'corruption'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_satyam_collapse", "Initiate a special government commission to resolve satyam_collapse issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_satyam_collapse", "Demand that the government address satyam_collapse concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_satyam_collapse", "Propose a joint multi-party round table to build consensus on satyam_collapse.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-05
ITEMS_2006_2010.append(make_news(
    key="ap2006_2009_05_ysr_helicopter",
    month="2009-05",
    title="Helicopter Crash of CM YS Rajasekhara Reddy Triggers Vacuum (2009-05)",
    desc="The tragic death of YSR in a helicopter crash in Nallamala forest creates a massive leadership crisis in AP. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_ysr_helicopter", "Initiate a special government commission to resolve ysr_helicopter issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_ysr_helicopter", "Demand that the government address ysr_helicopter concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_ysr_helicopter", "Propose a joint multi-party round table to build consensus on ysr_helicopter.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-06
ITEMS_2006_2010.append(make_news(
    key="ap2006_2009_06_indiramma_housing",
    month="2009-06",
    title="Indiramma Housing Scheme Launches Phase 3 Allocations (2009-06)",
    desc="The government releases housing subsidies for rural families, though local panels report minor ward favoritism. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['welfare'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_indiramma_housing", "Initiate a special government commission to resolve indiramma_housing issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_indiramma_housing", "Demand that the government address indiramma_housing concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_indiramma_housing", "Propose a joint multi-party round table to build consensus on indiramma_housing.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-07
ITEMS_2006_2010.append(make_news(
    key="ap2006_2009_07_coastal_corridor",
    month="2009-07",
    title="PCPIR Coastal Corridor Land Acquisitions Blocked (2009-07)",
    desc="Farmers in Kakinada clash with police, protesting land acquisition notices for the proposed petroleum corridor. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_coastal_corridor", "Initiate a special government commission to resolve coastal_corridor issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_coastal_corridor", "Demand that the government address coastal_corridor concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_coastal_corridor", "Propose a joint multi-party round table to build consensus on coastal_corridor.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-08
ITEMS_2006_2010.append(make_news(
    key="ap2006_2009_08_pavala_vaddi",
    month="2009-08",
    title="Pavala Vaddi Interest Subsidies for Self-Help Groups (2009-08)",
    desc="DWACRA women groups welcome the low-interest loan scheme, boosting rural micro-credit availability. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['rural', 'welfare'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_pavala_vaddi", "Initiate a special government commission to resolve pavala_vaddi issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_pavala_vaddi", "Demand that the government address pavala_vaddi concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_pavala_vaddi", "Propose a joint multi-party round table to build consensus on pavala_vaddi.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-09
ITEMS_2006_2010.append(make_news(
    key="ap2006_2009_09_naxal_surrenders",
    month="2009-09",
    title="Greyhounds Special Operations Lead to Naxal Deflations (2009-09)",
    desc="Special anti-Naxal police squads conduct operations in forest borders, leading to surrenders of area commanders. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['security_crisis'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("gov_action_naxal_surrenders", "Initiate a special government commission to resolve naxal_surrenders issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_naxal_surrenders", "Demand that the government address naxal_surrenders concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_naxal_surrenders", "Propose a joint multi-party round table to build consensus on naxal_surrenders.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-10
ITEMS_2006_2010.append(make_news(
    key="ap2006_2009_10_obulapuram_mining",
    month="2009-10",
    title="Obulapuram Mining Company Iron Ore Exports Stalled (2009-10)",
    desc="The Supreme Court halts mining operations along the Bellary border, citing forest boundary violations. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['environment', 'corruption'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_obulapuram_mining", "Initiate a special government commission to resolve obulapuram_mining issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_obulapuram_mining", "Demand that the government address obulapuram_mining concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_obulapuram_mining", "Propose a joint multi-party round table to build consensus on obulapuram_mining.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-11
ITEMS_2006_2010.append(make_news(
    key="ap2006_2009_11_fee_reimbursement",
    month="2009-11",
    title="Higher Education Fee Reimbursement Scheme Starts Trials (2009-11)",
    desc="Government pledges to reimburse college fees for backward class students, facing treasury clearance delays. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['welfare', 'education'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_fee_reimbursement", "Initiate a special government commission to resolve fee_reimbursement issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_fee_reimbursement", "Demand that the government address fee_reimbursement concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_fee_reimbursement", "Propose a joint multi-party round table to build consensus on fee_reimbursement.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2009-12
ITEMS_2006_2010.append(make_news(
    key="ap2006_2009_12_hyderabad_blasts",
    month="2009-12",
    title="Double Bomb Blasts in Hyderabad Cause Panic (2009-12)",
    desc="Terror attacks at Lumbini Park and Gokul Chat trigger curfew alerts and massive police combing operations. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['security_crisis'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("gov_action_hyderabad_blasts", "Initiate a special government commission to resolve hyderabad_blasts issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_hyderabad_blasts", "Demand that the government address hyderabad_blasts concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_hyderabad_blasts", "Propose a joint multi-party round table to build consensus on hyderabad_blasts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-01
ITEMS_2006_2010.append(make_news(
    key="ap2006_2010_01_aarogyasri_launch",
    month="2010-01",
    title="Aarogyasri Health Insurance Scheme Rolled Out (2010-01)",
    desc="YSR government launches the cashless health insurance scheme for BPL families, earning major rural popularity. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['welfare', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_aarogyasri_launch", "Initiate a special government commission to resolve aarogyasri_launch issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_aarogyasri_launch", "Demand that the government address aarogyasri_launch concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_aarogyasri_launch", "Propose a joint multi-party round table to build consensus on aarogyasri_launch.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-02
ITEMS_2006_2010.append(make_news(
    key="ap2006_2010_02_jalayagnam_audits",
    month="2010-02",
    title="Jalayagnam Irrigation Projects Face Pricing Inquiries (2010-02)",
    desc="Opposition TDP submits files to the vigilance commission, alleging massive cost escalations in canal tenders. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['corruption', 'infrastructure'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_jalayagnam_audits", "Initiate a special government commission to resolve jalayagnam_audits issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_jalayagnam_audits", "Demand that the government address jalayagnam_audits concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_jalayagnam_audits", "Propose a joint multi-party round table to build consensus on jalayagnam_audits.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-03
ITEMS_2006_2010.append(make_news(
    key="ap2006_2010_03_telangana_agitations",
    month="2010-03",
    title="KCR Begins Indefinite Fast Demanding Telangana Statehood (2010-03)",
    desc="Telangana statehood protests paralyze Hyderabad as students and employees launch joint strike programs. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics', 'protest'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_telangana_agitations", "Initiate a special government commission to resolve telangana_agitations issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_telangana_agitations", "Demand that the government address telangana_agitations concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_telangana_agitations", "Propose a joint multi-party round table to build consensus on telangana_agitations.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-04
ITEMS_2006_2010.append(make_news(
    key="ap2006_2010_04_satyam_collapse",
    month="2010-04",
    title="Satyam Computer Services Financial Fraud Shockwave (2010-04)",
    desc="Chairman Ramalinga Raju confesses to inflating accounts of the IT giant, raising concerns over corporate layoffs. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['economy', 'corruption'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_satyam_collapse", "Initiate a special government commission to resolve satyam_collapse issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_satyam_collapse", "Demand that the government address satyam_collapse concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_satyam_collapse", "Propose a joint multi-party round table to build consensus on satyam_collapse.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-05
ITEMS_2006_2010.append(make_news(
    key="ap2006_2010_05_ysr_helicopter",
    month="2010-05",
    title="Helicopter Crash of CM YS Rajasekhara Reddy Triggers Vacuum (2010-05)",
    desc="The tragic death of YSR in a helicopter crash in Nallamala forest creates a massive leadership crisis in AP. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("gov_action_ysr_helicopter", "Initiate a special government commission to resolve ysr_helicopter issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_ysr_helicopter", "Demand that the government address ysr_helicopter concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_ysr_helicopter", "Propose a joint multi-party round table to build consensus on ysr_helicopter.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-06
ITEMS_2006_2010.append(make_news(
    key="ap2006_2010_06_indiramma_housing",
    month="2010-06",
    title="Indiramma Housing Scheme Launches Phase 3 Allocations (2010-06)",
    desc="The government releases housing subsidies for rural families, though local panels report minor ward favoritism. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['welfare'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_indiramma_housing", "Initiate a special government commission to resolve indiramma_housing issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_indiramma_housing", "Demand that the government address indiramma_housing concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_indiramma_housing", "Propose a joint multi-party round table to build consensus on indiramma_housing.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-07
ITEMS_2006_2010.append(make_news(
    key="ap2006_2010_07_coastal_corridor",
    month="2010-07",
    title="PCPIR Coastal Corridor Land Acquisitions Blocked (2010-07)",
    desc="Farmers in Kakinada clash with police, protesting land acquisition notices for the proposed petroleum corridor. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['protest', 'land_rights'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("gov_action_coastal_corridor", "Initiate a special government commission to resolve coastal_corridor issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_coastal_corridor", "Demand that the government address coastal_corridor concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_coastal_corridor", "Propose a joint multi-party round table to build consensus on coastal_corridor.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-08
ITEMS_2006_2010.append(make_news(
    key="ap2006_2010_08_pavala_vaddi",
    month="2010-08",
    title="Pavala Vaddi Interest Subsidies for Self-Help Groups (2010-08)",
    desc="DWACRA women groups welcome the low-interest loan scheme, boosting rural micro-credit availability. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['rural', 'welfare'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("gov_action_pavala_vaddi", "Initiate a special government commission to resolve pavala_vaddi issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_pavala_vaddi", "Demand that the government address pavala_vaddi concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_pavala_vaddi", "Propose a joint multi-party round table to build consensus on pavala_vaddi.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-09
ITEMS_2006_2010.append(make_news(
    key="ap2006_2010_09_naxal_surrenders",
    month="2010-09",
    title="Greyhounds Special Operations Lead to Naxal Deflations (2010-09)",
    desc="Special anti-Naxal police squads conduct operations in forest borders, leading to surrenders of area commanders. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['security_crisis'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("gov_action_naxal_surrenders", "Initiate a special government commission to resolve naxal_surrenders issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_naxal_surrenders", "Demand that the government address naxal_surrenders concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_naxal_surrenders", "Propose a joint multi-party round table to build consensus on naxal_surrenders.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-10
ITEMS_2006_2010.append(make_news(
    key="ap2006_2010_10_obulapuram_mining",
    month="2010-10",
    title="Obulapuram Mining Company Iron Ore Exports Stalled (2010-10)",
    desc="The Supreme Court halts mining operations along the Bellary border, citing forest boundary violations. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['environment', 'corruption'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("gov_action_obulapuram_mining", "Initiate a special government commission to resolve obulapuram_mining issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_obulapuram_mining", "Demand that the government address obulapuram_mining concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_obulapuram_mining", "Propose a joint multi-party round table to build consensus on obulapuram_mining.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-11
ITEMS_2006_2010.append(make_news(
    key="ap2006_2010_11_fee_reimbursement",
    month="2010-11",
    title="Higher Education Fee Reimbursement Scheme Starts Trials (2010-11)",
    desc="Government pledges to reimburse college fees for backward class students, facing treasury clearance delays. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['welfare', 'education'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("gov_action_fee_reimbursement", "Initiate a special government commission to resolve fee_reimbursement issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_fee_reimbursement", "Demand that the government address fee_reimbursement concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_fee_reimbursement", "Propose a joint multi-party round table to build consensus on fee_reimbursement.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

# 2010-12
ITEMS_2006_2010.append(make_news(
    key="ap2006_2010_12_hyderabad_blasts",
    month="2010-12",
    title="Double Bomb Blasts in Hyderabad Cause Panic (2010-12)",
    desc="Terror attacks at Lumbini Park and Gokul Chat trigger curfew alerts and massive police combing operations. In Andhra Pradesh, this monthly event shapes key state development debates.",
    tags=['security_crisis'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("gov_action_hyderabad_blasts", "Initiate a special government commission to resolve hyderabad_blasts issues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Administrative delays stall the commission, drawing minor local criticism.", eff(-1, 0, -1, -2)), 1.2),
        reaction("opp_demands_hyderabad_blasts", "Demand that the government address hyderabad_blasts concerns and provide public subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Discussions break down due to partisan standoffs, leading to minor public fatigue.", eff(0, 0, -2, -1)), 1.25),
        reaction("joint_forum_hyderabad_blasts", "Propose a joint multi-party round table to build consensus on hyderabad_blasts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Radical subgroups refuse to cooperate, causing minor delays.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"apStabilityMemory": 2}, weight=0.2)
    ]
))

