---
name: political-scenario-news
description: Generates monthly news-event JSON files for the Indian political simulation game (scenarioKey, period, newsItems with gov_action/opp_demands/joint_forum/no_comment reactions, effects, hiddenEffects, risk). Every news item must be a distinct, researched real (or era-plausible) event for that specific month — never a recurring template of ~12 issues repeated annually — and every reaction must read like how that state's actual parties/leaders would react to that event, not boilerplate. Use whenever the user asks to create, draft, expand, or fix a scenario's news file for the game — e.g. "create news for Andhra Pradesh 2001", "generate the Bihar 1990s scenario", "add news items to this state's timeline", "make reactions for this news event", or any state + time period + "scenario"/"gov_action"/"opp_demands" mention. Trigger even without the full JSON schema spelled out — research the real history and produce the file. Not for generic news-writing or unrelated JSON tasks.
---

# Political Scenario News Generator

Produces `newsItems` JSON files for the Indian political game — the same format as
`andhra_pradesh_2001_news.json`. Each file covers one state/scenario over a period of
months. Every month has one news event; every event has exactly four reaction options
(`gov_action`, `opp_demands`, `joint_forum`, `no_comment`) with numeric effects, hidden
effects, and risk.

**This is a research + writing task, not a template-filling task.** Two hard rules,
non-negotiable regardless of how long the period is:

1. **No recurring issue cycle.** Do not pick ~12 representative issues and repeat them
   every year with only the year changed. Every single month gets its own distinct,
   separately-researched event. A 5-year scenario needs 60 *different* stories, not 12
   stories told 5 times. If you catch yourself reusing a title/description structure
   from an earlier month, stop and research that month again.
