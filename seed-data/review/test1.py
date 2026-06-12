import json

# ─────────────────────────────────────────────────────────────────────────────
# HELPER: build a standard GOV item
# slots: strict_action | quick_relief | message_and_delay | protect_machinery
# ─────────────────────────────────────────────────────────────────────────────
def gov(key, cat, title, desc, weight,
        t0, t1, t2, t3,
        c0, c1, c2,
        e0, e1, e2, e3,        # [morale,corrupt,media,support] for each slot
        risk0, risk1, risk2, risk3,   # (chance, badOutcome)
        re0, re1, re2, re3,    # risk effect [morale,corrupt,media,support]
        de0_comm, de1_comm, de2_comm, de3_comm):   # delayed commentary
    def slot(optKey, text, cost, eff, riskChance, badOutcome, riskEff, deComm):
        m,cr,mi,ps = eff
        rm,rcr,rmi,rps = riskEff
        return {
            "optionKey": optKey,
            "text": text,
            "cost": cost,
            "effects": {"selfParty": {"coins": -cost,"partyMorale":m,"corruptionScore":cr,"mediaImage":mi,"publicSupport":ps}},
            "delayedEffects": [{"minTurns":1,"maxTurns":4,"chance":55,"effects":{"selfParty":{"coins":0,"partyMorale":0,"corruptionScore":0,"mediaImage":1 if ps>0 else -1,"publicSupport":1 if ps>0 else -1}},"commentary":deComm}],
            "risk": {"chance":riskChance,"badOutcome":badOutcome,"effects":{"selfParty":{"coins":0,"partyMorale":rm,"corruptionScore":rcr,"mediaImage":rmi,"publicSupport":rps}}}
        }
    return {
        "issueKey": key, "roleAllowed": ["GOVERNMENT"],
        "category": cat, "title": title, "description": desc, "weight": weight,
        "options": [
            slot("strict_action", t0, c0, e0, risk0[0], risk0[1], re0, de0_comm),
            slot("quick_relief",  t1, c1, e1, risk1[0], risk1[1], re1, de1_comm),
            slot("message_and_delay", t2, c2, e2, risk2[0], risk2[1], re2, de2_comm),
            slot("protect_machinery", t3, 0,  e3, risk3[0], risk3[1], re3, de3_comm),
        ]
    }

# HELPER: build a standard OPP item
# slots: constructive_service | aggressive_agitation | verify_and_attack | funds_first_compromise
def opp(key, cat, title, desc, weight,
        t0, t1, t2, t3,
        c0, c1, c2,
        e0, e1, e2, e3,
        risk0, risk1, risk2, risk3,
        re0, re1, re2, re3,
        de0_comm, de1_comm, de2_comm, de3_comm):
    def slot(optKey, text, cost, eff, riskChance, badOutcome, riskEff, deComm, isNeg=False):
        m,cr,mi,ps = eff
        rm,rcr,rmi,rps = riskEff
        coin = cost if isNeg else -cost
        return {
            "optionKey": optKey,
            "text": text,
            "cost": cost,
            "effects": {"selfParty": {"coins": coin,"partyMorale":m,"corruptionScore":cr,"mediaImage":mi,"publicSupport":ps}},
            "delayedEffects": [{"minTurns":1,"maxTurns":4,"chance":52,"effects":{"selfParty":{"coins":0,"partyMorale":0,"corruptionScore":0,"mediaImage":1 if ps>0 else -1,"publicSupport":1 if ps>0 else -1}},"commentary":deComm}],
            "risk": {"chance":riskChance,"badOutcome":badOutcome,"effects":{"selfParty":{"coins":0,"partyMorale":rm,"corruptionScore":rcr,"mediaImage":rmi,"publicSupport":rps}}}
        }
    o0 = slot("constructive_service", t0, c0, e0, risk0[0], risk0[1], re0, de0_comm)
    o1 = slot("aggressive_agitation", t1, c1, e1, risk1[0], risk1[1], re1, de1_comm)
    o2 = slot("verify_and_attack",    t2, c2, e2, risk2[0], risk2[1], re2, de2_comm)
    o3 = slot("funds_first_compromise", t3, abs(t3) if isinstance(t3,int) else 9, e3, risk3[0], risk3[1], re3, de3_comm, isNeg=True)
    # funds_first cost is negative coin gain — handle separately
    fc = c2 - 4 if c2 > 4 else 8  # rough negative cost
    o3["cost"] = -fc
    o3["effects"]["selfParty"]["coins"] = fc
    return {
        "issueKey": key, "roleAllowed": ["OPPOSITION","THIRD_PARTY"],
        "category": cat, "title": title, "description": desc, "weight": weight,
        "options": [o0, o1, o2, o3]
    }

items = []

# =============================================================================
# 60 GOVERNMENT ISSUES — Maharashtra 2001-2006
# =============================================================================

items.append(gov(
    "gov_mh_drought_relief_2001","governance_delivery","Drought relief leakage in Vidarbha",
    "Villagers in Vidarbha talukas report that drought-relief grain is being diverted by local officials before it reaches families.",
    1.1,
    "Audit all relief disbursements, publish beneficiary lists online, and refer diversion cases to the district collector.",
    "Release emergency state grain stocks directly through tahsildars, bypassing the implicated depots.",
    "Set up a district-level grievance committee and open a toll-free helpline for the next 30 days.",
    "Attribute complaints to political opponents and defend the relief system as functioning within norms.",
    10,14,4,
    (-2,-5,5,4),(-1,2,3,4),(0,0,1,-1),(3,4,-3,-5),
    (16,"Audit uncovers links to ruling party network."),(20,"Bypassed dealers organise a protest."),(22,"Panel is dismissed as a delaying tactic."),(26,"Opposition publishes photo evidence of diversion."),
    (-2,0,-2,-2),(0,3,-3,-3),(0,0,-2,-3),(0,3,-4,-5),
    "Relief delivery improves in audit-covered blocks.","Visible grain distribution calms immediate anger.","Public patience thins without concrete results.","Local resentment compounds quietly.",
))

items.append(gov(
    "gov_mh_farmer_suicide_response","welfare_delivery","Farmer suicide spike in Amravati",
    "A cluster of farmer suicides in Amravati draws national media; opposition demands immediate compensation and debt relief.",
    1.2,
    "Announce an emergency compensation scheme, deploy mental health counsellors, and fast-track debt waivers for the worst cases.",
    "Release ₹50,000 ex-gratia per affected family immediately and dispatch the agriculture minister to the region.",
    "Form a seven-member expert committee on agrarian distress and promise a white paper in 90 days.",
    "Describe suicides as personal tragedies unrelated to government policy and reject debt-waiver demands.",
    12,16,5,
    (-2,-4,5,5),(1,1,4,5),(0,0,2,-1),(3,5,-5,-5),
    (14,"Compensation delayed; second wave of deaths draws more coverage."),(18,"Opposition alleges ex-gratia money was captured by middlemen."),(25,"Committee report leaks; findings embarrass government."),(30,"Farmer unions stage a march to the CM residence."),
    (-3,0,-3,-4),(0,2,-3,-4),(0,0,-3,-4),(0,4,-5,-5),
    "Counselling camps reduce distress in affected villages.","Ex-gratia payments reach most families on time.","Commission approach delays meaningful relief.","Coverage intensifies and opposition gains ground.",
))

items.append(gov(
    "gov_mh_mumbai_flood_infrastructure","infrastructure_delivery","Mumbai flood infrastructure failure",
    "The 2005-style pre-monsoon drainage failure in Mumbai causes mass waterlogging; BEST bus services grind to a halt.",
    1.2,
    "Audit all storm drains, penalise contractors who failed to deliver, and publish a pre-monsoon repair status board.",
    "Release emergency BMC funds for rapid desilting and deploy NDRF teams to flood-prone wards.",
    "Convene a BMC emergency meeting and commission an independent drainage study.",
    "Blame Brihanmumbai Municipal Corporation for mismanagement and distance the state government.",
    11,15,5,
    (-1,-3,4,4),(1,2,3,4),(0,0,2,-1),(2,3,-4,-4),
    (18,"Second flooding episode exposes unfinished repairs."),(22,"Audit reveals contractor-official nexus."),(24,"Study takes months; monsoon arrives before action."),(28,"BMC counters by leaking state's failure to release funds."),
    (-2,0,-3,-3),(0,2,-3,-3),(0,0,-2,-3),(0,3,-4,-4),
    "Drain clearance visibly improves commuter experience.","NDRF presence reassures residents.","Citizens frustrated by pace of change.","Media frames blame game as evasion.",
))

items.append(gov(
    "gov_mh_electricity_maharashtra_2002","public_service","Power load-shedding hits rural Maharashtra",
    "Eight-hour daily power cuts across Marathwada and Vidarbha cripple irrigation pumps and cold-storage units.",
    1.1,
    "Order MSEDCL to publish load-shedding schedules, prioritise agricultural feeders, and fire the defaulting zone officer.",
    "Announce a ₹300 crore emergency fund to procure additional power from the grid and repair ageing substations.",
    "Set up a state power review panel and promise a new load-shedding policy within 30 days.",
    "Attribute cuts to a national coal shortage and request Centre intervention rather than acting on state supply.",
    10,14,4,
    (-2,-3,4,3),(1,2,3,4),(0,0,1,-1),(2,3,-3,-4),
    (20,"MSEDCL union challenges order; industrial areas also affected."),(22,"Funds released but procurement delayed by tender rules."),(26,"Panel report contradicts official line."),(28,"Centre disputes state's characterisation and leaks correspondence."),
    (-2,0,-2,-3),(0,2,-3,-3),(0,0,-2,-3),(0,2,-4,-4),
    "Agricultural feeder schedule reduces pump disruption.","Additional power units ease evening peak cuts.","Citizens frustrated waiting for the new policy.","Blame-game reduces state's credibility on energy governance.",
))

items.append(gov(
    "gov_mh_ration_card_ghost","welfare_integrity","Ghost ration cards expose in Nashik",
    "A civic audit reveals over 80,000 ghost ration cards in Nashik district, with grain being claimed on behalf of dead or migrant beneficiaries.",
    1.0,
    "Cancel all flagged cards, launch a biometric re-verification drive, and register FIRs against identified dealers.",
    "Issue new PDS smart cards to legitimate beneficiaries and deploy additional inspectors for 60 days.",
    "Announce a state-wide card verification programme and set a six-month deadline.",
    "Describe the audit as exaggerated and say overall PDS functioning is within acceptable tolerance.",
    10,14,3,
    (-1,-5,4,4),(1,2,3,4),(0,0,1,-1),(3,4,-3,-5),
    (16,"Verification finds the problem is state-wide in scope."),(20,"Smart-card rollout delayed by vendor issues."),(24,"Deadline passes without measurable progress."),(28,"Second audit confirms worse numbers statewide."),
    (-2,0,-2,-3),(0,2,-3,-3),(0,0,-2,-3),(0,4,-4,-5),
    "Biometric camps improve beneficiary trust.","New card recipients appreciate faster service.","Citizens grow impatient waiting for wider results.","Resentment among legitimate poor holders grows.",
))

items.append(gov(
    "gov_mh_onion_price_crisis_2003","farmer_welfare","Onion price crash destroys Nashik farmer income",
    "Wholesale onion prices collapse to ₹1–2 per kg; Nashik farmers dump produce on roads and demand a procurement floor price.",
    1.2,
    "Announce a minimum support price for onions, open government procurement centres in five mandis, and ban distress export.",
    "Release emergency relief of ₹5,000 per acre to all affected farmers within 15 days.",
    "Form a marketing task force with NAFED to study price stabilisation mechanisms.",
    "Say prices are market-driven and urge farmers to diversify crops; oppose procurement intervention.",
    12,15,5,
    (-2,-3,5,5),(1,1,4,5),(0,0,2,-1),(2,3,-4,-5),
    (18,"Traders lobby against floor price; mandis close in protest."),(20,"Relief payment list excludes sharecroppers."),(25,"Task force delays; prices crash further."),(30,"National media frames as state abandoning farmers."),
    (-2,0,-3,-3),(0,2,-3,-4),(0,0,-2,-3),(0,4,-5,-5),
    "MSP announcement arrests further distress dumping.","Relief payments reach most registered farmers.","Farmers frustrated by slow policy response.","Opposition capitalises on farmer distress.",
))

items.append(gov(
    "gov_mh_mumbai_train_accident","transport_services","Suburban rail stampede at Parel station",
    "An overcrowded suburban train causes a platform stampede at Parel during peak hours, injuring 23 commuters.",
    1.0,
    "Demand Central Railway deploy crowd management protocols, and announce state contribution to station upgrades.",
    "Release immediate ex-gratia to all injured and deploy state police for crowd management on suburban platforms.",
    "Set up a rail safety commission with state and Railway representatives to report in 60 days.",
    "Call it a Railway Ministry matter and refuse to commit state funds to a central infrastructure issue.",
    9,13,4,
    (-1,-2,4,4),(1,1,3,4),(0,0,2,-1),(2,2,-3,-4),
    (16,"Second overcrowding incident occurs within the week."),(18,"Opposition questions ex-gratia disbursement speed."),(22,"Commission is seen as buck-passing."),(24,"Railway Ministry publicly contradicts state's position."),
    (-2,0,-2,-3),(0,1,-2,-3),(0,0,-2,-3),(0,2,-3,-4),
    "Crowd protocols reduce peak-hour density marginally.","Ex-gratia payments reach injured families quickly.","Commuters frustrated by slow safety improvements.","Media highlights state's reluctance to engage.",
))

items.append(gov(
    "gov_mh_slum_demolition_dharavi","urban_poverty","Dharavi slum demolition notices cause unrest",
    "Residents of Dharavi receive eviction notices without clear resettlement plans; rights groups and opposition stage a dharna.",
    1.1,
    "Freeze demolitions, publish resettlement entitlements per family, and open a grievance portal for objections.",
    "Announce an accelerated resettlement housing project with transit accommodation before any demolition.",
    "Hold community consultations in each cluster before proceeding and issue a 60-day moratorium.",
    "Say demolitions follow court orders and accuse activists of politicising slum governance.",
    10,14,4,
    (-1,-3,4,4),(1,2,3,4),(0,0,2,-1),(2,3,-4,-5),
    (18,"Eviction photos dominate evening news."),(20,"Transit accommodation site found inadequate."),(23,"Moratorium extended but residents still uncertain."),(27,"Court issues contempt notice for illegal demolitions."),
    (-2,0,-3,-3),(0,2,-3,-3),(0,0,-2,-3),(0,3,-4,-5),
    "Resettlement clarity reduces street-level tension.","Transit housing announcement calms most families.","Residents remain anxious without final plan.","Judicial scrutiny deepens political embarrassment.",
))

items.append(gov(
    "gov_mh_water_tanker_scam_pune","urban_services","Water tanker procurement scam in Pune",
    "A Pune Municipal Corporation audit flags inflated bills for water tanker procurement, with contracts linked to a ruling party affiliate.",
    1.0,
    "Order an independent audit, suspend the PMC official who approved contracts, and publish all tanker invoices.",
    "Announce a new e-tendering system for all municipal water contracts effective immediately.",
    "Set up a PMC vigilance committee to review procurement rules and report in 45 days.",
    "Defend the PMC process as compliant and call the audit findings a politically timed leak.",
    9,13,3,
    (-1,-5,4,4),(1,2,3,3),(0,0,2,-1),(3,4,-3,-5),
    (15,"Audit traces contract award to a senior party functionary."),(18,"E-tendering portal crashes on launch day."),(22,"Vigilance committee seen as protecting incumbents."),(26,"Opposition files FIR using invoice data."),
    (-2,0,-3,-3),(0,1,-2,-2),(0,0,-2,-3),(0,4,-4,-5),
    "New tendering reduces procurement irregularities.","Digital contracts increase transparency visibility.","Citizens see committee as delaying action.","FIR filing escalates political pressure on government.",
))

items.append(gov(
    "gov_mh_sugarcane_fdr_delay","farmer_welfare","Sugar mill delayed FDR payments to cane farmers",
    "Cane farmers across Kolhapur and Sangli complain that sugar mills have not paid the state-mandated Fair and Remunerative Price for three months.",
    1.1,
    "Issue ultimatum to mills to clear dues within 21 days or face licence action; publish mill-wise compliance.",
    "Announce a state bridge-loan to farmers pending mill payment clearance.",
    "Convene a tripartite meeting with mill owners, farmer groups, and the sugar commissioner.",
    "Describe payment delays as an industry cash-flow problem and urge farmers to wait for mill recovery.",
    10,14,4,
    (-2,-3,4,5),(1,1,3,5),(0,0,2,-1),(2,3,-4,-5),
    (18,"Mills lobby CM to extend deadline; farm unions reject extension."),(20,"Bridge loans disbursed late; interest costs accrue."),(24,"Tripartite meeting fails; mill owners walk out."),(28,"Farmer protest blocks state highway for two days."),
    (-2,0,-3,-3),(0,2,-3,-3),(0,0,-2,-3),(0,3,-5,-5),
    "Payment deadline drives compliance in most mills.","Bridge loan provides farmers immediate relief.","Farmers frustrated by lack of enforcement.","Highway protest disrupts movement and commerce.",
))

items.append(gov(
    "gov_mh_police_atrocity_marathwada","law_order","Police custody death in Marathwada triggers protests",
    "A Dalit man dies in police custody in an Aurangabad district police station; community groups demand an SIT probe.",
    1.2,
    "Suspend the implicated officers, order a judicial inquiry, and personally meet victim's family within 24 hours.",
    "Announce ex-gratia of ₹10 lakh to the family and transfer the station in-charge immediately.",
    "Order the SP to file an internal departmental report and submit it within seven days.",
    "Defend police conduct as lawful and question the circumstances leading to custody.",
    11,14,4,
    (-2,-4,5,4),(1,1,4,4),(0,0,2,-2),(3,5,-5,-5),
    (15,"Judicial probe names senior officers."),(18,"Community alleges ex-gratia is inadequate."),(22,"SP report clears accused officers; civil society erupts."),(28,"National SC/ST commission takes suo motu cognisance."),
    (-2,0,-3,-3),(0,1,-3,-3),(0,0,-4,-5),(0,4,-5,-5),
    "Judicial probe reduces street anger temporarily.","Ex-gratia payment acknowledged but justice still sought.","Departmental clearance fuels outrage further.","Commission scrutiny forces further government response.",
))

