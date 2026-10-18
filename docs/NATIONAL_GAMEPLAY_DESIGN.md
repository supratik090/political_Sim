# 🏛️ STATECRAFT: National Politics Mode
## Complete Game Design Document — v2.0

---

## 1. Game Concept

National Politics Mode is a long-form political strategy game where the player leads an Indian political party through multiple eras of national politics (2001–2025), building coalitions, contesting Lok Sabha seats across 30 states, calling confidence votes, and ultimately claiming the Prime Ministership.

Unlike the State Mode (a focused 60-turn card game in one state), the National Mode is a **meta-strategy layer** — the player orchestrates their party's national presence across all states simultaneously, dipping into individual state campaigns season by season.

### Core Rules
- **One National game at a time.** A player can have only one active national game. To start fresh (new era, new party), they must quit the current game. State Mode saves are unaffected.
- **All eras are freely accessible.** No era is locked. Player can start from 2001, 2010, or 2025.
- **YDP is a real national force.** The Youth Development Party (fictional player party) holds ~10% vote share in every state from the start, giving them ~54 Lok Sabha seats nationally — a credible independent bloc.
- **Every 12 turns triggers a State of the Union.** An animated national recap showing every state's numbers building up.
- **Elections are live, animated broadcasts.** State by state, seats are revealed and the national tally builds.
- **5 real historical events per era.** Based on actual political events of that period — they flash on screen, shift party power and content scores visibly.

---

## 2. YDP National Seat Calculation

YDP (Youth Development Party) is the fictional party the player can choose. It exists in every state as the Third Party with 10% vote share.

### 2001 Era — YDP Starting Seats (10% vote share per state)

The seat allocation uses simple proportional representation per state:
`YDP seats in state = round(totalSeats × 0.10)`

| State | Total Seats | YDP Seats (10%) |
|---|---|---|
| Uttar Pradesh | 80 | 8 |
| Maharashtra | 48 | 5 |
| West Bengal | 42 | 4 |
| Bihar | 40 | 4 |
| Tamil Nadu | 39 | 4 |
| Andhra Pradesh | 42 | 4 |
| Madhya Pradesh | 29 | 3 |
| Karnataka | 28 | 3 |
| Rajasthan | 25 | 3 |
| Gujarat | 26 | 3 |
| Odisha | 21 | 2 |
| Kerala | 20 | 2 |
| Jharkhand | 14 | 1 |
| Assam | 14 | 1 |
| Punjab | 13 | 1 |
| Chhattisgarh | 11 | 1 |
| Haryana | 10 | 1 |
| Delhi | 7 | 1 |
| Jammu & Kashmir | 6 | 1 |
| Uttarakhand | 5 | 1 |
| Himachal Pradesh | 4 | 0 |
| Goa | 2 | 0 |
| All remaining UTs/small states | ~17 | 1 |
| **TOTAL** | **543** | **~54 seats** |

**YDP starts with ~54 Lok Sabha seats** — more than INC's historical 51 in 2001. This makes YDP the 4th largest party by seats, sitting in the INDEPENDENT bloc. A strong starting position for an ambitious challenger.

### YDP Starting Position Summary
- **54 seats** across all states
- **Power: 54** (seat-based)
- **Content: 80** (fresh party, enthusiastic)
- **Alliance: INDEPENDENT** (unaffiliated)
- **Status:** Can be approached by NDA or INC immediately (their power ≫ 2×54)
- **Player strategic choice:** Join a coalition early for safety, or stay independent and grow

---

## 3. Screen Flow: From Login to Gameplay

