import json

filepath = "seed-data/national/national_configs/2001.json"
with open(filepath, "r", encoding="utf-8") as f:
    data = json.load(f)

# State Elections schedule for 2001 era mapped to turns (1 turn = 1 month)
data["stateElections"] = [
    {
        "stateCode": "UP",
        "stateName": "Uttar Pradesh",
        "electionTurn": 15,
        "electionMonth": "March 2002",
        "totalAssemblySeats": 403,
        "totalLokSabhaSeats": 80,
        "scenarioKey": "uttar_pradesh_2001"
    },
    {
        "stateCode": "MAHARASHTRA",
        "stateName": "Maharashtra",
        "electionTurn": 46,
        "electionMonth": "October 2004",
        "totalAssemblySeats": 288,
        "totalLokSabhaSeats": 48,
        "scenarioKey": "maharashtra_2001"
    },
    {
        "stateCode": "BIHAR",
        "stateName": "Bihar",
        "electionTurn": 50,
        "electionMonth": "February 2005",
        "totalAssemblySeats": 243,
        "totalLokSabhaSeats": 40,
        "scenarioKey": "bihar_2001"
    },
    {
        "stateCode": "ASSAM",
        "stateName": "Assam",
        "electionTurn": 5,
        "electionMonth": "May 2001",
        "totalAssemblySeats": 126,
        "totalLokSabhaSeats": 14,
        "scenarioKey": "assam_2001"
    },
    {
        "stateCode": "KERALA",
        "stateName": "Kerala",
        "electionTurn": 5,
        "electionMonth": "May 2001",
        "totalAssemblySeats": 140,
        "totalLokSabhaSeats": 20,
        "scenarioKey": "kerala_2001"
    },
    {
        "stateCode": "TAMIL_NADU",
        "stateName": "Tamil Nadu",
        "electionTurn": 5,
        "electionMonth": "May 2001",
        "totalAssemblySeats": 234,
        "totalLokSabhaSeats": 39,
        "scenarioKey": "tamil_nadu_2001"
    },
    {
        "stateCode": "WEST_BENGAL",
        "stateName": "West Bengal",
        "electionTurn": 5,
        "electionMonth": "May 2001",
        "totalAssemblySeats": 294,
        "totalLokSabhaSeats": 42,
        "scenarioKey": "west_bengal_2000"
    },
    {
        "stateCode": "PUNJAB",
        "stateName": "Punjab",
        "electionTurn": 14,
        "electionMonth": "February 2002",
        "totalAssemblySeats": 117,
        "totalLokSabhaSeats": 13,
        "scenarioKey": "punjab_2001"
    },
    {
        "stateCode": "GUJARAT",
        "stateName": "Gujarat",
        "electionTurn": 24,
        "electionMonth": "December 2002",
        "totalAssemblySeats": 182,
        "totalLokSabhaSeats": 26,
        "scenarioKey": "gujarat_2001"
    },
    {
        "stateCode": "MADHYA_PRADESH",
        "stateName": "Madhya Pradesh",
        "electionTurn": 35,
        "electionMonth": "November 2003",
        "totalAssemblySeats": 230,
        "totalLokSabhaSeats": 29,
        "scenarioKey": "madhya_pradesh_2001"
    },
    {
        "stateCode": "RAJASTHAN",
        "stateName": "Rajasthan",
        "electionTurn": 36,
        "electionMonth": "December 2003",
        "totalAssemblySeats": 200,
        "totalLokSabhaSeats": 25,
        "scenarioKey": "rajasthan_2001"
    },
    {
        "stateCode": "DELHI",
        "stateName": "Delhi",
        "electionTurn": 36,
        "electionMonth": "December 2003",
        "totalAssemblySeats": 70,
        "totalLokSabhaSeats": 7,
        "scenarioKey": "delhi_2001"
    },
    {
        "stateCode": "ANDHRA_PRADESH",
        "stateName": "Andhra Pradesh",
        "electionTurn": 40,
        "electionMonth": "April 2004",
        "totalAssemblySeats": 294,
        "totalLokSabhaSeats": 25,
        "scenarioKey": "andhra_pradesh_2001"
    },
    {
        "stateCode": "KARNATAKA",
        "stateName": "Karnataka",
        "electionTurn": 41,
        "electionMonth": "May 2004",
        "totalAssemblySeats": 224,
        "totalLokSabhaSeats": 28,
        "scenarioKey": "karnataka_2001"
    },
    {
        "stateCode": "ODISHA",
        "stateName": "Odisha",
        "electionTurn": 40,
        "electionMonth": "April 2004",
        "totalAssemblySeats": 147,
        "totalLokSabhaSeats": 21,
        "scenarioKey": "odisha_2001"
    },
    {
        "stateCode": "JHARKHAND",
        "stateName": "Jharkhand",
        "electionTurn": 50,
        "electionMonth": "February 2005",
        "totalAssemblySeats": 81,
        "totalLokSabhaSeats": 14,
        "scenarioKey": "jharkhand_2001"
    },
    {
        "stateCode": "HARYANA",
        "stateName": "Haryana",
        "electionTurn": 50,
        "electionMonth": "February 2005",
        "totalAssemblySeats": 90,
        "totalLokSabhaSeats": 10,
        "scenarioKey": "haryana_2001"
    }
]

