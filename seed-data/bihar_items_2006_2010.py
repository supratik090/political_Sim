from helper import reaction, no_comment, make_news, eff, risk

ITEMS_2006_2010 = []

# 2006-01
ITEMS_2006_2010.append(make_news(
    key="bh2006_2006_01_nitish_audits",
    month="2006-01",
    title="New State Cabinet Orders Audits of Prior Welfare Schemes",
    desc="The newly sworn-in JD(U)-BJP state cabinet orders direct audits of all welfare schemes, cooperative loans, and road projects sanctioned under prior regimes.",
    tags=['governance', 'corruption'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("launch_vigilance_probes", "Launch vigilance department probes against suspected contractors and freeze pending payments.",
                 ['GOVERNMENT'], eff(2, -1, 3, 3),
                 {},
                 risk(16, "Contractor associations strike, halting minor maintenance works across cities.", eff(-1, 0, -2, -1)), 1.2),
        reaction("label_audits_as_political_vendetta", "Label the audits as a political vendetta aimed at slandering RJD leaders before local polls.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Audit teams expose registry anomalies in two blocks, weakening the defense.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_independent_auditing_panel", "Propose hiring an independent national agency to conduct state audits to ensure transparency.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Auditing board setup delays keep the investigative reports pending.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"corruptionIgnoredMemory": 2}, weight=0.25)
    ]
))

# 2006-02
ITEMS_2006_2010.append(make_news(
    key="bh2006_2006_02_womens_reservation",
    month="2006-02",
    title="Government Announces 50% Women's Reservation in Panchayats",
    desc="In a historic move, Chief Minister Nitish Kumar announces a cabinet decision to reserve 50% of all Panchayati Raj seats for women candidates in Bihar.",
    tags=['politics', 'welfare'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("enforce_women_reservation_rules", "Enforce the reservation rules and organize district-wide training camps for women sarpanch candidates.",
                 ['GOVERNMENT'], eff(3, 0, 4, 5),
                 {},
                 risk(15, "Opposition claims male relatives will continue to act as proxy decision makers.", eff(0, 0, -2, -2)), 1.25),
        reaction("demand_sub_quotas_for_backward_class_women", "Demand dedicated sub-quotas for EBC and Dalit women within the 50% reservation pool.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Ruling party points to existing caste reservations, reducing impact of criticism.", eff(0, 0, -1, -1)), 1.2),
        reaction("propose_women_empowerment_charter", "Propose an all-party charter to dedicate 30% of village development funds exclusively to women's welfare.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Village council disputes prevent the consensus charter from being implemented.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 1}, weight=0.2)
    ]
))

# 2006-03
ITEMS_2006_2010.append(make_news(
    key="bh2006_2006_03_panchayat_preparations",
    month="2006-03",
    title="Panchayat Election Campaigns Focus on Women Candidates",
    desc="With local body polls scheduled, campaigns heat up in rural wards. Political parties focus on mobilizing rural women candidates for reserved seats.",
    tags=['election'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("campaign_on_women_empowerment_achievements", "Campaign on the government's historic reservation, calling it a social silent revolution.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Opposition highlights poor conditions of rural primary schools and roads.", eff(0, 0, -2, -2)), 1.15),
        reaction("highlight_administrative_neglect_in_villages", "Highlight that despite reservations, rural panchayats lack basic office spaces and funds.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Voters welcome the women reservation benefits, reducing opposition impact.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_bipartisan_polling_peace_panels", "Propose forming cross-party district committees to monitor polling booths on election day.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Clashes between student wings outside booths lead to localized delays.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2006-04
ITEMS_2006_2010.append(make_news(
    key="bh2006_2006_04_bicycle_scheme",
    month="2006-04",
    title="Government Launches Balika Cycle Yojana For Schoolgirls",
    desc="The Bihar government launches the Mukhyamantri Balika Cycle Yojana, providing a cash grant of Rs 2,000 directly to schoolgirls to purchase bicycles.",
    tags=['governance', 'welfare'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("rollout_direct_cycle_grants", "Rollout the grants directly through bank drafts at school events and monitor registrations.",
                 ['GOVERNMENT'], eff(3, 0, 4, 5),
                 {},
                 risk(18, "Reports of local bicycle retailers inflating prices draw newspaper criticism.", eff(-1, 0, -2, -2)), 1.25),
        reaction("demand_distribution_of_actual_cycles", "Demand the state distribute actual bicycles instead of cash, alleging that cash is spent on other needs.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Logistical costs of storage and transit delay cycle delivery by six months.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_school_transit_security", "Propose constructing dedicated bicycle stands and deploying road safety guards along rural school routes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Lack of police staff prevents regular route security patrols in remote blocks.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 1}, weight=0.2)
    ]
))

# 2006-05
ITEMS_2006_2010.append(make_news(
    key="bh2006_2006_05_panchayat_results",
    month="2006-05",
    title="Record Number of Women Candidates Win Panchayat Elections",
    desc="Panchayat poll results are declared, showing that women candidates have won over 50% of the seats, altering rural leadership profiles.",
    tags=['election', 'politics'],
    base_w=1.2, profile="election",
    reactions=[
        reaction("declare_victory_of_silent_revolution", "Declare this as the victory of sushasan, and announce immediate capacity building workshops.",
                 ['GOVERNMENT'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Reports of proxy rule by husbands trigger satirical press reports.", eff(-1, 0, -2, -1)), 1.2),
        reaction("demand_separate_offices_for_women_sarpanchs", "Demand separate panchayat office buildings to allow women sarpanchs to work without family interference.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Finance department states funds are constrained, postponing the plan.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_women_sarpanch_advisory", "Propose forming a district-level advisory council of women leaders to recommend rural health priorities.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Meetings face low attendance due to lack of local transport facilities.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2006-06
ITEMS_2006_2010.append(make_news(
    key="bh2006_2006_06_land_commission",
    month="2006-06",
    title="Government Appoints Bandyopadhyay Commission on Land Reforms",
    desc="The state cabinet appoints the Bandyopadhyay Commission to study land ceiling laws, sharecropper (bataidars) rights, and surplus land distribution.",
    tags=['governance', 'land_rights'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("instruct_commission_to_study_bataidar_titles", "Instruct the commission to collect detailed village bataidar logs to secure sharecropper titles.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Landowner groups voice concern, threatening counter protest rallies.", eff(-1, 0, -2, -3)), 1.2),
        reaction("oppose_sharecropper_legislation_for_harmony", "Oppose any radical land laws, arguing they will destroy agrarian peace and polarize villages.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Dalit and landless voter organizations boycott the party's rallies.", eff(0, 0, -2, -3)), 1.25),
        reaction("propose_voluntary_share_agreements", "Propose promoting voluntary written crop sharing agreements with tax incentives for landowners.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Low trust between landowners and bataidars keeps agreements low.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"ruralAngerMemory": 2}, weight=0.25)
    ]
))

# 2006-07
ITEMS_2006_2010.append(make_news(
    key="bh2006_2006_07_contract_teachers",
    month="2006-07",
    title="Government Announces Hiring of 1 Lakh Contract Teachers",
    desc="To address primary school teacher deficits, the government announces recruitment of 1 lakh teachers on contract via local panchayat boards.",
    tags=['governance', 'education'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("fast_track_panchayat_hirings", "Fast-track selection through panchayats, prioritizing local district applicants.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Allegations of bribery in local panchayat selections trigger police inquiries.", eff(-1, -1, -2, -2)), 1.2),
        reaction("demand_regular_bpsc_recruitment", "Demand recruitment through state service commission (BPSC), calling contract hiring substandard.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Unemployed youth welcome the quick contract jobs, ignoring BPSC debates.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_teacher_eligibility_test", "Propose introducing a mandatory Teacher Eligibility Test (TET) to screen selection quality.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Delay in testing schedules postpones the active recruitment rollout.", eff(0, 0, -2, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2006-08
ITEMS_2006_2010.append(make_news(
    key="bh2006_2006_08_muzaffarpur_revival",
    month="2006-08",
    title="State Cabinet Clears Bela Industrial Area Revival Plan",
    desc="The cabinet approves fiscal incentives and power supply guarantees to revive closed food-processing and leather units in Muzaffarpur's Bela zone.",
    tags=['governance', 'economy'],
    base_w=1.1, profile="governance",
    reactions=[
        reaction("allocate_industrial_revival_grants", "Allocate state grants and direct banks to offer low-interest working capital loans to units.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Delay in industrial grid connection limits the actual factory startups.", eff(0, 0, -1, -1)), 1.2),
        reaction("demand_priority_for_handloom_weavers", "Demand that state funds be spent on rural handloom weavers instead of urban private factory owners.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Trade chambers criticize the opposition as anti-industrialization.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_joint_training_itc", "Propose setting up a joint training institute inside Bela to train local youth for factory jobs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Construction delays keep the training center shell empty for months.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"economyIssueMissed": 1}, weight=0.3)
    ]
))

# 2006-09
ITEMS_2006_2010.append(make_news(
    key="bh2006_2006_09_fast_track_courts",
    month="2006-09",
    title="Special Fast-Track Courts Deliver First Criminal Convictions",
    desc="The state-appointed fast-track courts deliver speed convictions of several high-profile gang leaders, boosting the government's law record.",
    tags=['law_order'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("publicize_convictions_and_court_speed", "Publicize the trial speed on media, asserting the end of political criminal patronage in Bihar.",
                 ['GOVERNMENT'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Opposition claims selective targetting of specific community leaders.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_prosecution_of_ruling_mla_cases", "Demand that the fast-track courts prioritize cases against ruling coalition MLAs as well.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "Voters welcome the convictions of known gang lords, reducing impact.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_digitized_warrant_tracking", "Propose a centralized digitized warrant tracking database to prevent police delay in court summons.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Database errors and slow server links keep block stations offline.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"securityIgnoredMemory": 2}, weight=0.25)
    ]
))

# 2006-10
ITEMS_2006_2010.append(make_news(
    key="bh2006_2006_10_phc_medicine_scheme",
    month="2006-10",
    title="Free Generic Medicine Distribution Launched at Block PHCs",
    desc="The health department launches a scheme to supply 50 essential generic medicines for free to all outpatients at Primary Health Centers.",
    tags=['governance', 'welfare'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("establish_medicine_supply_depots", "Establish state supply depots and set up local drug quality testing boards.",
                 ['GOVERNMENT'], eff(2, 0, 3, 5),
                 {},
                 risk(15, "Audit reports expose supply of expired medicines in two blocks, drawing bad press.", eff(-1, -1, -2, -2)), 1.25),
        reaction("demand_hiring_of_doctors_first", "Demand hiring permanent doctors first, calling free medicine useless without diagnostic checks.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "PHC patients welcome the free medicines, ignoring doctor vacancy debates.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_district_mobile_health_vans", "Propose running mobile medical vans to distribute medicines directly to remote hamlets.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Vans break down due to poor road conditions in interior blocks.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 1}, weight=0.25)
    ]
))

# 2006-11
ITEMS_2006_2010.append(make_news(
    key="bh2006_2006_11_gandhi_setu_traffic",
    month="2006-11",
    title="Gandhi Setu Repairs Lead to Heavy Traffic Diversions",
    desc="Major structural repairs on the Mahatma Gandhi Setu bridge trigger gridlocks. Commuters face hours of delay crossing the Ganges.",
    tags=['infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("deploy_extra_traffic_police_pontoon", "Deploy extra traffic police, and order pontoon bridges to be set up for light vehicles.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(16, "Pontoon bridge installations are delayed by high river currents.", eff(0, 0, -2, -2)), 1.2),
        reaction("demand_central_funding_for_parallel_bridge", "Demand the Centre sanction a new parallel bridge immediately, calling repairs temporary eyewash.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Central ministry states feasibility studies must be completed first.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_regulated_night_freight", "Propose restricting heavy freight trucks to night hours only, keeping daytime clear for passenger cars.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Truck driver unions strike, blockading highway toll plazas.", eff(-1, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2006-12
ITEMS_2006_2010.append(make_news(
    key="bh2006_2006_12_rjd_protests_vendetta",
    month="2006-12",
    title="RJD Rallies in Patna Alleging Selective Police Harassment",
    desc="RJD cadres stage dharnas in Patna, accusing the NDA state government of using local police to selectively target its leaders and workers.",
    tags=['protest', 'politics'],
    base_w=1.2, profile="protest",
    reactions=[
        reaction("refuse_allegations_assert_rule_of_law", "Refuse the allegations, stating that police actions are based on court warrants and crime records.",
                 ['GOVERNMENT'], eff(2, 0, 2, 3),
                 {},
                 risk(15, "Vigilance raids on opposition leaders draw critical coverage from sympathetic media.", eff(-1, 0, -2, -1)), 1.2),
        reaction("condemn_regime_as_anti_social_justice", "Condemn the regime, calling it an attempt to suppress subaltern political voice.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "NDA releases lists of criminal records of the arrested cadres, neutralizing charges.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_bipartisan_police_complaints_board", "Propose setting up a bipartisan police complaints board to screen political harassment charges.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Home department opposes BPSC guidelines inclusion, stalling the board.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2007-01
ITEMS_2006_2010.append(make_news(
    key="bh2007_2007_01_nalanda_revival",
    month="2007-01",
    title="Assembly Passes Landmark Nalanda University Revival Bill",
    desc="The Bihar Assembly passes a bill to revive the historical Nalanda University as a global center of excellence, attracting international interest.",
    tags=['governance', 'education'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("allocate_land_and_form_mentor_group", "Allocate land in Rajgir and form an international mentor group led by Nobel laureates.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Local land acquisitions in Rajgir spark minor protests from potato farmers.", eff(0, 0, -1, -1)), 1.2),
        reaction("demand_focus_on_state_universities_first", "Demand that state funds be spent on regular state universities facing acute teacher vacancies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Literary bodies criticize the party for opposing a prestige educational project.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_scholarship_fund_for_bihari_students", "Propose that the university reserve 30% of its research fellowships exclusively for state students.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Mentor group rejects state-wise quotas to protect global ranking status.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2007-02
ITEMS_2006_2010.append(make_news(
    key="bh2007_2007_02_land_reform_panic",
    month="2007-02",
    title="Bandyopadhyay Commission Leak Sparks Landlord Alarms",
    desc="Leaked sections of the Bandyopadhyay land reform commission report suggest lowering land ceiling limits, triggering panic among large landholders.",
    tags=['land_rights', 'politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("clarify_report_as_recommendatory_only", "Clarify that the report is recommendatory only and no sudden land laws will be passed.",
                 ['GOVERNMENT'], eff(2, 0, 2, 3),
                 {},
                 risk(18, "Sharecropper organizations accuse the government of yielding to landowner lobbies.", eff(-1, 0, -2, -3)), 1.2),
        reaction("demand_rejection_of_ceiling_proposals", "Demand the government formally reject the ceiling cuts to protect agricultural investment stability.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Dalit voter bases shift away, accusing the party of protecting feudal land ownership.", eff(0, 0, -2, -3)), 1.25),
        reaction("propose_bipartisan_farmer_dialogue", "Propose setting up an all-party committee with farmer and landowner reps to study the clauses.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Tensions between groups disrupt the dialogue sessions, halting progress.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"ruralAngerMemory": 2}, weight=0.25)
    ]
))

# 2007-03
ITEMS_2006_2010.append(make_news(
    key="bh2007_2007_03_forward_caste_accusations",
    month="2007-03",
    title="Opposition Accuses Nitish Kumar of Favoring Forward Castes",
    desc="Opposition parties hold rallies in Patna, alleging that the JD(U)-BJP administration is systematically favoring forward castes in government postings.",
    tags=['politics', 'identity'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("advertise_ebc_welfare_allocations", "Advertise data on recent EBC and Dalit postings, defending the social justice balance of the cabinet.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Counter protests by elite associations polarize district voter pools.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_caste_wise_posting_audit", "Demand a caste-wise audit of all secretarial appointments to expose the representation deficit.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Governing allies release lists of previous RJD postings, neutralizing charges.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_mahadalit_inclusion_plan", "Propose formulating a dedicated Mahadalit category to target welfare directly to the poorest.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Other backward classes protest the new category, fearing dilution of their share.", eff(0, 0, -2, -1)), 1.15),
        no_comment(hidden={"identityIssueMissed": 1}, weight=0.2)
    ]
))

# 2007-04
ITEMS_2006_2010.append(make_news(
    key="bh2007_2007_04_mahadalit_commission",
    month="2007-04",
    title="Government Formulates Plan to Appoint Mahadalit Commission",
    desc="To address the poorest sections of Scheduled Castes, the state government announces plans to set up a Mahadalit Commission to recommend targeted welfare.",
    tags=['politics', 'welfare'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("appoint_mahadalit_commissioners", "Appoint the commissioners and allocate initial budget grants to study Dalit block populations.",
                 ['GOVERNMENT'], eff(3, 0, 4, 5),
                 {},
                 risk(15, "Paswan groups protest their exclusion from initial Mahadalit category drafts.", eff(-1, 0, -2, -3)), 1.2),
        reaction("label_commission_as_attempt_to_divide_dalits", "Label the commission as a political attempt to divide the Dalit vote share for electoral gain.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(14, "Non-Paswan Dalit groups criticize the party for opposing targeted welfare.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_inclusive_dalit_development_charter", "Propose that the budget grants be increased for all Scheduled Castes equally, bypassing new categories.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Debates over community quotas delay the release of general SC funds.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.2)
    ]
))

# 2007-05
ITEMS_2006_2010.append(make_news(
    key="bh2007_2007_05_bhagalpur_riots_cases",
    month="2007-05",
    title="State Reopens 1989 Bhagalpur Riots Cases; Key Accused Booked",
    desc="The state home department reopens several closed cases of the 1989 Bhagalpur communal riots, initiating fast-track trials against key accused.",
    tags=['law_order', 'identity'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("enforce_prosecutions_and_welfare_grants", "Enforce prosecutions strictly and announce welfare pensions for riot-affected survivors.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Conservative factions within coalition partner BJP voice concerns over timing.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_prosecution_of_administrative_officers", "Demand prosecution of the administrative officers who colluded in closing cases earlier.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "IPS unions protest, warning that prosecuting retired officers defames the cadre.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_communal_harmony_board", "Propose establishing a statutory Communal Harmony Board to monitor peace in Bhagalpur.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Rival religious groups boycott board meetings, keeping local trust low.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 1}, weight=0.25)
    ]
))

# 2007-06
ITEMS_2006_2010.append(make_news(
    key="bh2007_2007_06_gram_sampark",
    month="2007-06",
    title="Launch of Mukhyamantri Gram Sampark Yojana for Rural Roads",
    desc="The rural development department launches a major program to construct all-weather concrete roads linking isolated hamlets to nearby highways.",
    tags=['governance', 'infrastructure'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("allocate_gram_sampark_budgets", "Allocate state funds, and mandate local block panchayat boards to inspect road quality.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Panchayat selection of road routes triggers local caste disputes in blocks.", eff(0, 0, -2, -2)), 1.2),
        reaction("demand_probe_on_road_material_quality", "Demand that state engineers audit road materials, alleging usage of substandard local clay.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 3),
                 {},
                 risk(12, "Contractors suspend work, protesting against arbitrary inspection checks.", eff(-1, 0, -2, -1)), 1.15),
        reaction("propose_community_labor_road_model", "Propose employing local landless laborers for road construction to boost rural wages.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Lack of technical expertise among local laborers results in poor road life.", eff(0, 0, -2, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2007-07
ITEMS_2006_2010.append(make_news(
    key="bh2007_2007_07_darbhanga_floods",
    month="2007-07",
    title="Gandak Canal Breach Floods Agricultural Darbhanga",
    desc="Heavy seasonal rainfall breaches the Gandak canal system, submerging standing crops and flooding rural villages in Darbhanga district.",
    tags=['disaster_relief', 'rural'],
    base_w=1.2, profile="disaster_relief",
    reactions=[
        reaction("deploy_canal_repair_teams_relief", "Deploy emergency canal repair teams, distribute dry food packets, and waive local crop cess.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Bureaucratic delay in checking crop losses sparks farmer sit-ins in town.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_compensation_package_per_acre", "Demand that the state immediately release Rs 3,000 per acre compensation for ruined crops.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Finance department states canal funds are already committed, delaying relief.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_canal_concrete_lining_project", "Propose a long-term concrete lining project for all major Darbhanga canal banks.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Construction shutdown of canals during lining triggers farmer water protests.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2007-08
ITEMS_2006_2010.append(make_news(
    key="bh2007_2007_08_flood_package_dispute",
    month="2007-08",
    title="State Demands Rs 2,000 Crore Flood Package From Centre",
    desc="Following damages in Darbhanga and Champaran, the Bihar Cabinet passes a resolution demanding a Rs 2,000 crore relief package from UPA.",
    tags=['politics', 'disaster_relief'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("hold_patna_solidarity_conventions", "Hold conventions to demand central allocation, warning against step-motherly treatment.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Opposition accuses the state of failing to submit previous audit reports.", eff(0, 0, -2, -2)), 1.2),
        reaction("demand_independent_audit_of_past_relief", "Demand a central CAG audit of state relief spending, alleging diversion of funds.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, -1, 4, 3),
                 {},
                 risk(14, "Rural voters view the opposition as trying to block central package release.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_bipartisan_relief_panel_for_delhi", "Propose sending a joint treasury-opposition delegation to Delhi to lobby for the package.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Leader disagreements over draft memorandum prevent the delegation from flying.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"disasterIgnoredMemory": 2}, weight=0.2)
    ]
))

# 2007-09
ITEMS_2006_2010.append(make_news(
    key="bh2007_2007_09_bicycle_scheme_expansion",
    month="2007-09",
    title="Balika Cycle Yojana Expanded to Minority and Backward Classes",
    desc="Following the success of the schoolgirl cycle scheme, the government announces its expansion to girl students of minority and EBC sections.",
    tags=['governance', 'welfare'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("rollout_expanded_grants", "Rollout the expanded grants directly through bank drafts at school events.",
                 ['GOVERNMENT'], eff(3, 0, 4, 5),
                 {},
                 risk(15, "General category student unions protest, demanding merit-based cycles.", eff(0, 0, -2, -2)), 1.25),
        reaction("demand_income_based_cycle_grants", "Demand that the cycle scheme be made income-based, excluding affluent families within backwards.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Minority voter organizations accuse the party of trying to dilute welfare benefits.", eff(0, 0, -2, -2)), 1.15),
        reaction("propose_school_bus_alternative", "Propose that the state buy school buses for rural girls instead of distributing cycles.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "High fuel and maintenance costs keep the buses off rural routes.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 1}, weight=0.25)
    ]
))

# 2007-10
ITEMS_2006_2010.append(make_news(
    key="bh2007_2007_10_police_recruitment",
    month="2007-10",
    title="Government Starts Massive Police Recruitment Drive",
    desc="The home department announces a massive recruitment drive to fill 15,000 vacant constable posts, introducing biometric security checks.",
    tags=['governance', 'law_order'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("enforce_transparent_recruitment_rules", "Enforce transparent recruitment rules, deploy CCTVs, and publicize results on state portals.",
                 ['GOVERNMENT'], eff(3, 0, 3, 4),
                 {},
                 risk(15, "Failed applicants stage protest rallies, alleging evaluation anomalies.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_judicial_monitoring_of_selections", "Demand judicial monitoring of recruitment, alleging that ruling allies are selling slots.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Voters welcome the transparent biometric selection, reducing impact.", eff(0, 0, -1, -1)), 1.2),
        reaction("propose_police_training_infrastructure", "Propose allocating 20% of recruitment budget to build modern physical training yards in Gaya.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Construction delays keep the new training yards incomplete for months.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2007-11
ITEMS_2006_2010.append(make_news(
    key="bh2007_2007_11_contract_teacher_strike",
    month="2007-11",
    title="Contract Teachers Strike in Patna Demanding Equal Pay",
    desc="Newly recruited primary contract teachers launch protest strikes in Patna, demanding equal pay scales matching regular state teachers.",
    tags=['protest'],
    base_w=1.15, profile="protest",
    reactions=[
        reaction("refuse_pay_hike_warn_striking_staff", "Refuse the pay hike, citing state budget constraints, and warn of contract terminations.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(18, "Unions block primary school doors, shutting down classes in three districts.", eff(-1, 0, -2, -2)), 1.15),
        reaction("support_teachers_demand_assembly_hearing", "Support the teachers, demanding the government form an assembly committee to negotiate pay.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Public feels unsympathetic to strike, citing closed classes for their kids.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_performance_linked_pay_scale", "Propose a performance-linked pay scale where contract teachers can secure regular scales after tests.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Teacher unions reject testing clauses, continuing the strike.", eff(0, 0, -2, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2007-12
ITEMS_2006_2010.append(make_news(
    key="bh2007_2007_12_patna_zoo_upgrade",
    month="2007-12",
    title="Tourism Department Launches Patna Zoo Modernization Plan",
    desc="The tourism department approves a modernization plan for the Sanjay Gandhi Biological Park, constructing new enclosures and safari tracks.",
    tags=['governance'],
    base_w=1.1, profile="governance",
    reactions=[
        reaction("allocate_zoo_upgrade_funds", "Allocate state funds, and introduce battery-operated visitor vehicles inside the park.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Animal activists protest the noise of construction works inside animal zones.", eff(0, 0, -1, -1)), 1.2),
        reaction("demand_priority_for_district_parks", "Demand that state funds be spent on district parks first instead of centralizing budgets in Patna.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Patna citizens welcome the zoo upgrade, criticizing the opposition.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_corporate_animal_adoption", "Propose a model allowing private corporates to adopt and maintain animal enclosures.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Lack of corporate head offices in Patna results in low adoption rates.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2008-01
ITEMS_2006_2010.append(make_news(
    key="bh2008_2008_01_bihar_summit",
    month="2008-01",
    title="Government Hosts Global Bihar Summit to Attract Investment",
    desc="The state government hosts the first Global Bihar Summit in Patna, inviting NRI entrepreneurs and national business leaders to invest.",
    tags=['economy'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("announce_single_window_clearances", "Announce single-window clearance rules and tax waivers for agro-based business units.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Opposition highlights poor electricity supply index, keeping investors skeptical.", eff(0, 0, -2, -1)), 1.2),
        reaction("expose_barren_land_acquisitions", "Expose land acquisitions, alleging that fertile farming lands are being sold to corporates.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Trade bodies criticize the opposition, stating it blocks industrial growth.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_state_skill_development_mission", "Propose establishing a State Skill Development Mission to train rural youth for incoming jobs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Administrative delays in hiring trainers keep training centers idle.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"economyIssueMissed": 1}, weight=0.3)
    ]
))

# 2008-02
ITEMS_2006_2010.append(make_news(
    key="bh2008_2008_02_mahadalit_report",
    month="2008-02",
    title="Mahadalit Commission Identifies 18 Castes For Special Welfare",
    desc="The Mahadalit Commission submits its report, identifying 18 scheduled castes as 'Mahadalit' and recommending exclusive welfare programs.",
    tags=['politics', 'identity'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("accept_report_and_announce_welfare", "Accept the report and announce special grants for house construction and scholarships.",
                 ['GOVERNMENT'], eff(3, 0, 3, 5),
                 {},
                 risk(15, "Paswan community organizations hold protests, demanding their inclusion in lists.", eff(-1, 0, -2, -3)), 1.25),
        reaction("label_report_as_dalit_division_tool", "Label the report as a political tool to split the Dalit vote bank and isolate specific leaders.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(14, "Non-Paswan Dalit groups criticize the party for trying to block benefits.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_general_dalit_allowance", "Propose increasing general Dalit welfare budgets by 30% instead of dividing the category.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Debates over community shares stall the release of current SC funds.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.2)
    ]
))

# 2008-03
ITEMS_2006_2010.append(make_news(
    key="bh2008_2008_03_mahadalit_schemes",
    month="2008-03",
    title="Government Announces Free Radios for Mahadalit Families",
    desc="CM Nitish Kumar announces a scheme to distribute free transistor radios to Mahadalit families to promote state educational broadcasts.",
    tags=['governance', 'welfare'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("rollout_radio_distribution_drives", "Rollout the radio distribution drives through block welfare officers.",
                 ['GOVERNMENT'], eff(3, 0, 4, 4),
                 {},
                 risk(18, "Audit exposes corruption in procurement of substandard radio sets, drawing press.", eff(-1, -1, -2, -2)), 1.25),
        reaction("demand_cash_allowance_instead", "Demand the government distribute cash allowances instead, calling radios a cosmetic gimmick.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Welfare organizations point to high risk of cash diversion by male heads.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_community_radio_stations", "Propose setting up panchayat community radio stations to broadcast local farming tips.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Licensing delays from the central ministry keep the stations silent.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 1}, weight=0.25)
    ]
))

# 2008-04
ITEMS_2006_2010.append(make_news(
    key="bh2008_2008_04_chhapra_rail_factory",
    month="2008-04",
    title="Union Railway Minister Lalu Prasad Launches Chhapra Coach Factory",
    desc="Union Railway Minister Lalu Prasad Yadav lays the foundation stone for a mega wheel and coach factory in Chhapra, highlighting UPA's contributions.",
    tags=['infrastructure', 'politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("hail_project_as_state_rail_booster", "Welcome the project, and demand the Centre expedite matching funds for state feeder lines.",
                 ['GOVERNMENT'], eff(1, 0, 2, 3),
                 {},
                 risk(15, "Opposition claims state police are delaying land clearances for factory access.", eff(-1, 0, -2, -2)), 1.15),
        reaction("campaign_on_lalu_rail_achievements", "Campaign aggressively on the Chhapra factory, highlighting Lalu Prasad's railway turnaround.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "NDA releases data showing slow progress of previous local rail lines.", eff(-1, 0, -1, -1)), 1.25),
        reaction("propose_joint_chhapra_urban_bypass", "Propose a joint board representing state planners and railway officials to build bypasses around factory.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Jurisdictional disputes between state and central boards delay bypass design.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2008-05
ITEMS_2006_2010.append(make_news(
    key="bh2008_2008_05_urea_scarcity",
    month="2008-05",
    title="Urea Scarcity Triggers Farmer Rallies in South Bihar",
    desc="Shortage of fertilizer (urea) during the planting season causes farmer agitations in Gaya and Rohtas. Opposition blames state distribution.",
    tags=['protest', 'rural'],
    base_w=1.2, profile="land_rights",
    reactions=[
        reaction("procure_urea_stocks_increase_patrols", "Procure emergency urea stocks from national pools and deploy police guards at distribution centers.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Black marketing by local cooperative heads continues, drawing bad press.", eff(-1, -1, -2, -2)), 1.2),
        reaction("lead_urea_substation_sit_ins", "Lead farmer sit-ins outside agriculture department offices, demanding subsidy checks.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Clashes between farmers and security staff lead to police lathi-charge.", eff(-1, 0, -2, -1)), 1.2),
        reaction("propose_digitized_fertilizer_slips", "Propose issuing digitized slips linked to land records to prevent non-farmers from buying.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Frequent power failures at rural centers keep system terminals offline.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 3}, weight=0.25)
    ]
))

# 2008-06
ITEMS_2006_2010.append(make_news(
    key="bh2008_2008_06_naxal_rohtas",
    month="2008-06",
    title="Armed Attack on Rural Police Station in Rohtas",
    desc="Suspected Naxal factions attack a rural police outpost in Rohtas district, looting armaments and triggering search operations.",
    tags=['security_crisis'],
    base_w=1.2, profile="security_crisis",
    reactions=[
        reaction("deploy_stf_combing_operations", "Deploy special task force combing operations, seal borders, and suspend negligent station chiefs.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(16, "Local farm workers allege STF search excesses and harassment in villages.", eff(-1, 0, -2, -2)), 1.2),
        reaction("condemn_police_infrastructure_deficits", "Condemn the police infrastructure, alleging that rural outposts lack basic communication lines.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Security analysts accuse the opposition of trying to politicize a terror incident.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_village_defense_committees", "Propose forming village defense committees with licensed arms for village youths.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Local political disputes prevent the consensus selection of committee heads.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"securityIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2008-07
ITEMS_2006_2010.append(make_news(
    key="bh2008_2008_07_english_classes",
    month="2008-07",
    title="Government Introduces Spoken English Classes in Schools",
    desc="To improve employability, the education department partners with the British Council to run spoken English classes in senior state schools.",
    tags=['governance', 'education'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("allocate_english_training_funds", "Allocate funds to train state teachers and distribute spoken audio cassettes to schools.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Lack of functional audio players in rural schools limits the scheme.", eff(0, 0, -2, -1)), 1.2),
        reaction("demand_focus_on_basic_science_teachers", "Demand that the state hire basic science and math teachers first, calling English a cosmetic push.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Urban student unions welcome English classes, criticizing the opposition.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_private_sector_mentoring", "Propose private IT sector employees volunteer to mentor senior students on weekends.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Lack of private IT offices outside Patna limits the mentoring reach.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2008-08
ITEMS_2006_2010.append(make_news(
    key="bh2008_2008_08_kosi_deluge",
    month="2008-08",
    title="Kosi River Embankment Breach Deluges North Bihar",
    desc="The Kosi river breaches its embankment at Kushaha in Nepal, shifting its course and flooding five North Bihar districts, affecting 30 lakh people.",
    tags=['disaster_relief', 'rural'],
    base_w=1.35, profile="disaster_relief",
    reactions=[
        reaction("order_national_rescue_deploy_boats", "Order national rescue help, deploy state boats, and set up mega relief camps in highlands.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(22, "Shortage of rescue boats delays operations in Saharsa, drawing critical press.", eff(-2, 0, -3, -4)), 1.25),
        reaction("demand_national_calamity_status", "Demand the PM declare the breach a national calamity and release immediate Rs 2,000 crore relief.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 5),
                 {},
                 risk(16, "Central agencies delay declarations to assess damage, slowing relief flows.", eff(0, 0, -2, -1)), 1.3),
        reaction("propose_river_redirection_commission", "Propose a joint scientific commission of Nepal and Indian engineers to redirect the river.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(12, "Diplomatic protocol delays postpone the first meeting of the commission.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.1)
    ]
))

# 2008-09
ITEMS_2006_2010.append(make_news(
    key="bh2008_2008_09_kosi_rescue",
    month="2008-09",
    title="Army Deployed in Saharsa For Kosi Flood Rescue",
    desc="Army columns and NDRF battalions are deployed to rescue stranded families in Saharsa, Madhepura, and Supaul. Deluge is declared a National Calamity.",
    tags=['disaster_relief'],
    base_w=1.25, profile="disaster_relief",
    reactions=[
        reaction("coordinate_state_army_command", "Coordinate state relief cell with Army command, and allocate Rs 100 crore for medicine stocks.",
                 ['GOVERNMENT'], eff(3, 0, 3, 3),
                 {},
                 risk(18, "Distribution delays in remote blocks spark minor protest rallies by victims.", eff(-1, 0, -2, -2)), 1.2),
        reaction("expose_relief_camp_substandard_supplies", "Expose supply contracts, alleging that ruling party candidates are selling relief grain.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, -1, 4, 3),
                 {},
                 risk(14, "Victims express anger, stating the opposition is exploiting their misery.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_bipartisan_relief_monitoring_team", "Propose forming an all-party legislative committee to inspect relief camp distributions.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Rival party workers clash at camp gates, disrupting relief distributions.", eff(-1, 0, -1, -1)), 1.1),
        no_comment(weight=0.2)
    ]
))

# 2008-10
ITEMS_2006_2010.append(make_news(
    key="bh2008_2008_10_kosi_rehabilitation",
    month="2008-10",
    title="State Launches World Bank Funded Kosi Recovery Project",
    desc="The state government signs an agreement for a World Bank funded Kosi Flood Recovery Project to rebuild houses and roads in affected zones.",
    tags=['governance', 'infrastructure'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("allocate_reconstruction_subsidies", "Allocate reconstruction subsidies directly to beneficiary bank accounts to rebuild concrete homes.",
                 ['GOVERNMENT'], eff(3, 0, 3, 4),
                 {},
                 risk(15, "Delays in verification of beneficiary titles stall the initial payouts.", eff(0, 0, -2, -2)), 1.2),
        reaction("demand_probe_on_reconstruction_tenders", "Demand a probe into reconstruction tenders, alleging favoritism of specific contractors.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 3),
                 {},
                 risk(12, "Contractors strike, halting current road rebuilding works.", eff(-1, 0, -2, -1)), 1.15),
        reaction("propose_community_monitored_construction", "Propose that local village committees audit building materials and progress directly.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Panchayat heads decline oversight, citing lack of training in rules.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 2}, weight=0.25)
    ]
))

# 2008-11
ITEMS_2006_2010.append(make_news(
    key="bh2008_2008_11_land_reforms_shelved",
    month="2008-11",
    title="CM Clarifies Land Ceilings Will Not Be Lowered",
    desc="Seeking to address landowner concerns, Chief Minister Nitish Kumar clarifies that the government will not lower existing land ceiling limits.",
    tags=['land_rights', 'politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("declare_decision_to_protect_farm_investment", "Declare the decision as necessary to protect farm investments and maintain agrarian peace.",
                 ['GOVERNMENT'], eff(2, 0, 2, 4),
                 {},
                 risk(15, "Sharecropper organizations hold black flag rallies, alleging betrayal.", eff(-1, 0, -2, -3)), 1.2),
        reaction("label_decision_as_surrender_to_feudal_lobbies", "Label the decision as a surrender to feudal lobbies, demanding sharecropper protections.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Land-owning voter bases consolidate support behind the ruling alliance.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_bipartisan_sharecropper_compensation", "Propose a pension scheme for old sharecroppers who surrender cultivation claims.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "High financial burden stalls the pension scheme draft in cabinet.", eff(0, 0, -2, -1)), 1.15),
        no_comment(hidden={"ruralAngerMemory": 2}, weight=0.25)
    ]
))

# 2008-12
ITEMS_2006_2010.append(make_news(
    key="bh2008_2008_12_opposition_flood_yatras",
    month="2008-12",
    title="Lalu Prasad Launches Yatras Highlighting Flood Corruption",
    desc="RJD Chief Lalu Prasad Yadav launches state-wide yatras in flood-affected districts, alleging corruption in relief distributions.",
    tags=['politics', 'protest'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("counter_with_development_achievement_data", "Counter the yatra by releasing data on completed roads and active relief operations.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Opposition displays photos of unfinished bridges at several yatra stops.", eff(0, 0, -2, -1)), 1.15),
        reaction("intensify_yatra_focus_on_bureaucratic_apathy", "Intensify the yatra rallies, highlighting delayed cash distributions to flood victims.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Clashes between rival cadres at yatra venues draw police actions.", eff(-1, 0, -1, -1)), 1.25),
        reaction("propose_joint_reconstruction_charter", "Propose a joint assembly charter to coordinate rebuilding priorities without political battles.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Rivals refuse to sign, continuing political yatra campaigns.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2009-01
ITEMS_2006_2010.append(make_news(
    key="bh2009_2009_01_seat_sharing",
    month="2009-01",
    title="JD(U) and BJP Finalize Lok Sabha Seat Sharing",
    desc="Ahead of the general elections, the JD(U) and BJP finalize seat sharing in Bihar, while RJD and LJP form a separate UPA splinter front.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("announce_seat_sharing_and_launch_campaign", "Announce the sharing list and launch joint campaigns focusing on state growth.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Local BJP leaders in two districts rebel over seat transfers to JD(U).", eff(-1, 0, -2, -1)), 1.2),
        reaction("campaign_on_alliance_internal_friction", "Campaign on the friction between JD(U) and BJP on secular issues, calling them unstable.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "NDA resolves the disputes quickly, reducing the impact of criticism.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_bipartisan_campaign_code_of_ethics", "Propose a campaign code of ethics to restrict personal attacks during rallies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Rival candidates ignore the code, escalating personal accusations on stage.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2009-02
ITEMS_2006_2010.append(make_news(
    key="bh2009_2009_02_patna_marine_drive",
    month="2009-02",
    title="Urban Development Cell Proposes Patna Marine Drive",
    desc="The urban development cell proposes constructing a major Ganga riverfront expressway (Patna Marine Drive) to link East and West Patna.",
    tags=['governance', 'infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("allocate_expressway_preliminary_funds", "Allocate preliminary state funds and initiate surveys for the Ganga riverfront project.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Environmentalists challenge the design, citing threat to Ganga dolphin zones.", eff(0, 0, -2, -2)), 1.2),
        reaction("demand_subsidies_for_slums_along_river", "Demand that the state guarantee housing rehabilitation plots first to all riverfront slums.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Urban trade chambers criticize the opposition as anti-development.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_ppp_expressway_model", "Propose a public-private partnership model to attract global infrastructure developers.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Private developers demand cheap power guarantees before bidding, delaying project.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2009-03
ITEMS_2006_2010.append(make_news(
    key="bh2009_2009_03_lok_sabha_heat",
    month="2009-03",
    title="Lok Sabha Campaigning Reaches Peak in Bihar",
    desc="Campaigning for Bihar Lok Sabha seats reaches peak. NDA projects Nitish Kumar's clean image, while RJD warns of upper-caste domination.",
    tags=['election'],
    base_w=1.25, profile="election",
    reactions=[
        reaction("campaign_on_development_record_and_roads", "Campaign heavily on developmental achievements, showing road and bridge growth.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Opposition highlights instances of contract teacher strikes in districts.", eff(0, 0, -2, -2)), 1.2),
        reaction("highlight_incumbent_social_neglect_of_marginalized", "Highlight social neglect of marginalized Dalits, calling sushasan a media eyewash.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "NDA wins several rural seats due to strong EBC support equations.", eff(-1, 0, -1, -1)), 1.25),
        reaction("propose_public_television_debates", "Propose public TV debates on industrial investments and state revenue indices.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(10, "Opponents refuse to attend, leading to empty-chair media campaigns.", eff(-1, 0, -1, -1)), 1.1),
        no_comment(weight=0.2)
    ]
))

# 2009-04
ITEMS_2006_2010.append(make_news(
    key="bh2009_2009_04_naxal_belt_polling",
    month="2009-04",
    title="Lok Sabha Polling in Gaya and Jamui Under High Security",
    desc="Lok Sabha polling in sensitive Naxal belt districts concludes. Heavy security deployments ensure peaceful turnout in rural blocks.",
    tags=['election', 'security_crisis'],
    base_w=1.2, profile="security_crisis",
    reactions=[
        reaction("deploy_helicopter_surveillance_and_patrols", "Deploy helicopter surveillance and armed police patrols in sensitive polling blocks.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Local leaders allege police restrictions kept remote voters from polling.", eff(-1, 0, -2, -2)), 1.15),
        reaction("petition_ec_for_independent_booth_checks", "Petition the EC to verify EVM logs, alleging ruling party booth agents siphoned votes.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "EC rejects the petition, citing transparent polling agent registries.", eff(0, 0, -1, -1)), 1.2),
        reaction("propose_central_forces_for_counting", "Propose that counting centers allow only central paramilitary guards, keeping state police out.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "State police unions protest the proposal, calling it an insult to cadre.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"securityIgnoredMemory": 2}, weight=0.25)
    ]
))

# 2009-05
ITEMS_2006_2010.append(make_news(
    key="bh2009_2009_05_lok_sabha_sweep",
    month="2009-05",
    title="NDA Sweeps Bihar Lok Sabha Polls; RJD Reduced to 4 Seats",
    desc="The JDU-BJP alliance sweeps the Bihar Lok Sabha polls, winning 32 out of 40 seats. The RJD is reduced to only 4 seats in its worst setback.",
    tags=['election', 'politics'],
    base_w=1.3, profile="election",
    reactions=[
        reaction("declare_triumph_of_sushasan_and_growth", "Declare the sweep as a triumph of sushasan, and announce new road projects.",
                 ['GOVERNMENT'], eff(3, 0, 4, 5),
                 {},
                 risk(18, "Opposition files petitions in court challenging candidate affidavits.", eff(-1, 0, -2, -2)), 1.25),
        reaction("accept_verdict_vow_to_reorganize_cadres", "Accept the verdict, stating that RJD will reorganize its cadres to defend secularism.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(14, "Local party workers express frustration over losing cabinet influence.", eff(-1, 0, -2, -1)), 1.2),
        reaction("propose_joint_parliamentary_state_memo", "Propose a joint assembly memo to petition the Centre for Special Category Status.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Fierce rivalries between leaders prevent the joint memo draft.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.2)
    ]
))

# 2009-06
ITEMS_2006_2010.append(make_news(
    key="bh2009_2009_06_vaishali_clashes",
    month="2009-06",
    title="Post-Election Clashes Reported in Rural Vaishali",
    desc="Following the Lok Sabha results, clashes between RJD and JD(U) cadres are reported in rural Vaishali. District borders are sealed by police.",
    tags=['politics', 'security_crisis'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("deploy_police_pickets_and_arrest_history_sheeters", "Deploy police pickets in sensitive blocks and arrest suspected troublemakers.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Opposition claims local police are targetting only their cadre.", eff(-1, 0, -2, -2)), 1.15),
        reaction("demand_judicial_probe_on_police_bias", "Demand a judicial probe, alleging that local police colluded with ruling candidates during raids.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "Ruling party releases videos of opposition cadres instigating the clashes.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_cross_party_peace_marches", "Propose organizing joint cross-party peace marches through sensitive blocks.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Extreme factions boycott the marches, reducing their impact on the ground.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"securityIgnoredMemory": 2}, weight=0.25)
    ]
))

# 2009-07
ITEMS_2006_2010.append(make_news(
    key="bh2009_2009_07_right_to_service_bill",
    month="2009-07",
    title="Cabinet Initiates Drafting of Public Services Guarantee Act",
    desc="The state cabinet approves a plan to draft a Public Services Guarantee Act, penalizing bureaucrats for delays in issuing certificates and utilities.",
    tags=['governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("fast_track_bill_drafting_set_penalties", "Fast-track the draft, and set clear cash penalties to be deducted from negligent officer pay.",
                 ['GOVERNMENT'], eff(2, -1, 3, 4),
                 {},
                 risk(15, "Bureaucratic lobbies delay filings, protesting against salary deduction rules.", eff(-1, 0, -2, -2)), 1.25),
        reaction("demand_judicial_appeal_clauses", "Demand judicial appeal clauses, alleging that block officers will pass bad orders to avoid penalties.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Ruling party points to existing grievance boards, neutralizing criticism.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_digitized_service_counters", "Propose setting up single-window digitized counters (Vasudha Centers) in rural blocks.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Power cuts and network delays keep Vasudha terminals offline in remote blocks.", eff(0, 0, -2, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2009-08
ITEMS_2006_2010.append(make_news(
    key="bh2009_2009_08_drought_26_districts",
    month="2009-08",
    title="Severe Drought Declared in 26 Districts of Bihar",
    desc="A failure of monsoon rains triggers severe drought. The state government declares 26 districts drought-affected and plans emergency power supplies.",
    tags=['disaster_relief', 'rural'],
    base_w=1.25, profile="disaster_relief",
    reactions=[
        reaction("increase_rural_power_supply_hours", "Increase rural power supply to 8 hours daily for irrigation and waive tubewell cess.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Grid overload causes frequent trippings, failing to maintain the supply hours.", eff(0, 0, -2, -2)), 1.25),
        reaction("demand_complete_agricultural_loan_waiver", "Demand a complete waiver of all farm loans and immediate central aid of Rs 2,000 crore.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Cooperative banks warn of credit freeze if all loans are waived, delaying works.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_rainwater_harvesting_grants", "Propose cash grants for farmers to build farm ponds (Ahars and Pynes) to harvest rain.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Slow excavation work in dry clay soil delays pond benefits.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2009-09
ITEMS_2006_2010.append(make_news(
    key="bh2009_2009_09_diesel_subsidy",
    month="2009-09",
    title="Government Announces Direct Cash Diesel Subsidy for Farmers",
    desc="To save the standing kharif crop during drought, the government announces direct cash diesel subsidies for farmers running pump sets.",
    tags=['governance', 'rural'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("rollout_diesel_subsidy_through_block_officers", "Rollout the subsidy through block offices, using land registry records for verification.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Audit exposes corruption in fuel bills, drawing critical local press.", eff(-1, -1, -2, -2)), 1.25),
        reaction("demand_subsidy_be_transferred_directly_to_accounts", "Demand direct bank transfers, alleging block officers siphon cash commissions.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Lack of bank accounts in remote blocks delays the direct transfers.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_solar_pump_incentive_plan", "Propose shifting the budget to solar pumps to reduce agricultural diesel imports.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "High solar pump costs keep take-up low despite state subsidies.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 2}, weight=0.25)
    ]
))

# 2009-10
ITEMS_2006_2010.append(make_news(
    key="bh2009_2009_10_nalanda_mentor_meeting",
    month="2009-10",
    title="Amartya Sen Chairs First Nalanda Mentor Group Meeting",
    desc="Nobel Laureate Amartya Sen chairs the first Nalanda University Mentor Group meeting in Patna, finalizing the global curriculum drafts.",
    tags=['governance', 'education'],
    base_w=1.1, profile="governance",
    reactions=[
        reaction("allocate_infrastructure_development_grants", "Allocate infrastructure development grants and clear Rajgir campus construction contracts.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Landowner litigation in Rajgir delays construction starts.", eff(0, 0, -1, -1)), 1.2),
        reaction("demand_local_assembly_supervision_on_board", "Demand that the state assembly supervise board expenditures, alleging lack of oversight.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Board states global autonomy rules prohibit direct political control.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_bihar_history_research_center", "Propose setting up an exclusive center within the university to document Bihar's heritage.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Lack of historical document copies delays center research launches.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2009-11
ITEMS_2006_2010.append(make_news(
    key="bh2009_2009_11_assembly_bypolls",
    month="2009-11",
    title="RJD-LJP Alliance Wins 5 Assembly Bypoll Seats",
    desc="In assembly bypolls for 18 seats, the RJD-LJP alliance wins 5 seats, signaling organizational recovery attempts before the 2010 state elections.",
    tags=['election'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("downplay_bypoll_results_focus_on_general", "Downplay the bypolls, stating that local dynamics do not reflect state development support.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(15, "Cadres in polling districts raise concerns over local coordinate gaps.", eff(-1, 0, -2, -1)), 1.15),
        reaction("campaign_on_bypoll_victory_as_rjd_revival", "Campaign on the bypoll victory, calling it the beginning of the end of NDA rule in Bihar.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Governing allies release completed road maps, neutralizing yatra impact.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_bipartisan_polling_audits", "Propose that the EC double-check counting slips with EVM memory registry logs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "EC rejects the check as unnecessary, citing current protocol safety.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2009-12
ITEMS_2006_2010.append(make_news(
    key="bh2009_2009_12_mahadalit_land",
    month="2009-12",
    title="Government Announces Land Allocation Plan for Mahadalits",
    desc="The state cabinet approves a scheme to allocate 3 decimals of homestead land to every landless Mahadalit family in Bihar.",
    tags=['governance', 'land_rights'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("allocate_land_purchase_budgets_for_districts", "Allocate state budgets to purchase private land plots for distribution to families.",
                 ['GOVERNMENT'], eff(3, 0, 3, 5),
                 {},
                 risk(18, "Bureaucratic delays in identifying landless families stall actual registry.", eff(0, 0, -2, -2)), 1.25),
        reaction("demand_increase_to_five_decimals", "Demand that the allocation be increased to 5 decimals, calling 3 decimals too small.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Finance department states extra land purchases exceed budget capacity.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_panchayat_land_audits", "Propose that village panchayats verify beneficiary eligibility to prevent fraud allocations.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Local political blockings prevent regular panchayat audit meetings.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 2}, weight=0.25)
    ]
))

# 2010-01
ITEMS_2006_2010.append(make_news(
    key="bh2010_2010_01_boys_cycle_scheme",
    month="2010-01",
    title="Cycle Scheme Expanded to Backward Class Boy Students",
    desc="Following the success of the Balika Cycle Yojana, the government expands the cash cycle grants to boy students of backward and minority classes.",
    tags=['governance', 'welfare'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("rollout_grants_for_boys", "Rollout the grants directly through bank drafts at school events.",
                 ['GOVERNMENT'], eff(3, 0, 4, 5),
                 {},
                 risk(15, "General category student unions protest, demanding merit-based cycles.", eff(0, 0, -2, -2)), 1.25),
        reaction("demand_free_public_buses_for_students", "Demand the state run free student buses instead, calling cycle cash short-term eyewash.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "High transport operational costs keep buses off rural routes.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_school_development_monitors", "Propose that parent committees monitor cycle purchases and school attendance monthly.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Lack of parents attendance at meetings stalls committee audits.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 1}, weight=0.25)
    ]
))

# 2010-02
ITEMS_2006_2010.append(make_news(
    key="bh2010_2010_02_sushasan_campaign",
    month="2010-02",
    title="NDA Launches 'Sushasan' Campaign Highlighting Road Growth",
    desc="The JD(U) and BJP launch a state-wide campaign highlighting road construction and electricity index growth achieved in five years.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("counter_with_district_development_fairs", "Organize district development fairs to showcase completed bridges and school upgrades.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Opposition displays photos of unfinished bypasses near fair venues.", eff(0, 0, -2, -1)), 1.15),
        reaction("highlight_debt_and_contract_teacher_grievances", "Highlight growing state debt and the grievances of contract teachers in rallies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Public welcomes the visible highway connectivity, reducing impact of rallies.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_bipartisan_development_debate", "Propose a special debate on state GDP and finance parameters in the assembly.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Rival slogans disrupt the assembly debate within minutes, stalling the house.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2010-03
ITEMS_2006_2010.append(make_news(
    key="bh2010_2010_03_jehanabad_ prison_break",
    month="2010-03",
    title="Fast-Track Court Convicts Jehanabad Jailbreak Masterminds",
    desc="The fast-track court convicts the masterminds of the historic 2005 Jehanabad prison break case, sentencing them to life terms.",
    tags=['law_order'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("publicize_sentences_assert_rule_of_law", "Publicize the convictions on media, asserting the end of gang impunity in Bihar.",
                 ['GOVERNMENT'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Opposition claims selective acceleration of cases against their supporters.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_prosecution_of_jail_officials", "Demand prosecution of the jail officials who colluded in security lapses in 2005.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "Jail unions protest, warning that prosecuting guards defames the cadre.", eff(0, 0, -1, -1)), 1.2),
        reaction("propose_digitized_jail_surveillance", "Propose a centralized digitized jail surveillance database to prevent security lapses.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Database errors and slow server links keep block stations offline.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"securityIgnoredMemory": 2}, weight=0.25)
    ]
))

# 2010-04
ITEMS_2006_2010.append(make_news(
    key="bh2010_2010_04_vishwas_yatra_launch",
    month="2010-04",
    title="Nitish Kumar Launches State-wide 'Vishwas Yatra'",
    desc="CM Nitish Kumar launches the 'Vishwas Yatra' to visit villages directly, inspect developmental works, and hold direct citizen feedback meets.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("hold_village_chaupals_and_redress_grievances", "Hold village chaupals and order immediate action on local block officer complaints.",
                 ['GOVERNMENT'], eff(3, 0, 3, 4),
                 {},
                 risk(18, "Opposition groups hold black flag demonstrations at several yatra stops.", eff(-1, 0, -2, -2)), 1.2),
        reaction("highlight_local_corruption_in_yatra_villages", "Hold rallies along the yatra tracks, highlighting block-level welfare leakages.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Local residents welcome the CM's direct visits, ignoring opposition rallies.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_bipartisan_yatra_review_board", "Propose a joint assembly board to monitor village grievance redressals during yatra.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Rival party workers clash at chaupal venues, stalling joint reviews.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2010-05
ITEMS_2006_2010.append(make_news(
    key="bh2010_2010_05_gaya_rally",
    month="2010-05",
    title="Massive Turnout at Gaya Vishwas Yatra Rally",
    desc="CM Nitish Kumar's Vishwas Yatra rally in Gaya draws massive crowds of rural voters, showcasing support for the sushasan campaign.",
    tags=['politics', 'election'],
    base_w=1.2, profile="election",
    reactions=[
        reaction("announce_gaya_heritage_grants", "Announce fresh state development grants for Gaya heritage conservation and roads.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Election commission issues warnings regarding announcements close to polls.", eff(-1, 0, -2, -1)), 1.15),
        reaction("highlight_gaya_agricultural_losses_in_rallies", "Hold counter rallies in Gaya, focusing on dried-up tubewells and farmer debts.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Rival party workers disrupt the venues, leading to localized clashes.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_joint_gaya_tourism_charter", "Propose a joint tourism development charter for Gaya, inviting opposition ideas.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Rival boycott of tourism board meetings delays charter implementation.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2010-06
ITEMS_2006_2010.append(make_news(
    key="bh2010_2010_06_modi_poster_dispute",
    month="2010-06",
    title="Nitish Cancels BJP Dinner Over Narendra Modi Posters",
    desc="CM Nitish Kumar cancels a scheduled dinner for BJP leaders in Patna, protesting against posters showing him with Narendra Modi, drawing media focus.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("assert_secular_identity_and_alliances", "Assert the JD(U)'s independent secular identity while maintaining the state alliance.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "BJP local units express anger, threatening to review coalition terms.", eff(-2, 0, -2, -2)), 1.2),
        reaction("label_dispute_as_opportunistic_drama", "Label the dispute as opportunistic drama, alleging that JD(U) and BJP are complicit on ground.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(15, "NDA leaders hold joint press meets, neutralizing the opportunism charges.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_bipartisan_secularism_charter", "Propose a joint assembly charter to explicitly define secularism rules for state parties.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Legislative disputes delay the charter draft, leaving tensions active.", eff(0, 0, -1, -1)), 1.15),
        no_comment(weight=0.25)
    ]
))

# 2010-07
ITEMS_2006_2010.append(make_news(
    key="bh2010_2010_07_seemanchal_floods",
    month="2010-07",
    title="Mahananda River Floods Rural Seemanchal Districts",
    desc="Heavy rainfall in Seemanchal causes the Mahananda river to overflow, flooding agricultural lands and villages in Araria and Purnia districts.",
    tags=['disaster_relief', 'rural'],
    base_w=1.2, profile="disaster_relief",
    reactions=[
        reaction("deploy_boats_and_distribute_food", "Deploy rescue boats, distribute dry food packets, and waive local crop cess in Seemanchal.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Bureaucratic delay in checking crop losses sparks farmer sit-ins in town.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_compensation_package_per_acre_seemanchal", "Demand that the state release Rs 3,000 per acre compensation for ruined crops.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Finance department states flood budgets are already committed, delaying relief.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_embankment_safety_commission", "Propose a joint Nepal-Bihar river safety commission to monitor dam releases during monsoon.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Diplomatic protocols delay the commission meetings, keeping monsoon active.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2010-08
ITEMS_2006_2010.append(make_news(
    key="bh2010_2010_08_service_act_passed",
    month="2010-08",
    title="Assembly Passes Right to Public Services Act",
    desc="The Bihar Assembly passes the landmark Right to Public Services Act, guaranteeing delivery of key documents within specified timelines.",
    tags=['governance'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("enforce_act_and_set_up_monitoring_cells", "Enforce the act, set up monitoring cells in all districts, and penalize delayed officers.",
                 ['GOVERNMENT'], eff(3, 0, 4, 5),
                 {},
                 risk(15, "Bureaucratic lobbies delay registries, protesting against penalty rules.", eff(-1, 0, -2, -2)), 1.25),
        reaction("demand_judicial_appeal_clauses_rtps", "Demand judicial appeal clauses, alleging that block officers will pass bad orders to avoid penalties.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Ruling party points to existing grievance boards, neutralizing criticism.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_digitized_counters_extension", "Propose extending single-window digitized counters to all gram panchayat offices.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Power cuts and network delays keep counters offline in remote blocks.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 1}, weight=0.2)
    ]
))

# 2010-09
ITEMS_2006_2010.append(make_news(
    key="bh2010_2010_09_assembly_schedules",
    month="2010-09",
    title="EC Announces Six-Phase Bihar Assembly Election Schedule",
    desc="The EC announces a six-phase Bihar assembly election schedule for October-November, setting the code of conduct active.",
    tags=['election'],
    base_w=1.25, profile="election",
    reactions=[
        reaction("campaign_on_development_achievements_and_sushasan", "Campaign on the government's developmental achievements, showing road and bridge growth.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Opposition highlights instances of contract teacher strikes in districts.", eff(0, 0, -2, -2)), 1.2),
        reaction("campaign_on_social_neglect_of_marginalized_dalits", "Campaign aggressively on social neglect of marginalized Dalits, calling sushasan a media eyewash.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "NDA wins several rural seats due to strong EBC support equations.", eff(-1, 0, -1, -1)), 1.25),
        reaction("propose_bipartisan_polling_monitoring", "Propose requesting the EC to install CCTV cameras in all sensitive rural booths.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Technical errors in remote booths leave cameras offline on polling day.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2010-10
ITEMS_2006_2010.append(make_news(
    key="bh2010_2010_10_joint_campaigns",
    month="2010-10",
    title="Nitish and Sushil Modi Launch Joint Campaigns",
    desc="Displaying strong alliance unity to counter poster disputes, CM Nitish Kumar and BJP leader Sushil Modi launch joint campaigns in Sonepur.",
    tags=['politics', 'election'],
    base_w=1.2, profile="election",
    reactions=[
        reaction("advertise_coalition_unity_and_coordination", "Advertise the coalition's unity and coordinate joint worker meets in all blocks.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "RJD candidates split the backward class voter share in key blocks.", eff(0, 0, -2, -1)), 1.2),
        reaction("highlight_alliance_ideological_contradictions", "Highlight ideological differences between JDU and BJP on secular issues, calling them unstable.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "NDA resolves the disputes quickly, reducing the impact of criticism.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_bipartisan_agricultural_charter", "Propose drafting a joint agricultural development charter to protect crop support prices.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Delayed hearings prevent the charter from being signed by both camps.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2010-11
ITEMS_2006_2010.append(make_news(
    key="bh2010_2010_11_nda_landslide",
    month="2010-11",
    title="NDA Wins Historic Landslide in Bihar; Nitish Sworn In",
    desc="The JD(U)-BJP alliance wins a historic landslide of 206 out of 243 seats, reducing the RJD to 22. Nitish Kumar is sworn in as CM.",
    tags=['election', 'politics'],
    base_w=1.35, profile="election",
    reactions=[
        reaction("declare_triumph_of_development_and_sushasan_bihar", "Declare this as the triumph of development, and announce new road projects.",
                 ['GOVERNMENT'], eff(3, 0, 4, 5),
                 {},
                 risk(18, "Opposition alleges EVM tampering in three urban districts.", eff(-1, 0, -2, -2)), 1.25),
        reaction("accept_mandate_vow_to_reorganize_opposition", "Accept the mandate, stating that RJD will reorganize its cadres to defend secularism.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(14, "Local party workers express frustration over losing cabinet influence.", eff(-1, 0, -2, -1)), 1.2),
        reaction("propose_bipartisan_development_board_bihar", "Propose forming a bipartisan state development board to recommend highway priorities.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Fierce leader rivalries prevent the board from holding its first meeting.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.15)
    ]
))

# 2010-12
ITEMS_2006_2010.append(make_news(
    key="bh2010_2010_12_welfare_pension_hike",
    month="2010-12",
    title="New Cabinet Approves Hikes in Widows and Disability Pensions",
    desc="The newly sworn-in cabinet approves doubling the monthly welfare pension for widows and disabled, as a post-election developmental action.",
    tags=['governance', 'welfare'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("rollout_pension_hikes_immediately", "Rollout the pension hikes immediately through block welfare officers.",
                 ['GOVERNMENT'], eff(3, 0, 4, 5),
                 {},
                 risk(15, "Audit reports expose siphoning of pension funds in two districts, drawing bad press.", eff(-1, -1, -2, -2)), 1.25),
        reaction("demand_further_increase_to_match_inflation", "Demand the government further increase the pension to match inflation rates, calling the hike small.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Finance department states budget limits prevent further hikes.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_pension_auditing_boards", "Propose setting up block-level audit boards with parent and youth representatives.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Lack of volunteer interest keeps the audit boards vacant.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 1}, weight=0.25)
    ]
))

