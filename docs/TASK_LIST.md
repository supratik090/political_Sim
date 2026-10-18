# 🏛️ National Politics Mode — Master Task List

> Each task is self-contained. Complete and verify one before starting the next.
> Prompts are written so they can be handed directly to an AI coding agent.

---

## PHASE 1 — Foundation & Routing
*No new game logic. Wiring only. Fastest path to a visible skeleton.*

---

### TASK 1.1 — Lock Party Names in Create New Campaign

**Status:** `[X]` (Completed)

**What it does:**
In the existing "Create New Campaign" screen, party name text inputs are made read-only so party names are fixed to what the scenario defines.

---

### TASK 1.2 — Add NATIONAL Screen Key to App State

**Status:** `[X]` (Completed)

**What it does:**
Added `'NATIONAL'` as a valid screen key in `gameStore.js` and `App.jsx` routing.

---

### TASK 1.3 — Add National Mode Tab to Navigation

**Status:** `[X]` (Completed)

**What it does:**
Wiring up navigation routes in `DashboardLayout.jsx` and mobile navigation.

---

### TASK 1.4 — Mode Selection: Split Home into State / National Cards

**Status:** `[X]` (Completed)

**What it does:**
Home screen (`DashboardHome.jsx`) displays 2 large side-by-side mode selection hero cards for **State Mode** and **National Mode**.

---

## PHASE 2 — Seed Data: National Configs

---

### TASK 2.1 — Create National Seed Data Directory Structure

**Status:** `[X]` (Completed)

**What it does:**
Created `seed-data/national/national_configs/` directory structure for era JSON configuration files.

---

### TASK 2.2 — Seed 2001 Era: Alliances & Parties

**Status:** `[X]` (Completed)

**What it does:**
Populated `2001.json` with NDA, INC, LEFT, INDEPENDENT alliance structures and party data (including YDP, BJP, INC, CPM, SP, BSP, RJD).

---

### TASK 2.3 — Seed 2001 Era: State Seat Data (All 30 States)

**Status:** `[X]` (Completed)

**What it does:**
Added proportional seat allocations across all 30 states mapping to 543 Lok Sabha seats (YDP starting with ~54 seats).

---

### TASK 2.4 — Seed 2001 Era: 50 Historical Events & 3 Legislative Bills

**Status:** `[X]` (Completed)

**What it does:**
Populated `2001.json` with 10 seasons, each containing **5 real historical events** (50 total events across Indian Political, Finance, Disaster, Corruption, Achievement categories), each with:
- Baseline party power & content shifts (e.g. pro-govt vs anti-govt event dynamics)
- Global Mood of the Nation shift metrics (`nationalism`, `antiCorruption`, `proIncumbency`, `economicStrain`, `secularTrust`, `populism`)
- 4 reaction options per event (`SUPPORT_GOVT`, `AGITATE`, `OPPOSE`, `NEUTRAL`) with custom content/power/mood modifiers
- 3 Legislative Bills for the era (*POTA 2002*, *FRBM 2003*, *RTI 2005*) with YES/NO/ABSTAIN voting mechanics

---

### TASK 2.5 — Seed Remaining 5 Eras (2005–2025)

**Status:** `[ ]` (Pending)

Populate remaining era JSON configs (2005, 2010, 2015, 2020, 2025) with historical realignments.

---

## PHASE 3 — Backend: National Game API

### TASK 3.1 — NationalConfig Model & Repository
Spring Boot MongoDB documents (`NationalConfig`, `NationalAlliance`, `NationalParty`, etc.).

### TASK 3.2 — NationalGame Model & Repository
MongoDB save state documents (`NationalGame`, `NationalCoalition`, etc.).

### TASK 3.3 — National Config Seeder
Startup runner loading era JSON seed files into MongoDB.

### TASK 3.4 — National Game REST Controller
API endpoints for creating games, loading games, proposing alliances, and advancing seasons.

### TASK 3.5 — National Config Admin Endpoints
Admin CRUD endpoints for national game configurations.

---

## PHASE 4 — National Game UI: Core Screens

### TASK 4.1 — NationalGame Component Shell
React screen state machine (`NationalGame.jsx`).

### TASK 4.2 — Era Selection Screen
2001-2025 Era selector UI card grid.

### TASK 4.3 — Party Selection Screen
Selectable party list with starting seat totals and difficulty ratings.

### TASK 4.4 — National Dashboard Layout
Central hub displaying parliament seat tally, India map, and coalition status.

---

## PHASE 5 — Gameplay Mechanics & Seasons

### TASK 5.1 — Season Loop & State Priority List
Play vs Skip state selection for each season.

### TASK 5.2 — Historical Event News Flash Overlay
Breaking news animated flash overlay with choice mechanics.

### TASK 5.3 — Alliance Proposal & Negotiation Dialog
Interactive alliance offer/accept/decline flow.

### TASK 5.4 — State of the Union Animated Season Recap
Animated state-by-state seat count reveal broadcast.

### TASK 5.5 — No-Confidence Vote Mechanics
Confidence motion trigger and voting simulation.

---

## PHASE 6 — Polish & Era Transitions

### TASK 6.1 — Election Night Animated Broadcast
Era-end live election broadcast reveal.

### TASK 6.2 — Era Transition & State Persistence Logic
Carrying forward played states vs loading new era data for skipped states.

### TASK 6.3 — End-to-End Campaign Balancing
Tuning power, content decay, and alliance acceptance rates.