2. **No boilerplate reactions.** Never write a reaction as a generic sentence with the
   issue name swapped in (e.g. "Initiate a special government commission to resolve
   {issue} issues immediately" reused across items). Each reaction must be a specific
   action that reflects how the real parties/leaders in power at that place and time
   would actually respond to *that* event — see Step 3.

## Step 0 — Confirm scope

Get from the user (ask only what's missing — don't block on things you can infer):

1. **State/region + scenario theme** → becomes `scenarioKey` (snake_case, e.g.
   `andhra_pradesh_2001`, `bihar_lalu_era`, `punjab_insurgency_1984`).
2. **Time period** → `startMonth`/`endMonth` (`YYYY-MM`), which gives `months` count.
3. Whether `reviewStatus` should be `"draft"` or `"approved"` (default `"draft"` —
   don't mark your own output approved).

Don't ask more than this; proceed with sensible defaults and state your assumptions.

## Step 1 — Research the political landscape first

Before touching individual months, establish the real political map for the whole
period:
- Which party/coalition held state government, and who was Chief Minister — note
  every change of government inside the period (elections, defections, presidents-
  rule spells) with the month it happened.
- Who the main opposition party/parties were, and their key leaders, in each stretch
  of the period.
- Any third-force/regional parties relevant to the state (e.g. a statehood movement
  party, a Left front, a caste-based party) that would plausibly take the
  `THIRD_PARTY` role.

Put a short version of this in `sourceNotes` (e.g. "Government: TDP/N. Chandrababu
Naidu through 2004-05, then INC/Y.S. Rajasekhara Reddy from 2004-05 onward.
Opposition: INC until 2004, then TDP. Third force: TRS (Telangana statehood) from
2001."). You'll use this mapping constantly in Step 3 — reactions should match
*whoever actually held each role in that specific month*, which may change partway
through the scenario.

## Step 2 — Research each month's news

For every calendar month in range, find one real (or, where the record is thin,
clearly era-plausible) event specific to that month — spread across these domains as
the real history warrants, not evenly forced: politics/party moves, farmer/rural
distress, protests & land disputes, security/insurgency incidents, infrastructure &
industrial projects, corruption/financial scandals, identity/religious/cultural
events, economic policy, and statehood/separatist movements where relevant.

Practical approach:
- Search year by year or quarter by quarter (`web_search "<state> <year> politics"`,
  `"<state> <year> farmer protest"`, `"<state> <year> naxal attack"`, etc.) — don't
  try to cover 60 months in one or two queries.
- Build a running list of candidate events with approximate dates *before* assigning
  them to months, so you can check you're not accidentally reusing the same
  underlying event for two different months.
- Use real figures and place names where the record supports it (as in KCR/TRS
  formation, YSR's padayatra, a specific dam/project name). Never fabricate a specific
  real named person doing something they didn't do. Where the real record for a given
  month is genuinely thin, write a plausible, era-consistent filler event, but make it
  a new distinct event for that month — not a rerun of a previous month's story with
  the date changed.
- Keep a mental/scratch list of titles used so far and actively check new ones against
  it for repetition before finalizing.

## Step 3 — Write the news items

For every month in range, produce one `newsItems` entry. Read
`references/json_schema.md` for the exact field-by-field structure before writing —
follow it exactly (key names, nesting, `null` vs `{}` are meaningful).

Key points:
- `newsKey`: `{scenarioKey}_{yyyy}_{mm}_{issue_slug}` — `issue_slug` is a short
  snake_case tag for *this specific event* (e.g. `nagarjuna_sagar_gate_collapse`, not
  a reused generic tag like `irrigation_protests` copy-pasted every year).
- `title`: punchy, dated headline style naming the specific event, + `(YYYY-MM)`
  suffix. Two different months should never produce near-identical titles.
- `description`: 2 sentences — what happened + why it matters to the state's
  politics right then. Don't editorialize about which reaction is "correct."
- `issueTags`: 1-2 tags from a controlled vocabulary (see schema doc) — reuse *tags*
  across items (that's fine, tags are meant to be a small shared vocabulary), but the
  underlying event, title, and description must still be unique per item.
- `weights.baseSelectionWeight`: ~1.0-1.3 for normal items; push toward 1.25+ for
  higher-salience/crisis items, toward 1.15 for routine/ceremonial ones.
- `weights.reactionProfile`: a short label grouping similar issues (e.g.
  `governance`, `land_rights`, `politics`, `security_crisis`) — reuse across items.
- `type`: `"external"` for ordinary news beats; use `"crisis"` (with a non-null
  `crisisTriggerKey` and `crisisDuration` > 2) only for events meant to persist as a
  multi-month crisis state in the game engine. Ask the user if unsure whether any
  events should be crises — otherwise default everything to `"external"`.

Before finalizing each batch, scan your own titles/descriptions so far for repeats —
same place name + same issue type appearing in more than one month is a signal you
recycled an event instead of researching a new one.

## Step 4 — Build the four reactions per item, in character

Every item gets exactly these four `reactionOptions`, in this order:

| reactionKey suffix | roleAllowed | Stance |
|---|---|---|
| `__gov_action_{slug}` | `["GOVERNMENT"]` | The sitting government's response — direct, uses state machinery. |
| `__opp_demands_{slug}` | `["OPPOSITION","THIRD_PARTY"]` | Pressure/criticism from outside government. |
| `__joint_forum_{slug}` | `["GOVERNMENT","OPPOSITION","THIRD_PARTY"]` | Consensus-seeking, cross-party option. |
| `__no_comment_{slug}` | `["GOVERNMENT","OPPOSITION","THIRD_PARTY"]` | Disengagement/silence — always available, always the worst-performing option. |

**Write these like a political reporter describing what each real party would
actually do**, not like a form letter with the noun swapped. Before writing a
reaction, ask yourself: given who's actually in power this month (from your Step 1
mapping) and their real ideology/track record, and given what this specific event is,
what would they *plausibly, specifically* do?

- Pull from the real party's known style/priorities for the era — a pro-business
  government's `gov_action` on an industrial land dispute looks different from a
  populist government's; a Left-leaning opposition's `opp_demands` on a labor issue
  looks different from a regional party's on a statehood issue. Make that visible in
  the wording.
- Reference the real party by name where it's factually the governing/opposition
  party that month (e.g. "the TDP government announces...", "TRS legislators walk
  out..."), since that's just describing the organization's real action. But don't
  invent a direct quote and attribute it as something a specific named real
  politician said — describe the action/position, not a fabricated verbatim quote.
  Generic/composite spokesperson lines ("a state minister said...") are fine.
  Fictional characters can be quoted freely if you introduce one instead of naming a
  real person.
- Vary the *shape* of the action across items, not just the wording — a commission,
  a subsidy, an ordinance, a press conference, a legislative walkout, a fact-finding
  visit, a court petition, a public rally, a backroom deal, a media campaign are all
  different tools; don't reach for "form a commission" or "hold a round table" every
  time. Match the tool to the era and the event (e.g. no TV debates before India had
  24-hour news channels; ordinances and assembly walkouts are period-appropriate
  throughout).
- `no_comment`'s flavor should still be specific to the event even though it's always
  the weak option — "the CM's office declines to comment on the mine collapse" reads
  differently per event even though the mechanics are the same.

**Red flag check before finalizing each reaction:** if you could paste the same
sentence into a different news item by only changing the issue noun, rewrite it —
that's the boilerplate pattern to avoid.

Read `references/effects_calibration.md` before assigning numbers — it has the
severity tiers, sign conventions, and hidden-effect/risk conventions used across the
whole file. In short:
- All four `playerParty` effect fields (`partyMorale`, `corruptionScore`,
  `mediaImage`, `publicSupport`) are integers in **-10..10**.
- `no_comment` is always net-negative on morale/media/support.
- `gov_action` and `opp_demands` are net-positive for the role that's allowed to pick
  them, `joint_forum` is moderate-positive for everyone with a small corruption
  discount.
- Every reaction except `no_comment` normally carries a `risk` block (chance 5-20,
  a `badOutcome` string, and a smaller negative `effects` block that fires on that
  chance). `no_comment` usually has `risk: {}`.
- `hiddenEffects.publicMemory` accumulates long-run sentiment under scenario-specific
  keys (e.g. `apStabilityMemory`, `corruptionMemory`, `ruralTrustMemory`) — reuse the
  same key across an issue category so memory compounds meaningfully over the scenario.

## Step 5 — Assemble and validate

Wrap everything in the top-level object from `references/json_schema.md`
(`reviewStatus`, `scenarioKey`, `period`, `sourceNotes`, `defaults`, `newsItems`).

Then run the validator before handing back the file:

```bash
python3 /path/to/scripts/validate_scenario.py <output_file.json>
```

Fix everything it flags (missing keys, out-of-range effects, bad month formats,
duplicate keys, wrong `roleAllowed`, repeated titles/descriptions, boilerplate
reaction phrasing) before presenting the file to the user. If the file is large
(many months), write it incrementally in chunks of ~6-12 months at a time and
re-validate after each chunk rather than holding the whole thing in your head — the
validator's repetition warnings are most useful when checked chunk by chunk instead
of only at the very end.

## Step 6 — Deliver

Save the finished file to `/mnt/user-data/outputs/<scenarioKey>_news.json` and present
it. Briefly summarize (in chat, not in the file) which real events you drew on and any
months where you had to write plausible filler instead of grounded history.
