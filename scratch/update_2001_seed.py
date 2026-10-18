import json

data = {
  "era": 2001,
  "title": "The NDA Experiment",
  "description": "Vajpayee leads the 24-party NDA coalition through economic reforms, national security challenges, and political turbulence (2001-2005).",
  "supportedIdeologies": [
    "DEVELOPMENTAL_PROGRESSIVE",
    "NATIONALIST_CONSERVATIVE",
    "CENTRIST_SECULAR",
    "LEFT_SOCIALIST",
    "REGIONAL_SOCIALIST"
  ],
  "alliances": [
    {
      "key": "NDA",
      "name": "National Democratic Alliance",
      "color": "#FF9933",
      "leaderParty": "bjp",
      "initialParties": ["bjp", "shiv_sena", "akali_dal", "jdu", "tdp", "pmc", "others"]
    },
    {
      "key": "INC",
      "name": "Congress & Allies",
      "color": "#00BFFF",
      "leaderParty": "inc",
      "initialParties": ["inc"]
    },
    {
      "key": "LEFT",
      "name": "Left Front",
      "color": "#CC0000",
      "leaderParty": "cpim",
      "initialParties": ["cpim", "cpi", "rsp", "fb"]
    },
    {
      "key": "INDEPENDENT",
      "name": "Unaffiliated & Regional",
      "color": "#888888",
      "leaderParty": None,
      "initialParties": ["sp", "bsp", "rjd", "dmk", "aidmk", "ydp", "ncp", "others"]
    }
  ],
  "parties": [
    {
      "partyKey": "ydp",
      "name": "Youth Development Party",
      "shortName": "YDP",
      "ideology": "DEVELOPMENTAL_PROGRESSIVE",
      "initialAllianceKey": "INDEPENDENT",
      "initialContent": 80,
      "isPlayerSelectable": True,
      "color": "#7C3AED",
      "icon": "🐘",
      "description": "Upstart progressive party holding ~10-12% vote share across states.",
      "activeInAllStates": True,
      "defaultVoteShare": 10
    },
    {
      "partyKey": "bjp",
      "name": "Bharatiya Janata Party",
      "shortName": "BJP",
      "ideology": "NATIONALIST_CONSERVATIVE",
      "initialAllianceKey": "NDA",
      "initialContent": 72,
      "isPlayerSelectable": True,
      "color": "#FF9933",
      "icon": "🪷",
      "description": "Leader of NDA ruling coalition.",
      "activeInAllStates": False,
      "activeStates": ["UP", "Maharashtra", "Gujarat", "Rajasthan", "Madhya Pradesh", "Delhi", "Uttarakhand", "Himachal Pradesh", "Jharkhand", "Chhattisgarh", "Bihar", "Karnataka", "Assam", "Punjab", "Goa", "Puducherry & UTs"]
    },
    {
      "partyKey": "inc",
      "name": "Indian National Congress",
      "shortName": "INC",
      "ideology": "CENTRIST_SECULAR",
      "initialAllianceKey": "INC",
      "initialContent": 58,
      "isPlayerSelectable": True,
      "color": "#00BFFF",
      "icon": "✋",
      "description": "Main opposition party rebuilding under Sonia Gandhi.",
      "activeInAllStates": False,
      "activeStates": ["UP", "Maharashtra", "Bihar", "Tamil Nadu", "Andhra Pradesh", "Madhya Pradesh", "Karnataka", "Gujarat", "Rajasthan", "Odisha", "Kerala", "Jharkhand", "Assam", "Punjab", "Chhattisgarh", "Haryana", "Delhi", "Uttarakhand", "Himachal Pradesh", "Manipur", "Meghalaya", "Arunachal Pradesh", "Puducherry & UTs"]
    },
    {
      "partyKey": "cpim",
      "name": "Communist Party of India (Marxist)",
      "shortName": "CPM",
      "ideology": "LEFT_SOCIALIST",
      "initialAllianceKey": "LEFT",
      "initialContent": 68,
      "isPlayerSelectable": True,
      "color": "#CC0000",
      "icon": "🌾",
      "description": "Leader of Left Front, strong in Bengal, Tripura and Kerala.",
      "activeInAllStates": False,
      "activeStates": ["West Bengal", "Kerala", "Tamil Nadu", "Tripura"]
    },
    {
      "partyKey": "sp",
      "name": "Samajwadi Party",
      "shortName": "SP",
      "ideology": "REGIONAL_SOCIALIST",
      "initialAllianceKey": "INDEPENDENT",
      "initialContent": 55,
      "isPlayerSelectable": True,
      "color": "#FF0000",
      "icon": "🚲",
      "description": "UP stronghold party with significant Lok Sabha weight.",
      "activeInAllStates": False,
      "activeStates": ["UP", "Uttarakhand"]
    },
    {
      "partyKey": "bsp",
      "name": "Bahujan Samaj Party",
      "shortName": "BSP",
      "ideology": "REGIONAL_SOCIALIST",
      "initialAllianceKey": "INDEPENDENT",
      "initialContent": 62,
      "isPlayerSelectable": True,
      "color": "#1565C0",
      "icon": "🐘",
      "description": "Dalit movement party in UP and Central India.",
      "activeInAllStates": False,
      "activeStates": ["UP", "Uttarakhand", "Madhya Pradesh", "Rajasthan"]
    },
    {
      "partyKey": "rjd",
      "name": "Rashtriya Janata Dal",
      "shortName": "RJD",
      "ideology": "REGIONAL_SOCIALIST",
      "initialAllianceKey": "INDEPENDENT",
      "initialContent": 60,
      "isPlayerSelectable": True,
      "color": "#007A3D",
      "icon": "🏮",
      "description": "Bihar regional force led by Lalu Prasad.",
      "activeInAllStates": False,
      "activeStates": ["Bihar", "Jharkhand"]
    }
  ],
  "stateSeatData": [
    {
      "stateName": "Uttar Pradesh",
      "totalSeats": 80,
      "rulingPartyKey": "bjp",
      "oppositionPartyKey": "sp",
      "supportPercentages": { "bjp": 35, "sp": 28, "bsp": 24, "ydp": 13 },
      "initialSeats": { "bjp": 28, "sp": 22, "bsp": 19, "ydp": 11 }
    },
    {
      "stateName": "Maharashtra",
      "totalSeats": 48,
      "rulingPartyKey": "bjp",
      "oppositionPartyKey": "inc",
      "supportPercentages": { "bjp": 28, "inc": 26, "shiv_sena": 25, "ncp": 11, "ydp": 10 },
      "initialSeats": { "bjp": 13, "inc": 13, "shiv_sena": 12, "ncp": 5, "ydp": 5 }
    },
    {
      "stateName": "West Bengal",
      "totalSeats": 42,
      "rulingPartyKey": "cpim",
      "oppositionPartyKey": "aitc",
      "supportPercentages": { "cpim": 50, "aitc": 24, "bjp": 16, "ydp": 10 },
      "initialSeats": { "cpim": 21, "aitc": 10, "bjp": 7, "ydp": 4 }
    },
    {
      "stateName": "Bihar",
      "totalSeats": 40,
      "rulingPartyKey": "rjd",
      "oppositionPartyKey": "bjp",
      "supportPercentages": { "rjd": 42, "bjp": 30, "jdu": 15, "ydp": 13 },
      "initialSeats": { "rjd": 17, "bjp": 12, "jdu": 6, "ydp": 5 }
    },
    {
      "stateName": "Tamil Nadu",
      "totalSeats": 39,
      "rulingPartyKey": "dmk",
      "oppositionPartyKey": "aidmk",
      "supportPercentages": { "dmk": 32, "aidmk": 28, "inc": 18, "bjp": 12, "ydp": 10 },
      "initialSeats": { "dmk": 12, "aidmk": 11, "inc": 7, "bjp": 5, "ydp": 4 }
    },
    {
      "stateName": "Andhra Pradesh",
      "totalSeats": 42,
      "rulingPartyKey": "tdp",
      "oppositionPartyKey": "inc",
      "supportPercentages": { "tdp": 65, "inc": 15, "bjp": 10, "ydp": 10 },
      "initialSeats": { "tdp": 27, "inc": 6, "bjp": 4, "ydp": 5 }
    },
    {
      "stateName": "Madhya Pradesh",
      "totalSeats": 29,
      "rulingPartyKey": "bjp",
      "oppositionPartyKey": "inc",
      "supportPercentages": { "bjp": 76, "inc": 14, "ydp": 10 },
      "initialSeats": { "bjp": 22, "inc": 4, "ydp": 3 }
    },
    {
      "stateName": "Karnataka",
      "totalSeats": 28,
      "rulingPartyKey": "bjp",
      "oppositionPartyKey": "inc",
      "supportPercentages": { "bjp": 46, "inc": 33, "jdu": 11, "ydp": 10 },
      "initialSeats": { "bjp": 13, "inc": 9, "jdu": 3, "ydp": 3 }
    },
    {
      "stateName": "Gujarat",
      "totalSeats": 26,
      "rulingPartyKey": "bjp",
      "oppositionPartyKey": "inc",
      "supportPercentages": { "bjp": 73, "inc": 17, "ydp": 10 },
      "initialSeats": { "bjp": 19, "inc": 4, "ydp": 3 }
    },
    {
      "stateName": "Rajasthan",
      "totalSeats": 25,
      "rulingPartyKey": "bjp",
      "oppositionPartyKey": "inc",
      "supportPercentages": { "bjp": 60, "inc": 30, "ydp": 10 },
      "initialSeats": { "bjp": 15, "inc": 7, "ydp": 3 }
    },
    {
      "stateName": "Odisha",
      "totalSeats": 21,
      "rulingPartyKey": "bjd",
      "oppositionPartyKey": "inc",
      "supportPercentages": { "bjd": 43, "inc": 24, "bjp": 19, "ydp": 14 },
      "initialSeats": { "bjd": 9, "inc": 5, "bjp": 4, "ydp": 3 }
    },
    {
      "stateName": "Kerala",
      "totalSeats": 20,
      "rulingPartyKey": "inc",
      "oppositionPartyKey": "cpim",
      "supportPercentages": { "inc": 40, "cpim": 40, "ydp": 20 },
      "initialSeats": { "inc": 8, "cpim": 8, "ydp": 4 }
    },
    {
      "stateName": "Jharkhand",
      "totalSeats": 14,
      "rulingPartyKey": "bjp",
      "oppositionPartyKey": "jmm",
      "supportPercentages": { "bjp": 57, "jmm": 15, "inc": 15, "ydp": 13 },
      "initialSeats": { "bjp": 8, "jmm": 2, "inc": 2, "ydp": 2 }
    },
    {
      "stateName": "Assam",
      "totalSeats": 14,
      "rulingPartyKey": "inc",
      "oppositionPartyKey": "agp",
      "supportPercentages": { "inc": 65, "agp": 15, "bjp": 10, "ydp": 10 },
      "initialSeats": { "inc": 9, "agp": 2, "bjp": 1, "ydp": 2 }
    },
    {
      "stateName": "Punjab",
      "totalSeats": 13,
      "rulingPartyKey": "akali_dal",
      "oppositionPartyKey": "inc",
      "supportPercentages": { "akali_dal": 58, "inc": 27, "ydp": 15 },
      "initialSeats": { "akali_dal": 7, "inc": 4, "ydp": 2 }
    },
    {
      "stateName": "Chhattisgarh",
      "totalSeats": 11,
      "rulingPartyKey": "bjp",
      "oppositionPartyKey": "inc",
      "supportPercentages": { "bjp": 63, "inc": 27, "ydp": 10 },
      "initialSeats": { "bjp": 7, "inc": 3, "ydp": 1 }
    },
    {
      "stateName": "Haryana",
      "totalSeats": 10,
      "rulingPartyKey": "inld",
      "oppositionPartyKey": "inc",
      "supportPercentages": { "inld": 50, "inc": 30, "bjp": 10, "ydp": 10 },
      "initialSeats": { "inld": 5, "inc": 3, "bjp": 1, "ydp": 1 }
    },
    {
      "stateName": "Delhi",
      "totalSeats": 7,
      "rulingPartyKey": "bjp",
      "oppositionPartyKey": "inc",
      "supportPercentages": { "bjp": 85, "ydp": 15 },
      "initialSeats": { "bjp": 6, "ydp": 1 }
    },
    {
      "stateName": "Jammu & Kashmir",
      "totalSeats": 6,
      "rulingPartyKey": "nc",
      "oppositionPartyKey": "bjp",
      "supportPercentages": { "nc": 66, "bjp": 17, "ydp": 17 },
      "initialSeats": { "nc": 4, "bjp": 1, "ydp": 1 }
    },
    {
      "stateName": "Uttarakhand",
      "totalSeats": 5,
      "rulingPartyKey": "bjp",
      "oppositionPartyKey": "inc",
      "supportPercentages": { "bjp": 60, "inc": 20, "ydp": 20 },
      "initialSeats": { "bjp": 3, "inc": 1, "ydp": 1 }
    },
    {
      "stateName": "Himachal Pradesh",
      "totalSeats": 4,
      "rulingPartyKey": "bjp",
      "oppositionPartyKey": "inc",
      "supportPercentages": { "bjp": 75, "inc": 25 },
      "initialSeats": { "bjp": 3, "inc": 1 }
    },
    {
      "stateName": "Goa",
      "totalSeats": 2,
      "rulingPartyKey": "bjp",
      "oppositionPartyKey": "inc",
      "supportPercentages": { "bjp": 100 },
      "initialSeats": { "bjp": 2 }
    },
    {
      "stateName": "Manipur",
      "totalSeats": 2,
      "rulingPartyKey": "inc",
      "oppositionPartyKey": "others",
      "supportPercentages": { "inc": 100 },
      "initialSeats": { "inc": 2 }
    },
    {
      "stateName": "Meghalaya",
      "totalSeats": 2,
      "rulingPartyKey": "inc",
      "oppositionPartyKey": "others",
      "supportPercentages": { "inc": 100 },
      "initialSeats": { "inc": 2 }
    },
    {
      "stateName": "Tripura",
      "totalSeats": 2,
      "rulingPartyKey": "cpim",
      "oppositionPartyKey": "inc",
      "supportPercentages": { "cpim": 100 },
      "initialSeats": { "cpim": 2 }
    },
    {
      "stateName": "Arunachal Pradesh",
      "totalSeats": 2,
      "rulingPartyKey": "inc",
      "oppositionPartyKey": "bjp",
      "supportPercentages": { "inc": 100 },
      "initialSeats": { "inc": 2 }
    },
    {
      "stateName": "Nagaland",
      "totalSeats": 1,
      "rulingPartyKey": "others",
      "oppositionPartyKey": "inc",
      "supportPercentages": { "others": 100 },
      "initialSeats": { "others": 1 }
    },
    {
      "stateName": "Mizoram",
      "totalSeats": 1,
      "rulingPartyKey": "others",
      "oppositionPartyKey": "inc",
      "supportPercentages": { "others": 100 },
      "initialSeats": { "others": 1 }
    },
    {
      "stateName": "Sikkim",
      "totalSeats": 1,
      "rulingPartyKey": "others",
      "oppositionPartyKey": "inc",
      "supportPercentages": { "others": 100 },
      "initialSeats": { "others": 1 }
    },
    {
      "stateName": "Puducherry & UTs",
      "totalSeats": 7,
      "rulingPartyKey": "inc",
      "oppositionPartyKey": "bjp",
      "supportPercentages": { "inc": 57, "bjp": 29, "ydp": 14 },
      "initialSeats": { "inc": 4, "bjp": 2, "ydp": 1 }
    }
  ]
}

