# National Politics Mode — Implementation Plan

## Overview

A meta-strategy game mode layered on top of the existing State Campaign system.
Players choose at login / home: **State Mode** or **National Mode**.
Both are independent — a player may run both simultaneously with separate save states.

---

## Technical Architecture

### 1. Data Isolation & Persistence
- **State Mode**: Uses existing `games` collection and state scenario engine.
- **National Mode**: Uses dedicated `national_configs` and `national_games` MongoDB collections.
- **Save State Separation**: National Mode progress is saved independently from State Mode progress.
- **Admin Editability**: All `national_configs` (alliances, parties, state seats, 50 seasonal events, and 3 legislative bills per era) are loaded into MongoDB from JSON seed files (`seed-data/national/national_configs/*.json`) via `NationalConfigSeeder.java` and editable directly via the Admin Console endpoints (`/api/admin/national-configs/*`).

### 2. Mongo Data Models & Schema

#### `NationalConfig` (Collection: `national_configs`)
```json
{
  "_id": "651234...",
  "era": 2001,
  "title": "The NDA Experiment",
  "description": "Vajpayee leads NDA coalition...",
  "supportedIdeologies": [
    "DEVELOPMENTAL_PROGRESSIVE",
    "NATIONALIST_CONSERVATIVE",
    "CENTRIST_SECULAR",
    "LEFT_SOCIALIST",
    "REGIONAL_SOCIALIST"
  ],
  "alliances": [
    { "key": "NDA", "name": "National Democratic Alliance", "color": "#FF9933", "leaderParty": "bjp" }
  ],
  "parties": [
    { "partyKey": "ydp", "name": "Youth Development Party", "shortName": "YDP", "ideology": "DEVELOPMENTAL_PROGRESSIVE", "initialContent": 80, "isPlayerSelectable": true }
  ],
  "stateSeatData": [
    { 
      "stateName": "Uttar Pradesh", 
      "totalSeats": 80, 
      "rulingPartyKey": "bjp", 
      "oppositionPartyKey": "sp", 
      "supportPercentages": { "bjp": 35, "sp": 28, "bsp": 24, "ydp": 13 },
      "initialSeats": { "bjp": 28, "sp": 22, "bsp": 19, "ydp": 11 } 
    }
  ],
  "seasons": [
    {
      "seasonNumber": 1,
      "periodName": "Season 1 (Jan - Jun 2001)",
      "events": [
        {
          "eventKey": "2001_s1_ev1_kutch_earthquake",
          "headline": "Devastating Kutch Earthquake",
          "category": "DISASTER",
          "historicalDate": "January 26, 2001",
          "description": "...",
          "baselineIdeologyEffects": { 
            "NATIONALIST_CONSERVATIVE": { "content": -4, "power": 0 },
            "CENTRIST_SECULAR": { "content": 4, "power": 0 }
          },
          "publicOpinionShift": { "supportForGovt": -6, "morale": -12 },
          "reactions": [
            { 
              "key": "SUPPORT_GOVT", 
              "label": "Support Govt Relief", 
              "partyContentShift": 4, 
              "partyPowerShift": 0, 
              "publicOpinionShiftModifier": { "supportForGovt": 4, "morale": 4 } 
            }
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
      "ideologyStances": { "NATIONALIST_CONSERVATIVE": "YES", "CENTRIST_SECULAR": "NO" },
      "publicOpinionShift": { "IF_PASSED": { "supportForGovt": 8, "morale": 4 }, "IF_REJECTED": { "supportForGovt": -8, "morale": -4 } },
      "ideologyContentImpact": { "IF_VOTE_YES": { "NATIONALIST_CONSERVATIVE": 8, "CENTRIST_SECULAR": -10 } }
    }
  ]
}
```

### 3. Real Events Engine (5 per Season) & Legislative Bills
- **5 Events per Season**: 10 seasons = 50 real events per era across 5 categories (`POLITICAL`, `FINANCE`, `DISASTER`, `CORRUPTION`, `ACHIEVEMENT`).
- **5 Core Ideologies**: Event impacts apply to parties via ideology (`DEVELOPMENTAL_PROGRESSIVE`, `NATIONALIST_CONSERVATIVE`, `CENTRIST_SECULAR`, `LEFT_SOCIALIST`, `REGIONAL_SOCIALIST`).
- **4 Reaction Stances**: `SUPPORT_GOVT`, `AGITATE`, `OPPOSE`, `NEUTRAL`.
- **Public Opinion Metrics**: Shifts global `supportForGovt` (+/-) and `morale` (+/-).
- **3 Legislative Bills**: Vote YES, NO, or ABSTAIN on major bills with ideology-based voting alignment and content impacts.

### 4. Alliance & Coalition Engine
- **Power ($P$)**: Calculated from current Lok Sabha seat total.
- **Content ($C$)**: Scale $0 - 100$ representing internal party satisfaction.
- **Alliance Acceptance Threshold**: Proposer Power $\ge 2 \times$ Target Power for unaffiliated parties; $C < 35$ for poaching.
- **No-Confidence Vote**: Triggered when non-government coalition holds $\ge 272$ seats.

---

## Verification Plan

- Validation of `2001.json` seed data structure against MongoDB schema.
- Unit tests for alliance acceptance logic and seat allocation algorithms.
- Automated API tests for `/api/national/*` and `/api/admin/national-configs/*` endpoints.
- Integration tests for season advancement, event processing, and state data persistence.

