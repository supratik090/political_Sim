import json

# MongoDB Scenario definitions mapping to 2001 National Config state seat data
# Each state defines exactly the 3 parties from MongoDB: rulingPartyKey, oppositionPartyKey, and ydp (Third Party)

state_seat_data = [
  {
    "stateName": "Uttar Pradesh",
    "totalSeats": 80,
    "rulingPartyKey": "bjp",
    "oppositionPartyKey": "sp",
    "supportPercentages": { "bjp": 40, "sp": 30, "ydp": 20 },
    "initialSeats": { "bjp": 36, "sp": 27, "ydp": 17 }
  },
  {
    "stateName": "Maharashtra",
    "totalSeats": 48,
    "rulingPartyKey": "inc",
    "oppositionPartyKey": "shiv_sena",
    "supportPercentages": { "inc": 44, "shiv_sena": 32, "ydp": 14 },
    "initialSeats": { "inc": 24, "shiv_sena": 17, "ydp": 7 }
  },
  {
    "stateName": "West Bengal",
    "totalSeats": 42,
    "rulingPartyKey": "cpim",
    "oppositionPartyKey": "inc",
    "supportPercentages": { "cpim": 42, "inc": 30, "ydp": 10 },
    "initialSeats": { "cpim": 21, "inc": 16, "ydp": 5 }
  },
  {
    "stateName": "Bihar",
    "totalSeats": 40,
    "rulingPartyKey": "rjd",
    "oppositionPartyKey": "bjp",
    "supportPercentages": { "rjd": 30, "bjp": 36, "ydp": 15 },
    "initialSeats": { "rjd": 15, "bjp": 18, "ydp": 7 }
  },
  {
    "stateName": "Tamil Nadu",
    "totalSeats": 39,
    "rulingPartyKey": "aidmk",
    "oppositionPartyKey": "dmk",
    "supportPercentages": { "aidmk": 48, "dmk": 28, "ydp": 14 },
    "initialSeats": { "aidmk": 21, "dmk": 12, "ydp": 6 }
  },
  {
    "stateName": "Andhra Pradesh",
    "totalSeats": 42,
    "rulingPartyKey": "tdp",
    "oppositionPartyKey": "inc",
    "supportPercentages": { "tdp": 42, "inc": 28, "ydp": 15 },
    "initialSeats": { "tdp": 21, "inc": 14, "ydp": 7 }
  },
  {
    "stateName": "Madhya Pradesh",
    "totalSeats": 29,
    "rulingPartyKey": "bjp",
    "oppositionPartyKey": "inc",
    "supportPercentages": { "bjp": 45, "inc": 32, "ydp": 15 },
    "initialSeats": { "bjp": 14, "inc": 10, "ydp": 5 }
  },
  {
    "stateName": "Karnataka",
    "totalSeats": 28,
    "rulingPartyKey": "inc",
    "oppositionPartyKey": "bjp",
    "supportPercentages": { "inc": 42, "bjp": 34, "ydp": 14 },
    "initialSeats": { "inc": 13, "bjp": 11, "ydp": 4 }
  },
  {
    "stateName": "Gujarat",
    "totalSeats": 26,
    "rulingPartyKey": "bjp",
    "oppositionPartyKey": "inc",
    "supportPercentages": { "bjp": 50, "inc": 30, "ydp": 12 },
    "initialSeats": { "bjp": 14, "inc": 9, "ydp": 3 }
  },
  {
    "stateName": "Rajasthan",
    "totalSeats": 25,
    "rulingPartyKey": "bjp",
    "oppositionPartyKey": "inc",
    "supportPercentages": { "bjp": 38, "inc": 34, "ydp": 18 },
    "initialSeats": { "bjp": 11, "inc": 9, "ydp": 5 }
  },
  {
    "stateName": "Odisha",
    "totalSeats": 21,
    "rulingPartyKey": "bjd",
    "oppositionPartyKey": "inc",
    "supportPercentages": { "bjd": 40, "inc": 30, "ydp": 14 },
    "initialSeats": { "bjd": 10, "inc": 7, "ydp": 4 }
  },
  {
    "stateName": "Kerala",
    "totalSeats": 20,
    "rulingPartyKey": "inc",
    "oppositionPartyKey": "cpim",
    "supportPercentages": { "inc": 43, "cpim": 42, "ydp": 15 },
    "initialSeats": { "inc": 9, "cpim": 8, "ydp": 3 }
  },
  {
    "stateName": "Jharkhand",
    "totalSeats": 14,
    "rulingPartyKey": "bjp",
    "oppositionPartyKey": "jmm",
    "supportPercentages": { "bjp": 42, "jmm": 30, "ydp": 15 },
    "initialSeats": { "bjp": 7, "jmm": 5, "ydp": 2 }
  },
  {
    "stateName": "Assam",
    "totalSeats": 14,
    "rulingPartyKey": "inc",
    "oppositionPartyKey": "agp",
    "supportPercentages": { "inc": 45, "agp": 30, "ydp": 15 },
    "initialSeats": { "inc": 7, "agp": 5, "ydp": 2 }
  },
  {
    "stateName": "Punjab",
    "totalSeats": 13,
    "rulingPartyKey": "akali_dal",
    "oppositionPartyKey": "inc",
    "supportPercentages": { "akali_dal": 45, "inc": 32, "ydp": 15 },
    "initialSeats": { "akali_dal": 6, "inc": 5, "ydp": 2 }
  },
  {
    "stateName": "Chhattisgarh",
    "totalSeats": 11,
    "rulingPartyKey": "bjp",
    "oppositionPartyKey": "inc",
    "supportPercentages": { "bjp": 44, "inc": 34, "ydp": 12 },
    "initialSeats": { "bjp": 5, "inc": 4, "ydp": 2 }
  },
  {
    "stateName": "Haryana",
    "totalSeats": 10,
    "rulingPartyKey": "inld",
    "oppositionPartyKey": "inc",
    "supportPercentages": { "inld": 42, "inc": 32, "ydp": 16 },
    "initialSeats": { "inld": 5, "inc": 3, "ydp": 2 }
  },
  {
    "stateName": "Delhi",
    "totalSeats": 7,
    "rulingPartyKey": "inc",
    "oppositionPartyKey": "bjp",
    "supportPercentages": { "inc": 48, "bjp": 34, "ydp": 15 },
    "initialSeats": { "inc": 4, "bjp": 2, "ydp": 1 }
  },
  {
    "stateName": "Jammu & Kashmir",
    "totalSeats": 6,
    "rulingPartyKey": "nc",
    "oppositionPartyKey": "bjp",
    "supportPercentages": { "nc": 45, "bjp": 30, "ydp": 15 },
    "initialSeats": { "nc": 3, "bjp": 2, "ydp": 1 }
  },
  {
    "stateName": "Uttarakhand",
    "totalSeats": 5,
    "rulingPartyKey": "bjp",
    "oppositionPartyKey": "inc",
    "supportPercentages": { "bjp": 42, "inc": 32, "ydp": 16 },
    "initialSeats": { "bjp": 3, "inc": 1, "ydp": 1 }
  },
  {
    "stateName": "Himachal Pradesh",
    "totalSeats": 4,
    "rulingPartyKey": "bjp",
    "oppositionPartyKey": "inc",
    "supportPercentages": { "bjp": 46, "inc": 36, "ydp": 12 },
    "initialSeats": { "bjp": 2, "inc": 1, "ydp": 1 }
  },
  {
    "stateName": "Goa",
    "totalSeats": 2,
    "rulingPartyKey": "inc",
    "oppositionPartyKey": "bjp",
    "supportPercentages": { "inc": 38, "bjp": 32, "ydp": 15 },
    "initialSeats": { "inc": 1, "bjp": 1 }
  },
  {
    "stateName": "Manipur",
    "totalSeats": 2,
    "rulingPartyKey": "inc",
    "oppositionPartyKey": "others",
    "supportPercentages": { "inc": 50, "others": 35, "ydp": 15 },
    "initialSeats": { "inc": 1, "others": 1 }
  },
  {
    "stateName": "Meghalaya",
    "totalSeats": 2,
    "rulingPartyKey": "inc",
    "oppositionPartyKey": "others",
    "supportPercentages": { "inc": 50, "others": 35, "ydp": 15 },
    "initialSeats": { "inc": 1, "others": 1 }
  },
  {
    "stateName": "Tripura",
    "totalSeats": 2,
    "rulingPartyKey": "cpim",
    "oppositionPartyKey": "inc",
    "supportPercentages": { "cpim": 52, "inc": 33, "ydp": 15 },
    "initialSeats": { "cpim": 1, "inc": 1 }
  },
  {
    "stateName": "Arunachal Pradesh",
    "totalSeats": 2,
    "rulingPartyKey": "inc",
    "oppositionPartyKey": "bjp",
    "supportPercentages": { "inc": 50, "bjp": 35, "ydp": 15 },
    "initialSeats": { "inc": 1, "bjp": 1 }
  },
  {
    "stateName": "Nagaland",
    "totalSeats": 1,
    "rulingPartyKey": "others",
    "oppositionPartyKey": "inc",
    "supportPercentages": { "others": 60, "inc": 40 },
    "initialSeats": { "others": 1 }
  },
  {
    "stateName": "Mizoram",
    "totalSeats": 1,
    "rulingPartyKey": "others",
    "oppositionPartyKey": "inc",
    "supportPercentages": { "others": 60, "inc": 40 },
    "initialSeats": { "others": 1 }
  },
  {
    "stateName": "Sikkim",
    "totalSeats": 1,
    "rulingPartyKey": "others",
    "oppositionPartyKey": "inc",
    "supportPercentages": { "others": 60, "inc": 40 },
    "initialSeats": { "others": 1 }
  },
  {
    "stateName": "Puducherry & UTs",
    "totalSeats": 7,
    "rulingPartyKey": "inc",
    "oppositionPartyKey": "bjp",
    "supportPercentages": { "inc": 45, "bjp": 30, "ydp": 15 },
    "initialSeats": { "inc": 4, "bjp": 2, "ydp": 1 }
  }
]

with open('/Users/supratikde/Desktop/DEV/Political party Sim/seed-data/national/national_configs/2001.json', 'r') as f:
    full_config = json.load(f)

full_config['stateSeatData'] = state_seat_data

with open('/Users/supratikde/Desktop/DEV/Political party Sim/seed-data/national/national_configs/2001.json', 'w') as f:
    json.dump(full_config, f, indent=2)

print("Updated stateSeatData in 2001.json to match MongoDB state scenarios (3 parties per state: Ruling, Opposition, YDP)!")
