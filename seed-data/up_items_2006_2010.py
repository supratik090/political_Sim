from helper import reaction, no_comment, make_news, eff, risk

ITEMS_2006_2010 = []

# 2006-01
ITEMS_2006_2010.append(make_news(
    key="up2006_2006_01_reliance_dadri_protests",
    month="2006-01",
    title="Reliance Dadri Power Land Acquisition Protests Erupt",
    desc="Protests by local farmers against land acquisition for the proposed Reliance power project in Dadri escalate. Protesters block surveyors, demanding higher compensation.",
    tags=['land', 'politics', 'protest'],
    base_w=1.2, profile="land_rights",
    reactions=[
        reaction("enforce_dadri_survey_security", "Enforce the land survey under police protection while offering a revised compensation package for fertile land.",
                 ['GOVERNMENT'], eff(1, 0, 3, 3),
                 {},
                 risk(22, "Police clash with local protesters, leading to injuries and critical media coverage.", eff(-2, 0, -3, -4)), 1.2),
        reaction("join_dadri_resistance_committee", "Join the farmer resistance committee protests, demanding the project land acquisition be scrapped.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(18, "Industrialists accuse the opposition of blocking power infrastructure, reducing urban support.", eff(-2, 0, -1, -2)), 1.25),
        reaction("propose_environmental_impact_roundtable", "Propose a roundtable involving scientists and local farmer representatives to review the project design.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(12, "Radicalized farm groups boycott the roundtable, demanding project cancellation first.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"ruralUnrestIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2006-02
ITEMS_2006_2010.append(make_news(
    key="up2006_2006_02_encephalitis_vaccination_drive",
    month="2006-02",
    title="Gorakhpur Encephalitis Vaccination Drive Launched",
    desc="Following the previous year's high casualties, the health department launches a massive vaccination drive in Gorakhpur, targetting Japanese Encephalitis.",
    tags=['health', 'governance', 'good_news'],
    base_w=1.05, profile="governance",
    reactions=[
        reaction("deploy_rural_medical_camps", "Deploy rural medical camps to distribute vaccines directly in schools and village councils.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Vaccine stock shortages occur in remote blocks, leaving children unvaccinated.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_clean_water_program_integration", "Demand the vaccination drive integrate clean drinking water supply checks to block water-borne strains.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(10, "State health department claims budget limitations, slowing down integration.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_clean_water_infrastructure_plan", "Propose a state-backed clean drinking water infrastructure plan in affected districts to prevent future outbreaks.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(10, "Funding and agency jurisdiction disputes delay water pipe laying in remote blocks.", eff(0, 0, -2, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2006-03
ITEMS_2006_2010.append(make_news(
    key="up2006_2006_03_varanasi_temple_bombings",
    month="2006-03",
    title="Twin Blasts at Sankat Mochan Temple and Varanasi Station; 28 Killed",
    desc="Two coordinated bomb explosions rip through the Sankat Mochan Temple and Varanasi Cantt railway station, killing 28 and injuring over 100. High alerts issued.",
    tags=['security', 'politics', 'crisis', 'law_order'],
    base_w=1.5, profile="security_crisis",
    reactions=[
        reaction("deploy_paramilitary_temple_security", "Deploy rapid paramilitary forces around sensitive religious complexes and launch a statewide combing operation.",
                 ['GOVERNMENT'], eff(2, 0, 4, 3),
                 {},
                 risk(22, "Identity profiling during searches triggers local protests and minority concerns.", eff(-2, 0, -3, -4)), 1.25),
        reaction("demand_cabinet_resignation_blasts", "Organise public demonstrations and demand the resignation of the state cabinet, citing intelligence and security failures.",
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

# 2006-04
ITEMS_2006_2010.append(make_news(
    key="up2006_2006_04_aligarh_communal_violence",
    month="2006-04",
    title="Aligarh Communal Clashes Trigger Indefinite Curfew",
    desc="Clashes between two communities in Aligarh over a local disputation lead to arson and casualties. The administration imposes an indefinite curfew.",
    tags=['identity', 'violence', 'crisis', 'law_order'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("enforce_curfew_neutral_arrests", "Enforce the curfew strictly, deploy central rapid action forces, and order unbiased arrests of rioters.",
                 ['GOVERNMENT'], eff(1, -1, 3, 2),
                 {},
                 risk(20, "Local community groups accuse the police of partisan behavior during searches.", eff(-2, 0, -3, -4)), 1.2),
        reaction("organise_peace_harmony_marches", "Organise local inter-community harmony walks at curfew boundaries and demand independent judicial audit.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(12, "Radical groups organize counter-rallies, raising communal temperatures.", eff(-1, 0, -2, -2)), 1.2),
        reaction("propose_state_harmony_committee", "Propose a state harmony committee representing all community leaders to discuss grievances peacefully.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing by key members delays the release of the committee's recommendations.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"massCasualtyIgnoredMemory": 3, "identityIssueMissed": 2}, weight=0.2)
    ]
))

# 2006-05
ITEMS_2006_2010.append(make_news(
    key="up2006_2006_05_police_constables_cancelled",
    month="2006-05",
    title="High Court Cancels Recruitment of 22,000 Constables",
    desc="The Allahabad High Court cancels the selection of 22,000 police constables appointed during the SP regime, citing widespread bribery and manipulation of files.",
    tags=['law_order', 'governance', 'corruption'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("comply_cancel_recruitment_blacklist", "Comply with the court order, blacklist the involved officials, and announce fresh transparent recruitment exams.",
                 ['GOVERNMENT'], eff(2, -1, 3, 3),
                 {},
                 risk(15, "Affected constable candidates hold protests, blocking railway tracks in Lucknow.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_cid_investigation_regime_links", "Demand a CID investigation into the political linkages of the recruitment board, alleging corruption in ministerial offices.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "State departments delay access to files, slowing down the CID's initial steps.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_digitized_audit_portal", "Propose a digitized public audit portal to track all related government transactions and block corruption.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(12, "Technical integration delays keep the portal offline, drawing criticism for slow delivery.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"corruptionIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2006-06
ITEMS_2006_2010.append(make_news(
    key="up2006_2006_06_meerut_farmers_price_protests",
    month="2006-06",
    title="Sugarcane Farmers Protest Meerut Sugar Mill Payment Delays",
    desc="Sugarcane growers hold sit-ins outside private sugar mills in Meerut, protesting delayed payments and demanding the state enforce interest clauses on arrears.",
    tags=['rural', 'agriculture', 'protest'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("mandate_asset_liquidation_private_mills", "Issue a mandate to liquidate private sugar mill stocks to clear farmer dues within 30 days.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Mill owners challenge the mandate in court, stalling stock liquidation.", eff(-1, 0, -2, -2)), 1.25),
        reaction("lead_farmers_dharna_commissioner", "Lead farmer dharnas at the Meerut commissioner's office, demanding immediate state procurement bonus.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Protests block cargo routes, drawing complaints from local industry units.", eff(-1, 0, -2, -2)), 1.15),
        reaction("propose_tripartite_mediation_council", "Propose a tripartite mediation council representing labor unions, industry leaders, and state officials.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Radical sections of the union boycott the mediation, continuing localized protests.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 3}, weight=0.2)
    ]
))

# 2006-07
ITEMS_2006_2010.append(make_news(
    key="up2006_2006_07_bundelkhand_water_supply",
    month="2006-07",
    title="Bundelkhand Water Supply Project Special Package Announced",
    desc="The central government announces a special financial package for Bundelkhand water supply and check-dam construction projects, targeting drought-hit blocks.",
    tags=['rural', 'infrastructure', 'good_news'],
    base_w=1.1, profile="governance",
    reactions=[
        reaction("expedite_check_dam_construction", "Expedite checks and contracts for check-dams, coordinating directly with village panchayats.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Contractor cartels manipulate bids, delaying check-dam construction in Jhansi.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_cag_monitoring_package", "Demand the CAG monitor the package spending directly to prevent local administration leakages.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(10, "Central ministries claim standard state audit rules apply, diluting the demand.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_infrastructure_oversight_committee", "Propose a joint civic-expert oversight committee to monitor construction quality and manage traffic impact.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Inter-departmental coordination issues delay committee meetings, slowing down resolution of issues.", eff(0, 0, -1, -1)), 1.05),
        no_comment(hidden={"disasterIgnoredMemory": 2}, weight=0.25)
    ]
))

# 2006-08
ITEMS_2006_2010.append(make_news(
    key="up2006_2006_08_meerut_fair_fire_tragedy",
    month="2006-08",
    title="Meerut Trade Fair Fire Tragedy; Over 50 Killed",
    desc="A major fire sweeps through consumer goods stalls at a trade fair in Victoria Park, Meerut. Over 50 visitors are killed, sparking anger over lack of safety exits.",
    tags=['disaster', 'law_order', 'crisis'],
    base_w=1.3, profile="security_crisis",
    reactions=[
        reaction("order_magisterial_probe_safety_checks", "Order an immediate magisterial inquiry, cancel licenses of defaulting event managers, and announce victim aid.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(16, "Audit uncovers that municipal officers issued permits without checking fire exits, drawing media fire.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_independent_safety_audits", "Demand independent fire safety audits of all commercial hubs in the NCR zone, blaming civic corruption for the fire.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Chambers of commerce claim audits will halt trade during festival season, slowing progress.", eff(-1, 0, -1, -2)), 1.25),
        reaction("propose_security_advisory_board", "Propose setting up an independent security advisory board with defense experts to upgrade local safety protocols.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(12, "Implementation of board recommendations is delayed due to funding shortages.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"massCasualtyIgnoredMemory": 4}, weight=0.1)
    ]
))

# 2006-09
ITEMS_2006_2010.append(make_news(
    key="up2006_2006_09_mayawati_social_engineering",
    month="2006-09",
    title="Mayawati Sarvajan Samaj conferences Gain Traction",
    desc="BSP leader Mayawati hosts large-scale Brahmin-Dalit coordination conferences under the banner of 'Sarvajan Samaj', aiming to widen traditional caste coalitions.",
    tags=['election', 'politics', 'identity'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("welcome_social_inclusion_agenda", "Welcome the inclusive agenda in public statements, emphasizing backward-forward community harmony.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Traditional base voters express concern over seat dilution, causing minor local friction.", eff(-1, 0, -2, -2)), 1.15),
        reaction("expose_opportunistic_social_coalitions", "Expose past statements of both groups and campaign on opportunistic alliances aimed at securing votes.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Voters welcome the moderation in political rhetoric, diluting the opposition attack.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_state_harmony_committee", "Propose a state harmony committee representing all community leaders to discuss grievances peacefully.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing by key members delays the release of the committee's recommendations.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.25)
    ]
))

# 2006-10
ITEMS_2006_2010.append(make_news(
    key="up2006_2006_10_jama_masjid_imam_up_rally",
    month="2006-10",
    title="Delhi Jama Masjid Shahi Imam Holds Political Rally in UP",
    desc="The Shahi Imam of Delhi's Jama Masjid addresses a massive rally in Western UP, calling for minority alignment and testing electoral alliances ahead of state polls.",
    tags=['politics', 'identity', 'election'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("appeal_communal_harmony_elections", "Appeal to all communities to maintain electoral harmony and focus on developmental issues.",
                 ['GOVERNMENT'], eff(1, 0, 3, 2),
                 {},
                 risk(12, "Radical groups organize counter-rallies, raising local election tensions.", eff(-1, 0, -2, -1)), 1.15),
        reaction("expose_religious_vote_bank_politics", "Hold press conferences condemning the use of religious platforms for seat negotiations, demanding EC monitor rallies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(14, "Minority organizations accuse opposition of trying to suppress voter voice.", eff(0, 0, -2, -2)), 1.2),
        reaction("propose_state_harmony_committee", "Propose a state harmony committee representing all community leaders to discuss grievances peacefully.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing by key members delays the release of the committee's recommendations.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.25)
    ]
))

# 2006-11
ITEMS_2006_2010.append(make_news(
    key="up2006_2006_11_nithari_serial_killings",
    month="2006-11",
    title="Noida Nithari Serial Killings Exposed; Public Anger Erupts",
    desc="Discovery of skeletal remains in a drain in Nithari village, Noida, exposes serial killings of children. Locals stage massive protests, alleging police ignored missing logs.",
    tags=['violence', 'crisis', 'law_order'],
    base_w=1.4, profile="security_crisis",
    reactions=[
        reaction("suspend_noida_police_officers_probe", "Suspend Noida police officers for negligence, register murder cases, and request a CBI probe immediately.",
                 ['GOVERNMENT'], eff(1, -1, 3, 2),
                 {},
                 risk(22, "Dalit organizations launch protests, claiming police ignored victims due to poor background.", eff(-2, 0, -3, -4)), 1.2),
        reaction("lead_nithari_solidarity_marches", "Lead citizen solidarity marches in Noida, demanding immediate rehabilitation for the families and police reforms.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Marchers clash with police checkpoints near the suspect's house, leading to tear gas use.", eff(-1, 0, -2, -2)), 1.25),
        reaction("propose_security_advisory_board", "Propose setting up an independent security advisory board with defense experts to upgrade local safety protocols.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(12, "Implementation of board recommendations is delayed due to funding shortages.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"massCasualtyIgnoredMemory": 5, "securityIgnoredMemory": 4}, weight=0.05)
    ]
))

# 2006-12
ITEMS_2006_2010.append(make_news(
    key="up2006_2006_12_cbi_nithari_investigations",
    month="2006-12",
    title="CBI Takes Charge of Noida Nithari Killings Probe",
    desc="CBI teams assume charge of the Nithari serial killings investigation in Noida, questioning suspects and scanning local administrative records for missing logs.",
    tags=['security', 'law_order', 'politics'],
    base_w=1.3, profile="security_crisis",
    reactions=[
        reaction("cooperate_cbi_investigation_nithari", "Instruct all departments to cooperate with the CBI team and submit required district files immediately.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "CBI summons local administration chiefs, highlighting lack of coordination.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_judicial_commission_child_missing", "Demand a high court judge-led commission to draft standard operating rules for missing children logs.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(10, "Legal process takes months, delaying draft rules release.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_security_advisory_board", "Propose setting up an independent security advisory board with defense experts to upgrade local safety protocols.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(12, "Implementation of board recommendations is delayed due to funding shortages.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"securityIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2007-01
ITEMS_2006_2010.append(make_news(
    key="up2007_2007_01_assembly_elections_announced",
    month="2007-01",
    title="UP Assembly Election Dates Announced; Campaigns Launch",
    desc="The Election Commission announces seven-phase polling dates for the UP assembly elections. Key themes focus on law & order and caste quotas.",
    tags=['election', 'politics'],
    base_w=1.15, profile="election",
    reactions=[
        reaction("campaign_on_development_investment_dadri", "Campaign heavily on industrial development policies and investments in Noida and Kanpur.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Opposition coordination splits the government's voter share in key rural pockets.", eff(-1, 0, -2, -2)), 1.15),
        reaction("campaign_on_nithari_recruitment_failures", "Campaign heavily on the Nithari case and the police recruitment scams, demanding change in leadership.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Internal bickerings over ticket allocation spark minor rebel candidates contesting.", eff(-1, 0, -2, -2)), 1.2),
        reaction("propose_legislative_roundtable", "Propose a legislative roundtable with representatives from all parties to draft a consensus policy on the issue.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 2, 2),
                 {},
                 risk(8, "Lack of consensus among members delays the final report, rendering it inactive.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2007-02
ITEMS_2006_2010.append(make_news(
    key="up2007_2007_02_elections_campaigns_peak",
    month="2007-02",
    title="Electoral Campaigns Peak Ahead of First Phase Polling",
    desc="Rallies peak across UP divisions. Mayawati's BSP reaches out to Brahmin-Dalit combinations, and Samajwadi Party highlights industrial investments.",
    tags=['election', 'politics'],
    base_w=1.2, profile="election",
    reactions=[
        reaction("promise_farm_arrears_clearance", "Promise state-funded clearances of private sugar mill farmer arrears in election manifestos.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Election Commission issues notice regarding violation of model code of conduct.", eff(-1, 0, -2, -1)), 1.2),
        reaction("expose_constable_bribery_scam_belt", "Organise public assemblies in central districts exposing constables bribery and recruitment cancellations.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(10, "Government candidates claim recruitments were stayed by court, diluting the attack.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_direct_mayoral_elections", "Propose structural reforms to allow direct election of mayors to ensure civic accountability.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Voters show low interest in structural civic reforms during the high-volume campaign.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2007-03
ITEMS_2006_2010.append(make_news(
    key="up2007_2007_03_assembly_polling_phases",
    month="2007-03",
    title="Seven-Phase UP Assembly Polling Begins",
    desc="Balloting begins for the UP legislative assembly. Paramilitary units are deployed in central and eastern districts to check booth violence.",
    tags=['election', 'politics', 'law_order'],
    base_w=1.2, profile="election",
    reactions=[
        reaction("paramilitary_deployment_booths", "Deploy additional central rapid deployment forces in critical booths and check identities strictly.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Voter turnout drops in locked-down pockets, causing local party worker frustration.", eff(-1, 0, -2, -2)), 1.2),
        reaction("document_booth_irregularities_ec", "Submit logs of alleged local administration bias and request re-polling in flagged booth registers.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Election Commission rejects the complaints as unsubstantiated, reducing impact.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_digitized_voter_verification", "Propose launching biometric-based digitized voter verification systems at sensitive polling booths.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Implementation cost is deemed high by state election departments, stalling progress.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.35)
    ]
))

# 2007-04
ITEMS_2006_2010.append(make_news(
    key="up2007_2007_04_bsp_absolute_majority",
    month="2007-04",
    title="BSP Wins Historic Absolute Majority; Mayawati Sworn In as CM",
    desc="Bahujan Samaj Party (BSP) wins 206 out of 403 seats, securing a historic absolute majority in UP. Mayawati is sworn in as the Chief Minister.",
    tags=['election', 'politics', 'good_news'],
    base_w=1.3, profile="election",
    reactions=[
        reaction("commit_to_unified_governance", "Commit to unified governance, fast-tracking agricultural packages, and maintaining coalition coordination.",
                 ['GOVERNMENT'], eff(2, 0, 4, 3),
                 {},
                 risk(18, "Cabinet portfolio disputes between NCP and Congress surface immediately, generating critical press.", eff(-1, 0, -2, -2)), 1.2),
        reaction("characterize_change_as_incumbency_panic", "Characterize the leadership change as a sign of panic over economic decline and demand early assembly elections.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(12, "New CM's clean image and background receive positive media reviews, dampening the attack.", eff(-1, 0, -1, -1)), 1.25),
        reaction("propose_legislative_roundtable", "Propose a legislative roundtable with representatives from all parties to draft a consensus policy on the issue.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 2, 2),
                 {},
                 risk(8, "Lack of consensus among members delays the final report, rendering it inactive.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.25)
    ]
))

# 2007-05
ITEMS_2006_2010.append(make_news(
    key="up2007_2007_05_police_recruitment_investigation",
    month="2007-05",
    title="CM Mayawati Orders Probe into SP-Era Police Recruitments",
    desc="Chief Minister Mayawati orders a comprehensive investigation into all police constables recruitments executed between 2004 and 2006, alleging systemic bribes.",
    tags=['governance', 'corruption', 'politics'],
    base_w=1.2, profile="corruption",
    reactions=[
        reaction("order_board_audits_suspend_officers", "Order audits of recruitments board sheets, suspend the board chiefs, and blacklist suspect recruiters.",
                 ['GOVERNMENT'], eff(2, -2, 3, 3),
                 {},
                 risk(18, "Affected candidate groups organize protest rallies in Lucknow, claiming selective targeting.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_cbi_investigation_into_regime", "Demand the CBI take over the police recruitment files, alleging systemic involvement of CM's close aides.",
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

# 2007-06
ITEMS_2006_2010.append(make_news(
    key="up2007_2007_06_ips_officers_suspended",
    month="2007-06",
    title="Dozens of IPS and PPS Officers Suspended in UP",
    desc="The UP government suspends dozens of senior police officers (IPS/PPS) who headed recruitment boards, following reports from the special recruitment inquiry.",
    tags=['governance', 'law_order', 'politics'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("blacklist_corrupt_officers_announcements", "Blacklist the suspended officers from key district assignments and announce department-wide transparency audits.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Officers challenge the suspensions in the Central Administrative Tribunal, stalling trials.", eff(-1, 0, -2, -1)), 1.15),
        reaction("demand_restatement_of_wrongly_suspended", "Demand the reinstatement of officers, claiming the suspensions are politically motivated acts against specific castes.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Media details the bribery case sheets, diluting the opposition's defense.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_fixed_bureaucratic_tenures", "Propose establishing a Civil Services Board to enforce fixed tenures for administrative officers, reducing political interference.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political parties ignore the proposal as a limit on their executive powers.", eff(0, 0, -2, -1)), 1.05),
        no_comment(hidden={"governanceIssueMissed": 2}, weight=0.25)
    ]
))

# 2007-07
ITEMS_2006_2010.append(make_news(
    key="up2007_2007_07_sp_protests_ लखनऊ",
    month="2007-07",
    title="Samajwadi Party Cadres Hold Statewide Protest Rallies",
    desc="Samajwadi Party cadres clash with police during statewide protest rallies in Lucknow and Kanpur, protesting against selective arrests of their local unit leaders.",
    tags=['politics', 'protest', 'law_order'],
    base_w=1.15, profile="protest",
    reactions=[
        reaction("deploy_police_checkpoints_secretariat", "Deploy police checkpoints around the secretariat and detain violent agitators to maintain civic order.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Detention of senior MLAs triggers local highway blockades in Central UP.", eff(-1, 0, -2, -2)), 1.2),
        reaction("lead_legislative_protests", "Lead walkouts in the assembly and carry black banners to protest police high-handedness during rallies.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Rally blockades disrupt city transport, drawing complaints from commuter unions.", eff(-1, 0, -1, -2)), 1.25),
        reaction("propose_state_harmony_committee", "Propose a state harmony committee representing all community leaders to discuss grievances peacefully.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing by key members delays the release of the committee's recommendations.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"violenceIgnoredMemory": 2}, weight=0.25)
    ]
))

# 2007-08
ITEMS_2006_2010.append(make_news(
    key="up2007_2007_08_ganga_expressway_proposal",
    month="2007-08",
    title="Mayawati Government Proposes Noida-Ballia Ganga Expressway",
    desc="The UP government proposes the Ganga Expressway project connecting Noida to Ballia, promising a major infrastructure corridor and rapid industrialization of Eastern districts.",
    tags=['economy', 'infrastructure', 'governance'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("fast_track_corridor_land_acquisition", "Fast-track land surveys and announce a revised rehabilitation package for farmers along the expressway alignment.",
                 ['GOVERNMENT'], eff(2, 0, 4, 3),
                 {},
                 risk(20, "Environmental groups file petitions claiming the alignment damages Yamuna/Ganga floodplains.", eff(-1, 0, -2, -3)), 1.2),
        reaction("demand_independent_ecological_survey", "Demand an independent ecological and agricultural impact survey, claiming fertile crop fields are acquired at low rates.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Urban business associations accuse opposition of blocking NCR connectivity, affecting support.", eff(-1, 0, -1, -2)), 1.15),
        reaction("propose_infrastructure_oversight_committee", "Propose a joint civic-expert oversight committee to monitor construction quality and manage traffic impact.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Inter-departmental coordination issues delay committee meetings, slowing down resolution of issues.", eff(0, 0, -1, -1)), 1.05),
        no_comment(hidden={"economyMissedOpportunity": 2}, weight=0.25)
    ]
))

# 2007-09
ITEMS_2006_2010.append(make_news(
    key="up2007_2007_09_terai_region_floods",
    month="2007-09",
    title="Severe Monsoons Submerge Crop Fields in Terai Region",
    desc="Heavy monsoons cause severe flooding in Lakhimpur Kheri and Bahraich districts, displacing thousands. Standing sugarcane and paddy fields are submerged.",
    tags=['disaster', 'relief', 'rural'],
    base_w=1.15, profile="disaster_relief",
    reactions=[
        reaction("deploy_relief_camps_direct_grants", "Deploy emergency rescue teams, distribute grain packets, and release immediate compensation to affected families.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(16, "Relief distribution is delayed by damaged rural roads, causing protests at block offices.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_state_waive_local_crop_loans", "Demand the state government waive local agricultural crop loans and declare a complete moratorium on debt recoveries.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "State cooperative banks face liquidity issues, limiting credit roll-overs.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_all_party_relief_coordination", "Propose an all-party disaster relief coordination cell to streamline distribution of emergency supplies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(10, "Administrative delays in cargo clearance temporarily halt relief shipments.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2007-10
ITEMS_2006_2010.append(make_news(
    key="up2007_2007_10_kanshiram_memorial_inauguration",
    month="2007-10",
    title="Kanshiram Memorial Park Inaugurated in Lucknow",
    desc="Chief Minister Mayawati inaugurates the Kanshiram Memorial Park in Lucknow. Opposition parties hold protests over the allocation of state funds for statues.",
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

# 2007-11
ITEMS_2006_2010.append(make_news(
    key="up2007_2007_11_civil_court_bombings",
    month="2007-11",
    title="Civil Court Bombings Strike Faizabad, Varanasi, Lucknow",
    desc="Coordinated bomb explosions rip through civil court complexes in Faizabad, Varanasi, and Lucknow. Over 15 lawyers and litigants are killed; high security alerts are declared.",
    tags=['security', 'violence', 'crisis', 'law_order'],
    base_w=1.4, profile="security_crisis",
    reactions=[
        reaction("deploy_armed_police_court_premises", "Deploy armed security forces at all district courts, set up entry metal detectors, and coordinate central intelligence.",
                 ['GOVERNMENT'], eff(2, 0, 4, 3),
                 {},
                 risk(22, "Security check queues at court entrances trigger lawyer protests over delays.", eff(-2, 0, -3, -4)), 1.25),
        reaction("demand_cabinet_resignation_court_failures", "Organise public demonstrations and demand the resignation of the state cabinet, citing intelligence and security failures.",
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

# 2007-12
ITEMS_2006_2010.append(make_news(
    key="up2007_2007_12_dadri_land_acquisition_cancelled",
    month="2007-12",
    title="Dadri Land Acquisition Cancelled for Reliance Power",
    desc="Following prolonged farmer protests and court stay orders, the state government cancels the land acquisition for the Reliance gas-based power project in Dadri.",
    tags=['land', 'economy', 'protest'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("return_land_to_farmers_advertise_justice", "Return the acquired land to farmers immediately and advertise the step as a major triumph of agrarian justice.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Reliance Energy files a compensation claim for development costs, stalling land return registers.", eff(-1, 0, -2, -2)), 1.2),
        reaction("expose_industrial_investments_failure_dadri", "Campaign heavily on industrial policy failures, claiming the cancellation will drive away NCR investments.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Local farmers welcome the cancellation, diluting the industrial development pitch.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_tripartite_mediation_council", "Propose a tripartite mediation council representing labor unions, industry leaders, and state officials.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Radical sections of the union boycott the mediation, continuing localized protests.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"economyMissedOpportunity": 2}, weight=0.25)
    ]
))

# 2008-01
ITEMS_2006_2010.append(make_news(
    key="up2008_2008_01_winter_cold_wave_potato_crop",
    month="2008-01",
    title="Severe Cold Wave Damages Agra Potato Crops",
    desc="A severe winter cold wave and frost hit Western UP, damaging potato and mustard crops in Agra and Mathura. Farmers demand state crop assessments.",
    tags=['disaster', 'relief', 'rural'],
    base_w=1.1, profile="disaster_relief",
    reactions=[
        reaction("deploy_crop_assessment_teams", "Deploy immediate crop assessment teams from the agriculture department and announce cold wave tax exemptions.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Insurance companies dispute damage estimates, delaying payouts for months.", eff(-1, 0, -2, -2)), 1.15),
        reaction("demand_soft_loans_for_potato_farmers", "Demand that state cooperative banks waive agricultural pump bills and offer soft loans for the next season.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Cooperative banks face cash shortages, limiting the loan volume.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_rural_stabilization_policy", "Propose a bipartisan rural development and price stabilization task force to draft long-term support policies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Lack of immediate budget allocation delays the implementation of the task force proposals.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.25)
    ]
))

# 2008-02
ITEMS_2006_2010.append(make_news(
    key="up2008_2008_02_ganga_expressway_court_halt",
    month="2008-02",
    title="Court Halts Noida-Ballia Ganga Expressway Construction",
    desc="The High Court halts construction work on the Noida-Ballia Ganga Expressway project, citing environmental concerns and lack of clearance near the river basin.",
    tags=['environment', 'infrastructure', 'governance'],
    base_w=1.2, profile="governance",
    reactions=[
        reaction("appeal_to_supreme_court_expressway", "File an appeal in the Supreme Court immediately, requesting a stay on the High Court order to continue works.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Supreme Court declines to grant immediate stay, delaying the project timeline.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_scrapping_expressway_project", "Demand the expressway project be scrapped entirely, claiming the alignment damages Yamuna/Ganga floodplains.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(14, "Construction associations claim cancellation will delay NCR growth, drawing critical press.", eff(-1, 0, -1, -2)), 1.2),
        reaction("propose_independent_riverbed_audit", "Propose an independent committee of river hydrologists and archeologists to redesign the project safely.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Design changes delay project delivery by several years, increasing costs.", eff(0, 0, -1, -1)), 1.05),
        no_comment(hidden={"environmentalIssueMissed": 2}, weight=0.25)
    ]
))

# 2008-03
ITEMS_2006_2010.append(make_news(
    key="up2008_2008_03_student_union_elections_ban",
    month="2008-03",
    title="BSP Government Bans Student Union Elections in State Universities",
    desc="The UP government bans student union elections in state universities, citing law and order concerns. Student groups launch protests in Lucknow and Allahabad.",
    tags=['education', 'protest', 'politics'],
    base_w=1.15, profile="protest",
    reactions=[
        reaction("enforce_ban_maintain_campus_discipline", "Enforce the ban strictly, deploy police patrols near campus gates, and suspend student activists violating rules.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Clashes between student groups and police lead to campus shutdowns in Lucknow.", eff(-1, 0, -2, -2)), 1.15),
        reaction("lead_student_solidarity_rallies_demand", "Address student rallies outside campus gates and demand the state restore democratic student elections.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(14, "Security forces block the rallies, leading to tear gas use and traffic jams.", eff(-1, 0, -2, -2)), 1.2),
        reaction("propose_student_senate_electoral_reforms", "Propose launching reformist student senates with representatives from both student ranks and faculty.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(10, "Student groups reject the senate model, demanding traditional union polls.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2008-04
ITEMS_2006_2010.append(make_news(
    key="up2008_2008_04_noida_double_murder_case",
    month="2008-04",
    title="Aarushi Talwar-Hemraj Murdered in Noida; Media Frenzy",
    desc="A young girl and domestic help are found murdered in their Noida apartment. The Noida police's initial investigations trigger media frenzy and criticism.",
    tags=['violence', 'law_order', 'crisis'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("transfer_aarushi_case_to_cbi", "Transfer the case files to the CBI immediately to ensure a fair and scientifically audited investigation.",
                 ['GOVERNMENT'], eff(2, -1, 3, 3),
                 {},
                 risk(15, "Noida police handling is criticized globally, reflecting poorly on state forensics.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_reform_of_noida_forensics", "Demand a comprehensive reform of Noida police forensics, claiming the crime scene was not secured.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(10, "Police department defends actions as standard, diluting the reform debate.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_security_advisory_board", "Propose setting up an independent security advisory board with defense experts to upgrade local safety protocols.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(12, "Implementation of board recommendations is delayed due to funding shortages.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"massCasualtyIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2008-05
ITEMS_2006_2010.append(make_news(
    key="up2008_2008_05_rajesh_talwar_arrested",
    month="2008-05",
    title="Rajesh Talwar Arrested in Noida Double Murder Probe",
    desc="Noida police arrest Rajesh Talwar, the father of the deceased girl, charging him with the double murder. Public debates rage over police evidence sheets.",
    tags=['violence', 'law_order', 'politics'],
    base_w=1.2, profile="security_crisis",
    reactions=[
        reaction("allow_law_to_take_its_course", "Allow the judicial system to take its course, directing police to submit all case logs to court.",
                 ['GOVERNMENT'], eff(1, 0, 3, 2),
                 {},
                 risk(15, "Defense lawyers present gaps in police logs, causing negative media reviews.", eff(-1, 0, -2, -1)), 1.15),
        reaction("demand_cbi_takeover_immediate", "Expose errors in police logs at press conferences and demand the CBI take over case custody immediately.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(12, "Transfer processing is delayed by bureaucratic department approvals, dragging case out.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_security_advisory_board", "Propose setting up an independent security advisory board with defense experts to upgrade local safety protocols.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(12, "Implementation of board recommendations is delayed due to funding shortages.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2008-06
ITEMS_2006_2010.append(make_news(
    key="up2008_2008_06_cbi_takes_aarushi_case",
    month="2008-06",
    title="CBI Takes Charge of Noida Double Murder Case",
    desc="CBI teams officially assume charge of the Noida double murder case, questioning suspect staff and scanning original forensic logs from Noida police lines.",
    tags=['security', 'law_order', 'politics'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("instruct_state_police_cooperate_cbi", "Instruct Noida police to cooperate fully with the CBI team, handing over all case files and log books.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "CBI findings dispute Noida police theories, creating local department embarrassment.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_suspension_of_negligent_police", "Demand the immediate suspension of Noida police officers who failed to secure the crime scene.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(10, "Police department defends actions as standard, diluting the reform debate.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_security_advisory_board", "Propose setting up an independent security advisory board with defense experts to upgrade local safety protocols.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(12, "Implementation of board recommendations is delayed due to funding shortages.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2008-07
ITEMS_2006_2010.append(make_news(
    key="up2008_2008_07_indo_us_nuclear_deal_trust_vote",
    month="2008-07",
    title="State Parties Align Over Indo-US Nuclear Deal Trust Vote",
    desc="The Indo-US nuclear deal trust vote in Parliament triggers shifts in UP. BSP opposes the UPA coalition, while Samajwadi Party announces support for the UPA.",
    tags=['politics', 'election'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("defend_sp_support_as_national_interest", "Defend Samajwadi Party's support in public rallies as a step to protect national strategic energy interest.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(16, "Allied minority groups express concern over proximity to UPA policies, reducing support in mixed seats.", eff(-2, 0, -2, -2)), 1.2),
        reaction("denounce_sp_support_as_opportunistic", "Expose past anti-deal statements of SP leaders and campaign on opportunistic alliances aimed at securing central power.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(14, "Rural voters focus on local ticket candidates rather than international nuclear deal clauses.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_legislative_roundtable", "Propose a legislative roundtable with representatives from all parties to draft a consensus policy on the issue.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 2, 2),
                 {},
                 risk(8, "Lack of consensus among members delays the final report, rendering it inactive.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.25)
    ]
))

# 2008-08
ITEMS_2006_2010.append(make_news(
    key="up2008_2008_08_yamuna_expressway_land_protests",
    month="2008-08",
    title="Farmers Protest Yamuna Expressway Land Acquisition Rates",
    desc="Protests by farmers over land acquisition rates for the Yamuna Expressway project erupt in Greater Noida. Protesters block survey vehicles, demanding revised rates.",
    tags=['land', 'protest', 'infrastructure'],
    base_w=1.2, profile="land_rights",
    reactions=[
        reaction("negotiate_higher_compensation_expressway", "Negotiate higher compensation rates with farmer committee representatives and announce job cards for local youth.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Expressway builder groups threaten project halts, citing increased capital costs.", eff(-1, 0, -2, -2)), 1.2),
        reaction("lead_greater_noida_highway_blockade", "Join the farmer blockade in Greater Noida, demanding a statutory law linking compensation directly to market land rates.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Blockade halts industrial cargo movement in Noida NCR, drawing critical press.", eff(-1, 0, -1, -2)), 1.25),
        reaction("propose_tripartite_mediation_council", "Propose a tripartite mediation council representing labor unions, industry leaders, and state officials.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Radical sections of the union boycott the mediation, continuing localized protests.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"ruralUnrestIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2008-09
ITEMS_2006_2010.append(make_news(
    key="up2008_2008_09_swine_flu_lucknow_kanpur",
    month="2008-09",
    title="Swine Flu (H1N1) Cases Reported in Lucknow and Kanpur",
    desc="Health departments confirm Swine Flu (H1N1) virus cases in Lucknow and Kanpur divisions. Isolation wards are activated at district hospitals.",
    tags=['health', 'disaster', 'crisis'],
    base_w=1.15, profile="health_crisis",
    reactions=[
        reaction("fund_h1n1_screening_vaccines", "Allocate emergency state funds for H1N1 screening kits, antiviral medicine stockpiles, and hospital isolation beds.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Screening kits face distribution delays in rural block centers, leaving patients waiting.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_medical_audit_isolation_beds", "Demand an audit of district hospital facilities, claiming that isolation beds are insufficient to check spread.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(10, "State health department rejects central interference, stalling taskforce deployment.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_clean_water_infrastructure_plan", "Propose a state-backed clean drinking water infrastructure plan in affected districts to prevent future outbreaks.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(10, "Funding and agency jurisdiction disputes delay water pipe laying in remote blocks.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"healthCrisisIgnoredMemory": 3}, weight=0.25)
    ]
))

# 2008-10
ITEMS_2006_2010.append(make_news(
    key="up2008_2008_10_supreme_court_memorial_halt",
    month="2008-10",
    title="Supreme Court Halts Ambedkar Memorial Park Construction",
    desc="The Supreme Court issues a temporary work-halt order on the Ambedkar Memorial Park in Lucknow, pending an audit of environmental clearances and expenditure.",
    tags=['politics', 'economy', 'environment'],
    base_w=1.2, profile="politics",
    reactions=[
        reaction("accept_sc_halt_submit_impact_sheets", "Accept the Supreme Court halt, instruct the law department to submit environmental impact sheets to court immediately.",
                 ['GOVERNMENT'], eff(1, 0, 3, 2),
                 {},
                 risk(18, "Dalit organization cadres hold local protests, claiming the court order is biased.", eff(-1, 0, -2, -2)), 1.15),
        reaction("demand_legislative_audit_of_memorial_spending", "Demand a legislative committee audit the memorial park expenditure, claiming state funds are misused.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "State departments take months to compile spending data, delaying the audit release.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_state_harmony_committee", "Propose a state harmony committee representing all community leaders to discuss grievances peacefully.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing by key members delays the release of the committee's recommendations.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.25)
    ]
))

# 2008-11
ITEMS_2006_2010.append(make_news(
    key="up2008_2008_11_bundelkhand_statehood_protests",
    month="2008-11",
    title="Bundelkhand Statehood Agitations Block Jhansi Rail Lines",
    desc="Protests by Bundelkhand statehood coordination groups block railway tracks in Jhansi, demanding the bifurcation of UP to create a separate Bundelkhand state.",
    tags=['identity', 'politics', 'protest'],
    base_w=1.15, profile="politics",
    reactions=[
        reaction("support_bundelkhand_statehood_resolution", "Support a non-binding assembly resolution in favor of Bundelkhand statehood to address local sentiments.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Central departments reject the resolution as a state political card, stalling bifurcation.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_bundelkhand_special_package", "Demand a special legislative package for Bundelkhand development instead of dividing the state, citing unity.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Local statehood groups continue the rail blockade, calling the package insufficient.", eff(-1, 0, -2, -2)), 1.2),
        reaction("propose_state_harmony_committee", "Propose a state harmony committee representing all community leaders to discuss grievances peacefully.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing by key members delays the release of the committee's recommendations.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.25)
    ]
))

# 2008-12
ITEMS_2006_2010.append(make_news(
    key="up2008_2008_12_pwd_engineer_auraiya_murder",
    month="2008-12",
    title="PWD Engineer Manoj Gupta Murdered in Auraiya",
    desc="PWD Executive Engineer Manoj Gupta is beat to death in his Auraiya home, allegedly by a ruling BSP MLA and his associates for refusing to pay donation.",
    tags=['violence', 'politics', 'corruption', 'crisis'],
    base_w=1.35, profile="security_crisis",
    reactions=[
        reaction("register_fir_against_mla_auraiya", "Order the immediate arrest of the named BSP MLA under the Gangster Act and coordinate a fast-track trial.",
                 ['GOVERNMENT'], eff(2, -2, 3, 3),
                 {},
                 risk(20, "MLA's local caste base stages blockades, accusing the administration of betraying loyalists.", eff(-2, 0, -2, -3)), 1.2),
        reaction("lead_statewide_engineer_solidarity_dharnas", "Lead statewide silent marches of engineers and opposition workers, demanding judicial inquiry into donation books.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 4),
                 {},
                 risk(15, "Security forces use barriers, and some workers are injured, shifting media focus.", eff(-1, 0, -2, -2)), 1.25),
        reaction("propose_legislative_roundtable", "Propose a legislative roundtable with representatives from all parties to draft a consensus policy on the issue.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 2, 2),
                 {},
                 risk(8, "Lack of consensus among members delays the final report, rendering it inactive.", eff(0, 0, -1, -1)), 1.05),
        no_comment(hidden={"massCasualtyIgnoredMemory": 4}, weight=0.1)
    ]
))

# 2009-01
ITEMS_2006_2010.append(make_news(
    key="up2009_2009_01_engineer_murder_protests",
    month="2009-01",
    title="Engineers Association Protests Peak Across Districts",
    desc="The UP state engineers association holds protests in major cities over the Auraiya PWD engineer murder. They demand administrative protection from political demands.",
    tags=['politics', 'protest', 'governance'],
    base_w=1.2, profile="protest",
    reactions=[
        reaction("announce_engineer_security_cell", "Announce the setup of a dedicated police cell to coordinate security for PWD project sites and engineering offices.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Coordination cell reports administrative delays in verifying calls, leaving offices exposed.", eff(-1, 0, -2, -1)), 1.15),
        reaction("demand_cbi_audit_of_pwd_funds", "Demand a CBI investigation into PWD fund allocations, claiming ruling party figures enforce commission cuts.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "State departments take months to compile spending data, delaying the audit release.", eff(0, 0, -2, -1)), 1.25),
        reaction("propose_digitized_audit_portal", "Propose a digitized public audit portal to track all related government transactions and block corruption.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(12, "Technical integration delays keep the portal offline, drawing criticism for slow delivery.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"corruptionIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2009-02
ITEMS_2006_2010.append(make_news(
    key="up2009_2009_02_varun_gandhi_pilibhit_speech",
    month="2009-02",
    title="Varun Gandhi's Pilibhit Speech Triggers National Dispute",
    desc="BJP candidate Varun Gandhi's speech at an election rally in Pilibhit triggers controversy, with media and rival parties alleging communal profiling.",
    tags=['politics', 'identity', 'election'],
    base_w=1.25, profile="politics",
    reactions=[
        reaction("register_fir_under_national_security_act", "Instruct the police to register FIRs under the National Security Act (NSA) and request EC monitor speeches.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(20, "BJP workers launch protest rallies in Pilibhit, leading to police clashes.", eff(-2, 0, -2, -3)), 1.2),
        reaction("condemn_speech_demand_candidate_ban", "Condemn the speech at press conferences and demand the EC ban the candidate from contesting upcoming polls.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(12, "Candidate files a court petition challenging the EC notice, delaying final verdict.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_state_harmony_committee", "Propose a state harmony committee representing all community leaders to discuss grievances peacefully.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing by key members delays the release of the committee's recommendations.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.2)
    ]
))

# 2009-03
ITEMS_2006_2010.append(make_news(
    key="up2009_2009_03_varun_gandhi_pilibhit_arrest",
    month="2009-03",
    title="Varun Gandhi Arrested Under NSA in Pilibhit",
    desc="BJP leader Varun Gandhi surrenders at a Pilibhit court and is arrested under the National Security Act (NSA). High security alerts are declared in sensitive zones.",
    tags=['security', 'politics', 'crisis'],
    base_w=1.3, profile="security_crisis",
    reactions=[
        reaction("deploy_paramilitary_pilibhit_borders", "Deploy paramilitary forces at Pilibhit borders, enforce prohibitory orders, and secure court premises.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "BJP workers clash with police outside jail gates, leading to minor injuries.", eff(-1, 0, -2, -2)), 1.2),
        reaction("condemn_nsa_use_as_political_card", "Expose instances of selective NSA use by the state government and demand the court audit the arrest files.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Local media welcomes the arrest as a law and order check, diluting the critique.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_security_advisory_board", "Propose setting up an independent security advisory board with defense experts to upgrade local safety protocols.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(12, "Implementation of board recommendations is delayed due to funding shortages.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"securityIgnoredMemory": 3}, weight=0.25)
    ]
))

# 2009-04
ITEMS_2006_2010.append(make_news(
    key="up2009_2009_04_parliamentary_polling_phases",
    month="2009-04",
    title="Lok Sabha Polling Commences in Uttar Pradesh",
    desc="Voters cast ballots in the first phases of the general elections. UP remains the critical battlefield for regional and national coalitions.",
    tags=['election', 'politics'],
    base_w=1.2, profile="election",
    reactions=[
        reaction("promise_farm_subsidy_payouts", "Promise to accelerate cooperative sugar mill payouts and release rural development grants.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Model code of conduct rules delay the release of grants, causing candidate frustration.", eff(-1, 0, -2, -2)), 1.15),
        reaction("expose_incumbent_failures_rural_districts", "Campaign on agricultural distress, highlighting Bundelkhand droughts and unpaid sugarcane crop bills.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(12, "Rival party candidates campaign on regional pride cards, splitting votes.", eff(-1, 0, -2, -1)), 1.2),
        reaction("propose_legislative_roundtable", "Propose a legislative roundtable with representatives from all parties to draft a consensus policy on the issue.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 2, 2),
                 {},
                 risk(8, "Lack of consensus among members delays the final report, rendering it inactive.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

# 2009-05
ITEMS_2006_2010.append(make_news(
    key="up2009_2009_05_general_election_results_congress",
    month="2009-05",
    title="UP General Election Results: Congress Makes Major Comeback",
    desc="General Election results show Congress winning 21 seats in UP, SP securing 23, BSP winning 20, and BJP winning 10. Analysts trace a major shift in urban wards.",
    tags=['election', 'politics', 'good_news'],
    base_w=1.25, profile="election",
    reactions=[
        reaction("cooperate_with_new_central_ministries", "Instruct state ministries to coordinate with the new central cabinet to secure infrastructure grants.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Central departments delay releasing packages, citing state execution audits.", eff(-1, 0, -2, -2)), 1.2),
        reaction("celebrate_gains_reorganise_urban_ward", "Celebrate the urban gains as a mandate for developmental politics and reorganize the city executive units.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(12, "Internal bickerings over local body candidates weaken district unit focus.", eff(-1, 0, -2, -1)), 1.2),
        reaction("propose_state_harmony_committee", "Propose a state harmony committee representing all community leaders to discuss grievances peacefully.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing by key members delays the release of the committee's recommendations.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2009-06
ITEMS_2006_2010.append(make_news(
    key="up2009_2009_06_ Lucknow_parks_statues_speedup",
    month="2009-06",
    title="UP Government Speeds Up Park and Statue Construction",
    desc="CM Mayawati directs departments to speed up construction of the Kanshiram Memorial and Ambedkar parks in Lucknow, deploying extra shifts.",
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

# 2009-07
ITEMS_2006_2010.append(make_news(
    key="up2009_2009_07_rita_joshi_house_arson",
    month="2009-07",
    title="Congress Chief Rita Joshi's House Set on Fire; Protests",
    desc="The Lucknow home of UP Congress chief Rita Bahuguna Joshi is set on fire, allegedly by ruling party cadres following her controversial remarks about CM Mayawati.",
    tags=['violence', 'politics', 'crisis', 'law_order'],
    base_w=1.3, profile="security_crisis",
    reactions=[
        reaction("order_police_probe_arson_suspects", "Order an immediate police inquiry into the arson and suspend local patrol officers for security gaps.",
                 ['GOVERNMENT'], eff(1, -1, 3, 2),
                 {},
                 risk(20, "Evidence of local ruling party cadre involvement is leaked to media, causing outrage.", eff(-2, 0, -3, -4)), 1.2),
        reaction("lead_statewide_arson_protest_marches", "Lead statewide protest marches carrying blackened banners, demanding independent CBI probe into political arson.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 4),
                 {},
                 risk(15, "Marchers clash with police barricades, leading to minor injuries.", eff(-1, 0, -2, -2)), 1.25),
        reaction("propose_state_harmony_committee", "Propose a state harmony committee representing all community leaders to discuss grievances peacefully.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing by key members delays the release of the committee's recommendations.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"massCasualtyIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2009-08
ITEMS_2006_2010.append(make_news(
    key="up2009_2009_08_bundelkhand_drought_relief",
    month="2009-08",
    title="Bundelkhand Faces Sixth Consecutive Drought; Crop Failures Rise",
    desc="Severe drought hit Bundelkhand districts for the sixth consecutive season. Standing soybean and pulses crops are damaged, spurring local body calls for help.",
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

# 2009-09
ITEMS_2006_2010.append(make_news(
    key="up2009_2009_09_sugarcane_sap_price_dispute",
    month="2009-09",
    title="Farmers Protest Sugarcane State Advisory Price Hike",
    desc="Sugarcane growers stage protests in Muzaffarnagar and Meerut, claiming the recent state advisory price hike is insufficient to cover fertilizer costs.",
    tags=['rural', 'agriculture', 'protest'],
    base_w=1.15, profile="land_rights",
    reactions=[
        reaction("announce_additional_transport_subsidy", "Announce an additional state transport subsidy of ₹10 per quintal for direct sugarcane deliveries.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Private mills halt crushing operations, claiming the subsidy increases overhead costs.", eff(-1, 0, -2, -2)), 1.25),
        reaction("join_sugar_belt_highway_blockade", "Address protesting farmers at the Muzaffarnagar blockade and demand immediate railway rakes for export.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(14, "Highway blockade delays commercial freight transport, drawing complaints from logistics groups.", eff(-1, 0, -1, -2)), 1.2),
        reaction("propose_tripartite_mediation_council", "Propose a tripartite mediation council representing labor unions, industry leaders, and state officials.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Radical sections of the union boycott the mediation, continuing localized protests.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 3}, weight=0.2)
    ]
))

# 2009-10
ITEMS_2006_2010.append(make_news(
    key="up2009_2009_10_supreme_court_memorial_audit",
    month="2009-10",
    title="Supreme Court Orders Financial Audit of Memorial Spending",
    desc="The Supreme Court orders the Comptroller and Auditor General (CAG) to audit all state funds spent on construction of statues and memorial parks in Lucknow.",
    tags=['corruption', 'scam', 'politics'],
    base_w=1.2, profile="corruption",
    reactions=[
        reaction("comply_submit_memorial_expenditure_sheets", "Comply with the court order, submit all project invoices, and defend the spending in press statements.",
                 ['GOVERNMENT'], eff(1, -2, 3, 2),
                 {},
                 risk(18, "Audit documents reveal inflated stone rates, generating critical media coverage.", eff(-1, 0, -2, -3)), 1.2),
        reaction("demand_assembly_dossier_on_stone_rates", "Demand a legislative committee audit the memorial park expenditure, claiming state funds are misused.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 3),
                 {},
                 risk(12, "State departments take months to compile spending data, delaying the audit release.", eff(0, 0, -2, -1)), 1.2),
        reaction("propose_digitized_audit_portal", "Propose a digitized public audit portal to track all related government transactions and block corruption.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(12, "Technical integration delays keep the portal offline, drawing criticism for slow delivery.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"corruptionIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2009-11
ITEMS_2006_2010.append(make_news(
    key="up2009_2009_11_sugarcane_farmers_dharna_lucknow",
    month="2009-11",
    title="Sugarcane Farmers Hold Massive Dharna in Lucknow",
    desc="Thousands of sugarcane farmers from Western UP divisions hold a dharna near the Vidhan Sabha in Lucknow, demanding payment of previous year's arrears.",
    tags=['rural', 'agriculture', 'protest'],
    base_w=1.2, profile="land_rights",
    reactions=[
        reaction("mandate_private_mills_interest_payments", "Release emergency cash reserves to purchase centers to pay farmers immediately and clear the backlog.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Cash distribution is skewed toward politically connected large growers, sparking local scuffles.", eff(-1, 0, -2, -2)), 1.25),
        reaction("lead_farmers_march_secretariat", "Lead a protest march of affected farmers to the district collectorate, demanding written payment timelines.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Marchers clash with police barricades, leading to tear gas use and negative media.", eff(-1, 0, -2, -2)), 1.2),
        reaction("propose_automated_payment_link", "Propose an automated escrow system linking mill sales directly to farmers' bank accounts for immediate clearances.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 3),
                 {},
                 risk(10, "Technical integration with rural banks is delayed, leaving payments slow.", eff(0, 0, -2, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 3}, weight=0.2)
    ]
))

# 2009-12
ITEMS_2006_2010.append(make_news(
    key="up2009_2009_12_swine_flu_vaccine_rollout",
    month="2009-12",
    title="Swine Flu Vaccine Rollout Drive Launched in Major Cities",
    desc="To check winter swine flu cases, the health department launches a vaccine rollout drive across major hospitals in Lucknow, Kanpur, and Agra.",
    tags=['health', 'governance', 'good_news'],
    base_w=1.05, profile="governance",
    reactions=[
        reaction("deploy_vaccine_booths_hospitals", "Deploy dedicated vaccine distribution booths in all district hospitals, offering free shots to high-risk categories.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Vaccine cold storage units report electricity failures in rural blocks, damaging stocks.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_medical_infrastructure_audit", "Demand an audit of district hospital facilities, claiming that isolation beds are insufficient to check spread.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(10, "State health department rejects central interference, stalling taskforce deployment.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_clean_water_infrastructure_plan", "Propose a state-backed clean drinking water infrastructure plan in affected districts to prevent future outbreaks.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 3),
                 {},
                 risk(10, "Funding and agency jurisdiction disputes delay water pipe laying in remote blocks.", eff(0, 0, -2, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2010-01
ITEMS_2006_2010.append(make_news(
    key="up2010_2010_01_memorials_fire_incident",
    month="2010-01",
    title="Fire at Lucknow Dalit Memorial Park Triggers Tension",
    desc="A fire breakout at a wooden display shed in Kanshiram Smriti Upvan, Lucknow, triggers alerts. BSP cadres allege sabotage, while police point to electrical short circuit.",
    tags=['identity', 'security', 'politics'],
    base_w=1.15, profile="security_crisis",
    reactions=[
        reaction("upgrade_memorial_security_guards", "Upgrade the security detail at all major memorial parks in Lucknow, deploying extra armed guards.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(14, "Security check queues at court entrances trigger lawyer protests over delays.", eff(-1, 0, -1, -2)), 1.2),
        reaction("condemn_communal_sabotage_claims", "Hold press conferences condemning the sabotage claims, demanding the police release forensic logs of short-circuit analysis.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "Dalit organization cadres protest the comments, claiming opposition is trying to downplay threats.", eff(-1, 0, -2, -2)), 1.2),
        reaction("propose_state_harmony_committee", "Propose a state harmony committee representing all community leaders to discuss grievances peacefully.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing by key members delays the release of the committee's recommendations.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"identityIssueMissed": 2}, weight=0.25)
    ]
))

# 2010-02
ITEMS_2006_2010.append(make_news(
    key="up2010_2010_02_legislative_council_poll_violence",
    month="2010-02",
    title="Legislative Council Polls Witness Clashes in Central UP",
    desc="Voting for the UP legislative council seats is marred by clashes between ruling party and opposition cadres in Pratapgarh and Sultanpur, leading to minor injuries.",
    tags=['election', 'politics', 'law_order'],
    base_w=1.2, profile="election",
    reactions=[
        reaction("suspend_implicated_cops_booths", "Order the immediate transfer of local station house officers in clash areas and request EC audits.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Transferred officers file CAT appeals, claiming state political pressure.", eff(-1, 0, -2, -1)), 1.2),
        reaction("lead_march_against_poll_rigging", "Lead a march of opposition candidates to the state election commission, demanding detailed re-polls.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "EC rejects the petition, stating that violence logs are below thresholds.", eff(-1, 0, -2, -2)), 1.25),
        reaction("propose_legislative_roundtable", "Propose a legislative roundtable with representatives from all parties to draft a consensus policy on the issue.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 2, 2),
                 {},
                 risk(8, "Lack of consensus among members delays the final report, rendering it inactive.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.35)
    ]
))

# 2010-03
ITEMS_2006_2010.append(make_news(
    key="up2010_2010_03_pratapgarh_ashram_stampede",
    month="2010-03",
    title="Pratapgarh Ashram Stampede Kills 63 People",
    desc="A stampede at the Kripalu Maharaj Ashram in Pratapgarh during a free distribution event leads to the deaths of 63 people, mostly women and children.",
    tags=['disaster', 'law_order', 'crisis'],
    base_w=1.35, profile="security_crisis",
    reactions=[
        reaction("order_magisterial_probe_ashram_aid", "Order a fast-track magisterial inquiry, register a negligence case, and allocate state aid for victim families.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Inquiry uncovers that local police failed to manage the crowd despite event requests, drawing media fire.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_strict_guidelines_religious_assemblies", "Demand the government enforce strict safety and crowd management guidelines for all private religious events.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(12, "Religious groups organize counter-protests, claiming state interference in faith.", eff(-1, 0, -1, -2)), 1.25),
        reaction("propose_security_advisory_board", "Propose setting up an independent security advisory board with defense experts to upgrade local safety protocols.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(12, "Implementation of board recommendations is delayed due to funding shortages.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"massCasualtyIgnoredMemory": 5, "securityIgnoredMemory": 4}, weight=0.05)
    ]
))

# 2010-04
ITEMS_2006_2010.append(make_news(
    key="up2010_2010_04_yamuna_expressway_tappal_protests",
    month="2010-04",
    title="Yamuna Expressway Tappal Land Acquisition Protests Erupt",
    desc="Protests by farmers against land acquisition rates for the Yamuna Expressway project escalate in Tappal, Aligarh. Farmers block surveyor entries.",
    tags=['land', 'protest', 'infrastructure'],
    base_w=1.25, profile="land_rights",
    reactions=[
        reaction("negotiate_higher_compensation_expressway", "Negotiate higher compensation rates with farmer committee representatives and announce job cards for local youth.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Expressway builder groups threaten project halts, citing increased capital costs.", eff(-1, 0, -2, -2)), 1.2),
        reaction("join_tappal_farmer_dharnas", "Join the farmer dharnas in Tappal, demanding a complete review of land acquisition rates and environmental reports.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 4, 4),
                 {},
                 risk(15, "Clashes between protesters and site security lead to minor injuries, drawing critical press.", eff(-1, 0, -1, -2)), 1.25),
        reaction("propose_tripartite_mediation_council", "Propose a tripartite mediation council representing labor unions, industry leaders, and state officials.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Radical sections of the union boycott the mediation, continuing localized protests.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"ruralUnrestIgnoredMemory": 3}, weight=0.2)
    ]
))

# 2010-05
ITEMS_2006_2010.append(make_news(
    key="up2010_2010_05_tappal_police_clashes",
    month="2010-05",
    title="Violent Clashes in Tappal Between Farmers and Police",
    desc="Attempts by the administration to clear the Tappal protests lead to violent clashes between farmers and police forces. Several casualties are reported.",
    tags=['violence', 'protest', 'crisis', 'law_order'],
    base_w=1.35, profile="security_crisis",
    reactions=[
        reaction("suspend_aligarh_cops_compensation_hike", "Suspend Aligarh police chiefs for excessive force, order a judicial inquiry, and announce higher land payouts.",
                 ['GOVERNMENT'], eff(1, -1, 3, 2),
                 {},
                 risk(22, "Farmer unions reject the judicial probe, demanding complete withdrawal of land notifications.", eff(-2, 0, -3, -4)), 1.2),
        reaction("lead_statewide_farmer_solidarity_marches", "Lead statewide protest marches carrying blackened banners, demanding independent CBI probe into political arson.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 4),
                 {},
                 risk(15, "Marchers clash with police barricades, leading to minor injuries.", eff(-1, 0, -2, -2)), 1.25),
        reaction("propose_tripartite_mediation_council", "Propose a tripartite mediation council representing labor unions, industry leaders, and state officials.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(10, "Radical sections of the union boycott the mediation, continuing localized protests.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"massCasualtyIgnoredMemory": 4, "ruralUnrestIgnoredMemory": 3}, weight=0.15)
    ]
))

# 2010-06
ITEMS_2006_2010.append(make_news(
    key="up2010_2010_06_farmer_rehabilitation_policy",
    month="2010-06",
    title="UP Government Announces New Farmer Rehabilitation Policy",
    desc="To resolve Yamuna Expressway protests, the UP cabinet announces a new farmer rehabilitation policy, offering annuity payments and free commercial plots.",
    tags=['rural', 'land', 'good_news'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("advertise_policy_as_agrarian_victory", "Advertise the rehabilitation policy as a model for farmer-friendly industrial growth and start direct payments.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(18, "Acquisition boards report budget deficits in financing annuities, delaying payouts.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_statutory_status_rehabilitation", "Demand that the rehabilitation policy be passed as a statutory act in the assembly to prevent future revisions.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(12, "Assembly speaker rejects the resolution, leading to walkouts.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_rural_stabilization_policy", "Propose a bipartisan rural development and price stabilization task force to draft long-term support policies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Lack of immediate budget allocation delays the implementation of the task force proposals.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"ruralAngerMemory": 2}, weight=0.25)
    ]
))

# 2010-07
ITEMS_2006_2010.append(make_news(
    key="up2010_2010_07_heavy_rains_waterlogging",
    month="2010-07",
    title="Heavy Rains Cause Severe Waterlogging in Lucknow and Kanpur",
    desc="Torrential monsoon rains submerge civic roads in Lucknow and Kanpur. Commuters report traffic gridlocks, and health boards warn of dengue risks.",
    tags=['urban', 'disaster', 'crisis'],
    base_w=1.1, profile="health_crisis",
    reactions=[
        reaction("deploy_dewatering_pumps_clean_drives", "Deploy emergency dewatering pumps to low-lying wards, clear blocked storm drains, and launch sanitation campaigns.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Drains block again during subsequent showers, drawing resident complaints.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_expedited_sewer_reconstruction", "Demand the municipal corporations expedite the sewerage reconstruction phases, blaming contractor cartels.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(10, "Construction works are delayed by municipal budget limits, prolonging traffic bottlenecks.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_infrastructure_oversight_committee", "Propose a joint civic-expert oversight committee to monitor construction quality and manage traffic impact.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Inter-departmental coordination issues delay committee meetings, slowing down resolution of issues.", eff(0, 0, -1, -1)), 1.05),
        no_comment(hidden={"disasterIgnoredMemory": 3}, weight=0.25)
    ]
))

# 2010-08
ITEMS_2006_2010.append(make_news(
    key="up2010_2010_08_bareilly_communal_clashes",
    month="2010-08",
    title="Communal Clashes in Bareilly Trigger Indefinite Curfew",
    desc="Clashes between two groups during a religious procession in Bareilly lead to arson and curfew declarations. The state deploys rapid action force teams.",
    tags=['identity', 'violence', 'crisis', 'law_order'],
    base_w=1.25, profile="security_crisis",
    reactions=[
        reaction("enforce_curfew_unbiased_arrests", "Enforce the curfew strictly, deploy central rapid action forces, and order unbiased arrests of rioters.",
                 ['GOVERNMENT'], eff(1, -1, 3, 2),
                 {},
                 risk(20, "Local community groups accuse the police of partisan behavior during searches.", eff(-2, 0, -3, -4)), 1.2),
        reaction("organise_bareilly_harmony_walks", "Organise local inter-community harmony walks at curfew boundaries and demand independent judicial audit.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(12, "Radical groups organize counter-rallies, raising communal temperatures.", eff(-1, 0, -2, -2)), 1.2),
        reaction("propose_state_harmony_committee", "Propose a state harmony committee representing all community leaders to discuss grievances peacefully.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing by key members delays the release of the committee's recommendations.", eff(0, 0, -1, -1)), 1.1),
        no_comment(hidden={"massCasualtyIgnoredMemory": 3, "identityIssueMissed": 2}, weight=0.2)
    ]
))

# 2010-09
ITEMS_2006_2010.append(make_news(
    key="up2010_2010_09_ayodhya_title_suit_verdict",
    month="2010-09",
    title="Historic Ayodhya Verdict Delivered by Allahabad High Court",
    desc="The Allahabad High Court delivers its historic Ayodhya title suit verdict, dividing the disputed land into three equal parts. Massive security is deployed statewide.",
    tags=['security', 'politics', 'identity', 'crisis'],
    base_w=1.45, profile="security_crisis",
    reactions=[
        reaction("deploy_extra_paramilitary_harmony_vigils", "Deploy extensive paramilitary units in mixed wards, prohibit victory processions, and coordinate local harmony committees.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(18, "Prohibitory orders restrict peaceful assemblies, drawing minor complaints from civic groups.", eff(-1, 0, -1, -2)), 1.25),
        reaction("appeal_peace_respect_judiciary", "Issue joint public appeals to respect the judicial verdict and maintain communal harmony across all districts.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 4, 4),
                 {},
                 risk(8, "Voters view the appeal as a standard response, requesting active police patrols.", eff(0, 0, -1, -1)), 1.15),
        reaction("propose_state_harmony_committee", "Propose a state harmony committee representing all community leaders to discuss grievances peacefully.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 2),
                 {},
                 risk(10, "Political posturing by key members delays the release of the committee's recommendations.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"securityIgnoredMemory": 3, "identityIssueMissed": 3}, weight=0.1)
    ]
))

# 2010-10
ITEMS_2006_2010.append(make_news(
    key="up2010_2010_10_bundelkhand_package_demand",
    month="2010-10",
    title="CM Mayawati Demands Special Bundelkhand Package from PM",
    desc="Chief Minister Mayawati meets the Prime Minister and demands a special central development package for drought-prone Bundelkhand, citing federal sharing commitments.",
    tags=['politics', 'rural', 'governance'],
    base_w=1.15, profile="governance",
    reactions=[
        reaction("advertise_package_demand_victory", "Advertise the package demand as a major step to address regional neglect and pressure the central ministries.",
                 ['GOVERNMENT'], eff(2, 0, 3, 3),
                 {},
                 risk(15, "Central ministries delay package release, requesting state execution audits.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_state_package_first", "Demand the state government release matching development grants from its own treasury first, instead of blaming the center.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 3),
                 {},
                 risk(12, "State cabinet claims budget limits, leaving the demand unfulfilled.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_rural_stabilization_policy", "Propose a bipartisan rural development and price stabilization task force to draft long-term support policies.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(10, "Lack of immediate budget allocation delays the implementation of the task force proposals.", eff(0, 0, -1, -1)), 1.1),
        no_comment(weight=0.3)
    ]
))

# 2010-11
ITEMS_2006_2010.append(make_news(
    key="up2010_2010_11_memorials_cag_audit_report",
    month="2010-11",
    title="CAG Report Details Financial Discrepancies in Lucknow Memorials",
    desc="A CAG audit report tabled in the assembly details financial discrepancies, claiming that the state spent excess amounts on stone carvings and statues in Lucknow memorials.",
    tags=['corruption', 'scam', 'politics', 'crisis'],
    base_w=1.3, profile="corruption",
    reactions=[
        reaction("comply_cag_audit_judicial_probe", "Accept the CAG report recommendations, refer the discrepancies to a judicial commission, and promise rectifications.",
                 ['GOVERNMENT'], eff(2, -2, 3, 3),
                 {},
                 risk(18, "Judicial commission is delayed by file collections, drawing critical media.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_fir_against_cag_implicated_mlas", "Demand immediate police FIRs and asset freezing of senior department heads and builders named in the CAG log.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(3, 0, 5, 4),
                 {},
                 risk(15, "Legal processes are slow, and political divisions prevent immediate asset recoveries.", eff(0, 0, -2, -2)), 1.25),
        reaction("propose_digitized_audit_portal", "Propose a digitized public audit portal to track all related government transactions and block corruption.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(2, -1, 3, 2),
                 {},
                 risk(12, "Technical integration delays keep the portal offline, drawing criticism for slow delivery.", eff(0, 0, -1, -1)), 1.15),
        no_comment(hidden={"corruptionIgnoredMemory": 4}, weight=0.15)
    ]
))

# 2010-12
ITEMS_2006_2010.append(make_news(
    key="up2010_2010_12_winter_fog_rail_delays",
    month="2010-12",
    title="Severe Winter Fog Disrupts Rail and Road Transport in UP",
    desc="Thick winter fog covers North India, causing severe delays of over five hours in passenger train and bus services across Lucknow, Kanpur, and Varanasi hubs.",
    tags=['disaster', 'transport', 'infrastructure'],
    base_w=1.1, profile="health_crisis",
    reactions=[
        reaction("set_up_passenger_fog_shelters", "Set up heated passenger shelters and emergency food stalls at major municipal rail and bus terminals.",
                 ['GOVERNMENT'], eff(2, 0, 3, 4),
                 {},
                 risk(15, "Shelters report water supply breakdowns due to pipeline freezing, drawing complaints.", eff(-1, 0, -2, -2)), 1.2),
        reaction("demand_railway_safety_instrument_upgrades", "Demand the central railways install modern fog-safe signalling instruments at all major UP stations.",
                 ['OPPOSITION', 'THIRD_PARTY'], eff(2, 0, 3, 4),
                 {},
                 risk(10, "Railway boards cite supply delays, leaving schedules disrupted for the season.", eff(0, 0, -2, -1)), 1.15),
        reaction("propose_infrastructure_oversight_committee", "Propose a joint civic-expert oversight committee to monitor construction quality and manage traffic impact.",
                 ['GOVERNMENT', 'OPPOSITION', 'THIRD_PARTY'], eff(1, 0, 3, 2),
                 {},
                 risk(8, "Inter-departmental coordination issues delay committee meetings, slowing down resolution of issues.", eff(0, 0, -1, -1)), 1.05),
        no_comment(weight=0.3)
    ]
))