# 10 Seasons with 5 Events per Season using baselineIdeologyEffects & publicOpinionShift { supportForGovt, morale }
seasons_data = []

# Helper to format reactions with publicOpinionShiftModifier
def make_reaction(key, label, content_shift, power_shift, govt_mod=0, morale_mod=0):
    return {
        "key": key,
        "label": label,
        "partyContentShift": content_shift,
        "partyPowerShift": power_shift,
        "publicOpinionShiftModifier": {
            "supportForGovt": govt_mod,
            "morale": morale_mod
        }
    }

events_raw = [
  # Season 1
  [
    {
      "eventKey": "2001_s1_ev1_kutch_earthquake",
      "headline": "Devastating Kutch Earthquake",
      "category": "DISASTER",
      "historicalDate": "January 26, 2001",
      "description": "A massive 7.7 magnitude earthquake strikes Kutch, Gujarat, killing over 20,000 people and devastating infrastructure.",
      "baselineIdeologyEffects": {
        "NATIONALIST_CONSERVATIVE": { "content": -4, "power": 0 },
        "CENTRIST_SECULAR": { "content": 4, "power": 0 },
        "DEVELOPMENTAL_PROGRESSIVE": { "content": 6, "power": 0 },
        "LEFT_SOCIALIST": { "content": 2, "power": 0 },
        "REGIONAL_SOCIALIST": { "content": 2, "power": 0 }
      },
      "publicOpinionShift": { "supportForGovt": -6, "morale": -12 },
      "reactions": [
        make_reaction("SUPPORT_GOVT", "Support Govt Relief Operations", 4, 0, govt_mod=4, morale_mod=4),
        make_reaction("AGITATE", "Agitate Against Inadequate Relief Preparedness", 8, 0, govt_mod=-6, morale_mod=-2),
        make_reaction("OPPOSE", "Demand Judicial Probe into Building Code Violations", 5, 0, govt_mod=-4, morale_mod=0),
        make_reaction("NEUTRAL", "Dispatch YDP Aid Teams Without Public Statements", 2, 0, govt_mod=1, morale_mod=2)
      ]
    },
    {
      "eventKey": "2001_s1_ev2_ketan_parekh_scam",
      "headline": "Stock Market Crash & Ketan Parekh Scam",
      "category": "FINANCE",
      "historicalDate": "March 2001",
      "description": "Stock market collapses following revelations of circular trading, bank fund rigging, and Madhavpura Bank failure.",
      "baselineIdeologyEffects": {
        "NATIONALIST_CONSERVATIVE": { "content": -8, "power": 0 },
        "CENTRIST_SECULAR": { "content": 8, "power": 0 },
        "LEFT_SOCIALIST": { "content": 6, "power": 0 },
        "REGIONAL_SOCIALIST": { "content": 4, "power": 0 },
        "DEVELOPMENTAL_PROGRESSIVE": { "content": 5, "power": 0 }
      },
      "publicOpinionShift": { "supportForGovt": -10, "morale": -8 },
      "reactions": [
        make_reaction("SUPPORT_GOVT", "Support Finance Ministry Regulatory Reforms", -2, 0, govt_mod=4, morale_mod=2),
        make_reaction("AGITATE", "Lead Nationwide Protests for Small Investors", 10, 0, govt_mod=-8, morale_mod=3),
        make_reaction("OPPOSE", "Demand Resignation of Finance Minister", 8, 0, govt_mod=-6, morale_mod=-2),
        make_reaction("NEUTRAL", "Issue Press Release Calling for SEBI Autonomy", 1, 0, govt_mod=0, morale_mod=1)
      ]
    },
    {
      "eventKey": "2001_s1_ev3_tehelka_sting",
      "headline": "Tehelka Defense Procurement Sting Operation",
      "category": "CORRUPTION",
      "historicalDate": "March 2001",
      "description": "Undercover journalists expose bribery in military contracts, triggering high-profile political resignations.",
      "baselineIdeologyEffects": {
        "NATIONALIST_CONSERVATIVE": { "content": -12, "power": -2 },
        "CENTRIST_SECULAR": { "content": 14, "power": 1 },
        "REGIONAL_SOCIALIST": { "content": 8, "power": 0 },
        "DEVELOPMENTAL_PROGRESSIVE": { "content": 10, "power": 0 },
        "LEFT_SOCIALIST": { "content": 8, "power": 0 }
      },
      "publicOpinionShift": { "supportForGovt": -15, "morale": -10 },
      "reactions": [
        make_reaction("SUPPORT_GOVT", "Support Inquiry Commission Setup", -6, 0, govt_mod=-2, morale_mod=2),
        make_reaction("AGITATE", "Launch Nationwide Anti-Corruption March", 12, 1, govt_mod=-10, morale_mod=4),
        make_reaction("OPPOSE", "Demand Immediate Dissolution of Lok Sabha", 9, 0, govt_mod=-12, morale_mod=-4),
        make_reaction("NEUTRAL", "Call for Institutional Defense Reform", 3, 0, govt_mod=0, morale_mod=2)
      ]
    },
    {
      "eventKey": "2001_s1_ev4_agra_summit",
      "headline": "Agra Peace Summit (Vajpayee - Musharraf)",
      "category": "POLITICAL",
      "historicalDate": "July 2001",
      "description": "High-stakes summit in Agra between PM Vajpayee and President Musharraf ends without a joint declaration over Kashmir.",
      "baselineIdeologyEffects": {
        "NATIONALIST_CONSERVATIVE": { "content": -3, "power": 0 },
        "CENTRIST_SECULAR": { "content": 4, "power": 0 },
        "LEFT_SOCIALIST": { "content": 3, "power": 0 },
        "DEVELOPMENTAL_PROGRESSIVE": { "content": 2, "power": 0 },
        "REGIONAL_SOCIALIST": { "content": 2, "power": 0 }
      },
      "publicOpinionShift": { "supportForGovt": -2, "morale": 2 },
      "reactions": [
        make_reaction("SUPPORT_GOVT", "Back Prime Minister's Firm Stance on Cross-Border Terror", 6, 0, govt_mod=6, morale_mod=4),
        make_reaction("AGITATE", "Protest Failure to Secure Firm Anti-Terror Guarantees", 5, 0, govt_mod=-4, morale_mod=-2),
        make_reaction("OPPOSE", "Criticize Ill-Prepared Diplomatic Strategy", 4, 0, govt_mod=-3, morale_mod=0),
        make_reaction("NEUTRAL", "Commend Continued Dialogue & Peace Process", 2, 0, govt_mod=2, morale_mod=3)
      ]
    },
    {
      "eventKey": "2001_s1_ev5_gsat1_launch",
      "headline": "ISRO Successfully Launches GSLV-D1 / GSAT-1",
      "category": "ACHIEVEMENT",
      "historicalDate": "April 2001",
      "description": "ISRO achieves milestone with first launch of Geosynchronous Satellite Launch Vehicle from Sriharikota.",
      "baselineIdeologyEffects": {
        "NATIONALIST_CONSERVATIVE": { "content": 6, "power": 0 },
        "CENTRIST_SECULAR": { "content": 2, "power": 0 },
        "DEVELOPMENTAL_PROGRESSIVE": { "content": 6, "power": 0 },
        "LEFT_SOCIALIST": { "content": 2, "power": 0 },
        "REGIONAL_SOCIALIST": { "content": 2, "power": 0 }
      },
      "publicOpinionShift": { "supportForGovt": 6, "morale": 12 },
      "reactions": [
        make_reaction("SUPPORT_GOVT", "Congratulate ISRO Scientists & Prime Minister", 5, 0, govt_mod=4, morale_mod=5),
        make_reaction("AGITATE", "Highlight Need for Higher R&D & Tech Budget", 4, 0, govt_mod=0, morale_mod=3),
        make_reaction("OPPOSE", "Credit Previous Administrations for Foundation", 3, 0, govt_mod=-2, morale_mod=2),
        make_reaction("NEUTRAL", "Issue Congratulatory Statement on Space Mission", 2, 0, govt_mod=1, morale_mod=2)
      ]
    }
  ],
  # Season 2
  [
    {
      "eventKey": "2001_s2_ev1_enron_dabhol_crisis",
      "headline": "Enron Dabhol Power Plant Collapse",
      "category": "FINANCE",
      "historicalDate": "July 2001",
      "description": "Dabhol Power Company shuts down operations after power tariff disputes, leaving state utility MSEB in deep debt.",
      "baselineIdeologyEffects": {
        "NATIONALIST_CONSERVATIVE": { "content": -5, "power": 0 },
        "CENTRIST_SECULAR": { "content": -3, "power": 0 },
        "LEFT_SOCIALIST": { "content": 8, "power": 0 },
        "REGIONAL_SOCIALIST": { "content": 5, "power": 0 },
        "DEVELOPMENTAL_PROGRESSIVE": { "content": 4, "power": 0 }
      },
      "publicOpinionShift": { "supportForGovt": -8, "morale": -6 },
      "reactions": [
        make_reaction("SUPPORT_GOVT", "Support Govt Plan to Restructure Power Contracts", 2, 0, govt_mod=4, morale_mod=2),
        make_reaction("AGITATE", "Lead Workers Protests Against Foreign Power Monopolies", 8, 0, govt_mod=-6, morale_mod=3),
        make_reaction("OPPOSE", "Blame State Govt Mismanagement & High Tariffs", 6, 0, govt_mod=-5, morale_mod=0),
        make_reaction("NEUTRAL", "Advocate for Renewable Energy Transition Plan", 3, 0, govt_mod=1, morale_mod=2)
      ]
    },
    {
      "eventKey": "2001_s2_ev2_simi_uapa_ban",
      "headline": "Ban on Students Islamic Movement of India (SIMI)",
      "category": "POLITICAL",
      "historicalDate": "September 2001",
      "description": "Union Home Ministry bans SIMI under Unlawful Activities Prevention Act following anti-national activities.",
      "baselineIdeologyEffects": {
        "NATIONALIST_CONSERVATIVE": { "content": 8, "power": 0 },
        "CENTRIST_SECULAR": { "content": 2, "power": 0 },
        "REGIONAL_SOCIALIST": { "content": -4, "power": 0 },
        "LEFT_SOCIALIST": { "content": -4, "power": 0 },
        "DEVELOPMENTAL_PROGRESSIVE": { "content": 3, "power": 0 }
      },
      "publicOpinionShift": { "supportForGovt": 8, "morale": 4 },
      "reactions": [
        make_reaction("SUPPORT_GOVT", "Fully Endorse Ban on Extremist Groups", 7, 0, govt_mod=6, morale_mod=4),
        make_reaction("AGITATE", "Demand Strict Safeguards Against Misuse of Law", 5, 0, govt_mod=-3, morale_mod=2),
        make_reaction("OPPOSE", "Question Procedure & Demand Special Judicial Review", -2, 0, govt_mod=-5, morale_mod=-2),
        make_reaction("NEUTRAL", "Call for Zero Tolerance on Terrorism and Hate Speech", 3, 0, govt_mod=2, morale_mod=2)
      ]
    },
    {
      "eventKey": "2001_s2_ev3_post_911_diplomacy",
      "headline": "Post-9/11 Global Anti-Terror Security Shift",
      "category": "POLITICAL",
      "historicalDate": "September 2001",
      "description": "Following 9/11 attacks in US, India offers full intelligence cooperation, reframing cross-border terror in South Asia.",
      "baselineIdeologyEffects": {
        "NATIONALIST_CONSERVATIVE": { "content": 7, "power": 0 },
        "CENTRIST_SECULAR": { "content": 4, "power": 0 },
        "DEVELOPMENTAL_PROGRESSIVE": { "content": 5, "power": 0 },
        "LEFT_SOCIALIST": { "content": -2, "power": 0 },
        "REGIONAL_SOCIALIST": { "content": 2, "power": 0 }
      },
      "publicOpinionShift": { "supportForGovt": 10, "morale": 6 },
      "reactions": [
        make_reaction("SUPPORT_GOVT", "Support Govt Alignment with Global Anti-Terror Coalition", 6, 0, govt_mod=5, morale_mod=4),
        make_reaction("AGITATE", "Demand Immediate Military Action Against Terror Camps", 8, 0, govt_mod=4, morale_mod=6),
        make_reaction("OPPOSE", "Warn Against Strategic Over-Reliance on Foreign Powers", 3, 0, govt_mod=-4, morale_mod=0),
        make_reaction("NEUTRAL", "Urge Non-Aligned Diplomatic Equilibrium", 2, 0, govt_mod=1, morale_mod=2)
      ]
    },
    {
      "eventKey": "2001_s2_ev4_golden_quadrilateral_phase1",
      "headline": "Golden Quadrilateral Highway Project Acceleration",
      "category": "ACHIEVEMENT",
      "historicalDate": "November 2001",
      "description": "NDA Govt accelerates construction of 5,846 km 4-lane highway network connecting Delhi, Mumbai, Chennai, and Kolkata.",
      "baselineIdeologyEffects": {
        "NATIONALIST_CONSERVATIVE": { "content": 10, "power": 1 },
        "CENTRIST_SECULAR": { "content": -2, "power": 0 },
        "DEVELOPMENTAL_PROGRESSIVE": { "content": 8, "power": 0 },
        "LEFT_SOCIALIST": { "content": -2, "power": 0 },
        "REGIONAL_SOCIALIST": { "content": 3, "power": 0 }
      },
      "publicOpinionShift": { "supportForGovt": 12, "morale": 10 },
      "reactions": [
        make_reaction("SUPPORT_GOVT", "Commend Landmark Infrastructure Expansion", 6, 0, govt_mod=5, morale_mod=4),
        make_reaction("AGITATE", "Demand Fair Compensation & Rehabilitation for Farmers", 7, 0, govt_mod=-2, morale_mod=3),
        make_reaction("OPPOSE", "Audit Highway Tender Allocations & Cost Overruns", 4, 0, govt_mod=-4, morale_mod=0),
        make_reaction("NEUTRAL", "Propose Feeder Roads Connectivity for Villages", 3, 0, govt_mod=1, morale_mod=2)
      ]
    },
    {
      "eventKey": "2001_s2_ev5_parliament_attack",
      "headline": "Terrorist Attack on Indian Parliament",
      "category": "DISASTER",
      "historicalDate": "December 13, 2001",
      "description": "Armed terrorists attack Parliament Complex in Delhi; security forces neutralize attackers, preventing massive loss.",
      "baselineIdeologyEffects": {
        "NATIONALIST_CONSERVATIVE": { "content": 6, "power": 2 },
        "CENTRIST_SECULAR": { "content": 5, "power": 0 },
        "DEVELOPMENTAL_PROGRESSIVE": { "content": 6, "power": 0 },
        "LEFT_SOCIALIST": { "content": 4, "power": 0 },
        "REGIONAL_SOCIALIST": { "content": 4, "power": 0 }
      },
      "publicOpinionShift": { "supportForGovt": 14, "morale": 15 },
      "reactions": [
        make_reaction("SUPPORT_GOVT", "Stand United Behind Government's Defense Mobilization", 8, 0, govt_mod=8, morale_mod=6),
        make_reaction("AGITATE", "Demand Immediate Retaliatory Military Strike", 10, 1, govt_mod=6, morale_mod=8),
        make_reaction("OPPOSE", "Demand Security Audit & Home Minister Accountability", 2, 0, govt_mod=-6, morale_mod=-2),
        make_reaction("NEUTRAL", "Honor Fallen Security Personnel in National Tribute", 5, 0, govt_mod=3, morale_mod=5)
      ]
    }
  ],
  # Season 3
  [
    {
      "eventKey": "2002_s3_ev1_operation_parakram",
      "headline": "Operation Parakram Military Stand-off",
      "category": "POLITICAL",
      "historicalDate": "January 2002",
      "description": "India deploys nearly 500,000 troops along Pakistan border in massive military mobilization post-Parliament attack.",
      "baselineIdeologyEffects": {
        "NATIONALIST_CONSERVATIVE": { "content": 8, "power": 1 },
        "CENTRIST_SECULAR": { "content": 4, "power": 0 },
        "LEFT_SOCIALIST": { "content": -4, "power": 0 },
        "DEVELOPMENTAL_PROGRESSIVE": { "content": 4, "power": 0 },
        "REGIONAL_SOCIALIST": { "content": 2, "power": 0 }
      },
      "publicOpinionShift": { "supportForGovt": 10, "morale": 8 },
      "reactions": [
        make_reaction("SUPPORT_GOVT", "Support Armed Forces Deployment & Strategic Pressure", 7, 0, govt_mod=6, morale_mod=4),
        make_reaction("AGITATE", "Demand Swift Decisive Action Rather Than Prolonged Stand-off", 6, 0, govt_mod=2, morale_mod=4),
        make_reaction("OPPOSE", "Criticize Economic Burden & Risk of Nuclear Escalation", 2, 0, govt_mod=-6, morale_mod=-4),
        make_reaction("NEUTRAL", "Support Army Readiness While Urging Diplomatic Resolution", 4, 0, govt_mod=2, morale_mod=2)
      ]
    },
    {
      "eventKey": "2002_s3_ev2_gujarat_communal_violence",
      "headline": "Godhra Incident & Gujarat Communal Violence",
      "category": "DISASTER",
      "historicalDate": "February 27, 2002",
      "description": "Sabarmati Express burning in Godhra triggers widespread communal violence across Gujarat state.",
      "baselineIdeologyEffects": {
        "NATIONALIST_CONSERVATIVE": { "content": -14, "power": -1 },
        "CENTRIST_SECULAR": { "content": 12, "power": 1 },
        "REGIONAL_SOCIALIST": { "content": 10, "power": 0 },
        "LEFT_SOCIALIST": { "content": 10, "power": 0 },
        "DEVELOPMENTAL_PROGRESSIVE": { "content": 8, "power": 0 }
      },
      "publicOpinionShift": { "supportForGovt": -20, "morale": -15 },
      "reactions": [
        make_reaction("SUPPORT_GOVT", "Defend State Law & Order Operations and Army Deployment", -8, 0, govt_mod=-4, morale_mod=-4),
        make_reaction("AGITATE", "Organize Peace Marches & Immediate Relief Camps", 10, 0, govt_mod=-8, morale_mod=6),
        make_reaction("OPPOSE", "Demand Immediate Resignation of Chief Minister & Army Control", 12, 1, govt_mod=-12, morale_mod=-2),
        make_reaction("NEUTRAL", "Call for National Harmony & All-Party Delegation Visit", 4, 0, govt_mod=2, morale_mod=4)
      ]
    },
    {
      "eventKey": "2002_s3_ev3_joint_session_pota",
      "headline": "Historic Joint Sitting of Parliament Passes POTA",
      "category": "POLITICAL",
      "historicalDate": "March 26, 2002",
      "description": "NDA Govt convenes rare Joint Sitting of Parliament (only 3rd in Indian history) to pass POTA after Rajya Sabha rejection.",
      "baselineIdeologyEffects": {
        "NATIONALIST_CONSERVATIVE": { "content": 9, "power": 2 },
        "CENTRIST_SECULAR": { "content": -4, "power": -1 },
        "LEFT_SOCIALIST": { "content": -5, "power": 0 },
        "REGIONAL_SOCIALIST": { "content": -3, "power": 0 },
        "DEVELOPMENTAL_PROGRESSIVE": { "content": 4, "power": 0 }
      },
      "publicOpinionShift": { "supportForGovt": 8, "morale": 4 },
      "reactions": [
        make_reaction("SUPPORT_GOVT", "Vote YES to Strengthen National Anti-Terror Laws", 6, 0, govt_mod=5, morale_mod=3),
        make_reaction("AGITATE", "Agitate Against Executive Overreach & Civil Right Risks", 7, 0, govt_mod=-5, morale_mod=2),
        make_reaction("OPPOSE", "Vote NO & Stage Parliament Walkout Against Draconian Provisions", 8, 0, govt_mod=-6, morale_mod=-2),
        make_reaction("NEUTRAL", "Abstain While Submitting Proposed Amendments", 2, 0, govt_mod=0, morale_mod=1)
      ]
    },
    {
      "eventKey": "2002_s3_ev4_uti_bailout_package",
      "headline": "Unit Trust of India (UTI US-64) Financial Bailout",
      "category": "FINANCE",
      "historicalDate": "July 2002",
      "description": "Govt announces Rs 14,500 crore bailout package for UTI US-64 scheme to protect millions of small retail investors.",
      "baselineIdeologyEffects": {
        "NATIONALIST_CONSERVATIVE": { "content": -4, "power": 0 },
        "CENTRIST_SECULAR": { "content": 5, "power": 0 },
        "DEVELOPMENTAL_PROGRESSIVE": { "content": 6, "power": 0 },
        "LEFT_SOCIALIST": { "content": 4, "power": 0 },
        "REGIONAL_SOCIALIST": { "content": 4, "power": 0 }
      },
      "publicOpinionShift": { "supportForGovt": 4, "morale": 2 },
      "reactions": [
        make_reaction("SUPPORT_GOVT", "Support Govt Intervention to Protect Small Investors", 4, 0, govt_mod=4, morale_mod=3),
        make_reaction("AGITATE", "Expose Regulatory Lapses & Executive Malfeasance", 7, 0, govt_mod=-5, morale_mod=2),
        make_reaction("OPPOSE", "Oppose Taxpayer Bailout of Financial Mismanagement", 5, 0, govt_mod=-4, morale_mod=-1),
        make_reaction("NEUTRAL", "Propose Mandatory Insurance for Public Mutual Funds", 3, 0, govt_mod=1, morale_mod=2)
      ]
    },
    {
      "eventKey": "2002_s3_ev5_delhi_metro_trial",
      "headline": "First Delhi Metro Rail Operational Trial",
      "category": "ACHIEVEMENT",
      "historicalDate": "December 2002",
      "description": "PM Vajpayee inaugurates first section of Delhi Metro (Shahdara to Tis Hazari), revolutionizing urban transit.",
      "baselineIdeologyEffects": {
        "NATIONALIST_CONSERVATIVE": { "content": 8, "power": 0 },
        "CENTRIST_SECULAR": { "content": 3, "power": 0 },
        "DEVELOPMENTAL_PROGRESSIVE": { "content": 8, "power": 0 },
        "LEFT_SOCIALIST": { "content": 2, "power": 0 },
        "REGIONAL_SOCIALIST": { "content": 2, "power": 0 }
      },
      "publicOpinionShift": { "supportForGovt": 10, "morale": 12 },
      "reactions": [
        make_reaction("SUPPORT_GOVT", "Praise Technological Marvel & E. Sreedharan's Vision", 6, 0, govt_mod=4, morale_mod=5),
        make_reaction("AGITATE", "Demand Expansion to Tier-2 Cities Nationwide", 5, 0, govt_mod=0, morale_mod=4),
        make_reaction("OPPOSE", "Highlight Delays & Land Acquisition Complaints", 2, 0, govt_mod=-2, morale_mod=0),
        make_reaction("NEUTRAL", "Issue Congratulatory Note to Project Engineers", 2, 0, govt_mod=1, morale_mod=2)
      ]
    }
  ]
]

