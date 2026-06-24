from helper import reaction, no_comment, make_news, eff, risk

ITEMS_2001_2005 = []

# 2001-01
ITEMS_2001_2005.append(make_news(
    key="up2001_2001_01_hukum_singh_quota",
    month="2001-01",
    title="CM Rajnath Singh Pushes Quota Within Quota for OBCs",
    desc="Chief Minister Rajnath Singh introduces the Hukum Singh Committee recommendations, proposing a sub-quota for Most Backward Castes (MBCs) to ensure equitable reservation benefits.",
    tags=['politics', 'identity', 'governance'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("implement_sub_quota", "Implement the MBC sub-quota recommendations immediately across all government jobs.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Dominant backward groups launch state-wide protests, blocking highways in central UP.", eff(-1, 0, -2, -2)), 1.25),
        reaction("oppose_quota_division", "Oppose the division of backward quotas, calling it an electoral gimmick to split social unity.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Voters from most backward communities feel ignored by the opposition, leading to local anger.", eff(0, 0, -1, -2)), 1.2),
        reaction("propose_judicial_review_quota", "Propose a judicial commission to review the backwardness criteria before changing reservation structures.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 2, 2),
                 {},
                 risk(10, "Legal delays freeze all government recruitments, frustrating unemployed youth.", eff(-1, 0, -1, -1)), 1.05),
        no_comment(hidden={"identityIssueMissed": 1}, weight=0.2)
    ]
))

# 2001-02
ITEMS_2001_2005.append(make_news(
    key="up2001_2001_02_vhp_dharam_sansad",
    month="2001-02",
    title="VHP Dharam Sansad in Ayodhya Raises Communal Temperature",
    desc="The Vishva Hindu Parishad (VHP) hosts a Dharam Sansad in Ayodhya, demanding the immediate handover of acquired land for Ram temple construction.",
    tags=['politics', 'identity', 'security'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("increase_security_ayodhya", "Deploy additional state police and paramilitary forces to secure the disputed site borders.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Security blockades lead to local merchant protests over business losses.", eff(-1, 0, -1, -1)), 1.2),
        reaction("protest_religious_mobilization", "Organise harmony peace marches and demand the state government prevent religious gatherings near the site.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Radical groups accuse the opposition of being anti-faith, leading to minor clashes.", eff(-1, 0, -2, -1)), 1.15),
        reaction("propose_inter_faith_dialogue_board", "Propose establishing a permanent inter-faith dialogue board in Faizabad district to resolve local disputes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Both sides refuse to send representatives, rendering the board inactive.", eff(0, 0, -1, -1)), 1.05),
        no_comment(hidden={"securityIgnoredMemory": 2}, weight=0.25)
    ]
))