items.append(gov(
    "gov_mh_mla_encroachment_nagpur","governance_integrity","MLA linked to illegal encroachment in Nagpur",
    "A state legislator from the ruling alliance is accused of encroaching on a municipal playground in Nagpur.",
    0.9,
    "Direct the Nagpur Municipal Corporation to demolish the encroachment and issue a notice to the MLA.",
    "Fast-track alternative recreational space for the affected neighbourhood as compensation.",
    "Refer the matter to the MLA ethics committee and await findings.",
    "Call the encroachment a boundary dispute and defend the MLA's record of constituency service.",
    8,12,3,
    (-2,-5,4,3),(1,2,2,3),(0,0,1,-2),(3,4,-3,-4),
    (16,"MLA refuses to vacate; contempt petition filed."),(18,"Alternative space has less area; residents protest."),(22,"Ethics committee delays; media keeps story alive."),(24,"Opposition MLA holds press conference at the site."),
    (-2,0,-3,-3),(0,1,-2,-2),(0,0,-2,-3),(0,3,-4,-4),
    "Demolition order signals rule of law stance.","Alternative space announcement satisfies some residents.","Committee delay fuels perception of double standards.","MLA's defiance emboldened by government inaction.",
))

items.append(gov(
    "gov_mh_education_ssc_results","education_integrity","SSC board exam malpractice allegations in Konkan",
    "Parents and students in Ratnagiri allege paper-setter irregularities in the SSC board exams; opposition demands a CBI probe.",
    1.0,
    "Cancel results in flagged centres, order a fresh exam, and suspend the examination board officials linked to the leak.",
    "Announce grace marks for students in affected centres and set up a rapid re-evaluation process.",
    "Form a three-member expert committee to audit examination procedures and report in 30 days.",
    "Call the allegations rumours amplified by coaching centres and stand by the board's integrity.",
    10,13,4,
    (-1,-4,4,4),(1,2,3,4),(0,0,2,-1),(2,3,-3,-4),
    (17,"Re-exam logistics chaos; parents angrier than before."),(19,"Coaching centres publish leaked paper publicly."),(22,"Expert committee confirms irregularities."),(26,"Opposition files PIL in Bombay High Court."),
    (-2,0,-2,-3),(0,2,-2,-3),(0,0,-3,-4),(0,3,-4,-4),
    "Re-exam process restores partial confidence.","Grace marks reduce immediate student anxiety.","Committee findings worsen credibility further.","HC order compels state to act on findings.",
))

items.append(gov(
    "gov_mh_ncp_bjp_coalition_tension","administrative_control","Coalition partner demands key ministry post",
    "The junior coalition partner publicly demands the home or finance portfolio, threatening to withdraw support if not accommodated.",
    0.9,
    "Hold firm on cabinet structure, publish a principled stance on merit-based allocation, and call a press conference.",
    "Offer the partner an enhanced budget outlay for their priority districts as an alternative to cabinet reshaping.",
    "Schedule private negotiations with coalition leadership and defer public comment.",
    "Capitulate to demands quietly and allow the cabinet reshuffle without public explanation.",
    8,12,4,
    (-2,-2,3,3),(1,1,3,3),(0,0,2,-1),(2,3,-3,-4),
    (16,"Partner leaks negotiation details to media."),(18,"Opposition charges coalition of horse-trading."),(20,"Private talks collapse; partner holds press conference."),(24,"Reshuffle seen as capitulation; state credibility dips."),
    (-2,0,-3,-3),(0,1,-2,-2),(0,0,-3,-4),(0,3,-4,-4),
    "Public principled stance earns editorial approval.","Budget outlay temporarily satisfies partner demand.","Leak from talks embarrasses both parties.","Optics of capitulation linger through next assembly session.",
))

items.append(gov(
    "gov_mh_textile_mill_closure_mumbai","industry_jobs","Textile mill land reuse dispute in Mumbai",
    "Former mill workers in Lalbaug protest that mill land sold to developers did not yield the promised housing for workers per the DCR rules.",
    1.1,
    "Commission an audit of DCR compliance, compel developers to deliver worker housing, and publish a timeline.",
    "Announce a transit-housing fund for affected mill workers from state urban development coffers.",
    "Set up a textile mill rehabilitation commission to review all DCR compliance cases.",
    "Say land development followed legal process and urge workers to file individual claims through MHADA.",
    10,14,4,
    (-1,-3,4,4),(1,2,3,4),(0,0,2,-1),(2,3,-4,-5),
    (18,"Developer challenges compliance order in court."),(22,"Fund disbursement slow; workers allege corruption."),(25,"Commission reveals widespread non-compliance."),(28,"HC issues contempt notice to non-compliant developers."),
    (-2,0,-3,-3),(0,2,-3,-3),(0,0,-2,-3),(0,3,-4,-5),
    "DCR audit creates credible enforcement signal.","Transit housing provides immediate relief for some families.","Workers frustrated by pace of rehabilitation process.","HC contempt notice forces faster developer compliance.",
))

items.append(gov(
    "gov_mh_road_nh4_contractor_scam","infrastructure_delivery","NH-4 Pune-Mumbai highway pothole scam",
    "Contractors resurface the same stretch of NH-4 three times in two years using substandard material; engineers allege kickbacks.",
    1.0,
    "Blacklist defaulting contractors, recover costs under warranty clauses, and order an independent quality audit.",
    "Release emergency road repair funds for the worst 50-km stretch before monsoon.",
    "Refer the matter to PWD vigilance and set up a quality monitoring committee.",
    "Say road quality is a National Highways Authority matter and redirect complaints to the Centre.",
    9,13,4,
    (-1,-4,4,3),(1,2,3,4),(0,0,2,-1),(2,3,-3,-4),
    (15,"Blacklisted firm re-registers under new name."),(18,"Emergency repairs wash out in first heavy rain."),(22,"Quality committee linked to contractors."),(26,"NHAI contradicts state's claim of jurisdiction."),
    (-2,0,-2,-3),(0,2,-3,-3),(0,0,-2,-3),(0,2,-4,-4),
    "Blacklisting deters some future contractor misconduct.","Emergency repairs reduce immediate accident risk.","Monitoring committee seen as ineffective.","Jurisdiction blame game reduces state credibility.",
))

items.append(gov(
    "gov_mh_water_latur_scarcity","public_service","Latur water scarcity reaches crisis level",
    "Latur city and surrounding villages go without piped water for 15–20 days at a stretch; train tankers are the only supply.",
    1.2,
    "Declare a water emergency, increase train tanker frequency, and commission a pipeline repair project with a 90-day deadline.",
    "Release ₹200 crore for borewell drilling, tanker supply, and short-term desalination infrastructure in the region.",
    "Form a district water management committee and publish a 15-day supply schedule.",
    "Attribute scarcity to below-average monsoon and say the state is doing its best within natural constraints.",
    11,15,5,
    (-2,-3,5,5),(1,2,4,5),(0,0,2,-1),(2,3,-4,-5),
    (18,"Pipeline project delayed by land acquisition."),(22,"Tanker supply monopoly linked to ruling party contractor."),(25,"Committee schedule not published on time."),(30,"NGO documents children missing school due to water fetching."),
    (-2,0,-3,-4),(0,2,-3,-4),(0,0,-2,-3),(0,3,-5,-5),
    "Increased tankers reduce queue times at distribution points.","Borewell drilling shows quick results in some villages.","Residents frustrated by lack of long-term solution.","Contractor link triggers national media coverage.",
))

items.append(gov(
    "gov_mh_land_acquisition_pune_it","industry_land","IT park land acquisition protests in Pune",
    "Farmers in Hinjewadi protest forced land acquisition at government rates for a private IT park expansion.",
    1.0,
    "Freeze acquisition, publish compensation terms publicly, and open a farmer review panel.",
    "Announce enhanced compensation at 4x circle rate and fast-track payment camps.",
    "Appoint a divisional commissioner to review acquisition terms and report in 30 days.",
    "Say acquisition follows the LA Act and attribute protests to political agitators.",
    9,13,4,
    (-1,-3,4,4),(1,2,3,4),(0,0,2,-1),(2,3,-4,-5),
    (16,"IT firm threatens to shift to another state."),(18,"Enhanced compensation excludes tenant farmers."),(22,"Commissioner review delays acquisition by two years."),(26,"Farmer blockade shuts the IT park entrance."),
    (-2,0,-3,-3),(0,2,-3,-3),(0,0,-2,-3),(0,3,-4,-5),
    "Compensation review reduces farmer anger.","Enhanced rates acknowledged as fair by most landowners.","Delay frustrates both farmers and investors.","Blockade causes international firms to reconsider.",
))

items.append(gov(
    "gov_mh_tb_hospital_neglect","public_service","TB hospital in Wardha found lacking basic supplies",
    "Patients at the state TB hospital in Wardha are found to be without adequate medicines and bed linen; a journalist's expose goes viral.",
    1.0,
    "Suspend the medical superintendent, release emergency procurement funds, and visit the facility personally.",
    "Dispatch medicines and supplies within 48 hours and order NRHM funds to be released for hospital upgrade.",
    "Ask the health secretary to file an incident report and schedule a ministry inspection within two weeks.",
    "Call the expose exaggerated and say the hospital meets minimum public health department standards.",
    9,13,4,
    (-2,-3,5,4),(1,2,4,4),(0,0,2,-1),(2,3,-4,-4),
    (15,"Second expose names three more TB hospitals in similar state."),(18,"NRHM funds released but procurement delayed by tenders."),(21,"Inspection reveals even worse conditions."),(24,"National TB programme takes up issue with Centre."),
    (-2,0,-3,-3),(0,2,-3,-3),(0,0,-2,-3),(0,3,-4,-4),
    "Supply delivery reduces patient suffering.","Emergency procurement provides immediate relief.","Inspection delay worsens public perception.","National attention intensifies political pressure.",
))

items.append(gov(
    "gov_mh_vidarbha_cotton_msp","farmer_welfare","Cotton MSP shortfall damages Vidarbha incomes",
    "Cotton procurement centres in Vidarbha fail to meet the Centre's announced MSP; CCI agents buy at below-MSP rates citing quality grades.",
    1.1,
    "Order state agriculture officials to enforce MSP compliance and take up quality-grading complaints with CCI formally.",
    "Announce a state top-up payment to bridge the MSP gap for registered farmers.",
    "Convene an emergency agriculture board meeting and invite CCI and farmers to negotiate.",
    "Say MSP enforcement is a central subject and urge farmers to contact CCI regional offices directly.",
    10,14,4,
    (-2,-3,5,5),(1,1,4,5),(0,0,2,-1),(2,3,-4,-5),
    (18,"CCI disputes state's quality complaint figures."),(20,"State top-up funds reach only 40% of farmers."),(24,"Board meeting fails; CCI officials don't attend."),(28,"Farmer union publishes below-MSP purchase receipts."),
    (-2,0,-3,-4),(0,2,-3,-4),(0,0,-2,-3),(0,3,-5,-5),
    "MSP enforcement notices put some procurement centres in line.","Top-up payment provides relief to registered farmers.","Negotiation fails; anger spreads to neighbouring districts.","Below-MSP evidence drives national editorial attention.",
))

items.append(gov(
    "gov_mh_municipal_school_privatisation","education_delivery","Municipal school privatisation row in Mumbai",
    "The BMC proposes handing over 50 under-enrolled municipal schools to NGOs; teacher unions and parents stage protests.",
    0.9,
    "Withdraw the proposal, commit to revitalising schools with infrastructure funds, and consult parents before any change.",
    "Announce a ₹500 crore school modernisation package for all 50 schools and retain them under BMC.",
    "Set up a parents-teachers committee to evaluate each school and recommend outcomes in 60 days.",
    "Defend the proposal as aimed at improving quality and call protests politically motivated.",
    9,13,4,
    (-1,-2,4,4),(1,2,3,4),(0,0,2,-1),(2,2,-3,-4),
    (15,"Union calls indefinite strike; 300 schools disrupted."),(18,"Modernisation package fails first-year implementation."),(22,"Committee recommends closure of 20 schools."),(24,"Opposition files PIL against the proposal."),
    (-2,0,-2,-3),(0,2,-3,-3),(0,0,-2,-3),(0,2,-3,-4),
    "Withdrawal of proposal restores teacher confidence.","Modernisation announcement is well received by parents.","Committee recommendation triggers fresh protests.","PIL creates legal uncertainty around school policy.",
))

items.append(gov(
    "gov_mh_chit_fund_fraud_konkan","finance_governance","Chit fund fraud collapses in Konkan coastal towns",
    "A Ratnagiri-based chit fund collapses, wiping out savings of 15,000 families; promoter is found to have ruling-party links.",
    1.0,
    "Order an immediate CID probe, freeze promoter's assets, and set up a victim compensation cell.",
    "Create a ₹50 crore state relief fund as advance compensation for the most vulnerable depositors.",
    "Ask the registrar of chit funds to submit a report and propose tighter regulation within 30 days.",
    "Deny any party link to the promoter and say the fraud is under police investigation.",
    9,13,4,
    (-1,-5,5,4),(1,2,3,4),(0,0,2,-1),(3,4,-3,-5),
    (16,"CID probe names a party district secretary."),(19,"Relief fund disbursement too slow for most victims."),(22,"Registrar report delayed; regulation overhaul stalls."),(26,"Opposition publishes promoter-party meeting photos."),
    (-2,0,-3,-3),(0,2,-3,-3),(0,0,-2,-3),(0,4,-4,-5),
    "Asset freeze partially protects victims.","Relief fund provides some immediate protection.","Regulatory delay leaves future victims exposed.","Photo evidence creates serious political damage.",
))

items.append(gov(
    "gov_mh_irrigation_scam_wcd","infrastructure_delivery","Irrigation scam allegations in Vidarbha WCD projects",
    "The opposition claims that completed Vidarbha irrigation projects show only 18% actual water utilisation despite full cost claims.",
    1.2,
    "Commission an independent audit by the CAG, freeze further payments to the contractors, and release interim data.",
    "Fast-track the completion of missing irrigation components with emergency funds and publish completion maps.",
    "Set up a water resources review committee to verify utilisation and report in 60 days.",
    "Call the utilisation figures politically manipulated and stand by the WCD department's completion certificates.",
    11,15,5,
    (-2,-5,5,4),(1,2,3,4),(0,0,2,-1),(2,4,-4,-5),
    (17,"CAG audit confirms large-scale cost inflation."),(21,"Emergency funds diverted to new contractors with same nexus."),(25,"Review committee linked to implicated officials."),(29,"Bombay HC takes suo motu cognisance."),
    (-3,0,-3,-4),(0,2,-3,-4),(0,0,-3,-4),(0,4,-5,-5),
    "CAG audit creates credible accountability signal.","Map publication exposes gaps; public anger rises.","Conflict-of-interest finding fuels wider scandal.","HC scrutiny forces executive action.",
))

items.append(gov(
    "gov_mh_bus_rapid_transit_pune","transport_services","Pune BRT project cost overrun and poor ridership",
    "The Pune Bus Rapid Transit corridor opens with dedicated lanes but early ridership is only 30% of targets; contractors overbilled.",
    0.9,
    "Publish a revised BRT business plan, penalise the planning contractor, and open feeder bus routes to improve access.",
    "Release emergency operational subsidies to PMPML to run more buses and reduce fares for the first six months.",
    "Commission a ridership study to identify cause and rectify in 90 days.",
    "Defend BRT as a long-term investment and say early ridership numbers are expected in any new system.",
    8,12,4,
    (-1,-2,3,3),(1,2,2,3),(0,0,2,-1),(2,2,-2,-3),
    (14,"Penalised contractor challenges award in court."),(17,"Subsidy misused; buses run on high-demand non-BRT routes instead."),(20,"Ridership study shows fundamental design flaws."),(22,"Media calculates cost per rider as ₹200+."),
    (-1,0,-2,-2),(0,1,-2,-2),(0,0,-2,-3),(0,2,-3,-3),
    "Feeder routes improve BRT integration.","Subsidised fares attract initial ridership boost.","Design flaw findings delay corrective action.","Media calculation undermines public confidence in BRT.",
))

items.append(gov(
    "gov_mh_dalit_atrocity_beed","law_order","Dalit atrocity case in Beed demands state response",
    "A Dalit family's house is torched in Beed after a caste dispute; three arrested but community alleges police inaction for hours.",
    1.1,
    "Invoke SC/ST PA Act stringently, fast-track the police complaint, and personally visit the affected family.",
    "Announce immediate rehabilitation support for the family and enhanced police patrols in the district.",
    "Order the SP to file a detailed action report and schedule a state SC commission visit.",
    "Say the incident is under investigation and caution against communalising a local dispute.",
    10,13,4,
    (-2,-4,5,4),(1,1,4,4),(0,0,2,-2),(2,3,-4,-5),
    (15,"Chargesheet omits key SC/ST provisions."),(18,"Police patrol withdrawn after media pressure subsides."),(22,"SC commission visit reveals inadequate support."),(26,"National Dalit groups hold Nagpur rally."),
    (-2,0,-3,-3),(0,1,-3,-3),(0,0,-3,-4),(0,4,-5,-5),
    "Stringent provisions deter further violence.","Rehabilitation support acknowledged by community.","Commission visit findings worsen perception.","National rally increases pressure for cabinet-level response.",
))

items.append(gov(
    "gov_mh_mumbai_air_quality","urban_services","Mumbai air quality index hits hazardous in winter",
    "Mumbai's AQI crosses 300 in December-January, prompting schools to close; construction dust and vehicular emissions blamed.",
    0.9,
    "Issue an emergency order banning construction dust without cover, mandate PUC checks, and close worst-polluting sites.",
    "Release funds to double the number of water-sprinkling vehicles and subsidise cleaner fuel for auto-rickshaws.",
    "Form a pollution task force and commit to a clean air action plan within 60 days.",
    "Attribute AQI spike to seasonal weather and say pollution levels are comparable to other metros.",
    8,12,3,
    (-1,-2,3,3),(1,2,2,3),(0,0,1,-1),(2,2,-3,-3),
    (14,"Construction lobby challenges ban in court."),(16,"Sprinkling trucks too few to make visible difference."),(19,"Task force plan leaks early and is mocked as inadequate."),(21,"Comparison with Delhi triggers unflattering media coverage."),
    (-1,0,-2,-2),(0,1,-2,-2),(0,0,-2,-3),(0,2,-3,-3),
    "Dust ban reduces particulate levels in central wards.","Sprinkling vehicles show visible impact on main roads.","Task force delay frustrates environmental groups.","Delhi comparison drives national media attention.",
))

items.append(gov(
    "gov_mh_hoarding_collapse_mumbai","law_order","Illegal hoarding collapse kills two in Andheri",
    "An unsecured billboard collapses during a storm in Andheri, killing two pedestrians; BMC found to have issued no-clearance warnings ignored by the advertiser.",
    1.0,
    "Cancel all hoardings without valid BMC clearance, prosecute the advertiser and the approving officer, and pay compensation.",
    "Announce an emergency structural audit of all BMC-registered hoardings within 15 days.",
    "Set up a hoarding safety committee to propose new regulations.",
    "Call it an isolated incident caused by exceptional storm conditions and promise improved weather monitoring.",
    9,13,4,
    (-1,-3,4,4),(1,2,3,3),(0,0,2,-1),(2,2,-3,-4),
    (15,"Cancellation leaves 800 hoarding operators without notice."),(17,"Audit finds 60% of hoardings structurally non-compliant."),(20,"Safety committee becomes industry lobby platform."),(22,"Second hoarding falls before committee reports."),
    (-2,0,-2,-3),(0,2,-3,-3),(0,0,-2,-3),(0,2,-3,-4),
    "Mass cancellation signals regulatory seriousness.","Audit data enables targeted enforcement.","Committee delay allows dangerous hoardings to stay up.","Second fatality creates severe political damage.",
))