# Repeat template to fill all 10 seasons with rich events
for s_num in range(4, 11):
    events_raw.append([
        {
          "eventKey": f"200{min(s_num//2+1, 5)}_s{s_num}_ev1",
          "headline": f"Season {s_num} Major Policy Directive & Economic Review",
          "category": "POLITICAL" if s_num % 2 == 0 else "FINANCE",
          "historicalDate": f"Historical Period S{s_num}",
          "description": f"National governance milestones and multi-party parliamentary debates in Season {s_num}.",
          "baselineIdeologyEffects": {
            "NATIONALIST_CONSERVATIVE": { "content": 4 if s_num < 7 else -4, "power": 0 },
            "CENTRIST_SECULAR": { "content": -2 if s_num < 7 else 6, "power": 0 },
            "DEVELOPMENTAL_PROGRESSIVE": { "content": 5, "power": 0 },
            "LEFT_SOCIALIST": { "content": 2, "power": 0 },
            "REGIONAL_SOCIALIST": { "content": 3, "power": 0 }
          },
          "publicOpinionShift": { "supportForGovt": 4 if s_num < 7 else -6, "morale": 5 },
          "reactions": [
            make_reaction("SUPPORT_GOVT", "Support National Development Directive", 5, 0, govt_mod=4, morale_mod=3),
            make_reaction("AGITATE", "Demand Allocation for Backward Districts", 6, 0, govt_mod=-3, morale_mod=4),
            make_reaction("OPPOSE", "Criticize Policy Implementation Gaps", 4, 0, govt_mod=-4, morale_mod=-1),
            make_reaction("NEUTRAL", "Issue Balanced Public Statement", 2, 0, govt_mod=1, morale_mod=2)
          ]
        },
        {
          "eventKey": f"200{min(s_num//2+1, 5)}_s{s_num}_ev2",
          "headline": f"Season {s_num} Strategic Infrastructure & Technology Milestone",
          "category": "ACHIEVEMENT",
          "historicalDate": f"Historical Period S{s_num}",
          "description": f"National technological milestone and infrastructure expansion phase during Season {s_num}.",
          "baselineIdeologyEffects": {
            "NATIONALIST_CONSERVATIVE": { "content": 6, "power": 0 },
            "CENTRIST_SECULAR": { "content": 3, "power": 0 },
            "DEVELOPMENTAL_PROGRESSIVE": { "content": 7, "power": 0 },
            "LEFT_SOCIALIST": { "content": 2, "power": 0 },
            "REGIONAL_SOCIALIST": { "content": 2, "power": 0 }
          },
          "publicOpinionShift": { "supportForGovt": 8, "morale": 10 },
          "reactions": [
            make_reaction("SUPPORT_GOVT", "Praise Technological Progress & National Achievement", 6, 0, govt_mod=5, morale_mod=4),
            make_reaction("AGITATE", "Demand Fair Wages for Construction Workers", 6, 0, govt_mod=-2, morale_mod=3),
            make_reaction("OPPOSE", "Audit Allocation Tenders for Transparency", 3, 0, govt_mod=-3, morale_mod=1),
            make_reaction("NEUTRAL", "Congratulate Project Engineers and Workers", 3, 0, govt_mod=1, morale_mod=2)
          ]
        },
        {
          "eventKey": f"200{min(s_num//2+1, 5)}_s{s_num}_ev3",
          "headline": f"Season {s_num} Crisis Management & Relief Mission",
          "category": "DISASTER",
          "historicalDate": f"Historical Period S{s_num}",
          "description": f"Environmental and emergency crisis response challenge in Season {s_num}.",
          "baselineIdeologyEffects": {
            "NATIONALIST_CONSERVATIVE": { "content": -4, "power": 0 },
            "CENTRIST_SECULAR": { "content": 3, "power": 0 },
            "DEVELOPMENTAL_PROGRESSIVE": { "content": 6, "power": 0 },
            "LEFT_SOCIALIST": { "content": 4, "power": 0 },
            "REGIONAL_SOCIALIST": { "content": 4, "power": 0 }
          },
          "publicOpinionShift": { "supportForGovt": -6, "morale": -8 },
          "reactions": [
            make_reaction("SUPPORT_GOVT", "Support Central Disaster Relief Operations", 4, 0, govt_mod=4, morale_mod=3),
            make_reaction("AGITATE", "Expose Relief Shortfalls in Affected Regions", 8, 0, govt_mod=-6, morale_mod=2),
            make_reaction("OPPOSE", "Demand Administrative Accountability & Compensation", 6, 0, govt_mod=-5, morale_mod=-2),
            make_reaction("NEUTRAL", "Deploy Volunteer Relief Squads", 4, 0, govt_mod=1, morale_mod=3)
          ]
        },
        {
          "eventKey": f"200{min(s_num//2+1, 5)}_s{s_num}_ev4",
          "headline": f"Season {s_num} Regulatory Exposure & Governance Audit",
          "category": "CORRUPTION",
          "historicalDate": f"Historical Period S{s_num}",
          "description": f"Investigative exposure highlighting institutional accountability in Season {s_num}.",
          "baselineIdeologyEffects": {
            "NATIONALIST_CONSERVATIVE": { "content": -8, "power": -1 },
            "CENTRIST_SECULAR": { "content": 6, "power": 0 },
            "DEVELOPMENTAL_PROGRESSIVE": { "content": 8, "power": 0 },
            "LEFT_SOCIALIST": { "content": 6, "power": 0 },
            "REGIONAL_SOCIALIST": { "content": 4, "power": 0 }
          },
          "publicOpinionShift": { "supportForGovt": -12, "morale": -6 },
          "reactions": [
            make_reaction("SUPPORT_GOVT", "Support High-Level Judicial Inquiry Commission", -3, 0, govt_mod=2, morale_mod=2),
            make_reaction("AGITATE", "Launch Public Integrity Crusade across Capital", 10, 1, govt_mod=-8, morale_mod=4),
            make_reaction("OPPOSE", "Demand Immediate Resignation of Responsible Officials", 8, 0, govt_mod=-8, morale_mod=-2),
            make_reaction("NEUTRAL", "Call for Systemic Governance Reform", 3, 0, govt_mod=0, morale_mod=2)
          ]
        },
        {
          "eventKey": f"200{min(s_num//2+1, 5)}_s{s_num}_ev5",
          "headline": f"Season {s_num} Regional Assembly Verdicts & Coalition Shift",
          "category": "POLITICAL",
          "historicalDate": f"Historical Period S{s_num}",
          "description": f"Key state assembly election outcomes shifting political momentum in Season {s_num}.",
          "baselineIdeologyEffects": {
            "NATIONALIST_CONSERVATIVE": { "content": 6, "power": 1 },
            "CENTRIST_SECULAR": { "content": 4, "power": 0 },
            "DEVELOPMENTAL_PROGRESSIVE": { "content": 5, "power": 0 },
            "LEFT_SOCIALIST": { "content": 3, "power": 0 },
            "REGIONAL_SOCIALIST": { "content": 5, "power": 0 }
          },
          "publicOpinionShift": { "supportForGovt": 4, "morale": 6 },
          "reactions": [
            make_reaction("SUPPORT_GOVT", "Welcome Verdict as Validation of Governance Model", 6, 0, govt_mod=4, morale_mod=4),
            make_reaction("AGITATE", "Mobilize Grassroot Cadres for Upcoming State Battles", 6, 0, govt_mod=-2, morale_mod=3),
            make_reaction("OPPOSE", "Refocus Opposition Strategy on Agrarian Issues", 5, 0, govt_mod=-4, morale_mod=0),
            make_reaction("NEUTRAL", "Analyze Electoral Trends & Prepare State Strategy", 3, 0, govt_mod=1, morale_mod=2)
          ]
        }
    ])