### 3.1 Mode Selection Screen

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   👋 Welcome back, [Player Name]                            │
│                                                             │
│   ┌─────────────────────────┐  ┌─────────────────────────┐ │
│   │     🗺️ STATE MODE        │  │   🏛️ NATIONAL MODE       │ │
│   │                         │  │                         │ │
│   │  Command a single       │  │  Lead your party to     │ │
│   │  state campaign.        │  │  national majority.     │ │
│   │                         │  │                         │ │
│   │  • Card-based turns     │  │  • Coalition politics   │ │
│   │  • 60 turns / 5 years   │  │  • 10 seasons / era     │ │
│   │  • One state at a time  │  │  • Multi-era (25 years) │ │
│   │  • Deep tactical        │  │  • Real history events  │ │
│   │                         │  │                         │ │
│   │  [Continue] [New Game]  │  │  [Continue] [New Game]  │ │
│   └─────────────────────────┘  └─────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**National Mode [New Game]** — if player has an existing national save, show a warning:
```
⚠️  You already have an active national game (BJP, Era 2001, Season 4).
    Starting a new game will permanently erase it.
    [Cancel]   [Erase & Start New Game]
```

---

### 3.2 National Mode New Game — Screen 1: Choose Era

All eras are freely accessible. No era is locked.