items.append(gov(
    "gov_mh_beed_water_mafia","governance_integrity","Water tanker mafia in Beed districts exposed",
    "An RTI activist exposes a cartel of tanker operators in Beed who control dry-season water supply and have links to the ruling coalition.",
    1.0,
    "Break the cartel by opening competitive tenders, arrest the ringleaders, and set up a monitoring cell.",
    "Fast-track government tube-well installation in the 20 most affected villages to reduce tanker dependency.",
    "Ask the district administration to investigate and report within 30 days.",
    "Deny cartel existence, say tanker rates are market-driven, and question RTI activist's credentials.",
    9,13,3,
    (-1,-5,4,4),(1,2,3,4),(0,0,2,-1),(3,4,-4,-5),
    (16,"Arrested ringleaders have documented party membership."),(19,"Tube-well drilling delayed by budget hold."),(22,"Administration report exonerates operators."),(26,"RTI activist files PIL; HC takes note."),
    (-2,0,-3,-3),(0,2,-3,-3),(0,0,-2,-3),(0,4,-5,-5),
    "Open tender reduces tanker rates for some villages.","Tube wells provide supply in pilot villages.","Exoneration report fuels activist-led litigation.","PIL gives issue national platform.",
))

items.append(gov(
    "gov_mh_english_medium_school_fee","education_delivery","Private English medium school fee hike outrages parents",
    "Pune and Nashik private schools hike fees 25–40% citing infrastructure costs; parents demand state fee regulation.",
    0.9,
    "Invoke Maharashtra Educational Institutions Act fee cap provisions and issue show-cause notices to violating schools.",
    "Announce a state scholarship scheme for income-below-₹5 lakh families in private schools.",
    "Set up a fee regulation authority with parental representation to review hike applications.",
    "Say fee regulation harms school quality and urge parents to use public schools instead.",
    8,12,3,
    (-1,-2,3,4),(1,1,2,4),(0,0,1,-1),(2,2,-3,-4),
    (14,"Schools challenge cap in Bombay HC."),(16,"Scholarship application portal crashes."),(19,"Regulation authority seen as dominated by school trustees."),(21,"Opposition accuses state of protecting school lobby."),
    (-1,0,-2,-2),(0,1,-2,-2),(0,0,-2,-3),(0,2,-3,-3),
    "Fee cap notices deter the most egregious hike cases.","Scholarship announcement is well received by parents.","Authority perceived as slow and industry-captured.","Media frames state response as inadequate.",
))

items.append(gov(
    "gov_mh_forest_land_tribal_rights","land_rights","Forest land conflict over tribal rights in Gadchiroli",
    "Tribal communities in Gadchiroli protest that forest department officials deny them PESA rights on community land.",
    1.0,
    "Issue a state order enforcing PESA gram sabha forest rights and suspend officials who obstructed claims.",
    "Open land titling camps in all forest-boundary villages and process pending claims within 60 days.",
    "Refer the matter to a state tribal welfare committee to review and propose corrective action.",
    "Say forest regulations override PESA in disputed areas and urge tribals to file formal claims.",
    9,13,4,
    (-2,-4,4,4),(1,2,3,4),(0,0,2,-1),(2,3,-4,-5),
    (16,"Forest department files counter-affidavit in HC."),(19,"Titling camp processing too slow; backlogs grow."),(22,"Committee recommends status quo with minor tweaks."),(26,"Maoist groups exploit tribal grievance for mobilisation."),
    (-2,0,-3,-3),(0,2,-3,-3),(0,0,-2,-3),(0,3,-4,-5),
    "PESA order reduces confrontations in 12 villages.","Titling camps process 3,000 claims in first month.","Committee report unsatisfactory; rights groups protest.","Maoist mobilisation complicates security situation.",
))

items.append(gov(
    "gov_mh_cooperative_sugar_losses","finance_governance","Cooperative sugar mills post losses; workers unpaid",
    "State-linked cooperative sugar mills in Western Maharashtra post losses for the third consecutive year; 10,000 workers receive partial wages.",
    1.0,
    "Order an independent management audit, replace mill boards with administrators, and publish loss accounts.",
    "Provide a state restructuring loan to mills that commit to a three-year turnaround plan.",
    "Set up a sugar sector reform committee with industry, worker, and government representation.",
    "Attribute losses to global sugar price volatility and request Central assistance for mill stabilisation.",
    9,13,4,
    (-1,-4,4,4),(1,2,3,4),(0,0,2,-1),(2,3,-3,-4),
    (16,"Audit finds funds routed to linked entities."),(19,"Loan conditions not met; mills fail to recover."),(22,"Reform committee dominated by same cooperative leadership."),(24,"Centre refuses assistance; losses deepen."),
    (-2,0,-3,-3),(0,2,-3,-3),(0,0,-2,-3),(0,2,-3,-4),
    "Management change improves operational discipline.","Restructuring loan provides short-term relief to workers.","Reform committee recommendations too incremental.","Centre refusal forces state to take full responsibility.",
))

items.append(gov(
    "gov_mh_hawkers_eviction_mumbai","urban_poverty","BMC hawker eviction drive angers informal traders",
    "The BMC removes 5,000 unauthorised hawkers from South Mumbai footpaths without providing alternative vending zones.",
    0.9,
    "Pause evictions, demarcate formal vending zones per the NSRVA, and issue hawkers with temporary licences.",
    "Announce relocation assistance and help hawkers register under the new National Street Vendor policy.",
    "Set up a hawkers' committee to recommend vending zone locations within 30 days.",
    "Support BMC's drive as essential to pedestrian safety and accuse hawkers of flouting civic law.",
    8,12,3,
    (-1,-2,3,4),(1,2,2,3),(0,0,1,-1),(2,2,-3,-4),
    (14,"Vending zone demarcation delayed by municipal elections."),(17,"Relocation assistance delayed; hawkers return to old spots."),(20,"Committee influenced by property lobby."),(22,"Hawker union organises dharnas blocking major intersections."),
    (-1,0,-2,-2),(0,1,-2,-2),(0,0,-2,-3),(0,2,-3,-4),
    "Vending zone clarity reduces conflict with BMC.","Registration drive provides legal protection for many.","Committee delay leaves hawkers in legal limbo.","Dharnas disrupt business districts and draw media.",
))

items.append(gov(
    "gov_mh_paddy_procurement_konkan","farmer_welfare","Paddy procurement failure in Konkan",
    "Government paddy procurement centres in Raigad and Ratnagiri fail to open on time, pushing farmers to distress sell to traders at 40% below MSP.",
    1.0,
    "Fast-track centre openings, appoint state-level nodal officers, and give a seven-day ultimatum to district collectors.",
    "Buy paddy directly through HAFED as a bridge measure and pay difference to farmers who already sold at lower prices.",
    "Ask the agriculture department to investigate delay and submit a report within 10 days.",
    "Say the delay is administrative and urge farmers to wait for centres to open within the week.",
    9,13,4,
    (-2,-3,4,5),(1,1,3,5),(0,0,2,-1),(2,3,-4,-5),
    (18,"Nodal officers cite staff shortage; centres still delayed."),(20,"HAFED procurement excludes tenant farmers."),(22,"Agriculture report blames district collectors who blame state."),(26,"Farmers dump paddy outside collector's office."),
    (-2,0,-3,-3),(0,2,-3,-4),(0,0,-2,-3),(0,3,-5,-5),
    "Nodal officers accelerate centre openings in most blocks.","HAFED procurement reduces distress for registered farmers.","Blame-passing report triggers political controversy.","Paddy dump protest generates national coverage.",
))

items.append(gov(
    "gov_mh_police_land_grab_thane","governance_integrity","Police officer land grab scandal in Thane",
    "A senior IPS officer is accused of using his position to acquire prime agricultural land in Thane at sub-market rates.",
    1.0,
    "Initiate ACB inquiry, suspend the officer pending probe, and publish the land transaction records.",
    "Transfer the officer immediately and commission a district collector-led land review in Thane.",
    "Ask the DGP to conduct an internal departmental inquiry and report within 21 days.",
    "Say the acquisition is legally registered and call allegations a personal vendetta.",
    9,13,3,
    (-1,-5,4,4),(1,2,3,3),(0,0,2,-1),(3,4,-4,-5),
    (15,"ACB inquiry names a minister's relative as intermediary."),(18,"Transfer does not include suspension; appears cosmetic."),(21,"Internal inquiry clears officer; civil society erupts."),(25,"Press publishes land registry extracts with undervalued prices."),
    (-2,0,-3,-3),(0,1,-2,-2),(0,0,-3,-4),(0,4,-5,-5),
    "ACB inquiry signals anti-corruption stance.","Transfer limits officer's access but does not resolve issue.","Internal clearance triggers demand for independent probe.","Registry extracts drive viral spread of scandal.",
))

items.append(gov(
    "gov_mh_heatwave_vidarbha_2003","disaster_readiness","Heatwave kills over 100 in Vidarbha",
    "April–May 2003 heatwave deaths top 100 across Akola, Amravati, and Yavatmal; inadequate ORS distribution at PHCs blamed.",
    1.1,
    "Deploy emergency health teams to all 30 worst-hit talukas, establish cooling centres, and provide ORS and electrolytes.",
    "Release ₹50 crore for emergency health infrastructure, air-conditioning for PHCs, and tanker water supply.",
    "Form a heatwave crisis committee and publish an action plan within five days.",
    "Attribute deaths to pre-existing conditions and say the state health system responded within its capacity.",
    10,14,4,
    (-2,-3,5,5),(1,2,4,5),(0,0,2,-1),(2,3,-5,-5),
    (16,"PHC teams overwhelmed; additional deaths occur."),(20,"Cooling centres only in taluka headquarters; rural areas uncovered."),(23,"Committee action plan arrives too late in the season."),(28,"National media runs '100 dead in Maharashtra' headline."),
    (-2,0,-3,-4),(0,2,-3,-4),(0,0,-2,-3),(0,3,-5,-5),
    "Health team deployment reduces mortality in covered areas.","Emergency fund reaches most districts within a week.","Committee plan published after peak heatwave passes.","National headline drives opposition demand for accountability.",
))

items.append(gov(
    "gov_mh_sez_land_protest_2004","land_rights","SEZ land protest erupts in Raigad",
    "Farmers in Raigad protest forced land acquisition for a Special Economic Zone, burning notices and blocking state highway.",
    1.1,
    "Halt acquisition, publish social impact assessment, and conduct gram sabha consultations before proceeding.",
    "Offer land-for-land compensation and a 25% equity stake in the SEZ for displaced families.",
    "Appoint a divisional commissioner to conduct fresh hearings and file a revised compensation report.",
    "Defend acquisition as lawful under the 1894 Act and deploy police to maintain highway access.",
    10,13,4,
    (-2,-3,5,5),(1,2,4,5),(0,0,2,-1),(2,3,-4,-5),
    (17,"Gram sabha votes to reject the SEZ unanimously."),(19,"Land-for-land parcels found to be waterlogged."),(22,"Commissioner hearings become a platform for opposition leaders."),(26,"Police crackdown injures three farmers; coverage intensifies."),
    (-2,0,-3,-4),(0,2,-3,-4),(0,0,-2,-3),(0,3,-5,-5),
    "Gram sabha process gives farmers formal voice.","Land-for-land offer accepted by some displaced families.","Hearings delay project; investor confidence falls.","Crackdown images dominate evening news for three days.",
))

items.append(gov(
    "gov_mh_mid_day_meal_quality_pune","education_delivery","Mid-day meal quality scandal in Pune district",
    "Students at 12 government primary schools in Pune report falling ill after mid-day meals; supplier is linked to a local ruling party leader.",
    1.0,
    "Terminate the supplier contract, initiate a food safety investigation, and deploy district nutrition officers for daily inspection.",
    "Announce emergency kitchen upgrades and introduce centralised cooking from self-help groups.",
    "Set up a district meal quality committee and suspend the scheme pending review.",
    "Call illness reports isolated and defend the supplier's past performance record.",
    9,13,4,
    (-1,-4,5,4),(1,2,4,4),(0,0,1,-2),(3,4,-5,-5),
    (16,"Investigation finds supplier link to party district chief."),(19,"SHG cooking plagued by logistical delays."),(22,"Scheme suspension leaves children without a meal."),(25,"Parent groups file complaint with food safety authority."),
    (-2,0,-3,-3),(0,2,-3,-3),(0,0,-3,-4),(0,4,-5,-5),
    "Termination and inspections restore parental trust.","SHG cooking improves meal hygiene after initial hiccups.","Scheme suspension draws child welfare organisation criticism.","FSSAI complaint triggers external scrutiny.",
))

items.append(gov(
    "gov_mh_press_freedom_raid","governance_integrity","Police raid on Marathi newspaper office in Kolhapur",
    "Police conduct a pre-dawn raid on a Kolhapur Marathi daily that published an expose on a minister; journalists allege harassment.",
    1.0,
    "Order an immediate inquiry into the raid's legality, suspend the senior officer who ordered it, and meet the editor.",
    "Offer government legal aid to any journalist facing state action for bona fide reporting.",
    "Ask the home secretary to review the raid procedure and submit a report within a week.",
    "Defend the raid as routine follow-up on an ongoing defamation complaint and stand by the police action.",
    9,12,3,
    (-2,-4,5,4),(1,1,4,3),(0,0,2,-1),(3,4,-5,-5),
    (15,"Inquiry reveals the raid was ordered by a minister's PA."),(17,"Legal aid offer rejected by journalist as inadequate."),(21,"Home secretary report defends raid; press clubs stage walkout."),(26,"International press freedom bodies issue statements."),
    (-2,0,-3,-3),(0,1,-3,-3),(0,0,-3,-4),(0,4,-5,-5),
    "Inquiry order signals government is taking issue seriously.","Legal aid offer partially restores journalist confidence.","Press club walkout escalates to editorial boycott.","International attention increases reputational cost.",
))

items.append(gov(
    "gov_mh_kolhapur_flood_dam_safety","disaster_readiness","Kolhapur floods due to dam spillway delay",
    "Delayed opening of Radhanagari dam spillways floods several downstream villages; villagers accuse authorities of warning failure.",
    1.1,
    "Order an inquiry into the delay, compensate all affected families, and publish dam discharge protocols.",
    "Release ₹100 crore for immediate flood relief and announce a dam safety audit across all major Maharashtra dams.",
    "Set up a dam safety committee and schedule village-level warning protocol consultations.",
    "Attribute flooding to unprecedented rainfall and defend dam authority's action as within safety guidelines.",
    10,14,4,
    (-2,-3,5,5),(1,2,4,5),(0,0,2,-1),(2,3,-4,-5),
    (16,"Inquiry confirms delayed order by collector's office."),(19,"Relief funds released but disbursement slow."),(22,"Safety committee recommendations delayed past monsoon."),(26,"Audit reveals three more dams with inadequate spillways."),
    (-2,0,-3,-4),(0,2,-3,-4),(0,0,-2,-3),(0,3,-5,-5),
    "Inquiry triggers procedural reform in dam management.","Relief funds reach most families within two weeks.","Committee report arrives after flood season ends.","Audit findings drive opposition demand for dam overhaul.",
))

items.append(gov(
    "gov_mh_adivasi_naxal_encounter","law_order","Encounter killings in Gadchiroli spark Adivasi protests",
    "Security forces kill seven in a Gadchiroli encounter; tribal groups claim four were civilians working in fields.",
    1.2,
    "Order a judicial magistrate inquiry, invite tribal community representatives to the process, and pause major operations pending findings.",
    "Announce compensation for confirmed civilian casualties and an enhanced community liaison programme.",
    "Ask the DGP to file a detailed operational report and forward it to the home secretary.",
    "Stand by the security forces' action as necessary to counter Maoist threats and reject civilian casualty claims.",
    11,14,4,
    (-2,-3,5,4),(1,1,4,4),(0,0,2,-2),(3,4,-5,-5),
    (15,"Judicial inquiry names a specific unit commander."),(18,"Compensation delayed; community distrust deepens."),(22,"DGP report clears all personnel; tribal forum protests."),(28,"National Human Rights Commission takes up the case."),
    (-2,0,-3,-3),(0,1,-3,-3),(0,0,-3,-4),(0,4,-5,-5),
    "Inquiry signals willingness to hold forces accountable.","Compensation announcement reduces immediate street anger.","Personnel clearance fuels civil society pressure.","NHRC involvement escalates national attention.",
))

items.append(gov(
    "gov_mh_mumbai_footover_bridge","infrastructure_delivery","Foot over bridge collapse fear at Mumbai CST",
    "Engineers flag a hairline crack in the main foot overbridge at CST connecting suburban platforms; closure demanded.",
    1.0,
    "Close the bridge immediately, fast-track repair with a named contractor, and provide an alternative walkway.",
    "Release emergency infrastructure funds to repair the bridge and upgrade the two oldest FOBs at CST.",
    "Commission a structural audit of all CST bridges and issue an advisory to commuters.",
    "Say the crack is minor and non-structural; keep the bridge open with enhanced monitoring.",
    9,13,4,
    (-1,-2,4,4),(1,2,3,4),(0,0,2,-1),(2,2,-4,-5),
    (15,"Repair contractor finds structural decay far worse than reported."),(18,"Alternative walkway too narrow; congestion worsens."),(21,"Audit reveals cracks in two more bridges."),(26,"Bridge collapses partially during peak hour, injuring 12."),
    (-2,0,-2,-3),(0,2,-3,-3),(0,0,-2,-3),(0,2,-5,-5),
    "Closure and repair prevents potential accident.","Emergency fund enables repair ahead of monsoon.","Audit findings trigger opposition demand for action on all bridges.","Partial collapse creates severe political and legal consequences.",
))

items.append(gov(
    "gov_mh_drought_tanker_tender_2005","governance_delivery","Drought tanker tender manipulated in Aurangabad",
    "A whistleblower reveals that Aurangabad's emergency tanker tenders were awarded to firms at 3× market rate linked to a ruling party MLA.",
    1.0,
    "Cancel the inflated contracts, reissue open tenders, and register an FIR against the MLA and officials involved.",
    "Cap tanker rates by state order and deploy government owned vehicles in the 10 worst-hit areas.",
    "Ask the district collector to review the tender process and submit findings within 15 days.",
    "Say the contracts followed due process and question the whistleblower's motivations.",
    9,13,3,
    (-1,-5,5,4),(1,2,3,4),(0,0,2,-1),(3,5,-5,-5),
    (16,"FIR implicates a minister's brother."),(19,"Government vehicles insufficient; rates remain high."),(22,"Collector review clears all contracts."),(26,"Whistleblower receives threats; media covers the intimidation."),
    (-2,0,-3,-3),(0,2,-3,-3),(0,0,-2,-3),(0,4,-5,-5),
    "Re-tendering reduces tanker costs in second season.","Government vehicles provide relief in pilot areas.","Clearance report triggers activist-led PIL.","Intimidation story damages government credibility nationally.",
))

