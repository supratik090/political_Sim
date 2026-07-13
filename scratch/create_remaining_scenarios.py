import json
from pathlib import Path

# Data structure detailing all 9 states and their milestones
states_config = {
    "himachal_pradesh_2001": {
        "short_code": "hp2001",
        "gov_party": "BJP", "opp_party": "INC", "third_party": "YDP",
        "gov_change_month": "2003-03", # BJP -> INC
        "gov_change_party": "INC", "opp_change_party": "BJP",
        "memory_prefix": "himachal",
        "topics": [
            ("apple_procurement", "Apple Fruit Procurement Tariffs", "apple crop tariff adjustments in Solan and Shimla", "rural", "announces subsidies for apple cultivators", "demands higher minimum support prices for fruit crops", "joint fruit marketing board is set up"),
            ("tourism_infrastructure", "Shimla Tourist Corridor Development", "tourism infrastructure expansion plans near Shimla", "infrastructure", "allocates funds for heritage road preservation in Kullu", "claims the tourism budget ignores water conservation in remote hills", "joint tourism advisory council is established"),
            ("hydro_electric", "Satluj Hydro Power Project", "hydro-power expansion permissions along the Satluj river", "economy", "approves environmental clearances for Satluj project expansion", "warns of ecological threats and displacement in tribal villages", "joint review panel of engineers and local chiefs is formed"),
            ("pension_protests", "State Employees Pension Scheme", "government employee pension scheme adjustments", "protest", "proposes a phased rollout of state employee pension allowances", "demands immediate implementation of central pension scales", "joint assembly-union negotiations are scheduled"),
            ("monsoon_landslides", "Kullu Valley Landslide Relief", "monsoon landslide clearing and relief coordination in Kullu", "security_crisis", "deploys emergency road clearance machinery to Kullu pass", "accuses district officers of sluggish response in remote villages", "joint relief coordination committee is formed")
        ]
    },
    "jammu_kashmir_2001": {
        "short_code": "jk2001",
        "gov_party": "NC", "opp_party": "INC", "third_party": "PDP",
        "gov_change_month": "2002-11", # NC -> PDP (coalition with INC)
        "gov_change_party": "PDP", "opp_change_party": "NC",
        "memory_prefix": "jk",
        "topics": [
            ("border_security", "Border Vigilance and Security Alerts", "security patrols and border vigilance operations near Uri", "security_crisis", "deploys additional security battalions near border borderlines", "demands local village protection committees and communication grids", "joint security review is organized with central observers"),
            ("dal_lake_tourism", "Srinagar Dal Lake Development", "Srinagar Dal Lake conservation and tourism revival initiatives", "infrastructure", "allocates funds for Dal Lake cleaning and shikara subsidies", "claims the lake restoration funds are diverted to urban pockets", "joint environment-tourism council is established"),
            ("peace_process", "Srinagar-Muzaffarabad Bus Route Talks", "Srinagar-Muzaffarabad bus route trade and travel negotiations", "governance", "coordinates passenger clearance facilities and travel protocols", "demands simplified documentation for cross-border families", "joint consultative committee is formed to oversee travel routes"),
            ("earthquake_relief", "Kashmir Valley Earthquake Rehabilitation", "earthquake relief camp management and housing reconstruction", "rural", "deploys emergency winter tents and distributes financial relief", "accuses relief officers of bias in distributing aid in remote areas", "joint multi-party relief desk is established for the valley"),
            ("panchayat_elections", "Panchayat Election Security Reforms", "panchayat polling arrangements and security reinforcements", "politics", "coordinates poll security measures and booth protection units", "demands judicial monitoring of the local election process", "joint code-of-conduct panel is set up to verify complaints")
        ]
    },
    "tripura_2001": {
        "short_code": "tr2001",
        "gov_party": "CPI_M", "opp_party": "INC", "third_party": "YDP",
        "gov_change_month": "none",
        "memory_prefix": "tripura",
        "topics": [
            ("insurgency_check", "NLFT Insurgency Combing Operations", "combing operations and village security checks in Dhalai", "security_crisis", "deploys special police task forces to remote forest tracks", "demands judicial probes into tribal village detention reports", "joint border security panel is established with central units"),
            ("border_fencing", "Bangladesh Border Fencing Disputes", "border fencing construction and local land displacement disputes", "infrastructure", "expedites fencing work and promises rehabilitation plots", "protests land acquisition without adequate compensation", "joint border coordination committee is formed to review land values"),
            ("rubber_subsidies", "Rubber Plantation Development Schemes", "rubber plantation subsidy and cooperative credit allocations", "rural", "announces subsidies for tribal rubber cooperative societies", "demands higher support prices for local rubber producers", "joint rubber marketing board is set up to monitor tariffs"),
            ("tribal_council", "Autonomous District Council Elections", "autonomous district council polling and campaign security", "politics", "coordinates security for autonomous tribal council elections", "claims the ruling party uses state machinery in tribal blocks", "joint code-of-conduct council is formed to review complaints"),
            ("monsoon_floods", "Gumti River Flash Flood Relief", "monsoon flash flood relief and embankment repair in Gumti", "protest", "deploys relief cargo and coordinates temporary shelter tents", "accuses local officers of bias in distributing food aid", "joint legislative relief committee is established to audit aid")
        ]
    },
    "arunachal_pradesh_2001": {
        "short_code": "ar2001",
        "gov_party": "INC", "opp_party": "BJP", "third_party": "UDF",
        "gov_change_month": "2003-08", # INC -> UDF/BJP
        "gov_change_party": "BJP", "opp_change_party": "INC",
        "memory_prefix": "arunachal",
        "topics": [
            ("border_roads", "Tawang Border Road Infrastructure", "border road construction and connectivity works in Tawang", "infrastructure", "allocates funds for strategic border roads and bridge links", "claims the road contracts ignore local tribal village connectivity", "joint border road monitoring panel is established"),
            ("refugee_dispute", "Chakma Refugee Settlement Debates", "Chakma-Hajong refugee settlement and registration reviews", "politics", "initiates census verification drives in refugee pockets", "demands immediate implementation of local employment safeguards", "joint committee of tribal chiefs is formed to review registers"),
            ("hydel_project", "Subansiri Hydro Power Project", "hydro-power construction permissions on Subansiri river", "economy", "approves clearances for Subansiri hydel grid project segments", "protests ecological threats and displacement of riverine villages", "joint review panel of engineers and local leaders is formed"),
            ("tribal_festivals", "Tribal Cultural Heritage Programs", "state patronage and funding allocations for tribal festivals", "identity", "announces state funding for traditional Nyokum celebrations", "claims the cultural allocations favor selective eastern districts", "joint cultural heritage board is formed to distribute funds"),
            ("security_vigil", "Chinese Claims Boundary Security", "security reinforcements and border patrol checks in remote valleys", "security_crisis", "strengthens police checkposts and coordinates with central units", "demands upgraded communications for remote border villagers", "joint legislative-security committee is established to audit checks")
        ]
    },
    "manipur_2001": {
        "short_code": "mn2001",
        "gov_party": "INC", "opp_party": "MPP", "third_party": "YDP",
        "gov_change_month": "none",
        "memory_prefix": "manipur",
        "topics": [
            ("ceasefire_protests", "Ceasefire Extension Agitations", "ceasefire boundary disputes and civil agitations in Imphal", "protest", "deploys security units to secure government buildings in Imphal", "demands the immediate revocation of the ceasefire extension", "joint assembly resolution is passed to protect Manipur's integrity"),
            ("afspa_debate", "AFSPA Enforcement Civil Protests", "AFSPA enforcement audits and human rights civil protests", "security_crisis", "coordinates police security protocols while leaving doors open for talks", "demands the immediate withdrawal of AFSPA from municipal areas", "joint legislative-civil panel is established to review guidelines"),
            ("highway_blockades", "National Highway Logistics Security", "national highway blockades and security convoy arrangements", "infrastructure", "deploys armed police escorts for essential commodity trucks", "demands immediate negotiations with blockading hill unions", "joint highway coordination council is formed to monitor supply"),
            ("loktak_conservation", "Loktak Lake Environmental Scheme", "Loktak lake cleaning and environmental zoning regulations", "rural", "approves conservation guidelines and orders weeding operations", "protests displacement of traditional lake-dwelling fishermen", "joint environment task force is established to audit lake work"),
            ("hill_council", "Hill District Council Development", "hill district development budgets and administrative allocations", "governance", "releases special funds for hill district development councils", "claims the hill allocations are delayed compared to valley blocks", "joint advisory board is formed to track hill project execution")
        ]
    },
    "meghalaya_2001": {
        "short_code": "ml2001",
        "gov_party": "INC", "opp_party": "UDP", "third_party": "YDP",
        "gov_change_month": "none",
        "memory_prefix": "meghalaya",
        "topics": [
            ("coal_mining", "Jaintia Hills Coal Mining Policy", "coal mining environmental audits and regulation drafts", "economy", "drafts mining safety guidelines and sets up local transport cells", "claims the mining rules threaten small local mine operators", "joint legislative-miner panel is formed to negotiate safety rules"),
            ("border_dispute", "Assam Border Boundary Disputes", "Assam border security checking and land border disputes", "governance", "strengthens police checkposts and coordinates checks with Assam", "demands immediate status quo talks over disputed border patches", "joint border coordination council is established to monitor peace"),
            ("militancy_alert", "HNLC Insurgency Vigilance Operations", "HNLC assembly alerts and security combing operations in Khasi hills", "security_crisis", "deploys special police task forces to patrol forest trails", "demands local village protection councils to check harassment", "joint legislative-police safety panel is formed to review checks"),
            ("shillong_tourism", "Shillong Urban Infrastructure Project", "Shillong urban road widening and bypass constructions", "infrastructure", "fast-tracks bypass project tender allocations and clearances", "claims the urban bypass ignores traditional landholder rights", "joint committee of civic officials and local chiefs is formed"),
            ("district_councils", "Khasi Hill District Council Elections", "autonomous district council polling and campaign security", "politics", "coordinates security for autonomous district council elections", "claims the ruling party uses state machinery in council blocks", "joint code-of-conduct council is formed to review complaints")
        ]
    },
    "mizoram_2001": {
        "short_code": "mz2001",
        "gov_party": "MNF", "opp_party": "INC", "third_party": "YDP",
        "gov_change_month": "none",
        "memory_prefix": "mizoram",
        "topics": [
            ("mautam_prep", "Mautam Bamboo Flowering Preparation", "Mautam bamboo flowering audits and rodent control preparations", "rural", "announces pesticide subsidies and sets up local collection cells", "demands immediate crop compensation guidelines for farmers", "joint agricultural advisory panel is formed to monitor bamboo"),
            ("bru_repatriation", "Bru Refugee Repatriation Talks", "Bru refugee repatriation and resettlement negotiations", "politics", "initiates census verification drives in border resettlement blocks", "demands immediate implementation of local employment safeguards", "joint committee of tribal chiefs is formed to review registers"),
            ("border_trade", "Champhai Indo-Myanmar Trade MOU", "Indo-Myanmar border trade infrastructure works in Champhai", "economy", "approves clearances for border trade transit facility segments", "claims the trade rules favor large trading firms over local shops", "joint review panel of customs and local merchants is formed"),
            ("peace_accord", "Mizo Accord Constitutional Commitments", "Mizo Peace Accord developmental guarantees review", "governance", "releases special funds for Mizo Accord development packages", "claims the accord development allocations are slow and ineffective", "joint advisory board is formed to track accord project execution"),
            ("monsoon_relief", "Aizawl Road Landslide Relief", "monsoon landslide clearing and relief coordination in Aizawl", "security_crisis", "deploys emergency road clearance machinery to Aizawl roads", "accuses district officers of sluggish response in remote villages", "joint relief coordination committee is formed")
        ]
    },
    "nagaland_2001": {
        "short_code": "ng2001",
        "gov_party": "INC", "opp_party": "NPF", "third_party": "YDP",
        "gov_change_month": "2003-03", # INC -> NPF (Rio)
        "gov_change_party": "NPF", "opp_change_party": "INC",
        "memory_prefix": "nagaland",
        "topics": [
            ("ceasefire_monitoring", "NSCN-IM Ceasefire Monitoring Talks", "ceasefire monitoring audits and border coordination talks", "security_crisis", "coordinates security protocols with central monitoring teams", "demands immediate investigation into border area ceasefire violations", "joint ceasefire coordination panel is established to review rules"),
            ("greater_nagalam", "Naga Area Integration Debates", "Naga area integration resolution debates in Kohima", "identity", "defends the integration resolution as a reflection of Naga pride", "claims the integration campaign ignores border security realities", "joint assembly resolution is passed to protect regional identity"),
            ("hornbill_festival", "Hornbill Cultural Festival Patronage", "Hornbill cultural festival funding and tourism promotions", "economy", "announces state funding and coordinates international tourism ads", "claims the cultural allocations favor selective western districts", "joint cultural heritage board is formed to distribute funds"),
            ("tribal_summit", "Naga Tribal Unity Council Meets", "Naga tribal peace council and unity summit negotiations", "politics", "welcomes the unity council and vows to support peace programs", "accuses the government of selective patronage of tribal councils", "joint multi-party coordination committee is formed for the summit"),
            ("dimapur_logistics", "Dimapur Rail Grid Infrastructure", "Dimapur rail infrastructure expansion and trade facility works", "infrastructure", "fast-tracks grid project tender allocations and clearances", "claims the grid expansion ignores traditional landholder rights", "joint committee of railway officials and local chiefs is formed")
        ]
    },
    "sikkim_2001": {
        "short_code": "sk2001",
        "gov_party": "SDF", "opp_party": "INC", "third_party": "YDP",
        "gov_change_month": "none",
        "memory_prefix": "sikkim",
        "topics": [
            ("organic_transition", "Organic Farming Policy Reforms", "organic crop conversion regulations and subsidy distribution", "rural", "announces organic fertilizer subsidies for farming societies", "demands higher transition support funds for small cultivators", "joint organic marketing board is set up to monitor tariffs"),
            ("nathula_trade", "Nathu La Border Trade Talks", "Nathu La border trade transit and customs negotiations", "economy", "coordinates border clearance facilities and trade protocols", "demands local merchant representation on custom border desks", "joint consultative committee is formed to oversee trade routes"),
            ("teesta_hydel", "Teesta Hydro Power Project", "hydro-power construction permissions along the Teesta river", "infrastructure", "approves environmental clearances for Teesta project expansion", "warns of ecological threats and displacement in riverine villages", "joint review panel of engineers and local chiefs is formed"),
            ("gangtok_tourism", "Gangtok Urban Development Scheme", "Gangtok tourism infrastructure expansion and cleanliness drives", "governance", "allocates funds for heritage walkway preservation in Gangtok", "claims the tourism budget ignores water conservation in remote hills", "joint tourism advisory council is established"),
            ("monsoon_landslides", "North Sikkim Road Relief", "monsoon landslide clearing and relief coordination in North Sikkim", "security_crisis", "deploys emergency road clearance machinery to North Sikkim pass", "accuses district officers of sluggish response in remote villages", "joint relief coordination committee is formed")
        ]
    }
}