```
┌─────────────────────────────────────────────────────────────┐
│  🏛️ NATIONAL POLITICS — Choose Your Starting Era            │
│                                                             │
│  Each era represents a different political landscape.       │
│  Your coalitions and achievements carry forward between     │
│  eras if you play them sequentially.                        │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  2001   "The NDA Experiment"                         │   │
│  │  NDA minority govt, coalition politics begin.        │   │
│  │  Recommended starting era.               [Select ▶]  │   │
│  ├──────────────────────────────────────────────────────┤   │
│  │  2005   "UPA Rises"                                  │   │
│  │  INC forms UPA, NDA in opposition. Left is kingmaker.│   │
│  │                                          [Select ▶]  │   │
│  ├──────────────────────────────────────────────────────┤   │
│  │  2010   "The Scam Years"                             │   │
│  │  Coalition strains, corruption controversies.        │   │
│  │                                          [Select ▶]  │   │
│  ├──────────────────────────────────────────────────────┤   │
│  │  2015   "The Modi Wave"                              │   │
│  │  BJP wins outright majority. Opposition fragmented.  │   │
│  │                                          [Select ▶]  │   │
│  ├──────────────────────────────────────────────────────┤   │
│  │  2020   "Pandemic Politics"                          │   │
│  │  Economic strain, regional parties surge.            │   │
│  │                                          [Select ▶]  │   │
│  ├──────────────────────────────────────────────────────┤   │
│  │  2025   "The Fractured Mandate"                      │   │
│  │  NDA returns, weakened. Opposition I.N.D.I.A. grows. │   │
│  │                                          [Select ▶]  │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

### 3.3 New Game — Screen 2: Choose Your Party

```
┌─────────────────────────────────────────────────────────────┐
│  🏛️ ERA 2001 — Choose Your Party                            │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  [All ▾]  [Sort by Seats ▾]  🔍 Search               │  │
│  ├───────────────────────────────────────────────────────┤  │
│  │                                                       │  │
│  │  ● YDP   Youth Development Party    54 seats  IND    │  │
│  │    🌟 RECOMMENDED FOR NEW PLAYERS                     │  │
│  │    Present in all states. Independent. Pure upstart. │  │
│  │                                                       │  │
│  │  ○ BJP   Bharatiya Janata Party    182 seats  NDA    │  │
│  │    Ruling coalition. Inherit NDA but 35 seats short. │  │
│  │                                                       │  │
│  │  ○ INC   Indian National Congress   51 seats  INC    │  │
│  │    Main opposition. Must rebuild from weak base.     │  │
│  │                                                       │  │
│  │  ○ CPM   Communist Party of India  33 seats  LEFT    │  │
│  │    Left Front leader. Strong in Bengal, Kerala.      │  │
│  │                                                       │  │
│  │  ○ SP    Samajwadi Party            26 seats  IND    │  │
│  │    UP stronghold. Unaffiliated. Kingmaker potential. │  │
│  │                                                       │  │
│  │  ○ BSP   Bahujan Samaj Party        21 seats  IND    │  │
│  │    UP powerbase. Niche but strong. Hard mode.        │  │
│  │                                                       │  │
│  │  ○ RJD   Rashtriya Janata Dal       26 seats  IND    │  │
│  │    Bihar dominance. Lalu factor. High risk/reward.   │  │
│  │                                                       │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
│  Selected: YDP — "The Challenger"                           │
│  Difficulty: ★★★☆☆ Medium                                  │
│                                                             │
│  [Back]                              [Confirm & Continue ▶] │
└─────────────────────────────────────────────────────────────┘
```

**Difficulty ratings:**
- YDP — ★★★☆☆ Medium (strong start, must build identity)
- BJP — ★★☆☆☆ Easy (already in coalition, familiar machinery)
- INC — ★★★★☆ Hard (weak base, must rebuild)
- CPM — ★★★★☆ Hard (regional ceiling, hard to expand)
- SP/BSP/RJD — ★★★★★ Expert (single-state base, must punch far above weight)

---

### 3.4 New Game — Screen 3: Your Starting Position

```
┌─────────────────────────────────────────────────────────────┐
│  🏛️ YOUR STARTING POSITION — YDP, Era 2001                  │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  YOUR PARTY                                         │   │
│  │  Youth Development Party (YDP)                      │   │
│  │  54 Lok Sabha seats  Power: 54  Content: 80         │   │
│  │  Alliance: INDEPENDENT   Status: UNAFFILIATED        │   │
│  │  Active in: All 28 states (as Third Party)           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  NATIONAL LANDSCAPE                                 │   │
│  │                                                     │   │
│  │  NDA   ████████████ 237    (Minority Govt)          │   │
│  │  INC   ███ 51                                       │   │
│  │  LEFT  ███ 53                                       │   │
│  │  IND   ████████ 202  (includes YDP: 54)             │   │
│  │                                                     │   │
│  │  ── 272 majority line ──────────────────            │   │
│  │                                                     │   │
│  │  Majority: 272 seats needed                         │   │
│  │  You need 218 more seats or alliance partners       │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  PARTIES THAT CAN APPROACH YOU (their power ≥ 2×54)│   │
│  │  BJP (182) can propose alliance to you              │   │
│  │  You may accept or refuse                           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  YOUR OBJECTIVE: Reach and hold 272+ seats                  │
│  YOUR IMMEDIATE SITUATION: You are a free agent.            │
│  Bigger parties will try to recruit you. Choose wisely.     │
│                                                             │
│  [Back]                         [Begin — Season 1, 2001 ▶]  │
└─────────────────────────────────────────────────────────────┘
```

---

## 4. The National Dashboard (Central Hub)

### 4.1 Main Layout

```
┌─────────────────────────────────────────────────────────────┐
│  🏛️ NATIONAL PARLIAMENT    Era: 2001  Season: 3/10  Jan 2002│
├──────────────────────────────┬──────────────────────────────┤
│                              │  📊 SEAT TALLY               │
│                              │  Total: 543  Majority: 272   │
│    INDIA MAP                 │                              │
│    (States colored           │  NDA  ████████████ 237       │
│     by controlling           │  INC  ████ 62               │
│     alliance)                │  LEFT ███ 53                 │
│                              │  YDP  ███ 54 ← (YOU)         │
│    🟠 NDA                    │  IND  █████ 137              │
│    🔵 INC/UPA                │                              │
│    🔴 LEFT                   │  ── 272 majority line ──     │
│    🟡 YDP (your colour)      │                              │
│    ⬜ INDEPENDENT            │  Govt: NDA (minority) -35    │
│                              ├──────────────────────────────┤
│    [Click state for info]    │  ⚡ YOUR ACTIONS              │
│                              │  [Propose Alliance]          │
│                              │  [Respond to Proposals]  🔴1 │
│                              │  [Call No-Confidence] 🔒     │
│                              │  [View Alliance Details]     │
│                              │                              │
│                              │  [▶ Begin Season 4]          │
└──────────────────────────────┴──────────────────────────────┘
```

**Incoming proposal badge:** The "🔴1" on Respond to Proposals means BJP has sent YDP an alliance proposal this season. Player must respond before starting Season 4.

---

## 5. Real Historical Events & Legislative Bills System

### 5.1 Concept & The 5 Core Ideologies

In National Mode, history is alive. Every season features **5 real historical events** spanning 5 key categories:
1. 🇮🇳 **Indian Political** (Cabinet decisions, election results, party splits, border security)
2. 💼 **Finance & Economy** (Budgets, tax reforms, stock crashes, disinvestment)
3. 🌪️ **National Disaster & Crisis** (Earthquakes, cyclones, drought, pandemic, terror attacks)
4. 🚨 **Corruption & Controversies** (CAG reports, scams, investigative exposures, hawala)
5. 🏆 **National Achievement & Milestones** (Space launches, infrastructure completions, nuclear tests, sports wins)

With 10 seasons per era, each era contains **50 real historical events**!

#### The 5 Core Ideologies
Events do not target hardcoded party names directly. Instead, all events apply baseline impacts across the **5 Core Ideologies**:
1. `DEVELOPMENTAL_PROGRESSIVE` (YDP - Youth Development Party)
2. `NATIONALIST_CONSERVATIVE` (BJP, Shiv Sena, Akali Dal)
3. `CENTRIST_SECULAR` (INC, NCP)
4. `LEFT_SOCIALIST` (CPIM, CPI)
5. `REGIONAL_SOCIALIST` (SP, BSP, RJD, DMK, AIADMK, BJD, TDP, etc.)

---

### 5.2 Event Dynamics & 4 Reaction Choices

Each event specifies `baselineIdeologyEffects` that shift `content` and `power` for all parties belonging to that ideology.

When an event fires, the player MUST select one of **4 public reaction stances**:

| Reaction Stance | Description | Typical Impact |
|---|---|---|
| **1. Support Govt** | Stand with the ruling administration | Boosts `supportForGovt` & `morale`; strengthens ties with ruling alliance |
| **2. Agitate** | Mobilize street protests & public demonstrations | Boosts party enthusiasm (+Content); shifts `supportForGovt` downward |
| **3. Oppose** | Parliamentary opposition & media counter-blitz | Aligns with Opposition bloc; reduces `supportForGovt` |
| **4. Neutral** | Abstain or issue a measured non-committal statement | Zero risk, minimal reward; preserves existing status quo |

#### Public Opinion Metrics
Events and reaction choices adjust 2 core global metrics:
- **`supportForGovt`**: National percentage support shift for the ruling coalition (+/-).
- **`morale`**: Overall national optimism and public confidence (+/-).

---

### 5.3 Legislative Bills Voting System

In addition to seasonal events, **3 major Legislative Bills** are presented to Parliament during each 5-year era (e.g. 2001 Era: *Prevention of Terrorism Act (POTA)*, *Fiscal Responsibility and Budget Management (FRBM) Act*, *Right to Information (RTI) Act*).

```
┌─────────────────────────────────────────────────────────────┐
│  📜 PARLIAMENTARY VOTE — POTA BILL, 2002                    │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   │
│                                                             │
│  Bill Title: Prevention of Terrorism Act (POTA)             │
│  Category: Security & Law Enforcement                       │
│  Description: Special anti-terror law expanding detention.  │
│                                                             │
│  IDEOLOGY VOTING STANCES:                                   │
│  NATIONALIST_CONSERVATIVE: YES   CENTRIST_SECULAR: NO      │
│  LEFT_SOCIALIST: NO              REGIONAL_SOCIALIST: NO     │
│  DEVELOPMENTAL_PROGRESSIVE: NEUTRAL                         │
│                                                             │
│  HOW DOES YOUR PARTY VOTE?                                  │
│  [Vote YES (Support Govt)]     [Vote NO (Oppose Bill)]      │
│  [ABSTAIN]                                                  │
│                                                             │
│  IMPACT (based on ideology alignment):                      │
│  • Vote YES → Conservative Content +8, Secular Content -10  │
│  • Vote NO  → Secular Content +8, Conservative Content -10  │
│  • Public Opinion Shift: supportForGovt +8, morale +4       │
└─────────────────────────────────────────────────────────────┘
```

---

### 5.4 State Seat Allocation & Support Percentages

In `stateSeatData`, seats for each party in every state are dynamically allocated based on `supportPercentages`:
- Each state defines `rulingPartyKey`, `oppositionPartyKey`, and `supportPercentages` for active parties.
- `initialSeats` are derived proportionally from support percentages (totaling 543 Lok Sabha seats nationwide).
- Parties like `inc` specify `activeStates` explicitly (e.g., in West Bengal, active parties are `cpim`, `aitc`, `bjp`, and `ydp`).

---

### 5.4 2001 Era Events Breakdown (5 Events per Season × 10 Seasons = 50 Events)

#### Season 1 (Jan - Jun 2001)
1. 🌪️ **Gujarat Earthquake (Kutch)** — Disaster recovery crisis.
2. 💼 **Stock Market Crash & Ketan Parekh Scam** — Financial regulatory scandal.
3. 🚨 **Tehelka Defense Sting Operation** — Corruption exposure in defense procurement.
4. 🇮🇳 **Agra Summit (Vajpayee-Musharraf)** — High-stakes bilateral peace summit.
5. 🏆 **GSAT-1 Satellite Launch** — ISRO space technology breakthrough.

#### Season 2 (Jul - Dec 2001)
1. 🇮🇳 **Parliament House Terrorist Attack (Dec 13)** — National security crisis.
2. 💼 **UTI US-64 Mutual Fund Collapse** — Financial crisis affecting middle-class investors.
3. 🚨 **Enron Dabhol Power Plant Crisis** — Infrastructure & foreign investment dispute in Maharashtra.
4. 🌪️ **Orissa Severe Floods** — Agricultural crisis in Eastern India.
5. 🏆 **Golden Quadrilateral Highway Project Milestone** — Major national infrastructure expansion.

*(Subsequent seasons 3 to 10 follow the same 5-event structure covering 50 total historical moments across 2001–2005.)*
---

## 6. Season Flow — Detailed

### 6.1 Season Start Screen

```
┌─────────────────────────────────────────────────────────────┐
│  📅 SEASON 4 BEGINS — July 2002 to December 2002            │
├─────────────────────────────────────────────────────────────┤
│  SEASON 3 RECAP                                             │
│  📰 Gujarat Riots fired — YDP content rose to 85            │
│  ✅ Uttar Pradesh: YDP gained 2 seats  (You played)         │
│  ↻  Maharashtra: Skipped (AI) — YDP held 5 seats           │
│  ❌ Bihar: Skipped (AI) — YDP lost 1 seat                   │
│                                                             │
│  ALLIANCE EVENTS:                                           │
│  BJP has sent YDP an alliance proposal! [Respond ▶]         │
│  SP is now RESTLESS (Content: 38) — ripe for poaching       │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  THIS SEASON'S PRIORITY STATES                              │
│  🔴 Bihar       — YDP losing ground. AI cost you a seat    │
│  🟡 Rajasthan   — YDP competitive. AI at 50% efficiency     │
│  🟢 UP          — YDP strong. Safe to skip this season     │
│  🔵 Maharashtra  — Neutral. Could gain if played            │
│                                                             │
│  [Respond to BJP Proposal First]    [Begin State Selection] │
└─────────────────────────────────────────────────────────────┘
```

### 6.2 State Selection — Play or Skip

```
┌─────────────────────────────────────────────────────────────┐
│  STATE 1 OF 5 ACTIVE: BIHAR  (Season 4)                    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  SITUATION                                          │   │
│  │  YDP holds 4 Bihar seats. State campaign: Turn 18  │   │
│  │  AI played last season: YDP lost 1 seat (-1)        │   │
│  │  Current vote share: YDP 10%, BJP 30%, RJD 38%     │   │
│  │                                                     │   │
│  │  IF YOU PLAY (6 turns):                            │   │
│  │  • Full card gameplay resumes from Turn 18         │   │
│  │  • Seat outcome based on your decisions            │   │
│  │  • YDP Content +5 (party sees you showing up)      │   │
│  │                                                     │   │
│  │  IF YOU SKIP:                                      │   │
│  │  • AI runs at 50% effectiveness                    │   │
│  │  • Likely: YDP holds or loses 1 more seat          │   │
│  │  • YDP Content -8 (neglected)                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  [⏭️ Skip Bihar]              [🎮 Play Bihar — 6 turns]     │
│                                                             │
│  States remaining: 4 more after Bihar                       │
└─────────────────────────────────────────────────────────────┘
```

### 6.3 Season Checkpoint (after 6 turns in a state)

```
┌─────────────────────────────────────────────────────────────┐
│  ⏸️  SEASON 4 CHECKPOINT — Bihar Complete                    │
│                                                             │
│  You completed 6 turns in Bihar (now at Turn 24/60)        │
│                                                             │
│  RESULTS:                                                   │
│  • YDP Bihar seats: 4 → 5  (+1) 🟢                         │
│  • YDP public support in Bihar: +11                         │
│  • RJD took a hit — their content dropped                   │
│                                                             │
│  Bihar campaign saved. Resumes Season 5 from Turn 24.       │
│                                                             │
│  [Next State: Rajasthan ▶]                                  │
└─────────────────────────────────────────────────────────────┘
```

---

## 7. State of the Union — Season End Animated Recap

After all states have been played or skipped each season, before the National Dashboard re-opens, a **State of the Union** screen appears. This is an animated, state-by-state reveal of the national picture.

### 7.1 Why This Screen Exists

- Creates a rhythm of anticipation every season
- Makes the national consequences of state play feel real and dramatic
- Even in seasons where the player only played 2 states, watching the AI-simulated states update is engaging
- Mirrors the feel of election night coverage — numbers building up

### 7.2 State of the Union — Screen Flow

**Phase 1: Title Card**
```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│         📺  STATE OF THE UNION                              │
│              Season 4 Review                                │
│           July – December 2002                              │
│                                                             │
│         Nationwide seat update incoming...                  │
│                                                             │
│              [▶ Begin Reveal]                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Phase 2: State-by-State Animated Reveal**