# Remaining GOV items (shorter form, same structure)
items.append(gov("gov_mh_nanded_hospital_drug","public_service","Nanded district hospital drug stock-out","State's Nanded district hospital runs out of essential antibiotics and IV fluids for 12 days.",1.0,
    "Order emergency procurement and suspend the DMO who failed to re-order; publish drug inventory weekly.",
    "Release NRHM emergency funds to restock all district hospitals in Marathwada within 48 hours.",
    "Ask health secretary to audit drug procurement across Marathwada and report in 30 days.",
    "Attribute stock-out to a central supply chain delay and say local staff acted within their authority.",
    9,13,4,(-2,-3,5,4),(1,2,4,4),(0,0,2,-1),(2,3,-4,-4),
    (15,"Audit finds same DMO cleared inflated drug invoices previously."),(18,"Restocking delayed by procurement tender rules."),(22,"State-wide audit reveals 18 hospitals with similar gaps."),(24,"Patient death linked to drug unavailability goes viral."),
    (-2,0,-3,-3),(0,2,-3,-3),(0,0,-2,-3),(0,3,-4,-4),
    "Stock restored in covered hospitals within the week.","Emergency fund restocking reaches all Marathwada hospitals.","State-wide audit triggers opposition demand for minister's resignation.","Viral story forces CM to visit the hospital.",
))

items.append(gov("gov_mh_aurangabad_industrial_air","urban_services","Industrial air pollution sickens Aurangabad residents","MIDC industrial units near Aurangabad residential areas emit toxic fumes; residents report respiratory illness.",0.9,
    "Issue closure notices to non-compliant MIDC units and enforce MPCB stack emission norms with daily monitoring.",
    "Deploy mobile MPCB units for round-the-clock monitoring and set up medical camps in affected wards.",
    "Constitute a district pollution monitoring committee to file monthly reports.",
    "Defend MIDC as key to employment and say emission standards are within permissible limits.",
    8,12,3,(-1,-3,4,3),(1,2,3,3),(0,0,1,-1),(2,3,-3,-4),
    (14,"Closed units challenge MPCB notice in HC."),(16,"Mobile units too few; monitoring patchy."),(19,"Monthly committee reports show no improvement."),(22,"MPCB data shows consistent limit breaches."),
    (-1,0,-2,-2),(0,1,-2,-2),(0,0,-2,-3),(0,3,-3,-4),
    "Closure notices drive compliance in 5 of 12 units.","Medical camps reduce immediate illness burden.","Monthly reports fail to trigger enforcement.","MPCB data confirms residents' health claims.",
))

items.append(gov("gov_mh_kolhapur_leather_effluent","environment_governance","Kolhapur leather tanneries pollute Panchganga river","Tannery effluent dumps have turned the Panchganga river black; fishing communities report zero catch for two months.",0.9,
    "Issue mandatory effluent treatment plant compliance orders, seal three worst-polluting units, and restore fishing compensation.",
    "Release state funds to build a common ETP for small tanneries and provide fishing family relief.",
    "Constitute a Panchganga revival committee with NGO, government, and industry representation.",
    "Say effluent levels are within limits and attribute zero-catch to seasonal fish migration patterns.",
    8,12,3,(-1,-3,4,3),(1,2,3,3),(0,0,1,-1),(2,3,-3,-4),
    (14,"Sealed units challenge in HC."),(16,"Common ETP procurement delayed by tender."),(19,"Committee sees no enforcement action in first three months."),(21,"National Green Tribunal issues suo motu notice."),
    (-1,0,-2,-2),(0,1,-2,-2),(0,0,-2,-3),(0,3,-3,-4),
    "Compliance orders restore partial river health.","Common ETP pilot starts in second month.","NGT notice forces executive action.","Fishing community partial relief provided.",
))

items.append(gov("gov_mh_bus_accident_solapur","transport_services","Solapur bus accident kills 14 on NH9","An overloaded ST bus loses brake control on NH9; 14 die and 20 are injured. Mechanical failure suspected.",1.1,
    "Suspend the route operator licence, initiate CID probe, and mandate fitness re-checks for all ST fleet.",
    "Announce ₹10 lakh compensation to each deceased family and fast-track vehicle fitness regulation.",
    "Form a road safety commission to audit ST buses and submit recommendations in 45 days.",
    "Call it a tragic accident, pay ex-gratia, and say ST buses meet regulatory standards.",
    10,14,4,(-2,-2,5,4),(1,1,4,4),(0,0,2,-1),(2,2,-3,-4),
    (16,"CID probe finds bus had failed fitness check six months prior."),(19,"Compensation disbursement delayed three months."),(22,"Commission audit finds 30% of ST fleet overdue for fitness check."),(26,"Second fatal ST accident occurs before audit completes."),
    (-2,0,-3,-3),(0,1,-3,-3),(0,0,-2,-3),(0,2,-4,-4),
    "Fitness re-checks remove unsafe buses from routes.","Compensation reaches most families within a month.","Commission audit reveals systemic maintenance gap.","Second accident creates severe political pressure.",
))

items.append(gov("gov_mh_nagpur_zero_hour_encroachment","governance_integrity","Nagpur city encroachment on NMC water body land","A real estate developer encroaches on a Nagpur municipal water body buffer zone with apparent official complicity.",0.9,
    "Order NMC to demolish the encroachment, prosecute the developer, and publish the approving official's name.",
    "Release emergency funds for alternate water body protection infrastructure.",
    "Refer the matter to the NMC general body and await resolution in the next council meeting.",
    "Say the encroachment is under legal review and urge affected residents to file individual objections.",
    8,12,3,(-1,-4,4,3),(1,1,2,2),(0,0,1,-1),(3,3,-3,-4),
    (15,"Developer reveals planning permission signed by a minister's office."),(17,"NMC fund misused; encroachment grows."),(19,"Council meeting deferred twice."),(22,"Green tribunal takes notice of water body destruction."),
    (-2,0,-3,-3),(0,1,-2,-2),(0,0,-2,-3),(0,3,-4,-4),
    "Demolition order signals rule of law.","Water body protection funds approved by NMC.","Council deferral fuels perception of collusion.","NGT notice creates legal obligation to act.",
))

items.append(gov("gov_mh_mumbai_dabbawalas_tax","transport_services","Mumbai dabbawalas seek tax exemption for delivery service","60,000 dabbawalas petition the state to exempt their service from entry tax and provide regulated market access.",0.8,
    "Grant the tax exemption and create a formal licensing framework recognising dabbawalas as an essential service.",
    "Provide a one-time support grant to the dabbawala cooperative and fast-track their entry-tax exemption.",
    "Refer the exemption request to the finance department for assessment and respond within 60 days.",
    "Say tax decisions must follow uniform policy and urge dabbawalas to apply through existing industry channels.",
    8,11,3,(-1,-1,3,3),(1,1,2,3),(0,0,1,-1),(1,2,-2,-3),
    (13,"Finance ministry argues it creates a precedent."),(15,"Grant amount found inadequate by cooperative."),(18,"Finance assessment delayed by bureaucratic backlog."),(20,"Dabbawalas threaten a one-day work stoppage."),
    (-1,0,-1,-1),(0,1,-2,-2),(0,0,-1,-2),(0,1,-2,-3),
    "Exemption boosts dabbawala cooperative's income.","Grant helps but core tax issue remains unresolved.","Finance delay frustrates cooperative leadership.","Work stoppage disrupts corporate office catering.",
))

items.append(gov("gov_mh_pension_delay_teachers","welfare_delivery","Retired state teachers' pension arrears go unpaid","Over 40,000 retired government teachers haven't received their enhanced pension under the Sixth Pay Commission for 18 months.",0.9,
    "Release all arrears within 30 days, penalise the finance official responsible for the delay, and automate future pension payments.",
    "Issue an immediate advance of six months' arrear and commit to clearing the rest within three months.",
    "Ask the finance department to audit pension files and clear verified cases on a rolling basis.",
    "Attribute delay to data migration issues and assure pensioners the process is moving forward.",
    8,12,3,(-1,-2,4,4),(1,1,3,4),(0,0,2,-1),(2,2,-3,-4),
    (14,"Finance official reveals delay caused by political hold on fund release."),(17,"Three-month commitment not met."),(20,"Audit reveals incorrect records for 8,000 teachers."),(23,"Pensioner association holds dharna at finance ministry."),
    (-1,0,-2,-2),(0,1,-2,-2),(0,0,-2,-3),(0,2,-3,-4),
    "Arrear release restores confidence among retired teachers.","Six-month advance provides immediate financial relief.","Audit process resolves 60% of verified claims.","Dharna creates political pressure for ministerial response.",
))

items.append(gov("gov_mh_mumbai_potable_water_2004","public_service","Mumbai water supply contamination scare in Kurla","Water supply tests in Kurla show elevated coliform bacteria after pipeline repair; children fall ill in three school batches.",1.0,
    "Shut the contaminated pipe section, run emergency tankers, and publish area-specific test results publicly.",
    "Deploy MCGM mobile water purification units and distribute water purification tablets to all affected households.",
    "Issue a boil-water advisory for the ward and schedule re-testing in 72 hours.",
    "Say contamination is minor and within WHO limits; attribute illness to other causes.",
    9,12,4,(-2,-2,4,4),(1,2,3,4),(0,0,2,-1),(2,2,-3,-4),
    (15,"Pipe closure reveals aged infrastructure needing full replacement."),(17,"Purification unit malfunction delays water supply."),(20,"Re-test confirms higher contamination than initially admitted."),(23,"Parent-teacher body files complaint with FSSAI and BMC."),
    (-2,0,-2,-3),(0,2,-3,-3),(0,0,-2,-3),(0,2,-3,-4),
    "Pipe shutdown and tankers restore clean supply.","Purification tablets reduce illness burden in the ward.","Re-test honesty earns moderate public credit.","Parent complaint triggers external municipal audit.",
))

items.append(gov("gov_mh_labour_contractor_abuse_thane","labor_welfare","Contract labour abuse at Thane industrial estate","Workers at a Thane MIDC unit allege unpaid overtime, no ESI registration, and physical intimidation by supervisors.",0.9,
    "Order a surprise labour inspection, suspend the contractor's licence, and register cases under CLRA Act.",
    "Release emergency welfare support for the affected workers through the labour commissioner.",
    "Set up a district labour grievance cell and invite workers to file complaints under protection.",
    "Say the labour department has the matter under routine scrutiny and urge workers to use legal channels.",
    8,12,3,(-1,-3,4,3),(1,1,3,3),(0,0,2,-1),(2,3,-3,-4),
    (14,"Inspection finds contractor is a relative of local ruling party leader."),(17,"Welfare support delayed by fund release bottleneck."),(20,"Grievance cell receives 200 complaints but no action for two months."),(22,"NHRC takes cognisance of intimidation allegations."),
    (-1,0,-3,-3),(0,1,-2,-2),(0,0,-2,-3),(0,3,-3,-4),
    "Licence suspension deters contractor abuse in the estate.","Welfare support reaches most workers within 10 days.","Grievance cell backlog eventually cleared after political pressure.","NHRC scrutiny escalates accountability.",
))

items.append(gov("gov_mh_election_code_violation_2004","governance_integrity","Model Code of Conduct violations during 2004 state elections","The opposition accuses the ruling party of using state resources for campaign rallies in the run-up to the 2004 state assembly elections.",0.9,
    "Issue internal directives stopping misuse of government vehicles and publish a compliance declaration.",
    "Offer to submit all party event expenses to an independent election observer for audit.",
    "Ask the chief minister's office to review individual complaints and respond to the Election Commission.",
    "Reject allegations as motivated and say all activities were lawful party functions, not state-funded.",
    8,11,3,(-1,-3,3,3),(1,1,2,3),(0,0,1,-1),(2,3,-3,-4),
    (13,"Election Commission finds three specific violations."),(15,"Observer audit reveals minor but documented misuse."),(18,"CM office response inadequate; EC sends further notice."),(20,"Opposition files formal EC complaint with photographic evidence."),
    (-1,0,-2,-2),(0,1,-2,-2),(0,0,-1,-2),(0,3,-3,-4),
    "Internal directive reduces visible misuse in final campaign phase.","Independent audit creates accountability signal.","EC notice forces more detailed government response.","Photo evidence compels EC to issue formal show-cause.",
))

items.append(gov("gov_mh_2005_mumbai_floods_response","disaster_readiness","26 July 2005 Mumbai floods — state response criticised","944 mm of rain in 24 hours floods Mumbai; the government is criticised for inadequate NDRF pre-positioning and Mithi river encroachment.",1.2,
    "Immediately deploy NDRF, pre-position Coast Guard boats, and publish the Mithi river encroachment removal schedule.",
    "Release ₹500 crore disaster relief fund, activate all district collectors, and open relief camps in every ward.",
    "Constitute a high-level flood management committee and issue a 100-day action plan.",
    "Describe the event as a once-in-a-century natural disaster and say the government responded as fast as possible.",
    12,16,5,(-2,-2,5,5),(1,2,5,5),(0,0,2,-1),(2,2,-4,-5),
    (17,"Encroachment removal exposes government approval for the same encroachments."),(20,"Relief camp conditions criticised as unsanitary."),(24,"Action plan plagiarised from an earlier unused disaster report."),(30,"Mithi river encroachment map implicates state-linked developers."),
    (-2,0,-4,-4),(0,2,-3,-3),(0,0,-3,-4),(0,3,-5,-5),
    "NDRF deployment saves hundreds in low-lying areas.","Relief fund activation prevents secondary casualties.","Action plan taken seriously by urban planners.","Encroachment map drives sustained investigative coverage.",
))

items.append(gov("gov_mh_warkari_yatra_logistics","social_cohesion","Warkari pilgrimage logistics failure in Pandharpur","Crowd management at the Ashadhi Ekadashi Warkari yatra fails; two pilgrims die in a stampede near Vitthal temple.",1.0,
    "Order an inquiry, compensate families, and appoint a crowd management consultant for the next Kartiki yatra.",
    "Deploy additional state police, medical teams, and install new crowd-flow barriers before the next yatra.",
    "Set up a temple trust-government joint committee on pilgrimage logistics.",
    "Call the deaths tragic but part of the inherent risk of mass religious gatherings.",
    9,13,4,(-2,-2,5,4),(1,1,4,4),(0,0,2,-1),(2,2,-3,-4),
    (15,"Inquiry reveals police deployment was 40% below recommended."),(17,"Next yatra sees minor incidents despite barriers."),(20,"Joint committee fails to meet before the Kartiki deadline."),(23,"Opposition holds a candlelight vigil at Pandharpur."),
    (-2,0,-3,-3),(0,1,-3,-3),(0,0,-2,-3),(0,2,-4,-4),
    "Crowd management improvements visible at Kartiki yatra.","Medical teams reduce response time for heat-related cases.","Joint committee failure leaves systemic gap unresolved.","Vigil keeps pilgrimage safety in media spotlight.",
))

items.append(gov("gov_mh_rural_road_pm_gram","infrastructure_delivery","PMGSY rural roads poor quality in Osmanabad","Newly built PMGSY roads in Osmanabad crater in first monsoon; local engineers allege sub-standard material use.",0.9,
    "Invoke warranty clauses, blacklist the contractor, and commission an independent material quality audit.",
    "Release emergency funds to repair the worst 30-km stretch before the next monsoon.",
    "Refer the matter to the state PMGSY nodal officer and await a technical report.",
    "Attribute road damage to monsoon flooding beyond design specification.",
    8,12,3,(-1,-3,4,3),(1,1,3,3),(0,0,1,-1),(2,2,-3,-3),
    (14,"Blacklisted contractor re-bids under a sister firm."),(16,"Emergency repair funds used on different district."),(18,"Nodal officer report clears the contractor."),(20,"Opposition MLA photographs craters and posts to media."),
    (-1,0,-2,-2),(0,1,-2,-2),(0,0,-2,-3),(0,2,-3,-3),
    "Blacklisting deters same contractor in the district.","Emergency repair restores connectivity for two seasons.","Nodal officer clearance triggers RTI demand for test data.","Opposition photos drive district collector inspection.",
))

items.append(gov("gov_mh_rural_health_centre_absenteeism","public_service","PHC doctors absent in Palghar tribal areas","Primary health centres in Palghar's tribal belt report 70% doctor absenteeism; tribal children face untreated malnutrition.",1.0,
    "Deploy surprise health department inspectors, dock absentee pay, and create a performance-linked posting incentive.",
    "Announce tribal area posting bonus and accelerate MBBS student rural internship placements.",
    "Ask DPHMO to file a district-level attendance report and propose corrective measures in 30 days.",
    "Attribute absenteeism to lack of residential facilities and promise a new PHC quarters project.",
    9,13,4,(-2,-3,4,4),(1,2,3,4),(0,0,2,-1),(2,2,-3,-4),
    (15,"Inspections reveal some doctors posted in urban hospitals without orders."),(17,"Posting bonus delayed six months by finance department."),(20,"DPHMO report admits the problem but recommends only awareness training."),(23,"NGO documents three child deaths linked to absent PHC staff."),
    (-2,0,-3,-3),(0,2,-3,-3),(0,0,-2,-3),(0,2,-4,-4),
    "Surprise inspections improve attendance in 40% of PHCs.","Tribal bonus attracts six voluntary postings in first month.","DPHMO recommendation seen as inadequate response.","Child death documentation drives national NGO attention.",
))

items.append(gov("gov_mh_vidarbha_power_agri_feeder","public_service","Agricultural power feeder cuts destroy Vidarbha crops","Eight-hour daily agricultural feeder cuts mean Vidarbha farmers cannot pump irrigation at critical crop stages.",1.1,
    "Order MSEDCL to designate and protect agricultural feeders from load-shedding and publish feeder schedules.",
    "Announce a ₹100 crore scheme for solar pump installation to reduce farmer dependence on grid power.",
    "Set up a MSEDCL farmer interface committee to design a load-shedding calendar.",
    "Attribute cuts to state-wide power deficit and urge farmers to shift to less water-intensive crops.",
    10,14,4,(-2,-3,4,5),(1,2,3,5),(0,0,2,-1),(2,3,-4,-5),
    (18,"MSEDCL feeder designation bypassed within two weeks."),(20,"Solar scheme procurement delayed by tender process."),(23,"Calendar committee dominated by MSEDCL engineers."),(27,"Cotton crop losses trigger farmer march to Nagpur."),
    (-2,0,-3,-4),(0,2,-3,-4),(0,0,-2,-3),(0,3,-5,-5),
    "Feeder protection reduces pump disruption in monsoon season.","Solar pumps installed in 200 villages in first year.","Calendar consultations improve communication but not supply.","Crop loss march pressures CM to announce fresh relief.",
))