# State Issues for 2001 era
data["stateIssues"] = [
    # UP Issues
    {
        "id": "UP_CASTE_VIOLENCE",
        "stateCode": "UP",
        "title": "Caste Violence & Social Justice",
        "icon": "⚖️",
        "category": "SOCIAL_JUSTICE",
        "description": "Escalating inter-caste violence, Dalit atrocities, and friction over representation in state bureaucracy.",
        "baseImpact": 1.4
    },
    {
        "id": "UP_LAW_ORDER",
        "stateCode": "UP",
        "title": "Law & Order Collapse & Mafia Raj",
        "icon": "🚔",
        "category": "SECURITY",
        "description": "Organized extortion gangs, political patronage for crime lords, and rampant highway robberies.",
        "baseImpact": 1.5
    },
    {
        "id": "UP_AGRARIAN_DISTRESS",
        "stateCode": "UP",
        "title": "Sugarcane Arrears & Agrarian Distress",
        "icon": "🌾",
        "category": "AGRICULTURE",
        "description": "Millions owed to sugarcane growers by defaulting private sugar mills, triggering farmer demonstrations.",
        "baseImpact": 1.3
    },
    {
        "id": "UP_MANDAL_POLITICS",
        "stateCode": "UP",
        "title": "Identity Polarization & Reservation Clashes",
        "icon": "🗳️",
        "category": "POLITICAL",
        "description": "High-voltage electoral mobilization around backward class sub-quotas and upper caste backlash.",
        "baseImpact": 1.2
    },
    {
        "id": "UP_POWER_CRISIS",
        "stateCode": "UP",
        "title": "Chronic Power Deficit & Grid Collapse",
        "icon": "⚡",
        "category": "INFRASTRUCTURE",
        "description": "Severe load-shedding of 16+ hours a day in Purvanchal and Bundelkhand, paralyzing local workshops.",
        "baseImpact": 1.1
    },

    # BIHAR Issues
    {
        "id": "BIHAR_JUNGLE_RAJ",
        "stateCode": "BIHAR",
        "title": "'Jungle Raj' & Lawlessness",
        "icon": "🚨",
        "category": "SECURITY",
        "description": "Kidnapping for ransom operates as a parallel industry with alleged political impunity across Patna and districts.",
        "baseImpact": 1.6
    },
    {
        "id": "BIHAR_CASTE_POLARIZATION",
        "stateCode": "BIHAR",
        "title": "Caste Polarization & Private Senas",
        "icon": "⚔️",
        "category": "SOCIAL_JUSTICE",
        "description": "Feudal private militias and armed agrarian uprisings clash in central Bihar's rural heartland.",
        "baseImpact": 1.5
    },
    {
        "id": "BIHAR_FLOOD_DISASTER",
        "stateCode": "BIHAR",
        "title": "Kosi Flood Devastation & Embankment Breaches",
        "icon": "🌊",
        "category": "DISASTER",
        "description": "Annual monsoon inundations sweep North Bihar villages amid corruption allegations in embankment contracts.",
        "baseImpact": 1.3
    },
    {
        "id": "BIHAR_EDUCATION_CRISIS",
        "stateCode": "BIHAR",
        "title": "Education Decay & Examination Paper Leaks",
        "icon": "📚",
        "category": "EDUCATION",
        "description": "Teacher absenteeism, ghost colleges, and widespread cheating scandals erode state degree credibility.",
        "baseImpact": 1.2
    },
    {
        "id": "BIHAR_INFRA_COLLAPSE",
        "stateCode": "BIHAR",
        "title": "Potholed Highways & Healthcare Collapse",
        "icon": "🏥",
        "category": "INFRASTRUCTURE",
        "description": "Dilapidated National and State highways isolate remote blocks, while primary healthcare centers lack doctors.",
        "baseImpact": 1.4
    },

    # MAHARASHTRA Issues
    {
        "id": "MH_VIDARBHA_FARMER_CRISIS",
        "stateCode": "MAHARASHTRA",
        "title": "Vidarbha Agrarian Crisis & Farmer Suicides",
        "icon": "🌾",
        "category": "AGRICULTURE",
        "description": "BT Cotton crop failures, spiraling moneylender debts, and unseasonal weather trigger alarming suicide rates.",
        "baseImpact": 1.6
    },
    {
        "id": "MH_MUMBAI_INFRA_STRAIN",
        "stateCode": "MAHARASHTRA",
        "title": "Mumbai Infrastructure Strain & Slum Transit",
        "icon": "🚆",
        "category": "URBAN",
        "description": "Overcrowded local trains, slum rehabilitation standoffs, and seasonal flood vulnerability in the financial capital.",
        "baseImpact": 1.3
    },
    {
        "id": "MH_COALITION_FRICTION",
        "stateCode": "MAHARASHTRA",
        "title": "Coalition Instability & Alliance Friction",
        "icon": "🤝",
        "category": "POLITICAL",
        "description": "Constant skirmishes between Congress-NCP partners and vocal regional resistance from the Shiv Sena-BJP front.",
        "baseImpact": 1.2
    },
    {
        "id": "MH_MILL_WORKERS_CRISIS",
        "stateCode": "MAHARASHTRA",
        "title": "Girni Kamgar (Mill Workers) Displacement",
        "icon": "🏭",
        "category": "LABOR",
        "description": "Redevelopment of Central Mumbai textile mill lands into luxury complexes leaves thousands of workers unpaid.",
        "baseImpact": 1.3
    },
    {
        "id": "MH_REGIONAL_IMBALANCE",
        "stateCode": "MAHARASHTRA",
        "title": "Development Gap: Western MH vs Marathwada",
        "icon": "⚖️",
        "category": "ECONOMY",
        "description": "Disproportionate allocation of state irrigation and industrial budgets favoring sugar belt baronies.",
        "baseImpact": 1.1
    }
]

with open(filepath, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("Successfully injected stateElections and stateIssues into 2001.json")