Each state appears one by one (or group of small states together). Map highlights the state. Numbers animate in.

```
┌─────────────────────────────────────────────────────────────┐
│  📺 STATE OF THE UNION — Season 4 Results                   │
├──────────────────────────────┬──────────────────────────────┤
│                              │  STATES DECLARED: 8 / 28    │
│    INDIA MAP                 │  ─────────────────────────   │
│    (current state            │                              │
│     highlights as            │  Running National Tally:     │
│     it reveals)              │  NDA  ██████████ 198         │
│                              │  INC  ████ 62                │
│  ← UTTAR PRADESH glows 🟡   │  LEFT ████ 53                │
│    "Declared"                │  YDP  ████ 56 (+2)  ← YOU   │
│                              │  IND  ███ 102                │
│                              │                              │
│                              │  ── 272 majority line ──    │
│                              │                              │
│                              │  ✅ UTTAR PRADESH (80 seats) │
│                              │  YDP  ██ 10  (+2) 🟢         │
│                              │  BJP  ████ 28  (-1)          │
│                              │  SP   ████ 22  (±0)          │
│                              │  BSP  ███ 20  (+1)           │
│                              │                              │
│                              │  [⏭️ Skip Remaining States]  │
└──────────────────────────────┴──────────────────────────────┘
```

