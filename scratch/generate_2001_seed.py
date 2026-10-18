import json

data = {
  "era": 2001,
  "title": "The NDA Experiment",
  "description": "Vajpayee leads the 24-party NDA coalition through nuclear tensions, economic reforms, national disasters, and political turbulence (2001-2005).",
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
      "description": "Upstart progressive party holding ~10% vote share in all states.",
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
      "activeStates": ["UP", "Maharashtra", "Gujarat", "Rajasthan", "Madhya Pradesh", "Delhi", "Uttarakhand", "Himachal Pradesh", "Jharkhand", "Chhattisgarh"]
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
      "activeInAllStates": True
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
      "description": "Leader of Left Front, strong in Bengal and Kerala.",
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
      "ideology": "BAHUJAN_SOCIAL",
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
      "ideology": "REGIONAL_POPULIST",
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
    { "stateName": "Uttar Pradesh", "totalSeats": 80, "ydpSeats": 8, "competitiveness": "HIGH", "initialSeats": { "bjp": 29, "sp": 22, "bsp": 19, "inc": 10 } },
    { "stateName": "Maharashtra", "totalSeats": 48, "ydpSeats": 5, "competitiveness": "HIGH", "initialSeats": { "bjp": 13, "shiv_sena": 15, "inc": 10, "ncp": 8 } },
    { "stateName": "West Bengal", "totalSeats": 42, "ydpSeats": 4, "competitiveness": "HIGH", "initialSeats": { "cpim": 21, "inc": 8, "aitc": 7, "others": 6 } },
    { "stateName": "Bihar", "totalSeats": 40, "ydpSeats": 4, "competitiveness": "HIGH", "initialSeats": { "rjd": 17, "bjp": 12, "jdu": 6, "inc": 4, "others": 1 } },
    { "stateName": "Tamil Nadu", "totalSeats": 39, "ydpSeats": 4, "competitiveness": "HIGH", "initialSeats": { "dmk": 12, "aidmk": 10, "inc": 7, "bjp": 4, "others": 6 } },
    { "stateName": "Andhra Pradesh", "totalSeats": 42, "ydpSeats": 4, "competitiveness": "HIGH", "initialSeats": { "tdp": 29, "inc": 5, "bjp": 4, "others": 4 } },
    { "stateName": "Madhya Pradesh", "totalSeats": 29, "ydpSeats": 3, "competitiveness": "MEDIUM", "initialSeats": { "bjp": 25, "inc": 4 } },
    { "stateName": "Karnataka", "totalSeats": 28, "ydpSeats": 3, "competitiveness": "MEDIUM", "initialSeats": { "bjp": 13, "inc": 9, "jdu": 3, "others": 3 } },
    { "stateName": "Gujarat", "totalSeats": 26, "ydpSeats": 3, "competitiveness": "LOW", "initialSeats": { "bjp": 20, "inc": 6 } },
    { "stateName": "Rajasthan", "totalSeats": 25, "ydpSeats": 3, "competitiveness": "MEDIUM", "initialSeats": { "bjp": 16, "inc": 9 } },
    { "stateName": "Odisha", "totalSeats": 21, "ydpSeats": 2, "competitiveness": "MEDIUM", "initialSeats": { "bjd": 9, "inc": 5, "bjp": 4, "others": 3 } },
    { "stateName": "Kerala", "totalSeats": 20, "ydpSeats": 2, "competitiveness": "MEDIUM", "initialSeats": { "inc": 8, "cpim": 8, "bjp": 1, "others": 3 } },
    { "stateName": "Jharkhand", "totalSeats": 14, "ydpSeats": 1, "competitiveness": "HIGH", "initialSeats": { "bjp": 8, "jmm": 2, "inc": 2, "jdu": 1, "others": 1 } },
    { "stateName": "Assam", "totalSeats": 14, "ydpSeats": 1, "competitiveness": "MEDIUM", "initialSeats": { "inc": 10, "agp": 2, "bjp": 2 } },
    { "stateName": "Punjab", "totalSeats": 13, "ydpSeats": 1, "competitiveness": "MEDIUM", "initialSeats": { "akali_dal": 8, "inc": 4, "bjp": 1 } },
    { "stateName": "Chhattisgarh", "totalSeats": 11, "ydpSeats": 1, "competitiveness": "MEDIUM", "initialSeats": { "bjp": 7, "inc": 4 } },
    { "stateName": "Haryana", "totalSeats": 10, "ydpSeats": 1, "competitiveness": "MEDIUM", "initialSeats": { "inld": 5, "inc": 3, "bjp": 1, "others": 1 } },
    { "stateName": "Delhi", "totalSeats": 7, "ydpSeats": 1, "competitiveness": "LOW", "initialSeats": { "bjp": 7 } },
    { "stateName": "Jammu & Kashmir", "totalSeats": 6, "ydpSeats": 1, "competitiveness": "HIGH", "initialSeats": { "nc": 4, "bjp": 1, "others": 1 } },
    { "stateName": "Uttarakhand", "totalSeats": 5, "ydpSeats": 1, "competitiveness": "MEDIUM", "initialSeats": { "bjp": 3, "inc": 2 } },
    { "stateName": "Himachal Pradesh", "totalSeats": 4, "ydpSeats": 0, "competitiveness": "LOW", "initialSeats": { "bjp": 3, "inc": 1 } },
    { "stateName": "Goa", "totalSeats": 2, "ydpSeats": 0, "competitiveness": "LOW", "initialSeats": { "bjp": 2 } },
    { "stateName": "Manipur", "totalSeats": 2, "ydpSeats": 0, "competitiveness": "HIGH", "initialSeats": { "inc": 2 } },
    { "stateName": "Meghalaya", "totalSeats": 2, "ydpSeats": 0, "competitiveness": "HIGH", "initialSeats": { "inc": 2 } },
    { "stateName": "Tripura", "totalSeats": 2, "ydpSeats": 0, "competitiveness": "MEDIUM", "initialSeats": { "cpim": 2 } },
    { "stateName": "Arunachal Pradesh", "totalSeats": 2, "ydpSeats": 0, "competitiveness": "LOW", "initialSeats": { "inc": 2 } },
    { "stateName": "Nagaland", "totalSeats": 1, "ydpSeats": 0, "competitiveness": "LOW", "initialSeats": { "others": 1 } },
    { "stateName": "Mizoram", "totalSeats": 1, "ydpSeats": 0, "competitiveness": "LOW", "initialSeats": { "others": 1 } },
    { "stateName": "Sikkim", "totalSeats": 1, "ydpSeats": 0, "competitiveness": "LOW", "initialSeats": { "others": 1 } },
    { "stateName": "Puducherry & UTs", "totalSeats": 7, "ydpSeats": 1, "competitiveness": "LOW", "initialSeats": { "inc": 4, "bjp": 2, "others": 1 } }
  ],
  "seasons": [
    # Season 1
    {
      "seasonNumber": 1,
      "periodName": "Season 1 (Jan - Jun 2001)",
      "events": [
        {
          "eventKey": "2001_s1_ev1_kutch_earthquake",
          "headline": "Devastating Kutch Earthquake",
          "category": "DISASTER",
          "historicalDate": "January 26, 2001",
          "description": "A massive 7.7 magnitude earthquake strikes Kutch, Gujarat, killing over 20,000 people and devastating infrastructure.",
          "baselinePartyEffects": {
            "bjp": { "content": -4, "power": 0 },
            "inc": { "content": 4, "power": 0 },
            "ydp": { "content": 6, "power": 0 }
          },
          "moodShift": { "antiIncumbency": 6, "nationalism": 4 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Support Govt Relief Operations", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": { "proIncumbency": 3 } },
            { "key": "AGITATE", "label": "Agitate Against Inadequate Relief Preparedness", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 5 } },
            { "key": "OPPOSE", "label": "Demand Judicial Probe into Building Code Violations", "partyContentShift": 5, "partyPowerShift": 0, "moodShiftModifier": { "antiCorruption": 4 } },
            { "key": "NEUTRAL", "label": "Dispatch YDP Aid Teams Without Public Statements", "partyContentShift": 2, "partyPowerShift": 0, "moodShiftModifier": { "secularTrust": 2 } }
          ]
        },
        {
          "eventKey": "2001_s1_ev2_ketan_parekh_scam",
          "headline": "Stock Market Crash & Ketan Parekh Scam",
          "category": "FINANCE",
          "historicalDate": "March 2001",
          "description": "Stock market collapses following revelations of circular trading, bank fund rigging, and Madhavpura Bank failure.",
          "baselinePartyEffects": {
            "bjp": { "content": -8, "power": 0 },
            "inc": { "content": 8, "power": 0 },
            "cpim": { "content": 6, "power": 0 }
          },
          "moodShift": { "antiCorruption": 12, "economicStrain": 8 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Support Finance Ministry Regulatory Reforms", "partyContentShift": -2, "partyPowerShift": 0, "moodShiftModifier": { "fiscalPrudence": 4 } },
            { "key": "AGITATE", "label": "Lead Nationwide Protests for Small Investors", "partyContentShift": 10, "partyPowerShift": 0, "moodShiftModifier": { "antiCorruption": 6 } },
            { "key": "OPPOSE", "label": "Demand Resignation of Finance Minister", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 6 } },
            { "key": "NEUTRAL", "label": "Issue Press Release Calling for SEBI Autonomy", "partyContentShift": 1, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2001_s1_ev3_tehelka_sting",
          "headline": "Tehelka Defense Procurement Sting Operation",
          "category": "CORRUPTION",
          "historicalDate": "March 2001",
          "description": "Undercover journalists expose bribery in military contracts, triggering high-profile political resignations.",
          "baselinePartyEffects": {
            "bjp": { "content": -12, "power": -2 },
            "inc": { "content": 14, "power": 1 },
            "sp": { "content": 6, "power": 0 },
            "ydp": { "content": 10, "power": 0 }
          },
          "moodShift": { "antiCorruption": 20, "antiIncumbency": 14 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Support Inquiry Commission Setup", "partyContentShift": -6, "partyPowerShift": 0, "moodShiftModifier": { "proIncumbency": -4 } },
            { "key": "AGITATE", "label": "Launch Nationwide Anti-Corruption March", "partyContentShift": 12, "partyPowerShift": 1, "moodShiftModifier": { "antiCorruption": 8 } },
            { "key": "OPPOSE", "label": "Demand Immediate Dissolution of Lok Sabha", "partyContentShift": 9, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 8 } },
            { "key": "NEUTRAL", "label": "Call for Institutional Defense Reform", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2001_s1_ev4_agra_summit",
          "headline": "Agra Peace Summit (Vajpayee - Musharraf)",
          "category": "POLITICAL",
          "historicalDate": "July 2001",
          "description": "High-stakes summit in Agra between PM Vajpayee and President Musharraf ends without a joint declaration over Kashmir.",
          "baselinePartyEffects": {
            "bjp": { "content": -2, "power": 0 },
            "inc": { "content": 4, "power": 0 },
            "cpim": { "content": 3, "power": 0 }
          },
          "moodShift": { "nationalism": 8 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Back Prime Minister's Firm Stance on Cross-Border Terror", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 5 } },
            { "key": "AGITATE", "label": "Protest Failure to Secure Firm Anti-Terror Guarantees", "partyContentShift": 5, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 3 } },
            { "key": "OPPOSE", "label": "Criticize Ill-Prepared Diplomatic Strategy", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": {} },
            { "key": "NEUTRAL", "label": "Commend Continued Dialogue & Peace Process", "partyContentShift": 2, "partyPowerShift": 0, "moodShiftModifier": { "secularTrust": 3 } }
          ]
        },
        {
          "eventKey": "2001_s1_ev5_gsat1_launch",
          "headline": "ISRO Successfully Launches GSLV-D1 / GSAT-1",
          "category": "ACHIEVEMENT",
          "historicalDate": "April 2001",
          "description": "ISRO achieves milestone with first launch of Geosynchronous Satellite Launch Vehicle from Sriharikota.",
          "baselinePartyEffects": {
            "bjp": { "content": 6, "power": 0 },
            "inc": { "content": 2, "power": 0 },
            "ydp": { "content": 4, "power": 0 }
          },
          "moodShift": { "nationalism": 10, "proIncumbency": 4 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Congratulate ISRO Scientists & Prime Minister", "partyContentShift": 5, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 4 } },
            { "key": "AGITATE", "label": "Highlight Need for Higher R&D & Tech Budget", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": {} },
            { "key": "OPPOSE", "label": "Credit Previous Administrations for Foundation", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} },
            { "key": "NEUTRAL", "label": "Issue Congratulatory Statement on Space Mission", "partyContentShift": 2, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        }
      ]
    },
    # Season 2
    {
      "seasonNumber": 2,
      "periodName": "Season 2 (Jul - Dec 2001)",
      "events": [
        {
          "eventKey": "2001_s2_ev1_enron_dabhol_crisis",
          "headline": "Enron Dabhol Power Plant Collapse",
          "category": "FINANCE",
          "historicalDate": "July 2001",
          "description": "Dabhol Power Company shuts down operations after power tariff disputes, leaving state utility MSEB in deep debt.",
          "baselinePartyEffects": {
            "bjp": { "content": -5, "power": 0 },
            "inc": { "content": -3, "power": 0 },
            "cpim": { "content": 8, "power": 0 }
          },
          "moodShift": { "economicStrain": 10, "antiCorruption": 6 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Support Govt Plan to Restructure Power Contracts", "partyContentShift": 2, "partyPowerShift": 0, "moodShiftModifier": { "fiscalPrudence": 3 } },
            { "key": "AGITATE", "label": "Lead Workers Protests Against Foreign Power Monopolies", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "populism": 5 } },
            { "key": "OPPOSE", "label": "Blame State Govt Mismanagement & High Tariffs", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 4 } },
            { "key": "NEUTRAL", "label": "Advocate for Renewable Energy Transition Plan", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2001_s2_ev2_simi_uapa_ban",
          "headline": "Ban on Students Islamic Movement of India (SIMI)",
          "category": "POLITICAL",
          "historicalDate": "September 2001",
          "description": "Union Home Ministry bans SIMI under Unlawful Activities Prevention Act following anti-national activities.",
          "baselinePartyEffects": {
            "bjp": { "content": 8, "power": 0 },
            "inc": { "content": 2, "power": 0 },
            "sp": { "content": -4, "power": 0 }
          },
          "moodShift": { "nationalism": 12, "secularTrust": -4 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Fully Endorse Ban on Extremist Groups", "partyContentShift": 7, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 6 } },
            { "key": "AGITATE", "label": "Demand Strict Safeguards Against Misuse of Law", "partyContentShift": 5, "partyPowerShift": 0, "moodShiftModifier": { "secularTrust": 4 } },
            { "key": "OPPOSE", "label": "Question Procedure & Demand Special Judicial Review", "partyContentShift": -2, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 3 } },
            { "key": "NEUTRAL", "label": "Call for Zero Tolerance on Terrorism and Hate Speech", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2001_s2_ev3_post_911_diplomacy",
          "headline": "Post-9/11 Global Anti-Terror Security Shift",
          "category": "POLITICAL",
          "historicalDate": "September 2001",
          "description": "Following 9/11 attacks in US, India offers full intelligence cooperation, reframing cross-border terror in South Asia.",
          "baselinePartyEffects": {
            "bjp": { "content": 7, "power": 0 },
            "inc": { "content": 4, "power": 0 },
            "ydp": { "content": 5, "power": 0 }
          },
          "moodShift": { "nationalism": 14, "proIncumbency": 5 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Support Govt Alignment with Global Anti-Terror Coalition", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 5 } },
            { "key": "AGITATE", "label": "Demand Immediate Military Action Against Terror Camps", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 8 } },
            { "key": "OPPOSE", "label": "Warn Against Strategic Over-Reliance on Foreign Powers", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} },
            { "key": "NEUTRAL", "label": "Urge Non-Aligned Diplomatic Equilibrium", "partyContentShift": 2, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2001_s2_ev4_golden_quadrilateral_phase1",
          "headline": "Golden Quadrilateral Highway Project Acceleration",
          "category": "ACHIEVEMENT",
          "historicalDate": "November 2001",
          "description": "NDA Govt accelerates construction of 5,846 km 4-lane highway network connecting Delhi, Mumbai, Chennai, and Kolkata.",
          "baselinePartyEffects": {
            "bjp": { "content": 10, "power": 1 },
            "inc": { "content": -2, "power": 0 },
            "ydp": { "content": 5, "power": 0 }
          },
          "moodShift": { "proIncumbency": 8, "economicStrain": -4 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Commend Landmark Infrastructure Expansion", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "proIncumbency": 4 } },
            { "key": "AGITATE", "label": "Demand Fair Compensation & Rehabilitation for Farmers", "partyContentShift": 7, "partyPowerShift": 0, "moodShiftModifier": { "populism": 5 } },
            { "key": "OPPOSE", "label": "Audit Highway Tender Allocations & Cost Overruns", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": { "antiCorruption": 4 } },
            { "key": "NEUTRAL", "label": "Propose Feeder Roads Connectivity for Villages", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2001_s2_ev5_parliament_attack",
          "headline": "Terrorist Attack on Indian Parliament",
          "category": "DISASTER",
          "historicalDate": "December 13, 2001",
          "description": "Armed terrorists attack Parliament Complex in Delhi; security forces neutralize attackers, preventing massive loss.",
          "baselinePartyEffects": {
            "bjp": { "content": 6, "power": 2 },
            "inc": { "content": 5, "power": 0 },
            "ydp": { "content": 6, "power": 0 }
          },
          "moodShift": { "nationalism": 25, "proIncumbency": 8 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Stand United Behind Government's Defense Mobilization", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 10 } },
            { "key": "AGITATE", "label": "Demand Immediate Retaliatory Military Strike", "partyContentShift": 10, "partyPowerShift": 1, "moodShiftModifier": { "nationalism": 12 } },
            { "key": "OPPOSE", "label": "Demand Security Audit & Home Minister Accountability", "partyContentShift": 2, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 5 } },
            { "key": "NEUTRAL", "label": "Honor Fallen Security Personnel in National Tribute", "partyContentShift": 5, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 6 } }
          ]
        }
      ]
    },
    # Season 3
    {
      "seasonNumber": 3,
      "periodName": "Season 3 (Jan - Jun 2002)",
      "events": [
        {
          "eventKey": "2002_s3_ev1_operation_parakram",
          "headline": "Operation Parakram Military Stand-off",
          "category": "POLITICAL",
          "historicalDate": "January 2002",
          "description": "India deploys nearly 500,000 troops along Pakistan border in massive military mobilization post-Parliament attack.",
          "baselinePartyEffects": {
            "bjp": { "content": 8, "power": 1 },
            "inc": { "content": 4, "power": 0 },
            "cpim": { "content": -4, "power": 0 }
          },
          "moodShift": { "nationalism": 18, "economicStrain": 6 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Support Armed Forces Deployment & Strategic Pressure", "partyContentShift": 7, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 8 } },
            { "key": "AGITATE", "label": "Demand Swift Decisive Action Rather Than Prolonged Stand-off", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 6 } },
            { "key": "OPPOSE", "label": "Criticize Economic Burden & Risk of Nuclear Escalation", "partyContentShift": 2, "partyPowerShift": 0, "moodShiftModifier": { "economicStrain": 4 } },
            { "key": "NEUTRAL", "label": "Support Army Readiness While Urging Diplomatic Resolution", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2002_s3_ev2_gujarat_communal_violence",
          "headline": "Godhra Incident & Gujarat Communal Violence",
          "category": "DISASTER",
          "historicalDate": "February 27, 2002",
          "description": "Sabarmati Express burning in Godhra triggers widespread communal violence across Gujarat state.",
          "baselinePartyEffects": {
            "bjp": { "content": -14, "power": -1 },
            "inc": { "content": 12, "power": 1 },
            "sp": { "content": 10, "power": 0 },
            "bsp": { "content": 8, "power": 0 }
          },
          "moodShift": { "secularTrust": -20, "antiIncumbency": 12 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Defend State Law & Order Operations and Army Deployment", "partyContentShift": -8, "partyPowerShift": 0, "moodShiftModifier": { "proIncumbency": -5 } },
            { "key": "AGITATE", "label": "Organize Peace Marches & Immediate Relief Camps", "partyContentShift": 10, "partyPowerShift": 0, "moodShiftModifier": { "secularTrust": 8 } },
            { "key": "OPPOSE", "label": "Demand Immediate Resignation of Chief Minister & Army Control", "partyContentShift": 12, "partyPowerShift": 1, "moodShiftModifier": { "antiIncumbency": 10 } },
            { "key": "NEUTRAL", "label": "Call for National Harmony & All-Party Delegation Visit", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": { "secularTrust": 4 } }
          ]
        },
        {
          "eventKey": "2002_s3_ev3_joint_session_pota",
          "headline": "Historic Joint Sitting of Parliament Passes POTA",
          "category": "POLITICAL",
          "historicalDate": "March 26, 2002",
          "description": "NDA Govt convenes rare Joint Sitting of Parliament (only 3rd in Indian history) to pass POTA after Rajya Sabha rejection.",
          "baselinePartyEffects": {
            "bjp": { "content": 9, "power": 2 },
            "inc": { "content": -4, "power": -1 },
            "cpim": { "content": -5, "power": 0 }
          },
          "moodShift": { "nationalism": 12, "antiIncumbency": -4 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Vote YES to Strengthen National Anti-Terror Laws", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 5 } },
            { "key": "AGITATE", "label": "Agitate Against Executive Overreach & Civil Right Risks", "partyContentShift": 7, "partyPowerShift": 0, "moodShiftModifier": { "secularTrust": 5 } },
            { "key": "OPPOSE", "label": "Vote NO & Stage Parliament Walkout Against Draconian Provisions", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 5 } },
            { "key": "NEUTRAL", "label": "Abstain While Submitting Proposed Amendments", "partyContentShift": 2, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2002_s3_ev4_uti_bailout_package",
          "headline": "Unit Trust of India (UTI US-64) Financial Bailout",
          "category": "FINANCE",
          "historicalDate": "July 2002",
          "description": "Govt announces Rs 14,500 crore bailout package for UTI US-64 scheme to protect millions of small retail investors.",
          "baselinePartyEffects": {
            "bjp": { "content": -4, "power": 0 },
            "inc": { "content": 5, "power": 0 },
            "ydp": { "content": 4, "power": 0 }
          },
          "moodShift": { "fiscalPrudence": -6, "populism": 6 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Support Govt Intervention to Protect Small Investors", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": { "populism": 4 } },
            { "key": "AGITATE", "label": "Expose Regulatory Lapses & Executive Malfeasance", "partyContentShift": 7, "partyPowerShift": 0, "moodShiftModifier": { "antiCorruption": 6 } },
            { "key": "OPPOSE", "label": "Oppose Taxpayer Bailout of Financial Mismanagement", "partyContentShift": 5, "partyPowerShift": 0, "moodShiftModifier": { "fiscalPrudence": 5 } },
            { "key": "NEUTRAL", "label": "Propose Mandatory Insurance for Public Mutual Funds", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2002_s3_ev5_delhi_metro_trial",
          "headline": "First Delhi Metro Rail Operational Trial",
          "category": "ACHIEVEMENT",
          "historicalDate": "December 2002",
          "description": "PM Vajpayee inaugurates first section of Delhi Metro (Shahdara to Tis Hazari), revolutionizing urban transit.",
          "baselinePartyEffects": {
            "bjp": { "content": 8, "power": 0 },
            "inc": { "content": 3, "power": 0 },
            "ydp": { "content": 5, "power": 0 }
          },
          "moodShift": { "proIncumbency": 6, "nationalism": 5 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Praise Technological Marvel & E. Sreedharan's Vision", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "proIncumbency": 4 } },
            { "key": "AGITATE", "label": "Demand Expansion to Tier-2 Cities Nationwide", "partyContentShift": 5, "partyPowerShift": 0, "moodShiftModifier": { "populism": 4 } },
            { "key": "OPPOSE", "label": "Highlight Delays & Land Acquisition Complaints", "partyContentShift": 2, "partyPowerShift": 0, "moodShiftModifier": {} },
            { "key": "NEUTRAL", "label": "Issue Congratulatory Note to Project Engineers", "partyContentShift": 2, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        }
      ]
    },
    # Season 4
    {
      "seasonNumber": 4,
      "periodName": "Season 4 (Jul - Dec 2002)",
      "events": [
        {
          "eventKey": "2002_s4_ev1_kalam_presidential_election",
          "headline": "Dr. APJ Abdul Kalam Elected 11th President of India",
          "category": "ACHIEVEMENT",
          "historicalDate": "July 25, 2002",
          "description": "Renowned scientist Dr. APJ Abdul Kalam is elected President with cross-party consensus, inspiring the nation.",
          "baselinePartyEffects": {
            "bjp": { "content": 10, "power": 1 },
            "inc": { "content": 6, "power": 0 },
            "cpim": { "content": -3, "power": 0 },
            "ydp": { "content": 8, "power": 0 }
          },
          "moodShift": { "nationalism": 20, "proIncumbency": 6 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Enthusiastically Support Kalam's People's Presidency", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 8 } },
            { "key": "AGITATE", "label": "Call for Vision 2020 Youth Technology Initiatives", "partyContentShift": 7, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 6 } },
            { "key": "OPPOSE", "label": "Question Symbolic Political Nominations", "partyContentShift": -4, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 2 } },
            { "key": "NEUTRAL", "label": "Welcome Election of Eminent Defense Scientist", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2002_s4_ev2_severe_monsoon_drought",
          "headline": "Severe Pan-India Monsoon Drought Crisis",
          "category": "DISASTER",
          "historicalDate": "August 2002",
          "description": "India faces its worst drought in 15 years as monsoon fails across 14 major agricultural states.",
          "baselinePartyEffects": {
            "bjp": { "content": -10, "power": 0 },
            "inc": { "content": 8, "power": 0 },
            "sp": { "content": 6, "power": 0 },
            "rjd": { "content": 6, "power": 0 }
          },
          "moodShift": { "economicStrain": 16, "antiIncumbency": 10 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Back Foodgrains Taskforce & Relief Allocation", "partyContentShift": 2, "partyPowerShift": 0, "moodShiftModifier": { "proIncumbency": 2 } },
            { "key": "AGITATE", "label": "Organize Farmers Rallies for Loan Waiver & Grain Subsidy", "partyContentShift": 10, "partyPowerShift": 1, "moodShiftModifier": { "populism": 8 } },
            { "key": "OPPOSE", "label": "Condemn Delayed Famine Relief Packages", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 6 } },
            { "key": "NEUTRAL", "label": "Propose National River Linking Project Relief", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2002_s4_ev3_akshardham_attack",
          "headline": "Akshardham Temple Terrorist Attack",
          "category": "DISASTER",
          "historicalDate": "September 24, 2002",
          "description": "Terrorists attack Akshardham Temple complex in Gandhinagar; NSG commandos eliminate terrorists after intense siege.",
          "baselinePartyEffects": {
            "bjp": { "content": 6, "power": 1 },
            "inc": { "content": 3, "power": 0 },
            "ydp": { "content": 4, "power": 0 }
          },
          "moodShift": { "nationalism": 16, "secularTrust": -6 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Support NSG Action & Strict Anti-Terror Measures", "partyContentShift": 7, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 6 } },
            { "key": "AGITATE", "label": "Demand Immediate Dismantling of Terror Networks", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 8 } },
            { "key": "OPPOSE", "label": "Question Intelligence Failure in Capital Vicinity", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 4 } },
            { "key": "NEUTRAL", "label": "Appeal for Calm & Inter-Faith Harmony", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": { "secularTrust": 5 } }
          ]
        },
        {
          "eventKey": "2002_s4_ev4_jk_assembly_elections",
          "headline": "Jammu & Kashmir Assembly Elections (Historic Turnout)",
          "category": "POLITICAL",
          "historicalDate": "October 2002",
          "description": "Credible, peaceful assembly polls lead to coalition government between PDP and Congress, ending NC dominance.",
          "baselinePartyEffects": {
            "inc": { "content": 10, "power": 1 },
            "bjp": { "content": 2, "power": 0 },
            "ydp": { "content": 5, "power": 0 }
          },
          "moodShift": { "nationalism": 12, "secularTrust": 8 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Hail Election Commission & Security Forces for Fair Polls", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 5 } },
            { "key": "AGITATE", "label": "Demand Healing Touch Policy Implementation in Valley", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "secularTrust": 5 } },
            { "key": "OPPOSE", "label": "Criticize Alliance Compromises with Regional Parties", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} },
            { "key": "NEUTRAL", "label": "Congratulate People of J&K for Democratic Participation", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2002_s4_ev5_idbi_debt_restructuring",
          "headline": "IDBI & Financial Institutions Restructuring Act",
          "category": "FINANCE",
          "historicalDate": "November 2002",
          "description": "Parliament passes legislation to convert IDBI into a commercial bank to clear non-performing assets.",
          "baselinePartyEffects": {
            "bjp": { "content": 5, "power": 0 },
            "inc": { "content": 2, "power": 0 },
            "cpim": { "content": -4, "power": 0 }
          },
          "moodShift": { "fiscalPrudence": 8, "economicStrain": -2 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Support Banking Sector Deregulation & Reform", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": { "fiscalPrudence": 4 } },
            { "key": "AGITATE", "label": "Protest Bank Employees Union Job Security Risks", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "populism": 4 } },
            { "key": "OPPOSE", "label": "Oppose Privatization of Public Financial Institutions", "partyContentShift": 5, "partyPowerShift": 0, "moodShiftModifier": {} },
            { "key": "NEUTRAL", "label": "Recommend Strict Corporate Governance Oversight", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        }
      ]
    },
    # Season 5
    {
      "seasonNumber": 5,
      "periodName": "Season 5 (Jan - Jun 2003)",
      "events": [
        {
          "eventKey": "2003_s5_ev1_vat_rollout_protests",
          "headline": "Value Added Tax (VAT) Resistance & Trader Strikes",
          "category": "FINANCE",
          "historicalDate": "January 2003",
          "description": "Trader associations launch nationwide bandhs protesting proposed transition to Value Added Tax.",
          "baselinePartyEffects": {
            "bjp": { "content": -6, "power": 0 },
            "inc": { "content": 5, "power": 0 },
            "ydp": { "content": 6, "power": 0 }
          },
          "moodShift": { "economicStrain": 8, "antiIncumbency": 6 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Defend VAT as Essential Modernization of Indirect Taxes", "partyContentShift": 2, "partyPowerShift": 0, "moodShiftModifier": { "fiscalPrudence": 5 } },
            { "key": "AGITATE", "label": "Support Trader Strikes Against Excessive Documentation", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "populism": 6 } },
            { "key": "OPPOSE", "label": "Demand Deferral of VAT Until State Consensus Is Reached", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 4 } },
            { "key": "NEUTRAL", "label": "Propose Phased Rollout with Threshold Exemptions", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2003_s5_ev2_frbm_act_introduction",
          "headline": "Passage of Fiscal Responsibility & Budget Management (FRBM) Act",
          "category": "FINANCE",
          "historicalDate": "February 2003",
          "description": "Parliament passes FRBM Act targeting zero revenue deficit and capping fiscal deficit at 3% of GDP.",
          "baselinePartyEffects": {
            "bjp": { "content": 8, "power": 1 },
            "inc": { "content": 4, "power": 0 },
            "cpim": { "content": -6, "power": 0 }
          },
          "moodShift": { "fiscalPrudence": 15, "proIncumbency": 4 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Vote YES for Institutional Fiscal Discipline", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "fiscalPrudence": 6 } },
            { "key": "AGITATE", "label": "Warn That Deficit Caps Will Slash Social Welfare Spending", "partyContentShift": 7, "partyPowerShift": 0, "moodShiftModifier": { "populism": 6 } },
            { "key": "OPPOSE", "label": "Oppose Rigid Constraints on Development Spending", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": {} },
            { "key": "NEUTRAL", "label": "Support Bill with Escape Clause for Emergency Years", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2003_s5_ev3_defense_modernization_deals",
          "headline": "Major Defense Modernization & Aircraft Carrier Procurement",
          "category": "ACHIEVEMENT",
          "historicalDate": "March 2003",
          "description": "Cabinet Committee on Security approves key defense procurements including Phalcon AWACS and carrier modernization.",
          "baselinePartyEffects": {
            "bjp": { "content": 7, "power": 0 },
            "inc": { "content": 2, "power": 0 },
            "ydp": { "content": 4, "power": 0 }
          },
          "moodShift": { "nationalism": 12, "proIncumbency": 4 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Back Strategic Defense Upgrades & Armed Forces Capabilities", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 5 } },
            { "key": "AGITATE", "label": "Demand Indigenous Defense Manufacturing Commitments", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 4 } },
            { "key": "OPPOSE", "label": "Scrutinize Offsets Transparency & Contract Pricing", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": { "antiCorruption": 4 } },
            { "key": "NEUTRAL", "label": "Acknowledge Strategic Defense Requirements", "partyContentShift": 2, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2003_s5_ev4_sars_outbreak_response",
          "headline": "Global SARS Outbreak & India Health Vigilance",
          "category": "DISASTER",
          "historicalDate": "April 2003",
          "description": "As SARS spreads across Asia, Indian health ministry enforces airport screening and quarantine protocols.",
          "baselinePartyEffects": {
            "bjp": { "content": 4, "power": 0 },
            "inc": { "content": 2, "power": 0 },
            "ydp": { "content": 4, "power": 0 }
          },
          "moodShift": { "proIncumbency": 4, "economicStrain": 4 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Support Airport Screening & Medical Contingency Measures", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": { "proIncumbency": 3 } },
            { "key": "AGITATE", "label": "Expose Shortages of Isolation Wards in Public Hospitals", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 4 } },
            { "key": "OPPOSE", "label": "Criticize Travel Regulations Impact on Tourism & Trade", "partyContentShift": 2, "partyPowerShift": 0, "moodShiftModifier": {} },
            { "key": "NEUTRAL", "label": "Publish Public Health Awareness Guidelines", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2003_s5_ev5_state_polls_himachal",
          "headline": "Himachal Pradesh & North-East Assembly Elections",
          "category": "POLITICAL",
          "historicalDate": "May 2003",
          "description": "Congress wins Himachal Assembly elections, boosting morale; regional coalitions hold sway in Tripura and Meghalaya.",
          "baselinePartyEffects": {
            "inc": { "content": 10, "power": 1 },
            "bjp": { "content": -6, "power": 0 },
            "cpim": { "content": 6, "power": 0 }
          },
          "moodShift": { "antiIncumbency": 8, "secularTrust": 4 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Reaffirm NDA Alliance Unity & National Agenda", "partyContentShift": 2, "partyPowerShift": 0, "moodShiftModifier": { "proIncumbency": 2 } },
            { "key": "AGITATE", "label": "Consolidate Anti-NDA Regional Blocs Ahead of General Polls", "partyContentShift": 8, "partyPowerShift": 1, "moodShiftModifier": { "antiIncumbency": 6 } },
            { "key": "OPPOSE", "label": "Claim Verdict as Rejection of NDA Economic Policies", "partyContentShift": 7, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 5 } },
            { "key": "NEUTRAL", "label": "Analyze Electoral Trends & Prepare State Units", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        }
      ]
    },
    # Season 6
    {
      "seasonNumber": 6,
      "periodName": "Season 6 (Jul - Dec 2003)",
      "events": [
        {
          "eventKey": "2003_s6_ev1_mumbai_twin_blasts",
          "headline": "Mumbai Twin Bomb Blasts (Gateway & Zaveri Bazaar)",
          "category": "DISASTER",
          "historicalDate": "August 25, 2003",
          "description": "Dual car bombs explode at Gateway of India and Zaveri Bazaar in Mumbai, killing 54 people.",
          "baselinePartyEffects": {
            "bjp": { "content": 4, "power": 0 },
            "inc": { "content": -4, "power": 0 },
            "ydp": { "content": 4, "power": 0 }
          },
          "moodShift": { "nationalism": 18, "secularTrust": -8 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Support Immediate Intelligence Mobilization & Counter-Terror", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 6 } },
            { "key": "AGITATE", "label": "Demand Stringent Action Against Sleeper Cells", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 8 } },
            { "key": "OPPOSE", "label": "Blame Security Lapses in Maharashtra State Administration", "partyContentShift": 5, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 5 } },
            { "key": "NEUTRAL", "label": "Organize Blood Donation & Peace Drives in Mumbai", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": { "secularTrust": 4 } }
          ]
        },
        {
          "eventKey": "2003_s6_ev2_chandrayaan1_approval",
          "headline": "Approval of Chandrayaan-1 Lunar Mission",
          "category": "ACHIEVEMENT",
          "historicalDate": "August 15, 2003",
          "description": "PM Vajpayee formally announces India's maiden lunar exploration mission, Chandrayaan-1, during Independence Day address.",
          "baselinePartyEffects": {
            "bjp": { "content": 10, "power": 1 },
            "inc": { "content": 3, "power": 0 },
            "ydp": { "content": 6, "power": 0 }
          },
          "moodShift": { "nationalism": 16, "proIncumbency": 6 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Hail Historic Announcement for Indian Space Science", "partyContentShift": 7, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 6 } },
            { "key": "AGITATE", "label": "Urge Increased Funding for Basic Education & Science Institutes", "partyContentShift": 5, "partyPowerShift": 0, "moodShiftModifier": {} },
            { "key": "OPPOSE", "label": "Question Scientific Priorities Amid Rural Poverty", "partyContentShift": -2, "partyPowerShift": 0, "moodShiftModifier": { "populism": 4 } },
            { "key": "NEUTRAL", "label": "Issue Felicitations to ISRO Rocket Engineers", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2003_s6_ev3_telgi_stamp_scam",
          "headline": "Exposure of Telgi Fake Stamp Paper Scam",
          "category": "CORRUPTION",
          "historicalDate": "October 2003",
          "description": "Multi-thousand crore counterfeit stamp paper scam led by Abdul Karim Telgi unravels across 12 states.",
          "baselinePartyEffects": {
            "inc": { "content": -8, "power": 0 },
            "bjp": { "content": -4, "power": 0 },
            "ydp": { "content": 8, "power": 0 }
          },
          "moodShift": { "antiCorruption": 22, "antiIncumbency": 10 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Support CBI Investigation & Digitization of Stamp Duty", "partyContentShift": 2, "partyPowerShift": 0, "moodShiftModifier": { "antiCorruption": 4 } },
            { "key": "AGITATE", "label": "Expose Police-Politician Nexus Across Affected States", "partyContentShift": 10, "partyPowerShift": 1, "moodShiftModifier": { "antiCorruption": 8 } },
            { "key": "OPPOSE", "label": "Demand Court-Monitored SIT Investigation", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 6 } },
            { "key": "NEUTRAL", "label": "Recommend Overhaul of Stamp Paper Distribution System", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2003_s6_ev4_loc_ceasefire_agreement",
          "headline": "Historic India-Pakistan Ceasefire Agreement",
          "category": "POLITICAL",
          "historicalDate": "November 25, 2003",
          "description": "India and Pakistan agree to a formal ceasefire along the Line of Control (LoC) and International Border.",
          "baselinePartyEffects": {
            "bjp": { "content": 12, "power": 1 },
            "inc": { "content": 4, "power": 0 },
            "cpim": { "content": 6, "power": 0 }
          },
          "moodShift": { "nationalism": 14, "proIncumbency": 8 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Back Prime Minister's Statesmanlike Peace Accord", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "proIncumbency": 6 } },
            { "key": "AGITATE", "label": "Insist Ceasefire Be Linked to Zero Terror Infiltration", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 5 } },
            { "key": "OPPOSE", "label": "Express Skepticism Over Sustainability of Accord", "partyContentShift": 2, "partyPowerShift": 0, "moodShiftModifier": {} },
            { "key": "NEUTRAL", "label": "Welcome Peace Measures for Border Villagers", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": { "secularTrust": 4 } }
          ]
        },
        {
          "eventKey": "2003_s6_ev5_assembly_elections_dec2003",
          "headline": "BJP Sweeps Assembly Polls in MP, Rajasthan & Chhattisgarh",
          "category": "POLITICAL",
          "historicalDate": "December 2003",
          "description": "BJP wins decisive majorities in Madhya Pradesh, Rajasthan, and Chhattisgarh, altering national momentum.",
          "baselinePartyEffects": {
            "bjp": { "content": 16, "power": 2 },
            "inc": { "content": -12, "power": -1 },
            "sp": { "content": 2, "power": 0 }
          },
          "moodShift": { "proIncumbency": 14, "antiIncumbency": -8 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Celebrate Verdict as Mandate for NDA Governance Model", "partyContentShift": 8, "partyPowerShift": 1, "moodShiftModifier": { "proIncumbency": 6 } },
            { "key": "AGITATE", "label": "Mobilize Regional Coalitions to Counter Electoral Surge", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": {} },
            { "key": "OPPOSE", "label": "Refocus Opposition Strategy on Rural Unemployment", "partyContentShift": 7, "partyPowerShift": 0, "moodShiftModifier": { "populism": 6 } },
            { "key": "NEUTRAL", "label": "Analyze State Elections & Assess Strategic Alliances", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        }
      ]
    },
    # Season 7
    {
      "seasonNumber": 7,
      "periodName": "Season 7 (Jan - Jun 2004)",
      "events": [
        {
          "eventKey": "2004_s7_ev1_saarc_islamabad_summit",
          "headline": "SAARC Islamabad Summit Peace Breakthrough",
          "category": "POLITICAL",
          "historicalDate": "January 2004",
          "description": "PM Vajpayee and President Musharraf agree to resume Composite Dialogue process during SAARC summit.",
          "baselinePartyEffects": {
            "bjp": { "content": 10, "power": 1 },
            "inc": { "content": 3, "power": 0 },
            "cpim": { "content": 5, "power": 0 }
          },
          "moodShift": { "nationalism": 12, "proIncumbency": 6 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Endorse Diplomatic Breakthrough & Regional Peace Vision", "partyContentShift": 7, "partyPowerShift": 0, "moodShiftModifier": { "proIncumbency": 5 } },
            { "key": "AGITATE", "label": "Demand Verification Mechanisms for Terror Infrastructure", "partyContentShift": 5, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 4 } },
            { "key": "OPPOSE", "label": "Caution Against Pre-Election Diplomatic PR Stunts", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} },
            { "key": "NEUTRAL", "label": "Support Bilateral Dialogue on Trade & Confidence Building", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2004_s7_ev2_india_shining_campaign",
          "headline": "'India Shining' Campaign Launch & Early Poll Push",
          "category": "POLITICAL",
          "historicalDate": "February 2004",
          "description": "NDA Govt launches Rs 500-crore 'India Shining' media campaign and recommends early dissolution of 13th Lok Sabha.",
          "baselinePartyEffects": {
            "bjp": { "content": 8, "power": 1 },
            "inc": { "content": -4, "power": 0 },
            "cpim": { "content": -4, "power": 0 }
          },
          "moodShift": { "proIncumbency": 10, "populism": -6 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Highlight Economic Growth & 8%+ GDP Expansion Rate", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "proIncumbency": 5 } },
            { "key": "AGITATE", "label": "Expose 'Rural Distress Behind India Shining Publicity'", "partyContentShift": 10, "partyPowerShift": 1, "moodShiftModifier": { "populism": 8 } },
            { "key": "OPPOSE", "label": "File Complaint Against Misuse of Govt Funds for Party Ads", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "antiCorruption": 6 } },
            { "key": "NEUTRAL", "label": "Focus Campaign on Balanced Urban-Rural Development", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2004_s7_ev3_insat3e_edusat_launches",
          "headline": "ISRO EDUSAT Launch Dedicated to Distance Education",
          "category": "ACHIEVEMENT",
          "historicalDate": "March 2004",
          "description": "ISRO prepares launch of EDUSAT (GSAT-3), world's first satellite built exclusively for satellite-based education.",
          "baselinePartyEffects": {
            "bjp": { "content": 6, "power": 0 },
            "inc": { "content": 3, "power": 0 },
            "ydp": { "content": 5, "power": 0 }
          },
          "moodShift": { "nationalism": 8, "proIncumbency": 3 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Commend Technology Drive for Remote Classroom Learning", "partyContentShift": 5, "partyPowerShift": 0, "moodShiftModifier": { "proIncumbency": 3 } },
            { "key": "AGITATE", "label": "Demand Free Receiver Terminals for Rural Govt Schools", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "populism": 4 } },
            { "key": "OPPOSE", "label": "Point Out Teacher Vacancies & School Infrastructure Gaps", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": {} },
            { "key": "NEUTRAL", "label": "Congratulate Educational Planners & Space Engineers", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2004_s7_ev4_14th_loksabha_election_verdict",
          "headline": "14th Lok Sabha Election Verdict: UPA Emerges Ahead",
          "category": "POLITICAL",
          "historicalDate": "May 13, 2004",
          "description": "General election results surprise analysts: Congress-led UPA secures 218 seats, NDA drops to 181 seats.",
          "baselinePartyEffects": {
            "inc": { "content": 20, "power": 4 },
            "bjp": { "content": -16, "power": -3 },
            "cpim": { "content": 14, "power": 2 },
            "ydp": { "content": 8, "power": 1 }
          },
          "moodShift": { "antiIncumbency": 20, "populism": 14 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Offer Conditional Support to INC-led Government Formation", "partyContentShift": 6, "partyPowerShift": 1, "moodShiftModifier": { "secularTrust": 5 } },
            { "key": "AGITATE", "label": "Leverage Kingmaker Seat Position for Policy Concessions", "partyContentShift": 10, "partyPowerShift": 2, "moodShiftModifier": { "populism": 6 } },
            { "key": "OPPOSE", "label": "Maintain Strict Third-Bloc Opposition Stance", "partyContentShift": 5, "partyPowerShift": 0, "moodShiftModifier": {} },
            { "key": "NEUTRAL", "label": "Congratulate Winner & Offer Issue-Based Support", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2004_s7_ev5_stock_market_black_monday",
          "headline": "Stock Market Circuit Breaker Black Monday Crash",
          "category": "FINANCE",
          "historicalDate": "May 17, 2004",
          "description": "Sensex plummets 11.1% in single day over market anxieties regarding Left Front influence on economic policy.",
          "baselinePartyEffects": {
            "inc": { "content": -8, "power": -1 },
            "cpim": { "content": -10, "power": 0 },
            "bjp": { "content": 6, "power": 0 }
          },
          "moodShift": { "economicStrain": 18, "fiscalPrudence": -8 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Support Manmohan Singh's Reassurances on Economic Reforms", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": { "fiscalPrudence": 6 } },
            { "key": "AGITATE", "label": "Condemn Market Speculation & Corporate Panic-Mongering", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "populism": 6 } },
            { "key": "OPPOSE", "label": "Warn That Left Dictation Will Derail National Economy", "partyContentShift": 7, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 5 } },
            { "key": "NEUTRAL", "label": "Call for Stable Financial Policy Statement", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        }
      ]
    },
    # Season 8
    {
      "seasonNumber": 8,
      "periodName": "Season 8 (Jul - Dec 2004)",
      "events": [
        {
          "eventKey": "2004_s8_ev1_manmohan_singh_sworn_in",
          "headline": "Dr. Manmohan Singh Sworn In as Prime Minister",
          "category": "POLITICAL",
          "historicalDate": "May 22, 2004",
          "description": "Dr. Manmohan Singh assumes office as PM after Sonia Gandhi declines post; UPA coalition takes office.",
          "baselinePartyEffects": {
            "inc": { "content": 14, "power": 2 },
            "bjp": { "content": -6, "power": 0 },
            "cpim": { "content": 8, "power": 1 }
          },
          "moodShift": { "proIncumbency": 10, "secularTrust": 10 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Welcome Renowned Economist PM & Offer Reform Support", "partyContentShift": 7, "partyPowerShift": 0, "moodShiftModifier": { "fiscalPrudence": 5 } },
            { "key": "AGITATE", "label": "Demand Immediate Rural Minimum Wage Fixation", "partyContentShift": 7, "partyPowerShift": 0, "moodShiftModifier": { "populism": 6 } },
            { "key": "OPPOSE", "label": "Criticize Dual Power Center Arrangement (PM & NAC)", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 4 } },
            { "key": "NEUTRAL", "label": "Extend Standard Parliamentary Cooperation to New Govt", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2004_s8_ev2_ncmp_unveiled",
          "headline": "National Common Minimum Programme (NCMP) Unveiled",
          "category": "POLITICAL",
          "historicalDate": "June 2004",
          "description": "UPA and Left allies release NCMP focusing on rural employment, education, agriculture, and social harmony.",
          "baselinePartyEffects": {
            "inc": { "content": 10, "power": 1 },
            "cpim": { "content": 10, "power": 1 },
            "bjp": { "content": -4, "power": 0 }
          },
          "moodShift": { "populism": 16, "secularTrust": 8 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Endorse Focus on Health, Education & Employment Guarantee", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "populism": 5 } },
            { "key": "AGITATE", "label": "Demand Timelines for Universal Guarantee Implementation", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "populism": 6 } },
            { "key": "OPPOSE", "label": "Warn of Fiscal Bankruptcy from Unfunded Populist Schemes", "partyContentShift": 5, "partyPowerShift": 0, "moodShiftModifier": { "fiscalPrudence": 5 } },
            { "key": "NEUTRAL", "label": "Support Positive Social Provisions While Monitoring Execution", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2004_s8_ev3_kumbakonam_fire_tragedy",
          "headline": "Kumbakonam School Fire Tragedy",
          "category": "DISASTER",
          "historicalDate": "July 16, 2004",
          "description": "Devastating fire at Lord Krishna School in Kumbakonam, Tamil Nadu, claims lives of 94 school children.",
          "baselinePartyEffects": {
            "inc": { "content": -4, "power": 0 },
            "bjp": { "content": 2, "power": 0 },
            "ydp": { "content": 5, "power": 0 }
          },
          "moodShift": { "antiIncumbency": 8, "antiCorruption": 10 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Support Emergency School Safety Audits & Relief Grants", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": { "proIncumbency": 2 } },
            { "key": "AGITATE", "label": "Lead Protests Against Corrupt School Building Inspectors", "partyContentShift": 9, "partyPowerShift": 0, "moodShiftModifier": { "antiCorruption": 8 } },
            { "key": "OPPOSE", "label": "Demand Criminal Prosecution of School Management & Officials", "partyContentShift": 7, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 5 } },
            { "key": "NEUTRAL", "label": "Establish YDP Victim Support Trust Fund", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2004_s8_ev4_nregs_drafting",
          "headline": "Introduction of Rural Employment Guarantee Scheme Bill",
          "category": "ACHIEVEMENT",
          "historicalDate": "August 2004",
          "description": "National Advisory Council (NAC) drafts historic legislation guaranteeing 100 days wage employment per rural family.",
          "baselinePartyEffects": {
            "inc": { "content": 12, "power": 1 },
            "cpim": { "content": 8, "power": 0 },
            "bjp": { "content": -2, "power": 0 }
          },
          "moodShift": { "populism": 20, "proIncumbency": 8 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Vote YES & Celebrate Historic Social Protection Law", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "populism": 6 } },
            { "key": "AGITATE", "label": "Demand Expansion of Guarantee to Urban Unemployed", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "populism": 8 } },
            { "key": "OPPOSE", "label": "Highlight Potential Corruption & Leakages in Wage Delivery", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": { "antiCorruption": 5 } },
            { "key": "NEUTRAL", "label": "Propose Direct Bank Transfer Mechanism to Plug Leaks", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": { "fiscalPrudence": 4 } }
          ]
        },
        {
          "eventKey": "2004_s8_ev5_tsunami_catastrophe",
          "headline": "Indian Ocean Tsunami Catastrophe",
          "category": "DISASTER",
          "historicalDate": "December 26, 2004",
          "description": "Massive 9.1 magnitude undersea earthquake triggers destructive tsunami along Tamil Nadu, AP, Andaman coast; 18,000 dead.",
          "baselinePartyEffects": {
            "inc": { "content": 4, "power": 0 },
            "bjp": { "content": 2, "power": 0 },
            "ydp": { "content": 6, "power": 0 }
          },
          "moodShift": { "nationalism": 16, "antiIncumbency": 4 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Support Govt Rejection of Foreign Aid & Self-Reliant Relief", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 8 } },
            { "key": "AGITATE", "label": "Mobilize Cadres for Coastal Rehabilitation & Disaster Warning Systems", "partyContentShift": 9, "partyPowerShift": 0, "moodShiftModifier": { "populism": 6 } },
            { "key": "OPPOSE", "label": "Criticize Delayed Tsunami Early Warning Buoy Deployment", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 4 } },
            { "key": "NEUTRAL", "label": "Coordinate Relief Supply Trains from States", "partyContentShift": 5, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        }
      ]
    },
    # Season 9
    {
      "seasonNumber": 9,
      "periodName": "Season 9 (Jan - Jun 2005)",
      "events": [
        {
          "eventKey": "2005_s9_ev1_nrhm_launch",
          "headline": "Launch of National Rural Health Mission (NRHM)",
          "category": "ACHIEVEMENT",
          "historicalDate": "April 12, 2005",
          "description": "PM Manmohan Singh launches NRHM to provide accessible, affordable, and quality healthcare to rural populations.",
          "baselinePartyEffects": {
            "inc": { "content": 10, "power": 1 },
            "cpim": { "content": 4, "power": 0 },
            "ydp": { "content": 5, "power": 0 }
          },
          "moodShift": { "proIncumbency": 8, "populism": 10 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Praise Creation of ASHA Workers & Primary Health Hubs", "partyContentShift": 7, "partyPowerShift": 0, "moodShiftModifier": { "proIncumbency": 4 } },
            { "key": "AGITATE", "label": "Demand Minimum Wage & Permanent Status for ASHA Workers", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "populism": 6 } },
            { "key": "OPPOSE", "label": "Highlight Shortage of Doctors & Medicines in Health Centers", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": {} },
            { "key": "NEUTRAL", "label": "Support Maternal & Child Health Focus", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2005_s9_ev2_rti_act_passed",
          "headline": "Parliament Passes Landmark Right to Information (RTI) Act",
          "category": "ACHIEVEMENT",
          "historicalDate": "May 11, 2005",
          "description": "Historic transparency law passed, empowering citizens to request government information and combat corruption.",
          "baselinePartyEffects": {
            "inc": { "content": 14, "power": 1 },
            "cpim": { "content": 8, "power": 0 },
            "bjp": { "content": 4, "power": 0 },
            "ydp": { "content": 8, "power": 0 }
          },
          "moodShift": { "antiCorruption": 25, "secularTrust": 12 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Vote YES & Celebrate Democracy Transparency Benchmark", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "antiCorruption": 8 } },
            { "key": "AGITATE", "label": "Demand Removal of Security Agency Exemption Clauses", "partyContentShift": 7, "partyPowerShift": 0, "moodShiftModifier": { "antiCorruption": 6 } },
            { "key": "OPPOSE", "label": "Warn That Bureaucratic Red Tape Will Stall Information Access", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} },
            { "key": "NEUTRAL", "label": "Establish YDP Citizen RTI Guidance Clinics", "partyContentShift": 5, "partyPowerShift": 0, "moodShiftModifier": { "secularTrust": 4 } }
          ]
        },
        {
          "eventKey": "2005_s9_ev3_sensex_7000_milestone",
          "headline": "Sensex Crosses Landmark 7,000 Mark",
          "category": "FINANCE",
          "historicalDate": "June 2005",
          "description": "Stock market surges past 7,000 points driven by robust FII inflows, corporate profits, and economic expansion.",
          "baselinePartyEffects": {
            "inc": { "content": 8, "power": 1 },
            "bjp": { "content": 2, "power": 0 },
            "cpim": { "content": -4, "power": 0 }
          },
          "moodShift": { "proIncumbency": 6, "economicStrain": -6 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Attribute Market Boom to Sound Macroeconomic Policy", "partyContentShift": 5, "partyPowerShift": 0, "moodShiftModifier": { "proIncumbency": 4 } },
            { "key": "AGITATE", "label": "Highlight Widening Wealth Inequality & Agricultural Lag", "partyContentShift": 7, "partyPowerShift": 0, "moodShiftModifier": { "populism": 6 } },
            { "key": "OPPOSE", "label": "Warn of Overheating Asset Bubble & Speculative Capital", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": { "fiscalPrudence": 4 } },
            { "key": "NEUTRAL", "label": "Encourage Retail Investor Financial Literacy Programs", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2005_s9_ev4_advani_jinnah_controversy",
          "headline": "LK Advani's Jinnah Remarks Controversy in Pakistan",
          "category": "POLITICAL",
          "historicalDate": "June 2005",
          "description": "BJP Leader LK Advani describes M.A. Jinnah as 'secular' during Karachi visit, sparking storm within Sangh Parivar.",
          "baselinePartyEffects": {
            "bjp": { "content": -12, "power": -1 },
            "inc": { "content": 6, "power": 0 },
            "cpim": { "content": 4, "power": 0 }
          },
          "moodShift": { "nationalism": -6, "secularTrust": 6 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Reaffirm Moderate Statesmanlike Diplomatic Engagement", "partyContentShift": 2, "partyPowerShift": 0, "moodShiftModifier": { "secularTrust": 4 } },
            { "key": "AGITATE", "label": "Expose Ideological Contradictions & Rift in Opposition Leadership", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": -4 } },
            { "key": "OPPOSE", "label": "Condemn Distortion of Partition History", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 6 } },
            { "key": "NEUTRAL", "label": "Decline Comment on Internal Opposition Turmoil", "partyContentShift": 2, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2005_s9_ev5_bihar_hung_assembly",
          "headline": "Bihar Assembly Election Hung Verdict & President's Rule",
          "category": "POLITICAL",
          "historicalDate": "February - May 2005",
          "description": "Feb 2005 Bihar elections result in hung assembly; Governor dissolves house, triggering political conflict.",
          "baselinePartyEffects": {
            "rjd": { "content": -8, "power": -1 },
            "bjp": { "content": 6, "power": 0 },
            "jdu": { "content": 8, "power": 1 },
            "inc": { "content": -4, "power": 0 }
          },
          "moodShift": { "antiIncumbency": 10, "antiCorruption": 6 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Support Constitutional Validity of Governor's Action", "partyContentShift": -3, "partyPowerShift": 0, "moodShiftModifier": {} },
            { "key": "AGITATE", "label": "Demand Fresh Free and Fair Polls Under Central Forces", "partyContentShift": 8, "partyPowerShift": 1, "moodShiftModifier": { "antiCorruption": 6 } },
            { "key": "OPPOSE", "label": "Condemn Subversion of Democratic Mandate in Bihar", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 6 } },
            { "key": "NEUTRAL", "label": "Prepare YDP Candidates for Impending Re-Elections", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        }
      ]
    },
    # Season 10
    {
      "seasonNumber": 10,
      "periodName": "Season 10 (Jul - Dec 2005)",
      "events": [
        {
          "eventKey": "2005_s10_ev1_mumbai_deluge_july26",
          "headline": "26th July Mumbai Torrential Deluge Crisis",
          "category": "DISASTER",
          "historicalDate": "July 26, 2005",
          "description": "Record 944 mm rainfall in 24 hours paralyzes Mumbai, causing over 1,000 fatalities and complete civic paralysis.",
          "baselinePartyEffects": {
            "inc": { "content": -8, "power": 0 },
            "bjp": { "content": 3, "power": 0 },
            "ydp": { "content": 5, "power": 0 }
          },
          "moodShift": { "antiIncumbency": 12, "antiCorruption": 10 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Support Central Relief Grant & Disaster Management Force Setup", "partyContentShift": 3, "partyPowerShift": 0, "moodShiftModifier": { "proIncumbency": 2 } },
            { "key": "AGITATE", "label": "Expose Builder Lobby Encroachments & Drainage Neglect", "partyContentShift": 10, "partyPowerShift": 0, "moodShiftModifier": { "antiCorruption": 8 } },
            { "key": "OPPOSE", "label": "Demand Dismissal of Municipal Corporation Leadership", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 6 } },
            { "key": "NEUTRAL", "label": "Deploy YDP Relief Columns Across Suburbs", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2005_s10_ev2_indous_nuclear_deal",
          "headline": "Indo-US Civil Nuclear Agreement Joint Statement",
          "category": "ACHIEVEMENT",
          "historicalDate": "July 18, 2005",
          "description": "PM Manmohan Singh and President George W. Bush announce landmark civilian nuclear energy cooperation agreement in Washington.",
          "baselinePartyEffects": {
            "inc": { "content": 14, "power": 2 },
            "cpim": { "content": -12, "power": -1 },
            "bjp": { "content": -6, "power": 0 },
            "ydp": { "content": 8, "power": 0 }
          },
          "moodShift": { "nationalism": 15, "proIncumbency": 8 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Back Historic Deal Ending Nuclear Isolation & Securing Energy", "partyContentShift": 8, "partyPowerShift": 1, "moodShiftModifier": { "nationalism": 6 } },
            { "key": "AGITATE", "label": "Demand Safeguards for Indigenous Fast Breeder Reactor Program", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 5 } },
            { "key": "OPPOSE", "label": "Oppose Compromising Strategic Autonomy to Foreign Power", "partyContentShift": 5, "partyPowerShift": 0, "moodShiftModifier": {} },
            { "key": "NEUTRAL", "label": "Request Detailed Parliamentary Debate on IAEA Separation Plan", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2005_s10_ev3_kashmir_earthquake",
          "headline": "Kashmir Border Earthquake Disaster",
          "category": "DISASTER",
          "historicalDate": "October 8, 2005",
          "description": "7.6 magnitude earthquake strikes Jammu & Kashmir region, causing severe destruction across LoC.",
          "baselinePartyEffects": {
            "inc": { "content": 4, "power": 0 },
            "bjp": { "content": 2, "power": 0 },
            "ydp": { "content": 5, "power": 0 }
          },
          "moodShift": { "nationalism": 12, "secularTrust": 6 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Support Armed Forces Disaster Relief & Cross-LoC Aid Points", "partyContentShift": 7, "partyPowerShift": 0, "moodShiftModifier": { "nationalism": 6 } },
            { "key": "AGITATE", "label": "Demand Winter Shelter Housing for Displaced Valley Families", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "populism": 6 } },
            { "key": "OPPOSE", "label": "Criticize Slow Tenting & Medical Assistance Distribution", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": { "antiIncumbency": 4 } },
            { "key": "NEUTRAL", "label": "Send All-Party Relief Supplies to Border Villages", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": { "secularTrust": 4 } }
          ]
        },
        {
          "eventKey": "2005_s10_ev4_cash_for_query_sting",
          "headline": "Cash-for-Query Sting Exposes Parliament Corruption",
          "category": "CORRUPTION",
          "historicalDate": "December 12, 2005",
          "description": "Cobrapost sting operation catches 11 Members of Parliament accepting cash bribes to ask questions in Lok Sabha.",
          "baselinePartyEffects": {
            "bjp": { "content": -10, "power": -1 },
            "inc": { "content": -6, "power": 0 },
            "bsp": { "content": -8, "power": 0 },
            "ydp": { "content": 10, "power": 0 }
          },
          "moodShift": { "antiCorruption": 28, "antiIncumbency": 14 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Vote YES for Immediate Expulsion of All 11 Corrupt MPs", "partyContentShift": 8, "partyPowerShift": 0, "moodShiftModifier": { "antiCorruption": 10 } },
            { "key": "AGITATE", "label": "Launch Public Clean Politics Crusade & Reform Drive", "partyContentShift": 12, "partyPowerShift": 1, "moodShiftModifier": { "antiCorruption": 12 } },
            { "key": "OPPOSE", "label": "Demand Privileges Committee Due Process Before Expulsion", "partyContentShift": -4, "partyPowerShift": 0, "moodShiftModifier": {} },
            { "key": "NEUTRAL", "label": "Support Code of Conduct Oversight for Parliamentarians", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        },
        {
          "eventKey": "2005_s10_ev5_vat_nationwide_completion",
          "headline": "Nationwide VAT Implementation Milestone",
          "category": "FINANCE",
          "historicalDate": "December 2005",
          "description": "25 states successfully transition to Value Added Tax regime, boosting tax revenue collections by 14%.",
          "baselinePartyEffects": {
            "inc": { "content": 10, "power": 1 },
            "cpim": { "content": 4, "power": 0 },
            "bjp": { "content": -2, "power": 0 }
          },
          "moodShift": { "fiscalPrudence": 12, "proIncumbency": 6 },
          "reactions": [
            { "key": "SUPPORT_GOVT", "label": "Commend Empowered Committee of State Finance Ministers", "partyContentShift": 6, "partyPowerShift": 0, "moodShiftModifier": { "fiscalPrudence": 5 } },
            { "key": "AGITATE", "label": "Demand Lower VAT Rates on Essential Medicines & Foodgrains", "partyContentShift": 7, "partyPowerShift": 0, "moodShiftModifier": { "populism": 6 } },
            { "key": "OPPOSE", "label": "Point Out Compliance Costs Burdening Small Retailers", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": {} },
            { "key": "NEUTRAL", "label": "Advocate for Tax Revenue Sharing Safeguards for States", "partyContentShift": 4, "partyPowerShift": 0, "moodShiftModifier": {} }
          ]
        }
      ]
    }
  ],
  "legislativeBills": [
    {
      "billKey": "POTA_2002",
      "title": "Prevention of Terrorism Act (POTA), 2002",
      "introducedYear": 2002,
      "category": "SECURITY_LAW",
      "description": "Special anti-terror law expanding police detention powers and admissibility of confessions.",
      "govtStance": "YES",
      "oppositionStance": "NO",
      "publicOpinionShift": {
        "IF_YES": { "nationalism": 10, "secularTrust": -5 },
        "IF_NO": { "nationalism": -5, "secularTrust": 8 }
      },
      "partyContentImpact": {
        "IF_YES_GOVT_ALLIANCE": 8,
        "IF_YES_OPPOSITION_ALLIANCE": -10,
        "IF_NO_GOVT_ALLIANCE": -12,
        "IF_NO_OPPOSITION_ALLIANCE": 10
      }
    },
    {
      "billKey": "FRBM_2003",
      "title": "Fiscal Responsibility and Budget Management (FRBM) Act, 2003",
      "introducedYear": 2003,
      "category": "FINANCE",
      "description": "Statutory framework mandating reduction of fiscal deficits and ensuring long-term fiscal stability.",
      "govtStance": "YES",
      "oppositionStance": "NO",
      "publicOpinionShift": {
        "IF_YES": { "fiscalPrudence": 12 },
        "IF_NO": { "populism": 8 }
      },
      "partyContentImpact": {
        "IF_YES": 5,
        "IF_NO": -3
      }
    },
    {
      "billKey": "RTI_2005",
      "title": "Right to Information (RTI) Act, 2005",
      "introducedYear": 2005,
      "category": "CONSTITUTIONAL",
      "description": "Landmark transparency law guaranteeing citizen access to public records and government files.",
      "govtStance": "YES",
      "oppositionStance": "YES",
      "publicOpinionShift": {
        "IF_YES": { "antiCorruption": 15, "secularTrust": 6 },
        "IF_NO": { "antiCorruption": -15 }
      },
      "partyContentImpact": {
        "IF_YES": 8,
        "IF_NO": -12
      }
    }
  ]
}

with open('/Users/supratikde/Desktop/DEV/Political party Sim/seed-data/national/national_configs/2001.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Successfully generated 2001.json with", len(data['seasons']), "seasons and", sum(len(s['events']) for s in data['seasons']), "total events!")
