from helper import reaction, no_comment, make_news, eff, risk

ITEMS_2001_2005 = []

# 2001-01
ITEMS_2001_2005.append(make_news(
    key="bh2001_2001_01_panchayat_polls",
    month="2001-01",
    title="Government Announces Panchayat Polls After 23-Year Hiatus",
    desc="The Bihar state government announces the schedule for Panchayat elections, marking the first local body polls in the state since 1978. Intense political rivalries ignite in rural districts.",
    tags=['election', 'politics'],
    base_w=1.25, profile="election",
    reactions=[
        reaction("fast_track_local_polls", "Deploy state police to fast-track municipal arrangements and secure polling booths.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Opposition claims bias in block-level seat reservations, creating local disputes.", eff(0, 0, -2, -1)), 1.2),
        reaction("demand_paramilitary_deployment", "Demand deployment of central paramilitary forces to prevent booth capturing by dominant groups.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Delays in central force arrival lead to localized clashes in remote panchayats.", eff(0, 0, -1, -2)), 1.25),
        reaction("propose_bipartisan_polling_watch", "Propose forming all-party ward committees to monitor electoral peace at polling centers.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Rival party workers refuse to sit together on panels, causing localized stalemates.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"politicalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-02
ITEMS_2001_2005.append(make_news(
    key="bh2001_2001_02_post_jharkhand_deficit",
    month="2001-02",
    title="Separation of Jharkhand Triggers State Treasury Crisis",
    desc="Following the creation of mineral-rich Jharkhand, the Bihar assembly debates the massive loss of mining revenue and the challenge of paying government salaries.",
    tags=['governance', 'economy'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("request_central_assistance_package", "Send an official cabinet team to Delhi to request a special financial recovery package for Bihar.",
                 ['GOVERNMENT'], eff(2, -1, 3, 4),
                 {},
                 risk(16, "Central ministries delay approvals, demanding detailed fiscal reform plans first.", eff(-1, 0, -2, -2)), 1.25),
        reaction("expose_mismanagement_of_mines", "Expose previous state mining lease documents, alleging massive corruption under prior regimes.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Ruling coalition labels the charges as politically motivated slander.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_agriculture_taxation_review", "Propose reviewing commercial agriculture and dairy duties to boost internal state revenue.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Farmer unions protest the proposed duties, forcing a rollback of the draft.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"economyIssueMissed": 1}, weight=0.25)
    ]
))

# 2001-03
ITEMS_2001_2005.append(make_news(
    key="bh2001_2001_03_panchayat_violence",
    month="2001-03",
    title="Clashes Erupt in Rural Districts Over Panchayat Campaigning",
    desc="Pre-election clashes are reported in Central Bihar districts. Rival caste factions mobilize supporters, leading to local security concerns.",
    tags=['protest', 'security_crisis'],
    base_w=1.2, profile="security_crisis",
    reactions=[
        reaction("impose_crpc_prohibitions", "Impose Section 144 CrPC prohibitions and arrest history-sheeters to enforce electoral peace.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Local leaders allege targetting of their candidates by district police.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_judicial_inquiry_on_clashes", "Demand a judicial inquiry into police inaction, alleging state favoritism of ruling candidates.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "Ruling party releases videos of opposition cadres instigating the violence.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_peace_marches", "Propose organizing joint cross-party peace marches through sensitive blocks to defuse caste tensions.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Extreme factions boycott the marches, reducing their impact on the ground.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"securityIgnoredMemory": 2}, weight=0.25)
    ]
))

# 2001-04
ITEMS_2001_2005.append(make_news(
    key="bh2001_2001_04_panchayat_turnout",
    month="2001-04",
    title="Panchayat Elections See Historic Turnout Among Marginalized",
    desc="Panchayat polling concludes with an unprecedented voter turnout. Margnalized communities vote in large numbers, changing rural power dynamics.",
    tags=['election', 'politics'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("celebrate_grassroots_mandate", "Hail the turnout as a victory for social justice and decentralized democracy in Bihar.",
                 ['GOVERNMENT'], eff(2, 0, 3, 5),
                 {},
                 risk(12, "Newly elected sarpanchs complain of lack of office spaces and funds.", eff(0, 0, -2, -1)), 1.2),
        reaction("demand_administrative_training", "Demand that the state immediately conduct administrative training for the newly elected local leaders.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(14, "Training schedules face administrative delays, keeping work stalled.", eff(-1, 0, -1, -1)), 1.25),
        reaction("propose_decentralized_development_charter", "Propose a direct funding model where 40% of state schemes are managed by village sabhas.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 3),
                 {},
                 risk(10, "Bureaucratic lobbies block direct funding, citing lack of auditing capacity.", eff(0, 0, -2, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2001-05
ITEMS_2001_2005.append(make_news(
    key="bh2001_2001_05_flood_preparedness",
    month="2001-05",
    title="Early Monsoon Rains Spark North Bihar Flood Concerns",
    desc="Heavy pre-monsoon showers raise water levels in the Gandak and Kosi rivers. North Bihar districts report waterlogging in low-lying crop zones.",
    tags=['disaster_relief', 'rural'],
    base_w=1.2, profile="disaster_relief",
    reactions=[
        reaction("allocate_pre_flood_embankment_funds", "Allocate emergency state funds to reinforce river embankments and prepare rescue boats.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Contractors siphon embankment repair funds, drawing critical local press.", eff(-1, -1, -2, -2)), 1.25),
        reaction("demand_cag_audit_of_flood_repairs", "Demand a CAG audit of embankment works, alleging prior funds were spent on paper only.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "District administrations refuse to share files, citing emergency protocols.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_community_flood_shelters", "Propose constructing permanent elevated concrete shelters in high-risk zones using relief labor.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Land acquisition issues in flood plains stall shelter construction projects.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2001-06
ITEMS_2001_2005.append(make_news(
    key="bh2001_2001_06_kidnap_accusations",
    month="2001-06",
    title="Opposition Launches Rallies Alleging Rising Ransom Gangs",
    desc="BJP and JD(U) hold joint protest rallies in Patna, accusing the RJD government of failing to check organized kidnapping-for-ransom networks.",
    tags=['protest', 'law_order'],
    base_w=1.2, profile="protest",
    reactions=[
        reaction("launch_anti_kidnapping_taskforce", "Form a special police anti-kidnapping task force with fast-track trial powers.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(16, "Human rights groups allege procedural excesses during suspect raids.", eff(-1, 0, -2, -1)), 1.15),
        reaction("expose_political_patronage_of_gangs", "Expose phone logs and photographs alleging ties between local ruling MLAs and gang leaders.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, -1, 4, 4),
                 {},
                 risk(12, "Ruling party files defamation suits, leading to prolonged legal battles.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_witness_protection_program", "Propose a state-backed witness protection program to encourage testimony against gangs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Lack of dedicated budget leaves witness houses understaffed and unsafe.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"corruptionIgnoredMemory": 2}, weight=0.25)
    ]
))

# 2001-07
ITEMS_2001_2005.append(make_news(
    key="bh2001_2001_07_rural_power_outages",
    month="2001-07",
    title="Rural Electrification Demands Grow Amid Summer Outages",
    desc="North Bihar rural areas report daily power outages of over 20 hours. Farmers demand cheap electricity for diesel pump alternatives.",
    tags=['infrastructure', 'rural'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("procure_extra_grid_power", "Procure extra power from the national grid and set up dedicated feeder lines for rural farming zones.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "State electricity board reports heavy fiscal deficits, delaying line works.", eff(-1, 0, -2, -2)), 1.2),
        reaction("lead_substation_sit_ins", "Lead farmer sit-ins outside electricity board offices, demanding immediate tariff reductions.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Clashes with security staff lead to arrests of block leaders.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_biomass_solar_microgrids", "Propose establishing decentralized rice-husk biomass power plants in remote village clusters.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Private microgrid developers pull out, citing low tariff recovery returns.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2001-08
ITEMS_2001_2005.append(make_news(
    key="bh2001_2001_08_rjd_social_justice",
    month="2001-08",
    title="Rabri Devi Defends RJD Social Justice Record Against Centre",
    desc="CM Rabri Devi attacks the central government, accusing it of using central investigating agencies to destabilize the social justice government in Bihar.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("hold_district_social_justice_conventions", "Hold grand conventions across the state to rally backward class and minority voters.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Counter-mobilizations by forward castes polarize voter dynamics.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_presidents_rule", "Demand the dismissal of the state government, submitting a governor memo on lawlessness.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(14, "Parliamentary allies decline support, calling the demand politically premature.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_assembly_development_debate", "Propose a special assembly debate focusing purely on post-separation resource sharing.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Frequent disruptions and sloganeering prevent the assembly from voting on resolutions.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"politicalStabilityMemory": 2}, weight=0.2)
    ]
))

# 2001-09
ITEMS_2001_2005.append(make_news(
    key="bh2001_2001_09_teacher_pay_strike",
    month="2001-09",
    title="Primary School Teachers Launch Strike Over Unpaid Salaries",
    desc="Thousands of primary school teachers protest outside the Patna secretariat, demanding immediate clearance of unpaid DA and salary arrears.",
    tags=['protest'],
    base_w=1.15, profile="protest",
    reactions=[
        reaction("release_partial_arrears_with_bonds", "Release 30% of the arrears immediately, offering treasury bonds for the remaining portion.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(18, "Unions reject bonds, continuing blockades of district school inspector offices.", eff(-1, 0, -2, -2)), 1.15),
        reaction("support_teachers_demand_payout", "Support the teachers, demanding the government cut its advertising budgets to pay staff.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Ruling party releases salary expenditure audits, calling the strike politically timed.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_teacher_salary_escrow", "Propose creating a dedicated escrow account for education funds to prevent redirection of salaries.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Finance department raises legal objections to locking state funds in escrow.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2001-10
ITEMS_2001_2005.append(make_news(
    key="bh2001_2001_10_sugar_mill_crisis",
    month="2001-10",
    title="Closure of North Bihar Sugar Mills Sparks Farmer Distress",
    desc="Three major sugar mills in Champaran and Darbhanga shut down operations, leaving sugarcane farmers without buyers and demanding government intervention.",
    tags=['rural', 'economy'],
    base_w=1.2, profile="land_rights",
    reactions=[
        reaction("announce_sugar_mill_bailout", "Announce state loans to revive the mills and clear pending crop payments for farmers.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Revival works drag on, leaving the current season crops to rot in fields.", eff(0, 0, -2, -2)), 1.2),
        reaction("lead_mill_gates_blockades", "Lead farmer protests at mill gates, demanding the state nationalize the closed mills.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Mill owners obtain court stays against state intervention, stalling the demand.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_crop_diversification_subsidies", "Propose cash subsidies for farmers to switch from sugarcane to maize and pulses.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Farmers express reluctance to abandon traditional crops, leaving subsidies unused.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 2}, weight=0.25)
    ]
))

# 2001-11
ITEMS_2001_2005.append(make_news(
    key="bh2001_2001_11_barauni_refinery_strike",
    month="2001-11",
    title="Barauni Refinery Labor Strike Disrupts Local Fuel Supply",
    desc="Contract worker unions at the Barauni oil refinery launch an indefinite strike, demanding job regularization and safety benefits.",
    tags=['protest', 'economy'],
    base_w=1.15, profile="protest",
    reactions=[
        reaction("police_protection_for_non_striking_staff", "Deploy state police to protect non-striking staff and ensure refinery operations continue.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(18, "Clashes between striking workers and police trigger local shutdowns in Begusarai.", eff(-1, 0, -2, -2)), 1.15),
        reaction("support_regularization_demands_in_assembly", "Support the workers, introducing assembly resolutions demanding central public sector job guarantees.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Refinery management threatens to shift future expansion budgets to other states.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_tripartite_labor_tribunal", "Propose a tripartite arbitration panel of labor commissioners, union heads, and IOCL management.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Union factions reject the arbitration terms, prolonging the deadlock.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2001-12
ITEMS_2001_2005.append(make_news(
    key="bh2001_2001_12_calamity_fund_row",
    month="2001-12",
    title="State Accuses Centre of Withholding Flood Calamity Funds",
    desc="The Bihar Finance Minister accuses the central government of releasing inadequate calamity funds, citing biased treatment compared to other states.",
    tags=['politics', 'disaster_relief'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("publish_central_neglect_report", "Publish a detailed report on central fund allocations and hold protest rallies in Delhi.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Central agencies counter that Bihar failed to submit proper utilization certificates.", eff(-1, 0, -2, -2)), 1.25),
        reaction("demand_cag_probe_on_relief_spending", "Demand a CAG audit of relief fund allocations, alleging diversion of central aid to party bases.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, -1, 4, 3),
                 {},
                 risk(14, "Rural voters feel the opposition is trying to block calamity aid, leading to local anger.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_inter_state_disaster_council", "Propose a coalition of flood-affected states to demand objective, formula-based relief allocation.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Neighboring states decline joint action due to their own political alliances.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 2}, weight=0.2)
    ]
))

# 2002-01
ITEMS_2001_2005.append(make_news(
    key="bh2002_2002_01_rjd_reorganization",
    month="2002-01",
    title="Lalu Prasad Reorganizes RJD Committees to Secure Base",
    desc="RJD Chief Lalu Prasad Yadav initiates a massive organizational rejig, prioritizing local OBC and minority representatives in district committees.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("launch_district_membership_drives", "Launch extensive membership drives, offering cheap party identity cards to rural youth.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Discontented old cadres resign in protest over seat reallocations.", eff(-1, 0, -2, -2)), 1.2),
        reaction("expose_nepotism_in_committee_choices", "Expose family ties and crime cases of the new committee members, calling it dynasty politics.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "OBC voter organizations interpret the charges as anti-backward bias.", eff(0, 0, -2, -3)), 1.25),
        reaction("propose_bipartisan_youth_assembly", "Propose establishing a non-partisan Youth Assembly to discuss educational reforms in the state.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Rival youth wings clash at the inaugural venue, forcing a postponement.", eff(-1, 0, -1, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2002-02
ITEMS_2001_2005.append(make_news(
    key="bh2002_2002_02_patna_bypass_project",
    month="2002-02",
    title="Government Clears Patna Bypass Expressway Plan",
    desc="The urban development department clears the layout for a major bypass expressway around Patna to reduce growing traffic congestion in the capital.",
    tags=['governance', 'infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("allocate_bypass_construction_funds", "Allocate state funds and award contracts to construct the bypass under strict completion timelines.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Local landowners in Patna outskirts file suits challenging the land valuation.", eff(0, 0, -2, -2)), 1.2),
        reaction("demand_subsidies_for_slums_displaced", "Demand that the state provide guaranteed housing plots first to all families displaced by construction.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Urban trade chambers accuse the opposition of blocking civic infrastructure.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_bot_expressway_model", "Propose a Build-Operate-Transfer (BOT) model to attract private developers and save public funds.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Private bidders pull out, citing low toll revenue estimates in the state.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2002-03
ITEMS_2001_2005.append(make_news(
    key="bh2002_2002_03_sand_mining_alarms",
    month="2002-03",
    title="Illegal Sand Mining on Son Riverbed Sparks Alarms",
    desc="Environmental groups and local farmers raise alarms over illegal sand mining along the Son riverbed, alleging erosion of riverbanks and drop in water tables.",
    tags=['governance', 'environment'],
    base_w=1.1, profile="governance",
    reactions=[
        reaction("deploy_mining_guards_seize_vehicles", "Deploy armed mining guards, impose fines, and seize all unregistered excavators at the sites.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(16, "Mining mafia attacks the guard posts, leading to local law and order concerns.", eff(-1, 0, -2, -2)), 1.2),
        reaction("expose_mafia_patronage_by_ministers", "Expose cabinet minister letters recommending mining permit exemptions to specific contractors.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, -1, 4, 3),
                 {},
                 risk(12, "Ruling party claims the letters are forged, filing counter police cases.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_district_sand_cooperatives", "Propose transferring mining rights to local panchayat-run sand cooperatives to secure local revenue.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Administrative delays in registry leave the cooperatives inactive for months.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2002-04
ITEMS_2001_2005.append(make_news(
    key="bh2002_2002_04_muzaffarpur_crime",
    month="2002-04",
    title="Merchant Robberies Trigger Trade Strike in Muzaffarpur",
    desc="A series of armed robberies targetting cash traders in Muzaffarpur sparks outrage. Local chambers of commerce announce an indefinite market closure.",
    tags=['protest', 'law_order'],
    base_w=1.2, profile="protest",
    reactions=[
        reaction("increase_patrols_in_merchant_zones", "Deploy extra police platoons, set up check-posts, and hold meetings with trade leaders.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Delayed arrests lead to trade bodies continuing the market closures.", eff(-1, 0, -2, -2)), 1.2),
        reaction("lead_merchant_dharnas_against_police", "Lead merchant dharnas outside the SSP office, demanding immediate transfer of district police chiefs.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Trade groups distance themselves, saying they want security, not political battles.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_armed_market_guards_subsidies", "Propose subsidizing private security installations and licensed arms for registered merchant groups.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Police department objects, citing risks of arms misuse in public.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"securityIgnoredMemory": 2}, weight=0.25)
    ]
))

# 2002-05
ITEMS_2001_2005.append(make_news(
    key="bh2002_2002_05_railway_investments",
    month="2002-05",
    title="Central Railway Minister Nitish Kumar Announces Bihar Projects",
    desc="Union Railway Minister Nitish Kumar announces several mega projects for Bihar, including coach factories and new lines, heating up the state development debate.",
    tags=['infrastructure', 'politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("demand_state_role_in_land_clearance", "Demand the Centre transfer development funds to the state for coordinate land acquisitions first.",
                 ['GOVERNMENT'], eff(1, 0, 2, 3),
                 {},
                 risk(15, "Delays in state land clearance are highlighted by central ministers as anti-growth.", eff(-1, 0, -2, -2)), 1.15),
        reaction("campaign_on_central_development_benefits", "Campaign on the central railway projects, highlighting the NDA's commitment to industrializing Bihar.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Ruling party releases data showing slow progress of previously announced lines.", eff(-1, 0, -1, -1)), 1.25),
        reaction("propose_joint_railway_investment_board", "Propose a joint board representing state planners and railway officials to synchronize urban bypasses.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Jurisdictional disputes between state and central boards stall the project meetings.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2002-06
ITEMS_2001_2005.append(make_news(
    key="bh2002_2002_06_patna_waterlogging",
    month="2002-06",
    title="Pre-Monsoon Showers Clog Patna Drainage System",
    desc="Sudden heavy showers clog Patna's primary drainage lines. Major residential and commercial areas report waist-deep waterlogging.",
    tags=['governance', 'environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("deploy_water_pumps_clear_drains", "Deploy emergency pumping sets, clear municipal clogs, and suspend negligent municipal engineers.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(15, "Frequent power cuts during showers stall pumping works, causing public anger.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_municipal_corruption_probe", "Demand an independent probe into municipal expenditure, alleging siphoning of drain desilting funds.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, -1, 4, 3),
                 {},
                 risk(12, "Ruling party blames the rapid unplanned urban growth under previous central schemes.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_patna_drainage_master_plan", "Propose hiring international consultants to design a permanent gravity-based drainage master plan.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Master plan designs require years of survey, leaving the current season unresolved.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2002-07
ITEMS_2001_2005.append(make_news(
    key="bh2002_2002_07_kosi_embankment_breach",
    month="2002-07",
    title="Embankment Breach in Kosi Region Deluges 100 Villages",
    desc="A sudden breach in the Kosi river embankment in Saharsa district submerges over 100 villages, displacing thousands of families overnight.",
    tags=['disaster_relief', 'rural'],
    base_w=1.25, profile="disaster_relief",
    reactions=[
        reaction("launch_emergency_boat_rescue", "Deploy state rescue boats, distribute dry grain packets, and set up medical camps in elevated spots.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Shortage of country boats delays rescue in interior hamlets, drawing local criticism.", eff(-1, 0, -2, -2)), 1.25),
        reaction("demand_judicial_probe_on_embankment_safety", "Demand a judicial inquiry into embankment safety audits, alleging negligence in structural maintenance.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(14, "Audit processes delay the release of urgent local relief works, angering victims.", eff(0, 0, -2, -2)), 1.2),
        reaction("propose_elevated_village_cluster_plan", "Propose constructing raised mud platforms (chauras) to safeguard cattle and families during seasonal breaches.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Delayed execution keeps the raised platforms unfinished before next monsoons.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2002-08
ITEMS_2001_2005.append(make_news(
    key="bh2002_2002_08_pds_grain_scam",
    month="2002-08",
    title="Alleged Diversion of PDS Wheat Sparks Auditing Row",
    desc="Auditing officers report irregularities in state food storage yards, alleging that central PDS wheat allocations were diverted to private mills.",
    tags=['governance', 'corruption'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("suspend_warehouse_managers_order_probe", "Suspend suspected warehouse managers, order police FIRs, and mandate digitized stock ledgers.",
                 ['GOVERNMENT'], eff(2, -1, 3, 3),
                 {},
                 risk(16, "Warehouse unions strike in protest, disrupting current foodgrain supplies.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_cbi_investigation_into_grain_scam", "Demand a CBI investigation, alleging that high-level department heads are complicit in the diversion.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, -1, 4, 3),
                 {},
                 risk(12, "Ruling party accuses the opposition of trying to create administrative panic.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_panchayat_pds_monitoring", "Propose delegating ration card verification and shop monitoring directly to block panchayat heads.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Local political blockings prevent regular panchayat audit meetings.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"corruptionIgnoredMemory": 2}, weight=0.2)
    ]
))

# 2002-09
ITEMS_2001_2005.append(make_news(
    key="bh2002_2002_09_bhagalpur_silk_crisis",
    month="2002-09",
    title="Bhagalpur Silk Weavers Protest Power and Credit Scarcity",
    desc="Traditional silk weavers in Bhagalpur stage protest rallies, demanding dedicated power supply lines and interest waivers on handloom loans.",
    tags=['economy', 'protest'],
    base_w=1.15, profile="protest",
    reactions=[
        reaction("announce_handloom_subsidy_package", "Announce interest waivers on cooperative loans and subsidize power tariffs for handloom units.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "State cooperative banks delay credit rollouts, keeping weavers in distress.", eff(0, 0, -2, -1)), 1.2),
        reaction("demand_free_marketing_centers", "Demand the government set up state-run marketing centers to eliminate exploitation by middlemen.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Middlemen cartels threaten to stop buying, stalling local trade transactions.", eff(-1, 0, -1, -1)), 1.15),
        reaction("propose_bhagalpur_silk_park", "Propose establishing a modern integrated silk industrial park under a public-private partnership.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "High land acquisition costs delay park development planning.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"economyIssueMissed": 1}, weight=0.3)
    ]
))

# 2002-10
ITEMS_2001_2005.append(make_news(
    key="bh2002_2002_10_ljp_mobilizations",
    month="2002-10",
    title="LJP Holds Massive Rallies Demanding Scheduled Caste Reforms",
    desc="The Lok Janshakti Party (LJP) led by Ram Vilas Paswan holds rallies in Patna, demanding special recruitment drives for scheduled castes and police reforms.",
    tags=['politics', 'identity'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("promise_sc_backlog_recruitment", "Promise to fill all pending SC backlog vacancies in state departments within six months.",
                 ['GOVERNMENT'], eff(2, 0, 2, 4),
                 {},
                 risk(15, "General category employee unions protest, threatening strike actions.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_exclusive_sc_welfare_board", "Demand the creation of a statutory SC Welfare Board with judicial powers to probe atrocities.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Ruling party argues the current commission is sufficient, stalling the bill.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_judicial_commission_on_recruitment", "Propose a high court judge-led commission to review reservation compliance across departments first.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Commission hearings drag on, delaying active recruitment drives.", eff(-1, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 1}, weight=0.2)
    ]
))

# 2002-11
ITEMS_2001_2005.append(make_news(
    key="bh2002_2002_11_jehanabad_clashes",
    month="2002-11",
    title="Land Ownership Disputes Trigger Clashes in Jehanabad",
    desc="Tensions between agrarian unions and land-owning factions erupt into armed clashes in rural Jehanabad. State police seal district borders.",
    tags=['security_crisis', 'land_rights'],
    base_w=1.2, profile="security_crisis",
    reactions=[
        reaction("deploy_special_task_force", "Deploy state special task forces and establish permanent police pickets in sensitive hamlets.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(16, "Local farm workers allege police harassment and search excesses.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_land_redistribution_speedup", "Demand that the state fast-track redistribution of surplus ceiling lands to landless laborers.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Land-owning organizations file court challenges, freezing the distributions.", eff(-1, 0, -1, -2)), 1.2),
        reaction("propose_district_land_tribunals", "Propose setting up localized arbitration tribunals with representatives from both sides to resolve titles.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Lack of historical registry documents makes title arbitration impossible, stalling work.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 2}, weight=0.25)
    ]
))

# 2002-12
ITEMS_2001_2005.append(make_news(
    key="bh2002_2002_12_rural_phc_deficit",
    month="2002-12",
    title="PHC Audits Expose Shortage of Doctors in Rural Blocks",
    desc="A state health department audit reveals that over 60% of rural Primary Health Centers (PHCs) are operating without permanent doctors.",
    tags=['governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("mandate_rural_service_for_graduates", "Mandate three years of rural service for all state medical college graduates and fill PHC vacancies.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Medical students strike in Patna, protesting against the compulsory posting rule.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_doubling_of_rural_phc_pay", "Demand the government double the salaries of rural doctors and provide safe residential quarters.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Finance department rejects the pay hike, citing treasury deficit.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_telemedicine_link_projects", "Propose setting up telemedicine links connecting rural PHCs to district referral hospitals.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Frequent power cuts and poor internet make telemedicine terminals non-functional.", eff(0, 0, -2, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2003-01
ITEMS_2001_2005.append(make_news(
    key="bh2003_2003_01_opposition_unity",
    month="2003-01",
    title="BJP and JD(U) Hold High-Level Alliance Coordination Meetings",
    desc="Seeking to challenge the 13-year RJD regime, leaders of the BJP and JD(U) hold seat-sharing talks to present a single opposition front.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("dismiss_alliance_as_opportunistic", "Dismiss the alliance as opportunistic, highlighting the developmental records of the RJD.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Cadres in urban constituencies express concerns over rising opposition coordination.", eff(0, 0, -2, -1)), 1.15),
        reaction("jointly_announce_seat_sharing", "Jointly announce seat sharing and pledge to end administrative corruption if voted to power.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Factional leaders in three districts rebel, filing independent nominations.", eff(-1, 0, -1, -2)), 1.25),
        reaction("propose_bipartisan_development_code", "Propose a code of campaign ethics to restrict personal attacks and focus rallies on infrastructure.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Rivals ignore the code, escalating personal accusations on stage.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2003-02
ITEMS_2001_2005.append(make_news(
    key="bh2003_2003_02_labor_pension",
    month="2003-02",
    title="Government Expands Old Age Pension for Landless Laborers",
    desc="CM Rabri Devi announces an expansion of the Old Age Pension scheme, specifically targeting landless agricultural laborers and widows in rural blocks.",
    tags=['governance', 'welfare'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("increase_welfare_budget_allocations", "Increase the pension budget and set up village panchayat committees to identify eligible families.",
                 ['GOVERNMENT'], eff(2, 0, 3, 5),
                 {},
                 risk(15, "Local middlemen demand commissions from beneficiaries, drawing critical press.", eff(-1, -1, -2, -2)), 1.25),
        reaction("demand_biometric_verification_to_stop_leakage", "Demand biometric database verification to stop cash siphoned by non-existent beneficiaries.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Lack of biometric devices delays pension payouts for months, angering elders.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_post_office_direct_deposits", "Propose transferring all pension payouts directly through local post office accounts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Rural post offices report heavy staff shortages, stalling account openings.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 1}, weight=0.25)
    ]
))

# 2003-03
ITEMS_2001_2005.append(make_news(
    key="bh2003_2003_03_patna_university_clashes",
    month="2003-03",
    title="Senate Elections Trigger Patna University Student Clashes",
    desc="Tensions during the Patna University senate poll campaign erupt into clashes between rival student groups, forcing police to execute lathi-charges.",
    tags=['politics', 'protest'],
    base_w=1.15, profile="protest",
    reactions=[
        reaction("suspend_elections_enforce_campus_discipline", "Suspend the senate elections, restrict political entry, and deploy police guards at hostel gates.",
                 ['GOVERNMENT'], eff(1, 0, 3, 2),
                 {},
                 risk(15, "Student unions unite to launch a strike, alleging suppression of democratic rights.", eff(-1, 0, -2, -2)), 1.2),
        reaction("condemn_police_barbarism_on_students", "Condemn the police lathi-charge, demanding the immediate release of all arrested student leaders.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "Parent associations criticize the party for supporting rowdy campus groups.", eff(-1, 0, -2, -1)), 1.2),
        reaction("propose_bipartisan_student_welfare_panel", "Propose forming a student-teacher welfare panel to monitor senate campaign funding limits.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Student groups reject funding limits, refusing to cooperate with the panel.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2003-04
ITEMS_2001_2005.append(make_news(
    key="bh2003_2003_04_gandhi_setu_repairs",
    month="2003-04",
    title="Government Clears Mahatma Gandhi Setu Pipeline Repairs",
    desc="The cabinet clears a special budget to repair the Mahatma Gandhi Setu pipelines, crucial for linking water and transit between North and South Bihar.",
    tags=['governance', 'infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("fast_track_bridge_repair_contracts", "Award fast-track repair contracts and restrict heavy truck transit to ensure structural safety.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Truck associations strike, halting freight movement across the Ganges.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_cbi_probe_on_bridge_contracts", "Demand a CBI investigation into previous repair contracts, alleging massive siphoning of state funds.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, -1, 4, 3),
                 {},
                 risk(14, "Commuters criticize the opposition, stating repair works should not be politicized.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_ganga_ferry_services", "Propose launching state-run ferry services for passengers during bridge repair hours.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Lack of river ports near Patna delays ferry launches for months.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2003-05
ITEMS_2001_2005.append(make_news(
    key="bh2003_2003_05_lathi_rally",
    month="2003-05",
    title="RJD Holds Historic 'Lathi Rally' in Patna Gandhi Maidan",
    desc="RJD Chief Lalu Prasad Yadav organizes a massive 'Lathi Rally' in Patna, drawing lakhs of rural supporters carrying lathis to symbolize grassroots empowerment.",
    tags=['politics'],
    base_w=1.3, profile="politics",
    reactions=[
        reaction("hail_rally_as_grassroots_defiance", "Hail the rally as a display of subaltern pride and defiance against elite political conspiracies.",
                 ['GOVERNMENT'], eff(3, 0, 4, 5),
                 {},
                 risk(18, "Opposition files petitions in court, alleging misuse of state buses for transport.", eff(-2, 0, -2, -2)), 1.25),
        reaction("condemn_rally_as_promotion_of_lawlessness", "Condemn the rally, arguing it projects muscle politics and frightens urban citizens.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(14, "Rural voter blocks interpret the criticism as an attack on their presence in capital.", eff(0, 0, -2, -3)), 1.2),
        reaction("propose_development_rally_alternative", "Propose that all future rallies be held on development parameters, banning weapons or lathis.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Rivals mock the proposal, continuing traditional rally styles.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.15)
    ]
))

# 2003-06
ITEMS_2001_2005.append(make_news(
    key="bh2003_2003_06_lathi_rally_fallout",
    month="2003-06",
    title="Debates Heat Up in Assembly Over Lathi Rally Expenditures",
    desc="Following the Lathi Rally, opposition MLAs disrupt assembly proceedings, demanding details of the public funds and transport utilized for the event.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("present_expenditure_audits_defend_event", "Present audited bills showing the event was fully funded by party donations, defending the turnout.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Discrepancies in bus hiring records draw critical local newspaper coverage.", eff(-1, -1, -2, -1)), 1.15),
        reaction("demand_refund_of_state_transport_costs", "Demand that RJD refund state transport corporations for the special trains used by rally attendees.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Railway board states special trains are standard paid commercial runs.", eff(0, 0, -1, -1)), 1.2),
        reaction("propose_bipartisan_assembly_audit", "Propose an all-party assembly audit panel to clear all doubts regarding public expenditure.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "MLAs refuse to sit on the panel, stalling the auditing process.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2003-07
ITEMS_2001_2005.append(make_news(
    key="bh2003_2003_07_paddy_procurement",
    month="2003-07",
    title="Farmers Block Rohtas Highways Demanding Paddy Buying Centers",
    desc="Paddy farmers in Rohtas district block national highways, protesting the lack of government buying centers and exploitation by local grain agents.",
    tags=['land_rights', 'rural'],
    base_w=1.2, profile="land_rights",
    reactions=[
        reaction("open_emergency_procurement_centers", "Open emergency state buying centers in Rohtas and guarantee minimum support prices.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Delayed payments from state coop banks trigger fresh sit-ins.", eff(-1, 0, -2, -2)), 1.2),
        reaction("lead_farmer_marches_demanding_agent_ban", "Lead farmer marches to district collectorates, demanding a complete ban on private middleman trading.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Private trading lobbies suspend buying, leaving farmers without immediate cash.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_digitized_procurement_slips", "Propose issuing digitized buying slips to prevent private agents from using farmer credentials.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Frequent power failures at rural centers keep system terminals offline.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 2}, weight=0.25)
    ]
))

# 2003-08
ITEMS_2001_2005.append(make_news(
    key="bh2003_2003_08_gaya_dengue_outbreak",
    month="2003-08",
    title="Sanitation Failures Trigger Major Dengue Outbreak in Gaya",
    desc="Over 500 cases of dengue are reported in Gaya. Local hospitals face acute shortage of blood platelets and beds, sparking public panic.",
    tags=['governance'],
    base_w=1.2, profile="health_crisis",
    reactions=[
        reaction("deploy_medical_teams_and_fogging", "Deploy medical teams from Patna, subsidize platelet kits, and launch district-wide fogging operations.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Substandard fogging chemicals lead to complaints and poor mosquito control.", eff(-1, -1, -2, -2)), 1.2),
        reaction("expose_hospital_negligence_and_waste", "Expose pile-ups of waste and broken generators in Gaya hospitals, accusing the government of collapse.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, -1, 4, 3),
                 {},
                 risk(12, "Hospital staff unions protest, accusing the opposition of defaming field workers.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_district_health_emergency_board", "Propose a district health board with local doctors to manage emergency logistics.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Disagreements over board leadership delay supply distributions.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 2}, weight=0.25)
    ]
))

# 2003-09
ITEMS_2001_2005.append(make_news(
    key="bh2003_2003_09_caste_representation_row",
    month="2003-09",
    title="Opposition Accuses Government of Bias in Police Postings",
    desc="Opposition parties hold a joint press meet, releasing lists of recent police station officer (SO) appointments to allege systematic caste bias.",
    tags=['politics', 'identity'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("assert_representation_figures", "Assert that the postings reflect state representation and backward class empowerment goals.",
                 ['GOVERNMENT'], eff(2, 0, 2, 4),
                 {},
                 risk(15, "Accusations of neglecting merit trigger protests by student bodies in Patna.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_merit_based_posting_rules", "Demand a transparent merit-based posting policy monitored by a police selection board.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Backward class voter organizations interpret this as an attempt to restore elite hegemony.", eff(0, 0, -2, -3)), 1.25),
        reaction("propose_bipartisan_police_reforms_panel", "Propose an all-party legislative committee to review posting rules in line with court directives.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Delayed hearings prevent the committee from submitting its report.", eff(-1, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 1}, weight=0.2)
    ]
))

# 2003-10
ITEMS_2001_2005.append(make_news(
    key="bh2003_2003_10_bhojpuri_cinema_tax_waiver",
    month="2003-10",
    title="Cabinet Approves Entertainment Tax Waivers for Regional Films",
    desc="To promote Bhojpuri and Maithili languages, the state cabinet approves entertainment tax waivers for films shot locally inside Bihar.",
    tags=['governance', 'politics'],
    base_w=1.1, profile="governance",
    reactions=[
        reaction("launch_regional_film_subsidy", "Launch a regional film development fund and clear plans to build a film city in Rajgir.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Lack of immediate infrastructure in Rajgir leaves projects on paper only.", eff(0, 0, -1, -1)), 1.2),
        reaction("demand_priority_for_primary_schools", "Demand that state funds be spent on primary school roofs instead of commercial film subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Regional artists union criticizes the opposition as anti-cultural.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_school_cultural_programs", "Propose that tax-exempt films screen educational history chapters for free at rural schools.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Lack of projector facilities in rural schools prevents the screens.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2003-11
ITEMS_2001_2005.append(make_news(
    key="bh2003_2003_11_assam_attacks_retaliation",
    month="2003-11",
    title="Anti-Bihari Attacks in Assam Trigger Student Protests in Patna",
    desc="Reports of attacks on Bihari railway candidates in Assam trigger angry student demonstrations in Patna, causing minor rail blockades.",
    tags=['protest', 'security_crisis'],
    base_w=1.2, profile="security_crisis",
    reactions=[
        reaction("contact_assam_government_for_safety", "Contact the Assam government to demand safety measures and deploy police to clear Patna rail tracks.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Rail clearing leads to clashes with student groups near Patna junction.", eff(-1, 0, -2, -2)), 1.2),
        reaction("lead_dharnas_outside_assam_houses", "Lead student dharnas outside central railway offices, demanding reserve quotas for local state candidates.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Railway ministry rejects regional quotas, citing national recruitment rules.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_national_integration_peace_council", "Propose an all-party delegation to travel to Assam to coordinate peace and student dialogues.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political groups in Assam refuse to host the delegation, stalling peace talks.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"securityIgnoredMemory": 2}, weight=0.25)
    ]
))

# 2003-12
ITEMS_2001_2005.append(make_news(
    key="bh2003_2003_12_doctor_kidnapping",
    month="2003-12",
    title="Kidnapping of Patna Doctor Sparks IMA Strike Notice",
    desc="A prominent doctor is kidnapped in Patna. The Indian Medical Association (IMA) issues a strike notice, threatening shutdown of all private clinics.",
    tags=['protest', 'law_order'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("launch_anti_ransom_operation", "Instruct DGP to coordinate anti-ransom operations, rescue the doctor, and assign guards to clinics.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Extended rescue search leads to IMA executing the private clinic shut-down.", eff(-1, -1, -2, -2)), 1.2),
        reaction("lead_medical_cadre_protests", "Lead protest rallies with IMA members, demanding immediate rollback of license fees and safer zones.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "General public complains about lack of emergency medical access during rallies.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_hospital_security_bill", "Propose a statutory Hospital Security Act to make offenses against doctors non-bailable.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Legal drafting delays keep the bill pending in the assembly secretariat.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"securityIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2004-01
ITEMS_2001_2005.append(make_news(
    key="bh2004_2004_01_alliance_maneuvers",
    month="2004-01",
    title="UPA Alliance Talks Begin Ahead of General Elections",
    desc="The RJD, Congress, and LJP initiate high-level seat-sharing talks in Patna to present a unified UPA front against the NDA.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("concede_seats_for_national_unity", "Concede five seats to allies to lock down the coalition, announcing joint rallies.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Local party cadres rebel in the ceded seats, filing independent papers.", eff(-2, 0, -1, -2)), 1.2),
        reaction("highlight_alliance_internal_contradictions", "Highlight contradictions between RJD and LJP on law and order, calling the alliance unstable.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(15, "Coalition leaders resolve differences quickly, reducing the impact of charges.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_joint_development_manifesto", "Propose that the coalition draft a written manifesto focusing purely on state finance recoveries.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Disagreements over specific tax sharing delay the manifesto launch.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2004-02
ITEMS_2001_2005.append(make_news(
    key="bh2004_2004_02_charwaha_vidyalaya_review",
    month="2004-02",
    title="Government Evaluates Charwaha Vidyalaya SHEPHERD Schools",
    desc="The education department orders an evaluation of RJD's shepherd school model (Charwaha Vidyalayas), drawing mixed reviews from educationists.",
    tags=['governance', 'education'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("allocate_modernization_funds_for_schools", "Allocate extra state funds to add vocational computer blocks to successful shepherd schools.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Audit reports expose siphoning of school funds in two districts, drawing bad press.", eff(-1, -1, -2, -2)), 1.25),
        reaction("demand_conversion_to_regular_schools", "Demand that the state convert these schools into regular primary schools with standard infrastructure.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Marginalized sections view this as attempt to close down subaltern spaces.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_panchayat_educational_audit", "Propose that local panchayats oversee school attendance and teacher postings directly.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Panchayat heads decline oversight, citing lack of training in school rules.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"educationIssueMissed": 1}, weight=0.25)
    ]
))

# 2004-03
ITEMS_2001_2005.append(make_news(
    key="bh2004_2004_03_lok_sabha_campaigns",
    month="2004-03",
    title="Lok Sabha Election Campaigns Reach Peak in Bihar",
    desc="Campaigning for 40 parliamentary seats heats up. RJD focuses on social justice and secularism, while NDA attacks the state's development record.",
    tags=['election'],
    base_w=1.25, profile="election",
    reactions=[
        reaction("campaign_on_social_empowerment_gains", "Campaign heavily on social empowerment and the representation of backward classes in politics.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Opposition highlights instances of delayed crop payments and rural power cuts.", eff(0, 0, -2, -2)), 1.2),
        reaction("highlight_fifteen_years_development_deficit", "Highlight 15 years of development deficit, focusing on closed mills and student out-migration.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Ruling candidates win several key seats due to strong regional caste equations.", eff(-1, 0, -1, -1)), 1.25),
        reaction("propose_debates_on_industrial_investments", "Propose a series of public debates on attracting private agro-industries to second-tier cities.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(10, "Rivals refuse to attend, leading to media campaigns calling them anti-dialogue.", eff(-1, 0, -1, -1)), 1.1),
        no_comment(weight=0.2)
    ]
))

# 2004-04
ITEMS_2001_2005.append(make_news(
    key="bh2004_2004_04_polling_violence",
    month="2004-04",
    title="Incidents of Booth Capturing Reported in Saran and Hajipur",
    desc="Lok Sabha polling in Saran and Hajipur witness instances of booth capturing. The Election Commission orders re-polling in multiple centers.",
    tags=['election', 'security_crisis'],
    base_w=1.2, profile="security_crisis",
    reactions=[
        reaction("order_strict_re_polling_with_state_police", "Order strict re-polling, deploying extra police forces and installing video recorders.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Opposition accuses the local administration of bias towards the ruling candidates.", eff(-1, 0, -2, -2)), 1.15),
        reaction("petition_ec_for_exclusive_central_forces", "Petition the EC to deploy exclusive central paramilitary forces for all re-polling booths.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "EC delays approvals, citing logistics of central battalions during multi-phase polls.", eff(0, 0, -1, -1)), 1.2),
        reaction("propose_all_party_polling_monitors", "Propose that every polling center allow a joint candidate team to inspect EVM seals live.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Cadres clash outside booths despite joint monitoring, causing minor delays.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"securityIgnoredMemory": 2}, weight=0.25)
    ]
))

# 2004-05
ITEMS_2001_2005.append(make_news(
    key="bh2004_2004_05_election_results",
    month="2004-05",
    title="UPA Sweeps Bihar Lok Sabha Polls; RJD Wins 22 Seats",
    desc="The RJD-Congress-LJP alliance sweeps Bihar, winning 29 out of 40 seats. Lalu Prasad Yadav is sworn in as the Union Railway Minister.",
    tags=['election', 'politics'],
    base_w=1.3, profile="election",
    reactions=[
        reaction("declare_social_justice_triumph", "Declare the mandate as a triumph of secular forces and launch state-wide celebration rallies.",
                 ['GOVERNMENT'], eff(3, 0, 4, 5),
                 {},
                 risk(18, "Opposition files petitions challenging candidate affidavits in three seats.", eff(-1, 0, -2, -2)), 1.25),
        reaction("highlight_governance_deficit_in_state_despite_delhi", "Highlight that despite Delhi power, the state administration remains crippled by lack of funds.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(14, "Ruling party argues the UPA victory will bring massive packages to Bihar.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_joint_development_manifesto_revision", "Propose an all-party convention to draft a joint state economic recovery plan to submit to UPA.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Fierce rivalries between state leaders prevent the convention from signing draft.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.2)
    ]
))

# 2004-06
ITEMS_2001_2005.append(make_news(
    key="bh2004_2004_06_barauni_power_shutdown",
    month="2004-06",
    title="Barauni Thermal Power Station Shuts Down Operations",
    desc="A technical breakdown at the Barauni thermal power station leads to complete power shutdowns, plunging Patna and central Bihar into blackouts.",
    tags=['governance', 'infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("allocate_emergency_boiler_repair_funds", "Allocate emergency funds to replace boiler parts and deploy mobile diesel generators.",
                 ['GOVERNMENT'], eff(1, 0, 2, 3),
                 {},
                 risk(15, "Generator fuel bills trigger auditing rows and local press criticisms.", eff(-1, -1, -2, -2)), 1.15),
        reaction("demand_dismantling_of_state_power_utility", "Demand dismantling the corrupt state utility board and importing power from NTPC directly.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Utility board unions strike, threatening to shut down grid lines.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_grid_modernization_treaty", "Propose signing a long-term modernization treaty with NTPC to manage state generation plants.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Negotiations stall over employee pension transfer clauses, delaying work.", eff(0, 0, -2, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2004-07
ITEMS_2001_2005.append(make_news(
    key="bh2004_2004_07_monsoon_floods",
    month="2004-07",
    title="Kosi and Bagmati Rivers Submerge 20 North Bihar Districts",
    desc="Heavy seasonal rain in Nepal triggers massive water releases, causing Kosi and Bagmati rivers to flood 20 districts and displace over 20 lakh people.",
    tags=['disaster_relief', 'rural'],
    base_w=1.25, profile="disaster_relief",
    reactions=[
        reaction("launch_mega_aerial_relief_operations", "Deploy state resources for aerial food drops, and set up medical camps in dry highland areas.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Substandard food packets distributed trigger protest rallies at block offices.", eff(-1, -1, -2, -2)), 1.25),
        reaction("demand_immediate_central_relief_package", "Demand the central government declare it a national disaster and release Rs 1,000 crore relief.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Central delegation delays visits to assess damage, slowing relief flows.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_river_embankment_safety_commission", "Propose a joint Nepal-Bihar river safety commission to monitor dam releases during monsoon.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Diplomatic protocols delay the commission meetings, keeping monsoon active.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2004-08
ITEMS_2001_2005.append(make_news(
    key="bh2004_2004_08_central_relief_allocation",
    month="2004-08",
    title="Central UPA Cabinet Announces Rs 500 Crore Bihar Package",
    desc="Following visits by UPA ministers, the central government announces a special Rs 500 crore package for Bihar flood relief and infrastructure repairs.",
    tags=['politics', 'disaster_relief'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("hail_package_as_benefit_of_double_engine", "Hail the package as a benefit of UPA coordination and speed up road repair works.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Opposition alleges diversion of central funds to specific political strongholds.", eff(0, 0, -2, -2)), 1.2),
        reaction("demand_cag_oversight_of_package_expenditure", "Demand that the CAG monitor the package, alleging prior relief funds were siphoned.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, -1, 4, 3),
                 {},
                 risk(12, "Ruling party accuses the opposition of trying to block the development funds.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_district_wise_fund_allocation", "Propose allocating the fund to districts strictly based on population and damage indices.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Delayed damage assessments stall the allocation, leaving funds unspent.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 2}, weight=0.25)
    ]
))

# 2004-09
ITEMS_2001_2005.append(make_news(
    key="bh2004_2004_09_kislay_kaushal_kidnap",
    month="2004-09",
    title="Patna School Student Kislay Kaushal Kidnapped; Public Outrage",
    desc="Armed men kidnap school student Kislay Kaushal in Patna. The incident triggers massive public fury and demands for immediate police action.",
    tags=['law_order', 'security_crisis'],
    base_w=1.35, profile="security_crisis",
    reactions=[
        reaction("order_police_crackdown_on_ransom_gangs", "Order a massive police crackdown on suspected gang hideouts in Patna outskirts.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(22, "Extended search fails to rescue the student, drawing critical news channels.", eff(-2, 0, -3, -4)), 1.25),
        reaction("lead_citizen_protest_rallies", "Lead citizen protest rallies in Patna, demanding the CM's resignation over law collapse.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 5),
                 {},
                 risk(16, "Police resort to tear gas to clear rallies, leading to cadre arrests.", eff(-1, 0, -2, -1)), 1.3),
        reaction("propose_fast_track_courts_for_kidnappers", "Propose setting up special fast-track courts to try kidnapping suspects within 30 days.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(12, "Legal department raises objections to fast-tracking trials, stalling the bill.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"securityIgnoredMemory": 3}, weight=0.1)
    ]
))

# 2004-10
ITEMS_2001_2005.append(make_news(
    key="bh2004_2004_10_kidnap_protests",
    month="2004-10",
    title="Patna Schools and Markets Shut Down in Kidnapping Protests",
    desc="Protesting the failure to rescue Kislay Kaushal, trade bodies and school associations call for a complete shutdown of Patna markets and institutions.",
    tags=['protest'],
    base_w=1.25, profile="protest",
    reactions=[
        reaction("deploy_forces_guarantee_school_security", "Deploy police guards outside all schools and assure trade leaders of speedy investigation.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Clashes between student protestors and police trigger minor injuries.", eff(-1, 0, -2, -3)), 1.2),
        reaction("continue_indefinite_patna_bandh", "Continue the protest strikes, demanding the home portfolio be transferred to a senior administrator.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "General public gets frustrated by school shutdowns, demanding normal classes.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_cross_party_peace_resolution", "Propose an assembly resolution condemning the kidnap and forming a joint peace advisory.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Opposition boycotts the assembly session, calling the resolution a PR stunt.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.2)
    ]
))

# 2004-11
ITEMS_2001_2005.append(make_news(
    key="bh2004_2004_11_presidents_rule_demands",
    month="2004-11",
    title="Opposition Submits Memo to Governor Demanding President's Rule",
    desc="NDA leaders meet the Governor of Bihar, submitting a memorandum on the law and order state and demanding the imposition of President's Rule.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("dismiss_demand_as_undemocratic", "Dismiss the demand as undemocratic, asserting that the state government enjoys a clear majority.",
                 ['GOVERNMENT'], eff(2, 0, 2, 3),
                 {},
                 risk(15, "Governor sends a report to Centre on law and order, creating administrative tension.", eff(-1, 0, -2, -2)), 1.15),
        reaction("hold_state_wide_dharnas_against_jungle_raj", "Hold state-wide dharnas, calling the regime 'Jungle Raj' and demanding central intervention.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "Ruling party cadres disrupt the dharna spots, leading to localized clashes.", eff(-1, 0, -2, -1)), 1.2),
        reaction("propose_all_party_governance_debate", "Propose a special debate on law and order in the assembly to clear all allegations.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Rival slogans disrupt the assembly debate within minutes, stalling the house.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2004-12
ITEMS_2001_2005.append(make_news(
    key="bh2004_2004_12_police_crackdown",
    month="2004-12",
    title="Police Launch Major Crackdown on Ransom Hideouts",
    desc="Under severe public pressure, state police launch coordinate raids in Patna, Nalanda, and Vaishali, arresting several gang members.",
    tags=['law_order'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("publicize_arrests_and_seizure_of_arms", "Publicize the arrest details on state media, promising safety for all school children.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Opposition claims the main gang leaders were tipped off and escaped.", eff(0, 0, -2, -2)), 1.2),
        reaction("label_crackdown_as_cosmetic_before_polls", "Label the crackdown as cosmetic, alleging it is timed to mislead voters before assembly polls.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "IMA welcomes the police actions, reducing the impact of criticism.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_district_safety_boards", "Propose safety committees in every district with schools, parents, and police reps.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Lack of police staff prevents them from attending committee meetings.", eff(0, 0, -1, -1)), 1.15),
        no_comment(weight=0.3)
    ]
))

# 2005-01
ITEMS_2001_2005.append(make_news(
    key="bh2005_2005_01_assembly_campaigns",
    month="2005-01",
    title="Assembly Campaigning Reaches Peak; UPA Alliances Split",
    desc="With assembly polls scheduled, RJD and LJP decide to fight independently, turning the election into a three-cornered contest with the NDA.",
    tags=['election'],
    base_w=1.25, profile="election",
    reactions=[
        reaction("campaign_on_social_justice_legacy", "Campaign heavily on social justice legacy, warning against upper-caste NDA resurgence.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "LJP candidate campaigns split the secular vote share in key blocks.", eff(-1, 0, -2, -2)), 1.15),
        reaction("highlight_administrative_paralysis_and_scams", "Highlight administrative paralysis and road deficits, offering a development roadmap.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Ruling party rallies counter with social justice appeals, keeping vote tight.", eff(0, 0, -1, -1)), 1.3),
        reaction("propose_bipartisan_governance_accord_draft", "Propose that all parties sign a draft pledging to support infrastructure regardless of mandate.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Rival candidates refuse to sign, calling it pre-election posturing.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2005-02
ITEMS_2001_2005.append(make_news(
    key="bh2005_2005_02_hung_assembly_results",
    month="2005-02",
    title="Bihar Assembly Elections Result in Hung House",
    desc="The election results deliver a hung assembly. NDA wins 92 seats, RJD 75, and LJP 29, leaving no coalition with a clear majority to form government.",
    tags=['election', 'politics'],
    base_w=1.3, profile="politics",
    reactions=[
        reaction("assert_right_to_form_coalition", "Hold talks with independent MLAs to secure support, asserting RJD's right to form cabinet.",
                 ['GOVERNMENT'], eff(2, 0, 2, 3),
                 {},
                 risk(18, "LJP refuses to support any RJD-led cabinet, keeping the deadlock active.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_nda_claim_to_govern", "Demand that the Governor invite the NDA as the single largest pre-poll alliance.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Governor refuses to invite NDA, citing lack of signed letters from allies.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_all_party_governance_talks", "Propose an all-party round table to explore a neutral compromise cabinet for the state.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Fierce leader rivalries prevent the round table from meeting on schedule.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"politicalStabilityMemory": 3}, weight=0.2)
    ]
))

# 2005-03
ITEMS_2001_2005.append(make_news(
    key="bh2005_2005_03_presidents_rule",
    month="2005-03",
    title="President's Rule Imposed in Bihar; Rabri Devi Steps Down",
    desc="Following the deadlock, Governor Buta Singh recommends President's Rule. The Union Cabinet approves; CM Rabri Devi formally steps down.",
    tags=['politics'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("pledge_cooperation_with_governor_administration", "Pledge cooperation with Governor's administration while preparing cadres for fresh polls.",
                 ['GOVERNMENT'], eff(2, 0, 2, 3),
                 {},
                 risk(15, "Cadres express frustration over loss of administrative access in districts.", eff(-1, 0, -2, -2)), 1.15),
        reaction("label_rule_as_backdoor_rjd_regime", "Label the President's Rule as a backdoor RJD regime run by UPA allies from Delhi.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "Governor issues administrative transfers of corrupt block officers, reducing impact.", eff(0, 0, -1, -1)), 1.2),
        reaction("propose_bipartisan_advisory_council", "Propose forming a bipartisan advisory council of ex-MLAs to assist the Governor.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Governor administration declines, citing direct bureaucratic control rules.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"politicalStabilityMemory": 2}, weight=0.25)
    ]
))

# 2005-04
ITEMS_2001_2005.append(make_news(
    key="bh2005_2005_04_ljp_defection_drama",
    month="2005-04",
    title="Rumours of LJP Defections Spark Horse-Trading Accusations",
    desc="Local news channels report that RJD is trying to win over LJP MLAs to form a majority, leading to fierce accusations of horse-trading.",
    tags=['politics', 'corruption'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("deny_defection_claims_assert_stability", "Deny the claims, stating that any political alignment will be transparent and legal.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(16, "Audio clips of alleged MLA negotiations leak, drawing critical press.", eff(-1, -1, -2, -2)), 1.15),
        reaction("demand_strict_anti_defection_action", "Demand that the Governor freeze assembly proceedings and disqualify defecting MLAs.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Legal experts state that anti-defection rules only apply inside the house.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_public_morality_pledge", "Propose that all parties sign a public pledge to not accept defecting MLAs in their ranks.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Rivals dismiss the pledge as posturing, continuing private talks.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"corruptionIgnoredMemory": 2}, weight=0.25)
    ]
))

# 2005-05
ITEMS_2001_2005.append(make_news(
    key="bh2005_2005_05_assembly_dissolution",
    month="2005-05",
    title="Cabinet Dissolves Bihar Assembly; Legal Challenges Filed",
    desc="On Governor Buta Singh's recommendation, the Union Cabinet dissolves the Bihar Assembly overnight. NDA files immediate challenges in Supreme Court.",
    tags=['politics'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("defend_dissolution_to_prevent_horse_trading", "Defend the dissolution as a necessary step to prevent horse-trading and clean the mandate.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Supreme Court issues critical remarks during preliminary hearings.", eff(-1, 0, -2, -2)), 1.2),
        reaction("condemn_dissolution_as_murder_of_democracy", "Condemn the dissolution as murder of democracy, calling for state-wide black day rallies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Clashes between cadres during rallies draw police security actions.", eff(-1, 0, -1, -1)), 1.25),
        reaction("propose_speedy_fresh_polls_resolution", "Propose that all parties pass a resolution demanding fresh elections be held within 90 days.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "EC states poll schedules depend on monsoon and security forces availability.", eff(0, 0, -1, -1)), 1.15),
        no_comment(weight=0.2)
    ]
))

# 2005-06
ITEMS_2001_2005.append(make_news(
    key="bh2005_2005_06_supreme_court_hearings",
    month="2005-06",
    title="Supreme Court Begins Hearings on Assembly Dissolution Cases",
    desc="A constitution bench of the Supreme Court begins hearings on petitions challenging the dissolution of the Bihar assembly, drawing national focus.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("submit_governor_reports_in_defense", "Submit detailed Governor security intelligence reports defending the dissolution decision.",
                 ['GOVERNMENT'], eff(1, 0, 2, 3),
                 {},
                 risk(15, "SC judges question the validity of intelligence reports, causing bad press.", eff(-1, 0, -2, -2)), 1.15),
        reaction("demand_strict_adherence_to_srbommai_rules", "Demand adherence to SR Bommai rules, asserting that majority must only be tested on floor.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "Ruling allies claim the Bommai precedent does not apply to un-constituted assemblies.", eff(0, 0, -1, -2)), 1.2),
        reaction("propose_constitutional_clarification", "Propose a parliamentary bill to explicitly define Governor powers regarding assembly dissolution.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "National parties delay debates, leaving the current legal case unresolved.", eff(0, 0, -1, -1)), 1.15),
        no_comment(weight=0.25)
    ]
))

# 2005-07
ITEMS_2001_2005.append(make_news(
    key="bh2005_2005_07_mid_day_meal_audits",
    month="2005-07",
    title="Governor Orders Direct Audits of School Mid-Day Meals",
    desc="The Governor's administration orders district collectorates to audit primary school mid-day meals, exposing leakage of food grain allocations.",
    tags=['governance', 'welfare'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("enforce_audit_and_penalize_suppliers", "Enforce audit recommendations, cancel supplier licenses, and register police cases.",
                 ['GOVERNMENT'], eff(2, -1, 3, 3),
                 {},
                 risk(15, "Supplier lobbies strike, disrupting meal distributions in three districts.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_cbi_probe_on_prior_meal_budgets", "Demand a CBI probe into previous meal budgets, alleging RJD siphoned development aid.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, -1, 4, 3),
                 {},
                 risk(12, "RJD claims the audit is a politically motivated hunt by UPA opponents.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_parents_mid_day_meal_committees", "Propose delegating meal cooking and monitoring to local school mother committees.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Lack of basic kitchen sheds in rural schools prevents local cooking.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 1}, weight=0.25)
    ]
))

# 2005-08
ITEMS_2001_2005.append(make_news(
    key="bh2005_2005_08_rural_roads_push",
    month="2005-08",
    title="Governor Administration Fast-Tracks Rural Road Projects",
    desc="The Governor's administration directs the rural development cell to fast-track pending PMGSY road construction works in Central Bihar.",
    tags=['governance', 'infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("allocate_matching_state_treasury_funds", "Allocate matching state funds to clear pending land compensation files for contractors.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Agrarian unions protest, demanding higher land valuation rates.", eff(0, 0, -2, -2)), 1.2),
        reaction("demand_probe_on_prior_road_delays", "Demand a probe into prior road delays, alleging contractors paid kickbacks to stay idle.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 3),
                 {},
                 risk(12, "Contractor associations strike, halting current construction works.", eff(-1, 0, -2, -1)), 1.15),
        reaction("propose_district_road_quality_panels", "Propose appointing retired engineers to audit road quality before clearing payment files.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Oversight audits delay payments, slowing down overall construction speed.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2005-09
ITEMS_2001_2005.append(make_news(
    key="bh2005_2005_09_fresh_election_campaigns",
    month="2005-09",
    title="Fresh Bihar Assembly Elections Announced; NDA Campaigns on Change",
    desc="The EC announces fresh assembly elections for October-November. Nitish Kumar projects himself as the chief ministerial face of change and development.",
    tags=['election'],
    base_w=1.25, profile="election",
    reactions=[
        reaction("campaign_on_social_justice_defence", "Campaign heavily on social justice defense, warning against upper-caste NDA policies.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Voter fatigue arises over long incumbency, slowing down campaign energy.", eff(-1, 0, -2, -1)), 1.15),
        reaction("campaign_on_development_and_sushasan", "Campaign aggressively on development and good governance ('Sushasan'), offering road maps.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "RJD candidates counter with local community coordination, keeping seats close.", eff(-1, 0, -1, -1)), 1.25),
        reaction("propose_bipartisan_polling_monitoring_team", "Propose requesting the EC to install CCTV cameras in all sensitive rural booths.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Technical errors in remote booths leave cameras offline on polling day.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2005-10
ITEMS_2001_2005.append(make_news(
    key="bh2005_2005_10_sc_verdict_dissolution",
    month="2005-10",
    title="Supreme Court Declares Assembly Dissolution Unconstitutional",
    desc="The Supreme Court declares the assembly dissolution unconstitutional but declines to restore the house, ordering current polls to proceed.",
    tags=['politics'],
    base_w=1.3, profile="politics",
    reactions=[
        reaction("accept_verdict_focus_on_election_campaign", "Accept the verdict, stating that the public court will deliver the final political judgment.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(18, "Opposition uses the verdict to launch aggressive campaigns against cabinet bias.", eff(-1, 0, -2, -2)), 1.15),
        reaction("demand_immediate_resignation_of_union_cabinet", "Demand resignation of the Union Home Minister and Governor Buta Singh over the SC verdict.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Central ministers refuse to step down, calling the verdict procedural.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_bipartisan_resolution_on_governor_powers", "Propose that the assembly pass a resolution defining clear guidelines for Governor reports.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Electoral campaigns prevent parties from attending joint drafting meetings.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2005-11
ITEMS_2001_2005.append(make_news(
    key="bh2005_2005_11_nda_victory",
    month="2005-11",
    title="NDA Wins Majority in Bihar; Nitish Kumar Sworn In as CM",
    desc="The JD(U)-BJP alliance wins a clean majority of 143 seats, ending 15 years of RJD rule. Nitish Kumar is sworn in as the Chief Minister.",
    tags=['election', 'politics'],
    base_w=1.35, profile="election",
    reactions=[
        reaction("declare_era_of_development_and_sushasan", "Declare an era of development, and announce immediate plans to clear highway projects.",
                 ['GOVERNMENT'], eff(3, 0, 4, 5),
                 {},
                 risk(18, "RJD alleges irregularities in EVM transport in three urban districts.", eff(-1, 0, -2, -2)), 1.25),
        reaction("accept_mandate_vow_to_defend_social_justice", "Accept the mandate, stating that RJD will act as a vigilant opposition to protect social justice.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(14, "Local party workers express frustration over losing cabinet influence.", eff(-1, 0, -2, -1)), 1.2),
        reaction("propose_bipartisan_development_council", "Propose forming a bipartisan state development council to recommend highway priorities.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Fierce leader rivalries prevent the council from holding its first meeting.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.15)
    ]
))

# 2005-12
ITEMS_2001_2005.append(make_news(
    key="bh2005_2005_12_buta_singh_row",
    month="2005-12",
    title="NDA Demands Governor Buta Singh Resignation After SC Verdict",
    desc="Following the Supreme Court's detailed verdict on dissolution, the state cabinet and NDA leaders demand the immediate resignation of Governor Buta Singh.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("send_cabinet_memo_to_president_demanding_recall", "Send a formal cabinet memorandum to the President requesting the immediate recall of the Governor.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "UPA allies in Delhi delay action, citing administrative procedures.", eff(0, 0, -2, -1)), 1.2),
        reaction("defend_governor_action_as_preventive", "Defend the Governor's actions, stating he acted to prevent horse-trading and corruption.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "SC verdict details draw critical media coverage, weakening the defense.", eff(0, 0, -2, -2)), 1.2),
        reaction("propose_judicial_standards_for_governors", "Propose that the Inter-State Council adopt standard judicial guidelines for governor appointments.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Lack of consensus among states stalls the guidelines draft in Delhi.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"politicalStabilityMemory": 2}, weight=0.25)
    ]
))