States reveal in order of seat size (largest first: UP, Maharashtra, West Bengal...). For each state:
- The map highlights that state in an animated glow
- The right panel shows a mini seat breakdown for that state
- The national running tally animates to reflect the new numbers
- Player-played states show a ✅ marker and the actual result
- AI-simulated states show a 🤖 marker and the AI result

**Phase 3: Final Tally Card**

```
┌─────────────────────────────────────────────────────────────┐
│  📺 SEASON 4 — FINAL NATIONAL TALLY                         │
│                                                             │
│  NDA   ████████████████████████ 241  (was 237) +4           │
│  INC   █████████ 66             (was 62)  +4                │
│  LEFT  ███████ 53               (was 53)  ±0                │
│  YDP   ████████ 58  ← YOU       (was 54)  +4 🟢             │
│  IND   █████████ 125            (was 137) -12               │
│                                                             │
│  ── 272 majority line ──────────────────────────────────    │
│                                                             │
│  SEASON HIGHLIGHTS:                                         │
│  🌟 YDP gained 4 seats this season — best performance       │
│  📉 Independent bloc fragmented — parties seeking alliances │
│  ⚠️  NDA still 31 seats short of majority                  │
│                                                             │
│  BJP has renewed their alliance proposal to YDP.            │
│                                                             │
│  [Continue to National Dashboard ▶]                         │
└─────────────────────────────────────────────────────────────┘
```