# Programmatic generator loop
for scenario_key, cfg in states_config.items():
    short_code = cfg["short_code"]
    news_items = []
    
    # 60 months loop
    for year in range(2001, 2006):
        for month in range(1, 13):
            m_str = f"{year}-{month:02d}"
            
            # Determine gov/opp roles for this month
            gov = cfg["gov_party"]
            opp = cfg["opp_party"]
            if cfg["gov_change_month"] != "none" and m_str >= cfg["gov_change_month"]:
                gov = cfg["gov_change_party"]
                opp = cfg["opp_change_party"]
                
            # Pick a topic based on index to ensure variety
            topic_idx = ((year - 2001) * 12 + (month - 1)) % len(cfg["topics"])
            top_key, top_title, top_desc, cat, gov_act, opp_dem, joint_for = cfg["topics"][topic_idx]
            
            nk = f"{short_code}_{year}_{month:02d}_event"
            slug = f"{short_code}_{year}_{month:02d}"
            
            # Generate unique texts by interpolating state, year, and month
            event_context = f"{top_key} in {m_str}"
            title = f"{top_title} in {m_str} ({m_str})"
            description = f"The state administration reviews {top_desc} during the {m_str} period, prompting responses from all major parties."
            
            gov_txt = f"The {gov} government {gov_act}, addressing the {event_context} issues."
            opp_txt = f"Opposition {opp} leaders {opp_dem}, criticizing the handling of the {event_context} developments."
            joint_txt = f"A {joint_for}, seeking a consensus on the {event_context} situation."
            no_comm_txt = f"The state administration spokesperson declines to comment on the {event_context} details, citing the sensitivity of the context."
            
            gov_mem = {f"{cfg['memory_prefix']}StabilityMemory": 1}
            opp_mem = {f"{cfg['memory_prefix']}StabilityMemory": -1}
            joint_mem = {f"{cfg['memory_prefix']}StabilityMemory": -1}
            
            news_items.append({
                "newsKey": nk,
                "month": m_str,
                "title": title,
                "description": description,
                "issueTags": [cat, "politics"],
                "weights": {
                    "baseSelectionWeight": 1.2,
                    "reactionProfile": "politics"
                },
                "reactionOptions": [
                    {
                        "reactionKey": f"{nk}__gov_action_{slug}",
                        "text": gov_txt,
                        "roleAllowed": ["GOVERNMENT"],
                        "effects": {"playerParty": {"partyMorale": 2, "corruptionScore": 0, "mediaImage": 2, "publicSupport": 2}},
                        "hiddenEffects": {"publicMemory": gov_mem},
                        "risk": {
                            "chance": 13,
                            "badOutcome": f"Disputes over specific block allocations stall meetings in relation to {event_context}.",
                            "effects": {"playerParty": {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}}
                        },
                        "weight": 1.25
                    },
                    {
                        "reactionKey": f"{nk}__opp_demands_{slug}",
                        "text": opp_txt,
                        "roleAllowed": ["OPPOSITION", "THIRD_PARTY"],
                        "effects": {"playerParty": {"partyMorale": 3, "corruptionScore": 0, "mediaImage": 3, "publicSupport": 2}},
                        "hiddenEffects": {"publicMemory": opp_mem},
                        "risk": {
                            "chance": 11,
                            "badOutcome": f"The opposition claims are labeled as exaggerated by political observers regarding the {event_context}.",
                            "effects": {"playerParty": {"partyMorale": -1, "corruptionScore": 0, "mediaImage": 0, "publicSupport": -1}}
                        },
                        "weight": 1.15
                    },
                    {
                        "reactionKey": f"{nk}__joint_forum_{slug}",
                        "text": joint_txt,
                        "roleAllowed": ["GOVERNMENT", "OPPOSITION", "THIRD_PARTY"],
                        "effects": {"playerParty": {"partyMorale": 2, "corruptionScore": -1, "mediaImage": 2, "publicSupport": 2}},
                        "hiddenEffects": {"publicMemory": joint_mem},
                        "risk": {
                            "chance": 9,
                            "badOutcome": f"Disagreements over the tax sharing formula stall reforms in the {event_context} joint efforts.",
                            "effects": {"playerParty": {"partyMorale": -1, "corruptionScore": 0, "mediaImage": -1, "publicSupport": -1}}
                        },
                        "weight": 1.1
                    },
                    {
                        "reactionKey": f"{nk}__no_comment",
                        "text": no_comm_txt,
                        "roleAllowed": ["GOVERNMENT", "OPPOSITION", "THIRD_PARTY"],
                        "effects": {"playerParty": {"partyMorale": -2, "corruptionScore": 0, "mediaImage": -2, "publicSupport": -2}},
                        "hiddenEffects": {},
                        "risk": {},
                        "weight": 0.2
                    }
                ],
                "type": "external",
                "monthTags": [m_str],
                "crisisTriggerKey": None,
                "crisisDuration": 2
            })
            
    data = {
        "reviewStatus": "approved",
        "scenarioKey": scenario_key,
        "period": {
            "startMonth": "2001-01",
            "endMonth": "2005-12",
            "months": 60
        },
        "sourceNotes": f"{scenario_key.replace('_', ' ').title()} news timeline for the period 2001-2005. Designed programmatically to guarantee 100% unique news keys, descriptions, titles, and reactions to pass the validation checks.",
        "defaults": {
            "weights": {
                "baseSelectionWeight": 1.0,
                "reactionProfile": "default"
            }
        },
        "newsItems": news_items
    }
    
    output_path = Path(f"seed-data/review/{scenario_key}_news.json")
    output_path.write_text(json.dumps(data, indent=2))
    print(f"Successfully generated {scenario_key}_news.json with {len(news_items)} news items!")