# 2001-03
ITEMS_2001_2005.append(make_news(
    key="up2001_2001_03_anti_copying_act_protests",
    month="2001-03",
    title="Protests Erupt Over Anti-Copying Act Enforcement in State Exams",
    desc="Strict enforcement of the Anti-Copying Act during UP Board exams leads to student protests and boycotts in Allahabad and Kanpur.",
    tags=['education', 'law_order', 'protest'],
    base_w=1.05, profile="protest",
    reactions=[
        reaction("enforce_act_with_cctv", "Continue strict enforcement of the act and authorize center superintendents to call police against copying mafias.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(16, "Clashes between student groups and police lead to minor injuries, drawing critical press.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_humanitarian_relaxation_of_act", "Demand relaxation of the act's criminal clauses, claiming it treats minor students like criminals.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Middle-class parent associations criticize the opposition for supporting cheating.", eff(-1, 0, -2, -2)), 1.15),
        reaction("propose_board_exam_digitization", "Propose complete digitization of exam center layouts and modernizing the syllabus to focus on analytical questions.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Lack of computers in rural government centers delays exam delivery.", eff(0, 0, -2, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2001-04
ITEMS_2001_2005.append(make_news(
    key="up2001_2001_04_meerut_sugarcane_protests",
    month="2001-04",
    title="Sugarcane Farmers Block Meerut Highway Over Arrears Delay",
    desc="Thousands of sugarcane growers block the Delhi-Dehradun highway near Meerut. They protest payment delays by private mills and demand state advisory price hikes.",
    tags=['rural', 'agriculture', 'protest'],
    base_w=1.2, profile="land_rights",
    reactions=[
        reaction("release_cane_subsidy_funds", "Release emergency state funds to clear cooperative mill dues and mandate private mills clear dues within 14 days.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Private mill owners threaten lockouts, claiming financial inability to pay immediate arrears.", eff(-1, 0, -2, -2)), 1.25),
        reaction("lead_farmer_dharna_meerut", "Join the highway blockade and lead a march of farmers to the commissioner's office to demand interest on arrears.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Commuter queues and freight delays draw complaints from industrial transport associations.", eff(-1, 0, -1, -2)), 1.2),
        reaction("propose_automated_payment_link", "Propose an automated escrow system linking mill sales directly to farmers' bank accounts for immediate clearances.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(10, "Technical integration with rural banks is delayed, leaving payments slow.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 3}, weight=0.2)
    ]
))

# 2001-05
ITEMS_2001_2005.append(make_news(
    key="up2001_2001_05_taj_corridor_clearance_row",
    month="2001-05",
    title="Taj Heritage Corridor Project Environmental Row Escalates",
    desc="Central pollution control authorities query the Uttar Pradesh government regarding the Taj Heritage Corridor project, alleging land reclamation near the Yamuna riverbed threatens the monument.",
    tags=['environment', 'governance', 'economy'],
    base_w=1.1, profile="governance",
    reactions=[
        reaction("defend_corridor_as_tourism_boon", "Defend the corridor as a major tourism infrastructure boost and speed up construction work.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(20, "Environmental court issues a temporary work-halt order, leaving project assets stranded.", eff(-1, 0, -2, -2)), 1.15),
        reaction("demand_cbi_probe_corridor_spending", "Expose unauthorized landfilling near the Taj Mahal and demand a CBI investigation into corruption in contract awards.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(14, "Local tourism unions complain that the opposition is blocking jobs and Agra's development.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_independent_riverbed_audit", "Propose an independent committee of river hydrologists and archeologists to redesign the project safely.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Design changes delay project delivery by several years, increasing costs.", eff(0, 0, -1, -1)), 1.05),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2001-06
ITEMS_2001_2005.append(make_news(
    key="up2001_2001_06_panchayat_elections_setbacks",
    month="2001-06",
    title="BJP Suffers Setbacks in Panchayat Polls; Dissidents Rise",
    desc="Local body and Panchayat election results show significant gains for Samajwadi Party and Bahujan Samaj Party, triggering internal dissent against BJP CM Rajnath Singh.",
    tags=['election', 'politics'],
    base_w=1.1, profile="election",
    reactions=[
        reaction("reorganise_district_party_panels", "Reorganize the district party executive panels and announce fresh rural development grants.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(15, "Dissident MLAs continue to hold private meetings, demanding a cabinet reshuffle.", eff(-1, 0, -2, -2)), 1.15),
        reaction("campaign_on_government_incumbency", "Campaign aggressively on the government's failures in rural development and power distribution.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(12, "Opposition parties fail to agree on seat-sharing in upcoming by-polls, splitting votes.", eff(-1, 0, -2, -1)), 1.2),
        reaction("propose_panchayat_finance_decentralization", "Propose directly transferring state development funds to Gram Panchayats, bypassing district bureaucracy.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(10, "District council members protest their loss of power, stalling administrative roll-out.", eff(0, 0, -2, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2001-07
ITEMS_2001_2005.append(make_news(
    key="up2001_2001_07_eastern_up_floods",
    month="2001-07",
    title="Torrential Rains Trigger Severe Floods in Eastern UP Districts",
    desc="Heavy monsoon rainfall causes the Ghaghara and Gandak rivers to overflow, submerging hundreds of villages in Gorakhpur and Deoria. Disaster relief teams are deployed.",
    tags=['disaster', 'relief', 'rural'],
    base_w=1.15, profile="disaster_relief",
    reactions=[
        reaction("deploy_disaster_teams_aid", "Deploy emergency medical teams, distribute grain packets, and release immediate compensation to affected families.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Relief distribution is delayed by damaged rural roads, causing protests at block offices.", eff(-1, 0, -2, -2)), 1.25),
        reaction("demand_central_flood_relief_pkg", "Demand the state government request an emergency central flood relief package and waive local land revenue taxes.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Central government disputes state damage estimates, delaying the release of funds.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_all_party_relief_coordination", "Propose an all-party disaster relief coordination cell to streamline distribution of emergency supplies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(10, "Administrative delays in cargo clearance temporarily halt relief shipments.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2001-08
ITEMS_2001_2005.append(make_news(
    key="up2001_2001_08_obc_sub_quota_legal_challenge",
    month="2001-08",
    title="High Court Admits Legal Challenges to OBC Sub-Quota Scheme",
    desc="The Allahabad High Court admits multiple writ petitions challenging the state government's proposed sub-classification of OBC reservations, stalling the recruitment process.",
    tags=['politics', 'identity', 'law_order'],
    base_w=1.1, profile="politics",
    reactions=[
        reaction("instruct_advocate_general_defend", "Instruct the state advocate general to defend the sub-quota policy aggressively, submitting census data on backward representation.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "The court grants an interim stay on recruitment, drawing protests from beneficiary groups.", eff(-1, 0, -2, -2)), 1.15),
        reaction("demand_special_assembly_session_quota", "Demand a special assembly session to pass a statutory bill guaranteeing the new sub-quota, bypass court stays.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Legal experts warn that a statutory bill during ongoing judicial review invites contempt charges.", eff(-1, 0, -2, -1)), 1.2),
        reaction("propose_state_harmony_committee", "Propose a state harmony committee representing all community leaders to discuss grievances peacefully.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing by key members delays the release of the committee's recommendations.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.25)
    ]
))

# 2001-09
ITEMS_2001_2005.append(make_news(
    key="up2001_2001_09_simbhaoli_sugar_mill_protests",
    month="2001-09",
    title="Farmers Protest Near Simbhaoli Sugar Mill Over Delayed Payments",
    desc="Sugarcane farmers stage a sit-in outside the Simbhaoli sugar mill in Western UP, demanding immediate cash clearance of previous season's dues before crushing starts.",
    tags=['rural', 'agriculture', 'protest'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("order_mill_owners_payout", "Issue a government mandate ordering mill management to liquidate sugar stock assets to clear farmer dues immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Mill owners file a court petition challenging the mandate, stalling stock liquidation.", eff(-1, 0, -2, -2)), 1.25),
        reaction("demand_cooperative_bank_loans_farmers", "Demand that state cooperative banks issue interest-free soft loans to affected farmers to buy fertilizer.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Bank cash reserves are low, limiting the volume of loans disbursed in the block.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_tripartite_mediation_council", "Propose a tripartite mediation council representing labor unions, industry leaders, and state officials.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Radical sections of the union boycott the mediation, continuing localized protests.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 3}, weight=0.2)
    ]
))

# 2001-10
ITEMS_2001_2005.append(make_news(
    key="up2001_2001_10_ayodhya_site_security_alert",
    month="2001-10",
    title="Ayodhya Security Alert: VHP Activists Enter Disputed Complex",
    desc="A group of VHP activists breaches the outer barricades of the disputed site complex in Ayodhya, raising security alarms. Police restore order and make preventive arrests.",
    tags=['security', 'politics', 'crisis'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("tighten_outer_barricades_patrols", "Tighten the security parameter barricades and deploy additional rapid action force units to Ayodhya town.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Local residents complain of travel restrictions and arbitrary identity checks during festivals.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_administrative_explanation", "Demand a formal explanation in the assembly regarding the security breach, citing administrative negligence.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(12, "Ruling coalition dismisses the attack as a minor trespassing incident, diluting the debate.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_security_advisory_board", "Propose setting up an independent security advisory board with defense experts to upgrade local safety protocols.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(12, "Implementation of board recommendations is delayed due to funding shortages.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"securityIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2001-11
ITEMS_2001_2005.append(make_news(
    key="up2001_2001_11_kalp_yojana_primary_education",
    month="2001-11",
    title="CM Rajnath Singh Launches 'Kalp Yojana' for Primary Schools",
    desc="Chief Minister Rajnath Singh launches the 'Kalp Yojana' scheme aimed at improving primary education quality, basic school infrastructure, and midday meal distribution.",
    tags=['education', 'governance', 'good_news'],
    base_w=1.0, profile="governance",
    reactions=[
        reaction("allocate_infrastructure_grants", "Allocate direct capital grants to village education committees to construct clean drinking water units in schools.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Local contractors use sub-standard materials, leading to pipeline leaks within months.", eff(-1, 0, -2, -2)), 1.15),
        reaction("demand_independent_audit_of_yojana", "Demand an independent academic audit of the scheme, claiming funds are diverted for political ads.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(10, "Media reviews the school improvements positively, making the opposition look cynical.", eff(0, 0, -1, -1)), 1.1),
        reaction("propose_digitized_audit_portal", "Propose a digitized public audit portal to track all related government transactions and block corruption.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(12, "Technical integration delays keep the portal offline, drawing criticism for slow delivery.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2001-12
ITEMS_2001_2005.append(make_news(
    key="up2001_2001_12_assembly_campaigns_launch",
    month="2001-12",
    title="Assembly Campaigning Commences Across UP Districts",
    desc="With the legislative term nearing its end, major political parties kick off their assembly election campaigns in Western and Central UP. Law & order and development are major themes.",
    tags=['election', 'politics'],
    base_w=1.1, profile="election",
    reactions=[
        reaction("campaign_on_welfare_and_MBC_quota", "Campaign heavily on primary school welfare schemes and the Hukum Singh sub-quota recommendations.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Opposition coordination splits the government's voter share in key rural pockets.", eff(-1, 0, -2, -2)), 1.15),
        reaction("campaign_on_governance_breakdown", "Campaign heavily on governance breakdowns, highlighting farmer dues and the stalled recruitments.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(12, "Internal bickerings over ticket allocation spark minor rebel candidates contesting.", eff(-1, 0, -2, -2)), 1.2),
        reaction("propose_legislative_roundtable", "Propose a legislative roundtable with representatives from all parties to draft a consensus policy on the issue.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 2, 2),
                 {},
                 risk(8, "Lack of consensus among members delays the final report, rendering it inactive.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2002-01
ITEMS_2001_2005.append(make_news(
    key="up2002_2002_01_campaigns_peak",
    month="2002-01",
    title="Campaigning Peaks as UP Elections Near First Phase",
    desc="High-decibel election rallies sweep across Western districts. BSP focus on Dalit empowerment, SP targets backward-Muslim coalitions, and BJP highlights nationalism and MBC quotas.",
    tags=['election', 'politics'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("promise_increased_rural_power_supply", "Promise to double rural electricity hours and subsidize tubewell tariffs in election manifestos.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(12, "Regulatory commission issues a notice regarding violation of model code of conduct.", eff(-1, 0, -2, -1)), 1.15),
        reaction("expose_incumbent_failures_sugar_belt", "Organise farmer assemblies in the sugar belt exposing unpaid crop dues and delayed MSP revisions.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(10, "Incumbent candidates claim global pricing drops caused delays, diluting the attack.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_direct_mayoral_elections", "Propose structural reforms to allow direct election of mayors to ensure civic accountability.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Voters show low interest in structural civic reforms during the high-volume campaign.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.35)
    ]
))

# 2002-02
ITEMS_2001_2005.append(make_news(
    key="up2002_2002_02_assembly_polling",
    month="2002-02",
    title="UP Assembly Polling Commences Under Strict Security",
    desc="Voters cast ballots in the first phases of the UP assembly elections. Heavy security forces are deployed in sensitive constituencies to prevent booth-capturing.",
    tags=['election', 'politics', 'law_order'],
    base_w=1.2, profile="election",
    reactions=[
        reaction("deploy_extra_paramilitary_booths", "Deploy additional central paramilitary forces in critical booths and conduct helicopter patrolling in ravines.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Voter turnout drops in locked-down pockets, causing local party worker frustration.", eff(-1, 0, -2, -2)), 1.2),
        reaction("document_booth_irregularities", "Submit detailed logs of alleged state machinery bias and request re-polling in flagged booths.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Election Commission rejects the complaints as unsubstantiated, reducing impact.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_digitized_voter_verification", "Propose launching biometric-based digitized voter verification systems at sensitive polling booths.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Implementation cost is deemed high by state election departments, stalling progress.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2002-03
ITEMS_2001_2005.append(make_news(
    key="up2002_2002_03_hung_assembly_presidents_rule",
    month="2002-03",
    title="Fractured Verdict Leads to President's Rule in Uttar Pradesh",
    desc="The UP election results yield a hung assembly. Samajwadi Party emerges as largest single party but lacks numbers; President's Rule is imposed on March 3.",
    tags=['election', 'politics', 'crisis'],
    base_w=1.3, profile="politics",
    reactions=[
        reaction("seek_coalition_allies", "Negotiate with smaller regional parties and independents to secure a stable coalition partner.",
                 ['GOVERNMENT'], eff(1, 0, 3, 2),
                 {},
                 risk(20, "Negotiations drag on, leaving the state administration in bureaucratic limbo under Governor.", eff(-2, 0, -2, -2)), 1.1),
        reaction("protest_presidents_rule_demand_mandate", "Launch public rallies protesting President's Rule, claiming the largest party should be invited to form government.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(15, "Rallies turn violent, leading to clashes with police and negative press.", eff(-1, 0, -2, -2)), 1.25),
        reaction("propose_legislative_roundtable", "Propose a legislative roundtable with representatives from all parties to draft a consensus policy on the issue.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 2, 2),
                 {},
                 risk(8, "Lack of consensus among members delays the final report, rendering it inactive.", eff(0, 0, -1, -1)), 1.05),
        no_comment(hidden={"democracyDefenceCredit": -3}, weight=0.25)
    ]
))

# 2002-04
ITEMS_2001_2005.append(make_news(
    key="up2002_2002_04_bsp_bjp_talks",
    month="2002-04",
    title="BSP and BJP Close In on Coalition Government Deal",
    desc="Behind-the-scenes negotiations pick up pace between BSP leader Mayawati and BJP high command to form a coalition government in Lucknow, ending the political deadlock.",
    tags=['politics', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("announce_common_minimum_program", "Agree on a common minimum development program emphasizing Dalit and MBC welfare grants.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(16, "Slighted regional allies express public dissent, threatening alliance numbers.", eff(-1, 0, -2, -2)), 1.15),
        reaction("denounce_alliance_as_unprincipled", "Issue press statements denouncing the alliance as an unprincipled compromise of secularism and ideology.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Allied parties form local blocks anyway, diluting the opposition's national attack.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_fixed_ministerial_performance_indices", "Propose introducing a quarterly public performance index for all state departments to monitor minister delivery.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Political parties dismiss the index idea as an academic exercise outside democratic realities.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.35)
    ]
))

# 2002-05
ITEMS_2001_2005.append(make_news(
    key="up2002_2002_05_mayawati_sworn_in_cm",
    month="2002-05",
    title="Mayawati Sworn In as CM; BSP-BJP Coalition Assumes Power",
    desc="Mayawati is sworn in as the Chief Minister of Uttar Pradesh for the third time, leading a BSP-BJP coalition. She promises stable governance and a push for social justice.",
    tags=['politics', 'governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("commit_to_unified_governance", "Commit to unified governance, fast-tracking agricultural packages, and maintaining coalition coordination.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Cabinet portfolio disputes between NCP and Congress surface immediately, generating critical press.", eff(-1, 0, -2, -2)), 1.2),
        reaction("characterize_coalition_as_opportunistic", "Characterize the leadership change as a sign of panic over economic decline and demand early assembly elections.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(12, "New CM's clean image and background receive positive media reviews, dampening the attack.", eff(-1, 0, -1, -1)), 1.25),
        reaction("propose_all_party_energy_task_force", "Propose an all-party energy task force to draft a long-term power generation roadmap for the state without foreign dependency.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Ideological divisions over privatization prevent the task force from releasing a consensus report.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2002-06
ITEMS_2001_2005.append(make_news(
    key="up2002_2002_06_ambेडकर_memorials_launch",
    month="2002-06",
    title="CM Mayawati Launches Ambedkar Memorial Projects in Lucknow",
    desc="Chief Minister Mayawati launches construction of the Ambedkar Memorial Park (Ambedkar Udyan) in Lucknow. Opposition parties criticize the allocation of state funds for memorials.",
    tags=['identity', 'politics', 'economy'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("defend_memorials_as_dalit_pride", "Defend the memorials as long-overdue symbols of Dalit pride and historical representation.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Opposition files public interest litigations, accusing the government of spending public money for self-promotion.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_diversion_to_hospitals", "Expose budget files of the project and demand the funds be diverted to construct rural primary health centers.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(14, "Dalit voter organizations interpret the demand as anti-Dalit bias, shifting support away.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_state_harmony_committee", "Propose a state harmony committee representing all community leaders to discuss grievances peacefully.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing by key members delays the release of the committee's recommendations.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.25)
    ]
))

# 2002-07
ITEMS_2001_2005.append(make_news(
    key="up2002_2002_07_law_and_order_debates",
    month="2002-07",
    title="UP Assembly Heated Debates Over Law and Order",
    desc="Samajwadi Party opposition leads multiple walkouts in the assembly over crime rates, alleging that local police are targetting political opponents.",
    tags=['politics', 'law_order'],
    base_w=1.1, profile="politics",
    reactions=[
        reaction("announce_police_modernization_grant", "Announce state funding for local police patrol vehicles and state-of-the-art forensic labs in all zones.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(15, "Audit uncovers irregularities in vehicle procurement tenders, causing media criticism.", eff(-1, 0, -2, -2)), 1.15),
        reaction("lead_assembly_walkouts", "Lead walkouts in the assembly, holding placards detailing crimes in the ruling MLAs' home districts.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "Speaker suspends protesting MLAs, allowing legislative bills to pass without opposition input.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_digitized_crime_registry", "Propose a public, online database of all active FIRs by district to improve transparency in police actions.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Police department cites privacy rules, refusing to share case data online.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2002-08
ITEMS_2001_2005.append(make_news(
    key="up2002_2002_08_western_up_power_protests",
    month="2002-08",
    title="Farmers Protest Tubewell Power Tariff Hikes in Western UP",
    desc="Farmer groups block electricity board offices in Meerut and Moradabad. They protest the recent increase in tubewell electricity tariffs during the sowing season.",
    tags=['rural', 'agriculture', 'protest'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("suspend_tariff_hike_for_tubewells", "Suspend the tariff hike for tubewells for the current cropping season, providing state power subsidies.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "State electricity utility reports severe losses, forcing longer power cuts in nearby cities.", eff(-1, 0, -2, -2)), 1.25),
        reaction("lead_farmers_sit_in_board_offices", "Lead farmer sit-ins and demand a statutory board to fix agricultural power rates with farmer representation.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Utility security calls local police, leading to tear gas use and negative media.", eff(-1, 0, -2, -2)), 1.2),
        reaction("propose_solar_pump_subsidies", "Propose a state-backed subsidy scheme for solar irrigation pumps to reduce dependence on grid power.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(10, "Solar pump suppliers take months to deliver units, frustrating early applicants.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 3}, weight=0.2)
    ]
))

# 2002-09
ITEMS_2001_2005.append(make_news(
    key="up2002_2002_09_raja_bhaiya_pota_arrest",
    month="2002-09",
    title="Independent MLA Raja Bhaiya Arrested Under POTA",
    desc="The UP government orders the arrest of independent MLA Raghuraj Pratap Singh (Raja Bhaiya) under the Prevention of Terrorism Act (POTA) on charges of conspiring against CM.",
    tags=['politics', 'law_order', 'identity'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("defend_arrest_as_national_security", "Defend the arrest in court as a vital step to check criminal politicians and maintain law and order.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(20, "Thakur community organizations stage mass rallies in central UP, protesting selective targeting.", eff(-2, 0, -2, -3)), 1.2),
        reaction("condemn_pota_misuse_hold_rallies", "Condemn the arrest as misuse of terror laws for political vendettas and hold solidarity rallies with the MLA.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(16, "Government releases police logs of weapons recovered from the MLA's estate, shifting media narrative.", eff(-1, 0, -2, -2)), 1.25),
        reaction("propose_judicial_review_pota_cases", "Propose a high court judge-led review panel to scan all POTA arrests in the state before trial starts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(12, "Panel reviews are delayed, leaving the MLA in custody and protests active.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"violenceIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2002-10
ITEMS_2001_2005.append(make_news(
    key="up2002_2002_10_bjp_bsp_cabinet_friction",
    month="2002-10",
    title="BJP-BSP Cabinet Friction Intensifies Over Transfers",
    desc="Tension rises within the ruling coalition as state BJP leaders accuse CM Mayawati of unilaterally transferring administrative officers in their constituencies without consultation.",
    tags=['politics', 'governance'],
    base_w=1.1, profile="governance",
    reactions=[
        reaction("convene_coalition_coordination_committee", "Convene a coalition coordination committee to negotiate officer transfer lists and restore alliance trust.",
                 ['GOVERNMENT'], eff(1, 0, 3, 2),
                 {},
                 risk(15, "Local party workers contest the consensus list, continuing district-level friction.", eff(-1, 0, -2, -2)), 1.15),
        reaction("exploit_frictions_demand_assembly_dissolution", "Expose cabinet bickerings in press conferences and demand the Governor dissolve the assembly for fresh elections.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "BJP high command instructs state leaders to patch up, leaving the opposition's pitch flat.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_fixed_bureaucratic_tenures", "Propose establishing a Civil Services Board to enforce fixed tenures for administrative officers, reducing political interference.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political parties ignore the proposal as a limit on their executive powers.", eff(0, 0, -2, -1)), 1.05),
        no_comment(weight=0.35)
    ]
))

# 2002-11
ITEMS_2001_2005.append(make_news(
    key="up2002_2002_11_bundelkhand_drought_crisis",
    month="2002-11",
    title="Bundelkhand Drought: Farmers Demand Emergency Water Relief",
    desc="Failure of monsoon rains leaves Bundelkhand reservoirs dry. Crop failures spur farmer distress, and local bodies demand immediate tanker supplies and debt waiver.",
    tags=['disaster', 'relief', 'rural'],
    base_w=1.25, profile="disaster_relief",
    reactions=[
        reaction("declare_bundelkhand_drought_waiver", "Declare Bundelkhand drought-affected, waiving land revenue and organizing water tanker supplies to villages.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Water tankers are diverted by local block politicians to allied villages, prompting scuffles.", eff(-1, 0, -2, -2)), 1.25),
        reaction("lead_bundelkhand_relief_kitchens", "Lead volunteer groups running community animal fodder centers and food kitchens in Bundelkhand.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(12, "Fodder transport vehicles are delayed at toll posts, limiting delivery reach.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_all_party_relief_coordination", "Propose an all-party disaster relief coordination cell to streamline distribution of emergency supplies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(10, "Administrative delays in cargo clearance temporarily halt relief shipments.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2002-12
ITEMS_2001_2005.append(make_news(
    key="up2002_2002_12_taj_corridor_construction",
    month="2002-12",
    title="Agra Taj Heritage Corridor Construction Commences",
    desc="Construction work begins on the Yamuna riverbed behind the Taj Mahal for the Taj Heritage Corridor project. Tourism builders welcome the development.",
    tags=['economy', 'governance', 'environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("fast_track_corridor_construction", "Fast-track construction work to complete the first phase of the tourism complex before the peak season.",
                 ['GOVERNMENT'], eff(1, 0, 3, 2),
                 {},
                 risk(20, "Pollution boards raise objections over lack of safety clearances, halting work.", eff(-1, 0, -2, -2)), 1.15),
        reaction("expose_unauthorized_river_landfilling", "Expose instances of illegal river sand dredging by the construction contractor, demanding police arrests.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(14, "Contractor sues the opposition for defamation, dragging the debate into court.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_independent_riverbed_audit", "Propose an independent committee of river hydrologists and archeologists to redesign the project safely.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Design changes delay project delivery by several years, increasing costs.", eff(0, 0, -1, -1)), 1.05),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2003-01
ITEMS_2001_2005.append(make_news(
    key="up2003_2003_01_graft_video_controversy",
    month="2003-01",
    title="Graft Video Controversy: CM Mayawati Facing Opposition Attacks",
    desc="Opposition parties release a video tape showing CM Mayawati allegedly asking BSP MLAs to contribute a portion of their local development funds to the party treasury.",
    tags=['corruption', 'politics', 'scam'],
    base_w=1.2, profile="corruption",
    reactions=[
        reaction("dismiss_video_as_doctored_conspiracy", "Dismiss the video as doctored by political opponents and order a forensic investigation into the source.",
                 ['GOVERNMENT'], eff(1, -2, 3, 2),
                 {},
                 risk(18, "Forensic lab reports confirm the voice signature matches, intensifying media attacks.", eff(-1, 0, -2, -3)), 1.2),
        reaction("demand_cm_resignation_protest_marches", "Organise state-wide protest marches demanding the CM's resignation and a judicial probe into party funds.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Security forces detain the marching leaders, leading to brief scuffles and traffic jams.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_digitized_audit_portal", "Propose a digitized public audit portal to track all related government transactions and block corruption.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(12, "Technical integration delays keep the portal offline, drawing criticism for slow delivery.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"corruptionIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2003-02
ITEMS_2001_2005.append(make_news(
    key="up2003_2003_02_raja_bhaiya_father_arrest",
    month="2003-02",
    title="Raja Bhaiya's Father Arrested; Thakur Groups Protest",
    desc="The UP government orders the arrest of Raja Bhaiya's father under POTA. Thakur caste organizations stage massive demonstrations in Central UP, alleging bias.",
    tags=['politics', 'identity', 'law_order'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("enforce_arrest_maintain_order", "Enforce the arrest to show that no political family is above the law, deploying extra police to Pratapgarh.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Thakur community leaders in the BJP express public anger, straining the coalition.", eff(-2, 0, -2, -3)), 1.2),
        reaction("join_pratapgarh_thakur_rallies", "Join the community protest rallies in Pratapgarh and demand the immediate revocation of POTA cases against the family.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Other backward caste voter groups view the alliance with Thakur elites negatively.", eff(-1, 0, -2, -2)), 1.2),
        reaction("propose_state_harmony_committee", "Propose a state harmony committee representing all community leaders to discuss grievances peacefully.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing by key members delays the release of the committee's recommendations.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.25)
    ]
))

# 2003-03
ITEMS_2001_2005.append(make_news(
    key="up2003_2003_03_taj_corridor_sc_halt",
    month="2003-03",
    title="Supreme Court Halts Agra Taj Heritage Corridor Work",
    desc="The Supreme Court of India orders an immediate halt to all construction work on the Taj Heritage Corridor project, citing threats to monument safety and Yamuna ecology.",
    tags=['environment', 'governance', 'politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("accept_sc_order_appoint_inquiry", "Accept the Supreme Court order, halt construction immediately, and appoint a state cabinet committee to review execution errors.",
                 ['GOVERNMENT'], eff(1, 0, 3, 2),
                 {},
                 risk(15, "Opposition claims the cabinet committee is a cover-up, continuing their assembly attacks.", eff(-1, 0, -2, -2)), 1.15),
        reaction("demand_cbi_probe_minister_kickbacks", "Demand a CBI investigation into kickbacks allegedly received by senior departments from Yamuna sand contractors.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "State departments delay file transfers to the CBI, slowing down initial steps.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_independent_riverbed_audit", "Propose an independent committee of river hydrologists and archeologists to redesign the project safely.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Design changes delay project delivery by several years, increasing costs.", eff(0, 0, -1, -1)), 1.05),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2003-04
ITEMS_2001_2005.append(make_news(
    key="up2003_2003_04_madhumita_shukla_murder",
    month="2003-04",
    title="Poetess Madhumita Shukla Shot Dead in Lucknow",
    desc="Young poetess Madhumita Shukla is shot dead in her Lucknow apartment. Media reports allege her association with a senior BSP minister, sparking a political storm.",
    tags=['violence', 'politics', 'law_order', 'crisis'],
    base_w=1.3, profile="security_crisis",
    reactions=[
        reaction("order_police_probe_suspend_officers", "Order a fast-track police investigation and suspend the local circle officer to ensure a fair probe.",
                 ['GOVERNMENT'], eff(1, -1, 3, 2),
                 {},
                 risk(20, "Evidence of links to the cabinet minister is leaked to media, causing public outrage.", eff(-2, 0, -3, -4)), 1.2),
        reaction("demand_cbi_investigation_murder", "Demand the case be transferred to the CBI immediately, alleging state police are destroying evidence to shield minister.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 5),
                 {},
                 risk(16, "Government delays the formal request to the Centre, drawing critical editorials.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_security_advisory_board", "Propose setting up an independent security advisory board with defense experts to upgrade local safety protocols.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(12, "Implementation of board recommendations is delayed due to funding shortages.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"massCasualtyIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2003-05
ITEMS_2001_2005.append(make_news(
    key="up2003_2003_05_amarmani_tripathi_probe",
    month="2003-05",
    title="Madhumita Probe Points to Minister Amarmani Tripathi",
    desc="Police diaries and telephone logs leaked to the press indicate the involvement of BSP Minister Amarmani Tripathi in the Madhumita Shukla murder case. BJP partners demand action.",
    tags=['politics', 'corruption', 'violence'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("remove_minister_pending_probe", "Remove Minister Amarmani Tripathi from the cabinet pending completion of the police investigation.",
                 ['GOVERNMENT'], eff(2, -1, 3, 3),
                 {},
                 risk(18, "Minister's loyalist MLAs threaten to pull out of the coalition, creating government instability.", eff(-2, 0, -2, -2)), 1.2),
        reaction("expose_minister_criminal_records", "Hold press conferences detailing the minister's past criminal records, demanding his immediate arrest.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Supporters of the minister stage local counter-protests, causing minor transport halts.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_legislative_roundtable", "Propose a legislative roundtable with representatives from all parties to draft a consensus policy on the issue.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 2, 2),
                 {},
                 risk(8, "Lack of consensus among members delays the final report, rendering it inactive.", eff(0, 0, -1, -1)), 1.05),
        no_comment(hidden={"corruptionIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2003-06
ITEMS_2001_2005.append(make_news(
    key="up2003_2003_06_bjp_pressure_on_cm",
    month="2003-06",
    title="BJP High Command Pressures CM Mayawati to Act on Minister",
    desc="With the Madhumita case generating national headlines, the central BJP leadership pressures CM Mayawati to refer the case to the CBI or face withdrawal of support.",
    tags=['politics', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("refer_case_to_cbi", "Refer the Madhumita Shukla murder case to the CBI, committing to full state police cooperation.",
                 ['GOVERNMENT'], eff(2, -1, 4, 3),
                 {},
                 risk(15, "CBI summons the CM's close aides, creating internal administration panic.", eff(-2, 0, -2, -2)), 1.2),
        reaction("denounce_alliance_weakness_campaign", "Organise street corner campaigns highlighting the moral failure and instability of the BJP-BSP alliance.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(12, "National issues dominate headlines, diluting local impact of campaigns.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_fixed_ministerial_performance_indices", "Propose introducing a quarterly public performance index for all state departments to monitor minister delivery.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Political parties dismiss the index idea as an academic exercise outside democratic realities.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2003-07
ITEMS_2001_2005.append(make_news(
    key="up2003_2003_07_cbi_searches_taj_corridor",
    month="2003-07",
    title="CBI Conducts Searches in Taj Corridor Scam Investigation",
    desc="CBI teams raid offices of Uttar Pradesh departments and contract firms, seizing documents relating to Taj Heritage Corridor project expenditure.",
    tags=['corruption', 'scam', 'politics'],
    base_w=1.2, profile="corruption",
    reactions=[
        reaction("cooperate_with_cbi_investigation", "Instruct all departments to cooperate with the CBI team and submit required financial files immediately.",
                 ['GOVERNMENT'], eff(2, -1, 3, 3),
                 {},
                 risk(15, "Raid documents reveal signatures of senior coalition leaders, sparking mutual blame.", eff(-2, 0, -2, -2)), 1.2),
        reaction("demand_prosecution_of_senior_ministers", "Hold legislative debates demanding the immediate prosecution of senior cabinet ministers named in the CBI logs.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Speaker rejects the debate request, leading to opposition walkout and local protests.", eff(-1, 0, -2, -2)), 1.25),
        reaction("propose_digitized_audit_portal", "Propose a digitized public audit portal to track all related government transactions and block corruption.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(12, "Technical integration delays keep the portal offline, drawing criticism for slow delivery.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"corruptionIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2003-08
ITEMS_2001_2005.append(make_news(
    key="up2003_2003_08_coalition_collapses_mulayam_cm",
    month="2003-08",
    title="BSP-BJP Coalition Collapses; Mulayam Singh Sworn In as CM",
    desc="Following BJP support withdrawal, Mayawati resigns as Chief Minister. Mulayam Singh Yadav is sworn in as CM after assembling support from rebel MLAs and Congress.",
    tags=['politics', 'governance', 'crisis'],
    base_w=1.3, profile="governance",
    reactions=[
        reaction("announce_common_development_agenda", "Announce a common development agenda focused on rural industrial parks and removing POTA cases.",
                 ['GOVERNMENT'], eff(2, 0, 4, 3),
                 {},
                 risk(18, "Portfolio allocations spark disputes with allied Congress, delaying cabinet formation.", eff(-1, 0, -2, -2)), 1.2),
        reaction("protest_horse_trading_governor_action", "Organise public demonstrations protesting the Governor's decision to invite the coalition, alleging horse-trading of MLAs.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(14, "Voters welcome the stability of the new majority, diluting the protest impact.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_legislative_roundtable", "Propose a legislative roundtable with representatives from all parties to draft a consensus policy on the issue.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 2, 2),
                 {},
                 risk(8, "Lack of consensus among members delays the final report, rendering it inactive.", eff(0, 0, -1, -1)), 1.05),
        no_comment(hidden={"democracyDefenceCredit": -3}, weight=0.2)
    ]
))

# 2003-09
ITEMS_2001_2005.append(make_news(
    key="up2003_2003_09_mulayam_revokes_pota_cases",
    month="2003-09",
    title="CM Mulayam Singh Orders Revocation of POTA Cases",
    desc="Chief Minister Mulayam Singh Yadav orders the immediate revocation of POTA cases against MLA Raja Bhaiya and his father, fulfilling a key coalition assurance.",
    tags=['politics', 'law_order', 'identity'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("enforce_pota_revocation_release", "Instruct the jail department to release Raja Bhaiya and withdraw all POTA notification files from court.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Central security departments raise objections, claiming POTA is under federal jurisdiction.", eff(-1, 0, -2, -2)), 1.2),
        reaction("protest_freeing_criminals_terror_laws", "Organise legislative debates protesting the revocation, claiming the government is shielding criminal elites.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(12, "Raja Bhaiya's supporters hold grand welcome rallies, overshadowing opposition debates.", eff(0, 0, -2, -2)), 1.2),
        reaction("propose_state_harmony_committee", "Propose a state harmony committee representing all community leaders to discuss grievances peacefully.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing by key members delays the release of the committee's recommendations.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 1}, weight=0.25)
    ]
))

# 2003-10
ITEMS_2001_2005.append(make_news(
    key="up2003_2003_10_vhp_ayodhya_arrests",
    month="2003-10",
    title="VHP Ayodhya Sankalp Diwas: Thousands Detained",
    desc="High tension sweeps Ayodhya as the VHP hosts a Sankalp Diwas. The state administration deploys massive security, detaining thousands of activists at rail and road borders.",
    tags=['security', 'politics', 'crisis'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("maintain_border_barricades_security", "Maintain strict border barricades, suspend local train routes to Faizabad, and coordinate police patrols in sensitive wards.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(20, "Commuters protest train suspensions, causing travel gridlocks across East UP.", eff(-1, 0, -2, -3)), 1.2),
        reaction("demand_security_relaxation_activists", "Lobby the Union home ministry to direct the state government to allow peaceful assembly and release activists.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Local peace groups criticize the opposition for escalating communal tensions.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_security_advisory_board", "Propose setting up an independent security advisory board with defense experts to upgrade local safety protocols.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(12, "Implementation of board recommendations is delayed due to funding shortages.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"securityIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2003-11
ITEMS_2001_2005.append(make_news(
    key="up2003_2003_11_amarmani_tripathi_cbi_arrest",
    month="2003-11",
    title="CBI Arrests Former Minister Amarmani Tripathi in Murder Case",
    desc="The CBI arrests former minister Amarmani Tripathi in Lucknow for his role in the Madhumita Shukla murder, dealing a political blow to his supporters in the coalition.",
    tags=['violence', 'politics', 'corruption'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("distance_government_from_tripathi", "Issue state statements clarifying that the law will take its own course and distance the party from Tripathi's actions.",
                 ['GOVERNMENT'], eff(2, -1, 3, 3),
                 {},
                 risk(15, "Tripathi's localized caste base in Gorakhpur organizes protest blockades against the state.", eff(-1, 0, -2, -2)), 1.2),
        reaction("expose_criminal_ministerial_patronage", "Organise public campaigns showcasing links between the CM's circle and arrested MLAs, demanding independent trials.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "State police releases records of actions taken, reducing the effectiveness of campaigns.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_legislative_roundtable", "Propose a legislative roundtable with representatives from all parties to draft a consensus policy on the issue.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 2, 2),
                 {},
                 risk(8, "Lack of consensus among members delays the final report, rendering it inactive.", eff(0, 0, -1, -1)), 1.05),
        no_comment(hidden={"corruptionIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2003-12
ITEMS_2001_2005.append(make_news(
    key="up2003_2003_12_sugarcane_sap_hike",
    month="2003-12",
    title="State Government Announces revision of Sugarcane SAP",
    desc="The UP cabinet announces a significant hike in the State Advisory Price (SAP) for sugarcane. Farmer unions welcome the step but private mills warn of delayed crushing.",
    tags=['rural', 'agriculture', 'good_news'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("advertise_sap_hike_as_farmer_victory", "Advertise the SAP hike as a historic victory for marginal farmers and coordinate mill opening dates.",
                 ['GOVERNMENT'], eff(2, 0, 4, 4),
                 {},
                 risk(18, "Private mills halt crushing operations, claiming the SAP is higher than global sugar rates.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_interest_on_crushing_delays", "Demand the government penalize private mills that delay crushing and pay interest to farmers who wait.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Mill owners challenge penalties in court, dragging the dispute out.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_tripartite_mediation_council", "Propose a tripartite mediation council representing labor unions, industry leaders, and state officials.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Radical sections of the union boycott the mediation, continuing localized protests.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 2}, weight=0.25)
    ]
))

# 2004-01
ITEMS_2001_2005.append(make_news(
    key="up2004_2004_01_up_development_council_launch",
    month="2004-01",
    title="Mulayam Singh Yadav Launches UP Development Council",
    desc="CM Mulayam Singh Yadav launches the UP Development Council to attract major corporate investments, inviting industry leaders to set up units in the state.",
    tags=['economy', 'industry', 'good_news'],
    base_w=1.1, profile="governance",
    reactions=[
        reaction("advertise_investment_deals", "Advertise major corporate investment agreements in industrial zones (Noida/Kanpur) to boost investor confidence.",
                 ['GOVERNMENT'], eff(2, 0, 4, 3),
                 {},
                 risk(15, "Opposition claims land is allocated at throwaway prices, initiating localized land disputes.", eff(-1, 0, -2, -2)), 1.2),
        reaction("expose_crony_capitalism_allocations", "Expose instances of prime land allocated to specific corporate houses without transparent bidding.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Business chambers issue statements criticizing the opposition for blocking jobs, affecting urban support.", eff(-1, 0, -1, -2)), 1.25),
        reaction("propose_independent_investment_audit", "Propose a state audit of all industrial land allocations by a panel under a retired high court judge.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Audit process delays ongoing corporate acquisitions, slowing down investments.", eff(0, 0, -2, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2004-02
ITEMS_2001_2005.append(make_news(
    key="up2004_2004_02_eastern_up_power_grid_failure",
    month="2004-02",
    title="Power Grid Failure Causes Blackout in Eastern UP",
    desc="A major transmission line failure in the eastern grid causes severe power blackouts in Gorakhpur and Basti divisions during board exam preparations.",
    tags=['disaster', 'infrastructure', 'crisis'],
    base_w=1.1, profile="health_crisis",
    reactions=[
        reaction("divert_power_urban_to_student_zones", "Divert electricity from heavy manufacturing zones to student residential centers during exam study hours.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(15, "Industrial associations protest, claiming factory production losses and worker layoffs.", eff(-1, 0, -2, -2)), 1.15),
        reaction("demand_emergency_grid_upgrade_funds", "Demand immediate state budget allocations to upgrade central grid sub-stations in rural Eastern UP.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(10, "Finance department claims budget limits prevent immediate capital releases.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_infrastructure_oversight_committee", "Propose a joint civic-expert oversight committee to monitor construction quality and manage traffic impact.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Inter-departmental coordination issues delay committee meetings, slowing down resolution of issues.", eff(0, 0, -1, -1)), 1.05),
        no_comment(hidden={"disasterIgnoredMemory": 2}, weight=0.25)
    ]
))

# 2004-03
ITEMS_2001_2005.append(make_news(
    key="up2004_2004_03_sp_kalyan_singh_alliance",
    month="2004-03",
    title="Samajwadi Party Aligns with Kalyan Singh's Faction",
    desc="Ahead of the Lok Sabha elections, Samajwadi Party completes seat-sharing negotiations with Kalyan Singh's Rashtriya Kranti Party to consolidate backward caste support.",
    tags=['election', 'politics'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("campaign_on_joint_backward_solidarity", "Campaign heavily on backward caste solidarity and joint development schemes in rural rallies.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Minority voter organizations express concern over Kalyan Singh's past role, reducing support in mixed seats.", eff(-2, 0, -2, -2)), 1.2),
        reaction("highlight_opportunistic_alliance", "Expose past critical statements exchanged by both leaders and campaign on opportunistic alliances.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "Rural voters focus on local ticket candidates rather than past leadership statements.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_legislative_roundtable", "Propose a legislative roundtable with representatives from all parties to draft a consensus policy on the issue.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 2, 2),
                 {},
                 risk(8, "Lack of consensus among members delays the final report, rendering it inactive.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2004-04
ITEMS_2001_2005.append(make_news(
    key="up2004_2004_04_lucknow_saree_stampede",
    month="2004-04",
    title="Lucknow Stampede: 21 Women Killed During Saree Distribution",
    desc="A stampede at a birthday event hosted by a BJP candidate in Lucknow leads to the deaths of 21 women during free saree distribution, sparking national outrage.",
    tags=['violence', 'election', 'crisis'],
    base_w=1.3, profile="security_crisis",
    reactions=[
        reaction("register_firs_against_event_organisers", "Instruct the police to register criminal negligence FIRs against the organizers and order a judicial inquiry.",
                 ['GOVERNMENT'], eff(2, -1, 3, 3),
                 {},
                 risk(18, "BJP leaders claim the police actions are politically motivated, leading to street protests.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_candidate_disqualification_saree", "Demand the Election Commission disqualify the candidate for violating the model code of conduct and distributing freebies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 4),
                 {},
                 risk(15, "EC processes take weeks, shifting media focus to next phase campaigns.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_strict_campaign_distribution_ban", "Propose an all-party agreement banning all material distribution events during election campaign phases.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(10, "Local cadres continue distributing material off-camera, rendering the ban ineffective.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"massCasualtyIgnoredMemory": 4}, weight=0.1)
    ]
))

# 2004-05
ITEMS_2001_2005.append(make_news(
    key="up2004_2004_05_general_election_results",
    month="2004-05",
    title="Lok Sabha Results: SP and BSP Secure Major Gains in UP",
    desc="General Election results show Samajwadi Party winning 35 seats and Bahujan Samaj Party securing 19 seats in UP, cementing their positions as national kingmakers.",
    tags=['election', 'politics', 'good_news'],
    base_w=1.25, profile="election",
    reactions=[
        reaction("leverage_seats_for_central_packages", "Leverage the seats to negotiate special central development and infrastructure packages for UP in the new cabinet.",
                 ['GOVERNMENT'], eff(2, 0, 4, 3),
                 {},
                 risk(16, "Central coalition demands local concessions, delaying package release.", eff(-1, 0, -2, -2)), 1.2),
        reaction("campaign_on_national_policy_influence", "Campaign on regional representation, stating that BSP's Dalit agenda will now influence national policy files.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(12, "Inner party rivalries over central portfolios weaken local unit focus.", eff(-1, 0, -2, -1)), 1.2),
        reaction("propose_state_harmony_committee", "Propose a state harmony committee representing all community leaders to discuss grievances peacefully.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing by key members delays the release of the committee's recommendations.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2004-06
ITEMS_2001_2005.append(make_news(
    key="up2004_2004_06_ghaghara_river_floods",
    month="2004-06",
    title="Ghaghara River Crosses Danger Mark; Villages Evacuated",
    desc="Heavy pre-monsoon rains in Nepal cause the Ghaghara river to cross danger marks in Bahraich. The administration orders evacuation of low-lying floodplains.",
    tags=['disaster', 'relief', 'rural'],
    base_w=1.1, profile="disaster_relief",
    reactions=[
        reaction("deploy_boats_evacuate_plains", "Deploy rescue boats, set up high-ground relief tents, and arrange dry ration supplies for evacuated families.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Relief tents lack proper sanitation, leading to minor water-borne disease outbreak.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_permanent_embankment_upgrades", "Demand that the state government construct concrete river embankments rather than repeated temporary sandbagging.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "High project cost prevents immediate approval from finance departments.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_all_party_relief_coordination", "Propose an all-party disaster relief coordination cell to streamline distribution of emergency supplies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(10, "Administrative delays in cargo clearance temporarily halt relief shipments.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.25)
    ]
))

# 2004-07
ITEMS_2001_2005.append(make_news(
    key="up2004_2004_07_police_recruitment_scam",
    month="2004-07",
    title="Police Recruitment Scam: Opposition Alleges Systemic Bribery",
    desc="Opposition parties release documents alleging that recruitment boards accepted bribes for constable appointments in multiple district lines. Protests held in Lucknow.",
    tags=['corruption', 'scam', 'governance'],
    base_w=1.2, profile="corruption",
    reactions=[
        reaction("order_departmental_probe_into_recruitment", "Order a departmental inquiry led by an IPS officer and suspend flagged board members pending results.",
                 ['GOVERNMENT'], eff(1, -2, 3, 2),
                 {},
                 risk(18, "Inquiry report delays, leading to protests by candidate groups demanding fresh tests.", eff(-1, 0, -2, -2)), 1.15),
        reaction("demand_judicial_commission_into_bribes", "Demand a high court judge-led commission to scan recruitment sheets and cancel selected candidates list.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Judicial process is slow, and selected candidates file counter-appeals, stalling recruitment.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_digitized_audit_portal", "Propose a digitized public audit portal to track all related government transactions and block corruption.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(12, "Technical integration delays keep the portal offline, drawing criticism for slow delivery.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"corruptionIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2004-08
ITEMS_2001_2005.append(make_news(
    key="up2004_2004_08_reliance_dadri_announcement",
    month="2004-08",
    title="Reliance Dadri Mega Power Project Announced by CM",
    desc="Chief Minister Mulayam Singh Yadav announces a mega gas-based power project in Dadri, Ghaziabad, to be executed by Reliance Energy, promising to solve the state's power shortages.",
    tags=['economy', 'industry', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("fast_track_gas_pipeline_clearance", "Fast-track land acquisition and gas pipeline right-of-way clearances for the Dadri plant construction.",
                 ['GOVERNMENT'], eff(2, 0, 4, 3),
                 {},
                 risk(20, "Local farmers form resistance committees, protesting acquisition rates in Dadri villages.", eff(-1, 0, -2, -3)), 1.2),
        reaction("demand_environment_impact_assessment", "Demand a detailed environmental and local livelihood impact assessment of the project before land is transferred.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Business lobbies accuse the opposition of blocking power supply, reducing urban support.", eff(-1, 0, -1, -1)), 1.15),
        reaction("propose_tripartite_mediation_council", "Propose a tripartite mediation council representing labor unions, industry leaders, and state officials.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Radical sections of the union boycott the mediation, continuing localized protests.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"economyMissedOpportunity": 2}, weight=0.25)
    ]
))

# 2004-09
ITEMS_2001_2005.append(make_news(
    key="up2004_2004_09_goonda_raj_campaign",
    month="2004-09",
    title="Opposition Launches Statewide 'Goonda Raj' Protest Campaign",
    desc="BSP and BJP launch a coordinated protest campaign against the ruling Samajwadi Party, alleging a complete breakdown of law and order and the rise of criminal gangs.",
    tags=['politics', 'law_order', 'protest'],
    base_w=1.2, profile="protest",
    reactions=[
        reaction("announce_gangster_act_crackdown", "Direct police commissioners to invoke the Gangster Act against active mafia networks and confiscate illegal properties.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Localized gang clashes occur during police raids, raising security alerts in Eastern UP.", eff(-1, 0, -2, -2)), 1.2),
        reaction("organise_law_and_order_rallies", "Organise large-scale public rallies in major cities, showcasing dossiers of criminal cases against ruling coalition MLAs.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Rally blockades disrupt city transport, drawing complaints from commuter unions.", eff(-1, 0, -1, -2)), 1.25),
        reaction("propose_security_advisory_board", "Propose setting up an independent security advisory board with defense experts to upgrade local safety protocols.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(12, "Implementation of board recommendations is delayed due to funding shortages.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"violenceIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2004-10
ITEMS_2001_2005.append(make_news(
    key="up2004_2004_10_bundelkhand_loan_waiver",
    month="2004-10",
    title="Cabinet Announces Interest Waiver for Bundelkhand Farmers",
    desc="To check agrarian distress, the state cabinet announces an interest waiver on cooperative bank crop loans for marginal farmers in Bundelkhand.",
    tags=['rural', 'agriculture', 'good_news'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("release_bank_compensation_funds", "Release direct state compensation to rural cooperative banks to offset the interest loss and restart credit lines.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Banks report delay in state compensation transfers, slowing down fresh loan disbursals.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_complete_principal_loan_waiver", "Demand a complete waiver of the loan principal, claiming interest waiver is insufficient for indebted families.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "State budget deficit prevents principal waiver, leaving the demand unfulfilled.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_rural_stabilization_policy", "Propose a bipartisan rural development and price stabilization task force to draft long-term support policies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Lack of immediate budget allocation delays the implementation of the task force proposals.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 2}, weight=0.25)
    ]
))

# 2004-11
ITEMS_2001_2005.append(make_news(
    key="up2004_2004_11_court_stays_constable_recruitment",
    month="2004-11",
    title="High Court Stays Police Constable Recruitment Over Bribery",
    desc="The Allahabad High Court issues a stay order halting the appointment of thousands of police constables, citing prima facie evidence of bribery and manipulation of marks sheets.",
    tags=['law_order', 'governance', 'corruption'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("accept_court_stay_appoint_new_committee", "Accept the stay, suspend the recruitment board chairman, and set up a new committee with transparent rules.",
                 ['GOVERNMENT'], eff(2, -1, 3, 3),
                 {},
                 risk(15, "Selected candidates hold protests outside the secretariat, demanding jobs.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_cbi_probe_into_recruitment", "Demand the CBI take over the police recruitment files, alleging systemic involvement of CM's close aides.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "CBI probe is delayed by state department files transfer disputes.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_digitized_audit_portal", "Propose a digitized public audit portal to track all related government transactions and block corruption.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(12, "Technical integration delays keep the portal offline, drawing criticism for slow delivery.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"corruptionIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2004-12
ITEMS_2001_2005.append(make_news(
    key="up2004_2004_12_amu_minority_reservation",
    month="2004-12",
    title="Aligarh Muslim University Minority Quota Proposal Sparks Debate",
    desc="A proposal to introduce a 50% reservation for Muslim candidates in post-graduate courses at Aligarh Muslim University (AMU) triggers intense political debate in the state.",
    tags=['identity', 'education', 'politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("support_amu_minority_status_quota", "Support the minority status and quota in legislative resolution, stating it protects minority educational rights.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Opposition coalitions organize student rallies, claiming the quota is unconstitutional.", eff(-2, 0, -2, -2)), 1.15),
        reaction("oppose_quota_as_unconstitutional", "Oppose the reservation scheme, claiming it violates central educational laws and court rulings.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Minority organizations accuse the opposition of bias, reducing local support.", eff(0, 0, -2, -2)), 1.2),
        reaction("propose_state_harmony_committee", "Propose a state harmony committee representing all community leaders to discuss grievances peacefully.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing by key members delays the release of the committee's recommendations.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.25)
    ]
))

# 2005-01
ITEMS_2001_2005.append(make_news(
    key="up2005_2005_01_raju_pal_murder",
    month="2005-01",
    title="BSP MLA Raju Pal Murdered in Allahabad; Curfew Imposed",
    desc="Bahujan Samaj Party MLA Raju Pal is shot dead in broad daylight in Allahabad, allegedly by gang members of local MP Atiq Ahmed. Widespread violence and curfews are reported.",
    tags=['violence', 'politics', 'crisis', 'law_order'],
    base_w=1.35, profile="security_crisis",
    reactions=[
        reaction("deploy_police_arrest_suspects", "Deploy massive police forces to Allahabad, declare curfews in sensitive zones, and order the arrest of named suspects.",
                 ['GOVERNMENT'], eff(1, -1, 3, 2),
                 {},
                 risk(20, "Supporters of the accused MP stage counter-protests, leading to police clashes.", eff(-2, 0, -3, -4)), 1.2),
        reaction("lead_statewide_condemnation_rallies", "Lead state-wide silent marches carrying photos of Raju Pal, demanding the immediate transfer of the probe to the CBI.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 5),
                 {},
                 risk(18, "Protests turn violent in Allahabad, drawing critical media coverage for public safety.", eff(-1, 0, -2, -2)), 1.25),
        reaction("propose_security_advisory_board", "Propose setting up an independent security advisory board with defense experts to upgrade local safety protocols.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(12, "Implementation of board recommendations is delayed due to funding shortages.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"massCasualtyIgnoredMemory": 4}, weight=0.1)
    ]
))

# 2005-02
ITEMS_2001_2005.append(make_news(
    key="up2005_2005_02_allahabad_protests_violence",
    month="2005-02",
    title="Allahabad Protests Peak Over Slow Raju Pal Probe",
    desc="Tension persists in Allahabad as Dalit organizations and BSP cadres block main roads. They accuse local police of failing to arrest the key conspirators behind the MLA's murder.",
    tags=['politics', 'protest', 'law_order', 'identity'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("fast_track_investigation_officer", "Appoint a senior IPS officer from outside the zone to lead the investigation and arrest the remaining named suspects.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(16, "Defense lawyers file stay petitions, delaying police custodial interrogation of suspects.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_home_minister_resignation_murder", "Demand the resignation of the state Home Minister, holding him responsible for police failures to protect MLAs.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(14, "Government rejects the resignation request, leading to assembly walkouts.", eff(0, 0, -2, -2)), 1.2),
        reaction("propose_state_harmony_committee", "Propose a state harmony committee representing all community leaders to discuss grievances peacefully.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing by key members delays the release of the committee's recommendations.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"securityIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2005-03
ITEMS_2001_2005.append(make_news(
    key="up2005_2005_03_industrial_investment_policy",
    month="2005-03",
    title="Mulayam Singh Yadav Announces New Industrial Investment Policy",
    desc="The UP government announces a new industrial investment policy offering tax concessions and fast-track land allocations for IT and automotive units in Noida and Kanpur.",
    tags=['economy', 'industry', 'good_news'],
    base_w=1.05, profile="economy_positive",
    reactions=[
        reaction("launch_industrial_advertising_campaign", "Launch a national advertising campaign to attract tech and automotive firms to UP, showcasing land availability.",
                 ['GOVERNMENT'], eff(2, 0, 4, 4),
                 {},
                 risk(15, "A sudden power grid outage in central zones causes production halts, drawing criticism.", eff(-1, 0, -3, -2)), 1.2),
        reaction("demand_local_youth_employment_guarantees", "Demand that the policy mandate a 70% job quota for local state university graduates in all subsidized units.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Industry chambers warn that job quotas will divert new investments to other states.", eff(-1, 0, -2, -3)), 1.15),
        reaction("propose_tripartite_mediation_council", "Propose a tripartite mediation council representing labor unions, industry leaders, and state officials.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Radical sections of the union boycott the mediation, continuing localized protests.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2005-04
ITEMS_2001_2005.append(make_news(
    key="up2005_2005_04_bundelkhand_farmer_suicides",
    month="2005-04",
    title="Bundelkhand Farmer Suicides Rise, Sparking Media Alerts",
    desc="A cluster of suicides among indebted cotton and soybean farmers in Bundelkhand districts draws national media coverage. Farm groups demand complete debt relief.",
    tags=['rural', 'agriculture', 'crisis'],
    base_w=1.3, profile="security_crisis",
    reactions=[
        reaction("launch_agrarian_distress_relief_package", "Announce an emergency crop package including subsidized seed distribution, direct cash grants, and family counseling camps.",
                 ['GOVERNMENT'], eff(2, 0, 4, 5),
                 {},
                 risk(16, "Logistical errors delay seed distribution, causing frustration in remote blocks.", eff(-2, 0, -3, -3)), 1.25),
        reaction("demand_immediate_private_debt_moratorium", "Demand the state government pass a moratorium on private moneylenders' activities in distressed districts.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(14, "Private lenders halt all informal credits, cutting off farmers' only source of immediate cash.", eff(-1, 0, -2, -2)), 1.2),
        reaction("propose_rural_stabilization_policy", "Propose a bipartisan rural development and price stabilization task force to draft long-term support policies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Lack of immediate budget allocation delays the implementation of the task force proposals.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"ruralUnrestIgnoredMemory": 4}, weight=0.15)
    ]
))

# 2005-05
ITEMS_2001_2005.append(make_news(
    key="up2005_2005_05_raju_pal_widow_by_election",
    month="2005-05",
    title="Raju Pal's Widow Wins Allahabad By-Election, Blow to SP",
    desc="Pooja Pal, the widow of murdered MLA Raju Pal, wins the high-profile Allahabad West assembly by-election, representing BSP. Political analysts describe the result as a public vote on law and order.",
    tags=['election', 'politics'],
    base_w=1.2, profile="election",
    reactions=[
        reaction("accept_verdict_commit_to_area_welfare", "Accept the verdict, congratulate the winner, and allocate civic development funds to Allahabad West.",
                 ['GOVERNMENT'], eff(1, 0, 3, 2),
                 {},
                 risk(12, "Internal party factions blame the local candidate for the defeat, causing local friction.", eff(-1, 0, -2, -1)), 1.15),
        reaction("declare_victory_against_criminal_influence", "Declare the victory a public mandate against criminal influence in politics and demand faster trial prosecutions.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(15, "Security alerts remain tight in the ward, limiting political celebrations.", eff(-1, 0, -2, -2)), 1.2),
        reaction("propose_legislative_roundtable", "Propose a legislative roundtable with representatives from all parties to draft a consensus policy on the issue.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 2, 2),
                 {},
                 risk(8, "Lack of consensus among members delays the final report, rendering it inactive.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2005-06
ITEMS_2001_2005.append(make_news(
    key="up2005_2005_06_noida_land_allotment_scandal",
    month="2005-06",
    title="Noida Land Allotment Audit Exposes Contractor Fraud",
    desc="A municipal audit of Noida authority land allotments reveals contractor fraud, alleging that premium residential plots were allocated at undervalued rates to shell companies.",
    tags=['corruption', 'scam', 'governance'],
    base_w=1.15, profile="corruption",
    reactions=[
        reaction("blacklist_shell_firms_and_prosecute", "Blacklist the flagged shell firms, cancel plot allotments, and file criminal cases against municipal engineers.",
                 ['GOVERNMENT'], eff(2, -2, 3, 3),
                 {},
                 risk(18, "Developers file court cases against cancellation, stalling real estate projects.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_cbi_investigation_into_noida_authority", "Demand a CBI investigation into the Noida authority, alleging systemic political linkages to plot undervaluation.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Noida authority departments delay access to files, slowing down the CBI's initial steps.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_digitized_audit_portal", "Propose a digitized public audit portal to track all related government transactions and block corruption.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(12, "Technical integration delays keep the portal offline, drawing criticism for slow delivery.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"corruptionIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2005-07
ITEMS_2001_2005.append(make_news(
    key="up2005_2005_07_ayodhya_terrorist_attack",
    month="2005-07",
    title="Terrorist Attack on Ayodhya Complex Neutralized",
    desc="Five armed terrorists attempt to breach the inner security perimeter of the Ram Janmabhoomi complex in Ayodhya. Security forces neutralize all attackers; one civilian is killed.",
    tags=['security', 'violence', 'crisis', 'law_order'],
    base_w=1.45, profile="security_crisis",
    reactions=[
        reaction("deploy_paramilitary_red_alert", "Declare a red alert across the state, deploy additional paramilitary units in Ayodhya, and tighten temple security.",
                 ['GOVERNMENT'], eff(2, 0, 4, 3),
                 {},
                 risk(22, "Extended curfews in mixed wards spark minor local resident clashes with security.", eff(-2, 0, -3, -4)), 1.25),
        reaction("demand_resignation_of_cabinet_failures", "Organise public demonstrations and demand the resignation of the state cabinet, citing intelligence and security failures.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 5),
                 {},
                 risk(20, "Protests are viewed as politicizing a national tragedy, drawing critical media editorials.", eff(-1, 0, -2, -2)), 1.25),
        reaction("propose_security_advisory_board", "Propose setting up an independent security advisory board with defense experts to upgrade local safety protocols.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(12, "Implementation of board recommendations is delayed due to funding shortages.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"massCasualtyIgnoredMemory": 5, "securityIgnoredMemory": 4}, weight=0.05)
    ]
))

# 2005-08
ITEMS_2001_2005.append(make_news(
    key="up2005_2005_08_law_and_order_governor_report",
    month="2005-08",
    title="Governor Sends Law and Order Report to Center",
    desc="The Governor of Uttar Pradesh sends a detailed report to the Union Home Ministry regarding the security situation, citing recent attacks and political killings.",
    tags=['politics', 'law_order'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("defend_state_law_order", "Defend the state's security actions in press conferences, claiming the Governor's report is politically motivated.",
                 ['GOVERNMENT'], eff(2, 0, 3, 2),
                 {},
                 risk(15, "Union home ministry issues a formal advisory to the state, causing political embarrassment.", eff(-1, 0, -2, -2)), 1.15),
        reaction("demand_imposition_of_presidents_rule", "Lobby central coalition leaders and demand the imposition of President's Rule in UP due to security collapse.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(12, "State ruling coalition MLAs show complete unity, making the demand look ineffective.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_legislative_roundtable", "Propose a legislative roundtable with representatives from all parties to draft a consensus policy on the issue.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 2, 2),
                 {},
                 risk(8, "Lack of consensus among members delays the final report, rendering it inactive.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.35)
    ]
))

# 2005-09
ITEMS_2001_2005.append(make_news(
    key="up2005_2005_09_gorakhpur_encephalitis_outbreak",
    month="2005-09",
    title="Encephalitis Outbreak Kills Over 500 Children in Gorakhpur",
    desc="A major outbreak of Japanese Encephalitis in Gorakhpur and surrounding divisions leads to the deaths of over 500 children. Government hospitals report severe bed shortages.",
    tags=['health', 'disaster', 'crisis', 'rural'],
    base_w=1.35, profile="health_crisis",
    reactions=[
        reaction("launch_emergency_pediatric_wings", "Allocate emergency funds to set up special pediatric wings in district hospitals and distribute fogging machines.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Durg shortages and high patient volume trigger doctor protests over hospital conditions.", eff(-1, 0, -2, -3)), 1.2),
        reaction("demand_central_medical_taskforce", "Demand the central health ministry deploy a pediatric taskforce to UP, alleging state medical failure.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "State health department rejects central interference, stalling taskforce deployment.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_clean_water_infrastructure_plan", "Propose a state-backed clean drinking water infrastructure plan in affected districts to prevent future outbreaks.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(10, "Funding and agency jurisdiction disputes delay water pipe laying in remote blocks.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"healthCrisisIgnoredMemory": 4}, weight=0.1)
    ]
))

# 2005-10
ITEMS_2001_2005.append(make_news(
    key="up2005_2005_10_mau_communal_riots",
    month="2005-10",
    title="Communal Riots in Mau; Curfews and High Security",
    desc="Clashes between two groups during a festival in Mau lead to arson, looting, and several casualties. The administration imposes curfews and shoots-on-sight orders.",
    tags=['identity', 'violence', 'crisis', 'law_order'],
    base_w=1.3, profile="security_crisis",
    reactions=[
        reaction("enforce_mau_curfew_arrest_provokers", "Enforce the Mau curfew strictly, arrest key community leaders inciting violence, and deploy rapid action force.",
                 ['GOVERNMENT'], eff(1, -1, 3, 2),
                 {},
                 risk(20, "Dalit and minority organizations accuse police of biased arrests, escalating tension.", eff(-2, 0, -3, -4)), 1.2),
        reaction("lead_peace_delegation_to_mau", "Lead an all-party peace delegation to Mau to interact with affected families and demand independent judicial inquiry.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(15, "Security forces block the delegation at borders, citing law and order risks.", eff(-1, 0, -2, -2)), 1.2),
        reaction("propose_state_harmony_committee", "Propose a state harmony committee representing all community leaders to discuss grievances peacefully.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing by key members delays the release of the committee's recommendations.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"massCasualtyIgnoredMemory": 4, "identityIssueMissed": 2}, weight=0.15)
    ]
))

# 2005-11
ITEMS_2001_2005.append(make_news(
    key="up2005_2005_11_krishnanand_rai_murder",
    month="2005-11",
    title="BJP MLA Krishnanand Rai Shot Dead in Ghazipur",
    desc="BJP MLA Krishnanand Rai and six of his associates are shot dead in Ghazipur district. Attackers used automatic weapons, causing political shock and widespread protests.",
    tags=['violence', 'politics', 'crisis', 'law_order'],
    base_w=1.4, profile="security_crisis",
    reactions=[
        reaction("transfer_ghazipur_police_cbi_request", "Order the immediate transfer of district police officers and request a CBI probe into the Ghazipur shootout.",
                 ['GOVERNMENT'], eff(1, -1, 3, 2),
                 {},
                 risk(20, "BJP leaders reject the transfers as cosmetic, organizing statewide dharnas.", eff(-2, 0, -3, -4)), 1.2),
        reaction("lead_solidarity_rallies_demand_arrests", "Lead massive silent rallies in Varanasi and Ghazipur, demanding the immediate arrest of the named mafia-politicians.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 5),
                 {},
                 risk(18, "Protesters block national highways, leading to clashes with police barricades.", eff(-1, 0, -2, -2)), 1.25),
        reaction("propose_security_advisory_board", "Propose setting up an independent security advisory board with defense experts to upgrade local safety protocols.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(12, "Implementation of board recommendations is delayed due to funding shortages.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"massCasualtyIgnoredMemory": 5, "securityIgnoredMemory": 4}, weight=0.05)
    ]
))

# 2005-12
ITEMS_2001_2005.append(make_news(
    key="up2005_2005_12_ghazipur_protests_rai_murder",
    month="2005-12",
    title="Ghazipur Protests Peak as BJP Leaders Hold Dharna",
    desc="Sustained protests over the murder of MLA Krishnanand Rai sweep across Ghazipur and Varanasi. Opposition leaders lead dharnas, demanding the arrest of MP Mukhtar Ansari.",
    tags=['politics', 'protest', 'law_order', 'identity'],
    base_w=1.3, profile="security_crisis",
    reactions=[
        reaction("fast_track_court_ghazipur", "Announce the setup of a fast-track court in Ghazipur to try all accused in the shootout within six months.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Defense lawyers file appeals, delaying the start of the fast-track court proceedings.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_assembly_censure_mafia_mlas", "Introduce private member resolutions in the assembly to censor and suspend MLAs linked to mafia syndicates.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(14, "Ruling coalition rejects the resolution, leading to a legislative deadlock.", eff(0, 0, -2, -2)), 1.2),
        reaction("propose_state_harmony_committee", "Propose a state harmony committee representing all community leaders to discuss grievances peacefully.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing by key members delays the release of the committee's recommendations.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"securityIgnoredMemory": 3, "identityIssueMissed": 2}, weight=0.2)
    ]
))