---

## 8. Alliance Proposal Flow

### 8.1 Incoming Proposal (player receives one)

```
┌─────────────────────────────────────────────────────────────┐
│  📩 ALLIANCE PROPOSAL RECEIVED — FROM BJP (NDA)             │
│                                                             │
│  BJP SAYS:                                                  │
│  "The National Democratic Alliance invites the Youth        │
│   Development Party to join our coalition. Together,        │
│   we can provide a stable government for India."            │
│                                                             │
│  WHAT BJP OFFERS:                                           │
│  • 1 Cabinet Ministry (to be allocated)                    │
│  • Joint campaign support in 3 states of your choice       │
│  • Formal seat-sharing in upcoming state elections          │
│                                                             │
│  IF YOU JOIN NDA:                                           │
│  NDA coalition: 241 + 58 = 299 seats 🏆 MAJORITY           │
│  Your seats: 58 (unchanged, you retain identity)           │
│  You can still play all your states independently          │
│  You can leave if NDA content drops below 25               │
│                                                             │
│  YOUR POWER vs NDA LEADER:                                  │
│  BJP Power: 182   YDP Power: 58                             │
│  BJP has ≥ 2× your power ✅ — They are eligible to propose  │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  YOUR RESPONSE                                      │   │
│  │                                                     │   │
│  │  ○ Accept — Join NDA alliance                       │   │
│  │  ○ Decline — Remain independent for now            │   │
│  │  ○ Counter — Ask for 2 ministries instead          │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  [Confirm Response]                                         │
└─────────────────────────────────────────────────────────────┘
```