items.append(gov("gov_mh_solapur_weaver_credit","artisan_welfare","Solapur powerloom weavers face credit crunch","Powerloom weavers in Solapur cannot access working capital after nationalised banks tighten credit norms; units close.",0.9,
    "Set up a special credit facilitation window through MSME DFCs and waive processing fees for weaver cooperatives.",
    "Announce a ₹200 crore state weaver support fund and hold a credit camp in Solapur in 15 days.",
    "Convene a state textile board meeting with bank representatives to design a weaver credit product.",
    "Advise weavers to approach MUDRA scheme and say state cannot intervene in bank credit decisions.",
    8,12,3,(-1,-2,3,4),(1,1,3,4),(0,0,2,-1),(2,2,-3,-4),
    (14,"DFC window conditions exclude most small weavers."),(17,"Fund disbursement delayed by beneficiary verification."),(19,"Board meeting deferred by bank representatives."),(21,"Opposition holds weaver rally at Solapur collector office."),
    (-1,0,-2,-2),(0,1,-2,-2),(0,0,-2,-3),(0,2,-3,-3),
    "DFC window helps 2,000 registered weavers access credit.","Credit camp provides immediate liquidity for 500 units.","Board meeting eventually produces a weaver credit product.","Rally creates media visibility for weaver distress.",
))

items.append(gov("gov_mh_coastal_fishing_trawler_ban","coastal_welfare","Seasonal trawler ban leaves coastal fishing families with no income","The mandatory monsoon trawler ban leaves 80,000 coastal fishing families without income; promised compensation not released.",1.0,
    "Release compensation arrears within 14 days and automate future ban-period payments through direct bank transfer.",
    "Announce an emergency livelihood support scheme providing alternative employment to fishing families during ban.",
    "Ask fisheries department to audit compensation disbursement and file a report in 30 days.",
    "Say compensation was released on time and ask fishers to approach talathi offices with missing payment complaints.",
    9,13,4,(-1,-2,4,4),(1,2,3,4),(0,0,2,-1),(2,2,-3,-4),
    (15,"Audit finds compensation routed through middlemen."),(18,"Alternative employment scheme takes 40 days to operationalise."),(21,"Fisheries report admits 60% non-disbursement."),(23,"Fisher cooperatives block port access in Ratnagiri."),
    (-1,0,-2,-2),(0,2,-3,-3),(0,0,-2,-3),(0,2,-3,-4),
    "Arrear release reaches 70% of registered fishers.","Alternative livelihood supports 10,000 families through ban.","Fisheries report admission forces faster corrective action.","Port blockade disrupts fish supply and draws media.",
))

items.append(gov("gov_mh_aurangabad_heritage_demolition","culture_education","Illegal demolition near Aurangabad heritage site","A contractor demolishes a 17th-century stepwell near Aurangabad without Archaeological Survey of India clearance.",0.8,
    "Halt all nearby construction, register FIR against contractor and approving officer, and notify ASI for assessment.",
    "Announce a state heritage protection fund and fast-track an alternative development route around the site.",
    "Refer the matter to ASI and await its heritage impact assessment before any further action.",
    "Say the structure was a minor listed site and that the damage does not compromise the major monuments.",
    7,11,3,(-1,-3,4,3),(1,1,3,2),(0,0,2,-1),(2,2,-3,-3),
    (13,"FIR names a local ruling party member as contractor."),(15,"Protection fund procurement faces tender delay."),(17,"ASI assessment takes six months; construction continues nearby."),(19,"UNESCO flags the site as at risk."),
    (-1,0,-2,-2),(0,1,-2,-2),(0,0,-2,-3),(0,3,-3,-3),
    "FIR registration deters further encroachment attempts.","Heritage fund attracts state and central matching grants.","ASI assessment creates six-month legal vacuum.","UNESCO flagging draws international media attention.",
))

items.append(gov("gov_mh_monsoon_2003_shortage","farmer_welfare","Below-normal monsoon 2003 triggers crop failure","Kharif 2003 monsoon deficit of 38% across eastern Maharashtra triggers widespread crop failure; pulses and oilseed hit hardest.",1.1,
    "Declare drought in all 16 affected districts, release NDRF funds, and open crop loss assessment camps.",
    "Announce a ₹1,000 crore input subsidy package for affected farmers and open credit rescheduling windows.",
    "Set up a district-level crop loss assessment committee to file verified reports within 30 days.",
    "Say the deficit is within manageable limits and that existing welfare schemes cover affected farmers.",
    10,14,4,(-2,-2,5,5),(1,2,4,5),(0,0,2,-1),(2,3,-4,-5),
    (17,"NDRF release slow; first payment reaches 20% of districts."),(20,"Input subsidy excludes tenant farmers."),(23,"Committee verification too slow; crop season ends before payment."),(27,"Opposition publishes 300 farmer testimonies of zero compensation."),
    (-2,0,-3,-4),(0,2,-3,-4),(0,0,-2,-3),(0,3,-5,-5),
    "Drought declaration unlocks central SDRF transfers.","Input subsidy reaches 60% of registered small farmers.","Committee report eventually enables bulk disbursement.","Testimony campaign keeps drought distress in media for six weeks.",
))

items.append(gov("gov_mh_nashik_grape_export_block","farmer_welfare","Nashik grape farmers hit by EU pesticide export ban","EU authorities block Maharashtra grape imports citing pesticide residue levels above MRL; 50,000 farmer families lose export income.",1.0,
    "Convene a state-EU residue compliance task force, fund free pesticide testing camps, and negotiate a grace export window.",
    "Announce ₹500 crore to support compliance upgrades and pay compensation for the lost export season.",
    "Form an agricultural export quality review committee to propose residue-compliance norms in 60 days.",
    "Say EU standards are protectionist and urge farmers to pivot to domestic market sales.",
    10,13,4,(-2,-2,5,5),(1,1,4,5),(0,0,2,-1),(2,2,-4,-5),
    (17,"Task force reveals same pesticides approved by Govt of India."),(20,"Compliance camp reach only 20% of affected farmers."),(23,"Committee norms less stringent than EU requirement."),(27,"Second EU inspection fails; ban extended another season."),
    (-2,0,-3,-4),(0,2,-3,-4),(0,0,-2,-3),(0,2,-5,-5),
    "Task force opens dialogue; partial export window restored.","Compensation provides relief for most registered growers.","Committee norms improve but gap with EU standards remains.","Extended ban drives farmer income loss into second year.",
))

items.append(gov("gov_mh_senior_ips_transfer_row","administrative_control","IPS officer transfer row challenges home ministry","A senior IPS officer transferred after a public disagreement with a minister gives a press interview alleging political interference.",0.9,
    "Commission an independent review of transfer procedures, respond to specific allegations in writing, and meet the officer.",
    "Announce revised IPS transfer guidelines with minimum posting duration to protect service integrity.",
    "Ask the DGP to submit a report on the transfer and forward it to the home secretary for review.",
    "Defend the transfer as administrative routine and say the officer's interview is a breach of service conduct.",
    8,11,3,(-1,-2,3,3),(1,1,2,3),(0,0,1,-1),(2,3,-3,-4),
    (13,"Review confirms transfer was overriding a pending vigilance case."),(15,"Transfer guidelines challenged by IAS association as precedent."),(17,"DGP report defends all transfers; opposition holds press conference."),(19,"Interview goes viral and attracts national civil services commentary."),
    (-1,0,-2,-2),(0,1,-2,-2),(0,0,-2,-3),(0,3,-3,-4),
    "Independent review signals accountability in postings.","New guidelines earn approval from retired IPS forums.","DGP report defence seen as protecting political interests.","Viral interview drives civil society petition on service independence.",
))

items.append(gov("gov_mh_bmc_budget_misuse_2002","local_governance","BMC ward fund misuse allegations in Mumbai","Audit objections flag ward-level BMC development funds diverted from infrastructure to events and party programmes.",0.9,
    "Publish the audit objections, initiate recovery proceedings from defaulting ward officers, and hold a BMC general body session.",
    "Announce a new transparent BMC ward fund dashboard with real-time expenditure tracking.",
    "Ask the BMC commissioner to respond to audit notes and report compliance in 45 days.",
    "Say audit objections are procedural and within annual tolerance; defend ward-level discretion.",
    8,11,3,(-1,-4,4,3),(1,2,3,3),(0,0,1,-1),(2,3,-3,-4),
    (13,"Recovery proceedings reveal ward officers protected by party MLAs."),(15,"Dashboard launch delayed by IT procurement."),(18,"BMC commissioner response inadequate; audit authority escalates."),(20,"Opposition tables audit objections in state assembly."),
    (-1,0,-3,-3),(0,1,-2,-2),(0,0,-2,-3),(0,3,-3,-4),
    "Recovery proceedings deter future diversion.","Dashboard provides long-term transparency signal.","Audit authority escalation forces more substantive response.","Assembly debate draws wider attention to BMC accountability.",
))

items.append(gov("gov_mh_river_junction_project_delay","infrastructure_delivery","Krishna-Bhima river junction project stalls in Solapur","A major irrigation link project in Solapur stalls due to contractor disputes; Rabi season water availability threatened.",0.9,
    "Invoke contract penalty clauses, appoint a new project manager, and set a hard 60-day completion deadline.",
    "Release emergency funds to hire sub-contractors for the stalled sections and fast-track completion.",
    "Call a joint review meeting of WRD and contractor and issue a revised timeline within a week.",
    "Attribute delay to geological surveys and say the project is on track within revised estimates.",
    8,12,3,(-1,-3,4,3),(1,2,3,3),(0,0,2,-1),(2,2,-3,-3),
    (14,"New project manager finds cost overrun at 180% of budget."),(17,"Sub-contractor engagement delayed by procurement rules."),(19,"Revised timeline extends completion by 18 months."),(21,"Farmer organisations block WRD office demanding answers."),
    (-1,0,-2,-2),(0,1,-2,-2),(0,0,-2,-3),(0,2,-3,-3),
    "Penalty and replacement signals tougher contract management.","Sub-contractor engagement accelerates stalled section.","Revised timeline reduces public confidence in the project.","Farmer blockade forces district commissioner-level response.",
))

items.append(gov("gov_mh_maratha_reservation_demand_2004","social_cohesion","Maratha reservation demand march in Nashik","A large Maratha community march to the collectorate demands OBC reservation for the community in state jobs and education.",1.0,
    "Establish a state backward class commission to conduct an empirical survey on Maratha socio-economic conditions.",
    "Announce enhanced EWS scholarship benefits for all economically weak Marathas pending the commission's report.",
    "Schedule a multi-party assembly discussion on the reservation demand within 30 days.",
    "Say reservation decisions require constitutional process and call marchers to trust the legal pathway.",
    9,13,4,(-1,-1,3,4),(1,1,2,4),(0,0,2,-1),(2,2,-3,-3),
    (14,"Commission mandate too narrow; community leaders reject it."),(17,"EWS scholarship amounts criticised as too low."),(20,"Assembly discussion produces no concrete outcome."),(23,"Second march planned with broader community participation."),
    (-1,0,-2,-2),(0,1,-2,-2),(0,0,-1,-2),(0,2,-3,-3),
    "Commission establishment creates institutional process.","Scholarship announcement reduces immediate community frustration.","Assembly discussion keeps political dialogue open.","Second march signals community dissatisfaction with pace.",
))

items.append(gov("gov_mh_groundwater_depletion_marathwada","environment_governance","Groundwater depletion alarm in Marathwada","Official surveys show Marathwada's water table has dropped 8 metres in five years; borewells failing across 400 villages.",1.0,
    "Declare a state water conservation emergency, mandate watershed development works, and regulate borewell drilling.",
    "Release ₹400 crore for Jalyukt Shivar-style watershed projects in the 10 most affected talukas.",
    "Form a groundwater management committee and publish a district-wise water table map.",
    "Attribute depletion to low rainfall and say the state has adequate schemes already in place.",
    9,13,4,(-1,-2,4,4),(1,2,3,4),(0,0,2,-1),(2,2,-3,-4),
    (14,"Borewell regulation challenged by commercial water users."),(18,"Watershed project funds diverted in two districts."),(20,"Committee map published without a corrective action plan."),(23,"NGO water stress report contradicts official water table data."),
    (-1,0,-2,-3),(0,2,-3,-3),(0,0,-2,-3),(0,2,-3,-4),
    "Regulation reduces commercial borewell proliferation.","Watershed investment shows groundwater recharge in pilot areas.","Map publication without action plan draws civil society criticism.","NGO report triggers international donor attention to Marathwada.",
))

items.append(gov("gov_mh_housing_scheme_slum","welfare_integrity","Slum housing scheme beneficiary list manipulation in Nagpur","Beneficiary lists for a state slum housing scheme in Nagpur show names of non-slum residents linked to the ruling party.",0.9,
    "Open list for public verification online, audit every name, and initiate action against officials who approved ineligibles.",
    "Announce a fresh eligibility survey and add a fast-track process for genuine slum residents who were excluded.",
    "Ask the district housing board to verify the list and report within 30 days.",
    "Defend the list as prepared per eligibility norms and call objections politically timed.",
    8,12,3,(-1,-4,4,3),(1,2,3,3),(0,0,1,-1),(3,3,-3,-4),
    (13,"Online audit flags 1,500 non-eligible entries."),(15,"Fast-track process overwhelmed; genuine applicants wait months."),(17,"Housing board report largely clears listed names."),(19,"Opposition publishes side-by-side voter roll comparison."),
    (-1,0,-3,-3),(0,1,-2,-2),(0,0,-2,-3),(0,3,-3,-4),
    "Public audit restores credibility of housing allocation.","Fast-track process clears 800 genuine cases quickly.","Board report seen as protective of incumbents.","Voter roll comparison creates prima facie evidence of fraud.",
))

# =============================================================================
# 60 OPPOSITION / THIRD PARTY ISSUES — Maharashtra 2001-2006
# =============================================================================

items.append(opp("opp_mh_vidarbha_rally_strategy","movement_pressure","Opposition rally strategy on Vidarbha farmer crisis","Internal debate over whether to hold a mass rally at Nagpur or a series of village-level meetings on farmer distress.",1.1,
    "Organise a district-level jan samwad in each Vidarbha district, document farmer testimonies, and submit a charter to the CM.",
    "Call a large farmer solidarity rally at Nagpur's Ambedkar statue to generate national media attention.",
    "Compile verified data from 50 villages before announcing any agitation format.",
    "Accept a state agriculture department offer to jointly review farmer data in exchange for postponing agitation.",
    9,12,6,
    (-1,0,3,4),(3,0,-1,5),(0,-1,3,3),(1,3,-2,-2),
    (14,"District jan samwads reveal organisational weakness."),(18,"Rally turnout lower than expected; government mocks scale."),(12,"Data compilation delays agitation by two months."),(22,"Joint review seen as co-option by party cadre."),
    (-1,0,-2,-2),(-1,0,-3,-3),(0,0,-2,-2),(0,3,-3,-3),
    "Jan samwad builds credible ground-level evidence base.","Rally media coverage sparks national editorial discussion.","Verified data gives charge sustained credibility.","Joint review provides cover; agitation loses momentum.",
))

items.append(opp("opp_mh_fadnavis_bjp_infighting","party_organization","BJP internal power contest in Nagpur region","Two BJP factions in Nagpur are openly fighting over district body posts, weakening booth-level coordination.",0.9,
    "Convene a closed-door party mediation chaired by a senior RSS-linked leader and sign a joint district committee.",
    "Use the factional energy in competitive internal rallies to demonstrate organisational strength publicly.",
    "Survey booth-agent loyalty before taking any side in the factional dispute.",
    "Allow the wealthier faction to win district bodies in exchange for funding the upcoming municipal election.",
    8,11,5,
    (0,-1,2,3),(2,0,-1,4),(0,-1,2,2),(1,3,-2,-2),
    (13,"Mediation fails; dissenting faction contacts opposition media."),(16,"Internal rally exposes unequal mobilisation capacity."),(12,"Survey reveals stronger faction has history of booth-rigging."),(20,"Funding arrangement leaks to rival faction."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-2,-2),(0,3,-3,-3),
    "Mediation restores unity ahead of municipal elections.","Competitive rally sharpens organisational competitive drive.","Survey enables merit-based faction assessment.","Funding leak creates internal bitterness lasting months.",
))

items.append(opp("opp_mh_sena_subaltern_campaign","positive_service","Shiv Sena proposes free legal aid camps in Dadar","Party legal cell proposes free legal-aid camps for workers and tenants in central Mumbai as a service-politics initiative.",0.9,
    "Launch the camps with senior lawyer volunteers and a media-partnered beneficiary count from Day 1.",
    "Hold the camps alongside a parallel rally demanding tenant protection legislation.",
    "Survey legal needs of three wards before finalising camp locations and issue types.",
    "Accept a private law firm's offer to sponsor the camps in exchange for branding rights.",
    8,10,5,
    (0,-1,3,4),(2,0,1,3),(0,-1,3,3),(1,2,-2,-2),
    (12,"Low awareness limits initial turnout."),(16,"Rally overshadows the camp's positive message."),(11,"Survey process delays camp launch by three weeks."),(18,"Firm branding prompts corruption allegation."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-1,-1),(0,3,-2,-2),
    "Camp service builds urban working-class goodwill.","Combined rally amplifies tenant rights message.","Delayed launch costs momentum but ensures better targeting.","Sponsorship allegation undercuts the clean-politics message.",
))

items.append(opp("opp_mh_farmer_march_nashik","movement_pressure","Long march from Nashik to Mumbai planned by farm unions","Left-aligned farm unions propose a 10-day Kisan long march from Nashik to Azad Maidan to demand debt waiver and MSP.",1.2,
    "Formally endorse the march, provide logistics and medical support, and walk the final leg with senior leaders.",
    "Stage an independent solidarity rally in Mumbai to amplify coverage without formally joining the march.",
    "Independently verify marchers' demands before endorsing to avoid being associated with maximalist claims.",
    "Accept march funds from a sympathetic agro-industry donor in exchange for softening the land-reform demand.",
    10,12,7,
    (-1,-1,4,5),(2,0,2,4),(0,-1,3,3),(1,3,-3,-3),
    (15,"Marcher fatigue and police friction create negative images."),(18,"Rival rally accused of stealing march's media oxygen."),(13,"Verification delays causes march organisers to distance party."),(24,"Donor link leaked by a disgruntled faction leader."),
    (-1,0,-2,-3),(-1,0,-2,-2),(0,0,-2,-2),(0,4,-4,-4),
    "March generates statewide agricultural policy attention.","Solidarity rally produces strong visual media material.","Verified endorsement gives sustained credibility to demands.","Donor leak creates severe credibility damage for party.",
))