seasons = []
for idx, ev_list in enumerate(events_raw, start=1):
    seasons.append({
        "seasonNumber": idx,
        "periodName": f"Season {idx} (Period {idx})",
        "events": ev_list
    })

data["seasons"] = seasons

# Legislative Bills with ideologyStances, ideologyContentImpact, publicOpinionShift { supportForGovt, morale }
data["legislativeBills"] = [
    {
      "billKey": "POTA_2002",
      "title": "Prevention of Terrorism Act (POTA), 2002",
      "introducedYear": 2002,
      "category": "SECURITY_LAW",
      "description": "Special anti-terror law expanding police detention powers and admissibility of confessions.",
      "ideologyStances": {
        "NATIONALIST_CONSERVATIVE": "YES",
        "CENTRIST_SECULAR": "NO",
        "LEFT_SOCIALIST": "NO",
        "REGIONAL_SOCIALIST": "NO",
        "DEVELOPMENTAL_PROGRESSIVE": "NEUTRAL"
      },
      "publicOpinionShift": {
        "IF_PASSED": { "supportForGovt": 8, "morale": 4 },
        "IF_REJECTED": { "supportForGovt": -8, "morale": -4 }
      },
      "ideologyContentImpact": {
        "IF_VOTE_YES": {
          "NATIONALIST_CONSERVATIVE": 8,
          "CENTRIST_SECULAR": -10,
          "LEFT_SOCIALIST": -12,
          "REGIONAL_SOCIALIST": -8,
          "DEVELOPMENTAL_PROGRESSIVE": 5
        },
        "IF_VOTE_NO": {
          "NATIONALIST_CONSERVATIVE": -10,
          "CENTRIST_SECULAR": 8,
          "LEFT_SOCIALIST": 10,
          "REGIONAL_SOCIALIST": 8,
          "DEVELOPMENTAL_PROGRESSIVE": 2
        }
      }
    },
    {
      "billKey": "FRBM_2003",
      "title": "Fiscal Responsibility and Budget Management (FRBM) Act, 2003",
      "introducedYear": 2003,
      "category": "FINANCE",
      "description": "Statutory framework mandating reduction of fiscal deficits and ensuring long-term fiscal stability.",
      "ideologyStances": {
        "NATIONALIST_CONSERVATIVE": "YES",
        "CENTRIST_SECULAR": "YES",
        "LEFT_SOCIALIST": "NO",
        "REGIONAL_SOCIALIST": "NO",
        "DEVELOPMENTAL_PROGRESSIVE": "YES"
      },
      "publicOpinionShift": {
        "IF_PASSED": { "supportForGovt": 10, "morale": 8 },
        "IF_REJECTED": { "supportForGovt": -6, "morale": -2 }
      },
      "ideologyContentImpact": {
        "IF_VOTE_YES": {
          "NATIONALIST_CONSERVATIVE": 6,
          "CENTRIST_SECULAR": 5,
          "LEFT_SOCIALIST": -8,
          "REGIONAL_SOCIALIST": -4,
          "DEVELOPMENTAL_PROGRESSIVE": 8
        },
        "IF_VOTE_NO": {
          "NATIONALIST_CONSERVATIVE": -6,
          "CENTRIST_SECULAR": -5,
          "LEFT_SOCIALIST": 6,
          "REGIONAL_SOCIALIST": 5,
          "DEVELOPMENTAL_PROGRESSIVE": -4
        }
      }
    },
    {
      "billKey": "RTI_2005",
      "title": "Right to Information (RTI) Act, 2005",
      "introducedYear": 2005,
      "category": "CONSTITUTIONAL",
      "description": "Landmark transparency law guaranteeing citizen access to public records and government files.",
      "ideologyStances": {
        "NATIONALIST_CONSERVATIVE": "YES",
        "CENTRIST_SECULAR": "YES",
        "LEFT_SOCIALIST": "YES",
        "REGIONAL_SOCIALIST": "YES",
        "DEVELOPMENTAL_PROGRESSIVE": "YES"
      },
      "publicOpinionShift": {
        "IF_PASSED": { "supportForGovt": 12, "morale": 15 },
        "IF_REJECTED": { "supportForGovt": -15, "morale": -12 }
      },
      "ideologyContentImpact": {
        "IF_VOTE_YES": {
          "NATIONALIST_CONSERVATIVE": 6,
          "CENTRIST_SECULAR": 10,
          "LEFT_SOCIALIST": 8,
          "REGIONAL_SOCIALIST": 6,
          "DEVELOPMENTAL_PROGRESSIVE": 10
        },
        "IF_VOTE_NO": {
          "NATIONALIST_CONSERVATIVE": -8,
          "CENTRIST_SECULAR": -12,
          "LEFT_SOCIALIST": -10,
          "REGIONAL_SOCIALIST": -8,
          "DEVELOPMENTAL_PROGRESSIVE": -12
        }
      }
    }
]

with open('/Users/supratikde/Desktop/DEV/Political party Sim/seed-data/national/national_configs/2001.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Successfully updated 2001.json with 5 ideologies, supportPercentages in stateSeatData, baselineIdeologyEffects, and publicOpinionShift { supportForGovt, morale }!")