### 8.2 Outgoing Proposal (player sends one)

```
┌─────────────────────────────────────────────────────────────┐
│  🤝 PROPOSE ALLIANCE — SP (Samajwadi Party)                 │
├─────────────────────────────────────────────────────────────┤
│  TARGET ANALYSIS                                            │
│  SP  •  22 seats  •  Power: 22  •  Content: 38 (RESTLESS)  │
│  Status: Unaffiliated  •  Primary: UP, Uttarakhand          │
│                                                             │
│  ELIGIBILITY CHECK                                          │
│  Your Power (58) ≥ 2 × SP Power (44)  ✅                   │
│  SP is unaffiliated ✅                                       │
│  SP is RESTLESS ✅ — high acceptance probability            │
│  Estimated acceptance: 71%                                  │
│                                                             │
│  IF ACCEPTED:                                               │
│  YDP + SP = 58 + 22 = 80 seats                             │
│  You become a credible bloc — parties will notice           │
│                                                             │
│  IF REFUSED:                                                │
│  SP Content -5, Cooldown: 1 season                          │
│                                                             │
│  [Cancel]                        [Send Proposal ✉️]          │
└─────────────────────────────────────────────────────────────┘
```

### 8.3 Alliance Proposal Rules — Complete Logic

**Proposing to Unaffiliated Party:**
```
ACCEPT if:
  proposerPower >= 2 × targetPower
  AND targetContent < 80

REFUSE if:
  proposerPower < 2 × targetPower     (you're too small)
  OR targetContent >= 80               (they're loyal to independence)
```