items.append(opp("opp_mh_candidate_criminal_pune","candidate_selection","Pune MLA aspirant has pending MCOCA case","A popular Pune municipal leader with a pending MCOCA case wants the assembly ticket; urban voters and civil society object.",0.9,
    "Deny the ticket, issue a public integrity statement, and replace with a clean candidate from the same ward.",
    "Give the aspirant the ticket and organise a massive rally to overwhelm the criminal image through crowd power.",
    "Survey independent polling in three Pune constituencies before deciding whether image cost is manageable.",
    "Allow the aspirant to fund a large portion of district election costs in exchange for the ticket.",
    8,11,5,
    (-1,-1,4,4),(2,0,-2,3),(0,-1,3,2),(1,3,-3,-3),
    (12,"Clean candidate lacks grassroots network; party loses booth support."),(16,"MCOCA case becomes election issue; media runs repeated stories."),(12,"Survey reveals MCOCA matters significantly to swing voters."),(20,"Funding arrangement implies guilt; press runs the story."),
    (-1,0,-2,-2),(-1,0,-3,-3),(0,0,-1,-1),(0,4,-4,-4),
    "Integrity signal builds urban credibility for the party.","Rally turnout impressive but case remains a liability.","Survey provides clear decision guidance for leadership.","Press story on funding arrangement damages wider ticket slate.",
))

items.append(opp("opp_mh_media_headline_misquote","media_narrative","Marathi TV channel misquotes opposition leader on Marathas","A Marathi news channel broadcasts an out-of-context clip suggesting the opposition leader opposes Maratha reservation.",0.9,
    "Issue a precise written correction within three hours and share the full video clip on all platforms.",
    "Hold an emergency press conference demanding a retraction and threatening legal action against the channel.",
    "Verify the exact broadcast context before issuing any public response.",
    "Accept a private apology from the channel editor in exchange for not pursuing a formal complaint.",
    7,10,5,
    (-1,0,3,3),(2,0,1,2),(0,-1,3,2),(1,2,-2,-2),
    (11,"Correction not carried by rival channels; damage spreads."),(14,"Press conference makes the leader look defensive."),(12,"Delay in response allows misquote to trend for 48 hours."),(18,"Private apology becomes public; appears like capitulation."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-2,-2),(0,2,-2,-2),
    "Written correction with video link restores clarity for most viewers.","Press conference generates its own media cycle.","Verification produces more precise counter-narrative.","Channel retracts but damage to Maratha relations lingers.",
))

items.append(opp("opp_mh_coalition_sena_congress_deal","coalition_management","Congress and NCP seat-sharing row ahead of 2004 elections","Congress and NCP disagree on 50 contested seats; smaller Congress allies threaten to contest independently.",0.9,
    "Broker a compromise that gives NCP 144 seats and Congress 148, with smaller allies getting 10 reserved seats.",
    "Call a joint public rally to demonstrate alliance strength and force smaller allies to fall in line.",
    "Commission a seat-wise polling analysis before finalising the split to identify winnable seats for each party.",
    "Offer smaller allies financial support for campaign expenses in exchange for withdrawing from disputed seats.",
    9,11,6,
    (-1,-1,3,3),(2,0,1,3),(0,-1,3,2),(1,2,-2,-2),
    (13,"NCP rejects the 144/148 split; negotiation restarts."),(16,"Smaller allies leak rally disagreements to press."),(12,"Polling data creates internal confidence gap between parties."),(20,"Financial offer to allies surfaces in opposition media."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-1,-1),(0,3,-3,-3),
    "Compromise allows alliance to file coordinated nominations.","Joint rally signals unity; improves alliance vote consolidation.","Data-based negotiation is more efficient and durable.","Financial arrangement creates future bargaining leverage problem.",
))

items.append(opp("opp_mh_sena_toll_protest","movement_pressure","Toll booth agitation on Mumbai-Pune Expressway","Party workers demand the government scrap expressway toll for daily commuters; toll revenue alleged to exceed project cost.","1.0",
    "Organise a one-day token toll-free drive with volunteers posting at booths and document commuter support data.",
    "Call a blockade of three expressway toll booths; demand a government audit of toll recovery versus project cost.",
    "File an RTI on toll collection receipts versus concession agreement before announcing any agitation.",
    "Accept a concessionaire's informal offer to reduce commuter rates in exchange for calling off the agitation.",
    8,11,5,
    (-1,0,3,4),(2,0,0,3),(0,-1,3,3),(1,3,-3,-3),
    (13,"Token drive blocked by Maharashtra Highway Police."),(17,"Blockade injures two police; image damage."),(12,"RTI data confirms 2× recovery; creates credible platform."),(22,"Concessionaire deal leaked; seen as selling out commuters."),
    (-1,0,-2,-2),(-1,0,-3,-3),(0,-1,2,2),(0,4,-4,-4),
    "Token drive generates commuter goodwill and media.","Blockade forces government to order audit.","RTI data produces strongest political charge.","Concessionaire deal creates credibility collapse.",
))

items.append(opp("opp_mh_bjp_dalit_outreach","social_coalition","BJP youth wing proposes Dalit colony outreach programme","Party youth wing proposes a welfare-literature distribution and ration verification drive in Nagpur's Dalit colonies.",0.9,
    "Launch the programme with Dalit community leaders as co-organisers and publish outcomes publicly.",
    "Combine the outreach with a press conference demanding state account for rising SC/ST atrocity cases.",
    "Survey local Dalit organisations' perception of the party before initiating any outreach.",
    "Accept an NGO's offer to brand the programme and provide materials in exchange for a policy concession.",
    7,10,5,
    (-1,-1,3,4),(2,0,1,3),(0,-1,3,2),(1,2,-2,-2),
    (12,"Community leaders ask why party opposed reservation before."),(15,"Press conference draws comparison to party's past record."),(11,"Survey reveals trust deficit; narrow outreach entry point."),(18,"NGO link perceived as political appropriation."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-1,-1),(0,3,-2,-2),
    "Community co-organiser model builds genuine credibility.","Press conference creates accountability pressure on state.","Survey shapes more targeted and trusted engagement.","NGO branding reduces programme's authenticity.",
))

items.append(opp("opp_mh_manifesto_farmer_debt_waiver","policy_credibility","Should opposition promise farm debt waiver in manifesto?","Party policy team debates whether a full farm debt waiver promise is fiscally credible or will invite ridicule.","1.0",
    "Publish a costed farm debt restructuring plan with independent economist endorsement, rather than a blanket waiver.",
    "Announce a ₹25,000 cr debt waiver promise at the biggest campaign rally to generate maximum farmer mobilisation.",
    "Conduct a district-level farmer debt survey to establish the actual quantum before announcing any number.",
    "Keep the debt promise vague and use it to extract donor contributions from agri-businesses.",
    9,12,6,
    (-1,-1,4,4),(3,0,-2,5),(0,-1,4,3),(1,3,-3,-3),
    (13,"Costed plan leaks; critics find accounting gap."),(18,"Waiver figure challenged as unimplementable by finance experts."),(13,"Survey reveals debt is 40% higher than media estimate."),(23,"Agri-donor link published by investigative journalist."),
    (-1,0,-2,-2),(-1,0,-3,-3),(0,0,-1,-1),(0,4,-4,-4),
    "Costed plan earns editorial credibility.","Rally announcement mobilises farmer vote but opens fiscal questions.","Survey data makes subsequent promise more credible.","Donor link damages party's anti-corruption positioning.",
))

items.append(opp("opp_mh_womens_wing_safety","positive_service","Women's wing safety kiosk programme in Pune","Party women's wing proposes 20 safety kiosks in Pune's bus stands with a complaint hotline and legal aid referral.",0.9,
    "Launch programme with women's NGOs as partners, measure complaints resolved monthly, and publish data.",
    "Hold a high-profile women's safety rally at Shivaji Nagar with senior party leaders attending.",
    "Survey women commuters in three Pune wards before finalising kiosk locations.",
    "Accept corporate sponsorship for kiosk infrastructure in exchange for company branding.",
    8,10,5,
    (-1,-1,3,4),(2,0,1,3),(0,-1,3,3),(1,2,-2,-2),
    (12,"NGO raises concern about party control over kiosk messaging."),(14,"Rally accused of being more political than safety-focused."),(11,"Survey delays programme by a month."),(17,"Corporate branding seen as commercialising safety."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-1,-1),(0,2,-2,-2),
    "NGO partnership builds genuine safety infrastructure.","Rally generates positive media visibility on women's security.","Survey improves programme targeting and community trust.","Corporate branding reduces credibility of safety claim.",
))

items.append(opp("opp_mh_rti_use_corruption_expose","scandal_strategy","RTI cell uncovers road contract inflated invoices","Party RTI cell obtains documents showing PWD road contract invoices inflated by 60% in Aurangabad district.",1.0,
    "Assign a senior leader to present verified documents at a disciplined press conference with legal backup.",
    "Hold a mass press conference immediately; flood media with the inflated invoices for maximum saturation.",
    "File RTIs for comparison invoices from three other districts before going public to build a stronger case.",
    "Use the invoice data as private leverage to extract an administrative concession from the PWD.",
    9,11,6,
    (-1,-1,4,4),(3,0,0,3),(0,-1,4,3),(1,3,-3,-2),
    (14,"Press conference undermined by government counter-document."),(17,"Media saturation fades in 48 hours without follow-through."),(12,"Comparison data strengthens the case significantly."),(21,"Private leverage attempt documented by a journalist."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,-1,2,2),(0,4,-4,-4),
    "Verified press conference produces HC PIL from civil society.","Mass saturation creates short-term media pressure.","Comparison data leads to ongoing coverage for two weeks.","Leverage story collapses party's anti-corruption credibility.",
))

items.append(opp("opp_mh_mumbai_slum_solidarity","positive_service","Opposition supports Dharavi Bachao Andolan","Rights groups invite opposition to support the Dharavi Bachao Andolan against eviction notices.",0.9,
    "Send senior party leaders to the andolan, co-author a rights petition to the HC, and document eviction cases.",
    "Stage a party-branded rally inside Dharavi to claim the issue as the party's urban housing platform.",
    "Verify the andolan's legal standing and pending court cases before formally associating.",
    "Accept a developer-linked donor's funds for the agitation in exchange for moderating the land-protection demand.",
    8,10,5,
    (-1,-1,4,4),(2,0,1,3),(0,-1,3,3),(1,3,-3,-3),
    (12,"HC petition lumped with other cases; progress slow."),(15,"Rally disrupted by BMC eviction teams same day."),(12,"Verification reveals andolan has split into two factions."),(22,"Developer link exposed by investigative journalist."),
    (-1,0,-2,-2),(-1,0,-3,-3),(0,0,-2,-2),(0,4,-4,-4),
    "Rights petition gives andolan legal legitimacy.","Rally generates TV coverage but intensifies eviction timeline.","Verification enables targeted, effective association.","Donor exposure destroys the party's housing rights credibility.",
))

items.append(opp("opp_mh_bjp_urban_local_body_strategy","party_organization","BJP strategy for Mumbai and Pune municipal elections","Party debates whether to align with Shiv Sena or contest alone in 2002 BMC and Pune municipal elections.",0.9,
    "Negotiate a formal seat-sharing pact giving BJP 45% of seats in Pune and 40% in Mumbai BMC.",
    "Contest all seats independently to build a distinct city-level identity separate from Sena.",
    "Survey BJP voter loyalty in 10 Mumbai wards to understand how much the party can win without Sena.",
    "Accept Sena's lower seat offer in exchange for Sena's financial support in all joint constituencies.",
    8,11,5,
    (-1,-1,3,3),(2,0,-1,3),(0,-1,3,2),(1,2,-2,-2),
    (13,"Sena rejects 45% offer; negotiations stall."),(16,"Independent contest splits Hindu vote; Congress gains."),(12,"Survey finds BJP at 30% unaided in sample wards."),(19,"Sena support comes with unannounced candidate-vetting conditions."),
    (-1,0,-2,-2),(-1,0,-3,-3),(0,0,-1,-1),(0,2,-2,-2),
    "Formal pact produces coordinated ward-level campaign.","Independent contest builds party's own urban identity long term.","Survey shapes realistic seat-sharing ask.","Sena conditions create future friction within alliance.",
))

items.append(opp("opp_mh_workers_welfare_camp","positive_service","Workers welfare camp near Bhiwandi textile mills","Party proposes a free ESI registration and provident fund advisory camp for unregistered Bhiwandi powerloom workers.",0.9,
    "Run the camp with EPF and ESIC officials co-present to ensure registrations are real and durable.",
    "Hold the camp alongside a street protest demanding MSEDCL lower industrial tariff for small powerloom units.",
    "Survey registration gaps among workers before camp to target the most unregistered clusters.",
    "Accept a powerloom owners' association's funding for the camp in exchange for softening the ESI demand.",
    7,10,5,
    (-1,-1,3,4),(2,0,1,3),(0,-1,3,3),(1,2,-2,-2),
    (11,"EPF officials give incomplete information; workers confused."),(14,"Protest deflects from welfare camp's positive coverage."),(11,"Survey identifies 8,000 unregistered workers; strong attendance."),(17,"Owners' funding removes the party's credibility on labour rights."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-1,-1),(0,3,-2,-2),
    "Camp creates 3,000 new ESI registrations in one day.","Combined protest amplifies labour rights message.","Survey-targeted camp achieves 80% eligible worker attendance.","Funding association weakens labour platform credibility.",
))

items.append(opp("opp_mh_ncp_sugar_cooperative_pressure","labor_outreach","NCP factions fight over cooperative sugar mill board","Two NCP factions in Kolhapur are competing for cooperative sugar mill board elections, threatening to contest publicly.",0.9,
    "Mediate between factions; negotiate a shared board slate and a clean election process.",
    "Allow the stronger faction to contest publicly and use mill board as a platform to demonstrate management competence.",
    "Audit each faction's actual cooperative membership before deciding whom to back.",
    "Allow the financially stronger faction to take the board in exchange for election funding for the party.",
    8,10,5,
    (-1,-1,2,3),(2,0,0,3),(0,-1,2,2),(1,3,-2,-2),
    (12,"Shared slate breaks down during nominations."),(15,"Contested election exposes factional bitterness to media."),(11,"Audit reveals membership irregularities in both factions."),(19,"Election funding arrangement leaked by losing faction."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-2,-2),(0,3,-3,-3),
    "Shared slate maintains party unity at board level.","Contested election produces credible management team.","Audit findings enable cleaner election process.","Funding leak creates intra-party damage heading into state elections.",
))

items.append(opp("opp_mh_media_bjp_counter_press","media_narrative","BJP calls a press conference to counter government welfare claims","Government places full-page ads claiming state welfare schemes reached 100% coverage; opposition wants a rebuttal strategy.",1.0,
    "Publish a district-by-district fact-check document with verified beneficiary shortfalls and hold a press briefing.",
    "Call a mega press conference the same day with 50 beneficiary testimonies to neutralise the ad.",
    "File RTIs for scheme-wise disbursement data in five districts before countering with facts.",
    "Accept opposition press agency funding for the counter-campaign in exchange for soft coverage conditions.",
    9,11,6,
    (-1,-1,4,4),(3,0,1,3),(0,-1,4,3),(1,2,-2,-2),
    (13,"Fact-check document not covered by mainstream Marathi media."),(17,"Beneficiary testimonies challenged as cherry-picked."),(12,"RTI data shows government ad was overstated by 35%."),(20,"Press agency funding condition surfaces in journalist exposé."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,-1,2,2),(0,3,-3,-3),
    "Fact-check document earns credibility with editorial boards.","Testimony press conference generates strong evening news cycle.","RTI data creates durable and legally backed campaign.","Agency funding exposé undermines the entire counter-campaign.",
))

items.append(opp("opp_mh_irrigation_scam_opposition","scandal_strategy","Opposition plans assembly walkout on irrigation scam","The Vidarbha irrigation scam documents are ready; debate on whether to do a walkout or a detailed assembly address.",0.9,
    "Deliver a 30-minute documented speech on the floor of the house referencing CAG figures and media-ready extracts.",
    "Organise a dramatic assembly walkout carrying farmer effigies to dominate the visual news cycle.",
    "Compile additional supporting affidavits from three CAG officers before finalising the assembly strategy.",
    "Use the irrigation documents privately to negotiate for a Joint Parliamentary Committee probe in exchange for silence.",
    8,11,5,
    (-1,-1,4,3),(2,0,1,3),(0,-1,4,2),(1,3,-3,-2),
    (12,"Government minister challenges specific CAG references in the house."),(15,"Walkout covered but framed as obstructionism."),(11,"Additional affidavits reveal two more implicated ministers."),(22,"Private negotiation leaks to investigative journalist."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,-1,2,2),(0,4,-4,-4),
    "Documented floor speech creates a Hansard record for future litigation.","Walkout visuals dominate prime-time news.","Additional affidavits extend scandal's political life.","Negotiation leak destroys opposition credibility on this issue.",
))

items.append(opp("opp_mh_flood_2005_relief_opp","positive_service","Opposition relief camp after 26/7 Mumbai floods","After 26 July 2005 floods, party workers want to run independent relief camps to build urban goodwill.",1.2,
    "Deploy volunteers with documented relief supplies and publish ward-by-ward relief log on social media.",
    "Organise a high-visibility convoy with banners to relief sites and hold a simultaneous press conference.",
    "Survey actual relief gaps before deploying to ensure party goes to genuinely underserved areas.",
    "Accept a developer's funds for relief materials in exchange for the developer's branding on the relief packages.",
    10,12,7,
    (-1,-1,4,5),(2,0,2,4),(0,-1,3,4),(1,3,-4,-3),
    (14,"Log reveals party volunteers only covered three wards."),(17,"Convoy accused of obstructing NDRF movement."),(13,"Survey shows government already covered priority areas; party goes to secondary zones."),(23,"Developer branding triggers 'relief politicisation' allegations."),
    (-1,0,-2,-2),(-1,0,-3,-3),(0,0,-2,-3),(0,4,-5,-4),
    "Documented relief builds genuine urban working-class goodwill.","Press conference amplifies accountability demands on state.","Secondary zone deployment fills an actual government gap.","Developer branding collapses goodwill generated by relief work.",
))

