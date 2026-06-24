from helper import reaction, no_comment, make_news, eff, risk

ITEMS_2001_2005 = []

# 2001-01
ITEMS_2001_2005.append(make_news(
    key="rj2001_2001_01_drought_relief",
    month="2001-01",
    title="Severe Drought Declared in 30 Districts; Famine Relief Works Begin",
    desc="Chief Minister Ashok Gehlot declares 30 out of 32 districts as drought-affected. The state government initiates massive famine relief works, offering wage employment to rural families.",
    tags=['disaster_relief', 'rural'],
    base_w=1.25, profile="disaster_relief",
    reactions=[
        reaction("expand_famine_relief_employment", "Expand the relief work budget to employ all seeking laborers and pay wages weekly.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Delay in central aid creates a heavy cash deficit in the state treasury.", eff(0, 0, -2, -2)), 1.2),
        reaction("demand_wheat_for_work_expansion", "Demand that the state government expand the 'Wheat for Work' scheme using central food grain reserves.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Grain shipments from central storehouses face transit bottlenecks, causing local delay.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_micro_watershed_checkdams", "Propose constructing permanent check dams and micro-watersheds under relief labor instead of temporary roads.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Technical design delays keep half of the check-dam projects unfinished before monsoons.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2001-02
ITEMS_2001_2005.append(make_news(
    key="rj2001_2001_02_rti_beawar_dharna",
    month="2001-02",
    title="MKSS Holds Dharna in Beawar Demanding RTI Enforcement",
    desc="The Mazdoor Kisan Shakti Sangathan (MKSS) led by Aruna Roy holds a massive dharna in Beawar, demanding that the government enforce the newly drafted state Right to Information rules.",
    tags=['protest', 'governance'],
    base_w=1.15, profile="protest",
    reactions=[
        reaction("accept_rti_transparency_rules", "Formally accept the rules, notifying photocopies of development muster rolls at panchayat offices.",
                 ['GOVERNMENT'], eff(2, -1, 4, 4),
                 {},
                 risk(16, "Local block development officers strike in protest, citing administrative burden.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_full_legal_rti_act", "Demand the government pass a statutory Right to Information Act with penal clauses for non-compliant officers.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Bureaucratic lobbies release pamphlets claiming the act will compromise administrative privacy.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_digitized_gram_sabha_records", "Propose digital publishing of all block-level expenses at computer centers in district libraries.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Lack of internet connectivity in remote blocks keeps the database offline.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2001-03
ITEMS_2001_2005.append(make_news(
    key="rj2001_2001_03_free_fodder_scheme",
    month="2001-03",
    title="Free Fodder Distribution Scheme Launched in Barmer and Jaisalmer",
    desc="To save cattle during the extreme fodder scarcity in western Rajasthan, the state government announces a scheme to distribute free fodder in Barmer and Jaisalmer.",
    tags=['disaster_relief', 'rural'],
    base_w=1.2, profile="disaster_relief",
    reactions=[
        reaction("set_up_cattle_camps_with_subsidies", "Establish large-scale cattle camps and provide cash subsidies directly to gaushalas for fodder purchase.",
                 ['GOVERNMENT'], eff(2, 0, 3, 5),
                 {},
                 risk(18, "Audit exposes corruption in fodder supply bills, drawing critical local press.", eff(-1, -1, -2, -2)), 1.25),
        reaction("demand_fodder_transport_tax_waiver", "Demand a complete waiver of transport taxes on fodder shipments from neighboring Punjab and Haryana.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Inter-state checking points delay shipments citing permit paperwork.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_dryland_grass_reserves", "Propose developing permanent grasslands (gochar land) with drought-resistant grass seeds for the future.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Encroachments on village common lands stall the grassland development program.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 2}, weight=0.2)
    ]
))

# 2001-04
ITEMS_2001_2005.append(make_news(
    key="rj2001_2001_04_panchayati_raj_polls",
    month="2001-04",
    title="Panchayati Raj Polls Focus on Women Sarpanch Leadership",
    desc="Local body and Panchayati Raj elections focus on the participation of women sarpanchs under the 33% reservation rule, with campaigns heating up across rural wards.",
    tags=['election', 'politics'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("launch_leadership_training_for_women", "Launch state-wide leadership and administrative training workshops for newly elected women sarpanchs.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Male family members continue to act as proxy decision makers in several panchayats.", eff(0, 0, -2, -2)), 1.2),
        reaction("demand_direct_devolution_of_funds_to_sarpanch", "Demand that the state government transfer development funds directly to sarpanch bank accounts, bypassing block officers.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(14, "Block development officers protest, claiming direct transfer invites financial irregularities.", eff(-1, 0, -1, -1)), 1.25),
        reaction("propose_panchayat_finance_oversight_board", "Propose a district-level oversight board with school teachers and retired officers to audit panchayat files.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Local political leaders boycott the oversight board, calling it bureaucratic interference.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2001-05
ITEMS_2001_2005.append(make_news(
    key="rj2001_2001_05_water_trains_ajmer",
    month="2001-05",
    title="Summer Water Crisis: Special Water Trains Dispatched to Ajmer",
    desc="With local reservoirs drying up, the government coordinates with Indian Railways to run special water trains to Ajmer and Pali to meet critical municipal drinking needs.",
    tags=['disaster_relief', 'infrastructure'],
    base_w=1.25, profile="disaster_relief",
    reactions=[
        reaction("fast_track_pipeline_linking_reservoirs", "Fast-track construction of drinking water pipeline links from Bisalpur dam to city distribution centers.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Protests erupt in Tonk district over diversion of their irrigation water to Ajmer city.", eff(-1, 0, -2, -3)), 1.25),
        reaction("demand_waiving_of_municipal_water_cess", "Demand the state government waive the municipal water cess for all households in drought-declared districts.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Municipal corporations report severe revenue shortage, slowing down pipe repairs.", eff(0, 0, -2, -2)), 1.2),
        reaction("propose_mandating_rooftop_harvesting", "Propose mandating rooftop rainwater harvesting structures in all new buildings in Ajmer and Pali.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(8, "Low enforcement by municipal inspectors results in poor compliance in older wards.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2001-06
ITEMS_2001_2005.append(make_news(
    key="rj2001_2001_06_cheating_laws_exams",
    month="2001-06",
    title="Strict Anti-Cheating Penal Laws Introduced in State Exams",
    desc="To check copying mafias, the state cabinet approves strict penal laws making mass copying in Board exams a non-bailable offense with jail terms.",
    tags=['governance', 'law_order'],
    base_w=1.1, profile="governance",
    reactions=[
        reaction("enforce_rules_with_special_flying_squads", "Enforce the laws strictly, deploying special flying squads to sensitive rural exam centers.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(16, "Student groups in university campuses stage protests, alleging police high-handedness.", eff(-1, 0, -2, -1)), 1.15),
        reaction("demand_repeal_of_criminal_clauses_for_minors", "Demand repeal of the criminal clauses for minors, claiming it treats young students like hardened convicts.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Parent-teacher associations criticize the party for supporting exam malpractice.", eff(-1, 0, -2, -2)), 1.2),
        reaction("propose_digitized_question_delivery", "Propose digital delivery of question papers to centers 30 minutes before exams to prevent leaks.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Power cuts in rural centers prevent printing of papers on schedule.", eff(0, 0, -2, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2001-07
ITEMS_2001_2005.append(make_news(
    key="rj2001_2001_07_employee_protests",
    month="2001-07",
    title="Government Employees Strike Over Dearness Allowance Delay",
    desc="State government employees launch protest rallies in Jaipur, demanding the immediate release of delayed dearness allowance (DA) and rollback of salary cut proposals.",
    tags=['protest'],
    base_w=1.2, profile="protest",
    reactions=[
        reaction("warn_unions_and_enforce_no_work_no_pay", "Warn the unions, enforce 'No Work, No Pay' rules, and freeze new hiring to manage state funds.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(18, "Unions block secretariat entrances, escalating the strike to essential services.", eff(-1, 0, -2, -2)), 1.15),
        reaction("support_employees_demand_cabinet_payout", "Support the employees, demanding that the cabinet release the DA by cutting publicity budgets.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Public feels unsympathetic to employees, citing their own agricultural losses.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_tripartite_fiscal_panel", "Propose a tripartite fiscal committee representing finance officers, union heads, and MLAs to audit the state budget.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Cabinet rejects MLA inclusion, stalling the panel discussions.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2001-08
ITEMS_2001_2005.append(make_news(
    key="rj2001_2001_08_jat_reservation_demands",
    month="2001-08",
    title="Jat Organizations Demand Implementation of Central OBC Quota",
    desc="Following state-level OBC status, Jat community organizations hold rallies demanding the implementation of their quota benefits in central government recruitments.",
    tags=['politics', 'identity'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("recommend_jat_inclusion_to_centre", "Send an official state cabinet recommendation to the National Commission for Backward Classes for central inclusion.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Other OBC groups in the state express concerns over dilution of reservation share.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_sub_quotas_for_most_backward_classes", "Demand dedicated sub-quotas for the most backward classes (MBC) within OBC to protect them.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Dominant Jat voter organizations interpret the demand as anti-Jat bias.", eff(0, 0, -2, -3)), 1.25),
        reaction("propose_judicial_commission_on_representation", "Propose a high court judge-led commission to study representation levels across all communities first.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Commission hearings drag on, delaying reservation implementations.", eff(-1, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 1}, weight=0.2)
    ]
))

# 2001-09
ITEMS_2001_2005.append(make_news(
    key="rj2001_2001_09_rtu_kota_approval",
    month="2001-09",
    title="Cabinet Approves RTU Kota to Promote Technical Education",
    desc="The state cabinet clears the proposal to establish the Rajasthan Technical University (RTU) in Kota to streamline engineering and technical courses.",
    tags=['governance', 'education'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("allocate_land_and_start_infrastructure", "Allocate land in Kota and release initial budget grants to construct the university administrative block.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Student unions in other cities protest, demanding the university headquarters be split.", eff(0, 0, -1, -1)), 1.2),
        reaction("demand_priority_for_government_polytechnics", "Demand that state funds be spent on rural polytechnics first instead of creating a centralized university.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Kota citizens welcome the university, criticizing the opposition's stance.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_public_private_curriculum_sync", "Propose aligning the university curriculum with IT industry majors to ensure direct campus placements.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Private curriculum sync takes months of board approval, delaying syllabus launch.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2001-10
ITEMS_2001_2005.append(make_news(
    key="rj2001_2001_10_municipal_polls",
    month="2001-10",
    title="Municipal Corporation Polls See Close Contest",
    desc="Elections to major municipal corporations including Jaipur, Jodhpur, and Kota see high voter turnout and intense campaigns by both major parties.",
    tags=['election'],
    base_w=1.2, profile="election",
    reactions=[
        reaction("campaign_on_urban_sanitation_funds", "Campaign on the government's allocation of special sanitation and sewerage development funds for cities.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Urban voters raise issues of frequent drinking water cuts during summers.", eff(0, 0, -2, -2)), 1.15),
        reaction("highlight_municipal_taxation_hikes", "Highlight the recent increases in house taxes and water cess, calling the corporations corrupt.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Ruling party releases list of completed sewerage lines, reducing impact.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_decentralized_ward_budgets", "Propose delegating 30% of municipal budgets directly to ward committees with citizen representation.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Municipal councilors oppose devolution as threat to their financial powers.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2001-11
ITEMS_2001_2005.append(make_news(
    key="rj2001_2001_11_border_security_beefed",
    month="2001-11",
    title="Security Beefed Up Along Jaisalmer International Border",
    desc="Following rising national security tensions, BSF and state police increase patrols along the Jaisalmer and Bikaner international border sectors.",
    tags=['governance', 'security'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("coordinate_state_police_bsf_command", "Coordinate state border police with BSF and set up village security committees in border hamlets.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Border village check-posts disrupt local livestock grazing movements, drawing complaints.", eff(-1, 0, -1, -2)), 1.2),
        reaction("demand_rehabilitation_package_for_border_villages", "Demand that the state announce a special rehabilitation package for families displaced by mine-laying.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Defense ministry delays clearance for compensation surveys due to security rules.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_border_village_water_grid", "Propose an emergency water pipeline grid to secure water supply for distant border outposts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "High pipeline laying costs in sand dunes delay the grid project.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"securityIgnoredMemory": 2}, weight=0.25)
    ]
))

# 2001-12
ITEMS_2001_2005.append(make_news(
    key="rj2001_2001_12_disaster_fund_disputes",
    month="2001-12",
    title="Central Team Visits Rajasthan; Disaster Fund Row Escalates",
    desc="A central delegation visits to assess drought damage. The state government accuses the central government of releasing insufficient calamity funds.",
    tags=['disaster_relief', 'politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("publish_drought_damage_white_paper", "Publish a detailed white paper on crop losses and hold a sit-in demonstration in Delhi for fair funds.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Central ministries accuse the state of failing to submit timely utilization audits.", eff(-1, 0, -2, -2)), 1.25),
        reaction("demand_independent_audit_of_relief_spending", "Demand a central CAG audit of state calamity fund spending, alleging redirection of funds to non-drought zones.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, -1, 4, 3),
                 {},
                 risk(14, "Rural voters feel the opposition is trying to block drought aid, leading to local anger.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_national_disaster_norms_revision", "Propose a bipartisan committee of state finance ministers to rewrite national calamity relief norms.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Inter-state differences prevent a consensus draft on the new norms.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 2}, weight=0.2)
    ]
))

# 2002-01
ITEMS_2001_2005.append(make_news(
    key="rj2002_2002_01_stepwell_restoration",
    month="2002-01",
    title="Government Launches Stepwell Restoration Project in Jaipur",
    desc="The tourism and heritage department launches a project to restore historical stepwells (baoris) in Jaipur to recharge local groundwater tables.",
    tags=['governance', 'environment'],
    base_w=1.1, profile="governance",
    reactions=[
        reaction("allocate_funds_and_clear_encroachments", "Allocate heritage funds and clear commercial encroachments surrounding the stepwells.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(16, "Displaced shopkeepers protest, obtaining a court stay on demolitions in old city.", eff(0, 0, -2, -2)), 1.2),
        reaction("demand_priority_for_piped_water_connections", "Demand that the budget be spent on piped water connections in slums instead of stepwell beautifications.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Heritage preservation groups criticize the party as anti-cultural.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_community_stepwell_adoption", "Propose a model allowing local merchant associations to adopt and maintain stepwells under state supervision.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Lack of volunteer interest in less touristy wards keeps stepwells neglected.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2002-02
ITEMS_2001_2005.append(make_news(
    key="rj2002_2002_02_assembly_by_polls",
    month="2002-02",
    title="Assembly By-Elections Test Gehlot Government Support",
    desc="Assembly by-elections in three rural constituencies are scheduled. The campaigns focus heavily on the government's drought management record.",
    tags=['election'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("advertise_famine_relief_employment_figures", "Advertise the total number of relief works and free fodder camps set up by the administration.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Opposition highlights instances of delayed wage payments in the polling districts.", eff(0, 0, -2, -2)), 1.2),
        reaction("campaign_on_agrarian_distress_and_crop_failure", "Campaign aggressively on agrarian distress, highlighting dried-up wells and farmer debt defaults.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Local ruling candidates win two out of three seats due to strong local dynamics.", eff(-1, 0, -1, -1)), 1.25),
        reaction("propose_bipartisan_drought_monitoring_panel", "Propose a bipartisan assembly panel to monitor relief work allocations in polling districts live.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Frequent coordinate changes prevent the panel from publishing regular reports.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2002-03
ITEMS_2001_2005.append(make_news(
    key="rj2002_2002_03_tubewell_tariff_protests",
    month="2002-03",
    title="Farmers Protest Tubewell Electricity Tariff Hikes",
    desc="The state electricity board announces an increase in electricity tariffs for agricultural tubewells. Farmer groups block highways in Sikar and Jhunjhunu.",
    tags=['protest', 'rural'],
    base_w=1.2, profile="land_rights",
    reactions=[
        reaction("suspend_tariff_hike_provide_power_subsidies", "Suspend the tariff hike for tubewells and provide matching power subsidies from the state budget.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "State power utility reports severe losses, leading to longer power cuts in cities.", eff(-1, 0, -2, -2)), 1.25),
        reaction("lead_highway_blockades_demanding_free_power", "Join the highway blockades, demanding interest-free crop loans and free electricity for small farmers.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Commuters queue and freight delays draw complaints from trade chambers.", eff(-1, 0, -1, -2)), 1.2),
        reaction("propose_solar_pump_subsidy_program", "Propose a subsidy scheme for solar irrigation pumps to reduce dependence on grid power.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(10, "Solar pump suppliers take months to deliver units to applicants.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 3}, weight=0.2)
    ]
))

# 2002-04
ITEMS_2001_2005.append(make_news(
    key="rj2002_2002_04_churu_heatwave",
    month="2002-04",
    title="Severe Heatwave Grips Churu; Emergency Water Camps Set Up",
    desc="Temperatures in Churu and Bikaner exceed 48 degrees Celsius. The local administration sets up emergency drinking water camps and limits outdoor work hours.",
    tags=['disaster_relief'],
    base_w=1.25, profile="health_crisis",
    reactions=[
        reaction("allocate_heatwave_relief_funds", "Allocate emergency medical funds to stock dehydration medicines and run mobile water tankers.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Tankers report water source depletion, causing queue fights in outskirts.", eff(0, 0, -2, -2)), 1.2),
        reaction("demand_heatwave_be_declared_calamity", "Demand that heatwaves be declared a natural calamity under national relief guidelines to secure central grants.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Central ministry rejects the request, citing standard climate definitions.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_green_belt_shelters", "Propose planting extensive green belts and constructing solar-shaded passenger shelters along main bus routes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Slow sapling growth in sandy soil delays green belt benefits.", eff(0, 0, -1, -1)), 1.05),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.25)
    ]
))

# 2002-05
ITEMS_2001_2005.append(make_news(
    key="rj2002_2002_05_ranthambore_tiger_poaching",
    month="2002-05",
    title="Tiger Poaching Alarms Raised in Ranthambore Reserve",
    desc="Wildlife conservationists report the recovery of steel traps and poisoned carcasses inside the Ranthambore Tiger Reserve, alleging active poaching networks.",
    tags=['governance', 'environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("deploy_armed_forest_guards_raise_patrols", "Deploy armed state forest guards, set up border check-posts, and suspend local forest rangers for neglect.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(16, "Local cattle grazers protest the closure of traditional forest entry points.", eff(-1, 0, -2, -1)), 1.2),
        reaction("demand_cbi_probe_on_poaching_syndicates", "Demand a CBI investigation into poaching syndicates, alleging complicity of senior forest department officers.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, -1, 4, 3),
                 {},
                 risk(12, "Forest guards union warns that the charges defame honest field staff.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_joint_tribal_patrol_crews", "Propose hiring local tribal youth as paid forest protectors to utilize their track tracking skills.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Delayed wage releases cause high dropout rates among tribal protectors.", eff(0, 0, -2, -1)), 1.15),
        no_comment(hidden={"environmentalIssueMissed": 2}, weight=0.2)
    ]
))

# 2002-06
ITEMS_2001_2005.append(make_news(
    key="rj2002_2002_06_famine_relief_labor",
    month="2002-06",
    title="Famine Relief Work Employment Crosses 10 Lakh Mark",
    desc="With the agricultural season frozen due to drought, the total number of laborers employed under state famine relief works crosses 10 lakh in Rajasthan.",
    tags=['disaster_relief', 'rural'],
    base_w=1.25, profile="disaster_relief",
    reactions=[
        reaction("increase_relief_wage_rates", "Increase the daily relief wage rates to match state minimum wages and distribute grain packets.",
                 ['GOVERNMENT'], eff(2, 0, 3, 5),
                 {},
                 risk(18, "Delay in verifying work outputs leads to payment backlogs at block offices.", eff(-1, 0, -2, -2)), 1.25),
        reaction("demand_weekly_audits_to_check_corruption", "Demand weekly social audits of muster rolls, alleging that ghost names are being used to siphon funds.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, -1, 4, 3),
                 {},
                 risk(14, "Audit processes delay the release of current week wages, angering workers.", eff(0, 0, -2, -2)), 1.2),
        reaction("propose_post_office_direct_wage_payouts", "Propose transferring all relief wages directly through rural post office savings accounts to curb leakages.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 3),
                 {},
                 risk(10, "Post offices report staff shortages, causing long queues for payouts.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2002-07
ITEMS_2001_2005.append(make_news(
    key="rj2002_2002_07_yamuna_water_deadlock",
    month="2002-07",
    title="Haryana and Rajasthan Yamuna Water Share Talks Deadlocked",
    desc="Inter-state talks regarding Rajasthan's share of Yamuna canal water end in a deadlock. Farmers in Bharatpur threaten to block border canals.",
    tags=['land_rights'],
    base_w=1.2, profile="land_rights",
    reactions=[
        reaction("petition_supreme_court_for_water_release", "File an urgent petition in the Supreme Court requesting directions to Haryana to release the designated share.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Legal hearings are postponed, leaving the current kharif crop without water.", eff(0, 0, -2, -2)), 1.15),
        reaction("lead_farmer_border_sit_in", "Join the farmer unions in a massive sit-in at the state border, demanding Haryana open the gates.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "State border police arrests protestors to prevent inter-state clashes.", eff(-1, 0, -1, -2)), 1.25),
        reaction("propose_canal_concrete_lining", "Propose concrete lining of the feeder canals to reduce transit water seepage losses by 20%.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Construction works require canal shutdowns, disrupting minor water supplies.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 2}, weight=0.25)
    ]
))

# 2002-08
ITEMS_2001_2005.append(make_news(
    key="rj2002_2002_08_monsoon_failure_crop_ruin",
    month="2002-08",
    title="Monsoon Failure Ruins Bajra and Mustard Crops in West",
    desc="A near-complete failure of the monsoon rains in western Rajasthan ruins the standing crops of bajra and mustard, pushing farmers into deep debt.",
    tags=['disaster_relief', 'rural'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("waive_interest_on_cooperative_loans", "Waive off interest on cooperative bank loans and defer principal recoveries for one year.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Cooperative banks report severe liquidity crisis, stalling new crop loans.", eff(-1, 0, -2, -2)), 1.25),
        reaction("demand_complete_crop_loan_waiver", "Demand a complete waiver of all agricultural loans and immediate central compensation of Rs 5,000 per acre.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Nationalized banks refuse crop loan waivers, citing credit discipline guidelines.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_drip_irrigation_grants", "Propose providing 80% subsidies for drip irrigation systems to adapt to dry farming patterns.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Farmers find system cost high even with subsidies, leading to low takeup.", eff(0, 0, -2, -1)), 1.15),
        no_comment(hidden={"ruralAngerMemory": 3}, weight=0.2)
    ]
))

# 2002-09
ITEMS_2001_2005.append(make_news(
    key="rj2002_2002_09_employee_strike_escalation",
    month="2002-09",
    title="State-wide Government Employee Strike Paralyzes Offices",
    desc="State employees escalate their agitation, launching an indefinite strike. Government offices, revenue departments, and registry cells remain locked.",
    tags=['protest'],
    base_w=1.2, profile="protest",
    reactions=[
        reaction("enforce_esma_and_arrest_union_leaders", "Enforce the Essential Services Maintenance Act (ESMA) and authorize arrests of union coordinators.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(20, "Mass arrests draw critical media and lead to solidarity strikes by teacher unions.", eff(-1, 0, -3, -3)), 1.2),
        reaction("demand_reconciliation_and_release_of_da", "Demand the immediate release of union leaders, suspension of ESMA, and release of the dearness allowance.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Ruling party accuses the opposition of promoting strike anarchy.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_judicial_pay_referee", "Propose appointing a retired High Court judge as a referee to evaluate the state's financial limits and union demands.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Referee findings take months, keeping the current strike active.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2002-10
ITEMS_2001_2005.append(make_news(
    key="rj2002_2002_10_sikar_farmer_protests",
    month="2002-10",
    title="Farmer Unions Block Highways in Sikar for Cheap Power",
    desc="Thousands of farmers led by agrarian unions block major highways in Sikar, demanding cheap electricity supply and replacement of burnt transformers in 24 hours.",
    tags=['protest', 'rural'],
    base_w=1.2, profile="protest",
    reactions=[
        reaction("guarantee_six_hours_power_and_replace_transformers", "Guarantee six hours of continuous power supply daily and mandate transformer replacements in 48 hours.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Grid overload causes frequent trippings, failing to maintain the guarantee.", eff(0, 0, -2, -2)), 1.2),
        reaction("lead_dharna_outside_grid_stations", "Lead farmer dharnas outside grid substations, demanding the removal of surcharge fees on delayed bills.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Utility security locks gates, leading to brief clashes and negative press.", eff(-1, 0, -2, -1)), 1.2),
        reaction("propose_transformer_insurance_scheme", "Propose an insurance scheme where transformer maintenance costs are shared between utility and village committees.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Village committees refuse to pay their share, stalling insurance rollout.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 3}, weight=0.25)
    ]
))

# 2002-11
ITEMS_2001_2005.append(make_news(
    key="rj2002_2002_11_heritage_tourism_fest",
    month="2002-11",
    title="Rajasthan Heritage Tourism Festival Inaugurated in Udaipur",
    desc="CM Ashok Gehlot inaugurates the Rajasthan Heritage Tourism festival in Udaipur, aimed at promoting historical palaces as international travel destinations.",
    tags=['governance', 'economy'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("advertise_heritage_incentives", "Advertise special tax incentives for palace hotels to invest in eco-friendly waste management setups.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(12, "Local citizen forums protest the privatization of historical fort boundaries.", eff(0, 0, -2, -1)), 1.2),
        reaction("expose_hotel_lease_concessions_to_corporates", "Expose palace hotel lease documents, alleging that the government gave major tax concessions to private hotel groups.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 3),
                 {},
                 risk(12, "Tourism unions complain that the opposition is blocking local job growth.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_heritage_revival_tax", "Propose a small heritage conservation tax on luxury palace stays to fund restoration of local stepwells.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Palace hotel association challenges the tax in court, staying collections.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"economyIssueMissed": 1}, weight=0.3)
    ]
))

# 2002-12
ITEMS_2001_2005.append(make_news(
    key="rj2002_2002_12_tariff_rollback",
    month="2002-12",
    title="Government Rolls Back Rural Power Tariff Hikes",
    desc="To defuse ongoing farmer protests in Sikar and Mewar, the state government announces a partial rollback of the rural electricity tariff hikes.",
    tags=['politics', 'rural'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("declare_rollback_in_farmer_interest", "Declare the rollback as a gesture of goodwill to farmers and promise state budget subsidies to utility board.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Urban consumers criticize the subsidy, citing high urban electricity bills.", eff(0, 0, -1, -2)), 1.2),
        reaction("label_rollback_as_electoral_desperation", "Label the rollback as electoral desperation, demanding a permanent policy prohibiting farm tariff hikes.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "Farmers welcome the immediate tariff drop, ignoring the policy debate.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_bipartisan_tariff_regulatory_panel", "Propose a regulatory panel with farmer representatives to discuss tariff revisions before announcements.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Utility officers oppose the panel, claiming it compromises tariff autonomy.", eff(0, 0, -1, -1)), 1.15),
        no_comment(weight=0.3)
    ]
))

# 2003-01
ITEMS_2001_2005.append(make_news(
    key="rj2003_2003_01_parivartan_yatra_launch",
    month="2003-01",
    title="BJP Launches 'Parivartan Yatra' Led by Vasundhara Raje",
    desc="The BJP launches its state-wide election campaign march 'Parivartan Yatra' led by Vasundhara Raje, aiming to cover all 200 assembly constituencies.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("counter_with_development_yatras", "Counter the march by launching district-level 'Development Yatras' highlighting water pipeline completions.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "State employees hold black-flag demonstrations at several government yatra stops.", eff(-1, 0, -2, -2)), 1.15),
        reaction("intensify_yatra_focus_on_governance_failures", "Intensify the yatra rallies, highlighting delayed relief wages and government employees' anger.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Cadre fatigue arises due to continuous travel schedules, slowing down local work.", eff(-1, 0, -1, -1)), 1.3),
        reaction("propose_bipartisan_campaign_code", "Propose a code of campaign ethics to prohibit personal attacks and focus rallies on development parameters.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Rival parties ignore the code, escalating personal accusations on stage.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2003-02
ITEMS_2001_2005.append(make_news(
    key="rj2003_2003_02_mid_day_meal",
    month="2003-02",
    title="Mid-Day Meal Scheme Expanded with Soy Products",
    desc="The state government expands the mid-day meal scheme in all primary schools, incorporating local soy-based high-protein products to combat malnutrition.",
    tags=['governance', 'welfare'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("increase_school_meal_allocations", "Increase the per-student meal budget and set up school kitchen committees with mothers of students.",
                 ['GOVERNMENT'], eff(2, 0, 3, 5),
                 {},
                 risk(15, "Audit exposes substandard soy supplies in two districts, drawing critical press.", eff(-1, -1, -2, -2)), 1.25),
        reaction("demand_fresh_milk_in_meals_instead", "Demand that the state distribute fresh milk from local cooperatives instead of processed soy, supporting farmers.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Education department cites transport decay risks for fresh milk, stalling the idea.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_organic_kitchen_gardens", "Propose developing organic vegetable kitchen gardens within school backyards managed by local panchayats.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Lack of water supply in desert schools prevents garden maintenance, drying them up.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 1}, weight=0.25)
    ]
))

# 2003-03
ITEMS_2001_2005.append(make_news(
    key="rj2003_2003_03_reservoir_depletion",
    month="2003-03",
    title="Water Levels in Bisalpur Dam Drop to Record Lows",
    desc="Following prolonged drought, the water level in Bisalpur Dam drops to record lows. The government plans water rationing for Jaipur and Ajmer city supplies.",
    tags=['disaster_relief', 'infrastructure'],
    base_w=1.2, profile="disaster_relief",
    reactions=[
        reaction("enforce_municipal_water_rationing", "Enforce alternate-day municipal water rationing and deploy water tankers to tail-end urban zones.",
                 ['GOVERNMENT'], eff(1, 0, 2, 3),
                 {},
                 risk(15, "Tanker distribution delays trigger local protests and water theft incidents.", eff(-1, 0, -2, -2)), 1.15),
        reaction("demand_suspension_of_dam_water_for_industries", "Demand that the government suspend Bisalpur water allocations to industrial parks until summer ends.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(14, "Chamber of commerce warns that shutdowns will lead to job cuts.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_historical_well_recharge_drive", "Propose a massive project to clean and link historical stepwells to the city emergency supply lines.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "High contamination in stepwells requires intensive filtration, delaying supplies.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.25)
    ]
))

# 2003-04
ITEMS_2001_2005.append(make_news(
    key="rj2003_2003_04_gurjar_st_demands",
    month="2003-04",
    title="Gurjar Community Rallies Demand Scheduled Tribe Status",
    desc="Gurjar community organizations hold a massive convention in Eastern Rajasthan, demanding Scheduled Tribe (ST) status to secure education and job opportunities.",
    tags=['politics', 'identity'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("promise_commission_to_study_demands", "Promise to set up a state committee to study the community's representation and forward recommendations.",
                 ['GOVERNMENT'], eff(2, 0, 2, 3),
                 {},
                 risk(18, "Meena community organizations warn of counter-protests, opposing any ST quota split.", eff(-1, 0, -2, -3)), 1.2),
        reaction("oppose_st_inclusion_to_preserve_social_peace", "Oppose the ST demand, arguing that altering ST lists will create severe friction with existing tribal communities.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Gurjar voter organizations boycott the party's campaign in Bharatpur and Karauli.", eff(0, 0, -2, -3)), 1.25),
        reaction("propose_economic_backwardness_quota", "Propose a new reservation category for economically backward families across all communities.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Legal experts warn that the EBC quota exceeds court limits, stalling implementation.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 1}, weight=0.2)
    ]
))

# 2003-05
ITEMS_2001_2005.append(make_news(
    key="rj2003_2003_05_ebc_quota_announcement",
    month="2003-05",
    title="Government Announces 14% EBC Quota Proposal",
    desc="Seeking to address reservation demands, CM Ashok Gehlot announces a cabinet proposal to reserve 14% of government jobs for Economically Backward Classes (EBC).",
    tags=['politics'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("forward_resolution_to_parliament", "Pass a unanimous assembly resolution forwarding the EBC quota bill to Parliament to amend the constitution.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Opposition claims the bill is a pre-election stunt with no constitutional validity.", eff(0, 0, -2, -1)), 1.2),
        reaction("label_bill_as_unconstitutional_eyewash", "Label the bill as an unconstitutional eyewash designed to mislead upper-caste voters before elections.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(14, "Castes organizations accuse the party of opposing reservation benefits for the poor.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_bipartisan_legal_drafting_panel", "Propose a bipartisan legal committee to study how the bill can be structured to survive Supreme Court scans.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Legislative delays prevent the committee from submitting its draft before assembly dissolution.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2003-06
ITEMS_2001_2005.append(make_news(
    key="rj2003_2003_06_parivartan_yatra_mewar",
    month="2003-06",
    title="BJP Parivartan Yatra Draws Large Crowds in Mewar",
    desc="The BJP's Parivartan Yatra reaches the crucial Mewar region (Udaipur and Chittorgarh), drawing large crowds of rural voters and highlighting local issues.",
    tags=['politics', 'election'],
    base_w=1.2, profile="election",
    reactions=[
        reaction("announce_mewar_development_grants", "Announce fresh state development grants for Mewar historical conservation and rural roads.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(15, "Election commission issues warnings regarding announcement of grants close to polls.", eff(-1, 0, -2, -1)), 1.15),
        reaction("highlight_mewar_agricultural_losses", "Hold massive rallies in the yatra tracks, focusing on dried-up tubewells and farmer debt defaults.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Rival party workers disrupt rallies, leading to localized clashes.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_joint_tribal_welfare_charter", "Propose a joint tribal welfare charter for Mewar districts, focusing on forest produce rights.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Forest department raises legal objections to tribal produce rights, stalling it.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2003-07
ITEMS_2001_2005.append(make_news(
    key="rj2003_2003_07_ebc_quota_court_stay",
    month="2003-07",
    title="High Court Stays Implementation of 14% EBC Quota",
    desc="The Rajasthan High Court issues an interim stay on the implementation of the proposed 14% EBC reservation, citing Supreme Court rulings on the 50% quota ceiling.",
    tags=['politics', 'law_order'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("instruct_advocate_general_appeal", "Instruct the state advocate general to defend the EBC policy, citing the special backward status of dryland families.",
                 ['GOVERNMENT'], eff(1, 0, 2, 3),
                 {},
                 risk(15, "Court stay remains active, drawing protests from upper-caste associations.", eff(-1, 0, -2, -2)), 1.15),
        reaction("demand_constitutional_amendment_by_center", "Demand that the central government pass a constitutional amendment in Parliament to allow quotas beyond 50%.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "Central ministers delay action, claiming they are studying the legal impact.", eff(0, 0, -1, -1)), 1.2),
        reaction("propose_scholarship_model_alternative", "Propose shifting the budget to high-value scholarships for EBC students in lieu of direct reservations.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Students organizations protest the shift, demanding guaranteed jobs.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.25)
    ]
))

# 2003-08
ITEMS_2001_2005.append(make_news(
    key="rj2003_2003_08_employee_hostility",
    month="2003-08",
    title="State Employee Unions Campaign Against Ruling Party",
    desc="Angered by previous salary cuts and ESMA arrests, state employee unions announce they will actively campaign against the ruling Congress in the upcoming polls.",
    tags=['politics', 'protest'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("negotiate_with_union_leaders_withdraw_cuts", "Hold emergency talks with union leaders and announce the complete withdrawal of past salary cuts.",
                 ['GOVERNMENT'], eff(2, 0, 2, 3),
                 {},
                 risk(18, "Unions demand a written cabinet guarantee, showing skepticism about poll promises.", eff(-1, 0, -2, -2)), 1.2),
        reaction("welcome_employee_support_pledge_reforms", "Welcome the unions' support, pledging to restore all employee dearness allowance scales in the first cabinet meet.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 4),
                 {},
                 risk(12, "Media columns warn that restoring all scales will bankrupt the state.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_permanent_pay_board", "Propose a statutory pay board with union representation to handle wage reviews automatically every five years.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Both sides focus on seat dynamics, ignoring the pay board proposal.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2003-09
ITEMS_2001_2005.append(make_news(
    key="rj2003_2003_09_assembly_poll_dates",
    month="2003-09",
    title="Rajasthan Assembly Poll Dates Announced",
    desc="The Election Commission announces that the Rajasthan Legislative Assembly elections will be held on December 1, 2003, kicking off intense party campaigns.",
    tags=['election'],
    base_w=1.2, profile="election",
    reactions=[
        reaction("deploy_cadres_coordinate_campaign", "Deploy youth cadres to rural constituencies, focusing campaigns on famine relief work successes.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Local rebel candidates file nominations in 12 districts, splitting the vote.", eff(-1, 0, -2, -2)), 1.15),
        reaction("lead_joint_opposition_rallies", "Lead joint opposition rallies with coalition partners, targeting employee anger and farm water shortages.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Seat-sharing adjustments trigger protests by disappointed local ticket seekers.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_webcast_of_sensitive_booths", "Propose requesting the EC to webcast voting in sensitive booths to prevent muscle-power rigging.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "EC cites lack of internet lines in remote sand dune booths, stalling the idea.", eff(0, 0, -2, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2003-10
ITEMS_2001_2005.append(make_news(
    key="rj2003_2003_10_campaigns_peak",
    month="2003-10",
    title="Raje's Change Promise vs Gehlot's Relief: Campaigns Peak",
    desc="Campaigns reach peak. Raje promises industrial growth and stable electricity, while Gehlot highlights the government's management of the historic drought.",
    tags=['election'],
    base_w=1.25, profile="election",
    reactions=[
        reaction("announce_post_poll_farm_power_subsidies", "Announce election promises to reduce agricultural power rates by 30% if voted to power.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Urban voter forums criticize the promise as fiscally irresponsible.", eff(0, 0, -2, -1)), 1.2),
        reaction("highlight_incumbent_failures_on_power", "Highlight frequent rural power cuts and the crop damage in Western districts due to water shortage.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 5),
                 {},
                 risk(12, "Ruling party releases relief logs, claiming they saved the state from famine.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_bipartisan_development_debates", "Propose a series of public debates on state highway network upgrades and tourism investment plans.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Opponents decline to attend, turning the debates into empty-chair PR stunts.", eff(-1, 0, -1, -1)), 1.1),
        no_comment(weight=0.2)
    ]
))

# 2003-11
ITEMS_2001_2005.append(make_news(
    key="rj2003_2003_11_evms_introduced",
    month="2003-11",
    title="EVMs Used Across All Constituencies in Rajasthan",
    desc="Electronic Voting Machines (EVMs) are deployed across all 200 constituencies in Rajasthan for the first time, with high voter turnouts reported in rural zones.",
    tags=['election'],
    base_w=1.2, profile="election",
    reactions=[
        reaction("express_confidence_in_relief_mandate", "Express confidence that the rural poor have voted to return the government for its drought management.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Exit polls predict a significant swing in favor of the opposition coalition.", eff(-1, 0, -2, -2)), 1.15),
        reaction("thank_voters_for_turning_out_for_change", "Release statements thanking the voters for turning out in large numbers to secure an administrative change.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Allied parties express concerns about local candidate coordination in three seats.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_post_poll_all_party_dinner", "Propose an all-party dinner to maintain cordial relations after a high-voltage campaign.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Major political figures decline to attend, leaving the event low-profile.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2003-12
ITEMS_2001_2005.append(make_news(
    key="rj2003_2003_12_raje_sworn_in",
    month="2003-12",
    title="BJP Landslide; Vasundhara Raje Sworn In as CM",
    desc="The BJP wins a landslide victory, securing 120 seats. Vasundhara Raje is sworn in as the first female Chief Minister of Rajasthan at a grand ceremony in Jaipur.",
    tags=['election', 'politics'],
    base_w=1.35, profile="election",
    reactions=[
        reaction("declare_reforms_era_and_tax_cuts", "Celebrate the victory, declare an era of administrative reform, and announce immediate tax cuts for local tourism units.",
                 ['GOVERNMENT'], eff(3, 0, 4, 5),
                 {},
                 risk(18, "Opposition files immediately in court challenging the land allotments made for the ceremony.", eff(0, 0, -2, -2)), 1.25),
        reaction("accept_mandate_restructure_party", "Accept the mandate, reorganise the state party executive panels, and vow to audit the new government's spendings.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "Dissident leaders in the party hold private meetings, demanding leadership changes.", eff(-1, 0, -2, -1)), 1.2),
        reaction("propose_bipartisan_assembly_panels", "Propose an assembly committee representing all parties to monitor the rollout of rural water grids.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Fierce rivalry between leaders prevents the committee from holding its first meet.", eff(0, 0, -1, -1)), 1.15),
        no_comment(weight=0.15)
    ]
))

# 2004-01
ITEMS_2001_2005.append(make_news(
    key="rj2004_2004_01_barmer_oil_discovery",
    month="2004-01",
    title="Cairn Energy Announces Major Oil Discovery in Barmer",
    desc="Cairn Energy discovers a major onshore oil field (Mangala field) in Barmer district. Initial estimates indicate substantial commercial reserves.",
    tags=['economy', 'governance'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("announce_industrial_corridor_plans", "Inaugurate the development zone and announce plans for an industrial refinery corridor in Western Rajasthan.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Local landowners file court cases demanding higher values for pipeline lands.", eff(0, 0, -1, -2)), 1.25),
        reaction("demand_royalty_guarantees_for_state", "Demand that the state government secure 50% royalty shares from the Centre before clearing project lands.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Industrial chambers criticize the opposition for trying to stall investments.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_local_employment_training_hubs", "Propose setting up petroleum engineering and safety training centers in Barmer to employ local youth.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Lack of technical instructors delays the launch of the training center.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"economyIssueMissed": 1}, weight=0.2)
    ]
))

# 2004-02
ITEMS_2001_2005.append(make_news(
    key="rj2004_2004_02_single_window_clearance",
    month="2004-02",
    title="Raje Government Announces Single-Window Clearance System",
    desc="To attract industrial investment, the Raje government introduces a single-window clearance system for environmental and land clearances in the state.",
    tags=['governance', 'economy'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("implement_system_with_online_tracking", "Implement the single-window system online, setting a strict 30-day limit for industrial clearances.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(15, "Environmental groups protest, claiming the fast-track system bypasses forest checks.", eff(0, 0, -2, -2)), 1.2),
        reaction("expose_land_allotment_concessions_to_corporates", "Expose land files, alleging that prime plots were allotted to private groups at throwaway rates.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, -1, 4, 3),
                 {},
                 risk(12, "Business forums release data showing the rates are compliant, neutralizing the issue.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_independent_environmental_oversight", "Propose an oversight committee of retired judges and green activists to monitor clearances.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Bureaucratic delays keep the committee inactive, leaving clearances to officers.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2004-03
ITEMS_2001_2005.append(make_news(
    key="rj2004_2004_03_general_election_campaigns",
    month="2004-03",
    title="Lok Sabha Campaigns Peak; BJP Seeks to Build on Landslide",
    desc="General election campaigns peak. The BJP campaigns on the 'India Shining' theme and Raje's reforms, while Congress highlights rural water issues.",
    tags=['election'],
    base_w=1.2, profile="election",
    reactions=[
        reaction("announce_rural_tourism_investment_plan", "Announce plans to build a heritage tourism circuit in Shekhawati to generate rural jobs.",
                 ['GOVERNMENT'], eff(1, 0, 2, 3),
                 {},
                 risk(15, "Local hotel lobbies protest new tax compliance rules in the circuit.", eff(0, 0, -2, -1)), 1.15),
        reaction("highlight_rural_water_shortages", "Highlight dried-up wells and the lack of pipeline connections in Jodhpur and Pali districts.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Ruling party points out that the pipelines are under active construction, reducing impact.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_all_party_manifesto_audits", "Propose that both parties submit their election manifestos to a state audit panel to check fiscal limits.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Voters show little interest in auditing manifestos, limiting campaign benefits.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2004-04
ITEMS_2001_2005.append(make_news(
    key="rj2004_2004_04_lok_sabha_polling",
    month="2004-04",
    title="Lok Sabha Polling Recorded Peacefully in Desert Districts",
    desc="Rajasthan records over 50% voter turnout in the Lok Sabha elections. Polling passes off peacefully with minor clashes in Alwar.",
    tags=['election'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("express_confidence_in_governance_mandate", "Express confidence that voters have supported the government's industrial reforms and single-window system.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Exit polls predict a close contest in at least five constituencies.", eff(0, 0, -2, -1)), 1.15),
        reaction("thank_voters_for_raising_agrarian_issues", "Release statements thanking the voters for turning out to raise the voice of dryland farmers.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Alliance partners complain about insufficient joint campaign meets.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_post_poll_cordial_meet", "Propose a post-poll reconciliation meeting of all regional leaders to discuss water-sharing strategies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Major figures decline to attend, keeping the meeting low-profile.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2004-05
ITEMS_2001_2005.append(make_news(
    key="rj2004_2004_05_lok_sabha_results",
    month="2004-05",
    title="BJP Wins 21 Lok Sabha Seats; Raje Consolidates Power",
    desc="The BJP wins 21 out of 25 Lok Sabha seats in Rajasthan, cementing Vasundhara Raje's leadership in the state despite the NDA's national defeat.",
    tags=['election', 'politics'],
    base_w=1.3, profile="election",
    reactions=[
        reaction("declare_mandate_for_industrial_reforms", "Declare the mandate as public approval of the state's industrial reforms and fast-track the SEZ files.",
                 ['GOVERNMENT'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Farmers unions in Ganganagar warn of protests if water sharing is not prioritized.", eff(-1, 0, -1, -2)), 1.2),
        reaction("restructure_opposition_district_panels", "Reorganize the district party panels, focusing on building farmer base in canal districts.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "Internal friction arises between senior leaders over responsibility for the defeat.", eff(-1, 0, -2, -1)), 1.2),
        reaction("propose_bipartisan_water_grid_bill", "Propose an all-party assembly bill to establish a state-wide drinking water pipeline grid.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Utility cabinet disputes delay the drafting of the water grid bill.", eff(0, 0, -1, -1)), 1.15),
        no_comment(weight=0.2)
    ]
))

# 2004-06
ITEMS_2001_2005.append(make_news(
    key="rj2004_2004_06_it_policy_digital_land",
    month="2004-06",
    title="State Announces Comprehensive IT Policy to Digitise Land Records",
    desc="The government announces a new IT policy, initiating a project to digitize all rural land records to prevent ownership scams and ease loan approvals.",
    tags=['governance', 'economy'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("launch_digitization_drives_in_tahsils", "Launch digitization drives in all tahsils, setting up computer kiosks with print facilities.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Local patwaris strike, claiming the digital records bypass their authority.", eff(-1, -1, -2, -2)), 1.25),
        reaction("demand_training_for_illiterate_farmers", "Demand that the government provide free training and assistance for illiterate farmers to access records.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Bureaucrats state that kiosk helpers are already trained, neutralizing the demand.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_local_panchayat_land_registers", "Propose maintaining matching physical registers in local panchayats to check database errors.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Panchayats report lack of lockup space, leaving registers vulnerable.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"economyIssueMissed": 1}, weight=0.25)
    ]
))

# 2004-07
ITEMS_2001_2005.append(make_news(
    key="rj2004_2004_07_sariska_tiger_disappearance",
    month="2004-07",
    title="Tiger Disappearance Alarms Raised in Sariska Reserve",
    desc="Wildlife groups report that no tigers have been spotted in Sariska Tiger Reserve for several months, raising alarms of intensive illegal poaching.",
    tags=['governance', 'environment'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("order_immediate_tiger_census_audit", "Order an immediate scientific census audit and suspend the chief wildlife warden for failing to report sightings.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(18, "CBI files reports suggesting complete tiger extinction, drawing heavy national press.", eff(-1, 0, -2, -3)), 1.2),
        reaction("demand_cbi_probe_and_minister_resignation", "Demand a CBI investigation and the resignation of the forest minister, alleging state collusion with poachers.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(14, "Forest unions protest, claiming that field guards lack defensive weapons.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_local_village_relocation_package", "Propose a special financial package to relocate villages inside the reserve buffer zones to reduce conflict.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Villagers refuse relocation, demanding land titles in adjacent blocks.", eff(0, 0, -2, -1)), 1.15),
        no_comment(hidden={"environmentalIssueMissed": 2}, weight=0.2)
    ]
))

# 2004-08
ITEMS_2001_2005.append(make_news(
    key="rj2004_2004_08_heritage_tourism_sync",
    month="2004-08",
    title="Government Proposes Heritage Tourism Hubs",
    desc="The tourism department submits proposals to link historical forts of Jaipur, Jodhpur, and Udaipur under a single-window heritage tourism ticket system.",
    tags=['governance', 'economy'],
    base_w=1.1, profile="governance",
    reactions=[
        reaction("launch_joint_heritage_tickets_and_travel", "Launch the joint ticket system and coordinate with private airlines for daily heritage shuttle flights.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(12, "Local taxi unions protest the direct shuttle lines, blockading airport entries.", eff(0, 0, -2, -1)), 1.15),
        reaction("demand_heritage_fee_allocation_to_local_civic", "Demand that 40% of the heritage ticket fees be spent on local municipal water works in historical zones.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Tourism departments claim the fees are locked for conservation, ignoring the demand.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_cultural_guide_licensing_model", "Propose a standard licensing model for local youth to act as certified heritage guides, generating jobs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Guide associations strike, protesting against the registration test difficulty.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"economyIssueMissed": 1}, weight=0.3)
    ]
))

# 2004-09
ITEMS_2001_2005.append(make_news(
    key="rj2004_2004_09_gharsana_water_protests",
    month="2004-09",
    title="Farmers in Gharsana Protest Reduced Canal Water Allowances",
    desc="Agrarian distress flares up as farmers in Gharsana and Rawla block canal offices, protesting the government's decision to implement the water allowance reduction.",
    tags=['land_rights', 'protest', 'rural'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("refuse_allowance_change_request_patience", "Refuse to rollback the water reduction, citing regional canal capacity limits, and urge patience.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(20, "Farmer organizations mobilize thousands, blockading all regional offices.", eff(-1, 0, -2, -3)), 1.2),
        reaction("lead_farmers_sit_in_demanding_old_allowance", "Join the farmers' sit-in, demanding that the Raje cabinet suspend the water reduction immediately.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Local administrative offices report total deadlock, halting all development files.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_bipartisan_water_audit_committee", "Propose an all-party committee of MLAs to audit water levels in the Indira Gandhi canal basin.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Fierce political posturing prevents the committee from agreeing on audit dates.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 3}, weight=0.15)
    ]
))

# 2004-10
ITEMS_2001_2005.append(make_news(
    key="rj2004_2004_10_gharsana_police_firing",
    month="2004-10",
    title="Tragic Police Firing on Protesting Farmers in Gharsana",
    desc="Tensions turn violent as police open fire on protesting farmers in Gharsana and Rawla, resulting in several deaths and hundreds of injuries.",
    tags=['security_crisis', 'protest', 'rural'],
    base_w=1.4, profile="security_crisis",
    reactions=[
        reaction("impose_curfew_order_judicial_probe", "Impose curfews, call in the army for flag marches, and order a judicial inquiry into the firing.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(22, "Farmer unions across the state launch solidarity blockades, drawing heavy national criticism.", eff(-2, 0, -3, -4)), 1.25),
        reaction("condemn_firing_demand_cm_resignation", "Condemn the police action as draconian, demand the CM's resignation, and hold protest rallies in Jaipur.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 5),
                 {},
                 risk(15, "Police prevents rallies entering the capital citing assembly bans.", eff(-1, 0, -2, -1)), 1.3),
        reaction("propose_immediate_compensation_and_talks", "Propose Rs 5 lakh compensation for victims' families and invite farmer leaders to Jaipur for immediate talks.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(12, "Farmer leaders refuse to travel to Jaipur until all detained protestors are released.", eff(0, 0, -2, -1)), 1.15),
        no_comment(hidden={"securityIgnoredMemory": 4}, weight=0.1)
    ]
))

# 2004-11
ITEMS_2001_2005.append(make_news(
    key="rj2004_2004_11_ganganagar_curfew",
    month="2004-11",
    title="Curfew and Army Flag Marches in Sri Ganganagar",
    desc="Strict curfews remain active in Gharsana and Rawla. The army holds flag marches to restore order, while opposition MLAs boycott assembly sessions.",
    tags=['protest', 'law_order'],
    base_w=1.3, profile="protest",
    reactions=[
        reaction("enforce_curfew_and_negotiate_secretly", "Enforce the curfew strictly while initiating back-channel talks with moderate farmer unions.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Radical union wings leak talk details, accusing moderates of selling out.", eff(-1, 0, -2, -2)), 1.2),
        reaction("defy_prohibitory_orders_court_arrest", "Defy prohibitory orders to enter Gharsana, lead dharnas, and court arrest in solidarity with farmers.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Detention of senior leaders triggers brief stone-pelting incidents by cadres.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_neutral_administrative_mediator", "Propose requesting a retired senior IAS officer to act as a mediator to resolve the water schedule disputes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Both sides reject initial mediator choices, delaying the talks.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2004-12
ITEMS_2001_2005.append(make_news(
    key="rj2004_2004_12_gharsana_peace_agreement",
    month="2004-12",
    title="Government Signs Peace Agreement with Farmer Unions",
    desc="The Raje government signs a formal peace agreement with the Kisan Sangharsh Samiti (KSS), agreeing to restore water allocations, ending the three-month strike.",
    tags=['politics', 'rural'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("hail_agreement_as_victory_for_peace", "Hail the agreement as a victory for cooperative development and announce immediate release of detained farmers.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Rival political groups claim the government yielded to pressure after causing deaths.", eff(-1, 0, -2, -2)), 1.2),
        reaction("label_agreement_as_belated_clumsy_concession", "Label the agreement as a belated concession that could have saved lives if done in September.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Farmers celebrate the restoration of water, reducing political utility of the issue.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_statutory_water_regulatory_commission", "Propose establishing a statutory state water commission to prevent arbitrary allocation changes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Drafting the water commission bill is delayed by department jurisdiction rows.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.2)
    ]
))

# 2005-01
ITEMS_2001_2005.append(make_news(
    key="rj2005_2005_01_sariska_poaching_inquiry",
    month="2005-01",
    title="CBI Begins Inquiry into Sariska Tiger Disappearance",
    desc="The central government directs the CBI to initiate a comprehensive inquiry into the vanishing tigers of Sariska Tiger Reserve and check poaching links.",
    tags=['governance', 'environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("cooperate_with_cbi_and_share_patrol_logs", "Direct the state forest cell to share all patrol logs and coordinate raids on suspected skin trader dens.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(15, "Raids expose involvement of local forest guards, drawing critical headlines.", eff(-1, -1, -2, -1)), 1.2),
        reaction("demand_judicial_audit_of_all_tiger_reserves", "Demand a judicial audit of all tiger reserves in the state, accusing the department of inflating tiger census numbers.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Forest unions protest, claiming the audit target acts as harassment.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_community_wildlife_watch_guards", "Propose setting up village wildlife watch committees around Sariska with funds from international NGOs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "NGO fund clearances face central security delays, stalling the watch guards.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2005-02
ITEMS_2001_2005.append(make_news(
    key="rj2005_2005_02_vat_introduction_protests",
    month="2005-02",
    title="State Introduces VAT; Merchant Unions Call Bandh",
    desc="The state assembly passes the Value Added Tax (VAT) bill. Retail and wholesale merchant unions call for a state-wide business bandh in protest.",
    tags=['governance', 'economy'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("enforce_vat_raise_small_trader_limits", "Enforce VAT on schedule but raise tax-exemption limits for small-scale local retailers.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(15, "State tax revenue drops below projections in the first quarter, limiting welfare funds.", eff(0, 0, -2, -2)), 1.2),
        reaction("lead_merchant_dharnas_against_double_taxation", "Lead merchant dharnas, demanding the suspension of VAT until a simplified single-point tax is designed.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Economic columns criticize the opposition for stalling crucial fiscal reforms.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_vat_facilitation_kiosks", "Propose setting up computerized VAT facilitation centers in all market zones to assist shopkeepers.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Software errors in billing terminals delay transactions, causing initial chaos.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"economyIssueMissed": 1}, weight=0.25)
    ]
))

# 2005-03
ITEMS_2001_2005.append(make_news(
    key="rj2005_2005_03_cbi_confirms_extinction",
    month="2005-03",
    title="CBI Report Confirms Complete Tiger Extinction in Sariska",
    desc="The CBI submits its final report to the Prime Minister, confirming that poaching has completely wiped out the tiger population in Sariska Tiger Reserve.",
    tags=['governance', 'environment'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("accept_report_announce_translocation_project", "Accept the report findings, create a special anti-poaching force, and propose a tiger translocation project.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Poaching syndicates remain active in adjacent districts, threatening translocation plans.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_censure_of_forest_ministry_in_assembly", "Demand a formal censure of the forest ministry in the assembly, calling the extinction a national shame.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Ruling party points to the new translocation plan, reducing censure impact.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_forest_boundary_fencing_audit", "Propose a complete satellite monitoring and electronic fence audit of the reserve borders.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "High costs of electronic fencing keep the project on paper.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 2}, weight=0.2)
    ]
))

# 2005-04
ITEMS_2001_2005.append(make_news(
    key="rj2005_2005_04_fort_encroachments_court",
    month="2005-04",
    title="HC Orders Removal of Encroachments Around Jaipur Forts",
    desc="Madras High Court, wait, High Court, the Rajasthan High Court orders the immediate removal of all illegal commercial constructions and slums near Amber and Nahargarh forts.",
    tags=['governance'],
    base_w=1.1, profile="governance",
    reactions=[
        reaction("enforce_demolitions_and_relocate_slums", "Enforce the demolitions strictly to preserve heritage, providing transit housing for displaced families.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(16, "Displaced slum dwellers stage sit-ins on main roads, causing traffic disruptions.", eff(0, 0, -2, -2)), 1.2),
        reaction("demand_regularization_of_old_habitations", "Demand that the state regularize old habitations, accusing the government of favoring tourism over poor families.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Heritage conservation trusts criticize the party for supporting illegal actions.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_heritage_fringe_rehabilitation_zones", "Propose developing dedicated handicraft market zones for displaced families outside the fort boundaries.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Allotment delays keep the handicraft markets unfinished for months.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2005-05
ITEMS_2001_2005.append(make_news(
    key="rj2005_2005_05_anti_poaching_patrols",
    month="2005-05",
    title="State Announces Strict Anti-Poaching Patrol Laws",
    desc="Following the Sariska crisis, the state assembly passes a bill setting up an armed Tiger Protection Force with power to shoot poachers in self-defense.",
    tags=['governance', 'environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("deploy_protection_battalions_in_reserves", "Deploy the protection battalions in Ranthambore and Sariska immediately, equipped with wireless networks.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Local shepherd groups protest the high restrictions on grazing entries.", eff(0, 0, -2, -1)), 1.2),
        reaction("demand_oversight_on_force_weapons_use", "Demand that the force weapons use be monitored by judicial officers, alleging risk of harassment of tribals.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Wildlife lobbies criticize the party for seeming to weaken anti-poaching security.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_eco_tourism_revenue_sharing", "Propose sharing 10% of tiger reserve entry fees directly with surrounding village committees for development.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Finance department delays revenue sharing rules, stalling payouts.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2005-06
ITEMS_2001_2005.append(make_news(
    key="rj2005_2005_06_bainsla_takes_charge",
    month="2005-06",
    title="Colonel Kirori Singh Bainsla Takes Charge of Gurjar Agitation",
    desc="Retired Colonel Kirori Singh Bainsla assumes leadership of the Gurjar Arakshan Sangharsh Samiti, announcing a state-wide mobilization drive for ST status.",
    tags=['politics', 'identity'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("initiate_formal_secretariat_talks", "Initiate formal talks at the secretariat and promise to compile community census data for the backward commission.",
                 ['GOVERNMENT'], eff(2, 0, 2, 3),
                 {},
                 risk(15, "Meena community organizations warn of counter-protests, opposing any ST quota split.", eff(-1, 0, -2, -3)), 1.15),
        reaction("demand_unconditional_support_for_backward_castes", "Demand that the government support the Gurjar demands in the state assembly by passing a fresh resolution.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Tribal groups view the demand as threat to their seats, shifting support away.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_statutory_backward_welfare_board", "Propose establishing a welfare board with substantial development budgets for nomadic and backward castes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Nomadic representatives reject the board as a diversion from reservation demands.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 1}, weight=0.2)
    ]
))

# 2005-07
ITEMS_2001_2005.append(make_news(
    key="rj2005_2005_07_jodhpur_water_scarcity",
    month="2005-07",
    title="Monsoon Delay Triggers Water Scarcity in Jodhpur and Ajmer",
    desc="A delay in monsoon rains causes severe drinking water depletion in Jodhpur. Municipal authorities coordinate emergency water tanker schedules.",
    tags=['disaster_relief'],
    base_w=1.2, profile="disaster_relief",
    reactions=[
        reaction("release_emergency_tanker_funds", "Release emergency municipal funds to hire private water tankers and repair local borewells.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Tanker supply logs show anomalies, leading to media allegations of leakages.", eff(-1, -1, -2, -1)), 1.25),
        reaction("demand_completion_of_indira_gandhi_canal_pipelines", "Demand that the government speed up the pipe links from the Indira Gandhi canal to Jodhpur.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(10, "Feeder canal maintenance works delay water release for several weeks.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_civic_water_audit_cells", "Propose setting up ward-level water monitoring cells with citizen volunteers to track leaks.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Low volunteer participation in summer months slows cell formation.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 2}, weight=0.2)
    ]
))

# 2005-08
ITEMS_2001_2005.append(make_news(
    key="rj2005_2005_08_bharatpur_dalit_protests",
    month="2005-08",
    title="Dalit Organizations Protest Over Land Allotments in Bharatpur",
    desc="Protests erupt in Bharatpur district as Dalit organizations demand that the government distribute ceiling-surplus land to landless families as promised.",
    tags=['politics', 'identity', 'protest'],
    base_w=1.15, profile="protest",
    reactions=[
        reaction("launch_district_land_allotment_surveys", "Order district collectors to identify surplus lands and issue possession titles to beneficiary lists in 90 days.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Dominant landholding groups block access to surveyed lands, causing local disputes.", eff(-1, 0, -2, -2)), 1.2),
        reaction("lead_dharnas_outside_collector_offices", "Lead farmer and landless laborers dharnas outside collector offices, demanding immediate physical possession.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Police detains leaders, causing brief stone-pelting incidents.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_cooperative_farming_leases", "Propose leasing state lands to cooperative societies of landless families with soft credit backing.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Lack of bank guarantees delays release of credit to societies.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 1}, weight=0.25)
    ]
))

# 2005-09
ITEMS_2001_2005.append(make_news(
    key="rj2005_2005_09_cairn_pipeline_sub",
    month="2005-09",
    title="Cairn Energy Submits Barmer Pipeline Development Plans",
    desc="Cairn Energy submits its development report for a heated pipeline to transport thick Barmer crude oil to Gujarat ports, seeking state clearances.",
    tags=['economy', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("approve_pipeline_clearances", "Approve the pipeline clearances and coordinate with district land cells for fast-track easement rights.",
                 ['GOVERNMENT'], eff(1, 0, 3, 4),
                 {},
                 risk(14, "Environment cells warn of pipeline transit risks near desert wildlife reserves.", eff(0, 0, -1, -1)), 1.2),
        reaction("demand_domestic_refinery_construction_first", "Demand that the state focus on constructing a refinery in Barmer first instead of piping crude to Gujarat.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Oil companies state that refinery setup requires high capital and years to build.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_pipeline_safety_audit_commission", "Propose an independent pipeline safety commission representing state geologists and wildlife bodies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Safety audit processes delay the start of pipeline laying by several months.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"economyIssueMissed": 1}, weight=0.25)
    ]
))

# 2005-10
ITEMS_2001_2005.append(make_news(
    key="rj2005_2005_10_land_portal_launch",
    month="2005-10",
    title="Government Launches Digital Portal for Land Records",
    desc="The Chief Minister launches the digital land record portal 'Apna Khata', allowing farmers to obtain print copies of land registry records.",
    tags=['governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("expand_apna_khata_kiosks", "Expand apna khata kiosks in all major cooperative bank branches to ease rural loan clearances.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Technical server crashes during registry updates draw complaints from farmers.", eff(0, 0, -2, -1)), 1.2),
        reaction("demand_removal_of_kiosk_print_fees", "Demand that the print copies be provided free of cost, calling the current kiosk fee a burden.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Administrative boards claim fees are necessary to maintain servers, ignoring the demand.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_local_panchayat_sync", "Propose sync of digital portals with local panchayat records weekly to check entry errors.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Lack of trained operators in panchayats delays database sync.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2005-11
ITEMS_2001_2005.append(make_news(
    key="rj2005_2005_11_heritage_ad_campaigns",
    month="2005-11",
    title="Rajasthan Tourism Launches International Heritage Campaign",
    desc="The state tourism board launches a large-scale international ad campaign 'Padharo Mhare Desh' to promote winter palace travel, seeking global bookings.",
    tags=['economy'],
    base_w=1.1, profile="governance",
    reactions=[
        reaction("organise_tourism_conventions_in_europe", "Organize tourism roadshows in Europe and offer single-window hotel license renewals.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(12, "Local heritage guides strike, protesting against foreign agency permit rules.", eff(0, 0, -2, -1)), 1.15),
        reaction("expose_monopoly_palace_leases", "Expose list of heritage hotels leased to political family trusts, alleging monopoly on tourism profits.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 3),
                 {},
                 risk(12, "Hotel unions claim the leases are legally compliant, reducing impact.", eff(0, 0, -1, -1)), 1.2),
        reaction("propose_rural_homestay_subsidies", "Propose subsidies for rural homestays in heritage villages to spread tourism revenues to families.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Lack of transport links to remote villages limits homestay bookings.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"economyIssueMissed": 1}, weight=0.3)
    ]
))

# 2005-12
ITEMS_2001_2005.append(make_news(
    key="rj2005_2005_12_jhalawar_communal_tensions",
    month="2005-12",
    title="Minor Tensions in Jhalawar District Brought Under Control",
    desc="Minor communal clashes are reported in Jhalawar district following disputes over a religious procession. Local administration deploys police to restore peace.",
    tags=['security_crisis', 'identity'],
    base_w=1.2, profile="security_crisis",
    reactions=[
        reaction("deploy_extra_police_make_preventive_arrests", "Deploy additional police battalions, enforce prohibitory orders, and make preventive arrests of instigators.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Local business unions protest over trade losses due to early shop closures.", eff(-1, 0, -1, -1)), 1.2),
        reaction("lead_harmony_peace_marches_in_sensitive_wards", "Lead peace harmony marches in the affected wards and demand a judicial review of process permits.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Radical outfits accuse the party of soft-pedaling on process violations.", eff(-1, 0, -2, -1)), 1.2),
        reaction("propose_district_communal_harmony_board", "Propose setting up a permanent committee of local community elders to resolve process disputes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Rival religious heads refuse to attend board meetings, leaving it inactive.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"securityIgnoredMemory": 2}, weight=0.25)
    ]
))

