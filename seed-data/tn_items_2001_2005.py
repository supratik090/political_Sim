from helper import reaction, no_comment, make_news, eff, risk

ITEMS_2001_2005 = []

# 2001-01
ITEMS_2001_2005.append(make_news(
    key="tn2001_2001_01_it_corridor",
    month="2001-01",
    title="State Government Announces Expansion of IT Corridor in Taramani",
    desc="The state government announces plans to establish the Phase II of the Information Technology corridor along Old Mahabalipuram Road (OMR) in Chennai, aiming to attract global software majors.",
    tags=['governance', 'economy'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("fast_track_it_corridor", "Fast-track land acquisitions and offer tax incentives to incoming MNCs to build the tech corridor.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(12, "Local landholders file cases in court claiming unfair land valuation, delaying construction.", eff(0, 0, -1, -2)), 1.2),
        reaction("oppose_it_privilege_demand_rural_funds", "Oppose the focus on tech parks, demanding that the budget be redirected to agricultural pump subsidies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(10, "Urban youth and trade chambers criticize the party as anti-growth and anti-employment.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_joint_venture_it_park", "Propose a public-private joint venture model that guarantees employment shares for local district youth.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(8, "Private developers refuse joint employment quotas, stalling the agreement.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"economyIssueMissed": 1}, weight=0.25)
    ]
))

# 2001-02
ITEMS_2001_2005.append(make_news(
    key="tn2001_2001_02_pmk_vanniyar_quota",
    month="2001-02",
    title="PMK Demands Exclusive Vanniyar Sub-Quota in State Reservation",
    desc="The Pattali Makkal Katchi (PMK) holds a massive rally in northern Tamil Nadu demanding a dedicated sub-quota for the Vanniyar community within the backward class reservation pool.",
    tags=['politics', 'identity'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("appoint_caste_census_commission", "Announce the appointment of a special commission to collect updated caste data and study the sub-quota request.",
                 ['GOVERNMENT'], eff(2, 0, 2, 3),
                 {},
                 risk(15, "Other backward caste organizations accuse the government of playing favorites and start counter-protests.", eff(-1, 0, -2, -2)), 1.15),
        reaction("oppose_quota_splitting_for_unity", "Oppose the sub-quota, arguing it will split the backward classes and damage state social harmony.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Vanniyar caste groups boycott the party's rallies in the northern districts.", eff(0, 0, -2, -3)), 1.25),
        reaction("propose_overall_quota_expansion", "Propose petitioning the central government to expand the overall state reservation limits beyond 69%.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Supreme Court re-emphasizes the 50% limit, rendering the petition ineffective.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 1}, weight=0.2)
    ]
))

# 2001-03
ITEMS_2001_2005.append(make_news(
    key="tn2001_2001_03_alliance_negotiations",
    month="2001-03",
    title="AIADMK and DMK Lead High-Stakes Alliance Talks for Assembly Polls",
    desc="With assembly elections approaching, the DMK and AIADMK camps hold hectic seat-sharing negotiations with national parties and regional caste groups to secure coalitions.",
    tags=['politics'],
    base_w=1.1, profile="politics",
    reactions=[
        reaction("concede_seats_to_national_allies", "Concede assembly seats to national allies to lock down a formidable, unified electoral alliance.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Local party cadres rebel in the ceded constituencies, filing nominations as independents.", eff(-2, 0, -1, -2)), 1.2),
        reaction("demand_lion_share_of_seats", "Demand the lion's share of seats for local regional candidates, resisting national party pressure.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(15, "National parties walk out of coalition talks, forming a multi-cornered contest.", eff(-1, 0, -2, -2)), 1.25),
        reaction("propose_common_minimum_program", "Propose forming the alliance based on a written common minimum program focusing on welfare and water issues.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Disagreements over specific irrigation clauses delay the alliance announcement.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2001-04
ITEMS_2001_2005.append(make_news(
    key="tn2001_2001_04_election_campaigns",
    month="2001-04",
    title="Assembly Campaigning Reaches Fever Pitch Across Tamil Nadu",
    desc="Political leaders crisscross the state. The AIADMK-led alliance attacks the DMK on corruption and power tariff hikes, while DMK highlights IT sector growth and social welfare.",
    tags=['election'],
    base_w=1.25, profile="election",
    reactions=[
        reaction("announce_rural_debt_waiver_promise", "Announce an election promise to waive off all crop loans from cooperative banks if voted to power.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Urban taxpayer groups criticize the promise as fiscally irresponsible.", eff(0, 0, -2, -1)), 1.2),
        reaction("highlight_incumbent_corruption_scams", "Focus the campaign entirely on incumbent corruption cases and high power tariffs in rural regions.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Ruling party releases old court acquittals, dulling the corruption charges.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_debates_on_development", "Propose a series of public debates on industrial investments and infrastructural development in second-tier cities.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(10, "Opponents refuse to attend, leading to empty-chair media stunts that look weak.", eff(-1, 0, -1, -1)), 1.1),
        no_comment(weight=0.2)
    ]
))

# 2001-05
ITEMS_2001_2005.append(make_news(
    key="tn2001_2001_05_election_results",
    month="2001-05",
    title="AIADMK Alliance Wins Landslide; J. Jayalalithaa Sworn In as CM",
    desc="The AIADMK-led alliance sweeps the Tamil Nadu assembly polls, winning 196 seats. J. Jayalalithaa is sworn in as Chief Minister, despite unresolved legal disqualifications.",
    tags=['election', 'politics'],
    base_w=1.3, profile="election",
    reactions=[
        reaction("declare_welfare_reforms_victory", "Declare the mandate as a victory of poor people and launch immediate distribution of free cycles for students.",
                 ['GOVERNMENT'], eff(3, 0, 4, 5),
                 {},
                 risk(20, "Opposition files immediate petition in Supreme Court challenging the CM's swearing-in ceremony.", eff(-2, 0, -2, -2)), 1.25),
        reaction("challenge_legality_of_swearing_in", "Hold press conferences challenging the Governor's decision to swear in a convicted leader, calling it unconstitutional.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(14, "Ruling party cadres stage street blockades, accusing the opposition of disrespecting the mandate.", eff(-1, 0, -2, -1)), 1.2),
        reaction("propose_bipartisan_governance_accord", "Propose a bipartisan assembly committee to monitor the implementation of election manifestos without delay.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Fierce rivalry between leaders prevents the committee from holding its first meeting.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.15)
    ]
))

# 2001-06
ITEMS_2001_2005.append(make_news(
    key="tn2001_2001_06_karunanidhi_midnight_arrest",
    month="2001-06",
    title="DMK Chief Karunanidhi Arrested in Dramatic Midnight Police Raid",
    desc="In a midnight raid, state police arrest former CM M. Karunanidhi in connection with an alleged Chennai flyover construction scam. Visuals of the arrest trigger national debate.",
    tags=['security_crisis', 'corruption'],
    base_w=1.35, profile="security_crisis",
    reactions=[
        reaction("defend_arrest_as_rule_of_law", "Defend the police actions as an unbiased enforcement of law against high-level municipal corruption.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(22, "National TV channels broadcast the arrest visuals, generating massive public sympathy for the arrested leader.", eff(-2, 0, -3, -4)), 1.25),
        reaction("condemn_police_barbarism_and_protest", "Condemn the arrest as political vendetta, release video footage, and call for state-wide protest rallies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 5),
                 {},
                 risk(16, "Police resort to tear gas and lathi-charges, leading to arrest of key party workers.", eff(-1, 0, -2, -1)), 1.3),
        reaction("propose_central_judicial_probe", "Propose an independent judicial probe by a retired Supreme Court judge to examine the arrest and flyover contracts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(12, "State cabinet rejects the proposal, asserting state police jurisdiction.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"securityIgnoredMemory": 3}, weight=0.1)
    ]
))

# 2001-07
ITEMS_2001_2005.append(make_news(
    key="tn2001_2001_07_dmk_protest_strikes",
    month="2001-07",
    title="DMK Protests Against Midnight Arrest Freeze Chennai Traffic",
    desc="DMK cadres block railways and public highways across the state, demanding the immediate release of Karunanidhi. Commercial establishments in Chennai close down.",
    tags=['protest'],
    base_w=1.25, profile="protest",
    reactions=[
        reaction("deploy_police_force_clear_roads", "Deploy rapid police battalions to clear blockades immediately and ensure all state buses run under escort.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Clashes between police and protestors result in damage to public property and bad press.", eff(-1, 0, -2, -3)), 1.2),
        reaction("continue_indefinite_jail_bharu_protests", "Continue the 'Jail Bharo' campaign, directing thousands of cadres to peacefully court arrest in every district headquarters.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "General public gets frustrated by daily traffic jams and retail shut-downs.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_all_party_peace_conference", "Propose a round-table conference of all major political parties to restore normalcy and avoid street violence.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Ruling party boycotts the conference, calling the protestors lawbreakers.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.2)
    ]
))

# 2001-08
ITEMS_2001_2005.append(make_news(
    key="tn2001_2001_08_cm_eligibility_hearings",
    month="2001-08",
    title="Supreme Court Begins Hearings on CM Jayalalithaa's Appointment",
    desc="A constitution bench of the Supreme Court begins final hearings on petitions challenging the appointment of J. Jayalalithaa as CM due to her conviction in corruption cases.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("assert_popular_mandate_in_court", "Defend the appointment by arguing that the popular electoral mandate overrides technical administrative disqualifications.",
                 ['GOVERNMENT'], eff(2, 0, 2, 3),
                 {},
                 risk(15, "Judges express skepticism, causing market jitters and administration slowdown.", eff(-1, 0, -2, -2)), 1.15),
        reaction("demand_strict_adherence_to_constitution", "Submit amicus curiae briefs demanding strict enforcement of anti-corruption clauses for public office holders.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "Ruling party accuses the opposition of trying to win in court what they lost in elections.", eff(0, 0, -1, -2)), 1.2),
        reaction("propose_legislative_clarification_bill", "Propose an all-party national bill in Parliament to explicitly clarify disqualification rules for assembly contests.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "National parties delay debate on the bill, leaving state uncertainty active.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2001-09
ITEMS_2001_2005.append(make_news(
    key="tn2001_2001_09_ops_sworn_in",
    month="2001-09",
    title="Supreme Court Disqualifies CM; O. Panneerselvam Sworn In",
    desc="The Supreme Court rules that J. Jayalalithaa cannot hold the post of CM due to her conviction. J. Jayalalithaa steps down; loyalist minister O. Panneerselvam is sworn in as CM.",
    tags=['politics'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("declare_loyalty_and_interim_governance", "Swear loyalty to the party leader and state that the interim administration will continue all welfare schemes.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Opposition mocks the new CM as a dummy ruler, damaging the government's authority.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_immediate_assembly_dissolution", "Label the new administration a shadow regime and demand immediate dissolution of the house for fresh elections.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "The ruling majority easily wins the assembly vote of confidence, neutralizing the demand.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_state_administrative_reorganization", "Propose shifting focus to administrative restructuring to ensure bureaucracy runs smoothly during this transition.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Lack of strong political leadership slows down bureaucratic clearances.", eff(0, 0, -2, -1)), 1.1),
        no_comment(weight=0.2)
    ]
))

# 2001-10
ITEMS_2001_2005.append(make_news(
    key="tn2001_2001_10_local_body_clashes",
    month="2001-10",
    title="Violent Clashes Mar Local Body Elections in Chennai",
    desc="Local body elections in Tamil Nadu, particularly inside Chennai Corporation, witness violent clashes, ballot-box snatching, and booth-capturing allegations between DMK and AIADMK.",
    tags=['election', 'security_crisis'],
    base_w=1.2, profile="security_crisis",
    reactions=[
        reaction("re_poll_sensitive_booths_with_police", "Order immediate re-polling in all sensitive booths under heavy state police and CCTV supervision.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Opposition claims local police are colluding with the ruling party candidates.", eff(-1, 0, -2, -2)), 1.15),
        reaction("petition_election_commission_for_central_forces", "Petition the State Election Commission to deploy central paramilitary forces for all re-polling.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "Commission delays deployment citing lack of nearby battalions.", eff(0, 0, -1, -1)), 1.2),
        reaction("propose_digitized_booth_monitoring", "Propose trial run of electronic voting machine (EVM) telemetry to track polling anomalies live.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "EVM network issues in semi-urban wards lead to voting delays.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"securityIgnoredMemory": 2}, weight=0.25)
    ]
))

# 2001-11
ITEMS_2001_2005.append(make_news(
    key="tn2001_2001_11_cauvery_water_protests",
    month="2001-11",
    title="Delta Sugarcane and Paddy Farmers Protest Cauvery Water Scarcity",
    desc="A poor monsoon in Karnataka triggers water scarcity in the Cauvery basin. Paddy farmers in Thanjavur and Tiruvarur block national highways demanding water release.",
    tags=['land_rights', 'protest'],
    base_w=1.2, profile="land_rights",
    reactions=[
        reaction("request_cauvery_board_meeting", "Send an official delegation to Delhi to request the Cauvery River Authority order immediate water release.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Karnataka government rejects the authority's advisory, leading to stalemate.", eff(-1, 0, -1, -2)), 1.2),
        reaction("lead_delta_farmers_march", "Lead a massive solidarity march of farmers to the state border, demanding Karnataka open the dams.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Commuters criticize the border blockades which disrupt inter-state freight cargo.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_drip_irrigation_subsidies", "Propose a state-backed emergency subsidy scheme for drip irrigation and short-duration crop seeds.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(10, "Farmers refuse to switch crops mid-season, leaving the subsidies unused.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 2}, weight=0.2)
    ]
))

# 2001-12
ITEMS_2001_2005.append(make_news(
    key="tn2001_2001_12_tansi_acquittal",
    month="2001-12",
    title="Madras High Court Acquits J. Jayalalithaa in TANSI Case",
    desc="The Madras High Court acquits former CM J. Jayalalithaa in the TANSI land acquisition and Pleasant Stay Hotel cases, clearing her primary legal obstacles to return as CM.",
    tags=['politics', 'corruption'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("celebrate_acquittal_as_truth_victory", "Organize state-wide celebrations, calling the acquittal a triumph of truth over political conspiracies.",
                 ['GOVERNMENT'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Opposition claims the state prosecution intentionally presented a weak case.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_state_appeal_in_supreme_court", "Hold rallies demanding that the state government immediately file an appeal in the Supreme Court against the acquittal.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(14, "Ruling party workers clash with opposition protestors near court campuses.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_legal_reform_board", "Propose a state legal reform board to oversee prosecution procedures in high-profile corruption cases.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, -1, 3, 2),
                 {},
                 risk(10, "Bureaucratic resistance stalls board creation, leaving prosecution norms unchanged.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"corruptionIgnoredMemory": 2}, weight=0.2)
    ]
))

# 2002-01
ITEMS_2001_2005.append(make_news(
    key="tn2002_2002_01_andipatti_by_poll_prep",
    month="2002-01",
    title="OPS Resigns as CM; Andipatti By-Election Scheduled",
    desc="Following her legal acquittal, Chief Minister O. Panneerselvam resigns. The Election Commission announces the by-election schedule for the Andipatti constituency.",
    tags=['election'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("launch_intensive_andipatti_campaign", "Deploy senior cabinet ministers to coordinate a massive campaign in Andipatti to secure a record margin.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Opposition files complaints of code of conduct violations regarding developmental project announcements.", eff(0, 0, -2, -2)), 1.2),
        reaction("field_strong_candidate_against_jj", "Form a joint opposition front and field a consensus local candidate to challenge the party leader in Andipatti.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Alliance partners disagree on candidate selection, weakening the joint campaign.", eff(-1, 0, -2, -2)), 1.25),
        reaction("propose_independent_poll_monitoring", "Propose requesting the EC to install webcams at all polling booths in Andipatti to prevent rigging.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Technical setup errors prevent half of the webcams from functioning on polling day.", eff(0, 0, -2, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2002-02
ITEMS_2001_2005.append(make_news(
    key="tn2002_2002_02_jj_resumes_cm",
    month="2002-02",
    title="J. Jayalalithaa Wins Andipatti; Sworn In as Chief Minister",
    desc="J. Jayalalithaa wins the Andipatti assembly by-election by a margin of over 40,000 votes and is sworn in as the Chief Minister of Tamil Nadu for the third time.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("announce_new_infrastructure_investments", "Celebrate the victory and announce a major road-widening project across southern districts.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Farmers protest land acquisition for the highway expansion.", eff(0, 0, -1, -2)), 1.15),
        reaction("condemn_use_of_state_machinery_in_polls", "Release a report detailing how state official cars and police were misused to secure the by-poll victory.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(10, "Local residents reject the charges, pointing to the high margin of votes.", eff(0, 0, -1, -1)), 1.2),
        reaction("propose_bipartisan_development_charter", "Propose a charter for regional growth in southern districts, inviting both treasury and opposition ideas.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Boycott of meetings by rival groups delays charter implementation.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2002-03
ITEMS_2001_2005.append(make_news(
    key="tn2002_2002_03_temple_audit_scheme",
    month="2002-03",
    title="Government Introduces Scheme to Audit Hindu Temple Assets",
    desc="The Hindu Religious and Charitable Endowments (HR&CE) department announces a special audit of all temple gold assets, jewellery, and land leases across the state.",
    tags=['governance', 'identity'],
    base_w=1.1, profile="governance",
    reactions=[
        reaction("enforce_audit_for_transparency", "Implement the asset audit strictly to prevent thefts and ensure temple lands pay fair market rent.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(16, "Traditional temple priests and conservative groups organize sit-ins, alleging state interference.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_audit_include_all_faiths", "Demand that the state government audit all religious properties equally, accusing it of selectively targeting temples.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Secular organizations accuse the party of drumming up communal division.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_independent_devotee_board", "Propose that audits be conducted by a board of retired judges and temple devotees rather than government officers.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Disputes over board membership selection delay the audit process.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 1}, weight=0.25)
    ]
))

# 2002-04
ITEMS_2001_2005.append(make_news(
    key="tn2002_2002_04_veerappan_hostage_demands",
    month="2002-04",
    title="Forest Brigand Veerappan Demands Release of Extremist Prisoners",
    desc="Sandalwood smuggler Veerappan sends an audio cassette demanding the release of several imprisoned Tamil nationalist activists in exchange for not taking new hostages.",
    tags=['security_crisis'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("reject_demands_intensify_stf_operations", "Reject all extortion demands and order the Special Task Force (STF) to intensify combing operations in Sathyamangalam forests.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "STF combing operations trigger protests from local forest tribals alleging harassment.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_peaceful_negotiation_avoid_violence", "Demand the government prioritize safety and send an emissary to negotiate the brigand's surrender peacefully.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(15, "Security analysts accuse the opposition of showing weakness against a known criminal.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_joint_state_border_patrol", "Propose a joint command linking Tamil Nadu, Karnataka, and central intelligence to capture the gang.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Inter-state sharing disputes slow down intelligence coordination.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"securityIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2002-05
ITEMS_2001_2005.append(make_news(
    key="tn2002_2002_05_animal_sacrifice_ban",
    month="2002-05",
    title="Government Bans Animal Sacrifice in Temples Across State",
    desc="The state government enforces the decades-old Tamil Nadu Animals and Birds Sacrifices Prohibition Act, banning animal sacrifice in temples. Rural communities protest.",
    tags=['identity'],
    base_w=1.15, profile="identity",
    reactions=[
        reaction("defend_ban_as_humane_reform", "Defend the ban as a humane and progressive reform that aligns temple practices with animal welfare standards.",
                 ['GOVERNMENT'], eff(1, 0, 3, 2),
                 {},
                 risk(18, "Subaltern and rural communities view the ban as an attack on their traditional deity rituals.", eff(-2, 0, -2, -3)), 1.2),
        reaction("demand_immediate_withdrawal_of_ban", "Condemn the ban, arguing it infringes on the religious freedom and cultural customs of rural folk.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Animal rights groups launch a media campaign criticizing the party's stance.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_exemption_for_small_temples", "Propose amending the act to exempt village-level temples while regulating practices in major municipal shrines.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Legal experts warn that selective exemption will not survive constitutional challenges.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.2)
    ]
))

# 2002-06
ITEMS_2001_2005.append(make_news(
    key="tn2002_2002_06_cauvery_deadlock",
    month="2002-06",
    title="Cauvery River Authority Meeting Ends in Deadlock",
    desc="The Cauvery River Authority meeting chaired by the Prime Minister ends without a water-sharing agreement. Delta farmers in Thanjavur block local railway tracks.",
    tags=['land_rights'],
    base_w=1.2, profile="land_rights",
    reactions=[
        reaction("file_contempt_petition_against_karnataka", "File a contempt petition in the Supreme Court against Karnataka for failing to release the mandatory water quota.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Court delays listing the petition, leaving the current agricultural season in crisis.", eff(0, 0, -2, -2)), 1.15),
        reaction("lead_joint_farmer_rail_roko", "Join the farmer unions in a state-wide 'Rail Roko' strike to register a strong protest against Karnataka's stance.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Train cancellations cause massive passenger delays and transport industry complaints.", eff(-1, 0, -1, -2)), 1.2),
        reaction("propose_cauvery_basin_authority_reform", "Propose reforming the Cauvery Board to give it statutory powers to take control of reservoirs during droughts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Political opposition from neighbouring states stalls the reform bill in Parliament.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 3}, weight=0.25)
    ]
))

# 2002-07
ITEMS_2001_2005.append(make_news(
    key="tn2002_2002_07_vaiko_pota_arrest",
    month="2002-07",
    title="MDMK Leader Vaiko Arrested Under POTA for Pro-LTTE Speech",
    desc="MDMK general secretary Vaiko is arrested by state police under the Prevention of Terrorism Act (POTA) for making speeches supporting the banned LTTE organization.",
    tags=['security_crisis', 'politics'],
    base_w=1.3, profile="security_crisis",
    reactions=[
        reaction("justify_arrest_as_national_security", "Justify the arrest under POTA, stating that no support for armed terror outfits will be tolerated in the state.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(20, "Human rights groups and opposition parties accuse the government of abusing POTA for political vendetta.", eff(-2, 0, -2, -2)), 1.2),
        reaction("condemn_pota_misuse_demand_repeal", "Condemn the arrest as a gross abuse of anti-terror laws to silence political rivals, and demand POTA's repeal.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Governing allies release audio clips of the speech, shifting the media debate.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_judicial_review_committee", "Propose a high court-appointed review committee to screen all POTA bookings before arrests are executed.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Review process is delayed, leaving the leader in judicial custody.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"securityIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2002-08
ITEMS_2001_2005.append(make_news(
    key="tn2002_2002_08_severe_drought",
    month="2002-08",
    title="Severe Drought Declared in 28 Districts of Tamil Nadu",
    desc="A failure of the Southwest monsoon triggers severe drought. The state government declares 28 districts drought-affected as groundwater levels drop to historic lows.",
    tags=['disaster_relief'],
    base_w=1.25, profile="disaster_relief",
    reactions=[
        reaction("announce_drought_relief_package", "Announce an emergency financial relief package of Rs 150 crore and supply drinking water by tankers.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Bureaucratic delays in identifying beneficiaries spark protests at collector offices.", eff(-1, 0, -2, -2)), 1.25),
        reaction("demand_complete_land_revenue_waiver", "Demand a complete waiver of agricultural land revenue taxes and immediate central assistance of Rs 1,000 crore.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Central team delays visit, stalling the release of central relief funds.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_emergency_desalination_feasibility", "Propose feasibility studies for multiple cost-effective desalination plants along the state's coastline.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "High capital costs delay private bidders from taking up the projects.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2002-09
ITEMS_2001_2005.append(make_news(
    key="tn2002_2002_09_anti_conversion_act",
    month="2002-09",
    title="Government Introduces Prohibition of Forcible Conversion Act",
    desc="The Chief Minister announces the promulgation of an ordinance prohibiting forcible religious conversions, attracting intense praise and criticism from various sectors.",
    tags=['identity', 'politics'],
    base_w=1.2, profile="identity",
    reactions=[
        reaction("defend_act_against_fraudulent_conversions", "Defend the legislation as a necessary measure to protect vulnerable sections from fraudulent conversions.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Minority organizations and civil rights groups organize state-wide black flag demonstrations.", eff(-2, 0, -2, -3)), 1.2),
        reaction("condemn_act_as_communal_and_regressive", "Condemn the ordinance as communal, regressive, and a direct threat to constitutional freedom of religion.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Traditionalist voter blocks shift away, accusing the party of minority appeasement.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_all_faith_governing_council", "Propose setting up an all-faith council to monitor religious conversions voluntarily, bypassing police involvement.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Rival religious heads refuse to sit together on the council, stalling the initiative.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.2)
    ]
))

# 2002-10
ITEMS_2001_2005.append(make_news(
    key="tn2002_2002_10_anti_conversion_protests",
    month="2002-10",
    title="Opposition Groups Hold Joint Rally Against Anti-Conversion Law",
    desc="Opposition parties, minority forums, and secular groups stage a massive joint rally in Chennai demanding the immediate withdrawal of the anti-conversion law.",
    tags=['protest'],
    base_w=1.15, profile="protest",
    reactions=[
        reaction("refuse_withdrawal_warn_against_instigation", "Refuse to withdraw the law, warning opposition leaders against instigating public unrest for electoral gains.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(16, "Secular outfits gain support among urban middle-class voters, leading to negative press.", eff(-1, 0, -2, -2)), 1.15),
        reaction("pledge_to_repeal_law_if_elected", "Pledge to repeal the anti-conversion law immediately upon coming to power in the state.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(14, "Conservative groups release pamphlets criticizing the pledge as an attack on culture.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_judicial_interpretation_panel", "Propose a panel of retired high court judges to review the law's clauses to prevent misuse by local police.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Activists call the panel a stalling tactic, continuing localized protests.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2002-11
ITEMS_2001_2005.append(make_news(
    key="tn2002_2002_11_transport_strike",
    month="2002-11",
    title="State-wide Transport Strike Disrupts Public Transit",
    desc="State transport corporation unions launch an indefinite strike demanding wage revisions and gratuity settlements, leaving thousands of commuters stranded.",
    tags=['protest'],
    base_w=1.15, profile="protest",
    reactions=[
        reaction("declare_strike_illegal_hire_temp_drivers", "Declare the strike illegal under ESMA, hire temporary drivers, and warn striking staff of dismissal.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Trade unions expand the strike, blockading bus depots in major cities.", eff(-1, 0, -2, -2)), 1.2),
        reaction("support_workers_demand_interim_payout", "Support the unions, demanding that the government release interim funds to pay retired staff dues.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Private bus operators hike fares during the strike, drawing commuter ire.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_tripartite_arbitration_tribunal", "Propose a tripartite arbitration tribunal led by a labor commissioner to negotiate new wage scales.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(10, "Radical union leaders refuse arbitration, prolonging the transport deadlock.", eff(0, 0, -2, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2002-12
ITEMS_2001_2005.append(make_news(
    key="tn2002_2002_12_sacrifice_ban_court_stay",
    month="2002-12",
    title="Madras HC Stays Enforcement of Animal Sacrifice Ban",
    desc="The Madras High Court issues an interim stay on the enforcement of the temple animal sacrifice ban, citing traditional customs and scheduled tribe exemption appeals.",
    tags=['identity', 'governance'],
    base_w=1.1, profile="identity",
    reactions=[
        reaction("comply_with_stay_appeal_later", "Comply with the court order, directing local police to suspend active enforcement pending final hearings.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(14, "Animal welfare groups accuse the administration of yielding to political pressure.", eff(-1, 0, -1, -1)), 1.15),
        reaction("hail_stay_as_victory_for_customs", "Hail the stay as a major victory for local rural customs, and demand the law be permanently scrapped.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(12, "Urban reform organizations criticize the party for promoting outdated practices.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_hygiene_guidelines_for_temples", "Propose drafting strict health and hygiene guidelines for animal sacrifices instead of a total ban.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Religious conservatives reject state-monitored guidelines inside sanctums.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 1}, weight=0.25)
    ]
))

# 2003-01
ITEMS_2001_2005.append(make_news(
    key="tn2003_2003_01_sathankulam_by_poll",
    month="2003-01",
    title="AIADMK Candidate Wins Sathankulam By-Election",
    desc="The AIADMK candidate wins the Sathankulam assembly by-election, supported from outside by the BJP. The joint DMK-Congress campaign fails to secure the seat.",
    tags=['election'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("hail_mandate_as_approval_of_reforms", "Hail the victory as public approval of the government's tough fiscal and administrative reforms.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Opposition alleges high-level cash distribution by the ruling party workers.", eff(-1, 0, -2, -1)), 1.2),
        reaction("highlight_alliance_coordination_flaws", "Highlight coordination flaws in the opposition campaign and vow to build a stronger alliance model.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Allied parties issue statements blaming each other for the defeat.", eff(-1, 0, -2, -2)), 1.2),
        reaction("propose_evm_security_checks", "Propose that the Election Commission execute double-blind tally checks of all EVM seals prior to counting.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "EC rejects the proposal as unnecessary, citing current protocol safety.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2003-02
ITEMS_2001_2005.append(make_news(
    key="tn2003_2003_02_rainwater_harvesting",
    month="2003-02",
    title="Government Mandates Rainwater Harvesting in All Buildings",
    desc="To combat recurring water crisis, the state government passes a law mandating Rainwater Harvesting (RWH) installations in all public and private buildings in Chennai.",
    tags=['governance'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("set_strict_compliance_deadlines", "Set a strict three-month deadline, warning that municipal water connections will be cut for non-compliance.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Plumbing materials and contractor fees spike, creating public resentment in middle-class wards.", eff(0, 0, -2, -2)), 1.25),
        reaction("demand_subsidies_for_low_income_homes", "Demand that the state government provide full financial subsidies to low-income and slum households for RWH setup.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(10, "Ruling party accuses the opposition of trying to dilute a critical ecological measure.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_public_awareness_camp", "Propose launching a large-scale civic awareness campaign with college volunteers to demonstrate RWH designs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(8, "Volunteers report low public attendance at local municipal workshops.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.2)
    ]
))

# 2003-03
ITEMS_2001_2005.append(make_news(
    key="tn2003_2003_03_veeranam_water_project",
    month="2003-03",
    title="Chennai Water Crisis: Veeranam Project Pipeline Accelerated",
    desc="Amid a severe summer drinking water shortage in Chennai, the state cabinet resolves to fast-track the Veeranam pipeline project to draw water from the Veeranam lake.",
    tags=['governance', 'infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("allocate_emergency_funds_for_pipeline", "Allocate emergency state budget funds to complete the 235 km pipeline work ahead of schedule.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(16, "Farmers near Veeranam lake protest, claiming the project will dry up local irrigation canals.", eff(-1, 0, -2, -2)), 1.2),
        reaction("expose_prior_project_leakages", "Expose prior pipeline leakage reports, accusing the administration of waste and substandard contracting.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, -1, 4, 3),
                 {},
                 risk(14, "Local media highlights Chennai's urgent thirst, painting the opposition as obstacle creators.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_shared_water_treaty_with_farmers", "Propose a formal treaty guaranteeing local farmers priority water rights during low rainfall years.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Negotiations drag on as farmer groups demand statutory veto rights over water release.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 2}, weight=0.25)
    ]
))

# 2003-04
ITEMS_2001_2005.append(make_news(
    key="tn2003_2003_04_delta_labor_migration",
    month="2003-04",
    title="Water Scarcity Triggers Mass Farm Labor Migration in Delta",
    desc="The absence of Cauvery water forces agricultural laborers in Thanjavur and Nagapattinam to migrate to Tiruppur and Chennai in search of construction and textile jobs.",
    tags=['land_rights'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("launch_rural_employment_works", "Launch emergency rural road and desiltation works under state funds to provide local employment.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Limited funds restrict the works to few blocks, causing regional dissatisfaction.", eff(-1, 0, -2, -2)), 1.25),
        reaction("demand_interest_free_cash_allowance", "Demand the government issue an interest-free monthly cash allowance of Rs 2,000 to all registered delta farm workers.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Finance department states state treasury is near deficit, ruling out cash handouts.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_rural_industrial_parks", "Propose setting up small agro-processing industrial parks in delta districts to diversify local employment.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(10, "Industrial developers demand cheap power guarantees before buying land plots.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 3}, weight=0.2)
    ]
))

# 2003-05
ITEMS_2001_2005.append(make_news(
    key="tn2003_2003_05_staff_strike_notice",
    month="2003-05",
    title="Government Employees Union Serves Indefinite Strike Notice",
    desc="The Joint Action Committee of Tamil Nadu Teachers and Government Employees Organisations (JACTTO-GEO) serves a strike notice protesting pension cuts and dearness allowance freezes.",
    tags=['protest'],
    base_w=1.2, profile="protest",
    reactions=[
        reaction("warn_unions_of_strict_esma_action", "Issue a cabinet warning that the strike will invite arrest under the Essential Services Maintenance Act (ESMA) and salary cuts.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(15, "Union leaders reject the warning, mobilizing thousands of teachers for the strike.", eff(-1, 0, -2, -2)), 1.15),
        reaction("support_employees_warn_govt_of_backlash", "Publicly support the employee demands, warning the government that treating teachers like criminals will face severe backlash.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "A segment of public opinion is unsympathetic to employees, citing tax money costs.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_bipartisan_pay_commission", "Propose a bipartisan pay commission of MLAs and union heads to audit the state budget and find a compromise.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Ruling party refuses to include MLAs in the commission, stalling the proposal.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2003-06
ITEMS_2001_2005.append(make_news(
    key="tn2003_2003_06_staff_mass_dismissal",
    month="2003-06",
    title="Government Dismisses Over 1.7 Lakh Striking Employees",
    desc="In an unprecedented move to break the state-wide strike, the Tamil Nadu government uses ESMA to dismiss over 170,000 striking government employees and teachers overnight.",
    tags=['governance', 'protest'],
    base_w=1.3, profile="governance",
    reactions=[
        reaction("defend_dismissal_for_fiscal_discipline", "Defend the tough action as necessary to protect public funds and maintain essential state services.",
                 ['GOVERNMENT'], eff(2, 0, 2, 2),
                 {},
                 risk(22, "National unions express outrage, and closed schools lead to heavy middle-class anger.", eff(-2, 0, -3, -4)), 1.2),
        reaction("condemn_draconian_action_demand_reinstatement", "Condemn the dismissals as authoritarian, hold dharnas, and pledge to restore all jobs immediately.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 5),
                 {},
                 risk(15, "State police arrests protesting leaders under assembly guidelines.", eff(-1, 0, -2, -1)), 1.3),
        reaction("propose_high_court_mediation", "Propose requesting the Madras High Court to appoint an independent mediator to resolve the dispute and restore services.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(12, "State cabinet opposes judicial interference in administrative executive powers.", eff(0, 0, -2, -1)), 1.15),
        no_comment(hidden={"securityIgnoredMemory": 3}, weight=0.1)
    ]
))

# 2003-07
ITEMS_2001_2005.append(make_news(
    key="tn2003_2003_07_sc_reinstatement_orders",
    month="2003-07",
    title="Supreme Court Orders Reinstatement of Dismissed Employees",
    desc="The Supreme Court, while hearing appeals against the mass dismissals, orders the state government to reinstate the employees upon their submitting an unconditional apology.",
    tags=['governance'],
    base_w=1.25, profile="governance",
    reactions=[
        reaction("comply_and_accept_written_apologies", "Comply with the court's advice, reinstating employees who submit a standard written apology.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Rival unions refuse to apologize, keeping local educational offices in friction.", eff(0, 0, -2, -2)), 1.2),
        reaction("demand_full_reinstatement_without_apology", "Demand that the government reinstate all employees with full back-pay without demanding humiliating apologies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(12, "Ruling party points out that the court itself mandated the apology, reducing impact.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_state_administrative_code_review", "Propose a review of the state service rules to establish clear dispute-resolution protocols for the future.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Administrative departments focus on backlog tasks, leaving code review on paper.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2003-08
ITEMS_2001_2005.append(make_news(
    key="tn2003_2003_08_tnpcee_regulation",
    month="2003-08",
    title="Assembly Passes Bill to Regulate Professional Course Admissions",
    desc="The Tamil Nadu Assembly passes a bill to regulate admissions to engineering and medical colleges, aiming to curb high capitation fees charged by private institutions.",
    tags=['governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("impose_strict_price_caps_on_seats", "Enforce strict price caps on private colleges and mandate a 50% government quota in all private institutions.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Private college managements association files a petition in High Court, staying the cap.", eff(-1, 0, -2, -2)), 1.2),
        reaction("expose_politician_owned_private_colleges", "Expose list of private colleges owned by ruling party leaders, accusing the bill of being an eyewash.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, -1, 4, 3),
                 {},
                 risk(12, "Colleges deny political ownership, claiming trust-run education status.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_merit_scholarship_fund", "Propose a state-backed merit scholarship fund for students from government schools entering professional courses.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Fund allocation is delayed in the current budget, frustrating applicants.", eff(0, 0, -2, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2003-09
ITEMS_2001_2005.append(make_news(
    key="tn2003_2003_09_the_hindu_breach_privilege",
    month="2003-09",
    title="Speaker Issues Warrants Against 'The Hindu' Journalists",
    desc="The Tamil Nadu Assembly Speaker issues arrest warrants against senior editors of the prominent newspaper 'The Hindu' for alleged breach of privilege in editorial articles.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("defend_house_privilege_and_authority", "Defend the Speaker's decision, stating that the dignity of the legislative house must be protected from biased media.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(20, "Journalist guilds and national newspapers stage joint black-band protests, damaging media image.", eff(-2, 0, -3, -3)), 1.2),
        reaction("condemn_attack_on_press_freedom_demand_withdrawal", "Condemn the warrants as an assault on the fourth estate, hold solidarity rallies, and petition the Governor.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 4),
                 {},
                 risk(14, "Speaker declares the petition invalid, asserting assembly autonomy.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_press_privilege_code_codification", "Propose codifying the assembly's privileges to clearly define rules and avoid arbitrary arrest powers.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "House committee delays discussion on codification indefinitely.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"mediaIssueMissed": 1}, weight=0.25)
    ]
))

# 2003-10
ITEMS_2001_2005.append(make_news(
    key="tn2003_2003_10_dmk_leaves_nda",
    month="2003-10",
    title="DMK Pulls Out of BJP-led NDA Coalition at Centre",
    desc="In a major political realignment, the DMK announces its decision to pull out of the BJP-led National Democratic Alliance (NDA) at the Centre, citing regional interests.",
    tags=['politics'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("minimize_impact_on_state_governance", "Minimize the impact, stating that the state government enjoys a stable majority independent of central alliances.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(15, "Opposition alliance gains momentum, attracting smaller parties to their fold.", eff(-1, 0, -2, -2)), 1.15),
        reaction("consolidate_secular_alliance", "Consolidate the secular alliance in the state by initiating talks with Congress and Left parties for the general election.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Alliance partners demand high seat allocations, causing seat-sharing frictions.", eff(-1, 0, -1, -1)), 1.25),
        reaction("propose_federal_front_resolution", "Propose a joint assembly resolution demanding greater financial autonomy for states under federal lines.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Rival parties prioritize seat bargaining over assembly resolutions.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2003-11
ITEMS_2001_2005.append(make_news(
    key="tn2003_2003_11_rwh_northeast_monsoon",
    month="2003-11",
    title="Heavy Northeast Monsoon Rains Test Rainwater Harvesting",
    desc="Heavy northeast monsoon rains submerge Chennai streets. The recently installed Rainwater Harvesting (RWH) systems across the city face their first major operational test.",
    tags=['governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("advertise_groundwater_recharge_success", "Advertise the rise in Chennai's groundwater levels as proof of the RWH policy's grand success.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Poorly maintained public pits overflow, causing minor street logging in north Chennai.", eff(0, 0, -1, -2)), 1.2),
        reaction("expose_poor_stormwater_drain_maintenance", "Expose the poor condition of stormwater drains, accusing the corporation of causing preventable flooding.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Civic bodies point out that RWH prevented a larger flood, dulling the criticism.", eff(0, 0, -1, -1)), 1.2),
        reaction("propose_joint_drainage_monitoring_cells", "Propose local ward-level monitoring cells with resident welfare associations to audit stormwater layout.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(8, "Low resident participation in initial meetings slows cell formation.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2003-12
ITEMS_2001_2005.append(make_news(
    key="tn2003_2003_12_dpa_alliance_formed",
    month="2003-12",
    title="Democratic Progressive Alliance Formed in Tamil Nadu",
    desc="The DMK formally launches the 'Democratic Progressive Alliance' (DPA) in Tamil Nadu, uniting Congress, PMK, MDMK, and Left parties against the AIADMK-BJP coalition.",
    tags=['politics'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("dismiss_alliance_as_opportunistic", "Dismiss the alliance as an opportunistic grouping of ideologically disparate parties seeking power.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Combined voter base of DPA shows high numbers in initial opinion polls.", eff(-2, 0, -2, -3)), 1.2),
        reaction("launch_joint_rallies_highlight_cadre_unity", "Launch joint public rallies in major cities, demonstrating strong cadre-level coordination among the alliance.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 5),
                 {},
                 risk(14, "Seat-sharing adjustments trigger localized protests by disappointed aspirants.", eff(-1, 0, -2, -1)), 1.3),
        reaction("propose_bipartisan_water_manifesto", "Propose drafting a common water resources manifesto for the state to appeal to delta farming blocks.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Differences in views on neighboring state canals delay the manifesto draft.", eff(0, 0, -1, -1)), 1.15),
        no_comment(weight=0.2)
    ]
))

# 2004-01
ITEMS_2001_2005.append(make_news(
    key="tn2004_2004_01_free_bicycle_scheme",
    month="2004-01",
    title="CM Launches Free Bicycle Scheme for SC/ST School Girls",
    desc="Chief Minister Jayalalithaa launches a welfare scheme to distribute free bicycles to all SC/ST girl students in government-aided schools to curb dropout rates.",
    tags=['governance', 'welfare'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("expand_scheme_to_all_backward_class_girls", "Expand the scheme to include all backward class girl students in government schools immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 5),
                 {},
                 risk(15, "Budget department notes substantial extra cost, warning of capital fund cuts.", eff(0, 0, -2, -2)), 1.25),
        reaction("demand_free_textbooks_and_uniforms_first", "Demand that the state government first distribute quality textbooks and uniforms, calling the bicycles a gimmick.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Parents of beneficiary girls welcome the bicycles, ignoring the opposition critique.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_local_bicycle_assembly_hubs", "Propose setting up local assembly hubs in rural districts to generate job opportunities for youth.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(10, "Bicycle manufacturers refuse to set up scattered assembly lines due to logistics.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 1}, weight=0.2)
    ]
))

# 2004-02
ITEMS_2001_2005.append(make_news(
    key="tn2004_2004_02_vaiko_released_jail",
    month="2004-02",
    title="MDMK Leader Vaiko Released on Bail After 19 Months",
    desc="MDMK General Secretary Vaiko is released on bail from Vellore prison after spending 19 months in detention under POTA. A large crowd of supporters gathers at the prison gates.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("reiterate_cases_stand_in_courts", "State that the release is on bail and that the trial for his unlawful speeches will proceed strictly in court.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(15, "Vaiko launches a massive state-wide tour, drawing large crowds and critical press.", eff(-1, 0, -2, -2)), 1.15),
        reaction("welcome_leader_intensify_dpa_campaign", "Organize a massive welcome rally in Chennai and integrate him into the front-line DPA campaign.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Opposing allies release old videos of his controversial speeches, causing minor friction.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_pota_review_assembly_resolution", "Propose a unanimous assembly resolution urging the Centre to repeal POTA during the winter session.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Ruling coalition opposes the resolution, blocking the assembly debate.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2004-03
ITEMS_2001_2005.append(make_news(
    key="tn2004_2004_03_general_election_campaigns",
    month="2004-03",
    title="Lok Sabha Campaigns Peak; DPA Targets Employee Anger",
    desc="With the general election approaching, the DPA alliance heavily targets the AIADMK government's previous actions against striking government employees and anti-conversion laws.",
    tags=['election'],
    base_w=1.25, profile="election",
    reactions=[
        reaction("announce_post_poll_welfare_benefits", "Announce plans to increase state pension allocations for government employees after the elections.",
                 ['GOVERNMENT'], eff(1, 0, 2, 3),
                 {},
                 risk(18, "Employees view the announcement as an insincere pre-election promise, showing skepticism.", eff(-1, 0, -2, -2)), 1.2),
        reaction("campaign_with_reinstated_staff_unions", "Campaign jointly with reinstated employees and minority groups, highlight the 'draconian' past rules.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 5),
                 {},
                 risk(12, "Governing party cadres release files on historical strikes during opposition rule.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_bipartisan_pension_reforms", "Propose a bipartisan committee to design a sustainable pension system that guarantees employee safety.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Voters find technical pension details too complex, limiting campaign impact.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2004-04
ITEMS_2001_2005.append(make_news(
    key="tn2004_2004_04_lok_sabha_polling",
    month="2004-04",
    title="High Turnout Recorded in Tamil Nadu Lok Sabha Polling",
    desc="Tamil Nadu records a high voter turnout of over 62% in the Lok Sabha elections. Polling passes off peacefully with minor scuffles in Madurai and Tiruchirappalli.",
    tags=['election'],
    base_w=1.2, profile="election",
    reactions=[
        reaction("express_confidence_in_development_mandate", "Express confidence that silent voters have supported the government's infrastructure and water projects.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Exit polls predict a significant sweep for the opposition alliance.", eff(-1, 0, -2, -2)), 1.15),
        reaction("thank_voters_for_protesting_authoritarianism", "Release statements thanking the voters for turning out in large numbers to reject authoritarian governance.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Minor alliance partners complain about insufficient media focus on their candidates.", eff(-1, 0, -1, -1)), 1.25),
        reaction("propose_post_poll_all_party_dinner", "Propose an all-party dinner to maintain cordial political relations after a heated election campaign.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Major leaders decline the invitation, leaving the event low-profile.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2004-05
ITEMS_2001_2005.append(make_news(
    key="tn2004_2004_05_dpa_sweep_rollback",
    month="2004-05",
    title="DPA Sweeps Tamil Nadu; Government Rolls Back Key Laws",
    desc="The DPA sweeps all 39 Lok Sabha seats in Tamil Nadu. In response to the defeat, Chief Minister Jayalalithaa announces the complete rollback of the anti-conversion act and animal sacrifice ban.",
    tags=['election', 'politics'],
    base_w=1.35, profile="election",
    reactions=[
        reaction("declare_policy_corrections_in_public_interest", "State that the rollbacks are made in deference to the public sentiment and promise fresh welfare steps.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(20, "Opposition mocks the rollbacks as political desperation and demands the CM's resignation.", eff(-2, 0, -2, -3)), 1.2),
        reaction("label_rollback_as_moral_victory", "Label the rollbacks as a massive moral victory for the DPA coalition's persistent public campaigns.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 5),
                 {},
                 risk(15, "Alliance partners begin intense lobbying for ministerial berths in the new central cabinet.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_referendum_mechanism", "Propose establishing a legislative referendum system to test major social bills before enacting them.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Legal experts cite constitutional limits on state-level referendums, stalling the bill.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.15)
    ]
))

# 2004-06
ITEMS_2001_2005.append(make_news(
    key="tn2004_2004_06_veeranam_completed",
    month="2004-06",
    title="New Veeranam Project Completed; Water Reaches Chennai",
    desc="The New Veeranam Project is successfully completed. Drinking water from Veeranam Lake is piped to Chennai, easing the city's acute water crisis.",
    tags=['governance', 'infrastructure'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("inaugurate_with_media_coverage", "Inaugurate the project with extensive media coverage highlighting the government's ability to deliver under pressure.",
                 ['GOVERNMENT'], eff(2, 0, 3, 5),
                 {},
                 risk(15, "Opposition claims the pipeline design is prone to leakage and poses ecological risks.", eff(0, 0, -1, -2)), 1.2),
        reaction("audit_project_costs_alleging_graft", "Demand a public audit of the project costs, alleging financial irregularities in the emergency pipe tenders.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 3),
                 {},
                 risk(12, "Metro water board releases details of cost compliance, neutralizing the graft charges.", eff(0, 0, -1, -1)), 1.25),
        reaction("propose_lake_desiltation_program", "Propose a master plan to desilt all major feeding lakes in the state to maximize storage capacity.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "High costs delay the desiltation work in remote rural reservoirs.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2004-07
ITEMS_2001_2005.append(make_news(
    key="tn2004_2004_07_kumbakonam_school_fire",
    month="2004-07",
    title="Tragic Fire at Kumbakonam School Claims 94 Lives",
    desc="A devastating fire breaks out in a thatched-roof school building in Kumbakonam, claiming the lives of 94 young children. The tragedy shocks the nation.",
    tags=['security_crisis', 'disaster_relief'],
    base_w=1.4, profile="security_crisis",
    reactions=[
        reaction("arrest_management_mandate_concrete_roofs", "Order immediate arrest of the school management, announce compensation, and ban thatched roofs in schools.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(20, "Over 500 small rural schools shut down due to inability to construct concrete roofs, leaving students stranded.", eff(-1, 0, -2, -3)), 1.25),
        reaction("demand_resignation_of_education_minister", "Condemn the government's poor safety inspection systems and demand the immediate resignation of the education minister.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Ruling party releases safety inspection logs from the previous administration, showing similar neglect.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_mandatory_fire_safety_audits", "Propose a joint task force of fire officials and parent groups to audit every school in the state in 30 days.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "Lack of trained fire personnel delays safety certifications for several months.", eff(0, 0, -2, -1)), 1.15),
        no_comment(hidden={"securityIgnoredMemory": 4}, weight=0.1)
    ]
))

# 2004-08
ITEMS_2001_2005.append(make_news(
    key="tn2004_2004_08_kanchi_seer_national_talks",
    month="2004-08",
    title="Kanchi Seer Meets Delegates on National Temple Reforms",
    desc="Kanchi Kamakoti Peetham pontiff Jayendra Saraswathi hosts a high-profile meeting of religious scholars to propose national temple management reforms, drawing media focus.",
    tags=['identity'],
    base_w=1.1, profile="identity",
    reactions=[
        reaction("welcome_seer_reforms", "Welcome the Seer's proposals and offer state administrative support to host regional conferences.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(14, "Secular organizations accuse the government of promoting orthodox Brahminical influence.", eff(-1, 0, -2, -1)), 1.15),
        reaction("protest_religious_interference_in_governance", "Organize press meets asserting that temple lands and properties belong to the public, not religious heads.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Traditionalist Hindu groups accuse the party of anti-religious bias.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_bipartisan_cultural_heritage_trust", "Propose a public heritage trust to manage ancient temple architectures without changing worship customs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Both priests and secularists refuse to participate in the trust, stalling it.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 1}, weight=0.3)
    ]
))

# 2004-09
ITEMS_2001_2005.append(make_news(
    key="tn2004_2004_09_metro_feasibility_study",
    month="2004-09",
    title="Feasibility Study for Chennai Metro Rail Project Initiated",
    desc="The state government commissions a preliminary technical feasibility study for a modern Metro Rail network in Chennai to address growing traffic congestion.",
    tags=['governance', 'infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("approve_metro_funding_plan", "Approve the state's equity share and formally request central funding under joint ownership.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Central ministries request revisions in route maps, delaying the cabinet clearance.", eff(0, 0, -1, -1)), 1.2),
        reaction("demand_priority_for_buses_and_flyovers", "Demand the budget be spent on low-cost electric buses and flyovers, calling the Metro an expensive luxury.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Urban commuters and tech professionals criticize the party's short-sighted transport views.", eff(0, 0, -2, -2)), 1.2),
        reaction("propose_joint_suburban_rail_integration", "Propose integrating the Metro plan with the existing suburban railway network to ensure low-cost travel.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Railway board cites technical differences in tracks, stalling the integration talks.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2004-10
ITEMS_2001_2005.append(make_news(
    key="tn2004_2004_10_veerappan_operation_cocoon",
    month="2004-10",
    title="Forest Smuggler Veerappan Shot Dead in Operation Cocoon",
    desc="In a major security breakthrough, forest brigand and sandalwood smuggler Veerappan is shot dead by the Tamil Nadu Special Task Force (STF) in 'Operation Cocoon'.",
    tags=['security_crisis'],
    base_w=1.35, profile="security_crisis",
    reactions=[
        reaction("celebrate_stf_success_award_officers", "Celebrate the operation as a historic success for state law and order, and announce promotions for STF officers.",
                 ['GOVERNMENT'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Human rights groups demand an autopsy, alleging the shootout was a staged encounter.", eff(-1, 0, -2, -2)), 1.25),
        reaction("demand_judicial_probe_on_encounter", "Demand a judicial inquiry into the circumstances of the shootout, claiming key secrets were buried with him.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Public and police families criticize the party for seeming to side with a criminal.", eff(-1, 0, -2, -2)), 1.2),
        reaction("propose_forest_development_package", "Propose a special development and livelihood package for the tribal villages in the Sathyamangalam hills.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Administrative delays keep the tribal package funds stuck in department accounts.", eff(0, 0, -2, -1)), 1.15),
        no_comment(hidden={"securityIgnoredMemory": 1}, weight=0.2)
    ]
))

# 2004-11
ITEMS_2001_2005.append(make_news(
    key="tn2004_2004_11_kanchi_seer_arrest",
    month="2004-11",
    title="Kanchi Seer Jayendra Saraswathi Arrested in Murder Case",
    desc="The chief pontiff of the Kanchi Mutt, Jayendra Saraswathi, is arrested by state police in connection with the murder of temple manager Sankararaman. The arrest sparks intense debate.",
    tags=['security_crisis', 'identity'],
    base_w=1.35, profile="security_crisis",
    reactions=[
        reaction("assert_no_one_above_law_in_murder", "Assert that the law is supreme, stating that the arrest was based on concrete forensic evidence in a murder case.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(22, "National conservative bodies and political outfits organize country-wide protests, calling it an assault on faith.", eff(-2, 0, -3, -4)), 1.2),
        reaction("warn_against_religious_victimization_of_mutt", "Warn against the selective targeting of traditional institutions, demanding that the case be handed to CBI.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(15, "Secular voters and subaltern forums accuse the party of soft-pedaling on a criminal case.", eff(-1, 0, -2, -2)), 1.25),
        reaction("propose_fast_track_court_trial", "Propose a fast-track court trial in a neighboring state to ensure an unbiased judicial outcome without street clashes.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Supreme Court transfer hearings delay the start of the trial by months.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"securityIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2004-12
ITEMS_2001_2005.append(make_news(
    key="tn2004_2004_12_tsunami_disaster",
    month="2004-12",
    title="Indian Ocean Tsunami Devastates Coastal Tamil Nadu",
    desc="Giant tsunami waves triggered by a massive earthquake devastate coastal Tamil Nadu, particularly Nagapattinam and Cuddalore, claiming over 8,000 lives in the state.",
    tags=['disaster_relief'],
    base_w=1.45, profile="disaster_relief",
    reactions=[
        reaction("deploy_full_state_machinery_aid", "Deploy the military and state administration for immediate rescue, relief distribution, and temporary shelters.",
                 ['GOVERNMENT'], eff(3, 0, 4, 5),
                 {},
                 risk(20, "Rehabilitation projects face land allotment delays, causing protests in fishing hamlets.", eff(-1, 0, -2, -3)), 1.3),
        reaction("demand_national_disaster_declaration", "Demand the Centre declare the tsunami a national disaster and fully fund permanent concrete housing for fishermen.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 5),
                 {},
                 risk(15, "Inter-departmental audits delay the release of central housing grants.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_tsunami_early_warning_system", "Propose establishing a state-of-the-art deep-sea oceanographic early warning system along the coastline.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(10, "Technical delay in import of sensor units keeps the warning system offline for a year.", eff(0, 0, -2, -1)), 1.15),
        no_comment(hidden={"disasterIgnoredMemory": 5}, weight=0.1)
    ]
))

# 2005-01
ITEMS_2001_2005.append(make_news(
    key="tn2005_2005_01_tsunami_relief_camps",
    month="2005-01",
    title="Tsunami Relief Camps Face Claims of Resource Disparities",
    desc="As relief camps operate in Nagapattinam, Dalit organizations allege social discrimination and resource disparities in aid distribution by local committees.",
    tags=['disaster_relief'],
    base_w=1.25, profile="disaster_relief",
    reactions=[
        reaction("appoint_government_relief_supervisors", "Appoint direct government administrative officers to oversee all relief camps and ensure equal distribution.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Local private donors object to government takeover of their camps, slowing aid supply.", eff(0, 0, -2, -1)), 1.2),
        reaction("demand_all_party_relief_audit", "Demand an all-party audit of aid distribution lists to identify and correct caste-based exclusions.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Bureaucrats claim auditing mid-relief disrupts operations, leading to delays.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_biometric_aid_cards", "Propose issuing biometric relief smartcards to guarantee direct delivery of aid to every family head.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Lack of card readers in remote coastal zones delays verification.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2005-02
ITEMS_2001_2005.append(make_news(
    key="tn2005_2005_02_seer_granted_bail",
    month="2005-02",
    title="Supreme Court Grants Bail to Kanchi Seer",
    desc="The Supreme Court grants bail to Kanchi pontiff Jayendra Saraswathi, criticizing the state prosecution for lack of direct evidence to justify long-term detention.",
    tags=['politics', 'identity'],
    base_w=1.2, profile="identity",
    reactions=[
        reaction("comply_with_bail_strengthen_charge_sheet", "Comply with the bail order, directing the state law cell to compile supplementary charge sheets with forensic logs.",
                 ['GOVERNMENT'], eff(1, 0, 2, 2),
                 {},
                 risk(15, "Media publishes leaks of the weak case logs, leading to criticism of state police.", eff(-1, 0, -2, -2)), 1.15),
        reaction("hail_bail_demand_independent_probe", "Hail the Supreme Court bail order, calling the case a political frame-up, and demand a CBI investigation.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(14, "Activists accuse the party of trying to derail a serious criminal investigation.", eff(-1, 0, -1, -2)), 1.25),
        reaction("propose_religious_institutions_act_review", "Propose reviewing the HR&CE Act to define the boundaries of police action inside math properties.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Secular MLAs raise concerns about weakening state oversight of temple funds.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.25)
    ]
))

# 2005-03
ITEMS_2001_2005.append(make_news(
    key="tn2005_2005_03_vat_implementation",
    month="2005-03",
    title="State Introduces Value Added Tax; Merchants Protest",
    desc="The state government tables a bill to implement the Value Added Tax (VAT) system, triggering protests and shutdowns from retail merchant associations.",
    tags=['governance', 'economy'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("implement_vat_with_retailer_exemptions", "Implement VAT on schedule, but raise the exemption threshold for small-scale local retailers.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(15, "Revenue collections fall below target, leading to fiscal limits in welfare funds.", eff(0, 0, -2, -2)), 1.2),
        reaction("lead_merchant_dharnas_against_double_taxation", "Lead merchant dharnas, demanding the suspension of VAT until a simplified single-point tax is designed.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Economists criticize the opposition for stalling crucial fiscal modernization.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_vat_education_workshops", "Propose setting up computerized VAT facilitation centers in all market zones to assist shopkeepers.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Software errors in billing terminals delay transactions, causing initial chaos.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"economyIssueMissed": 1}, weight=0.25)
    ]
))

# 2005-04
ITEMS_2001_2005.append(make_news(
    key="tn2005_2005_04_riverbed_sand_mining",
    month="2005-04",
    title="High Court Orders Halt on Illegal Riverbed Sand Mining",
    desc="Responding to PILs on ecological damage to Palar and Cauvery rivers, the Madras High Court orders a temporary halt on unlicensed sand mining operations.",
    tags=['governance', 'land_rights'],
    base_w=1.2, profile="land_rights",
    reactions=[
        reaction("takeover_sand_quarries_under_state_corp", "Take over all sand mining operations under the state public works corporation to regulate extraction.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Construction industries strike over sand supply shortages and price hikes.", eff(-1, 0, -2, -2)), 1.25),
        reaction("demand_cbi_probe_on_mining_cartels", "Demand a CBI probe into political links of private sand mining barons who bypassed court limits.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, -1, 4, 3),
                 {},
                 risk(14, "Construction workers union protests against the party for blocking their daily wages.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_manufactured_sand_subsidies", "Propose state subsidies for manufactured sand (M-sand) to reduce dependency on riverbed extraction.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Builders claim M-sand quality is unverified, slowing down adoption.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 2}, weight=0.2)
    ]
))

# 2005-05
ITEMS_2001_2005.append(make_news(
    key="tn2005_2005_05_it_boom_sholinganallur",
    month="2005-05",
    title="Special Economic Zones Cleared in Sholinganallur",
    desc="The government clears land approvals for Special Economic Zones (SEZs) in Sholinganallur, OMR, paving the way for IT parks and housing complexes.",
    tags=['economy'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("fast_track_infrastructure_in_sez", "Fast-track road, power, and water supply to the SEZ to attract global tech developers.",
                 ['GOVERNMENT'], eff(1, 0, 3, 4),
                 {},
                 risk(12, "Local environment groups protest water extraction from nearby marshlands.", eff(0, 0, -2, -1)), 1.2),
        reaction("demand_affordable_housing_mandate", "Demand that developers reserve 30% of the SEZ residential area for low-income and service staff housing.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Real estate lobbies delay projects, claiming the mandate makes them unviable.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_monorail_link_for_it_corridor", "Propose a state-backed Monorail link along OMR to connect the SEZ directly with the city suburbs.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Private transit operators lobby against the track layout, slowing approvals.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"economyIssueMissed": 1}, weight=0.25)
    ]
))

# 2005-06
ITEMS_2001_2005.append(make_news(
    key="tn2005_2005_06_vaiko_alliance_shifts",
    month="2005-06",
    title="MDMK Leader Vaiko Meets Chief Minister; Alliance Shift Indicated",
    desc="MDMK chief Vaiko holds a surprise meeting with CM Jayalalithaa, indicating a major shift in political alliances ahead of next year's assembly elections.",
    tags=['politics'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("welcome_meeting_as_constructive", "Welcome the meeting as a constructive step towards building a broad coalition based on state interests.",
                 ['GOVERNMENT'], eff(2, 0, 2, 3),
                 {},
                 risk(15, "Alliance cadres express confusion given past arrests under POTA by the CM.", eff(-1, 0, -2, -1)), 1.15),
        reaction("dismiss_alliance_shift_as_opportunistic", "Dismiss the shift as opportunistic, stating that the public remembers the leader's past jail term.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "A segment of voters views the opposition as insecure about losing allies.", eff(0, 0, -1, -1)), 1.2),
        reaction("propose_code_of_alliance_ethics", "Propose establishing a code of alliance ethics to ensure coalition shifts are based on policies rather than posts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Rival parties ignore the code, focusing on seat bargaining.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2005-07
ITEMS_2001_2005.append(make_news(
    key="tn2005_2005_07_unorganized_labor_welfare",
    month="2005-07",
    title="Government Announces Welfare Board for Unorganized Workers",
    desc="The state government announces the establishment of a dedicated welfare board for construction workers, weavers, and unorganized manual laborers, providing pensions and insurance.",
    tags=['governance', 'welfare'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("increase_welfare_benefits", "Increase the pension allocation and add education grants for children of registered laborers.",
                 ['GOVERNMENT'], eff(2, 0, 3, 5),
                 {},
                 risk(15, "Registration process is slowed down by lack of digital files in rural blocks.", eff(0, 0, -2, -2)), 1.25),
        reaction("demand_spot_registration_in_villages", "Demand that the government organize spot registration camps in villages to bypass middleman bribe demands.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Ruling party sets up camps, claiming credit for the opposition's idea.", eff(0, 0, -1, -1)), 1.2),
        reaction("propose_universal_labor_insurance", "Propose a universal health insurance scheme for all unorganized sector workers under joint state-private backing.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Insurance companies demand high premiums, delaying policy rollout.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"welfareIssueMissed": 1}, weight=0.2)
    ]
))

# 2005-08
ITEMS_2001_2005.append(make_news(
    key="tn2005_2005_08_dalit_panchayat_presidents",
    month="2005-08",
    title="Dalit Organizations Protest Over Reserved Panchayat Presidency",
    desc="Protests erupt in southern districts as Dalit organizations demand that the state government enforce rights of Dalit presidents in reserved village panchayats against local caste opposition.",
    tags=['politics', 'identity'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("deploy_special_officers_ensure_safety", "Deploy special district police officers to sensitive panchayats to ensure reserved presidents can function safely.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Dominant local caste organizations block village services in protest, creating friction.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_suspension_of_opposing_ward_members", "Demand the government immediately suspend ward members who boycott meetings called by Dalit presidents.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Local administrative bodies warn that mass suspensions will stall panchayat functions.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_panchayat_equality_workshops", "Propose mandatory district-level equality and legal training workshops for all elected village representatives.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Low attendance by local ward members makes the workshops ineffective.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.2)
    ]
))

# 2005-09
ITEMS_2001_2005.append(make_news(
    key="tn2005_2005_09_stf_excesses_protests",
    month="2005-09",
    title="Protests Over Alleged STF Excesses During Hunt for Veerappan",
    desc="Civil rights groups and Veerappan's widow Muthulakshmi hold a demonstration demanding compensation for forest villagers who allegedly faced excesses during task force years.",
    tags=['protest'],
    base_w=1.15, profile="protest",
    reactions=[
        reaction("appoint_rehabilitation_commission", "Appoint a special retired judge commission to scan compensation claims and provide village development funds.",
                 ['GOVERNMENT'], eff(2, 0, 2, 3),
                 {},
                 risk(15, "STF veterans association protests, claiming the move damages police morale.", eff(-1, 0, -2, -1)), 1.15),
        reaction("demand_cbi_probe_on_stf_human_rights", "Demand a CBI investigation into human rights violations and immediate suspension of implicated officers.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(14, "Ruling party accuses the opposition of trying to defame police heroes.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_forest_tribal_welfare_trust", "Propose a trust run jointly by forest officials and tribal heads to manage local education and employment.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Trust funds are caught in bureaucratic clearances, delaying projects.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2005-10
ITEMS_2001_2005.append(make_news(
    key="tn2005_2005_10_chennai_urban_floods",
    month="2005-10",
    title="Torrential Monsoon Rains Cause Severe Flooding in Chennai",
    desc="Heavy northeast monsoon rains submerge low-lying areas of Chennai. Municipal drainage systems fail, forcing the evacuation of thousands of residents.",
    tags=['disaster_relief'],
    base_w=1.25, profile="disaster_relief",
    reactions=[
        reaction("distribute_cash_and_grain_relief", "Distribute immediate cash relief of Rs 2,000 and dry grains to all affected ration cardholders.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Long queues and chaos at distribution centers lead to local complaints of poor planning.", eff(-1, 0, -2, -2)), 1.25),
        reaction("demand_independent_audit_of_drain_funds", "Demand an independent judicial audit of funds spent on drainage desilting over the past three years.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "Ruling party releases work logs, claiming the flood was due to historic rainfall levels.", eff(0, 0, -1, -1)), 1.2),
        reaction("propose_chennai_waterway_restoration_plan", "Propose a master plan to restore the Adyar and Cooum canals to their original carrying capacities.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Encroachments along the banks delay canal-widening works for a long time.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2005-11
ITEMS_2001_2005.append(make_news(
    key="tn2005_2005_11_minjur_desalination",
    month="2005-11",
    title="Construction of Minjur Desalination Plant Begins",
    desc="The state government lays the foundation stone for the 100 MLD Minjur Desalination Plant to secure drinking water supply for North Chennai, using reverse osmosis.",
    tags=['governance', 'infrastructure'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("fast_track_desalination_terminal", "Fast-track construction works and sign long-term water purchase agreements with developers.",
                 ['GOVERNMENT'], eff(1, 0, 3, 4),
                 {},
                 risk(14, "Environmentalists file petitions warning of saline discharge damage to local fishing grounds.", eff(-1, 0, -1, -1)), 1.2),
        reaction("expose_high_tariff_cost_per_litre", "Expose the project contract files, alleging high water tariffs that will burden city taxpayers.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 3),
                 {},
                 risk(12, "Public prioritizes drinking water safety over marginal cost arguments, ignoring the critique.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_rainwater_and_desalination_mix", "Propose a balanced water grid combining rainwater reservoirs and desalination to keep costs low.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Technical integration of the two different systems slows down pipeline laying.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"environmentalIssueMissed": 1}, weight=0.25)
    ]
))

# 2005-12
ITEMS_2001_2005.append(make_news(
    key="tn2005_2005_12_vyasarpadi_stampede",
    month="2005-12",
    title="Tragic Stampede at Vyasarpadi Flood Relief Center",
    desc="A sudden rush at a flood relief distribution center in Vyasarpadi, Chennai, leads to a tragic stampede in which 42 people lose their lives and many are injured.",
    tags=['security_crisis', 'disaster_relief'],
    base_w=1.35, profile="security_crisis",
    reactions=[
        reaction("announce_increased_ex_gratia_and_enforce_tokens", "Announce Rs 2 lakh ex-gratia, suspend the local center officer, and switch to door-to-door token systems.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Token distribution is slow, leaving many flood-affected families without immediate aid.", eff(0, 0, -2, -2)), 1.2),
        reaction("demand_resignation_of_relief_commissioner", "Demand the resignation of the relief commissioner and hold street protests over poor crowd management.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Police bans assembly near distribution sites, leading to minor clashes.", eff(-1, 0, -2, -1)), 1.25),
        reaction("propose_direct_bank_transfers_for_aid", "Propose transferring all flood cash assistance directly into bank accounts to eliminate physical queues.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(12, "Many rural and poor families lack active bank accounts, slowing down benefit delivery.", eff(0, 0, -2, -1)), 1.15),
        no_comment(hidden={"disasterIgnoredMemory": 4}, weight=0.15)
    ]
))

