from helper import reaction, no_comment, make_news, eff, risk

ITEMS_2006_2010 = []

# 2006-01
ITEMS_2006_2010.append(make_news(
    key="rj2006_2006_01_mahindra_sez_jaipur",
    month="2006-01",
    title="Special Economic Zone Cleared Near Jaipur",
    desc="The state government clears land approvals for the Mahindra World City Special Economic Zone (SEZ) near Jaipur, aiming to build IT and manufacturing parks.",
    tags=['economy', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("fast_track_sez_power_and_water", "Fast-track infrastructure connections to the SEZ to attract global software and auto majors.",
                 ['GOVERNMENT'], eff(1, 0, 3, 4),
                 {},
                 risk(12, "Local farmer groups protest, claiming water diversion will dry up rural tube-wells.", eff(0, 0, -2, -1)), 1.2),
        reaction("demand_jobs_guarantee_for_local_district", "Demand that the SEZ developers reserve 50% of assembly and floor jobs for local district youth.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Developers lobby warns that strict quotas will shift investments to other states.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_mass_transit_link_to_sez", "Propose a state-backed Bus Rapid Transit (BRTS) corridor to connect Jaipur city suburbs directly with the SEZ.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "High acquisition costs along highway sectors delay the BRTS launch.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"economyIssueMissed": 1}, weight=0.25)
    ]
))

