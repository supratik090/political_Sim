from helper import reaction, no_comment, make_news, eff, risk

ITEMS_2006_2010 = []

# 2006-01
ITEMS_2006_2010.append(make_news(
    key="tn2006_2006_01_free_tv_rice_promises",
    month="2006-01",
    title="DMK Manifesto Promises Free TVs and Rs 2/kg Rice",
    desc="The DMK releases its assembly election manifesto, promising to distribute free color televisions to every household and supply rice at Rs 2 per kg under the public distribution system.",
    tags=['politics', 'welfare'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("dismiss_promises_as_economic_ruin", "Dismiss the promises as fiscally ruinous and warn that the state will face massive debt.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(16, "Rural voters show high enthusiasm for the welfare promises in initial polls.", eff(0, 0, -2, -3)), 1.2),
        reaction("highlight_welfare_benefits_for_poor", "Highlight the television as an education tool and the cheap rice as a vital step to eliminate hunger.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 5),
                 {},
                 risk(14, "Finance columnists write critical editorials warning of budget deficits.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_targeted_welfare_model", "Propose that freebies be limited strictly to below-poverty-line (BPL) families to preserve the state budget.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Voters find targeted criteria confusing, favoring universal distribution schemes.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 2}, weight=0.2)
    ]
))

# 2006-02
ITEMS_2006_2010.append(make_news(
    key="tn2006_2006_02_alliance_scenarios",
    month="2006-02",
    title="PMK and MDMK Alliance Negotiations Intensify",
    desc="With assembly elections declared, regional groups PMK and MDMK hold parallel alliance negotiations with both major fronts, seeking maximum seat shares.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("offer_cabinet_berth_guarantees", "Offer cabinet berth guarantees and key district seats to secure the partners within the alliance.",
                 ['GOVERNMENT'], eff(2, 0, 2, 3),
                 {},
                 risk(15, "Internal party MLAs express anger over losing their sitting constituencies.", eff(-1, 0, -2, -2)), 1.15),
        reaction("demand_strict_seat_sharing_limits", "Demand strict seat-sharing limits to preserve the party's own grassroots candidate strength.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(14, "Partner parties walk away, opening talks with the rival coalition.", eff(-1, 0, -2, -2)), 1.25),
        reaction("propose_post_poll_governance_panel", "Propose establishing a post-poll steering committee to distribute powers equitably after elections.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Steering committee talks break down over coordinator choices.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2006-03
ITEMS_2006_2010.append(make_news(
    key="tn2006_2006_03_mdmk_switches_sides",
    month="2006-03",
    title="MDMK Switches Sides; Joins AIADMK Alliance",
    desc="In a major pre-election blow to the DMK-led DPA, Vaiko's MDMK formally switches sides and joins the AIADMK alliance after receiving a seat offer of 35 seats.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("welcome_mdmk_and_launch_joint_campaign", "Welcome the MDMK into the fold and launch a joint campaign highlighting the combined front's strength.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Sitting MLAs in the allotted 35 seats protest and refuse to coordinate campaign work.", eff(-1, 0, -2, -2)), 1.2),
        reaction("dismiss_departure_as_minor_loss", "Dismiss the departure as a minor loss, stating that MDMK's voter base has already shifted to the DPA.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Cadres in southern districts report increased local contest challenges.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_voter_loyalty_rallies", "Propose holding voter loyalty rallies in the contested districts to reassure grassroots supporters.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Heavy rain delays key loyalty rallies, reducing voter attendance.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2006-04
ITEMS_2006_2010.append(make_news(
    key="tn2006_2006_04_campaign_freebie_debates",
    month="2006-04",
    title="Campaign Highlights: Freebies vs Fiscal Prudence",
    desc="The assembly campaign debates center on the DMK's free TV and cheap rice promises versus the AIADMK's warnings of budget deficits and inflation.",
    tags=['election'],
    base_w=1.25, profile="election",
    reactions=[
        reaction("highlight_past_infrastructure_and_growth", "Focus on the state's industrial investments, IT parks, and road connectivity constructed under the regime.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Voters find infrastructure arguments less appealing than direct household welfare promises.", eff(0, 0, -1, -3)), 1.2),
        reaction("highlight_welfare_benefits_for_households", "Highlight the direct economic relief that free TVs and Rs 2/kg rice will bring to rural families.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 5),
                 {},
                 risk(12, "Critics warn that distribution logistics will lead to corruption and leaks.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_bipartisan_economic_advisory", "Propose establishing a bipartisan economic advisory council to review welfare funding sources.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Voters view the advisory proposal as a sign of hesitation to deliver benefits.", eff(-1, 0, -1, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2006-05
ITEMS_2006_2010.append(make_news(
    key="tn2006_2006_05_assembly_polls_dmk_wins",
    month="2006-05",
    title="DMK Minority Government Sworn In with Congress Support",
    desc="The assembly election results lead to a hung house. The DMK emerges as the single largest party and forms a minority government supported from outside by the Congress.",
    tags=['election', 'politics'],
    base_w=1.3, profile="election",
    reactions=[
        reaction("assert_regime_stability_and_welfare", "Assert that the coalition is stable and that all welfare promises will be fulfilled starting this week.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Congress allies demand a share in the cabinet, creating initial friction.", eff(-1, 0, -2, -2)), 1.2),
        reaction("label_government_as_weak_and_dependent", "Label the new regime a weak, dependent government that will collapse at the first disagreement.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(14, "Ruling party releases consensus development agenda, gaining positive press.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_legislative_coordination_committee", "Propose a formal legislative coordination committee representing all alliance partners to draft bills.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Delays in selecting the committee coordinator stall initial policy reviews.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.2)
    ]
))

# 2006-06
ITEMS_2006_2010.append(make_news(
    key="tn2006_2006_06_tv_rice_implementation",
    month="2006-06",
    title="CM Signs Orders for Rs 2/kg Rice and Free Color TVs",
    desc="In his first cabinet meeting, Chief Minister M. Karunanidhi signs files to implement the Rs 2 per kg rice scheme and orders tenders for the first phase of free color TVs.",
    tags=['governance', 'welfare'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("launch_tenders_and_ration_allocations", "Approve global tenders for television procurement and increase state grain allocations at ration shops.",
                 ['GOVERNMENT'], eff(2, 0, 3, 5),
                 {},
                 risk(18, "Opposition files cases alleging favoritism in selecting electronic suppliers.", eff(-1, 0, -2, -2)), 1.25),
        reaction("demand_investigation_into_tv_procurement_costs", "Expose procurement details, demanding an investigation into why public money is spent on commercial imports.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 3),
                 {},
                 risk(14, "Rural families express anger at the opposition for trying to stall the TV delivery.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_domestic_tv_assembly_hubs", "Propose that the TVs be assembled within the state to create employment for engineering graduates.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Supplier companies state that setting up local plants will take over a year.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 2}, weight=0.2)
    ]
))

# 2006-07
ITEMS_2006_2010.append(make_news(
    key="tn2006_2006_07_hogenakkal_survey",
    month="2006-07",
    title="Hogenakkal Water Supply Project Survey Sparks Row",
    desc="The Tamil Nadu government begins land and hydrological surveys for the Hogenakkal Drinking Water Project in Dharmapuri. Karnataka politicians raise strong objections.",
    tags=['governance', 'land_rights'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("assert_right_to_drinking_water_project", "Assert that Hogenakkal falls within state borders and continue the survey under police protection.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(16, "Karnataka activists stage protests near the border, disrupting commercial transport.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_all_party_border_delegation", "Demand the state government lead an all-party delegation to the Prime Minister to secure central protection.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "PMO delays meeting schedule due to ongoing Parliament session.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_joint_border_water_commission", "Propose a joint technical water commission with Karnataka representatives to verify water levels at Hogenakkal.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Karnataka government boycotts the commission, continuing its protests.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2006-08
ITEMS_2006_2010.append(make_news(
    key="tn2006_2006_08_local_polls_alliance",
    month="2006-08",
    title="Congress and DMK Negotiate Local Body Seat Sharing",
    desc="Tensions rise within the ruling alliance as local Congress committees demand a higher share of mayoral and ward seats for the upcoming civic body polls.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("concede_key_mayoral_seats_to_allies", "Concede the Madurai and Coimbatore mayoral candidacies to allies to preserve the front's stability.",
                 ['GOVERNMENT'], eff(2, 0, 2, 3),
                 {},
                 risk(15, "Local DMK district secretaries rebel, filing independent nominations in key wards.", eff(-1, 0, -2, -2)), 1.15),
        reaction("refuse_extra_seats_assert_party_strength", "Refuse to yield seats, stating that the party's own cadres are best placed to win municipal posts.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(14, "Allies run separate campaigns in several wards, splitting the alliance vote.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_joint_civic_manifesto", "Propose a joint civic manifesto focusing on city garbage disposal and sewer upgrades to unite both cadres.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(10, "Seat disputes overshadow the manifesto, reducing public interest.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2006-09
ITEMS_2006_2010.append(make_news(
    key="tn2006_2006_09_free_tv_first_phase",
    month="2006-09",
    title="First Phase of Free Color TV Distribution Launched",
    desc="The Chief Minister launches the first phase of Free Color TV distribution at a function in Chennai, handing over sets to poor families in selected slums.",
    tags=['governance', 'welfare'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("expand_distribution_to_rural_panchayats", "Expand the distribution drive to rural panchayats, prioritizing low-income households first.",
                 ['GOVERNMENT'], eff(2, 0, 3, 5),
                 {},
                 risk(15, "Villages report supply delays due to manufacturing backlogs, drawing local complaints.", eff(0, 0, -2, -2)), 1.25),
        reaction("expose_malfunctioning_tv_sets", "Expose reports of malfunctioning TV sets in some centers, accusing the government of buying cheap quality.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Suppliers quickly replace the damaged units, weakening the opposition critique.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_local_service_maintenance_centers", "Propose setting up local cooperative electronics repair centers to handle warranty issues and create jobs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Lack of trained technicians delays the repair center rollout.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 1}, weight=0.25)
    ]
))

# 2006-10
ITEMS_2006_2010.append(make_news(
    key="tn2006_2006_10_local_poll_violence",
    month="2006-10",
    title="Violence and Rigging Allegations Mar Chennai Civic Polls",
    desc="The Chennai Corporation elections witness clashes, booth-capturing allegations, and police lathi-charges. Opposition AIADMK demands re-polling in all wards.",
    tags=['security_crisis', 'election'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("reject_rigging_claims_order_limited_repoll", "Reject the systemic rigging claims but order re-polling in 12 specific booths where logs show anomalies.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(20, "Opposition files high court petition and launches a state-wide dharna over democracy murder.", eff(-1, 0, -2, -3)), 1.2),
        reaction("organise_mass_dharna_demand_commissioner_arrest", "Organize a mass dharna outside the State Election Commission, demanding the arrest of the commissioner.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "High court stays the protest, forcing cadres to disperse with minor injuries.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_cctv_and_central_forces_for_repoll", "Propose complete CCTV recording and central paramilitary force deployment for all re-polling wards.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Administrative delays in hiring cameras push back the poll dates.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"securityIgnoredMemory": 2}, weight=0.2)
    ]
))

# 2006-11
ITEMS_2006_2010.append(make_news(
    key="tn2006_2006_11_cauvery_tribunal_draft",
    month="2006-11",
    title="Cauvery Tribunal Draft Allocation Triggers Farmer Concerns",
    desc="The draft findings of the Cauvery Water Disputes Tribunal are circulated. Delta farmer groups express concerns that the proposed monthly allocations are insufficient.",
    tags=['land_rights', 'protest'],
    base_w=1.2, profile="land_rights",
    reactions=[
        reaction("submit_revision_memorandum_to_tribunal", "Submit an official revision memorandum to the tribunal demanding guaranteed shares during distressed years.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Tribunal delays reviewing the memorandum, keeping the draft unchanged.", eff(0, 0, -1, -2)), 1.15),
        reaction("lead_farmer_dharnas_demanding_assured_share", "Lead farmer dharnas outside central water offices, demanding the UPA government guarantee the state's water share.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Water department officials claim the allocations are final, stalling discussions.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_inter_state_farmers_council", "Propose setting up an inter-state non-political council of farmers to negotiate water sharing directly.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Neighboring state farmer unions boycott the council, citing regional interests.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 3}, weight=0.25)
    ]
))

# 2006-12
ITEMS_2006_2010.append(make_news(
    key="tn2006_2006_12_farm_loan_waiver",
    month="2006-12",
    title="State Government Waives Off Cooperative Farm Loans",
    desc="The state government announces a complete waiver of agricultural loans availed by small and marginal farmers from cooperative banks, totaling over Rs 3,000 crore.",
    tags=['governance', 'welfare'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("release_matching_funds_to_cooperative_banks", "Release matching state budget funds to cooperative banks to restore their lending capacities immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 5),
                 {},
                 risk(18, "Commercial banks refuse to extend new credits, claiming cooperative debts are risky.", eff(0, 0, -2, -2)), 1.25),
        reaction("demand_nationalized_bank_loan_waiver_too", "Demand that nationalized commercial banks waive off all agricultural debts too, calling the state scheme partial.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Union Finance Ministry rejects the demand, citing national credit norms.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_crop_insurance_integration", "Propose integrating the waiver with a compulsory crop insurance scheme to prevent future defaults.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Insurance enrollment processes are slow, leaving many farmers uncovered.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 1}, weight=0.2)
    ]
))

# 2007-01
ITEMS_2006_2010.append(make_news(
    key="tn2007_2007_01_samacheer_kalvi_panel",
    month="2007-01",
    title="Uniform Education System Feasibility Committee Set Up",
    desc="The government appoints a high-level committee to study the feasibility of implementing a Uniform System of School Education (Samacheer Kalvi) across all schools.",
    tags=['governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("approve_uniform_syllabus_recommendations", "Approve the committee's recommendation to unify State Board, Matriculation, and Anglo-Indian syllabi.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Private school managements protest, claiming the uniform syllabus dilutes quality.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_retention_of_choice_and_quality", "Demand that private schools retain their syllabus choices, accusing the government of ideological control.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Parent-teacher associations support the uniform syllabus, reducing opposition impact.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_gradual_syllabus_phasing", "Propose a phased introduction starting with primary classes to allow teacher training and book printings.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Printing delays leave several schools without new books in the first term.", eff(0, 0, -2, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2007-02
ITEMS_2006_2010.append(make_news(
    key="tn2007_2007_02_cauvery_final_verdict",
    month="2007-02",
    title="Cauvery Water Tribunal Delivers Final Verdict",
    desc="The Cauvery Water Disputes Tribunal delivers its final verdict, allocating 419 tmc ft of water annually to Tamil Nadu. Karnataka plans to appeal in the Supreme Court.",
    tags=['land_rights'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("demand_immediate_gazetting_of_verdict", "Welcome the verdict and demand the central government immediately gazette the order to make it legally binding.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Central government delays gazetting due to upcoming elections in Karnataka.", eff(-1, 0, -2, -2)), 1.2),
        reaction("condemn_center_delay_hold_black_flag_protests", "Condemn the central government's delay in gazetting the verdict and hold black-flag protests.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Ruling party accuses the opposition of trying to damage relations with the Centre.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_joint_basin_audit_board", "Propose a joint basin audit board representing both states to monitor water storage levels weekly.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Karnataka officials decline the audit board, citing sovereignty over their dams.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 3}, weight=0.2)
    ]
))

# 2007-03
ITEMS_2006_2010.append(make_news(
    key="tn2007_2007_03_metro_rail_planning",
    month="2007-03",
    title="Chennai Metro Rail Proposal Sent for Central Clearance",
    desc="The state government submits the detailed project report (DPR) for Phase I of the Chennai Metro Rail Project, seeking cabinet approvals and financial tie-ups.",
    tags=['governance', 'infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("negotiate_international_soft_loans", "Negotiate soft loans with international funding agencies (like JICA) to secure low-interest capital.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Negotiation terms demand matching land acquisition speed, creating local pressures.", eff(0, 0, -1, -1)), 1.2),
        reaction("expose_potential_corridor_displacements", "Expose maps of proposed corridors, claiming that hundreds of heritage commercial buildings will be demolished.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Metro planners alter designs to tunnel underground, neutralizing the critique.", eff(0, 0, -1, -1)), 1.2),
        reaction("propose_monorail_extension_to_suburbs", "Propose a cheaper Monorail extension to connect far-off suburbs with the main Metro stations.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(8, "Technical coordination between Metro and Monorail designs delays approvals.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2007-04
ITEMS_2006_2010.append(make_news(
    key="tn2007_2007_04_neyveli_lignite_protests",
    month="2007-04",
    title="NLC Contract Workers Strike Over Regularization",
    desc="Over 10,000 contract workers at the Neyveli Lignite Corporation (NLC) launch an indefinite strike, demanding job regularization and equal pay as permanent staff.",
    tags=['protest'],
    base_w=1.15, profile="protest",
    reactions=[
        reaction("mediate_with_union_and_ministry", "Appoint a state labor team to mediate between union leaders and the central coal ministry to find a compromise.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Coal ministry rejects immediate regularization, leading to resumption of strike.", eff(-1, 0, -2, -2)), 1.2),
        reaction("support_nlc_workers_blockade_gates", "Join the strike in solidarity, blockading NLC gates and demanding that the CM intervene personally.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Power generation drops, causing brief power cuts across northern districts.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_phased_induction_policy", "Propose a phased induction policy to regularize 1,000 workers annually based on seniority.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Radical sections of the union reject the phased model, demanding total relief.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2007-05
ITEMS_2006_2010.append(make_news(
    key="tn2007_2007_05_madurai_dinakaran_attack",
    month="2007-05",
    title="Madurai Office of 'Dinakaran' Newspaper Attacked by Protestors",
    desc="A violent crowd attacks the Madurai office of the 'Dinakaran' newspaper after it publishes a survey showing M.K. Stalin as the preferred successor to the CM over Alagiri.",
    tags=['security_crisis', 'politics'],
    base_w=1.3, profile="security_crisis",
    reactions=[
        reaction("order_police_action_refer_to_cbi", "Condemn the violence, order the immediate arrest of the attackers, and refer the case to the CBI.",
                 ['GOVERNMENT'], eff(2, -1, 3, 3),
                 {},
                 risk(20, "Ruling family divisions spill into the open, causing administrative confusion.", eff(-2, 0, -2, -3)), 1.2),
        reaction("demand_resignation_of_home_minister", "Accuse the government of failing to protect the press and demand the resignation of the minister handling police.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Ruling party points to the arrests made, calling the demand political posturing.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_press_protection_bill", "Propose a state bill to provide special security and legal protections to media houses during political rows.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Journalist unions call the bill a token gesture, demanding wider law and order action.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"securityIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2007-06
ITEMS_2006_2010.append(make_news(
    key="tn2007_2007_06_free_gas_stoves",
    month="2007-06",
    title="Government Launches Free Gas Stoves and LPG Scheme",
    desc="The state government launches a major welfare scheme to distribute free gas stoves and provide LPG cylinder connections to rural women to replace wood-fired stoves.",
    tags=['governance', 'welfare'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("expedite_gas_stove_procurements", "Expedite stove procurements and setup local cylinder distribution agencies in rural hubs.",
                 ['GOVERNMENT'], eff(2, 0, 3, 5),
                 {},
                 risk(16, "Refill cylinder prices rise nationally, making it hard for poor families to buy refills.", eff(0, 0, -2, -2)), 1.25),
        reaction("demand_kerosene_ration_increase_instead", "Demand that the government increase the cheap kerosene ration instead, calling gas connections a burden.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Rural women welcome the clean stoves, ignoring the kerosene arguments.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_bio_gas_subsidies_alternative", "Propose matching subsidies for community biogas units in cattle-rearing villages as a cheaper alternative.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Maintenance issues in community bio-gas tanks keep them mostly offline.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 1}, weight=0.25)
    ]
))

# 2007-07
ITEMS_2006_2010.append(make_news(
    key="tn2007_2007_07_nanguneri_sez_land",
    month="2007-07",
    title="Land Acquisition Protests Erupt for Nanguneri SEZ",
    desc="Farmers and local activists in Tirunelveli district protest against the acquisition of agricultural land for the proposed Nanguneri Special Economic Zone.",
    tags=['land_rights', 'protest'],
    base_w=1.2, profile="land_rights",
    reactions=[
        reaction("raise_compensation_guarantee_jobs", "Announce a 30% hike in land compensation and guarantee one job per affected family in the incoming industries.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Private developers object to job guarantees, delaying investment commitments.", eff(0, 0, -2, -2)), 1.25),
        reaction("join_farmers_rally_demand_barren_land_use", "Join the farmers' rally, demanding that the SEZ be relocated to barren land in adjacent blocks.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Local builders and contractors accuse the party of blocking development in Nellai.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_leasing_model_for_farmers", "Propose a lease model where farmers retain land ownership and receive monthly rentals from the industries.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Legal structures for long-term corporate leases are delayed in assembly.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 2}, weight=0.2)
    ]
))

# 2007-08
ITEMS_2006_2010.append(make_news(
    key="tn2007_2007_08_sethusamudram_shipping_row",
    month="2007-08",
    title="Sethusamudram Shipping Canal Controversy Escalates",
    desc="The Sethusamudram Shipping Canal Project sparks debate. Conservative groups and opposition parties claim that dredging the canal will damage the Ram Setu bridge.",
    tags=['politics', 'identity'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("assert_economic_benefits_of_canal", "Defend the project, stating that the canal will reduce shipping times and bring massive growth to southern ports.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Conservative organizations launch state-wide human chain protests and blockades.", eff(-1, 0, -2, -2)), 1.2),
        reaction("oppose_dredging_demand_route_alignment", "Oppose the current dredging route, demanding the project be aligned to bypass the Ram Setu structure.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Industrial associations criticize the opposition for stalling crucial shipping infra.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_scientific_archeological_study", "Propose an independent commission of marine archeologists to study the structure before dredging proceeds.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Supreme Court halts dredging pending study submissions, delaying the project.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.2)
    ]
))

# 2007-09
ITEMS_2006_2010.append(make_news(
    key="tn2007_2007_09_lord_ram_remarks_row",
    month="2007-09",
    title="CM Karunanidhi's Remarks on Lord Ram Cause Row",
    desc="Chief Minister Karunanidhi makes controversial remarks questioning the historical existence of Lord Ram during a speech on the Sethusamudram project, drawing protests.",
    tags=['politics', 'identity'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("defend_remarks_as_rationalist", "Defend the statements as consistent with the rationalist Dravidian ideology of social reformer Periyar.",
                 ['GOVERNMENT'], eff(2, 0, 2, 2),
                 {},
                 risk(20, "Conservative bodies call for a state-wide bandh, leading to minor clashes in temple towns.", eff(-2, 0, -2, -3)), 1.2),
        reaction("condemn_remarks_demand_apology", "Condemn the remarks as an insult to millions of believers and demand an immediate public apology from the CM.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Rationalist forums organize counter-rallies, accusing the opposition of communalism.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_focus_on_dredging_logistics", "Propose that both sides move past theological arguments and focus on the project's financial feasibility.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Media ignores the financial arguments, keeping focus on the religious row.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.2)
    ]
))

# 2007-10
ITEMS_2006_2010.append(make_news(
    key="tn2007_2007_10_sethusamudram_sc_stay",
    month="2007-10",
    title="Supreme Court Stays Sethusamudram Dredging at Ram Setu",
    desc="The Supreme Court issues an interim stay on dredging activities at the Ram Setu site, responding to petitions regarding environmental impact and cultural heritage.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("comply_with_stay_prepare_scientific_affidavit", "Comply with the stay order, directing state geologists to prepare detailed data for the next hearing.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(15, "Coalition allies express frustration over the judicial delay, creating minor friction.", eff(-1, 0, -1, -1)), 1.15),
        reaction("hail_stay_demand_permanent_alignment_change", "Hail the stay as a victory for cultural heritage and demand a permanent cancellation of the current route.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "Port worker unions complain that the stay delays shipping sector employment.", eff(-1, 0, -1, -1)), 1.2),
        reaction("propose_environmental_panel_inclusion", "Propose adding independent environmentalists to the state legal team to present a balanced view.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Selecting acceptable panel members delays the court affidavit submission.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2007-11
ITEMS_2006_2010.append(make_news(
    key="tn2007_2007_11_dmk_youth_wing_nellai",
    month="2007-11",
    title="DMK Youth Wing Conference in Nellai Showcases Stalin's Leadership",
    desc="A massive DMK Youth Wing Conference is held in Tirunelveli (Nellai). The event focuses on M.K. Stalin's leadership, signaling a succession transition within the party.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("promote_youth_leaders_to_district_posts", "Approve the elevation of several youth wing members to district administrative posts to revitalize the party.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Older senior leaders express resentment over being sidelined by younger cadres.", eff(-1, 0, -2, -2)), 1.15),
        reaction("criticize_dynastic_succession_rallies", "Hold public campaigns criticizing the transition as dynastic politics, calling it a disregard for democratic merit.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Ruling party releases lists of opposition family members in politics, neutralizing impact.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_youth_representation_bill", "Propose a legislative resolution encouraging all parties to reserve 20% of assembly tickets for youth candidates.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Rival parties ignore the proposal, calling it a PR distraction.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2007-12
ITEMS_2006_2010.append(make_news(
    key="tn2007_2007_12_ecr_demolition_notices",
    month="2007-12",
    title="Demolition Notices Issued to ECR Resorts for CRZ Violations",
    desc="The Coastal Zone Management Authority issues demolition notices to several luxury resorts and private villas along the East Coast Road (ECR) for violating environmental rules.",
    tags=['governance'],
    base_w=1.1, profile="governance",
    reactions=[
        reaction("enforce_demolitions_for_coastal_protection", "Enforce the notices strictly, stating that no commercial violations will be tolerated on coastal zones.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(16, "Resort owners association files a court appeal, securing a stay on notices.", eff(-1, 0, -2, -1)), 1.2),
        reaction("demand_enforcement_on_major_corporate_builders", "Demand that the state focus demolitions on major corporate builders rather than small local fishing homes.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Fishermen unions state that their residential zones are unaffected, dulling the issue.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_coastal_eco_tourism_guidelines", "Propose drafting clear eco-tourism guidelines that allow low-impact resorts while protecting the coast.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Drafting guidelines delays enforcement, allowing violations to remain active.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2008-01
ITEMS_2006_2010.append(make_news(
    key="tn2008_2008_01_muslim_sub_quota",
    month="2008-01",
    title="Government Introduces 3.5% Muslim Sub-Quota",
    desc="The state government passes an ordinance providing a 3.5% sub-quota for Muslims within the Backward Classes reservation pool in government jobs and education.",
    tags=['politics', 'identity'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("enforce_sub_quota_in_admissions", "Implement the sub-quota immediately for the current academic admissions cycle.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Other backward communities express concern about reduced general BC seats.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_sub_quota_for_other_neglected_groups", "Demand similar sub-quotas for other neglected backward communities, calling the policy selective.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Minority organizations accuse the party of seeking to block their benefits.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_comprehensive_backwardness_survey", "Propose a fresh socio-economic survey to scientificially determine backwardness prior to splitting quotas.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Survey execution delays recruitment processes, causing anger among job seekers.", eff(-1, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.2)
    ]
))

# 2008-02
ITEMS_2006_2010.append(make_news(
    key="tn2008_2008_02_sethusamudram_resolution",
    month="2008-02",
    title="Assembly Resolution Urges Centre to Complete Shipping Canal",
    desc="The Tamil Nadu Assembly passes a resolution urging the central government to complete the Sethusamudram Shipping Canal Project on the current alignment without delays.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("send_resolution_delegation_to_delhi", "Send a ministerial delegation to Delhi to submit the resolution to the Prime Minister.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Central ministries request patience citing ongoing Supreme Court stay hearings.", eff(0, 0, -1, -1)), 1.15),
        reaction("boycott_resolution_assembly_session", "Boycott the assembly vote, claiming the resolution disregards the religious sentiments of millions.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(14, "Ruling party uses the boycott to label the opposition as anti-development.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_bipartisan_legal_consultation", "Propose a bipartisan committee of legal experts to draft a joint affidavit for the Supreme Court.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Disagreements over Ram Setu's status prevent the committee from drafting the affidavit.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2008-03
ITEMS_2006_2010.append(make_news(
    key="tn2008_2008_03_hogenakkal_foundation",
    month="2008-03",
    title="Foundation Stone Laid for Hogenakkal Drinking Water Project",
    desc="Chief Minister Karunanidhi lays the foundation stone for the Hogenakkal Drinking Water Project. Protests break out in Karnataka, with calls to boycott Tamil goods.",
    tags=['governance', 'land_rights'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("declare_project_will_proceed_on_schedule", "Declare that the project is vital for the fluorosis-affected districts of Dharmapuri and will proceed on schedule.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Border transport links are shut down by protestors, causing trade losses.", eff(-1, 0, -2, -2)), 1.25),
        reaction("condemn_karnataka_protests_demand_security", "Condemn the attacks on Tamil establishments in Bangalore and demand central security for border areas.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Union Home ministry urges both states to show restraint, delaying central force dispatch.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_tripartite_water_sharing_talks", "Propose immediate tripartite talks between the two state CMs and the central water resources minister.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Karnataka government declines talks until after their state elections.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.2)
    ]
))

# 2008-04
ITEMS_2006_2010.append(make_news(
    key="tn2008_2008_04_hogenakkal_on_hold",
    month="2008-04",
    title="CM Temporarily Puts Hogenakkal Water Project on Hold",
    desc="Chief Minister Karunanidhi announces that the Hogenakkal project will be put on temporary hold until elections in Karnataka are completed, to avoid provoking communal rows.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("defend_decision_as_responsible_statesmanship", "Defend the decision as responsible statesmanship to protect Tamil lives and properties in Karnataka.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(18, "Opposition labels the decision as surrender, staging protests in Dharmapuri.", eff(-1, 0, -2, -3)), 1.2),
        reaction("condemn_deferral_as_cowardly_surrender", "Condemn the deferral as a cowardly surrender of state rights, demanding immediate resumption of work.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Ruling party points out that the pause is brief, neutralizing some criticism.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_construction_of_local_storage_first", "Propose constructing internal distribution pipes within Dharmapuri first while waiting for border clearances.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Contractors refuse to lay pipes without source reservoir clarity, delaying work.", eff(0, 0, -2, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2008-05
ITEMS_2006_2010.append(make_news(
    key="tn2008_2008_05_noyyal_river_pollution",
    month="2008-05",
    title="Farmers in Erode Protest Noyyal River Pollution",
    desc="Farmer organizations block local highways in Erode, protesting against the discharge of untreated chemical effluents from Tiruppur dyeing units into the Noyyal river.",
    tags=['protest', 'land_rights'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("order_inspection_of_dyeing_units", "Order state pollution board to inspect the dyeing units and seal those without zero liquid discharge (ZLD) systems.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Dyeing owners threaten layoffs, leading to protests by textile labor unions.", eff(-1, 0, -2, -2)), 1.25),
        reaction("lead_farmers_march_to_pollution_board", "Lead a farmers' march to the state pollution control board office demanding permanent closure of violating units.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Textile export associations warning of order cancellations and job losses receives press.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_common_effluent_plant_subsidies", "Propose state subsidies for establishing Common Effluent Treatment Plants (CETPs) in textile zones.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Construction of CETPs is delayed by land dispute clearances.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 2}, weight=0.2)
    ]
))

# 2008-06
ITEMS_2006_2010.append(make_news(
    key="tn2008_2008_06_decentralization_report",
    month="2008-06",
    title="Committee Submits Local Body Decentralization Report",
    desc="The state committee on administrative reforms submits its report, recommending the transfer of health and primary education budgets directly to municipal councils.",
    tags=['governance'],
    base_w=1.1, profile="governance",
    reactions=[
        reaction("accept_decentralization_reforms", "Accept the report recommendations and initiate legislative bills to transfer primary health funds to corporations.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "State department officers association protests their loss of administrative oversight.", eff(-1, 0, -2, -1)), 1.2),
        reaction("demand_strict_bureaucratic_audit_first", "Demand that the government first conduct a financial audit of municipal expenditures before transferring new budgets.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Mayors accuse the opposition of blocking local municipal empowerment.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_phased_budget_devolution", "Propose a pilot run in two corporations to test the budget transfer mechanism before a state-wide rollout.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Bureaucratic delays keep the pilot guidelines stuck in department files.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2008-07
ITEMS_2006_2010.append(make_news(
    key="tn2008_2008_07_pmk_withdraws_support",
    month="2008-07",
    title="PMK Withdraws Support from DMK minority State Government",
    desc="The Pattali Makkal Katchi (PMK) announces the withdrawal of its support from the DMK minority state government, citing differences over reservation and local issues.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("assert_legislative_majority_with_allies", "Reassure that the government remains stable with the backing of Congress and Left parties, dismissing the pullout.",
                 ['GOVERNMENT'], eff(1, 0, 2, 3),
                 {},
                 risk(15, "Left parties express minor differences over central fuel price hikes, increasing tension.", eff(-1, 0, -2, -2)), 1.15),
        reaction("demand_immediate_floor_test_in_assembly", "Label the government unstable and demand the Governor order an immediate floor test in the assembly.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(14, "Ruling party coordinates with Congress, passing a voice vote easily during budget.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_all_party_coordination_charter", "Propose a new legislative coordination charter to discuss bill amendments with all parties before voting.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Rival parties reject the charter, focusing on seat bargaining.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2008-08
ITEMS_2006_2010.append(make_news(
    key="tn2008_2008_08_metro_rail_approval",
    month="2008-08",
    title="Union Cabinet Approves Chennai Metro Rail Project Funding",
    desc="The Union Cabinet formally approves the Chennai Metro Rail Project Phase I, committing to share 50% of the project cost under joint ownership with the state.",
    tags=['governance', 'infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("commence_route_demarcation_and_tenders", "Commence the route demarcation and issue international tenders for tunneling and coach imports.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(14, "Shopkeepers in historical commercial zones launch protests against land acquisition.", eff(-1, 0, -1, -2)), 1.2),
        reaction("demand_compensation_at_market_rates_for_shops", "Support the shopkeepers, demanding that the government pay 300% market rate compensation for acquisitions.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Transit advocates write columns criticizing the opposition for delaying public transport.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_elevated_corridors_to_reduce_cost", "Propose modifying the design to use elevated corridors instead of underground tunnels to reduce acquisition costs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Metro planners reject elevated design in old heritage zones due to narrow roads.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2008-09
ITEMS_2006_2010.append(make_news(
    key="tn2008_2008_09_financial_crisis_impact",
    month="2008-09",
    title="Global Financial Crisis Hits Sriperumbudur Automobile Hub",
    desc="The global financial downturn leads to export order cancellations, hitting the automobile and electronic manufacturing hubs in Sriperumbudur and Oragadam.",
    tags=['economy'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("announce_manufacturing_incentive_package", "Announce an emergency state incentive package reducing electricity duty for export-oriented factories.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(15, "Revenue department warns of tax collections falling below state targets.", eff(0, 0, -2, -2)), 1.2),
        reaction("expose_layoff_rates_demand_labor_safety", "Expose job loss statistics, demanding the state government ban lay-offs of contract assembly staff.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Manufacturing associations claim strict ban will force factory closures.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_re_skilling_grants_for_labor", "Propose state-backed re-skilling grants for laid-off youth to transition to food processing industries.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Coordination delays with technical colleges keep the grants offline.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"economyIssueMissed": 1}, weight=0.25)
    ]
))

# 2008-10
ITEMS_2006_2010.append(make_news(
    key="tn2008_2008_10_sl_war_resolution",
    month="2008-10",
    title="Assembly Resolution Demands Indian Intervention for SL Ceasefire",
    desc="As the Sri Lankan Civil War intensifies, the Tamil Nadu Assembly passes a resolution urging the central government to halt military assistance and demand a ceasefire.",
    tags=['politics', 'identity'],
    base_w=1.3, profile="politics",
    reactions=[
        reaction("threaten_resignation_of_mps_to_center", "Threaten that state MPs will resign from the central cabinet if India does not enforce an immediate ceasefire.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(20, "Central ministries state that foreign policy cannot be dictated by state-level demands.", eff(-1, 0, -2, -2)), 1.2),
        reaction("condemn_empty_threats_demand_immediate_pullout", "Condemn the MP resignation threats as an empty drama and demand the ruling party pull out of UPA cabinet today.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 5),
                 {},
                 risk(14, "Ruling party releases correspondence proving active lobbying with the PM.", eff(0, 0, -1, -1)), 1.3),
        reaction("propose_relief_consignment_delegation", "Propose sending a joint all-party relief consignment of food and medicines to northern Sri Lanka under UN flags.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Sri Lankan government delays clearance for the consignment ship at Colombo.", eff(0, 0, -2, -1)), 1.15),
        no_comment(hidden={"identityIssueMissed": 3}, weight=0.15)
    ]
))

# 2008-11
ITEMS_2006_2010.append(make_news(
    key="tn2008_2008_11_all_party_sl_protest",
    month="2008-11",
    title="All-Party Rally Demands Halt of Indian Military Aid to SL",
    desc="A massive all-party rally is organized in Chennai. Leaders demand the UPA government immediately stop radar and logistics support to the Sri Lankan army.",
    tags=['protest'],
    base_w=1.25, profile="protest",
    reactions=[
        reaction("convey_rally_views_to_prime_minister", "Convey the unanimous views of the rally to the Prime Minister during a personal cabinet meet in Delhi.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Defense analysts write columns asserting that India cannot compromise regional security interests.", eff(-1, 0, -1, -1)), 1.15),
        reaction("lead_student_picketing_of_central_offices", "Lead student wing picketing of central government passport and railway offices across the state.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Police arrests several student protestors, leading to minor injuries and local disruption.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_refugee_rehabilitation_fund", "Propose establishing a special state fund to build permanent concrete housing for Sri Lankan Tamil refugees in camps.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Central intelligence agencies raise security objections over permanent camp housing.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2008-12
ITEMS_2006_2010.append(make_news(
    key="tn2008_2008_12_human_chain_sl_tamils",
    month="2008-12",
    title="State-wide Human Chain Protest in Support of SL Tamils",
    desc="Thousands of citizens, students, and political workers form a massive human chain across the state capital in support of civilian protection in the Sri Lankan war zone.",
    tags=['protest', 'identity'],
    base_w=1.2, profile="identity",
    reactions=[
        reaction("participate_in_chain_with_ministers", "Direct all cabinet ministers to participate in the human chain to express solidarity with the civilian struggle.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Opposition claims the ministers are protest-acting while retaining central cabinet posts.", eff(-1, 0, -2, -2)), 1.2),
        reaction("condemn_government_double_standards_on_war", "Expose state budget items funding central police academies, accusing the govt of double standards on security.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Voters find the comparison far-fetched, ignoring the double standard argument.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_peace_envoy_delegation_to_un", "Propose sending an unofficial delegation of cultural leaders to the UN Human Rights Council in Geneva.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Visa and diplomatic passport clearance delays prevent the delegation from traveling.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 1}, weight=0.25)
    ]
))

# 2009-01
ITEMS_2006_2010.append(make_news(
    key="tn2009_2009_01_sl_war_casualties_rage",
    month="2009-01",
    title="Sri Lankan Civil War Casualties Trigger Protests in State",
    desc="Reports of high civilian casualties in the Mullaitivu region of Sri Lanka trigger intense protests across Tamil Nadu, with several self-immolation incidents.",
    tags=['security_crisis', 'identity'],
    base_w=1.35, profile="security_crisis",
    reactions=[
        reaction("appeal_for_calm_and_dispatch_relief", "Appeal for public calm, announce state compensation for self-immolation families, and send emergency relief materials.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(20, "Protestors call the compensation an insult, storming government offices in central districts.", eff(-2, 0, -2, -3)), 1.2),
        reaction("condemn_congress_and_dmk_for_complicity", "Condemn the ruling UPA for complicity in the war and demand immediate withdrawal of all support to the Centre.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 5),
                 {},
                 risk(14, "Police makes preventive arrests of key leaders under assembly guidelines.", eff(-1, 0, -2, -1)), 1.3),
        reaction("propose_refugee_camp_safety_resolution", "Propose a unanimous assembly resolution demanding that international observers be allowed into Sri Lankan refugee camps.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Central government declines to forward the resolution, citing diplomatic limits.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 3}, weight=0.15)
    ]
))

# 2009-02
ITEMS_2006_2010.append(make_news(
    key="tn2009_2009_02_ls_alliance_shifts",
    month="2009-02",
    title="PMK and MDMK Join AIADMK Alliance for Lok Sabha Polls",
    desc="Ahead of the general elections, the PMK and MDMK formally join the AIADMK-led alliance, creating a strong consolidated front against the DMK-Congress camp.",
    tags=['politics'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("launch_joint_campaign_highlighting_dpa_failures", "Launch a joint campaign, highlighting the ruling front's failures on power cuts and the Sri Lankan issue.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Cadres of allied parties dispute local campaign budgets, causing minor friction.", eff(-1, 0, -2, -1)), 1.2),
        reaction("dismiss_alliance_as_defeated_combination", "Dismiss the alliance as a grouping of parties that lost the previous Lok Sabha contests, expressing confidence.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Combined voting percentage of the new front looks high in initial poll logs.", eff(-1, 0, -2, -2)), 1.15),
        reaction("propose_federal_growth_charter", "Propose a growth charter detailing how the regional alliance will secure federal funds for state projects.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "National parties ignore the regional charter, focusing on national stability themes.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2009-03
ITEMS_2006_2010.append(make_news(
    key="tn2009_2009_03_hc_advocates_police_clash",
    month="2009-03",
    title="Violent Clash in Madras High Court Premises",
    desc="A violent clash erupts between advocates protesting the Sri Lankan issue and state police inside the Madras High Court premises. Vehicles are set on fire.",
    tags=['security_crisis', 'law_order'],
    base_w=1.3, profile="security_crisis",
    reactions=[
        reaction("order_judicial_inquiry_suspend_officers", "Order a judicial inquiry by a retired judge and suspend the police officers who ordered the lathi-charge.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Police officers association protests, claiming they were acting under orders to clear court entries.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_resignation_of_home_secretary", "Demand the immediate resignation of the Home Secretary and organize lawyer boycotts in all district courts.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Litigants face delays due to court boycotts, generating public criticism.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_court_security_police_division", "Propose establishing a separate court security police division under the direct control of the High Court Registrar.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(12, "Lack of immediate funds delays training of the special security division.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"securityIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2009-04
ITEMS_2006_2010.append(make_news(
    key="tn2009_2009_04_karunanidhi_hunger_strike",
    month="2009-04",
    title="CM Karunanidhi Goes on Sudden Hunger Strike for SL Ceasefire",
    desc="Chief Minister Karunanidhi launches a sudden hunger strike at the Anna Memorial in Chennai, demanding the Sri Lankan government declare an immediate ceasefire.",
    tags=['politics', 'identity'],
    base_w=1.35, profile="politics",
    reactions=[
        reaction("terminate_strike_after_ceasefire_assurances", "Terminate the hunger strike after six hours, claiming the central government received assurances of ceasefire.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(22, "Reports emerge that the war has not stopped, leading to opposition mockery of the fast-strike drama.", eff(-2, 0, -3, -4)), 1.25),
        reaction("label_strike_as_political_charade", "Label the hunger strike as a brief, political charade designed to fool voters before next week's Lok Sabha polling.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 5),
                 {},
                 risk(14, "Ruling party cadres stage blockades, accusing the opposition of anti-Tamil bias.", eff(-1, 0, -1, -1)), 1.3),
        reaction("propose_all_party_embassy_lobbying", "Propose a joint all-party delegation to lobby the foreign embassies in Delhi for diplomatic intervention.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Embassies refuse to meet the state delegation citing international protocol rules.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 3}, weight=0.1)
    ]
))

# 2009-05
ITEMS_2006_2010.append(make_news(
    key="tn2009_2009_05_general_election_results",
    month="2009-05",
    title="UPA Alliance Wins 27 Seats in Tamil Nadu; SL War Ends",
    desc="The general election results are declared. The DMK-Congress UPA alliance wins 27 seats in Tamil Nadu. In Sri Lanka, the military defeats the LTTE, ending the civil war.",
    tags=['election', 'politics'],
    base_w=1.3, profile="election",
    reactions=[
        reaction("declare_victory_and_negotiate_berths", "Celebrate the victory as voter endorsement of welfare schemes and negotiate ministerial berths in the new cabinet.",
                 ['GOVERNMENT'], eff(3, 0, 3, 4),
                 {},
                 risk(18, "Opposition claims the win was secured by cash distribution and state machinery misuse.", eff(-1, 0, -2, -2)), 1.2),
        reaction("condemn_use_of_money_power_in_polls", "Release a report detailing systematic voter bribe payments in multiple districts and demand re-polls.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(14, "EC validates the results, stating that opposition charges lack specific proof logs.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_tamil_refugee_repatriation_charter", "Propose a national charter to assist the repatriation and rehabilitation of displaced Sri Lankan Tamils.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Sri Lankan government delays visa approvals for Indian rehabilitation teams.", eff(0, 0, -2, -1)), 1.15),
        no_comment(weight=0.2)
    ]
))

# 2009-06
ITEMS_2006_2010.append(make_news(
    key="tn2009_2009_06_stalin_deputy_cm",
    month="2009-06",
    title="M.K. Stalin Appointed Deputy Chief Minister",
    desc="Chief Minister Karunanidhi appoints Local Administration Minister M.K. Stalin as the Deputy Chief Minister, officially handing him charge of Home and General Administration.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("consolidate_administration_under_new_deputy", "Consolidate the state administration under the new Deputy CM, launching city development monitoring drives.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Madurai district secretary Alagiri's supporters express dissent, delaying local project works.", eff(-1, 0, -2, -1)), 1.15),
        reaction("condemn_formalization_of_dynasty", "Condemn the appointment, calling it the formalization of dynastic rule in Tamil Nadu and bypassing senior leaders.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Ruling party releases list of senior cabinet promotions, proving merit-based appointments.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_bipartisan_governance_reforms", "Propose a bipartisan assembly committee to discuss urban governance and local body finance devolution.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Rival parties boycott committee meetings, stalling the devolution draft.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2009-07
ITEMS_2006_2010.append(make_news(
    key="tn2009_2009_07_kalaignar_insurance_scheme",
    month="2009-07",
    title="Kalaignar Insurance Scheme for Poor Families Launched",
    desc="The state government launches the Kalaignar Insurance Scheme, a cashless health insurance program providing up to Rs 1 lakh for life-saving treatments for poor families.",
    tags=['governance', 'welfare'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("enroll_beneficiaries_with_smartcards", "Organize school-level enrollment camps and issue smartcards to speed up health coverage.",
                 ['GOVERNMENT'], eff(2, 0, 3, 5),
                 {},
                 risk(15, "Private hospitals report billing delay disputes, temporarily turning away patients.", eff(0, 0, -2, -2)), 1.25),
        reaction("demand_upgrades_to_government_hospitals_first", "Demand that government funds be spent upgrading state hospitals instead of paying premiums to private insurers.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Voters welcome the cashless private hospital options, ignoring the critique.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_joint_health_audit_panel", "Propose a joint panel of medical experts and MLAs to monitor the quality of surgeries performed under the scheme.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Hospital lobbies delay panel inspections citing patient privacy rules.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 1}, weight=0.2)
    ]
))

# 2009-08
ITEMS_2006_2010.append(make_news(
    key="tn2009_2009_08_tiruppur_dyeing_closures",
    month="2009-08",
    title="High Court Orders Closure of Polluting Tiruppur Dyeing Units",
    desc="The Madras High Court directs the closure of all dyeing units in Tiruppur that fail to achieve Zero Liquid Discharge (ZLD) of effluents into the Noyyal river.",
    tags=['governance', 'land_rights'],
    base_w=1.2, profile="land_rights",
    reactions=[
        reaction("implement_closures_and_tender_zld_plants", "Implement the closures strictly and announce state loans for setting up advanced ZLD plants.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Textile export unions declare a strike, leading to mass lay-offs of garment workers.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_welfare_package_for_laid_off_garment_workers", "Demand that the state government provide immediate monthly cash assistance to laid-off garment workers.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Finance department claims budget limits, refusing to issue cash payouts.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_agro_industrial_shift_loans", "Propose soft loans for displaced workers to shift to organic farming or non-polluting manufacturing.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Workers show low interest in organic farming loans, leaving funds unused.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 2}, weight=0.2)
    ]
))

# 2009-09
ITEMS_2006_2010.append(make_news(
    key="tn2009_2009_09_108_ambulance_service",
    month="2009-09",
    title="108 Emergency Ambulance Service Network Expanded",
    desc="The state health department announces the deployment of 200 new high-tech ambulances to expand the 108 Emergency service in rural and hilly districts.",
    tags=['governance', 'health_crisis'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("fast_track_gps_enabled_dispatch", "Fast-track GPS integration in dispatch rooms to reduce response times in remote villages.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Cellular network issues in hilly zones cause dispatch delays, drawing local press.", eff(0, 0, -2, -1)), 1.2),
        reaction("demand_icu_facilities_in_taluk_hospitals", "Demand that the government build ICU facilities in taluk hospitals first, calling ambulances transport vans.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Public welcomes the quick ambulance response times, ignoring the critique.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_first_responder_community_training", "Propose training village youth as certified first responders to manage medical emergencies before ambulances arrive.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Lack of trainer doctors limits the number of youth certified in the first quarter.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2009-10
ITEMS_2006_2010.append(make_news(
    key="tn2009_2009_10_coimbatore_airport_land",
    month="2009-10",
    title="Row Over Land Acquisition for Coimbatore Airport Expansion",
    desc="Landowners and farmer groups in Coimbatore block airport access roads, protesting against the state's land acquisition rates for the runway expansion project.",
    tags=['land_rights', 'protest'],
    base_w=1.2, profile="land_rights",
    reactions=[
        reaction("raise_compensation_and_offer_commercial_plots", "Raise compensation rates and offer alternative commercial shop plots to affected families.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Re-routing access roads delays expansion works by over six months.", eff(0, 0, -1, -2)), 1.2),
        reaction("join_farmers_protest_demand_runway_reshaping", "Join the farmers' protest, demanding that the runway expansion be redesigned to avoid agricultural fields.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Chamber of commerce accuses the party of blocking industrial growth in Western TN.", eff(0, 0, -2, -2)), 1.2),
        reaction("propose_airport_joint_stock_option", "Propose offering equity shares in the airport corporation to landowners in exchange for their plots.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Civil aviation ministry raises legal objections to state-offered private equity.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 2}, weight=0.25)
    ]
))

# 2009-11
ITEMS_2006_2010.append(make_news(
    key="tn2009_2009_11_medical_college_fees",
    month="2009-11",
    title="Controversy Over Private Medical College Fee Regulations",
    desc="A government-appointed committee fixes fee structures for private medical colleges. Managements protest, claiming the fees do not cover operational costs.",
    tags=['governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("enforce_fixed_fees_cancel_licenses_for_excess", "Enforce the fixed fee structures strictly, warning of license cancellation for colleges charging capitation fees.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Managements association shuts down admission counters in protest, stalling selection.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_state_takeover_of_violating_colleges", "Demand that the state government immediately take over colleges that refuse to comply with fee limits.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(14, "Legal advisors state that arbitrary takeover violates property rights, stalling action.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_differential_fees_based_on_income", "Propose a differential fee model where high-income students pay full costs to subsidize poor students.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Private colleges challenge the model in court, securing an interim stay.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2009-12
ITEMS_2006_2010.append(make_news(
    key="tn2009_2009_12_aiadmk_assembly_boycott",
    month="2009-12",
    title="AIADMK Boycotts Assembly Sessions Alleging Speaker Bias",
    desc="Opposition party AIADMK announces a boycott of the winter assembly sessions, alleging that the Speaker is biased and does not allocate sufficient debate time.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("proceed_with_legislative_business", "Proceed with passing bills on schedule, stating that the opposition is running away from debates.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(15, "Assembly debates look one-sided, drawing critical editorials on democratic norms.", eff(-1, 0, -2, -2)), 1.15),
        reaction("hold_parallel_mock_assembly_outside", "Hold parallel mock assembly sessions on the streets, highlighting crucial issues like power cuts.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Police detains MLAs for holding unauthorized public gatherings.", eff(-1, 0, -1, -1)), 1.25),
        reaction("propose_speaker_convened_reconciliation_meet", "Propose that the Speaker convene a special reconciliation meeting to draft new debate time allocations.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Rival leaders refuse to attend, leaving the boycott active.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2010-01
ITEMS_2006_2010.append(make_news(
    key="tn2010_2010_01_pennagaram_by_poll",
    month="2010-01",
    title="DMK Candidate Wins Pennagaram Assembly By-Election",
    desc="The DMK candidate wins the Pennagaram assembly by-election, defeating the PMK and AIADMK. The opposition alleges widespread distribution of cash to voters.",
    tags=['election'],
    base_w=1.25, profile="election",
    reactions=[
        reaction("celebrate_mandate_as_welfare_endorsement", "Celebrate the victory as public endorsement of the deputy CM's development and welfare programs.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Opposition files compilation of cash distribution videos with the Election Commission.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_disqualification_and_fresh_polling", "Demand that the EC disqualify the candidate and order fresh polling under central police supervision.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "EC holds inquiry but validates results citing lack of direct link to candidate.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_digitized_expense_monitoring", "Propose that the EC use real-time bank monitoring of all candidate accounts during by-elections.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "EC cites lack of banking integration in rural zones, stalling the proposal.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2010-02
ITEMS_2006_2010.append(make_news(
    key="tn2010_2010_02_pmk_non_aligned_front",
    month="2010-02",
    title="PMK Calls for Non-Aligned Third Front in State Politics",
    desc="PMK founder S. Ramadoss calls on smaller regional parties and caste organizations to form a non-aligned third front to break the DMK-AIADMK duopoly.",
    tags=['politics'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("ignore_front_propose_bilateral_talks", "Ignore the call publicly, but initiate private bilateral discussions with key constituent parties.",
                 ['GOVERNMENT'], eff(2, 0, 2, 3),
                 {},
                 risk(15, "Allies leak details of private talks, causing embarrassment and minor friction.", eff(-1, 0, -2, -1)), 1.15),
        reaction("warn_that_third_front_splits_opposition_votes", "Warn smaller parties that a third front only benefits the ruling regime by splitting anti-incumbency votes.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "PMK leaders criticize the opposition for being arrogant and dismissive of smaller groups.", eff(-1, 0, -2, -2)), 1.2),
        reaction("propose_coalition_governance_panel", "Propose a coalition governance seminar to discuss how multi-party fronts can run stable administrations.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Low turnout at the seminar limits its political impact.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2010-03
ITEMS_2006_2010.append(make_news(
    key="tn2010_2010_03_new_secretariat_complex",
    month="2010-03",
    title="New Legislative Assembly-Secretariat Complex Inaugurated",
    desc="Prime Minister Manmohan Singh inaugurates the grand new Tamil Nadu Legislative Assembly-Secretariat complex at Government Estate in Chennai, built under the DMK regime.",
    tags=['governance', 'infrastructure'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("hold_first_assembly_session_in_new_hall", "Hold the budget assembly session in the new hall, highlighting it as a modern symbol of state pride.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Opposition boycotted the opening, alleging high project cost overruns and poor ventilation.", eff(-1, 0, -2, -2)), 1.2),
        reaction("expose_cost_overruns_pledge_hospital_shift", "Expose budget files of the project, pledging to convert the building into a public hospital if voted to power.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, -1, 4, 4),
                 {},
                 risk(12, "Architectural associations criticize the pledge to shift functions as wasteful.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_public_heritage_guided_tours", "Propose organizing guided tours for school students to view the eco-friendly design elements of the complex.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(8, "Security departments restrict tourist access citing security concerns.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2010-04
ITEMS_2006_2010.append(make_news(
    key="tn2010_2010_04_uniform_education_intro",
    month="2010-04",
    title="Uniform Education System Rolled Out in State Schools",
    desc="The state education department begins rolling out the Uniform Education System (Samacheer Kalvi) for classes 1 and 6, using unified textbooks printed by the government.",
    tags=['governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("distribute_free_uniform_textbooks", "Distribute free uniform textbooks to all government school children on the first day of the term.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Private schools challenge the textbook content in court, seeking permission to use extra guides.", eff(0, 0, -2, -2)), 1.2),
        reaction("expose_historical_errors_in_textbooks", "Expose instances of historical errors and praise of political leaders in the new textbooks, demanding revisions.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Education department issues corrigendum slips, neutralizing the textbook controversy.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_curriculum_review_board", "Propose a curriculum review board of university professors to screen textbooks annually before printing.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Board formation is delayed, leaving current errors uncorrected in classes.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2010-05
ITEMS_2006_2010.append(make_news(
    key="tn2010_2010_05_minjur_desalination_opens",
    month="2010-05",
    title="100 MLD Minjur Desalination Plant Starts Operations",
    desc="The Minjur Desalination Plant starts full operations, supplying 100 million litres of water daily to industrial units and residential areas in North Chennai.",
    tags=['governance', 'infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("launch_pipeline_connections_to_housing", "Inaugurate pipeline extensions connecting the plant directly to North Chennai municipal housing units.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Minor pipeline leaks in industrial zones delay water delivery to homes.", eff(0, 0, -1, -1)), 1.2),
        reaction("demand_cag_audit_of_water_tariffs", "Demand a CAG audit of the water purchase agreement, claiming the state pays high prices to the private plant operator.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 3),
                 {},
                 risk(12, "Public welcomes the regular water supply, ignoring the tariff audit demand.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_solar_power_for_desalination", "Propose setting up a dedicated solar farm near the plant to reduce high grid power consumption costs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Land acquisition issues for the solar farm delay panel setup.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2010-06
ITEMS_2006_2010.append(make_news(
    key="tn2010_2010_06_world_classical_tamil_conf",
    month="2010-06",
    title="World Classical Tamil Conference Held in Coimbatore",
    desc="The state government hosts the historic World Classical Tamil Conference (Semmozhi Conference) in Coimbatore, celebrating Tamil language, culture, and literature.",
    tags=['identity', 'politics'],
    base_w=1.3, profile="politics",
    reactions=[
        reaction("advertise_cultural_pride_and_achievements", "Advertise the conference globally, showcasing the Dravidian regime's contribution to securing classical language status.",
                 ['GOVERNMENT'], eff(3, 0, 4, 4),
                 {},
                 risk(18, "Opposition boycotts the event, calling it a self-aggrandizing show for the CM's family.", eff(-1, 0, -2, -2)), 1.25),
        reaction("criticize_conference_expenses_during_power_cuts", "Criticize the massive expenditure on the conference while Western districts face daily four-hour power cuts.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Tamil scholars criticize the party for politicizing a linguistic celebration.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_tamil_research_fellowships", "Propose establishing 100 permanent international research fellowships for Tamil studies in state universities.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "University senate approval delays prevent early fellowship admissions.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"identityIssueMissed": 1}, weight=0.2)
    ]
))

# 2010-07
ITEMS_2006_2010.append(make_news(
    key="tn2010_2010_07_2g_spectrum_controversy",
    month="2010-07",
    title="2G Spectrum Allocation Controversy Targets DMK Minister",
    desc="Opposition parties target the DMK, alleging that Union Telecom Minister A. Raja bypassed guidelines in allocating 2G spectrum licenses, causing huge loss to exchequer.",
    tags=['corruption', 'politics'],
    base_w=1.35, profile="corruption",
    reactions=[
        reaction("defend_policy_as_cheap_telephony", "Defend the policy in media, arguing that the pricing ensured cheap telephone access for millions of rural poor.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(22, "National audit reports leaks detail massive discrepancies, damaging state govt image.", eff(-2, -2, -3, -4)), 1.2),
        reaction("demand_immediate_resignation_and_cbi_arrest", "Demand the immediate resignation and arrest of the minister, holding state-wide protests over corruption.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 5),
                 {},
                 risk(16, "Police detains protestors, leading to localized clashes near party offices.", eff(-1, 0, -2, -1)), 1.3),
        reaction("propose_joint_parliamentary_probe", "Propose a Joint Parliamentary Committee (JPC) inquiry to review the entire spectrum pricing history since 1999.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(12, "Parliamentary debate deadlocks delay JPC formation by several months.", eff(0, 0, -2, -1)), 1.15),
        no_comment(hidden={"corruptionIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2010-08
ITEMS_2006_2010.append(make_news(
    key="tn2010_2010_08_western_tn_power_grid_protests",
    month="2010-08",
    title="Farmers Protest High-Voltage Lines on Cropland in West",
    desc="Farmer groups in Tiruppur and Coimbatore protest against the installation of high-voltage power transmission lines across agricultural lands, demanding underground cables.",
    tags=['land_rights', 'protest'],
    base_w=1.2, profile="land_rights",
    reactions=[
        reaction("offer_double_compensation_for_easements", "Offer double compensation for land easement rights and guarantee subsidized power for affected farms.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "State power utility states underground cabling is technically impossible for high voltage, stalling talks.", eff(0, 0, -2, -2)), 1.25),
        reaction("join_farmers_dharna_demand_route_change", "Join the farmers' dharna demanding the line route be shifted along state highways to avoid cropland.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Utility security calls police to clear transmission towers, leading to minor clashes.", eff(-1, 0, -2, -1)), 1.2),
        reaction("propose_grid_safety_standards_audit", "Propose an independent expert panel to audit radiation and crop yield safety under transmission lines.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Panel inspections take months, keeping project construction on hold.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 3}, weight=0.25)
    ]
))

# 2010-09
ITEMS_2006_2010.append(make_news(
    key="tn2010_2010_09_uniform_syllabus_stayed",
    month="2010-09",
    title="High Court Stays Uniform Syllabus for Private Schools",
    desc="The Madras High Court issues a stay on the implementation of the uniform syllabus for private matriculation schools, citing lack of consultation on elective courses.",
    tags=['governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("file_immediate_appeal_in_supreme_court", "File an immediate appeal in the Supreme Court to lift the stay, asserting the state's right to unify school syllabus.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "SC delays hearings, leaving parents and teachers confused over which books to study.", eff(-1, 0, -2, -2)), 1.2),
        reaction("hail_stay_demand_curriculum_revision", "Hail the stay and demand the government revise the textbooks to include standard international science sections.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Ruling party accuses the opposition of siding with private school lobbies.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_interim_dual_syllabus_choice", "Propose allowing schools to choose between state books and matriculation courses for the current academic term.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Double examinations confusion arises, frustrating students.", eff(0, 0, -2, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2010-10
ITEMS_2006_2010.append(make_news(
    key="tn2010_2010_10_sc_upholds_samacheer_kalvi",
    month="2010-10",
    title="Supreme Court Upholds Samacheer Kalvi Implementation",
    desc="The Supreme Court sets aside the High Court stay, upholding the implementation of Samacheer Kalvi. The court orders all schools to use the uniform syllabus.",
    tags=['governance'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("enforce_syllabus_and_distribute_free_guides", "Direct all district educational officers to inspect schools and distribute free study guides for students.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Private schools lobby for extra school hours to teach CBSE content.", eff(0, 0, -1, -1)), 1.15),
        reaction("demand_removal_of_political_contents", "Comply with the order but demand a committee remove sections praising local political figures from history books.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Educational department delays book changes, keeping current prints active.", eff(0, 0, -1, -1)), 1.2),
        reaction("propose_teacher_training_grants", "Propose state training grants for teachers to adapt to the new uniform curriculum formats.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(8, "Training center schedules overlap with exam terms, reducing attendance.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2010-11
ITEMS_2006_2010.append(make_news(
    key="tn2010_2010_11_raja_resigns_2g",
    month="2010-11",
    title="Union Telecom Minister A. Raja Resigns Over CAG Report",
    desc="Following the tabling of the CAG report detailing an estimated loss of Rs 1.76 lakh crore in 2G spectrum allocations, Telecom Minister A. Raja resigns from cabinet.",
    tags=['corruption', 'politics'],
    base_w=1.4, profile="corruption",
    reactions=[
        reaction("accept_resignation_assert_cooperation_with_law", "Accept the resignation, stating that the minister resigned to protect parliament values, and promise full cooperation.",
                 ['GOVERNMENT'], eff(2, -2, 3, 3),
                 {},
                 risk(20, "CBI carries out raids on state capital trust offices, generating critical news headlines.", eff(-2, 0, -2, -3)), 1.25),
        reaction("demand_dismissal_of_state_coalition_govt", "Demand the Governor dismiss the state minority government, calling it a regime built on spectrum scam funds.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 5),
                 {},
                 risk(15, "Governor states the assembly majority remains stable, rejecting the petition.", eff(0, 0, -2, -1)), 1.3),
        reaction("propose_state_anti_corruption_ombudsman", "Propose establishing a state Lokayukta (ombudsman) with independent powers to scan MLA assets.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(12, "Drafting the ombudsman bill is delayed by assembly committee debates.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"corruptionIgnoredMemory": 4}, weight=0.15)
    ]
))

# 2010-12
ITEMS_2006_2010.append(make_news(
    key="tn2010_2010_12_monsoon_floods_delta",
    month="2010-12",
    title="Monsoon Floods Damage Crops in Delta Districts",
    desc="Heavy northeast monsoon rains submerge thousands of acres of standing paddy crops in Thanjavur and Tiruvarur. Farmers demand emergency relief.",
    tags=['disaster_relief'],
    base_w=1.2, profile="disaster_relief",
    reactions=[
        reaction("announce_per_acre_compensation", "Announce an emergency compensation of Rs 10,000 per damaged acre and waive current crop loans.",
                 ['GOVERNMENT'], eff(2, 0, 3, 5),
                 {},
                 risk(15, "Revenue surveyors take weeks to measure damaged plots, stalling payouts.", eff(0, 0, -2, -2)), 1.25),
        reaction("demand_central_drought_flood_package", "Demand the central government send a team and release an emergency relief package of Rs 500 crore.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(10, "Central team delays visit, leaving farmers to wait for relief.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_river_embankment_strengthening", "Propose a long-term engineering project to raise and reinforce embankments along Cauvery distributaries.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "High project cost keeps construction works slow in downstream blocks.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.3)
    ]
))