**Poaching from Another Alliance:**
```
ACCEPT if:
  targetContent < 35                   (DISCONTENTED or DEFECTING)
  AND proposerPower >= 1.5 × targetPower
  AND target is NOT alliance leader

REFUSE if:
  targetContent >= 35
  OR target is alliance leader
```

**Counter-Proposal (Ministry Negotiation):**
```
Player or AI can counter a proposal by asking for 1 additional ministry.
The proposing party accepts the counter if:
  targetPower / proposerPower > 0.3   (target is significant)
  AND proposer coalition total < 300  (they need the seats badly)
```

---

## 9. No-Confidence Vote Flow

### 9.1 Trigger Conditions

**Player can call No-Confidence if:**
- Player coalition ≥ 272 seats (can independently win the vote)
- OR enough parties with Content < 40 exist to push govt below 272

**Government auto-falls if:**
- Ruling coalition drops below 272 between seasons (due to defections or AI seat shifts)
- System announces: "The government has lost its majority"

**Timing:** No-Confidence can only be called from the National Dashboard screen. Never mid-state.

### 9.2 Vote Calculation

```
For each non-player party:
  Content > 70          → Votes to SUPPORT current govt (stability first)
  Content 50-70         → Votes with their alliance
  Content 35-50         → Abstains (effectively reduces majority threshold)
  Content < 35          → Votes AGAINST current govt (rebellion)

If total AGAINST votes > total SUPPORT votes:
  → Government Falls
  → Leader of largest non-govt alliance invited to form government
```

---

## 10. Election Night Animation (Era Transition)

When Season 10 ends (60 months complete), an **Election Night Broadcast** screen opens.

```
┌─────────────────────────────────────────────────────────────┐
│  📺 LOK SABHA GENERAL ELECTION — ELECTION NIGHT BROADCAST   │
├──────────────────────────────┬──────────────────────────────┤
│                              │  NATIONAL TALLY              │
│    INDIA MAP                 │  Majority: 272               │
│    (states pulse gold        │                              │
│     as they report)          │  NDA   █████████████ 248     │
│                              │  INC   ███████ 92            │
│     Uttar Pradesh DECLARED   │  YDP   ██████ 82  (+24) 🏆   │
│    "YDP gains 6 seats!"      │  LEFT  ███ 38                │
│                              │  IND   ████ 83               │
│                              │                              │
│                              │  ── 272 majority line ──    │
│                              ├──────────────────────────────┤
│                              │  LATEST DECLARATION          │
│                              │  📍 Uttar Pradesh (80 seats) │
│                              │  YDP: 14 seats (+6)          │
│                              │  BJP: 24 seats (-5)          │
│                              │  SP:  22 seats (±0)          │
│                              │  INC: 10 seats (-1)          │
│                              │                              │
│                              │  [▶ Next State] [Fast-fwd ⏩]│
└──────────────────────────────┴──────────────────────────────┘
```

**After all states report:**
- Final seat count locked for the era
- If player's coalition ≥ 272 seats: **VICTORY SCREEN** — Player becomes Prime Minister
- Option to proceed to next era (e.g. 2005) carrying forward party reputation and coalition links