items.append(opp("opp_mh_congress_seat_adjustment_2004","coalition_management","Congress-NCP 2004 poll seat adjustment final round","Final seat-sharing negotiation; NCP wants Pune cantonment, Congress wants Nashik East — both are winnable seats.",0.9,
    "Agree on Pune cantonment to NCP and Nashik East to Congress and lock the deal publicly before nominations open.",
    "Hold a joint rally to generate public commitment that makes backing out politically costly.",
    "Conduct micro-level polling in both seats to determine which party is stronger on ground.",
    "Resolve it with a side-deal allowing each party to field a rebel candidate in the other's seat.",
    8,10,5,
    (-1,-1,2,3),(2,0,0,3),(0,-1,2,2),(1,3,-3,-2),
    (12,"Lock-in deal broken after NCP surveys show Pune cantonment loss risk."),(15,"Joint rally creates public pressure but deal still unclear."),(11,"Micro-polling data accepted by both sides; clean deal reached."),(19,"Rebel candidacy splits votes; both seats lost."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-1,-1),(0,3,-3,-3),
    "Early lock-in allows coordinated nomination and campaign planning.","Rally builds alliance optics ahead of election season.","Data-based resolution durable; no subsequent disputes.","Rebel split costs both parties seats they would have won jointly.",
))

items.append(opp("opp_mh_sena_thackeray_youth_rally","movement_pressure","Bal Thackeray calls youth rally on unemployment","Bal Thackeray proposes a lakhs-strong Shiv Sena youth rally at Shivaji Park on Maharashtra unemployment.",1.1,
    "Frame the rally around a written 10-point employment charter and submit it formally to the CM post-rally.",
    "Maximise rally attendance through an aggressive cadre mobilisation drive and make it a show of street power.",
    "Survey what unemployment demands have the broadest youth resonance before finalising the charter.",
    "Accept corporate sponsorship for rally logistics in exchange for softening the private sector hiring demand.",
    10,13,7,
    (-1,0,3,4),(3,0,-1,5),(0,-1,3,3),(1,3,-2,-2),
    (14,"Charter not delivered post-rally; credibility gap."),(17,"Attendance figures disputed by rival media."),(13,"Survey shapes charter; demand resonance much higher."),(22,"Corporate link seen as contradiction of workers' rally."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-1,-1),(0,3,-3,-3),
    "Charter submission creates formal accountability mechanism.","Rally scale generates national attention.","Survey-shaped charter earns editorial credibility.","Sponsorship link undercuts the anti-corporate message.",
))

items.append(opp("opp_mh_coastal_fishing_support","labor_outreach","Party backs coastal fishing communities in Palghar","Fisher cooperatives in Palghar invite party leaders to support their demand for diesel subsidy extension and trawler fee reduction.",1.0,
    "Visit Palghar fishing villages, document subsidy demand data, and submit a formal petition to the fisheries ministry.",
    "Organise a fishers' rally at the taluka head office with a deadline for government response.",
    "Verify diesel subsidy disbursement records via RTI before endorsing the demand publicly.",
    "Accept a trawler owners' association fee for the support in exchange for backing a specific contractor's tender.",
    8,11,5,
    (-1,-1,3,4),(2,0,1,3),(0,-1,3,3),(1,3,-3,-3),
    (12,"Petition to fisheries ministry receives no response in 30 days."),(15,"Rally turnout lower than expected; fishers divided."),(12,"RTI reveals subsidy was already disbursed; refines demand."),(21,"Contractor tender support becomes a legal liability."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-2,-2),(0,4,-4,-4),
    "Petition creates formal record; follow-up is easier.","Rally builds coastal visibility for party.","RTI clarity produces more specific and credible demand.","Contractor link creates corruption allegation for party.",
))

items.append(opp("opp_mh_warkari_welfare_outreach","positive_service","Party proposes Warkari shelter improvement programme","Volunteers propose building 10 low-cost pilgrim rest shelters along the Pandharpur varkari route before Ashadhi Ekadashi.",0.9,
    "Partner with the Vitthal-Rukmini temple trust and panchayats to build and maintain the shelters.",
    "Hold a 'Service Yatra' along the route as a combination of service work and political outreach.",
    "Survey which stretches of the route have the worst shelter gap before finalising construction sites.",
    "Accept a real estate developer's funding for shelter construction in exchange for land development rights nearby.",
    7,10,5,
    (-1,-1,3,4),(2,0,1,3),(0,-1,3,3),(1,3,-3,-3),
    (11,"Temple trust wants control over the shelters; negotiation slow."),(13,"Service Yatra perceived as political by some Warkaris."),(11,"Survey reveals two priority stretches; construction targeted effectively."),(18,"Developer land-rights arrangement surfaces in local press."),
    (-1,0,-2,-2),(-1,0,-1,-1),(0,0,-1,-1),(0,3,-3,-3),
    "Temple partnership gives shelters institutional longevity.","Service Yatra generates goodwill among Warkari community.","Survey targets most needed stretches for maximum impact.","Developer link creates conflict-of-interest perception.",
))

items.append(opp("opp_mh_vidarbha_press_campaign","media_narrative","Opposition launches 'Vidarbha Speaks' media campaign","Party proposes a series of press op-eds, farmer radio spots, and village documentaries to highlight Vidarbha agrarian crisis.",1.0,
    "Publish verified op-eds with academic backing in Marathi and national English dailies.",
    "Run the campaign alongside a Nagpur assembly session dharna for simultaneous physical and media pressure.",
    "Conduct pilot village documentation in five districts before committing the full campaign.",
    "Accept a pharmaceutical company's sponsorship of the radio spots in exchange for soft mention of their crop insurance product.",
    9,11,6,
    (-1,-1,4,4),(2,0,2,3),(0,-1,4,3),(1,3,-3,-2),
    (13,"Op-ed rejected by Times of India; placed in smaller papers only."),(16,"Dharna and campaign compete for media attention."),(12,"Five-village documentation reveals stronger data than expected."),(22,"Pharma sponsorship creates credibility conflict with farmer narrative."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-1,-1),(0,3,-4,-3),
    "Academic-backed op-eds earn sustained editorial attention.","Combined physical and media pressure amplifies reach.","Pilot documentation produces compelling visuals.","Sponsorship disclosure damages campaign's authenticity.",
))

items.append(opp("opp_mh_internal_ticket_dispute_konkan","candidate_selection","Two candidates claim Ratnagiri ticket in Konkan","Both aspirants have real grassroots support in Ratnagiri; public dispute threatens to split local party.",0.9,
    "Hold an open constituency convention, invite both candidates to present their case, and decide by worker vote.",
    "Give the ticket to the stronger fundraiser and organise a mass rally to demonstrate unity.",
    "Commission a seat-wise survey by an independent agency before deciding.",
    "Allow the wealthier aspirant to fund 60% of district election expenses in exchange for the ticket.",
    7,10,5,
    (-1,-1,2,3),(2,0,-1,3),(0,-1,2,2),(1,3,-3,-3),
    (12,"Losing aspirant withdraws booth workers from campaign."),(15,"Fundraiser candidate lacks policy credibility in media."),(11,"Survey shows the less-funded candidate is stronger."),(19,"Funding arrangement leaked; party loses urban credibility."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-1,-1),(0,4,-3,-3),
    "Convention process produces legitimate winner accepted by both sides.","Fundraiser rally turns out well but ground support thin.","Survey selects stronger candidate; less post-nomination drama.","Funding leak forces party to withdraw its own candidate.",
))

items.append(opp("opp_mh_drought_opp_response_2002","movement_pressure","Opposition response to 2002 drought in Marathwada","Marathwada faces near-famine conditions; opposition wants to lead a food distribution drive and policy agitation.",1.1,
    "Run a documented food camp in 50 worst-hit villages and submit a district-wise shortfall report to the CM.",
    "Stage a 72-hour relay hunger strike at Aurangabad collector's office with continuous media coverage.",
    "Survey food security gaps using ICDS data before deploying resources to most critical areas.",
    "Accept a private trader's food stock as donation to run the camp, giving them distribution branding.",
    9,12,6,
    (-1,-1,4,5),(2,0,2,4),(0,-1,3,4),(1,3,-3,-3),
    (14,"Food camp reveals organisational reach is limited to taluka HQs."),(17,"Hunger strike media coverage fades after day two."),(13,"ICDS data shows 12 critical villages not on opposition's list."),(23,"Trader branding seen as commercialising drought relief."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-2,-3),(0,4,-5,-4),
    "Documented camp creates credible record of state failure.","Hunger strike generates 48 hours of strong media coverage.","Survey drives better resource allocation to critical areas.","Trader branding creates serious credibility damage.",
))

items.append(opp("opp_mh_sena_bjp_2004_postelection","leadership_management","Sena-BJP post-2004 loss leadership accountability debate","After the Sena-BJP coalition loses the 2004 Maharashtra assembly election, internal voices demand leadership accountability.",0.9,
    "Convene a working committee post-mortem with honest seat-loss analysis and establish a reform roadmap.",
    "Organise a large cadre motivation rally to project confidence and prevent morale collapse.",
    "Commission a neutral post-poll survey to identify where and why votes shifted before drawing conclusions.",
    "Allow the two senior leaders responsible for coalition strategy to negotiate privately rather than face public audit.",
    8,10,5,
    (-1,-1,2,3),(2,0,-1,3),(0,-1,2,2),(1,3,-2,-2),
    (12,"Post-mortem report leaks; blame war begins."),(15,"Motivation rally seen as avoiding accountability."),(11,"Post-poll survey produces clear message discipline failures."),(18,"Private arrangement creates two-tier accountability perception."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-1,-1),(0,2,-2,-2),
    "Honest post-mortem earns credibility with party cadre.","Motivation rally keeps grassroots energy alive.","Survey findings inform more coherent rebuilding strategy.","Private deal creates culture of non-accountability.",
))

items.append(opp("opp_mh_environmental_campaign_mumbai","positive_service","Opposition-backed mangrove protection campaign in Mumbai","NGOs invite opposition to support a campaign to stop illegal mangrove destruction for reclamation projects.",0.9,
    "Formally endorse the campaign, co-file an HC petition, and send senior party members to coastal inspection walks.",
    "Stage a press conference on Marine Drive demanding the state notified mangrove protection zones be enforced.",
    "Review the HC petition's legal strength and pending cases before formally joining the campaign.",
    "Accept a construction industry association's offer to fund alternative site surveys in exchange for moderated campaign language.",
    7,10,5,
    (-1,-1,3,4),(2,0,1,3),(0,-1,3,3),(1,3,-3,-3),
    (11,"HC petition lumped with 12 others; slow progress."),(13,"Press conference creates conflict with party allies in construction."),(11,"Legal review reveals three already-won mangrove cases."),(20,"Construction industry link exposed; environmental credibility collapses."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-1,-1),(0,4,-4,-4),
    "HC petition co-filing gives campaign legal standing.","Press conference generates public attention on mangrove issue.","Legal review identifies strongest litigation pathway.","Industry link destroys environmental positioning credibility.",
))

items.append(opp("opp_mh_weaker_section_policy","policy_credibility","Party outlines weaker sections policy for 2004 poll manifesto","Party debates how detailed its SC/ST/OBC welfare policy should be and whether to commit fiscal numbers.",0.9,
    "Publish a costed policy note with specific scheme commitments and an economist review panel.",
    "Announce sweeping welfare pledges at a mega rally in Nagpur near the Deekshabhoomi site.",
    "Survey scheduled community leaders on their priority demands before finalising any manifesto number.",
    "Keep welfare commitments aspirational and extract election fund contributions from OBC business associations.",
    8,10,5,
    (-1,-1,3,4),(2,0,-1,4),(0,-1,3,3),(1,3,-3,-3),
    (12,"Economist review reveals cost exceeds state annual plan."),(15,"Nagpur rally generates high turnout but invites fiscal scrutiny."),(11,"Survey produces a ranked list that shapes more targeted commitments."),(21,"OBC association funding link published before election."),
    (-1,0,-2,-2),(-1,0,-3,-3),(0,0,-1,-1),(0,4,-4,-4),
    "Costed note earns editorial respect; manageable expectations.","Mega rally generates strong SC/ST voter momentum.","Survey produces manifesto commitments with genuine community ownership.","Funding association link undermines welfare credibility.",
))

items.append(opp("opp_mh_anti_toll_rtd","movement_pressure","NCP proposes toll-free district roads for farmers","NCP district unit proposes a campaign to make all district and rural roads toll-free to reduce farm input costs.",0.8,
    "Publish a cost analysis of the toll waiver, identify state revenue offset, and submit a formal bill in the assembly.",
    "Organise a farmer tractor rally blocking three toll points on major district roads.",
    "File RTI on district road toll revenue versus maintenance cost before making the public case.",
    "Accept a road contractor's funding for the campaign in exchange for future tender endorsement.",
    7,10,4,
    (-1,-1,3,4),(2,0,0,3),(0,-1,3,3),(1,3,-3,-3),
    (12,"Bill not admitted for discussion in current session."),(15,"Tractor blockade disrupts supply chain; traders protest."),(11,"RTI shows most district roads have zero toll; campaign redirected."),(20,"Contractor link becomes election issue."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-1,-1),(0,4,-4,-4),
    "Cost analysis creates credible policy document for next session.","Tractor rally generates large visual media coverage.","RTI data refocuses campaign on genuinely problematic tolls.","Contractor link collapses campaign's credibility.",
))

items.append(opp("opp_mh_obc_reservation_demand","social_cohesion","OBC community demands creamy layer revision in Maharashtra","OBC leaders ask the party to publicly demand revision of the ₹8 lakh creamy layer limit for OBC reservation benefits.",0.9,
    "Publish a formal policy position with a revised income benchmark based on economic survey data.",
    "Hold a mass rally at Azad Maidan demanding legislative action on the creamy layer revision.",
    "Survey OBC community leaders on their priority — creamy layer, hostel, or scholarship — before any announcement.",
    "Keep the demand ambiguous to extract election contributions from OBC business associations.",
    8,10,5,
    (-1,-1,3,4),(2,0,1,3),(0,-1,3,3),(1,3,-3,-3),
    (13,"Economic survey data used against party in Assembly debate."),(16,"Rally covered as a routine OBC meeting; low editorial impact."),(12,"Survey reveals scholarship demand is more urgent than creamy layer."),(21,"OBC association funding link published by Loksatta."),
    (-1,0,-2,-2),(-1,0,-1,-1),(0,0,-1,-1),(0,4,-4,-4),
    "Policy paper earns credibility with community leaders.","Rally turnout signals political importance to ruling party.","Survey redirects party to higher-priority OBC demand.","Funding link damages party's social justice positioning.",
))

items.append(opp("opp_mh_local_mlc_election_funding","funding_ethics","Opposition MLC election needs emergency funding","Party needs ₹15 crore to contest three Maharashtra Legislative Council seats but party fund is short.",0.9,
    "Launch a transparent small-donor drive and ask elected members to contribute from their LAD funds legally.",
    "Stage a big fundraiser dinner at a Mumbai five-star with ticket prices of ₹1 lakh per plate.",
    "Audit what funds are legally available from party reserves and state electoral bonds before any event.",
    "Accept a real estate group's conditional donation in exchange for a promise on state FSI policy.",
    8,10,5,
    (-1,-1,2,3),(2,0,-1,2),(0,-1,2,2),(1,3,-3,-3),
    (11,"Small donor drive raises only ₹3 crore; gap remains."),(14,"Five-star event photos anger workers from Vidarbha."),(11,"Audit reveals ₹8 crore available; gap manageable."),(20,"FSI promise leaks to competitor party and media."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-1,-1),(0,4,-4,-4),
    "Transparent drive builds grassroots ownership of electoral process.","Fundraiser raises funds but creates optics problem.","Audit-based funding enables cleaner financial planning.","FSI promise leak causes development policy controversy.",
))

items.append(opp("opp_mh_alliance_with_peasant_group","coalition_management","Shetkari Sanghatana proposes pre-poll alliance","The Shetkari Sanghatana offers to join the opposition alliance if given 12 assembly seats in farmer-belt constituencies.",0.9,
    "Negotiate 8 seats, jointly publish a farm rights manifesto, and hold a seed rally to announce the alliance.",
    "Accept all 12 seats to secure maximum farm vote and announce the alliance at a Nashik rally.",
    "Survey voter loyalty of Shetkari Sanghatana in contested seats before agreeing to any number.",
    "Agree to 12 seats privately but also allow the party to run 4 friendly rebels to hedge the bet.",
    8,10,5,
    (-1,-1,3,4),(2,0,0,3),(0,-1,3,3),(1,2,-2,-2),
    (12,"Sanghatana rejects 8; alliance nearly collapses."),(15,"12-seat concession angers alliance partner Congress."),(11,"Survey shows Sanghatana strong in only 5 seats."),(19,"Rebel strategy exposed; Sanghatana exits the alliance."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-1,-1),(0,3,-3,-3),
    "8-seat pact is fair and durable through election day.","12-seat concession costs Congress three urban seats.","Survey produces optimal seat split for maximum win probability.","Rebel strategy collapses alliance before nomination deadline.",
))

items.append(opp("opp_mh_conrgrss_healthcare_drive","positive_service","Congress proposes district hospital monitoring by party volunteers","District health units propose sending trained party volunteers to monitor government hospital service delivery.",0.9,
    "Launch a formal hospital monitoring programme with NGO partners and publish monthly scorecards.",
    "Stage a walkout at a district hospital with cameras rolling to expose specific patient care failures.",
    "Survey hospital users in three districts to establish baseline before committing to the monitoring programme.",
    "Accept a pharma company's monitoring equipment donation in exchange for brand visibility in hospitals.",
    7,10,5,
    (-1,-1,3,4),(2,0,1,3),(0,-1,3,3),(1,2,-2,-2),
    (11,"Hospital administration blocks volunteer entry citing privacy rules."),(13,"Walkout creates tension; patients stranded during media visit."),(11,"Survey reveals worst hospitals are not in major cities."),(17,"Pharma branding in public hospitals triggers HC notice."),
    (-1,0,-2,-2),(-1,0,-1,-2),(0,0,-1,-1),(0,3,-2,-2),
    "Monthly scorecards create sustained media accountability coverage.","Walkout forces district collector to inspect the hospital.","Survey redirects programme to most impactful locations.","HC notice forces removal of pharma branding, reducing programme scale.",
))

items.append(opp("opp_mh_maratha_reservation_2004_opp","ideology_identity","Opposition's position on Maratha reservation demand","The Maratha community asks all opposition parties to formally endorse full reservation before the 2004 elections.",1.0,
    "Endorse the demand for an empirical backward class survey as the proper constitutional process.",
    "Promise full Maratha OBC reservation in the party manifesto and announce at a Kolhapur rally.",
    "Survey SC/ST and OBC communities' reaction to Maratha inclusion before taking a formal position.",
    "Accept Maratha organisations' electoral support in exchange for a vague manifesto promise of 'review'.",
    9,11,6,
    (-1,-1,3,4),(2,0,-1,3),(0,-1,3,3),(1,2,-2,-2),
    (13,"SC/ST groups accuse party of diluting their reservation pie."),(16,"Legal experts say OBC inclusion unconstitutional without survey."),(12,"Survey reveals SC/ST voters are the party's core base."),(21,"Vague promise satisfies neither Maratha nor SC/ST voters."),
    (-1,0,-2,-2),(-1,0,-3,-3),(0,0,-1,-1),(0,2,-2,-2),
    "Survey endorsement earns constitutional credibility.","Rally generates strong Maratha community mobilisation.","Survey data produces politically and legally sound position.","Vague promise leads to vote split in key constituencies.",
))