# 2006-02
ITEMS_2006_2010.append(make_news(
    key="rj2006_2006_02_nregs_rural_launch",
    month="2006-02",
    title="NREGS Launched in Six Backward Districts of Rajasthan",
    desc="The National Rural Employment Guarantee Scheme (NREGS) is launched in six backward districts of Rajasthan, providing 100 days of guaranteed manual wage labor.",
    tags=['governance', 'welfare', 'rural'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("speed_up_job_card_distribution_and_works", "Speed up job card distribution in rural blocks and initiate desiltation works in community ponds.",
                 ['GOVERNMENT'], eff(2, 0, 3, 5),
                 {},
                 risk(15, "Delay in central fund releases causes wage payment backlogs at block offices.", eff(0, 0, -2, -2)), 1.25),
        reaction("demand_expansion_to_all_thirty_two_districts", "Demand that the state government expand the scheme to all districts immediately, citing widespread dryland unemployment.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Central ministry states expansion will proceed in phases, limiting immediate impact.", eff(0, 0, -1, -1)), 1.2),
        reaction("propose_mandatory_panchayat_social_audits", "Propose mandatory social audits of NREGS works by local gram sabhas to prevent muster roll fraud.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 3),
                 {},
                 risk(10, "Panchayat secretaries strike, protesting against audit procedures.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 1}, weight=0.2)
    ]
))

# 2006-03
ITEMS_2006_2010.append(make_news(
    key="rj2006_2006_03_ranthambore_mining_protests",
    month="2006-03",
    title="Protests Over Limestone Mining Near Ranthambore Buffer Zone",
    desc="Environmentalists and local villagers stage protests against limestone mining leases granted near the Ranthambore Tiger Reserve buffer boundary, alleging threat to wildlife.",
    tags=['protest', 'environment'],
    base_w=1.15, profile="protest",
    reactions=[
        reaction("suspend_violating_mining_leases_and_audit", "Suspend all mining leases within 5 km of the reserve boundary and order a fresh satellite boundary audit.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(16, "Mining labor unions strike, protesting against job losses in Sawai Madhopur.", eff(-1, 0, -2, -1)), 1.2),
        reaction("lead_villagers_march_to_mining_office", "Lead a protestors' march to the state mining department office demanding permanent cancellation of leases.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Industrial cement lobbies warning of factory shutdowns receives heavy press.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_eco_sensitive_mining_buffer", "Propose demarcating a statutory 10 km eco-sensitive buffer zone where only low-impact tourism is allowed.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "State cabinet delays buffer zone clearance, citing mining revenue commitments.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 2}, weight=0.25)
    ]
))

# 2006-04
ITEMS_2006_2010.append(make_news(
    key="rj2006_2006_04_alwar_dust_storm",
    month="2006-04",
    title="Severe Dust Storm Damages Mustard Crops in Alwar",
    desc="A severe dust storm and high winds lash northern districts of Alwar and Bharatpur, damaging harvested mustard and standing wheat crops.",
    tags=['disaster_relief', 'rural'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("announce_emergency_crop_loss_allowance", "Announce an emergency crop loss compensation of Rs 2,000 per hectare for affected small-holders.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Survey delays by local patwaris cause protests at district collector offices.", eff(0, 0, -2, -2)), 1.2),
        reaction("demand_complete_revenue_tax_waiver_for_season", "Demand a complete waiver of land revenue taxes and electricity surcharge fees for the current season.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "State board states utility debt limits prevent power surcharge waivers.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_agro_meteorology_warning_cells", "Propose setting up block-level weather warning cells to alert farmers prior to storms.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Lack of weather radars in remote blocks delays warning messages.", eff(0, 0, -1, -1)), 1.05),
        no_comment(hidden={"disasterIgnoredMemory": 2}, weight=0.3)
    ]
))

# 2006-05
ITEMS_2006_2010.append(make_news(
    key="rj2006_2006_05_gurjar_rail_blockades",
    month="2006-05",
    title="Gurjar Agitation Blocks Delhi-Jaipur Railway Lines",
    desc="Gurjar reservation protests flare up. Activists block railway tracks and national highways in Dausa and Karauli, demanding Scheduled Tribe (ST) status.",
    tags=['politics', 'identity', 'protest'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("deploy_security_forces_keep_tracks_open", "Deploy state armed police to keep railway tracks clear and offer talks with Colonel Bainsla.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(18, "Clashes between police and protestors result in track blockades spreading to Bharatpur.", eff(-1, 0, -2, -3)), 1.2),
        reaction("support_gurjar_reservation_demands_in_assembly", "Support the reservation demands, urging the government to pass a bill guaranteeing ST status.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Meena community organizations launch counter-protests, threatening the party's base.", eff(0, 0, -2, -3)), 1.25),
        reaction("propose_nomadic_tribes_quota_subdivision", "Propose creating a new reservation sub-category for Nomadic and Pastoral communities within the state quota.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Nomadic representatives boycotted the proposal, demanding full ST status.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.2)
    ]
))

# 2006-06
ITEMS_2006_2010.append(make_news(
    key="rj2006_2006_06_gurjar_talks_deadlock",
    month="2006-06",
    title="Initial Round of Talks with Gurjar Leaders Ends in Deadlock",
    desc="Secretariat negotiations between Gurjar representatives and state cabinet ministers end in a deadlock. Protestors refuse to vacate highways.",
    tags=['politics', 'protest'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("refuse_illegal_blockades_and_warn_unions", "State that no negotiations will be held under coercion and warn that blockades will face legal action.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(16, "Protestors block additional state highway sectors, isolating eastern districts.", eff(-1, 0, -2, -2)), 1.15),
        reaction("demand_neutral_mediator_and_immediate_talks", "Demand the government appoint a neutral mediator and release all detained activists to restart talks.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "Ruling party accuses the opposition of trying to fuel social unrest.", eff(0, 0, -1, -1)), 1.2),
        reaction("propose_bipartisan_assembly_mediation_panel", "Propose a bipartisan assembly committee representing all communities to mediate the reservation dispute.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Fierce rivalry between leaders prevents the committee from holding its first meet.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2006-07
ITEMS_2006_2010.append(make_news(
    key="rj2006_2006_07_urban_rainwater_mandate",
    month="2006-07",
    title="Rainwater Harvesting Mandate Enforced in Urban Housing",
    desc="The urban development authority enforces rainwater harvesting rules for all houses built on plots over 300 square yards, targeting water table recovery.",
    tags=['governance', 'environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("set_compliance_deadlines_with_penalties", "Set a six-month compliance deadline, warning that municipal water connections will be cut for non-compliance.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Plumbing equipment costs spike, generating complaints in middle-class wards.", eff(0, 0, -2, -2)), 1.2),
        reaction("demand_subsidies_for_slum_housing_RWH", "Demand that the state provide full financial subsidies to low-income households for RWH installations.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Ruling party points out that the rule excludes low-income plots, reducing impact.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_school_volunteer_awareness_drives", "Propose partnering with school science clubs to demonstrate rainwater harvesting designs in neighborhoods.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(8, "Low resident turnout at local ward demonstrations slows down compliance.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2006-08
ITEMS_2006_2010.append(make_news(
    key="rj2006_2006_08_barmer_flash_floods",
    month="2006-08",
    title="Flash Floods Devastate Kawad Village in Desert Barmer",
    desc="Unprecedented torrential rainfall causes flash floods in the desert district of Barmer. Kawad village is submerged, forcing emergency evacuations by boat and helicopter.",
    tags=['disaster_relief', 'rural'],
    base_w=1.25, profile="disaster_relief",
    reactions=[
        reaction("deploy_disaster_teams_and_release_relief", "Deploy emergency disaster response teams, distribute food packets, and release immediate compensation to families.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Relief distribution is delayed by sand dune road collapses, drawing local criticism.", eff(-1, 0, -2, -2)), 1.25),
        reaction("demand_central_famine_and_flood_relief_package", "Demand the state request an emergency central relief package and waive local land revenue taxes.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Central team disputes damage estimates in desert zones, delaying fund release.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_desert_drainage_master_plan", "Propose a drainage master plan to construct concrete outfall channels to divert floodwaters safely.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "High costs of channel excavation in loose sand delay project execution.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2006-09
ITEMS_2006_2010.append(make_news(
    key="rj2006_2006_09_sez_land_corruption",
    month="2006-09",
    title="Opposition Alleges Graft in Mahindra SEZ Land Allotments",
    desc="The opposition Congress holds a press conference, alleging financial irregularities and cronyism in prime land allotments for the Mahindra SEZ near Jaipur.",
    tags=['corruption', 'politics'],
    base_w=1.2, profile="corruption",
    reactions=[
        reaction("defend_allocations_as_compliant_with_rules", "Defend the allotments in assembly, releasing audit files showing compliance with single-window guidelines.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(18, "Media publishes lease reports showing undervalued plots, damaging media image.", eff(-1, -1, -2, -2)), 1.15),
        reaction("demand_cbi_probe_on_industrial_leases", "Demand a CBI investigation and immediate suspension of the industry department head named in reports.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(14, "Chamber of commerce warns that graft campaigns damage state investment climate.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_digitized_land_lease_bidding", "Propose that all future industrial leases be processed through an online public auction portal.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(10, "Software errors in the auction portal delay subsequent project clearances.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"corruptionIgnoredMemory": 2}, weight=0.25)
    ]
))

# 2006-10
ITEMS_2006_2010.append(make_news(
    key="rj2006_2006_10_urban_local_polls",
    month="2006-10",
    title="Municipal Corporation Polls Scheduled in Kota and Udaipur",
    desc="Elections to municipal corporations in Kota and Udaipur are announced. Campaigns focus heavily on urban sewerage systems and electricity tariff rates.",
    tags=['election'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("campaign_on_sewerage_network_expansions", "Campaign on the completion of sewerage networks and the launch of new city bus routes under state funds.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Voters protest over delayed road restoration works after pipe laying.", eff(0, 0, -2, -2)), 1.15),
        reaction("highlight_road_disruptions_and_tax_hikes", "Highlight dug-up roads, delayed projects, and high property taxes in commercial wards.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Ruling party wins Kota mayor seat due to strong local candidate backing.", eff(-1, 0, -1, -1)), 1.25),
        reaction("propose_ward_level_grievance_portals", "Propose launching digital grievance portals for each ward to resolve local civic issues in 7 days.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Lack of staff in ward offices prevents timely resolution of digital complaints.", eff(0, 0, -2, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2006-11
ITEMS_2006_2010.append(make_news(
    key="rj2006_2006_11_bisalpur_pipeline",
    month="2006-11",
    title="Bisalpur-Jaipur Water Pipeline Project Initiated",
    desc="The government lays the foundation stone for the Bisalpur-Jaipur drinking water pipeline project, aiming to transport 360 MLD of water to the parched capital.",
    tags=['governance', 'infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("allocate_funds_and_speed_up_pipeline_laying", "Allocate state infrastructure bonds and set a strict deadline to complete pipeline laying before summers.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(14, "Farmers in Tonk protest, claiming pipeline diversion dries up local irrigation tanks.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_prioritizing_drinking_water_for_tonk", "Demand that the government first secure Tonk's agricultural water needs before piping water to Jaipur.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Jaipur residents criticize the opposition for blocking city drinking water project.", eff(0, 0, -2, -2)), 1.2),
        reaction("propose_water_sharing_treaty_and_audits", "Propose a formal treaty guaranteeing local villages 40% of Bisalpur water during low monsoon years.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Negotiations delay pipeline contract awards by several months.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2006-12
ITEMS_2006_2010.append(make_news(
    key="rj2006_2006_12_barmer_flood_loans",
    month="2006-12",
    title="Government Waives Crop Loan Interest in Flood-hit Barmer",
    desc="To assist recovery in flood-devastated Kawad, the state government waives cooperative bank crop loan interest for all small-holders in Barmer district.",
    tags=['governance', 'welfare', 'rural'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("release_matching_funds_to_rural_cooperatives", "Release matching funds to rural cooperative banks to restore credit lines for the upcoming winter sowing.",
                 ['GOVERNMENT'], eff(2, 0, 3, 5),
                 {},
                 risk(15, "Commercial banks refuse to extend credit, claiming rural defaults are high.", eff(0, 0, -2, -1)), 1.25),
        reaction("demand_full_loan_waiver_for_flood_affected", "Demand that the government waive the principal crop loans too, calling the interest waiver a token gesture.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Finance department cites deficit limits, refusing principal waivers.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_weather_linked_insurance_subsidies", "Propose state subsidies for weather-indexed crop insurance to prevent defaults during climate extremes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Insurance enrollment is delayed by lack of digital land records in remote blocks.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 1}, weight=0.25)
    ]
))

# 2007-01
ITEMS_2006_2010.append(make_news(
    key="rj2007_2007_01_nri_summit_jaipur",
    month="2007-01",
    title="Government Hosts NRI Summit 'Pravasi Rajasthanis' in Jaipur",
    desc="CM Vasundhara Raje hosts a high-profile summit 'Pravasi Rajasthanis' in Jaipur, aiming to secure investment pledges in heritage hotels and IT parks.",
    tags=['economy'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("announce_single_window_incentives_for_nris", "Announce fast-track approvals and tax exemptions for NRI investments in heritage conservation.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(12, "Local merchant groups protest, claiming NRI incentives create unfair competition.", eff(0, 0, -2, -1)), 1.15),
        reaction("demand_focus_on_local_small_industries", "Demand that the government support local micro-industries first instead of offering tax cuts to NRI groups.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Trade chambers criticize the opposition as anti-investment.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_nri_rural_development_trust", "Propose setting up an NRI-backed trust to fund drinking water pipeline projects in ancestral villages.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Trust registration formalities delay project launches by a year.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"economyIssueMissed": 1}, weight=0.3)
    ]
))

# 2007-02
ITEMS_2006_2010.append(make_news(
    key="rj2007_2007_02_bainsla_calls_bandh",
    month="2007-02",
    title="Colonel Bainsla Calls State-wide Bandh Over ST Quota",
    desc="Gurjar leader Colonel Bainsla calls for a state-wide bandh, demanding that the Raje cabinet immediately recommend ST status to the central government.",
    tags=['politics', 'identity', 'protest'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("deploy_police_escorts_ensure_trade_runs", "Deploy police escorts for national highways and appeal to Gurjar groups to join the Chopra committee hearings.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(18, "Protestors block the Agra-Jaipur highway, disrupting cargo transport.", eff(-1, 0, -2, -2)), 1.2),
        reaction("condemn_delay_in_st_recommendations", "Condemn the government's delay in sending the ST recommendation, holding the CM responsible for blockades.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(14, "Meena community organizations warn that supporting the demand will damage relations.", eff(0, 0, -2, -3)), 1.25),
        reaction("propose_inter_community_reconciliation_panel", "Propose setting up a reconciliation panel representing Gurjar and Meena elders to discuss a consensus quota.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Rival group heads refuse to sit together on the panel, stalling the initiative.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.2)
    ]
))

# 2007-03
ITEMS_2006_2010.append(make_news(
    key="rj2007_2007_03_religious_freedom_bill",
    month="2007-03",
    title="Assembly Passes Rajasthan Religious Freedom Bill",
    desc="The Rajasthan Assembly passes the Religious Freedom Bill, prohibiting forcible religious conversions. Christian and Muslim groups raise concerns.",
    tags=['identity', 'politics'],
    base_w=1.2, profile="identity",
    reactions=[
        reaction("defend_bill_as_social_safety_measure", "Defend the bill as a measure to prevent fraudulent conversions of tribal families in southern districts.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Minority organizations hold protest rallies in Jaipur, drawing critical press.", eff(-2, 0, -2, -2)), 1.2),
        reaction("condemn_bill_as_divisive_and_unconstitutional", "Condemn the bill as a divisive and unconstitutional attempt to split tribal communities for vote-bank gains.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Traditionalist voter groups shift away, accusing the party of minority appeasement.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_judicial_clearance_for_conversions", "Propose that conversions be reviewed by a district magistrate-led panel instead of police, to avoid harassment.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Legal experts warn that magistrate review is also unconstitutional, stalling the draft.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.2)
    ]
))

# 2007-04
ITEMS_2006_2010.append(make_news(
    key="rj2007_2007_04_freedom_bill_hc_stay",
    month="2007-04",
    title="Madras HC, wait, High Court Stays Religious Freedom Bill Enforcement",
    desc="The Rajasthan High Court issues an interim stay on the enforcement of the Religious Freedom Bill, sending the draft to the Governor for presidential review.",
    tags=['identity'],
    base_w=1.15, profile="identity",
    reactions=[
        reaction("comply_with_stay_await_presidential_review", "Comply with the stay order, directing local police to suspend active enforcement pending presidential reviews.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(14, "Conservative organizations accuse the government of failing to defend the bill in court.", eff(-1, 0, -1, -1)), 1.15),
        reaction("hail_stay_demand_permanent_withdrawal_of_bill", "Hail the stay and demand the permanent withdrawal of the bill, calling it a blow to communal harmony.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(12, "Traditionalist groups launch pamphlet campaigns criticizing the opposition.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_all_faith_peace_councils", "Propose setting up voluntary all-faith peace councils in tribal zones to discuss social grievances.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Rival religious outfits boycott the councils, continuing local friction.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2007-05
ITEMS_2006_2010.append(make_news(
    key="rj2007_2007_05_patoli_violence",
    month="2007-05",
    title="Violent Clashes and Police Firing in Patoli Claim 15 Lives",
    desc="Gurjar protests turn violent in Patoli as demonstrators clash with police and block national highways. Police firing results in 15 deaths.",
    tags=['security_crisis', 'protest', 'identity'],
    base_w=1.4, profile="security_crisis",
    reactions=[
        reaction("order_judicial_inquiry_deploy_forces", "Order a judicial inquiry, deploy extra paramilitary forces to secure tracks, and invite leaders for talks.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(22, "Gurjar outfits block roads in adjacent districts, isolating Eastern Rajasthan.", eff(-2, 0, -3, -4)), 1.25),
        reaction("condemn_brutal_police_action_demand_resignation", "Condemn the police action as brutal, demand the Home Minister's resignation, and call a state shutdown.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 5),
                 {},
                 risk(15, "Commuter queues and local shutdown losses draw complaints from transport associations.", eff(-1, 0, -2, -1)), 1.3),
        reaction("propose_immediate_interim_compensation_talks", "Propose Rs 5 lakh ex-gratia for victims' families and set up a neutral administrative committee to hold talks.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(12, "Protestors refuse talks until all detained activists are released without charge.", eff(0, 0, -2, -1)), 1.15),
        no_comment(hidden={"securityIgnoredMemory": 4}, weight=0.1)
    ]
))

# 2007-06
ITEMS_2006_2010.append(make_news(
    key="rj2007_2007_06_meena_counter_protests",
    month="2007-06",
    title="Meena Community Counter-Protests Raise Social Tensions",
    desc="Meena community organizations stage counter-rallies opposing Gurjar ST status demands, warning that sharing tribal quotas will dilute existing benefits.",
    tags=['politics', 'identity'],
    base_w=1.3, profile="politics",
    reactions=[
        reaction("appeal_for_social_harmony_reassure_meenas", "Appeal for social harmony, stating that the government will protect the interests of existing ST groups.",
                 ['GOVERNMENT'], eff(2, 0, 2, 3),
                 {},
                 risk(18, "Gurjar leaders accuse the CM of bias, resuming road blockades in Dausa.", eff(-2, 0, -2, -3)), 1.2),
        reaction("condemn_divide_and_rule_policy", "Accuse the ruling party of playing divide-and-rule politics, pitting two backward communities against each other.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Opposition cadres in northern districts split along caste lines, weakening campaigns.", eff(-1, 0, -2, -2)), 1.25),
        reaction("propose_proportional_quota_expansion", "Propose expanding the overall reservation pool and allocating separate sub-quotas to preserve peace.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Supreme Court stays the proposal for exceeding 50% reservation limit.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 3}, weight=0.15)
    ]
))

# 2007-07
ITEMS_2006_2010.append(make_news(
    key="rj2007_2007_07_chopra_committee_setup",
    month="2007-07",
    title="Chopra Committee Set Up to Study Gurjar Quota Claims",
    desc="To defuse ongoing tensions, the state government appoints a committee headed by Jasraj Chopra to study the socio-economic status of Gurjars.",
    tags=['governance', 'politics'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("direct_committee_to_submit_report_early", "Direct the committee to submit its report in three months and appeal to protestors to vacate tracks.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Gurjar leaders reject the committee, calling it a delay tactic to avoid action.", eff(-1, 0, -2, -1)), 1.15),
        reaction("demand_statutory_assembly_bill_instead_of_panel", "Demand that the state cabinet bypass the committee and pass a statutory bill recommending ST status.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Existing ST organizations boycott the party's rallies in Mewar.", eff(0, 0, -2, -2)), 1.2),
        reaction("propose_bipartisan_observer_panel_for_committee", "Propose adding bipartisan MLA observers to the committee to ensure transparency in findings.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Rival parties prioritize seat bargaining over panel observer roles.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2007-08
ITEMS_2006_2010.append(make_news(
    key="rj2007_2007_08_bajra_procurement_protests",
    month="2007-08",
    title="Farmers in Sikar Protest Low Bajra Procurement Prices",
    desc="Farmer organizations block local grain markets in Sikar and Jhunjhunu, protesting against low bajra procurement prices and delayed state purchases.",
    tags=['protest', 'rural'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("raise_procurement_prices_clear_dues", "Announce a 10% hike in state advisory procurement prices and mandate cooperative cash clearances in 7 days.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "State warehouses report storage space depletion, delaying fresh purchases.", eff(0, 0, -2, -2)), 1.25),
        reaction("lead_farmer_dharnas_outside_collectorates", "Lead farmer dharnas outside collectorates, demanding the waiver of local market cess fees for the season.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "District councils report severe revenue losses, slowing down rural road repairs.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_automated_grain_escrow_accounts", "Propose an automated escrow system linking grain sales directly to farmers' bank accounts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Technical integration with rural banks is delayed, leaving payments slow.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 2}, weight=0.25)
    ]
))

# 2007-09
ITEMS_2006_2010.append(make_news(
    key="rj2007_2007_09_sc_buffer_zone_demolition",
    month="2007-09",
    title="SC Orders Removal of Commercial Resorts in Tiger Buffer Zones",
    desc="The Supreme Court directs the state government to demolish all unlicensed commercial resorts operating inside the buffer zones of Ranthambore and Sariska reserves.",
    tags=['governance', 'environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("enforce_demolitions_strictly", "Enforce the demolitions strictly, stating that wildlife protection overrides commercial resort interests.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(16, "Resort owners association files appeals, securing a stay on notices.", eff(-1, 0, -2, -1)), 1.2),
        reaction("demand_focus_on_corporate_hotel_chains", "Demand that the state demolish major corporate hotels first instead of targeting small local homestays.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Local guides union complains that the stay delays tourism jobs, dulling issue.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_eco_tourism_joint_guidelines", "Propose eco-tourism guidelines that allow low-impact heritage hotels while protecting buffers.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Drafting guidelines delays enforcement, allowing violations to remain active.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2007-10
ITEMS_2006_2010.append(make_news(
    key="rj2007_2007_10_chopasni_school_tragedy",
    month="2007-10",
    title="Water Contamination Tragedy at Chopasni School Claims 4 Lives",
    desc="A severe water contamination incident at a residential school in Chopasni, Jodhpur, results in the death of 4 students and hospitalizes over fifty, triggering anger.",
    tags=['security_crisis', 'health_crisis'],
    base_w=1.3, profile="security_crisis",
    reactions=[
        reaction("suspend_school_management_mandate_tank_cleanings", "Order immediate suspension of the school administration, compensate families, and mandate school tank cleaning.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Water supply departments report pipeline leaks near sewer lines, drawing bad press.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_judicial_audit_of_all_residential_schools", "Demand a judicial audit of all government and private residential school sanitation facilities in the state.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Department officials cite lack of inspectors, delaying safety audits by months.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_parents_sanitation_audit_committees", "Propose setting up parents-led sanitation committees in every school to check water quality monthly.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Low parent attendance in initial meetings keeps the audit committees inactive.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"securityIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2007-11
ITEMS_2006_2010.append(make_news(
    key="rj2007_2007_11_cairn_production_wells",
    month="2007-11",
    title="Cairn Energy Begins Drilling Barmer Production Wells",
    desc="Cairn Energy begins drilling the commercial production wells in the Mangala oil field, Barmer. The project plans to start oil delivery by late next year.",
    tags=['economy', 'infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("fast_track_refinery_memorandums", "Fast-track land acquisitions and sign a memorandum of understanding (MoU) with central petroleum bodies for a local refinery.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(14, "Environment ministries raise concerns about refinery emission impact on desert ecosystems.", eff(0, 0, -1, -1)), 1.2),
        reaction("demand_refinery_royalty_guarantees_for_state", "Demand that the state secure 40% royalty shares from central oil revenues before clearing refinery lands.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Oil companies state that high royalty demands make the project unviable.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_refinery_technical_colleges", "Propose setting up a specialized petroleum university in Barmer under joint public-private funding.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "University senate approvals delay the syllabus launch by several terms.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"economyIssueMissed": 1}, weight=0.25)
    ]
))

# 2007-12
ITEMS_2006_2010.append(make_news(
    key="rj2007_2007_12_gehlot_jan_akrosh_yatra",
    month="2007-12",
    title="Congress Launches 'Jan Akrosh Yatra' Against Raje Government",
    desc="Opposition leader Ashok Gehlot launches the 'Jan Akrosh Yatra' across Rajasthan, targeting the Raje government on law and order and Gurjar protests.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("counter_with_suraj_sankalp_yatra", "Counter the opposition march by launching 'Suraj Sankalp' rallies highlighting single-window IT reforms.",
                 ['GOVERNMENT'], eff(2, 0, 2, 3),
                 {},
                 risk(15, "Rebel MLAs continue to hold private meetings demanding a cabinet reshuffle.", eff(-1, 0, -2, -2)), 1.15),
        reaction("intensify_jan_akrosh_rallies", "Intensify the Jan Akrosh rallies in Eastern districts, focusing on police firing casualties in Patoli.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Opposition parties fail to agree on joint candidates in upcoming by-polls.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_bipartisan_campaign_code_of_ethics", "Propose establishing a code of campaign ethics to prevent personal attacks and focus on development.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Rival parties ignore the code, focusing on caste mobilization.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2008-01
ITEMS_2006_2010.append(make_news(
    key="rj2008_2008_01_mustard_frost_damage",
    month="2008-01",
    title="Severe Cold Wave Damages Mustard Crops in North",
    desc="A severe cold wave and ground frost damage mustard and cumin crops in Sriganganagar, Hanumangarh, and Churu. Farmers demand emergency relief.",
    tags=['disaster_relief', 'rural'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("announce_frost_relief_package", "Announce an emergency frost calamity compensation of Rs 3,000 per damaged hectare and waive land revenues.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Survey delays by local patwaris cause protests at district collector offices.", eff(0, 0, -2, -2)), 1.2),
        reaction("demand_complete_crop_loan_waiver", "Demand a complete crop loan waiver and immediate power tariff cuts for tubewell pumping during winter.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Utility board states debt limits prevent power tariff cuts, stalling the idea.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_agro_meteorology_warning_cells", "Propose setting up block-level weather warning cells to alert farmers prior to cold waves.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Lack of weather radars in remote blocks delays warning messages.", eff(0, 0, -1, -1)), 1.05),
        no_comment(hidden={"disasterIgnoredMemory": 2}, weight=0.3)
    ]
))

# 2008-02
ITEMS_2006_2010.append(make_news(
    key="rj2008_2008_02_chopra_report_submission",
    month="2008-02",
    title="Chopra Committee Declines ST Recommendation; Advises Relief",
    desc="The Jasraj Chopra Committee submits its report, declining to recommend ST status for Gurjars but advising special development packages for their villages.",
    tags=['politics', 'identity'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("accept_report_announce_development_package", "Accept the report recommendations and announce a special package of Rs 280 crore for Gurjar-dominated blocks.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(16, "Gurjar leaders reject the package, calling for a fresh state shutdown.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_statutory_assembly_bill_for_st", "Demand that the state government bypass the committee report and pass a statutory bill recommending ST status.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Meena community organizations boycott the party's campaign in Mewar.", eff(0, 0, -2, -2)), 1.2),
        reaction("propose_nomadic_category_subdivision", "Propose creating a new reservation sub-category for Nomadic and Pastoral communities within the state quota.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Nomadic representatives boycotted the proposal, demanding full ST status.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"identityIssueMissed": 1}, weight=0.25)
    ]
))

# 2008-03
ITEMS_2006_2010.append(make_news(
    key="rj2008_2008_03_pilupura_agitation",
    month="2008-03",
    title="Gurjars Launch 'Pilupura' Agitation; Block Agra Highway",
    desc="Gurjar groups led by Colonel Bainsla launch a fresh round of protests in Pilupura, blocking the Jaipur-Agra national highway and rail tracks.",
    tags=['politics', 'identity', 'protest'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("deploy_police_keep_tracks_open", "Deploy state armed police to keep railway tracks clear and offer talks with Colonel Bainsla.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(18, "Clashes between police and protestors result in track blockades spreading to Bharatpur.", eff(-1, 0, -2, -3)), 1.2),
        reaction("support_gurjar_reservation_demands_in_assembly", "Support the reservation demands, urging the government to pass a bill guaranteeing ST status.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Meena community organizations launch counter-protests, threatening the party's base.", eff(0, 0, -2, -3)), 1.25),
        reaction("propose_nomadic_tribes_quota_subdivision", "Propose creating a new reservation sub-category for Nomadic and Pastoral communities within the state quota.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Nomadic representatives boycotted the proposal, demanding full ST status.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.2)
    ]
))

# 2008-04
ITEMS_2006_2010.append(make_news(
    key="rj2008_2008_04_bayana_violence",
    month="2008-04",
    title="Violent Clashes in Bayana Result in 20 Deaths",
    desc="Violent clashes between police and Gurjar protestors in Bayana, Bharatpur district, result in the death of 20 people. A high security alert is declared.",
    tags=['security_crisis', 'protest', 'identity'],
    base_w=1.4, profile="security_crisis",
    reactions=[
        reaction("order_judicial_inquiry_deploy_forces", "Order a judicial inquiry, deploy extra paramilitary forces to secure tracks, and invite leaders for talks.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(22, "Gurjar outfits block roads in adjacent districts, isolating Eastern Rajasthan.", eff(-2, 0, -3, -4)), 1.25),
        reaction("condemn_brutal_police_action_demand_resignation", "Condemn the police action as brutal, demand the Home Minister's resignation, and call a state shutdown.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 5),
                 {},
                 risk(15, "Commuter queues and local shutdown losses draw complaints from transport associations.", eff(-1, 0, -2, -1)), 1.3),
        reaction("propose_immediate_interim_compensation_talks", "Propose Rs 5 lakh ex-gratia for victims' families and set up a neutral administrative committee to hold talks.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(12, "Protestors refuse talks until all detained activists are released without charge.", eff(0, 0, -2, -1)), 1.15),
        no_comment(hidden={"securityIgnoredMemory": 4}, weight=0.1)
    ]
))

# 2008-05
ITEMS_2006_2010.append(make_news(
    key="rj2008_2008_05_jaipur_blasts",
    month="2008-05",
    title="Serial Bomb Blasts Rock Jaipur; 70 Dead",
    desc="Eight serial bomb blasts rock Jaipur's crowded old city zones in fifteen minutes, claiming over 70 lives and injuring hundreds. A red alert is declared.",
    tags=['security_crisis', 'security'],
    base_w=1.45, profile="security_crisis",
    reactions=[
        reaction("deploy_forces_and_announce_special_security_cell", "Deploy state police, announce ex-gratia, and establish a dedicated Anti-Terrorism Squad (ATS) in Jaipur.",
                 ['GOVERNMENT'], eff(3, 0, 3, 4),
                 {},
                 risk(20, "Intelligence gaps lead to delayed arrests of key suspects, drawing critical press.", eff(-1, 0, -2, -3)), 1.25),
        reaction("condemn_government_intelligence_failure", "Condemn the blasts as a major intelligence failure of the Raje government and demand central agency probe.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Public views the criticism as political opportunism during a national tragedy.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_cctv_network_for_old_city", "Propose installing a comprehensive CCTV and wireless security network across all gates of Jaipur old city.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(10, "Technical setup delays keep the CCTV system offline for several months.", eff(0, 0, -2, -1)), 1.15),
        no_comment(hidden={"securityIgnoredMemory": 5}, weight=0.1)
    ]
))

# 2008-06
ITEMS_2006_2010.append(make_news(
    key="rj2008_2008_06_gurjar_pact",
    month="2008-06",
    title="Government Signs Pact Offering 5% Special Quota to Gurjars",
    desc="The state government signs a pact with Gurjar leaders, proposing a new Special Backward Class (SBC) category offering 5% reservation, ending the Bayana protest.",
    tags=['politics', 'identity'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("draft_bill_for_assembly_passage", "Draft a bill incorporating the SBC quota for immediate passage in the monsoon session of the assembly.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Meena community organizations protest, claiming the SBC category will overlap benefits.", eff(-1, 0, -2, -2)), 1.2),
        reaction("label_pact_as_election_compromise", "Label the pact as an election compromise that will fail judicial scrutiny, demanding constitutional solutions.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Gurjar voters welcome the reservation announcement, ignoring the legal debate.", eff(0, 0, -1, -2)), 1.25),
        reaction("propose_bipartisan_legal_audit_of_bill", "Propose a bipartisan committee of legal experts to check if the bill can survive Supreme Court scans.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Fierce rivalry between leaders prevents the committee from agreeing on audit dates.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"identityIssueMissed": 1}, weight=0.2)
    ]
))

# 2008-07
ITEMS_2006_2010.append(make_news(
    key="rj2008_2008_07_sariska_tiger_translocation",
    month="2008-07",
    title="First Translocated Tiger Released in Sariska Reserve",
    desc="To revive the extinct population, the forest department releases the first translocated tiger brought from Ranthambore into the Sariska Tiger Reserve.",
    tags=['governance', 'environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("advertise_revival_success_and_monitor", "Inaugurate the release with media coverage highlighting the state's successful wildlife conservation efforts.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(14, "Radio collar telemetry issues lead to the tiger wandering near local villages, creating panic.", eff(0, 0, -1, -2)), 1.2),
        reaction("demand_village_relocation_funds_first", "Demand that the government first release relocation funds for buffer villages before releasing more predators.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Conservation groups criticize the party for prioritizing relocation disputes over tiger survival.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_joint_village_eco_tourism_guild", "Propose setting up cooperative eco-tourism guides in buffer villages to share tiger tracking profits.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Licensing tests delay guide deployment, keeping villagers without jobs.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2008-08
ITEMS_2006_2010.append(make_news(
    key="rj2008_2008_08_assembly_passes_quota_bill",
    month="2008-08",
    title="Assembly Passes Rajasthan Backward Classes Bill",
    desc="The Rajasthan Assembly passes a bill providing 5% reservation to Gurjars under SBC and 14% to economically backward classes, taking total reservation to 68%.",
    tags=['politics', 'identity'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("enforce_bill_and_request_ninth_schedule", "Enforce the bill immediately and request the central government to place it under the Ninth Schedule of the constitution.",
                 ['GOVERNMENT'], eff(3, 0, 3, 4),
                 {},
                 risk(18, "General category organizations file immediate petitions in High Court challenging the bill.", eff(-1, 0, -2, -2)), 1.2),
        reaction("label_bill_as_unconstitutional_eyewash", "Label the bill as an unconstitutional eyewash designed to mislead voters before upcoming assembly polls.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(14, "Gurjar organizations accuse the opposition of trying to block their reservation benefits.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_bipartisan_legal_coordination_committee", "Propose an all-party committee of MLAs to draft a joint affidavit for defending the bill in court.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Legislative delays prevent the committee from submitting its draft before polls.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"identityIssueMissed": 1}, weight=0.2)
    ]
))

# 2008-09
ITEMS_2006_2010.append(make_news(
    key="rj2008_2008_09_quota_bill_hc_stay",
    month="2008-09",
    title="High Court Stays Implementation of new Reservation Bill",
    desc="The Rajasthan High Court stays the implementation of the new reservation bill, citing Supreme Court rulings on the 50% limit and lack of quantifiable data.",
    tags=['politics', 'law_order'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("instruct_advocate_general_defend", "Instruct the state advocate general to defend the bill, citing the special backward status of dryland families.",
                 ['GOVERNMENT'], eff(1, 0, 2, 3),
                 {},
                 risk(15, "Court stay remains active, drawing protests from Gurjar associations.", eff(-1, 0, -2, -2)), 1.15),
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

# 2008-10
ITEMS_2006_2010.append(make_news(
    key="rj2008_2008_10_assembly_poll_announcement",
    month="2008-10",
    title="Rajasthan Assembly Poll Dates Scheduled",
    desc="The Election Commission announces that the Rajasthan Legislative Assembly elections will be held on December 4, 2008, starting high-intensity campaigns.",
    tags=['election'],
    base_w=1.2, profile="election",
    reactions=[
        reaction("campaign_on_suraj_sankalp_growth", "Campaign on the government's Suraj Sankalp development record, single-window reforms, and tiger revival projects.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Local rebel candidates file nominations in 15 districts, splitting the vote.", eff(-1, 0, -2, -2)), 1.15),
        reaction("highlight_reservation_chaos_and_blasts", "Highlight the reservation agitations, police firing deaths, and security failures during the Jaipur blasts.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 5),
                 {},
                 risk(14, "Seat-sharing adjustments trigger localized protests by disappointed candidates.", eff(-1, 0, -1, -1)), 1.25),
        reaction("propose_webcast_monitoring_sensitive", "Propose requesting the EC to webcast voting in sensitive booths in Eastern districts to prevent rigging.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "EC cites lack of internet lines in remote rural booths, stalling the webcasts.", eff(0, 0, -2, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2008-11
ITEMS_2006_2010.append(make_news(
    key="rj2008_2008_11_campaigns_clash",
    month="2008-11",
    title="Campaigns Reach Fever Pitch Across State",
    desc="Campaigns peak. Raje highlights industrial growth and the new reservation bill, while Gehlot promises stable governance, social security, and peace.",
    tags=['election'],
    base_w=1.25, profile="election",
    reactions=[
        reaction("announce_post_poll_welfare_allowances", "Announce election promises to double monthly old-age pension benefits if voted to power.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Urban voter forums criticize the promise as fiscally irresponsible.", eff(0, 0, -2, -1)), 1.2),
        reaction("highlight_incumbent_failures_on_internal_security", "Focus the campaign entirely on incumbent failures in preventing the Jaipur blasts and managing agitations.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 5),
                 {},
                 risk(12, "Ruling party releases safety audits, claiming quick arrest of blast suspects.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_bipartisan_development_debates", "Propose a series of public debates on state highway upgrades and tourism investment plans.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Opponents decline to attend, turning the debates into empty-chair PR stunts.", eff(-1, 0, -1, -1)), 1.1),
        no_comment(weight=0.2)
    ]
))

# 2008-12
ITEMS_2006_2010.append(make_news(
    key="rj2008_2008_12_gehlot_resumes_cm",
    month="2008-12",
    title="Congress Wins Narrow Majority; Ashok Gehlot Sworn In",
    desc="The Congress wins a narrow majority, securing 96 seats (supported by independents). Ashok Gehlot is sworn in as the Chief Minister of Rajasthan for his second term.",
    tags=['election', 'politics'],
    base_w=1.35, profile="election",
    reactions=[
        reaction("declare_social_security_agenda", "Declare a social security agenda, launching immediate audits of NREGS works in rural blocks.",
                 ['GOVERNMENT'], eff(3, 0, 3, 4),
                 {},
                 risk(18, "Opposition claims the government is built on opportunism, demanding a floor test.", eff(-1, 0, -2, -2)), 1.25),
        reaction("accept_mandate_reorganise_district_panels", "Accept the mandate, reorganise the district party panels, and vow to audit the new government's spendings.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "Dissident leaders in the party hold private meetings, demanding leadership changes.", eff(-1, 0, -2, -1)), 1.2),
        reaction("propose_bipartisan_water_grid_bill", "Propose an all-party assembly bill to establish a state-wide drinking water pipeline grid.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Utility cabinet disputes delay the drafting of the water grid bill.", eff(0, 0, -1, -1)), 1.15),
        no_comment(weight=0.15)
    ]
))

# 2009-01
ITEMS_2006_2010.append(make_news(
    key="rj2009_2009_01_mgnrega_social_audits",
    month="2009-01",
    title="Government Launches MGNREGA Social Audits in Rural Blocks",
    desc="The state government launches systematic social audits of all MGNREGA works in rural blocks, partnering with civil rights groups to check corruption.",
    tags=['governance', 'welfare', 'rural'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("publish_audit_findings_online", "Publish all audit findings online and black-list corrupt rural contractors immediately.",
                 ['GOVERNMENT'], eff(2, -1, 4, 4),
                 {},
                 risk(15, "Panchayat secretaries strike, protesting against NGO involvement in audits.", eff(-1, 0, -2, -1)), 1.2),
        reaction("demand_cbi_probe_on_muster_roll_fraud", "Demand a CBI investigation into muster roll fraud, claiming senior department heads are involved.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, -1, 4, 3),
                 {},
                 risk(12, "Local labor unions complain that audits delay current week wages, drawing criticism.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_biometric_labor_attendance", "Propose introducing biometric attendance systems at all rural MGNREGA works to prevent fraud.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 3),
                 {},
                 risk(10, "Lack of cellular signals in desert blocks delays biometric uploads.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 1}, weight=0.25)
    ]
))

# 2009-02
ITEMS_2006_2010.append(make_news(
    key="rj2009_2009_02_cheap_wheat_scheme",
    month="2009-02",
    title="Cheap Wheat Scheme Expanded for BPL Families",
    desc="The state government expands the cheap food grain scheme, providing wheat at Rs 2 per kg under the public distribution system for BPL families.",
    tags=['governance', 'welfare'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("expand_scheme_to_include_marginal_farmers", "Expand the scheme to include all marginal farmers in drought-affected blocks.",
                 ['GOVERNMENT'], eff(2, 0, 3, 5),
                 {},
                 risk(15, "Grain procurement shortages lead to long queues at rural ration shops.", eff(0, 0, -2, -2)), 1.25),
        reaction("demand_free_sugar_and_oil_ration_instead", "Demand that the government distribute free cooking sugar and oil too, calling the cheap wheat partial.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Rural families welcome the cheap wheat, ignoring the extra demand.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_cooperative_ration_shops_run_by_women", "Propose hand-over of ration shops to women self-help groups to reduce middleman corruption.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "SHGs report lack of storage facilities, slowing down grain deliveries.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 1}, weight=0.25)
    ]
))

# 2009-03
ITEMS_2006_2010.append(make_news(
    key="rj2009_2009_03_ls_campaigns",
    month="2009-03",
    title="Lok Sabha Campaigns Begin Across Rajasthan",
    desc="With the general election announced, campaigns peak. Congress highlights rural welfare audits, while BJP targets central inflation and security.",
    tags=['election'],
    base_w=1.2, profile="election",
    reactions=[
        reaction("announce_post_poll_farmers_pension_grants", "Announce election promises to introduce a pension scheme for old-age small-holders if voted to power.",
                 ['GOVERNMENT'], eff(1, 0, 2, 3),
                 {},
                 risk(15, "Taxpayer forums write critical columns warning of deficit hikes.", eff(0, 0, -2, -1)), 1.15),
        reaction("campaign_on_incumbent_welfare_failures", "Campaign aggressively on delays in NREGS wage releases and the rise in food inflation.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Ruling party releases audit logs, proving high NREGS employment rates.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_bipartisan_irrigation_manifesto", "Propose drafting a joint water resources manifesto for the state to appeal to desert farmers.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Differences on canal priorities delay the manifesto draft.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2009-04
ITEMS_2006_2010.append(make_news(
    key="rj2009_2009_04_mount_abu_eco_zone",
    month="2009-04",
    title="Mount Abu Declared Eco-Sensitive Zone by Union Ministry",
    desc="The Union Environment Ministry declares Mount Abu an eco-sensitive zone, halting all new commercial hotel constructions and mining leases in the region.",
    tags=['governance', 'environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("enforce_eco_zone_guidelines_strictly", "Enforce the eco-zone guidelines strictly, setting up a state eco-monitoring cell in Sirohi district.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(15, "Hotel and tourism associations strike, protesting against the ban on expansions.", eff(-1, 0, -2, -1)), 1.2),
        reaction("demand_compensation_for_local_hotel_staff", "Demand that the state provide financial assistance to local hotel staff laid off due to project freezes.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Eco-groups criticize the opposition for defending commercial lobbies.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_low_impact_eco_tourism_charter", "Propose a charter allowing low-impact home-stays run by local communities within the zone.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Drafting the charter guidelines delays implementation, allowing violations to continue.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2009-05
ITEMS_2006_2010.append(make_news(
    key="rj2009_2009_05_lok_sabha_results_landslide",
    month="2009-05",
    title="Congress Wins 20 Lok Sabha Seats in Rajasthan Landslide",
    desc="The Lok Sabha election results show a landslide victory for the Congress in Rajasthan, winning 20 out of 25 seats, while the BJP is reduced to 4 seats.",
    tags=['election', 'politics'],
    base_w=1.3, profile="election",
    reactions=[
        reaction("declare_victory_and_negotiate_central_funds", "Celebrate the victory, and negotiate central funds for the Barmer refinery project.",
                 ['GOVERNMENT'], eff(3, 0, 3, 4),
                 {},
                 risk(18, "Opposition claims the win was due to administrative bias and cash distribution.", eff(-1, 0, -2, -2)), 1.2),
        reaction("reorganise_opposition_district_committees", "Reorganise the state party executive panels, focusing on building candidate bases in northern districts.",
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

# 2009-06
ITEMS_2006_2010.append(make_news(
    key="rj2009_2009_06_bisalpur_pipeline_completed",
    month="2009-06",
    title="Bisalpur-Jaipur Water Pipeline Completed; Water Reaches City",
    desc="The Bisalpur-Jaipur drinking water pipeline is successfully completed. Water reaches the municipal distribution lines in southern Jaipur, easing scarcity.",
    tags=['governance', 'infrastructure'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("inaugurate_with_media_coverage", "Inaugurate the pipeline with extensive media coverage, highlighting the government's ability to deliver key projects.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Minor pipeline leaks in industrial zones delay water delivery to homes.", eff(0, 0, -1, -1)), 1.2),
        reaction("demand_cag_audit_of_pipeline_costs", "Demand a CAG audit of the pipeline construction costs, alleging financial irregularities in emergency pipe tenders.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 3),
                 {},
                 risk(12, "Public welcomes the regular water supply, ignoring the graft charges.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_water_grid_expansion_to_rural", "Propose expanding the pipeline grid to rural villages along the pipeline route in Tonk district.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "High costs keep construction works slow in downstream blocks.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2009-07
ITEMS_2006_2010.append(make_news(
    key="rj2009_2009_07_drought_declared_26_districts",
    month="2009-07",
    title="Severe Drought Declared in 26 Districts of Rajasthan",
    desc="Following prolonged rain deficits, the state government declares 26 out of 33 districts as drought-affected. Calamity relief works are initiated.",
    tags=['disaster_relief', 'rural'],
    base_w=1.25, profile="disaster_relief",
    reactions=[
        reaction("launch_relief_works_and_cattle_camps", "Launch emergency rural desiltation works under NREGS and provide cash subsidies to cattle camps.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Delayed wage releases cause protests at block offices in Western districts.", eff(-1, 0, -2, -2)), 1.25),
        reaction("demand_central_drought_flood_package", "Demand the central government send a team and release an emergency relief package of Rs 1,000 crore.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(10, "Central team delays visit, leaving farmers to wait for relief.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_drip_irrigation_subsidies_drought", "Propose providing 80% subsidies for drip irrigation systems to adapt to dry farming patterns.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Farmers find system cost high even with subsidies, leading to low takeup.", eff(0, 0, -2, -1)), 1.15),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2009-08
ITEMS_2006_2010.append(make_news(
    key="rj2009_2009_08_barmer_oil_production",
    month="2009-08",
    title="Cairn Starts Commercial Oil Production from Barmer",
    desc="PM Manmohan Singh and CM Ashok Gehlot inaugurate commercial oil production from Cairn Energy's Mangala field in Barmer, marking a milestone.",
    tags=['economy', 'infrastructure'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("promote_investment_in_local_allied_units", "Promote investment in local oil field service industries and declare tax holidays for local setups.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Local landholders file cases demanding higher value for refinery lands.", eff(0, 0, -1, -2)), 1.2),
        reaction("demand_statutory_refinery_memorandum_with_hpc", "Demand that the state sign a binding treaty with HPCL for the refinery before piping crude away.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Refinery feasibility report updates delay the draft treaty by a year.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_barmer_petroleum_university", "Propose establishing a specialized petroleum university in Barmer under joint public-private funding.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "University senate approvals delay the syllabus launch by several terms.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"economyIssueMissed": 1}, weight=0.25)
    ]
))

# 2009-09
ITEMS_2006_2010.append(make_news(
    key="rj2009_2009_09_jaipur_ioc_fire",
    month="2009-09",
    title="Devastating Fire at Jaipur IOC Depot Claims 12 Lives",
    desc="A massive fire breaks out at the Indian Oil Corporation (IOC) depot terminal near Jaipur, burning for several days and forcing the evacuation of nearby zones.",
    tags=['security_crisis'],
    base_w=1.35, profile="security_crisis",
    reactions=[
        reaction("deploy_disaster_teams_order_safety_audit", "Deploy emergency teams, announce compensation, and order a state-wide safety audit of all fuel depots.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Depot managers cite central jurisdiction, delaying safety audits by several months.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_relocation_of_depot_away_from_residential", "Demand the immediate relocation of the fuel depot away from residential zones and stage protests.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Relocation cost estimates are high, leaving the demand unfulfilled for years.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_joint_safety_regulatory_board", "Propose a joint board representing state pollution control and central oil safety officers to monitor depots.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Inter-departmental coordination delays prevent board meetings, slowing progress.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"securityIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2009-10
ITEMS_2006_2010.append(make_news(
    key="rj2009_2009_10_teacher_transfers",
    month="2009-10",
    title="Rural Teachers Protest Demanding Home Transfers",
    desc="Thousands of primary school teachers in rural blocks stage dharnas, demanding a transparent online transfer policy to move to their home districts.",
    tags=['protest'],
    base_w=1.15, profile="protest",
    reactions=[
        reaction("launch_digital_transfer_portal", "Launch a digital portal for merit-based transfers and process the first round of transfers online.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Allegations of portal server glitches trigger protests in Jodhpur.", eff(0, 0, -2, -2)), 1.2),
        reaction("demand_allowance_hikes_for_rural_service", "Demand that teachers serving in desert blocks receive a 20% salary allowance hike as rural incentive.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Finance department cites budget limits, refusing rural salary hikes.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_bipartisan_transfer_norms_committee", "Propose a bipartisan committee of MLAs and teacher union representatives to draft new transfer guidelines.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing prevents the committee from finalizing the guidelines.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2009-11
ITEMS_2006_2010.append(make_news(
    key="rj2009_2009_11_balotra_dyeing_closures",
    month="2009-11",
    title="High Court Orders Closure of Balotra Dyeing Units",
    desc="The Rajasthan High Court directs the closure of all unlicensed textile dyeing units in Balotra that discharge chemical effluents into the Luni river.",
    tags=['governance', 'land_rights'],
    base_w=1.2, profile="land_rights",
    reactions=[
        reaction("implement_closures_and_tender_treatment_plants", "Implement the closures strictly and announce state loans for setting up advanced treatment plants.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Textile workers unions strike, protesting against job losses in Balotra.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_welfare_package_for_displaced_workers", "Demand that the state government provide immediate monthly cash assistance to displaced textile workers.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Finance department claims budget limits, refusing to issue cash payouts.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_common_treatment_plant_subsidies", "Propose state subsidies for establishing Common Effluent Treatment Plants (CETPs) in textile zones.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Construction of CETPs is delayed by land dispute clearances.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 2}, weight=0.2)
    ]
))

# 2009-12
ITEMS_2006_2010.append(make_news(
    key="rj2009_2009_12_janani_suraksha_launch",
    month="2009-12",
    title="Janani Shishu Suraksha Welfare Scheme Launched",
    desc="The state government launches the Janani Shishu Suraksha scheme, providing free transport and medicines to pregnant women in rural government hospitals.",
    tags=['governance', 'welfare'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("expand_scheme_with_nutritional_kits", "Expand the scheme by providing free nutritional kits (dry fruits and soy) to mothers post-delivery.",
                 ['GOVERNMENT'], eff(2, 0, 3, 5),
                 {},
                 risk(15, "Substandard kit supply reports in two districts draw critical local press.", eff(-1, -1, -2, -2)), 1.25),
        reaction("demand_upgrades_to_rural_primary_health", "Demand that state funds be spent upgrading rural primary health centers first, calling the kits a token.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Rural families welcome the free transport, ignoring the health center critique.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_midwife_training_programs", "Propose training village midwives as certified health guides to assist rural home-deliveries.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Medical associations protest the certification, citing safety concerns.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 1}, weight=0.25)
    ]
))

# 2010-01
ITEMS_2006_2010.append(make_news(
    key="rj2010_2010_01_jaipur_corporation_polls",
    month="2010-01",
    title="Municipal corporation elections in Jaipur and Jodhpur",
    desc="Elections to municipal corporations in Jaipur and Jodhpur are held. The Congress wins majorities, securing the mayoral posts.",
    tags=['election'],
    base_w=1.2, profile="election",
    reactions=[
        reaction("announce_special_sewerage_grants_for_mayors", "Announce special sewerage and road development grants for the new municipal councils.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Local citizen forums protest over frequent water cuts during summer months.", eff(0, 0, -2, -2)), 1.15),
        reaction("highlight_delayed_road_widening_projects", "Highlight delayed road widening projects and high house taxes in commercial wards.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Ruling party wins Jodhpur mayor seat, reducing opposition campaign impact.", eff(-1, 0, -1, -1)), 1.25),
        reaction("propose_ward_grievance_portals", "Propose launching digital grievance portals for each ward to resolve local civic issues in 7 days.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Lack of staff in ward offices prevents timely resolution of digital complaints.", eff(0, 0, -2, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2010-02
ITEMS_2006_2010.append(make_news(
    key="rj2010_2010_02_cumin_frost_damage",
    month="2010-02",
    title="Frost Damage to Cumin and Coriander Crops in West",
    desc="Severe ground frost damages standing cumin and coriander crops in Jaisalmer and Barmer. Farmers demand state calamity relief.",
    tags=['disaster_relief', 'rural'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("announce_cumin_calamity_compensation", "Announce an emergency compensation of Rs 4,000 per damaged hectare and waive current crop loan interest.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Survey delays by local patwaris cause protests at district collector offices.", eff(0, 0, -2, -2)), 1.2),
        reaction("demand_complete_crop_loan_waiver_for_ cumin", "Demand a complete crop loan waiver and immediate power tariff cuts for tubewell pumping during winter.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Utility board states debt limits prevent power tariff cuts, stalling the idea.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_agro_meteorology_warning_cells_cumin", "Propose setting up block-level weather warning cells to alert farmers prior to cold waves.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Lack of weather radars in remote blocks delays warning messages.", eff(0, 0, -1, -1)), 1.05),
        no_comment(hidden={"disasterIgnoredMemory": 2}, weight=0.3)
    ]
))

# 2010-03
ITEMS_2006_2010.append(make_news(
    key="rj2010_2010_03_gurjar_fresh_protests",
    month="2010-03",
    title="Gurjars Call for Fresh Agitation Over Reservation Delay",
    desc="Alleging slow implementation of the proposed 5% SBC quota, Gurjar organizations call for a fresh mobilization of youth in Eastern districts.",
    tags=['politics', 'identity', 'protest'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("promise_sub_classification_in_assembly", "Promise to introduce a sub-classification model in the assembly and set up a state backward commission cell.",
                 ['GOVERNMENT'], eff(2, 0, 2, 3),
                 {},
                 risk(15, "Meena community organizations warn of counter-protests, opposing any ST quota split.", eff(-1, 0, -2, -3)), 1.15),
        reaction("demand_immediate_gazette_notification_of_quota", "Demand that the state government immediately issue the gazette notification of the 5% SBC quota.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Existing ST organizations boycott the party's campaign in Mewar.", eff(0, 0, -2, -2)), 1.2),
        reaction("propose_special_backward_classes_scholarships", "Propose high-value educational scholarships for SBC students while waiting for court clearances.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Students organizations protest the shift, demanding guaranteed jobs.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 1}, weight=0.25)
    ]
))

# 2010-04
ITEMS_2006_2010.append(make_news(
    key="rj2010_2010_04_cbse_syllabus_transition",
    month="2010-04",
    title="Government Schools Transition to CBSE Syllabus Format",
    desc="The state education department announces that all government secondary schools will transition to a curriculum matching the CBSE format, using NCERT books.",
    tags=['governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("distribute_free_ncert_textbooks", "Distribute free NCERT textbooks to all government school children on the first day of the term.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Matriculation schools challenge the textbook content in court, seeking guide permissions.", eff(0, 0, -2, -2)), 1.2),
        reaction("expose_historical_errors_in_new_textbooks", "Expose instances of historical errors and praise of political leaders in the new textbooks, demanding revisions.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Education department issues corrigendum slips, neutralizing the textbook controversy.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_teacher_training_grants_cbse", "Propose state training grants for teachers to adapt to the new curriculum formats.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(8, "Training center schedules overlap with exam terms, reducing attendance.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2010-05
ITEMS_2006_2010.append(make_news(
    key="rj2010_2010_05_pali_water_trains",
    month="2010-05",
    title="Summer Scarcity: Water Trains Resumed to Pali",
    desc="Drinking water sources in Pali district dry up completely. The state government resumes running special water trains from Jodhpur to meet local needs.",
    tags=['disaster_relief', 'infrastructure'],
    base_w=1.2, profile="disaster_relief",
    reactions=[
        reaction("allocate_funds_and_speed_up_pipeline_laying_pali", "Allocate state infrastructure bonds and set a strict deadline to complete pipeline laying before summers.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(14, "Farmers in Jodhpur protest, claiming pipeline diversion dries up local irrigation tanks.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_waiving_of_municipal_water_cess_pali", "Demand the state government waive the municipal water cess for all households in drought-declared districts.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Municipal corporations report severe revenue shortage, slowing down pipe repairs.", eff(0, 0, -2, -2)), 1.2),
        reaction("propose_stepwell_recharge_pali", "Propose a massive project to clean and link historical stepwells to the city emergency supply lines.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "High contamination in stepwells requires intensive filtration, delaying supplies.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.25)
    ]
))

# 2010-06
ITEMS_2006_2010.append(make_news(
    key="rj2010_2010_06_rural_colleges_proposal",
    month="2010-06",
    title="Cabinet Clears Proposal for New Rural Colleges",
    desc="The state cabinet clears a proposal to establish 15 new government degree colleges in rural blocks, aiming to improve access to higher education for youth.",
    tags=['governance', 'education'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("allocate_land_and_start_infrastructure_colleges", "Allocate land in rural blocks and release initial budget grants to construct the college administrative blocks.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Student unions in other cities protest, demanding university headquarters split.", eff(0, 0, -1, -1)), 1.2),
        reaction("demand_priority_for_polytechnics_first", "Demand that state funds be spent on rural polytechnics first instead of creating centralized colleges.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Rural citizens welcome the colleges, criticizing the opposition's stance.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_vocational_curriculum_sync", "Propose aligning the college curriculum with local industries to ensure direct placements.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Private curriculum sync takes months of board approval, delaying syllabus launch.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2010-07
ITEMS_2006_2010.append(make_news(
    key="rj2010_2010_07_rajsamand_mining_clearances",
    month="2010-07",
    title="Marble Mining Leases Stalled Over Forest Clearances",
    desc="Over 200 marble mining leases in Rajsamand are stalled following new guidelines from the state forest department demanding detailed wildlife impact clearances.",
    tags=['governance', 'environment'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("enforce_guidelines_strictly", "Enforce the clearances strictly, stating that environmental protection is vital for Rajsamand ecosystems.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(16, "Marble mining labor unions strike, protesting against job losses in Rajsamand.", eff(-1, 0, -2, -1)), 1.2),
        reaction("demand_welfare_package_for_displaced_miners", "Demand that the state government provide immediate monthly cash assistance to displaced miners.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Finance department claims budget limits, refusing to issue cash payouts.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_common_environmental_audit_subsidies", "Propose state subsidies for conducting collective environmental audits to speed up clearances.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Construction of audit zones is delayed by land dispute clearances.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2010-08
ITEMS_2006_2010.append(make_news(
    key="rj2010_2010_08_child_marriage_campaign",
    month="2010-08",
    title="State-wide Campaign Against Child Marriage Launched",
    desc="The government launches a state-wide legal and social campaign against child marriages, targeting high-incidence blocks during Akshaya Tritiya.",
    tags=['governance', 'identity'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("enforce_penalties_on_clerics_and_parents", "Enforce strict penalties on clerics, printers of invitation cards, and parents involved in child marriages.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Rural community leaders protest, claiming the campaign harasses families during festivals.", eff(-2, 0, -2, -2)), 1.2),
        reaction("demand_focus_on_girls_higher_education_subsidies", "Demand that the government focus on girls' higher education subsidies, calling the penal campaign superficial.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(12, "Educational department delays scholarship distributions, neutralizing the critique.", eff(0, 0, -1, -1)), 1.2),
        reaction("propose_community_pledge_programs", "Propose organizing voluntary community pledge programs in panchayats to delay marriages.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Low volunteer participation in sensitive blocks keeps the programs inactive.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 1}, weight=0.25)
    ]
))

# 2010-09
ITEMS_2006_2010.append(make_news(
    key="rj2010_2010_09_canal_water_pollution",
    month="2010-09",
    title="Hanumangarh Farmers Protest Indira Gandhi Canal Pollution",
    desc="Farmers in Hanumangarh stage protests, alleging that chemical and industrial waste discharged from Punjab factories is contaminating Indira Gandhi Canal water.",
    tags=['protest', 'land_rights', 'environment'],
    base_w=1.2, profile="land_rights",
    reactions=[
        reaction("raise_pollution_issue_with_punjab_govt", "Send a high-level ministerial delegation to Punjab to demand immediate sealing of polluting factory lines.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Punjab factories dispute the pollution source, delaying any corrective action.", eff(0, 0, -1, -2)), 1.15),
        reaction("lead_farmers_border_sit_in_punjab", "Lead a farmers' border sit-in, demanding that the central government intervene to stop water contamination.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "State border police arrests protestors to prevent inter-state clashes.", eff(-1, 0, -1, -2)), 1.25),
        reaction("propose_canal_water_treatment_plants", "Propose constructing water treatment plants at canal entry points to filter water before municipal distribution.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "High construction costs of treatment plants delay the project by a year.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 2}, weight=0.25)
    ]
))

# 2010-10
ITEMS_2006_2010.append(make_news(
    key="rj2010_2010_10_gurjar_pilupura_blockade",
    month="2010-10",
    title="Gurjars Resume Agitation in Pilupura; Block Rail Tracks",
    desc="Gurjar protestors block railway tracks in Pilupura, Bharatpur district, demanding the immediate implementation of the 5% reservation under SBC.",
    tags=['politics', 'identity', 'protest'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("deploy_police_keep_tracks_open_pilupura", "Deploy state armed police to keep railway tracks clear and offer talks with Colonel Bainsla.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(18, "Clashes between police and protestors result in track blockades spreading to Dausa.", eff(-1, 0, -2, -3)), 1.2),
        reaction("support_gurjar_reservation_demands_in_assembly_pilupura", "Support the reservation demands, urging the government to pass a bill guaranteeing SBC status.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Meena community organizations launch counter-protests, threatening the party's base.", eff(0, 0, -2, -3)), 1.25),
        reaction("propose_nomadic_tribes_quota_subdivision_pilupura", "Propose creating a new reservation sub-category for Nomadic and Pastoral communities within the state quota.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Nomadic representatives boycotted the proposal, demanding full ST status.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.2)
    ]
))

# 2010-11
ITEMS_2006_2010.append(make_news(
    key="rj2010_2010_11_gurjar_bainsla_talks",
    month="2010-11",
    title="Government Initiates Talks with Colonel Bainsla in Bayana",
    desc="The state government sends a senior ministerial team to hold talks with Gurjar leader Colonel Bainsla in Bayana to resolve the railway blockade.",
    tags=['politics', 'protest'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("propose_sub_classification_in_assembly", "Promise to introduce a sub-classification model in the assembly and set up a state backward commission cell.",
                 ['GOVERNMENT'], eff(2, 0, 2, 3),
                 {},
                 risk(15, "Meena community organizations warn of counter-protests, opposing any ST quota split.", eff(-1, 0, -2, -3)), 1.15),
        reaction("demand_immediate_gazette_notification_of_quota_bainsla", "Demand that the state government immediately issue the gazette notification of the 5% SBC quota.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Existing ST organizations boycott the party's campaign in Mewar.", eff(0, 0, -2, -2)), 1.2),
        reaction("propose_special_backward_classes_scholarships_bainsla", "Propose high-value educational scholarships for SBC students while waiting for court clearances.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Students organizations protest the shift, demanding guaranteed jobs.", eff(0, 0, -2, -1)), 1.15),
        no_comment(weight=0.3)
    ]
))

# 2010-12
ITEMS_2006_2010.append(make_news(
    key="rj2010_2010_12_monsoon_floods_east",
    month="2010-12",
    title="Unseasonal Winter Rains Damage standing Crops in East",
    desc="Unseasonal heavy winter rains damage standing mustard and wheat crops in Bharatpur and Alwar districts. Farmers demand immediate relief.",
    tags=['disaster_relief', 'rural'],
    base_w=1.2, profile="disaster_relief",
    reactions=[
        reaction("announce_per_acre_compensation_east", "Announce an emergency compensation of Rs 10,000 per damaged acre and waive current crop loans.",
                 ['GOVERNMENT'], eff(2, 0, 3, 5),
                 {},
                 risk(15, "Revenue surveyors take weeks to measure damaged plots, stalling payouts.", eff(0, 0, -2, -2)), 1.25),
        reaction("demand_central_drought_flood_package_east", "Demand the central government send a team and release an emergency relief package of Rs 500 crore.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(10, "Central team delays visit, leaving farmers to wait for relief.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_canal_embankment_strengthening_east", "Propose a long-term engineering project to raise and reinforce embankments along feeder canals.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "High project cost keeps construction works slow in downstream blocks.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.3)
    ]
))

