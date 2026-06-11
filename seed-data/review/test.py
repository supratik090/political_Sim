
import json, copy, re

with open('west_bengal_2000_monthly_issues_review.json') as f:
    data = json.load(f)

# Helper: short noun phrase from title for embedding in text
def noun(title):
    # strip trailing s from "complaints", "allegations" etc for concise embed
    t = title.strip().rstrip('.')
    return t[0].lower() + t[1:]

def first_word(title):
    return title.split()[0].lower()

# =============================================================================
# Per-item bespoke option texts for ALL 120 items
# Format: issueKey -> [slot0_text, slot1_text, slot2_text, slot3_text]
# slot0 = decisive/clean, slot1 = spend/visible, slot2 = stall/manage, slot3 = shield/corrupt
# For GOV: strict_action, quick_relief, message_and_delay, protect_machinery
# For OPP: constructive_service, aggressive_agitation, verify_and_attack, funds_first_compromise
# =============================================================================

ITEM_TEXTS = {
# ==================== GOVERNMENT ====================
"gov_teacher_recruitment_irregularity": [
    "Suspend the implicated officials, publish the full merit list online, and open a fresh review with outside examiners.",
    "Deploy emergency verification camps in all districts to fast-track clean appointments and show visible progress.",
    "Constitute a three-member inquiry panel, freeze pending appointments, and await its report before acting.",
    "Defend the recruitment process as rule-bound and call the allegations a pre-election smear campaign.",
],
"gov_flood_relief_leakage": [
    "Audit every relief packet disbursed, name the middlemen publicly, and hand the cases to the district magistrate.",
    "Dispatch a fresh direct supply through block officers, bypassing the contractors accused of diversion.",
    "Form a relief monitoring committee, publish a helpline number, and allow complaints for 30 days.",
    "Attribute leakage reports to opposition mischief and defend the existing distribution mechanism publicly.",
],
"gov_local_leader_extortion": [
    "Suspend the accused district leader immediately and issue a written public statement on zero tolerance.",
    "Quietly compensate the affected businesses and redeploy the leader to a non-contact administrative post.",
    "Ask the district president to investigate internally; suspend public comment pending findings.",
    "Stand by the accused, call the charges politically motivated, and rally local cadre around him.",
],
"gov_hospital_medicine_shortage": [
    "Order an immediate supply audit, publish the shortfall data, and hold the procurement officer accountable.",
    "Release emergency funds for medicines and equipment within 48 hours with public delivery tracking.",
    "Announce a health task force and schedule a ministerial district visit within two weeks.",
    "Attribute the shortage to central supply delays and deny any local procurement mismanagement.",
],
"gov_ration_shop_diversion": [
    "Freeze the dealer's licence, publish the diverted grain quantity, and open a direct-beneficiary helpdesk.",
    "Dispatch double the usual stock before the next festival and run door-to-door beneficiary verification.",
    "Issue a formal show-cause notice to the dealer and set a 30-day compliance deadline.",
    "Dismiss reports as exaggerated and point to overall statewide distribution figures as proof of health.",
],
"gov_primary_school_absenteeism": [
    "Launch surprise cluster inspections, dock absent teachers' pay, and publish block-level attendance data.",
    "Hire community attendance monitors for each school and pre-distribute a term's mid-day meal supply.",
    "Direct district inspectors to file monthly reports and convene a departmental review next quarter.",
    "Blame the opposition-aligned teachers' union for inflating absence figures ahead of elections.",
],
"gov_rural_road_contract_delay": [
    "Cancel the defaulting contractor's order, invoke penalty clauses in the agreement, and re-tender within 30 days.",
    "Divert emergency public works funds to restart visibly stalled construction before the monsoon.",
    "Call a joint site meeting of engineers and panchayat heads and issue a public revised timeline.",
    "Attribute delays to soil-testing disputes and blame central-supply bottlenecks beyond state control.",
],
"gov_electricity_load_shedding": [
    "Order emergency procurement of coal, publish a daily load schedule, and hold the utility board accountable.",
    "Announce an immediate ₹50 crore fund to repair the five worst-affected substations with a 14-day deadline.",
    "Convene an emergency session of the state electricity board and promise a schedule within one week.",
    "Attribute load-shedding to a national coal shortage and say the state is managing better than most.",
],
"gov_police_excess_complaint": [
    "Order a magisterial probe, suspend the identified officer, and personally meet the families of the injured.",
    "Provide immediate medical and legal aid to the injured and deploy additional officers for community reassurance.",
    "Ask the superintendent of police to submit a departmental report within 10 days.",
    "Defend police conduct as restrained given the provocation and challenge the opposition to prove otherwise.",
],
"gov_tea_garden_wage_arrears": [
    "Give garden managements a 15-day ultimatum to clear arrears or face licence suspension; publish the list.",
    "Release emergency welfare funds directly to workers through cooperative banks to tide them over.",
    "Convene a tripartite labour meeting between workers, garden owners, and the labour commissioner.",
    "Call it a private labour dispute and urge both sides to negotiate without state interference.",
],
"gov_college_seat_allocation": [
    "Publish complete seat allocation data online and launch a live grievance portal with a three-day resolution window.",
    "Add 200 seats through an emergency order and fast-track verification at each affected institution.",
    "Constitute a student-faculty review panel to investigate the allocation and report within three weeks.",
    "Say allocations strictly followed regulations and accuse the opposition of fomenting campus agitation.",
],
"gov_municipal_garbage_backlog": [
    "Deploy dedicated ward-level sanitation teams, launch a complaint line, and publish daily clearance numbers.",
    "Hire private contractors for emergency pre-monsoon clearance and pay overtime to existing sanitation staff.",
    "Issue a civic advisory and convene an emergency municipal council session on the backlog.",
    "Attribute the backlog to an unusual waste volume spike and assure normal service within days.",
],
"gov_industrial_land_protest": [
    "Freeze acquisition proceedings, publish compensation terms publicly, and invite farmer review panels.",
    "Announce enhanced compensation rates and open door-to-door documentation camps immediately.",
    "Appoint a revenue officer to visit affected blocks and submit a report within 21 days.",
    "Say the acquisition is legally compliant and attribute protests to outside political agitators.",
],
"gov_fisherfolk_harbor_damage": [
    "Commission emergency harbour repairs, name the responsible project engineer, and report progress weekly.",
    "Transfer emergency disaster funds directly to the harbour board and begin visible repair within days.",
    "Constitute a coastal infrastructure review panel to submit repair recommendations within 30 days.",
    "Point to the Centre's delayed ports-department funds as the real cause of the unfinished repairs.",
],
"gov_anganwadi_payment_delay": [
    "Release the full pending honorarium within seven days and install a digital payment tracker for future cycles.",
    "Announce an emergency advance from state welfare funds to anganwadi workers pending central disbursement.",
    "Ask the women and child development commissioner to audit the backlog and release a payment schedule.",
    "Call the delay a temporary cash-flow issue in the central grant cycle and say it will self-correct.",
],
"gov_minority_scholarship_delay": [
    "Personally call the scholarship directorate to account, name delayed cases, and authorise state-bridge funds.",
    "Release an advance tranche from state funds immediately to bridge the central payment gap.",
    "Ask the minority welfare department to submit a disbursement schedule and prevent further delay.",
    "Attribute the delay to mandatory central database verification rules and deny any administrative neglect.",
],
"gov_tribal_land_record_error": [
    "Dispatch survey teams to correct records in situ, publish rectified claims district-wise, and accept legal aid requests.",
    "Open emergency record-correction camps in all affected blocks with extra revenue staff and a fast deadline.",
    "Appoint a revenue sub-divisional officer to review flagged records and report within 45 days.",
    "Say records follow established survey protocols and attribute protests to miscommunication by intermediaries.",
],
"gov_panchayat_audit_objection": [
    "Publish the audit objections, seek recovery from named panchayat heads, and refer the worst cases to vigilance.",
    "Release a special compliance grant to allow panchayats to regularise pending expenditure quickly.",
    "Form an audit response committee to prepare panchayat replies within the statutory deadline.",
    "Describe audit notes as routine procedural observations and defend local spending as within norms.",
],
"gov_bus_fare_hike_backlash": [
    "Direct the transport regulator to roll back the hike, and tie future fare revisions to a transparent formula.",
    "Announce a state fuel-subsidy scheme for operators to absorb the hike without passing it to commuters.",
    "Set up a fare review committee with commuter representation to report within three weeks.",
    "Say the hike reflects real fuel costs and urge commuters to accept the pricing reality.",
],
"gov_rice_procurement_delay": [
    "Open additional procurement centres, penalise identified middlemen by name, and set a payment deadline.",
    "Divert state buffer stocks to affected districts immediately and open emergency fair-price procurement counters.",
    "Convene an emergency agriculture board meeting and announce a procurement resolution timeline.",
    "Attribute delays to central FCI bottlenecks and say the state acted within its jurisdictional powers.",
],
"gov_teacher_transfer_racket": [
    "Suspend the implicated transfer brokers, publish all transfer orders with written justification, and launch an STF probe.",
    "Immediately implement a digital transfer portal that removes offline intermediaries entirely.",
    "Constitute a three-member committee to review the transfer process and propose reforms in 60 days.",
    "Call the brokerage allegations fabricated and defend the existing transfer protocol as transparent.",
],
"gov_health_subcentre_locked": [
    "Order surprise inspections statewide, dock pay of absent staff, and publish attendance data weekly.",
    "Deploy mobile health units to cover locked sub-centres while a rapid staff posting drive fills vacancies.",
    "Ask district CMOs to file weekly attendance reports and schedule a review in 30 days.",
    "Attribute locked centres to staff shortages caused by central health cadre rules, not local management.",
],
"gov_bridge_safety_warning": [
    "Close the bridge immediately, commission the repair with a named contractor, and give a 21-day completion deadline.",
    "Release emergency infrastructure funds to fast-track repair and provide an alternative ferry service same week.",
    "Ask the PWD to inspect and file a structural report; defer closure until the report is in hand.",
    "Say the warnings are precautionary and that the bridge has been in regular use without structural incident.",
],
"gov_fertilizer_shortage": [
    "Order emergency fertilizer procurement from IFFCO, name black-market dealers in the FIR, and reopen depots.",
    "Release state emergency agricultural funds to stock cooperative shops before the sowing deadline.",
    "Convene an emergency agriculture board meeting to find alternate supply routes within the week.",
    "Attribute the shortage to a national production shortfall and say the state is managing within its allocation.",
],
"gov_urban_water_contamination": [
    "Shut the contaminated pipeline section, test all ward water sources, and publish results within 48 hours.",
    "Distribute bottled water through municipal vehicles immediately and deploy tankers to the affected ward.",
    "Issue a health advisory, ask the water board to file an incident report, and await results before acting.",
    "Call the reports exaggerated and say one section of pipeline damage does not indicate systemic contamination.",
],
"gov_college_teacher_strike": [
    "Convene an emergency government-union meeting, release half the arrears immediately, and commit to a payment date.",
    "Pay one month's arrears upfront as a gesture of good faith and announce a task force on service rules.",
    "Form a bipartite committee with union and education department to resolve service rule disputes.",
    "Describe the strike as illegal during exams, invoke essential services rules, and call for return to work.",
],
"gov_cyclone_shelter_shortage": [
    "Accelerate incomplete shelter construction with emergency funds, name contractors in default, and set a deadline.",
    "Deploy mobile cyclone shelters and pre-position relief material at temporary sites before storm season.",
    "Commission an inspection report from the disaster management authority within 15 days.",
    "Say the shelters under construction meet norms and describe concerns as premature alarmism.",
],
"gov_women_safety_march": [
    "Order enhanced police patrols on all cited routes, fast-track pending harassment cases, and meet march organisers.",
    "Announce an emergency safe-transport scheme with 50 new escort buses on high-risk routes immediately.",
    "Set up a women's safety review committee and schedule a ministerial interaction with march leaders.",
    "Describe the march demands as already addressed by existing police protocols and criticise disruptive tactics.",
],
"gov_small_industry_closure": [
    "Announce a targeted credit guarantee scheme, waive penalty interest, and open factory-level revival camps.",
    "Release ₹200 crore in emergency working capital loans through the state industrial development bank.",
    "Convene a MSME task force with chamber representatives to draft a support policy within 30 days.",
    "Say closures reflect national credit tightening and insist state policy is supportive of small industry.",
],
"gov_festival_security_plan": [
    "Publish the full security plan, hold a joint consultation with festival organisers, and accept verified amendments.",
    "Deploy extra forces and simultaneously fund community volunteer marshals to bridge any access restrictions.",
    "Ask the district collector to revise the plan in consultation with all community groups and reissue.",
    "Defend police restrictions as essential and accuse critics of prioritising politics over public safety.",
],
"gov_river_embankment_breach": [
    "Deploy emergency repair teams to the three weakest points, publish a repair log daily, and pre-position relief.",
    "Release disaster-preparedness funds immediately for embankment patching before monsoon peaks.",
    "Ask the irrigation department to inspect and rank embankments by risk and submit a repair order list.",
    "Say embankments were maintained per schedule and attribute concerns to seasonal pre-monsoon anxiety.",
],
"gov_youth_job_fair_quality": [
    "Engage NASSCOM and large local employers for the next fair, and publish placement statistics transparently.",
    "Announce a state skills-guarantee scheme where youth who attend the fair receive certified training vouchers.",
    "Form a youth employment advisory panel to recommend quality standards for future fairs.",
    "Defend the fair's scale and say employment is a market-driven outcome the state can only facilitate.",
],
"gov_cooperative_bank_stress": [
    "Commission an independent auditor, freeze new credit expansion, and publish a depositor protection plan.",
    "Arrange a state liquidity support line to protect depositors and prevent any run on the cooperative.",
    "Ask the registrar of cooperative societies to inspect accounts and report within two months.",
    "Defend the bank's fundamentals and accuse the opposition of deliberately spreading depositor panic.",
],
"gov_railway_coordination_blame": [
    "Write formally to the Railway Board demanding a joint suburban operations committee with state representation.",
    "Announce a state-funded shuttle bus fleet on all poorly served rail corridors as an immediate alternative.",
    "Convene a coordination meeting with divisional railway managers and report outcomes to the assembly.",
    "Say rail is a central subject and redirect criticism to the Railway Ministry as the responsible authority.",
],
"gov_public_exam_paper_leak": [
    "Cancel and reschedule the exam, deploy a special task force, and arrest those named in the leak chain.",
    "Announce free re-examination with full logistical support and compensate registered candidates for costs.",
    "Constitute a board-level probe committee and ban social media discussion to contain speculation.",
    "Call the leak an unverified rumour and warn against irresponsible fear-mongering before exams.",
],
"gov_market_fire_response": [
    "Order a fire services audit at all major markets, name the officer who approved the fire clearance, and compensate traders.",
    "Set up an emergency trade relief fund and deploy additional fire tenders to all markets within 24 hours.",
    "Ask the fire department to submit an incident report and schedule a municipal safety review meeting.",
    "Say response time was within norms and attribute the damage to the building's illegal storage.",
],
"gov_slum_eviction_notice": [
    "Suspend all eviction notices until a fair and documented resettlement plan is published and agreed.",
    "Announce an accelerated resettlement housing scheme with dedicated transit accommodation before any relocation.",
    "Ask the urban development department to prepare a community consultation report before any action.",
    "Say evictions follow court orders and accuse activists of inciting vulnerable communities for political gain.",
],
"gov_teacher_union_pressure": [
    "Negotiate a time-bound concession package with the union, tied to no-strike commitments through the academic year.",
    "Offer an immediate salary revision advance and promise full revision within the next budget cycle.",
    "Form a bipartite committee with union and finance department to assess demands and report in 45 days.",
    "Resist all demands publicly, citing fiscal constraints, and challenge the union to justify its numbers.",
],
"gov_district_collector_transfer": [
    "Publish the transfer order with written administrative reasons and invite feedback through official channels.",
    "Arrange a ceremonial farewell for the outgoing collector and appoint a well-regarded replacement quickly.",
    "Say the transfer is routine administrative rotation and deflect further questions to the chief secretary.",
    "Describe the move as entirely routine and accuse critics of personalising standard administrative decisions.",
],
"gov_rural_drinking_water": [
    "Deploy repair teams to the 20 worst-affected villages, publish a tube-well status dashboard, and set deadlines.",
    "Release emergency Jal Jeevan Mission funds for rapid tube-well repairs before summer intensifies.",
    "Ask the public health engineering department to file a district-wise repair priority list within a week.",
    "Say 90% of tube wells are functional and attribute remaining failures to local overuse beyond design capacity.",
],
"gov_sports_stadium_cost": [
    "Commission an independent cost audit, publish findings, and hold the project management consultant accountable.",
    "Announce a revised funding model with private co-investment to reduce state cost and demonstrate efficiency.",
    "Ask the finance department to review the project's cost escalation and submit a variance report.",
    "Defend the cost as necessary for world-class infrastructure and compare it favourably with national benchmarks.",
],
"gov_old_age_pension_backlog": [
    "Open pension disbursement camps in every block, clear the backlog within 30 days, and automate future payments.",
    "Release the full pending pension amount as a one-time lump sum through post offices and rural banks.",
    "Ask the social welfare department to produce a block-wise beneficiary backlog report within a fortnight.",
    "Attribute delays to central database migration and say state payment is fully up to date on its own accounts.",
],
"gov_crop_insurance_confusion": [
    "Deploy claim-facilitation desks at every block agriculture office and simplify the form to a single page.",
    "Announce a state top-up payment to bridge the gap while insurance claims are processed nationally.",
    "Convene an emergency agriculture board meeting with insurance company representatives to resolve disputes.",
    "Say the confusion is the insurer's responsibility and that the state correctly enrolled farmers as required.",
],
"gov_illegal_sand_mining": [
    "Raid identified sites, seize equipment, file FIRs, and name any politically connected operators in the press note.",
    "Station rapid response teams at three worst riverbanks and increase police boat patrols to deter mining.",
    "Ask the mines department and police to file a joint enforcement action plan within a fortnight.",
    "Say enforcement is ongoing and dismiss patronage allegations as defamatory without evidence.",
],
"gov_library_grant_delay": [
    "Publish the full grant decision list with evaluation scores; form a panel to review past selections for bias.",
    "Release all overdue grants immediately and double the next round's allocation to repair cultural goodwill.",
    "Ask the cultural affairs secretary to review grant disbursal criteria and propose an improved process.",
    "Defend the grant committee's expertise and call complaints sour grapes from unsuccessful applicants.",
],
"gov_price_rise_fair_shop": [
    "Increase fair-price shop supply quotas by 20%, ban hoarding with inspections, and publish stock data online.",
    "Announce a direct household relief transfer for BPL families to offset inflation on essential items.",
    "Set up a state price monitoring cell and publish a fortnightly bulletin on essential goods availability.",
    "Attribute pressure to global commodity inflation and say state prices remain below the national average.",
],
"gov_district_hospital_corruption": [
    "Freeze the disputed equipment purchase, commission an independent audit, and name any linked intermediaries.",
    "Announce a clean procurement portal for all hospital supplies and fast-track tenders with public disclosure.",
    "Ask the health department's internal audit wing to review the invoices and report within 30 days.",
    "Defend the purchase as competitively priced and accuse the opposition of misrepresenting technical specs.",
],
"gov_school_midday_meal_quality": [
    "Conduct kitchen inspections in all flagged schools, terminate non-compliant suppliers, and publish results.",
    "Double the per-meal budget temporarily and assign a nutritionist to each cluster for quality oversight.",
    "Ask district education officers to file weekly meal quality reports and act on complaints within 48 hours.",
    "Call quality complaints isolated incidents and note that crores of children receive meals without incident daily.",
],
"gov_border_area_smuggling": [
    "Coordinate with the BSF and customs for joint operations, publish seizure data monthly, and name convicted networks.",
    "Deploy additional district police at high-traffic entry points and install CCTV at key border market crossings.",
    "Ask the home department to form a border-security task force and submit a situation report within 21 days.",
    "Say border security is primarily a central responsibility and ask the Home Ministry to deploy more forces.",
],
"gov_handloom_credit_gap": [
    "Open a direct-weaver credit scheme bypassing cooperative middlemen and announce ₹50 crore in first-year loans.",
    "Hold state-funded buyer-seller meets in weaver clusters and pre-purchase artisan stock for government outlets.",
    "Convene an emergency meeting of the handloom board to design a credit facilitation framework.",
    "Say credit is available through NABARD schemes and describe the problem as one of awareness rather than access.",
],
"gov_district_court_backlog": [
    "Write to the Law Commission for additional judge postings and announce a state-funded e-court upgrade.",
    "Release emergency infrastructure funds for additional court rooms and support staff in the overloaded districts.",
    "Ask the state law department to compile a backlog-reduction proposal and present it to the high court.",
    "Say court administration is under the judiciary's jurisdiction and urge lawyers to raise it through bar councils.",
],
"gov_public_bus_accident": [
    "Mandate roadworthiness checks for all state buses within two weeks and publish results by depot.",
    "Announce ex-gratia to the victims' families and order a rapid route-safety audit of all high-accident corridors.",
    "Ask the transport authority to file a full incident report and place it before the assembly transport committee.",
    "Call it a tragic but isolated incident and note that the state has a better road safety record than neighbouring states.",
],
"gov_housing_scheme_names": [
    "Open the beneficiary list for public review online, invite objections within 15 days, and audit every flagged name.",
    "Add a corrective tranche of beneficiaries immediately and establish a fast-track appeals window.",
    "Ask the block development officer to verify the list and report discrepancies within three weeks.",
    "Say the list was prepared per eligibility guidelines and call protests the work of disqualified applicants.",
],
"gov_cultural_board_patronage": [
    "Publish all grant decisions with evaluation scores, appoint a rotating external panel, and review past selections.",
    "Release a special arts revival fund open to all applicants through a new transparent online portal.",
    "Ask the cultural affairs secretary to review the board's grant criteria and propose reform in 45 days.",
    "Defend the board's expertise and call the complaints sour grapes from unsuccessful applicants.",
],
"gov_urban_drainage_failure": [
    "Deploy drainage clearance crews to the 10 worst-blocked wards and publish a clearance map updated daily.",
    "Release emergency civic funds for pump procurement and contractor engagement within 24 hours.",
    "Issue a civic alert and schedule an emergency municipal council session on drainage infrastructure.",
    "Say the flooding was caused by unprecedented single-day rainfall and not by drainage system failure.",
],
"gov_rural_police_vacancy": [
    "Fast-track constable recruitment, post temporary personnel from adjacent districts, and set a six-month fill deadline.",
    "Deploy 200 home guards to the most under-staffed rural thanas as an immediate stop-gap measure.",
    "Ask the home department to submit a state-wide staffing gap report and an accelerated recruitment plan.",
    "Say vacancy levels are within a manageable threshold and point to crime statistics to show no safety gap.",
],
"gov_migrant_worker_return": [
    "Open MGNREGS demand registration camps, link returning workers to skill-upgradation programmes immediately.",
    "Release emergency ration entitlements and job cards for returnees and launch a district employment fair.",
    "Ask the rural development department to map returnees by district and submit a support plan.",
    "Say the state's rural employment schemes already cover returnees and advise them to apply through gram sabhas.",
],
"gov_college_hostel_safety": [
    "Conduct surprise hostel inspections, suspend wardens in default, and release emergency repairs in 15 days.",
    "Announce a ₹100 crore hostel modernisation package and deploy contractors to the worst three campuses.",
    "Ask the education department to file a condition report on all government hostels within a month.",
    "Say safety concerns are isolated and note that thousands of students live in hostels without incident.",
],
"gov_party_cadre_arrogance": [
    "Set up open district grievance offices and invite the public to complain directly to party leadership.",
    "Launch a high-profile public outreach campaign to reset the party's image at the ground level.",
    "Issue internal conduct circulars to all district units and schedule a cadre review meeting.",
    "Call critics unhappy former allies and say voter trust in the party remains strong.",
],
"gov_minister_health_absence": [
    "Announce the minister's immediate departure to the affected district and commit to a full day's health camp.",
    "Deploy a special health response team to the district and publicly brief the media on the steps taken.",
    "Explain that the minister was handling a concurrent state commitment and confirm a rescheduled visit.",
    "Say the absence was unavoidable and that administrative machinery handled the situation effectively.",
],

# ==================== OPPOSITION ====================
"opp_district_faction_fight": [
    "Convene a joint mediation session chaired by a state leader; get both factions to sign a shared election work plan.",
    "Channel the rivalry into a large joint district march and let public turnout settle the internal credibility contest.",
    "Survey booth committees to see which faction is delivering better ground work and reward accordingly.",
    "Let the financially stronger faction lead quietly in exchange for funding commitment for the coming rally.",
],
"opp_student_wing_bandh_pressure": [
    "Back a peaceful campus assembly with a clear student charter rather than a general bandh.",
    "Support the bandh demand, but deploy student marshals at every sensitive junction to prevent violence.",
    "Build a documented grievance list with verified cases before committing to any disruptive agitation.",
    "Accept a shorter targeted bandh of three hours on a single route to satisfy cadre without broad disruption.",
],
"opp_candidate_ticket_dispute": [
    "Hold an open constituency convention so both aspirants can publicly present their case to local workers.",
    "Set a final deadline, call a district rally, and let the turnout each aspirant brings influence the decision.",
    "Commission a quick booth-agent survey and award the ticket to whoever scores higher on ground support.",
    "Allow the losing aspirant to contest independently in exchange for financial contributions to other seats.",
],
"opp_donor_policy_pressure": [
    "Decline the conditional offer and launch a transparent small-donor crowdfunding drive instead.",
    "Accept the donation but route it through a registered public trust to dilute the appearance of a quid pro quo.",
    "Verify whether the donor group's earlier demands left any documented paper trail before accepting or refusing.",
    "Accept the funds quietly, keep the policy promise vague, and honour it selectively only if in power.",
],
"opp_booth_worker_dropout": [
    "Visit every dormant booth personally, acknowledge the neglect openly, and set up a monthly support structure.",
    "Announce a well-publicised cadre rally with clear role assignments to re-energise drifting booth workers.",
    "Map which booths have inactive workers, prioritise the swing seats, and rebuild there first.",
    "Offer a financial incentive to booth agents in the most critical seats to prevent further dropout.",
],
"opp_scandal_evidence_quality": [
    "Assign a research team to verify every document before any public statement or press conference is held.",
    "Hold an immediate press briefing with available evidence and escalate through street pressure while gathering more.",
    "Cross-check all documents against official gazette records and pending RTI replies before going public.",
    "Use the allegation privately to extract an administrative concession before taking the issue to the press.",
],
"opp_coalition_seat_demand": [
    "Offer the ally a meaningful role in the coalition's shadow cabinet and acknowledge two additional constituencies.",
    "Call a joint public rally to demonstrate alliance unity and make the political cost of breaking it too high.",
    "Commission a voter survey of the ally's target seats before committing to any revised seat-sharing formula.",
    "Offer the ally leadership a private arrangement to smooth over the public disagreement quietly.",
],
"opp_youth_unemployment_tour": [
    "Run a documented district listening tour; publish a district-wise unemployment report at the end.",
    "Combine the tour with a public meeting at each stop to link youth grievances with party demands.",
    "Pilot the tour in two swing districts, measure media response, then decide on a full rollout.",
    "Execute the tour with minimal party expenditure and have local workers host to show financial discipline.",
],
"opp_farmer_blockade_pressure": [
    "Organise a disciplined sit-in at the procurement office that highlights the delay without blocking traffic.",
    "Back the blockade with disciplined marshals at every junction and pre-brief media on the specific demand.",
    "Build a documented procurement grievance dossier first; call the blockade only when evidence is airtight.",
    "Accept a shorter, symbolic route blockade of three hours to satisfy cadre without alienating commuters.",
],
"opp_media_spokesperson_gaffe": [
    "Issue a calm factual correction within 12 hours, brief newspaper editors personally, and replace the spokesperson.",
    "Counter the gaffe with a high-energy public rally that generates fresh footage and displaces the damaging clip.",
    "Audit recent party communications, publish a corrected factsheet, and hold an internal media training session.",
    "Have the spokesperson insist there was no error in a paid-circulation correction note, then move on.",
],
"opp_minority_outreach_suspicion": [
    "Visit the community leadership quietly with a written list of specific pending demands and a delivery timeline.",
    "Join a public community solidarity event in force with a disciplined and respectful message.",
    "Collect first-hand testimony from community members before releasing any public statement on their behalf.",
    "Accept the community's endorsement with a private understanding about support in selected constituencies.",
],
"opp_women_wing_campaign": [
    "Fully endorse the safety campaign, send two senior leaders to launch it, and publicise beneficiary numbers.",
    "Run the safety campaign alongside a press conference highlighting the government's failure on women's safety.",
    "Verify that legal aid and transport resources are secured before committing to the full campaign roll-out.",
    "Let the women's wing run the campaign independently so the party retains financial and reputational distance.",
],
"opp_cleanliness_drive_offer": [
    "Endorse the ward cleanliness drive openly, assign senior volunteers, and share daily progress on social media.",
    "Run the drive but simultaneously stage a media walkabout to link every clean ward to government failure.",
    "Pilot the drive in one ward, measure public and media response, then scale with verified results.",
    "Support the drive with minimal party funds but maximise leadership photo opportunities for visibility.",
],
"opp_blood_donation_camp": [
    "Commit senior party volunteers as organisers, publicise the camp widely, and publish donor numbers post-event.",
    "Run the camp but organise a simultaneous press statement linking the blood shortage to hospital funding cuts.",
    "Confirm attendance only after verifying that adequate cold-chain equipment and trained staff are arranged.",
    "Allow student volunteers to front the camp and keep party involvement low-key to reduce cost.",
],
"opp_unity_march_tension": [
    "Participate actively in the peace march with a disciplined delegation and a clear, non-partisan message.",
    "Join the march in force with the party flag but hold a separate post-march rally framing it as political pressure.",
    "Consult civil society organisers on whether party participation would help or polarise the march further.",
    "Accept an endorsement role only if the march committee agrees to feature party demands in the public statement.",
],
"opp_rumor_against_govt": [
    "Decline to repeat the rumour and task the research cell to find verifiable primary source documents instead.",
    "Run with the story at a press conference and let public pressure force the government to release documents.",
    "File an RTI on the tender process first; present factual findings rather than unverified social media claims.",
    "Use the rumour privately to pressure the district administration for a local administrative concession.",
],
"opp_old_leader_relevance": [
    "Offer the veteran a ceremonial state-level advisory role with genuine presence at one flagship event.",
    "Call an internal discipline meeting and make clear that public dissent will cost him future campaign prospects.",
    "Survey district workers on whether the veteran commands real voter loyalty before making any concession.",
    "Negotiate a private financial arrangement with the leader to ensure public silence through the election cycle.",
],
"opp_social_media_troll_row": [
    "Issue a clear statement distancing the party from abusive accounts and launch a clean digital conduct code.",
    "Counter the troll controversy with a high-energy rally that generates fresh social media content.",
    "Audit which accounts are genuinely linked to the party before releasing any statement.",
    "Have party IT cell issue a denial claiming the accounts are government plants, then drop the subject.",
],
"opp_funds_short_before_rally": [
    "Launch a transparent public crowdfunding appeal and turn the fundraiser itself into a show of popular support.",
    "Announce a cadre emergency fundraiser tied to the rally; make the financial constraint part of the narrative.",
    "Cut lower-priority rally expenditure and renegotiate with vendors before seeking external funds.",
    "Accept a large donor's conditional offer and schedule settlement of any policy expectations for after the election.",
],
"opp_candidate_criminal_record": [
    "Replace the aspirant with a clean candidate and issue a public statement on the party's integrity criteria.",
    "Retain the aspirant but hold a public accountability session where he addresses the pending cases directly.",
    "Commission an internal legal review of each pending case before deciding whether to grant the ticket.",
    "Allow the aspirant to run from a less prominent seat where street strength matters more than image.",
],
"opp_worker_clash_with_police": [
    "Send party lawyers to secure bail and hold a candlelight vigil outside the police station the same evening.",
    "Stage a mass demonstration at the police station and demand immediate release before midnight.",
    "Document all police action through video and eyewitness accounts before deciding on a public response.",
    "Negotiate worker release quietly through a back-channel contact in the district administration.",
],
"opp_manifesto_costing_gap": [
    "Commission a costed policy note with an economist, invite academic review, and publish before any rally.",
    "Announce the manifesto at a major rally and generate public momentum before detractors can audit it.",
    "Pilot two key promises in sympathetic panchayats and build an evidence base before formalising the manifesto.",
    "Keep promise language aspirational rather than specific so no single commitment becomes a hostage to cost.",
],
"opp_rural_listening_tour": [
    "Assign two senior leaders to the tour, brief them on specific local issues, and publish a findings report.",
    "Combine the listening tour with a public meeting at each stop to link service politics with party demands.",
    "Run a pilot in one district, measure media and voter response, then expand the format.",
    "Execute the tour by having local workers host, reducing party overheads while maintaining visibility.",
],
"opp_teacher_applicant_forum": [
    "Form a legal support group for applicants, gather authenticated documents, and prepare a writ petition.",
    "Hold an open public forum with applicants on the steps of the education secretariat for media coverage.",
    "File an RTI for the full recruitment record before making any public commitment to the applicants.",
    "Use the applicants' organised frustration as leverage for a private administrative concession on the recruitment.",
],
"opp_health_camp_opportunity": [
    "Fully endorse the camp, provide logistical support, and invite the press to cover beneficiary numbers.",
    "Run the camp but simultaneously hold a press conference linking the demand to government health failures.",
    "Verify that medicine stock and medical staff are secured before formally associating with the event.",
    "Allow the doctors to run the camp independently; the party keeps its name available but out of direct cost.",
],
"opp_opposition_alliance_symbol": [
    "Redesign all coalition campaign material to feature all partner symbols equally and share the updated brief.",
    "Call a joint press conference of all alliance partners to display public unity and reset campaign materials.",
    "Survey voter response in one constituency on symbol prominence before agreeing to a joint design standard.",
    "Offer the smaller ally a private financial package to accept the current symbol arrangement without public dispute.",
],
"opp_district_office_rent_due": [
    "Launch a transparent crowdfunding campaign to pay the rent and turn the financial story into a solidarity moment.",
    "Stage a rally at the office building to generate media attention and cadre fundraising simultaneously.",
    "Cut all discretionary spending in the district for 30 days to free up the overdue rent amount.",
    "Accept a single large donor's offer quietly and manage any policy expectations informally later.",
],
"opp_student_leader_radical_speech": [
    "Bring the student leader into a private briefing, agree a revised disciplined platform, and redirect energy.",
    "Endorse the speech's core message publicly and add a moderating framing statement in the same release.",
    "Commission a quick swing-voter survey before deciding whether to endorse, distance, or rebrand the speech.",
    "Keep the student leader in play as long as mobilisation numbers justify the image risk with moderate voters.",
],
"opp_govt_welfare_claim_response": [
    "Publish a district-by-district counter-data brief with verified beneficiary testimonies and media-ready graphics.",
    "Launch a same-day social media counter-blitz with real beneficiary voices to neutralise the government ad.",
    "File RTIs for scheme data in all districts, await official figures, and then publish a credible fact-check.",
    "Offer editors exclusive access to an opposition policy event in exchange for fair coverage of the counter-claim.",
],
"opp_local_language_identity": [
    "Organise inclusive cultural events celebrating local heritage and invite participation across all communities.",
    "Hold a regional language pride rally and use the turnout to pressure the government on cultural budget allocations.",
    "Commission party researchers to document genuine cultural grievances before framing any public narrative.",
    "Accept the identity campaign platform conditionally if cultural organisations commit electoral support in return.",
],
"opp_tea_worker_solidarity": [
    "Spend a full day in the tea belt with workers, document wage arrear figures, and publish a formal demand charter.",
    "Organise a workers' march to the district collector's office and demand the labour minister meet the press.",
    "Verify wage arrear data from multiple gardens and check for contradictions before public commitment.",
    "Extend conditional political support in exchange for the union's commitment to mobilise in specific constituencies.",
],
"opp_panchayat_defector_offer": [
    "Welcome the defector conditionally, pending a public accountability statement about past affiliations.",
    "Organise a public joining ceremony immediately to maximise the signal value to other potential defectors.",
    "Conduct a quiet survey of the defector's real voter base in the panchayat before granting any party position.",
    "Accept the defection privately and agree to suppress any prior complaints against the defector's conduct.",
],
"opp_newspaper_editor_meeting": [
    "Prepare a serious district-wise policy alternative brief and present it personally to editors before the press cycle.",
    "Launch a same-day targeted social media campaign to supplement the editorial meeting with digital coverage.",
    "File RTI requests for government scheme data and offer editors the verified results as exclusive material.",
    "Offer editors priority access to the party's next major event in exchange for fairer coverage of opposition views.",
],
"opp_volunteer_data_drive": [
    "Launch a structured volunteer intake with training sessions, clear role assignments, and a data-use policy.",
    "Tie the data drive to a major district rally so booth workers get systematically organised in one mobilising event.",
    "Pilot the data system in two booths, measure accuracy and worker comfort, and scale only after validation.",
    "Outsource the data work to a friendly private firm, keeping party leadership's direct costs off the books.",
],
"opp_public_interest_litigation": [
    "Assign a senior advocate, prepare well-documented affidavits, and file a properly researched PIL.",
    "File the PIL immediately for media impact and supplement with street agitation to maintain pressure.",
    "Wait for the RTI response on the scandal before filing so that the PIL has a complete evidentiary basis.",
    "Use the threat of a PIL to negotiate a quiet administrative concession before incurring legal costs.",
],
"opp_candle_vigil_or_b_bandh": [
    "Back the candlelight vigil as the primary form; it earns broader public sympathy without disruptive backlash.",
    "Support the bandh but deploy trained marshals to prevent incidents and brief media on specific demands.",
    "Gauge public preference in two sample areas before committing to either format.",
    "Propose a hybrid: three-hour symbolic shutdown followed by a vigil to satisfy both camps without full bandh cost.",
],
"opp_regional_pride_rally": [
    "Organise inclusive regional pride events that focus on development grievances without exclusionary rhetoric.",
    "Hold the full-scale regional pride rally; leverage turnout size to pressure the government on district allocations.",
    "Document specific regional development grievances before framing any public pride narrative.",
    "Accept the regional pride platform conditionally if cultural bodies back the party in the upcoming election.",
],
"opp_anti_corruption_hotline": [
    "Launch the hotline through a verified registration system to prevent abuse and assign case officers.",
    "Open the hotline with a major press conference to generate maximum public submissions quickly.",
    "Run a two-week pilot in one district before scaling state-wide; assess complaint quality and system load.",
    "Use hotline submissions privately to identify the most damaging cases before deciding which to publicise.",
],
"opp_union_support_condition": [
    "Accept the union's endorsement in exchange for a written policy position on their key wage demand.",
    "Stage a joint rally with union leaders to demonstrate solidarity and amplify both organisations' pressure.",
    "Verify the union's membership base and actual polling influence before committing to any formal arrangement.",
    "Accept union support conditionally and delay formal acknowledgment of the strike demand until after elections.",
],
"opp_college_debate_invite": [
    "Accept the invite, prepare well on the policy data, and use the debate to showcase governance alternatives.",
    "Accept the debate and use it as a platform for a post-debate campus rally to energise student supporters.",
    "Assess whether the college forum is sympathetic or adversarial before committing senior leadership.",
    "Accept the invite but send a well-briefed second-tier spokesperson to limit leadership reputational risk.",
],
"opp_misinformation_in_whatsapp": [
    "Issue a clear correction through official party channels and set up a rapid-response fact-check team.",
    "Counter misinformation with a higher-volume social media blitz of verified content to displace the false claims.",
    "Trace whether the false posts link to party workers before issuing any public statement.",
    "Have the party IT cell post a denial claiming the messages are planted by the government's cyber wing.",
],
"opp_village_committee_capture": [
    "Call an open meeting with all village committee members and announce an independent review process.",
    "Turn the capture issue into a local agitation to demand fresh elections and use press coverage as leverage.",
    "Document which committees have been captured through testimonies before proposing any structural remedy.",
    "Quietly recognise the dominant faction's control in exchange for their commitment not to defect before polling.",
],
"opp_fundraiser_dinner_backlash": [
    "Replace the high-ticket dinner with an open-invitation public meeting that also accepts voluntary contributions.",
    "Hold the dinner but ensure equal billing with a large free community meal on the same evening.",
    "Survey likely attendees and media perception in advance before setting the ticket price threshold.",
    "Proceed with the high-ticket dinner but keep the guest list unpublished to manage the optics.",
],
"opp_retired_bureaucrat_recruitment": [
    "Offer the bureaucrat a well-defined advisory role on governance policy that gives genuine input without cadre friction.",
    "Announce the recruitment at a public event to maximise the signal of the party's administrative competence.",
    "Consult district unit heads and senior cadre before making any offer to avoid internal resentment.",
    "Accept the offer privately and keep the formal announcement vague to manage both sides of the internal debate.",
],
"opp_cadre_fund_misuse": [
    "Commission an immediate internal audit, suspend the treasurer, and publish the findings to all district units.",
    "Call a district press conference to announce the investigation and preempt the government from breaking the story.",
    "Verify the allegation's source before acting; ensure the evidence is solid before any public statement.",
    "Quietly resolve the matter internally with the treasurer in exchange for future financial cooperation.",
],
"opp_flood_relief_volunteers": [
    "Deploy party volunteers with documented supplies, keep a public log of villages helped, and invite press coverage.",
    "Stage a high-visibility relief convoy with cameras and explicitly link the effort to the government's failure.",
    "Survey the actual relief need before committing resources to avoid over-promising or under-delivering.",
    "Deploy volunteers only where media presence guarantees coverage; skip villages where cameras cannot reach.",
],
"opp_district_yatra_route": [
    "Divide the yatra into two legs, covering all disputed districts, and hold an open route-planning meeting.",
    "Set the route by measuring social media buzz and crowd potential to maximise national media attention.",
    "Survey booth-level activation needs across districts and route the yatra to the highest-need areas.",
    "Let the financially strongest district unit host the main yatra stop in exchange for funding the logistics.",
],
"opp_local_press_blackout": [
    "Invite editors and senior reporters to a detailed policy briefing and build a genuine information relationship.",
    "Generate independent news value through a major rally or agitation that local papers cannot ignore.",
    "Investigate whether the blackout is editorial policy or advertiser pressure before deciding on a response.",
    "Fund a semi-independent local news platform that covers party events in exchange for reliable publication.",
],
"opp_policy_on_industry_land": [
    "Publish a clear 'fair compensation and consent' land policy note and invite civil society review.",
    "Announce the policy position from a major constituency rally to generate momentum before it can be challenged.",
    "Pilot the policy framework in one sympathetic block and build a factual evidence base before wider adoption.",
    "Keep the land policy deliberately ambiguous to avoid alienating either farmer or industry voter segments.",
],
"opp_religious_festival_invite": [
    "Accept all festival invites across communities and attend each with an identically sized, cross-community delegation.",
    "Attend with the full party delegation and distribute a welfare outreach pamphlet addressing all communities.",
    "Consult community leaders of all groups before accepting any single invite to prevent perceived bias.",
    "Accept the invite only if the festival committee agrees to also invite the party to equal-sized events of other groups.",
],
"opp_booth_agent_training": [
    "Run a comprehensive booth-agent training programme with mock polling exercises and clear assignment sheets.",
    "Tie the training to a district rally so booth agents experience both mobilisation and operational preparation.",
    "Pilot the training in five contested booths, assess results, and refine the curriculum before a wider rollout.",
    "Outsource training to a sympathetic NGO to reduce party costs while maintaining the political benefit.",
],
"opp_press_conference_evidence": [
    "Delay the press conference until all documents are verified and assign a senior leader who knows the material.",
    "Hold the press conference immediately with available evidence; public pressure will force further disclosure.",
    "File an RTI for the missing documents, await the response, and then hold a fully evidenced press conference.",
    "Use the threat of a press conference to extract a quiet administrative concession before going public.",
],
"opp_youth_music_outreach": [
    "Back the event fully, co-curate the programme with youth volunteers, and promote it as party-wide.",
    "Turn the cultural event into a protest-art rally that links youth expression with specific party demands.",
    "Pilot the event in one college town; measure media and voter response before rolling it out state-wide.",
    "Contribute minimal party funds but ensure maximum leadership photo-opportunity at the final performance.",
],
"opp_senior_leader_rebellion": [
    "Offer the leader a genuine campaign role in his home district and schedule a joint public appearance.",
    "Call a party discipline session and signal publicly that rebellion will cost him any future candidacy.",
    "Commission a quiet survey of the leader's real voter following before making any concession.",
    "Negotiate a private financial arrangement with the leader to secure his public silence through polling day.",
],
"opp_model_village_promise": [
    "Publish a costed and legally viable model village proposal and invite gram sabha endorsement.",
    "Announce the model village pledge from the biggest rally on the schedule for maximum electoral impact.",
    "Pilot the model village framework in one sympathetic panchayat before making it a state-wide promise.",
    "Keep the model village language aspirational and vague enough to avoid being held to precise deliverables.",
],
"opp_grassroots_manifesto_input": [
    "Convene district jan-sabhas to collect verified local demands and incorporate a curated selection in the manifesto.",
    "Hold a state-wide manifesto convention and let the sheer scale of participation generate campaign momentum.",
    "Pilot consultations in two swing districts to assess what input is feasible before opening the process more widely.",
    "Accept local demands selectively based on their electoral salience rather than their policy merit.",
],
"opp_rival_opposition_poaching": [
    "Visit poached workers personally, address their grievances, and announce a structured local organiser support fund.",
    "Organise a counter-rally in the affected area to demonstrate the party's continuing strength and energy.",
    "Identify why workers are leaving; address the root grievance before attempting any counter-recruitment.",
    "Offer financial incentives to the most critical poached workers to secure their return before the election.",
],
"opp_minor_scandal_overreach": [
    "Limit the charge to documented facts, present it at one disciplined press conference, and avoid escalation.",
    "Run with the maximum framing of the issue and use street pressure to force further government disclosure.",
    "Verify every detail of the allegation before finalising the framing to avoid a credibility rebound.",
    "Use the minor irregularity privately to negotiate a local administrative accommodation before going public.",
],
"opp_local_riot_statement": [
    "Issue a carefully worded appeal for peace that names no community and calls for accountability through law.",
    "Hold a solidarity rally in the affected area and use it to demand both justice and better policing.",
    "Gather testimony from affected residents of all communities before releasing any public statement.",
    "Release a statement calibrated to maximise support in the dominant community in the affected area.",
],
"opp_women_candidate_pressure": [
    "Commit to fielding at least two more women candidates and publish the updated nomination criteria publicly.",
    "Make the women's candidate pledge at a major public rally and link it to the party's broader gender platform.",
    "Survey likely women candidates by booth-level popularity before finalising how many seats to commit.",
    "Accept the pledge publicly but manage implementation through quiet negotiation with local power brokers.",
],
"opp_anti_incumbency": [
    "Organise a district listening campaign to hear voter grievances and produce a credible reform agenda.",
    "Capitalise on anti-incumbency with a high-energy accountability rally naming specific government failures.",
    "Map which voter segments are most anti-incumbent and document their top three issues before campaigning.",
    "Channel anti-incumbency sentiment into a fundraising moment before formalising any electoral strategy.",
],
}

# Apply texts to each item
new_items = []
for item in data['issueItems']:
    ni = copy.deepcopy(item)
    key = item['issueKey']
    if key not in ITEM_TEXTS:
        print(f"MISSING KEY: {key}")
        new_items.append(ni)
        continue
    texts = ITEM_TEXTS[key]
    for opt, text in zip(ni['options'], texts):
        opt['text'] = text
    new_items.append(ni)

data['issueItems'] = new_items

with open('west_bengal_2000_monthly_issues_review_v3.json','w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Done. Items written:", len(new_items))