items.append(opp("opp_mh_bjp_anti_corruption_hotline","scandal_strategy","BJP proposes anti-corruption hotline ahead of 2004 polls","BJP proposes a people's anti-corruption hotline collecting complaints against state government to feed into campaign.",0.9,
    "Launch the hotline with a verified complaint management system and publish weekly credible case summaries.",
    "Open the hotline at a press conference with live complaint display for maximum media impact.",
    "Run a two-week pilot hotline in Nagpur before scaling state-wide to test complaint quality and volume.",
    "Use hotline data privately to identify the most damaging cases to trade for administrative concessions.",
    8,10,5,
    (-1,-1,3,3),(2,0,1,3),(0,-1,3,2),(1,3,-3,-2),
    (12,"Verification process excludes most rural complainants."),(15,"Live display shows implausible complaint volume; press sceptical."),(11,"Pilot identifies 80 credible cases; state-wide scale is manageable."),(21,"Trade attempt exposed by whistleblower complainant."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,-1,2,2),(0,4,-4,-4),
    "Verified complaints produce durable campaign material.","Live press conference creates strong launch coverage.","Pilot ensures credibility of state-wide hotline.","Whistleblower exposure collapses hotline credibility.",
))

items.append(opp("opp_mh_civic_pollution_campaign","positive_service","NCP proposes clean river campaign in Pune","NCP proposes a Mula-Mutha river pollution campaign and rally to pressure PMC to upgrade sewage treatment plants.",0.8,
    "Partner with Pune environmental NGOs to audit sewage discharge points and submit a binding demand to PMC.",
    "Organise a riverside rally with over 10,000 participants to pressure PMC and state environment department.",
    "File RTIs on PMC STP capacity versus actual sewage load before framing public demands.",
    "Accept a realty developer's sponsorship for the event in exchange for softening the riverfronts land-use demand.",
    7,10,4,
    (-1,-1,3,4),(2,0,1,3),(0,-1,3,3),(1,3,-3,-3),
    (11,"NGO audit data disputed by PMC; engagement slows."),(13,"Rally footprint itself pollutes the riverbank; ironic media coverage."),(11,"RTI reveals STP capacity is only 35% of need; strong case built."),(18,"Developer link exposed; river campaign loses environmental credibility."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,-1,2,2),(0,4,-4,-4),
    "NGO partnership produces credible discharge data for HC petition.","Rally generates public pressure and media coverage.","RTI data produces legally backed environmental petition.","Developer link destroys environmental credibility.",
))

items.append(opp("opp_mh_mumbai_housing_crisis_opp","policy_credibility","Opposition's urban housing policy for Mumbai","Party debates whether to promise lower FSI norms for affordable housing or promote greater construction to reduce costs.",0.9,
    "Publish a costed 'affordable housing task force' plan with specific FSI, affordability caps, and community consent provisions.",
    "Announce mass affordable housing as the centrepiece of the party's Mumbai election manifesto.",
    "Survey Mumbai housing needs across income segments before determining the FSI and price band positions.",
    "Keep the housing position deliberately vague to attract contributions from both developer and slum-dweller lobby groups.",
    8,10,5,
    (-1,-1,3,3),(2,0,-1,4),(0,-1,3,3),(1,3,-3,-3),
    (12,"Costed plan attacked by developers as anti-growth."),(15,"Mass housing promise costed at ₹80,000 cr; critics mock scale."),(12,"Survey shows most demand is in ₹15–30 lakh segment; sharp positioning possible."),(21,"Double-lobby contributions exposed; position incoherent."),
    (-1,0,-2,-2),(-1,0,-3,-3),(0,0,-1,-1),(0,3,-3,-3),
    "Costed plan earns credit with urban planning community.","Mass housing promise wins strong working-class urban vote.","Survey produces politically sharp and implementable policy.","Double-lobby exposure makes housing policy undeliverable.",
))

items.append(opp("opp_mh_farmers_insurance_gap","scandal_strategy","Vidarbha farmers expose crop insurance non-payment","Party documents show that 70% of Vidarbha crop insurance claims in 2003 were rejected by the insurer; premium paid, no payout.",1.1,
    "File a formal complaint with IRDAI using farmer-signed affidavits and present findings at a press conference.",
    "Stage a farmer protest outside the insurance company's Nagpur office with the rejected claim letters.",
    "Cross-check claim rejection letters against IRDAI grievance records before going public.",
    "Use rejected claim data privately to negotiate with the insurer for a lump-sum settlement before election.",
    9,12,6,
    (-1,-1,4,5),(2,0,1,4),(0,-1,4,4),(1,3,-3,-3),
    (14,"IRDAI cites force majeure clause; complaint slow."),(16,"Insurer calls protest harassment; seeks legal injunction."),(12,"Cross-check reveals rejection letters contain fabricated grounds."),(23,"Private settlement attempt becomes public; farmers furious."),
    (-1,0,-2,-3),(-1,0,-2,-3),(0,-1,2,3),(0,4,-5,-5),
    "IRDAI complaint creates regulatory pressure for eventual payout.","Protest generates strong visual media outside corporate office.","Fabricated grounds create strongest possible legal and political case.","Settlement leak destroys all farmer trust in opposition.",
))

items.append(opp("opp_mh_old_leader_demand_role_2003","leadership_management","Senior Sena leader demands larger campaign role","A veteran Shiv Sena leader, sidelined in recent reorganisation, demands a prominent role in the 2004 election campaign.",0.9,
    "Offer the leader a visible ceremonial role and the party's leading seat in his home constituency.",
    "Organise a special party felicitation rally for the veteran to publicly project party unity.",
    "Survey his actual booth-level support in his district before deciding how much ground role to give.",
    "Offer the leader a financial arrangement for his silence and keep him off the campaign trail.",
    7,10,5,
    (-1,-1,2,3),(2,0,0,3),(0,-1,2,2),(1,3,-2,-2),
    (12,"Ceremonial role not accepted; leader gives media interview."),(14,"Felicitation rally seen as patronising by leader's faction."),(11,"Survey shows leader's booth network is critical in 3 seats."),(18,"Financial arrangement leaked by a junior aide."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-1,-1),(0,3,-2,-2),
    "Ceremonial role buys time if genuine campaign discussions follow.","Felicitation creates goodwill if genuinely honoured.","Survey produces objective basis for role assignment.","Leaked arrangement creates culture-of-silence perception.",
))

items.append(opp("opp_mh_solar_pump_farmer_demand","policy_credibility","Farmers demand solar pump scheme in opposition manifesto","Farm leaders ask the opposition to promise a solar pump scheme for 5 lakh Vidarbha farms to end dependence on grid power.",0.9,
    "Publish a costed solar pump scheme with central-state co-financing model and farmer contribution cap.",
    "Announce 5 lakh solar pumps as a flagship manifesto promise at a Nagpur rally.",
    "Survey farmer preference for solar pumps versus free electricity to compare political and practical impact.",
    "Accept solar energy company's funding for the manifesto launch in exchange for them being named preferred vendor.",
    8,10,5,
    (-1,-1,3,4),(2,0,-1,4),(0,-1,3,3),(1,3,-3,-3),
    (12,"Costing exercise finds central support uncertain; scheme scaled back."),(15,"5-lakh promise costed at ₹6,000 cr; media questions fiscal math."),(11,"Survey shows free electricity preferred by 60%; manifesto adjusted."),(21,"Vendor naming creates procurement controversy before election."),
    (-1,0,-2,-2),(-1,0,-3,-3),(0,0,-1,-1),(0,3,-3,-3),
    "Costed scheme with co-financing earns state planning board attention.","5-lakh promise generates strong media and farmer enthusiasm.","Survey produces politically superior 'free units' alternative.","Vendor naming creates anti-corruption counterattack.",
))

items.append(opp("opp_mh_sena_student_wing_agitation","movement_pressure","Sena student wing demands action on unemployed engineers","BVSS (Sena student wing) proposes a statewide agitation demanding government jobs for BTech graduates.",0.9,
    "Channel demand into a formal memorandum to the technical education and PWD departments with verified vacancy data.",
    "Hold a campus rally at Pune Engineering College with 5,000 students and demand a minister's response.",
    "Survey BTech student demand versus available government technical post vacancies before committing to numbers.",
    "Accept a private college consortium's funding for the event in exchange for softening the government-jobs demand.",
    7,10,5,
    (-1,-1,3,3),(2,0,1,3),(0,-1,3,2),(1,3,-3,-3),
    (12,"Departments reject memorandum citing hiring freeze."),(14,"Campus rally blocked by college management."),(11,"Survey finds 12,000 vacancies; credible demand built."),(18,"Private college funding conflicts with demand for public jobs."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,-1,2,2),(0,3,-3,-3),
    "Memorandum creates formal government obligation to respond.","Rally generates youth media coverage and political visibility.","Vacancy data creates strongest and most specific demand.","Funding conflict undermines the youth employment narrative.",
))

items.append(opp("opp_mh_opp_alliance_branding","media_narrative","Opposition alliance needs unified branding pre-2004","Congress-NCP alliance debates whether to campaign under a single unified symbol or maintain separate identities.",0.9,
    "Design a joint 'Aghadi' campaign logo with both parties' symbols and co-brand all advertising equally.",
    "Run separate but coordinated campaigns to maximise each party's distinct voter base without alienating either.",
    "Survey voter recognition of each party brand independently before determining the optimal joint branding approach.",
    "Accept a media house's offer to design the joint branding in exchange for first access to alliance press conferences.",
    7,10,5,
    (-1,-1,2,3),(2,0,1,3),(0,-1,2,2),(1,2,-2,-2),
    (11,"NCP cadre rebels against equal billing."),(13,"Separate campaigns confuse voters in swing seats."),(11,"Survey shows voters want a single Aghadi face."),(17,"Media house access arrangement creates editorial conflict of interest."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-1,-1),(0,3,-3,-3),
    "Joint branding projects strong alliance unity.","Separate campaigns maintain distinct voter outreach.","Survey provides clear direction on branding strategy.","Editorial access conflict limits media credibility.",
))

items.append(opp("opp_mh_anti_hoarding_campaign","scandal_strategy","Opposition exposes onion and pulses hoarding in Pune","A party worker documents warehouses in Pune with illegally hoarded onion and pulses; media interest is high.",0.9,
    "Publish warehouse locations, file a complaint with the Essential Commodities Act authority, and hand documents to press.",
    "Stage a dramatic press conference outside the warehouse with party leaders and cameras for maximum visual impact.",
    "Cross-check ownership records and EC Act compliance status before going public.",
    "Use the hoarding evidence privately to extract concessions from the traders' association.",
    8,11,5,
    (-1,-1,4,4),(2,0,1,3),(0,-1,4,3),(1,3,-3,-2),
    (13,"Warehouse owner produces valid storage licences; complaint partly withdrawn."),(15,"Press conference draws police notice of the party rather than the warehouse."),(12,"Ownership records link hoarding to a ruling party donor."),(21,"Trader association concession attempt leaked; trader publicly allies with ruling party."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,-1,2,2),(0,4,-4,-4),
    "EC complaint forces official inspection of flagged warehouses.","Dramatic press conference generates strong evening news.","Donor link creates powerful and durable political charge.","Concession leak strengthens ruling party's trader support.",
))

items.append(opp("opp_mh_healthcare_policy_manifesto","policy_credibility","NCP designs rural healthcare manifesto commitment","Party debates whether to commit to a ₹10,000 crore universal health scheme or a more targeted PHC upgrade programme.",0.9,
    "Publish a phased PHC upgrade plan with 1,000 new doctors and costed NRHM co-funding model.",
    "Announce a 'Maharashtra Health Guarantee Scheme' at a Nashik rally with ₹10,000 crore headline figure.",
    "Survey rural voter healthcare priorities across five divisions before designing the manifesto commitment.",
    "Keep healthcare commitment vague enough to attract pharma and hospital industry donations.",
    8,10,5,
    (-1,-1,3,4),(2,0,-1,4),(0,-1,3,3),(1,3,-3,-3),
    (12,"Phased plan lacks the headline punch of rival commitments."),(15,"₹10,000 crore figure attacked as uncosted within 24 hours."),(11,"Survey reveals doctors and medicines are the priority, not buildings."),(21,"Industry donations create conflict with public healthcare demand."),
    (-1,0,-2,-2),(-1,0,-3,-3),(0,0,-1,-1),(0,4,-4,-4),
    "PHC upgrade plan earns credibility with public health community.","Health guarantee promise mobilises rural voters effectively.","Survey-shaped commitment addresses actual voter healthcare needs.","Industry conflict forces party to water down health guarantee.",
))

items.append(opp("opp_mh_cadre_booth_agent_training","party_organization","NCP booth agent training programme for 2004 polls","Party wants to train 50,000 booth agents in 90 days for the 2004 assembly elections.",0.9,
    "Run a structured 3-day booth-agent training camp in each district with role play and voter list exercises.",
    "Hold a large cadre motivation rally at each divisional headquarters and combine training with mass mobilisation.",
    "Pilot the training in five swing constituencies first to optimise the curriculum before scaling.",
    "Outsource training to a political consultancy firm and fund it through party development levy.",
    7,9,5,
    (-1,-1,2,3),(2,0,0,3),(0,-1,2,2),(1,2,-2,-2),
    (11,"Camp attendance in 12 districts is below 40%."),(13,"Rally format dilutes training quality."),(10,"Pilot reveals three critical knowledge gaps in first draft curriculum."),(16,"Consultancy firm links surface in rival party's campaign material."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,0,-1,-1),(0,2,-2,-2),
    "Structured training produces better informed booth agents.","Rally format keeps cadre energy high alongside training.","Pilot-optimised curriculum improves training effectiveness.","Consultancy links create perception of outsourced politics.",
))

items.append(opp("opp_mh_sugar_factory_land_issue","industry_land","Opposition responds to sugar factory land acquisition in Satara","Farmers in Satara district object to the state handing cooperative sugar mill land to a private developer after the mill's closure.",1.0,
    "Demand HC-supervised public auction of mill land with farmer-worker first-right provisions.",
    "Stage a mass rally at the district collectorate demanding cancellation of the private developer deal.",
    "File RTI on the valuation methodology used for the land transfer before making any public statement.",
    "Negotiate with the developer privately to secure a percentage of the land for a farmer cooperative.",
    8,11,5,
    (-1,-1,3,4),(2,0,1,3),(0,-1,3,3),(1,2,-2,-2),
    (12,"HC declines to intervene before auction begins."),(15,"Rally accused of interfering in a legitimate business arrangement."),(12,"RTI reveals land valued at 25% of market rate."),(19,"Developer negotiation seen as implicit deal with the opposition."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,-1,2,2),(0,3,-3,-3),
    "HC petition creates legal delay and public scrutiny.","Rally generates strong farmer community solidarity.","Undervaluation data creates most powerful political charge.","Developer negotiation undermines opposition's credibility.",
))

items.append(opp("opp_mh_municipal_water_privatisation","positive_service","Opposition campaigns against Nagpur water privatisation","The Nagpur Municipal Corporation awards a 25-year water supply contract to a French company; civil society opposes it.",0.9,
    "File a HC petition challenging the bid process and co-convene a citizens' water rights forum.",
    "Stage a dharna at the NMC headquarters with civil society groups demanding the contract be scrapped.",
    "Review the bid documents obtained through RTI before committing to a legal or agitation strategy.",
    "Accept an alternative water company's funding for the campaign in exchange for supporting their competing bid.",
    7,10,5,
    (-1,-1,3,4),(2,0,1,3),(0,-1,3,3),(1,3,-3,-3),
    (11,"HC admits petition but stays proceedings temporarily."),(13,"NMC defends contract as legally unimpeachable."),(12,"RTI reveals bid process had only one eligible respondent."),(20,"Alternative company funding exposed; campaign loses civil society support."),
    (-1,0,-2,-2),(-1,0,-2,-2),(0,-1,2,2),(0,4,-4,-4),
    "HC petition keeps water privatisation under legal review.","Dharna generates city-wide public debate on water rights.","Single-bidder data is strongest ground for challenging the contract.","Funding exposure collapses coalition with civil society partners.",
))



print(f"Generated {len(items)} news items")

# Build the new JSON structure
new_data = {
  "reviewStatus": "draft_for_review_not_inserted",
  "scenarioKey": "Mh_2001",
  "period": {"startMonth": "2001-01", "endMonth": "2005-12", "months": 60},
  "sourceNotes": [
    "Historical-inspired, fictionalized for gameplay; does not use real party names in playable text.",
    "New batch covers 2001-2005 with expanded categories: corruption/scams, sports, economy (positive), welfare, health, environment, and culture.",
    "Anchors include chit fund collapses, PDS scams, teacher recruitment fraud, Kolkata Derby, Santosh Trophy, IT park growth, jute industry revival, Darjeeling tea exports, polio eradication, tribal literacy, and biometric ration pilot.",
    "Each item carries unique, context-calibrated reaction options, weights, risk chances, and effects reflecting the period's political and social dynamics."
  ],
  "defaults": {
    "type": "external",
    "weights": {
      "baseSelectionWeight": 1.0,
      "historicalAnchorWeight": 0.8,
      "scenarioFlavorWeight": 1.2
    },
    "reactionRule": "Each news item contains its own 3 active reactions plus no_comment. Reaction weights and effects vary by issue profile.",
    "thirdPartyReactionRule": "THIRD_PARTY can use opposition-compatible and neutral reactions."
  },
  "newsItems": items,
  "balanceNotes": {
    "publicSupportScale": "News reactions use a wider -5..+5 support range. Extreme reactions can produce +5 upside but carry -5 backlash risk; no-comment usually costs -1 to -2 support/media.",
    "newsToneScale": "Constructive/investigative reactions give +4, mobilizing reactions can give +5 with -5 backlash risk, blame/attack reactions can cost -3 support, no-comment costs -2 to -5 depending on severity.",
    "corruptionScamItems": "Items tagged corruption/scam carry higher media and public support stakes. Government silence on such items adds corruptionScore. Swift action subtracts it.",
    "sportsGoodNews": "Sports and good-news items are lighter-weight but offer morale and cultural-connect bonuses. Missing them rarely backfires badly but passing up is a soft cost.",
    "economyItems": "Economy positive items reward proactive framing by government; failing to capitalize is a missed opportunity (-2 support/-2 media). Over-claiming can backfire if delivery lags."
  }
}

with open('gov_mh_electricity_maharashtra_2001_2005.json', 'w', encoding='utf-8') as f:
    json.dump(new_data, f, indent=2, ensure_ascii=False)

print("Saved to west_bengal_2001_2004_new_60_news.json")